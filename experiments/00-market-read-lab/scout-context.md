# Scout Context

**Status**: lightweight brief for autonomous Market Read Lab scouts.

## Mission

Generate plain market-read questions a strategist or operator would recognize, then annotate what each question teaches Truffle about capture, structure, or source coverage. For now, go wide on **basic question types** before narrowing into lab-specific pressure tests. A useful downstream read is the reality check.

System learning is the second layer, not the headline.

## Temporary Bias: Strategist-First Blind Runs

For the next few Scouts, bias toward questions **The Strategist** would ask before knowing Truffle's current system shape. Do not start from "what can the store answer?" Start from "what would a senior creative / strategist want to know before making a positioning, offer, or market-entry call?"

It is acceptable, and useful, if the best candidates expose obvious source gaps. Mark them honestly:

- `store-only` when captured State can answer enough.
- `local-existing` when prior run artifacts or existing local signals are enough.
- `bounded-live` when the real answer needs a small outside source panel and Scout can write a concrete plan.
- `live-external-needs-approval` when the answer needs broader, unclear, login-gated, expensive, or unplanned live work.

If the best Strategist question is not autonomous-safe, Scout may select it and stop for approval rather than downgrading to a safer but less revealing store-only question.

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
- **Strategist-native question shapes**, even when Truffle cannot answer them yet:
  - **Whitespace / sameness:** what is everyone saying or showing, and where is there real room to sound different?
  - **Audience / identity:** who is each brand really speaking to, and which customer identity is underserved?
  - **Promise / proof:** what outcomes are promised, what proof is offered, and which claims feel unsupported?
  - **Trust / risk reversal:** who earns trust fastest, what trust devices do they use, and what objections remain unhandled?
  - **Offer packaging:** what would a buyer think they are buying, what bundles/ladders are table stakes, and what feels confusing?
  - **Creative inputs:** what exact phrases, visuals, proof points, and price anchors would go into a five-second brief?
  - **Channel / acquisition surface:** what do paid ads, affiliates, listicles, creators, SEO pages, and social posts reveal that owned sites do not?
  - **Customer pain / objection mining:** what do reviews, forums, Reddit, Trustpilot, or comments say people praise, distrust, or regret?
  - **Launch / market-entry read:** if a new entrant launched tomorrow, what should it copy, avoid, or attack?
  - **Competitor narrative:** who is framed as the default, challenger, premium clinic, cheap access point, or trust leader?

## Strategist Seed Questions

Use these as inspiration, not a fixed queue. Prefer plain-language market reads over system probes.

- **Where is the sameness?** In GLP-1, TRT, longevity/NAD, or sexual health, what claims, visuals, offer structures, and trust devices have become table stakes, and where is there actual white space?
- **Who is winning trust fastest?** Which brands make a skeptical buyer feel safest in the first 30 seconds, and what proof, clinician presence, guarantees, pricing, reviews, or regulatory language do they use?
- **What would a creative director steal?** Across a category, which exact phrases, hero claims, price anchors, visuals, and offer bundles are worth putting into a five-second brief?
- **What would a new entrant avoid?** Which positioning lanes are overcrowded, confusing, risky, or undifferentiated?
- **Who owns which buyer identity?** Which brands speak to optimization, shame-free access, clinical seriousness, masculinity, convenience, affordability, luxury, or longevity status?
- **What is the trust gap?** What objections show up in customer reviews/forums/comments, and which brands answer them on owned pages vs leave them exposed?
- **Where is the channel story different from the website story?** What do ads, affiliates, listicles, SEO pages, creator content, or social comments emphasize that owned pages do not?
- **Who is considered the default?** In third-party surfaces, which brands are repeatedly named as best, cheapest, premium, safest, or most controversial, and how does that differ from the store's captured universe?
- **What is the offer ladder?** What does each brand use as the entry offer, upsell, bundle, subscription, lab/intake anchor, or continuity mechanism?
- **What changed recently enough to matter?** What launches, pricing shifts, regulatory moves, partnerships, or new claims would invalidate a cached strategic read?

## Autonomy Rules

- To start, prefer **store-only** questions for unattended Loop 1 runs, but Scout should still propose beyond-store questions when they expose a source-ingredient gap.
- During the Strategist-first blind run window, do **not** treat `store-only` as inherently better. Prefer the most Strategist-real question, then gate execution by evidence mode.
- Mark every candidate with `autonomous_eligible: yes/no`.
- Mark every candidate with `evidence_mode: store-only | local-existing | bounded-live | live-external-needs-approval`.
- Bounded-live is allowed only with `budget_class: light`, a named evidence goal,
  allowed/preferred source families, disallowed families, and stop rules.
- Broad news research, broad crawling, login-only/paywalled sources, private data, and
  live work without a bounded plan need explicit approval before Loop 1 acts.
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
- Bounded-live convention: `experiments/00-market-read-lab/_design/2026-06-19-bounded-live-evidence-proposal.md`.
- Deep background only when needed: `_design/cohorts-categories/2026-06-18-wallow.md`.
