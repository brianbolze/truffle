# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
learning_tags: [query-time-grouping-enough, depth-backfill, denominator-reconciliation, freshness-monitoring, schema-edge-entity-type]
```

## 30-second operator read

- **Did the run work?** Yes — store-only buyer read across 4 Transactional consumer-goods
  brands (Warby, Nike, Therabody, Hyperice). Clean answer + a sharper gap map.
- **What was awkward?** The interesting finding is a *fielding* gap, not a frame break: the
  schema carries price + revenue shape well, but the non-price retail decision (returns,
  warranty, channel, FSA/HSA) lives only in prose. Catalog-breadth comparison is uneven
  because `offerings.md` enumeration scope differs (Nike rostered only its recovery line).
- **What should the next agent know?** "No new primitive needed" holds; this is the
  consumer-goods analog of run 045's "body carries the decision" finding — recurring, now
  on a cohort whose *price* the spine does carry, which isolates the gap to non-price
  factors. Don't over-read 4 price-publishing brands as proof the frame handles all
  transactional retail.

## What happened

Scaffolded scout (046), generated a 6-candidate slate, selected C1 (transactional
consumer-goods buyer read) for reader value + reach (physical-retail shape under-tested
since the watch run 033) + a clean builder lens. Renamed to
`consumer-goods-transactional-buyer-read`. Loop 1 read all four `profile.md` + `offerings.md`
files plus the SCHEMA price-visibility token definition; confirmed `business_model:
Transactional` across the store (28 hits, mostly out-of-scope). No external sources, no
spend, no store mutation.

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
| W1 | wish | A catalog buyer's non-price purchase-protection factors — **return window, warranty length, free-shipping threshold, FSA/HSA, payment (BNPL), channel** — are captured in all 4 profiles but **only in prose** (`How it works / model`, `Credibility & proof`). No frontmatter or `offerings.md` field carries them, so a 4-brand purchase-protection table can't be drawn structurally; several cells are "not quoted." | That a new field/block should be built — only that the want is real and cross-brand-comparable and currently unfielded. Four brands is too thin to mandate a primitive. | read.md Result(2) + Gap Map; C4; `store/{warbyparker,nike,therabody,hyperice}-com/profile.md` "How it works" | depth-backfill, schema-edge-entity-type |
| G1 | gap | `portfolio_shape: Catalog` deliberately means *un-enumerable*, so catalog breadth lives in `offerings.md`, whose **enumeration scope varies**: Hyperice rostered all 65 handles; Therabody `indexed-complete`; **Nike enumerated only its recovery/wellness line** (rest parked in `unverified_fields`); Warby exemplars-only. A "who's widest" read is a coverage artifact, not a market fact. | That the offerings module is broken — only that cross-brand breadth is comparable solely where enumeration scope matches. | read.md Result(3); C5; `store/nike-com/profile.md` unverified_fields; `store/hyperice-com/offerings.md` (65 handles) | denominator-reconciliation, coverage-caveat |
| S1 | surprise | The per-line price-visibility token (`[published]`/`[on-request]`) handled the **consumer-line-vs-services split cleanly across all 4** — each has a `[published]` hardware catalog and an `[on-request]` services/B2B leg (Warby exams, Therabody Reset/Coach/corporate, Nike free membership, Hyperice team sales). A useful trap avoided: no company-level "transparent pricing" scalar was needed or implied. | That this graduates anything — only that per-line-token-not-company-scalar (cousin to L006) corroborated on a fresh, non-intermediary entity type. | read.md Result(1); C3; SCHEMA.md:142 price-visibility note | query-time-grouping-enough |
| G2 | gap | Therabody + Hyperice were captured **mid-Prime-Day-sale**; `offerings.md` prices are sale snapshots with strike-through regular prices ("re-check before ranking"). `captured_at` dates the capture but **carries no flag that the merchandising state was promotional**, so a returning buyer can't distinguish a sale snapshot from a regular-price one without reading the offerings note. | That a sale-state flag should be added — only that `captured_at` alone doesn't signal promotional pricing, and a price read off it can mislead. | read.md Source Gaps; C6; `store/therabody-com/offerings.md` site_notes; `store/hyperice-com/profile.md` unverified_fields | freshness-monitoring, source-rigor |

## Inputs and scope

- **Store slice:** `store/{warbyparker-com, nike-com, therabody-com, hyperice-com}/`
  (`profile.md` + `offerings.md` each). All `business_model: Transactional / One-time`.
- **Schema reference:** `SCHEMA.md` price-visibility token note (:142) + offerings pointer (:215).
- **Denominator check:** `grep -rl "business_model: Transactional" store/*/profile.md` → 28
  hits; most are luxury watches (covered run 033), apple/ford/casio/swatch, or clinical
  pharmacy supply — out of scope for the consumer-catalog buyer question. Seed set is
  explicitly partial.
- **Exclusions:** no external sources, no Firecrawl, no captures re-render, no store mutation.

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

Low friction — the four profiles + offerings were directly readable; no helper gap. The
only manual step was cross-reading four prose "How it works" blocks to assemble the
purchase-protection comparison (the W1 finding), which is the gap itself, not a tooling
friction.

## Evidence limits

- Seed n=4, all price-publishing — can't see how the frame handles a gated/quote-only
  physical-product seller (loop1_failure_mode guarded; stated as "not found," not "not
  there").
- Nike breadth understated (recovery-line-only enumeration).
- Therabody/Hyperice prices are a Prime Day sale snapshot; not current-price-grade.
- No receipts written — all claims are local store reads (store clocks cited inline in
  read.md Evidence Used); `receipts/` left empty by design for a store-only read.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a** (store-only)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no live browsing, no spend, no store mutation)
- Required citations / receipts present and source-graded: **pass** (store paths + clocks, C1–C6)
- No snippet treated as evidence: **pass** (no external snippets used)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (store `captured_at` cited; sale-snapshot flagged)
- Absence language says "not found", not "not true": **pass**

## Surprises

The price-visibility token's per-line design (S1) quietly did the hardest part of the job —
keeping a "this brand publishes prices" read honest about each brand's `[on-request]`
services leg without any company-level scalar. The expected story was "subscription schema
strains on transactional retail"; the actual story is the opposite — price/revenue fit is
clean, and the strain is on the *non-price* retail factors the schema never had a field
for.

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

**Fired:** `query-time-grouping-enough` (frame generalizes, no new primitive),
`depth-backfill` (non-price retail factors unfielded), `denominator-reconciliation`
(uneven offerings enumeration → breadth coverage artifact), `freshness-monitoring`
(sale-snapshot pricing), `schema-edge-entity-type` (transactional physical-retail). No new
tag coined — existing set fit.

"No new primitive needed" is a valid outcome — and is the verdict here.

## Next-run advice

- The "body carries the decision, structured spine doesn't" shape has now surfaced on
  agencies (045) and consumer goods (046) — a learning pass may want to look at whether
  these cluster with the marketplace/take-rate (L006) family or form their own
  "prose-only decision factors" lesson. **Not a run's call** — flagging for the next pass.
- If re-running consumer goods, deliberately pick a brand that **gates** physical-product
  pricing (a made-to-order or dealer-network seller) to test the other half of the
  price-visibility token on transactional retail.
- Avoid re-treading schema-edge entity-fit as a headline — it's saturated; this run earned
  its keep by leading with buyer value and using the fit question as the builder lens.
