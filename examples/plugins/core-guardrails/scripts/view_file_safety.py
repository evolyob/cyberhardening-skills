#!/usr/bin/env python3
"""ViewFile Safety Guard: Unified 800-line limit with grep probe enforcement."""
import sys
import json
from pathlib import Path

MAX_VIEW_LINES = 800
MEDIA_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp", ".ico", ".pdf", ".mp4"}


def exceeds_limit(p: Path, limit: int = 801) -> bool:
    """Terminates immediately upon finding limit lines (zero full-scan overhead)."""
    lines = 0
    try:
        with open(p, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                lines += chunk.count(b"\n")
                if lines >= limit:
                    return True
    except Exception:
        pass
    return False


def main():
    try:
        raw = sys.stdin.read().strip()
        if not raw:
            print(json.dumps({"decision": "allow"})); return

        args = json.loads(raw).get("toolCall", {}).get("args", {})
        target = Path(args.get("AbsolutePath") or args.get("file_path") or "")
        if not target.is_file() or target.suffix.lower() in MEDIA_EXTS:
            print(json.dumps({"decision": "allow"})); return

        # 1. Binary check (first 512 bytes)
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

        # 3. Unconstrained read: fast size check + bounded probe (< 801 lines)
        if target.stat().st_size > 40_000 and exceeds_limit(target, MAX_VIEW_LINES + 1):
            reason = f"[LARGE FILE] {target.name} exceeds {MAX_VIEW_LINES} lines. Prohibited from unconstrained read! Run grep -n to locate target symbols/headings, or specify exact StartLine/EndLine."
            print(json.dumps({"decision": "deny", "reason": reason}))
            return

    except Exception:
        pass

    print(json.dumps({"decision": "allow"}))


if __name__ == "__main__":
    main()
