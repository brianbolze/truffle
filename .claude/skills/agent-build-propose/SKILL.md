---
name: agent-build-propose
description: Create or revise a review-ready Agentic Build proposal.md for one Truffle change packet. Use when explicitly asked to run agent-build-propose or draft an Agentic Build proposal; stop before implementation.
disable-model-invocation: true
argument-hint: <change request, slug, or existing packet path>
---

$ARGUMENTS

## Purpose

Create or revise one review-ready `proposal.md` for an Agentic Build change packet.

## Task

You are not being asked to complete the requested Truffle change. You are being
asked to turn the user's request into a review-ready proposal for one bounded
Agentic Build change packet.

Given the request:

1. Identify the proposed change.
2. Define what success would mean.
3. Define acceptance checks for that success.
4. Compare the smallest viable approach with one or two alternatives.
5. Write or update `proposal.md`.
6. Stop before implementation.

## Required Context

Read these before writing:

- `experiments/01-agentic-build/README.md`
- `experiments/01-agentic-build/2026-06-21-proposal.md`
- `experiments/01-agentic-build/2026-06-21-lead-context.md`
- `.claude/skills/agent-build-propose/proposal-template.md`

## Output

- If the user gives an existing packet path, update that packet's `proposal.md`.
- Otherwise create `experiments/01-agentic-build/changes/YYYY-MM-DD-short-slug/proposal.md`.
- Choose a short lowercase hyphen slug from the requested change.
- Use `proposal-template.md` as the structure.

## Rules

- Only create or update the packet `proposal.md`; do not make implementation changes.
- Keep frame context inside `proposal.md`; if the problem is too unclear for that, stop and say a separate frame is needed.
- Fill the required fields: `risk`, `write_scope`, `spend_stop`, `acceptance_checks`, `escalate_if`.
- If a required field is unknown, write `unknown` plus why.
- Compare the smallest viable option with one or two alternatives before recommending.
- Prefer the simplest option that can meet the acceptance checks this proposal defines.
- Follow the size defaults in `2026-06-21-lead-context.md`.
- Treat `high` risk as planning-only unless Brian explicitly approves implementation later.
- Notice something worth remembering that's *out of scope* for this packet (a Truffle gap, a build-process friction, a recurring correction)? Log it as an observation per [`learning/AGENTS.md`](../../../experiments/01-agentic-build/learning/AGENTS.md) — capture only; the review pass decides what to do with it.

## Final Response

End with:

- proposal path
- one-sentence recommendation
- risk
- review needed: approve, revise, park, or cut before implementation
- `No implementation changes were made.`
