# CLAUDE.md

## What this repo is
My copy of TheAlgorithms/Python (`chris-mills03/Python-Lab6`) for CS440 Lab 6.
All work stays in this repo. Never contribute to TheAlgorithms/Python.

## Rules to follow
Read these before changing any code. If they conflict, CONTRIBUTING.md wins.
@CONTRIBUTING.md
@AGENTS.md

## The task: issue 15633
Source: TheAlgorithms/Python issue 15633 (summarized below).
- File: `other/password.py`, function `alternative_password_generator(chars_incl, i)`
- Expected: it returns a password of length `i` that contains every character in `chars_incl`.
- Bug: when `chars_incl` is longer than `i`, the password is too long
  (length 5 with "abcdefgh" returns 8 characters; length 3 with "abcd" returns 5).
- Cause: `i -= len(chars_incl)` makes `i` negative, so no random characters are
  added and the function returns all of `chars_incl`.
- Fix: raise a `ValueError` when `i < len(chars_incl)`, and add doctests for valid and invalid input.

## Git
- Work on branch `issue-15633` and only change `other/password.py`.
- Commit when asked. Never push; I push and open the PR myself.
