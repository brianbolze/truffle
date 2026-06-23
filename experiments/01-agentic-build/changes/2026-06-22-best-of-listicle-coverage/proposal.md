# Proposal: Best-Of Listicle Coverage Radar

Date: 2026-06-22
Status: implemented
Source request: Market Read Lab quick win #7 - best-of listicle coverage, using the Agentic Build proposal flow. Started as proposal-only; implementation was later approved by Brian.

## Required Fields

risk: medium
write_scope: Primary: `QUERYING.md`. Optional: one tiny checklist under `experiments/00-market-read-lab/templates/read.md` `External Completeness Check` if implementation review thinks the template reminder is worth it. Do not touch `store/`, tools, prompts, schemas, receipt schema, operator prompts, or live run artifacts.
spend_stop: none. This proposal does not browse, scrape, call Firecrawl, or run live evidence. Future implementation is docs-only.
acceptance_checks: `git diff --check` on touched docs; manual review confirms the recipe says "coverage radar, not census", requires dated/source-graded listicles, uses cross-source recurrence rather than listicle rank/order, filters non-operator entities before set math, diffs against profiled store entries, and keeps capture candidates propose-don't-write. If `templates/read.md` is touched, the edit is only a short reminder under the existing `External Completeness Check` section, not a second recipe or new artifact contract. No tests required unless implementation touches code or templates with generated checks.
escalate_if: implementation needs a helper script, Firecrawl/network calls, new bounded-live authority, a changed spend ceiling, a persistent listicle/source-panel signal, a category object, a store write, a capture campaign, or an auto-writeback queue.

## Short Answer

Approve a docs-only `QUERYING.md` recipe that names the repeated bounded-live pattern:

SERP direction-finding -> at least two authoritative "best [category] [year]" listicles -> verbatim named-set extraction -> operator-only cleanup -> cross-source recurrence head -> diff against profiled store entries -> tiered capture-candidate worklist with caveats.

This should live primarily as a query/read recipe, not a helper, monitor, durable Signal, category object, or capture job. The purpose is to catch corpus selection bias and missing market segments. It is not a way to rank companies or declare a complete market denominator.

## Frame Clarification

"Best-of listicle coverage" sounds like a source-ingestion feature, but the runs show a narrower and safer job.

The useful thing is not that a listicle says who is best. The useful thing is that two independent third-party surfaces can expose a named set the store cannot see. In run 012, the GLP-1 panel showed the store missed the big-brand / insurance-concierge tier while over-covering the small compounding tail. In run 022, the same pattern proved the store's women-leaning telehealth view was a coverage artifact; dedicated menopause/HRT operators were missing. In run 024, the recipe surfaced a whole behavioral-health lane absent from the captured "telehealth" corpus.

So the frame is:

- **Use for:** membership, whitespace, and selection-bias checks when store-only coverage may be misleading.
- **Do not use for:** objective rankings, quality scores, market share, exhaustive category census, or recurring monitoring.
- **Evidence grade:** secondary and affiliate/SEO-confounded. Cross-source recurrence is decision-grade for capture prioritization; single-source names are weaker leads.
- **Output:** a boundary statement plus tiered proposed capture candidates, not store mutation.

## Problem

The bounded-live coverage-radar recipe has now recurred enough to be usable, but it is buried across run artifacts and triage notes. Future agents have two bad paths available:

1. They re-invent the method from memory, miss the caveats, and overclaim listicle order or tail names.
2. They treat the recurrence as a build signal and create a helper/source primitive before the method earns that weight.

The current docs already allow bounded-live source panels, and `templates/read.md` already has an External Completeness Check section. What is missing is the concrete recipe and its traps.

## Brainstormed Options

1. **Docs-only `QUERYING.md` recipe.** Add a named "bounded-live coverage radar" recipe that explains when to use listicles, how to extract/diff the named set, and what language to avoid.
2. **Docs recipe plus tiny read-template checklist.** Add the `QUERYING.md` recipe and, only if useful, a short reminder in `templates/read.md` under External Completeness Check: list source panel, recurrence head, store diff, tiered candidates, and limits.
3. **Helper script.** Build `tools/listicle_radar.py` or similar to run extraction and diffing.
4. **Persistent listicle/source-panel signal.** Store listicle panels as durable category-grain evidence or Signals.
5. **Capture campaign.** Immediately research the Tier-1 worklists from runs 022/024.

## Recommendation

Choose option 1 as the core approved change. Allow option 2 only as a tightly scoped add-on if the implementer can keep it to a small reminder inside the existing `External Completeness Check` section.

The recipe is stable enough to name after three sightings. `QUERYING.md` is the earned home because the pattern is a reader/query convention. A read-template reminder is less essential because the template already has an `External Completeness Check` slot; if added, it should only help agents remember the recipe's output shape, not create a second recipe, receipt schema, or prompt contract.

A helper script would add knobs around a method that is still mostly judgment: source authority, affiliate contamination, operator-vs-payer filtering, aggregator exclusion, and category boundary decisions. A persistent Signal or category object would cross the exact persistence boundary Market Read Lab is trying to test carefully. A capture campaign may be valuable later, but that is resourcing and scope approval, not this packet.

Risk is `medium` because the docs shape future autonomous bounded-live behavior and paid-source confidence, even though the edit is docs-only. The risk is acceptable if the recipe preserves the current bounded-live ceilings and makes the caveats louder than the mechanics.

## Proposed Recipe Shape

The `QUERYING.md` addition should say, in substance:

1. Use this only when membership/completeness is load-bearing and the store-derived cohort may be selection-biased.
2. Treat SERP results as direction-finding. Use them to choose authoritative listicles and direct brand confirmations, not as claim support.
3. Capture/read at least two authoritative listicles with URL, date, source grade, spend note, and affiliate/SEO caveat. A third source is optional only when the head is unstable and still within the bounded-live plan.
4. Extract verbatim named entities, then clean the set before intersection:
   - keep category-relevant operators/platforms;
   - exclude payers/carriers, marketplaces, aggregators, manufacturers, or adjacent entities unless the selected question explicitly includes them;
   - log exclusions when they materially affect membership.
5. Use cross-source recurrence as the strongest head. Single-listicle names are Tier-2 leads; SERP-only names are direction-finding Tier-3.
6. Diff against the store by profiled company, not raw directory existence. Use `scripts/store.py find` for aliases where possible; supplement with token and body greps when the category boundary requires it.
7. Write the result as "coverage radar, not census." Do not treat listicle rank/order as quality. Do not say store-absent means market-absent. Do not auto-capture or write back.

## Implementation Sketch

1. Add a new `QUERYING.md` recipe near the external-signal/source-panel section, probably after Recipe 8, titled something like `Bounded-live coverage radar`.
2. Link the recipe back to the bounded-live constraints rather than restating all spend policy.
3. Optional only: add a brief checklist under `experiments/00-market-read-lab/templates/read.md` `External Completeness Check`:
   - source panel and inclusion rule;
   - cross-source recurrence head;
   - store diff method;
   - tiered proposed capture candidates;
   - caveats / excluded entity classes.
4. Do not edit operator prompts. The current bounded-live gate already covers receipts, spend, and snippets; prompt changes would exceed this packet.
5. Do not mark MRL-002 resolved. This closes one named recipe slice, not the whole State/Signals query-recipe family.

## Review Notes

Proposal review found the evidence threshold met and recommended approval with a scope trim: `QUERYING.md` is the core implementation; the `templates/read.md` edit is allowed only if tiny. That is now reflected in the recommendation and write scope.

The next reviewer should focus on scope creep. If the proposal starts sounding like "track best-of listicles over time", "store category panels", "add a receipt schema", or "change operator prompts", park or revise it. The value here is a small reading convention that makes a bounded outside denominator safer.

## Implementation Receipt

Implemented 2026-06-22.

- Added a new `QUERYING.md` recipe: `Bounded-live coverage radar - "who is the store missing?"`.
- Kept implementation to the core approved scope: `QUERYING.md` only.
- Did not edit `experiments/00-market-read-lab/templates/read.md`, operator prompts, receipt schema, tools, Signals paths, schemas, `store/`, or live run artifacts.
- Preserved the guardrails: bounded-live only; SERP snippets direction-finding only; at least two dated/source-graded authoritative listicles; clean operator/platform set before intersection; recurrence over rank; profiled-store diff; propose-don't-write output; no auto-capture, persistence, category object, monitor, or new spend authority.
- Worktree caveat: the repository currently contains unrelated untracked `store/*/signals/wayback/...20260622T00*.json` artifacts from earlier work. They were present before this packet's implementation, are not part of this change packet, and are explicitly excluded from the implementation scope.

Verification:

- `git diff --check -- QUERYING.md` -> passed.
- Drift sweep deterministic gate, 2026-06-22:
  - `ruff check scripts tools routines` -> passed.
  - `python3 -m pytest tests/ -q` -> 91 passed.
  - `python3 scripts/querycheck.py --strict` -> passed.
  - `python3 scripts/offeringscheck.py` -> passed.
  - `python3 scripts/cohortcheck.py --cohort telehealth` -> passed.
  - `python3 scripts/cohortcheck.py --cohort productivity_saas` -> passed.
  - `python3 scripts/build_db.py --check` -> passed.
  - `python3 scripts/store.py health` -> completed with existing stubs/staleness/module-clock-skew report.
  - `python3 scripts/visualcheck.py` -> failed on pre-existing missing tile paths in `store/joinamble-com/visual.md`, `store/niagenplus-com/visual.md`, `store/ro-co/visual.md`, `store/rugiet-com/visual.md`, and `store/telolife-com/visual.md`; unrelated to this docs packet.
