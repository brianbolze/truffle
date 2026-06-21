# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [query-time-grouping-enough, depth-backfill, denominator-reconciliation, source-rigor]
```

## 30-second operator read

- **Did the run work?** Yes. The `published/partial/gated` price-visibility axis generalizes cleanly to a 7-brand watch cohort (5 luxury maisons publish no watch price by convention; Swatch/Casio publish everything; Cartier splits by category). store-only, no spend.
- **What was awkward?** Casio sits under `primary_industry: Technology`, so a `Consumer Goods` grep under-counts the watch cohort by 1 (hand-added). 0/7 have `offerings.md` or the structured price-visibility token — entire read came from `profile.md` prose.
- **What should the next agent know?** Two reusable nuggets to verify: **gate-type** (intake / enterprise-quote / dealer-scarcity) and **gate-grain** (brand / category / product). The luxury "price on request" is a market *posture*, not a funnel tactic — do not read it through the telehealth intake-gate lens. Run-028 token-absence trap re-confirmed on a 3rd vertical.

## What happened

Selected (Scout) the watch-cohort price-visibility read from a 5-candidate slate. Loop 1: drew the 7-brand cohort (`primary_industry: Consumer Goods` = 6 + casio under Technology), read each `profile.md` (Overview, What-they-offer, site_notes, unverified_fields, business_model, portfolio_shape), built the price-presentation map, and produced the recipe-generalization verdict. No external/live evidence; all 7 captured 2026-05-31.

## Discovery ledger

Greedy raw learning for this run. Preserve singletons here before triage compresses
anything, then Loop 2 appends the useful rows to `discovery-ledger.md`. Do not merge
rows, dedup into backlog items, or translate wishes into build proposals inside the run.

Use short IDs such as `O1`, `W1`, `F1`, `S1`, or `G1` so reviews can cite them.

| ID | Kind | Raw observation / wish / friction / surprise / gap | Evidence or pointer | Why it matters | Discovery clock |
|---|---|---|---|---|---|
| O1 | observation | Price-visibility `gated` value hides ≥3 distinct **gate types**: telehealth = sales-intake, SaaS = enterprise-quote, luxury watches = dealer/boutique/scarcity convention. | read.md Result (2); rolex/patek/ap/lange site_notes | The cut composes cross-vertical, but "gated" is not one mechanism — naive equivalence would mislabel a posture as a funnel. | recur-watch |
| O2 | observation | The price gate runs at 3 **grains**: brand (Rolex whole catalog), category (Cartier: watches gated, jewelry/fragrance published), product (Swatch MoonSwatch, Casio Moflin withheld inside a published catalog). | read.md Result (2); cartier/swatch/casio profile.md | Telehealth reads saw mostly brand-grain; this vertical makes sub-brand grain first-class. | recur-watch |
| O3 | observation | 0/7 watch brands have `offerings.md` or the SCHEMA `[published\|partial\|on-request]` token; whole read from prose. | `ls`/`grep` (this run); read.md C8 | Re-confirms run-028 (structured price-visibility token doesn't populate off telehealth) on a 3rd vertical — a naive token grep inverts the truth. | recur-watch |
| S1 | surprise | Luxury "price on request" is a deliberate exclusivity/channel/allocation posture; for Rolex/Patek the real gate is the dealer waitlist, not the website. | read.md Result (2), Gap Map | Semantic mismatch with telehealth/SaaS gating — the contracted failure mode; held cleanly as Judgment, not State. | recur-watch |
| G1 | gap/friction | `primary_industry: Consumer Goods` grep returns 6; casio is under `Technology`, so the watch cohort is under-counted by 1 without a hand-add. | read.md Companies Seen | Cross-field under-count flavor of MRL-001's anchored-only caveat, now on a non-telehealth slice. | recur-watch |
| W1 | wish | A reading-discipline addend (not a field): when reading price visibility, name gate-type × gate-grain. | read.md Result (2), Market Pattern | Lightest possible fix if it recurs; explicitly NOT a `gate_type`/`price_visibility` enum migration. | recur-watch |

## Inputs and scope

- Cohort: 7 brands — rolex-com, patek-com, audemarspiguet-com, alange-soehne-com, cartier-com (luxury); swatch-com, casio-com (accessible).
- Drawn from `grep '^primary_industry:' store/*/profile.md` (Consumer Goods = 6) + hand-add of casio (under Technology, but a watch-catalog brand).
- Files read: each brand's `store/<domain>/profile.md` (Overview, What they offer, site_notes, unverified_fields, business_model, portfolio_shape). Checked `ls store/<d>/` and token grep for structured price-visibility surface (0/7).
- Exclusions: maintenance/service pricelists (AP, Lange) — not product pricing. No external/live sources (store-only contract).

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

- One cross-field denominator wrinkle (G1): the watch cohort doesn't sit under a single `primary_industry` value (Casio is `Technology`), so a clean grep under-counts by 1 and needed a hand-add. Minor; same flavor as MRL-001's anchored-only caveat.
- No `offerings.md` for any of the 7, so the structured price-visibility surface was unavailable — read fell back to prose (expected per run-028, not a surprise).

## Evidence limits

- Actual luxury watch price *levels* are not on any captured page by design — unreachable store-only; correctly left unstated ("not published," not "not true").
- The scarcity/allocation/waitlist gate (esp. Rolex/Patek) is market knowledge, not owned-page State — labeled Judgment.
- Uniform 2026-05-31 capture (~20 days); fine for a posture read, accessible-tier price levels are point-in-time.

## Loop 1 exit check

Record `pass` / `fail` for the mandatory exit check before setting final `run_status`.

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a**
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no live browsing, no spend, no store mutation, no triage graduation)
- Required citations / receipts present and source-graded: **pass** (C1–C8, all primary local paths)
- No snippet treated as evidence: **pass** (no external snippets used)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (all 2026-05-31, primary)
- Absence language says "not found", not "not true": **pass** (luxury "no online price" framed as deliberate posture / not-published, never as capture failure)

## Surprises

- The luxury gate is a market posture, not a conversion funnel (S1) — semantically distinct from the telehealth intake-gate the lab has read 4×. Held as Judgment.
- The gate runs at category grain *inside* Cartier (watches gated, jewelry/fragrance published) and at product grain (MoonSwatch, Moflin) — sub-brand grains the telehealth reads rarely surfaced (O2).

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
| `query-time-grouping-enough` | The whole read was a grouping over existing prose State; no durable category/field needed. | no-op (reinforces MRL-002) |
| `depth-backfill` | 0/7 watch brands have `offerings.md` or the structured price-visibility token; signal lives in prose only. | watch for recurrence (reinforces MRL-008 run-028 branch; backfill gap, not defect) |
| `denominator-reconciliation` | Casio under `Technology` breaks a single-grep `Consumer Goods` cohort draw (under-count by 1). | watch for recurrence (MRL-001 cross-field flavor on a non-telehealth slice) |
| `source-rigor` | Luxury "no online price" must read as deliberate posture, not capture failure; gate-type semantics differ across verticals. | watch for recurrence (MRL-008 — a gate-type-semantics flavor) |

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

- **Loop 2 re-check:** verify the 7-brand split (5 luxury gated / Cartier partial / Swatch+Casio published) against each `profile.md`; confirm 0/7 have `offerings.md`/token (C8); pressure-test the gate-type × gate-grain framing (O1/O2) — that distinction carries the generalization verdict.
- **Try later:** a 4th price-visibility vertical (Finance/VC — "rate card vs quote-gated advisory") would, if it shows the same gate-type×grain pattern, harden W1 toward an MRL-002 reading-discipline addend. Until then it's recur-watch, no build.
- **Avoid:** reading luxury "price on request" as an intake-funnel or a coverage gap; claiming the structured price-visibility token works off telehealth (it's 0/7 here).
- **Note:** runner-up Scout candidate D (offerings-roster completeness) still untested — revisit if a completeness-grain calibration is wanted.
