# Scout

## Prior Context Read

- `triage.md`: Open items skew to two saturated families. **MRL-002** (State-read query
  recipe) has been reinforced by 5 cohort attribute-extraction runs (008/009/010/013/015) —
  Acknowledged P1, recipe-level, no helper wanted. **MRL-005/006** (backend relation edge +
  capture-grain) just had their recurrence bar *met* by runs 014 (clinical/OpenLoop, GLP-1)
  and 016 (pharmacy/Strive, non-GLP-1) — graduation is now a human decision, and run 016
  explicitly advises *against* a third compounded-cohort relation read for new design signal.
  **MRL-008** (signal confound siblings) and **MRL-010** (review bodies) are both
  graduation-decision-ready. The lab is over-fed on cohort attribute extraction and backend
  relations; the open ground is elsewhere.
- `scout-context.md`: Two-test selection (reader value beats generic Claude+web; run teaches a
  Truffle design pressure). Design uncertainties named but **under-tested as a run subject**:
  *relations/neighborhood* on the **competitive/substitute** axis (every relation run so far was
  backend supplier/clinical, never "who competes with X"), *change-pulse/freshness*, and the
  *single-company* framing (every run to date was cohort-wide aggregation).
- Last 3 `run-notes.md` (014/015/016): 014 backend counterparty (GLP-1), 015 cross-cohort
  table-stakes, 016 non-GLP-1 backend. All store-only, all reinforcing existing triage rather
  than opening new ground. 016's own next-run advice: stop re-running relation reads on more
  compounded cohorts; the open move is the human graduation call, not another sighting.
- Current run artifacts: fresh scaffold (017).

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| C1. For an anchor brand (Hone Health), who are its true **substitutes** (same job-to-be-done) vs **adjacent peers** (overlapping but different job), and what captured evidence surfaces make that distinction knowable? | mixed | yes | store-only | First **competitive/substitute** relation read — every prior relation run was backend (supplier/clinical). First **single-company-centric** read (all priors were cohort-wide). Tests the named-but-untested "relations/neighborhood" design uncertainty + a cold-start reader job. | Captured cohort State (offerings, audience, positioning, pricing) for the candidate neighbor set; explicit job-to-be-done criterion for substitute vs adjacent; named inclusion/exclusion. | Calling overlap "substitution" without a job criterion; treating the store cohort as the full competitive universe (anchored-only under-count, MRL-001). |
| C2. For the brands carrying ≥3 captured signal types (Trustpilot + Wayback + SEC-EDGAR), what does **fusing** the signals into one per-brand picture reveal that any single signal hides — and does a fused multi-signal read create false completeness? | system-test | yes | store-only | First run to *fuse* signals per brand; runs 005/006/007 each read one signal in isolation. Tests confidence/source-grain + synthesis. | Per-brand signal captures with their confound siblings; an explicit fusion rule that keeps grains distinct. | Re-confirming MRL-008 without new design signal; implying a durable "brand-health score." |
| C3. What is the **freshness profile** of the captured store — which cohorts/fields/signal types are stale enough that a market read built on them could be wrong, and what would a minimal staleness flag need to watch? | system-test | yes | store-only | Change-pulse/freshness is the least-tested design uncertainty; "trust the cache over time" is a named value job never run as a subject. | Store capture clocks per domain/module; signal capture dates; a defensible "stale" threshold per surface. | Meta/internal — low reader value; inventing a staleness threshold with no decision attached. |
| C4. In a **fresh, never-read cohort** (e.g. hair-loss or mental-health telehealth), what offer/access structures are table stakes vs differentiated? | market | yes | store-only | Reader value on a new cohort. | Cohort frontmatter cut + attribute extraction. | Pure MRL-002 re-feed — saturated 5×; weak design test ("no new primitive" already established). |
| C5. Which captured brands make the **strongest efficacy/clinical claims**, and what **proof devices** (studies, MD bylines, lab partners) do they attach — where is claim-to-proof thinnest? | market | yes | store-only | Pattern-extraction on the claims/substantiation surface (only touched once, run 009 longevity). | `Credibility & access` blocks + body proof claims across a cohort. | Re-feeds MRL-002 state-recipe; claim grading is subjective without a rubric. |
| C6. Across the captured cohort, which brands publish a real **competitor/alternatives comparison page** of their own, and what does owned-comparison framing reveal about perceived rivals? | market | bounded-live | bounded-live | Owned "vs" pages are a relation source surface the lab hasn't sampled. | Captured "/compare" or "vs" pages; light live check where uncaptured. | Sprawl into open browsing; affiliate "vs" pages confound. |

## Selected Question(s)

1. **C1 — Hone Health substitute-vs-adjacent map** (recommended). Opens the one relation axis
   the lab has never touched (competitive/substitute, not backend), in the one framing it has
   never used (single anchor, not cohort-wide), against a deliberately *straddling* anchor
   (Hone sits across TRT and longevity, named a multi-cohort straddler in run 008) so the
   substitute/adjacent boundary is genuinely contested rather than trivial.
2. **C2 — multi-signal fusion** (strong alternate). Best if the operator wants to keep pushing
   the Signals layer; defer because it risks re-confirming MRL-008 rather than opening ground.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "For Hone Health as the anchor brand, who are its true substitutes (same job-to-be-done) versus adjacent peers (overlapping offerings but a different job), and what captured store evidence surfaces make that substitute-vs-adjacent distinction knowable?"
selected_slug: hone-substitute-adjacent-map
run_type: mixed
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Captured store brands plausibly in Hone's neighborhood — the TRT/hormone and longevity/men's-health cohorts via anchor_category grep, plus generalists that offer hormone/longevity lines without anchoring (the MRL-001 anchored-only under-count applies; the candidate neighbor set is a floor, not the full competitive universe)."
likely_source_panel: "store/<domain>/profile.md (positioning, audience, parent/owns), telehealth.md (offerings, pricing model, modality, value_chain_role), offerings.md (line breadth) for Hone and each candidate neighbor."
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/triage.md"
disallowed_actions:
  - "live browsing / WebSearch / Firecrawl spend"
  - "store/ mutation or write-back"
  - "creating a durable competitor/similar-to relation field, object, or edge table"
  - "treating offering overlap as substitution without a stated job-to-be-done criterion"
  - "treating the store cohort as the complete competitive universe"
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from already-captured store State (cohort frontmatter + offerings + positioning). No spend, no live browse, no write-back. The design output is a query-time judgment (is a substitute set cheap to derive, or does it want a durable relation primitive?), not a system change."
loop1_failure_mode: "Collapsing 'overlapping offerings' into 'substitute' without applying the job-to-be-done test; or implying the store-derived neighbor set is Hone's full competitive field rather than a captured-floor sample (MRL-001 anchored-only under-count)."
```

## Selection Notes

C1 clears both tests. **Value:** a cited substitute-vs-adjacent map for one named brand is a
cold-start reader job (who actually competes with X) where Truffle's edge over generic
Claude+web is captured offering/positioning overlap with citations and an explicit job
criterion. **Design:** it tests the *relations/neighborhood* uncertainty on the competitive
axis — orthogonal to the backend-relation work (MRL-005/006) that is already
graduation-pending — and the *boundary/membership* uncertainty (what surfaces make the
neighbor set knowable). Likely honest outcome: query-time cohort grouping plus a job criterion
is enough, and no durable competitor primitive is needed — but on a relation axis the lab has
never examined, which is the point. Deliberately store-only to keep the cycle autonomous-safe;
a bounded-live Exa/"alternatives-to" panel (C6-style) is the obvious follow-up if the
store-only neighbor set proves too thin to trust.
