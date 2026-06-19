---
name: market-read-lab
description: Use when starting, scaffolding, running, reviewing, or triaging Market Read Lab runs in this Web Research / Truffle project. Handles numbered run folders, Loop 1 / Loop 2 prompts, and the no-auto-graduation convention.
argument-hint: <new run question/slug, or loop action>
---

$ARGUMENTS

## Purpose

Use this skill for `experiments/00-market-read-lab/`.

The lab runs repeated market reads to learn which source ingredients, category/cohort
questions, relation shapes, and non-company evidence Truffle actually needs. Scout should
start from plain operator questions a strategist would recognize, then use architecture
learning as the annotation and selection lens. Persist the **runs**, not the ontology.

## Ground Rules

- Keep artifacts outside `store/`.
- Use repo templates in `experiments/00-market-read-lab/templates/`; do not fork a
  second template set inside this skill.
- Treat `experiments/00-market-read-lab/templates/` and the operator prompts as the
  only template authority. Never infer current conventions from prior run artifacts.
- Runs `000`-`002` are pre-autonomy historical runs. Use them only for evidence,
  triage context, and pressure patterns; do not copy their headers, stage behavior,
  source rigor, or artifact shape.
- Name runs `NNN-YYYY-MM-DD-short-slug/`.
- Loop agents may submit triage candidates, but must not implement, spike, or offer
  to implement system changes.
- Graduation from triage is an explicit human decision.
- `triage.md` is the system-pressure queue, not a persistent question backlog.
  Candidate questions live in run `scout.md` files unless Brian explicitly creates a
  separate shared question queue.
- Prior runs are evidence, not templates. Repeated pressure earns conventions; one
  sighting earns only a queue submission.
- `pressure_lenses_fired` is for short `kebab-case` recurrence tags, not approvals.
  Use the tag guide in `run-notes.md`; explain each fired tag in the Fired tag table.
- Scout reads `experiments/00-market-read-lab/scout-context.md`; the original wallow
  doc is deep background, not default context.
- Scout candidates must include `autonomous_eligible: yes/no` and
  `evidence_mode: store-only | local-existing | live-external-needs-approval`.
- Scout must fill the selected run contract in `scout.md`; it is the canonical handoff
  to Loop 1.
- Scout-only may write only `scout.md` and the YAML header at the top of
  `run-notes.md`. The header is the stage lock for later routines.
- For current/news/policy/pricing claims, search snippets are direction-finding only.
  Use confident language only after receipts capture exact URLs, capture dates,
  source type, and primary/secondary status.
- New receipts should use `experiments/00-market-read-lab/templates/receipt.md`.
  Snippet-only receipts are leads, not evidence for confident claims.

## Scaffold a New Run

When the user asks to kick off, create, or start a Market Read Lab run, run the
scaffold script for them. Do not tell the user to run it manually unless they
explicitly ask for the command.

Default mode is Scout-only:

```bash
python3 .claude/skills/market-read-lab/scripts/new_run.py \
  --slug "short-slug"
```

The script:

- picks the next run number,
- creates the run folder and `receipts/`,
- copies the current run artifact templates,
- leaves `templates/receipt.md` as the shared pattern for new receipt files,
- seeds `scout.md` when a question is provided,
- writes a clean `run-notes.md` header,
- prints a ready-to-use Scout or Loop 1 prompt with the target path filled in.

After running it, report the created run path and paste the prompt the next agent
should use.

If a question is already selected but the evidence contract is not complete, still
start Scout so it can fill the Selected Run Contract:

```bash
python3 .claude/skills/market-read-lab/scripts/new_run.py \
  --slug "short-slug" \
  --question "Question to sharpen into a run contract?"
```

Print a Loop 1 prompt only when the run is contract-ready:

```bash
python3 .claude/skills/market-read-lab/scripts/new_run.py \
  --slug "short-slug" \
  --question "Question to answer?" \
  --mode loop1 \
  --evidence-mode store-only \
  --expected-denominator "Store companies matching the selected offer/category criteria." \
  --allowed-source "store/" \
  --allowed-source "experiments/00-market-read-lab/triage.md" \
  --why-autonomous-safe "Answerable from local store files and existing lab artifacts." \
  --loop1-failure-mode "Overstating completeness from a partial denominator."
```

## Run Scout-only

Use `experiments/00-market-read-lab/templates/operator-scout-prompt.md` with the
target run path filled in.

Fill only:

- `scout.md`
- the YAML header at the top of `run-notes.md`

Scout should generate 5-10 candidate questions and recommend 1-2. Go wide across basic
question types first (competitors, market maps, crowded categories, pricing, releases,
claims, channels, reputation, backend dependencies), then name what each question teaches
Truffle. Prefer unattended-safe questions (`autonomous_eligible: yes`,
`evidence_mode: store-only`) for the selected autonomous run, but still include beyond-store
candidates when they expose an important source-ingredient, membership, relation, or grain
gap.

Fill the `Selected Run Contract` for the best selected question. Include the exact
question, run type, autonomy flag, evidence mode, expected denominator, likely source
panel, allowed sources, disallowed actions, approval need, why the run is autonomous-safe,
and the Loop 1 failure mode to watch.

If the selected question is unattended-safe, set `run_status: scout-only`,
`autonomous_eligible: yes`, the selected `evidence_mode`, and
`termination_reason: completed`. If it needs live external evidence, approval, or human
reframing, set `run_status: needs-human-review`, `autonomous_eligible: no`, the selected
`evidence_mode`, and `termination_reason: blocked-by-approval` or
`needs-human-review`.

It should not write `read.md`, fill `run-notes.md` below the YAML header, write review
files, or update `triage.md`.

## Run Loop 1

Read:

- `experiments/00-market-read-lab/README.md`
- `experiments/00-market-read-lab/scout-context.md`
- `experiments/00-market-read-lab/triage.md`
- the target run's `scout.md`
- the last 3 completed `run-notes.md` files, if useful
- target receipts

Before research, gate on the run header and Scout contract:

- Continue only if `run_status: scout-only`.
- Treat the `Selected Run Contract` in `scout.md` as canonical.
- A filled contract has non-empty `selected_question`, `autonomous_eligible`,
  `evidence_mode`, `approval_needed`, `allowed_sources`, `disallowed_actions`, and
  `loop1_failure_mode`. Empty `allowed_sources: []` is not enough for Loop 1.
- Continue only if `autonomous_eligible: yes`, `approval_needed: no`, and
  `evidence_mode` is `store-only` or `local-existing`.
- Use only `allowed_sources`; do not perform `disallowed_actions`.
- If the header or contract is missing, conflicting, or not autonomous-safe, update only
  the `run-notes.md` header to `run_status: needs-human-review` and the right
  `termination_reason`, then stop.

Then fill only:

- `read.md`
- `run-notes.md`
- receipts needed to make the run auditable

For external/current-event reads, receipt rigor matters more than breadth. A tiny panel
is fine, but snippets alone are not citation-grade for law, policy, price, or partnership
claims.

Use `templates/receipt.md` for new receipts. At minimum, record URL or local path,
capture date or store clock, source type, source grade, snippet-only status, and claim
IDs supported.

If the selected question is not autonomous-eligible or needs live external evidence,
set `run_status: needs-human-review`, set the right `termination_reason`, and stop
before spending or browsing.

Before finishing, complete the `Loop 1 exit check` in `run-notes.md`. Set
`run_status: read-done` and `termination_reason: completed` only if every check passes.
Otherwise set `run_status: needs-human-review` and
`termination_reason: failed-loop1-exit-check`, and do not tell the operator to start
Loop 2.

Do not run Consumer Review or Developer Review in Loop 1.

Keep State (captured facts), Signals (dated changes or indicators), and
Judgments (market interpretation) distinguishable in the read. Label judgments
and tie them back to the state/signals they rely on.

At the end, tell the operator to start Loop 2 in a fresh session only if
`run_status: read-done`. Do not offer to run Loop 2 in the same session.

## Run Loop 2

Use `experiments/00-market-read-lab/templates/operator-loop2-prompt.md` with the
target run path filled in.

Before review, gate on the run header:

- Continue only if `run_status: read-done`.
- If `scout.md`, `read.md`, or `run-notes.md` is missing or too incomplete to review,
  update only the `run-notes.md` header to `run_status: needs-human-review` and
  `termination_reason: needs-human-review`, then stop.

Fill:

- `consumer-review.md`
- `developer-review.md`

Consumer Review is verdict-first: was the produced read valuable enough for a
human or agent to trust, reuse, or act on? Use JTBD, value diagnostics, and
persona lenses after that judgment.

Developer Review starts with system capability pressure, especially where the
read crosses from State or Signals into Judgment. Persona lenses are checks, not
sections to fill mechanically.

Update `triage.md` only when review adds new evidence. Keep queue YAML canonical;
avoid prose-only shadow state below an item.

When a later run adds evidence to an existing item without changing its current state,
append a short dated **Evidence Log** entry under that item. Do not invent new YAML
keys such as `evidence_addendum`.

When both reviews are complete, update only the `run-notes.md` YAML header to
`run_status: reviewed` and `termination_reason: completed`. `reviewed` does not
graduate triage items or approve system changes.

## Triage

Use `experiments/00-market-read-lab/triage.md`.

Statuses: `Submitted`, `Researching`, `Acknowledged`, `Duplicated`, `Resolved`.

Priorities: `P0`, `P1`, `P2`, `P3`, `Low`, `Out-of-scope`.

Do not graduate or implement a triage item unless Brian explicitly approves it.
