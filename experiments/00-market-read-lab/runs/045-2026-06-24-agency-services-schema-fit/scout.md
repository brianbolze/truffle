# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue):
  L005 (query-time grouping enough only when corpus carries the cut) and L006 (price-visibility
  token grain on intermediaries) are live. The recent observation stream (036–044) is a
  heavy **schema-edge-entity-type** + **query-time-grouping-enough** streak: marketplaces (036),
  wearable-hybrid revenue (037), deep-tech (042), finance/investor (035), usage-based dev-infra
  (044). Recurring verdicts: `denominator-reconciliation` industry-draw contamination (n=4),
  prose-carries-the-decision-fact / structured fields blind, unit-incommensurability (023/043/044).
  Recent CR1s note a shift to **buyer-primary value** (043/044).
- `scout-context.md`: select for reader value + reach + source-family diversity + calibration,
  not store-answerability. Name the builder lens. Gap-probes are first-class.
- Last 3 `run-notes.md` files: 042 (deep-tech maturity, store-only, reviewed), 043 (wearable
  TCO, store-only, reviewed), 044 (usage-based pricing comparability, store-only, reviewed).
  Also read 040 (bounded-live) — it **blocked** on a Firecrawl PDF spend overrun (15 credits on
  one ToS parse), a strong caution against bounded-live for an unattended run.
- Current run artifacts: fresh scout-only scaffold.

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **C1** — For a marketing/brand/innovation leader building a shortlist of **creative/strategy agency partners** (ideo, redantler, heco-partners, bullish, parlance), can the store support a vendor comparison — what each does, who it serves, positioning wedge, proof, and how to engage — or does the product/price-shaped universal schema leave a **services** buyer with nothing comparable? | gap-probe | yes | store-only | Untested entity type: pure **project-based professional-services** firms — no `offerings.md`, no SKU grain, bespoke/contact-gated pricing. The most product-hostile corner the schema-edge series hasn't hit; real B2B-buyer reader value (compare-a-field + 5s-handoff). | Does `offering_category`/`business_model`/price-visibility express what a **services** buyer needs (differentiation, clients/proof, engagement model) when there is no catalog spine to bind to? | The "no-catalog" end of the entity spectrum — opposite of marketplace/wearable/deep-tech probes. Whether the schema has *nothing* to grab vs. the wrong-grain thing. | profile.md State for all 5; offerings absence; price-visibility tokens; clients/case-study evidence in bodies. | Concluding "schema fails services" when prose actually carries the buyer decision (the recurring `prose-carries-it` outcome). |
| **C2** — Within those 5, parlance **partially publishes** engagement pricing (on /news pages) while the other 4 are fully contact-gated — does the price-visibility token + State capture this transparency split, and does it matter to a buyer? | value-read | yes | store-only | A clean internal contrast (1 transparent vs 4 opaque) on an entity type whose pricing convention is "never published." | Whether the price-visibility token is meaningful/legible on services firms. | Narrower than C1; risks being a sub-finding of it. | parlance vs the other 4 token + pricing lines. | Too narrow to be its own run; better folded into C1. |
| **C3** — Across the captured **VC/investor** firms (firstround, lsvp, sequoia, spero-vc, thrivecap, blueowl, standishspring), can a founder choosing whom to raise from compare thesis/stage/check-size/portfolio from State? | value-read | yes | store-only | Founder-side reader value. | Schema fit for capital allocators. | Investor entity type. | Stage/check/thesis fields across firms. | **Run 035 already covered finance/investor schema-fit** (L005 notes the price axis breaks for allocators) — likely a repeat. |
| **C4** — For the luxury-watch cohort (rolex, patek, AP, lange, cartier, swatch), can the store support "which maison fits my budget/positioning" beyond the price-visibility read run 033 already did? | value-read | yes | store-only | Consumer reader value. | Positioning/whitespace on a consumer-goods cohort. | Consumer-goods entity type. | Positioning + price-visibility State. | **Run 033 already read this cohort's price visibility** — recurrence without a new axis. |
| **C5** — Across the store, can a reader assemble a **five-second handoff brief** for an unfamiliar single company (cold-start job) directly from one profile.md, and which fields actually carry that load? | calibration | yes | store-only | Tests the cold-start + 5s-handoff jobs head-on. | Which fields are brief-load-bearing. | The brief-readiness frontier. | One/few profiles read as a brief consumer would. | **Run 038 (agent-delegation grounding)** already probed delegated-read adequacy; risks overlap. |
| **C6** — For a B2B buyer choosing a **brand/design agency**, do the store's `visual.md` layers (where present: bullish, parlance) add buyer-relevant differentiation that profile.md alone misses? | gap-probe | yes | local-existing | Uses the under-read visual-evidence layer. | Whether visual.md is a buyer ingredient for design-agency comparison. | The visual-evidence layer's buyer utility. | visual.md for bullish + parlance. | Only 2/5 have visual.md — too thin a denominator for a standalone run; fold as a sub-angle of C1. |

## Selected Question(s)

1. **C1** — Can the store support a creative/strategy **agency** vendor comparison for a
   services buyer, or does the product/price-shaped schema leave a services buyer with
   nothing comparable? (Folds C2's pricing-transparency split and C6's visual.md angle in
   as sub-observations.)

These are Scout recommendations until the operator confirms; C1 is the clear pick on
reach (new entity type), reader value (real B2B services-buyer job), and calibration
against the schema-edge streak.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "For a marketing/brand/innovation leader building a shortlist of creative/strategy agency partners (ideo, redantler, heco-partners, bullish, parlance), can the captured store support a vendor comparison — what each does, who it serves, its positioning wedge, proof/clients, and how to engage — or does Truffle's product/price-shaped universal schema leave a services buyer with nothing comparable?"
selected_slug: agency-services-schema-fit
run_type: mixed
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "The 5 captured pure project-based professional-services agencies tagged offering_category [Services / Consulting] + business_model Services / Project-based: ideo-com, redantler-com, heco-partners, bullish-co, parlance-cc. Clerky-com (legaltech hybrid, has priced packages) is an explicit foil, not in the core set. Treat the set as partial."
likely_source_panel: "store/<domain>/profile.md for the 5 agencies (+ clerky as foil); visual.md where present (bullish, parlance); no external sources."
builder_lens: "Schema fit for the no-catalog, no-list-price, project-based professional-services entity type — does offering_category / business_model / price-visibility express what a services buyer needs (differentiation, clients/proof, engagement model), or does the product-catalog spine have nothing to bind to?"
reach_reason: "Reaches the most product-hostile corner of the entity spectrum the schema-edge series has not hit — opposite end from marketplace/wearable/deep-tech/investor probes. Tests whether the schema fails by having *nothing to grab* rather than the wrong-grain thing."
allowed_sources:
  - "store/ (profile.md, visual.md, captures/ for the 5 agencies + clerky foil)"
  - "experiments/00-market-read-lab/learning/"
  - "SCHEMA.md / TAXONOMIES.md for token/field semantics"
disallowed_actions:
  - "Any live browsing, Firecrawl/SERP spend, or external capture"
  - "Mutating store/ or any project KB"
  - "Creating durable primitives or proposing/graduating lessons"
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Fully answerable from already-captured local store files and lab artifacts; store-only; no spend, no write-back, no external sources."
loop1_failure_mode: "Overclaiming 'the schema fails services' when prose actually carries the buyer decision (the recurring prose-carries-it outcome), or treating the 5-agency set as a census rather than a partial cohort."
```

## Selection Notes

C1 wins the slate because it extends the schema-edge series to the one entity type it has
not reached (pure project-based services with no catalog/price), serves a real B2B
services-buyer comparison job, and is calibration-rich: it can confirm or break the
recent `prose-carries-the-decision` and `query-time-grouping-enough` pattern on a cohort
where the schema's product spine is structurally absent rather than wrong-grain. C2 and C6
are real but narrower — folded into C1 as sub-angles (the parlance transparency split; the
visual.md buyer-utility check). C3/C4 risk repeating runs 035/033. C5 overlaps run 038.
Store-only chosen deliberately (not for ease): the question is about what the *existing
capture* expresses for this entity type, and 040's bounded-live spend block argues against
unattended live work this cycle.
