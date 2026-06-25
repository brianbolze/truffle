# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation (ID · kind) |
|---|---|---|---|
| **Capture** | No gap surfaced — the captures already hold the flags (`unverified_fields`, `site_notes`, self-reported prose). | All 6 profiles carry their flags; the brief renders them. | S1 · surprise |
| **Structure** | **Strength + a boundary.** The State/Signals/Judgment separation is intact (the brief files limits under "Provenance"), but the *structured* trust surface has no high-salience render path; the only default-path protection is unstructured captor prose. | `unverified_fields`/`site_notes` → tab 4; caveat-in-Overview is captor-written, not a field. | G1 · gap; VR1 · risk-miss |
| **Query / access** | n/a — local read, no query-recipe pressure. | — | — |
| **Freshness / automation** | n/a — not a freshness read. | — | — |
| **Synthesis** | **The pressure point.** The presentation layer (`brief.py`) is a *synthesis/relay* surface, and its salience ordering — hero `description` at peak, structured flags in tabs 2/4, proof collapsed — is where the recurring relay-risk actually bites. The docstring claims the trust surface is "rendered visibly as the product," which overstates its salience. | `brief.py:1-7` docstring vs `:190-222,259-263,381`. | G2 · gap; S2 · surprise; W1 · wish |
| **Guardrails** | **Strength.** The run's own guardrails held: the evidence-verifier pass caught and corrected an overstatement (VR1) before it shipped — the 3-lens Loop 2 working as designed (4th consecutive VR-catch after 042/045/048). | read.md Result(2) pre/post; VR1. | VR1 · risk-miss |

## Lenses

**Steward — is the system still honest?** Yes, with a caveat. State/Signals/Judgment separation
holds and every flag is present in the artifact. The honesty risk is *salience*, not content: a
reader who trusts the default 5-second view over-trusts unless the captor happened to write a
caveat into an auto-open section. The `brief.py` docstring ("trust surface rendered visibly as the
product") is itself a small honesty overstatement — the limits surface is tab-gated, not visible by
default. Filed as G2.

**Dev Agent — can repeated toil be removed with a convention or tiny helper?** If anything ever
graduates (it shouldn't yet), the grep-verifiable shape is an ordering change in one file
(`brief.py`): surface one flag at hero grain, or auto-open the limits section — no new field, no
schema edit, the data already renders. That's W1, held. Resist building a "flag salience" config
knob; the fix, if real, is one layout decision, not a primitive.

**Founder — does this compound the warm/cited/cheap asset while staying light?** The run is light
(local, zero spend, regenerable briefs) and the finding compounds: it gives the present-layer owner
a located, cited target without minting ontology. The anti-pattern to avoid is treating "salience"
as a capture or schema problem — it is purely a presentation Judgment, owned downstream of State.

## Recommendation

- **No-op / keep as observation:** yes. Append S1/G1/S2/G2/W1/VR1/CR1/DR1 to the stream; propose
  nothing. The lightest path (W1) is a present-layer Judgment, graduation is Brian's call.
- **Watch for recurrence:** `source-rigor` + `tooling-ergonomics` (the relay preserves-but-buries
  the structured flags) — pair with the 038/042/048 R-rows next learning pass; this run is the
  *presentation-surface* instance of that thread, the first to test the literal relay.
- **Severe `risk-miss` to surface now:** none. VR1 is a contained, corrected in-run slip, not a
  shipped defect; the structural finding (structured flags off the 5-second path) is a salience
  observation against a Judgment surface, not a live data-integrity failure.

## Raw learning to preserve

DR row added to `run-notes.md` Observations (DR1). No lesson proposed; no system change; no edit to
any live skill/recipe/schema/template.
