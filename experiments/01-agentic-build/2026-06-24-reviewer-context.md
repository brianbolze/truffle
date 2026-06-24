# Reviewer Context: Agentic Build

**Date**: 2026-06-24
**Status**: first draft for v0 review posture.

## What This Is

Mutable judgment context for the review agent. The
[`agent-build-review`](../../.claude/skills/agent-build-review/SKILL.md) skill is the
durable recipe (modes, spawn rule, where to write); this doc is how to *judge*.

Keep it short, and **point, don't restate**. Risk calibration, hard lines, posture,
decision vocabulary, and size defaults live in
[`2026-06-21-lead-context.md`](2026-06-21-lead-context.md) — defer to it, never
re-document it. Lessons about *how to review* sharpen this doc; the recipe stays put.

## Reviewer Job

One independent critique of a frame, proposal, or implemented change: surface findings
and a recommended lean so the lead can decide. Never decide; never edit what you reviewed.

## Posture (v0)

Conservative, tracking the lead's [current posture](2026-06-21-lead-context.md). One
reviewer per artifact; findings-first, only as long as the findings require. Loosen only
after real runs show it catches the right things without becoming drag.

## Disciplines

Most review misses so far were hygiene failures, not missed checks. Hold these:

- **Check before asserting.** Read the actual artifact / diff; never critique from memory.
- **Absence isn't proof.** "Not found" ≠ "not there" — say which, and flag what the
  review couldn't see. A clean pass is not "no issues."
- **Don't overfit your own findings.** One smell is not a pattern.
- **Findings-first, short, plain.** Lead with what matters; no padding, no coined jargon.

## What To Stress, By Mode

Point to the rubric; these are emphases, not a checklist.

- **frame** — grade the framing itself; the `/frame` skill is context on what a frame is
  *for*, not a grading rubric, and [lead-context](2026-06-21-lead-context.md) holds the
  value / pillar / persona links. Headline: **has it jumped to solution-space?** Then: is
  the problem **root-caused**, or are only symptoms named? what **bigger problem(s)** does
  it touch? is the **success condition testable**? is it anchored to a **value pillar /
  persona**? what's missing — non-goals, open questions? Frames leak solutions even when
  told not to — catching that is this mode's main job.
- **proposal** — rubric: the packet's stated fields (`risk`, `write_scope`,
  `spend_stop`, `acceptance_checks`, `escalate_if`). Stress scope creep; schema /
  persistence / new-entity risk; hidden standing infrastructure; additive-only changes
  (what does it replace?); whether the simplest option was really considered.
- **change** — rubric: the
  [`review-change`](../../.claude/skills/review-change/SKILL.md) skill (engine checklist)
  **+** the accepted proposal. Stress whether the patch matches what was accepted;
  whether `acceptance_checks` pass; whether it stayed in `write_scope`; and the
  **failure / unattended path** (what happens on crash, or when no one's watching).

## Recommended Lean

End with a lean in the lead's decision vocabulary — the **Decision Rules** in
[`2026-06-21-proposal.md`](2026-06-21-proposal.md) — or plain words if none fits. Mark it
clearly as a recommendation; the lead decides.

## Learning Loop

When a review surfaces something worth remembering, log an observation per
[`learning/AGENTS.md`](learning/AGENTS.md) — capture only. Accepted lessons about *how
to review* graduate into this doc.
