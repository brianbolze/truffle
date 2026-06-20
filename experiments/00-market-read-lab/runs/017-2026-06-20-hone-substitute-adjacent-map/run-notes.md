# Run Notes

```yaml
run_status:            reviewed
evidence_mode:         store-only
autonomous_eligible:   yes
termination_reason:    completed
pressure_lenses_fired: [relation-pressure, query-time-grouping-enough, denominator-reconciliation, coverage-caveat]
```

> **Loop 2 outcome (2026-06-20):** Reviewed via a 3-pass adversarial workflow (evidence verifier +
> consumer + developer, Sonnet). **Verifier: PASS-WITH-FIXES** — reproduced the candidate-field grep
> (16 non-Hone brands; TRT 8 / longevity-NAD 7 ex-Hone / labs 1) and 6 tier placements clean; two
> precision catches **both fixed in `read.md`** (functionhealth "no Rx prescribing; testing+review
> only"; Hone 40+/50+ panel A/B caveat). No external/snippet evidence; floor language correct.
> **Consumer: valuable** — answers a decisive cold-start question with cited, auditable tiering;
> folded the verifier-adjacent "rank Tier-1 by closeness" suggestion into `read.md` (mylifeforce
> closest mirror). **Developer: submit-triage-candidate** — State/Judgment boundary clean; the
> competitive-relation-as-Judgment finding (buyer-relative, not enum-derivable) is genuinely new vs
> MRL-002 and distinct from MRL-005/006's joinable relation-as-fact. **Triage:** new **MRL-011**
> (P3/Submitted, hold-for-recurrence, no `competitors:` field) + Evidence Log reinforcements on
> **MRL-002** (recipe generalizes to relation/neighborhood ops) and **MRL-001** (competitive-set
> flavor of the anchored-only floor). No graduation; no `store/` mutation; no Human Notes touched.

## 30-second operator read

- **Worked.** First **competitive/substitute** relation read (all prior relation runs were backend
  supplier/clinical) and first **single-anchor** read (all priors cohort-wide). Anchor = Hone Health.
  Zero spend, store-only.
- **Headline:** Hone's 16 captured neighbors split into 3 tiers — **Tier 1** broad lab-led
  optimization substitutes (mylifeforce/gogeviti/gethealthspan/defymedical), **Tier 2** TRT-optimization
  brands that substitute only for the *male-T* buyer, **Tier 3** adjacent unbundled components
  (functionhealth diagnostics-only, vitalityrx enclomiphene-only, agelessrx longevity-Rx, NAD+
  supplement sellers).
- **Design nugget for next agent:** the neighbor set is **cheap to enumerate** (`anchor_category`
  grep) but the substitute-vs-adjacent **judgment is NOT enum-derivable** — `anchor_category` lumps
  vitalityrx (adjacent) with defymedical (substitute) and misses that functionhealth (`labs`) is
  adjacent despite sharing Hone's exact wedge. "Substitute" is also **buyer-relative** (Tier 2 flips).
  So: query-time-grouping-enough; a `competitors:`/`similar_to:` primitive is **not** warranted, and
  the read shows *why it would be hard* (relation-as-judgment, not relation-as-fact like MRL-005/006).

## What happened

Scout selected C1 (Hone substitute/adjacent map). Loop 1: read `honehealth-com/profile.md` for the
anchor job-to-be-done; `grep anchor_category` for the candidate field (16 brands: TRT 8, longevity/NAD
7, labs 1); pulled each candidate's `anchor_category`/`audience`/`modality`/`pay_model` + positioning
comments; applied a stated job criterion (cross-shop for the *same lab/physician-led optimization
job*) to tier substitute vs adjacent. Wrote `read.md` (State cited, Judgments labeled) + one
derivation receipt. No external sources, no spend, no write-back, no field/object created.

## Inputs and scope

- `store/honehealth-com/profile.md` (C0, anchor).
- `grep -lE "^anchor_category: (TRT|longevity/NAD|labs)" store/*/telehealth.md` → 16 candidates (C1).
- Per-candidate `telehealth.md` frontmatter + positioning comments (C2–C17).
- Exclusions: no external denominator; per-SKU `offerings.md` overlap not censused (line-level only);
  un-anchored generalists selling hormone/longevity lines excluded (MRL-001 floor).

## Live evidence plan

Required only for `bounded-live`; leave `null` for `store-only` and `local-existing`.

```yaml
live_evidence_plan: null
```

## Live evidence used

Required for every outside source used in `bounded-live`. Leave `[]` for local-only runs.

```yaml
live_evidence_used: []
```

## Friction log

- **Substitute/adjacent tiering is a per-brand prose read**, not a field lookup — the positioning
  comments in `telehealth.md` carried the discriminating signal (wedge, front door, both-sex vs
  men-only), which made the read fast, but there is **no single greppable field** that separates
  substitute from adjacent. This is the design point, not a tooling complaint.
- Anchor-job extraction needed the full `profile.md` Overview + Positioning prose; `anchor_category`
  alone (longevity/NAD) understates Hone's multi-line hormone breadth.

## Evidence limits

- **Anchored-only floor (MRL-001).** Candidate field is the *anchored* TRT/longevity/labs set;
  generalists selling hormone/longevity without anchoring are excluded. Neighbor set = floor, not
  Hone's full competitive universe.
- **Supply-side inference only.** "Would a buyer cross-shop" is inferred from positioning State, not
  demand-side evidence (no SERP/Exa/owned-vs panel; store-only by contract).
- **Buyer-relativity.** Tier 2 substitute/adjacent status depends on which Hone buyer (male-T vs
  both-sex-longevity); State can't pick the buyer.
- Line-level offering read, not a SKU census; fine for a job judgment, not a catalog-overlap proof.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a**
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no live browse, no spend, no `store/` mutation, no
  competitor field/object/edge created, no "overlap = substitution" without the job criterion, no
  "full competitive universe" claim — floor language used)
- Required citations / receipts present and source-graded: **pass** (C0–C17 → receipt S1–S3,
  `source_grade: derived`/State)
- No snippet treated as evidence: **pass** (no external snippets; all store State)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no current/news
  claims; store State only, clocks 2026-05-31→06-18)
- Absence language says "not found", not "not true": **pass** (un-anchored generalists framed as a
  floor / excluded, not "no other competitors exist")

## Surprises

- **The diagnostic wedge does not separate substitute from adjacent.** functionhealth shares Hone's
  *exact* wedge (lab panel as front door) yet is the cleanest **adjacency** — because it stops at
  testing and never prescribes. Sharing a mechanic ≠ serving the job.
- **"Substitute" is buyer-relative.** The same Tier-2 TRT brand is a substitute for the male-T buyer
  and adjacent for the both-sex/longevity buyer. A competitor relation can't be a single fact; it's a
  judgment indexed to a buyer/job.
- **Hone's moat is the bundle, not any component.** Each component (diagnostics, T, longevity-Rx,
  supplements) is attacked by a focused adjacent player; only Tier 1 reproduces the whole bundle.

## Pressure tags

| Fired tag | What fired in this run | Triage implication |
|---|---|---|
| `relation-pressure` | First **competitive/substitute** relation surface (vs backend MRL-005/006). A substitute set is a useful reader artifact, but it is **relation-as-judgment**, not the joinable relation-as-fact of parent/owns/backend. | submit candidate (new, P3) — name the competitive-relation surface as a *judgment*, distinct from MRL-005/006's backend-fact edges; hold for recurrence. Graduation human-gated. |
| `query-time-grouping-enough` | Neighbor set enumerated in one `anchor_category` grep; tiering done at read-time with a job criterion. No durable competitor object needed. | reinforce MRL-002 — extends the State-read recipe family to a **relation/neighborhood** operation (not just attribute extraction); recipe-level only. |
| `denominator-reconciliation` | Anchored-only grep under-counts offerers; neighbor set is a floor. | reinforce MRL-001 (does not move) — now a *competitive-set* flavor of the anchored-only caveat. |
| `coverage-caveat` | Substitute judgment lacks demand-side corroboration store-only; supply-side positioning inference only. | watch — a bounded-live Exa/"alternatives-to" panel would corroborate; pairs with MRL-001's "external panel as fallback" note. |

New tag needed? No. Existing tags fit; the *new content* is the competitive-relation-as-judgment
distinction, captured under `relation-pressure`.

## Triage submissions

For Loop 2 to weigh (append Evidence Logs / propose, do not implement):

1. **New candidate — competitive/substitute relation surface as a Judgment (suggest P3, Submitted).**
   First lab read on the competitive axis. Finding: a substitute set is enumerable from
   `anchor_category` but the substitute-vs-adjacent line is a **positioning judgment that frontmatter
   enums underdetermine**, and "substitute" is **buyer-relative**. This is distinct from MRL-005/006
   (backend relation-as-*fact*, joinable). Proposed framing: hold as a passive condition; if a 2nd
   single-anchor competitive read recurs, decide whether the engine should *serve* a query-time
   substitute recipe (not store a competitor edge). Explicitly do **not** build a `competitors:` field
   or edge table — the relation is a judgment, not a fact. Link: MRL-002, MRL-005.
2. **MRL-002 (reinforce):** extends the State-read recipe family from attribute extraction to a
   **relation/neighborhood** operation (anchor-job read → cohort grep → job-criterion tiering).
   Recipe-level; no helper.
3. **MRL-001 (reinforce, does not move):** competitive-set flavor of the anchored-only under-count;
   neighbor set is a floor.

**Do not implement, spike, or recommend immediate graduation from inside the run.**

## Next-run advice

- The obvious follow-up is a **bounded-live** version of this anchor read: an Exa-neighbor /
  "alternatives to Hone" SERP / owned-"vs"-page panel to corroborate the substitute set demand-side
  and surface generalists the anchored-only grep missed (MRL-001 floor). That would also be the
  natural 2nd sighting to test the new competitive-relation candidate.
- Avoid re-running this as another *store-only* single-anchor read on a different brand expecting new
  *design* signal — the "enumerate cheap, judge hard, buyer-relative" finding would likely just
  repeat. The open move is the demand-side (bounded-live) test, or the human call on the new candidate.
- A women-first or menopause-first anchor would re-rank the same cohort — useful only to demonstrate
  buyer-relativity concretely, not for new design pressure.
