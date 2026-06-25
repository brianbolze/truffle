# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue):
  L005 (query-time grouping enough only when corpus carries the cut), L006 (proposed — price-visibility
  token reports buyer-reachability, not what an intermediary charges; wants a 2nd/3rd entity-type sighting).
  Observations 036–043 are dominated by the `schema-edge-entity-type` lens (does the universal schema fit
  marketplaces / wearables / deep-tech / SaaS / finance) and the recurring `denominator-reconciliation`
  finding (industry draw ≠ entity-shape cohort, n=4). Two price-*incomparability* sightings already exist:
  run-023 (GLP-1 per-month vs per-dose vs membership-inclusive) and run-043 S2 (wearable year-one TCO unit
  non-uniformity). Both stayed `query-time-grouping-enough` / no-new-primitive.
- `scout-context.md`: select for value + reach + roadmap learning, source-family diversity, calibration
  against blind spots; do not optimize for store-answerability; name the builder lens for any value-read.
- Last 3 `run-notes.md` files (041 state-change-pulse, 042 deep-tech maturity, 043 wearable TCO): all
  store-only; 042/043 found *positive* store strengths (maturity legible from prose; buyer TCO assemblable),
  breaking the earlier "lands on builder not buyer" CR1 streak. 041 mapped the captures/ diff substrate gap.
- Current run artifacts, if resuming: fresh scaffold (044), no prior scout.md.

**Deliberate diversification:** runs 036–042 over-index on "does the universal *schema* fit entity-shape X."
This slate favors candidates with a different builder lens (pricing-grain, relations, confidence, freshness)
and a concrete external reader, while staying store-only and autonomous-safe.

## Candidate Questions

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **C1 (lead).** For a developer/CTO comparing usage-based dev-infra tools (Datadog, Snowflake, Stripe, Twilio, PostHog, AWS), can the store let a buyer actually *compare cost*, or do the metered units (per-host vs per-credit vs per-event vs %-of-volume vs per-message) defeat apples-to-apples even with verbatim pricing present? | value-read | yes | store-only | Real buyer (infra spend), under-priced cohort; extends price-incomparability to a **3rd pricing shape** after GLP-1 (023) and wearable TCO (043). | Price-comparability grain on **consumption/usage** pricing; does verbatim pricing + the price-visibility token support a metered-tool comparison, or is unit-incommensurability the ceiling? `business_model: Usage-based` as a cohort key (positive-key contrast to run-039 SaaS collapse). | Whether the store's pricing convention generalizes to metered B2B, and whether the token convention is even *present* on these (mostly pre-2.3) captures. | Verbatim metered rates per profile (have: datadog $15/host, $0.10/GB; stripe %); token presence/absence per offering line; capture clocks. | Calling tools "comparable" when units are incommensurable; treating a missing token as `[published]` (it = predates-convention). |
| C2. For a founder choosing which captured investor/VC firm to approach (firstround, lsvp, sequoiacap, spero-vc, thrivecap, blueowl, bullish, heco), can the store differentiate them on the founder's deciding axes — stage focus, sector thesis, check/fund size, portfolio — or do they collapse to one "VC firm" bucket? | calibration | yes | store-only | Real reader (founder); calibrates L005 on the capital-allocator slice run-035 flagged as the axis-breaking case, on a **new field family** (selection-differentiation, not fee posture). | Does the universal schema carry investor-*differentiating* State, or is the slice flattened? Confidence/membership lens. | Whether L005's "corpus carries the cut" holds for investors; whether differentiation lives in prose. | Per-firm stage/sector/check-size/portfolio lines from profile bodies. | Re-running run-035 (fee posture) under a new label; thin differentiation read. |
| C3. In the primary-/general-care telehealth cohort (onemedical, sesamecare, ro, hims, lifemd, eden-health), what care model does each use — membership vs visit-fee vs insurance, async vs synchronous, employed-clinician vs provider-marketplace? | value-read | yes | store-only | Buyer/strategist field comparison in a vertical the lab hasn't cut by *care model*. | Structure lens: does the store separate care-delivery models, or only product/price? | Whether care-model is a legible cut or prose-only. | Per-brand care-model lines. | Resembles 013 (sexual-health access models) / 025 (geography); risk of re-tread. |
| C4. Across profiles that reference the **same** third entity (shared parent, acquirer, backend pharmacy, named competitor), do the two captures *agree*? | gap-probe | yes | store-only | Extends run-039 G3 (Coda ownership chain disagreed with itself) into a store-wide consistency probe. | Relation/provenance lens: cross-profile reconciliation of shared edges. | Whether the store silently disagrees with itself on shared entities. | Pairs of profiles naming the same entity; the conflicting lines. | Few enough shared edges that n is tiny; could collapse to run-039 G3 alone. |
| C5. In a trust-critical vertical (compounded Rx or longevity), what *credibility* signals does each brand present (named medical director, advisors, licensure/accreditation, lab partners), and can a skeptical buyer compare trustworthiness from State? | value-read | yes | store-only | Buyer trust comparison. | Confidence/proof lens. | Whether credibility is a comparable cut. | Per-brand credibility lines. | Overlaps run-021 (trust proof devices); re-tread risk. |
| C6. For the captured DTC eyewear/apparel/consumer-goods entities, can the store support a buyer comparison? | value-read | yes | store-only | — | — | — | — | **Reject: n too small** (warbyparker ~n=1; nike apparel-adjacent). Not a cohort. |
| C7. Across the captured store, which profiles' market-sensitive State is at highest staleness risk for a buyer, judged by capture clock + price volatility flags? | calibration | yes | store-only | Freshness buyer-risk. | Freshness lens. | — | — | **Reject: near-duplicate of run-032/run-043 S3**; little new. |

## Selected Question(s)

1. **C1 — usage-based dev-infra pricing comparability.** Strongest balance of real reader value (a CTO/developer
   comparing metered infra spend), reach (a 3rd pricing-shape after 023/043, an under-priced cohort), a fresh
   builder lens (price-comparability grain on consumption pricing + token-convention presence), and a clean
   store-only autonomous boundary. Positive cohort-key candidate (`business_model: Usage-based` recovers the
   slice) gives a useful contrast to run-039's SaaS-collapse.
2. (Runner-up) **C2 — investor-selection differentiation** — good calibration of L005 on the capital-allocator
   slice, but adjacent enough to run-035 that C1 wins on freshness and reader value.

## Selected Run Contract

```yaml
selected_question: "For a developer/CTO comparing usage-based dev-infrastructure tools (Datadog, Snowflake, Stripe, Twilio, PostHog, AWS), can Truffle's captured State let a buyer actually compare cost, or do the incommensurable metered units (per-host vs per-credit vs per-event vs %-of-volume vs per-message) defeat an apples-to-apples comparison even when verbatim pricing is present — and is the price-visibility token convention even present across these mostly pre-2.3 captures?"
selected_slug: usage-based-pricing-comparability
run_type: mixed
question_mode: value-read
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Store companies with business_model: Usage-based / Consumption that are dev-infra / B2B software — core cohort datadoghq, snowflake, stripe, twilio, posthog, aws (blueenergy + waldo are non-infra and excluded with reason). Subscription-priced dev tools (cloudflare, openai, notion, linear, airtable) available as contrast foils. Treat the cohort list as partial until grep-confirmed."
likely_source_panel: "store/<domain>/profile.md only — business_model + offering_category + primary_industry frontmatter, the 'What they offer' verbatim pricing lines and price-visibility tokens, site_notes / unverified_fields. No external sources."
builder_lens: "Price-comparability grain on consumption/usage pricing: whether verbatim metered pricing + the per-offering price-visibility token let a buyer compare metered B2B tools, or whether unit-incommensurability is the ceiling (3rd pricing-shape after run-023 GLP-1, run-043 wearable TCO). Secondary: is business_model: Usage-based a clean cohort key (positive-key contrast to run-039), and is the token convention present on pre-2.3 captures or absent (a backfill/coverage caveat, not [published])."
reach_reason: "Prices a cohort the lab has never priced and a pricing shape (metered B2B infra) distinct from the two prior price-incomparability sightings; tests whether the store's pricing convention generalizes off the DTC/telehealth substrate it was built on."
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/learning/"
  - "SCHEMA.md / TAXONOMIES.md (contract reference only)"
disallowed_actions:
  - "No live browsing, WebSearch, Firecrawl, or any paid capture."
  - "No store/ mutation, write-back, or durable primitive creation."
  - "No learning/lessons.md, brian.md, or passes/ writes."
  - "No treating a missing price-visibility token as [published]."
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Fully answerable from local store/profile.md files and existing lab artifacts; no external evidence, no spend, no write-back."
loop1_failure_mode: "Overclaiming comparability by normalizing incommensurable metered units into a false single-number ranking; or misreading absent price-visibility tokens (pre-2.3 captures) as published pricing rather than a convention-coverage gap."
```

## Selection Notes

C1 deliberately steps off the `schema-edge-entity-type` lens that dominated runs 036–042 and instead presses
the **pricing-comparability grain** — a lens last touched at run-023 and run-043 S2, now on a third, B2B-metered
pricing shape and a cohort the lab has never priced. It is a value-read with a named builder lens (not a pure
reader-value pick), and it carries two live design hooks: (a) whether `business_model: Usage-based` is a clean
positive cohort key (contrast run-039's SaaS-collapse), and (b) whether the price-visibility token convention is
even present on the (mostly pre-2.3) dev-infra captures — a coverage/backfill calibration. Store-only and
autonomous-safe. Runner-up C2 calibrates L005 on investors but reads as adjacent to run-035; held as the next
candidate, not selected.
