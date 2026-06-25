# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue):
  L001–L005 read. L005 (query-time-grouping-enough only when the corpus carries the cut)
  and the run-035 finding (schema gives investors a *subtractive* gate but no *positive*
  capital-allocator shape) are the live design pressure. observations.md stream is empty
  post-migration (rows ≤035 archived); no recent singleton to repeat.
- `scout-context.md`: two-test selection (value/reach + design); optimize slate for
  reader value, reach, source-family diversity, calibration — not store-answerability.
- Last 3 `run-notes.md` files (033 watches, 034 ads-transparency, 035 finance/investor):
  the **cross-vertical schema-fit arc** (027 SaaS → 033 watches → 035 finance) is the
  productive open thread. 035 explicitly parks *re-running finance* (needs a less
  VC-skewed cohort or a real consumer) — so a repeat finance read would be a parked next
  step and is rejected. The blank quadrant is the **marketplace / commission** entity
  shape, untested in any run.
- Question-history map: 36 prior runs. Telehealth deep; SaaS / watches / finance tested
  for generalizability; source families Trustpilot / Wayback / SEC / ads / SERP tested.
  **Never tested:** the two-sided **marketplace** entity shape, and the physical-goods
  **maker** shape outside luxury watches.

## Candidate Questions

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **C1 — Marketplace schema-fit.** Across the store's 5 marketplace/commission entities (airbnb, etsy, doordash, uber, upwork), does the universal `offering_category` / `business_model` / price-visibility frame express what a reader needs about a two-sided platform — take rate, GMV, supply vs demand side — or is it a finance-035-style "industry holds the entity but the schema can't carry its economics" gap? | calibration / gap-probe | yes | store-only | Marketplaces are the last untested entity shape in the generalizability arc; a reader profiling Uber/Airbnb needs take-rate + two-sidedness, not a subscription price. | Does the commerce-shaped schema (grown on DTC subscription) carry the marketplace/commission shape, or repeat the run-035 subtractive-gate-without-positive-shape result on a *new* shape? Tests offering grain + business_model closed-set fit. | Reaches a brand-new entity quadrant; extends 027/033/035 to its blank cell. | The 5 `profile.md` files + frontmatter + prose; SCHEMA/TAXONOMIES for the `business_model` closed set + offering_category list. | Two-stacked-absence trap (run-035 S1): "schema can't express take rate" vs "marketing site doesn't show it" — these are huge public co's whose economics live in 10-Ks, not on-site. |
| **C2 — Physical-goods maker price-visibility beyond luxury.** Across non-luxury makers (ford, nike, hyperice, warbyparker, electra-aero, onepeloton, evoloh), how does each present/price its catalog, and does the run-033 `published/partial/gated` × `gate-type × gate-grain` reading discipline generalize past watches? | calibration | yes | store-only | Extends the watch read (033) to mass-market makers where MSRP is published but the *channel* (dealer vs DTC) complicates "who sets the price." | Tests whether 033's gate-type×grain addend survives a non-luxury maker cohort, or needs a channel axis. | Reaches the maker shape beyond luxury; second data point for run-033 W1's graduation bar. | 7 `profile.md` + offerings where present; dealer/DTC channel prose. | Conflating "transactional" flatten with reality; Ford's dealer MSRP ≠ DTC price posture. Lower novelty — 033 already mapped the price-visibility axis. |
| **C3 — Untested-vertical schema census.** Across the Energy/Automotive/Manufacturing/Logistics/Hospitality slice (~17 co's), which structured fields populate vs sit empty, and where does the telehealth-shaped schema leave the most on the floor? | gap-probe | yes | store-only | Maps schema-fit across *all* remaining untested verticals at once — a coverage read of where the universal schema is thinnest. | Broad field-census (run-035 F1 grain); tests schema generalizability breadth, not depth. | Reaches every untested vertical, but shallowly. | Frontmatter census across ~17 profiles. | Too broad / shallow — risks a thin "fields are empty" census that doesn't isolate *why* (schema-can't vs firm-didn't). C1 is the sharper cut of the same pressure. |
| **C4 — Marketplace take-rate corroboration (live).** For the 5 marketplaces, what take rate / commission does each actually charge, per primary sources (10-K, investor pages, fee schedules), and how much of that is visible on the marketing site the store captured? | value-read | yes (bounded) | bounded-live | A reader's real marketplace question is "what's the take rate" — tests whether the store's on-site capture can ever answer it or needs an external source family. | Names the missing source family for marketplace economics (filings/fee-pages), like L003 did for review bodies. | Reaches off-site primary economics the store doesn't capture. | SEC 10-K / official fee schedules per brand; capture dates; primary/secondary grade. | Sprawl into financial-analysis; snippet-grade take-rate numbers read as fact. Heavier than needed when C1 can first establish the gap store-only. |
| **C5 — Marketplace trust two-sidedness (live).** For the marketplace cohort, do reviews/forums split by *side* (driver vs rider, host vs guest, seller vs buyer), and does the store's single-brand frame even have a place to hold a two-sided reputation? | gap-probe | yes (bounded) | bounded-live | Two-sided trust is a real reader need a one-brand profile can't express; probes a structural store gap. | Tests whether reputation State needs a side dimension for marketplaces. | Reaches a structural relation/grain gap. | SERP + ≥1 review surface per side; bounded panel. | Broad review-mining sprawl; the gap may be obvious without spend. Defer until C1 confirms the entity shape is worth a source-panel follow-up. |
| **C6 — Cross-store business_model distribution calibration.** Across all 136 captured entities, how does `business_model` distribute, how many are empty/`Other`, and does the closed set have a long tail of misfit entity shapes (marketplace, maker, allocator, utility)? | calibration | yes | store-only | A meta-read on whether the `business_model` closed set fits the captured universe or is telehealth-overfit. | Tests the closed-set itself (schema-edge), one level up from a single cohort. | Reaches the whole store, but as a distribution not a read. | `business_model` grep across all profiles + closed-set from SCHEMA. | Meta-without-a-reader; risks restating run-027's overfit finding without a fresh cut. C1 grounds the same question in a concrete cohort. |

## Selected Question(s)

1. **C1 — Marketplace schema-fit.** Highest reach (brand-new entity quadrant), clear
   builder lens (does the commerce-shaped schema carry two-sided marketplace economics),
   store-only and autonomous-safe, and it advances the live generalizability arc to its
   last blank cell while sharpening run-035's subtractive-gate finding on a new shape.
   C4/C5 are the natural bounded-live follow-ups *if* C1 confirms the on-site gap.

## Selected Run Contract

```yaml
selected_question: "Across the store's 5 marketplace/commission entities (airbnb, etsy, doordash, uber, upwork), does the universal offering_category / business_model / price-visibility frame express what a reader needs about a two-sided platform — take rate, GMV, supply vs demand side — or is it a run-035-style gap where the industry holds the entity but the schema cannot carry its economics?"
selected_slug: marketplace-schema-fit
run_type: system-test
question_mode: calibration
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "The 5 store profiles with business_model: Marketplace / Commission (airbnb-com, etsy-com, doordash-com, uber-com, upwork-com). Verify the set in Loop 1; treat as the full marketplace cohort in the store, not a sample of a larger known set."
likely_source_panel: "store/<domain>/profile.md frontmatter + prose for all 5; SCHEMA.md / TAXONOMIES.md for the business_model closed set + offering_category list. No external sources."
builder_lens: "Schema-fit / persistence boundary: tests whether the universal commerce schema's offering_category + business_model + price-visibility surface carries the two-sided marketplace entity shape, or produces a finance-035-style positive-shape gap (entity gated correctly but no field set for take rate / GMV / supply-vs-demand side)."
reach_reason: "Reaches the one entity shape (two-sided marketplace) untested across all 36 prior runs; the generalizability arc has hit subscription, transactional-luxury, and investor shapes but never commission/platform."
allowed_sources:
  - "store/ (the 5 marketplace profiles + any offerings.md / signals they carry)"
  - "SCHEMA.md, TAXONOMIES.md (the contract for business_model + offering_category)"
  - "experiments/00-market-read-lab/learning/ (context only)"
disallowed_actions:
  - "No external/live browsing, no Firecrawl, no scrape, no SERP."
  - "No store/ mutation or write-back."
  - "No durable primitive creation or schema edit; this is a read, not a build."
  - "No lesson proposal or graduation."
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from 5 already-captured local profiles + the local schema contract. No spend, no live evidence, no write-back."
loop1_failure_mode: "Two-stacked-absence confusion (run-035 S1): reporting 'the schema can't express take rate / GMV' when the real cause is that the marketing site the store captured never showed it (schema-can't vs firm-didn't-on-site). The cohort is large public companies whose economics live in 10-Ks, so an empty economics surface must be split into the two causes, and absence stated as 'not captured', not 'not disclosed anywhere'. Secondary trap: overclaiming a market verdict from n=5 — this is a schema-fit read, not a marketplace-market claim."
```

## Selection Notes

C1 selected over C2 (lower novelty — 033 already mapped the price-visibility axis on
makers) and C3/C6 (too broad / meta, weaker reader grounding). C4 and C5 are the
bounded-live follow-ups C1 sets up but does not require: C1 first establishes store-only
whether the gap exists and which side of the run-035 schema-can't / firm-didn't line it
falls on, before any source-panel spend. Rejected re-running finance (run-035 explicitly
parks it pending a less VC-skewed cohort or a real consumer) as a parked next step.
