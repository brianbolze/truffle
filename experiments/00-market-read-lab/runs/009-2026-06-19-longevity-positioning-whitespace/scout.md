# Scout

## Prior Context Read

- `triage.md`: Active queue. MRL-002 (query recipes, P1, Acknowledged) and MRL-008
  (signal source-rigor/confound, P1, Acknowledged) are the two matured pressures.
  MRL-001 (denominator reconciliation, P2) keeps recurring as the load-bearing caveat.
  MRL-003 (depth-backfill altRx/Marque) is concrete corpus-health. Graduation is human-gated;
  triage is system pressure, **not** a question backlog.
- `scout-context.md`: Strategist-first blind-run window. Bias toward questions a senior
  strategist/creative would ask *before* knowing the system shape — positioning, whitespace,
  promise/proof, offer ladders, trust devices. System learning is the second layer. Prefer
  store-only for unattended Loop 1, but a beyond-store question that exposes a source gap is OK
  as a candidate marked `live-external-needs-approval`.
- Last 3 completed `run-notes.md` (006 Wayback / 007 SEC-EDGAR / 008 TRT price-visibility):
  006/007 were Signals reads (each attached cleanly to per-domain paths — negative recurrence on
  MRL-007). 008 was the first State read after three Signals reads — a recurrence test of run 000's
  GLP-1 price-visibility on the TRT cohort. Finding: **price posture tracks business model, not
  molecule** (now a two-category pattern). 008's explicit next-run advice: run a *third* store-only
  category read, and try a **fresh read axis** rather than a third price-visibility grouping.
- Current run artifacts: none (fresh `009` scaffold).

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| In the longevity/NAD telehealth cohort, what **positioning wedge** does each brand anchor on (NAD+ precursor supply vs rapamycin/senolytics vs biomarker-diagnostic-first vs hormone-optimization), what **proof devices** do they lead with, and where is the sameness vs real whitespace? | market | yes | store-only | Strategist-native whitespace/positioning read on a clean ~8-brand cohort; a **fresh read axis** (positioning/claims, not pricing) on the cohort 008 flagged. Tests whether captured State (telehealth.md positioning notes + offerings.md) supports a claims/proof read without crossing into Judgment. | `telehealth.md` `anchor_category`/positioning notes + `offerings.md` hero claims/proof per brand; verbatim hero/claim language with capture dates. | Crossing from State into Judgment when labeling "wedge"/"whitespace"; mistaking the captured hero (point-in-time) for a durable position. |
| Does **price posture track business model not molecule** in a *third* category (longevity/NAD)? Re-run the publish/membership-floor/gated split. | market | yes | store-only | Direct recurrence of 000/008; would make the pattern three-category. | `offerings.md` `Visibility` column + verbatim price on the anchor line per brand. | Third time on the same recipe → low system novelty; price often bundled in longevity (diagnostic+protocol), muddying the "anchor line." |
| Across the GLP-1 cohort, what is the **offer ladder** — entry offer, intake/lab anchor, subscription/continuity mechanism, and upsell — and what's become table stakes? | market | yes | store-only | Offer-packaging archetype on the deepest cohort; high strategist value, untested read shape. | `offerings.md` roster tiers/bundles + `telehealth.md` funnel notes per brand. | Offer structures are A/B-volatile (Ro, eden, brello flagged point-in-time) — captured floor, not live. |
| Who **owns whom** across the store — parent/owns relations, shared-brand families (forhers/hims, Keeps/Nurx), and which "independent" brands are actually one operator? | market/system-test | yes | store-only | Membership/relations read; tests whether parent/owns frontmatter is joinable enough to answer a consolidation question. | `frontmatter parent`/`owns` fields across packs; `profile.md` ownership lines. | Sparse/uneven ownership capture → false "independent" reads (absence ≠ independence). |
| In sexual-health/ED telehealth, **who leads with price vs identity vs discretion**, and what trust devices (guarantees, clinician presence, reviews) does each use in the first 30 seconds? | market | yes | store-only | Trust/positioning archetype on a distinct cohort (bluechew/rexmd/rugiet + men's-health ED lines). | `telehealth.md` hero/positioning + `offerings.md` ED line claims per brand. | ED cohort overlaps men's-health generalists; cohort-boundary labor (MRL-001) again. |
| What do **customer reviews/forums** say longevity buyers praise vs distrust, and which brands answer those objections on owned pages? | market | no | live-external-needs-approval | Customer-pain/objection mining — a genuine source-ingredient gap (reviews/forums not in store as State). | Live Trustpilot/Reddit/forum capture + owned-page rebuttal mapping; primary URLs + capture dates. | Snippets are leads only; needs approval + spend. Exposes the reviews-as-source gap honestly. |
| Which longevity/NAD brands have **changed their offer or pricing recently** (Wayback/Signals), and would that invalidate a cached strategic read? | market | partial | local-existing | Freshness watch reusing 006's Wayback signal pattern on the longevity cohort. | Existing `signals/` captures for cohort domains; Wayback tenure/continuity context (MRL-008 confound rule). | Most cohort domains may lack prior signal captures → thin denominator; would need fresh capture (approval). |

## Selected Question(s)

1. **In the longevity/NAD telehealth cohort, what positioning wedge does each brand anchor on, what proof devices do they lead with, and where is the sameness vs real whitespace?** (store-only, autonomous-safe)

This is a Scout recommendation until the operator confirms; for the autonomous cycle it proceeds to Loop 1 under the contract below.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "In the longevity/NAD telehealth cohort, what positioning wedge does each brand anchor on (NAD+ precursor supply vs rapamycin/senolytics vs biomarker-diagnostic-first vs hormone-optimization), what proof devices do they lead with, and where is the sameness vs real whitespace?"
selected_slug: longevity-positioning-whitespace
run_type: market
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Store brands whose telehealth.md anchor_category is longevity/NAD (agelessrx, gethealthspan, gogeviti, honehealth, mylifeforce, niagenplus, prohealth, truniagen ~8), plus a flag for adjacent straddlers (joinfridays longevity line, getopt longevity frame) inspected but scored separately."
likely_source_panel: "store/<domain>/telehealth.md frontmatter + positioning notes; store/<domain>/offerings.md hero claims / proof / anchor offer; store/<domain>/profile.md positioning line."
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/"
disallowed_actions:
  - "live browsing / WebSearch / Firecrawl spend"
  - "store/ mutation or write-back"
  - "treating captured point-in-time hero copy as a durable position without dating it"
  - "graduating triage items or implementing system changes"
approval_needed: no
why_autonomous_safe: "Answerable entirely from captured State (telehealth.md + offerings.md + profile.md) already on disk; no current/news/policy/pricing claim requiring live verification; cohort is well-represented in the store."
loop1_failure_mode: "Crossing from captured State into unlabeled Judgment when naming 'wedge' or 'whitespace'; overstating completeness from a partial cohort; mistaking a point-in-time hero (several flagged A/B-volatile) for a durable position."
```

## Selection Notes

- **Decision leverage:** Positioning/whitespace is the most directly creative-brief-useful read shape
  in scout-context, and the longevity/NAD cohort is dense and clean (~8 brands) yet untouched by prior
  reads (000/008 were GLP-1/TRT pricing; 005-007 were Signals).
- **Fresh axis on purpose:** 008's next-run advice warned against a third price-visibility grouping.
  This selects the *same flagged cohort* but a **different read axis** (positioning/proof/whitespace),
  higher system-novelty for Loop 2's developer lens — it pressure-tests where a claims read crosses
  from State into Judgment, a different question than the price recipe.
- **Why not the review-mining candidate:** highest strategist value but needs live reviews/forums →
  `live-external-needs-approval`, out of scope for an unattended cycle. Kept as a candidate because it
  honestly exposes the reviews-as-source gap.
- **Treat prior patterns as hypotheses:** the "price-posture = model" law is *not* assumed here; this
  read may surface a different organizing axis (e.g. supply-access vs clinical-protocol vs
  diagnostic-first) worth noting.

Selected question is `autonomous_eligible: yes`, `evidence_mode: store-only`, `approval_needed: no`
→ proceed to Loop 1.
