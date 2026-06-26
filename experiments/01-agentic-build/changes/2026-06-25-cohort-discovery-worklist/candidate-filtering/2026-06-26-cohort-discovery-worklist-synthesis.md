---
created: 2026-06-26
last_updated: 2026-06-26
author: Codex
status: draft synthesis
source_packet: experiments/01-agentic-build/changes/2026-06-25-cohort-discovery-worklist
---

# Cohort Discovery Worklist Synthesis

**Frame: Truffle should discover missing companies by producing a capture worklist, not by growing the store automatically.** The system should find useful candidates, preserve the evidence that found them, and promote only the companies that would improve a named cohort read.

The right next solution is a **cohort discovery worklist** with a simple, agent-led filtering layer.

Not an autonomous crawler.

Not a category ontology.

Not a full `/cohort-discovery` skill yet.

## Quick Skim

**What we learned:** discovery is not one problem. It has at least four different jobs: find source surfaces, extract entities, filter candidates, and decide which real candidates deserve full profiles.

**What worked:** page extraction improved discovery materially, and the Claude-style qualifier proved a simple agent rubric can keep publishers/source artifacts out while preserving surfaced real companies.

**What failed:** query-only discovery is not enough, and Codex-style hard-coded boundary machinery is too brittle to graduate. It encoded too much Telehealth / conversation-intelligence judgment in code (our test sets).

**Recommendation:** build the next version as a packet-local worklist workflow:

1. Define the cohort question and why more coverage would help.
2. Build a source panel from store seeds, SERPs, listicles/pages, and selected alternatives/comparison pages.
3. Extract entity candidates into evidence cards.
4. Run an agent-led candidate filter that emits two distinct judgments: qualification and capture usefulness.
5. Output a proposed worklist: `capture_ready`, `existing_profile`, `review`, `preserve_source_evidence`, `product_or_workflow`, and `drop`.
6. Validate on a third cohort before any reusable verb graduates.

The core rule: **real company is not enough. Profile-worthy means it improves neighborhood context or cross-company synthesis.**

## The Proposed Shape

Call it a **worklist verb** in spirit, even if it stays packet-local for now:

```text
/cohort-discovery-worklist
```

The verb should answer:

> Given a cohort or neighborhood question, which missing companies are worth considering for full Truffle capture, and what evidence supports that call?

It should not answer:

> What is the definitive market map?

And it definitely should not:

> Capture every discovered company into `store/`.

## Approach Overview

The simplest useful system is a staged worklist:

```text
cohort question
  -> store baseline
  -> source panel
  -> page/entity extraction
  -> candidate cards
  -> candidate filtering
  -> capture worklist
  -> optional full /research-company capture
```

Each stage has a different job.

| Stage | Job | Output |
| --- | --- | --- |
| Scope | Name the cohort question and why coverage matters | Small brief + spend cap |
| Store baseline | Separate already-profiled companies from net-new candidates | Existing profile map |
| Source panel | Find pages that expose market membership | SERPs, listicles, directories, owned comparison pages |
| Page/entity extraction | Pull companies/products/source domains from those pages | Candidate evidence cards |
| Filtering | Decide what each candidate is and whether capture is useful | Routed worklist |
| Capture | Run `/research-company` only on earned targets | New store profiles |

The important move is that **source evidence survives even when the publisher does not become a company profile**. A listicle can be valuable market evidence; Forbes does not become a target just because it found competitors.

## Candidate Filtering

Candidate filtering is the hinge.

It needs to keep two judgments separate:

1. **Qualification:** what is this entity?
2. **Promotion/usefulness:** if it is a "real" candidate company, does a full profile capture deserve to exist?

Claude's prototype handled qualification well. Codex's prototype correctly noticed the missing promotion judgment. The right solution borrows both, but keeps the implementation light.

### Judgment 1: Qualification

Question:

> Is this a real company/brand with its own offering in this cohort, or is it a source artifact, directory, product, workflow, or junk?

Recommended routes:

- `company_candidate` - real company/brand with its own in-cohort offering.
- `existing_profile` - already captured in the store.
- `preserve_source_evidence` - publisher, source page, directory, broad evidence surface.
- `product_or_workflow` - product, feature, workflow, or SKU inside a larger platform.
- `review` - plausible but evidence is thin or ambiguous.
- `drop` - junk, nav artifact, reference page, non-market object.

Rules:

- Judge by **own offering**, not by whether the candidate hosted a listicle.
- Preserve owned `best X` / `alternatives` pages as biased evidence.
- Use qrels and Brian labels only _after_ routing, for scoring.
- A homepage "peek" can resolve identity, but does not prove capture-worthiness.

### Judgment 2: Promotion / Usefulness

Question:

> Would a full Truffle profile materially improve a named cohort read?

This is where Claude's track under-built the solution. It treated "real in-cohort company" as close to "capture." That is how a clean qualifier can still produce a bloated queue with Amazon, Walgreens, local clinics, and broad adjacent actors.

Recommended outputs:

- `capture_ready` - full profile likely improves the named read.
- `cohort_fit_review` - real or plausible company, but capture value is uncertain.
- `preserve_source_evidence` - useful evidence, but full profile is not justified.
- `existing_profile` - use the store record, do not recapture.

The promotion call should be agent judgment, not regex.

Useful caveat tags:

- `dual_role_source`
- `tangential_giant`
- `local_clinic`
- `adjacent_tool`
- `broad_platform`
- `thin_snippet`
- `owned_seo_evidence`
- `existing_profile`

These tags make review easier without pretending to be a durable taxonomy.

_Key note_: Maintaining this list of tags introduces brittleness / maintenance burden. Take into consideration when designing the "final" solution.

## One Pass Or Two?

Start with **one agent pass that emits both judgments**:

```text
candidate_card
  -> kind / qualification route
  -> usefulness verdict
  -> one-line synthesis reason
  -> caveat tags
```

Do not mint a separate Gate 2 script just because Codex had one.

Split into a second store-aware promotion pass only when the usefulness decision needs context the first pass does not have. That will often happen, because "worth full capture" depends on:

- what the store already has;
- which cohort read is being served;
- whether the candidate improves comparison, pricing, positioning, claims, offer structure, or source-attested alternatives;
- whether a lightweight candidate card is enough.

So the conceptual split is mandatory. The operational split should earn itself.

## What We Tried

### Query-Only Discovery

The broad discovery packet did not earn a reusable verb.

Telehealth remained weak even after better query construction. Conversation intelligence was stronger, but the benchmark mixed company targets with product/workflow targets.

Conclusion: **better prompts over the same source families are not enough.**

### Search Harness

The search harness reframed discovery as entity retrieval:

- generate candidates;
- score top-K;
- measure precision, recall, and nDCG against frozen labels.

Telehealth raw-unit ranking was poor at top-K, and source/publisher domains competed with real capture targets.

Conclusion: **the system needed page/entity extraction plus filtering, not another query-only pass.**

### Page Extraction

Page extraction materially improved the candidate pool:

- Telehealth moved from P@10 `0.100` to `0.600`.
- Telehealth nDCG@10 moved from `0.139` to `0.562`.
- Conversation intelligence improved more modestly but still moved up.

Conclusion: **keep page/listicle extraction in the recipe.** It exposes entities hidden behind source pages.

### Claude Candidate Filter

Claude built the simple version:

```text
evidence card -> agent decides kind + route
```

It passed the cleanliness test:

- 0 pure publishers in `capture`.
- All surfaced telehealth holdouts preserved.
- Nearly all surfaced conversation-intelligence core targets preserved.

But it under-built promotion. It answered "is this real?" better than "does this deserve full capture?"

Conclusion: **use Claude's qualification rubric as the core, but add "usefulness".**

### Codex Candidate Filter

Codex built the cautious version:

```text
kind-first cards -> boundary resolution -> capture readiness -> comparison merge
```

It found the right concepts:

- `existing_profile` is distinct from net-new capture.
- Homepage confirmation proves existence, not usefulness.
- Owned comparison pages are biased evidence.
- Broad/local/adjacent actors need a synthesis reason.

But it encoded too much market-specific logic in code. The result was useful prototype evidence, not a maintainable system.

Conclusion: **borrow the concepts, park the machinery.**

## Recommended Worklist Output

The worklist should be small enough to review and rich enough to audit. This is an illustrative row shape, not a schema contract; the third-cohort run should decide which fields actually divide decisions.

Each row should look roughly like:

```json
{
  "name": "ExampleCo",
  "domain": "example.com",
  "cohort": "example-cohort",
  "qualification_route": "company_candidate",
  "promotion_route": "capture_ready",
  "evidence_summary": "Named in 3 source families; homepage shows own in-cohort product.",
  "usefulness_reason": "Would improve pricing and positioning comparison against existing store profiles.",
  "caveat_tags": ["owned_seo_evidence"],
  "source_evidence": ["serp", "listicle_page", "owned_comparison"],
  "store_status": "not_profiled"
}
```

The route is the product. The prose reason is the guardrail.

The `review` / `cohort_fit_review` piles need a closing rule. Keep them capped, batch-review only the top few, and expire or demote unresolved rows to `preserve_source_evidence` unless a specific synthesis need pulls them forward.

## Recommended Validation

The next validation should test value, not just cleanliness.

Use four separate checks:

1. **Discovery recall:** the source panel and page extraction surface enough known-relevant companies to make the worklist worth judging.
2. **Source-pollution precision:** publishers, directories, source pages, and junk do not enter `capture_ready`.
3. **Filter recall preservation:** known strong surfaced companies remain in `company_candidate`, `capture_ready`, or `review`; they are not dropped by the filter.
4. **Usefulness:** the promoted `capture_ready` set improves a named cohort read enough to justify full profile cost.

The first and fourth checks are the important additions. A perfect filter over a thin candidate set still produces a weak worklist.

Example synthesis tests:

- Would these captures add a price band the current store does not cover?
- Would they expose a distinct offer structure, GTM pattern, channel, or claim?
- Would they clarify a competitor/substitute neighborhood around already-profiled companies?
- Would the current store answer be misleading without them?

If the answer is no, the candidate may still be preserved as evidence. It just should not become a profile.

## Next Slice

Run one more packet-local validation before graduating anything.

Recommended shape:

1. Pick a **third cohort** outside Telehealth and conversation intelligence.
2. Run the worklist recipe with page extraction and candidate cards.
3. Use a single agent pass to emit qualification + usefulness fields.
4. Add a small store-aware promotion review only if the first pass cannot make usefulness calls honestly.
5. Score the four checks above.
6. Only then decide whether a reusable verb earns implementation.

The third cohort matters. Without it, we are still at risk of overfitting to Telehealth and AI meeting/revenue tools. If the third cohort is mostly greenfield, usefulness should lean on cross-company gap coverage; if it has store seeds, usefulness can also test neighborhood value around already-captured companies.

## What To Build Later, If It Earns It

If validation passes, the eventual reusable shape should be a thin verb or skill:

```text
/cohort-discovery-worklist <cohort/question> [--seed domains] [--spend cap]
```

Inputs:

- cohort/question;
- seed companies or store query;
- source panel limits;
- optional evaluation labels for validation runs;
- explicit spend cap

Many of these inputs should have reasonable defaults if not provided.

Default cap posture: spend should concentrate on source-panel pages and a small number of identity peeks. Full Firecrawl company capture remains out of scope until the worklist is reviewed.

Outputs:

- source panel receipt;
- candidate cards;
- routed worklist;
- evaluation report when labels exist;
- no store writes.

Non-goals:

- no auto-capture;
- no stored cohort ontology;
- no market-share claim;
- no generic score;
- no durable category membership table yet.

The verb should propose work. `/research-company` still does the capture.

## Recommendation

Move forward with the worklist system, but keep it narrow:

**Build the next version around page extraction + evidence cards + an agent-led qualification/usefulness pass.**

Keep Claude's simplicity.

Keep Codex's promotion caution.

Do not carry forward Codex's regex ladder.

Do not let a clean list of real companies masquerade as a good capture queue. The thing that earns graduation is not "we found companies." It is:

> We found the companies whose profiles would make a specific cohort read better.

That is the right bar for Truffle coverage growth.

## Open Questions

- What third cohort best tests generality without becoming another Telehealth-shaped case?
- When does usefulness require a separate store-aware promotion pass versus one enriched agent pass?
- What minimum evidence should make a candidate `capture_ready` rather than `cohort_fit_review`?
- How much source evidence should be preserved when a company does not earn full capture?
- What is the smallest review surface Brian needs before approving a capture batch?

## Sources

- `experiments/01-agentic-build/changes/2026-06-25-cohort-discovery-worklist/decision-surface.md`
- `experiments/01-agentic-build/changes/2026-06-25-cohort-discovery-worklist/receipts/page-extraction-probe.md`
- `experiments/01-agentic-build/changes/2026-06-25-cohort-discovery-worklist/candidate-filtering/README.md`
- `experiments/01-agentic-build/changes/2026-06-25-cohort-discovery-worklist/candidate-filtering/claude-prototyping/results-claude.md`
- `experiments/01-agentic-build/changes/2026-06-25-cohort-discovery-worklist/candidate-filtering/codex-prototyping/README.md`
- `_design/2026-06-26-coverage-strategy-frame.md`
