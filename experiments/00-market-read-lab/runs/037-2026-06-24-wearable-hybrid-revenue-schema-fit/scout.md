# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue):
  L005 (query-time grouping enough + structured-absence ≠ market-absence), L006
  (price-visibility token reports buyer-reachability, not what an intermediary charges
  its own side; `proposed`, held pending a 2nd entity-type sighting beyond
  marketplaces). Run-036 observations: schema fits the marketplace shape positively but
  has no structured field for two-sided economics (take rate), and `business_model`,
  not `primary_industry`, is the cohort-recovering key.
- `scout-context.md`: select for value + reach + roadmap learning, not store-answerability;
  name the builder lens; gap-probes are first-class; don't merely execute a parked step.
- Last 3 `run-notes.md` files: 034 (GLP-1 ads transparency, bounded-live), 035
  (finance/investor schema fit — investors got an *empty* business_model, subtractive
  gate), 036 (marketplace schema fit — first positive non-telehealth fit; economics
  grain has no structured field).
- Current run artifacts, if resuming: fresh scaffold.

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| C1 **(recommended)** Across the captured connected-hardware health/recovery brands (Oura, Whoop, Eight Sleep, Peloton) plus the pure-hardware foils (Therabody, Hyperice, Nike, Apple), what core offering + revenue model does each run, and does the universal `offering_category` / `business_model` frame express the device-sale + recurring-subscription **hybrid** ("device-as-a-service"), or does it collapse the split into a single `business_model` value? | calibration | yes | store-only | Recognizable consumer field (Oura vs Whoop vs Eight Sleep vs Peloton); a strategist or buyer reads this directly. Fresh cohort never read by the lab. | Whether `business_model` encodes hybrid hardware+subscription **revenue grain**, or the split survives only in `STRAIN:` inline comments / prose. New entity shape (connected hardware) vs the marketplace/investor runs. | A new schema-edge shape (hybrid revenue) distinct from two-sided marketplaces and subtractive-gate investors; tests whether the single-valued `business_model` enum is lossy on a co-primary revenue structure. | Store-only profiles; their inline `STRAIN`/comment markers; cross-brand `business_model` + `offering_category` + body pricing. | Overclaiming a clean "hybrid" pattern across a heterogeneous cohort — Whoop (sub-primary) ≠ Oura (device+membership) ≠ Therabody (pure one-time). The finding *is* the heterogeneity. |
| C2 The energy/aero deep-tech cluster (CFS, Electra Aero, Euclid Power, Evoloh, Sora Fuel, Verdego Aero, Blue Energy): for pre-revenue/B2B deep-tech with no DTC pricing, does the schema's `price_visibility` / `offering_category` / `business_model` degrade gracefully or go empty (echo of run-035 investor subtractive gate)? | gap-probe | yes | store-only | Tests schema against a pre-revenue B2B-hardware shape the telehealth-shaped schema never anticipated. | Whether structured fields fail-closed (empty) or mislabel on pre-revenue deep-tech; `business_model` already empty for 2/7 (cfs, sorafuel). | A 4th non-DTC entity shape after SaaS/investor/marketplace. | Store-only profiles. | Reader value is low (obscure companies); risk of an inward schema-audit with no downstream consumer. |
| C3 Across the connected-hardware cohort, is captured pricing actually comparable (device price + $/mo membership), or do units/structures (one-time device, mandatory sub, free-device-sub-only, content sub) defeat a clean cross-brand price table? | value-read | yes | store-only | Price comparability is a recurring reader job (cf. runs 023, 033). | Price-grain on a hardware+subscription cohort; does the store hold both the device price and the recurring price at comparable grain? | Price-comparability axis on a non-telehealth cohort. | Store-only profiles + body pricing lines. | Re-runs the 023/033 price-grain shape without enough new pressure; partial overlap with C1. |
| C4 A cross-store read of every `STRAIN:` inline marker: where does the universal schema strain, and do the strain sites cluster by entity shape (hybrid-revenue, two-sided, pre-revenue, house-of-brands)? | calibration | yes | store-only | Meta-map of known schema tension; could sharpen the schema-edge thread. | Whether strain sites are a coherent map or scattered one-offs. | The schema's own self-flagged tension surface. | Store-only grep of profile comments. | Too inward — a schema-audit, not a market read; weak downstream reader. |
| C5 Connected-hardware trust/proof devices: what clinical / accuracy / validation claims do wearables make (FDA clearance, peer-reviewed studies, sensor accuracy), and does the store capture proof at decision grade? | value-read | yes | store-only | Proof claims are a real buyer concern for health wearables. | Proof-device capture on a hardware cohort (cf. run 021 telehealth proof devices). | Proof-claim grain on hardware vs telehealth. | Store-only profiles. | Lower schema reach; mostly re-tests run-021's proof-device finding on a new cohort. |
| C6 Relations: who do connected-hardware buyers cross-shop (Oura vs Whoop vs Apple Watch vs Eight Sleep) per captured competitor/positioning evidence, and can the store map the substitute set without external demand-side evidence? | value-read | yes | store-only | Cross-shop is a recognizable buyer question. | Relation/neighborhood read on a fresh cohort. | Substitute mapping on hardware. | Store-only positioning/competitor prose. | `relation-pressure` is heavily tested (001/014/016/017/026/030); low marginal learning store-only. |

## Selected Question(s)

1. **C1** — connected-hardware hybrid-revenue schema fit (recommended).
2. C2 — deep-tech pre-revenue schema degradation (backup; lower reader value, strong calibration reach).

These may be Scout recommendations until Brian or the operator confirms one.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: >
  Across the captured connected-hardware health/recovery brands (Oura, Whoop, Eight
  Sleep, Peloton) plus the pure-hardware foils (Therabody, Hyperice, Nike, Apple), what
  core offering and revenue model does each run, and does the universal offering_category
  / business_model frame express the device-sale + recurring-subscription hybrid
  ("device-as-a-service"), or does it collapse that split into a single business_model
  value?
selected_slug: wearable-hybrid-revenue-schema-fit
run_type: system-test
question_mode: calibration
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: >
  Store companies whose offering_category includes "Physical Products / Hardware" AND
  that sell a connected device with a companion app — the connected-hardware cohort
  (Oura, Whoop, Eight Sleep, Peloton as core; Therabody, Hyperice, Nike, Apple as
  pure-/mixed-hardware foils). Denominator is a query-time judgment, not a structured
  field; "hardware" alone over-includes apparel (Nike) and platform devices (Apple).
likely_source_panel: store-only (profile.md frontmatter + body pricing/model lines)
builder_lens: >
  Whether the single-valued business_model enum encodes a co-primary hardware+subscription
  revenue structure, or whether the device-sale vs membership split survives only in
  STRAIN inline comments / prose — a revenue-grain test on a new entity shape, the
  hardware analogue of run-036's missing two-sided-economics field.
reach_reason: >
  Reaches a fresh, reader-recognizable cohort (consumer wearables) and a new schema-edge
  shape (hybrid device-as-a-service revenue) distinct from two-sided marketplaces (036)
  and subtractive-gate investors (035). Tests whether business_model is lossy on
  co-primary revenue, not just whether the store can group the cohort.
allowed_sources:
  - "store/ (connected-hardware profiles + pure-hardware foils)"
  - "experiments/00-market-read-lab/learning/"
  - "SCHEMA.md / TAXONOMIES.md (to read the business_model / offering_category contract)"
disallowed_actions:
  - "Live browsing, SERP, or Firecrawl spend"
  - "store/ mutation or write-back"
  - "Durable primitive / field creation or lesson graduation"
  - "Proposing a schema change (observe the grain; do not fix it)"
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: >
  Answerable entirely from local store profiles and the SCHEMA/TAXONOMIES contract; no
  spend, no live evidence, no write-back. Pure calibration read.
loop1_failure_mode: >
  Overclaiming a uniform "hybrid" pattern across a heterogeneous cohort — Whoop
  (subscription-primary, cheap/free device) ≠ Oura (device + membership) ≠ Eight Sleep
  (device + mandatory Autopilot) ≠ Therabody/Hyperice/Nike (pure one-time). The honest
  result is the spread of revenue shapes under one offering_category, and where the
  single business_model value loses that split.
```

## Selection Notes

C1 wins the two-test screen: genuine reader value (a recognizable consumer field) **and**
the strongest design reach — a new schema-edge mechanism (single-valued `business_model`
losing a co-primary hardware+subscription split) that extends the schema-edge-entity-type
thread onto a shape neither marketplaces (036) nor investors (035) tested. It is not
merely a parked next step: the STRAIN markers already visible in Oura/Whoop/Eight Sleep
frontmatter make the grain question concrete, and the cohort scatters across three
`primary_industry` values, independently re-testing run-036's "business_model is the
cohort-recovering key" finding. C2 is the backup — strong calibration reach but weak
downstream reader value (obscure pre-revenue companies). C4/C6 were rejected as too
inward (C4 schema-audit) or low marginal learning (C6 relation shape already heavily
tested store-only).
