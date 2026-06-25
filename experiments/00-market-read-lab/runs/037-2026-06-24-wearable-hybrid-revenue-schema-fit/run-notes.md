# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
learning_tags: [schema-edge-entity-type, query-time-grouping-enough, depth-backfill, denominator-reconciliation, source-rigor]
```

## 30-second operator read

- Did the run work? Yes — clean store-only calibration. The schema-edge question resolved
  sharply: `business_model` is single-valued and lossy on hybrid hardware+subscription
  revenue, and the loss is masked at this cohort by consistent captor judgment until
  Apple flips the tag on an identical structure.
- What was awkward? Nothing operationally. The denominator was settled by one exhaustive
  grep; no friction.
- What should the next agent know? The headline finding is a reproducibility risk-miss
  (R1: Oura `Subscription` vs Apple `Transactional`, same two-leg structure) and a
  cohort-draw inversion of run-036 G3 (here `business_model` *splits* the coherent cohort
  rather than recovering it). Also a second-entity-type boundary on L006 (S2): the
  price-visibility token does NOT mislead here — sharpening, not graduating, L006.

## What happened

Read the SCHEMA/TAXONOMIES `business_model` + `offering_category` contract, then pulled
frontmatter + body pricing/model lines for the 8-company panel (4 connected hybrids + 4
foils). Confirmed the cohort denominator with one exhaustive grep of all 19 Hardware
profiles × `business_model`. Synthesized the two-leg structure table, the Oura-vs-Apple
tag flip, and the reader-filter risk-miss. No live evidence, no spend, no store mutation.

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
| S1 | surprise | The single-valued `business_model` enum ("the primary model if several apply", TAXONOMIES:76) is structurally lossy on co-primary hardware+subscription revenue: all 4 connected hybrids run two revenue legs (device + recurring) but the field can name only one. The split is recoverable only from prose / inline `STRAIN:` comments — and even the comment channel is inconsistent (Oura/Whoop/Eight Sleep carry a STRAIN marker; Peloton carries none, only body prose). | That the field is broken or a new field is needed — single-valued is a deliberate contract choice; this maps the cost, not a defect to fix at n=4. | read.md Result(1) table; TAXONOMIES.md:76; ouraring profile:48, whoop:40/42, eightsleep:44, onepeloton:43/64 | schema-edge-entity-type, query-time-grouping-enough |
| G1 | gap | No structured field encodes the **composite** revenue shape (which leg is required vs optional, who bundles whom). `offering_category` is a partial, inconsistent proxy — it carries the 2nd-offering *type* for Oura/Whoop/Peloton but Eight Sleep's mandatory Autopilot sub is absent from it entirely (demoted to "companion"). | That a composite-revenue field should be built — n=4, single cohort, prose carries it fine for a human reader; "no new primitive needed" stays live. | read.md Gap Map; eightsleep profile:42/44 (sub absent from offering_category) | depth-backfill, query-time-grouping-enough |
| R1 | risk-miss | The primary-leg tag is **not reproducible** across structurally identical companies: Oura (device one-time + recurring app) → `Subscription`; Apple (device one-time + recurring services) → `Transactional / One-time`. A reader filtering `business_model: Subscription` for recurring-revenue businesses misses Apple; filtering `Transactional` for device-sellers misses all 4 wearables. The field answers neither "has a device" nor "has recurring revenue" for hybrids. | That either capture is wrong — both are defensible primary-leg reads; the risk is a reader trusting the single field to filter hybrids in/out. n=1 flip (Oura vs Apple), not yet a proven defect. | read.md Result(2),(3); ouraring profile:48, apple profile:40/65 | schema-edge-entity-type, source-rigor |
| G2 | gap | Cohort-draw **inversion** of run-036 G3: there `business_model` was the cohort-recovering key (marketplaces); here it *splits* a structurally coherent cohort (Subscription vs Transactional within connected hardware), and only looks like a key (`Hardware` ∧ `Subscription` recovers the 4 pure-plays, C1) because the four members were tagged homogeneously — a coverage artifact, not a robust key. `primary_industry` scatters across 3 values for similar brands. | That `business_model` is a bad key in general — it's a per-cohort property; the note is that entity-shape cohorts need a query-time judgment, not a single industry/model draw. | read.md Companies Seen; C1 grep (19 Hardware profiles); run-036 G3 | denominator-reconciliation, schema-edge-entity-type |
| S2 | surprise | Second entity-type test for L006 (after marketplaces): the SCHEMA price-visibility token does **not** mislead on hardware hybrids — it reads correctly per-offering (device `[published]`, membership `[partial]`/`[published]`) because these entities are not two-sided/intermediary and the buyer can obtain every price. Evidence that L006's trap is specific to two-sided/intermediary shapes, not non-DTC broadly. | That this graduates or alters L006 — decision boundary; this is an out-of-band observation that *sharpens L006's scope*, nothing more. | read.md What Would Change; lessons.md L006; whoop profile:65-67, oura profile:71-73 | schema-edge-entity-type, source-rigor |
| W1 | wish | If anything ever graduates from S1/G1, the lightest path is making `business_model` a **ranked multi-select** (like `offering_category`) so a hybrid carries `[Subscription, Transactional]` — NOT a new per-company composite-revenue field. Load-bearing reason: it reuses an existing multi-select pattern and resolves both reader-filters in R1 with zero new field family. | That it should graduate now — only the lightest path *if* a 2nd homogeneous hybrid cohort + a real consumer who needs to *filter* (not just read) by composite model appear. Mirrors run-036 W1 anti-sprawl landing. | read.md What Would Change; TAXONOMIES.md:110 (offering_category multi-select precedent) | query-time-grouping-enough |

## Inputs and scope

- **Panel (8):** core hybrids — ouraring-com, whoop-com, eightsleep-com, onepeloton-com;
  foils — therabody-com, hyperice-com, nike-com, apple-com.
- **Denominator grep:** all `store/*/profile.md` with `offering_category ⊇ Physical
  Products / Hardware` (19 profiles) × `business_model`. The four `Subscription` are
  exactly the four connected hybrids (C1).
- **Contract files:** `TAXONOMIES.md:74-87` (`business_model` closed set, single-valued)
  and `:110` (`offering_category` ranked multi-select).
- **Exclusions:** watches (7), Ford, Warby Parker, Electra Aero, beta-team — Hardware but
  not connected-health/recovery. Apple kept as the mixed foil deliberately (it is the
  tag-flip case).
- **Source panel:** store-only. No live evidence, no spend.

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

None. One grep settled the denominator; profiles carried the structure in frontmatter +
body. No missing helper, no path confusion.

## Evidence limits

- Prices are promo-period snapshots (every profile flags an active sale) — used only as
  structure illustration, not live magnitudes.
- The reproducibility risk-miss (R1) rests on a single tag-flip (Oura vs Apple); it is a
  surfaced risk, not a proven defect across many captures.
- n=4 core cohort, single entity shape. The "no structured composite field" gap is mapped,
  not generalized beyond connected hardware.
- A *magnitude* read of hybrid economics (ASP vs LTV, attach, churn) would need filings/IR,
  out of scope and not attempted.

## Loop 1 exit check

Record `pass` / `fail` for the mandatory exit check before setting final `run_status`.

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a** (store-only)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no live browse, no spend, no store mutation, no schema-change proposal)
- Required citations / receipts present and source-graded: **pass** (all store paths + line numbers; contract cites)
- No snippet treated as evidence: **pass** (store-only)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (prices labeled point-in-time snapshots, structure-only; no live magnitude asserted)
- Absence language says "not found", not "not true": **pass** (C1 framed as "within the captured store", per L004)

## Surprises

The Scout hypothesis ("`business_model` is a pure splitter for this cohort") was half
wrong in an interesting way: `Hardware ∧ Subscription` recovers the four pure-plays
*precisely* (C1), so it looks like a clean key — but that is a homogeneity artifact, and
it breaks at Apple, whose identical hybrid structure is tagged `Transactional`. So the
field both recovers and splits depending on captor judgment of the dominant leg (S1, R1,
G2). Also: L006's price-visibility trap does **not** reproduce on this second entity type
(S2), which is a useful scoping signal for the parked lesson.

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

Fired: `schema-edge-entity-type` (the core lens — a 3rd non-DTC shape after investor/035
and marketplace/036), `query-time-grouping-enough` (prose + query reads the blend; no
field needed), `depth-backfill` (no composite-revenue field), `denominator-reconciliation`
(cohort draw is a query-time judgment, no single key), `source-rigor` (the reproducibility
risk-miss + price-snapshot discipline). No new tag needed.

"No new primitive needed" is the honest outcome here.

## Next-run advice

- The schema-edge-entity-type thread now has three shapes (investor subtractive gate /
  035, marketplace two-sided economics / 036, hardware hybrid revenue / 037). A learning
  pass might cluster these into one "the single-valued `business_model` enum loses
  *composite* revenue structures" lesson — but that's the pass's call, not a run's.
- If re-running this shape, the sharpest test of R1 would be a *new* capture of a
  structurally identical wearable to see whether the primary-leg tag is applied
  consistently — that would harden or dissolve the reproducibility risk-miss.
- Avoid re-running as a pure price-comparability read (C3 candidate) — it would overlap
  this without new schema pressure.
