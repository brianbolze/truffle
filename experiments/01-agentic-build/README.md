# Agentic Build

**Status:** scaffolded operating experiment.

## Purpose

Agentic Build is a file-backed way to run small Truffle improvement batches with worker agents, proposal review, optional revisions, implementation review, and a final human merge gate.

The point is not to add a task system. The point is to let agents try bounded solutions while preserving the problem frame and learning when a solution gets cut.

## Core Rule

**Lead agent owns the merge.** Workers can propose and implement. Reviewers can approve or request changes. The lead agent can accept, request one revision, park, or cut a packet before or after implementation.

Rejected work is not wasted if the `frame.md` and review notes survive.

## Top-Level Docs

- [`2026-06-21-frame.md`](2026-06-21-frame.md) - why this workflow exists, what it must protect, and what it is not.
- [`2026-06-21-proposal.md`](2026-06-21-proposal.md) - proposed v0 operating model.

## Batch Shape

```text
experiments/01-agentic-build/
  README.md
  2026-06-21-frame.md
  2026-06-21-proposal.md
  batches/
    YYYY-MM-DD-short-batch-name/
      batch-plan.md
      merge-docket.md
      decisions.md
      packets/
        01-short-packet-name/
          frame.md
          proposal.md
          proposal-review.md
          lead-decision.md
          implementation-notes.md
          packet-review.md
```

Create `batches/` only when the first batch starts.

## Packet Lifecycle

1. `frame.md` - worker states the problem before solutions.
2. `proposal.md` - worker considers options and recommends one.
3. `proposal-review.md` - separate reviewer audits the proposal.
4. `lead-decision.md` - lead accepts, requests one revision, parks, or cuts.
5. `implementation-notes.md` - worker implements only after acceptance.
6. `packet-review.md` - reviewer audits the implemented patch.
7. `merge-docket.md` - lead summarizes what Brian should merge, hold, or cut.

## Constraints

- Keep batches to **3 packets by default**.
- Keep packet write sets disjoint, or use git worktrees.
- Prefer docs, recipes, lints, self-contained scripts / tools, and small code changes over new infrastructure.
- Do not create new Truffle schema, entities, categories, monitors, or write-backs unless a packet explicitly frames and earns that scope.
- One revision phase per packet. After that, the lead chooses: implement, park, or cut.

## First Candidate Batch

The natural first batch is `mrl-quickwins`:

- `cohort-discovery-verb`
- `denominator-and-capture-candidate-receipts`
- `signal-confound-rules`

Code hygiene such as `sec_edgar` delta and `captured_at` lint should be a second batch unless the first batch stays unusually small.
