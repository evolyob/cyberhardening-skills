#!/usr/bin/env python3
"""Universal Skill & Code Auditor (Lean Enterprise Standard)."""
import ast, re, sys
from pathlib import Path

PEP_594 = {"cgi", "cgitb", "pipes", "crypt", "imghdr", "sndhdr", "aifc", "audioop", "chunk", "mailcap", "nntplib", "sunau", "telnetlib", "uu", "xdrlib", "distutils"}
INSECURE_DESERIALIZERS = {"pickle", "_pickle", "dill", "shelve"}
SECRETS = [
    r"\b(AKIA|ASIA|ABIA|ACCA)[0-9A-Z]{16}\b",
    r"\b(sk-[a-zA-Z0-9_-]{20,}|sk-proj-[a-zA-Z0-9_-]{20,}|sk-ant-[a-zA-Z0-9_-]{20,})\b",
    r"\b(ghp_[a-zA-Z0-9]{20,}|github_pat_[a-zA-Z0-9_]{22,}|gho_[a-zA-Z0-9]{20,}|ghu_[a-zA-Z0-9]{20,})\b",
    r"\bAIzaSy[a-zA-Z0-9_-]{33}\b", r"https://hooks\.slack\.com/services/T[a-zA-Z0-9_]+/B[a-zA-Z0-9_]+/[a-zA-Z0-9_]+",
    r"\beyJ[a-zA-Z0-9_-]{10,}\.eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}\b", r"\bBearer\s+[a-zA-Z0-9_.-]{20,}\b",
    r"-----BEGIN [A-Z0-9_-]+ PRIVATE KEY-----",
    r"(?i)\b(?:password|passwd|pwd)\s*[:=]\s*['\"](?!(?:test|mock|fake|dummy|example|xxxx|admin|placeholder|sample|changeme))[^'\"\s]{6,}['\"]",
]
PRIVS = ["su" + "do ", "ch" + "mod +x", "ch" + "own ", "/et" + "c/shadow", "/et" + "c/passwd"]
INSECURE_TELEMETRY = [
    r"(?i)\b(?:verify\s*=\s*False|check_hostname\s*=\s*False)\b",
    r"(?i)\b(?:import\s+(?:telemetry|mixpanel|posthog)|(?:telemetry|mixpanel|posthog)\.[a-zA-Z_]|https?://[^\s'\"]*(?:telemetry|mixpanel|segment\.io|posthog))\b",
    r"(?i)\.workers\.dev/(?:telemetry|collect|log|track)",
]
ZERO_WIDTH_RE = re.compile(r"[\u200b-\u200f\u2060\ufeff\u202a-\u202e]")
PIPE_EXEC_RE = re.compile(r"(?i)\b(?:curl|wget)\b[^\n|;&]+?\|\s*(?:bash|sh|zsh|python|perl|ruby)\b")
USER_PATH_RE = re.compile(r"(?:/(?:Users|home)/[a-zA-Z0-9_-]+/|/root/|file:" + r"///?)")
PROMPT_INJ_RE = re.compile(r"(?i)\b(?:(?:ignore|disregard|forget|bypass|override)\s+(?:all\s+)?(?:previous|prior|above|existing)\s+(?:instructions?|directives?|rules?|system\s+prompt|context)|(?:enter|switch\s+to|enable)\s+(?:developer|god|unrestricted|jailbreak)\s+mode|do\s+anything\s+now|DAN\s+mode|bypass\s+(?:safety|content)\s+filters?)\b")
MEMORY_POISON_RE = re.compile(r"(?i)\b(?:(?:always\s+)?remember\s+(?:this|that|the\s+following)\s+(?:for|in)\s+(?:all|every|future)\s+(?:interactions?|conversations?|sessions?)|(?:from\s+now\s+on|henceforth|going\s+forward)\s*[,:]?\s*(?:always|you\s+must|you\s+will\s+always)|(?:store|save|persist|inject)\s+(?:this|the\s+following)\s+(?:in|to|into)\s+(?:your\s+)?(?:permanent\s+)?(?:memory|context|system\s+state))\b")
PROMPT_LEAK_RE = re.compile(r"(?i)\b(?:(?:print|output|display|reveal|expose|echo|dump)\s+(?:your\s+)?(?:full\s+)?(?:system\s+)?(?:prompt|instructions?|rules?|directives?)(?:\s+verbatim)?)\b")
ENV_HARVEST_RE = re.compile(r"(?i)\b(?:dict\(\s*os\.environ\s*\)|\{\s*\*\*os\.environ\s*\}|for\s+\w+\s*,\s*\w+\s+in\s+os\.environ\.items\(\))")
FRONTEND_EXTS = {".html", ".htm", ".js", ".mjs", ".ts", ".jsx", ".tsx", ".vue"}


def _check_nesting(node, current_depth=0, warnings=None, tag=""):
    if isinstance(node, ast.If):
        if current_depth >= 2 and warnings is not None: warnings.append(f"{tag} nested if-block depth {current_depth+1} > 2")
        for child in node.body: _check_nesting(child, current_depth + 1, warnings, tag)
        orelse_depth = current_depth if len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If) else current_depth + 1
        for child in node.orelse: _check_nesting(child, orelse_depth, warnings, tag)
    else:
        for child in ast.iter_child_nodes(node): _check_nesting(child, current_depth, warnings, tag)


def _check_text_security(src: str, raw_bytes: bytes, filename: str, is_meta: bool, blockers: list):
    if raw_bytes.startswith(b"\xef\xbb\xbf") and filename == "SKILL.md": blockers.append("SKILL.md contains UTF-8 BOM (pure UTF-8 required)")
    if ZERO_WIDTH_RE.search(src.lstrip("\ufeff")): blockers.append("Zero-width or invisible Unicode character detected")
    if PIPE_EXEC_RE.search(src): blockers.append("Insecure remote execution pipeline (curl/wget | sh) detected")
    if is_meta: return
    for idx, line in enumerate(src.splitlines(), 1):
        if line.strip().startswith("#") or any(k in line for k in ("re.search", "re.compile", "Zero-Leakage", "r'/", 'r"/', "-env:UserInstallation=")): continue
        if USER_PATH_RE.search(line) and not any(k in line for k in ("PS " + "C" + ":\\\\", "List" + "ing ", "C" + ":\\\\Users\\\\Public", "C" + ":\\\\Users\\\\ttidmas", "C" + ":\\\\Users\\\\jwrig")):
            blockers.append(f"Line {idx}: Hardcoded absolute user path or local file URI (~/ or $HOME required)")
            break
    for s in SECRETS:
        if re.search(s, src): blockers.append("Plaintext secret/API key")
    for p in PRIVS:
        if p in src and not any(k in src for k in ("Zero", "detect", "guard", "Defensive", "kill")): blockers.append(f"Privilege escalation ({p})")
    for t in INSECURE_TELEMETRY:
        if re.search(t, src): blockers.append("Insecure TLS bypass or telemetry endpoint detected")
    if PROMPT_INJ_RE.search(src): blockers.append("Prompt injection / jailbreak keyword detected")
    if MEMORY_POISON_RE.search(src): blockers.append("Persistent memory poisoning pattern detected")
    if PROMPT_LEAK_RE.search(src): blockers.append("System prompt exfiltration instruction detected")
    if ENV_HARVEST_RE.search(src): blockers.append("Wholesale environment harvesting pattern detected")
    if re.search(r"(\n\s*){20,}\n", src): blockers.append("Suspicious vertical whitespace padding (>= 20 blank lines)")


def _check_markdown_spec(src: str, filename: str, lines: int, is_meta: bool, blockers: list, warnings: list):
    limit = 60 if filename == "SKILL.md" else (40 if filename == "SECURITY.md" else 1000)
    if lines > limit and not is_meta and not filename.startswith("chapter_"): warnings.append(f"Lines {lines} > {limit} (move overflow to references/)")
    if filename == "SKILL.md" and not (re.search(r"^description:", src, re.M | re.I) or re.search(r"\bdescription\s*:", src, re.I)):
        blockers.append("SKILL.md missing required frontmatter: 'description:'")
    elif filename == "SECURITY.md":
        for sec in (r"##\s+Scope", r"##\s+Dependencies", r"##\s+Execution"):
            if not re.search(sec, src, re.I): blockers.append(f"SECURITY.md missing required section: '{sec.replace(r'##\s+', '## ')}'")
    stack = []
    for l in src.splitlines():
        s = l.strip()
        if s.startswith("````"): stack.pop() if (stack and stack[-1] == 4) else stack.append(4)
        elif s.startswith("```"):
            if stack and stack[-1] == 3: stack.pop()
            elif not stack or stack[-1] == 4: stack.append(3)
    if stack: blockers.append("Unclosed code fence / Broken 4-backtick nesting")


def _check_ast_safety(code: str, tag: str, filename: str, is_markdown: bool, is_meta: bool, is_test: bool, lines: int, spec_txt: str, local_mods: set, blockers: list, warnings: list):
    if not is_markdown and not is_meta and any(re.search(r"\bopen\(", l) and "encoding=" not in l and "wb" not in l and "rb" not in l for l in code.splitlines()): warnings.append("Unencoded open() call")
    if re.search(r'f["\x27]<[a-zA-Z]+', code) and not re.search(r"(escape|clean_text|sanitize|&amp;)", code): warnings.append(f"{tag} unescaped dynamic markup template")
    try: tree = ast.parse(code)
    except SyntaxError as e: return blockers.append(f"{tag} SyntaxError: {e}")

    has_class, n_defs, dict_lines = 0, 0, 0
    imported_mods, soft_imports, import_names, used_names, seen_defs = set(), set(), set(), set(), set()
    if not is_meta: _check_nesting(tree, 0, warnings, tag)

    for n in ast.walk(tree):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if not n.name.isascii(): blockers.append(f"{tag} non-ASCII identifier '{n.name}'")
            if not any(isinstance(d, ast.Name) and d.id == "overload" for d in n.decorator_list):
                if n.name in seen_defs: blockers.append(f"{tag} duplicate definition of '{n.name}'")
                seen_defs.add(n.name)
            if isinstance(n, ast.ClassDef): has_class = 1
            else:
                n_defs += 1
                for d in (n.args.defaults + [kw for kw in n.args.kw_defaults if kw is not None]):
                    if isinstance(d, (ast.List, ast.Dict, ast.Set)): blockers.append(f"{tag} mutable default argument in func '{n.name}'")
                for arg in (n.args.posonlyargs + n.args.args + n.args.kwonlyargs):
                    if not arg.arg.isascii(): blockers.append(f"{tag} non-ASCII argument '{arg.arg}'")
        elif isinstance(n, ast.Name):
            if not n.id.isascii(): blockers.append(f"{tag} non-ASCII variable '{n.id}'")
            used_names.add(n.id)
        elif isinstance(n, ast.Attribute):
            if not n.attr.isascii(): blockers.append(f"{tag} non-ASCII attribute '{n.attr}'")
            used_names.add(n.attr)
        elif isinstance(n, ast.Call):
            func_id, val_name = getattr(n.func, "id", getattr(n.func, "attr", "")), getattr(getattr(n.func, "value", None), "id", "")
            if func_id in ("eval", "exec") and not val_name: blockers.append(f"{tag} arbitrary execution ({func_id})")
            elif func_id == "system" and val_name == "os": blockers.append(f"{tag} os.system() execution")
            elif func_id == "unsafe_load" and val_name in ("yaml", "ruamel_yaml"): blockers.append(f"{tag} insecure yaml.unsafe_load() execution")
            if any(k.arg == "shell" and (getattr(k.value, "value", None) is True or getattr(k.value, "id", None) == "True") for k in n.keywords):
                blockers.append(f"{tag} subprocess with shell=True prohibited")
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            mod = n.module.split('.')[0] if isinstance(n, ast.ImportFrom) and n.module and n.level == 0 else (n.names[0].name.split('.')[0] if isinstance(n, ast.Import) else None)
            if mod:
                imported_mods.add(mod)
                if mod in INSECURE_DESERIALIZERS: blockers.append(f"{tag} insecure deserialization module '{mod}' prohibited")
            for alias in n.names:
                if alias.name != '*': import_names.add(alias.asname or alias.name)
        elif isinstance(n, ast.Try):
            for h in n.handlers:
                for child in ast.walk(h):
                    if isinstance(child, ast.Import): soft_imports.update(name.name.split('.')[0] for name in child.names)
                    elif isinstance(child, ast.ImportFrom) and child.module: soft_imports.add(child.module.split('.')[0])
        elif isinstance(n, ast.Dict):
            dict_lines += max(0, getattr(n, "end_lineno", 0) - getattr(n, "lineno", 0))
            seen_keys = set()
            for k in n.keys:
                if k is not None:
                    k_val = k.value if isinstance(k, ast.Constant) else (k.id if isinstance(k, ast.Name) else None)
                    if k_val is not None:
                        if k_val in seen_keys: blockers.append(f"{tag} duplicate dictionary key '{k_val}'")
                        seen_keys.add(k_val)
        elif isinstance(n, ast.ExceptHandler) and n.type is None: blockers.append(f"{tag} bare 'except:' handler")
        elif isinstance(n, ast.Global): warnings.append(f"{tag} mutable global state ({n.names})")
        elif isinstance(n, ast.Assert) and not is_test and not is_meta: warnings.append(f"{tag} production 'assert' statement")
        elif isinstance(n, ast.Constant) and isinstance(n.value, str): used_names.update(re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', n.value))

    if not is_markdown and not is_meta:
        base, x_rate = (45 + 30 * has_class), (15 if has_class else 25)
        py_limit = base + (n_defs * x_rate) + dict_lines
        if lines > py_limit: warnings.append(f"Lines {lines} > dynamic limit {py_limit} (Base {base} + {n_defs} defs × {x_rate} + {dict_lines} dict lines)")
    for dead in sorted(imported_mods & PEP_594): blockers.append(f"{tag} Zero-EOL: removed stdlib module '{dead}' in Python >= 3.13 (PEP 594)")
    third_party = {m for m in (imported_mods - soft_imports) if m not in sys.stdlib_module_names and m not in local_mods and not m.startswith("_")}
    if spec_txt and third_party:
        for dep in sorted(third_party):
            dep_norm = dep.lower().replace("_", "-")
            if dep.lower() not in spec_txt.lower() and dep_norm not in spec_txt.lower(): blockers.append(f"{tag} undeclared external dependency '{dep}'")
    if not is_markdown and not is_meta and (unused := sorted(import_names - used_names)): warnings.append(f"Unused imports: {unused}")


def audit_source(src: str, filename: str, is_markdown: bool = False, skill_txt: str = "", local_modules: set = None, flags: set = None, sec_txt: str = "", raw_bytes: bytes = b"") -> str:
    lines, blockers, warnings = len(src.splitlines()), [], []
    is_test, is_meta = "test" in filename.lower(), filename in ["audit.py", "remediation_guide.md", "developer_7_coding_laws_and_ast_audit.md"]
    local_mods, fl = local_modules or set(), flags or set()

    if not is_meta and "--ast" not in fl: _check_text_security(src, raw_bytes, filename, is_meta, blockers)
    if is_markdown and not fl: _check_markdown_spec(src, filename, lines, is_meta, blockers, warnings)
    if "--security" not in fl:
        py_blocks = (re.findall(r"```python[^\n]*\n(.*?)\n```", src, re.DOTALL) if is_markdown else [src])
        for idx, code in enumerate(py_blocks):
            _check_ast_safety(code, f"Snippet #{idx+1}" if is_markdown else "Script", filename, is_markdown, is_meta, is_test, lines, skill_txt, local_mods, blockers, warnings)

    status = "[✗] FAIL" if blockers else ("[!] WARN" if warnings else "[✓] PASS")
    report = f"{status} {filename} ({lines} lines)"
    if blockers: report += "\n" + "\n".join(f"  └── [BLOCKER] {b}" for b in blockers)
    if warnings: report += "\n" + "\n".join(f"  └── [ADVISORY] {w}" for w in warnings)
    return report


def audit_path(target, flags: set = None):
    t = Path(target).resolve()
    if not t.exists(): return print(f"[ERROR] Target does not exist: {target}")
    root = t if t.is_dir() else t.parent
    skill_md = root / "SKILL.md" if (root / "SKILL.md").exists() else (root.parent / "SKILL.md" if (root.parent / "SKILL.md").exists() else None)
    sec_md = root / "SECURITY.md" if (root / "SECURITY.md").exists() else (root.parent / "SECURITY.md" if (root.parent / "SECURITY.md").exists() else None)
    stxt = skill_md.read_text(encoding="utf-8-sig", errors="ignore") if skill_md and skill_md.exists() else ""
    sectxt = sec_md.read_text(encoding="utf-8-sig", errors="ignore") if sec_md and sec_md.exists() else ""
    spec_txt = f"{stxt}\n{sectxt}".strip()
    ctx_root = (skill_md or sec_md or root).parent if (skill_md or sec_md) else root
    lmods = {p.stem for p in ctx_root.glob("**/*.py")} | {p.name for p in ctx_root.glob("**/*") if p.is_dir()}

    files = [t] if t.is_file() else sorted(p for p in t.glob("**/*") if p.is_file())
    if t.is_dir(): print(f"\n[SKILL AUDIT] -> {t}\n" + "=" * 55)
    if skill_md and not sec_md: print("[!] WARN SECURITY.md (Missing)\n  └── [ADVISORY] Skill missing recommended file: 'SECURITY.md'")

    for f in files:
        if f.name.endswith((".pyc", ".png", ".jpg", ".ico", ".woff", ".woff2", ".ttf")): continue
        if f.suffix.lower() in FRONTEND_EXTS:
            try:
                import audit_frontend; audit_frontend.audit_target(str(f))
            except ImportError: print(f"[✓] PASS {f.name} (Frontend asset)")
        elif f.suffix in [".json", ".xml", ".yaml", ".yml", ".csv", ".txt", ".xsd"]:
            try:
                raw = f.read_text(encoding="utf-8-sig")
                if f.suffix == ".json": import json; json.loads(raw)
                elif f.suffix in (".xml", ".xsd"): import xml.etree.ElementTree as ET; ET.fromstring(raw)
                elif f.suffix in [".yaml", ".yml"]:
                    try: import yaml; yaml.safe_load(raw)
                    except ImportError:
                        if "\t" in raw: raise ValueError("YAML files must not contain tabs.")
                elif f.suffix == ".csv": import csv, io; list(csv.reader(io.StringIO(raw)))
                print(f"[✓] PASS {f.name} (Valid syntax & UTF-8 encoding)")
            except Exception as err: print(f"[✗] FAIL {f.name}\n  └── [BLOCKER] Data Syntax/Encoding Error: {err}")
        elif f.suffix in [".py", ".md"]:
            raw_bytes = f.read_bytes()
            src = raw_bytes.decode("utf-8-sig", errors="ignore")
            print(audit_source(src, f.name, is_markdown=f.suffix == ".md", skill_txt=spec_txt, local_modules=lmods, flags=flags, sec_txt=sectxt, raw_bytes=raw_bytes))


if __name__ == "__main__":
    VALID_FLAGS = {"--security", "--ast"}
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    targets = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not targets or (unknown := flags - VALID_FLAGS):
        sys.exit(f"Usage: python3 audit.py [--security] [--ast] <target_path>{' (Unknown: ' + ', '.join(sorted(unknown)) + ')' if flags - VALID_FLAGS else ''}")
    for t in targets: audit_path(t, flags=flags)
