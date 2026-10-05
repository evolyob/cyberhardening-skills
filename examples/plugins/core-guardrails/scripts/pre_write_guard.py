#!/usr/bin/env python3
"""
Pre-Write Guard (Unified PreToolUse Gating for write_to_file & replace_file_content).
Enforces:
  1. Directory Hygiene (Downloads/ script block)
  2. Plaintext Secrets & Hardcoded Local Paths (with Shannon entropy & false positive filter)
  3. Wholesale os.environ Harvesting
  4. Anti-AI Voice & Terminology Gate
"""

import sys
import json
import re
import math
from pathlib import Path

RULES_GATE_PATH = Path(__file__).resolve().parent / "rules_gate.json"
TARGET_ANTI_AI_EXTS = (".md", ".typ", ".tex", ".txt")


def calculate_shannon_entropy(text_val: str) -> float:
    if not text_val:
        return 0.0
    prob = [float(text_val.count(c)) / len(text_val) for c in set(text_val)]
    return -sum(p * math.log2(p) for p in prob)


def is_line_exempt(line: str) -> bool:
    s = line.strip().lower()
    return any(p in s for p in ("re.compile", "re.search", "re.match", "re.findall", "regex", "pattern"))


def is_false_positive_secret(sec_name: str, token: str, line: str, dummies: list[str]) -> bool:
    if any(ch in token for ch in ("[", "]", "{", "}", "\\", "*", "+", "?", "|")) or is_line_exempt(line):
        return True
    lower = token.lower()
    if any(d in lower for d in dummies) or lower.startswith(("sk-test-", "sk-fake-", "ghp_test", "ghp_mock")):
        return True

    # Entropy checks on token bodies
    if "AWS" in sec_name and (len(set(token[4:])) <= 4 or calculate_shannon_entropy(token[4:]) < 2.3):
        return True
    if "Google" in sec_name and (len(set(token[6:])) <= 5 or calculate_shannon_entropy(token[6:]) < 2.5):
        return True
    if "GitHub" in sec_name and (len(set(token.split("_")[-1])) <= 4 or calculate_shannon_entropy(token.split("_")[-1]) < 2.3):
        return True
    if "JWT" in sec_name and len(token.split(".")) == 3:
        sig = token.split(".")[2]
        if len(set(sig)) <= 3 or calculate_shannon_entropy(sig) < 2.0:
            return True
    if "Bearer" in sec_name:
        t = re.sub(r"^Bearer\s+", "", token, flags=re.IGNORECASE)
        if len(set(t)) <= 4 or calculate_shannon_entropy(t) < 2.3:
            return True
    return False


def check_security(content: str, rules: dict) -> str | None:
    if not content:
        return None

    path_re = re.compile(rules.get("path_pattern", r"(?:/(?:Users|home)/[a-zA-Z0-9_-]+/|/root/|(?<![a-zA-Z0-9])[a-zA-Z]:[\\/])"))
    secret_pats = [(s["name"], re.compile(s["regex"])) for s in rules.get("secret_patterns", [])]
    ingress_pats = [(i["name"], re.compile(i["regex"])) for i in rules.get("ingress_patterns", [])]
    dummies = rules.get("dummy_substrings", ["example", "dummy", "test", "mock", "fake"])

    for idx, line in enumerate(content.splitlines(), start=1):
        if not is_line_exempt(line):
            if path_re.search(line):
                return f"[SECURITY DENIAL] Line {idx} contains hardcoded local path or URI (~/ required)."
            for name, pat in ingress_pats:
                if pat.search(line):
                    return f"[SECURITY DENIAL] Line {idx} contains {name}! Harvesting prohibited."

        for sec_name, pat in secret_pats:
            for m in pat.finditer(line):
                if not is_false_positive_secret(sec_name, m.group(0), line, dummies):
                    return f"[SECURITY DENIAL] Line {idx} contains plaintext {sec_name}! Manage credentials via environment variables."
    return None


def check_anti_ai(target_path: Path, args: dict, rules: dict) -> str | None:
    fname = str(target_path).lower()
    if not fname.endswith(TARGET_ANTI_AI_EXTS) or re.search(r"(noai|detox|remediation|template|rule)", fname):
        return None

    text = args.get("CodeContent") or ""
    check_start, check_end = 1, None
    t_content, r_content = args.get("TargetContent"), args.get("ReplacementContent") or ""

    if not text and target_path.is_file() and t_content:
        orig = target_path.read_text(encoding="utf-8", errors="ignore")
        idx = orig.find(t_content)
        if idx != -1:
            check_start = orig[:idx].count("\n") + 1
            check_end = check_start + r_content.count("\n")
            text = orig[:idx] + r_content + orig[idx + len(t_content):]
    text = text or r_content

    tech_denies = [
        ((f"(?<!{re.escape(v[:v.index(k)])})" if v[:v.index(k)] else "") + re.escape(k) +
         (f"(?!{re.escape(v[v.index(k)+len(k):])})" if v[v.index(k)+len(k):] else ""))
        if k in v else re.escape(k)
        for k, v in rules.get("tech_terms_zh", {}).items()
    ]
    all_denies = [re.escape(w) for w in rules.get("hard_buzzwords_zh", [])] + tech_denies + \
                 [p["regex"] for p in rules.get("formulaic_patterns_zh", []) + rules.get("patterns_en", [])]
    deny_re = re.compile(f"({'|'.join(all_denies)})", re.IGNORECASE)
    whitelists = rules.get("contextual_whitelists_zh", {})

    violations, in_code, fence = [], False, ""
    for num, raw_line in enumerate(text.splitlines(), start=1):
        s = raw_line.strip()
        if not in_code and (s.startswith("````") or s.startswith("```")):
            in_code, fence = True, ("````" if s.startswith("````") else "```")
            continue
        if in_code and s.startswith(fence):
            in_code = False
            continue
        if in_code or not s or (check_end is not None and not (check_start <= num <= check_end)):
            continue

        prose = re.sub(r"`[^`\n]+`", "", raw_line)
        m = deny_re.search(prose)
        if m:
            violations.append(f"Line {num}: '{m.group(1)}' ({s[:40]})")
            continue
        for term, w_pat in whitelists.items():
            if term in prose and not re.search(w_pat, prose, re.IGNORECASE):
                violations.append(f"Line {num}: '{term}' ({s[:40]})")

    if violations:
        return f"[ANTI-AI GATE DENIAL] {target_path.name} detected {len(violations)} formulaic AI tell(s). Rewrite in active human voice:\n" + "\n".join(violations)
    return None


def evaluate_payload(payload: dict) -> dict:
    args = payload.get("toolCall", {}).get("args", {})
    target_str = args.get("TargetFile") or args.get("file_path") or ""
    if target_str and re.search(r"/Downloads/.*\.(py|sh)$", target_str):
        return {"decision": "deny", "reason": "[DIRECTORY HYGIENE DENIAL] ~/Downloads/ is delivery-only. Store scratch scripts in scratch/."}

    rules = json.loads(RULES_GATE_PATH.read_text(encoding="utf-8")) if RULES_GATE_PATH.is_file() else {}
    code = args.get("CodeContent") or args.get("ReplacementContent") or ""

    sec_err = check_security(code, rules)
    if sec_err:
        return {"decision": "deny", "reason": sec_err}

    ai_err = check_anti_ai(Path(target_str) if target_str else Path(""), args, rules)
    if ai_err:
        return {"decision": "deny", "reason": ai_err}

    return {"decision": "allow"}


def main() -> None:
    try:
        raw = sys.stdin.read().strip()
        print(json.dumps(evaluate_payload(json.loads(raw)) if raw else {"decision": "allow"}))
    except Exception:
        print(json.dumps({"decision": "allow"}))


if __name__ == "__main__":
    main()
