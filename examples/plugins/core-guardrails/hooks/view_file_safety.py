#!/usr/bin/env python3
"""ViewFile Safety Guard: Binary block + smart overlap chunk planner."""
import sys
import json
from pathlib import Path

MAX_VIEW_LINES = 800
STEP = 750  # 800-line window with 50-line boundary overlap
MEDIA_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp", ".ico", ".pdf", ".mp4"}

def count_lines(p: Path) -> int:
    try:
        with open(p, "rb") as f:
            return sum(chunk.count(b"\n") for chunk in iter(lambda: f.read(65536), b""))
    except Exception:
        return 0

def main():
    try:
        raw = sys.stdin.read().strip()
        if not raw:
            print(json.dumps({"decision": "allow"})); return

        args = json.loads(raw).get("toolCall", {}).get("args", {})
        target = Path(args.get("AbsolutePath") or args.get("file_path") or "")
        if not target.is_file() or target.suffix.lower() in MEDIA_EXTS:
            print(json.dumps({"decision": "allow"})); return

        # 1. Binary check
        with open(target, "rb") as f:
            if b"\x00" in f.read(512):
                print(json.dumps({"decision": "deny", "reason": f"[BINARY BLOCK] {target.name} is a binary file."}))
                return

        # 2. Specified range check
        start, end = args.get("StartLine"), args.get("EndLine")
        if start is not None and end is not None:
            if (int(end) - int(start) + 1) > MAX_VIEW_LINES:
                print(json.dumps({"decision": "deny", "reason": f"[SPAN EXCEEDED] Maximum {MAX_VIEW_LINES} lines per read."}))
                return
            print(json.dumps({"decision": "allow"})); return

        # 3. Unspecified range on large files: chunk plan or grep guidance
        total = count_lines(target)
        if total > MAX_VIEW_LINES:
            total_batches = (total + STEP - 1) // STEP
            if total > 3000:
                reason = f"[LARGE FILE PROTECTION] {target.name} has {total} lines (~{total_batches} batches). Prohibited from full continuous reads! Use grep -n to probe headings or inspect precise line ranges."
            else:
                batches = [f"Batch {i+1} (StartLine: {s}, EndLine: {min(s + MAX_VIEW_LINES - 1, total)})"
                           for i, s in enumerate(range(1, total + 1, STEP))]
                plan = "; ".join(batches)
                reason = f"[CHUNK READING PLAN] {target.name} has {total} lines ({total_batches} batches). Read sequentially via: {plan}."
            print(json.dumps({"decision": "deny", "reason": reason}))
            return

    except Exception:
        pass

    print(json.dumps({"decision": "allow"}))

if __name__ == "__main__":
    main()
