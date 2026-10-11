#!/usr/bin/env python3
"""Interactive CNS 42001 & ISO Dual Statement of Applicability (SoA) Generator."""
import argparse
import json
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "index.json"

def load_controls() -> list[dict]:
    if not DATA_PATH.exists():
        return []
    try:
        data = json.loads(DATA_PATH.read_text(encoding="utf-8-sig"))
        return data if isinstance(data, list) else data.get("controls", [])
    except Exception:
        return []

def evaluate_applicability(answers: dict) -> list[dict]:
    controls = load_controls()
    results = []
    
    is_inhouse_dev = answers.get("inhouse_dev", True)
    is_public_facing = answers.get("public_facing", True)
    uses_cloud_llm = answers.get("cloud_llm", True)
    handles_confidential = answers.get("confidential_data", False)
    
    for c in controls:
        cid = c.get("id", "")
        status = "Applicable"
        justification = c.get("default_justification", "Mandatory operational governance control aligned with organizational AIMS baseline.")
        
        # Rule 1: No In-House Model Development
        if not is_inhouse_dev and cid in ("A.6.1.2", "A.6.1.3", "A.6.2.2", "A.6.2.3", "A.6.2.4", "A.7.2", "A.7.6"):
            status = "Excluded"
            justification = "Organization consumes external models via API only; no internal pre-training, fine-tuning, or algorithm engineering conducted."
            
        # Rule 2: Internal-Only Model Processing
        elif not is_public_facing and cid in ("A.8.2", "A.8.3", "A.8.4", "A.8.5"):
            status = "Excluded"
            justification = "System operates strictly in internal ETL / batch processing with zero citizen-facing interfaces or external users."
            
        # Rule 3: No Third-Party Cloud API Vendor
        elif not uses_cloud_llm and cid in ("A.10.1", "A.10.2", "A.10.3", "A.10.4"):
            status = "Excluded"
            justification = "Air-gapped on-premises architecture with zero third-party foundation model API dependencies."
            
        # Rule 4: Confidential Data Protection
        elif handles_confidential and cid in ("A.7.4", "A.7.5", "A.9.4"):
            justification = "Mandatory egress DLP and tokenized synthetic masking enforced under National AI Safety Guidelines."
            
        results.append({
            "id": cid,
            "cns_ref": c.get("cns_ref", cid),
            "iso27002_ref": c.get("iso27002_ref", "5.1"),
            "status": status,
            "justification": justification,
            "artifact": c.get("artifact", "[Compliance Evidence / 合規佐證]")
        })
    return results

def render_markdown(results: list[dict], org_name: str) -> str:
    lines = [
        f"# CNS 42001 & ISO 27001 Statement of Applicability (SoA)",
        f"",
        f"> Organization Scope: **{org_name}** | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"",
        f"| Unified Control ID | CNS/ISO Ref | ISO 27002 Ref | Status | Justification & Policy Reference | Implementation Artifact |",
        f"| :--- | :--- | :--- | :---: | :--- | :--- |"
    ]
    for r in results:
        lines.append(f"| `SOA-{r['id']}` | **{r['cns_ref']}** | **{r['iso27002_ref']}** | `{r['status']}` | {r['justification']} | `{r['artifact']}` |")
    return "\n".join(lines) + "\n"

def prompt_user_interactive() -> dict:
    print("=== CNS 42001 & ISO Dual SoA Assessment Wizard ===\n")
    org = input("1. Organization / Agency Name [Default: Enterprise AI Unit]: ").strip() or "Enterprise AI Unit"
    
    q1 = input("2. Does organization train/fine-tune models in-house? (y/n) [y]: ").strip().lower()
    q2 = input("3. Are AI outputs exposed directly to public citizens/users? (y/n) [y]: ").strip().lower()
    q3 = input("4. Are commercial 3rd-party APIs (OpenAI/Claude) integrated? (y/n) [y]: ").strip().lower()
    q4 = input("5. Does system process confidential / PII records? (y/n) [n]: ").strip().lower()
    
    return {
        "org_name": org,
        "inhouse_dev": q1 != "n",
        "public_facing": q2 != "n",
        "cloud_llm": q3 != "n",
        "confidential_data": q4 == "y"
    }

def main():
    parser = argparse.ArgumentParser(description="Generate CNS 42001 & ISO Dual SoA Markdown Report")
    parser.add_argument("-o", "--output", help="Destination file path for generated Markdown")
    parser.add_argument("--auto", action="store_true", help="Run with default enterprise profile non-interactively")
    args = parser.parse_args()

    answers = {
        "org_name": "Enterprise AI Governance Unit",
        "inhouse_dev": True,
        "public_facing": True,
        "cloud_llm": True,
        "confidential_data": False
    } if args.auto else prompt_user_interactive()

    results = evaluate_applicability(answers)
    md_content = render_markdown(results, answers.get("org_name", "Enterprise AI Unit"))

    if args.output:
        out_path = Path(args.output).expanduser().resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md_content, encoding="utf-8-sig")
        print(f"\n[✓] SoA successfully generated and saved to: {out_path}")
    else:
        print("\n" + md_content)

if __name__ == "__main__":
    main()
