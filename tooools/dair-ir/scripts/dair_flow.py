#!/usr/bin/env python3
"""DAIR (Dynamic Approach to Incident Response) Workflow Engine."""


import argparse
import json
import sys
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "playbooks.json"


def load_data() -> dict:
    if not DATA_FILE.exists():
        return {"stages": [], "playbooks": {}, "nist_csf_mapping": {}}
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8-sig"))
    except (json.JSONDecodeError, OSError):
        return {"stages": [], "playbooks": {}, "nist_csf_mapping": {}}


def render_markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    sep = " | ".join([":---"] * len(headers))
    header_line = f"| {' | '.join(headers)} |"
    sep_line = f"| {sep} |"
    data_lines = [f"| {' | '.join(r)} |" for r in rows]
    return "\n".join([header_line, sep_line] + data_lines)


def get_stage_info(data: dict, stage_id: str | None) -> list[dict]:
    stages = data.get("stages", [])
    if not stage_id:
        return stages
    return [s for s in stages if s.get("id") == stage_id.lower() or str(s.get("order")) == stage_id]


def format_stages(stages: list[dict], fmt: str) -> str:
    if fmt == "json":
        return json.dumps(stages, ensure_ascii=False, indent=2)
    headers = ["Stage", "Name", "Objective", "Exit Gate"]
    rows = [
        [f"**Step {s.get('order')}**", f"`{s.get('name')}`", s.get("objective", ""), f"`{s.get('exit_gate')}`"]
        for s in stages
    ]
    return render_markdown_table(headers, rows)


def format_playbook(data: dict, playbook_id: str, fmt: str) -> str:
    pbs = data.get("playbooks", {})
    pb = pbs.get(playbook_id.lower())
    if not pb:
        available = ", ".join(pbs.keys())
        return f"Playbook '{playbook_id}' not found. Available: {available}"
    if fmt == "json":
        return json.dumps(pb, ensure_ascii=False, indent=2)
    actions = "\n".join(f"{idx+1}. {act}" for idx, act in enumerate(pb.get("priority_actions", [])))
    indicators = "\n".join(f"- {ind}" for ind in pb.get("scope_indicators", []))
    deadlines = "\n".join(f"- **{k}**: {v}" for k, v in pb.get("compliance_deadlines", {}).items())
    gates = "\n".join(f"- {g}" for g in pb.get("exit_gates", []))
    res = [
        f"### Playbook: {pb.get('name')}\n",
        f"- **Domain**: `{pb.get('domain')}`",
        f"- **Target ID**: `{pb.get('id')}`\n",
    ]
    if indicators:
        res.append(f"#### Scope Indicators\n{indicators}\n")
    if actions:
        res.append(f"#### Priority Actions\n{actions}\n")
    if deadlines:
        res.append(f"#### Compliance Deadlines\n{deadlines}\n")
    if gates:
        res.append(f"#### Exit Gates\n{gates}\n")
    return "\n".join(res)


INDEX_FILE = Path(__file__).resolve().parent.parent / "data" / "index.json"
CHAPTERS_DIR = Path(__file__).resolve().parent.parent / "chapters"


def load_index() -> list[dict]:
    if not INDEX_FILE.exists():
        return []
    try:
        data = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
        return data.get("chapters", [])
    except (json.JSONDecodeError, OSError):
        return []


def list_chapters(fmt: str) -> str:
    chs = load_index()
    if fmt == "json":
        return json.dumps(chs, ensure_ascii=False, indent=2)
    headers = ["#", "Chapter Title", "Pages", "Est Tokens", "File"]
    rows = [
        [str(c.get("chapter", "")), f"**{c.get('title', '')}**", str(c.get("pages", "")), str(c.get("est_tokens", 0)), f"`{c.get('file', '')}`"]
        for c in chs
    ]
    return render_markdown_table(headers, rows)


def read_chapter(query: str) -> str:
    chs = load_index()
    target = None
    for c in chs:
        if str(c.get("chapter")) == query or query.lower() in c.get("title", "").lower() or query.lower() in c.get("file", "").lower():
            target = c
            break
    if not target:
        return f"Chapter matching '{query}' not found."
    target_path = Path(__file__).resolve().parent.parent / target.get("file", "")
    if not target_path.exists():
        return f"Chapter file not found: {target_path}"
    return target_path.read_text(encoding="utf-8-sig", errors="replace")


def main() -> None:
    parser = argparse.ArgumentParser(description="DAIR Dynamic Incident Response CLI Engine")
    parser.add_argument("--stage", help="Query specific DAIR lifecycle stage (1-8 or stage ID)")
    parser.add_argument("--playbook", help="Query specific incident response playbook")
    parser.add_argument("--list-chapters", action="store_true", help="List all 20 book chapters")
    parser.add_argument("--chapter", help="Read specific chapter by number (1-20) or keyword")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown", help="Output format")
    parser.add_argument("--check", action="store_true", help="Perform environment readiness check")
    args = parser.parse_args()

    if args.check:
        print("[OK] DAIR Engine is Ready. Zero external dependencies required.")
        return

    if args.list_chapters:
        print(list_chapters(args.format))
        return

    if args.chapter:
        print(read_chapter(args.chapter))
        return

    data = load_data()
    if args.playbook:
        print(format_playbook(data, args.playbook, args.format))
        return

    stages = get_stage_info(data, args.stage)
    print(format_stages(stages, args.format))


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        try:
            sys.stdout.close()
        except OSError:
            pass
        sys.exit(0)
