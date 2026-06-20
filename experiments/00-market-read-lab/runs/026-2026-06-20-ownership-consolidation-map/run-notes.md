# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [relation-pressure, coverage-caveat, denominator-reconciliation, query-time-grouping-enough]
```

## 30-second operator read

- **Did the run work?** Yes. First ownership/consolidation read in the lab. Store renders
  a `parent`/`owns` map but can't traverse it: of ~21 referenced targets, only 2 are
  captured, and **lifemd↔rexmd is the only fully-reconciled, both-sides-captured edge**.
- **What was awkward?** Nothing tool-wise — pure frontmatter grep. The friction is
  conceptual: absence (`parent: []`) is bare 103/109 times, so independent-vs-undisclosed
  isn't decidable per-field.
- **What should the next agent know?** This is MRL-006's "join fails because target isn't
  captured" generalized to the cleanest relation axis. No new primitive needed; the gap is
  **counterpart capture coverage**. Pairs with MRL-005/006 (relations) and MRL-009
  (capture worklist).

## What happened

Probed store frontmatter for all non-empty `parent:`/`owns:` edges (13 + 15), tested
which referenced targets resolve to captured profiles (2 of ~21), checked bidirectional
reconciliation, and quantified the `parent: []` absence-discipline distribution. Wrote
`read.md` + one derived receipt. Store-only, no spend.

## Discovery ledger

Greedy raw learning for this run. Preserve singletons here before triage compresses
anything, then Loop 2 appends the useful rows to `discovery-ledger.md`. Do not merge
rows, dedup into backlog items, or translate wishes into build proposals inside the run.

Use short IDs such as `O1`, `W1`, `F1`, `S1`, or `G1` so reviews can cite them.

| ID | Kind | Raw observation / wish / friction / surprise / gap | Evidence or pointer | Why it matters | Discovery clock |
|---|---|---|---|---|---|
| O1 | observation | Ownership disclosure is sparse but clean: 13 brands disclose non-empty `parent:`, 15 non-empty `owns:`, with explicit provenance `#` comments on most. | read.md C1; receipt edge tables | A `parent`/`owns` consolidation *map* exists; it's a thin disclosed-only slice. | notice-only |
| O2 | surprise | The cleanest relation in the schema (structured `parent`/`owns` frontmatter, often explicit attestation) **dangles 18-of-21 times** — only lifemd.com, qualtrics.com, rexmd.com of ~21 referenced targets are captured (and rexmd/lifemd are the two ends of the single reconciled pair). | read.md C2; receipt joinability test | Generalizes MRL-006 ("join fails because target uncaptured") from prose-pharmacy edges to the clean ownership axis. | ready-for-triage |
| O3 | observation | Exactly **one** fully-captured, bidirectionally-reconciled ownership edge exists store-wide: `lifemd ↔ rexmd`. `delighted → qualtrics` is captured but **unreciprocated** (qualtrics `owns` omits delighted). | read.md C3, C4; receipt | Reconciliation is testable only when both ends are captured, and even then can be one-directional — a join-integrity caveat for any ownership traversal. | ready-for-triage |
| O4 | observation | The richest `owns:` facts ride in on general public companies (Amazon/Etsy/Nike/Uber/Twilio/Ford/Casio), but their siblings were never captured → cleanest data is the most orphaned. | read.md Market Pattern #2; receipt owns list | Corpus selection bias determines which ownership facts are even present; they're confident but un-traversable. | notice-only |
| G1 | gap | Store **cannot traverse** parent→portfolio or claim a consolidation rate. The 4 multi-child clusters (amazon, thirtymadison, niagenbioscience, richemont) all have **uncaptured** parents; richemont pair is inferred. | read.md C5; receipt concentration block | The structural gap-probe answer: query-time map yes, traversal/claim no — binding limit is coverage + denominator, not representation. | ready-for-triage |
| G2 | gap | Absence is not self-describing: 103/109 `parent: []` are **bare** (no comment); only 6 distinguish "independent" (IDEO/Rugiet) from "not stated" (Swatch/Notion/alliahealth). | read.md C6, C8; receipt absence block | A naive consolidation read treating every empty as "independent" would badly overstate the independent share. The convention *can* mark this but rarely does. | ready-for-triage |
| W1 | wish | If anything graduates, the right shape is **capturing the parent/sibling entities** (Thirty Madison, Niagen Bioscience, LifeMD siblings) — not a `competitors`/edge table. Capture turns dangling pointers into joinable portfolios. | read.md What Would Change; Missing/Stale Coverage | Names the only fix that makes the clean axis actually join, consistent with MRL-006 order-of-ops (capture target first, then the edge already exists). | recur-watch |
| S1 | surprise | `query-time-grouping-enough` splits in two on this axis: TRUE for a string-grouped map (group children by parent value), FALSE for traversal and FALSE for a consolidation claim. | read.md builder-lens verdict | Sharpens the recurring `query-time-grouping-enough` tag — "groupable" ≠ "joinable" ≠ "claimable." | recur-watch |
| F1 | friction | Assembling the map needed a join across two greps (`parent:` child→up and `owns:` parent→down) plus a per-target existence test; no single canonical "ownership view." | run-notes friction log | Mirrors MRL-002's multi-surface friction; one sighting, recur-watch only. | recur-watch |

## Inputs and scope

- **Store slice:** all 135 `store/*/profile.md` dirs; 126 carry `parent:`/`owns:` fields.
- **Queries:** `grep "^parent: \[[^]]"` / `grep "^owns: \[[^]]"` (non-empty edges);
  per-target `store/<slug>/` existence test; `parent: []` total/with-comment/bare counts.
- **Exclusions:** none — whole-corpus read (intentionally spans telehealth + general brands).
- **Receipt:** `receipts/ownership-edge-map-2026-06-20.md`.

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

Building the "ownership view" required joining two greps (child→`parent` and
parent→`owns`) plus a per-target existence test — there is no single canonical ownership
surface (F1). Low-severity; one sighting.

## Evidence limits

- Map is **disclosed-only** → a floor, not a census of true ownership.
- Corpus is **selection-biased** (telehealth-heavy + ad-hoc general brands) → concentration
  counts are not a market-structure measurement.
- Richemont parent edges (×2) are **inferred (STRAIN)**, not primary attestations.
- 103/109 `parent: []` are bare → cannot decide independent vs undisclosed per-field.

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
- No disallowed action happened: **pass** (no live browsing, no store mutation, no primitive, no triage graduation)
- Required citations / receipts present and source-graded: **pass** (receipt graded `derived`, C1–C8)
- No snippet treated as evidence: **pass** (no snippets used)
- Current/news/pricing/policy claims carry capture dates and source grade: **n/a** (no current/external claims)
- Absence language says "not found", not "not true": **pass** ("undisclosed-or-uncaptured", explicit floor framing)

## Surprises

The schema's *cleanest* relation axis (structured `parent`/`owns`, often with explicit
ownership attestation) still fails to join 19-of-21 times because counterpart entities
aren't captured (O2) — the same failure mode MRL-006 found on messy prose-pharmacy edges.
And `query-time-grouping-enough` bifurcates: groupable ≠ joinable ≠ claimable (S1).

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
| `relation-pressure` | First ownership/consolidation relation read; `parent`/`owns` is the clean joinable axis but dangles 19/21. | watch for recurrence — pairs with MRL-005/006 (counterpart-capture-coverage is the cross-relation bottleneck). |
| `coverage-caveat` | Only 2/21 referenced targets captured; 4 multi-child clusters all have uncaptured parents. | watch — feeds MRL-009 capture-worklist shape. |
| `denominator-reconciliation` | Map is disclosed-only over a selection-biased corpus; no consolidation rate is claimable. | watch — same MRL-001 selection-bias flavor (invisible to store-only queries). |
| `query-time-grouping-enough` | Grouping children by parent value works; traversal + consolidation claim do not. | watch — sharpens the tag (groupable ≠ joinable ≠ claimable). |

## Optional triage evidence

Loop 2 should decide placement, but the mature evidence here is the **cross-relation
generalization**: O2/O3/G1 show the clean `parent`/`owns` axis fails to join for the same
reason MRL-006 named on prose-pharmacy edges — counterpart entities aren't captured. This
is an Evidence Log entry for **MRL-006** (capture-grain / join-target-existence) and/or
**MRL-005** (relation edge), not a new item: it reinforces "capture the target first, the
clean edge already exists" on a third relation flavor (corporate ownership). G2 (bare-empty
absence discipline) is a candidate note for MRL-008 (source-rigor: absence not
self-describing). No new primitive; no field/edge-table wanted (consistent with MRL-005/006/011).

**Do not implement, spike, or recommend immediate graduation from inside the run.**

## Next-run advice

- A second relation read that lands on a backend-naming-dense *and* counterpart-captured
  cohort would test whether traversal ever works in practice (vs always dangling).
- If a human approves an MRL-009 capture pass, capturing Thirty Madison + Niagen Bioscience
  + LifeMD siblings would create the first traversable portfolios and let an intra-corpus
  consolidation rate be computed — then re-run this read to compare.
- Avoid treating `parent: []` as "independent" — 95% are bare/undisclosed.
