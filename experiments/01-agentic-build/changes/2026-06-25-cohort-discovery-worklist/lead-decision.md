# Lead Decision: Cohort Discovery Worklist

Date: 2026-06-25
Decision: accept-for-implementation - approved by Brian.
Packet: `proposal.md` + `proposal-review.md`
Strategic frame: [`_design/2026-06-26-coverage-strategy-frame.md`](../../../../_design/2026-06-26-coverage-strategy-frame.md)
Current outcome: validation is complete and the broad verb is held; see [`decision-surface.md`](decision-surface.md).

## Decision

Brian approved the revised proposal after the independent proposal review recommended
`revise-once` and the proposal was tightened around concrete validation sets.

Implementation is approved as a validation packet, not as a reusable engine verb. Work
must happen in a git worktree and stay packet-local.

## Scope Approved

- Freeze packet-local validation inputs.
- Run dry discovery validation against:
  - masked telehealth holdouts from Notion Organizations;
  - conversation-intelligence / AI meeting tools, with adjacent transcription-dev tools separated.
- Write receipts and `implementation-notes.md`.

## Boundaries Held

- No edits to `store/`, `tools/`, `skills/`, `QUERYING.md`, schemas, or Signals paths.
- No `/research-company` captures and no store writes.
- No reusable `/cohort-discovery` skill in this packet.
- Notion Organizations is an evaluation oracle for the telehealth holdout, not a discovery source.
- If the union does not beat the best single feeder, park or downscope rather than pass by explanation.

## Brian Amendment During Implementation

F0/F1 Notion rows are not a strong pollution set because Notion is already curated. Treat
them only as a secondary over-rank check. The hard pollution gate is Brian's curated
low-formidability / wrong-type negatives plus a human review checkpoint over generated
not-in-store and uncertain candidates before final scoring.

## Risk

Medium. The packet uses live external discovery and may shape future agent authority, but
does not change the engine contract or write to the store.
