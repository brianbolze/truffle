---
created: 2026-06-20
last_updated: 2026-06-20
status: frame - Market Read Lab redesign (v2)
supersedes_in_practice: 2026-06-20-redesign-frame.md  # v1 kept as history; predates the decisions below
authors: Brian + Claude
sources: [retro/2026-06-20-first-20-runs-retro.md, retro/2026-06-20-idea-harvest.md, README.md, scout-context.md, triage.md, _design/cohorts-categories/*, _design/2026-05-30-architecture.md, .claude/rules/engine-dev.md]
---

# Frame: Market Read Lab redesign (v2)

## 30-second skim

The Lab is a **discovery engine for Truffle's roadmap** — "what are we missing?" — that got built like a *safe, autonomous, convergent answer pipeline*. Opposite shapes. It picked questions the store could already answer, then a clean backlog compressed the divergence the runs did produce (~345 raw observations → ~2 ideas). That thinness is self-defeating: a Lab meant to stop Truffle from guessing the category/ingredient fork, by going thin, *forces the very guess it exists to prevent.*

**The redesign problem:** *make each run reliably **generate, keep, and reach for** ambitious market-learning — without losing Truffle's file-first, provenance-first, anti-Doro discipline.*

**Three forks settled this session** (everything below assumes them):

1. **Keep it unattended — relax the budget/safety envelope, not the autonomy.** The reach-vs-autonomy "tension" was mostly manufactured by over-conservative spend rules. Light-touch approvals at most.
2. **Discovery-first — everything ladders to roadmap.** Two lenses (below), not two customers. The consumer read is an *instrument to measure value*, not a deliverable. Gap-probes welcome.
3. **Deep + reach on telehealth; breadth via `productivity_saas`** (a second cohort Brian fills in parallel). A run *may* propose companies to add — side effect, not purpose.

> **Using this doc:** the [Issues to address](#issues-to-address) section is the actionable list — start there.

> **First implementation pass:** make only small apparatus edits. Start by updating Scout selection, run observation capture, and review prompts/templates so runs stop optimizing for store-answerability and stop pushing raw learning directly into triage. Do not build new ingredient tools, run captures, change `store/`, or redesign automation in this pass.

## Diagnosis

**One cause:** the apparatus optimized a *clean / safe / convergent pipeline* when the purpose needed a *reaching / generous / divergent loop.* Three couplings did it:

- **Over-conservative budget → store-only selection.** Discovering a gap means reaching *past* the store; "autonomous-safe" collapsed to "store-only," so the runner avoided the only questions that expose gaps.
- **The value-test → easy questions.** Scout gated on "beat generic Claude+websearch *from the store*."
- **A convergent backlog → compressed divergence.** A dedup-happy triage was the *only* cross-run memory; a backlog is the wrong structure for idea-generation.

Two sharper cuts: **the value lens was structurally blinded** — gating on store-answerability meant it could only ever report *"valuable,"* never chart the shortfall; and **recurrence did double duty** — fine for *deciding to build*, anti-generative for *noticing* (the richest vein, new sources, was mostly single-run sightings the apparatus discounted).

## The job: two lenses, one goal

Everything ladders to **roadmap prioritization.** Two co-equal lenses, plus a secondary byproduct:

- **Value lens** (consumer seat) — does Truffle add real value to a reader, *where*, and *where not*? The read is the instrument; the point is charting the value frontier, not harvesting the read.
- **Builder lens** (system seat) — what capability, ingredient, source-family, grain, or structure is missing? *The original purpose.*
- **Corpus byproduct** (secondary) — a run *may* propose companies/data to capture (to Brian, for now) to enrich the Lab's own substrate for future probes.

## Issues to address

The redesign agenda. Each item is a *problem + what good looks like*, not a prescribed mechanism — pick mechanisms in the design pass.

### Must address

- **Selection stops gating on store-answerability.** Scout picks for *reach + value*; gap-probes (expected to fail store-only) are first-class. Open: what *does* Scout optimize for when reach, value, source-diversity, and calibration compete?
- **A new budget/safety envelope.** With "store-only" gone as the safety proxy: define a generous spend ceiling and a *fail-closed* condition that isn't "don't reach." Relaxed ≠ unbounded.
- **A divergent retention home that never merges.** Observations, wishes, frictions, surprises — and singletons — must survive *before* any triage compresses them. Greedy, append-only, traceable, navigable-without-merge, without becoming a swamp.
- **Two clocks.** Separate *notice-and-keep* (greedy, singletons welcome) from *build-and-graduate* (recurrence required). Today one clock does both and discounts the singletons.
- **Repoint the two review lenses.** The value lens must be free to report *"added little / here's where Truffle fell short"* (today it structurally can't); the builder lens must stop over-pulling to *"what should we build?"* and report gaps as observation.

### Should address

- **Observe in-run; shape out-of-run.** A run reports friction and wishes; turning those into recipes/fields/tools is a *separate, named, human-paced* pass (like this session). Define when it runs.
- **Cheap to harvest, not just cheap to run.** Those 345 observations needed five agents to recover — kept-but-buried is still lost.
- **Define "one great run."** Now that discovery is primary, is a clean *gap-map* (no consumer answer) a complete run? What's mandatory vs. opportunistic in a run's output?
- **Define success after the next batch.** *Not* triage count — candidates: distinct preserved observations, source families tested, denominator failures mapped, sharper build/no-build calls.

### Bonus

- **Runs propose corpus additions** (to Brian) to improve future-run substrate; `productivity_saas` is the near-term target. Propose-first; auto-spawn is later + separate.
- **Second-cohort interplay** — how a deep telehealth corpus and a thin bootstrapping cohort coexist and give genuinely-different-market friction.

### Out of scope

- Building the ingredient-capture tools the harvest named (they're *input*, not this build list).
- Deciding the durable category/cohort ontology (a Lab *output*, downstream).
- Auto-graduation into `SCHEMA.md` / `TAXONOMIES.md` / `QUERYING.md` / `store/` structure.
- **Auto-spawned** corpus-discovery — a future, *separate* Routine/skill.
- Replacing company-keying with a market graph; a generic market score; a polished product surface.

## Constraints & what to protect

**Binding constraints**

- **File-first, low-infra, anti-Doro.** No living service, graph DB, embeddings, reconciliation engine, or served API. If the fix needs standing infrastructure, it's wrong.
- **Corpus growth is propose-first, ≠ ontology-minting.** Capturing a company via `/research-company` writes clean State (grows the farm); minting durable category/judgment objects from a run stays gated.
- **Judgments stay labeled; coverage caveats first-class.** Substitutes, whitespace, boundaries are buyer-/source-relative. *Not found ≠ not there.*
- **Don't over-engineer the fix.** A checklist or file convention beats a system. Brian's time is the scarce resource.

**Protect (don't redesign) — these held under the hardest test:** evidence hygiene (snippets are leads; receipts), the adversarial double-check, the guardrails (describe-don't-judge, propose-don't-write, no auto-graduation), and the fact that every run still leaves a cited, inspectable artifact.

## References

[Diagnosis](retro/2026-06-20-first-20-runs-retro.md) · [Evidence harvest](retro/2026-06-20-idea-harvest.md) · [v1 frame (history)](2026-06-20-redesign-frame.md) · [origin proposal](../../../_design/cohorts-categories/2026-06-19-market-read-lab-proposal.md) · [wallow](../../../_design/cohorts-categories/2026-06-18-wallow.md) · [architecture](../../../_design/2026-05-30-architecture.md) · [engine-dev rules](../../../.claude/rules/engine-dev.md)

## Addendum: first pass landed

After this frame was written, the first small apparatus pass landed.

- **Scout selection** now uses `question_mode`, `builder_lens`, and `reach_reason`, and explicitly treats value-read, gap-probe, and calibration questions as valid. Store-answerability is no longer the gate.
- **Bounded-live** now has a light default envelope: 2 source families, 6 outside sources read/captured, and 20 paid capture credits, with fail-closed rules before broadening.
- **Divergent retention** now has two levels: per-run `run-notes.md` Discovery ledger rows, then the append-only cross-run `discovery-ledger.md`. Loop 2 must add cross-run ledger rows before marking a run reviewed.
- **Review and triage** prompts now ask the value lens to name where Truffle fell short, ask the builder lens to record gaps as observations first, and keep triage to short backlog-ready bullets with pointers back to the ledger or run artifacts.

Still intentionally not done: no `store/` changes, no new capture tools, no schema/taxonomy/querying promotion, no automation redesign, and no rewrite of already-written triage narrative.
