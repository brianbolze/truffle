# Packet Review: Source Page Tool

Date: 2026-06-26
Mode: change - patch audit after implementation.
Reviewed: `proposal.md`, `proposal-review.md`, `implementation-notes.md`, and the implemented patch (`tools/source_page.py`, `tools/source_page.md`, `tools/README.md`, `tests/test_source_page.py`, `tests/fixtures/source_page/listicle.html`).
Independence: reviewer did not author the implementation in this visible thread context.

## Findings

**1 - Fallback exceptions break the tool's one-envelope failure contract.** `source_page` documents a stricter failure shape than most existing tools: even `ok:false` cases should still print one JSON envelope, then exit 2 (`tools/source_page.md` exit-code section; module docstring repeats the same invariant). The direct-HTTP path honors that, but the fallback path can still raise before `main()` prints anything. `capture_firecrawl()` builds an envelope, then calls `load_key()` outside the `try`; a missing `FIRECRAWL_API_KEY` raises `RuntimeError`. It also catches only `urllib.error.URLError`, `TimeoutError`, and `OSError` around `firecrawl_scrape()`, while `firecrawl_scrape()` returns `json.load(response)`, so malformed/non-JSON Firecrawl responses raise `JSONDecodeError`/`ValueError` and escape. I confirmed both with mocked probes. That misses the unattended/failure-path bar and partially weakens acceptance checks #2 and #6: the spend boundary is single-call, but not every malformed fallback outcome becomes the promised inspectable envelope. Suggested fix: convert fallback auth failure and JSON/malformed-response exceptions into `ok:false` `firecrawl.dev/scrape` envelopes, with no retry and with `cost.firecrawl_credits_estimate` reflecting whether a Firecrawl response was actually reached.

## Acceptance Check Read

- Deterministic gates passed: `ruff check tools/source_page.py tests/test_source_page.py`, `ruff format --check tools/source_page.py tests/test_source_page.py`, `/Users/brianbolze/.pyenv/versions/3.11.9/bin/python3 -m pytest tests/test_source_page.py -q` (22 passed), and `/Users/brianbolze/.pyenv/versions/3.11.9/bin/python3 -m pytest tests/ -q` (113 passed). The default `python3` lacks `pytest`, so I used the project pyenv Python.
- Scope matches the accepted proposal: one URL, print-only, direct-first, explicit fallback only, no store/cohort/experiment writes, no `page_role`, no cohort/candidate/classification output, no new schema drift validator.
- I did not rerun the live Flow Space / Tana / Forbes smoke checks because they require network and the Forbes fallback spends Firecrawl. I reviewed the recorded receipt and deterministic tests instead.

## What Is Strong

- The proposal-review findings were mostly folded in cleanly: `ok:true` now means useful reduced evidence, and the tests pin the thin-shell, binary, garbled-gzip, and single-call/no-retry boundaries.
- The tool keeps judgment out of the capture primitive. Output stays page-grain evidence (`title`, normalized `text`, absolute `links`) rather than cohort or source-panel logic.
- No contract blast-radius gate appears earned: this adds a new `tools/` entry and docs/tests, but does not change `SCHEMA.md`, `TAXONOMIES.md`, `SIGNALS.md`, or store persistence.

## Recommended Lean

Recommendation: **hold-after-review** until finding 1 is fixed, then merge without another broad review. The patch is otherwise narrow, tested, and faithful to the approved proposal; this is a small failure-path repair, not a redesign.

No decision was made; the reviewed artifact was not edited.
