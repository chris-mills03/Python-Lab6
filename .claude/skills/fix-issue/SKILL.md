---
name: fix-issue
description: Fix the issue described in CLAUDE.md, following CONTRIBUTING.md and AGENTS.md. Use when asked to fix or work on the issue.
---

# Fix the issue

Follow these steps in order. Stop where it says **Ask** and wait for my answer.

## 1. Understand
- Reread "The task" in CLAUDE.md, then read the whole target file, including
  its existing doctests.
- Confirm you're on the branch named in CLAUDE.md (`git status`).

## 2. Reproduce
- Show the bug with a one-line `python3 -c "..."` using the examples from
  CLAUDE.md. Keep the real output to compare with after the fix.

## 3. Plan (**Ask**)
- In a few sentences, explain the root cause, the smallest change that fixes
  it, and the doctests you'll add.
- Name the CONTRIBUTING.md or AGENTS.md rule behind each choice.
- Wait for my approval before editing.

## 4. Implement
- Change only the target file, and keep its existing structure and comments.
- Raise `ValueError` for bad input, with the message assigned to `msg` first.
- Add doctests for valid input and for the error case. Run them, and paste the
  real output; never write expected output by hand.

## 5. Validate
- Run the `validate-change` skill. If anything fails, fix it and validate again.
- Rerun the reproduction from step 2 to show the bug is gone.

## 6. Wrap up (**Ask**)
- Propose a commit message such as `fix: other/password.py <what changed>`,
  without links to the upstream issue.
- Draft a PR description from `.github/pull_request_template.md`:
  - Summarize the bug, cause and fix at the top.
  - Tick only the boxes that are true; at least one under "Describe your change".
  - Don't include upstream issue links or `TheAlgorithms/Python#` references.
  - Print it in the chat so I can paste it on GitHub.
- Commit only after I approve.

