---
created: 2026-06-24
last_updated: 2026-06-24
authors: codex, reviewed by Claude + Brian
status: accepted by Brian, moving on to implementation
supersedes: _archive/2026-06-24-learning-migration-proposal.md
reviewed_with: _archive/2026-06-24-learning-migration-proposal-review.md
---

# Proposal: Market Read Lab Learning Migration

## Problem statement

Market Read Lab learned the right lesson after the first batch of runs: raw observations need a greedy, append-only home, and build decisions need a separate gated step. The current setup only gets halfway there.

`discovery-ledger.md` is doing useful work: it already preserves one row per sighting before anything is consolidated. `triage.md` is the confusing layer. It turns recurring sightings into backlog-shaped items, invites solution language too early, and creates a second place agents must decide whether to write.

The migration should not rebuild a working observation stream as hundreds of files. It should **retire triage, move the observation stream under `learning/`, remove the readiness clock, and add a gated lessons layer.**

## Recommendation

**Kill `triage.md` as an active surface. Keep the observation stream, but simplify and move it.**

Use this shape:

```text
experiments/00-market-read-lab/
  learning/
    README.md
    AGENTS.md
    observations.md
    lessons.md
    brian.md
    passes/
      _TEMPLATE.md
      NNN-YYYY-MM-DD-pass.md
```

This borrows the Agentic Build learning loop, but not its exact storage shape. Agentic Build uses one file per sighting because its observations are rare and bursty. Market Read Lab produces frequent, structured observations, often 8-12 per run. A table is the simpler substrate here.

## Decision

### Retire `triage.md`

Archive it with a clear banner:

> Legacy Market Read Lab triage surface. Do not append. Forward learning process lives in `learning/`.

Do not migrate every triage item. Seed only a few high-signal lessons into `learning/lessons.md`.

### Move `discovery-ledger.md` into `learning/observations.md`

Do not treat the ledger as the disease. Its core contract is good:

- append rows
- one row per sighting
- no deduping or merging
- cite the run
- do not turn wishes into fields, tools, recipes, or build proposals

What needs to change is the action pressure around it. Drop the old `Discovery clock` values: `ready-for-triage`, `recur-watch`, `notice-only`. Readiness is the review pass's job.

Recommended active table:

```md
| Date | Run | ID | Kind | Saw | Not claiming | Evidence pointer | Tags |
|---|---|---|---|---|---|---|---|
```

If a no-churn migration is preferred, preserve the exact old ledger in `_archive/` and start a new `learning/observations.md` with the simplified table. The important design call is table-based observations under `learning/`, not file-per-sighting observations.

### Add `lessons.md`

`lessons.md` replaces triage as the only reviewed decision surface.

States:

```text
proposed -> accepted -> graduated
               \-> parked
               \-> dropped
```

Each lesson should include:

- source observations
- state
- route
- rule stated generally, without naming a single run or company
- what it replaces
- approval / graduation notes

Routes:

- `Agentic Build` - engine change packet
- `docs/recipe edit` - light documentation or convention edit
- `capture worklist` - proposed capture/corpus work
- `roadmap` - Notion/BACKLOG-sized product decision
- `no-op` - accepted as a no-build or anti-sprawl lesson

### Add `brian.md`

Keep Brian-specific taste and correction patterns out of `lessons.md`.

`brian.md` is the protected lane for `brian-correction` observations: communication preferences, judgment corrections, recurring taste calls, and process tells that are about Brian rather than Market Read Lab as a system.

This mirrors Agentic Build's protected lane and prevents "learn Brian" from diluting general process lessons.

### Use `passes/`, not `reviews/`

Market Read Lab already has per-run `consumer-review.md` and `developer-review.md`. Calling the cross-run consolidation folder `reviews/` would collide with that language.

Use:

```text
learning/passes/
```

A pass reads observations, clusters by shape, proposes lessons or Brian-lane candidates, and lists what it deliberately left alone.

## Observation contract

`learning/observations.md` is not the place for every useful market finding. It is the stream of system-learning signals: something was hard, unexpected, wanted, unseeable at the needed grain, risky, or corrected by Brian.

Neutral descriptive findings stay in the run artifact. If a finding fits no learning kind, it belongs in `read.md` or the relevant review file, not in `learning/observations.md`.

### Closed kind set

Use a small MRL-specific set:

```text
friction | surprise | wish | gap | risk-miss | brian-correction
```

Definitions:

- `friction` - the run was harder, slower, or more confusing than it should be.
- `surprise` - the system or evidence did something unexpected, including a useful trap avoided.
- `wish` - "I wanted X and it was not there"; includes source-family wants.
- `gap` - the run's gap-probe answer or structural frontier: Truffle cannot see this at the needed grain.
- `risk-miss` - a risk almost shipped or did ship past the run/review.
- `brian-correction` - Brian corrected judgment, taste, scope, or communication.

### Gap / wish dedupe

Do not double-log the same sighting as both `gap` and `wish`.

If a `gap` row names the missing grain, source family, or frontier, the obvious wanted persistence shape usually belongs in `Not claiming`, not in a second `wish` row. Add a separate `wish` only when it is a distinct want, not the solution-shadow of the same gap.

### Crosswalk from current vocabulary

| Current term | New handling |
|---|---|
| `observation` | Map to the closest specific kind. If none fits, keep it in `read.md`; neutral findings do not enter the learning stream. |
| `source-idea` | Usually `wish`; add `source-family:<name>` in `Tags`. |
| `source-gap` | Do not add as a kind. Use `wish` or `gap`. |
| `gap` | Keep as `gap`. This is central to MRL. |
| `value-miss` | Usually a review QA note. Use `surprise` or `friction` only if it points to a repeatable system issue; otherwise keep it in the run review. |
| `trap-avoided` | Use `surprise` plus `trap-avoided` tag. |
| `ready-for-triage` / `recur-watch` / `notice-only` | Drop. Review passes decide readiness. |

### Tags

Use tags as loose recurrence handles, not a taxonomy and not approval to build.

Examples:

```text
denominator-reconciliation
source-rigor
source-panel
coverage-caveat
query-time-grouping-enough
freshness-monitoring
relation-pressure
tooling-ergonomics
trap-avoided
```

Tags can stay close to today's `pressure_lenses_fired`, renamed to `learning_tags` in new run headers.

## Learning pass contract

A learning pass is out-of-band. It is not Loop 2.

It should:

1. Read all active observations first.
2. Read prior passes, `lessons.md`, and `brian.md` only as dedupe context.
3. Cluster by shape, not topic.
4. Propose sparingly.
5. Leave most observations unconsolidated.
6. Add proposed lessons to `lessons.md`.
7. Add Brian-lane candidates to the pass note, not directly to `brian.md`.
8. Stamp or mark nothing as graduated without Brian's nod.
9. Edit no live Truffle skill, recipe, schema, or template.

In v0, observations do not carry a `graduated-into` back-stamp. `lessons.md` owns the source-row links; pass reviewers can grep `lessons.md` to see whether a row has already been used. Add a back-link column later only if review becomes painful.

Pass note shape:

```md
---
date: YYYY-MM-DD
proposed: N
left: M
---

**Pass summary.**

**Proposed / advanced.**

**Brian-lane candidates.**

**Deliberately left unconsolidated.**

**Anti-Merge attestation.**
```

## Migration plan

### Step 1 - Create `learning/`

Add:

- `learning/README.md`
- `learning/AGENTS.md`
- `learning/observations.md`
- `learning/lessons.md`
- `learning/brian.md`
- `learning/passes/_TEMPLATE.md`

Keep these files short. The point is a clean contract, not another operating manual.

### Step 2 - Archive `triage.md`

Move it to:

```text
experiments/00-market-read-lab/_archive/triage-legacy-2026-06-24.md
```

Add the legacy banner first. Do not import every item.

### Step 3 - Move or restart the observation stream

Preferred implementation:

- create `learning/observations.md` with the simplified active table
- preserve the exact old `discovery-ledger.md` in `_archive/` for provenance
- seed only active/future observations into the new table

Alternate implementation:

- move `discovery-ledger.md` to `learning/observations.md`
- keep old rows in a "Legacy rows" section
- start the simplified table below it

Either is acceptable. Do not convert sightings into individual files.

### Step 4 - Seed only a few lessons

Suggested seeds:

- bounded-live coverage radar graduated to `QUERYING.md`
- headline signal fields need confound context before confident reads
- review/forum body text is a source ingredient gap
- denominator and selection-bias caveats travel with market reads
- query-time grouping works only when corpus shape supports the reader cut

These should be short. Link back to old run files or archived triage/ledger evidence rather than copying the Evidence Log narrative.

### Step 5 - Update active contracts

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

Main edits:

- remove active references to `triage.md`
- replace `discovery-ledger.md` with `learning/observations.md`
- rename `pressure_lenses_fired` to `learning_tags`
- remove `Optional triage evidence`
- remove readiness language from run-stage templates
- tell Loop 1 and Loop 2 to append observations, not propose lessons
- tell Scout to use lessons/passes as context, not as a question queue

### Step 6 - Keep historical runs frozen

Do not rewrite old run folders. They remain evidence and learning history.

## What this replaces

This replaces:

- `triage.md` as active queue
- `discovery-ledger.md` as a root-level active file
- `Discovery clock` readiness values
- `Optional triage evidence` sections in run/review templates
- Loop-stage attempts to decide backlog maturity

It does not replace:

- run artifacts
- consumer/developer review
- evidence receipts
- bounded-live rules
- Scout/Loop 1/Loop 2 stage gates
- the core append-only observation stream

## Non-goals

- No dashboard, database, embeddings, or service.
- No file-per-sighting observation directory for MRL v0.
- No migration of every old triage item.
- No rewrite of historical run folders.
- No Scout queue sourced from lessons or observations.
- No run-stage lesson proposal or graduation.
- No general cross-project learning system yet.

## Open questions

**Do we preserve old `discovery-ledger.md` inside `learning/observations.md` or archive it and start fresh?** Recommendation: archive the exact old file for provenance and start a simplified `learning/observations.md` going forward. This avoids a large mechanical table migration while keeping the table shape.

**Should positive calibration be a first-class kind?** Recommendation: not in v0. Use `surprise` only when the calibration is genuinely unexpected; otherwise let the run result carry the positive finding and use tags if needed.

**Should a learning pass run after every MRL run?** Recommendation: no. MRL produces many observations per run, so a per-run trigger would recreate Loop 2. Run a pass on a nudge: after several runs, after a severe `risk-miss`, or when Brian asks.

**When does `observations.md` rotate?** Not a v0 problem. When the table becomes hard to scan, close the current season/batch into `_archive/` and start a fresh table. Do not shard before the table hurts.

**When should this become the shared Truffle learning pattern?** Not yet. Let Agentic Build and Market Read Lab co-evolve with their different observation volumes first. Generalize after both have survived a few review passes.

## Key references

- [`experiments/00-market-read-lab/_design/_archive/2026-06-24-learning-migration-proposal.md`](_archive/2026-06-24-learning-migration-proposal.md) - archived first draft; useful for contrast, especially the over-ported file-per-sighting shape.
- [`experiments/00-market-read-lab/_design/_archive/2026-06-24-learning-migration-proposal-review.md`](_archive/2026-06-24-learning-migration-proposal-review.md) - review that prompted this updated shape.
- [`experiments/00-market-read-lab/_design/retro/2026-06-20-first-20-runs-retro.md`](retro/2026-06-20-first-20-runs-retro.md) - diagnosis of the triage failure.
- [`experiments/00-market-read-lab/_design/retro/2026-06-20-idea-harvest.md`](retro/2026-06-20-idea-harvest.md) - evidence that raw runs were rich and triage compressed the signal.
- [`experiments/00-market-read-lab/_design/2026-06-20-redesign-frame-v2.md`](2026-06-20-redesign-frame-v2.md) - current redesign frame; this proposal updates its discovery/triage mechanics.
- [`experiments/00-market-read-lab/README.md`](../README.md) - main lab contract to update.
- [`experiments/00-market-read-lab/discovery-ledger.md`](../discovery-ledger.md) - current append-only observation stream; parent of `learning/observations.md`.
- [`experiments/00-market-read-lab/triage.md`](../triage.md) - active triage surface to archive.
- [`.claude/skills/market-read-lab/SKILL.md`](../../../.claude/skills/market-read-lab/SKILL.md) - local skill contract to update.
- [`experiments/00-market-read-lab/templates/`](../templates/) - run and operator templates to update.
- [`experiments/01-agentic-build/2026-06-23-learning-system-frame.md`](../../01-agentic-build/2026-06-23-learning-system-frame.md) - frame for the broader cross-run learning loop.
- [`experiments/01-agentic-build/_design/2026-06-23-learning-system-proposal.md`](../../01-agentic-build/_design/2026-06-23-learning-system-proposal.md) - Agentic Build learning proposal; borrow the gated review principle, not necessarily the storage shape.
- [`experiments/01-agentic-build/learning/AGENTS.md`](../../01-agentic-build/learning/AGENTS.md) - useful reference for no-fix, Anti-Merge, and Brian-lane rules.
