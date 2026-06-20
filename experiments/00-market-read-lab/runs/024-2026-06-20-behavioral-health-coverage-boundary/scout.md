# Scout

## Prior Context Read

- `triage.md`: MRL-002 (read-recipe family, Acknowledged P1) now spans 8+ store-only
  surfaces, all landing `query-time-grouping-enough`. MRL-001 (denominator, Acknowledged
  P2) has a now-*live-confirmed* selection-bias flavor (run 022): some whitespace is
  invisible to every store-only query and needs outside evidence/capture. MRL-009 holds a
  tiered women's-menopause capture worklist (human-gated). MRL-005/006 backend-relation
  graduation clock is met but human-gated. MRL-010 reviews/forums bodies at 3 sightings,
  graduation-decision-ready, human-gated.
- `scout-context.md`: pick for reader value + reach + source-family diversity; do NOT
  optimize for store-answerability; gap-probes are first-class with a bounded plan; repeat
  a recent shape only when it tests a materially different cohort boundary / source family.
- Last 3 `run-notes.md` (021, 022, 023): **loud, convergent next-run advice** — store-only
  telehealth cohort cuts are *saturated* (021 = "17th run to land on
  `query-time-grouping-enough`; marginal design return is low"). The two named under-tested
  directions: (a) **generalization beyond telehealth's core lane**, which for real depth
  needs a capture-first run [NOT autonomous — Firecrawl spend]; (b) **bounded-live external
  corroboration** [autonomous under the standing `live_evidence_plan`]. 022 explicitly:
  "a second bounded-live whitespace category would extend the coverage-radar recipe's
  evidence."
- Current run artifacts: fresh scaffold (024), temporary slug `scout-candidates`.

Grounding probe (cheap, store-only, for candidate honesty): 54 `telehealth.md` packs;
**0** anchored to mental/behavioral/psychiatry; `anchor_category` distribution is
GLP-1 / TRT / longevity-NAD / sexual-health / peptides / hair / labs / primary-care /
womens-HRT / multi-none. The captured corpus boundary is plainly **Rx-commerce /
metabolic / hormone-shaped**, with no behavioral-health-anchored brand.

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|
| C1. Does a dedicated **behavioral / mental-health telehealth** segment exist (online therapy + psychiatry + Rx) that the captured telehealth corpus has *not* captured, and where does the corpus's membership boundary actually fall (Rx-commerce/hormone lane vs behavioral lane)? | gap-probe (boundary-calibration) | yes | bounded-live | Produces a named capture worklist for a major adjacent segment **and** maps the outer edge of what "telehealth" means in this store — a different *lane*, not another within-lane category. 3rd sighting of the coverage-radar recipe on a maximally-different vertical. | Reaches past the store's comfortable hormone/GLP-1 core into a lane it appears not to cover at all; tests the membership/boundary design uncertainty head-on. | ≥2 authoritative "best online therapy/psychiatry 2026" listicles → verbatim named sets → cross-source intersection → store token-diff; capture dates + affiliate-disclosure flags. | Reading 2 affiliate listicles as a census; conflating "not in store by token match" with "doesn't exist"; concluding "behavioral health isn't telehealth" rather than "this corpus wasn't built to cover it." |
| C2. Coverage-radar on **dermatology / skincare Rx telehealth** (Curology, Apostrophe, Dermatica, Agency, Nurx-derm): which named brands recur across authoritative listicles, and how many are store-absent? | gap-probe | yes | bounded-live | Tests the recipe on a segment *inside* the store's Rx-commerce lane (partial overlap: hims/hers/ro/nurx do derm) → a more interesting present/absent diff than a near-disjoint boundary. | Within-lane whitespace; less of a reach than C1 (derm is hormone-adjacent Rx-commerce). | Same coverage-radar panel as C1. | Same affiliate/census trap; derm overlaps existing brands, so token-match false-negatives are likelier. |
| C3. Coverage-radar on **fertility / reproductive telehealth** (Kindbody, Maven, Ro-fertility, Legacy, Carrot): who exists, who's store-absent? | gap-probe | yes | bounded-live | Another whitespace worklist; fertility is a distinct buyer/segment. | Adjacent women's/repro lane; partially overlaps run 022's menopause finding. | Same panel. | Overlaps 022's women's-segment finding — risk of near-repeat rather than a new boundary. |
| C4. Across the captured GLP-1 cohort, does the **first-month promo vs steady-state price** gap (run 023's promo confound) shift if re-read against current owned pricing pages? | calibration | no | bounded-live (deep owned-page reads) | Would test promo decay over time. | Freshness of captured pricing. | Owned-page deep reads across ~19 brands — broad, sprawl-prone. | Exceeds a *light* bounded plan; drifts into pricing-depth crawl (022's stated failure mode). **Reject: too broad for the standing light plan.** |
| C5. Store-only: cut the corpus by **`pay_model` × `compounding_posture`** to map cash-pay vs insurance vs compounded lanes. | value-read | yes | store-only | Clean enum cross-tab. | Nothing new — 9th+ store-only enum cut. | Store grep only. | **Reject: saturated.** Run 021 explicitly flags marginal return on another store-only cohort cut as low. |
| C6. Store-only calibration: across the corpus, what fraction of `Price (verbatim)` cells are **promo-framed / point-in-time** (extending run 023's 8/19 finding corpus-wide)? | calibration | yes | store-only | Quantifies a real freshness/confound risk corpus-wide. | Freshness boundary, but store-only. | Store grep + manual promo classification. | Another store-only cut; lower reach than C1. Useful but redundant with the saturation signal. |
| C7. **Men's-side mirror** of run 022: does an authoritative "best men's-health / TRT telehealth 2026" listicle panel name brands the (already men's-heavy) store is *missing* — i.e., is the men's cohort over- or under-covered vs market? | gap-probe (calibration) | yes | bounded-live | Calibrates whether the store's known men's-hormone over-representation is *complete* coverage or just *dense* coverage. | Tests the *other* side of run 020/022's selection-bias asymmetry. | Same coverage-radar panel. | Store is dense here, so the diff may be ~empty (low yield); affiliate tail noise. |

## Selected Question(s)

1. **C1 — behavioral/mental-health telehealth boundary coverage-radar (bounded-live).**
   Recommended. It is the highest-reach autonomous-safe candidate: it follows the loud
   saturation signal away from store-only cuts, uses the sanctioned bounded-live recipe,
   and — unlike a 3rd within-lane whitespace (C2/C3) — probes a genuinely *different lane*,
   so it tests both the recipe's generalization and the corpus's outer membership boundary.
   Secondary: **C2 (derm)** if a within-lane partial-overlap diff is preferred over a
   boundary probe.

These are Scout recommendations until Brian or the operator confirms one.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: >-
  Does a dedicated behavioral / mental-health telehealth segment (online therapy +
  psychiatry + behavioral Rx) exist that the captured telehealth corpus has not captured,
  and where does the corpus's membership boundary actually fall — Rx-commerce/hormone lane
  vs behavioral-health lane? Produce a tiered capture-candidate worklist and a clear
  store-vs-market boundary statement.
selected_slug: behavioral-health-coverage-boundary
run_type: mixed
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: bounded-live
expected_denominator: >-
  Store side: 54 telehealth.md packs, 0 anchored to mental/behavioral/psychiatry (grep
  floor; treat as floor, not census — a behavioral line could exist inside a multi/none
  brand). Market side: the cross-source-recurrence head of >=2 authoritative
  "best online therapy / psychiatry telehealth 2026" listicles.
likely_source_panel: >-
  2 firecrawl_search queries (best online therapy 2026; best online psychiatry / mental-
  health telehealth 2026) to surface authoritative listicles, then JSON-scrape >=2
  authoritative listicles for verbatim named brand sets; cross-source intersection;
  token-match diff against store/*/.
reach_reason: >-
  Reaches past the store's hormone/GLP-1/Rx-commerce core into a behavioral-health lane
  the corpus appears not to cover at all, directly probing the boundary/membership design
  uncertainty rather than re-grouping already-captured State. Gives the bounded-live
  coverage-radar recipe its 3rd sighting on a maximally different vertical.
allowed_sources:
  - store/ (token-match diff + telehealth.md anchor grep; floor only)
  - experiments/00-market-read-lab/triage.md
  - "bounded-live source families from live_evidence_plan below"
disallowed_actions:
  - write-back to store/
  - code/schema/template changes
  - durable primitive / taxonomy-value creation
  - triage graduation
  - Firecrawl crawl or owned-page pricing/offer-depth reads (membership read only)
live_evidence_plan:
  approved_by: Brian
  approval_scope: autonomous Market Read Lab runs (standing bounded-live policy; runs 011/012/022 precedent)
  budget_class: light
  review_after: "this is the 4th bounded-live run (011/012/022 were the first 3, reviewed at the run-022 checkpoint)"
  evidence_goal: >-
    Determine whether a dedicated behavioral/mental-health telehealth segment exists that
    the store has not captured, and map where the captured telehealth corpus's membership
    boundary falls. Output: a tiered capture-candidate worklist + a store-vs-market
    boundary statement. Membership read only — no pricing/offer/quality depth.
  source_families_allowed: [SERP/listicle, owned/official brand pages (light, identity-confirm only), reviews/forums (light)]
  source_families_preferred: ["authoritative 'best online therapy / psychiatry / mental-health telehealth 2026' listicles", owned brand front-door pages]
  source_families_disallowed: [login-only/paywalled, broad crawling, private data, ad/social scraping, owned-page pricing/offer-depth reads]
  stop_when:
    - ">=2 authoritative listicles yield a cross-recurrence named set and the store diff is computable with caveats"
    - the next source would expand the question (pricing/offer/quality depth) rather than verify membership
    - remaining uncertainty is a framing judgment, not a sourcing gap
  disallowed_actions: [write-back to store/, code/schema/template changes, durable primitive creation, triage graduation]
approval_needed: no
why_autonomous_safe: >-
  Standing bounded-live policy (runs 011/012/022 precedent); light source panel only
  (a few searches + ~2 JSON scrapes + a grep); membership read, no pricing/offer depth;
  no write-back, no store mutation, no durable primitive. Stop rule fires once the
  store-vs-market diff is computable.
loop1_failure_mode: >-
  Broadening from a membership coverage-radar into open-ended browsing or owned-page
  pricing/offer depth; reading 2 affiliate listicles as a market census; conflating
  "not found by token match" with "does not exist"; over-reading a near-disjoint result
  as "behavioral health isn't telehealth" rather than "this corpus wasn't built to cover
  it."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. This run deliberately follows the
saturation signal (runs 021/022/023) away from store-only telehealth cuts and toward the
sanctioned autonomous direction (bounded-live external corroboration), but sharpens it
from "another whitespace category" into a **boundary probe**: C1 tests a different *lane*,
not another within-lane category, so a 3rd coverage-radar sighting earns its keep by
testing recipe generalization *and* mapping the corpus's outer membership edge. The
within-lane alternatives (C2 derm, C3 fertility) are held as the secondary slate; the
pure store-only cuts (C5/C6) are recorded but rejected as saturated per run 021's explicit
marginal-return note; C4 is rejected as too broad for the standing *light* plan.
