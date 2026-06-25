# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue):
  L005 (query-time grouping enough when corpus carries the cut) and L006 (price-visibility
  token = buyer-reachability, not intermediary take rate) are the live lessons. Observations
  036–042 form a dense **schema-fit / entity-shape diagnostic** arc on non-telehealth slices
  (marketplaces, wearables, finance, deep-tech). Two recurrences are mature: `denominator-reconciliation`
  (industry draw ≠ entity-shape cohort) at n=4, and "decision-grade fact lives off the captured
  surface" at n=4. A third pattern: the last several gap-probes' value keeps landing on the
  **builder/Pantry** consumer, not the buyer (run-038 CR1, 039 CR1, 041 CR1).
- `scout-context.md`: select for reader value + reach + builder lens; don't default to store-only
  for ease; gap-probes are first-class but must name the builder lens; don't let lessons originate
  questions.
- Last 3 `run-notes.md` files (039 SaaS neighborhood, 041 state-change pulse, 042 deep-tech maturity):
  all store-only, all gap-probes whose payload landed on the builder. 040 (bounded-live state
  availability) is parked at `needs-human-review` — a caution against another similar bounded-live
  spend this cycle.
- Current run artifacts: fresh scaffold (043), temporary slug.

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **C1.** For a buyer choosing a connected sleep/recovery device (Oura, Whoop, Eight Sleep, Peloton, Apple), what is the **year-one total cost of ownership** (device + required vs optional subscription) and the lock-in, and can the store deliver an apples-to-apples year-one number per brand from captured State? | value-read | yes | store-only | Year-one total cost + "is the subscription mandatory" is the buyer's #1 deciding fact for this cohort; a real shopper question. Directly **flips run-037's hybrid-revenue *schema* finding into a *buyer-value* test**: does the single-valued `business_model` lossiness actually block the buyer, or does prose carry the composite cost fine? | Whether composite cost-of-ownership (one-time device + required/optional recurring) is **legible and assemblable from State for a buyer decision**, or whether the lossy single-model field + prose blend blocks an apples-to-apples year-one total. Tests the value frontier, not the schema. | Reaches past the schema-fit arc into a buyer-facing value-read; counterweight to the "lands on builder not buyer" streak. | Per-brand: device price(s), subscription price + cadence, required-vs-optional flag, all from captured profile State with capture clocks; flag flash-sale/point-in-time prices. | Manufacturing false comparability — sale-snapshot prices, size-dependent device prices, and "required for first 12 months then optional" nuance can be flattened into a fake single number. |
| C2. Across the captured telehealth store, can a reader assemble a defensible **total 3-month committed cost to start GLP-1** per brand despite known unit incomparability (run-023)? | value-read | yes | store-only | Buyer's hardest real GLP-1 question. | Whether price incomparability (run-023) is decision-blocking or assemblable with caveats. | Buyer value on the messiest price ingredient. | Per-brand entry price, multi-month commitment terms, capture clocks. | Re-confirming run-023 rather than adding the buyer-assembly angle. |
| C3. In a cut-carrying cohort (telehealth, with `anchor_category`), can the store draw a competitor neighborhood from State alone — calibrating run-039's SaaS "neighborhood not queryable" finding? | calibration | yes | store-only | Tests whether 039's failure is a SaaS-corpus artifact or store-wide. | Horizontal-relation absence — but 039 S1 already found it **structurally** absent store-wide, so this likely re-confirms. | Relation axis. | parent/owns + body competitor lines across the cohort. | Low marginal value — 039 already settled the structural answer. |
| C4. For an unfamiliar captured company, does its `profile.md` deliver a true **5-second cold-start** for a First Contact reader — what's strong, what forces a return to the live site? | calibration | yes | store-only | Tests the under-probed "cold-start" value job + the Scott-Witt 5-second-handoff frontier. | Synthesis/presentation sufficiency, not field design. | A different value job. | A sampled set of profiles read cold. | Navel-gazing; hard to keep falsifiable without a real reader. |
| C5. Which connected-wearable brands run **active paid acquisition** right now (Ads Transparency), and does it match their captured positioning? | gap-probe | no | bounded-live | Source-panel diversity (7 store-only runs in a row). | Ads source family on a new cohort. | A live source panel. | Ads Transparency Center captures, dated. | 040 just blocked a bounded-live spend; caution this cycle. Defer. |
| C6. Across the captured store, which brands disclose a **financing / BNPL** option (Affirm/Klarna) and at what grain — is "true cost over time" a capturable buyer ingredient? | value-read | yes | store-only | Real buyer affordability fact; cross-cohort. | Whether financing terms are a consistently captured ingredient or incidental prose. | A cross-cohort buyer ingredient. | Financing lines across profiles. | Likely too sparse/incidental to yield a clean read. |

## Selected Question(s)

1. **C1 — connected sleep/recovery device year-one total cost of ownership (buyer-value read).**

Rationale: highest real reader value (a genuine shopper decision), reaches past the recent
schema-fit/gap-probe arc into a buyer-facing value-read, and carries a sharp builder lens — it
**pressure-tests whether run-037's hybrid-revenue schema lossiness (G1/CR1) is actually
decision-blocking for a buyer, or whether prose carries the composite cost fine.** That directly
informs whether anything from 037 should ever graduate. Store-only is the right mode (data
confirmed present and rich: Eight Sleep Pod $2,749 + Autopilot $199–399/yr + rental $169/mo;
Oura ring + $5.99/mo membership), and it avoids another bounded-live spend the cycle after 040
parked at needs-human-review. C5 (the diversity candidate) is deferred for that reason.

These may be Scout recommendations until Brian or the operator confirms one.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "For a buyer choosing a connected sleep/recovery device (Oura, Whoop, Eight Sleep, Peloton, Apple Watch), what is the year-one total cost of ownership — device plus required-vs-optional subscription — and the lock-in, and can the store deliver an apples-to-apples year-one number per brand from captured State alone?"
selected_slug: wearable-year-one-cost-of-ownership
run_type: mixed
question_mode: value-read
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "The connected sleep/recovery device makers already captured in the store: ouraring-com, whoop-com, eightsleep-com, onepeloton-com, apple-com. Pure one-time-purchase recovery-hardware foils (therabody-com, hyperice-com, nike-com) available as a contrast set. Partial denominator by construction — not the whole wearable market."
likely_source_panel: "store/<domain>/profile.md (frontmatter business_model / offering_category / price-visibility tokens + body pricing + site_notes), store/<domain>/offerings.md where present. No external sources."
builder_lens: "Whether composite cost-of-ownership (one-time device + required/optional recurring subscription) is legible and assemblable into an apples-to-apples year-one total from captured State for a buyer decision — or whether the single-valued business_model field plus prose-only blend blocks comparability. A buyer-value-frontier test of run-037's hybrid-revenue schema finding, not a new schema probe."
reach_reason: "Reaches past the recent store-only schema-fit/gap-probe arc into a buyer-facing value-read, deliberately to test whether the recurring 'value lands on builder not buyer' frontier is a property of question design or of the store. Pressure-tests whether run-037 G1/CR1 lossiness is decision-blocking."
allowed_sources:
  - "store/ouraring-com/, store/whoop-com/, store/eightsleep-com/, store/onepeloton-com/, store/apple-com/ (profile.md, offerings.md, captures/ markdown if needed)"
  - "store/therabody-com/, store/hyperice-com/, store/nike-com/ (foil/contrast set)"
  - "experiments/00-market-read-lab/learning/ (context only)"
  - "SCHEMA.md, TAXONOMIES.md (contract reference only)"
disallowed_actions:
  - "No live browsing, Firecrawl, or any external source."
  - "No store/ mutation, write-back, durable primitive creation, or lesson graduation."
  - "No confident year-one number without carrying the point-in-time/sale-snapshot and size-dependent caveats the profiles flag."
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from local captured State; no spend, no external sources, no write-back. Store data confirmed present and rich for the cohort."
loop1_failure_mode: "Manufacturing false comparability — flattening sale-snapshot prices, size-dependent device prices, and required-then-optional subscription nuance into a fake single year-one number instead of an honestly-caveated, assemblable range. Absence language must say 'not captured', not 'no such cost'."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. This template records the
candidate slate and the Selected Run Contract; it should not carry its own preference
for question type or evidence mode.

Post-candidate pressure check applied: C1 deliberately breaks the store-only schema-fit
monotony with a buyer-value read; it is **not** a re-run of 037 (schema lens) but its
buyer-value inverse. C3 rejected as low marginal value (039 S1 already settled horizontal
relation as structurally absent store-wide). C5 deferred — bounded-live spend is cautioned
this cycle after 040 parked at needs-human-review.
