#!/usr/bin/env python3
"""Deterministic ISO 42001 & ISO 27002 Crosswalk Query Engine."""
import argparse
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
INDEX_FILE = DATA_DIR / "index.json"
GLOSSARY_FILE = DATA_DIR / "glossary.json"


def load_json_safe(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8-sig", errors="replace"))
    except Exception:
        return {}


def format_markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    if not rows:
        return "*No matching records found.*"
    head = "| " + " | ".join(headers) + " |"
    sep = "| " + " | ".join([":---"] * len(headers)) + " |"
    body = "\n".join("| " + " | ".join(r) + " |" for r in rows)
    return f"{head}\n{sep}\n{body}"


def execute_filter(keyword: str, out_format: str) -> str:
    idx_data = load_json_safe(INDEX_FILE)
    glossary = load_json_safe(GLOSSARY_FILE).get("terms", [])
    chapters = idx_data.get("chapters", [])
    controls = idx_data.get("controls", [])
    kw = keyword.strip().lower()

    matched_controls = [
        c for c in controls
        if kw in c.get("id", "").lower()
        or kw in c.get("cns_ref", "").lower()
        or kw in c.get("title", "").lower()
        or kw in c.get("iso27002_ref", "").lower()
        or kw in c.get("summary", "").lower()
    ]
    matched_terms = [
        t for t in glossary
        if kw in t.get("term", "").lower()
        or kw in t.get("term_zh", "").lower()
        or kw in t.get("iso_ref", "").lower()
        or kw in t.get("definition", "").lower()
        or kw in t.get("definition_zh", "").lower()
    ]
    matched_chapters = [
        c for c in chapters
        if kw in c.get("id", "").lower()
        or kw in c.get("title", "").lower()
        or kw in c.get("title_zh", "").lower()
    ]

    if out_format == "json":
        return json.dumps({
            "keyword": keyword,
            "matched_controls": matched_controls,
            "matched_terms": matched_terms,
            "matched_chapters": matched_chapters
        }, ensure_ascii=False, indent=2)

    lines = [f"# Harmonization Crosswalk Search: `{keyword}`\n"]
    if matched_controls:
        lines.append("## Matched Standard Controls")
        rows = [[c.get("id", ""), c.get("title", ""), c.get("iso27002_ref", ""), c.get("summary", "")] for c in matched_controls]
        lines.append(format_markdown_table(["Control ID", "Official Title", "ISO 27002 Mapping", "Summary"], rows))
        lines.append("")

    if matched_chapters:
        lines.append("## Matched Chapters")
        rows = [[c["id"], c["title_zh"], c["file"]] for c in matched_chapters]
        lines.append(format_markdown_table(["Chapter ID", "Title (ZH)", "File Path"], rows))
        lines.append("")

    if matched_terms:
        lines.append("## Matched Glossary Terms")
        rows = [[t["term_zh"], t["term"], t["iso_ref"], t["definition_zh"]] for t in matched_terms]
        lines.append(format_markdown_table(["術語 (ZH)", "Term (EN)", "標準參照", "定義與說明"], rows))
        lines.append("")

    if not matched_controls and not matched_chapters and not matched_terms:
        lines.append("*No matching records found across controls, chapters, or glossary.*")

    return "\n".join(lines).strip()


def execute_batch(batch_path: Path, out_format: str) -> str:
    batch_data = load_json_safe(batch_path)
    if not batch_data:
        return json.dumps({"error": f"Failed to load batch file: {batch_path}"}) if out_format == "json" else f"Error: Failed to load {batch_path}"

    chapters = batch_data.get("chapters", [])
    if out_format == "json":
        return json.dumps({"total_chapters": len(chapters), "chapters": chapters}, ensure_ascii=False, indent=2)

    rows = [[str(c.get("index", "")), c.get("id", ""), c.get("title_zh", c.get("title", "")), c.get("file", "")] for c in chapters]
    return format_markdown_table(["Index", "ID", "Title", "File Path"], rows)


def main():
    p = argparse.ArgumentParser(description="Query ISO 42001 & ISO 27002 Crosswalk Registry")
    p.add_argument("--filter", "-f", help="Search keyword across terms and control references")
    p.add_argument("--batch", "-b", help="Inspect and batch parse a target index.json file")
    p.add_argument("--format", choices=["markdown", "json"], default="markdown", help="Output format")
    args = p.parse_args()

    if args.filter:
        print(execute_filter(args.filter, args.format))
        return

    if args.batch:
        print(execute_batch(Path(args.batch), args.format))
        return

    # Default: Output full chapter index
    index_data = load_json_safe(INDEX_FILE)
    if args.format == "json":
        print(json.dumps(index_data, ensure_ascii=False, indent=2))
        return

    chapters = index_data.get("chapters", [])
    rows = [[str(c.get("index", "")), c.get("id", ""), c.get("title_zh", ""), c.get("file", "")] for c in chapters]
    print(format_markdown_table(["Index", "Chapter ID", "Title (ZH)", "File Path"], rows))


if __name__ == "__main__":
    main()
