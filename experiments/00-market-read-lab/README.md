# Market Read Lab

**Status**: Active development - ran manual/autonomous trials, tested the local Claude Routine chain, now moving to a single-routine runner with bounded-live evidence allowed only by plan.

## Purpose

Run repeated market reads to learn which category / cohort / non-company primitives Truffle actually needs.

**Posture**: Persist the **runs**, not the ontology.

## How It Works

Market Read Lab is a file-backed research loop. It picks a market question, answers it
or maps the gap from approved evidence, preserves raw learning in a cross-run discovery
stream, reviews where Truffle helped or fell short, and queues only the system pressure
that is mature enough for a backlog.

The runner should stay boring. The repo holds the contract: templates, prompts, stage rules, and run artifacts.

Observed constraint: Claude Desktop local routines require explicit approval when one routine
updates/arms another scheduled task, regardless of permission mode. Do not rely on a self-arming
Scout -> Loop 1 -> Loop 2 task chain for unattended operation. Prefer one local routine whose short
prompt points at the repo skill and runs the full cycle under these file contracts.

Local routine prompt:

```md
Run one autonomous Market Read Lab cycle.

Use `.claude/skills/market-read-lab/SKILL.md` and run the "Autonomous Full Cycle" workflow.
```

Each run moves through three gated work stages:

1. **Scout** chooses a question and decides whether it is safe to run unattended.
2. **Loop 1 / Read** answers the question or maps the gap, writes receipts, preserves
   raw observations in the run, and passes only if the evidence checklist is clean.
3. **Loop 2 / Review** reviews the read from consumer and developer lenses, records
   value shortfalls and capability gaps in the cross-run discovery ledger, then submits
   triage pressure only when useful.

Stages advance through the `run_status` header in `run-notes.md`. If the status is not the expected prior state, the stage stops. This makes double-fires, missed fires, and manual re-runs boring instead of dangerous.

The lab does **not** create durable categories, mutate `store/`, or write back to project systems.
Live evidence and light capture spend are allowed only in `evidence_mode: bounded-live` runs with a filled `live_evidence_plan`; broader live work remains `live-external-needs-approval` and stops for human review.

## Template Authority

Current conventions live in `templates/` and in the operator prompts. Prior runs are evidence and learning history, not templates.

Runs `000`-`002` were produced while the lab contract was still changing. Run `003` is an incomplete Scout-only slate from before the Selected Run Contract settled. Treat `000`-`003` as historical examples of pressure or question-shape only, and **do not copy their artifact shape, headers, source rigor, or stage behavior**. When a run conflicts with `templates/`, the template wins.

## Artifacts By Stage

| Stage | Job | Artifacts |
|---|---|---|
| **Scout** | Pick a useful market or system-test question for value + reach, including bounded gap-probes, and fill the Selected Run Contract. | `scout.md`, `run-notes.md` header |
| **Loop 1 / Read** | Answer the selected question or map the gap, capture the evidence trail, and preserve raw observations before triage. | `read.md`, `run-notes.md`, `receipts/` |
| **Loop 2 / Review** | Split the result through Consumer and Developer lenses: value frontier, shortfalls, and observed capability gaps before proposals. | `consumer-review.md`, `developer-review.md`, `run-notes.md`, `discovery-ledger.md`, optional `triage.md` Evidence Log entries |
| **Discovery** | Keep the append-only notice-and-keep stream for raw learning and singletons. | `discovery-ledger.md` |
| **Triage** | Keep a markdown backlog of system pressure. | `triage.md` |

`scout-context.md`, `discovery-ledger.md`, `triage.md`, and prior `run-notes.md` feed
the next Scout.

## Folder Shape

```text
experiments/00-market-read-lab/
  README.md
  scout-context.md
  discovery-ledger.md
  triage.md
  templates/
  runs/
    NNN-YYYY-MM-DD-short-slug/
      scout.md
      run-notes.md
      receipts/
      read.md
      consumer-review.md
      developer-review.md
```

`read.md` and review files are stage artifacts. A fresh Scout-only scaffold may not have
them yet.

## Run 0

Seed run:

```text
runs/000-2026-06-19-glp1-pricing-visibility/
```

Question:

> In GLP-1 / medical weight loss telehealth, which companies publish pricing, which hide
> it behind intake, and what offer structures are becoming table stakes?

## Rules

**Authority**: use `templates/` and the operator prompts, not prior run files. Use
`templates/operator-scout-prompt.md`, `templates/operator-loop1-prompt.md`, and
`templates/operator-loop2-prompt.md` for manual fresh-agent sessions; use
`templates/operator-full-cycle-prompt.md` for the scheduled local routine.

**Run shape**: keep artifacts outside `store/`; these are experiments and judgments,
not shared State. Name run folders `NNN-YYYY-MM-DD-short-slug/`. In the autonomous
full cycle, the initial scaffold may use a temporary slug such as `scout-candidates`;
after Scout selects the question, rename the folder from `selected_slug` before Loop 1.

**Stage gates**: Scout-only mode writes `scout.md` plus the `run-notes.md` YAML
header, then stops. Loop 1 no-ops unless `run_status: scout-only`; it sets
`read-done` only after the mandatory exit check passes. Loop 2 no-ops unless
`run_status: read-done`; after both reviews are complete, it sets
`run_status: reviewed`. Fail closed to `needs-human-review`.

**Evidence modes**: Scout candidates must include `autonomous_eligible` and
`evidence_mode`. The current question-selection policy lives in `scout-context.md`;
the README only defines the stable modes. `store-only` and `local-existing` use
already-captured evidence. `bounded-live` requires a small planned source panel with
`live_evidence_plan` and `live_evidence_used`; it is valid for reach and gap-probes
when the stop rules are clear. `budget_class: light` means smallest useful source
panel, not a census: default ceiling is 2 source families, 6 outside sources read or
captured, and 20 paid capture credits. Stop as `insufficient-evidence` or
`needs-human-review` before exceeding the plan. `live-external-needs-approval` is for
broader, unclear, or ceiling-breaking live needs.

**Source rigor**: for current/news/policy/pricing claims, snippets are
direction-finding only. Receipts need exact URLs or local paths, capture dates or store
clocks, source type, source grade, and claim IDs before synthesis uses confident
language. Absence language says "not found", not "not true."

**Discovery boundary**: each run keeps raw observations, wishes, frictions, surprises,
source ideas, and gap findings in `run-notes.md`, then Loop 2 appends them to
`discovery-ledger.md` before any triage compression. Singletons are valid learning.
They do not need recurrence to be noticed.

**Triage boundary**: triage is the downstream build-and-graduate clock, not the
discovery stream. Loop agents may submit candidates or Evidence Log entries only when
review adds evidence mature enough for the backlog; raw narrative detail stays in
`discovery-ledger.md`. Loop agents must not implement, spike, or offer to implement
system changes. Loop 2 must never edit `Human Notes` sections in `triage.md`.
`pressure_lenses_fired: []` is a greppable recurrence handle, not a fixed taxonomy or
approval to build.

"No new primitive needed" is a valid outcome.

## Autonomous Launch Checklist

Before enabling unattended runs:

- Confirm the live scheduled-task prompts are copied from `templates/operator-*.md`
  or intentionally equivalent; the repo does not store the scheduler config.
- Give each stage a specific target run path. Do not let Loop 1 or Loop 2 choose a
  run opportunistically.
- Run the first autonomous pass as Scout-only, or as a full chain only when Scout
  selects `autonomous_eligible: yes`, `approval_needed: no`, and
  `evidence_mode: store-only`, `local-existing`, or planned `bounded-live`.
- Keep broad live browsing, unplanned Firecrawl spend, write-back, and durable primitive
  creation outside the unattended permission scope.
- Use "Run now" once per live task to approve only the narrow file/Bash tools needed
  and verify it fails closed when `run_status` is not the expected prior state.
- For unattended operation, prefer one routine running the full cycle from the repo skill.
  Chained routines are acceptable for manual testing, but self-arming handoffs are approval-gated.
