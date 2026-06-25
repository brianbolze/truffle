# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
learning_tags: [query-time-grouping-enough, depth-backfill, denominator-reconciliation, source-rigor, coverage-caveat]
```

## 30-second operator read

- Did the run work? Yes — store-only buyer-value read on the connected sleep/recovery
  cohort. Year-one TCO assembled cleanly from State for 4/5 brands; Apple Watch hit an
  entity-grain wall (catalog-grain capture, no Watch SKU price).
- What was awkward? Normalizing to one "year-one $" — Whoop bundles the device into the
  sub, others separate; billing cadences differ; every device price is a sale snapshot.
- What should the next agent know? This is the **buyer-value inverse of run-037's schema
  probe**. Payload: 037's hybrid-revenue `business_model` lossiness is real but **not
  decision-blocking for a human buyer** (prose carries it); it blocks only a programmatic
  apples-to-apples sort. Notably, value landed on the **buyer** here — a counter to the
  recent run-038/039/041 "lands on builder not buyer" streak.

## What happened

Drew the cohort by entity-shape (connected device + recurring layer), not by industry.
Read each profile's frontmatter + body pricing + site_notes/unverified_fields. Assembled a
per-brand year-one TCO range (device + first-year sub at captured cadence), carrying every
point-in-time flag and the required-vs-optional status from prose. Used Therabody/Hyperice/
Nike as a one-time-only foil contrast. One receipt (R1, store-query, derived). No spend, no
external source, no store mutation.

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
| S1 | surprise | The buyer's hardest composite fact — year-one TCO (device + required-vs-optional sub) — **is assemblable from captured State** for 4/5 brands: device price, sub price, billing cadence, and mandatory-vs-optional status are all present with capture clocks and point-in-time flags. A positive gap-probe result: the store carries the buyer's deciding fact, just not in one scannable column. Buyer-value inverse of run-037 (schema-lens) and a counter to the recent "value lands on builder not buyer" streak (038/039/041 CR1). | That it's apples-to-apples — it's an honestly-caveated *range*, not a single sortable number (see S2). | read.md Result table; R1 | query-time-grouping-enough |
| G1 | gap | The **required-vs-optional subscription** flag — the single most decision-relevant fact for year-one cost — lives only in prose / `STRAIN:` comments, never a structured field (Whoop "you join, you don't buy"; Eight Sleep "required for the first 12 months"; Oura "the only way to unlock… insights"; Peloton "must hold an All-Access Membership"). A buyer must read paragraphs to learn if the recurring cost is mandatory. Buyer-decision-relevance instance of run-037 G1/CR1. | That a structured flag should be built — n=4, single cohort, prose carries it for a human read; "no new primitive needed" stays live. | read.md Gap Map(1); run-037 G1/CR1 | depth-backfill, query-time-grouping-enough |
| S2 | surprise | The "year-one" unit is **structurally non-uniform** across the cohort, defeating a clean apples-to-apples sort even with all data present: Whoop bundles the device *into* the sub (year-one = sub only, $0 device) while others separate them; cadence differs (Whoop/Eight Sleep annual, Oura/Peloton monthly); rental paths (Eight Sleep $169/mo, Peloton $124.99/mo) reshape the whole TCO. Normalizing needs per-brand judgment, not a field. Cousin of run-023 GLP-1 price-incomparability, now on connected devices. | That the numbers are wrong — each is captured correctly; only that they aren't unit-comparable across the cohort. | read.md Gap Map(2); run-023 | source-rigor, denominator-reconciliation |
| G2 | gap | **Apple Watch is the cohort member the store cannot answer** — Apple is captured at company/catalog grain (a multi-product giant; only Mac entry prices quoted inline), with no Apple-Watch-SKU price. A single-product buyer question hits an entity-grain mismatch: a catalog-grain profile can't answer a SKU-grain buyer ask. New flavor vs the n=4 industry-draw recurrence — this is grain *within* a captured company, not cohort-draw contamination. | That the capture is wrong — catalog-grain is right for Apple; only that this grain can't serve a single-product TCO question. | read.md Gap Map(4), Result(C5); apple profile:33,40,59 | coverage-caveat, denominator-reconciliation |
| S3 | surprise | **Every device number is a point-in-time sale snapshot**, and the profiles flag it honestly — Oura flash sale with a same-day price disagreement ($279 vs $399 for Ceramic), Eight Sleep "4th July Sale", Peloton "limited-time" refurb ($695, ends June 15). A year-one TCO inherits that volatility wholesale; the read is a dated snapshot, not a durable price. | That prices are unreliable in the store — the captures are honest and clock-stamped; only that a TCO built on them is a snapshot. | read.md Gap Map(3); ouraring/eightsleep/onepeloton site_notes | source-rigor, freshness-monitoring |
| S4 | surprise | The one-time foils (Therabody/Hyperice/Nike) confirm `business_model: Transactional / One-time` is **accurate when revenue is single-leg** — no sub, year-one = sticker price. Clean contrast that proves the lock-in is a vendor *choice*, not a category inevitability. Mirrors run-037's pure-one-time foils (Therabody/Hyperice/Nike again). | That the field is always right — only that it's accurate for the single-leg case; the hybrid lossiness (G1) is the real edge. | read.md foil table; therabody/hyperice/nike business_model | query-time-grouping-enough |
| W1 | wish | If anything ever graduates from G1, the lightest path is run-037 W1's landing — a **ranked multi-select `business_model`** or a structured required-vs-optional flag — and **only** if a real consumer needs to *filter/sort* brands by composite cost programmatically. This run is positive evidence the human-read case does **not** need it: prose carried the buyer decision today. | That it should graduate now — only the lightest path *if* a filtering (not reading) consumer appears. "No new primitive needed" stays live. | read.md What Would Change; run-037 W1 | query-time-grouping-enough |
| VR1 | surprise | (Evidence verifier) Oura's membership is **value-gating, not strictly mandatory** — State says the ring "will still function… but the insights… much more limited," so Oura is the **only** cohort member where a buyer can legally pay **$0 recurring** (device-only floor $244). The read's "required for value: yes" column is defensible but flattens a real $0-recurring path that distinguishes Oura's lock-in from Whoop/Eight Sleep/Peloton (all strictly mandatory). | That the read was wrong — the column captures it; only that the sharper buyer fact is "Oura is the lone optional-recurring case," a precision the table compresses. | ouraring profile:81; read.md Result table | source-rigor, query-time-grouping-enough |
| CR1 | gap | (Consumer review) The year-one TCO is the run's own **Judgment** (an assembled, normalized range), **not** a store-queryable field — a downstream system can consume the per-brand device + sub prices as ingredients but cannot consume "year-one TCO" as State. Same "diagnosable but not queryable / map-not-ingredient" frontier as run-039 CR1, here on the **price** axis rather than relations. | That the read failed — it lands its buyer value; only that the headline number is synthesis, not an ingredient a Pantry consumer can query. | consumer-review.md; read.md Result | query-time-grouping-enough, denominator-reconciliation |

## Inputs and scope

- **Cohort (connected, device + recurring):** store/ouraring-com, whoop-com, eightsleep-com,
  onepeloton-com, apple-com (Apple Watch). Drawn by entity-shape, not `primary_industry`.
- **Foil set (one-time hardware):** store/therabody-com, hyperice-com, nike-com.
- **Files read:** each `profile.md` (frontmatter + body pricing + site_notes/unverified_fields).
- **Excluded:** all external sources (store-only contract); offerings.md not needed (body
  pricing sufficient); whole non-cohort store.

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

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a** (store-only)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no external source, no spend, no store mutation)
- Required citations / receipts present and source-graded: **pass** (R1, store-query/derived, claim map)
- No snippet treated as evidence: **pass** (all evidence is captured State, file:line cited)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (prices stamped as 2026-06-24 sale snapshots; volatility flagged S3)
- Absence language says "not found", not "not true": **pass** (Apple Watch SKU price "not captured" / below grain; Whoop checkout "gated, not captured")

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
