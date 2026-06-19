---
created: 2026-06-19
authors: codex
status: frame
---

# Frame: Market Read Lab triage steward

## 30-second skim

The triage agent should be a **triage steward**, not a builder.

It can edit the queue: reclassify priority/status, reorder items, merge duplicates, tighten titles, rewrite `evidence_summary`, and clarify `proposed_next_step`. That is the point of the role.

It still should not graduate items into Truffle system changes, mutate `store/`, alter code/templates, spend, browse live, or write to project systems. Graduation stays human-gated until a narrow quick-win class is explicitly allowed.

The key split:

- **Run agents submit evidence.** They may add a new item or append dated evidence/color to an existing item, but should not rewrite the canonical item.
- **Triage steward curates the queue.** It periodically folds recurring evidence into a cleaner canonical item, changes priority/status, dedupes, and prepares human-ready graduation candidates.

This solves the current tension: runs stay append-only and low-authority; the queue still improves over time.

## Working Model

### Run Agent Authority

Run agents may:

- submit a new triage candidate;
- append a dated **Evidence Log** entry to an existing item;
- suggest priority/status changes in review notes;
- link receipts, source runs, and related items.

Run agents may not:

- rewrite existing YAML fields;
- reorder the Queue;
- merge or mark duplicates;
- edit `Human Notes`;
- graduate, spike, or implement system changes.

### Triage Steward Authority

The steward may edit non-human parts of `triage.md`:

- reclassify `priority` and `status`;
- reorder Queue items by current priority;
- rewrite `title`, `evidence_summary`, and `proposed_next_step` for clarity;
- fold repeated Evidence Log entries into the canonical YAML summary;
- mark duplicates and link the canonical item;
- move resolved items when resolution is explicit;
- draft graduation candidates for Brian.

The steward may not:

- edit `Human Notes`;
- change Truffle code, templates, schema, or store artifacts;
- create durable primitives or category/cohort objects;
- write to Notion Roadmap or downstream Pantry systems;
- treat triage pressure as approval to build.

## Priority Convention

Use Brian's labels exactly.

| Priority | Meaning |
|---|---|
| `P0` | Urgent correctness/safety issue. Fix now. |
| `P1` | Must fix/do in the next batch. Trigger is met, cost/risk is recurring, and the next response is clear. |
| `P2` | Should fix/add, but competes with other items. Real pressure, not urgent. |
| `P3` | Watch / nice-to-have. Usually one sighting, sparse evidence, or prerequisite pressure. |
| `Low` | Minor cleanup, weak signal, or non-urgent convention candidate. |
| `Out-of-scope` | Project judgment, one-off research idea, ontology gravity, or not a Truffle job. |

Do not promote priority just because an idea is interesting. Promote when repeated evidence shows a trust, autonomy, toil, or corpus-health cost.

## Status Convention

Keep the workflow small:

`Submitted -> Researching -> Acknowledged / Duplicated / Resolved`

- **Submitted:** queued pressure, not yet accepted.
- **Researching:** actively being compared, clarified, or de-risked.
- **Acknowledged:** accepted as real pressure, but not implemented.
- **Duplicated:** merged into or superseded by another item.
- **Resolved:** implemented, intentionally closed, or explicitly declined.

Do not add a separate `Graduated` status yet. If something is ready, leave it as a graduation candidate in the item or in a steward note.

## Steward Rubric

For each item, ask:

1. **Is the pressure real?** Evidence from runs, receipts, reviews, or repeated friction.
2. **What kind of pressure is it?** Capture, structure, query/access, freshness, synthesis, guardrail, corpus-health, or out-of-scope.
3. **What changed since the first sighting?** Same root cause, broader family, trigger met, or no new signal.
4. **What is the smallest response?** No-op, watch, wording cleanup, template convention, QUERYING recipe, helper, backlog item, roadmap candidate.
5. **What is the risk?** Durable identity, ontology, write-back, external spend, weak current claims, or breaking contracts.
6. **Who benefits?** Strategist, Pantry, First Contact, Steward, Dev Agent, Beekeeper-Brian, Founder.

WSJF is useful as a lens, not a spreadsheet:

```text
priority lean = value + urgency + risk reduction - effort - blast radius
```

No fake precision.

## Rewording Rules

- **Title:** name the durable pressure, not the solution.
- **Evidence summary:** summarize the current case, including recurrence count and limits.
- **Proposed next step:** name the smallest safe response and the anti-scope guard.
- **Linked items:** point to runs, receipts, and related MRL items.

Bad:

> Build category profiles.

Better:

> Category-grain signal home for non-company exogenous events - hold for recurrence.

## Starting Point

Start by improving `triage.md` conventions and running periodic steward passes. Do not create a separate triage database, scoring system, or automation layer yet.

The first useful steward output can be either:

- a direct edit to non-human sections of `triage.md`, or
- a short `triage-review-YYYY-MM-DD.md` when the pass is broad or controversial.

Each broad pass should name:

- priority/status changes;
- duplicate merges;
- wording cleanups;
- graduation candidates;
- human gates required.

## Hard Gates

Human approval is still required before:

- changing Truffle code, schema, prompts, or templates;
- mutating `store/` or project systems;
- creating durable category/cohort/relation primitives;
- live browsing, Firecrawl spend, or external capture;
- writing to Notion Roadmap;
- treating a candidate as graduated.
