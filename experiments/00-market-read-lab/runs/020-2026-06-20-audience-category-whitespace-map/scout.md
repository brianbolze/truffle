# Scout

## Prior Context Read

- `triage.md`: 11 open items. Heaviest pressure is the **State-read recipe family** (MRL-002, 6 source surfaces tested) and the **anchored-only denominator under-count** (MRL-001, recurs across ~6 cohorts). Relations (MRL-005/006/011), reviews-bodies (MRL-010, graduation-ready), and change-pulse (MRL-012) are the live relation/source/freshness threads. Used only to annotate candidates and sharpen evidence bars — not to source questions.
- `scout-context.md`: two-test selection (reader value beats generic Claude+web AND the run teaches Truffle something). Start from the market question; don't let triage or a parked next-step originate it; say "not found," not "not there."
- Last 3 `run-notes.md` (017 substitute-map, 018 change-pulse, 019 visual-cluster): the last three runs all probed **new store surfaces** (competitive-set, temporal/diff, visual prose). 018's next-run advice floated a "staleness/decay audit" — deliberately *not* selected here, to avoid executing a parked next-step.
- Current run artifacts: fresh scaffold (slug `scout-candidates`).

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| **C1. Audience × category whitespace** — cutting the store by `audience` (men-only/first, women-only/first, all-genders) instead of category, where is the gender market thin or empty per condition, and is the apparent men-vs-women brand asymmetry real or a store-coverage artifact? | market | yes | store-only | First read to use `audience` as the **primary axis** (all 20 priors cut by `anchor_category`); whitespace mapping is a strategist job generic Claude can't do without hand-collating 54 sites. 54/54 have both fields. | Per-brand `audience` value (verbatim, not from name), `anchor_category`, the audience×category cross-tab, fill-rate; absence framed as "no captured brand," anchored-only under-count carried. | Whitespace = pure absence claim; "no women's longevity brand" is bounded by store coverage, not the market. Over-reading the 15-vs-5 men/women asymmetry as a market fact. |
| C2. Insurance vs cash-pay posture by category | market | yes | store-only | Reader wants to know which conditions still take insurance vs went cash-only. | `pay_model` field across cohorts. | Near-constant field (run 015 found cash-pay 49/54) → low-information; likely table-stakes, not a differentiator. |
| C3. Which brands lead on clinical credibility (named MDs, advisors, studies) vs price vs convenience? | market | yes | store-only | Positioning read for a strategist. | `Credibility & access` prose across brands; re-derivation risk (MRL-002 quote-don't-paraphrase guard). | Credibility is prose, not a field — heavy interpretation; partially covered by run 009 (longevity). |
| C4. Included-labs/bloodwork as table stakes vs premium wedge | market | yes | store-only | Offer-structure reader question. | `Labs:` frontmatter + offer prose. | Close to runs 008/010/015 offer-ladder family; risk of recurrence with no new design lesson. |
| C5. Cold-start quality probe — pick 3 unfamiliar captured brands, does the store profile cold-start them in 5s? | system-test | yes | store-only | "Cold-start a company" is the **least-tested value job** (every run is cross-field aggregate). | 3 profile.md reads vs a blind reader's needs. | Low design yield for the lab; overlaps /query-companies' job; hard to make falsifiable. |
| C6. Best-designed telehealth listicle vs visual.md clusters | market | no | bounded-live | 2nd visual sighting (run 019 next-step) corroborated demand-side. | Listicle panel + visual.md. | Parked next-step from 019; bounded-live; defer until a store-only 2nd visual read exists. |
| C7. Staleness/decay audit — oldest `captured_at` per load-bearing field | system-test | yes | store-only | Decay side of freshness, complements run 018. | capture clocks across modules. | **Explicitly a parked next-step** from run 018's advice — rejected per scout-context (don't let advice originate the question). |

## Selected Question(s)

1. **C1 — Audience × category whitespace.** Reader-recognizable (a founder/strategist scoping the telehealth market wants the gender-whitespace map), store-only and autonomous-safe (54/54 coverage on both fields), and genuinely novel: it pivots the State-read recipe family onto the **`audience` axis** for the first time and onto a **whitespace/absence** question, which is the sharpest possible test of the lab's "say not-found, not not-there" discipline and the persistence-boundary question (is an audience cut worth durable State, or is it query-time-enough like every prior cut?).

Runner-up: C3 (credibility positioning) — held as a future positioning read; more prose-interpretation risk and partly covered by run 009.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "Cutting the captured telehealth store by audience (men-only/men-first, women-only/women-first, all-genders) rather than by category, how does brand supply distribute across the audience × anchor_category grid — where is the gender market thin or empty per condition, and is the apparent men-leaning vs women-leaning brand asymmetry (15 vs 5 on first count) a real captured pattern or a store-coverage artifact?"
selected_slug: audience-category-whitespace-map
run_type: market
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "The 54 store domains with a telehealth.md; all 54 carry both audience and anchor_category. Treat as a floor — the anchored-only under-count (MRL-001) means multi/none generalists that serve a category without anchoring to it fall out of any per-category cell."
likely_source_panel: "Local store only: store/*/telehealth.md frontmatter (audience, anchor_category), with audience value taken verbatim from the field (not inferred from brand name), and the body note when the field comment flags a straddler."
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/triage.md"
disallowed_actions:
  - "live browsing / WebSearch / Firecrawl"
  - "store/ mutation or write-back"
  - "creating a durable audience-cohort object, audience_cluster field, or score"
  - "treating empty cells as market absence rather than store-coverage absence"
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from already-captured local store frontmatter and existing lab artifacts; no spend, no live evidence, no store mutation, no durable primitive. Pure query-time grouping on two clean enums."
loop1_failure_mode: "Reading empty/thin audience×category cells as proven market whitespace instead of store-coverage whitespace; over-claiming the men-vs-women asymmetry as a market fact when it is a captured-supply count bounded by the cohort's intentional men's/hormone tilt and the anchored-only under-count."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. C1 was chosen because it originates
from a real downstream reader's question (gender-whitespace map), clears the value test
(54-site hand-collation generic Claude can't do reliably), and clears the design test on
two axes the lab hasn't pushed: a **new field axis** (`audience`) for the MRL-002 recipe
family, and a **whitespace/absence** read that stress-tests the "not-found ≠ not-there"
and persistence-boundary conventions. C7 (staleness audit) was deliberately rejected
despite being cheap, because it merely executes run 018's parked next-step rather than
originating from a reader question.
