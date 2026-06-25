# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
learning_tags: [schema-edge-entity-type, query-time-grouping-enough, depth-backfill, source-panel, denominator-reconciliation]
```

## 30-second operator read

- **Did the run work?** Yes. Clean store-only calibration of the marketplace entity shape
  (5/5: airbnb, etsy, doordash, uber, upwork). Split verdict: the schema's *classification*
  fields fit marketplaces **well** (better than investors, run-035) — `offering_category:
  Marketplace / Platform` + `business_model: Marketplace / Commission` are real, designed-for
  values whose example cos are literally Airbnb/Uber. But the *economics* (take rate, GMV,
  monetized side) have **no structured home** — prose-only.
- **What was awkward?** Nothing operationally. The interpretive care is the two-stacked-absence
  split (run-035 S1): the store is NOT blind to take rate — it holds verbatim fee schedules
  in prose for 3/5 (etsy, doordash, upwork); airbnb + uber don't disclose fee % on-site
  (10-K scope). "schema-can't" (no field) ≠ "firm-didn't-on-site."
- **What should the next agent know?** This is the **first positive non-telehealth schema
  fit** (every prior generalizability read found overfit or a subtractive gate). Lands at
  **"no new primitive needed"** — economics are prose-carried, mostly disclosed, and a
  structured take-rate/GMV field would be sparse + unit-mismatched at n=5. Two reusable nuggets:
  (a) `business_model` (not `primary_industry`) is the load-bearing field for the marketplace
  cohort — it's industry-orthogonal; (b) the price-visibility token has a **grain mismatch**
  on marketplaces — it tags the *consumer* offering price, not the platform's take rate.

## What happened

Gated on `run_status: scout-only` + a complete store-only Selected Run Contract. Drew the
cohort via `grep -rl '^business_model: Marketplace / Commission' store/*/profile.md` (5, full
set). Read each `profile.md` (classification frontmatter + Overview/What-they-offer/business-model
prose + unverified_fields). Read the TAXONOMIES closed sets (`Marketplace / Platform` :47,
`Marketplace / Commission` :83) and the SCHEMA price-visibility token note (:142). Built the
classification-fit vs economics-gap split, applied the run-035 two-stacked-absence discipline to
the economics absence. No external/live evidence, no spend, no store write-back.

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
| O1 | surprise | **First positive non-telehealth schema fit.** All 5 marketplaces populate `offering_category: Marketplace / Platform` + `business_model: Marketplace / Commission` cleanly; both are designed-for closed-set values (TAXONOMIES:47/:83 example cos = Airbnb, Uber). Contrast run-035: investors got an *empty* business_model (subtractive gate). | That the schema fits *all* non-DTC shapes — only that the marketplace shape, unlike investor, is named positively + accurately. | read.md Result(1), Market Pattern #1; TAXONOMIES.md:47,:83 | schema-edge-entity-type, query-time-grouping-enough |
| O2 | gap | Marketplace **economics** (take rate, GMV, monetized side) have **no structured field** — all prose / `unverified_fields`. `target_market` gestures at two-sidedness but doesn't encode *which side pays*; no take_rate/gmv/monetized_side field. | That a field is needed — n=5, heterogeneous, unit-mismatched numbers; prose likely enough. | read.md Result(2), table; profile bodies (etsy:67–72, doordash:65–67, upwork:59–60) | depth-backfill, query-time-grouping-enough |
| S1 | surprise | **Two-stacked-absence resolved toward the store's favor:** the store is NOT blind to take rate — it holds verbatim fee schedules in prose for **3/5** (etsy 6.5%+, doordash 15–30%, upwork 3–10%). airbnb + uber simply don't disclose fee % on their *marketing* site (10-K scope). | That airbnb/uber "don't charge a fee" — only that it's *not captured on-site*. schema-can't ≠ firm-didn't-on-site. | read.md Result(3); airbnb profile.md:28/73, uber profile.md:71/106 | source-rigor, depth-backfill |
| G1 | gap | The SCHEMA price-visibility token `[published\|partial\|on-request]` has a **grain mismatch** on marketplaces: it tags the *consumer offering* price (airbnb Homes `[published]`, Trip services `[partial]`), but a platform's own "price" as a product is its **take rate** on the *other* side, which the token never addresses. | That the token is broken — only that it answers "can a buyer get a price," not "what does the platform charge." A grain insight, not a defect to fix at n=5. | read.md Gap Map; SCHEMA.md:142; airbnb profile.md:62/65/68 | schema-edge-entity-type |
| G2 | gap | The **filings / IR source family** (10-K, investor relations) is the missing panel for take rate of marketplaces that don't disclose on-site (airbnb, uber). The SEC tool captures funding *existence*, not take-rate/GMV. Marketplace analogue of L003 (uncaptured decision-grade ingredient). | That the store *should* capture filings economics — only that it's the panel an off-site take-rate read would need. Spend/approval-gated. | read.md Source Gaps; tools/ (SEC = existence only) | source-panel, depth-backfill |
| G3 | friction | `business_model` (not `primary_industry`) is the only field that recovers the marketplace cohort — the 5 scatter across 5 industries (Hospitality/Retail/Logistics/Automotive/Technology). A naive industry draw never assembles them. | That this is a defect — it's the *right* key working; just a note that marketplace ≠ an industry. | read.md Companies Seen; primary_industry grep | denominator-reconciliation |
| W1 | wish | If anything graduates from O2, the lightest path is a **documented prose/query convention** for marketplace economics (take rate, GMV, monetized side), **NOT** a per-marketplace structured field family — n=5, heterogeneous, unit-mismatched, off-site for 2/5. Mirrors run-035 W1's anti-sprawl landing. | That it should graduate now — only the lightest path *if* a real cross-marketplace economics consumer appears. "No new primitive needed" stays live. | read.md What Would Change | query-time-grouping-enough |

## Inputs and scope

- **Cohort/denominator:** `grep -rl '^business_model: Marketplace / Commission' store/*/profile.md`
  → 5 (airbnb-com, etsy-com, doordash-com, uber-com, upwork-com). Full set, grep-exact, not a sample.
- **Files read:** each brand's `store/<domain>/profile.md` (classification frontmatter, Overview,
  What-they-offer lines, business-model prose, unverified_fields). `ls store/<d>/` for module presence
  (offerings.md: only airbnb).
- **Contract read:** TAXONOMIES.md (`Marketplace / Platform` :47, `Marketplace / Commission` :83,
  business_model closed set :74–83); SCHEMA.md price-visibility token note (:142, :99).
- **Exclusions:** no external/live sources (store-only contract); off-site economics (10-K/IR) for
  airbnb + uber noted as not-captured, not pursued. No filings source family.

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

Minimal. The only manual step was per-profile prose extraction of take-rate/GMV facts
(hand-rolled grep over 5 bodies) — same MRL-002 query-machinery friction logged in
prior runs (035 F1 field-census grain), here on an "economics-from-prose" grain. One
sighting, not re-logged as a separate observation (rolls under the standing pattern).
No store write, no spend, no contract gate hit.

## Evidence limits

- **n=5, heterogeneous** (travel / crafts / food / rides / work). A schema-fit verdict,
  not a marketplace-market claim. The take-rate numbers are real but unit-incomparable
  (per-listing vs per-delivery-tier vs per-contract) — a reason prose beats a field here.
- **2/5 economics off-site** (airbnb, uber fee %): not captured, stated as *not captured*,
  not *not charged*. Closing this needs a filings/IR panel (G2), out of store-only scope.
- **Self-reported scale figures** (etsy GMS, upwork client spend) are marketing/CEO-bio
  copy per their own `unverified_fields` — quoted as captured, not independently verified.

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
- Required citations / receipts present and source-graded: **pass** (C1–C6 in read.md, local paths + capture clocks)
- No snippet treated as evidence: **pass** (all evidence is captured store prose/frontmatter)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (fee figures quoted as *captured* 2026-05-31/06-04, not asserted current)
- Absence language says "not found", not "not true": **pass** (airbnb/uber fee % = *not captured on-site*, not *not charged*)

## Surprises

The schema fits marketplaces *better* than expected — the contract's own example
companies for the two marketplace closed-set values are literally Airbnb and Uber, so
these fields were designed with this shape in mind, not retrofitted. This flips the
prior generalizability pattern: 027/033/035 all found overfit, subtractive gates, or
prose-only gaps; this is the first read where a non-telehealth entity shape is named
*positively and accurately* by the structured fields. (Preserved as O1/S1.)

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

Fired: `schema-edge-entity-type` (O1/G1 — marketplace shape at the schema edge),
`query-time-grouping-enough` (O1/O2/W1 — the no-new-primitive landing), `depth-backfill`
(O2/S1/G2 — economics missing as a field), `source-panel` (G2 — filings/IR family),
`denominator-reconciliation` (G3 — business_model is the cohort key, not industry). No
new tag coined; `schema-edge-entity-type` (used in 027/035) fits the marketplace shape
cleanly. "No new primitive needed" is the honest outcome.

## Next-run advice

- The **bounded-live follow-ups (Scout C4/C5)** are the natural next probes *if* a real
  consumer wants structured marketplace economics: C4 = take-rate corroboration from a
  filings/IR panel for the 2 off-site brands (airbnb, uber); C5 = two-sided reputation
  (does trust split by side — driver/rider, host/guest). Both need bounded plans; don't
  run on spec.
- For a sharper schema-fit verdict, a **2nd, more homogeneous marketplace cohort** (8–10
  food-delivery or e-commerce marketplaces) would test whether take-rate numbers are
  unit-comparable enough to ever justify a field — the n=5 heterogeneity is the main
  reason prose wins here.
- Re-check: the `business_model`-is-the-cohort-key finding (G3) is a reusable cohort-draw
  note for any future cross-shape read — industry grep won't assemble shape cohorts.
