# Proposal: golden fixtures for capture-parser contracts

Date: 2026-06-24
Status: proposed
Source request: `tools/BACKLOG.md` "Tool hardening" — "Golden fixture tests for capture parser contracts" `[weakness]` + "Tiny envelope validator before an envelope builder" `[idea]` (its "Act when: adding fixture tests" has fired). Surfaced as ready by the engine work-menu.

## Required Fields

*Acceptance checks are defined here; they do not already exist.*

risk: low
write_scope: new `tests/test_serpapi.py`, `tests/test_trustpilot.py`, `tests/test_exa.py`; extend the existing `tests/test_wayback.py` with tenure-path cases; new `tests/_envelope.py` (the tiny validator helper) + `tests/test_envelope_contract.py` (spine across live tools + the dispatch-tie). Mark the two `tools/BACKLOG.md` items done after. **No `tools/*.py` production edits expected** — these tests pin existing behavior.
spend_stop: none. Inline fixtures only — patch each tool's I/O seam. No live SerpAPI / Firecrawl / Exa / Wayback / SEC calls, no paid APIs, no web browsing, no store writes.
acceptance_checks: the gate `ruff check scripts tools routines && python3 -m pytest tests/ -q` passes. New tests must prove the named holes (enumerated below) and the dispatch-tie. Verify the dispatch-tie actually bites: during dev, transiently rename one tool's emitted `tool` value, confirm `test_envelope_contract.py` fails (routes to `branch_fallback`), then revert. Receipt → `implementation-notes.md`.
escalate_if: a fixture reveals a *real* contract violation in a shipped tool — a non-conforming spine (e.g. `ok` not `False` when `schema_drift` is non-empty), or an emitted `tool` value that doesn't match its `signal_delta.DISPATCH` key. That is a live bug, not a test to loosen: stop and surface it. Also escalate if pinning a parser turns out to need a production refactor rather than a fixture.

## Problem

The capture tools in `tools/` (serpapi, trustpilot, exa, wayback, …) fetch from messy external sources, parse the response, and emit a JSON "envelope" that downstream consumers trust. Today most of that parsing is guarded only by prose gotchas in each tool's companion `.md`. `_match.py`, `signal_delta.py`, `sec_edgar.py`, and the wayback *content-diff* path have regression tests; the **capture parsers themselves mostly don't**. So a quiet upstream reshape — or a careless edit — could turn a parser silently wrong, and nothing would fail.

A second, related gap: every tool hand-builds the same reserved envelope spine (`tool` / `source` / `captured_at` / `ok` / `input` / `schema_drift`), and nothing checks that they all agree on it. The shape is convention, not enforced.

## Short Answer

Add small, offline golden fixtures for exactly the untested parser branches, plus **one** shared envelope-spine validator used as a test helper (not a runtime factory). Patch each tool's existing I/O seam — no live calls — mirroring how `tests/test_wayback.py` and `tests/test_sec_edgar.py` already work. Scope is deliberately the *real* holes; the wayback content-diff and sec_edgar paths are already covered and are left alone.

## Constraints / Non-Goals

- **No live API calls, no spend, no store writes.** Patch I/O at the seam.
- **Do not rebuild existing coverage.** `tests/test_wayback.py` (diff/snapshot path) and `tests/test_sec_edgar.py` (name-match, card boundary) stay as-is; wayback gains only the *tenure*-path cases they don't cover.
- **A test helper, not an envelope builder.** The backlog is explicit: do *not* jump to a shared runtime factory. Local envelope construction stays inside each tool; the validator only *asserts* the spine.
- No new `tools/` production code, no schema change, no new dependency (stdlib + `unittest`, run under pytest like the rest).

## The real holes (what each fixture pins)

Grounded in the actual function seams, not a guess:

- **serpapi** (`PARSER_VERSION` v2; patch `fetch_google_search` + `fetch_ai_overview`):
  - *inline-AIO* — SERP returns `ai_overview.text_blocks` inline with no `page_token`; `fetch_and_parse` must parse it with **no second call** (`cost.credits` stays 1, `ai_overview_present=True`). (`serpapi.py:237,256`)
  - *async-error* — `page_token` present, second call returns `{"error": …}` with no `text_blocks`; must set `ai_overview_skipped=True` + `…_unavailable_reason`, `ai_overview_present=False`, `ok` stays True, **not** `schema_drift`. (`serpapi.py:252`)
  - *list-rejection* — `classify_list_item` / `extract_ranked_brands` rejects non-brand list items (label prefixes like "best/top", over-long snippets). Pure-function fixture. (`serpapi.py:122,139`)
- **trustpilot** (`PARSER_VERSION` v1; pure parsers on canned markdown, no patch needed for state):
  - *active-empty* — `classify_state(md, status, review_count=0)` → `"empty"`. (`trustpilot.py:298`)
  - *removed* — `_REMOVED_SIGNS` markdown → `"removed"`. (`trustpilot.py:294`)
  - *Cloudflare challenge* — `is_challenge_page(md)` True on the interstitial, and `fetch_and_parse` raises (→ exit 2) rather than parsing it. (`trustpilot.py:305,347`)
  - boundary: `validate_shape_v1` returns `[]` (no false exit-3) for non-`active` states. (`trustpilot.py:316`)
- **exa** (`exa_similar.py` + `exa_search.py`; patch `_http_post_json`): a response dict **missing `results`** → `find_similar` / `search` raises `RuntimeError` (→ exit 2). One case per tool — same seam. (`exa_similar.py:144`, `exa_search.py:146`)
- **wayback — tenure path only** (patch `fetch_cdx`; the diff path is already covered):
  - *empty-CDX* — never-archived URL → `fetch_cdx` returns `[]` → `lookup` is `ok=True`, `snapshot_count=0`, `first_seen=None`, confidence `"insufficient"`, `schema_drift=[]`. (`wayback.py:306,513`)
  - *malformed header* — `parse_records` on a header missing a `REQUIRED_COLUMNS` entry **raises `RuntimeError`** → exit 2 (CDX is a frozen feed: transport-class, *not* `schema_drift`). (`wayback.py:330`)

## The sharp edge to pin (one shared validator + dispatch-tie)

`signal_delta.py` dispatches on the **literal** envelope `tool` value (`DISPATCH.get(src, branch_fallback)`, and `subject_of()` switches on `env["tool"]`). A renamed or hand-built envelope therefore routes **silently** to the named-veto fallback instead of its real branch — a real source reads as "undiffable" with no error.

So `tests/_envelope.py` does two things:

1. `assert_valid_envelope(env, *, expects_cost=False, expects_parser_version=False)` — required spine keys present; `captured_at` is UTC `…Z` and parses; `schema_drift` is a list and **non-empty ⇒ `ok is False`**; output is a JSON object (not a bare list); `input` is an object; optional `cost`/`parser_version` typed when present.
2. A **dispatch-tie** assertion: for each delta-routed tool, build a *real* envelope (from the patched tool, **never** a hand-typed `{"tool": "…"}` literal — inventing the string is exactly the bug that hides the misroute) and assert `env["tool"] in signal_delta.DISPATCH`. This catches a rename on either side. The tie applies to the 5 routed tools (trustpilot / serpapi / trends / wayback / sec_edgar); exa and ads_transparency emit envelopes but have no delta branch by design, so they get the spine check only — stated explicitly so the test doesn't over-claim.

## Options considered

1. **Per-tool fixtures at the established seam + one shared spine helper + dispatch-tie.** Matches the one-file-per-tool convention (MAINTAINING.md:35) and the existing patch-the-seam pattern; failures localize to a tool. [should have]
2. **One consolidated `test_capture_contracts.py` parametrized over all tools.** Fewer files, but breaks the file-per-tool convention and makes a failure harder to localize. [should have — rejected]
3. **A runtime `tools/_envelope.py` factory every tool calls, then test the factory.** This is precisely the "envelope builder" the backlog says *not* to jump to: it edits all ~8 tools, changes production code, and removes the local construction the spec wants preserved. [could have — cut]

## Recommendation

Option 1. It is the smallest change that closes the named holes and pins the spine, stays tests-only (low risk, fully reversible by deleting files, zero spend), follows the repo's own conventions, and leaves a test helper that pins the spine for the *next* capture tool — which is what the backlog's "validator before a builder" actually asked for.

## Implementation Sketch

No code yet — scoped steps:

1. `tests/_envelope.py`: `assert_valid_envelope(...)` + a small registry of canonical tool names, cross-checked against `signal_delta.DISPATCH` keys.
2. `tests/test_serpapi.py`: inline-AIO, async-error, list-rejection (patch the two `fetch_*` calls; pure call for list-rejection).
3. `tests/test_trustpilot.py`: active-empty, removed, challenge (pure parsers + one `_firecrawl_scrape`-patched `fetch_and_parse` for the raise), plus the `validate_shape_v1` non-active boundary.
4. `tests/test_exa.py`: missing-`results` → RuntimeError, one case each for `exa_similar` / `exa_search`.
5. Extend `tests/test_wayback.py`: empty-CDX tenure `lookup`; malformed-header `parse_records` raise. (Leave the diff-path tests untouched.)
6. `tests/test_envelope_contract.py`: run `assert_valid_envelope` over one real envelope from each live tool; assert the dispatch-tie for the 5 routed tools.
7. Mark both `tools/BACKLOG.md` "Tool hardening" items done; receipt + gate output → `implementation-notes.md`.

## Review Notes

- Confirm `risk: low` holds: this is tests-only with no production edit on the expected path. The one thing that could change that is escalate_if firing — a fixture exposing a real spine/dispatch violation — which is a feature of the work, not scope creep.
- Watch that fixtures pin *behavior*, not incidental output formatting, so a benign future reword of a message doesn't make them brittle.
- The dispatch-tie is the load-bearing test. Reviewer should confirm the envelope under test is built from the real tool, not a literal — and that the "verify it bites" step in `acceptance_checks` was actually run.
