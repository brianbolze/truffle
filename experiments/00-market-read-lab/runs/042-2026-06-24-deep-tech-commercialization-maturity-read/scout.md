# Scout

## Prior Context Read

- `scout-context.md`: two-test selection (value/reach + design). Optimize the slate for
  reader value, reach, source-family/cohort diversity, and calibration against blind
  spots — not store-answerability. A pure reader question must still name a builder lens.
- `question_history.py`: runs 035–041 are a heavy **store-only schema/cohort
  introspection** streak — 035/036/037 enum-fit (`business_model`/`offering_category`),
  039 relations, 041 freshness. Five of the last six are builder-facing diagnostics.
- `learning/observations.md` / `lessons.md` (context, not a queue): three consecutive
  consumer reviews (038 CR1, 039 CR1, 041 CR1) flag the **same value-frontier shape — the
  read's strongest value lands on the builder/Pantry reader, not the buyer**. L005
  (query-time grouping enough only when the corpus carries the cut) and the "decision-grade
  fact lives off the captured surface" cluster (036 G2 / 037 / 038 G2, n=3) are the
  load-bearing prior pressure. The recurring `denominator-reconciliation` n=3 (industry ≠
  entity-shape cohort key) means any cohort draw must not lean on `primary_industry` alone.
- Last 3 completed `run-notes.md` (039 SaaS-neighborhood, 040 state-availability **parked
  at needs-human-review on a spend breach**, 041 capture-diff): 040 is a standing caution
  that bounded-live PDF/multi-page capture cost is invisible pre-call — bias this cycle to
  store-only unless a bounded plan is genuinely tight.
- Note: run-039's slate *raised and rejected* a deep-tech slice question (its Q4) **only
  because it framed it as another `business_model`/enum-fit run**. This slate's Q1 reaches
  the same cohort on a **different axis** (commercialization maturity / "is this real
  yet?"), which is reader-facing and never tested — not the rejected enum-fit lens.

## Candidate Questions

Selected for reader value, reach, cohort diversity, and roadmap learning. Not preferred
for store-answerability.

| Question | Mode | Auton? | Evidence | Why worth a run | Builder lens / design test | What it reaches | Trustworthy evidence needs | Failure mode |
|---|---|---|---|---|---|---|---|---|
| **Q1 (SELECTED).** Across the captured climate / energy / deep-tech slice (electra-aero, verdegoaero, blueenergy, cfs-energy, euclidpower, evoloh, sorafuel, beta-team), can a reader — or a delegated agent — tell a **shipping/commercial product apart from a pre-revenue pilot or pre-product vision** from captured State alone, and where does the DTC/telehealth-shaped schema force *commercialization maturity* to be invented? | gap-probe (calibration flavor) | yes | store-only | Real reader job: a climate/deep-tech scout or partner's first question is "is this real yet — flying/selling, or a render and a pre-order page?" Directly serves **make AI safe to delegate to** + **cold-start** on a vertical where overclaiming maturity is the signature failure. First read to test the **maturity/stage** axis (the deferred traction frame's reader edge) on a coherent deep-tech cohort. | **Pattern extraction + persistence boundary on a maturity axis:** the store has *no* `lifecycle`/`stage`/`maturity` field (confirmed). Does `description` + `unverified_fields` + funding-as-milestone prose carry "shipping vs vision" reliably, or does the reader have to invent it? Tests whether maturity deserves durable State or stays query-time — without re-running 029's store-wide signal-exposure read. | A near-untouched vertical (only 027 read non-telehealth, broadly) and a **new design axis** (stage/maturity), distinct from the 035–037 enum-fit streak and 029's signal-grain read. | Frontmatter (`description`, `unverified_fields`, `parent`/`owns`, funding/milestone prose), per-company prose bodies, and `site_notes` for ~8 deep-tech profiles; the slice as an explicit known-partial denominator. | Reading "2,200 pre-orders" / milestone / vision-page prose as commercial traction; conflating a funded company with a shipping one; treating the *absent* stage field as "these are all early" rather than "not captured at a structured grain." |
| Q2. For a buyer cross-shopping luxury/everyday watches (Rolex, Patek, AP, A. Lange, Cartier, Swatch, Casio), does captured State let a reader tell the brands apart on positioning, price band, and where-to-buy in ~5 seconds? | value-read | yes | store-only | Genuine buyer read; tests the "hand off in 5 seconds" job on a non-telehealth consumer cohort. | Pattern extraction + handoff-readiness on consumer goods. | A consumer cohort the lab only touched via price-visibility (033). | Frontmatter + prose for 7 watch profiles. | **Rejected:** 033 already read this cohort's price/catalog presentation; low new design pressure, and the buyer fact (price band) is the known store-loses axis. |
| Q3. Across the store's obscure long tail (newer/low-profile cos: exaveyra, norexi, parlance-cc, waldo-fyi, sorafuel, stemnovanetwork…), does capture depth + self-flagged confidence degrade vs the dense telehealth core — is the **cold-start** job uniform across the corpus? | calibration | yes | store-only | Reader value (cold-start an unfamiliar co) + a coverage-uniformity lens the lab never tests (it always reads dense cohorts). | Confidence-grain + coverage uniformity across the corpus. | The thin tail, deliberately, vs the always-read dense core. | `unverified_fields` density, body length, module presence across a thin-tail sample vs a dense-core sample. | **Held as runner-up:** strong, but more store-introspection than market read; Q1 carries more outward reader value while still testing coverage. |
| Q4. In the captured research/survey/feedback-tooling cluster (Qualtrics, Typeform, Delighted, Dovetail, Usertesting, Listenlabs), what positioning wedge + whitespace does each anchor on? | value-read | yes | store-only | Clean SaaS field comparison. | Pattern extraction on a SaaS cohort. | A coherent SaaS sub-cluster. | Frontmatter + prose for ~6 profiles. | **Rejected:** 039 already worked the SaaS slice's neighborhood/sub-markets; this re-treads it with less design pressure. |
| Q5. Bounded-live: for 3–4 deep-tech cos, does a light public panel (company newsroom + one trade-press article) confirm commercial-stage claims the marketing site makes? | gap-probe | no | bounded-live | Would sharpen Q1's maturity read with outside confirmation. | Source-panel for maturity verification. | Off-site maturity proof. | Newsroom + 1 trade article per co, tight ceiling. | **Rejected for autonomous run:** 040 just parked on an invisible PDF/multi-page spend breach; trade-press maturity confirmation risks sprawl. Park as a future bounded-live follow-on to Q1. |
| Q6. Across the store, which market-sensitive profiles are stale by capture clock and can a reader tell? | calibration | yes | store-only | Freshness readiness. | Freshness grain. | Staleness signal. | `captured_at` store-wide. | **Rejected:** recent repeat of 032 / 041. |

## Selected Question(s)

1. **Q1** — Deep-tech commercialization-maturity read. Strongest combination of (a) real
   outward reader value (the deciding fact for a deep-tech scout is "is this real yet?"),
   (b) reach into a near-untouched vertical on a **new design axis** (maturity/stage,
   not enum-fit), and (c) a corrective to the three-run "value lands on the builder, not
   the buyer" pattern — this run is deliberately pitched at an end reader's first question.
   It tests the deferred traction frame's reader edge without re-running 029. Q3 is the
   runner-up; Q5 is parked as a bounded-live follow-on only.

## Selected Run Contract

Canonical handoff to Loop 1. If this block and the candidate table disagree, trust this block.

```yaml
selected_question: "Across the captured climate/energy/deep-tech slice (electra-aero, verdegoaero, blueenergy, cfs-energy, euclidpower, evoloh, sorafuel, beta-team), can a reader — or a delegated agent — tell a shipping/commercial product apart from a pre-revenue pilot or pre-product vision from captured State alone, and where does the DTC/telehealth-shaped schema force commercialization maturity to be invented?"
selected_slug: deep-tech-commercialization-maturity-read
run_type: mixed
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "The ~8 captured deep-tech/hardware/climate profiles (electra-aero, verdegoaero, blueenergy-co, cfs-energy, euclidpower-com, evoloh-com, sorafuel-com, beta-team), confirmed by reading each profile; ford-com and uber-com are tagged Energy/Automotive-adjacent but are mature operating companies, not pre-revenue deep-tech, so they are foils/excluded from the pre-revenue read. Treat the slice as a known-partial, capture-biased denominator; say 'not found in the captured slice', never 'no such company'."
likely_source_panel: "store/<domain>/profile.md frontmatter (description, unverified_fields, site_notes, parent/owns, any funding/milestone prose), per-company module files, and prose bodies for the ~8 deep-tech profiles. No external sources."
builder_lens: "Pattern extraction + persistence boundary on a commercialization-maturity axis. The store has no lifecycle/stage/maturity structured field (confirmed by grep). Tests whether description + unverified_fields + funding-as-milestone prose let a reader reliably separate shipping/commercial from pre-revenue/pre-product, or whether maturity must be invented — and whether maturity deserves durable State or stays query-time. The reader edge of the deferred traction frame, distinct from 029's store-wide signal-exposure read."
reach_reason: "Reaches a near-untouched vertical (deep-tech/climate; only 027 read non-telehealth and only broadly) on a NEW design axis (stage/maturity), deliberately breaking the 035-041 enum-fit/cohort-introspection streak and the three-run 'value lands on builder not buyer' pattern by pitching at an end reader's first question."
allowed_sources:
  - "store/ (frontmatter + module files + prose bodies for the deep-tech profiles, plus any adjacent profiles those bodies name)"
  - "experiments/00-market-read-lab/learning/ (context only)"
disallowed_actions:
  - "No live browsing, WebSearch, Firecrawl, or curl"
  - "No store/ mutation or write-back"
  - "No durable primitive / field / category creation"
  - "No lesson proposal or graduation"
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from local store files and lab artifacts; read-only, no spend, no external sources, no write-back."
loop1_failure_mode: "Laundering vision/milestone/pre-order prose as commercial traction (reading '2,200 pre-orders' or a render as 'shipping'); OR treating the absent stage field as 'all early' rather than 'not captured at a structured grain' (the L005 structured-absence inverse). Must distinguish what the State attests from what the reader infers, and say 'not found in the captured slice', not 'not real'."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. The slate was generated from
reader-recognizable questions first, then pressure-checked against the learning stream:
the check *rejected* Q2/Q4/Q6 as recent repeats, *down-graded* Q5 to a parked bounded-live
follow-on (040's spend-breach caution), and *sharpened* Q1's axis to maturity/stage so it
is not the deep-tech enum-fit run that run-039's slate already rejected. The three-run
"value lands on the builder, not the buyer" consumer-review pattern is the design pressure
Q1 is built to push back on; the learning stream annotated the candidates, it did not
originate them.
