# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [source-rigor, query-time-grouping-enough, denominator-reconciliation, coverage-caveat, freshness-monitoring]
```

## 30-second operator read

- **Did the run work?** Yes. Clean store-only read; the answer is decisive and the design
  payload is sharp.
- **What was awkward?** Nothing about the data — it was already captured well. The interesting
  tension: the *honest* thing to do (refuse to rank verbatim prices) is also the *valuable*
  thing, so the read had to demonstrate the wrongness of a ranking without producing one. I
  showed two effective-monthly reconstructions explicitly labeled derived/Judgment to make the
  point, then argued against persisting them.
- **What should the next agent know?** The store's `visibility: published/partial` field is the
  unsung hero here — it already encodes "is this number self-contained." The comparability gap
  is a *query recipe* (a 4-axis normalization rubric), not a missing primitive. Don't let a
  future run quietly graduate a derived effective-price field.

## What happened

Re-verified the 19 GLP-1-anchored brands (run 012 cohort) all present in `store/`. Fanned out
three Haiku extraction passes to pull each brand's GLP-1 entry-price row verbatim from
`offerings.md` (price string, unit, what's-included, `visibility` flag, promo status). Compiled
into one receipt panel, then read for comparability. No external sources, no spend, no writes
to `store/`.

## Inputs and scope

- **Store slice:** 19 `anchor_category: GLP-1` brands' `offerings.md` (+ `site_notes`); cohort
  seeded from run 012, re-verified this run.
- **Scope:** GLP-1 weight-loss **entry** offer only (lowest/leading price per brand). Dose
  ladders and longer-plan tiers not exploded (intake-gated for ~half the cohort).
- **Exclusions:** no external/live sources; no per-dose matrix; intra-brand price conflicts
  reported not resolved.

## Live evidence plan

Required only for `bounded-live`; leave `null` for `store-only` and `local-existing`.

```yaml
live_evidence_plan: null
# For bounded-live, paste the selected Scout plan here.
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

- Pricing lives in different shapes per `offerings.md` (Roster table row vs `site_notes` prose
  vs Verbatim-anchors block). Extraction needed per-file judgment, not one grep — a recurring
  `tooling-ergonomics` smell, but mild; the `Price (verbatim)` + `Visibility` columns carried
  most of it where present.

## Evidence limits

- Entry-tier only; per-dose matrix **not found** in captured State (not proven absent).
- 8 promo prices are point-in-time (capture spread 2026-06-03 → 2026-06-18); a compare built on
  them is freshness-bound.
- Two brands carry intra-brand price conflicts across surfaces (directmeds, tryshed); which bills
  is **not found** in State.
- Effective-monthly figures (eden ~$198, hims ~$298) are **derived Judgment**, not captured —
  shown only to demonstrate why a verbatim sort misleads.

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
- No disallowed action happened: **pass** (no live/spend/store-mutation/write-back/primitive)
- Required citations / receipts present and source-graded: **pass** (1 receipt, primary store grade)
- No snippet treated as evidence: **pass** (all verbatim store files)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (per-brand `captured_at` in panel)
- Absence language says "not found", not "not true": **pass** (per-dose matrix / conflicts framed as not-found)

## Surprises

- The store's `visibility: published/partial` flag turned out to be exactly the comparability
  primitive — it already separates self-contained prices from cost-on-top, without anyone
  designing it for this question. The answer to "what primitive is missing" was "none; one you
  already have is doing the job."
- Eden's `$99` headline (cheapest verbatim number in the cohort) is structurally a loss-leader:
  add the mandatory `$99` membership and the effective floor (~$198) lands *above* genuinely
  all-in brands like telolife. The verbatim sort literally inverts the real-cost order.

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
| `query-time-grouping-enough` | Comparability is closed by a 4-axis normalization rubric run at query time over existing `visibility`+verbatim fields; no durable price-normalization object needed. | watch for recurrence — strengthens MRL-002 (query recipes); explicit "no new primitive" |
| `source-rigor` | ~8/19 entry prices are promotional/point-in-time; 2 brands carry intra-brand conflicts. A confident "cheapest" claim on these is double-false. | watch for recurrence — feeds MRL-008 (source-rigor convention): promo/point-in-time prices need a steady-state vs promo distinction |
| `denominator-reconciliation` | Answer leaned on the run-012 anchor cut; re-verified but still partial. | recurrence of MRL-001; no-op (caveated) |
| `coverage-caveat` | Entry-tier only; per-dose matrix and conflict-resolution not in captured State. | no-op / watch |
| `freshness-monitoring` | Promo prices rot; a price-compare is freshness-bound. | recurrence of MRL-012; no-op |

## Triage submissions

One candidate (Evidence Log color for an existing item; a possible new item — steward decides):

- **Strengthens MRL-002 (query recipes):** a concrete recipe candidate emerged — *"comparable
  price"* is a query-time normalization over four axes (what's-included via `visibility`,
  billing cadence/commitment, steady-state-vs-promo, binding-price-vs-floor). The store already
  carries the substrate (`visibility: published/partial` + verbatim price string + `site_notes`
  membership lines); the recipe is the missing piece, **not** a persisted normalized field.
- **Strengthens MRL-008 (source-rigor):** add a *promotional / point-in-time price* sub-case —
  captured prices that are struck-through, code-gated, or sale-framed should be treated like
  snippet-grade for any "cheapest/ranking" claim until reduced to steady-state.
- **Explicit anti-graduation note:** this run argues **against** persisting a derived
  effective-monthly price field (point-in-time, judgment-laden, rots). Flag if a future run
  tries to graduate one. No new primitive needed.

**Did not implement, spike, or graduate anything.**

## Next-run advice

- The off-telehealth generalization probe (Scout candidate 3) is the standout next question —
  it would test whether `visibility`-style flags and the normalization rubric hold off the
  intentional telehealth cohort.
- If anyone wants to *act* on a GLP-1 price compare, build the 4-axis rubric as a query recipe
  first; do not sort the verbatim numbers.
- A light re-capture pass stripping promo prices to steady-state would firm up any future
  price-compare and de-risk MRL-008's promo sub-case.
