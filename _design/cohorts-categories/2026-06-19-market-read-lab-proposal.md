# PROPOSAL - Market Read Lab

Date: 2026-06-19 - Status: approved / active experiment.

## Short answer

Run a scheduled **Market Read Lab** before building durable category machinery. The
bet: repeated LLM market reads can show which questions, source panels, relations,
news signals, templates, and artifacts Truffle actually needs.

Persist the **runs**, not the ontology.

Working home:

```text
experiments/00-market-read-lab/
```

## Why this

The current fork is too fuzzy for a direct build:

- News, monitoring, relations, category profiles, and non-company analysis are related,
  but they are not the same product / capability.
- Durable categories risk pulling Truffle into naming, membership, boundary, and
  ontology work too early.
- One-off market questions are useful now, even before the right storage primitive is
  obvious.

Scheduled LLM routines (Claude Code Routines, Codex Automations) are the way. v0
invests in the **small conventions** that keep many unattended runs comparable and
useful.

## Core posture

A run may mention "medical weight loss," "men's health," or "longevity," but that does
not mint a durable category. The lab can propose durable objects, source captures,
relations, templates, or tooling changes, but it should not promote them automatically.
It maintains pressure and evidence for later human prioritization.

## Loop Map

The lab has three loops. The sections below map directly to this loop map.

| Loop | Job | Artifacts |
|---|---|---|
| **1. Scout + Read** | Pick a useful market or system-test question, answer it, and capture operator learning. Scout may run alone first. | `scout.md`, `read.md`, `run-notes.md`, `receipts/` |
| **2. Review** | Split the result through Consumer and Developer lenses. | `consumer-review.md`, `developer-review.md` |
| **3. Triage** | Keep a markdown backlog of system pressure. | `triage.md` |

`read.md` is the answer. `run-notes.md` is the learning mechanism.
`triage.md` and prior `run-notes.md` feed the next Scout.

## Pressure Lenses

This table is a **starting hypothesis**, not a settled taxonomy. Run 0 and the design
review should pressure-test the table itself: add missing lenses, merge weak ones, and
delete anything that does not help triage.

| Repeated pressure | Possible triage candidate |
|---|---|
| Same company pairs recur | Typed relations |
| Same external sources define membership | Source panel capture |
| Same missing companies recur | Missing-company radar |
| Same market boundary recurs and stays stable | Dated membership doc |
| Same clean non-company anchors recur | Molecule / rule / source glossary |
| Same field is missing across otherwise relevant companies | Depth backfill or cohort-pack change |
| Same stale fields block reads | Refresh / monitoring recipe |
| Same answer needs live external context | News / source-capture routine |
| Same dated non-company moves recur | Event ledger |
| Same synthesis pattern recurs | Rendered market lens |
| Same caveat keeps recurring | Standard coverage / confidence language |
| Same source-grain mismatch recurs | Grain-specific capture convention |
| Same awkward run steps recur | Helper script, template, or tighter convention |
| Query-time grouping is repeatedly enough | No new primitive / keep as query-time answer |

Each run should say which lenses it touched, if any, and flag any lens the table is
missing. One sighting is a submission; recurrence is what makes it interesting.

## Experiment Shape

Keep this outside `store/`. These are experiments and judgments, not shared State.

```text
experiments/00-market-read-lab/
  README.md
  triage.md
  templates/
    scout.md
    read.md
    run-notes.md
    consumer-review.md
    developer-review.md
  runs/
    NNN-YYYY-MM-DD-short-slug/
      scout.md
      read.md
      run-notes.md
      consumer-review.md
      developer-review.md
      receipts/
```

Optional later: `run-record.json` for RUNS-inspired telemetry once scheduling needs
machine-readable model/tool/time metadata.

## Loop 1 - Scout + Read

### `scout.md`

Job: propose questions worth answering from store state, past lab runs, recent captures,
and roadmap pressure.

Scout can run in **Scout-only** mode: generate candidate questions, recommend 1-2,
and stop before answering. This lets question generation be agent-driven without
turning every Scout into a full read.

Before selecting questions, Scout reads:

- `triage.md`
- the last 3 `run-notes.md` files, if they exist
- the current run's prior artifacts, if resuming

Seed two kinds:

- **Market questions** - useful reads about a company neighborhood, offer pattern,
  source surface, event, molecule, treatment line, or buyer problem.
- **System-test questions** - questions chosen because they test a Truffle capability
  uncertainty: query-time grouping, source panels, missing-company detection, entity
  resolution, freshness, relation shape, or non-company evidence.

Output: 5-10 candidates, 1-2 selected questions, why each is worth a run, what evidence
would make it trustworthy, and what failure mode to watch.

Select for decision leverage, evidence readiness, freshness pressure, reuse pressure,
surprise potential, system-test value, and artifact pressure.

### `read.md`

Job: answer one selected question with cited store evidence and explicit caveats.

Keep it reader-facing: question, direct answer, evidence used, companies seen,
missing/stale coverage, source gaps, market pattern, and what would change the answer.
It may use query-time grouping, company profiles, offerings, cohort packs, signals, and
small source panels. It should not create shared State.

For Run 0, include one external completeness check: compare store-derived candidates
against a simple outside denominator (for example, one SERP/listicle/source panel or a
Brian-seeded known-player list). Report the denominator and the store hit rate.

### `run-notes.md`

Job: capture the run's learning loop. This is inspired more by `_design/retro/` than by
`modules/RUNS.md`: not just metadata, but what happened, what surprised the agent, and
what the next run should inherit.

Use a Markdown template, not a schema or linter.
Include one greppable line near the top:

```yaml
pressure_lenses_fired: []
```

## Loop 2 - Review

Reviews should be short, tied to the read and run notes, and end in triage submissions
or no-op.

### `consumer-review.md`

Question: **Would this have helped a real downstream use?**

Lenses:

- **Strategist / Scott** - strategic sharpness and non-technical legibility.
- **Brian / Telehealth** - live venture usefulness.
- **Pantry** - downstream workspace usefulness: Organizations, competitor links,
  market notes, write-back candidates.

### `developer-review.md`

Question: **What system change does this suggest?**

Lenses:

- **Steward** - provenance, freshness, grain, caveats, corpus health.
- **Founder** - anti-Doro discipline; avoid machinery and ontology too early.
- **Dev Agent** - cheap automation, linting, rendering, templates, or query helpers.

## Loop 3 - Triage

Use a markdown queue before reaching for Linear. Keep feedback close to the runs until
there are enough items, owners, and timing pressure to justify a separate task system.

Priorities: `P0`, `P1`, `P2`, `P3`, `Low`, `Out-of-scope`.

Statuses: `Submitted`, `Researching`, `Acknowledged`, `Duplicated`, `Resolved`.

## Launch Plan

Do one manual **Run 0** to shake out the templates, then run a quick design review of
the routines and artifacts before scheduling.

If the design review holds:

- Day 1: Scout + Read + Run Notes.
- Day 2: Consumer Review.
- Day 3: Developer Review.
- Day 4: Scout + Read + Run Notes.
- Day 5: Lab Review updates `triage.md`.

If the reads are not producing useful questions or system pressure after the first
batch, stop or narrow the lab.

## Non-goals

- No durable category entity in v0.
- No automatic graduation from lab artifact to engine artifact.
- No `cohorts/<slug>/` store layer unless a run proves no company-keyed home works.
- No generic market score.
- No broad-topic news ownership.
- No automated category discovery.
- No write-back to Pantry until freshness and evidence rules are clear.

## Recommended Run 0

Start with a question that is commercially live, evidence-rich, and likely to expose
coverage gaps:

> In GLP-1 / medical weight loss telehealth, which companies publish pricing, which
> hide it behind intake, and what offer structures are becoming table stakes?

This is narrow enough to answer from the store, broad enough to expose missing source
needs, and useful enough that the output is not just architecture homework.

---

## Addendum - Autonomous scheduling with Claude Code Routines

How the lab runs unattended. Posture: invest in conventions (file headers + prompt
language), not heavy infrastructure. Decided with Brian after two external research passes
(`_design/2026-06-19-*`); most of their proposed machinery was deferred as premature.

### Runner

**Local Desktop scheduled tasks** (Claude Desktop app -> New **Routine** -> **Local**).

_Rejected:_
- Cloud Routines: fresh git clone, can't see the untracked `experiments/` or the local
  store payloads that are .gitignored
- Claude `/loop`: needs an open session, accumulates context
- `claude -p` + system cron: contradicts the no-bespoke-infra preference and the iCloud-exec
  gotcha - launchd can't reliably exec a script inside this iCloud repo.

### The chain

```text
mrl-scout -> mrl-loop1 -> mrl-loop2 -> notify
```

No native "on-completion" trigger exists for local tasks, but each run is a fresh session
holding the `scheduled-tasks` MCP tools, so a stage arms the next as its last step via
`update_scheduled_task(taskId=…, fireAt=now+~3min)` (docs bless self/cross-rescheduling).
A full run completes back-to-back in ~10 min; each stage is still a fresh session, so the
fresh-context-between-loops convention is preserved for free.

**The arm time is convenience; the contract is status-based.** Every task no-ops unless
`run_status` exactly matches its expected prior state - so a missed fire, double fire, or
stale arm is provably harmless and re-runnable.

| Task | Schedule | Runs when | Does | Then |
|---|---|---|---|---|
| `mrl-scout` | Weekly | always | Scout-only -> new run folder, recommend/select question, set the run header (below) | arms `mrl-loop1` **only if** `evidence_mode` is `store-only`/`local-existing` **and** `autonomous_eligible: yes`; else stop + notify |
| `mrl-loop1` | Manual (armed) | `run_status: scout-only` | Loop 1 read + receipts, set `read-done` | arms `mrl-loop2` **only if the Loop 1 exit check passes** (below) |
| `mrl-loop2` | Manual (armed) | `run_status: read-done` | Loop 2 reviews + `Submitted` triage only, set `reviewed` | notify; arms nothing |

### Run header (top of `run-notes.md`)

Small, for auto-arm gating + debugging double/skipped fires. Not a ledger.

```yaml
run_status:            # scout-only | read-done | needs-human-review | reviewed
evidence_mode:         # store-only | local-existing | live-external-needs-approval
autonomous_eligible:   # yes | no
termination_reason:    # completed | needs-human-review | blocked-by-approval | failed-loop1-exit-check
pressure_lenses_fired: []
```

### Loop 1 mandatory exit check (verification yes, verify-stage no)

Before `mrl-loop1` arms `mrl-loop2`, a small **deterministic checklist** must pass:

- `evidence_mode` is `store-only` or `local-existing`
- `autonomous_eligible: yes`
- no snippets treated as evidence (search/news snippet = lead, not evidence, unless the
  URL was captured/fetched) — targets the Run 002 over-confidence failure
- required receipts / citations present
- current/news/pricing/policy claims carry capture dates
- no live browsing, spend, or unauthorized write-back happened

On any failure, Loop 1 writes and arms nothing:

```yaml
run_status: needs-human-review
termination_reason: failed-loop1-exit-check
```

This stays a **prompt/header/checklist convention** for the first 3-5 autonomous runs.
If evidence-hygiene failures recur, graduate it into a tiny deterministic script (or, only
then, a separate stage). No LLM verifier: its job is contract hygiene, and LLM judges are
unreliable on exactly these factual calls.

### Stays human to start (async, not a trigger you pull)

Framing/question selection beyond store-answerable picks, triage **graduation**, Firecrawl
**spend** (fresh `store/` captures), live browsing, write-back into shared State, and any new
durable primitive. The chain runs scout -> review unattended; you read the notification and
graduate pressure on your own clock.

### Caveats (from the docs)

- Fires only while the Desktop app is open and the machine is awake; one catch-up run for
  the most-recent missed fire within 7 days.
- First run of each task must be **Run now** once to approve "always allow" for its tools
  (Read/Write/Bash -> `store.py`, `new_run.py`, `git`), or autonomous fires stall on
  permission prompts.
