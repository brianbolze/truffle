# Developer Review

Question: **What Truffle system behavior does this run pressure?**

Reviewed via a 3-pass adversarial Loop 2 (evidence verifier + consumer + developer, Sonnet).

**Evidence verifier: PASS-WITH-FIXES.** Independently reproduced the candidate-field grep (16 non-Hone
brands; TRT 8 / longevity-NAD 7 ex-Hone / labs 1 — correct) and spot-checked 6 tier placements
(functionhealth, vitalityrx, mylifeforce, defymedical, truniagen, Hone anchor) against the actual store
files — all matched. Two precision catches, **both fixed in `read.md` during Loop 2**: (1) functionhealth
"does not prescribe protocols" sharpened to "no Rx hormone/optimization prescriptions; testing +
clinician result-review only" (it *does* deliver a reviewed protocol, just no Rx); (2) Hone's "$65 40+
biomarker" now flags the 40+/50+ A/B copy inconsistency the store's own `profile.md` notes. No external
sources, no snippets, floor/absence language correct.

## Capability pressure

| Capability | What did the run expose? | Smallest useful response |
|---|---|---|
| **Structure** | A **competitive/substitute relation** is *relation-as-Judgment*, not the joinable *relation-as-fact* of MRL-005/006 (parent/owns/pharmacy_partner/clinical_provider). "Substitute" is **buyer-relative** — the same Tier-2 TRT brand is substitute-for-male-T and adjacent-for-both-sex-longevity — so it cannot be a single durable edge. | Name the surface as a Judgment; do **not** add a `competitors:`/`similar_to:` field or edge table. New candidate MRL-011, hold for recurrence. |
| **Query / access** | The State-read recipe (anchor-job read → `anchor_category` grep → job-criterion classification) generalizes from *attribute* reads to a **relation/neighborhood** operation. Enumeration is one grep; tiering is read-time judgment. | Reinforce MRL-002; recipe-level only, no helper. |
| **Synthesis** | Sharing a *mechanic* (functionhealth has Hone's exact panel wedge) does not make a substitute — the job does. Tiering must read positioning prose, not enums. | Caveat language already correct; fold "enum necessary-not-sufficient" into any future QUERYING competitive-read recipe. |
| **Guardrails** | `denominator` floor held (anchored-only); buyer-relativity surfaced rather than hidden; store-only honored. | No-op — guardrails worked. |

## Lenses

**Steward** — Honest. Every tier call labeled Judgment and tied to a C-cited State source; State /
Judgment boundary clean; freshness and the two limits (floor, supply-side-only) visible. The verifier's
two precision fixes are now in `read.md`.

**Dev Agent** — No toil to remove yet. The neighbor enumeration is already one grep; the tiering is
irreducibly a judgment (that's the finding, not a missing helper). Resist building a competitor field —
it would dangle on buyer-relativity exactly as MRL-006 backend fields dangle on missing profiles.

**Founder** — Compounds the warm/cited asset (read + receipt) while staying light; anti-Doro-compliant
(no graph, no embeddings, no edge table, no standing infra). The new candidate is correctly *passive*.

## Recommendation

- **No-op / keep as observation:** Guardrail behavior (worked as intended).
- **Watch for recurrence:** A 2nd single-anchor competitive read (different anchor or buyer-job) →
  decide whether to serve a documented query-time substitute recipe in QUERYING.
- **Submit triage candidate:** Yes — **new MRL-011** (competitive-relation-as-Judgment), plus Evidence
  Log reinforcements on MRL-001 and MRL-002.

## Triage submissions

1. **New — MRL-011** (P3, Submitted): competitive/substitute relation surface as a Judgment; hold for
   recurrence; explicitly do **not** build a `competitors:`/`similar_to:` field or edge table.
2. **MRL-002** — Evidence Log: recipe generalizes from attribute reads to a relation/neighborhood
   operation (run 017). Recipe-level, no helper.
3. **MRL-001** — Evidence Log: competitive-set flavor of the anchored-only floor (run 017). Reinforces;
   does not move.

**Do not graduate, spike, or implement system changes.**
