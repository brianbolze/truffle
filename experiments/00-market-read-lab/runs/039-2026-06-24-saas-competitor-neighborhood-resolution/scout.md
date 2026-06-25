# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue):
  L005 (query-time grouping enough *only when the corpus already carries the cut*) and
  L006 (price-visibility token grain) are the most load-bearing for this slate. The
  observation stream's recent cluster (runs 035–038) is heavily `schema-edge-entity-type`
  on `business_model`/`offering_category` enum-fit, plus a recurring "decision-grade fact
  lives off the captured surface" gap (036 G2, 037 Source Gaps, 038 G2 — three sightings).
- `scout-context.md`: two-test selection (value/reach + design). Prefer source-family
  diversity and calibration against blind spots over store-answerability.
- Last 3 `run-notes.md` files (036 marketplace, 037 wearable-hybrid, 038
  delegation-grounding): all `store-only`, all schema-edge / business_model-centric. The
  slate should break that streak and test a *different* design uncertainty.
- Current run artifacts: fresh Scout-only scaffold; no prior receipts.

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **Q1 (SELECTED).** For the captured Technology/SaaS slice (~22 companies, nearly all tagged a single `offering_category: [Software / SaaS]`), can the store draw a competitor/substitute **neighborhood** — who competes with whom — from existing State alone, given there is **no competitor relation field** and the category enum collapses distinct sub-markets into one bucket? Where does neighborhood-drawing fall to prose/LLM judgment, and what relation or sub-category evidence is missing? | gap-probe (calibration flavor) | yes | store-only | A real reader ("who competes with Notion / Gong / Datadog?") and a roadmap pressure point: relation-as-primitive (run 001 tag `relation-already-a-primitive`) has never been tested store-only on a non-telehealth slice where the structured cut is *too coarse* to resolve sub-markets. Directly tests L005's boundary condition. | **Relations / neighborhood** + **persistence boundary**: does competitor neighborhood deserve durable relation/sub-category State, or is query-time grouping enough — and what happens when the corpus does NOT carry the cut (the inverse of every prior L005 confirmation)? | Reaches past telehealth's fine `anchor_category` enum into a slice with one coarse bucket; probes whether neighborhood survives on `description`/`target_market`/prose or needs a primitive. | Store frontmatter (`offering_category`, `target_market`, `description`, `parent`/`owns`), per-company modules, and prose bodies for ~22 Tech profiles; the captured set as an explicit (partial) denominator. | Presenting my own LLM-inferred competitor clusters as *store-grounded* neighborhood; claiming the captured slice = the real SaaS market (completeness trap). |
| Q2. Across the captured store, which profiles carry a `parent`/`owns` relation, how concentrated is ownership beyond telehealth, and can the store map corporate consolidation across verticals? | value-read | yes | store-only | Reader value (who owns whom) + relation pressure. | Relation primitive (parent/owns is the only relation field). | Whether the one existing relation field generalizes cross-vertical. | `parent`/`owns` frontmatter store-wide. | **Rejected:** too close to run 026 (ownership consolidation); little new design pressure. |
| Q3. In the captured research/survey/feedback-tooling sub-cluster (Qualtrics, Typeform, Delighted, Dovetail, Usertesting, Listenlabs, Granola), what positioning wedge and proof devices does each anchor on, and where is the whitespace? | value-read | yes | store-only | Reader value (field comparison) on a coherent non-telehealth cohort. | Pattern extraction + whitespace on a SaaS cohort. | Whether telehealth-style positioning reads generalize to SaaS. | Frontmatter + prose for ~7 profiles. | A clean answer that teaches little new about Truffle. **Folded into Q1** as a worked sub-cluster. |
| Q4. Across the Energy/deep-tech climate slice (blueenergy, cfs-energy, electra-aero, euclidpower, evoloh), does the DTC-shaped universal schema capture what matters for pre-revenue hardware startups (tech readiness, funding, no price)? | gap-probe | yes | store-only | Tests schema on a pre-revenue hardware cohort. | schema-edge-entity-type (again). | A new entity shape. | Frontmatter + prose for ~5 profiles. | **Rejected for this cycle:** another `business_model`/schema-fit run; slate is over-indexed on that lens (035–038). |
| Q5. Across the captured store, which market-sensitive profiles (pricing/offers) are now stale by capture clock, and can a reader tell? | calibration | yes | store-only | Freshness readiness. | Freshness/automation. | Staleness grain. | `captured_at` store-wide. | **Rejected:** recent repeat of run 032 (freshness grain). |
| Q6. For a buyer cross-shopping productivity/no-code workspaces (Notion, Airtable, Coda), does the store let a reader tell these three apart on job-to-be-done, or do they read as interchangeable? | value-read | yes | store-only | Narrow, high-reader-value substitute read. | Relations + differentiation grain. | Substitute resolution at n=3. | 3 profiles + prose. | Too narrow to expose system pressure; **subsumed by Q1**. |

## Selected Question(s)

1. **Q1** — SaaS competitor-neighborhood gap-probe. It carries the strongest combination
   of real reader value, source-family/cohort diversity (breaks the telehealth +
   business_model streak), and a sharp design test no prior run has run: whether
   query-time grouping (L005) holds when the structured cut is *too coarse* to separate
   sub-markets, and whether competitor neighborhood earns a relation primitive. Q3 and Q6
   are folded in as the concrete worked sub-clusters inside Q1.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "For the captured Technology/SaaS slice (~22 companies nearly all tagged offering_category [Software / SaaS]), can the store draw a competitor/substitute neighborhood — who competes with whom — from existing State alone, given there is no competitor relation field and the category enum collapses distinct sub-markets into one bucket? Where does neighborhood-drawing fall to prose/LLM judgment, and what relation or sub-category evidence is missing?"
selected_slug: saas-competitor-neighborhood-resolution
run_type: mixed
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "The ~22-27 captured profiles with primary_industry: Technology (a partial, capture-biased slice of the SaaS market, NOT the real universe). State this as a known-partial denominator; say 'not found in the captured slice', never 'no such competitor'."
likely_source_panel: "store/<domain>/profile.md frontmatter (offering_category, target_market, description, parent, owns, portfolio_shape, business_model), per-company modules (e.g. productivity_saas.md), and prose bodies. No external sources."
builder_lens: "Relations/neighborhood + persistence boundary: does competitor neighborhood deserve durable relation or sub-category State, or is query-time grouping enough — tested under the adverse condition where offering_category is too coarse to carry the cut (inverse of every prior L005 confirmation). Also tests whether description/target_market prose can substitute for an absent relation field."
reach_reason: "Probes past telehealth's fine anchor_category enum into a slice with one coarse Software/SaaS bucket and zero competitor field, so the neighborhood can only be drawn from prose + LLM judgment — the first store-only test of relation-primitive pressure where the structured cut genuinely fails."
allowed_sources:
  - "store/ (frontmatter + module files + prose bodies for Technology-tagged profiles, plus any adjacent profiles those bodies name)"
  - "experiments/00-market-read-lab/learning/ (context only)"
disallowed_actions:
  - "No live browsing, WebSearch, Firecrawl, or curl"
  - "No store/ mutation or write-back"
  - "No durable primitive / field / category creation"
  - "No lesson proposal or graduation"
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from local store files and existing lab artifacts; no spend, no external sources, no write-back. Read-only over the captured corpus."
loop1_failure_mode: "Laundering my own LLM-inferred competitor clusters as store-grounded neighborhood; OR claiming the captured slice is the real SaaS market (completeness overclaim). Must distinguish 'store carries this relation' from 'I inferred it from prose', and say 'not in the captured slice', not 'no competitor exists'."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. The slate was generated from
reader-recognizable questions first, then pressure-checked against the learning stream:
the check *rejected* Q2/Q4/Q5 as recent repeats or over-indexed lenses and *sharpened*
Q1's design test against L005 (it is the first run designed to test L005's failure side,
not confirm it) and the long-standing relation-primitive pressure (run 001). The learning
stream annotated the candidates; it did not originate them.
