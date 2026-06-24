---
name: agent-build-review
description: Independently critique one Agentic Build artifact — a frame, a proposal, or an implemented change — surfacing findings plus a recommended lean, never a decision. Use when explicitly asked to run agent-build-review, or to get an independent review of a frame/proposal/change before the lead decides. NOT the learning-consolidation pass (that's agent-learning-review).
disable-model-invocation: true
argument-hint: [frame|proposal|change] <packet path, or the thing to review>
---

$ARGUMENTS

## Purpose

Give one independent critique of a single Agentic Build artifact — a `frame`, a
`proposal`, or an implemented `change`. Surface findings and a recommended lean so the
lead can decide. You do **not** decide (accept / revise / park / cut / merge is the
lead's call, or Brian's), and you do not edit what you review.

## Independence — spawn if you authored it

Independent review is required; self-review is not enough.

- **You authored the artifact this session** (wrote the frame/proposal, or made the
  change) → spawn a fresh sub-agent to review it. Give it a short kickoff brief — why
  it's reviewing, the goal, the mode, and what to read — per
  [`effective-prompts.md`](../../docs/effective-prompts.md) (#8: the why + goal +
  pointers, not the how). Reviewing is judgment — let the reviewer inherit the main model.
- **You didn't author it** → you're already independent; review directly.

## Required context

Read before reviewing — these carry the rules; don't restate them:

- [`2026-06-24-reviewer-context.md`](../../../experiments/01-agentic-build/2026-06-24-reviewer-context.md) — reviewer disciplines, what to stress per mode, the lean to recommend, current posture.
- The rubric reviewer-context names for your mode, plus the packet's own docs
  (frame.md / proposal.md / the diff + the accepted proposal).

## Task

1. Resolve the mode — first argument (`frame` | `proposal` | `change`), inferred from
   the target if omitted. One artifact per run.
2. Read the context above, then read the artifact itself — actually read it; don't
   critique from memory.
3. Critique against the mode's rubric and the reviewer disciplines.
4. Write findings first, then a recommended lean (in the lead's decision vocabulary —
   see reviewer-context — or plain words if none fits), clearly marked as a recommendation.
5. Out-of-scope thing worth remembering? Log an observation per
   [`learning/AGENTS.md`](../../../experiments/01-agentic-build/learning/AGENTS.md) —
   capture only, never a fix.
6. Stop. Don't decide; don't edit the artifact.

## Output

- With a packet → write findings to it: `frame` → `frame-review.md`,
  `proposal` → `proposal-review.md`, `change` → `packet-review.md`.
- Standalone (no packet) → return the findings inline.

## Final response

End with:

- review path (or `inline`)
- mode + what was reviewed
- findings, most important first
- recommended lean — marked as a recommendation; the lead decides
- `No decision was made; the reviewed artifact was not edited.`
