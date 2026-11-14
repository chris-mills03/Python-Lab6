---
name: validate-change
description: Run every check CI and CONTRIBUTING.md require on the files changed on this branch, then report pass/fail. Use before committing or opening a PR.
---

# Validate Procedure

1. List the changed files: `git diff --name-only origin/master` (this includes
   uncommitted work). Every changed file must be one the fix needs.
2. For each changed `.py` file, run these from the repo root and record the result:
   - `python3 -m doctest -v <file>`
   - `uvx ruff check <file>`
   - `uvx ruff format --check <file>`
   - `uvx pytest <file> --doctest-modules`
   - `uvx pre-commit run --files <file>`
   If `uvx` can't reach the network, say so and keep the results that did run.
3. Review the diff against CONTRIBUTING.md and AGENTS.md, and answer each item
   yes or no with a line reference:
   - Type hints on every parameter and return value?
   - Erroneous input raises `ValueError` (or another fitting exception)?
   - Doctests cover both valid and erroneous input?
   - Descriptive names, no new single-letter names beyond what was already there?
   - No `print()` or `input()` added to the algorithm?
   - Comments explain why, not what, and stay within 88 characters?
   - Only one algorithm file changed, and not `README.md` or `DIRECTORY.md`?
4. Report a short table of each check and its result. If anything fails, fix it
   and run the checks again, up to three attempts. Then ask the user.
