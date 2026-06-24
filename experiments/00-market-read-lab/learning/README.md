# learning/ — Market Read Lab's cross-run learning loop

Raw run signals land here greedily; build decisions are gated and rare. This folder
separates **keeping** what a run noticed from **deciding** what Truffle should do about it.

## The loop

1. **Capture** — during a run, append one row per sighting to [`observations.md`](observations.md). No fixes, no dedup, no backlog shaping. Singletons count.
2. **Pass** — out-of-band (not every run), a learning pass reads observations, clusters by shape, and proposes a few lessons. Most observations stay unconsolidated. Notes land in [`passes/`](passes/).
3. **Propose → approve** — proposed lessons live in [`lessons.md`](lessons.md). Only Brian moves one to `graduated`, and nothing in a run or a pass edits a live Truffle skill, recipe, schema, or template.

Brian-specific taste and corrections take a protected lane in [`brian.md`](brian.md), never diluted into general lessons.

## What lives here

| File | Holds |
|---|---|
| [`observations.md`](observations.md) | Append-only stream of run sightings — the table. |
| [`lessons.md`](lessons.md) | The only reviewed decision surface: `proposed → accepted → graduated`. |
| [`brian.md`](brian.md) | Brian's corrections and taste calls — protected lane. |
| [`passes/`](passes/) | Out-of-band consolidation notes; one per pass. |
| [`AGENTS.md`](AGENTS.md) | The contract agents follow when capturing or running a pass. |

## Why it's shaped this way

The old triage queue was the only cross-run memory, and a dedup-happy backlog is the wrong
shape for a discovery lab — it compressed ~345 raw observations into ~2 ideas and invited
solution language before the evidence was in. This loop keeps the stream greedy and moves
**all** readiness judgment into the gated pass. It borrows Agentic Build's gated-review
principle but uses a single table instead of one-file-per-sighting, because MRL produces
many structured observations per run.

Read next: [`AGENTS.md`](AGENTS.md) for the rules. Migration rationale: [`../_design/2026-06-24-learning-migration-proposal.md`](../_design/2026-06-24-learning-migration-proposal.md).
