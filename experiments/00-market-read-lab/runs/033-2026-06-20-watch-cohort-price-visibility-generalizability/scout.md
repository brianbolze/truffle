# Scout

## Prior Context Read

- `question_history.py`: 32 prior runs. Heavy telehealth-internal coverage (price/positioning/offer/access/backend/trust/geo/ownership). Cross-vertical reached only twice: 027 (classification audit, not a market read) and 028 (SaaS price-visibility market read). Last three runs (029 traction-readiness, 031 confidence-grain, 032 freshness-grain) are a **store-meta-calibration trilogy** — a 4th meta read in a row would be fatigue, not reach.
- `scout-context.md`: select for value + reach + roadmap learning, not store-answerability; gap-probes first-class; name the builder lens for any pure value-read.
- `triage.md` (post-candidate check): MRL-002 (read-recipe family) is the dominant standing pressure — the price-visibility recipe is its most-reused member (008/013/023 telehealth, 028 SaaS). MRL-002's run-028 entry split the recipe into enum-grep / prose-read / structured-token and found the **structured price-visibility token does not generalize off telehealth (3/24 on SaaS)** — a known trap any cross-vertical price read must avoid. MRL-008 run-028 branch: an empty *structured* surface is a coverage signal, not a market fact.
- Last 3 `run-notes.md`: 032 next-run advice explicitly nominates the **offerings-roster-completeness** runner-up as untested (candidate D below). 031/032 both warn against reading a present-but-unevenly-formatted field as uniformly greppable (parse-hazard recurrence).
- Store composition (verified this scout): 139 dirs; `primary_industry` = Healthcare 68, Technology 24, Finance 9, Consumer Goods 6, Consulting 6, Energy 5, Sports 3, Automotive 3, Retail 2, Industrial 2, + singletons. A coherent **luxury/fashion-watch micro-cohort** exists: rolex, patek, audemarspiguet, alange-soehne, cartier (luxury) + swatch, casio (accessible).

## Candidate Questions

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **A. Across the captured watch brands (Rolex, Patek, AP, A. Lange, Cartier, Swatch, Casio), how does each present and price its catalog online — and does the lab's "can I get a price?" axis (published / partial / gated) still mean the same thing for physical luxury goods, where gating is dealer/scarcity convention rather than sales-intake?** | calibration (value-read body) | yes | store-only | A real reader (luxury/retail analyst) recognizes the field; surfaces a stark, true split (luxury = "price on request" boutique-gated; Swatch/Casio = full e-commerce inline prices). | Tests whether the price-visibility recipe — the MRL-002 family's most-reused member — generalizes to a **third vertical** with a *different gating mechanism* than telehealth-intake or SaaS-enterprise-quote. | Reaches off the design vertical onto physical goods; probes whether "published/partial/gated" is one axis or three vertical-specific axes; tests where the gate's *meaning* changes (scarcity vs sales). | profile.md prose + `business_model`/`portfolio_shape` per brand; the explicit "no public price" site_notes lines already captured for the 4 luxury maisons. | Forcing the telehealth "intake-gate" frame onto a luxury convention; reading "no price published" as a coverage gap rather than a deliberate market posture. |
| B. Cross-**industry** price-visibility composition: run the 3-value "can I get a price?" axis across ALL verticals at once (telehealth + SaaS + watches + finance) — does it compose into one corpus-wide cut, or do verticals need different price semantics? | calibration | yes | store-only | Directly tests the engine's "universal fields + reusable cuts" claim at market-read grain. | Cross-vertical cut composition. | Whole-corpus reach. | per-vertical price surfaces; `business_model`. | Too abstract / thin per-vertical n; overlaps 028; the structured token trap (3/24). Candidate A is the sharper, reader-recognizable instance of this. |
| C. Across the Finance/VC slice (blueowl, sequoiacap, firstround, lsvp, thrive, runway, stripe, spero, standish), what does each actually *sell/charge for*, and can the store's company-keyed schema describe a fund/holding the way it describes a DTC brand? | value-read | yes | store-only | Reader value (who are these, what's the product); tests schema fit on non-product entities. | entity-type / schema-edge for funds & holding cos. | Reaches the `Investor / Holding` entity_type edge. | profile.md + entity_type frontmatter. | "Product/price" framing is category-error for a VC fund (the LP/GP model isn't a consumer offer) — risk of forcing it. Overlaps 027's classification audit. |
| D. Across the captured store, can a downstream reader tell whether a company's `offerings.md` roster is **comprehensive vs partial** — does the store self-describe roster completeness, or is a thin roster indistinguishable from a fully-captured small catalog? | calibration | yes | store-only | Runner-up nominated by run 032; "build on top / compare a field" value jobs depend on rosters being trustworthy-complete. | completeness-grain / depth-backfill — the store's self-description of catalog coverage. | Probes whether thin = small or thin = under-captured. | offerings.md presence + `portfolio_shape` + capture-method notes across slices. | Would be the **4th meta-calibration run in a row** (029/031/032) — fatigue; lower reader reach than a real market read. |
| E. Across the SaaS/Tech slice, which brands publish a self-serve/PLG motion vs sales-led, and does GTM motion predict price visibility? | value-read | yes | store-only | Reader value for a GTM analyst. | recipe re-use. | low reach. | prose + business_model. | Near-duplicate of run 028; explicitly recently covered — reject as repeat. |

## Selected Question(s)

1. **Candidate A** — the watch-cohort price-visibility & presentation read.

Runner-up: **D** (offerings-roster completeness) if a meta-calibration is preferred over a fresh-vertical market read.

Rationale: A wins on all three scout tests. **Value/reach:** a reader-recognizable market read on a vertical the lab has *never* read as a market (027 only audited classification), with a stark true finding already visible in capture (4 luxury maisons publish no price by convention; Swatch/Casio publish everything). **Design:** it pressures the MRL-002 price-visibility recipe — the lab's single most-reused read — at a genuinely new frontier: a *third* gating mechanism (dealer/scarcity) distinct from telehealth-intake and SaaS-enterprise-quote, calibrating whether "published/partial/gated" is one universal axis or vertical-specific. **Repeat justification:** it is a *calibration* repeat of the price-visibility shape onto a maximally different vertical, exactly the recurrence scout-context endorses ("calibrates whether an earlier store-only answer was a coverage artifact"). It also breaks the 3-run meta-calibration streak with an actual market read. E is rejected as a near-duplicate of 028; B is the abstract version of A; C and D are viable but lower reach / fatigue-risk.

## Selected Run Contract

```yaml
selected_question: "Across the captured watch brands (Rolex, Patek Philippe, Audemars Piguet, A. Lange & Söhne, Cartier, Swatch, Casio), how does each present and price its catalog online, and does the lab's published/partial/gated price-visibility axis still mean the same thing for physical luxury goods — where access is gated by dealer/boutique/scarcity convention rather than by sales-intake?"
selected_slug: watch-cohort-price-visibility-generalizability
run_type: market
question_mode: calibration
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Captured companies with primary_industry: Consumer Goods (luxury/fashion watches: rolex, patek, audemarspiguet, alange-soehne, cartier, swatch) plus casio (primary_industry: Technology but a watch-catalog brand). ~7 brands. Name the cartier edge (watches request-appointment; only jewelry/fragrance priced) and the swatch/casio accessible-tier boundary explicitly."
likely_source_panel: "store-only: each brand's store/<domain>/profile.md (Overview, What they offer, site_notes, business_model, portfolio_shape, price prose). alange-soehne also has visual.md."
builder_lens: "Tests whether the price-visibility recipe (MRL-002's most-reused member) generalizes to a third vertical with a dealer/scarcity gating mechanism; calibrates whether published/partial/gated is one universal axis or needs a vertical-aware gate-type reading. Also tests the run-028 finding that the structured price-visibility token does not populate off telehealth."
reach_reason: "First market read (not classification audit) on the Consumer Goods vertical; pushes the lab's most-reused axis onto physical luxury goods where 'no price' is a deliberate posture, not a coverage gap or an intake gate."
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/ (prior runs, triage, discovery-ledger as evidence only)"
disallowed_actions:
  - "No live browsing, Firecrawl, or external search."
  - "No store/ mutation or write-back."
  - "No durable primitive / category object creation."
  - "No triage graduation."
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from already-captured local store files and lab artifacts; store-only; no spend, no write-back, no live evidence."
loop1_failure_mode: "Forcing the telehealth intake-gate frame onto a luxury dealer/scarcity convention; reading 'no public price' as a coverage gap rather than a market posture (must say 'not found / not published by convention', not 'not captured' and not 'we failed to capture'); and re-checking the run-028 trap — do NOT claim the structured price-visibility token works here (it is near-empty off telehealth)."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. Candidate A is a calibration read whose body delivers genuine reader value (a real watch-market price-presentation map) — the calibration is *how it generalizes the recipe*, not the only payload. The Loop 1 read should produce both: (1) the brand-by-brand presentation/price map a reader wants, and (2) the recipe-generalization verdict (does published/partial/gated compose, and what does the luxury "gate" actually mean).
