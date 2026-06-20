---
created: 2026-06-20
last_updated: 2026-06-20
status: frame - Market Read Lab redesign
sources:
  - experiments/00-market-read-lab/_design/retro/2026-06-20-first-20-runs-retro.md
  - experiments/00-market-read-lab/_design/retro/2026-06-20-idea-harvest.md
  - experiments/00-market-read-lab/README.md
  - experiments/00-market-read-lab/scout-context.md
  - experiments/00-market-read-lab/triage.md
  - _design/cohorts-categories/2026-06-19-market-read-lab-proposal.md
  - _design/cohorts-categories/2026-06-18-wallow.md
  - _design/2026-05-30-architecture.md
  - .claude/rules/engine-dev.md
---

# Frame: Market Read Lab redesign

## 30-second skim

The Lab should be redesigned as a **market-learning stress loop**, not an answer factory and not a clean backlog feeder.

The first ~20 runs did not prove the idea was weak. They proved the apparatus was aimed too conservatively, then tidied away much of the learning it still produced. The raw harvest found ~345 distinct observations and ~15 source-ingredient ideas, while triage collapsed the visible output to a handful of backlog items.

The redesign problem is therefore:

**How do we make each run reliably generate, preserve, and pressure-test ambitious market-learning - especially missing source ingredients, denominator gaps, boundary failures, and reusable friction - without violating Truffle's file-first, provenance-first, anti-Doro discipline?**

The next design should not start by adding machinery. It should first answer what a great run is for, how ambitious question selection should be, and how divergent observations survive long enough to be useful before any tidy graduation pass.

## Background

The Lab was created to de-risk a fuzzy Truffle question: company profiles are useful, but market understanding often needs neighborhoods, source panels, relations, category boundaries, denominator checks, and non-company evidence. Rather than build durable category machinery on a guess, the Lab would persist runs, ask real market questions, and watch what Truffle could and could not answer.

That origin still holds. The strongest thread from the wallow is not "build categories." It is **discover the best source ingredients and capture grains for future synthesis**.

The current apparatus protected several things worth keeping:

- **Store safety held.** Runs stayed outside `store/`, did not mint durable categories, and preserved propose-don't-write.
- **Evidence discipline improved.** Snippet over-trust was caught early and did not become the norm.
- **Adversarial review worked.** Review caught real factual, denominator, and overclaim errors without overturning the larger read value.

But the apparatus under-produced relative to its real purpose because it optimized the visible loop for a narrower job.

## Core diagnosis

**The Lab's productive unit was mis-scored.** It rewarded runs that could answer a market question from the existing store, especially under autonomous-safe constraints. That made the system feel clean, but it biased selection toward questions least likely to expose missing source ingredients.

**The raw run did more work than triage allowed us to see.** The harvest shows the runs generated a large amount of useful learning: ingredient wishes, friction, category-shape insights, use cases, and surprises. The clean triage funnel was doing backlog stewardship, not idea preservation.

**The scope was too narrow to prove the category question.** Telehealth, especially GLP-1 / hormones, is the current store's warmest neighborhood. Staying there mostly tests whether the warm store can answer warm questions.

**The review lenses drifted solution-shaped.** "What should Truffle build?" crowded out "what did the run wish it had, where did evidence fail, and what market need remained under-supported?" The answer kept converging toward query recipes because the machinery kept asking for build-shaped pressure.

The useful correction is not "the Lab failed." It is sharper:

**The Lab works as a raw learning generator, but the apparatus currently selects too safely and preserves too convergently.**

## Objectives

**Aim the Lab at missingness.** Runs should stress the store against valuable market questions that may reach beyond today's captured corpus. The expected product is not only an answer; it is a clearer map of what Truffle cannot yet see.

**Keep divergent learning alive.** Observations, ingredient wishes, source gaps, denominator failures, and surprises need a home that is not immediately deduped into canonical backlog items.

**Preserve real reader value.** The Lab should not become architecture homework. A good run still needs a real market-read job: strategist input, AI-safe delegation, coverage radar, supply-chain read, positioning/whitespace, freshness check, or capture-prioritization.

**Separate observing from proposing.** A run can report friction, evidence wishes, missing source families, and category-shape pressure. Deciding whether that becomes a recipe, capture tool, field, module, or backlog item is a later pass.

**Protect Truffle's core discipline.** Persist runs, not ontology. Keep State / Signals / Judgments boundaries visible. Propose, don't write. Prefer source captures, receipts, and query-time groupings over durable market objects until repeated consumers earn more.

## Constraints

**File-first, low-infra.** Markdown artifacts and simple scripts are the substrate. Any redesign that needs a living service, graph, hosted DB, or heavy entity-resolution layer violates the engine direction.

**Budget and autonomy matter.** Firecrawl / live capture spend is the real cost. Bounded-live source panels are useful, but broad live research, fresh company capture, and write-back remain human-gated.

**Autonomous safety can conflict with ambition.** The current gates make unattended runs clean, but "safe to run unattended" is not the same as "best stress test." The redesign has to handle that tension explicitly.

**Judgment must stay labeled.** Market patterns, substitutes, whitespace, and category definitions are often buyer-relative or source-relative. The Lab can surface them; it should not launder them into shared State.

**Coverage caveats are first-class.** Not found is not not there. Store-only reads are often bounded by corpus construction, anchored-only undercounts, stale captures, field fill-rate, or source-grain mismatch.

## Non-goals

- Build the new ingredient-capture tools named in the harvest.
- Capture the missing menopause/HRT or other brands during this redesign frame.
- Decide a durable category / cohort ontology.
- Promote triage items into `SCHEMA.md`, `TAXONOMIES.md`, `QUERYING.md`, or `store/`.
- Replace Truffle's company-keyed engine with a market graph.
- Make a generic automated category-discovery system.
- Turn the Lab into a polished market-intelligence product surface.

## What makes this hard

**Ambition fights reliability.** The most useful stress questions are often the ones the current store cannot answer cleanly. The apparatus must tolerate productive failure without becoming sloppy.

**Divergence fights stewardship.** Clean backlog triage is good at making decisions later. It is bad at preserving many small, weird, maybe-important observations now.

**Useful answers fight system learning.** A run can be valuable to a reader while teaching little about Truffle, or system-rich while thin as a market read. The Lab needs both, but not every artifact should be graded the same way.

**Source ingredients have different grains.** SERPs, listicles, owned pages, reviews, forums, Wayback, regulatory surfaces, suppliers, and news events do not collapse into one evidence model. The redesign should keep grain visible instead of forcing premature normalization.

**The store's warmth is uneven.** The store can out-complete one seed list and miss an entire segment in the next read. The apparatus has to treat coverage as local and tested, not globally trusted or globally weak.

## Open questions for the redesign

1. **What does one great run produce?** Is the target a useful direct answer plus raw observations, ingredient wishes, evidence gaps, and friction? Which of those are mandatory vs opportunistic?

2. **How much failure should a run welcome?** Should the Lab explicitly choose questions expected to fail store-only, or only questions with a bounded path to a partial answer?

3. **How wide should the next batch go?** Different telehealth segments may be enough to expose selection bias, but a genuinely different market may be needed to test whether the apparatus generalizes.

4. **What should Scout optimize for now?** Reader value, design pressure, source-family diversity, expected missingness, repeat calibration, and autonomous eligibility all compete. Which wins when they conflict?

5. **Where does raw learning live before triage?** The harvest worked because it refused to merge observations out. The redesign needs to define what gets preserved without turning the Lab into an unbounded notes swamp.

6. **When does triage get to compress?** Triage should remain useful for human-gated system decisions, but it should not be the first or only memory of a run's learning.

7. **What counts as an ingredient wish?** The harvest surfaced outside sources, deeper existing-source captures, structural category insights, and query/friction needs. The redesign needs enough shared vocabulary to capture these without pre-deciding the solution.

8. **How should bounded-live fit?** The only genuinely new ingredient use came from reaching outside. But live evidence has cost, source-rigor, and sprawl risks. The redesign needs a stance on when outside panels are part of the run's job.

9. **How should reviews grade the run?** Consumer and Developer review worked for quality control, but their current shape over-pulls toward "what should Truffle build?" What should they inspect instead if the goal is learning harvest?

10. **What would count as success after the next batch?** The answer should not be "more triage items." Better candidates: more distinct preserved observations, more tested source families, clearer denominator failures, sharper no-build decisions, and a better sense of which ingredients deserve later capture work.

## Principles to carry forward

**Stress before proving.** The Lab should not primarily prove that the store can answer questions it was built to answer.

**Divergence before convergence.** Keep the raw learning stream visible before collapsing anything into backlog state.

**Ingredient-first.** The north star is better future synthesis: which source surfaces, capture grains, receipts, and caveats make market reads more trustworthy?

**No ontology gravity.** Repeated market language is evidence, not permission to mint durable category objects.

**Smallest apparatus that preserves learning.** If a checklist or artifact convention can do the job, do not build a system around it.

**Honest partials beat false completeness.** A run that clearly maps why the answer cannot be trusted may be more valuable than a clean answer to an easy question.

## Decision Brian needs to make next

Before solution design, pick the redesign target:

**Recommended frame:** the Lab's next version should optimize for **ambitious market-learning yield per run**, with useful answers as the carrier and divergent observations as a first-class output.

That means the next proposal should be judged by whether it changes what questions get selected, what each run is asked to notice, and what survives after review - not by whether it adds more automation or a prettier backlog.
