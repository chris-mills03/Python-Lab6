"""PreToolUse hook: block git commands that could send work to upstream.

Exit code 2 tells Claude Code to cancel the command and show Claude the reason.
"""

import json
import sys

event = json.load(sys.stdin)
command = event.get("tool_input", {}).get("command", "")
words = command.split()

if "git" in words and "push" in words:
    target = words[words.index("push") + 1 :]
    remotes = [word for word in target if not word.startswith("-")]
    if remotes and remotes[0] != "origin":
        print("Blocked: only push to origin (your fork).", file=sys.stderr)
        sys.exit(2)

if "thealgorithms" in command.lower() and ("push" in words or "remote" in words):
    print("Blocked: never push to or add TheAlgorithms as a remote.", file=sys.stderr)
    sys.exit(2)