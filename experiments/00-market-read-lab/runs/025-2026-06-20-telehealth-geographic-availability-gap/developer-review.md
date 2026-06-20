# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Discovery disposition |
|---|---|---|---|
| **Capture** | Decision-grade availability needs each brand's eligibility/checkout state-gate or `/provider-credentials` page at *list* grain; the store holds only prose mentions. | wisp `/provider-credentials` and vitalityrx's 25-state list exist on-site but are captured as prose only. | Observation; live per-brand sweep is human-gated. |
| **Structure** | Availability is **not** one of the 8 telehealth cuts and **should not** become a brand-level field — it is a product×state (sometimes audience×state) property. | C1; intra-brand splits joiandblokes/vitalityrx/henrymeds/marek/hevahealth (C2–C5a). | **Submit MRL-014** with an explicit anti-graduation note. |
| **Query / access** | Availability prose lives in ≥2 files (`telehealth.md` body + `profile.md` Overview/`site_notes`/`unverified_fields`) — two grep passes needed (F1). | run-notes F1; mirrors MRL-002's price-in-3-surfaces friction. | Recur-watch only; **not** mature for a QUERYING note from one sighting. |
| **Freshness / automation** | Any captured state list is intrinsically point-in-time — struthealth dated "as of Sept 2024"; controlled-substance availability tracks shifting state law. | C6; S1. | Reinforces "don't persist as durable State"; watch. |
| **Synthesis** | The most protective finding (no brand-level field) sits third in Market Pattern; the skim layer under-serves a fast reader. | consumer lens check. | Single-sighting value-miss in `discovery-ledger.md`; no template change. |
| **Guardrails** | State/Signals/Judgment boundary held cleanly; "50 states" recorded then flagged, never tallied as coverage; absence = not-found. | dev verifier check (PASS); henrymeds self-flag (O4). | Strength to preserve. |

## Lenses

**Steward** — Honest. The read treats all availability language as captured brand *claims*,
never adjudicated truth; the 29 silent brands are not-found, not "available everywhere";
the three Market Patterns are labeled Judgments tied to State citations. The Loop-2
evidence verifier (PASS_WITH_FIXES) reproduced C1–C8 and C10 verbatim and caught **two
real misclassifications** — hevahealth (per-program 45/30/50 split) and niagenplus
(7-state at-home-kit exclusion) were lumped into the sub-component bucket when the store
actually records per-program exclusions. Both moved into the decision-grade group (7→9),
buckets re-resolved to exactly 54, and C9 corrected (8→6) in `read.md`. The fix *strengthens*
the core finding: hevahealth adds a clean audience×state sub-flavor.

**Dev Agent** — The only repeated toil is F1 (availability prose has no canonical home).
It mirrors MRL-002 but is a single sighting on this axis; not yet worth a QUERYING recipe.
No helper warranted.

**Founder** — A brand-level `available_states` field would be *negative* value: it would
force one answer onto a multi-answer entity and rot as state law shifts. The lightest true
substrate is the existing prose + (if ever) a per-offering-line verbatim, dated note.
No ontology gravity; the gap is capture-depth + intrinsic staleness, not a schema defect.

## Recommendation

- **No-op / keep as observation:** F1 friction (recur-watch); the skim-layer synthesis
  miss (single sighting → `discovery-ledger.md` only).
- **Watch for recurrence:** S1 (controlled-substance lines drive the hard state
  exclusions) and W1 (per-line dated availability is the only non-rotting grain) — a
  second-cohort sighting of the same product×state split would harden them.
- **Submit triage evidence:**
  1. **New item MRL-014** — *Geographic / state availability is a per-line, point-in-time
     property, not a brand field.* P3. Anti-graduation note: do **not** add an
     `available_states` brand field or a service-area object; hold for a second-cohort
     sighting before any per-line depth-backfill recipe. Well-evidenced: intra-brand
     splits verified verbatim (joiandblokes:26, vitalityrx:73, hevahealth:34).
  2. **MRL-008 Evidence Log addend** — the two-way "all 50 states" confound
     (claim-not-truth + sub-component-scope) is a new field-flavor of the confound family.
     Additive; does not move the graduation clock.

## Optional triage evidence

Submitted: MRL-014 (new) + MRL-008 Evidence Log entry (see `triage.md`). F1 held at
recur-watch (no MRL-002 entry from one sighting), per the Dev-Agent lens.

**Do not graduate, spike, or implement system changes.**
