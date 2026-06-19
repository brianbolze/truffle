# Market Read Lab Triage

**Status**: Active.

**Priorities**: `P0`, `P1`, `P2`, `P3`, `Low`, `Out-of-scope`.

**Statuses**: `Submitted`, `Researching`, `Acknowledged`, `Duplicated`, `Resolved`.

## Item Template

```yaml
id:
title:
priority:
status:
source_run:
source_review:
area:
evidence:
proposed_next_step:
linked_items:
```

Use the YAML block as the canonical item state. When later runs add evidence without
changing the item's current state, append a short dated **Evidence Log** under the item
instead of adding new YAML keys.

Never touch or add **Human Notes**. That's only for Brian / humans.

---

## Queue

### MRL-002 - Reusable store-query helper for market reads

```yaml
id: MRL-002
title: Reusable store-query helper for market reads
priority: P1
status: Submitted
source_run: runs/000-2026-06-19-glp1-pricing-visibility
source_review: operator-observation
area: query
evidence: Manual Loop 1 was 7+ minutes in while the agent hand-built a GLP-1 union, resolved Notion names to store slugs, classified roles/false positives, extracted SKU price visibility, and computed aggregates. The work is useful, but it is repeated market-read machinery being invented inside the run.
proposed_next_step: Candidate next step, if acknowledged: capture a reusable denominator-check convention that names the inputs considered, inclusion/exclusion judgment, dedupe/resolution method, false-positive risks, confidence language, and symmetric diff/write-back output. Keep it pattern-level for now; do not hard-code the GLP-1 query recipe or build a helper until another run shows recurrence.
linked_items:
  - runs/000-2026-06-19-glp1-pricing-visibility/receipts/operator-observation-latency.md
  - runs/001-2026-06-19-mens-health-backend-relations/run-notes.md
```

**Human Notes**
- **2026-06-19**: [Brian] After run 004, I decided to upgrade the priority to P1. 

**Evidence Log**

- **2026-06-19 · Run 001:** Relations read hand-built a second, different
  store-query surface in-run: pull `parent`/`owns` frontmatter, grep
  `telehealth.md` Fulfillment/Provider, and dedupe by hand. Different query
  shape, same pattern: strengthens the case for a QUERYING recipe layer over
  per-query committed helpers; does not yet justify a helper because the same
  query has not recurred.
- **2026-06-19 · Run 004 (third sighting):** Category-crowdedness read hand-built
  a third, distinct store-query surface in-run: a per-category breadth count
  derived from molecule strings in `offerings.md` roster cells, because the store
  has no per-SKU category dimension. Three distinct shapes now (Run 000 entity-set
  union / Run 001 relation-edge grep / Run 004 category grouping) — recurrence is
  consistent enough that a *documented QUERYING category-grouping recipe* looks
  earned: inputs, the roster-cell molecule match, and the whole-file-grep
  anti-pattern (Run 004's first pass grepped full bodies and returned TRT 53/53 /
  labs 53/53 — confidently wrong from prose/FAQ/negation), with captured-floor
  language. Pattern-level recipe, NOT a stored per-SKU category taxonomy (that
  would be the ontology gravity the anti-Doro line refuses) and NOT a built helper.
  Still a human graduation call; a fourth sighting is the trigger. MRL-001 was
  touched but not strengthened this run (the `value_chain_role` DTC gate was a
  clean 1:1 join, not the hard part).

### MRL-001 - Market denominator reconciliation convention

```yaml
id: MRL-001
title: Market denominator reconciliation convention for market reads
priority: P2
status: Submitted
source_run: runs/000-2026-06-19-glp1-pricing-visibility
source_review: run-notes; Loop 2 consumer + developer review
area: denominator-reconciliation
evidence: Run 0 showed the Notion Organizations denominator was slow, partial, and method-sensitive, while the internal store out-completed it. The store<->Notion symmetric diff was useful both as missing-company radar and as a Pantry write-back / capture worklist (~24 store GLP-1 sellers absent from Notion Organizations + 8 Notion names absent from the store). External SERP/listicle panels should be a fallback only when internal curated lists are thin.
proposed_next_step: If acknowledged, define a lightweight denominator artifact or section for market reads: sources checked, inclusion/exclusion rules, resolver/dedupe method, symmetric-diff write-back set, known gaps, confidence language, and when to reach for an external panel.
linked_items:
  - runs/000-2026-06-19-glp1-pricing-visibility/receipts/notion-organizations-glp1-denominator-seed.md
  - runs/000-2026-06-19-glp1-pricing-visibility/receipts/store-derived-glp1-list.md
```

### MRL-003 - Depth-backfill in-cohort module gaps

```yaml
id: MRL-003
title: Depth-backfill in-cohort module gaps (altRx, Marque)
priority: P2
status: Submitted
source_run: runs/000-2026-06-19-glp1-pricing-visibility
source_review: run-notes; Loop 2 developer review (Steward)
area: corpus-health
evidence: altrx-com (GLP-1-led "cheapest GLP-1 program" by its profile, no telehealth.md/offerings.md) and marquelongevitylab-com (no telehealth.md) are in-cohort but unqueryable on the cohort cuts. Run 0 submitted this as a backfill candidate but it never landed in the queue; Loop 2 Steward confirms it as live corpus-health pressure that silently shrinks any cohort query.
proposed_next_step: Run /deepen-offerings + telehealth.md capture for altrx-com, and telehealth.md for marquelongevitylab-com, so both are queryable on anchor_category / value_chain_role. Concrete and bounded; graduation is a human decision.
linked_items:
  - runs/000-2026-06-19-glp1-pricing-visibility/receipts/store-derived-glp1-list.md
```

### MRL-005 - Named-counterparty relation edge (supplier + clinical)

```yaml
id: MRL-005
title: Named-counterparty relation edge (pharmacy + clinical) - candidate, hold for recurrence
priority: P2
status: Submitted
source_run: runs/001-2026-06-19-mens-health-backend-relations
source_review: run-notes; Loop 2 developer review (Founder + Steward)
area: relations
evidence: Across 18 men-led/hormone telehealth brands, named pharmacy/clinical counterparties (Curexa, Strive, Hallandale, OpenLoop, MDIntegrations, Wasef PC, CareGLP) already resolve to store profiles, so a brand->backend edge would join, not dangle; supplier concentration ("which backend sits behind the most brands") is a genuinely useful market read. But the edge is named in only 5/18 (pharmacy) and ~3/18 (clinical), is claim-contaminated (BlueChew says "our own pharmacy" then names three third parties), and the load-bearing parent edge is already parent/owns while integration posture is already pharmacy_model. store.py relations already ranks join targets by in-degree for the joinable edges, so the joinable case needs nothing new.
proposed_next_step: Hold, do not graduate. If acknowledged and it later graduates, implement as joinable dotted-domain frontmatter mirroring parent/owns (already indexed by store.py relations / QUERYING Recipe 3) - NOT a new edge table or relation-type registry (anti-Doro). Gate graduation on recurrence: re-test on a backend-naming-dense cohort (compounding-heavy GLP-1) and see whether named-is-the-minority flips. Prerequisite is MRL-006 (the named entity must be captured into frontmatter before it can join).
linked_items:
  - runs/001-2026-06-19-mens-health-backend-relations/receipts/backend-relations-worksheet.md
  - MRL-006
  - MRL-002
```

### MRL-006 - Named-counterparty capture-grain gap

```yaml
id: MRL-006
title: Named-counterparty capture-grain gap (pharmacy + clinical entity into frontmatter)
priority: P3
status: Submitted
source_run: runs/001-2026-06-19-mens-health-backend-relations
source_review: run-notes (clinical-only P3); Loop 2 developer review (Steward, generalized to pharmacy)
area: capture-grain
evidence: Relation data is split by shape - parent/owns are clean joinable frontmatter, but pharmacy/clinical partners are prose claims in telehealth.md bodies, so "what does brand X depend on" requires reading structured + unstructured and deduping by hand. Most brands stop at "licensed US compounding pharmacy" / "licensed providers"; the few that name the entity (Curexa, Strive, OpenLoop, Wasef Health PC, CareGLP Affiliated P.C.) prove the grain is capturable. This is the prerequisite that makes MRL-005's edge joinable. Run 001 submitted a clinical-only version; developer review found it is the same gap for pharmacy.
proposed_next_step: If acknowledged, capture the named counterparty (pharmacy AND medical group) into joinable frontmatter when the page names it, recording the named entity or the explicit absence - never the possessive ("our pharmacy"). Capture-depth ask, not a new primitive. One sighting; watch for recurrence before acting.
linked_items:
  - runs/001-2026-06-19-mens-health-backend-relations/receipts/backend-relations-worksheet.md
  - MRL-005
```

### MRL-007 - Category-scoped / non-company exogenous-signal anchor

```yaml
id: MRL-007
title: Category-scoped / non-company exogenous-signal anchor - candidate, hold for recurrence
priority: P3
status: Submitted
source_run: runs/002-2026-06-19-glp1-news-monitoring
source_review: run-notes; Loop 2 developer review (Steward + Founder)
area: signals-grain
evidence: The signals that moved the GLP-1 read are category-level exogenous events - FDA compounding legality, NovoCare/LillyDirect reference pricing - that govern a whole cohort but have no per-domain home; the highest-consequence one (FDA status) has no company home at all. SIGNALS.md is strictly store/<domain>/signals/..., and already half-acknowledges this (Trends/SERP are keyword/category-grain, attached to a domain via --domain; a regulator has no domain). One sighting.
proposed_next_step: Hold, do not build. If it recurs, decide WHERE category-grain exogenous signals live - a market/topic-scoped path (e.g. store/_market/<topic>/...) vs a project-side monitor - explicitly NOT a graph, entity-resolution, non-company entity type, or served monitor (anti-Doro). The fork may resolve to "monitoring is a consumer/project cadence, not engine Signals." Gate on recurrence: a second run surfacing a homeless category-level signal.
linked_items:
  - runs/002-2026-06-19-glp1-news-monitoring/receipts/external-event-panel-2026-06-19.md
  - MRL-008
```

### MRL-008 - Minimal-monitor source-panel + source-rigor convention

```yaml
id: MRL-008
title: Minimal-monitor source-panel + source-rigor convention
priority: Low
status: Submitted
source_run: runs/002-2026-06-19-glp1-news-monitoring
source_review: run-notes; Loop 2 developer review (Dev Agent)
area: lab-artifact-convention
evidence: Run 002 improvised a reusable shape to stress a stored read against fresh external events - a small external panel plus a staleness-delta table (prior assumption -> current external reality -> verdict). Operator review found the panel was also over-confident and under-cited: snippet/news evidence is direction-finding, not citation-grade for policy/pricing claims. This is the second time a lab read invented an artifact (Run 000's denominator recipe was the first) - different artifact, same meta-pattern of in-run improvisation.
proposed_next_step: Candidate documented Loop-1 recipe/template, not a built monitor or script. Keep pattern-level: for current/news/policy/pricing reads, require exact URL, captured date, source type, primary/secondary status, and snippet-vs-fetched-body status before using confident language. Sighting #1 of a monitoring panel; watch for recurrence before promoting to a template.
linked_items:
  - runs/002-2026-06-19-glp1-news-monitoring/receipts/external-event-panel-2026-06-19.md
  - MRL-007
  - MRL-002
```

**Evidence Log**

- **2026-06-19 · Operator review:** The big Run 002 learning was not just
  "external news can invalidate a store read"; it was that lazy news fetching
  produced over-confident source tracking. Future monitoring/source-panel
  conventions should treat snippets as leads and primary pages as evidence.
- **2026-06-19 · Run 005 (first Signals-consumption sighting):** Generalizes this
  item from external-monitoring rigor to *captured-signal interpretation* rigor.
  Run 005 was the first market read to consume the Signals layer (Trustpilot, 20
  brands / 13 scorable). The captured `trust_score` conflates regard with
  solicitation posture: scores clustered 4.3–4.9 and tracked `paid_profile` +
  `asks_for_reviews`, while the only credible low score (hims 3.0) had the largest
  organic volume (8,554) and the two sub-2.5 brands had ~16–18 reviews. The confound
  flags (`paid_profile`, `asks_for_reviews`, `review_count`) are *captured correctly* —
  the risk is downstream: a consumer reading the score without its siblings will be
  misled. Candidate rule (pattern-level, NOT a build): when a read consumes a
  reputation/sentiment Signal, report the confound flags + volume alongside the score
  and keep "trusted/distrusted" a labeled, volume-weighted Judgment. Distinct grain
  from the Run 002 sighting (external snippet rigor) — same source-rigor family. First
  sighting at this grain; watch for recurrence before any convention.

### MRL-009 - Standard "write-back candidates" receipt section

```yaml
id: MRL-009
title: Standard "write-back candidates" receipt section for market reads
priority: Low
status: Submitted
source_run: runs/002-2026-06-19-glp1-news-monitoring
source_review: Loop 2 consumer review (Pantry)
area: operator-ergonomics
evidence: Three consecutive runs produced a Pantry-useful write-back output filed inside a system note rather than surfaced as a candidate - Run 000 a ~24-row store<->Notion node diff, Run 001 a ~6-edge brand->backend list, Run 002 a dated staleness/market note (Run 000's branded-price + compounding-legality claims now stale, with external cites). Three different shapes (Organizations, competitor links, market notes), same burial. Scout Q6 flagged the pattern; prior two consumer reviews declined to queue it at one/two sightings. Third sighting crosses the lab's "repeated pressure earns conventions" line.
proposed_next_step: Candidate a documented "write-back candidates" section/receipt convention so Pantry outputs surface consistently - a section, not a tool, and not auto-execution (propose-don't-write across the project boundary holds). Pattern-level; do not build a writer.
linked_items:
  - runs/000-2026-06-19-glp1-pricing-visibility/receipts/store-derived-glp1-list.md
  - runs/001-2026-06-19-mens-health-backend-relations/receipts/backend-relations-worksheet.md
  - runs/002-2026-06-19-glp1-news-monitoring/receipts/external-event-panel-2026-06-19.md
```

---

## Resolved

### MRL-004 - Market Read Lab scaffold skill

```yaml
id: MRL-004
title: Market Read Lab scaffold skill
priority: P2
status: Resolved
source_run: runs/001-2026-06-19-mens-health-backend-relations
source_review: operator-observation
area: operator-ergonomics
evidence: Creating Run 001 required manual folder creation, template copying, path references, and prompt assembly. This setup work will recur across many lab runs and is independent of the market analysis itself.
proposed_next_step: Graduated by explicit approval. Added local Claude skill `.claude/skills/market-read-lab/` with a small scaffold script that creates numbered run folders from repo templates and prints the Loop 1 prompt. No analysis, review, triage graduation, or scheduling is automated.
linked_items:
  - .claude/skills/market-read-lab/SKILL.md
  - .claude/skills/market-read-lab/scripts/new_run.py
```
