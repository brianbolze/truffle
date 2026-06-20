# Scout

## Prior Context Read

- `triage.md`: Active queue. Recurring acknowledged pressure is `denominator-reconciliation`
  (MRL-001), `source-rigor` (MRL-008), query recipes (MRL-002), depth-backfill (MRL-003),
  write-back receipt (MRL-009). Open relation items MRL-005/006/011, source-panel MRL-010,
  freshness MRL-012. Triage is annotation only — not a candidate source.
- `scout-context.md`: Two-test selection (value vs generic Claude+web; design pressure).
  Start from a reader-recognizable market question, not triage closure. Prefer store-only /
  local-existing when cached State is genuinely enough.
- Last 3 `run-notes.md` files (020 audience-whitespace, 021 trust-proof-devices,
  022 womens-whitespace-corroboration): all `reviewed`. 020/021 store-only, 022 bounded-live.
  Recurring lenses: `denominator-reconciliation`, `coverage-caveat`, `query-time-grouping-enough`.
- History map (`question_history.py`, 23 runs): heavily mined — GLP-1 (pricing visibility,
  offer ladder, trust gap, leaderboard, backend concentration), men's-health/TRT price, NAD/
  longevity positioning, ED/sexual-health access, category crowdedness, Trustpilot reputation,
  Wayback tenure, SEC funding, cross-cohort table-stakes, Hone substitutes, non-GLP1 backend,
  signal change-pulse, visual-brand cluster, audience whitespace, trust-proof devices, women's
  whitespace. **Under-tested:** whether captured *pricing itself* is comparable across brands
  (confidence/source-grain), licensure/regulatory disclosure patterns, and off-telehealth
  generalization.

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| In the store's GLP-1 cohort, is captured pricing actually comparable across brands, or do the pricing *units and structures* (per-month vs per-dose vs first-month-promo vs membership-inclusive vs dose-escalating) differ enough that any "cheapest brand" ranking is false confidence — and what minimum normalization would make a cross-brand price compare decision-grade? | mixed | yes | store-only | Tests the confidence/source-grain + persistence-boundary uncertainties directly; a meta-read on whether Truffle's own pricing State is decision-grade for "compare a whole field". Not yet run. | Each brand's captured price lines with their stated unit/cadence; explicit note where a unit is missing or ambiguous. | Treating a normalized number as published; over-claiming a "cheapest" winner when units don't align. |
| Across telehealth brands in the store, what provider-side trust/licensure disclosures (named medical director, state-licensure language, LegitScript/pharmacy accreditation, prescriber model) appear on owned pages, and how consistently is each surfaced? | market | yes | store-only | Provider-credibility angle distinct from 021's marketing proof-devices; tests depth-backfill (is this field captured uniformly?). | profile/visual/offerings text per brand naming disclosure type. | Depth-thin: disclosure may be uncaptured rather than absent — must say "not found". |
| Does the lab's cohort machinery generalize off telehealth — taking the store's SaaS/B2B captures (e.g. gong, clari, datadog, airtable, alpha-sense), what pricing-disclosure and offer-model patterns appear, and is the denominator even large/coherent enough to read? | system-test | yes | store-only | Tests whether reads generalize beyond the intentional telehealth cohort; design-test heavy. | Captured profiles/offerings for the B2B set; honest denominator count. | Thin/incoherent denominator; forcing a telehealth-shaped read onto B2B. |
| Across the captured telehealth cohort, what cancellation / refund / money-back-guarantee / commitment-exit terms do brands publish, and is "easy cancel / guarantee" becoming table stakes or a differentiator? | market | yes | store-only | Continuity terms partially seen in offer-ladder runs but exit/refund terms never isolated; reader-valuable. | offerings/profile text on refund, cancel, guarantee. | Terms often in ToS/checkout, likely uncaptured — high not-found risk. |
| In the GLP-1 cohort, which brands lead with quiz/intake-first acquisition vs buy-first vs price-first landing, and does the acquisition-surface pattern correlate with price visibility (published vs intake-gated)? | market | yes | store-only | Cross-tabs acquisition surface against the already-established price-visibility read; pattern-extraction. | landing/offer page structure + price-visibility flag per brand. | Landing structure may not be reliably captured; correlation over-read on small n. |
| Across the whole captured store, how stale is the cache — distribution of capture dates / store clocks by cohort — and which cohorts are most at risk of an invalidated read? | system-test | yes | store-only | Trust-the-cache-over-time job; meta corpus-health read feeding freshness pressure (MRL-012). | per-company capture timestamps from store files/signals. | Capture-date field semantics vary; mistaking missing timestamp for fresh. |

## Selected Question(s)

1. **(Recommended)** GLP-1 price comparability / unit-normalization — is captured pricing
   decision-grade for a cross-brand compare, or do units make any "cheapest" claim false
   confidence, and what minimum normalization closes the gap?
2. (Alt) Off-telehealth generalization probe on the B2B/SaaS captures.

Rationale: Candidate 1 is the freshest high-value store-only read. Every prior pricing run
(000, 008, 010, 013) *reported* prices or visibility; none asked whether the captured prices
are **comparable**. It directly exercises the confidence/source-grain and persistence-boundary
design uncertainties — does pricing need a normalized unit field to be decision-grade, or is
query-time grouping enough? It serves "compare a whole field" and "hand off in five seconds,"
and it beats generic Claude+web because it audits Truffle's *own* cited captured pricing rather
than re-scraping. Denominator is the already-established GLP-1 anchor set (~19 from run 012),
so denominator risk is contained.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "In the store's GLP-1 / compounded-semaglutide cohort, is the captured pricing actually comparable across brands, or do the pricing units and structures (per-month vs per-dose vs first-month-promo vs membership-inclusive vs dose-escalating tiers) differ enough that any cross-brand 'cheapest' ranking is false confidence — and what minimum normalization (unit, cadence, what's-included) would make a cross-brand price compare decision-grade?"
selected_slug: glp1-price-comparability-grain
run_type: mixed
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Store companies in the GLP-1 / compounded-semaglutide / medical-weight-loss cohort that carry captured pricing — anchored on the ~19-brand GLP-1 set established in run 012, treated as partial until verified against store files."
likely_source_panel: "store/<domain>/profile.md, offerings.md, and any pricing lines in captured State; no external sources."
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/triage.md"
  - "experiments/00-market-read-lab/ (prior run artifacts as evidence)"
disallowed_actions:
  - "Live browsing / Firecrawl spend / re-capture"
  - "Mutating store/"
  - "Write-back to project systems"
  - "Creating durable primitives or a normalized pricing schema"
  - "Graduating triage items"
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from already-captured store pricing State plus existing lab artifacts. No outside sources, no spend, no write-back. The read audits comparability of existing data; it does not normalize or persist anything."
loop1_failure_mode: "Presenting a normalized/derived price as if it were published, or declaring a 'cheapest brand' winner when captured units (per-dose vs per-month vs promo) are not actually aligned — i.e. manufacturing the very false confidence the question is probing."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. Candidate 1 selected over the
generalization probe (candidate 3) because its denominator is already established and its
design payload (is captured pricing decision-grade?) is sharper and lower-risk for an
unattended run. The off-telehealth probe is logged as the standout alternative for a future
cycle. Expect `denominator-reconciliation`, `source-rigor`, and either
`query-time-grouping-enough` or `depth-backfill` to be the live pressure lenses.
