# Scout

## Prior Context Read

- **History map (`question_history.py`):** 27 reviewed runs. 26/27 were telehealth-internal;
  027 was the first non-telehealth read but audited *classification*, not a market read.
  **No run has ever touched traction / "how is this company doing?"** — every read is a
  point-in-time State read or a single change-pulse (018) over already-captured signals.
- **`scout-context.md`:** select for value + reach + roadmap learning, not store-answerability;
  gap-probes are first-class with a bounded plan; name the builder lens. The under-tested
  design uncertainties are **change-pulse / freshness** (one run, 018) and the two frontiers
  the engine flags as *open* — **Judgments** and **Traction**.
- **`triage.md`:** MRL-002 (State-read recipe family) is **saturated** — ~15 evidence entries,
  all "recipe-level, query-time grouping is enough, no new primitive, doesn't move the clock."
  MRL-012 (run 018) is the one traction-adjacent item: change-pulse is a *capture-cadence +
  subject-identity + comparator-gap* problem, not a new primitive. No traction *coverage* read exists.
- **Roadmap anchor (`_design/2026-06-14-traction-frame.md`):** traction is the engine's
  named first-class *future* Signal for **market maps**; **v1 already shipped** (comparator +
  funding tool + `signals/` path, 2026-06-15). The frame's capability ladder is 5 steps:
  (1) capture repeatable signals, (2) make repeat captures *comparable* (deltas/velocity),
  (3) accumulate into a durable timeline, (4) roll up across a cohort, (5) feed a consumer
  judgment, never emit one. "Only #1 has real machinery today."
- **Store recon:** 135 dirs / **126 profiled**; **49 companies carry a `signals/` dir**
  (wayback ×102 page-subjects, trustpilot ×20, sec_edgar ×20, trends ×5, serpapi ×2,
  exa_similar ×2, ads_transparency ×1). So the store has a *partial* traction-adjacent
  substrate — this is a real gap-probe, not a near-empty confirm.
- **This run is operator-supervised** (Brian in the loop). Direction was chosen at the Scout
  gate: the **traction gap-probe**, store-only.

## Candidate Questions

Slate generated for reader value + reach + roadmap learning. The selected candidate is the
first lab read on the traction axis; alternatives are recorded for an honest scout trail.

| Question | Mode | Auto-eligible? | Evidence | Why worth a run | Builder lens / design test | What it reaches | Trustworthy evidence needs | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **[SELECTED] Across the captured store, what traction signal (capital/funding, demand, attention/visibility, growth/tenure) does any company actually expose today — at what grain, level-vs-delta, and for how many companies — and is the store *ready to roll a cohort traction-map* per the traction-frame's 5-step ladder?** | gap-probe (calibration) | yes | store-only | First lab read on the engine's named *future* axis (traction). Maps the store against the frame's own capability ladder — the cleanest possible "where are we on traction?" read. Roadmap-critical: the maps consumer is blocked on exactly this. | **Traction-signal readiness.** Which frame-ladder steps the store satisfies (capture/accumulate) vs not (comparability/cohort-rollup), and which captured `signals/` source-types are *real* traction proxies vs mislabeled (Wayback = tenure not traction; Exa = neighbors not traction). Tests the State/Signals/Judgment boundary on a live future-axis. | Reaches past every prior State read into the Signals layer as a *traction substrate*; probes coverage density, grain discipline, and rollup-readiness. | `signals/` dir walk per company (source-type, capture count, latest); profile.md for any traction-bearing *State* field (founded/funding/ticker/headcount); traction-frame + SIGNALS.md axis mapping; MRL-012/run-018 deltas. | Reporting "the store has no traction" (false: 49 cos have signals) **or** "the store has traction" (false: scattered level-reads, no cohort rollup). Must separate *captured* from *comparable* from *rollup-ready*, and flag which signal-types aren't traction at all. |
| Per-company competitor-triage: for one anchor (e.g. honehealth), assemble every traction proxy the store holds into a single cited "how is it doing?" card — does the store support a per-company traction read end-to-end? | gap-probe | yes | store-only | The frame's *first* named consumer (per-company triage). Concrete single-company depth. | Tests whether one company's scattered signals compose into a triage card. | Reaches the per-company triage use case. | One company's full `signals/` + profile State. | Narrow (n=1); the cohort-readiness question (selected) generalizes the same finding and exposes the rollup gap the maps consumer actually needs. Folds in as a worked example. |
| Which captured companies have ≥2 comparable captures on a *traction* signal (not just any signal), so a velocity/delta is computable today? | gap-probe | yes | store-only | Sharpens MRL-012 onto traction specifically. | Comparability (ladder step 2) coverage. | Reaches the delta-readiness frontier. | `signals/<type>/*.json` count per dir + capture-date gaps. | Run 018 already mapped this for *all* signals (≈6 usable Trustpilot velocities); standalone it's a near-repeat. Becomes a sub-section of the selected read (the comparability rung). |
| Bounded-live: for 5 cohort brands, capture a fresh funding/SERP traction signal and compare to what the store holds — how stale/absent is the traction layer live? | gap-probe | yes | bounded-live | Would test the capture rung live. | Live traction freshness. | Reaches live traction. | 2 source families, ≤6 captures, ≤20 credits. | Deferred: the store-only readiness map is the higher-information reach this cycle and spends nothing; live freshness is a clean follow-up once the store-side gap is mapped. The coverage-radar recipe is already named (012/022/024). |
| (Alternatives surfaced at the supervised gate, not selected this cycle) Judgment-boundary probe (threat/whitespace for one anchor); SaaS price-visibility recipe-generalizability (queued run 028). | — | — | — | Recorded for the scout trail. | — | — | — | Judgment is the other open frontier (defer to a later supervised run); 028 is the least-ambitious queued option. |

## Selected Question(s)

1. **Across the captured store, what traction signal does any company actually expose today
   — at what grain, level-vs-delta, for how many companies — and is the store ready to roll
   a cohort traction-map per the traction-frame's 5-step ladder?**

Rationale: this is the lab's first read on the engine's named *future* axis and directly
serves the blocked maps consumer. It is a true gap-probe with real roadmap learning (where
the store sits on the frame's capability ladder), it is store-only and autonomous-safe, and
the store recon proves it is non-trivial (49 companies carry signals, but the signal mix is
heterogeneous and mostly level-only). The contracted failure mode is the load-bearing
guardrail: do not let "captured" masquerade as "comparable" or "rollup-ready," and do not
read non-traction signals (Wayback tenure, Exa neighbors) as traction.

## Selected Run Contract

This block is the canonical handoff to Loop 1. If it disagrees with the candidate table,
Loop 1 trusts this block.

```yaml
selected_question: "Across the captured store, what traction signal (capital/funding, demand, attention/visibility, growth/tenure) does any company actually expose today — at what grain, level-vs-delta, and for how many companies — and is the store ready to roll a cohort traction-map per the traction-frame's 5-step capability ladder (capture / comparability / accumulate / cohort-rollup / feed-judgment)?"
selected_slug: traction-signal-coverage-readiness
run_type: mixed
question_mode: calibration
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Profiled store companies (126, not 135 dirs — count profile.md, per MRL-001 run-027 stub caveat) as the universe; the signal-bearing subset is the 49 companies with a signals/ dir. Treat both as partial: signals/ presence is capture-campaign-driven, not market-representative."
likely_source_panel: "store/<domain>/signals/<source_type>/<captured_at>.json (source-type, capture count, latest clock, level vs delta); store/<domain>/profile.md frontmatter + Overview for any traction-bearing STATE field (founded, funding, ticker, headcount, parent); _design/2026-06-14-traction-frame.md (axis ladder + v2 evidence labels); SIGNALS.md + tools/README.md (which tool proxies which axis); MRL-012 / runs/018 (comparability findings)."
builder_lens: "Traction-signal readiness against the frame's 5-step ladder. Which rungs the store satisfies (capture, accumulate) vs not (comparability is partial per MRL-012; cohort-rollup is unbuilt; judgment is correctly withheld). Which captured signal-types are genuine traction proxies (sec_edgar=capital, trustpilot velocity=demand/trust-flow, serpapi/trends/ads=attention/visibility) vs NOT traction (wayback=tenure/continuity, exa=neighbors). Tests the State/Signals/Judgment boundary on the engine's open future-axis without creating any primitive."
reach_reason: "First lab read on the traction axis and the maps-consumer's blocking question. Reaches past every prior point-in-time State read into the Signals layer as a traction substrate, and probes cohort-rollup readiness the store has never been asked for."
allowed_sources:
  - "store/"
  - "_design/2026-06-14-traction-frame.md"
  - "_design/2026-06-15-traction-approach.md"
  - "SIGNALS.md"
  - "tools/README.md"
  - "experiments/00-market-read-lab/triage.md"
  - "experiments/00-market-read-lab/discovery-ledger.md"
disallowed_actions:
  - "No Firecrawl / live web / scraping / SERP / signal re-capture."
  - "No store/ mutation or write-back."
  - "No durable primitive / field / category / signal-tool creation."
  - "No emitting a traction/formidability score or verdict as truth (the frame's hard line)."
  - "No triage graduation."
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from local store files (signals/ + profile.md) and existing design docs; no spend, no live browsing, no write-back, no judgment emission."
loop1_failure_mode: "Two symmetric traps. (a) Under-claim: 'the store has no traction layer' — false, 49 cos carry signals and v1 shipped. (b) Over-claim: treating capture as readiness — most captures are level-only single snapshots, comparability is partial (MRL-012), cohort-rollup is unbuilt, and Wayback/Exa aren't traction at all. Must keep 'captured' vs 'comparable' vs 'rollup-ready' distinct, tag each signal-type to its real axis (or NONE), and say 'not found / not captured', not 'not there'. Must NOT emit any formidability/traction verdict — only map the evidence substrate."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. This run is deliberately a
calibration/gap-probe on the engine's open *traction* frontier — the value-read layer is a
real "where does the store sit on traction-readiness?" answer the roadmap's maps consumer
needs, and the gap-probe layer is the roadmap learning (which ladder rungs are built). The
contracted failure mode is the load-bearing guardrail: keep capture / comparability /
rollup distinct, pin every signal-type to its true axis, and never cross from Signals
substrate into an emitted Judgment.
