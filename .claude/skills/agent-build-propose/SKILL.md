---
name: agent-build-propose
description: Create or revise a review-ready Agentic Build proposal.md for one Truffle change packet. Use when explicitly asked to run agent-build-propose or draft an Agentic Build proposal; stop before implementation.
disable-model-invocation: true
argument-hint: <change request, slug, or existing packet path>
---

$ARGUMENTS

## Purpose

Create or revise one review-ready, plan-only `proposal.md` for a bounded Agentic Build change packet.

Agentic Build is not the default for every task. Its job is to preserve reasoning, compare approaches, gate risky changes, or keep a cut/park record when that weight is earned.

## Work Protocol

Before writing, do your work "offstage". Do not narrate this checklist unless it changes the recommendation.

1. **Frame the capability, not just the request.** Identify the real job, success condition, non-goal, and what decision this proposal should unlock. If the request could mean materially different jobs, ask one clarifying question before writing.
2. **Check whether a packet is warranted.** If the request is an obvious low-risk direct fix, already answered by prior work, or too unclear to frame inside `proposal.md`, stop and report the smaller next move instead of manufacturing a proposal.
3. **Stretch before you shrink.** In scratch, consider several solution families before converging: the boring/small fix; the best prior-art path; a new-source or new-tool path; and a more ambitious version that would change the system's capability if it worked. Prior work is evidence, not the ceiling.
4. **Find the smallest meaningful slice.** For each promising family, ask: what is the smallest probe, MVP, or reversible change that would move us forward and teach something real? Prefer the slice that tests the important uncertainty, not the slice that merely creates the least surface area.
5. **Check prior art.** Search targeted local surfaces before proposing new machinery: `experiments/`, `_design/`, `BACKLOG.md`, relevant `skills/`, relevant `tools/`, and existing packets. Ask what each prior artifact proves, what it falsifies, and what it did not explore. Mention prior art only when it affects the recommendation, risk, or scope.
6. **Name the load-bearing value claim.** What must be true for this proposal to be worth building? If the proposal uses new tools, sources, or mechanisms, name the bet they are making.
7. **Define the cheapest disconfirming check.** What small test, fixture, dry run, known case, or review would reveal that the proposal is well-formed but useless?
8. **Converge hard.** Recommend the simplest path that preserves the upside and can pass the value check. Compare only the strongest 2-3 finalist options in `proposal.md`; keep discarded scratch options offstage unless one changes the recommendation.

## Required Context

Read these before writing:

- `experiments/01-agentic-build/README.md`
- `experiments/01-agentic-build/2026-06-21-proposal.md`
- `experiments/01-agentic-build/2026-06-21-lead-context.md`
- `.claude/skills/agent-build-propose/proposal-template.md`

Read additional docs when the proposed change touches their authority surface. Do not summarize orientation docs in the proposal unless they change the recommendation.

## Output

- If the user gives an existing packet path, update that packet's `proposal.md`.
- Otherwise create `experiments/01-agentic-build/changes/YYYY-MM-DD-short-slug/proposal.md`.
- Choose a short lowercase hyphen slug from the requested change.
- Use `proposal-template.md` as the structure; do not add new sections unless the proposal truly needs them.

## Rules

- Only create or update the packet `proposal.md`; do not make implementation changes.
- `proposal.md` is a **plan-only** artifact — the thing `proposal`-mode review judges and the lead decides *before* any code. Keep implementation evidence out of it: status never flips to `implemented`, and receipts / gate logs land in `implementation-notes.md` after the decision. Don't let the proposal and the change collapse into one file — that boundary is what lets review gate instead of just narrate.
- Keep frame context inside `proposal.md`; if the problem is too unclear for that, stop and say a separate frame is needed.
- Fill the required fields: `risk`, `write_scope`, `spend_stop`, `acceptance_checks`, `escalate_if`.
- If a required field is unknown, write `unknown` plus why.
- Diverge broadly in scratch, then compare only the strongest 2-3 finalist options before recommending.
- Prefer the simplest option that can meet the acceptance checks this proposal defines.
- Follow the size defaults in `2026-06-21-lead-context.md`.
- Treat `high` risk as planning-only unless Brian explicitly approves implementation later.
- Log an observation only for a reusable miss, Brian correction, severe risk, or recurring process friction. Routine work-phase judgment stays private.

## Final Response

End with:

- proposal path, or `no proposal written` plus why
- one-sentence recommendation
- risk, if a proposal was written
- review needed: approve, revise, park, or cut before implementation
- `No implementation changes were made.`
