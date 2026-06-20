# Scout

## Prior Context Read

- `triage.md`: MRL-010 (review/forum **bodies** as a source ingredient) is at 2 sightings (runs 008, 009), holding for a 3rd; MRL-008 (source-rigor / confound convention) and MRL-002 (query recipes) are the acknowledged recurring pressures. MRL-001 (denominator reconciliation) is acknowledged.
- `scout-context.md`: current policy **biases toward a `bounded-live` selection** when a light source panel would materially improve a Strategist-native answer; do not default to `store-only` for ease. Trust-gap, objection-mining, and whitespace question shapes are explicitly seeded.
- Last 3 `run-notes.md` files (008 TRT price-visibility, 009 longevity positioning, 010 GLP-1 offer ladder): **all three were `store-only` State reads.** In fact *all seven* reviewed runs to date are `store-only`. `bounded-live` is implemented in convention (README, prompts, templates, `new_run.py`) but **has never actually been exercised.** Runs 008 and 009 both *fired* a source-panel pressure lens because their load-bearing trust/whitespace claims needed review/forum bodies the store does not hold.
- Current run artifacts: fresh Scout-only scaffold (011), no prior receipts.

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| In compounded GLP-1 telehealth, where is the **trust gap** — what objections/regret cluster in customer reviews & forums, and do the brands answer them on their owned pages? | mixed | yes | bounded-live | First actual `bounded-live` exercise; pairs rich store State (owned-page trust devices already captured) against a live review/forum panel the store cannot hold; 3rd sighting test for MRL-010. | Store profile.md Credibility blocks (State) + a small panel of review/forum bodies (Trustpilot, Reddit, listicle) with exact URLs, capture dates, source grade, sampled-not-representative caveat. | Treating a sampled panel as "customers think…" (representativeness overreach); letting the panel sprawl across all 19 brands instead of a light 3–4 brand cut. |
| Across GLP-1 telehealth, which brands are named as the **default / best / cheapest** on third-party listicles & SERPs, and how does that differ from the store's captured universe? | mixed | yes | bounded-live | Tests SERP/listicle as a denominator cross-check + default-player discovery source ingredient. | SERP + 2–3 listicle captures with dates; store GLP-1 roster as the comparison set. | Snippet-as-evidence; "complete market" language from a seed list. |
| What recently **changed** (pricing, FDA compounding posture, launches) that would invalidate the store's cached GLP-1 reads? | market | no | live-external-needs-approval | High consumer value (freshness) but needs broad, open-ended news/regulatory browsing — outside a light bounded plan. | Primary regulatory/manufacturer pages, dated. | Open-ended news crawl; snippet overconfidence. MRL-007 flagged category-level signals have no home. |
| Which GLP-1 brands publish pricing vs gate it behind intake? | market | yes | store-only | Already answered (run 000); low novelty. | Store `offerings.md` Visibility column. | Redundant with 000/010. |
| Who are remedymeds' closest competitors/substitutes by offer shape? | market | yes | store-only | Neighborhood read, but store-only and lower strategic urgency than the trust gap. | Store cohort grep + offer comparison. | Query-time grouping mistaken for a durable category. |
| What do longevity/NAD buyers regret (trust dimension), via reviews/forums? | mixed | yes | bounded-live | Would also feed MRL-010, but 009 already worked this cohort store-only; GLP-1 has richer owned-page trust devices to contrast against. | Review/forum panel + store Credibility blocks. | Redundant cohort with 009. |

## Selected Question(s)

1. **In compounded GLP-1 telehealth, where is the trust gap — what objections and regret cluster in customer reviews/forums, and do the brands answer those objections on their owned pages?** (bounded-live, light 3–4 brand panel)

Rationale: it is the highest-leverage cycle available right now because it does three things at once — (a) it is a question a real strategist/creative director would ask before a positioning or offer call; (b) it is the **first real exercise of `bounded-live`**, the standing-but-untested evidence mode, so the system learns whether a light live source panel is operable unattended; (c) it directly tests **MRL-010** (review *bodies* vs *scores*) for its 3rd sighting, with GLP-1 chosen because the store already holds unusually rich owned-page trust devices (LegitScript seals, self-reported scale/outcome claims, money-back guarantees, named clinical benches) to contrast a live objection panel against.

## Selected Run Contract

```yaml
selected_question: "In compounded GLP-1 telehealth, where is the trust gap — what objections and regret cluster in customer reviews/forums, and do the brands answer those objections on their owned pages?"
selected_slug: glp1-trust-gap-reviews
run_type: mixed
autonomous_eligible: yes
evidence_mode: bounded-live
expected_denominator: "A light, deliberately-sampled panel of 3-4 GLP-1 telehealth brands already in the store, spanning the spectrum: a public/scale leader (hims), a compounding-heavy cheap-access brand (remedymeds), and a recognizable mid/premium player (henrymeds or ro). NOT the full 19-brand store roster; NOT a representative market census."
likely_source_panel: "Store profile.md Credibility blocks for the panel brands (State, owned-page trust devices) + a small live panel of review/forum bodies: each brand's Trustpilot review page (read low-star bodies for objection clusters), 1-2 Reddit/forum threads, optionally one third-party listicle for default-framing. Owned-page rebuttals checked against the store's already-captured Credibility/FAQ content first; only fetch an owned page live if the objection is not already addressed in captured State."
allowed_sources:
  - "store/ (GLP-1 panel-brand profile.md, telehealth.md, offerings.md)"
  - "experiments/00-market-read-lab/ (triage.md, prior run-notes as evidence)"
  - "approved bounded-live source families from live_evidence_plan (reviews/forums; SERP/listicle for default-framing only)"
disallowed_actions:
  - "write-back to store/"
  - "code, schema, or template changes"
  - "durable primitive / category creation"
  - "triage graduation"
  - "broad open-ended news/regulatory crawling (that is the separate live-external-needs-approval candidate)"
  - "login-only / paywalled / private sources"
live_evidence_plan:
  approved_by: Brian
  approval_scope: autonomous Market Read Lab runs
  budget_class: light
  review_after: 3 bounded-live runs
  evidence_goal: "Verify what objections/regret actually cluster in customer review & forum bodies for the panel brands, and whether those objections are answered on the brands' owned pages (captured State). Establish whether review/forum bodies are an operable bounded-live source ingredient."
  source_families_allowed:
    - reviews/forums (Trustpilot review bodies, Reddit/forum threads)
    - SERP/listicle (default-framing / which brand is named best/cheapest — cross-check only)
    - owned/official pages (only to check an owned-page rebuttal not already in captured State)
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
approval_needed: no
why_autonomous_safe: "Standing bounded-live policy (approved_by: Brian) with a filled, light plan. Reviews/forums + a single listicle are public, free-to-read, low-spend surfaces. Cohort is deliberately bounded to 3-4 store brands; owned-page rebuttals come from already-captured State first. No write-back, no schema/template/code change, no triage graduation. Stop rules fail closed to insufficient-evidence rather than expanding into a crawl."
loop1_failure_mode: "Over-claiming representativeness ('customers think X' instead of 'in this sampled panel, objections clustered around X'); panel sprawl beyond the 3-4 brand cut; treating SERP/listicle snippets as decision-grade; spending capture credit speculatively instead of on load-bearing objection/rebuttal verification."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. Two selection facts drove this:
its bias toward `bounded-live` when a light panel materially improves the answer, and the
empirical fact that `bounded-live` has never run despite being fully wired — so exercising
it now has outsized system-learning value beyond the market answer itself. GLP-1 was chosen
over longevity (009) and TRT (008) because the store holds the richest owned-page trust
devices there to contrast a live objection panel against, and because the compounded-GLP-1
trust controversy is unusually objection-dense (FDA-not-approved compounding, billing/cancellation,
provider-access complaints) — a strong stress test of whether review bodies are an operable
source ingredient.
