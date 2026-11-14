# CLAUDE.md: CS440 Lab 6 contribution agent

This repo is Chris's copy of TheAlgorithms/Python (`chris-mills03/Python-Lab6`),
used for CS440 Lab 6. The job: fix an issue from TheAlgorithms/Python **inside this
fork**, following the project's own contribution rules, and open the PR **in this
fork**. Never contribute to the upstream project.

## Read these before any change

@CONTRIBUTING.md
@AGENTS.md
@.github/pull_request_template.md

Precedence when they disagree: CONTRIBUTING.md, then AGENTS.md, then this file.
(AGENTS.md itself says it complements and never overrides CONTRIBUTING.md.)

## Hard rules (the hooks in `.claude/hooks/` enforce these)

- Never push to, open PRs on, comment on, or create issues on any TheAlgorithms
  repo. Read-only commands (`gh issue view ... -R TheAlgorithms/Python`) are fine.
- All fork and PR steps go through `python3 .claude/scripts/fork_pr.py`, not raw
  `gh pr create`. Inside a fork, `gh pr create` targets upstream by default.
- Don't write `TheAlgorithms/Python#<n>` or upstream issue/PR URLs in commits, PR
  bodies, or issues. GitHub would post a cross-reference on the upstream issue.
  Mirror the issue into this fork and use `Fixes #<fork issue number>`.
- One algorithm file per PR. Keep the diff minimal and keep existing style.
- Never edit `README.md` or `DIRECTORY.md` (GitHub Actions regenerates them).
- Never fabricate doctest output. Run it and paste the real result.
- Algorithms return values instead of printing them, and raise `ValueError` on bad
  input. Every parameter and return value has a type hint.

## Workflow

- `/fix-issue <upstream issue number>` runs the whole contribution end to end.
- `/validate-contribution` runs every local check CI will run, plus the
  CONTRIBUTING.md checklist.

## Code and tests in one PR

The PR template asks contributors not to change code and tests in a single PR, but
CONTRIBUTING.md requires doctests that cover both valid and erroneous input. For a
bug fix that changes behavior (for example, a new `ValueError`), include only the
doctests that demonstrate the fix, tick both boxes that apply, and explain this
precedence in one sentence in the PR description. State that choice to the user
before committing.

## Environment

- Windows laptop, WSL Ubuntu. Repo: `/mnt/c/Users/chris/CSU-2026/CS440/Lab6/Python-Lab6`.
- Tools: `git`, `gh` (logged in as chris-mills03), `python3`, `uv`/`uvx`.
- Fix branches start from `origin/master`, which holds this agent config, so a
  PR's diff contains only the fix.
