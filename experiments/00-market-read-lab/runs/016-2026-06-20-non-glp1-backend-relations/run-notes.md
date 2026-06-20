# Run Notes

```yaml
run_status:            reviewed
evidence_mode:         store-only
autonomous_eligible:   yes
termination_reason:    completed
pressure_lenses_fired: [relation-pressure, coverage-caveat, denominator-reconciliation]
```

> **Loop 2 outcome (2026-06-20):** Reviewed via a 3-pass adversarial workflow (evidence
> verifier + consumer + developer, Sonnet). **Verifier:** independently reproduced every
> load-bearing co-occurrence count (Strive ×2; Curexa/Tailor Made/Olympia ×2; Beluga
> singleton; no shared clinical network outside GLP-1; cohort = 35) clean, with **one real
> catch** — `belmarpharmasolutions-com` was overclaimed as a joinable supplier profile but has
> `captures/` only, **no `profile.md`**; among *cited* compounders only **Strive** truly joins
> today. Also flagged the receipt's denominator *method wording* (full-line `grep -v GLP-1`
> yields 33 not 35; value-parse yields the correct 35). **Both fixed in `read.md` + receipt**
> (now a 3-tier join-readiness distinction: joinable / captured-no-profile / no-store-entry).
> store-only discipline **PASS**. **Consumer verdict: valuable** — answers (not re-confirms) a
> decisive comparative question; the GLP-1↔non-GLP-1 axis-flip is a one-sentence structural
> insight; discipline clean (floors, no "concentration", no possessive-as-named). **Developer
> verdict: submit-triage-candidate** — State/Judgment boundary held (J1–J3 labeled, tied to
> evidence); the MRL-005 recurrence bar is **met** (2 cohorts × 2 axes, 2 joinable edges);
> minimal shape now needs both `clinical_provider:` + `pharmacy_partner:`. **Triage:** appended
> additive Evidence Logs to **MRL-005** (recurrence fires outside GLP-1 on the pharmacy axis),
> **MRL-006** (pharmacy-side grain split + join-fails-both-directions + "joinable = profile.md
> exists" contract sharpening), and **MRL-001** (non-GLP-1 floor + grep-method note). No new
> item; no graduation.

## 30-second operator read

- **Worked.** Store-only relation read on the **35 non-GLP-1** structured brands — the
  explicit MRL-005/006 re-test outside compounded GLP-1, the test runs 014 *and* 015 both
  named as the highest-value next step. Zero spend.
- **Headline (decisive):** backend sharing is **NOT a GLP-1 artifact** — but the joinable
  axis **flips**. Outside GLP-1 the shared backend is the **compounding pharmacy**, not a
  clinical network. **Strive Pharmacy** (`strivepharmacy-com`) is named by 2 brands and
  **resolves to a store profile** — the mirror of run 014's OpenLoop (clinical, joinable,
  GLP-1). Three more pharmacies recur ×2 but dangle (Curexa, Tailor Made, Olympia).
- **Next agent should know:** this *moves* MRL-005 — second cohort, second axis, a second
  store-joinable cross-brand backend edge. The minimal graduation shape now needs **both** a
  `clinical_provider:` and a `pharmacy_partner:` axis, not clinical-only. Still no helper, no
  edge table; most suppliers still dangle (MRL-006 capture-grain, pharmacy side).

## What happened

Scout selected the non-GLP-1 backend-relation read (C1) to decide whether the OpenLoop
clinical-concentration finding generalizes outside compounded GLP-1. Loop 1: `anchor_category`
grep → 35 non-GLP-1 brands; pulled `parent`/`owns` (`profile.md`) + `pharmacy_model`/
`value_chain_role` (`telehealth.md`) frontmatter; read Fulfillment + Clinical-entity body
prose for *named* third parties (skipping possessive "our pharmacy" per the run-001 guard);
counted store-wide recurrence per entity; resolved each against `store/`. Wrote `read.md`
(State/Judgment separated) + one derivation receipt. No external sources, no spend, no
write-back, no durable object/field created.

## Inputs and scope

- `grep anchor_category store/*/telehealth.md` minus GLP-1 → **35** brands (C1; anchor-only,
  under-counts offerers per MRL-001).
- `parent`/`owns` frontmatter (`profile.md`); `pharmacy_model`/`value_chain_role`
  (`telehealth.md`) (C2).
- Fulfillment + Clinical-entity body prose for named pharmacy/clinical entities (C3–C9).
- Entity resolution: `ls store/*<name>*` for Strive, Curexa, Tailor Made, Olympia, Empower,
  Belmar, Precision, Beluga, Hallandale, OpenLoop (C10–C11).
- Exclusions: no external denominator; Signals layer untouched; GLP-1 cohort (covered by run
  014); generalists that sell into these cohorts without anchoring (named as MRL-001 caveat).

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

- **Named-vs-possessive is a per-body prose read**, not a field lookup — exactly MRL-006's
  capture-grain gap, now firing from the *pharmacy* side across a second cohort. The
  `pharmacy_model` frontmatter comments (richly annotated this capture) carried most of the
  named entities, which sped the read materially — a positive contrast to run 014's manual
  body scan.
- **Entity resolution is a manual `ls store/*<name>*` per entity.** Tolerable at ~12 entities;
  a recurrence would want a documented step (the run-014 friction, repeated). Name variants
  (Olympia "Pharmaceuticals" vs "Pharmacy") make the resolution fuzzy.

## Evidence limits

- **Anchored-only denominator (MRL-001, now a non-GLP-1 cross-cohort sighting).** The 35 is
  the anchored non-GLP-1 set; recurrence counts are **floors**.
- **Absence of a named pharmacy ≠ absence of a relationship.** Many brands route to an
  unnamed "partner pharmacy"; the substrate is larger than the named floor.
- **2-brand co-occurrence is a lead, not concentration** — "concentration" language withheld
  by contract; the aggregate (4 pharmacies × 2 brands) is a substrate pattern, not a measured
  market structure.
- **Olympia name-variant** ("Pharmaceuticals" vs "Pharmacy") inferred as one entity, not
  adjudicated (C6).
- Owned-page self-report only; no external/state-board verification (store-only by contract).

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
- No disallowed action happened: **pass** (no live browse, no spend, no `store/` mutation, no edge/field/object created, no possessive-as-named, no "concentration" from 2-brand co-occurrence)
- Required citations / receipts present and source-graded: **pass** (C1–C11 → receipt S1, `source_grade: derived`)
- No snippet treated as evidence: **pass** (no external snippets; all store frontmatter + body prose)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no current/news claims; store State only, store clock 06-04→06-18)
- Absence language says "not found", not "not true": **pass** (no shared clinical network "not found"; unnamed pharmacies framed as floors)

## Surprises

- **The axis flips between cohorts.** Run 014 (GLP-1): clinical edge joins (OpenLoop ×2),
  pharmacy dangles. This run (non-GLP-1): **pharmacy edge joins (Strive ×2), clinical is
  singleton/in-house.** Not anticipated — the question hypothesized a clinical recurrence
  test; the answer arrived on the pharmacy axis.
- **invigormedical fronts 5 named pharmacies at once** — a single storefront over a pool of
  fulfillment partners, the clearest illustration that DTC brands are skins over a smaller
  compounder substrate.
- **The join fails from both directions:** named-but-uncaptured (Curexa, Tailor Made) *and*
  captured-but-unnamed (`hallandalerx-com`, a 503A compounder no brand cites).

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
| `relation-pressure` | Backend-relation recurrence *outside* GLP-1: pharmacy axis recurs+joins (Strive ×2), the mirror of run 014's clinical OpenLoop. Second cohort, second axis, second store-joinable cross-brand edge. | append Evidence Log to **MRL-005** — recurrence test fires on the pharmacy axis; refines minimal shape to need both `clinical_provider:` + `pharmacy_partner:`. Graduation human-gated. |
| `coverage-caveat` | Most named compounders dangle (Curexa, Tailor Made, Olympia, Empower, Precision, Valiant, Casa Pharma — no profiles); reverse dangle `hallandalerx` captured but uncited. | append to **MRL-006** — capture-grain gap now seen pharmacy-side, with a join-fails-both-directions finding. |
| `denominator-reconciliation` | Anchor-only grep under-counts offerers; counts are floors (now a non-GLP-1 cross-cohort sighting). | append to **MRL-001** Evidence Log (reinforces; does not move). |

New tag needed? No. Existing tags covered it.

## Triage submissions

Loop 2 should append dated **Evidence Log** entries (not rewrite canonical state) to:

1. **MRL-005** (named-counterparty relation edge) — the recurrence test runs 014/015 asked
   for fires on a **second cohort and the opposite axis**: outside GLP-1 the shared, store-
   joinable backend is the **pharmacy** (Strive Pharmacy → `strivepharmacy-com`, named by
   hevahealth + invigormedical), while the only named third-party clinical group (Beluga) is
   a singleton. Combined with run 014 (OpenLoop, clinical, GLP-1), the lab now has **two
   joinable cross-brand backend edges across two cohorts and two axes** — evidence the
   minimal shape must cover **both** a `clinical_provider:` and a `pharmacy_partner:`
   dotted-domain mirror, populated only when the entity resolves. Still a *lead*, not
   concentration (each pharmacy ×2 brands). Graduation human-gated.
2. **MRL-006** (named-counterparty capture-grain gap) — reconfirmed pharmacy-side: named
   compounders mostly dangle (Curexa, Tailor Made, Olympia, Empower, Precision, Valiant, Casa
   Pharma have no profiles); Strive + Belmar resolve. New finding: the join **fails from both
   directions** — `hallandalerx-com` is a captured 503A compounder no brand cites. Order of
   operations if MRL-005/006 graduate: capture the supplier profile first, then add the
   dotted-domain field.
3. **MRL-001** (denominator reconciliation) — non-GLP-1 cross-cohort recurrence of the
   anchored-only under-count; recurrence counts are floors.

**Do not implement, spike, or recommend immediate graduation from inside the run.**

## Next-run advice

- A **third** non-GLP-1 brand naming Strive (or any compounder clearing 3 brands) would push
  the pharmacy substrate from "recurrence lead" toward a defensible concentration claim —
  worth a watch on future TRT/longevity/peptide captures.
- A **bounded-live** follow-up could resolve the dangling compounders (Curexa, Tailor Made,
  Olympia) and the Olympia name-variant via state-board/SERP lookup, converting most of the
  substrate from un-joinable to joinable — a deliberate, scoped capture run, not a bolt-on.
- Avoid re-running the relation read on a *third* compounded cohort expecting new *design*
  signal — MRL-005's recurrence question is now answered on both axes; the open move is the
  human graduation decision, not another sighting.
