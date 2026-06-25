# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation (ID · kind) |
|---|---|---|---|
| **Capture** | The cheap, first-party traction floor the traction frame names (ticker / 10-Q for public filers) exists for beta-team yet is uncaptured — so the bottleneck is *unrun capture*, not discoverability, for at least the public-filer case. | beta-team ticker `BETA` + 10-Q (profile.md:123); `0/8` signals (C1). | S1 · surprise |
| **Structure** | The decisive frontier is the **State vs Signals** boundary: momentum is a Signals/time-axis fact; a single-capture State store carries only levels. The read correctly refused to dress a level table as momentum (after a VR1 correction). | read.md Lead/Gap Map; all `captured_at: 2026-06-14`. | G1 · gap; VR1 · risk-miss |
| **Query / access** | A momentum cohort roll-up (traction frame #4) has no substrate to query — `signal_delta.py` was never run here, so there's nothing to roll up. Sharpens run-029's store-wide census onto the cohort-comparison question. | C1; run-029 census. | G2 · gap |
| **Freshness / automation** | `captured_at` is per-profile freshness, not per-event recency — recent ($380M Apr 2026) and stale (Series B Apr 2025) events sit under one clock, so "what moved lately" is prose-only. | all 8 clocks identical; S3. | S3 · surprise |
| **Synthesis** | Strong: the read kept State/level vs Signals/delta distinct and labeled the momentum ranking as an *absent* Judgment, not a produced one. The 3-pass review caught a real "collapses onto maturity" overreach (capital ≠ maturity; cfs counterexample). | read.md Market Pattern; VR1. | S2 · surprise; VR1 · risk-miss |
| **Guardrails** | Source-rigor held: 7/8 figures flagged self-reported; only beta-team auditable; absence stated as not-captured (C1 limits), never not-true. No spend, no live browse, store-only contract honored. | C1/C2 grades; run-notes exit check all pass. | (no new row) |

## Lenses

**Steward** — Honest. State/Signals/Judgment stayed separated; the run's whole point is
*refusing* to emit a momentum Judgment the store can't ground. Self-reported grade and
single-capture limits are visible. The VR1 catch (capital ≠ maturity) removed the one place
the read had over-unified.

**Dev Agent** — The repeatable toil this exposes is *not* yet worth a helper: a momentum
read needs a 2nd capture, not a query recipe over the 1st. The grep-verifiable contract that
*would* matter (if anything graduates) is "public-filer → cheap SEC/IR Signal capture"; but
that's a capture-worklist item, spend-gated, not a synthesis helper. Resist adding a
traction-magnitude field — units don't commensurate (G3), so it would launder false
precision.

**Founder** — The asset compounds cheaply: C1 (signals-absence) + C2 (level table) are warm
files that scope a future traction probe without re-reading 8 profiles. No ontology gravity
added; "no new primitive needed now" is the right, light call. The cohort-momentum consumer
that would justify the roll-up does not exist yet.

## Recommendation

- **No-op / keep as observations.** "No new primitive needed now" stands; the payload is a
  roadmap finding for the traction frame (the missing piece is comparability #2 +
  durable-home #3, not capture #1).
- **Watch for recurrence** (`learning_tags`): `traction-readiness` (now 2nd sighting after
  run-029 — a learning pass may want to cluster these), `freshness-monitoring` /
  `source-rigor` (single-capture, self-reported levels), `denominator-reconciliation`
  (unit-incommensurable capital; named-8 not an industry draw).
- **Severe `risk-miss` to surface now:** none. VR1 is a precision overreach caught and
  corrected in-run, not a shipped defect.

## Raw learning to preserve

Developer-lane sightings are logged in `run-notes.md` Observations; a builder-frontier row
**DR1** added there (the cheap-floor-is-unrun-not-undiscoverable framing, sharpening S1). No
lessons proposed; no system change implemented or offered.
