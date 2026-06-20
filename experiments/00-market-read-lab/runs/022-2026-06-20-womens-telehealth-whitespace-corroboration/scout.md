# Scout

## Prior Context Read

- `triage.md`: 11 live items. The query-recipe (MRL-002) and denominator (MRL-001)
  items are the most-reinforced; MRL-001 just gained a **selection-bias denominator**
  flavor from run 020 (the captured cohort is non-representative *before* any grep, a
  bias no query-time fix touches). MRL-010 (reviews/forum bodies) crossed its
  third-sighting bar at run 011 and is graduation-decision-ready. Bounded-live source
  panels (MRL-001/012) are the named way to convert a store-bounded hypothesis into a
  market finding.
- `scout-context.md`: two-test selection (value + design). Prefer questions where
  Truffle's cited ingredients beat generic Claude+web AND the run teaches a design
  decision. Bounded-live is for a small public source panel that materially improves the
  read; needs a filled `live_evidence_plan`, `budget_class: light`.
- Last 3 `run-notes.md` files (019/020/021): **all store-only, all landed on
  `query-time-grouping-enough`.** Run 021 (proof devices) is the **17th** store-only
  cohort cut to land there and says explicitly: *"the signal is saturated; the marginal
  design return on another telehealth cohort cut is low. Bias the next Scout toward the
  genuinely under-tested directions: generalization beyond telehealth (needs a
  capture-first run), or external-corroboration `bounded-live`."* Run 020 (audience
  whitespace) names the specific high-value variant: a **bounded-live women's-telehealth
  listicle panel** to test whether the dedicated-women's-hormone/longevity whitespace is
  *real market* or just *store-absent*.
- Current run artifacts: temporary scaffold `022-…-scout-candidates`, Scout-only.

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| **C1 (RECOMMENDED).** Does the women's-hormone/menopause/longevity telehealth market contain dedicated women-anchored brands the store simply hasn't captured (selection bias) — or is supply genuinely thin? Test run 020's store-bounded 15-vs-5 men/women asymmetry against a small external named-set panel. | market | **yes** | **bounded-live** | First run to *convert* a store-bounded hypothesis (run 020) into a market-grounded read; directly tests MRL-001's selection-bias flavor and matures the bounded-live recipe (3rd bounded-live run = the `review_after: 3` checkpoint). | ≥2 authoritative "best women's telehealth / menopause 2026" listicles for the named set + owned brand pages to confirm audience positioning; cross-source recurrence as the inclusion bar (run-012 method). | Reading a listicle named-set as a "complete market"; over-claiming store gaps as market whitespace; affiliate/SEO confound (run 012). |
| C2. Which GLP-1 telehealth brands do "best of 2026" listicles/SERPs name now, and has the named set drifted since run 012 (one day prior)? | market | yes | bounded-live | Tests listicle-panel *freshness*/drift. | ≥2 authoritative listicles, dated. | Recurrence too soon — run 012 was yesterday; near-zero drift expected. Low marginal value. |
| C3. Generalize the State-read recipe beyond telehealth: cut a non-telehealth store cohort (e.g. the captured luxury/SaaS/aerospace domains) the same way. | market/system-test | **no** | live-external-needs-approval | Would test whether the MRL-002 recipe family is telehealth-specific. | A second cohort with real captured depth — the store's non-telehealth domains are singletons, so this needs a **capture-first** Firecrawl campaign. | Not autonomous-safe: needs unplanned Firecrawl spend + new captures. Flag for human-gated capture-first run. |
| C4. Compounded-semaglutide supply disruption pulse: which captured GLP-1 brands have publicly changed their compounded offering since the FDA compounding wind-down? | market | **no** | live-external-needs-approval | High reader value (a real change-pulse on a live policy event). | Primary owned/regulatory/manufacturer pages, dated; broad multi-brand sweep. | Source panel is broad/unclear + current-policy claims → sprawl risk; this is MRL-007 (category-level exogenous signal) territory. Needs a bounded plan or approval first. |
| C5. Spot-check the State/Judgment boundary run 021 drew: do a sample of brands' captured LegitScript / pharmacy-accreditation claims actually resolve on the issuing registry? | system-test | yes | bounded-live | Empirically tests whether device-*presence* (State) tracks device-*credibility* (Judgment) — the load-bearing caveat of run 021. | legitscript.com / PCAB-ACHC-NABP registry lookups for a small sample. | Narrow, verification-flavored; modest reader value; a few mismatches don't generalize. |
| C6. Best men's-health/TRT 2026 leaderboard vs the store's (heavy) men's coverage: does the external named set match, validating the store is *complete on its strong side*? | market | yes | bounded-live | Complement to C1 on the over-represented side — tests the selection-bias story from both ends. | ≥2 authoritative men's-TRT listicles + cross-source recurrence. | Less whitespace-interesting than C1 (store is already dense here); confirmatory, not discovery. |
| C7. Another store-only cross-cohort cut (e.g. proof-device presence × price-visibility correlation). | market | yes | store-only | — | store frontmatter only. | **Reject:** would be the 18th store-only cut to land on `query-time-grouping-enough`. Saturated; near-zero marginal design return per runs 020/021. |

## Selected Question(s)

1. **C1 — Women's-hormone/menopause/longevity telehealth whitespace, store vs market
   (bounded-live).** Recommended. It is the explicit run-020 next-step, the
   highest-value autonomous-safe direction given store-only saturation, and it closes a
   real design loop (does an external panel convert MRL-001's selection-bias hypothesis
   into a finding?).

Secondary if C1 is declined: **C6** (men's-side confirmatory leaderboard, same
machinery, lower discovery value).

These are Scout recommendations until Brian or the operator confirms one.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: >-
  Does the women's-hormone / menopause / longevity telehealth market contain dedicated
  women-anchored brands the captured store simply hasn't captured (selection bias), or is
  dedicated women-anchored supply genuinely thin? Build a small external named-set panel
  ("best women's telehealth / menopause / hormone 2026" listicles + owned brand pages),
  apply a cross-source-recurrence inclusion bar, and reconcile it against the store's
  women-leaning cohort (run 020's 5 women-leaning brands of 54) to test whether run 020's
  15-vs-5 men/women lean asymmetry is store selection-bias or a market signal.
selected_slug: womens-telehealth-whitespace-corroboration
run_type: market
autonomous_eligible: yes
evidence_mode: bounded-live
expected_denominator: >-
  Store side: the women-leaning brands among the 54 captured telehealth packs (run 020
  found 5, with GLP-1 drawing 3 of them) — treat as a floor (MRL-001 anchored-only +
  selection-bias). Market side: a cross-source-recurrence named set from >=2 authoritative
  "best women's telehealth / menopause / hormone 2026" listicles — a coverage radar, NOT a
  complete market (run-012 finding). The deliverable is the symmetric diff: market-named
  brands absent from the store (capture candidates) vs store brands absent from the panel.
likely_source_panel: >-
  >=2 authoritative third-party listicles (e.g. health/consumer press "best women's
  telehealth / menopause 2026"); owned/official brand pages to confirm audience positioning,
  category, and offer for each market-named brand; optional light reviews/forum triangulation
  only if a brand's audience framing is ambiguous.
allowed_sources:
  - store/ (women-leaning cohort + any market-named brand already captured)
  - experiments/00-market-read-lab/ (triage, prior run-notes as evidence)
  - approved bounded-live source families from live_evidence_plan (listicles/SERP, owned pages, light reviews)
disallowed_actions:
  - write-back to store/ or any project KB
  - Firecrawl crawl or speculative paid capture beyond light, load-bearing single-page captures
  - durable primitive creation (no womens_cohort object, audience_cluster field, or score)
  - triage graduation
  - treating any listicle named-set as a complete market denominator
live_evidence_plan:
  approved_by: Brian
  approval_scope: autonomous Market Read Lab runs
  budget_class: light
  review_after: 3 bounded-live runs   # NOTE: this is the 3rd (after 011, 012) — the review checkpoint
  evidence_goal: >-
    Determine whether dedicated women-anchored hormone/menopause/longevity telehealth brands
    exist in the market that the store has not captured (confirming run 020's selection-bias
    hypothesis), versus genuinely thin dedicated-women's supply. Produce a tiered
    capture-candidate list (cross-source-recurrence head vs single-source tail) and a clear
    statement of which side of run 020's asymmetry is coverage vs market.
  source_families_allowed:
    - SERP / listicle
    - owned / official brand pages
    - reviews / forums (light triangulation only)
  source_families_preferred:
    - authoritative third-party "best women's telehealth / menopause / hormone 2026" listicles (for the named set)
    - owned brand pages (to confirm audience positioning + category + offer)
  source_families_disallowed:
    - login-only or paywalled sources
    - broad crawling
    - private / non-public data
    - ad-scraping / social-scraping
  stop_when:
    - ">=2 authoritative listicles yield a cross-source-recurrence named set and the store diff is computable with visible caveats"
    - the next source would expand the question (e.g. into pricing/offer depth) rather than verify membership
    - the remaining uncertainty is a framing judgment (what counts as "women-anchored"), not a sourcing gap
    - sources conflict on a brand's audience framing in a way that needs human interpretation
  disallowed_actions:
    - write-back to store/
    - code, schema, or template changes
    - durable primitive creation
    - triage graduation
approval_needed: no
why_autonomous_safe: >-
  Standing bounded-live policy (approved_by Brian, scope: autonomous MRL runs). Light source
  panel only — a handful of free listicle/SERP searches plus a few owned-page reads; capture
  credit spent only on load-bearing single pages, never a crawl. No write-back, no store
  mutation, no durable primitive, no triage graduation. Membership-level read (who exists /
  who's captured), not a current-pricing or live-policy claim, so source-rigor risk is bounded.
loop1_failure_mode: >-
  Broadening from a membership check into open-ended browsing (offer/pricing depth, demand
  sizing); reading the listicle named-set as a complete market; over-claiming store absence as
  market whitespace; missing the affiliate/SEO confound on listicle inclusion (run 012). Stop
  with insufficient-evidence rather than crawling if <2 authoritative listicles surface.
```

## Selection Notes

The candidate slate deliberately spans store-only (C7), bounded-live (C1/C2/C5/C6),
and approval-gated live (C3/C4) so the recommendation isn't a railroad. But the design
evidence is one-directional: runs 019/020/021 are three consecutive store-only telehealth
cohort cuts that all landed on `query-time-grouping-enough`, and run 021 (the 17th such
landing) calls the marginal design return "low" and names the two under-tested directions.
Of those two, only **external-corroboration bounded-live** is autonomous-safe today
(generalization-beyond-telehealth needs a human-gated capture-first run — C3/C4). C1 is the
specific bounded-live variant run 020 already nominated as highest-value, and it closes a
live design loop on MRL-001 (does an external panel convert the selection-bias hypothesis
into a finding?).

**Operator flag:** this is the **3rd bounded-live run** (after 011 and 012), which is the
`review_after: 3` checkpoint in the standing `live_evidence_plan`. Proceeding is within the
standing approval window; the checkpoint is for *tightening after the batch*, not a hard
stop. Worth a human glance at the three bounded-live runs together after this one completes.
