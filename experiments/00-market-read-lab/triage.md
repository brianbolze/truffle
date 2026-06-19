# Market Read Lab Triage

**Status**: Active.

**Priorities**: `P0`, `P1`, `P2`, `P3`, `Low`, `Out-of-scope`.

**Statuses**: `Submitted`, `Researching`, `Acknowledged`, `Duplicated`, `Resolved`.

## Operating Convention

Run agents are additive. They may submit new candidates or append dated **Evidence Log**
entries to existing items, but should not rewrite canonical item state.

The triage steward curates. On periodic passes, the steward may update priority/status,
reorder the Queue, merge duplicates, and rewrite `title`, `evidence_summary`, or
`proposed_next_step` so each item reflects the current best framing.

Actual graduation into Truffle system changes remains human-gated.

## Item Template

```yaml
id:
title:
priority:
status:
created_from_run:
created_from_review:
area:
evidence_summary:
proposed_next_step:
linked_items:
```

Use the YAML block as the canonical item state. If a run adds evidence or color,
append a short dated **Evidence Log** under the item instead of adding new YAML keys.
The steward can later fold recurring evidence into the canonical YAML summary.

Never touch or add **Human Notes**. That's only for Brian / humans.

## Steward Pass Log

- **2026-06-19:** Folded recurring evidence into current `evidence_summary` fields, reclassified accepted pressure to `Acknowledged`, fixed missing `MRL-009` heading, and kept graduation as human-gated. No `Human Notes` touched.

---

## Queue

### MRL-002 - Market-read query recipes for State and Signals reads

```yaml
id: MRL-002
title: Market-read query recipes for State and Signals reads
priority: P1
status: Acknowledged
created_from_run: runs/000-2026-06-19-glp1-pricing-visibility
created_from_review: operator-observation
area: query
evidence_summary: Six reviewed runs now show recurring in-run query machinery. Runs 000/001/004 hand-built State-read patterns for entity-set union, relation grep, and category grouping. Runs 005/006/007 hand-built the same Signals-read pattern across Trustpilot, Wayback, and SEC-EDGAR captures - latest-per-dir, field extraction, integrity/confound sibling fields, and frontmatter joins. The pressure has crossed from watch to acknowledged recipe need; still docs/recipe level, not a helper script or stored taxonomy.
proposed_next_step: Candidate for human-approved graduation - add lightweight QUERYING recipes for category grouping and Signals reads. Keep them pattern-level with anti-footguns, captured-floor language, latest-per-dir idiom, and confound-sibling rule. Do not build a helper or entity-resolution table.
linked_items:
  - runs/000-2026-06-19-glp1-pricing-visibility/receipts/operator-observation-latency.md
  - runs/001-2026-06-19-mens-health-backend-relations/run-notes.md
  - runs/004-2026-06-19-scout-candidates/run-notes.md
  - runs/005-2026-06-19-trustpilot-signals-reputation-landscape/run-notes.md
  - runs/006-2026-06-19-wayback-offer-tenure-landscape/run-notes.md
  - runs/007-2026-06-19-sec-edgar-funding-footprint/run-notes.md
```

**Human Notes**
- **2026-06-19**: [Brian] After run 004, I decided to upgrade the priority to P1. 

**Evidence Log**

- **2026-06-19 · State-read recurrence:** Runs 000/001/004 each reinvented a different store-query surface in-run. The shared pressure is a documented query recipe layer, not a hard-coded GLP-1 helper or stored per-SKU category taxonomy.
- **2026-06-19 · Signals-read trigger met:** Runs 005/006/007 repeated the same raw Signals consumption loop across three signal grains. This earns a human look at a QUERYING signals-read recipe; the SEC CIK collision stays only a watch item unless a second cross-domain issuer collision appears.
- **2026-06-19 · State price-posture recipe recurred (run 008):** The TRT/hormone price-visibility read reused the exact State-read loop from run 000 (frontmatter grep → latest-capture + `offerings.md` `Visibility`-column extract → group/label), now on a second cohort. The recipe is "filter `telehealth.md` by `anchor_category`/`audience`, read the `Visibility` row per brand, label by business model." Confirms the *State* half of MRL-002 at recipe-level; still no helper script wanted.
- **2026-06-19 · State *positioning*-read recurrence + a field-fidelity guard (run 009):** The longevity/NAD positioning read extended the recipe family beyond pricing to a *positioning/credibility* surface — `anchor_category` grep → `Credibility & access` + `Notes` section read → supply↔diagnostic axis labeling. Same latest-capture + field-extract + group/label idiom, different captured surface. Loop 2's adversarial verifier caught **two field-read errors** (a "three of four" vs "four of four" Schedule-III count contradicted by the read's own table; gethealthspan's `access_model`/`Labs` re-derived from prose as "membership/required" when frontmatter says `à-la-carte/both` + `optional`). Both trace to *re-deriving fields from prose*. Adds a concrete guard to the recipe: **panel cells must quote frontmatter (`access_model`, `Labs:`) verbatim, never paraphrase from `Notes`.** Still recipe-level; no helper or stored taxonomy wanted.
- **2026-06-19 · State *offer-structure*-read recurrence + a prose-surface flavor (run 010):** The GLP-1 offer-ladder read (`anchor_category: GLP-1` grep → 19 brands → `site_notes`/Portfolio/Visibility-rule read → entry-offer/commitment/membership-wedge/price-visibility classification) is the **third** State-read surface, after price-posture (008, the `Visibility` *column*) and positioning (009, `access_model`/`Credibility` *frontmatter*). The new wrinkle: offer-structure attributes (billing cadence, upfront-multi-month, membership wedge) live in **narrative `site_notes` prose, not a greppable field** — extraction was read-prose-then-extract, not field-lookup. Loop 2's adversarial verifier re-checked 14 load-bearing sub-claims: **13 confirmed verbatim, 1 partial (the ≈9/≈7 split count, defensible), 0 contradicted** — 009's "quote, don't re-derive" guard held. Two refinements for the recipe: (a) a **prose-surface variant** — when the attribute isn't a discrete field, quote the sentence verbatim and label the interpretation as a Judgment cell; (b) an **ambiguous-cell flag** — when a classification overrides a brand's own surface signal (e.g., remedymeds' homepage "No Memberships" vs. its internal "membership" charge; tryshed/joinfound mixed lanes), say so. Still recipe-level; no helper or stored taxonomy wanted.

### MRL-008 - Captured-signal source-rigor and confound convention

```yaml
id: MRL-008
title: Captured-signal source-rigor and confound convention
priority: P1
status: Acknowledged
created_from_run: runs/002-2026-06-19-glp1-news-monitoring
created_from_review: run-notes; Loop 2 developer review (Dev Agent)
area: source-rigor
evidence_summary: Source-rigor pressure has matured from external snippet discipline into a broader Signals-consumption convention. Run 002 showed snippets/news are leads, not evidence for policy/pricing claims. Runs 005/006/007 then showed three captured Signal headline fields that mislead unless their integrity context travels with them - Trustpilot trust score needs paid-profile/review-volume flags, Wayback tenure days needs continuity/snapshot-density context, and SEC total hits needs match/vehicle/CIK/existence-only flags. The family is real, but the root causes differ, so the convention must name the confound flavor instead of flattening them.
proposed_next_step: Candidate for human-approved graduation - document a flavor-aware rule that headline Signal fields must travel with their integrity/confound siblings before a read uses confident language. Keep verdicts such as trusted, established, or funded as labeled Judgments. No monitor, score, or new schema yet.
linked_items:
  - runs/002-2026-06-19-glp1-news-monitoring/receipts/external-event-panel-2026-06-19.md
  - runs/005-2026-06-19-trustpilot-signals-reputation-landscape/run-notes.md
  - runs/006-2026-06-19-wayback-offer-tenure-landscape/run-notes.md
  - runs/007-2026-06-19-sec-edgar-funding-footprint/run-notes.md
  - MRL-002
  - MRL-007
```

**Evidence Log**

- **2026-06-19 · External-current rigor:** Run 002 showed lazy news/snippet sourcing can make a store read overconfident. Primary URLs, capture dates, and source grade are required for current/news/policy/pricing claims.
- **2026-06-19 · Captured-signal confounds:** Runs 005/006/007 repeated the same consumer risk across different signal types. The headline field is captured correctly, but a naive read is wrong unless the confound/integrity fields are surfaced with it.

### MRL-001 - Market denominator reconciliation convention

```yaml
id: MRL-001
title: Market denominator reconciliation convention for market reads
priority: P2
status: Acknowledged
created_from_run: runs/000-2026-06-19-glp1-pricing-visibility
created_from_review: run-notes; Loop 2 consumer + developer review
area: denominator-reconciliation
evidence_summary: Run 000 showed the market denominator can be slow, partial, and method-sensitive. The internal store out-completed Notion Organizations for the GLP-1 read, and the store-to-Notion symmetric diff was useful both as missing-company radar and as a Pantry write-back/capture worklist. Later runs touched denominator issues but mostly strengthened MRL-002's query-recipe case; MRL-001 remains the artifact/convention for naming sources checked, inclusion/exclusion rules, resolver/dedupe method, known gaps, and confidence language.
proposed_next_step: Acknowledge as a lightweight market-read section or receipt convention. External SERP/listicle panels should be fallback sources when internal curated lists are thin, not the default denominator source.
linked_items:
  - runs/000-2026-06-19-glp1-pricing-visibility/receipts/notion-organizations-glp1-denominator-seed.md
  - runs/000-2026-06-19-glp1-pricing-visibility/receipts/store-derived-glp1-list.md
  - MRL-002
  - runs/008-2026-06-19-trt-mens-health-price-visibility/run-notes.md
```

**Evidence Log**

- **2026-06-19 · Cohort-boundary labor recurred (run 008):** The TRT/hormone price-visibility read's only real toil was drawing the denominator — TRT-vs-longevity and exogenous-T-vs-SERM edges, plus excluding generalist all-gender brands that also run TRT lines. The headline 42/42/17 split *depends* on those calls, and multi-cohort straddlers (Hone, getOpt, Lifeforce) are named concretely for the first time. Reinforces the convention need: name sources checked, inclusion/exclusion rules, and known gaps, and surface straddlers for human judgment rather than forcing a silent call.
- **2026-06-19 · Positive contrast — clean frontmatter cut nearly erases the labor (run 009):** The longevity/NAD positioning read drew its cohort with a *single grep* on `anchor_category: longevity/NAD` (8 brands), needing only two straddlers (getopt, joinfridays) hand-called. The opposite of run 008's hand-drawn TRT boundary. Useful contrast: when a clean closed-set frontmatter cut exists, denominator reconciliation is cheap; the labor MRL-001 names is real only where the boundary is fuzzy (molecule/audience edges), not where a frontmatter field already partitions the set.

### MRL-003 - Depth-backfill in-cohort module gaps

```yaml
id: MRL-003
title: Depth-backfill in-cohort module gaps (altRx, Marque)
priority: P2
status: Acknowledged
created_from_run: runs/000-2026-06-19-glp1-pricing-visibility
created_from_review: run-notes; Loop 2 developer review (Steward)
area: corpus-health
evidence_summary: altrx-com and marquelongevitylab-com are in-cohort but not queryable on the module cuts needed for market reads. altRx is GLP-1-led by profile but lacks telehealth.md/offerings.md; Marque lacks telehealth.md. This silently shrinks cohort queries and is concrete corpus-health work rather than a new primitive.
proposed_next_step: Human-approved quick win candidate - run /deepen-offerings plus telehealth.md capture for altrx-com, and telehealth.md for marquelongevitylab-com. Keep it bounded to backfill, not schema work.
linked_items:
  - runs/000-2026-06-19-glp1-pricing-visibility/receipts/store-derived-glp1-list.md
```

### MRL-009 - Standard write-back candidates receipt section

```yaml
id: MRL-009
title: Standard write-back candidates receipt section
priority: P2
status: Acknowledged
created_from_run: runs/002-2026-06-19-glp1-news-monitoring
created_from_review: Loop 2 consumer review (Pantry)
area: operator-ergonomics
evidence_summary: Three consecutive runs produced Pantry-useful write-back candidates that were buried inside system notes rather than surfaced consistently - Run 000 had a store-to-Notion node diff, Run 001 had brand-to-backend relation candidates, and Run 002 had a dated staleness/market note. The repeated value is a visible proposed-writeback section, not auto-execution.
proposed_next_step: Acknowledge as a documented market-read receipt section for write-back candidates. Keep propose-dont-write across the project boundary; do not build a writer or mutate Notion.
linked_items:
  - runs/000-2026-06-19-glp1-pricing-visibility/receipts/store-derived-glp1-list.md
  - runs/001-2026-06-19-mens-health-backend-relations/receipts/backend-relations-worksheet.md
  - runs/002-2026-06-19-glp1-news-monitoring/receipts/external-event-panel-2026-06-19.md
```

### MRL-005 - Named-counterparty relation edge

```yaml
id: MRL-005
title: Named-counterparty relation edge - hold for recurrence
priority: P3
status: Submitted
created_from_run: runs/001-2026-06-19-mens-health-backend-relations
created_from_review: run-notes; Loop 2 developer review (Founder + Steward)
area: relations
evidence_summary: Across 18 men-led/hormone telehealth brands, named pharmacy/clinical counterparties already resolve to store profiles, so a brand-to-backend edge could join cleanly and supplier concentration is a useful market read. But named counterparties were the minority, the claims are contaminated by ambiguous possessive language, and existing parent/owns plus pharmacy_model already cover the cleaner relation cases.
proposed_next_step: Hold. Re-test on a backend-naming-dense cohort such as compounding-heavy GLP-1 before graduating. If it later graduates, implement only as joinable dotted-domain frontmatter mirroring parent/owns, not a new edge table or relation-type registry. MRL-006 remains the capture-grain prerequisite.
linked_items:
  - runs/001-2026-06-19-mens-health-backend-relations/receipts/backend-relations-worksheet.md
  - MRL-006
  - MRL-002
```

### MRL-006 - Named-counterparty capture-grain gap

```yaml
id: MRL-006
title: Named-counterparty capture-grain gap
priority: P3
status: Submitted
created_from_run: runs/001-2026-06-19-mens-health-backend-relations
created_from_review: run-notes (clinical-only P3); Loop 2 developer review (Steward, generalized to pharmacy)
area: capture-grain
evidence_summary: Relation data is split by shape. Parent/owns are clean joinable frontmatter, while pharmacy/clinical partners are prose claims in telehealth.md bodies, so "what does brand X depend on" requires structured plus unstructured reading. The few named counterparties prove the grain is capturable, but this is still a one-cohort/prerequisite sighting.
proposed_next_step: Watch for recurrence. If acknowledged later, capture named pharmacy and medical-group counterparties into joinable frontmatter when the page names them, recording explicit absence when useful and never treating possessive language like "our pharmacy" as a named entity.
linked_items:
  - runs/001-2026-06-19-mens-health-backend-relations/receipts/backend-relations-worksheet.md
  - MRL-005
```

### MRL-007 - Category-scoped / non-company exogenous-signal anchor

```yaml
id: MRL-007
title: Category-scoped / non-company exogenous-signal anchor - hold for recurrence
priority: P3
status: Submitted
created_from_run: runs/002-2026-06-19-glp1-news-monitoring
created_from_review: run-notes; Loop 2 developer review (Steward + Founder)
area: signals-grain
evidence_summary: Run 002 surfaced category-level exogenous events - FDA compounding legality and NovoCare/LillyDirect reference pricing - that govern a cohort but have no per-domain signal home. Later Signals runs did not strengthen the case; Trustpilot, Wayback, and SEC-EDGAR all attached cleanly to per-domain paths.
proposed_next_step: Hold. If another read surfaces a homeless category-level signal, decide whether it belongs in a market/topic-scoped path or as a project-side monitor. Explicitly do not create a graph, entity-resolution layer, non-company entity type, or served monitor from one sighting.
linked_items:
  - runs/002-2026-06-19-glp1-news-monitoring/receipts/external-event-panel-2026-06-19.md
  - runs/006-2026-06-19-wayback-offer-tenure-landscape/run-notes.md
  - runs/007-2026-06-19-sec-edgar-funding-footprint/run-notes.md
  - MRL-008
```

**Evidence Log**

- **2026-06-19 · Negative recurrence check:** Runs 005/006/007 all consumed per-domain Signals cleanly. No new evidence for a category-grain signal home beyond the original Run 002 sighting.

### MRL-010 - Reviews/forums body content as a source ingredient

```yaml
id: MRL-010
title: Reviews/forums body content as a source ingredient - hold for recurrence
priority: P3
status: Submitted
created_from_run: runs/009-2026-06-19-longevity-positioning-whitespace
created_from_review: Loop 2 developer review (adversarial workflow)
area: source-panel
evidence_summary: Two reads in the same sprint hit the same wall - strategist trust/whitespace and customer-pain questions need review/forum BODY content (objection mining, distrust of compounded NAD, churn complaints), not just ratings. Run 008 fired source-panel for customer-pain/trust; run 009 fired it again for longevity trust/whitespace. The store already captures Trustpilot/review *scores* in profile.md Credibility blocks, but not the review *bodies*, so the trust dimension of a positioning read is unanswerable store-only. Two sightings across two different read questions on adjacent runs is enough to name the gap; not enough to prescribe a schema change.
proposed_next_step: Hold for a third sighting. If it recurs, decide whether review/forum body content earns a place in profile.md (qualitative pull-quotes) or a signals/<source_type> capture grain. Do not build a scraper, monitor, or non-company entity from two sightings; keep ratings-vs-bodies as the concrete delta.
linked_items:
  - runs/008-2026-06-19-trt-mens-health-price-visibility/run-notes.md
  - runs/009-2026-06-19-longevity-positioning-whitespace/developer-review.md
  - MRL-008
```

**Evidence Log**

- **2026-06-19 · Second sighting (run 009):** The longevity/NAD positioning read's load-bearing whitespace ("do buyers trust this / what do they regret") and trust-gap claims need review/forum bodies the store doesn't hold as State. Ratings appear in some profile.md Credibility blocks; review content does not. Same underlying need as run 008's customer-pain read, fired by a different question.

---

## Resolved

### MRL-004 - Market Read Lab scaffold skill

```yaml
id: MRL-004
title: Market Read Lab scaffold skill
priority: P2
status: Resolved
created_from_run: runs/001-2026-06-19-mens-health-backend-relations
created_from_review: operator-observation
area: operator-ergonomics
evidence_summary: Creating Run 001 required manual folder creation, template copying, path references, and prompt assembly. This setup work will recur across many lab runs and is independent of the market analysis itself.
proposed_next_step: Graduated by explicit approval. Added local Claude skill `.claude/skills/market-read-lab/` with a small scaffold script that creates numbered run folders from repo templates and prints the Loop 1 prompt. No analysis, review, triage graduation, or scheduling is automated.
linked_items:
  - .claude/skills/market-read-lab/SKILL.md
  - .claude/skills/market-read-lab/scripts/new_run.py
```
