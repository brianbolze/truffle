# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Discovery disposition |
|---|---|---|---|
| **Capture** | New source family validated; coverage ~0. The ads/paid-acquisition surface is cheap (1 credit/domain), reliable (6/6 clean, 0 schema_drift), domain-keyed — but captured for 1/130 store-wide, 0 GLP-1. | G1; receipt; `ls store/*/signals/ads_transparency` | ready-for-triage (MRL-029 coverage evidence) — but resourcing, not design. |
| **Structure** | State/Signal/Judgment boundary held cleanly on a push signal — ads presence logged as a Signal (resourcing), read explicitly refuses the "who's winning" Judgment. | boundary_audit; read.md Market Pattern #3 | no-op — boundary worked. |
| **Query / access** | No recipe for "enumerate ads-presence across a panel"; brand→domain + parse hand-rolled. | F1 | recur-watch (MRL-002, ads grain). |
| **Freshness / automation** | No time-delta: ads captures single-point; `signal_delta.py` has no ads branch (mirrors sec_edgar/MRL-012). Tenure = first/last bookend only. | W1; read.md Source Gaps | recur-watch. |
| **Synthesis** | The four-trap inventory + push≠demand line is the clearest execution of the traction frame's push-vs-demand split the lab has produced — pedagogically reusable. | read.md Gap Map; O2 | strength; preserve. |
| **Guardrails** | Bounded-live discipline tight: 1 family / 6 captures / 6 credits, exactly at ceiling, every source logged, stop rule honored (panel stopped at 6, rest flagged not-sampled). | bounded_live_audit; run-notes exit check | strength. |

## Lenses

**Steward** — System stayed honest. Verifier re-derived every load-bearing count from the
raw JSON with **zero discrepancies** (incl. the 209d/309d quiet gaps and the 1/130
denominator, clarified as profiles-with-`profile.md`). Absence language consistently "not
visible on this surface," never "not advertising." No unlabeled Judgment found; the one
watch-point (Market Pattern #1 "well-resourced acquisition motion") is a defensible
Signal-level characterization (tenure + multi-format), not a "who's winning" Judgment.

**Dev Agent** — One real recurring-toil sighting (brand→domain + parse, F1), but a single
sighting → recur-watch, no helper. The cheapest latent fix is **ad-landing-domain
resolution** (a brand may target `try<brand>.com`, not its store `domain:` key), which could
flip a false zero — but it's one sighting and only affects the zero cases.

**Founder** — The run compounds the warm asset cheaply (6 reusable captures, tool validated)
without ontology gravity: **no new primitive needed to consume** the signal — the gap is
coverage + a delta branch, both spend/approval-gated. Consistent with run-029's "machinery
ahead of coverage."

## Recommendation

- **No-op / keep as observation:** the structure/boundary result (it worked); the market fact.
- **Watch for recurrence:** MRL-002 ads-grain recipe (F1); `signal_delta.py` ads branch (W1);
  ad-landing-domain resolution. All single-sighting.
- **Submit triage evidence (mature):** MRL-008 external-source branch — see below.

## Optional triage evidence

- **MRL-008 — new external-source branch flavor (one-sighting-confirmed, not yet recipe):**
  "**structured-zero ≠ market-absence on a live external source**" (run-034 S1) is a genuine
  extension of the run-028/033 empty-structured-surface branch from *store* surfaces to a
  *live external tool* — empirically new, not a restatement. The other three ads confounds
  (push≠demand, first-page≠volume, advertiser-legal-name≠brand) are **source-specific
  elaborations** of the existing source-rigor principle, worth a sub-note under the same
  branch, not separate items. Disposition: promote the external-source branch to
  "one-sighting confirmed"; a 2nd ads read on a different cohort would close it to a recipe.
  Pointer: `discovery-ledger.md` run-034 S1/O2/O3/O5; read.md Gap Map.
- **MRL-029 / traction-coverage:** stay **recur-watch, do not graduate.** Confirms ads is a
  real push-side traction ingredient the store lacks (coverage, not architecture), but
  widening it is a spend/approval resourcing decision MRL cannot close autonomously. Evidence
  for a coverage initiative, not a backlog item. Pointer: `discovery-ledger.md` run-034 G1/W1.
