# Scout Context

**Status**: lightweight brief for autonomous Market Read Lab scouts.

## Mission

Generate plain market-read questions a strategist or operator would recognize, then annotate what each question teaches Truffle about capture, structure, or source coverage. For now, go wide on **basic question types** before narrowing into lab-specific pressure tests. A useful downstream read is the reality check.

System learning is the second layer, not the headline.

## Current Pressure Areas

- **Neighborhood / relations:** nearby players, substitutes, competitors, parents, partners, suppliers, and similar companies.
- **Membership / coverage:** who belongs, who is missing, who is candidate/out, and what source surfaces make that knowable.
- **Pattern / differentiation:** offers, claims, pricing, UX, acquisition surfaces, and what is becoming normal or actually differentiated.
- **Source ingredients:** which repeatable source surfaces make synthesis better: SERPs, listicles, ads, reviews/forums, regulatory surfaces, Wayback, relationship pages, marketplaces, and other source-of-truth pages.
- **Grain / persistence:** what can stay query-time, what should be a durable evidence object, and what might eventually earn relation, membership, source-panel, or category/cohort State.
- **Confidence / source-grain mismatch:** avoid false completeness when source surfaces have different grains, freshness, and coverage.

## Scout For

- Market questions a real strategist, investor, operator, or researcher would actually ask.
- A wide slate of basic question archetypes before narrow recurrence probes:
  - **Company neighborhood:** who are X's closest competitors, substitutes, or peers?
  - **Current change watch:** what launched, changed, shipped, or got announced recently?
  - **Crowded categories:** which product, features, or offer areas are most saturated?
  - **Pricing benchmark:** who is cheapest, most expensive, transparent, or gated?
  - **Offer map:** who offers which products, formats, tiers, bundles, or care models?
  - **Positioning / claims:** who leads with price, outcomes, trust, convenience, or identity?
  - **Reputation / pain:** what customers complain about, praise, or distrust.
  - **Backend dependency:** Parents, suppliers, or platforms. For telehealth - shared pharmacies, provider groups
  - **Channel / access map:** (telehealth examples) cash-pay, insurance, membership, pharmacy, marketplace, or direct.
- **System-test questions that pressure Truffle design:** query-time grouping, source ingredients, membership coverage, relation shape, source rigor, freshness, entity resolution, capture grain, or persistence boundaries.
- Questions that may reveal an opportunity for a better source ingredient, even if the current store cannot fully answer them unattended. Prefer cheap / free sources, but don't exclude ideas for where some proprietary / paid sources would be helpful.
- Questions likely to produce evidence, recurrence, surprise, or **quick-win opportunities**, not broad opinions.

## Autonomy Rules

- To start, prefer **store-only** questions for unattended Loop 1 runs, but Scout should still propose beyond-store questions when they expose a source-ingredient gap.
- Mark every candidate with `autonomous_eligible: yes/no`.
- Mark every candidate with `evidence_mode: store-only | local-existing | live-external-needs-approval`.
- For now, live external fetching, Firecrawl spend, and broad news research need explicit approval before Loop 1 acts.
- Search/news snippets are "signals", not conclusive, reliable evidence in isolation. Current law, policy, pricing, or partnership claims require primary URLs, capture dates, and source type.
- Downstream consumers may layer in project-specific context, fields, detail, and judgments. The lab should surface useful candidates and caveats, not write those judgments for them.

## Avoid

- Auto-graduating triage items.
- Making completeness claims from one / limited sources.
- Treating one sighting as sufficient for system changes / infrastructure.
- Letting triage pressure crowd out straightforward market questions.
- Treating `triage.md` as a question backlog. It is primarily for system gaps / system pressure.
- Turning a query-time grouping into a durable category.
- Reusing prior run methods as defaults instead of hypotheses / experiments.
- Starting with internal architecture jargon when a normal operator question would suffice.

## Question Memory

- There is no shared persistent question queue yet.
- Candidate questions live in individual run `scout.md` files.
- `triage.md` is for system pressure and conventions, not "questions to run someday."
- Future Scouts may mine prior Scout files for inspiration, but should not treat old candidate lists as canonical.
- If question volume becomes hard to track, add a separate `questions.md` only by explicit decision; do not overload triage.

## Background Pointers

- Live memory: `triage.md` and the last 3 completed `run-notes.md` files.
- Design intent: `_design/cohorts-categories/2026-06-19-market-read-lab-proposal.md`.
- Deep background only when needed: `_design/cohorts-categories/2026-06-18-wallow.md`.
