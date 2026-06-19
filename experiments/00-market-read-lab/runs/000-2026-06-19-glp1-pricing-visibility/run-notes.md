# Run Notes

> **Historical run notice:** This run predates the current autonomous contract. Use it
> for evidence and pressure patterns only; do not copy its header, stage behavior,
> receipt rigor, or artifact shape. Current conventions live in
> `experiments/00-market-read-lab/templates/`.

```yaml
pressure_lenses_fired: [query-time-grouping-enough, missing-company-radar, coverage-caveat, depth-backfill, denominator-reconciliation, tooling-ergonomics-latency]
```

> The seed pre-filled `[source-panel, missing-company-radar, coverage-caveat]` before the read
> ran. The read **inverted the source-panel call** — see Pressure lenses below. A mid-run operator
> observation ([`receipts/operator-observation-latency.md`](receipts/operator-observation-latency.md))
> also flagged **latency** (7+ min, re-inventing query mechanics) as a first-class Run 0 learning —
> folded in below.

## 30-second operator read

- **Did it work? Yes — cleanly, store-only, no scraping or spend.** The whole answer came from
  three layers already in the store (`telehealth.md` cuts + `offerings.md` `Visibility` column +
  `profile.md`). The pricing-visibility question is essentially **one roster pass** (QUERYING Recipe 4).
- **What was awkward?** Membership over-counts on keyword grep — one negation ("No GLP-1") and one
  primary-care brand slipped in. Filter by `anchor_category` + `value_chain_role`, not raw text.
- **What the next agent should know:** the **store was a *stronger* denominator than the external
  Notion seed** on this cohort. The expected lab learning ("we need a source panel") did not hold.
  The real move is union-and-dedupe across the two curated lists we already have.

## What happened

Read the lab framework + the seed receipt, then built the store-derived GLP-1 universe by
unioning three signals (telehealth `anchor_category`/categories-served, offerings molecule rows,
profile bodies) → 53 raw slugs. Cleaned 1 negation false positive (bluechew "No GLP-1") and
flagged 1 profiled-but-not-GLP-1 (One Medical). Classified the rest by `value_chain_role`:
**48 DTC sellers + 3 compounding-pharmacy suppliers + 1 white-label infra.** Pulled the
`Visibility` token + verbatim price for every GLP-1 SKU (229 buyable rows) → the 33/42/25
published/partial/on-request split that anchors the read. Resolved the 34 Notion names via
`store.py resolve` and diffed both directions. Wrote `read.md` + the
[store-derived-list receipt](receipts/store-derived-glp1-list.md).

## Inputs and scope

- Store slices: `store/*/telehealth.md` (46), `store/*/offerings.md` (47 with GLP-1 rows),
  `store/*/profile.md` (126 corpus, 52 GLP-1-signal).
- Scripts: `scripts/store.py resolve`; ad-hoc parsers (`/tmp/glp1_*.py`) over frontmatter +
  the `## Roster` tables.
- External denominator: the Notion Organizations GLP-1 seed (34 primary rows), treated as
  one non-exhaustive list, never ground truth.
- Exclusions: bluechew (negation), One Medical (no GLP-1), onepeloton/truniagen (regex noise),
  the 3 compounding pharmacies + OpenLoop (supply/infra, not DTC).

## Friction log

- **Latency is the headline Run 0 learning (operator-flagged, live).** The run was 7+ min in and
  still assembling, because the agent re-invented *all four* market-read steps inside the run:
  denominator build, value-chain filter, visibility extraction, name→slug reconcile. The answer was
  accurate but **too slow for an unattended routine.** Crucially this is **not** an argument for a
  storage primitive — it's an argument for **query ergonomics**: a small committed helper over the
  existing parsers, not new State. (Resolves the apparent tension with the read's "no new primitive
  needed": no new *State* object, yes a *query* helper.)
- **Keyword membership is a footgun.** A raw `GLP-1` grep caught a *negation* and a primary-care
  brand. The clean denominator recipe is `telehealth.anchor_category == GLP-1` ∪ roster-molecule
  rows, gated by `value_chain_role == DTC brand`. Worth writing down as the standard recipe.
- **No helper for "build a cohort denominator."** Each layer was a one-off parse. Repeatable, but
  every market read will re-derive it — that's most of the 7 minutes. A thin `cohort_members(anchor=…)`
  helper over the existing parsers would remove the friction (no new storage).
- **Name→slug across a project KB needed manual nudging.** `store.py resolve` nailed most, but
  "Dr Hank", "Maximus Tribe", "Noom Med", "One Medical (Amazon)", "Mens" needed suffix/fuzzy
  handling. The resolver's `suggest()` covered the gap; a project-KB reconcile would want it wired.

## Evidence limits

- Both denominators are curated and **partial**; overlap ~50%. The union (~56 known) is a floor.
- Price *magnitude* is verbatim-string only — the floors in the read are hand-read, not sortable.
- The 33/42/25 split is **per-SKU**; brand-weighted it flattens toward even thirds. Grain stated.
- "Gated" conflates two things: a brand hiding *its own* price vs. a branded-drug row it doesn't
  price ("retail" / insurance-set). The read calls this out; a token alone doesn't separate them.
- `unclear`/empty cohort cuts are "looked, couldn't tell," not "no."

## Surprises

- **The store out-completed the external source.** Run 0 was set up expecting the store to be the
  *small* list needing an external panel to check completeness. It's the opposite — the store holds
  ~24 GLP-1 sellers the Notion primary seed omits, as many as the seed contains. The completeness
  risk was *under*-counting from a single curated list, either one.
- **Almost nobody is a true black box.** "Hide behind intake" is real but rare — most gate-led
  brands still flash a membership fee or a "starting at." The interesting axis is *floor vs. real
  number*, not *shown vs. hidden*.
- **Visibility is predictable from the model.** `access_model` + `compounding_posture` nearly
  determine the token — compounded-flat publishes, dose-laddered shows a floor, clinic gates.

## Pressure lenses

"No new primitive needed" is the honest headline for the **pricing-visibility capability** — it
was answerable at query time from a field the store already captures. Lenses that fired:

- **`query-time-grouping-enough` → NO new primitive.** Strongest signal. Visibility, molecule
  grouping, and cohort scoping are all query-time reads over existing layers. Don't build a
  pricing-visibility store object.
- **`missing-company-radar`.** The store↔Notion diff is itself the radar — and it fires in *both*
  directions (8 Notion names unprofiled; ~24 store sellers absent from Notion).
- **`coverage-caveat`.** "Not exhaustive / not-captured ≠ not-offered" recurred everywhere; the
  standard language is load-bearing for every market read.
- **`depth-backfill`.** altRx (GLP-1-led, no `telehealth.md`/`offerings.md`) and Marque (no
  `telehealth.md`) are in-cohort but unqueryable on the cuts. Module backfill, not a new primitive.
- **`tooling-ergonomics-latency` (operator-flagged).** The read was correct but slow because the
  market-read assembly logic isn't reusable. Maps to the table's existing
  *"Same awkward run steps recur → helper script, template, or tighter convention."* This is the
  one lens that points at *building* something — but a **query helper, not a State primitive**.
- **`denominator-reconciliation` (NEW — not in the table).** See below.

### The pressure-lens table is missing one

The table's relevant row is **"Same external sources define membership → source panel capture."**
Run 0 contradicts its premise: the **internal store was the better denominator**, and the cheap,
correct move was a **query-time union + dedupe across two curated lists (store ∪ project-KB),
resolved by `store.py`** — *not* capturing a new external source panel. The table has no lens for
"two internal/curated lists disagree; reconcile them." Proposed addition:

| Repeated pressure | Possible triage candidate |
|---|---|
| Same two curated lists (store ∪ project KB) disagree on membership | Query-time denominator reconcile (resolver join), report union as a floor — **no captured source panel** |

This also sharpens the existing "source panel" row: reach for a captured external panel only when
*both* internal lists are thin, not by default.

## Triage submissions

These are queue submissions only; none are graduated or approved for implementation by this run.

- **[P2 · Submitted] Depth-backfill in-cohort module gaps.** Run `/deepen-offerings` +
  `telehealth.md` for `altrx-com` (GLP-1-led, no module layer) and `telehealth.md` for
  `marquelongevitylab-com`. Small, concrete, makes them queryable on the cohort cuts.
- **[P3 · Submitted] Add the `denominator-reconciliation` lens** to the pressure table and reframe
  the "source panel" row (above). One sighting so far — watch for recurrence before acting.
- **[P2 · Submitted] Cut market-read latency with a query helper** (operator-flagged as the
  headline Run 0 cost). A thin committed helper over the *existing* parsers — `cohort_members(anchor=…)`
  returning the unioned, role-filtered slug list + each SKU's `Visibility`/price, plus a
  `reconcile(name_list)` wrapping `store.py resolve` — collapses the four re-derived steps into two
  calls. **Explicitly a query-ergonomics helper, not a State primitive** (anti-Doro line intact:
  one-off tool, no living infra). Pairs with documenting the recipe in QUERYING (membership =
  `anchor_category` ∪ roster-molecule, gated by `value_chain_role`; *not* a raw body grep — the
  bluechew negation + One Medical cases show why).
- **[Low · Submitted] Branded-drug visibility is ambiguous** ("hides own price" vs "doesn't set
  this price"). If branded-tier tracking becomes a question, that's a Signal/freshness job, not a
  State field.
- **[No-op] No pricing-visibility storage primitive.** Confirmed query-time-answerable.

## Next-run advice

- Build cohort denominators as **store ∪ project-KB, deduped via `store.py resolve`**; treat each
  source as a floor and report the symmetric difference (it's the missing-company radar).
- Scope membership by `value_chain_role` + `anchor_category`, **not** raw keyword — avoids
  supply-side, negation, and adjacent false positives.
- The `offerings.md` `Visibility` column is the workhorse for any "publish vs gate" question across
  *any* cohort — reuse it directly, don't re-derive.
- If completeness becomes truly load-bearing (not just a check), *that's* when an external SERP/
  listicle panel earns its cost — not before.
