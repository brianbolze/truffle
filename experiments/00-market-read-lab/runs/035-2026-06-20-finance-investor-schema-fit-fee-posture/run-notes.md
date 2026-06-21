# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [schema-edge-entity-type, query-time-grouping-enough, denominator-reconciliation, coverage-caveat]
```

## 30-second operator read

- **Did the run work?** Yes. First market read on the store's Finance/Investor vertical;
  clean store-only gap-probe. The verdict is crisp: the schema's *subtractive* investor
  gate (MRL-015) works; the *additive* capital-allocator shape is the open gap.
- **What was awkward?** The Scout contract's "~16" denominator over-counted — the 7
  Investor/Holding profiles are a *subset* of the 9 Finance & Fintech, not disjoint.
  Reconciled to 9 (receipt C1). Whitespace-dirty `primary_industry` strings (run-033 G1
  recurrence).
- **What should the next agent know?** The headline `query-time-grouping-enough: FALSE`
  is the first clean FALSE on a *content* axis (not trust-metadata). Don't read
  `business_model: empty` for the 7 VCs as a backfill gap — it's a *contracted* gate
  (distinct from the run-028/033 structured-absence branch). n=9, subtype-skewed (5/7
  early-stage VC) — verdict is schema-fit, not a finance-market claim.

## What happened

Scout selected C1 (Finance/Investor schema-fit + fee-posture, store-only, autonomous).
Loop 1: enumerated the union (grep `primary_industry`/`entity_type`), reconciled the
denominator to 9, extracted the schema-relevant frontmatter verbatim for all 9, read the
TAXONOMIES/SCHEMA contract for the investor gate + business_model closed set, and grepped
prose for disclosed fee/AUM/stage facts. Split the slice into 2 fintech products (schema
fits, = SaaS) and 7 capital allocators (schema gates correctly but has no positive shape).
Wrote read.md + one denominator/census receipt. No spend, no live browsing.

## Discovery ledger

Greedy raw learning for this run. Preserve singletons here before triage compresses
anything, then Loop 2 appends the useful rows to `discovery-ledger.md`. Do not merge
rows, dedup into backlog items, or translate wishes into build proposals inside the run.

Use short IDs such as `O1`, `W1`, `F1`, `S1`, or `G1` so reviews can cite them.

| ID | Kind | Raw observation / wish / friction / surprise / gap | Evidence or pointer | Why it matters | Discovery clock |
|---|---|---|---|---|---|
| O1 | observation | The schema's investor accommodation is **subtractive and contracted**: `entity_type: Investor / Holding` (TAXONOMIES:19) + the portfolio_shape empty-by-rule (:72) + the convention to leave `offering_category`/`business_model` empty. Fired correctly across all 7 allocators (blueowl the lone principled `Other`). | read.md Result/Market Pattern #3; receipt C2/C7 | The *negative* half of MRL-015 is **solved and working** — the schema generalizes well at preventing wrong product-shaped data on investors. First positive confirmation of the gate. | ready-for-triage |
| O2 | observation | But there is **no positive capital-allocator field set**: fund stage, AUM/fund-size band, vintage/fund number, check size, LP type, thesis sector all live in `description`/prose or are absent — none greppable. Only `entity_type` + `primary_industry` are structured finance cuts. | read.md Gap Map; receipt C2/C3 | The *additive* half of MRL-015 is the **open gap**. First vertical where prose-only fails a recognizable cross-entity reader cut ("all seed funds," "all >$1B"). | ready-for-triage |
| O3 | observation | `query-time-grouping-enough` fires **FALSE** for the finance reader — the **first clean FALSE on a *content* axis** (every prior content read 008–034 fired TRUE; only trust-metadata reads 031/032 fired FALSE). | read.md Result; pressure tags | Sharpens what `query-time-grouping-enough` means: TRUE for telehealth/SaaS *because* those verticals have populated structured cuts; the tag is corpus-shape-dependent, not universal. | ready-for-triage |
| O4 | observation | Capital allocators expose a **4th, deeper gate-type** (run-033 W1 bar): fee = mgmt-fee + carried-interest, absent from the `business_model` closed set AND structurally off the marketing site — the site is a **founder/LP-recruiting surface, not a commerce surface**. Distinct from telehealth sales-intake / SaaS enterprise-quote / luxury dealer-waitlist (all gate a *real* price). | read.md Result (gate-type); C5/C6 | Supplies the named 4th-vertical data point that run-033 W1 set as the graduation bar for the `gate-type × gate-grain` reading-discipline addend. | ready-for-triage |
| O5 | observation | The 2 fintech *products* (stripe usage-based/published, runway subscription/quote-gated) fit the schema **identically to the SaaS slice** (run 028) — every structured field populates, price-visibility axis applies. | read.md Subtype A; receipt C6 | Confirms the split is **entity_type, not industry**: `Finance & Fintech` industry holds both a clean-fit product cohort and a gated allocator cohort. The schema discriminates correctly. | ready-for-triage |
| S1 | surprise | `business_model: empty` for the 7 allocators is **two stacked absences** — (a) *schema-can't*: no closed-set value for fund economics; (b) *firm-didn't*: 6/7 don't disclose fees/AUM on-site anyway. A naive read of empty = "no business model" is wrong on both counts. | read.md Gap Map; receipt C2/C3 | The contracted `loop1_failure_mode` made concrete: this empty surface is **categorically different** from the run-028/033 backfill-gap branch (there the empty masked *disclosed* data; here it's the schema correctly declining to assert). | ready-for-triage |
| G1 | gap/friction | `primary_industry: Finance & Fintech` parses to 4 distinct *lines* in a naive `uniq` (6 value-only + 3 with inline `# comment` suffixes; the YAML value is clean). `grep -rl` (substring/per-file) is robust; an exact-line `==` match under-counts by 3. (Verifier fix: the 3 are comment-suffixed lines, not trailing-whitespace values.) | receipt Evidence; `uniq -c` output; Loop-2 verifier G1 | **Recurrence of run-033 G1** (casio cross-field under-count) on a new field — a real, repeated cohort-draw hazard. Second sighting earns a clearer note. | ready-for-triage |
| G2 | gap | Scout contract estimated "~16" for the union; actual = **9** (the 7 Investor/Holding nest inside the 9 Finance & Fintech). | read.md Companies Seen; receipt C1 | A denominator-estimate miss at Scout time — the two sets were assumed disjoint. Cheap to catch in Loop 1, but a reminder that Scout denominators are estimates to verify, not facts. | notice-only |
| W1 | wish | If anything graduates from the additive gap (O2), the lightest fix is a **documented prose convention / query recipe** for the capital-allocator facts (stage, AUM band, vintage, thesis), **NOT** a per-investor structured field family — n=9, non-design vertical, and the facts are mostly off-site (5/7), so a structured field would be sparse and rot. "No new primitive needed" remains live; the gap only graduates if a real downstream finance-cut consumer appears. | read.md What Would Change; Market Pattern #3 | Names the anti-sprawl path consistent with "spend on conventions, not infra"; keeps MRL-015's additive half at recur-watch pending a consumer + a 2nd, less VC-skewed finance cohort. | recur-watch |
| F1 | friction | Per-profile frontmatter extraction was a hand-rolled `awk`/`grep` pass over 9 files; no MRL-002 recipe covers a "cross-entity schema-fit / field-census" read (which fields populate vs empty across a cohort). | run-notes friction log | Mirrors the recurring MRL-002 query-machinery friction, now on a **field-census** grain (distinct from value-extraction). One sighting; recur-watch. | recur-watch |

## Inputs and scope

- **Slice:** `store/*/profile.md` where `primary_industry: Finance & Fintech` (9) ∪
  `entity_type: Investor / Holding` (7) → union 9. Consulting & Professional Services (6)
  read as adjacent context only (not in the denominator).
- **Fields read (verbatim, no prose re-derivation):** entity_type, offering_category,
  portfolio_shape, business_model, primary_industry, description, parent/owns,
  unverified_fields. Prose grepped for disclosed fee/AUM/fund-size/stage facts.
- **Contract:** TAXONOMIES.md:19,72,108; SCHEMA.md:66,70 (business_model 8-value set).
- **Exclusions:** no external denominator, no live browsing, no Firecrawl/Exa spend.

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

- F1: cross-entity field-census (which fields populate vs empty across the 9) was a
  hand-rolled `awk`/`grep` pass — no MRL-002 recipe covers a schema-fit/field-census read.
- G1: whitespace-dirty `primary_industry` strings forced `grep -rl` over exact-match.

## Evidence limits

- n=9 and subtype-skewed (5/7 allocators are early/multi-stage VC) — supports a schema-fit
  verdict + a subtype map, **not** a "finance market" claim.
- Store-only: no external denominator, so representativeness of the 9 is unknowable here
  (acceptable — the question is schema-fit, not market completeness).
- Fee/AUM absence for 5/7 = "not found on captured marketing pages," a market disclosure
  norm, **not** a capture failure (the store correctly flags it in `unverified_fields`).

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a** (store-only)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no spend, no live browse, no store mutation, no prose re-derivation)
- Required citations / receipts present and source-graded: **pass** (receipt C1–C7, derived/primary, local-store)
- No snippet treated as evidence: **pass** (no snippets used)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (store clocks per profile; no live/current claims)
- Absence language says "not found", not "not true": **pass** (fee/AUM framed as not-on-marketing-site)

## Surprises

- S1: `business_model: empty` for the 7 VCs is two stacked absences (schema-can't +
  firm-didn't) — categorically distinct from the run-028/033 backfill-gap branch.
- The split is **entity_type, not industry**: the same `Finance & Fintech` industry holds
  a clean-fit product cohort (stripe/runway) and a gated allocator cohort.

## Pressure tags

Short `kebab-case` tags for system pressure this run exposed. These are recurrence handles, not a fixed taxonomy and not permission to build.

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

Which tags fired, if any? Did this run need a new or clearer tag?

"No new primitive needed" is a valid outcome.

| Fired tag | What fired in this run | Triage implication |
|---|---|---|
| `schema-edge-entity-type` | First market read isolating the Investor/Holding entity-type (MRL-015): the subtractive gate works (O1); the additive capital-allocator shape is the open gap (O2). | submit triage candidate (MRL-015 evidence — first positive confirmation of the gate + first market-read demonstration of the additive gap) |
| `query-time-grouping-enough` | Fires **FALSE** for the finance reader — first clean FALSE on a *content* axis (O3). | submit triage candidate (MRL-002 — sharpens the tag as corpus-shape-dependent, not universal) |
| `denominator-reconciliation` | Union reconciled 16→9 (investors nest in Finance & Fintech); whitespace-dirty industry strings (G1, run-033 G1 recurrence). | watch for recurrence (MRL-001 — 2nd cross-field grep-hazard sighting) |
| `coverage-caveat` | n=9, subtype-skewed (5/7 early-stage VC); 5/7 don't disclose fees/AUM on-site (a market norm, not a gap). | no-op (correctly bounded in the read) |

New/clearer tag? No new tag coined. `schema-edge-entity-type` (first used run 027) fits
cleanly and is the load-bearing one this run.

## Optional triage evidence

Normally none. Add only concrete backlog evidence, with priority/status suggestions,
when the run has more than a raw singleton or when review adds evidence to an existing
item. Keep this to 1-3 backlog-ready bullets plus pointers to the Discovery ledger,
`discovery-ledger.md`, or run artifacts.

**Do not implement, spike, or recommend immediate graduation from inside the run.**
Raw learning belongs in the run Discovery ledger and `discovery-ledger.md`. Submit
triage only when the run adds enough evidence for a stewarded backlog item or Evidence
Log entry.

## Next-run advice

- The natural follow-up is a **second, less VC-skewed finance cohort** (more public asset
  managers / PE / banks / fintech infra) to test whether O2's "no positive shape" gap
  recurs or is a VC-cohort artifact, and whether blueowl's `business_model: Other`
  recurs for fee-bearing allocators.
- Don't re-run the price-visibility axis a 5th time unless it closes a new design
  decision — run-033 W1's 4th-vertical bar is now supplied (O4).
- The SERP-signal calibration (C3 in this run's slate) remains the strongest unrun
  candidate to complete the signals-family calibration set.
