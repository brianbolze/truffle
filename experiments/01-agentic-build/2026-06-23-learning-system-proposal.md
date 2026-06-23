# Proposal: Agentic Build Learning System

Date: 2026-06-23  
Status: proposed operating model

## Problem

Agentic Build is meant to let agents improve Truffle without Brian manually steering every step. But the system will only become trustworthy if it learns from its own misses.

Right now, that learning is fragile. A packet may include a useful `workflow_note`, a reviewer may catch a scope problem, or Brian may correct an agent's framing, but those lessons stay buried in individual packet files. The next agent has to rediscover them. That creates the worst version of autonomy: repeated mistakes with a clean-looking process around them.

The goal is not generic agent memory. Brian is rightly skeptical of opaque memory systems. The learning record should live in the repo, move through git, and be easy to inspect, challenge, and prune.

## Short Answer

Use a small repo-backed learning ledger plus a periodic consolidation step.

Agents may record raw lessons when packets close. A separate consolidation pass promotes repeated or severe lessons into active rules. Skill or template edits are proposed, not silently applied.

This gives Agentic Build a compounding loop without hidden state, background services, or automatic prompt mutation.

## Recommended Shape

Add one top-level learning file and, later, one small skill:

```text
experiments/01-agentic-build/
  LEARNING.md
```

`LEARNING.md` should have four sections:

- **Active Rules** - compact rules future Agentic Build skills must consult.
- **Verified Lessons** - evidence-backed lessons from prior packets, reviews, or Brian corrections.
- **Inbox** - raw observations from packet closes. Not policy yet.
- **Promotion Queue** - proposed edits to skills, templates, or lead context.

Then add two lightweight behaviors:

1. **Packet close writes evidence.** When a packet ends, the agent writes the normal close receipt and may append one raw learning item to `LEARNING.md` if the process taught us something real.
2. **Consolidation promotes sparingly.** After several packets, or after a painful failure, an agent reviews the inbox, groups repeats, cuts noise, and proposes any rule or skill changes.

The core distinction:

**Observation is not a rule. A rule is not a skill edit. A skill edit is a change packet.**

## Promotion Threshold

A lesson can graduate from inbox to verified / active rule when one of these is true:

- the same failure appears in two or more packets;
- Brian explicitly corrects the process or agent judgment;
- independent review catches a material miss;
- a replayed eval case shows the current skill still fails;
- the miss is severe enough that one occurrence justifies a guardrail.

Most observations should not graduate. Learning includes deleting weak lessons.

## Options Considered

### Option 1: Status Quo Plus Better Discipline

Keep the optional `workflow_note` and rely on agents to read old packets.

This is simple, but too weak. Useful lessons remain scattered, and future agents have no obvious place to consult.

### Option 2: Write Lessons Directly Into Skills

After each miss, update the relevant skill so the behavior improves immediately.

This sounds efficient, but it will overfit. One bad packet can turn into a permanent rule. Skills will bloat, and the system will start carrying lessons that were never verified.

### Option 3: Repo-Backed Ledger With Promotion Gates

Keep raw lessons, verified lessons, active rules, and proposed promotions in git-tracked markdown.

This is the recommended path. It is transparent, lightweight, and compatible with the current file-first operating model. It also creates a clean handoff between evidence, judgment, and behavior change.

### Option 4: Replay / Eval Harness

Save tricky prior requests and use them to test skills before changing them.

This is valuable, but not v0. Start with a few manually written eval cases only after the ledger shows repeated misses worth protecting against.

### Option 5: Background Dreaming Process

Run a scheduled agent that periodically scans packets and updates the process.

This is too much for now. A manually invoked consolidation skill gets most of the benefit without adding hidden automation, scheduler state, or noisy churn.

## Implementation Sequence

1. Create `LEARNING.md` with the four sections above.
2. Update lead context to tell agents when to append a learning item.
3. Add an `agent-build-close` skill that closes a packet and records one optional learning item.
4. Add an `agent-build-consolidate` skill only after a few packets produce enough real material.
5. Add replay cases later, only for repeated failures or high-risk misses.

## Success Criteria

- A future agent can see the current learning rules without reading every old packet.
- Brian can inspect the evidence behind any promoted rule.
- Skill changes happen through reviewable diffs, not hidden memory.
- The system gets sharper without becoming a task tracker, dashboard, daemon, or policy manual.
