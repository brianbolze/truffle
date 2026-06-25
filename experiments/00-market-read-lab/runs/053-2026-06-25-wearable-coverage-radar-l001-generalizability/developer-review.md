# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation |
|---|---|---|---|
| **Capture** | Strength: store anchoring via `ls store/` token-match grounds the diff; no "capture more" reflex. The missing-set is a candidate list, not a mandate. | read.md Companies Seen; receipt C1 S4 | S2 · surprise |
| **Structure** | Two `denominator-reconciliation` flavors: G1 (external sub-axis listicle disjointness) + **G2, a genuinely new flavor — contamination on the *store* side of the diff** (store's "wearable/recovery" grouping over-includes Peloton/Therabody/Hyperice/Nike vs the editorial "tracker" category). Prior instances (036/037/039/042/045/046/050) were all external-draw contamination. | read.md Result(2); receipt C1 | G1, G2 · gap |
| **Query / access** | The graduated L001 recipe (QUERYING Recipe 9) holds mechanically on a non-telehealth vertical but its "one category → one overlapping listicle population" assumption is telehealth-shaped; needs a sub-axis + cohort-boundary scope step. | read.md Verdict; lessons.md L001 | S1 · surprise; DR2 · gap |
| **Freshness / automation** | Wareable was a 3-week-old Firecrawl cache hit (mod 2026-06-02); correctly dated, no misrepresentation. Capture-set quality variance (Eight Sleep mid-sale snapshot, run-046 G2) is silently inherited by the binary diff. | run-notes live_evidence_used; consumer CR2 | CR2 · risk-miss |
| **Synthesis** | The `Market Pattern` bimodal framing was initially stated as a finding; it is a 2-list-panel Judgment (now relabeled in read.md per DR1). State-vs-Judgment boundary otherwise clean (missing-set, category boundary, single-source tail all labeled). | read.md Market Pattern (corrected); C2 | DR1 · gap |
| **Guardrails** | **Clean bounded-live spend.** 2 families / 3 sources / 3 net credits, all under the 8-credit, 5-source, 2-family ceiling. Stop rule fired after the 2nd list. Plan's `fail_closed_when` named the *class* "variable-cost formats" (run-047 DR1 hardening) and held. PCMag failure → same-family substitution, in-bounds, logged. | run-notes exit check + live_evidence_plan | R2 · surprise; DR3 · surprise |

## Lenses

**Steward** — The system stayed honest: provenance/grades carried, absence language correct,
the one over-confident section (bimodal market) relabeled as Judgment after review. The
captured-set quality-variance inheritance (CR2) is the one un-surfaced honesty edge — the
binary diff treats a mid-sale snapshot the same as an evergreen capture.

**Dev Agent** — The reusable signal is **family-level (not URL-level) source plans degrade
gracefully — but only when the substitute shares the planned source's *cost class*** (DR3,
sharpening R2). The PCMag→Wareable swap was safe because both are plain-markdown (~1 credit);
the run-040/047 breaches were "same family, different cost class" (PDF/JSON). Cost-class, not
just source-family, is the real substitution-safety constraint — and the plan schema names
neither cost-class nor enforces it.

**Founder** — The run compounds the warm/cheap asset (a reusable named-set + diff receipt)
and stays light: "no new primitive needed," membership stays a query-time recipe. No ontology
gravity. The only escalation gap is that the L001 generalization caveat (G1/G2) lives in
run-side narrative with no path to the lessons layer unless a learning pass reads it (DR2).

## Recommendation

- **No-op / keep as observation:** the run itself — clean gap-probe, no build, L001 holds
  with a documented caveat.
- **Watch for recurrence (`learning_tags`):** (1) **`denominator-reconciliation` — the new
  store-side flavor (G2)**; if a 2nd diff-based read shows the store cohort scoped too broadly
  for an external category, it earns its own cluster note distinct from the n=5+ industry-draw
  instances. (2) **`bounded-live-spend`** — DR3's cost-class-not-just-family substitution
  constraint, alongside the run-040/047/052 spend-class thread. (3) **L001 scope-note candidacy
  (DR2)** — a learning pass should decide whether G1/G2 amend Recipe 9 or stay run-side.
- **Severe `risk-miss` to surface now:** none. CR2 (captured-set quality-variance) and DR1
  (bimodal Judgment label) are calibration notes, not shipped errors; DR1 already corrected.

## Raw learning to preserve

New developer-side sightings appended to `learning/observations.md`: **DR1** (bimodal market
= unlabeled Judgment over-extrapolated from a 2-list panel; corrected), **DR2** (G1/G2 are
L001/Recipe-9 scope-note candidates with no escalation path out of run narrative), **DR3**
(source-substitution safety = source-family *and* cost-class jointly; plan schema names
neither). Plus evidence-verifier rows **VR1** (C2 Withings-overlap overreach, corrected) and
**VR2** (missing-set tiering — Garmin/Samsung weaker than Fitbit/Withings/Amazfit, corrected).

**Did not propose lessons, graduate, spike, or implement system changes.**
