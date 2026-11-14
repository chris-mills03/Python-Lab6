"""PreToolUse hook: stop any git command that could contribute to upstream.

Claude Code sends the pending tool call as JSON on stdin. Exit code 2 blocks
the call and shows the stderr message to Claude.
"""

import json
import re
import shlex
import subprocess
import sys

UPSTREAM = "thealgorithms"
UPSTREAM_REF = re.compile(r"TheAlgorithms/Python(#\d+|/(issues|pull)/\d+)", re.I)
GIT_OPTIONS_WITH_VALUE = {"-C", "-c", "--git-dir", "--work-tree"}


def git_subcommand(tokens: list[str]) -> tuple[str, list[str]]:
    """Return the git subcommand and its arguments, skipping global options.

    >>> git_subcommand(["git", "-C", "repo", "push", "upstream"])
    ('push', ['upstream'])
    """
    index = 1
    while index < len(tokens) and tokens[index].startswith("-"):
        index += 2 if tokens[index] in GIT_OPTIONS_WITH_VALUE else 1
    if index >= len(tokens):
        return "", []
    return tokens[index], tokens[index + 1 :]


def origin_url(cwd: str) -> str:
    result = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        capture_output=True,
        text=True,
        cwd=cwd or None,
        check=False,
    )
    return result.stdout.strip().lower()


def check(command: str, origin: str) -> str | None:
    """Return why the command is blocked, or None if it is allowed.

    >>> check("git push upstream master", "git@github.com:me/fork.git")
    'git push is only allowed to origin (your fork), not "upstream".'
    >>> check("git commit -m 'fix'", "https://github.com/thealgorithms/python.git")
    'origin points at TheAlgorithms, so this clone is upstream, not your fork.'
    >>> check("git commit -m 'Fixes TheAlgorithms/Python#15633'", "me/fork")
    'Do not reference the upstream issue: GitHub would link it upstream.'
    >>> check("git status && git commit -m 'fix length'", "me/fork") is None
    True
    """
    for segment in re.split(r"&&|\|\||;|\|", command):
        try:
            tokens = shlex.split(segment)
        except ValueError:
            tokens = segment.split()
        if not tokens or tokens[0] != "git":
            continue
        sub, args = git_subcommand(tokens)
        if sub in {"commit", "push"} and UPSTREAM in origin:
            return (
                "origin points at TheAlgorithms, so this clone is upstream, "
                "not your fork."
            )
        if sub == "push":
            remotes = [arg for arg in args if not arg.startswith("-")]
            if remotes and remotes[0] != "origin":
                return (
                    "git push is only allowed to origin (your fork), "
                    f'not "{remotes[0]}".'
                )
        if sub == "remote" and UPSTREAM in segment.lower():
            return (
                "Adding or changing a remote that points at TheAlgorithms is blocked."
            )
        if sub == "commit" and UPSTREAM_REF.search(segment):
            return "Do not reference the upstream issue: GitHub would link it upstream."
    return None


def main() -> int:
    event = json.load(sys.stdin)
    if event.get("tool_name") != "Bash":
        return 0
    command = event.get("tool_input", {}).get("command", "")
    if "git" not in command:
        return 0
    if reason := check(command, origin_url(event.get("cwd", ""))):
        print(f"Blocked by protect_upstream hook: {reason}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
