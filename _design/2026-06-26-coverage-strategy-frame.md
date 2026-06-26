# Frame: Strategic Coverage Growth

Date: 2026-06-26  
Status: frame; use to guide coverage/discovery proposals and evaluation packets.

## 30-second skim

**Truffle is crossing from user-pulled depth to intentional coverage growth.** Until now, companies entered the store because a user called `/research-company` for a specific company. That kept the corpus narrow, useful, and grounded. It also leaves a strategic gap: **to understand a company, you often need to understand its neighborhood.**

The question is no longer only "can Truffle research this company well?" It is: **what coverage deserves to exist?**

Coverage is valuable when it helps Truffle answer "cohort" level questions that a single-company profile cannot answer. But every new company profile has a cost: Firecrawl/API credits, agent time, store bloat, future search complexity, and a larger surface for stale or low-value data. So coverage growth needs criteria before it needs autonomy.

**Current priority order:** add company profiles when they are needed to understand an already-captured company's neighborhood, or when they unlock a cross-company comparison or pattern read. Everything else should stay in a worklist, source capture, or query-time grouping until it earns promotion.

## Why this matters

Truffle's early strength has been depth & accuracy: fresh, reliable, "primary-source" company intelligence captured once and reused. That is still the base. But several high-value use cases now depend on breadth:

- **Analyzing a whole "cohort".** Pricing, positioning, claims, offer structures, acquisition surfaces, and category language only become legible across a neighborhood.
- **Make single-company reads smarter.** A profile is easier to interpret when nearby competitors, substitutes, parents, partners, and source-attested alternatives are visible.
- **Build on top without re-capturing.** Downstream "pantry" systems and project-specific lenses need a trustworthy shared corpus, not a fresh scrape per project.
- **Make AI delegation safer.** Agents need enough captured context to avoid quietly filling gaps with generic web-search guesses that are proven to produce hallucinations.

The danger is that "more coverage" can become an undisciplined crawl. A big store is not automatically a better store. If it fills with source publishers, weak long-tail companies, adjacent tools, and project-specific judgments, Truffle gets harder to query and less trustworthy.

The strategic job is to broaden coverage **intentionally, efficiently, and with "graduation gates".**

## What makes it hard

**Usefulness is relative.** A company can be valuable for one project and noise for another. "Worth capturing" is not a universal fact like a homepage URL; it depends on the Truffle user, the market being analyzed, source surfaces, and the use case / query being served.

**Neighborhoods do not have clean "keys".** Company domains gave Truffle a simple identity anchor. Categories and cohorts do not. "DTC telehealth," "medical weight loss," "conversation intelligence," and "AI meeting tools" are useful lenses, but their boundaries are fuzzy and overlapping.

**Source evidence and profile targets are different things.** A listicle page, SERP, directory, or owned comparison page may be valuable evidence without its publisher deserving a company profile. The source should not compete with the companies it reveals.

**Capture is not free.** Full company capture spends credits and attention now, then creates future maintenance, refresh, and retrieval costs. Bloat is a real cost even in a file-first system.

**Coverage decisions require judgment before capture.** Before Truffle spends on a full profile, it may need a light evidence pass to decide whether the candidate is worth promoting at all. That decision interprets source role, cohort fit, neighborhood importance, likely future use, confidence, and cost; it is not the same job as structuring a known company profile.

## Capability goal

Long term, Truffle should be able to propose and grow coverage semi-autonomously while staying legible and cost efficient:

- identify useful missing companies around a question, cohort, or known company;
- stage candidates with evidence and caveats;
- separate source captures from company profile candidates;
- graduate only high-confidence, high-usefulness companies into the primary store;
- minimize standing review and maintenance load; bad promotion calls should be auditable without making Brian the reviewer for every candidate;
- preserve enough source evidence for later synthesis, signal reads, and eventual judgments even when no company profile is promoted.

Near term, the goal is more modest: **develop criteria and evaluation habits for coverage expansion** before turning discovery into a reusable verb.

## Current lean on strategic criteria

These are working criteria, not a settled framework. The point of the current experiments is to test whether they actually separate coverage-worthy companies from noise.

Company profiles deserve promotion to the primary store only when they clear a _"usefulness"_ bar. The first two reasons currently carry the most weight:

1. **Neighborhood context.** The company is needed to understand an already-captured company, including competitors, substitutes, parents, partners, or repeated source-attested alternatives.
2. **Cross-company synthesis.** The company unlocks a comparison or pattern read across a field: pricing, offer structures, claims, workflows, channel strategy, UX patterns, or market positioning.

Supporting reasons can raise confidence but should not dominate on their own:

- repeated appearance across trusted source surfaces;
- likely future query demand;
- relevance to a priority project or recurring user workflow;
- evidence that the store's current answer would be misleading without it.

The inverse is equally important: discoverable does not mean profile-worthy. Publishers, directories, marketplaces, source pages, weak one-off mentions, and adjacent infrastructure may be useful evidence while remaining out of the primary company store.

The promotion logic should stay inspectable without creating another standing review burden. Truffle needs enough evidence and reasoning to audit bad calls; the default direction is fewer manual interventions, not another queue to maintain.

## Coverage surfaces

Not every useful object should become a company profile.

| Surface | Default treatment | Why |
| --- | --- | --- |
| Company profile | Promote narrowly | Primary store should stay high-confidence and high-usefulness. |
| Candidate worklist | Stage by default | Lets Truffle inspect, compare, and review without bloating the corpus. |
| Source page/listicle/SERP | Preserve as signal evidence when useful | These can reveal market visibility, boundaries, and repeated co-occurrence without making the publisher profile-worthy. |
| Query-time grouping | Prefer _before_ durable cohort | Good pressure valve for one-off market questions. |
| Durable cohort/category | Earn later | Needs repeated use, a stable-enough boundary, and a clear reason to revisit or refresh. |
| Durable judgment/verdict | Keep separate from State | Promotion may use judgment, but verdicts like "formidable" or "worth entering" are viewer-relative and should not masquerade as company facts. |

This keeps the primary store narrow without throwing away useful evidence.

Some evidence can earn preservation without earning company-profile promotion. A SERP, listicle, comparison page, directory, or source panel can remain valuable as market-grain evidence about visibility, cohort boundaries, repeated co-occurrence, and potential traction/formidability signals. The publisher may not deserve a profile; the page may still be an ingredient.

## Initial use cases / requirements

Use the current cohort-discovery work as an experiment in coverage governance, not as a broad discovery launch. The near-term product question is: can Truffle help decide what coverage deserves promotion without making Brian maintain another queue?

**Find missing neighbors.** Given a captured company or known cohort, surface missing companies that would materially improve the neighborhood read.

**Stage before promoting.** Keep uncertain candidates, weak matches, and source-derived entities in a "worklist" until there is enough evidence to justify a full company profile capture.

**Preserve useful market evidence.** Keep source pages, SERPs, listicles, and directories when they explain visibility, cohort boundaries, or repeated co-occurrence, even if their publishers are not profile-worthy.

**Explain promotion calls lightly.** Show enough evidence to audit why a candidate was promoted, staged, or rejected, without making human review the default path.

**Improve field-level reads.** Coverage growth should make cross-company comparison, pattern reads, or traction/formidability signal reads better. If it only adds inventory, it has not earned the cost.

**Generalize beyond one market.** Use golden cohorts from more than one domain so the criteria do not quietly become a Telehealth ontology.

## Early leanings

**A staging area is probably load-bearing.** "Worklists" let Truffle gather candidate evidence, compare approaches, and review usefulness before spending on full capture or bloating the primary store.

**Light capture may be a bridge.** A cheap homepage WebFetch or browser-based fetch could help classify staged candidates before full Firecrawl capture, as long as it stays visibly lower authority than `/research-company`.

**Evaluation needs golden cohorts.** The current telehealth and conversation-intelligence sets are useful starts, but the coverage frame should not overfit to Telehealth. One or two additional known cohorts from different markets would make acceptance criteria more honest.

**Coverage serves synthesis.** The best reason to grow coverage is that a later field-level read becomes materially better. If added profiles do not improve neighborhood understanding or cross-company comparison, they probably have not earned primary-store space.

**Agents should do classification and judgement.** Don't try to develop fancy logic and heuristics in code to do things like (a) classifying whether a candidate company is a "capture candidate" versus a listicle "publisher" or (b) deciding whether a candidate "earns" graduation - lean on the agents _using_ the tools. 

**Toward honest judgments.** Long term, Truffle should move toward reliable traction/formidability judgments, but only if they can stay honest: physically separate from State, viewer/use-case aware, decomposed by evidence axis, cited to high-quality source ingredients, and explicit about confidence, counterevidence, freshness, and what the method cannot see. The near-term work is to capture better ingredients, not to mint a verdict.

## Open questions

- What minimum evidence should promote a staged candidate into a full company profile?
- Which source surfaces are best for membership discovery versus weak context?
- What are the right golden cohorts beyond Telehealth and conversation intelligence?
- Which preserved source captures are strong enough to feed later traction/formidability judgments?
- When does a repeated query-time grouping deserve a durable ["cohort"](cohorts-categories/2026-06-18-wallow.md) artifact / storage home?
- How should future search/read-back costs be measured as the store grows?
- What should a "light capture" be allowed to claim, and how does it graduate?

## Related references

- [Frame: a global company-research engine](2026-05-29-frame.md)
- [Wallow: cohorts and categories](cohorts-categories/2026-06-18-wallow.md)
- [External traction signals frame](2026-06-14-traction-frame.md)
- [External traction signals approach](2026-06-15-traction-approach.md)
- [Product Pillars / Themes](https://app.notion.com/p/afdbc4660a084f009ac2df226c3dfd23)
- [Value & Jobs-to-be-Done](https://app.notion.com/p/8f94edca56cd4d95822089e488a1d00c)
- [Data Strategy Notes](https://app.notion.com/p/24284b6d1f4980a4aa3fe6a0ec803700)
- [Cohort discovery worklist packet](../experiments/01-agentic-build/changes/2026-06-25-cohort-discovery-worklist/proposal.md)
