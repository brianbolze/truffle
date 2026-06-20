# Scout

## Prior Context Read

- `triage.md`: Reviewed. Mature/graduation-ready pressure clusters: MRL-002 (State-read query recipes, 6 surfaces), MRL-001 (denominator anchored-only under-count, 5 cohorts), MRL-008 (signal-confound convention), MRL-005/006 (backend relation edges, now two axes/two cohorts — graduation-ready), MRL-010 (review bodies, graduation-decision-ready), MRL-011 (substitute relation as Judgment, 1 sighting). Triage is heavily weighted to point-in-time State reads and relation reads.
- `scout-context.md`: Two-test selection (value vs generic Claude+search; design pressure/gap). Seven design uncertainties. The **change pulse / freshness** uncertainty and the **"trust the cache over time"** value job are the least-touched across the contract-era runs (004–017) — every one of those is a *point-in-time* State or Signals read. Run 002 (pre-contract) is the only freshness-adjacent run, and it was external news monitoring, not a diff of captured signals.
- Last 3 `run-notes.md` files (015 cross-cohort table-stakes, 016 non-GLP-1 backend, 017 Hone substitute map): all point-in-time; all reinforced MRL-001/002/005. None touched temporal change. Post-candidate check: nothing in the last 3 originates this candidate; they confirm the freshness axis is a genuine gap, not a parked next step.
- Current run artifacts: fresh scaffold (018), Scout-only.

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| Across the captured store, which brands' signals show a **detectable change between their ≥2 captures** (Trustpilot review velocity, SEC funding footprint, SERP visibility), and can the store support a "trust-the-cache-over-time" / change-pulse read **store-only** today? | mixed | yes | store-only | First temporal/diff read in the lab; tests the least-touched design uncertainty (change-pulse/freshness) and least-served value job (trust the cache over time); exercises `signal_delta.py`. Intrinsically store-only — generic Claude+search cannot diff *your* captured snapshots. | `signal_delta.py` runs over the ~13 domains with ≥2 captures; deltas + comparability vetoes recorded with capture timestamps; "no detectable change" stated as not-found, not no-change. | Thin temporal depth (~13 domains, mostly Trustpilot, ~1-week window) read as a market census; signal jitter (Trustpilot score noise, SERP volatility) mistaken for real change; two snapshots ≠ continuous monitoring. |
| In the captured derm/skincare or hair-loss cohort, what offer/access structures are table stakes vs differentiated? | market | yes | store-only | A cohort the lab hasn't read. | `anchor_category` grep + offer field extract. | Re-runs the mature MRL-002 recipe on a new surface — low *design* value; reader value only. |
| Which captured brands' `signals/` integrity flags (paid_profile, schema_drift, AIO-outage veto) would silently corrupt a naive Signals read, and how prevalent are they? | system-test | yes | store-only | Stress-tests MRL-008's confound convention at corpus scale. | Parse every `signals/*/*.json` for integrity siblings. | Overlaps heavily with MRL-008's already-acknowledged convention; risks re-confirming, not advancing. |
| Across the store, which brands carry an SEC/Form-D footprint AND a Trustpilot trust signal — does funding presence correlate with review posture? | market | yes | store-only | Cross-signal join. | Two signal reads joined per domain. | Correlation-from-tiny-n false confidence; MRL-007/008 already cover signal grain. |
| For brands captured twice at the *profile* level, what changed in offerings/pricing prose between captures (not just signals)? | system-test | partial | local-existing | Tests profile-level freshness, the deeper version of the change-pulse job. | Two `profile.md`/`offerings.md` snapshots per domain. | Most domains likely have only one profile capture; may be a near-empty denominator (itself a finding, but risk of thin read). |
| Which captured cohorts have the **stalest** captures (oldest `captured_at` / store clock), and which load-bearing fields are most at risk of being wrong? | system-test | yes | store-only | A freshness/staleness audit — adjacent to change-pulse but about decay, not delta. | Capture-clock scan across modules. | Audit-shaped, not a market read; weaker reader value; "stale ≠ wrong." |

## Selected Question(s)

1. **(recommended)** Across the captured store, which brands' signals show a detectable change between their ≥2 captures (Trustpilot review velocity, SEC funding footprint, SERP visibility), and can the store support a "trust-the-cache-over-time" / change-pulse read store-only today?

Rationale: clears both tests cleanly. **Value test:** the answer is intrinsically store-only — no external tool can diff Truffle's own append-only signal snapshots, so it beats generic Claude+search by construction; it serves the under-served "trust the cache over time" job. **Design test:** it is the *first* temporal/diff read in 18 runs, directly probing the change-pulse/freshness design uncertainty and the `signal_delta.py` machinery (does the store have enough temporal depth to answer a change-pulse read today, and what's the honest grain?). A likely honest outcome — "the store can answer this for ~13 domains over a ~1-week window, mostly Trustpilot velocity; broader change-pulse needs more capture cadence, not a new primitive" — is itself valuable freshness-pillar learning.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "Across the captured telehealth store, which brands' signals show a detectable change between their two-or-more captures (Trustpilot review velocity, SEC/Form-D funding footprint, SERP visibility), and what does this first temporal/diff read teach about whether the store can support a 'trust the cache over time' / change-pulse read store-only today?"
selected_slug: signal-change-pulse-readiness
run_type: mixed
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Store domains with >=2 captures in any one signal source_type (~13 observed: trustpilot dominant — agelessrx, eden-health, hims, honehealth, hydramed, joinamble, joinfridays, maximustribe, sermorelin; sec_edgar — hims, honehealth, maximustribe, waldo; serpapi — niagenplus, waldo). Treat as a partial, capture-cadence-bound set, NOT a market census."
likely_source_panel: "Local only: tools/signal_delta.py over store/<domain>/signals/<source_type>/<captured_at>.json pairs. No external fetch."
allowed_sources:
  - "store/"
  - "tools/signal_delta.py"
  - "tools/README.md and tools/signal_delta.md (tool semantics)"
  - "experiments/00-market-read-lab/triage.md"
disallowed_actions:
  - "Any live fetch, Firecrawl spend, or capture (the tool is a read-only consumer; do not run capture tools to manufacture a second snapshot)."
  - "Mutating store/ or writing back to any project system."
  - "Creating durable primitives, a monitor, or a stored change/diff object."
  - "Treating two snapshots as continuous monitoring or a market census."
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Pure local diff of already-captured signal envelopes via an existing read-only tool; no spend, no fetch, no write-back. The denominator is bounded by what is already on disk."
loop1_failure_mode: "Overstating change-pulse readiness from a thin, Trustpilot-heavy, ~1-week denominator; or mistaking signal jitter / rolling-window artifacts / paid-profile solicitation for real market change. Must report deltas with capture timestamps, comparability vetoes, and gap-days, and say 'not found' for no-detected-change rather than 'no change occurred'."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. This run deliberately picks the
least-tested design uncertainty (change-pulse/freshness) and least-served value job
(trust the cache over time) after confirming, pre-selection, that the store has just
enough temporal depth (~13 domains with ≥2 captures, ~June 8 → June 15 window) and a
working diff tool (`signal_delta.py`) to make the read tractable store-only. The
expected high-value outcome is a calibrated readiness verdict on the freshness pillar,
not a market census.
