---
name: market-read-lab
description: Use when starting, scaffolding, running, reviewing, triaging, or running autonomous Market Read Lab cycles in this Web Research / Truffle project. Handles numbered run folders, Scout/Read/Review gates, repo templates, and the no-auto-graduation convention.
argument-hint: <new run question/slug, or loop action>
---

$ARGUMENTS

## Purpose

Use this skill for `experiments/00-market-read-lab/`.

Market Read Lab runs repeated market reads to learn which source ingredients,
category/cohort questions, relation shapes, and non-company evidence Truffle actually
needs. Persist the **runs**, not the ontology.

## Route

- **Scaffold a run:** use `.claude/skills/market-read-lab/scripts/new_run.py`.
- **Run Scout:** use `experiments/00-market-read-lab/templates/operator-scout-prompt.md`.
- **Run Loop 1:** use `experiments/00-market-read-lab/templates/operator-loop1-prompt.md`.
- **Run Loop 2:** use `experiments/00-market-read-lab/templates/operator-loop2-prompt.md`.
- **Run one autonomous cycle:** follow **Autonomous Full Cycle** below.

## Invariants

- Keep run artifacts outside `store/`.
- Treat `experiments/00-market-read-lab/templates/` and operator prompts as the
  current template authority.
- Treat prior runs as evidence, not templates. Runs `000`-`003` are historical or
  incomplete pre-contract runs; do not copy their headers, source rigor, stage behavior,
  or artifact shape.
- Name runs `NNN-YYYY-MM-DD-short-slug/`.
- Advance stages only by `run_status` in `run-notes.md`.
- Use only the selected run contract's allowed sources.
- `bounded-live` is allowed only when the Selected Run Contract includes a filled
  `live_evidence_plan`; every outside source must be logged in `run-notes.md`
  `live_evidence_used`.
- Stop at `needs-human-review` for live browsing outside a bounded plan, unplanned
  Firecrawl spend, broad external research, `store/` mutation, write-back, durable
  primitive creation, or triage graduation.
- For current/news/policy/pricing claims, treat snippets as leads. Use confident
  language only after receipts capture exact URLs, capture dates, source type, and
  primary/secondary status.
- `triage.md` is the system-pressure queue, not a question backlog. Candidate questions
  live in run `scout.md` files unless Brian explicitly creates a shared question queue.
- Triage items may receive Evidence Log entries; only Brian/humans edit `Human Notes`.
- Graduation from triage is an explicit human decision.

## Scaffold a New Run

Default Scout-only scaffold:

```bash
python3 .claude/skills/market-read-lab/scripts/new_run.py --slug "short-slug"
```

This creates only `scout.md`, `run-notes.md`, and `receipts/.gitkeep`.

If a question is known but the run contract still needs Scout:

```bash
python3 .claude/skills/market-read-lab/scripts/new_run.py \
  --slug "short-slug" \
  --question "Question to sharpen into a run contract?"
```

Print a Loop 1 prompt only for a contract-ready run:

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

Contract-ready bounded-live scaffold:

```bash
python3 .claude/skills/market-read-lab/scripts/new_run.py \
  --slug "short-slug" \
  --question "Question to answer?" \
  --mode loop1 \
  --evidence-mode bounded-live \
  --expected-denominator "Store cohort plus a small external source panel." \
  --allowed-source "store/" \
  --allowed-source "approved bounded-live source families from live_evidence_plan" \
  --live-evidence-goal "Verify the load-bearing current/source-panel claims." \
  --source-family-allowed "SERP/listicle" \
  --source-family-allowed "review/forum" \
  --why-autonomous-safe "Standing bounded-live policy; light source panel only; no write-back." \
  --loop1-failure-mode "Broadening from source check into open-ended browsing."
```

Contract-ready Loop 1 scaffolds also create `read.md`. Review files are stage artifacts;
create them from templates only when Loop 2 runs.

After scaffolding, report the created run path and the printed prompt.

## Autonomous Full Cycle

Run exactly one Scout -> Loop 1 -> Loop 2 cycle in the current routine/session.
Use file gates between stages; do not hand off by updating scheduled tasks.

1. Read the README, `scout-context.md`, `triage.md`, and the Scout/Loop 1/Loop 2
   operator prompts.
2. Scaffold a temporary Scout run:

   ```bash
   python3 .claude/skills/market-read-lab/scripts/new_run.py --slug "scout-candidates"
   ```

3. Run Scout against the created path, following the current question-selection
   policy in `scout-context.md`.
4. Gate on `run-notes.md` and the Selected Run Contract. Continue only when:
   `run_status: scout-only`, `autonomous_eligible: yes`, `approval_needed: no`, and
   `evidence_mode` is `store-only`, `local-existing`, or `bounded-live` with a
   filled `live_evidence_plan`.
5. Rename the run before Loop 1:

   ```bash
   python3 .claude/skills/market-read-lab/scripts/rename_run.py TARGET_RUN_PATH
   ```

   `rename_run.py` prefers `selected_slug` from `scout.md` and falls back to the
   selected question.
6. Run Loop 1 against the current target path. If `read.md` is missing, create it
   from `templates/read.md` after the stage gate passes. Continue only if Loop 1 ends
   with `run_status: read-done`.
7. For Loop 2, prefer a quick workflow if the environment supports one. Use an
   adversarial verification shape with three focused passes: evidence verifier,
   consumer reviewer, and developer reviewer. If workflows are unavailable, run
   Loop 2 normally from the operator prompt. If review files are missing, create them
   from `templates/consumer-review.md` and `templates/developer-review.md` after the
   stage gate passes.
8. Stop after review.

If fresh worker sessions are available, they may run individual stages. The parent
routine still owns each gate: re-read artifacts after every stage before continuing.

Final report:

- run path
- final `run_status`
- `termination_reason`
- stage reached
- files touched
- triage changes
- any approval or evidence block

## Stage Notes

Scout writes only `scout.md` and the YAML header in `run-notes.md`. It should fill the
Selected Run Contract, including `selected_slug`, and leave the run at `scout-only` only
when the selected question is safe to run unattended.

Loop 1 writes only `read.md`, `run-notes.md`, and receipts. It creates `read.md` from
the template if needed, but only after the `run_status: scout-only` gate passes. It
must fail closed unless the Scout contract is complete, autonomous-safe, and
source-bounded. For `bounded-live`, it must also log every outside source in
`live_evidence_used`, record spend notes, and stop with `insufficient-evidence`
instead of expanding beyond the plan.

Loop 2 writes `consumer-review.md`, `developer-review.md`, and Evidence Log entries in
`triage.md` only when review adds evidence. It creates review files from templates if
needed, but only after the `run_status: read-done` gate passes. It does not edit
`Human Notes`, graduate triage, or implement system changes.
