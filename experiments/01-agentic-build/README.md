# Agentic Build

**Status:** scaffolded operating experiment.

## Purpose

Agentic Build is a file-backed way to let agents handle bounded Truffle changes with
just enough framing, proposal review, patch review, and a short human decision surface
to stay trustworthy.

It is not a “task” system. It preserves useful reasoning, lets agents cut bad ideas early,
and keeps rejected work from disappearing.

## Core Terms

**"Change packet"** - one bounded proposed change to Truffle. It may ship, park, or get cut.

**"Build batch"** - an optional wrapper around two or three change packets when coordination
or one combined review is useful.

**"Decision surface"** - the short human-facing summary that says what to merge, hold,
revise, park, or cut.

## Top-Level Docs

- [`2026-06-21-frame.md`](2026-06-21-frame.md) - why this workflow exists, what it must protect, and what it is not.
- [`2026-06-21-proposal.md`](2026-06-21-proposal.md) - proposed v0 workflow.
- [`2026-06-21-lead-context.md`](2026-06-21-lead-context.md) - current lead-agent posture and judgment heuristics.

## Working Shape

Start with normal agent work. Use a **"change packet"** when the change needs preserved
framing, proposal review, staging, or a cut/park record. Use a **"build batch"** only
when several change packets need coordination.

```text
experiments/01-agentic-build/
  changes/
    YYYY-MM-DD-short-name/
      frame.md
      proposal.md
      proposal-review.md
      lead-decision.md
      implementation-notes.md
      packet-review.md
  batches/
    YYYY-MM-DD-short-name/
      batch-plan.md
      decision-surface.md
      changes/
        01-short-name/
          ...
```

Create `changes/` or `batches/` only when the first run starts.

## Constraints

- Read the lead context before acting as the lead agent.
- Keep batch work to three change packets by default.
- Stage implementation outside live Truffle usage: use a worktree or packet-local patch artifact, then let the lead apply approved work to the live checkout.
- Do not create new Truffle schema, entities, categories, monitors, or write-backs unless a packet explicitly frames and earns that scope.
- Parked and cut packets need a decision reason and `revive_if`.
