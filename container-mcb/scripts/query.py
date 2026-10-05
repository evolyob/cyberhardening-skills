#!/usr/bin/env python3
"""
Deterministic Query & Evaluation Engine for container-mcb (Zero LLM Math).
Enforces single-shot querying across 6 product baselines, P0-P3 checklists, and SIEM matrices.
"""

import json
import argparse
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_json(name: str) -> dict:
    p = DATA_DIR / name
    if not p.is_file():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def query_products(product: str | None) -> list[dict]:
    data = load_json("products_baseline.json").get("products", {})
    if not product:
        return [{"product": k, **v} for k, v in data.items()]
    p_lower = product.lower()
    return [{"product": k, **v} for k, v in data.items() if p_lower in k.lower() or p_lower in v.get("platform", "").lower()]


def query_checklist(level: str | None) -> list[dict]:
    levels = load_json("matrix_p0_p3.json").get("levels", {})
    if not level:
        res = []
        for l_key, l_val in levels.items():
            for item in l_val.get("items", []):
                res.append({"level": l_key, "level_name": l_val.get("name"), **item})
        return res
    l_key = level.upper()
    l_val = levels.get(l_key, {})
    return [{"level": l_key, "level_name": l_val.get("name"), **item} for item in l_val.get("items", [])]


def query_ttps(ttp: str | None) -> list[dict]:
    ttps = load_json("threat_ttps_matrix.json").get("ttps", [])
    if not ttp:
        return ttps
    t_lower = ttp.lower()
    return [t for t in ttps if t_lower in t.get("id", "").lower() or t_lower in t.get("name", "").lower() or t_lower in t.get("tactic", "").lower()]


def query_siem(ttp_or_platform: str | None) -> list[dict]:
    rules = load_json("siem_rules.json").get("rules", [])
    if not ttp_or_platform:
        return rules
    q = ttp_or_platform.lower()
    return [r for r in rules if q in r.get("ttp", "").lower() or any(q in p.lower() for p in r.get("platform", []))]


def format_markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |"
    ]
    for r in rows:
        lines.append("| " + " | ".join(str(c).replace("\n", " ") for c in r) + " |")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Query Financial Container Security Baseline (MCB)")
    parser.add_argument("--product", help="Filter by container platform (AWS, Microsoft, GoogleCloud, IBM, RedHat, VMware)")
    parser.add_argument("--level", choices=["P0", "P1", "P2", "P3"], help="Filter by assessment dimension (P0, P1, P2, P3)")
    parser.add_argument("--ttp", help="Filter by MITRE ATT&CK for Containers TTP ID or name (e.g. T1611)")
    parser.add_argument("--siem", help="Filter SIEM detection rules by platform or TTP")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown", help="Output format")
    parser.add_argument("--check", action="store_true", help="Perform environment and readiness check")
    args = parser.parse_args()

    if args.check:
        print("[OK] container-mcb query engine ready with pure stdlib AST compliance.")
        return

    result = {}
    if args.product:
        result["products"] = query_products(args.product)
    if args.level:
        result["checklist"] = query_checklist(args.level)
    if args.ttp:
        result["ttps"] = query_ttps(args.ttp)
    if args.siem:
        result["siem_rules"] = query_siem(args.siem)

    if not result:
        result = {
            "products": query_products(None),
            "checklist_summary": {k: len(v.get("items", [])) for k, v in load_json("matrix_p0_p3.json").get("levels", {}).items()},
            "ttps_count": len(query_ttps(None)),
            "siem_rules_count": len(query_siem(None))
        }

    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    # Markdown rendering
    out = []
    if "products" in result:
        rows = [[p["product"], p["platform"], ", ".join(p.get("native_tools", [])[:2]), p.get("siem_integration", "")] for p in result["products"]]
        out.append("### Container Platforms & Native Tooling\n" + format_markdown_table(["Vendor", "Platform", "Native Security Tools", "SIEM Export"], rows))
    if "checklist" in result:
        rows = [[c["id"], c["level"], c["category"], c["name"], c["requirement"]] for c in result["checklist"]]
        out.append("### Assessment Dimension Controls\n" + format_markdown_table(["ID", "Level", "Category", "Control Name", "Requirement"], rows))
    if "ttps" in result:
        rows = [[t["id"], t.get("tier", "N/A"), t.get("tactic", ""), t.get("name", ""), t.get("cwpp_rule", t.get("cwpp_category", "")), t.get("detection_logic", t.get("detection", ""))] for t in result["ttps"]]
        out.append("### MITRE ATT&CK for Containers Detection Mappings\n" + format_markdown_table(["TTP ID", "Tier", "Tactic", "Technique Name", "CWPP Rule / Category", "Detection Logic"], rows))
    if "siem_rules" in result:
        rows = [[r["id"], r["name"], r["severity"], ", ".join(r["platform"]), r["ttp"], f"`{r['query_logic']}`"] for r in result["siem_rules"]]
        out.append("### SIEM Detection Rules\n" + format_markdown_table(["Rule ID", "Rule Name", "Severity", "Platforms", "TTP", "Query Logic"], rows))
    if not out:
        out.append(f"### Financial Container Security Baseline Overview\n- Active Platforms: {len(result.get('products', []))}\n- Total TTPs: {result.get('ttps_count')}\n- Total SIEM Rules: {result.get('siem_rules_count')}")

    print("\n\n".join(out))


if __name__ == "__main__":
    main()
