# Run Notes

```yaml
run_status:            reviewed
evidence_mode:         bounded-live
autonomous_eligible:   yes
termination_reason:    completed
pressure_lenses_fired: [source-panel, source-rigor, freshness-monitoring, coverage-caveat]
```

> **Loop 2 outcome (2026-06-19):** Reviewed via a 3-pass adversarial workflow (evidence verifier +
> consumer + developer, Sonnet). Verifier confirmed C1/C2/C4/C6 verbatim against receipts and rated
> C3/C5 *partial* on **framing** (not fact) — both tightened in `read.md` (C3 Signal label moved to
> front; C5 scoped to captured State). Bounded-live discipline audited **PASS** (4 sources logged,
> 5 credits, stopped at plan boundary, Reddit snippet-only throughout, no disallowed action).
> Consumer verdict: **valuable**. Developer verdict: **valuable** — first clean bounded-live run.
> Triage: appended Evidence Logs to **MRL-010** (3rd sighting + first actual use → graduation-decision-ready,
> human-gated) and **MRL-008** (review-score vs review-body confound flavor). `review_after`-3-runs clock: **1/3**.

## 30-second operator read

- **Did the run work?** Yes — and it is the **first bounded-live run** in the lab's history
  (all 7 prior reviewed runs were store-only). The light panel (3 Trustpilot low-star scrapes +
  1 Reddit search, **5 Firecrawl credits total**) produced a clean, sourced trust-gap answer the
  store could not produce alone.
- **What was awkward?** Nothing structurally — `?stars=1&stars=2` on Trustpilot + `waitFor` got
  full review bodies on the first try. The one judgment call was *stopping*: the clusters were
  obvious after 3 brands, so I held the line at the plan instead of widening to all 19.
- **What should the next agent know?** Bounded-live is operable as written. The review/forum body
  surface is high-signal and the read is materially better than store-only for any trust/objection
  question — this is the **3rd sighting for MRL-010** and the first that actually *used* the missing
  surface rather than just naming the gap. Confound discipline (MRL-008) matters: headline
  Trustpilot scores were misleading (remedymeds 4.6 vs hims 3.0) and the *bodies* told the story.

## What happened

Scout selected a bounded-live trust-gap question over easier store-only options, per
`scout-context.md`'s explicit bias. Loop 1: pulled the 3 panel brands' captured owned-page trust
State from the store (free), then captured each brand's Trustpilot 1-2★ review bodies live
(3 scrape credits), then ran one Reddit search to triangulate the dominant cluster off-platform
(2 search credits, snippet-only). Mapped objection clusters against owned-page trust devices,
wrote `read.md` + 3 receipts. Stopped at the plan boundary.

## Inputs and scope

- **Store (free):** `anchor_category: GLP-1` grep (19 brands → frame); `profile.md` Credibility
  blocks + revenue-model lines for hims, remedymeds, henrymeds.
- **Live panel (paid):** Trustpilot 1-2★ pages for the 3 brands; 1 Reddit `site:` search.
- **Exclusions:** the other 16 store GLP-1 brands (deliberate light sample); positive/invited
  reviews (objection-mining cut); owned-page live re-fetch (captured State sufficed).

## Live evidence plan

```yaml
live_evidence_plan:
  approved_by: Brian
  approval_scope: autonomous Market Read Lab runs
  budget_class: light
  review_after: 3 bounded-live runs
  evidence_goal: "Verify what objections/regret cluster in customer review & forum bodies for the panel brands, and whether those objections are answered on the brands' owned pages (captured State). Establish whether review/forum bodies are an operable bounded-live source ingredient."
  source_families_allowed:
    - reviews/forums (Trustpilot review bodies, Reddit/forum threads)
    - SERP/listicle (default-framing cross-check only)
    - owned/official pages (only to check a rebuttal not already in captured State)
  source_families_preferred:
    - reviews/forums
  source_families_disallowed:
    - login-only or paywalled sources
    - broad crawling
    - private / non-public data
    - broad news/regulatory browsing
  stop_when:
    - the panel shows clear objection clusters with visible caveats for 3-4 brands
    - the next source would widen the cohort rather than verify a load-bearing claim
    - the remaining uncertainty is a framing judgment, not a sourcing gap
    - sources conflict in a way that needs human interpretation
  disallowed_actions:
    - write-back to store/
    - code, schema, or template changes
    - durable primitive creation
    - triage graduation
```

## Live evidence used

```yaml
live_evidence_used:
  - source_or_query: "https://www.trustpilot.com/review/remedymeds.com?stars=1&stars=2"
    source_family: review/forum
    action_taken: scraped
    reason: "Capture remedymeds 1-2★ review bodies for objection clustering"
    source_grade: primary
    captured_at: 2026-06-19
    spend_note: paid-credit
    claim_ids_supported: [C1, C4, C6]
  - source_or_query: "https://www.trustpilot.com/review/henrymeds.com?stars=1&stars=2"
    source_family: review/forum
    action_taken: scraped
    reason: "Capture henrymeds 1-2★ review bodies; CS/ghosting + June-2026 degradation signal"
    source_grade: primary
    captured_at: 2026-06-19
    spend_note: paid-credit
    claim_ids_supported: [C1, C3, C6]
  - source_or_query: "https://www.trustpilot.com/review/hims.com?stars=1&stars=2"
    source_family: review/forum
    action_taken: scraped
    reason: "Capture hims 1-2★ review bodies; price bait-and-switch + billing"
    source_grade: primary
    captured_at: 2026-06-19
    spend_note: paid-credit
    claim_ids_supported: [C1, C2, C4, C6]
  - source_or_query: "firecrawl_search site:reddit.com — kept charging after cancel no refund (panel brands)"
    source_family: review/forum
    action_taken: searched
    reason: "Triangulate the dominant billing/cancellation cluster on a second source family"
    source_grade: direction-finding
    captured_at: 2026-06-19
    spend_note: paid-credit
    claim_ids_supported: [C1, C3]
```

Total spend: **5 Firecrawl credits** (3 scrape + 2 search). No owned-page live fetch (captured State used).

## Friction log

- None notable. Trustpilot's `?stars=` filter + `waitFor: 6000` returned full bodies first try;
  no stealth proxy or retry needed. The lab's bounded-live convention was sufficient to run
  unattended without any improvisation.

## Evidence limits

- **Prevalence unmeasured.** Low-star cut shows which objections cluster, not how often — the
  same brands carry thousands of positive invited reviews. Strictly "in this sampled panel."
- **henrymeds capture (2026-06-04) predates** the reviewer-reported mid-June service degradation;
  the degradation is a *Signal* from review bodies, not a confirmed corporate fact.
- **Reddit corroboration is snippet-only** (direction-finding), not opened.
- **Trustpilot score confound (MRL-008):** paid subscriptions + invited reviews + a merged hims
  profile make headline scores non-comparable; the bodies, not the scores, carried the read.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (planned bounded-live)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **pass**
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **pass** (4 sources)
- If `bounded-live`, stop rules and spend notes were recorded: **pass** (5 credits; stopped at plan boundary)
- No disallowed action happened: **pass** (no store write-back, schema/code/template change, no graduation)
- Required citations / receipts present and source-graded: **pass** (3 receipts)
- No snippet treated as evidence: **pass** (Reddit snippets labeled direction-finding; decision-grade claims rest on full Trustpilot bodies)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (all dated 2026-06-19; June-2026 degradation labeled a Signal)
- Absence language says "not found", not "not true": **pass** (store gap framed as "store holds scores not bodies")

## Surprises

- **The dominant objection is financial/operational, not clinical.** I expected the compounded-
  GLP-1 "is it real/safe?" controversy to lead; instead billing-after-cancel and CS ghosting
  dwarfed efficacy/safety doubt. The trust gap is *post-purchase*, exactly where owned-page trust
  devices (seals, guarantees, clinicians) don't reach.
- **The objection is the published offer's downstream.** remedymeds' "no refund once prescribed"
  and henrymeds' multi-month cancellation balance — both already in captured State — *are* the
  billing-trap reviews. The store accidentally already holds the cause; it just lacks the effect (bodies).
- **henrymeds appears to be in live service distress (June 2026)** per multiple reviewers — a real
  freshness signal a store-only read (captured 06-04) would have entirely missed.

## Pressure tags

| Fired tag | What fired in this run | Triage implication |
|---|---|---|
| `source-panel` | Review/forum **bodies** were required and, for the first time, actually *used* via bounded-live — 3rd sighting of MRL-010, now with a worked example proving the surface is operable and high-signal. | submit triage candidate (MRL-010 evidence: 3rd sighting + first actual use) |
| `source-rigor` | Headline Trustpilot scores were misleading vs the bodies; paid-sub/invited/merged confounds (MRL-008) had to be surfaced for the read to be honest. Reddit kept as snippet-only. | append MRL-008 evidence (confound recurred on a new signal grain: review *score* vs review *body*) |
| `freshness-monitoring` | henrymeds June-2026 service-degradation signal materially changes the read and post-dates the 06-04 capture. | watch for recurrence |
| `coverage-caveat` | Store holds review *scores* not *bodies*; the entire objection dimension is unanswerable store-only. | folds into MRL-010 |

No new tag needed. **"No new primitive needed"** holds: this is recipe/evidence-grade pressure
(does the lab adopt review bodies as a source ingredient?), not a call for a scraper, monitor, or
new schema object from one worked example.

## Triage submissions

1. **MRL-010 (Reviews/forums body content as a source ingredient) — append Evidence Log, 3rd
   sighting + first actual use.** Prior sightings (runs 008, 009) *named* the gap store-only; this
   run *used* bounded-live to fill it and confirms review/forum bodies are an operable, high-signal
   source ingredient for trust/objection reads. Recommendation for the human steward: this likely
   crosses MRL-010's stated "hold for a 3rd sighting" bar. Decision still human-gated — do not
   graduate. Concrete delta remains ratings-vs-bodies; the new datum is "bounded-live makes bodies
   reachable at ~3-5 credits per read without sprawl."
2. **MRL-008 (Captured-signal source-rigor / confound convention) — append Evidence Log.** The
   review *score* vs review *body* mismatch is a new flavor of the same confound family: the store
   captures the headline Trustpilot score (which is paid-sub/invited/merged-biased) but not the
   objection bodies, so a score-only read is overconfident. Reinforces the flavor-aware rule.
3. **Bounded-live operability note (not a new item):** first bounded-live run executed cleanly
   inside the standing plan at 5 credits; `live_evidence_plan` review_after-3-runs clock now at 1/3.

**Do not implement, spike, or recommend immediate graduation from inside the run.**

## Next-run advice

- To make MRL-010 a clean 4th sighting on a *different* cohort, run the same bounded-live
  trust-gap shape on TRT or longevity — if a *different* dominant cluster appears, the trust gap is
  category-specific; if billing/cancellation recurs, it's telehealth-subscription-wide.
- Keep the low-star cut + explicit "in this sampled panel" language; resist prevalence claims.
- Cheap improvement: capture the full star *distribution* alongside the low-star bodies so the read
  can at least bound how vocal-minority the objections are without a full balanced sample.
- Watch the henrymeds June-2026 degradation signal — if a future capture or run corroborates it
  from a primary source, it's a real Signals datum, not review noise.
