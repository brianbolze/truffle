# Scout

## Prior Context Read

- `triage.md`: 14 items. Relations tracked only on the **backend-prose** axis — MRL-005
  (named-counterparty pharmacy/clinical edge, prose in `telehealth.md`) and MRL-006
  (capture-grain split: `parent`/`owns` are clean frontmatter, partners are prose).
  MRL-006 explicitly notes `parent`/`owns` are the *clean joinable* relations vs prose
  partners — but **no run has ever aggregated the `parent`/`owns` axis into a market
  view**. MRL-011 (competitive/substitute relation = buyer-relative Judgment, not a
  fact). MRL-002 State-read recipe family now spans 8+ surfaces but never an
  ownership/consolidation cut. MRL-001 denominator pressure (anchored-only under-count;
  selection-bias under-count, 3-run-confirmed) is the dominant recurring caveat.
- `scout-context.md`: select for value + reach + builder lens, not store-answerability;
  gap-probes are first-class; name the builder lens; absence = "not found" not "not there".
- Last 3 `run-notes.md` (023 price-comparability / 024 behavioral coverage-radar /
  025 geographic availability): 023+025 store-only State/structure reads, 024 the 3rd
  bounded-live coverage-radar. None touched corporate ownership/consolidation.
- Current run artifacts: fresh scaffold (026).
- `question_history.py`: 26 prior runs. Relation runs (014/016/017) all backend/competitive.
  **Zero** ownership-consolidation reads. Store probe confirms a mixed 135-company corpus
  (telehealth + general brands) with `parent`/`owns` present in 126 profiles but sparse-
  valued, showing real concentration (thirtymadison, niagenbioscience, amazon, richemont
  each parent ≥2; multi-brand `owns` families: thirtymadison→rexmd/shapiromd/navamd,
  uber→eats/freight/health, etc.).

## Candidate Questions

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **Ownership/consolidation map: which captured brands roll up to a shared parent (`parent`/`owns`), how concentrated is ownership, and can the store map consolidation at query time — or is ownership mostly undisclosed/uncaptured?** | gap-probe (value-read flavor) | yes | store-only | Classic competitive-intel question ("who actually owns these brands"); first aggregation of the CLEAN joinable relation axis | Tests whether `parent`/`owns` frontmatter is dense+joinable enough to serve a consolidation map at query time vs needing durable relation State — distinct from MRL-005/006 (backend prose) and MRL-011 (buyer-relative judgment) | A relation axis never aggregated in the lab; the absence-isn't-proof boundary (parent:[] "independent" vs "not stated/unverified") | `parent`/`owns` frontmatter + inline provenance comments; profile.md Overview for disclosure source | Reading `parent: []` as "independent" when the comment says "not stated"; reading disclosed ownership as verified truth (claim-not-truth) |
| Second-cohort price-comparability (men's-hormone/TRT): are captured prices commensurable, or do units/structures diverge like GLP-1 (run 023)? | calibration | yes | store-only | Would harden run 023's normalization-rubric finding on a 2nd cohort | Tests whether the query-time price-normalization rubric generalizes | A 2nd cohort for the rubric | `offerings.md` Price/Visibility | Repeats 023 too closely; low novelty |
| Capture-freshness legibility: can a reader determine the "as-of" date for any load-bearing field, and how consistent are capture clocks across modules within a company? | gap-probe | yes | store-only | Tests the Freshness pillar from the STATE side (018 tested Signals side) | Whether capture clocks travel with fields/modules | Provenance/freshness grain frontier | capture clocks in frontmatter across modules | Could collapse to "yes dates exist" → low learning |
| Single-brand cold-start sufficiency: does profile.md alone answer First-Contact 5-second questions without cross-module assembly? | calibration | yes | store-only | Tests Cold-start / 5-second-handoff jobs (all 25 runs were cross-company) | Single-profile consumability vs cross-module assembly | A different value job + persona (First Contact) | 3–4 anchor profiles | Subjective; weak generalizable builder signal |
| Non-telehealth generalization: does the lab's State-read machinery produce a useful read on the store's general-brand slice (Uber/Ford/Nike/Notion/Casio…), or is it telehealth-tuned? | calibration | yes | store-only | Tests whether the recipe family generalizes off the telehealth corpus | Recipe portability off the dominant cohort | The non-telehealth corpus slice | general-brand profiles | Vague target; hard to pin one reader-valued question |
| Modality of proof: across the store, which credibility claims are self-asserted vs third-party-verifiable (LegitScript, SEC, named clinician licensure)? | gap-probe | yes | store-only | Adjacent to MRL-008 source-rigor | State/Judgment boundary on proof verifiability | Verifiability grain | profile.md Credibility blocks | Overlaps run 021 proof-device read |

## Selected Question(s)

1. **Ownership / consolidation map** — first aggregation of the clean joinable
   `parent`/`owns` relation axis. High reader value (who-owns-whom), novel builder lens
   (clean-relation density vs MRL-005/006 backend prose), store-only, autonomous-safe,
   and it directly stress-tests the absence-isn't-proof boundary the lab keeps flagging.

(Runner-up: capture-freshness legibility — held; lower reader pull, risk of low learning.)

## Selected Run Contract

```yaml
selected_question: "Across the captured store, which brands roll up to a shared corporate parent (via parent/owns frontmatter), how concentrated is ownership (any parent linked to multiple captured brands), and can the store map market consolidation at query time — or is ownership mostly undisclosed or uncaptured?"
selected_slug: ownership-consolidation-map
run_type: mixed
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "All store companies with a profile.md carrying parent/owns frontmatter (~126 of 135 dirs). Partial by construction — frontmatter records only what each site discloses, so the consolidation map is a floor, not a census."
likely_source_panel: "store/<domain>/profile.md frontmatter (parent:, owns:) + inline provenance comments + profile.md Overview/unverified_fields for the disclosure source."
builder_lens: "Whether the clean joinable parent/owns relation is dense enough to serve a market consolidation map at query time (query-time-grouping-enough) — distinct from MRL-005/006 backend-prose edges and MRL-011 buyer-relative competitive judgment. Also tests whether the parent:[]-with-comment convention cleanly separates disclosed-independent from undisclosed/uncaptured (absence discipline)."
reach_reason: "Aggregates a relation axis the lab has never mapped (corporate ownership), and probes the absence-isn't-proof boundary where parent:[] could mean independent OR not-stated."
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/triage.md"
disallowed_actions:
  - "live browsing / WebSearch / Firecrawl"
  - "store/ mutation or write-back"
  - "durable primitive / relation-table creation"
  - "triage graduation"
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from local store frontmatter and existing lab artifacts; no spend, no external sources, no write-back."
loop1_failure_mode: "Reading parent:[] as verified-independent (it often means not-stated/unverified), treating disclosed ownership as adjudicated truth, or overstating consolidation from a partial disclosed-only denominator."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. This run leads with reader value
(ownership/consolidation) and names a concrete builder lens (clean-relation density +
absence discipline) that no prior run has tested. The gap-probe framing is honest: the
likely finding is that ownership is sparsely disclosed, which is itself the result —
the question is whether the disclosed slice still maps meaningful concentration and
whether `parent: []` reliably means independent vs unknown.
