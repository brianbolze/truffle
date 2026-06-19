---
created: 2026-06-19 10:43
last_updated: 2026-06-19 10:43
authors: codex
status: proposed
---

# Market Read Lab - Loop Operating Model

Market Read Lab should automate evidence work, not strategic judgment. Put Brian-context at the high-leverage gates; keep the worker routines narrow.

## Frame

The lab is not an agent swarm. It is one operating loop with a few bounded roles.

The core question:

> Which parts can run without Brian, and which parts are risky because they decide what matters?

Simple answer: automate the work points, keep Brian close to the choice points.

## Diagram

```text
                          batch pattern review
                     +-----------------------------+
                     v                             |
[0 Frame] -> [1A Scout] -> [1B Read] -> [Gate Verify] -> [2 Review] -> [3 Triage]
 Brian        agent        semi-auto      agent          agent        Brian
 heavy        light        medium         light          medium       heavy
```

## Roles

| Role | Job | Context | Authority |
|---|---|---|---|
| **Run Framer** | Pick the question worth asking. | Very high | Human-led |
| **Scout** | Surface candidates, sources, and evidence readiness. | Low-medium | Recommend only |
| **Reader** | Answer the selected question from evidence. | Medium-high | Draft read |
| **Verifier** | Check evidence hygiene and artifact contract. | Low | Pass / warn / fail |
| **Reviewer** | Critique usefulness, reasoning, and system pressure. | Medium | Submit pressure |
| **Triage** | Decide what changes in Truffle, if anything. | Very high | Human-led |
| **Advisor** | Periodically review runs for drift and recurrence. | High | Recommend only |

## Loop Shape

**0. Frame**
Brian selects or approves the question, evidence mode, autonomy level, and stop conditions.

**1. Scout + Read**
Scout can run cheaply. Reader can be semi-autonomous, but should stop when a question needs live external evidence, spend, or strategic reframing.

**Gate. Verify**
Verification is mostly deterministic: required files, citations, source dates, snippet discipline, absence language, no unauthorized store writes, and `pressure_lenses_fired`.

It should judge contract quality, not decide market strategy.

**2. Review**
Reviewers pressure-test the read through consumer and developer lenses. They may submit triage candidates, but they do not graduate system changes.

**3. Triage**
Brian decides whether pressure becomes no-op, template tweak, verifier rule, capture convention, helper script, schema candidate, or monitor candidate.

**Periodic Advisor**
After every 3-5 runs, an advisor reads recent runs, verification results, reviews, and `triage.md`. It looks for repeated failures, drift, and overbuilding pressure.

## Design Rules

- **Context follows risk.** More context goes to Frame, Read judgment, Triage, and Advisor. Less context goes to Scout and Verify.
- **Verification is a gate, not a brain.** It protects evidence quality and run shape.
- **Reviews create pressure.** Triage decides what the system learns.
- **Advisor is periodic.** No always-on overwatch until batch review proves useful.
- **Prefer templates before tooling.** Add scripts or automations only after a failure repeats.

## Proposed v0 Change

Add one artifact between Loop 1 and Loop 2:

```text
runs/NNN-YYYY-MM-DD-short-slug/
  verification.md
```

Loop 2 should run only after verification returns `pass` or `warn`. A `fail` sends the run back for repair or human review.
