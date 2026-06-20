# Run Notes

```yaml
run_status:            reviewed
evidence_mode:         store-only
autonomous_eligible:   yes
termination_reason:    completed
pressure_lenses_fired: [relation-pressure, coverage-caveat, denominator-reconciliation]
```

## 30-second operator read

- **Worked.** Clean `store-only` relation read on the 19-brand anchored GLP-1 cohort — the explicit MRL-005/006 re-test.
- **Headline:** naming a backend counterparty is the exception (5/19); the one cross-brand, store-joinable counterparty is **OpenLoop Health** (clinical network behind MEDVi + joinfridays). Pharmacy partners are named-but-dangling (no profiles).
- **Next agent should know:** this *partially fires* the MRL-005 recurrence test — first concrete joinable cross-brand edge, but it's *clinical*, not pharmacy, and it's one recurrence (two brands), not "concentration." Argues for the minimal capture shape, not an edge table.

## What happened

Scout selected the relation/counterparty read on the compounding-heavy GLP-1 cohort (the cohort MRL-005 parked
for). Loop 1: grep `anchor_category: GLP-1` → 19 brands; pulled `pharmacy_model`/`value_chain_role`/`parent`/`owns`
frontmatter; scanned each `telehealth.md` Fulfillment + Clinical-entity body for *named* counterparties (vs the
possessive "our pharmacy" language run 001 warned about); resolved every named entity against `store/`. Wrote
`read.md` State/Signals/Judgment-separated. No external sources, no spend, no write-back.

## Inputs and scope

- `grep -rl "anchor_category: GLP-1" store/*/telehealth.md` → 19 brands (C1; anchor-only, under-counts per MRL-001).
- Per-brand `pharmacy_model`, `value_chain_role`, `parent:`, `owns:` frontmatter (C2).
- Per-brand `telehealth.md` Fulfillment + Clinical-entity prose for named pharmacy / clinical-group entities (C3/C4/C5).
- Profile-resolution: `ls store/*<entity>*` for OpenLoop, CraftedRx, Triad Rx, RedRock, Beaker, Eden Pharmacy, CareGLP, Hallandale.
- Exclusions: no external denominator; Signals layer untouched; multi/none generalists that sell GLP-1 without anchoring (LifeMD/Nurx/Wisp) are out of the anchored census by construction and named as a caveat.

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

- The "named vs unnamed" distinction is a per-body prose read, not a field lookup — there is no frontmatter that says
  "names a counterparty." This is exactly MRL-006's capture-grain gap surfacing again: the joinable relation primitives
  (`parent`/`owns`) live in `profile.md` frontmatter, while pharmacy/clinical partners live in `telehealth.md` prose, so
  "who does brand X depend on" needs both structured *and* unstructured reading. Repeated the run-001 manual loop.
- Resolving each named entity to a store profile is a manual `ls store/*<name>*` per entity. Tolerable at this scale; a
  recurrence would want a documented step, not a helper.

## Evidence limits

- **Absence of a name ≠ absence of a relationship.** 14/19 route to an unnamed pharmacy; a brand could use OpenLoop or a
  shared pharmacy without naming it on owned pages. The OpenLoop concentration is a **floor**, not a ceiling.
- **Anchor-only denominator** (MRL-001): multi/none GLP-1 offerers fall out of the census; this is the *anchored* cohort.
- **Two-brand recurrence is thin.** "Concentration" language is deliberately avoided in the read — one recurring entity
  across two brands is a lead, not a market-structure claim.
- joinfridays' captured pages link but do not capture its full partner-pharmacy list (`/terms-conditions/#pharma`).

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a**
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no live browsing, no spend, no store mutation, no edge/object created)
- Required citations / receipts present and source-graded: **pass** (C1-C5 in `read.md`, all store-local, store clock)
- No snippet treated as evidence: **pass** (no external snippets used)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no current/news claims; store State only)
- Absence language says "not found", not "not true": **pass** (unnamed = "not stated, not no-relationship"; floor framing)

## Surprises

- The concentration signal showed up on the **clinical** edge, not the pharmacy edge MRL-005 originally hypothesized.
  OpenLoop (a B2B clinician-staffing platform already in the store) silently powers ≥2 cohort brands' medical groups.
- The single counterparty that *both* recurs and joins to a store profile is the clinical one; every *pharmacy* name in
  the cohort is either dangling (no profile) or owned-sibling — so the pharmacy-supplier-concentration read MRL-005 framed
  is currently un-answerable for lack of join targets, while a different (clinical) edge answered instead.

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
| `relation-pressure` | Relation-surface recurrence on the compounding-heavy GLP-1 cohort. Confirmed 001's "named is the minority" (5/19) AND produced the first concrete cross-brand, store-joinable counterparty (OpenLoop, clinical, 2 brands). | submit Evidence Log to **MRL-005** + **MRL-006** — recurrence partially fires; graduation stays human-gated |
| `coverage-caveat` | Named pharmacy partners (CraftedRx/Triad/RedRock/Beaker/Eden Pharmacy) have **no store profiles**, so pharmacy edges dangle; joinfridays partner list uncaptured. | watch — backend counterparties are a corpus-health gap if the edge ever graduates |
| `denominator-reconciliation` | Anchor-only grep under-counts GLP-1 offerers (MRL-001, 4th cohort sighting). | append to **MRL-001** Evidence Log |

## Triage submissions

Loop 2 should append dated **Evidence Log** entries (not rewrite canonical state) to:

1. **MRL-005** (named-counterparty relation edge) — relation-surface recurrence on compounding-heavy GLP-1 *partially fires*:
   named-is-minority confirmed on a 2nd cohort (5/19), but the first store-joinable cross-brand counterparty appears —
   **OpenLoop Health behind MEDVi + joinfridays**. Crucially the recurrence is on the **clinical-provider** edge, not the
   pharmacy edge MRL-005 framed. Evidence for a *minimal* joinable shape (dotted-domain frontmatter mirror like
   `clinical_provider:` for brands that name a resolvable counterparty), **not** an edge table. Two brands = a lead, not
   concentration. Graduation human-gated.
2. **MRL-006** (named-counterparty capture-grain gap) — reconfirmed concretely: `parent`/`owns` are clean `profile.md`
   frontmatter (eden→edenpharmacy.com); pharmacy/clinical partners are `telehealth.md` prose; the read needed both. Adds
   the join-target finding: the only counterparty that resolves to a store profile is OpenLoop; pharmacy names dangle.
3. **MRL-001** (denominator reconciliation) — 4th cohort to hit the anchor-only-vs-all-offerers under-count.

Do not implement, spike, or graduate from inside the run.

## Next-run advice

- A **third** brand naming OpenLoop (or any pharmacy recurring across ≥2 brands) would push MRL-005 from "one recurrence"
  toward an actual concentration claim — worth a watch on future GLP-1 captures.
- Run the same relation read on a **non-GLP-1 / FDA-brand** cohort to test whether shared clinical networks (OpenLoop,
  SteadyMD, Wheel) recur outside compounded GLP-1 — that decides whether clinical-backend concentration is a GLP-1
  artifact or telehealth-wide.
- If MRL-005/006 ever graduate, the minimal shape is a dotted-domain frontmatter mirror of `parent`/`owns`, populated
  only when a page names a counterparty that resolves to a profile — not a new edge table or relation-type registry.
