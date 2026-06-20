# Scout

## Prior Context Read

- `triage.md`: 10 items. Live clusters: MRL-002 (State/Signals query recipes, P1, Acknowledged), MRL-008 (source-rigor/confound, P1), MRL-001 (denominator reconciliation, P2, with a recurring anchored-only-vs-all-offerers under-count finding), MRL-010 (review/forum *bodies*, 3rd sighting + first use, graduation-decision-ready). **Most relevant here:** **MRL-005** (named-counterparty relation edge — *"Hold. Re-test on a backend-naming-dense cohort such as compounding-heavy GLP-1 before graduating"*) and **MRL-006** (named-counterparty capture-grain gap — parent/owns are clean joinable frontmatter, pharmacy/clinical partners are prose in `telehealth.md` bodies). Both are P3/`Submitted`, explicitly parked *for this exact recurrence test*.
- `scout-context.md`: two-test selection (reader value + design value); go wide on archetypes not yet tried; `store-only` only when cached State is genuinely enough; the **Relations / neighborhood** design uncertainty is named but has been the load-bearing cut in only **one** prior run (001).
- Last 3 completed `run-notes.md` (011 GLP-1 trust-gap, 012 GLP-1 leaderboard, 013 sexual-health access map): 011/012 were the only two bounded-live runs (clock at 2/3); 013 deliberately preserved that clock with a `store-only` structural read. The State-read recipe (filter cohort → latest capture → field-extract → group/label) is well-worn on **price / positioning / offer / access** surfaces but has **never** been run on the **relation/counterparty** surface since 001.
- Store scoping (frontmatter + body grep, not an answer): `anchor_category: GLP-1` returns **19** brands. A body scan for pharmacy/clinical counterparties shows the grain is real and **partially named**: MEDVi names **Triad Rx / RedRock Pharmacy / Beaker Pharmacy** (pharmacy) + **OpenLoop Health / CareGLP P.C.s** (clinical); Direct Meds names **CraftedRx**; joinfridays names **OpenLoop Health** (clinical). Most others are `pharmacy_model: third-party` with the partner **explicitly unnamed**; a few are `integrated` with owned siblings (Eden → edenpharmacy.com; hims → Ohio facility; Ro → ro.OS). **OpenLoop recurs across two brands** — a concrete shared-backend signal absent from run 001's men's-health cohort.

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| In the store's compounded-GLP-1 cohort, which brands **name** a pharmacy / fulfillment or clinical-provider backend counterparty, do any counterparties **recur across brands** (supplier concentration), and is that relation load-bearing enough to capture as a joinable edge? | mixed (relation) | yes | store-only | **The explicit MRL-005/006 recurrence test** on the exact cohort triage named ("compounding-heavy GLP-1"). First relation-surface read since 001; first to test cross-brand counterparty recurrence. Closes a parked design decision rather than re-confirming MRL-002 a 5th time. | `pharmacy_model` frontmatter + the named-counterparty claim quoted verbatim from `telehealth.md` Fulfillment bodies; join each named entity to a store profile if one exists. | Treating possessive language ("our pharmacy") as a named entity (the 001 contamination); calling a thin named-set "supplier concentration"; over-reading an `integrated` flag as ownership when the page only claims integration. |
| Across the GLP-1 cohort, what is the split of `pharmacy_model` (third-party / integrated / owned) and `compounding_posture`, and what does that say about who controls fulfillment? | market (structure) | yes | store-only | Clean structural cut; would expose `pharmacy_model` fill-rate. | `pharmacy_model` + `compounding_posture` frontmatter verbatim per brand. | Overlaps run 013's structural-cut recipe; less fresh; doesn't test the relation edge. |
| Who are henrymeds' closest competitors / substitutes in the store, and what distinguishes a new compounded-GLP-1 entrant? | market (neighborhood) | yes | store-only | Untried single-anchor neighborhood archetype. | Cohort membership + per-brand offer/price/molecule cuts. | Calling a partial store cohort the whole competitive set. |
| In compounded GLP-1, what objections cluster in customer reviews and do brands rebut them on owned pages? | market (trust) | yes | bounded-live | MRL-010 4th sighting; pushes bounded-live clock to 3/3. | Trustpilot/Reddit bodies + owned-page rebuttal, dated, source-graded. | Re-runs 011's exact recipe; spends the bounded-live clock. |
| Across all captured cohorts, which brands disclose an owned vs partnered pharmacy, and how does vertical integration vary by category? | system-test | yes | store-only | Corpus-scale integration map. | Corpus-wide `pharmacy_model` grep + coverage accounting. | Denominator sprawl; anchored-only under-count (MRL-001). |

## Selected Question(s)

1. **Candidate 1** — the compounded-GLP-1 backend-counterparty / supplier-concentration relation map (`store-only`). Picked because it is the **designed recurrence test** MRL-005/006 explicitly parked for ("re-test on a backend-naming-dense cohort such as compounding-heavy GLP-1"), and the store scan already shows the trigger condition exists (named counterparties present; **OpenLoop recurs across two brands**) — a concrete shared-backend signal run 001's cohort lacked. It is the first relation-surface read since 001, breaks the price/positioning/offer/access recipe rut, and either advances or closes the MRL-005 graduation decision rather than re-confirming the well-worn State-read recipe. Stays `store-only`, preserving the bounded-live clock at 2/3.

Runner-up: Candidate 4 (GLP-1 trust-gap, bounded-live) — clean MRL-010 4th sighting, but it spends the bounded-live clock and re-exercises run 011's recipe with no new cut. Hold for a deliberate bounded-live cycle.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "In the store's compounded-GLP-1 cohort, which brands name a pharmacy/fulfillment or clinical-provider backend counterparty, do any named counterparties recur across brands (supplier concentration), and is that relation load-bearing enough to capture as a joinable edge?"
selected_slug:          glp1-backend-counterparty-concentration
run_type:               mixed
autonomous_eligible:    yes
evidence_mode:          store-only
expected_denominator:   "Store brands whose captured telehealth.md anchors GLP-1. Seed: anchor_category: GLP-1 (19 brands). Treat as partial; note that anchor-only grep under-counts GLP-1 offerers (MRL-001: multi/none generalists like LifeMD/Nurx/Wisp sell GLP-1 without anchoring), so the named-counterparty census is scoped to the anchored cohort and labeled as such, not as the whole GLP-1 universe."
likely_source_panel:    "store/<domain>/telehealth.md frontmatter (pharmacy_model, value_chain_role, compounding_posture, parent, owns) + the telehealth.md Fulfillment / Clinical-entity bodies + profile.md owns/parent. Join named counterparties to store/<entity>/ profiles where one exists. No external sources."
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/triage.md"
disallowed_actions:
  - "live browsing / WebSearch / Firecrawl spend"
  - "store/ mutation or write-back"
  - "creating durable relation edges, categories, or cohort objects"
  - "triage graduation"
live_evidence_plan: null
approval_needed:        no
why_autonomous_safe: "Answerable entirely from cached store State (frontmatter + Fulfillment/Clinical bodies + parent/owns) plus existing lab artifacts. No outside sources, no spend, no write-back. The only judgment is which prose counts as a 'named' counterparty vs possessive language, which is surfaced as an explicit inclusion rule per the 001 contamination guard."
loop1_failure_mode: "Treating possessive language ('our pharmacy', 'partner pharmacy') as a named entity (MRL-005 contamination); overclaiming 'supplier concentration' from a thin named-set; reading an `integrated`/`pharmacy_model` flag as proven ownership when the page only claims integration; overstating cohort completeness from the anchor-only denominator (MRL-001)."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. This Scout deliberately moved to the
**relation/neighborhood** design uncertainty — load-bearing in only one prior run (001) — and
chose the exact cohort MRL-005/006 parked for ("backend-naming-dense, compounding-heavy GLP-1"),
so the run advances a real graduation decision. Kept `store-only` to preserve the bounded-live
review clock at 2/3 for a future deliberate bounded-live run.
