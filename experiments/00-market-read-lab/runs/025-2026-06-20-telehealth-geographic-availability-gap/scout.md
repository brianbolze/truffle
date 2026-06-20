# Scout

## Prior Context Read

- `scout-context.md`: two-test selection (value/reach + design), value jobs, design
  uncertainties, evidence-mode ceilings. Optimize the slate for reader value + reach +
  source-family diversity, NOT store-answerability.
- `question_history.py`: 24 prior runs. Heavily mined: price-visibility (000/008/023),
  backend relations (001/014/016), signals (002/005/006/007/018), category crowding
  (004), positioning (009), offer ladder (010), trust-gap reviews (011), default-brand
  leaderboard (012), access/identity (013), cross-cohort table-stakes (015), competitive
  set (017), visual cluster (019), audience whitespace (020), proof devices (021),
  women's whitespace (022), price comparability (023), behavioral coverage (024).
- `triage.md` (post-candidate annotation): MRL-002 (query-recipe family, ~8 store-read
  surfaces — saturated), MRL-001 (denominator: anchored-only under-count + selection-bias,
  3-run confirmed), MRL-008 (confound family), MRL-010 (review bodies, 3 sightings),
  MRL-012 (change-pulse readiness). Bounded-live coverage-radar now run 3× (012/022/024)
  → "named, don't build"; a 4th would mostly repeat.
- discovery-ledger.md: header-only (raw learning has been living in run-notes Discovery
  ledgers + triage Evidence Logs).
- Grounding probe: telehealth cohort pack has **8 structured cuts** (`value_chain_role`,
  `pharmacy_model`, `audience`, `compounding_posture`, `anchor_category`, `modality`,
  `access_model`, `pay_model`). **No geographic / state-availability field.** A grep of
  54 `telehealth.md` bodies finds availability language in only ~16, mostly boilerplate
  ("licensed in all 50 states") + a few real exclusions (Marek: not NY/NJ/RI;
  state-limited treatments).

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **C1. Where can you actually get this?** Across the captured telehealth store, what does each brand disclose about *geographic / US-state availability* (serves all 50 states, names exclusions, or is silent), and can the store answer "can I get X in my state?" at all? | gap-probe | yes | store-only | "Where can I get this" is a first-order buyer question the lab has never read — every prior run is offer/price/relation/trust/visual/audience/category, never *place*. A clean gap-probe maps a real coverage frontier. | Tests whether geographic availability is a captured surface. It is NOT one of the 8 cohort cuts; it lives as sparse, mostly-boilerplate prose. Probes persistence-boundary (does availability deserve State?) + a confound (the "all 50 states" claim). | Reaches an axis orthogonal to all 24 prior runs; likely exposes a structural depth gap, not just a thin denominator. | Per-brand availability prose where present; honest "not found" where silent. State/Judgment line: a claim is captured State, not verified truth. | Reading boilerplate "50 states" as verified coverage; treating silence as "available everywhere." |
| C2. Cross-signal corroboration: for brands with ≥2 captured Signal families (Trustpilot / Wayback / SEC), do the signals *agree* on a coherent picture (trusted+established+funded) or contradict, and what does disagreement mean? | calibration | yes | store-only | Tests whether stacking captured signals raises or muddies confidence — a "trust the cache" calibration. | Confidence/source-grain at cross-signal grain (cross-sectional, vs run 018's temporal). | Probes whether multi-signal joins add signal or noise. | Per-brand signal triplets with confound siblings (MRL-008). | Over-reading a coincidental agreement as corroboration; ignoring confounds. |
| C3. Compounding-pathway disclosure: which brands disclose their 503A vs 503B vs FDA-brand pathway and Schedule status, and is this a clean structured cut or fuzzy prose? | value-read | yes | store-only | Regulatory pathway is decision-grade for a compounded-Rx buyer; partially covered by `compounding_posture`. | Tests whether `compounding_posture` carries the pathway or whether it's prose. | Reaches a regulatory surface (MRL-007 category-signal flavor). | Verbatim pathway claims per brand. | Re-deriving pathway from molecule rather than disclosed claim. |
| C4. Cancellation / refund-term disclosure: which brands disclose cancel/refund terms on owned pages, and how does that compare to the billing-after-cancel objection cluster run 011 found in review bodies? | value-read | yes (light) | bounded-live | Run 011 found billing-after-cancel is THE dominant trust objection; do owned pages pre-empt it? | Owned-page State vs review-body Signal (MRL-010, 3rd-sighting territory). | Reaches review bodies. | Owned cancellation pages + a small review panel. | Repeats MRL-010 ground already at graduation bar. |
| C5. Lab/diagnostic inclusion model across cohorts: who bundles labs vs gates vs excludes, and is "labs included" comparable across brands? | value-read | yes | store-only | A real "what do I actually get" comparability question. | Another MRL-002 store-read surface (saturated family). | Low reach — within the saturated store-read family. | `Labs:` field + prose per brand. | Adding a 9th near-identical store-read surface with little new learning. |
| C6. Corpus coverage-health map: which captured brands are module-thin (missing telehealth.md / offerings.md / visual.md) and silently shrink cohort reads? | calibration | yes | store-only | Internal calibration of what the store can answer; extends MRL-003. | Coverage-caveat / depth-backfill, but an internal audit, not a market read. | Low external reader value. | Module presence per domain. | Drifting into corpus-maintenance, not a market read. |
| C7. Acquisition-surface friction: quiz-walled vs direct-buy vs consult-gated front doors across the store — how much friction stands between a buyer and a price? | value-read | yes | store-only | Overlaps price-visibility `[on-request]` token reads heavily (000/008/010/023). | Mostly re-reads the price-visibility token. | Low reach — recently/repeatedly covered. | Front-door flow per brand. | Repeating the price-visibility family. |

## Selected Question(s)

1. **C1 — Geographic / US-state availability (gap-probe, store-only).** Recommended.
   Genuinely new axis (place, not offer); high first-order reader value; cleanly probes
   a structural store gap (availability is not one of the 8 cohort cuts) without needing
   a durable primitive or external spend. The gap map is the result.

Secondary: C2 (cross-signal corroboration calibration) if C1 is declined.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "Across the captured telehealth store, what does each brand disclose about geographic / US-state availability (serves all 50 states, names specific exclusions/limits, or is silent), and can the store answer 'can I get this in my state?' at all — or is availability a structural gap?"
selected_slug: telehealth-geographic-availability-gap
run_type: mixed
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "The 54 store companies carrying a telehealth.md cohort pack. Treat as partial: this is the captured cohort, not the market. The anchored-only under-count (MRL-001) does not bite here because the read spans the whole cohort, but corpus selection bias (MRL-001) still bounds it."
likely_source_panel: "store/<domain>/telehealth.md bodies (availability/licensing prose), profile.md site_notes + Overview, offerings.md where availability is stated per line. No external panel."
builder_lens: "Tests whether geographic/state availability is a captured surface in the telehealth cohort. It is NOT one of the 8 structured cuts and appears only as sparse, mostly-boilerplate prose (~16/54). Probes (a) the persistence boundary — does state availability deserve durable State, a depth-backfill, or stay query-time/uncaptured; and (b) a source-rigor confound — the 'licensed in all 50 states' claim is marketing boilerplate, not verified state-by-state coverage."
reach_reason: "Reads an axis orthogonal to all 24 prior runs (none touched geography/place). Expected to expose a structural depth gap rather than a thin-denominator artifact — a frontier the store cannot currently see."
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/triage.md"
  - "experiments/00-market-read-lab/discovery-ledger.md"
disallowed_actions:
  - "No live browsing, WebSearch, Firecrawl, or any external capture."
  - "No store/ mutation or write-back."
  - "No durable primitive / new frontmatter field creation."
  - "No triage graduation."
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from local store files and existing lab artifacts; the point of a gap-probe is precisely what store-only can and cannot say. No external spend, no write-back."
loop1_failure_mode: "Reading boilerplate 'all 50 states' claims as verified coverage (overclaiming), or reading silence as 'available everywhere' instead of 'not found'. Also: claiming a clean availability denominator when it is sparse prose."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. C1 wins on reach (a never-touched
axis) + first-order reader value + a clean autonomous-safe gap-probe shape. It is
deliberately store-only: the read's *value* is mapping what the store can/can't answer
about place, and verifying real state-by-state coverage would need a per-brand live
sweep far beyond the light ceiling — so bounded-live would change the question, not
improve it. The expected honest outcome is a depth/persistence-boundary finding plus a
boilerplate-claim confound, both new to the lab. Candidates C5/C6/C7 were kept on the
slate but flagged low-reach (saturated store-read family / internal audit / repeats
price-visibility). C4 is real but sits on MRL-010 ground already at its graduation bar.
