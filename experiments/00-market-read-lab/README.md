# Market Read Lab

**Status**: Active development - ran 3 runs manually, tested the local Claude Routine chain, now moving to a single-routine runner.

## Purpose

Run repeated market reads to learn which category / cohort / non-company primitives Truffle actually needs.

**Posture**: Persist the **runs**, not the ontology.

## How It Works

Market Read Lab is a scheduled research loop. It picks a market question, answers it from approved evidence, reviews whether the result was useful, and queues any system pressure it exposed.

The scheduled task is only the runner. The repo holds the contract: templates, prompts, stage rules, and run artifacts.

Observed constraint: Claude Desktop local routines require explicit approval when one routine
updates/arms another scheduled task, regardless of permission mode. Do not rely on a self-arming
Scout -> Loop 1 -> Loop 2 task chain for unattended operation. Prefer one local routine whose short
prompt points at the repo skill and runs the full cycle under these file contracts.

Local routine prompt:

```md
Run one autonomous Market Read Lab cycle.

Use `.claude/skills/market-read-lab/SKILL.md` and run the "Autonomous Full Cycle" workflow.
```

Each run moves through three stages:

1. **Scout** chooses a question and decides whether it is safe to run unattended.
2. **Loop 1** answers the question, writes receipts, and passes only if the evidence checklist is clean.
3. **Loop 2** reviews the read from consumer and developer lenses, then submits triage pressure when useful.

Stages advance through the `run_status` header in `run-notes.md`. If the status is not the expected prior state, the stage stops. This makes double-fires, missed fires, and manual re-runs boring instead of dangerous.

The lab does **not** create durable categories, mutate `store/`, spend Firecrawl credits, browse live sources, or write back to project systems unless a human explicitly approves that outside the unattended loop.

## Template Authority

Current conventions live in `templates/` and in the operator prompts. Prior runs are evidence and learning history, not templates.

Runs `000`-`002` were produced while the lab contract was still changing. Treat them as historical examples of pressure discovered, but **do not copy their artifact shape, headers, source rigor, or stage behavior**. When a run conflicts with `templates/`, the template wins.

## Loops

| Loop | Job | Artifacts |
|---|---|---|
| **1. Scout + Read** | Pick a useful market or system-test question, answer it, and capture operator learning. Scout may run alone first. | `scout.md`, `read.md`, `run-notes.md`, `receipts/` |
| **2. Review** | Split the result through Consumer and Developer lenses. | `consumer-review.md`, `developer-review.md` |
| **3. Triage** | Keep a markdown backlog of system pressure. | `triage.md` |

`triage.md`, `scout-context.md`, and prior `run-notes.md` feed the next Scout.

## Folder Shape

```text
experiments/00-market-read-lab/
  README.md
  scout-context.md
  triage.md
  templates/
  runs/
    NNN-YYYY-MM-DD-short-slug/
      scout.md
      read.md
      run-notes.md
      consumer-review.md
      developer-review.md
      receipts/
```

## Run 0

Seed run:

```text
runs/000-2026-06-19-glp1-pricing-visibility/
```

Question:

> In GLP-1 / medical weight loss telehealth, which companies publish pricing, which hide
> it behind intake, and what offer structures are becoming table stakes?

## Rules

- Keep artifacts outside `store/`; these are experiments and judgments, not shared State.
- Use `templates/` as the authoritative conventions, not prior run files.
- Do not infer new conventions from historical runs. Runs `000`-`002` are useful
  evidence, but not reliable examples for autonomous execution.
- Use `templates/operator-scout-prompt.md`, `templates/operator-loop1-prompt.md`,
  and `templates/operator-loop2-prompt.md` to start manual fresh agent sessions.
- Use `templates/operator-full-cycle-prompt.md` for the scheduled local routine.
- Scout reads `scout-context.md`; the original wallow doc is deep background, not
  default run context.
- Name run folders `NNN-YYYY-MM-DD-short-slug/`, where `NNN` is the zero-padded
  run number for this lab. Run 0 is `000`; the next market read is `001`.
  Dates are metadata, not unique IDs.
- In the autonomous full cycle, the initial scaffold may use a temporary slug such as
  `scout-candidates`; after Scout selects the question, rename the folder from the
  actual selected question before Loop 1.
- Triage pressure; do not auto-graduate engine artifacts.
- Loop agents may submit triage candidates, but must not implement, spike, or offer
  to implement system changes. Graduation is an explicit human decision after review.
- Scout-only mode writes `scout.md` plus the `run-notes.md` YAML header, then stops.
  It should recommend questions, not answer them.
- Scout candidates should include `autonomous_eligible` and `evidence_mode`. Prefer
  store-only candidates for unattended runs; for now, live external evidence needs approval.
- New runs default Scout-first. Print a Loop 1 prompt from the scaffold only when the
  Selected Run Contract and `run-notes.md` header are already contract-ready.
- Loop 1 must no-op unless `run_status: scout-only`; it sets `read-done` only after
  the mandatory exit check passes. Fail closed to `needs-human-review`.
- Loop 1 should tell the operator to start Loop 2 only when it ends with
  `run_status: read-done`; it should not offer to run Loop 2 itself.
- Loop 2 must no-op unless `run_status: read-done`; after both reviews are complete,
  it sets `run_status: reviewed`.
- Loop 2 must never edit `Human Notes` sections in `triage.md`.
- Pressure lenses are short `kebab-case` recurrence tags for system pressure a run
  exposed, e.g. `denominator-reconciliation`, `source-rigor`, `depth-backfill`.
  They are not a fixed taxonomy or permission to build.
- `pressure_lenses_fired: []` is the greppable recurrence handle. Leave it empty if
  no meaningful pressure fired; coin a tag in `run-notes.md` if no existing one fits.
- For current/news/policy/pricing claims, snippets are direction-finding only. Receipts
  need exact URLs, capture dates, source type, and primary/secondary status before
  the read (synthesis, judgements) uses confident language.
- New receipts should use `templates/receipt.md`; snippet-only receipts are leads, not
  evidence for confident claims (judgements).
- "No new primitive needed" is a valid outcome.

## Autonomous Launch Checklist

Before enabling unattended runs:

- Confirm the live scheduled-task prompts are copied from `templates/operator-*.md`
  or intentionally equivalent; the repo does not store the scheduler config.
- Give each stage a specific target run path. Do not let Loop 1 or Loop 2 choose a
  run opportunistically.
- Run the first autonomous pass as Scout-only, or as a full chain only when Scout
  selects `autonomous_eligible: yes`, `approval_needed: no`, and
  `evidence_mode: store-only` or `local-existing`.
- Keep live browsing, Firecrawl spend, write-back, and durable primitive creation
  outside the unattended permission scope.
- Use "Run now" once per live task to approve only the narrow file/Bash tools needed
  and verify it fails closed when `run_status` is not the expected prior state.
- For unattended operation, prefer one routine running the full cycle from the repo skill.
  Chained routines are acceptable for manual testing, but self-arming handoffs are approval-gated.
