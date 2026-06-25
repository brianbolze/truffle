# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
learning_tags: [schema-edge-entity-type, query-time-grouping-enough, denominator-reconciliation, source-rigor, tooling-ergonomics]
```

## 30-second operator read

- **Did the run work?** Yes — clean gap-probe landing. The store's biggest category token (`Services / Consulting`, 61 primary / ~82 anywhere) is a residual catch-all when read alone, but the discriminating cut already lives in existing State (the offering_category *pair* + `entity_type`). No new primitive needed (L005 vindicated; L006 cousin).
- **What was awkward?** Denominator is counting-method-sensitive: 61 primary vs ~82 anywhere vs 73 exact-token-frequency. Inline `# STRAIN` comments on the token line break naïve grep counts.
- **What should the next agent know?** The 52/9 telehealth-vs-professional split keys cleanly on the presence/absence of a `Biotech / Pharma` secondary. The honest fix, if anything graduates, is a one-line *reading convention* (don't cut on the primary token alone), not a sub-category.

## What happened

Store-only read. Grepped all 145 `store/*/profile.md` for `offering_category`; extracted the primary (first-array) token; found 61 with `Services / Consulting` primary. Split by `Biotech / Pharma` secondary → 52 telehealth wrappers / 9 professional-services. Pulled Overview prose for the 9 discriminating non-telehealth primaries to name sub-shapes (agency ×5, VC ×1, B2B health infra ×1, membership primary care ×1, energy services ×1). Wrote read.md + receipt C1. No live evidence, no spend, no store mutation.

## Observations

Greedy raw learning for this run. Preserve singletons here, then Loop 2 appends the
useful rows to `learning/observations.md`. Do not merge rows, dedup into backlog items,
or translate wishes into build proposals inside the run.

Use short IDs such as `F1`, `S1`, `W1`, `G1` so reviews can cite them. Kinds are the
closed set: `friction` · `surprise` · `wish` · `gap` · `risk-miss` · `brian-correction`.
Record the symptom in `Saw`; put the boundary you are deliberately not asserting in
`Not claiming` (no fix, no build proposal).

| ID | Kind | Saw | Not claiming | Evidence pointer | Tags |
|---|---|---|---|---|---|
| G1 | gap | The store's most-loaded category token, `Services / Consulting` (61 primary, ~82 anywhere — half the store), is a **residual catch-all when read as a primary token in isolation**: it merges ≥6 non-comparable jobs/buyers — DTC telehealth care-wrappers (52), creative/brand agencies (5: ideo, redantler, bullish, heco, parlance), VC partnership (lsvp), B2B telehealth infra (openloop), membership primary care (onemedical), renewable-energy project services (euclid). A cross-store cut keyed on the lead token alone silently merges IDEO + Lightspeed + henrymeds + Euclid into one "category." | That a new sub-category/field is needed — the discriminating cut already exists in State (see S1); only that the *primary token alone* over-merges. | read.md Result/C1; receipts/C1 | schema-edge-entity-type, denominator-reconciliation, query-time-grouping-enough |
| S1 | surprise | **The discriminating signal lives in the offering_category *pair*, not the primary token.** Presence/absence of a `Biotech / Pharma` secondary splits the 61 primaries 52 (telehealth wrapper) / 9 (professional services) with 100% clean separation in-sample; `entity_type: Investor / Holding` then flags VC. So `Services / Consulting` primary is doing two unrelated jobs at once — a telehealth-cohort *convention* AND a catch-all *residual* — which is exactly why reading it alone over-claims. The store can already discriminate; a reader just has to read the whole array + entity_type. | That the pair is a guaranteed universal discriminator — clean *in this sample*; a mis-tagged Biotech secondary on a non-telehealth firm would break it (none found). | read.md Result/Market Pattern; receipts/C1 | query-time-grouping-enough, schema-edge-entity-type |
| G2 | gap | **The bucket denominator is counting-method-sensitive.** Three defensible counts disagree: 61 (primary/first-array token), ~82 (token anywhere in array), 73 (raw exact-token frequency). The 82-vs-73 gap is an artifact: inline `# STRAIN`/qualifier comments on the token line break naïve exact-string matching. A "how many Services/Consulting companies" headline is meaningless without naming primary-vs-anywhere and the comment-stripping method. | That any one count is "the" number — only that the figure depends on a stated counting rule (L004 denominator-reconciliation in miniature). | receipts/C1; read.md Evidence Used C1 | denominator-reconciliation, source-rigor |
| S2 | surprise | **The "why this token" reasoning is unevenly machine-readable.** Some profiles carry an inline `# STRAIN`/qualifier comment explaining the assignment (firstround, sequoiacap, clerky, warbyparker, niagenplus, hims, keeps); most do not. So the captor's rationale for a contested classification exists as prose where it exists at all — there is no uniform structured "classification-rationale" surface, which is fine for reading but means the over-merge risk (G1) is invisible to a structured query that doesn't read prose. | That a structured rationale field should be built — only that STRAIN-comment coverage is partial, so absence of a comment ≠ absence of strain. | read.md Missing/Stale; several profile.md `# STRAIN` lines | source-rigor, schema-edge-entity-type |
| VR1 | risk-miss | (Evidence verifier, Loop 2) **The read's "the pair discriminates cleanly / counterexample none found" was an overreach — corrected in read.md.** Within the 9 non-telehealth primaries, **6 collapse to the identical `(Company, [Services / Consulting])` pair** (ideo, onemedical, redantler, bullish, heco, parlance) and 2 more share `(Company, [Services / Consulting, Software / SaaS])` (euclid, openloop) — non-comparable jobs the pair + entity_type cannot separate. So the pair cleanly peels the 52 telehealth wrappers off the residual, but does NOT discriminate *within* the residual; that needs prose/cohort tags. Also: the 61 count is method-sensitive (a *naïve* first-element parse → 68; correct 61 needs stripping inline `# STRAIN` comments first). Core finding (token is a residual catch-all; no new primitive) survives, sharpened. Same verifier-catches-a-slip value as runs 042/045/047/048/049 VR1. | That the finding is wrong — the catch-all + no-new-primitive core holds; only that "clean discriminator / none found" overstated the pair's power within the 9-firm tail. | read.md Result/Gap Map/What-Would-Change pre/post; group-by over the 9 primaries; receipt C1 | source-rigor, schema-edge-entity-type |
| W1 | wish | If anything ever graduates from G1/S1, the lightest path is a **one-line reading convention** in QUERYING.md or TAXONOMIES.md — "never group/compare on the `Services / Consulting` primary token alone; read the offering_category pair + entity_type" — **NOT** a sub-category, field, or stored object (the data to discriminate already renders). Load-bearing reason: the failure is *reader over-merge*, not missing capture. Mirrors the 036–049 anti-sprawl W1 landings (cut is in State; fix is a recipe, not a primitive). | That it should graduate now — only the lightest path *if* a real downstream consumer is shown to be materially burned by the over-merge. "No new primitive needed" stays live. | read.md Gap Map / What Would Change; .claude/rules/engine-dev.md ("queryability is the product"; "add a field only when it divides a real question") | query-time-grouping-enough, tooling-ergonomics |

## Inputs and scope

- **Slice:** all 145 `store/*/profile.md`; focus on the 61 with `Services / Consulting` as primary `offering_category` token, plus ~21 secondary-token holders for heterogeneity context.
- **Fields read:** `offering_category` (array, primary + secondary), `entity_type`, inline `# STRAIN`/qualifier comments, `## Overview` prose for the 9 discriminating non-telehealth primaries.
- **Refs:** SCHEMA.md / TAXONOMIES.md (token's intended meaning), L005 / L006 (lessons), `.claude/rules/engine-dev.md` (queryability-is-product, field-as-a-cut).
- **Exclusions:** no live browsing, no spend, no store mutation, no sub-category minted. Media/Content (n=2) and CPG (n=2) too thin to read — logged as coverage note, not in scope.

## Live evidence plan

Required only for `bounded-live`; leave `null` for `store-only` and `local-existing`.

```yaml
live_evidence_plan: null
# For bounded-live, paste the selected Scout plan here.
# Default light ceilings: 2 source families, 6 outside sources read/captured,
# 20 paid capture credits. Lower if Scout set a tighter plan.
# Fail closed before exceeding the ceiling, adding an unplanned source family,
# broadening into search/crawl, or using login/paywalled/private sources.
```

## Live evidence used

Required for every outside source used in `bounded-live`. Leave `[]` for local-only runs.

```yaml
live_evidence_used: []
# For bounded-live entries:
# - source_or_query:
#   source_family:
#   action_taken: searched | opened | captured | scraped | read-local-signal
#   reason:
#   source_grade: primary | secondary | direction-finding
#   captured_at:
#   spend_note: none | free | paid-credit
#   claim_ids_supported: []
```

## Friction log

Minor: token-frequency counting is brittle to inline `# STRAIN` comments (G2). Primary-token extraction needed first-element parsing, not a plain `grep -c`. No missing helper rose to the level of a recipe ask this run.

## Evidence limits

- In-sample only: the 52/9 split and the pair-discriminates-cleanly claim hold across the 61 captured primaries; not a universal guarantee (a mis-tagged Biotech secondary would break it — none found, said as "not found," not "not there").
- STRAIN-comment coverage is partial (S2), so the captor's classification rationale isn't uniformly available.
- No external completeness needed — the denominator is the store itself.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a**
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no mutation, no live browse, no primitive minted)
- Required citations / receipts present and source-graded: **pass** (receipt C1, primary store grade)
- No snippet treated as evidence: **pass** (store-only)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no current/pricing claims; per-profile `captured_at`)
- Absence language says "not found", not "not true": **pass**

## Surprises

The cleanest finding was the inverse of the hypothesis: the bucket *is* a catch-all (G1), but the store already carries the discriminating cut in the array pair + entity_type (S1), so the over-merge is a reading hazard, not a capture hole. The token quietly serves two unrelated jobs at once (telehealth convention + residual). See Observations S1/S2.

## Learning tags

Short `kebab-case` recurrence handles for system pressure this run exposed. They mirror
the run header's `learning_tags`. These are not a fixed taxonomy and not permission to
build — a learning pass decides what, if anything, recurs into a lesson.

Use an existing tag when it fits; coin a narrow tag only when the guide misses the thing.

| Tag | Use when |
|---|---|
| `denominator-reconciliation` | The answer depends on defining / cleaning / reconciling the company or source **set**. |
| `source-rigor` | Source grade blocks confidence: snippets, weak secondary sources, missing URLs, or missing capture dates. |
| `source-panel` | A repeated external source **set** seems needed to answer this kind of question. |
| `coverage-caveat` | Store coverage, stale captures, or incomplete modules materially limit the answer. |
| `depth-backfill` | A specific field/module is missing across otherwise relevant companies. |
| `query-time-grouping-enough` | The read was answerable by grouping existing store evidence; no durable category object is needed. |
| `freshness-monitoring` | Current pricing, news, policy, regulation, or launch motion could change or materially improve the answer. |
| `relation-pressure` | Competitors, named parents, suppliers, partners, or other counterparties seem repeatedly useful. |
| `tooling-ergonomics` | Repeated manual steps suggest a helper, query recipe, or template tweak. |

Which tags fired, if any? Did this run need a new or clearer tag? Mirror them into the
header `learning_tags`.

**Fired:** `schema-edge-entity-type` (dominant token's discriminating grain), `query-time-grouping-enough` (cut already in State; no sub-category), `denominator-reconciliation` (counting-method sensitivity), `source-rigor` (uneven STRAIN coverage, in-sample-only caveat), `tooling-ergonomics` (the lightest fix is a reading-convention recipe). No new tag needed.

"No new primitive needed" is a valid outcome — and it is this run's outcome.

## Next-run advice

- The pair-discriminates cut is worth a one-off calibration on a *different* over-loaded token (e.g., is `Software / SaaS` (34) similarly residual, or does it stay coherent?) to see whether "read the array, not the lead token" generalizes beyond Services/Consulting.
- If a learning pass ever touches this, route W1 toward a QUERYING/TAXONOMIES reading-convention note, not a schema change. It rhymes with L006 (token over-claims on edge entity types) — possible 2nd sighting for that lesson's grain.

## Next-run advice

What to try, avoid, or re-check.
