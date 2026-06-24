---
created: 2026-06-24
last_updated: 2026-06-24
authors: claude (opus)
status: review
reviews: 2026-06-24-learning-migration-proposal.md
---

# Review: Replace Market Read Lab Triage with Learning

**Verdict.** The diagnosis is right and the spine is right: triage's *fusion* (345 sightings → 2 fused-to-fixes items) is the disease, and a gated `lessons.md` with no fix-slot is the cure. Adopt that. But the proposal over-ports: it archives `discovery-ledger.md` as if it were part of the disease when it's actually the v2 redesign's **working** version of the very stream you want to rebuild. It also drops the `brian.md` lane and under-analyzes the `kind` mapping. Net: keep more of what works, copy less.

## What's clearly right — keep as-is
- Retire triage as an active surface; make a gated lessons layer the only consolidation step.
- Archive-don't-migrate, banner the legacy files, freeze historical runs, seed only ~5 lessons.
- Drop the `ready-for-triage / recur-watch / notice-only` readiness clock — let review decide readiness. (This is the one thing you correctly cut *from* the ledger.)
- The lessons state model and the routing set (`Agentic Build / docs / capture worklist / roadmap / no-op`) port cleanly.

## The big one: don't rebuild the discovery ledger as files
`discovery-ledger.md` already **is** an append-only, one-row-per-sighting, immutable, no-fix observation stream — read its Entry Rules: *"Append rows; do not merge, dedup, rewrite, or graduate… one row per sighting… do not turn wishes into fields, tools, recipes, or build proposals."* That's the observation contract verbatim. Its rows (runs 025–035) are rich and un-merged — it works. The fusion happened **downstream in triage**, not here.

So the "no fix slot" / "easier to grep and leave alone" arguments don't favor a directory of files over the table — the table already enforces no-fix and is *easier* to scan than 200 tiny files. One-file-per-sighting is the right shape for Agentic Build because its observations are **rare and bursty**; MRL's are **frequent and structured** (~8–12 rows/run, reliably). Porting the file shape inherits a cadence mismatch: the `≥5 observations → review` trigger would fire every single run.

**Lighter path:** kill triage, keep the ledger as the observation stream (rename to `learning/observations.md` if you like the namespace), add the gated `lessons.md` + a review pass. If you still want files, justify it against MRL's volume rather than assuming the Agentic Build shape transfers. This is the "what does it replace?" test applied to the migration itself.

## The `brian.md` lane is missing
Agentic Build has a first-class **protected `brian.md` lane** fed by `brian-correction`, deliberately kept *out* of `lessons.md` so "learn Brian" doesn't dilute into process lessons. The proposal carries `brian-correction` as a kind but routes everything to `lessons.md` and never mentions `brian.md`. Either adopt the lane or say explicitly why MRL drops it — given MRL is consumer/reach-judgment work where your taste gates a lot, I'd adopt it.

## The `kind` mapping is under-analyzed
You propose "add `value-miss` + `source-gap`" to the five. But MRL's live vocabulary is wider — `{observation, surprise, gap, wish, value-miss, friction, source-idea, trap-avoided}` — and needs an explicit crosswalk, not +2:
- **`source-gap` ≈ `wish`.** "I wanted source X and it wasn't there" *is* the wish gloss. Probably redundant.
- **The genuinely MRL-specific kind is `gap`, not `source-gap`** — the structural gap-probe answer ("store can't see this at query grain") is half a run's job and the 5 don't hold it cleanly.
- **`value-miss` probably isn't an observation kind at all.** Every value-miss row is a Loop-2 consumer-review catch on *this run's own synthesis* ("buried the lede," "axis only in R1") that got fixed in-place that same run. That's in-run QA, not cross-run learning — promoting it to immutable files clutters the stream with already-resolved items.
- **`trap-avoided` (positive) drops** under Agentic Build's "no positive heuristics in v0" rule. Worth noting you're losing it.

Agentic Build guards its five hard ("don't invent a sixth"); your own `brian.md#dont-prescribe-from-one-case` and the taxonomy-sprawl rule both say fix-with-tags-not-new-values. Recommendation: five + `gap`, push everything else onto `learning_tags`, revisit only on evidence.

## Two smaller flags
- **Naming collision.** MRL already has per-run `consumer-review.md` / `developer-review.md`. Calling the cross-run pass `reviews/` will confuse the two — use `passes/` or `consolidations/`.
- **Timing irony.** The two 2026-06-24 observations show Agentic Build's learning loop is *days old and still debugging its own contracts* (decide-vocab mismatch, review-mode-vs-stage mismatch). Cloning a one-week-old, still-settling pattern into a second home is itself prescribing-from-one-case. Your open-question #2 already leans "MRL-specific skill, generalize after both prove the shape" — apply that to the whole port, not just the skill.

## Bottom line
Ship the spine (kill triage, add gated lessons + `brian.md` lane). Don't convert the working ledger to files without a volume-based reason. Resolve the `kind` crosswalk before touching templates — it's the contract everything downstream keys on.
