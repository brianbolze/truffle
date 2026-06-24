---
name: agent-build-decide
description: Synthesize one Agentic Build change packet into a short decision surface for Brian and recommend a call. Brian decides — this verb does NOT decide, merge, or edit the packet's work. Use when explicitly asked to run agent-build-decide, or to turn a reviewed packet into Brian's decision surface. NOT the independent critique (that's agent-build-review).
disable-model-invocation: true
argument-hint: <packet path, or the packet to summarize>
---

$ARGUMENTS

## Purpose

Turn one change packet's current state into a **decision surface** for Brian: the short,
plain-English digest he decides from. You synthesize and recommend; **Brian decides.**

This is the lead's compression step. The review files are detailed *for the lead*; the
decision surface is short *for Brian*. You do not record the decision, merge anything, or
edit the packet's work. One packet per run.

## Required context

Read before writing — these carry the format and the rules; don't restate them:

- [`2026-06-21-lead-context.md`](../../../experiments/01-agentic-build/2026-06-21-lead-context.md) — the **Decision Surface** section (what the surface includes and how short it is) plus the lead's risk posture and hard lines.
- The packet's own docs — whatever exists: `proposal.md`, any `proposal-review.md` /
  `packet-review.md`, `frame.md`, `implementation-notes.md`.
- For the recommendation vocabulary: the **Decision Rules** in [`2026-06-21-proposal.md`](../../../experiments/01-agentic-build/2026-06-21-proposal.md).

## Task

1. Read the packet's docs and the context above.
2. Synthesize the packet's current state into a decision surface, in the format the
   lead-context **Decision Surface** section defines — no more than it asks for.
3. State the **decision needed** for the packet's current stage, and end with a
   **recommendation** in the decision vocabulary (the **Decision Rules** named in
   Required Context) — clearly a recommendation; Brian decides.
4. Report checks honestly. If no independent review exists in the packet, say so on the
   surface — don't let an unreviewed packet look ready. Absence isn't proof.
5. Out-of-scope thing worth remembering? Log an observation per
   [`learning/AGENTS.md`](../../../experiments/01-agentic-build/learning/AGENTS.md) —
   capture only, never a fix.
6. Stop. Don't decide, don't merge, don't edit the packet's work.

## Output

- Write the surface to `decision-surface.md` in the packet.
- Also return it inline in your final response (it's already short).

## Final response

End with:

- decision-surface path
- the surface itself
- your recommendation — marked as a recommendation; Brian decides
- `No decision was made; nothing was merged or edited.`
