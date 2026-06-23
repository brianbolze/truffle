# Implementation Notes: signal_delta Wayback Recursive Dir Loading

Date: 2026-06-22
Status: implemented and pushed
Commit: `a4b43b5` (`tools: recurse signal-delta directory loads`)

## What Changed

- `tools/signal_delta.py` directory inputs now load `*.json` recursively.
- `tests/test_signal_delta.py` covers file input, flat directory input, and nested Wayback page-slug directories.
- `tools/signal_delta.md` documents recursive directory loading.
- `tools/BACKLOG.md` moved the recursive loader item to Graduated.

## Verification

- `python3 -m pytest tests/test_signal_delta.py -q` — 17 passed.
- `ruff check tools/signal_delta.py tests/test_signal_delta.py` — passed.
- `git diff --check` — passed.

## Review

`/review-change` found no material issues. The implementation stayed inside the approved proposal:
loader, focused tests, docs, and backlog only; no Signals contract change, store mutation, live capture,
Wayback subject change, or domain-level page aggregation.

## Workflow Note

One post-push doc sweep found stale path wording in the tool docstring and docs. The docs now use the
same optional page-slug path as `scripts/signals.py persist`.
