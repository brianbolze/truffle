# Proposal Review: Source Page Tool

Date: 2026-06-26
Mode: proposal — gating the plan before code.
Reviewed: `proposal.md` (independent; reviewer did not author it).

## Boundary check

Clean proposal-mode review. Packet holds only `proposal.md` (`Status: proposed`); no
code in the tree (`git status`: untracked packet dir, one file). The plan/patch boundary
is intact — nothing to flag there.

## Verification (checked, not recalled)

The load-bearing claims hold against the repo:

- **P@10 numbers are real.** Telehealth 0.100→0.600, conversation-intelligence
  0.500→0.600 match the source packet's `implementation-notes.md` verbatim.
- **Envelope is faithful.** The proposed reserved spine (`tool` · `source` ·
  `captured_at` · `ok` · `input` · `schema_drift` · optional `cost`) matches
  `tools/README.md` exactly, and correctly omits `parser_version` (optional, drift-prone
  upstreams only).
- **The sketch describes the actual probe.** urllib fetch, bounded read, real UA,
  `HTMLParser` skipping script/style/noscript/svg, title/text/absolute-links, capped
  payloads, inline Firecrawl `/v2/scrape` (`markdown`+`links`, `maxAge:0`, US, no LLM) —
  all present in `page_extraction_probe.py`.
- **It is extraction, not graduation.** The source cohort verb is parked
  ("broad verb not graduated"; lead-decision: "No reusable `/cohort-discovery` skill").
  This lifts the proven generic primitive and leaves the parked verb behind — correct
  Truffle discipline.

## Findings (most important first)

**1 — The spend ceiling is asserted in prose, not enforced by a check.** `spend_stop`
and `escalate_if` are careful (one credit, one page, no retry loop, "retries that can
multiply spend" is a stop). But `acceptance_checks` #4 only verifies the fallback
*works* — it never verifies the *negative*: exactly one Firecrawl call per invocation,
no retry, no re-call on a malformed response. Per the "fail loud / spend boundary"
discipline, the strongest guarantee is a check, not a non-goal. The probe's
`run_firecrawl_fallback` is genuinely single-call-no-retry — good prior art — so this is
cheap to pin. *Recommend adding a negative spend check to `acceptance_checks`.*

**2 — `ok:true` inherits the probe's permissive semantics into a durable evidence
tool.** The probe sets `ok = 200<=status<400 and bool(parsed.text)` — any non-empty text
passes — and decodes `body.decode("utf-8", errors="replace")` with `Accept-Encoding:
identity`. For a probe scored on P@10 that's fine. For a generic tool meant to run on
arbitrary URLs, three silent-wrong paths ride along: a 200 with an empty JS shell
(a few hundred chars of nav) → `ok:true` with junk; a server that ignores `identity` and
gzips anyway → garbled bytes parsed to garbage text → `ok:true`; a non-utf-8 page →
mojibake. Acceptance check #3 tests `text_chars>5000` *externally*, but the tool's own
`ok` encodes no floor and no binary/encoding guard. This is the "fail loud before
silently wrong" line. *Recommend the plan decide explicitly what `ok` means — "HTTP
succeeded + parsed something" vs. "captured useful evidence" — and at minimum carry a
known-gotcha note (or a guard) for gzip/non-utf-8 bodies into `source_page.md`.*

**3 — Risk `medium` skips the line it's closest to.** The self-classification justifies
medium on "durable `tools/` entry + optional paid fallback." But lead-context lists
"paid capture posture" under *high*. Medium is defensible here — the path is flag-gated,
one credit, no new key (`FIRECRAWL_API_KEY` already exists for `trustpilot.py`) — but the
justification should engage the high line and say why bounded fallback keeps it medium,
rather than not naming it. Lead's call; flagging the gap in reasoning, not asserting the
bucket is wrong.

**4 — `schema_drift` is a structural placeholder here (minor).** A generic HTML reducer
has no fixed upstream schema to validate, so `schema_drift` stays `[]` and there's no
exit-3 path — correct per the convention (stable sources skip the validator), but the
plan doesn't say so. One line preventing the implementer from inventing a spurious
validator (or a future reviewer flagging the empty list as a bug) would close it.

## What's strong (a clean pass isn't "no issues")

- **Honors the no-premature-helper rule precisely.** `README.md` line 60 says don't
  pre-extract `_http.py`/`_firecrawl.py` for one user; `escalate_if` lists exactly those
  as stops. Tight alignment.
- **Boundary discipline is the best part.** Non-goals, `escalate_if`, and the explicit
  cuts of `page_role` and caller-provided raw-output paths are well-reasoned and match
  "capture not judgment / print not write." The `page_role` cut is right — classification
  is caller judgment.
- **Answers "what does it replace."** Not pure addition: it generalizes a proven
  primitive so agents stop re-rolling packet-local fetch hacks.

## What this review could not see

Plan-only review. I did not run the tool (it doesn't exist yet), so the silent-wrong
paths in finding 2 are reasoned from the probe's code, not observed. The acceptance
checks, *if* extended per findings 1–2, would catch them at implementation.

## Recommended lean (recommendation — the lead/Brian decides)

**Accept**, with findings 1 and 2 folded into `acceptance_checks` as conditions the
implementer honors (a negative spend check; an explicit `ok`-floor decision + a
gzip/encoding gotcha note). The plan is sound, faithful to conventions, well-scoped, and
de-risked by a real probe — the findings tighten it, they don't redirect it, and they're
small enough not to need a second review round. A lead who prefers those pinned in the
plan before greenlight could equally land on **revise** (lightweight); I'd not push the
packet to revise on findings 3–4 alone.

No decision was made; the reviewed artifact was not edited.
