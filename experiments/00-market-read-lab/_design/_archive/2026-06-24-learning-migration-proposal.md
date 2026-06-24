---
created: 2026-06-24
last_updated: 2026-06-24
authors: codex
status: proposal
---

# Proposal: Replace Market Read Lab Triage with Learning

## Problem statement

Market Read Lab now has too many places for the same job: per-run discovery tables, a cross-run `discovery-ledger.md`, review files, and `triage.md`. That is confusing for agents and worse for the system: it invites the exact failure the retro named, where raw learning gets compressed into a tidy backlog and starts carrying proposed fixes too early.

Adding the new `learning/` system on top of `triage.md` would make this worse, not better. The clean move is to retire triage as an active process and make `learning/` the single forward path for capture, review, and approved graduation.

## Recommendation

**Archive `triage.md` and `discovery-ledger.md` as legacy evidence. Do not maintain them alongside `learning/`.**

Use the Agentic Build learning pattern for Market Read Lab:

```text
experiments/00-market-read-lab/
  learning/
    README.md
    AGENTS.md
    observations/
      _TEMPLATE.md
      YYYY-MM-DD-short-slug-xxxx.md
    reviews/
      _TEMPLATE.md
      NNN-YYYY-MM-DD-pass.md
    lessons.md
```

The loop is intentionally small:

1. A run answers or gap-maps a market question.
2. During Loop 1 or Loop 2, agents write one observation file per sighting.
3. Observations record what was seen and what is not being claimed. They do not contain fixes.
4. A later batch review reads observations, clusters by shape, and proposes lessons.
5. Brian approves, parks, or drops proposed lessons.
6. Accepted lessons route to the right destination: Agentic Build, docs, a capture worklist, a roadmap note, or no-op.

No separate triage queue. No steward file. No Evidence Log accretion.

## Why this is better

**It removes the confusing middle layer.** Today an agent has to decide whether a finding belongs in `run-notes.md`, `discovery-ledger.md`, a review file, `triage.md`, or all of them. That ambiguity is a bug.

**It keeps observations from becoming fixes.** The observation template has no solution slot. That matters more than a reminder in prose.

**It preserves divergence without maintaining a table swamp.** One file per sighting is easier to append, grep, review, and leave alone than one ever-growing markdown table.

**It makes review the only consolidation step.** Loop 1 and Loop 2 notice. The learning review proposes. Brian gates. This preserves the "observe in-run, shape out-of-run" principle from the redesign frame.

**It gives graduation one clear home.** `lessons.md` can carry states: `proposed`, `accepted`, `graduated`, `parked`, `dropped`. That replaces triage statuses without preserving triage as a separate object.

## Proposed file roles

### `learning/observations/`

Append-only raw sightings. One file per distinct observation.

Use the same core shape as Agentic Build:

```md
---
date: YYYY-MM-DD
run: experiments/00-market-read-lab/runs/NNN-YYYY-MM-DD-slug
kind: friction | surprise | wish | risk-miss | value-miss | source-gap | brian-correction
graduated-into:
---

**Saw.** What happened, concretely.

**Not claiming.** What this does not prove, and the fix or generalization being resisted.
```

Market Read Lab probably needs `value-miss` and `source-gap` in addition to the Agentic Build kinds. Keep the set small. Do not carry forward the old `ready-for-triage` / `recur-watch` clock; review handles readiness.

### `learning/reviews/`

Batch consolidation notes. The review reads raw observations first, then prior reviews and lessons as dedupe context.

Each pass should:

- propose only a small number of lessons
- list observations deliberately left unconsolidated
- state the Anti-Merge attestation
- avoid editing or stamping observations
- stop before changing live Truffle docs or skills

### `learning/lessons.md`

The only reviewed decision surface.

Each lesson should include:

- state: `proposed | accepted | graduated | parked | dropped`
- source observations
- rule stated without naming a single run or company
- what it replaces
- route: `Agentic Build`, `docs/recipe edit`, `capture worklist`, `roadmap`, or `no-op`
- graduation link when it lands

This is not a backlog. It is a ledger of reviewed learning decisions.

## Migration plan

### Step 1 - Add `learning/`

Create the folder and templates by adapting the Agentic Build files, not by inventing a new mechanism.

Keep the Market Read Lab version narrow:

- include `value-miss` and `source-gap` if needed
- route lessons to MRL-relevant destinations
- point to the old `discovery-ledger.md` and `triage.md` only as legacy evidence

### Step 2 - Archive the old active surfaces

Move:

```text
experiments/00-market-read-lab/triage.md
experiments/00-market-read-lab/discovery-ledger.md
```

to something like:

```text
experiments/00-market-read-lab/_archive/triage-legacy-2026-06-24.md
experiments/00-market-read-lab/_archive/discovery-ledger-legacy-2026-06-24.md
```

Add a short banner to both before archiving:

> Legacy Market Read Lab learning surface. Do not append. Forward process lives in `learning/`.

Do not migrate every old row. The old files remain source evidence.

### Step 3 - Seed only the strongest legacy lessons

Start `lessons.md` with a small set, not a full import. Suggested seeds:

- bounded-live coverage radar graduated to `QUERYING.md`
- headline signal fields need confound context before confident reads
- review/forum body text is a source ingredient gap
- denominator and selection-bias caveats travel with market reads
- query-time grouping works only when the corpus shape supports the reader cut

Each seed should link to old run artifacts or the legacy files, but it should not copy the old Evidence Log narrative.

### Step 4 - Update the active contracts

Affected files:

- `experiments/00-market-read-lab/README.md`
- `.claude/skills/market-read-lab/SKILL.md`
- `.claude/skills/market-read-lab/scripts/new_run.py`
- `.claude/skills/market-read-lab/scripts/question_history.py`
- `experiments/00-market-read-lab/templates/operator-scout-prompt.md`
- `experiments/00-market-read-lab/templates/operator-loop1-prompt.md`
- `experiments/00-market-read-lab/templates/operator-loop2-prompt.md`
- `experiments/00-market-read-lab/templates/operator-full-cycle-prompt.md`
- `experiments/00-market-read-lab/templates/run-notes.md`
- `experiments/00-market-read-lab/templates/read.md`
- `experiments/00-market-read-lab/templates/consumer-review.md`
- `experiments/00-market-read-lab/templates/developer-review.md`
- `experiments/00-market-read-lab/templates/scout.md`
- `experiments/00-market-read-lab/scout-context.md`
- `experiments/00-market-read-lab/runs/README.md`

The edits should remove active references to `triage.md` and `discovery-ledger.md`, and replace them with `learning/`.

### Step 5 - Keep historical runs frozen

Do not rewrite old run folders. They are evidence and history. New runs use the new templates.

## Specific contract changes

### README

Replace the Discovery/Triage boundary with one Learning boundary:

- runs preserve raw learning by writing observation files
- review batches propose lessons
- accepted lessons route to the right downstream workflow
- no run mutates `store/`, skills, schema, docs, roadmap, or captures without the normal gate

### Market Read Lab skill

Remove:

- "triaging" from the description
- `triage.md` as a required read
- triage graduation as a disallowed action
- final report field for triage changes
- Loop 2 instructions to write Evidence Log entries

Add:

- read `learning/AGENTS.md` before Loop 1/Loop 2
- write observation files for distinct sightings
- verify reviewed runs either wrote observations or explicitly say none were found
- learning review is separate from the run cycle

### Run notes template

Replace:

- `pressure_lenses_fired`
- `## Discovery ledger`
- `## Pressure tags`
- `## Optional triage evidence`

With:

- `learning_tags: []`
- `## Learning observations`
- a short list of observation file links
- a note if no observations were found

`learning_tags` are search handles only. They are not a taxonomy and not approval to build.

### Loop 1 prompt

Loop 1 should write the read and any observation files it notices. It should not classify readiness or submit candidates.

### Loop 2 prompt

Loop 2 should write reviews and any additional observation files found during review. It should not propose lessons unless the user explicitly asked to run the learning review.

### Review templates

Replace optional triage sections with:

```md
## Learning observations

Observation files written:
- ...

Potential observations deliberately not written:
- ...
```

This keeps review honest without turning it into a proposal.

## Non-goals

- Do not build a dashboard, database, or service.
- Do not migrate all old triage/discovery entries.
- Do not rewrite historical runs.
- Do not make Scout choose from lessons or observations as a queue.
- Do not let a run propose or graduate fixes.
- Do not use `learning/` as a full project-management system.

## Open questions

**Should `discovery-ledger.md` be archived immediately or kept read-only for one transition batch?** Recommendation: archive immediately. The longer it stays visible, the more likely agents are to keep writing to it.

**Should Market Read Lab get its own review skill or share the Agentic Build review skill?** Recommendation: create a small MRL-specific review skill for now, copied from the Agentic Build pattern. Generalize only after both loops prove the same shape.

**Should `value-miss` and `source-gap` be observation kinds?** Recommendation: yes, because they are central to Market Read Lab and keep agents from stuffing value/frontier observations into generic `wish`.

**What happens to mature legacy items like MRL-008 or MRL-015?** Recommendation: seed only a few as lessons. Anything else stays in the archived files until a future observation or review pulls it forward.

## Key references

- [`experiments/01-agentic-build/2026-06-23-learning-system-frame.md`](../../01-agentic-build/2026-06-23-learning-system-frame.md) - problem frame for the cross-run learning loop.
- [`experiments/01-agentic-build/_design/2026-06-23-learning-system-proposal.md`](../../01-agentic-build/_design/2026-06-23-learning-system-proposal.md) - approved Agentic Build learning-system proposal.
- [`experiments/01-agentic-build/learning/README.md`](../../01-agentic-build/learning/README.md) - concise description of the active learning folder.
- [`experiments/01-agentic-build/learning/AGENTS.md`](../../01-agentic-build/learning/AGENTS.md) - agent-facing learning contract to adapt.
- [`experiments/01-agentic-build/learning/lessons.md`](../../01-agentic-build/learning/lessons.md) - lesson lifecycle and state model.
- [`experiments/00-market-read-lab/_design/retro/2026-06-20-first-20-runs-retro.md`](retro/2026-06-20-first-20-runs-retro.md) - diagnosis of the original triage failure.
- [`experiments/00-market-read-lab/_design/retro/2026-06-20-idea-harvest.md`](retro/2026-06-20-idea-harvest.md) - evidence that the raw runs were rich and the triage layer compressed them.
- [`experiments/00-market-read-lab/_design/2026-06-20-redesign-frame-v2.md`](2026-06-20-redesign-frame-v2.md) - current redesign frame; this proposal replaces its active discovery/triage mechanics with `learning/`.
- [`experiments/00-market-read-lab/README.md`](../README.md) - main lab contract to update.
- [`.claude/skills/market-read-lab/SKILL.md`](../../../.claude/skills/market-read-lab/SKILL.md) - local skill contract to update.
- [`experiments/00-market-read-lab/templates/`](../templates/) - run and operator templates to update.
- [`experiments/00-market-read-lab/triage.md`](../triage.md) - legacy active triage surface to archive.
- [`experiments/00-market-read-lab/discovery-ledger.md`](../discovery-ledger.md) - legacy cross-run discovery surface to archive.
