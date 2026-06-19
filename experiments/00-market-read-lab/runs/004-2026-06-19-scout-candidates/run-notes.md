# Run Notes

```yaml
run_status:            reviewed
evidence_mode:         store-only
autonomous_eligible:   yes
termination_reason:    completed
pressure_lenses_fired: [denominator-reconciliation, source-rigor, coverage-caveat, tooling-ergonomics]
```

## 30-second operator read

- **Did the run work?** Yes. Store-only, no spend, no mutation. Clean answer:
  GLP-1 is the most crowded captured-telehealth category by far (19/53 front door,
  41/53 selling it); mental health is the thin floor (10/53).
- **What was awkward?** There is no per-SKU category tag in the store, so the
  breadth count had to be hand-derived from molecule strings in roster cells. A naive
  whole-file grep inflated badly (TRT 53/53, labs 53/53) and had to be thrown out.
- **What should the next agent know?** The front-door (`anchor_category`) cut is clean
  and normalized; the breadth cut is *directionally* solid but its mid-band ranks are
  method-sensitive. Third sighting of the denominator/query-ergonomics pressure.

## What happened

Gated on the contract (scout-only → store-only → autonomous, all pass), then answered
the selected question entirely from `telehealth.md` + `offerings.md` frontmatter/roster.
Built two crowdedness cuts: front-door `anchor_category` (one per brand) and a
breadth count (distinct brands with a buyable SKU whose molecule cell names the
category). Cross-checked the two; surfaced the GLP-1 bolt-on pattern. One receipt.

## Inputs and scope

- Working set: **53 DTC telehealth brands** = `store/*/telehealth.md` packs gated to
  `value_chain_role == "DTC brand"` (54 packs total; 1 excluded — functionhealth-com,
  `diagnostics/labs`). All 53 also carry `offerings.md`.
- Files: `store/*/telehealth.md` (frontmatter), `store/*/offerings.md` (`## Roster`).
- Exclusions: non-telehealth profiles; non-DTC roles; family header rows in rosters.
- No external sources, no `store.py` resolve needed (slug ↔ pack join was 1:1).

## Friction log

- **No normalized per-SKU category field.** Breadth-by-category is not a stored cut;
  it had to be computed at query time from molecule strings. (`denominator-reconciliation`,
  `tooling-ergonomics`)
- **Whole-file grep is a trap.** First breadth pass over full file bodies returned
  TRT 53/53 and labs 53/53 — comparison/FAQ/negation prose. Switched to a roster-cell,
  buyable-row match. (`source-rigor`)
- Inline `#` comments on frontmatter values (esp. trailing on `anchor_category` /
  `value_chain_role`) must be stripped before counting, or values fragment.

## Evidence limits

- Captured telehealth only — the one deep cohort (135 profiles, 54 telehealth, 67
  offerings). Every count is a captured floor; "thin" = few captured brands, not thin
  market. (`coverage-caveat`)
- Breadth mid-band ranks (peptides/longevity/TRT, all 27–30) are close enough that
  molecule-set choices could reorder them. GLP-1 lead + mental-health floor are robust.
- Captures ~16–20d old at oldest; recent but not real-time. No price value used.

## Loop 1 exit check

Record `pass` / `fail` for the mandatory exit check before setting final `run_status`.

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only` or `local-existing`: **pass** (store-only)
- `approval_needed: no`: **pass**
- No disallowed action happened: **pass** (no browse/spend, no `store/` write, no
  primitive creation, no KB write-back, only `read.md` + receipts + run-notes touched)
- Required citations / receipts present and source-graded: **pass** (receipt graded
  `derived`; C1/C2/C3 mapped)
- No snippet treated as evidence: **pass** (no external sources used at all)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass**
  (no current/news/pricing/policy claims made; counts carry capture-date ranges)
- Absence language says "not found", not "not true": **pass** ("thin" framed as
  "few captured brands / not captured", never "thin market")

All items pass → `run_status: read-done`, `termination_reason: completed`.

## Surprises

- **GLP-1 bolt-on dominance.** 22 of 53 brands sell a GLP-1 SKU without anchoring on
  it — GLP-1 is the attach-everywhere line, not just the loudest front door.
- **The cohort is one shared shelf.** The "crowded middle" (peptides/longevity/TRT/
  ED/hair/HRT, all 22–30) is largely the *same* multi-line platforms stocking
  everything, not distinct sets of specialists per category.

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
| `denominator-reconciliation` | Crowdedness-per-category needed a denominator + grouping the store doesn't store (no per-SKU category tag); had to be hand-built at query time. | **Third sighting** — strengthens MRL-001/002. Submit as evidence-log, do not graduate. |
| `tooling-ergonomics` | Same as above from the helper angle: a third distinct market read re-invented store-query machinery in-run (Run 000 union, Run 001 relations grep, now category breadth). | Append to MRL-002 evidence log; recurrence now crosses "pattern, watch" → "consider a QUERYING recipe." Still a human call. |
| `source-rigor` | Naive whole-file grep produced confident-wrong breadth (TRT/labs 53/53); only a roster-cell match was trustworthy. | No-op / watch. Reinforces "molecule grep belongs in the roster cell, not the file body" (already QUERYING Recipe 4 guidance). |
| `coverage-caveat` | Telehealth is the only deep cohort; "thin" categories (esp. mental health) are likely capture artifacts, not market truth. | No-op / watch for recurrence. |

## Triage submissions

**Do not implement, spike, or recommend immediate graduation from inside the run.**

- **MRL-001 / MRL-002 — append evidence (third sighting).** This run is the third
  consecutive market read whose hard part was building a denominator + grouping the
  store doesn't hold natively, and re-inventing the query in-run. Distinct from prior
  shapes: Run 000 = entity-set union/reconciliation; Run 001 = relation-edge grep;
  Run 004 = **a missing per-SKU category dimension** forcing query-time molecule
  classification. The recurrence is now consistent enough that a *documented QUERYING
  recipe* for "group the cohort by category at query time" (inputs, roster-cell molecule
  match, the whole-file-grep anti-pattern, captured-floor language) looks earned —
  pattern-level, not a built helper, and a human decision.
- **No new tag or new queue item needed.** Existing tags covered everything.

## Next-run advice

- The front-door (`anchor_category`) cut is the clean, normalized, citable crowdedness
  measure — lead with it. Use breadth only as a directional corrective and say its
  mid-band ranks are soft.
- For any "competes in category X" count, match molecules **inside the roster cell**,
  never over the whole file — full-body grep inflates to ~100%.
- To pressure-test "mental health is thin," the lever is capturing telehealth brands
  outside the hormone/weight/longevity skew — a coverage move, not a method move.
- If a fourth run hits the same denominator/grouping wall, that is the signal to
  graduate a QUERYING category-grouping recipe (MRL-002).
