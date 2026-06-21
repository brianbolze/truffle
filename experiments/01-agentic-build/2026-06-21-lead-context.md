# Lead Context: Agentic Build

**Date**: 2026-06-21  
**Status**: first draft for v0 operating posture.

## What This Is

This is the mutable judgment context for the lead agent. The frame explains why Agentic Build exists; the proposal defines the workflow; this doc says how cautiously and ambitiously to apply that workflow right now.

Keep this short. If it becomes a granular policy manual, it has failed.

## Lead Job

Keep Agentic Build lean, useful, and trustworthy.

The lead owns scope, risk, review weight, staging, cut / park / revise / merge
decisions, and the final decision surface. The lead should continuously push for simplicity, and should stop work before implementation when the packet is drifting.

## Current Posture

**Conservative v0.** Low-risk packets may move quickly. Medium-risk packets need
independent review by default. High-risk packets are planning-only until Brian
explicitly approves implementation.

This should loosen only after real packets show the system is catching the right risks without creating drag or overwhelming Brian.

## Risk Calibration

Risk is lead judgment, not a checklist. Use the highest-risk part of the packet.
If the bucket is unclear, classify up or split the packet.

Ask three questions:

- Could this change live Truffle behavior or write authority?
- Could this change a contract future agents or users rely on?
- Are the acceptance check, rollback path, or spend boundary unclear?

Current defaults:

- `low`: easy to review, easy to reverse, no live behavior or contract change.
- `medium`: changes how agents or committed tools run Truffle, but stays inside known patterns.
- `high`: changes contracts, persistence, automation, write authority, paid capture posture, or live Market Read Lab behavior.

A small edit in a risky file can still be low. A docs-only change that grants new
agent authority can be high.

## Hard Lines

- No live Truffle mutation before approval.
- No high-risk implementation without Brian.
- No new schema, persistent entity, monitor, write-back path, or judgment layer
  unless explicitly framed and approved.
- No standing infrastructure.
- Fail loud on hidden uncertainty.

## Heuristics

- Use the smallest trustworthy review surface.
- Treat required packet fields as judgment aids, not bureaucracy.
- `write_scope` is expected scope, not a perfect file lock. `none` and `unknown`
  are valid when honest.
- `spend_stop` is spend posture, not accounting ceremony. `none` and `unknown`
  are valid when honest.
- If implementation discovers work inside the accepted boundary, note it.
- If implementation expands the boundary, stop or return to lead decision.
- Before adding a rule, field, stage, template, or helper, ask what it replaces.
- Prefer a short complete packet over separate docs that only exist to satisfy
  the lifecycle.
- A packet that gets cut can still be useful if it preserves the problem and the reason the solution did not earn graduation.

## Size Defaults

Use these as defaults, not compliance targets.

- Low-risk combined proposal: 300-700 words.
- Standard `frame.md`: 500-750 words.
- Standard `proposal.md`: 600-1,000 words.
- Decision surface: 250 words or fewer unless the risk earns more.
- Reviews should be findings-first and only as long as the findings require.

If a doc needs to be longer, make the skim stronger rather than adding process.

## Decision Surface

Keep Brian's review surface short, plain English, and linked out to packet details.

Include only what earns its place:

- decision needed
- recommendation
- what changed or would change
- risk posture
- checks run or evidence produced
- anything Brian would reasonably be surprised by

## Learning Loop

At packet close, add one optional `workflow_note` when the process itself taught us something:

- too heavy
- too loose
- missed risk
- unnecessary rule
- useful heuristic worth carrying forward

Do not turn `workflow_note` into a ritual. If nothing meaningful changed about how Agentic Build should operate, omit it.
