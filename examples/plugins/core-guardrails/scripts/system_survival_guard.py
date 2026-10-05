#!/usr/bin/env python3
"""
System Survival Guard PreToolUse Hook
Detects and pauses on catastrophic / destructive system commands (disk wipes, root deletions, permission destruction).
Requires manual confirmation via force_ask decision while allowing normal development & Git operations.
"""

import sys
import json
import re

# -----------------------------------------------------------------------------
# Destructive Command Patterns
# -----------------------------------------------------------------------------

# Category 1: Disk & File Wiping
DISK_WIPE_PATTERNS = [
    # dd with input file
    ("dd if=", re.compile(r"\bdd\b(?:\.exe)?\s+.*?\bif\s*=", re.IGNORECASE)),
    # mkfs format commands (e.g. mkfs.ext4, mkfs.xfs, mkfs /dev/sda)
    ("mkfs", re.compile(r"\bmkfs(?:\.[a-zA-Z0-9_-]+|\b)", re.IGNORECASE)),
    # shred disk/file wiper
    ("shred", re.compile(r"\bshred\b", re.IGNORECASE)),
    # rm -rf on critical root / user home directories
    (
        "rm -rf critical paths",
        re.compile(
            r"\brm\s+[^;\|&]*?"
            r"(?:-[a-zA-Z]*[rR][a-zA-Z]*[fF]|-[a-zA-Z]*[fF][a-zA-Z]*[rR]|--recursive\s+--force|--force\s+--recursive)"
            r"[^;\|&]*?\s+"
            r"(?:/(?:\*|\s|$)|~(?:\*|/|\s|$)|/home(?:\b|/|\*|\s|$)|/root(?:\b|/|\*|\s|$)|/etc(?:\b|/|\*|\s|$)|/usr(?:\b|/|\*|\s|$)|/var(?:\b|/|\*|\s|$)|/bin(?:\b|/|\*|\s|$)|/sbin(?:\b|/|\*|\s|$)|/boot(?:\b|/|\*|\s|$)|/dev(?:\b|/|\*|\s|$)|/lib(?:64)?(?:\b|/|\*|\s|$)|/sys(?:\b|/|\*|\s|$)|/proc(?:\b|/|\*|\s|$)|/(?:[a-zA-Z0-9_-]+)?(?:\s|$|;)|(?:\$\{HOME\}|\$HOME)(?:\b|/|\*|\s|$))",
            re.IGNORECASE,
        ),
    ),
    # drop database SQL operations
    ("drop database", re.compile(r"\bdrop\s+database\b", re.IGNORECASE)),
]

# Category 2: Permissions & System Schedule Destruction
PERMISSION_SCHEDULE_PATTERNS = [
    # crontab removal
    ("crontab -r", re.compile(r"\bcrontab\s+[^;\|&]*?(?:-[a-zA-Z]*r\b|--remove\b)", re.IGNORECASE)),
    # recursive chmod 777 on root or wide scopes
    (
        "chmod -R 777 /",
        re.compile(
            r"\bchmod\s+[^;\|&]*?(?:-[a-zA-Z]*R\b|--recursive\b)[^;\|&]*?777\s+(?:/(?:\*|\s|$)|~(?:\*|/|\s|$)|/home(?:\b|/|\*|\s|$)|/root(?:\b|/|\*|\s|$)|/etc(?:\b|/|\*|\s|$)|/usr(?:\b|/|\*|\s|$)|(?:\$\{HOME\}|\$HOME)(?:\b|/|\*|\s|$))",
            re.IGNORECASE,
        ),
    ),
    # Sensitive credential files tampering or destruction
    ("/etc/shadow or /etc/passwd", re.compile(r"/etc/(?:shadow|passwd)\b", re.IGNORECASE)),
    # Shell history wiping
    ("history -c", re.compile(r"\bhistory\s+[^;\|&]*?(?:-[a-zA-Z]*c\b|--clear\b)", re.IGNORECASE)),
]

ALL_DESTRUCTIVE_PATTERNS = DISK_WIPE_PATTERNS + PERMISSION_SCHEDULE_PATTERNS

# -----------------------------------------------------------------------------
# Evaluation Engine
# -----------------------------------------------------------------------------

def evaluate_command(command_line: str) -> dict:
    if not command_line or not command_line.strip():
        return {"decision": "allow"}

    cmd = command_line.strip()

    # Split subcommands across bash operators (;, &&, ||, |, $(), ``, newlines)
    # to evaluate individual command clauses
    for _, pattern in ALL_DESTRUCTIVE_PATTERNS:
        if pattern.search(cmd):
            return {
                "decision": "force_ask",
                "reason": "Destructive command detected. Manual confirmation required."
            }

    return {"decision": "allow"}

def main() -> None:
    try:
        raw_input = sys.stdin.read().strip()
        if not raw_input:
            print(json.dumps({"decision": "allow"}))
            return

        payload = json.loads(raw_input)
        args = payload.get("toolCall", {}).get("args", {})
        command_line = args.get("CommandLine") or args.get("command") or payload.get("CommandLine") or ""

        result = evaluate_command(command_line)
        print(json.dumps(result))
    except Exception:
        print(json.dumps({"decision": "allow"}))

if __name__ == "__main__":
    main()
