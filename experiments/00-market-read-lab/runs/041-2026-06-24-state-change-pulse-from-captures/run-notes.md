# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
learning_tags: [freshness-monitoring, coverage-caveat, source-rigor, query-time-grouping-enough, denominator-reconciliation]
```

## 30-second operator read

- Did the run work? Yes — clean store-only gap-probe. Direct answer: the store **cannot**
  reliably reconstruct company-State change between captures, by design.
- What was awkward? The `captures/<date>/` substrate co-mingles three capture purposes
  (full / partial-deepen / visual-render) with no marker, so "does this domain have a
  diffable history" needed a manual page-content pass, not a folder count.
- What should the next agent know? The C6 synthesis-lag hypothesis **dissolved** — profile
  `captured_at` trailing the newest folder is the visual/deepen folders being newer, not
  stale synthesis. Don't re-run C6 as a lag-hunt without first filtering folder purpose.

## What happened

Gap-probe of the persistence boundary (value job: trust the cache over time). Enumerated
the 21/145 domains with 2+ dated capture folders (C1); confirmed the State-overwrite /
Signals-append contract from architecture.md; classified the diffable substrate (C2, ~10/21
have 2+ dates with real market pages); ran the cleanest same-page diff (belmar 06-02 vs
06-13, C3) and found capture-method noise dominates; confirmed prose is the only change
channel (~7/145, C4). Concluded no new primitive needed; mapped what would change it.

## Observations

Greedy raw learning for this run. Preserve singletons here, then Loop 2 appends the
useful rows to `learning/observations.md`. Do not merge rows, dedup into backlog items,
or translate wishes into build proposals inside the run.

Use short IDs such as `F1`, `S1`, `W1`, `G1` so reviews can cite them. Kinds are the
closed set: `friction` · `surprise` · `wish` · `gap` · `risk-miss` · `brian-correction`.
Record the symptom in `Saw`; put the boundary you are deliberately not asserting in
`Not claiming` (no fix, no build proposal).

| ID | Kind | Saw | Not claiming | Evidence pointer | Tags |
|---|---|---|---|---|---|
| G1 | gap | Company **State has no append-only home**: `profile.md` is an overwriting snapshot and the `signals/` append layer is scoped to *external* source movement (funding/reviews/visibility), so a brand's own pricing/offers/positioning change is structurally un-versioned. The value job "what's new since last look" is unanswerable for company State today. | That an append-only State-history layer should be built — only that none exists; "no new primitive needed" stays live (no returning-reader consumer yet). | read.md Result(1); _design/2026-05-30-architecture.md:57,60,75 | freshness-monitoring, query-time-grouping-enough |
| G2 | gap | The only retained prior-State substrate, `captures/<date>/`, **co-mingles three capture purposes** (full capture / partial deepen-offerings / visual-evidence re-render) under one dated-folder convention with no purpose or scope marker. ~11/21 "second captures" are render-only or partial; only ~10/21 are diffable on 2+ dates, and even those rarely repeat the same page set. | That the folder convention is wrong — only that it isn't a clean diff substrate without a purpose/scope marker a reader can filter on. | read.md Result(2); receipts C1/C2; functionhealth 06-13 render variants / 06-16 tiles-only | coverage-caveat, denominator-reconciliation |
| S1 | surprise | In the **cleanest** diffable case (belmar, identical 4-page set 11 days apart), the homepage diff is 289 lines but ~all of it is **capture-method noise** — `www`/trailing-slash URL normalization plus an expanded nav mega-menu the earlier capture never rendered. Zero price/plan/offer lines changed. | That belmar didn't change at all in reality — only that the store-retained diff cannot distinguish real market change from scrape-depth/markup noise without per-line human judgment. | read.md Result(3); receipt C3 | source-rigor, freshness-monitoring |
| S2 | surprise | The C6 **synthesis-lag hypothesis dissolved**: profile `captured_at` trailing the newest capture folder (true for ~all 21) is not stale synthesis — the newer folders are visual re-renders / partial deepens, not market re-captures. The capture clock is honest about the profile it describes. | That synthesis lag is impossible — only that this signal (clock vs newest folder) does not detect it; a real lag can't be ruled out without a per-folder purpose marker. | read.md C6; receipts C1/C2 | source-rigor, coverage-caveat |
| W1 | wish | Wanted a way to tell, per dated capture folder, *what kind* of capture it was (full vs partial-deepen vs visual-render) and *what scope* it covered, so the diffable subset is selectable instead of hand-inspected each run. | That this should be built — only that its absence is what made the substrate un-diffable; lightest path (a folder marker) noted, held, not proposed. | read.md Source Gaps; receipt C2 | tooling-ergonomics, coverage-caveat |
| CR1 | surprise | (Consumer review) Value-frontier lands on the **builder/Pantry** reader, not the end buyer: the read's deliverable is "stop treating `captures/` as a change feed," which a downstream system consumes, while a buyer asking "did this brand's price change" gets nothing. Third consecutive run with this frontier shape (after run-038 CR1, run-039 CR1). | That the read failed the buyer — it's a gap-probe whose payload is a roadmap finding; only that the strongest value is not buyer-facing. | consumer-review.md; read.md Result | query-time-grouping-enough, coverage-caveat |
| DR1 | risk-miss | (Developer review) The load-bearing "capture-method noise dominates real change" claim (S1) rests on **n=1 same-page diff** (belmar). It is the cleanest available case and reproduces, but the run generalizes the noise-dominates conclusion from a single brand-pair. | That the claim is wrong — belmar verifiably shows it; only that one same-page diff is a thin base for a store-wide generalization without a 2nd clean pair. | developer-review.md; receipt C3 | source-rigor, coverage-caveat |

## Inputs and scope

- Store slice: all 145 `store/<domain>/`; focus on the 21 with 2+ top-level dated
  `captures/` folders (receipt C1).
- Queries: folder enumeration (C1), real-market-page counts excluding `homepage_*`/`tiles`/
  `.payloads` (C2), same-page `diff` (C3), prose change-phrase grep (C4).
- Contract reference: `_design/2026-05-30-architecture.md` (State/Signals split), `SCHEMA.md`.
- Exclusions: `_archive/` capture folders; `signals/` captures; no external/live sources.
- Denominator named partial (top-level dated folders only).

## Live evidence plan

Required only for `bounded-live`; leave `null` for `store-only` and `local-existing`.

```yaml
live_evidence_plan: null
# For bounded-live, paste the selected Scout plan here.
# Default light ceilings: 2 source families, 6 outside sources read/captured,
# 20 paid capture credits. Lower if Scout set a tighter plan.
# Fail closed before exceeding the ceiling, adding an unplanned source family,
# broadening into search/crawl, or using login/paywalled/private sources.
```

## Live evidence used

Required for every outside source used in `bounded-live`. Leave `[]` for local-only runs.

```yaml
live_evidence_used: []
# For bounded-live entries:
# - source_or_query:
#   source_family:
#   action_taken: searched | opened | captured | scraped | read-local-signal
#   reason:
#   source_grade: primary | secondary | direction-finding
#   captured_at:
#   spend_note: none | free | paid-credit
#   claim_ids_supported: []
```

## Friction log

Repeated manual steps, took a long time, confusing paths, missing helpers, schema mismatches.
Summarize the operational friction here after preserving concrete sightings in the
Observations section.

## Evidence limits

Coverage gaps, stale captures, weak source grain, risky inference.

## Loop 1 exit check

Record `pass` / `fail` for the mandatory exit check before setting final `run_status`.

- Status was `scout-only` before Loop 1: pass
- `Selected Run Contract` was present and consistent with header: pass
- `autonomous_eligible: yes`: pass
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: pass (store-only)
- `approval_needed: no`: pass
- If `bounded-live`, `live_evidence_plan` was present and followed: n/a (store-only)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: n/a
- If `bounded-live`, stop rules and spend notes were recorded: n/a
- No disallowed action happened: pass (no scrape/live/mutation; local reads only)
- Required citations / receipts present and source-graded: pass (C1–C4, local/primary)
- No snippet treated as evidence: pass (no snippets used)
- Current/news/pricing/policy claims carry capture dates and source grade: pass (no current/external claims; all local store state with store clocks)
- Absence language says "not found", not "not true": pass (C6 framed "not synthesis lag," not "no lag"; denominator named partial)

## Surprises

Anything unexpected after touching the data.
Summarize the surprises here after preserving concrete sightings in the Observations
section.

## Learning tags

Short `kebab-case` recurrence handles for system pressure this run exposed. They mirror
the run header's `learning_tags`. These are not a fixed taxonomy and not permission to
build — a learning pass decides what, if anything, recurs into a lesson.

Use an existing tag when it fits; coin a narrow tag only when the guide misses the thing.

| Tag | Use when |
|---|---|
| `denominator-reconciliation` | The answer depends on defining / cleaning / reconciling the company or source **set**. |
| `source-rigor` | Source grade blocks confidence: snippets, weak secondary sources, missing URLs, or missing capture dates. |
| `source-panel` | A repeated external source **set** seems needed to answer this kind of question. |
| `coverage-caveat` | Store coverage, stale captures, or incomplete modules materially limit the answer. |
| `depth-backfill` | A specific field/module is missing across otherwise relevant companies. |
| `query-time-grouping-enough` | The read was answerable by grouping existing store evidence; no durable category object is needed. |
| `freshness-monitoring` | Current pricing, news, policy, regulation, or launch motion could change or materially improve the answer. |
| `relation-pressure` | Competitors, named parents, suppliers, partners, or other counterparties seem repeatedly useful. |
| `tooling-ergonomics` | Repeated manual steps suggest a helper, query recipe, or template tweak. |

Which tags fired, if any? Did this run need a new or clearer tag? Mirror them into the
header `learning_tags`.

"No new primitive needed" is a valid outcome.

## Next-run advice

What to try, avoid, or re-check.
