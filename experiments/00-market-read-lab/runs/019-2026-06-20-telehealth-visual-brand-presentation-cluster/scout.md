# Scout

## Prior Context Read

- `triage.md`: Read. Open items cluster around the State-read query recipe (MRL-002, over-confirmed across 008/009/010/013/015/017), the denominator anchored-only floor (MRL-001, surfaced in 6+ runs), backend-relation edges (MRL-005/006, graduation bar met across 014/016), reviews/forums bodies (MRL-010, third sighting/graduation-ready), competitive-relation-as-judgment (MRL-011, single sighting), and change-pulse readiness (MRL-012, single sighting). All open items are now either graduation-ready or single-sighting holds.
- `scout-context.md`: Two-test selection (value + design); start from a reader-recognizable market question, not triage closure; prefer under-tested value jobs / design uncertainties; say "not found," not "not there"; query-time-grouping-enough is valid learning.
- Last 3 `run-notes.md` files (016/017/018): All `store-only`, all `reviewed`. 016/017 were relation reads (backend / competitive); 018 was the first temporal/diff read. Common thread in their next-run advice: the State-read attribute-extraction recipe is now over-confirmed — further single-cohort store-only attribute reads "would likely just repeat" with no new *design* signal. The open design frontiers are (a) demand-side / bounded-live corroboration, (b) the decay side of freshness, and (c) layers the lab has never consumed.
- Current run artifacts: fresh scaffold; no prior receipts.

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| **C1.** Across the captured telehealth cohort with a `visual.md` layer (34 brands), how does brand/design *presentation* cluster (premium-editorial vs functional-clinical vs budget-utility), and does a brand's presentation posture track its price-transparency or positioning posture? | mixed | yes | store-only | **First read to consume the `visual-evidence` layer as a cross-company ingredient.** Every prior run used `telehealth.md`/`offerings.md`/`profile.md`/signals; `visual.md` (impression + polarity-graded cards) has only ever been produced per-company, never aggregated. Reader value: a creative-director / strategist "how does this field present itself" read with cited per-card evidence — exactly the Scott-Witt brief surface. | The 34 `visual.md` files; each brand's `Visual & brand impression` + `polarity`-tagged evidence cards; join to `telehealth.md` price-visibility/positioning frontmatter. Cite specific cards, not just the impression prose. | Compounding subjectivity: `visual.md` is a Judgment-dense layer, so clustering already-interpreted impressions can manufacture a false market structure. Treating strong/weak card *tallies* as an objective quality score (the visual layer parks scoring by contract). 34/54 telehealth coverage + varying capture depth is a floor. |
| **C2.** Across the store, how stale is the load-bearing evidence — what is the oldest `captured_at` per brand and per load-bearing module, and which cohort reads are at risk of resting on decayed captures? | system-test | yes | store-only | The **decay** side of freshness, complementary to run 018's **delta** side (018's own next-run advice named it). Tests whether "trust the cache over time" needs a staleness surface distinct from the diff surface. | `captured_at` frontmatter across `profile.md`/`telehealth.md`/`offerings.md`/`visual.md`; per-module recency distribution. | Reads more as corpus-health than a market read a downstream reader would recognize; weaker on the value test. Conflating capture date with content-change date (a fresh capture of a static page ≠ new information). |
| **C3.** Across cohorts, what *proof devices* does each brand lean on (clinical studies cited, MD/PhD founder, named lab partner, money-back guarantee, real-patient testimonials), and which are cohort table-stakes vs differentiators? | market | yes | store-only | Reader value for a credibility/whitespace read; extends run 009's single-cohort positioning work to a cross-cohort proof axis. | `profile.md` Credibility blocks + `telehealth.md` positioning prose across cohorts. | High overlap with the over-confirmed State-read attribute-extraction recipe (MRL-002) — Loop 2 would likely flag "no new design signal." |
| **C4.** Which captured brands publish cancellation / refund / auto-renew terms on owned pages vs leave them unstated — and how does that transparency compare with the billing-after-cancel objection cluster run 011 found in reviews? | mixed | partial | bounded-live | Pairs the store's owned-page State with the run-011 review finding; reader-valuable trust read. | Owned cancellation/refund pages (often not captured in current modules) + the run-011 review evidence. | Likely needs live capture of owned policy pages not in the store today → drifts to bounded-live/approval; thin store coverage of refund terms. |
| **C5.** For the captured longevity/NAD or TRT cohort, do brands' owned "vs competitor" / "alternatives" pages name a consistent rival set, and how does that self-named competitive set compare to the store's anchored neighbor grep (run 017)? | mixed | partial | bounded-live | Natural demand-side 2nd sighting for MRL-011 (competitive-relation-as-judgment); would corroborate run 017 supply-side inference. | Owned comparison pages (live) + run-017 neighbor set. | Executes a parked MRL-011 next step rather than originating reader value; needs live browsing → bounded-live/approval. |
| **C6.** Across the store, which brands present as a standalone DTC brand but are skins over a shared backend (the run 016 "invigormedical fronts 5 pharmacies" pattern) — is single-storefront-over-many-suppliers a visible cross-brand pattern? | market | yes | store-only | Reader-valuable market-structure read. | `telehealth.md` fulfillment/clinical prose across the store. | Re-executes the MRL-005/006 backend-relation line whose recurrence question is already answered on both axes; low new design signal. |

## Selected Question(s)

1. **C1 — telehealth visual/brand presentation cluster (recommended).** It is the only candidate that consumes a store layer the lab has never read (`visual.md`), clears both tests cleanly, and is fully autonomous-safe `store-only` with zero spend. C2 (staleness/decay) is the runner-up — genuinely fresh design-wise but weaker on reader value. C3/C6 re-run over-confirmed recipes; C4/C5 drift to bounded-live/approval and partly execute parked next steps.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "Across the 34 captured telehealth brands that have a visual.md visual-evidence layer, how does brand/design presentation cluster (e.g. premium-editorial vs functional-clinical vs budget-utility), and does a brand's presentation posture track its price-transparency or positioning posture from telehealth.md? Surface cited cross-brand presentation patterns, NOT a quality score or ranking."
selected_slug: telehealth-visual-brand-presentation-cluster
run_type: mixed
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "The 34 store domains that have BOTH visual.md and telehealth.md (telehealth brands with a captured visual-evidence layer). Treat as a coverage floor: 34 of 54 telehealth.md brands have visual.md, and visual capture depth varies — report fill/coverage, do not claim the 34 are the visual universe."
likely_source_panel: "store/<domain>/visual.md (Visual & brand impression + polarity-graded evidence cards) joined to store/<domain>/telehealth.md frontmatter (price-visibility / anchor_category / positioning)."
allowed_sources:
  - "store/*/visual.md"
  - "store/*/telehealth.md"
  - "store/*/profile.md (for positioning/credibility context only)"
  - "experiments/00-market-read-lab/triage.md"
  - "modules/VISUAL.md (visual-evidence contract, to respect the no-score boundary)"
disallowed_actions:
  - "No live browsing, no Firecrawl/Exa spend, no re-rendering of pages."
  - "No store/ mutation or write-back."
  - "No durable primitive, category object, or visual-quality score/ranking field."
  - "Do not emit a quality score, grade, or leaderboard — the visual layer parks scoring by contract; surface cited patterns/clusters only."
  - "Do not treat strong/weak card tallies as an objective quality metric."
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from already-captured local store files (visual.md + telehealth.md). Zero spend, no live browsing, no write-back, no new primitive. The only risk is interpretive overreach, which the disallowed_actions and the no-score boundary bound."
loop1_failure_mode: "Manufacturing a false market structure by clustering already-interpreted impression prose; or sliding from 'cited presentation patterns' into an implicit quality ranking. Mitigate by citing specific evidence cards (with polarity), treating the impression paragraph as secondary to its own cards, reporting visual-coverage as a floor (34/54) with capture-depth variance, and refusing any score/leaderboard."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. C1 is recommended because it is
the first read to treat the `visual-evidence` layer as a cross-company ingredient — a
genuine **persistence-boundary + confidence/source-grain** design test (does a
Judgment-dense per-company layer aggregate without compounding subjectivity?) rather
than another pass over the over-confirmed State-read attribute-extraction recipe. The
design test can pass even if the answer is "visual State does not aggregate cleanly /
query-time-grouping-enough does not hold for an interpreted layer" — that is valid
learning about whether `visual.md` is a reusable market-read ingredient or only a
per-company artifact.
