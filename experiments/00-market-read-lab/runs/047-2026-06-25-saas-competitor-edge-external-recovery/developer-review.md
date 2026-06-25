# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation (ID · kind) |
|---|---|---|---|
| **Capture** | Rival *nodes* uncaptured (0/5); the edge is near-free to source but the endpoints aren't there. | `ls store/`; C1/C2 vs C3 | G1 · gap; S1 · surprise |
| **Structure** | Relation support is axis-asymmetric: vertical (`parent`/`owns`) structured, horizontal (`competes-with`) absent — confirmed on a 2nd anchor / 2nd sub-market, removing run-039's "maybe telehealth" residual. | profile.md frontmatter vs :74 | G1 · gap |
| **Query / access** | "Who competes with Datadog?" is not a structured query; the neighborhood is the run's Judgment, not store State (map-not-ingredient, run-039 CR1). | read.md Result(1)/(3) | G1 · gap; CR1 · surprise |
| **Freshness / automation** | Prose rivals read as current; no M&A-freshness flag (Splunk→Cisco, New Relic private). | C3; profile.md:74 | CR2 · wish |
| **Synthesis** | State/Signals/Judgment kept separate and labeled; one slip (snippet-grade corroboration stated as decision-grade) caught + corrected by the Loop-2 verifier. | read.md Result(2) pre/post VR1 | VR1 · risk-miss |
| **Guardrails** | Bounded-live spend ceiling **breached by one credit gross** (net 6 after refund); the no-PDF hardening patched one instance of a wider class. | C2 (creditsUsed 5); run-040 R1 | R1 · risk-miss; DR1 · risk-miss |

## Lenses

**Steward** — Honest. Provenance, grades, capture clocks, and the spend breach are all
visible; the one over-confident sentence (corroboration grade) was caught and corrected
in-run. The "edges are cheap" Judgment is hedged ("for well-known anchors"), though the hedge
sits three paragraphs below the lead rather than in it.

**Dev Agent** — The repeated toil is the bounded-live spend guardrail. R1 names two instances
(PDF, JSON); the *class* is "any Firecrawl format that delegates post-fetch processing (PDF
page-split, LLM/JSON extraction) and so carries a variable, pre-call-invisible per-unit cost."
The `live_evidence_plan` `fail_closed_when` block excludes PDF explicitly but not the class, so
the next plan-writer hardens against "PDF and JSON," not against the family — and the third
variable-cost format will breach again. A class-level rule ("disallow post-fetch
variable-cost formats under a light ceiling") is the grep-verifiable contract that removes the
toil. (DR1.)

**Founder** — The run compounds the warm/cheap asset and stays light: it correctly declines a
`competes-with` field (endpoints dangle → fails engine-dev's fillable-cut bar) and lands the
no-build call S1 sharpens (re-deriving the edge is cheap AND the nodes are missing — doubly
unmotivated). No ontology gravity added.

## Recommendation

- **No-op / keep as observation:** the relation-structure gap (G1) and the W1 no-field
  disposition — both correct, both held as observations, no build.
- **Watch for recurrence:** `bounded-live-spend` (now 2 runs: 040 PDF, 047 JSON),
  `relation-pressure` (039 + 047), the builder-not-buyer value frontier (`coverage-caveat` /
  CR1, now 038/039/041/047 with 043/044 as the buyer-break counterexamples).
- **Severe `risk-miss` to surface now:** none severe. DR1 (the class-framing of the spend
  guardrail) is the most actionable — it's a one-line plan-contract fix a future Scout can
  apply, but it is an out-of-band learning-pass call, not a run-side change.

## Raw learning to preserve

Appended to `learning/observations.md` as VR1 (verifier slip + correction) and DR1 (spend
guardrail class-framing), alongside the run rows G1/S1/R1/S2/W1 and consumer rows CR1–CR3.

**No lessons proposed, nothing graduated, no spike or system change implemented.**
