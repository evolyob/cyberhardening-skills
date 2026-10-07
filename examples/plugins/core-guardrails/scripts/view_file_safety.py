#!/usr/bin/env python3
"""ViewFile Safety Guard: Binary block + smart overlap chunk planner."""
import sys
import json
from pathlib import Path

MAX_VIEW_LINES = 800
MEDIA_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp", ".ico", ".pdf", ".mp4"}

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

    except Exception:
        pass

    print(json.dumps({"decision": "allow"}))

if __name__ == "__main__":
    main()
