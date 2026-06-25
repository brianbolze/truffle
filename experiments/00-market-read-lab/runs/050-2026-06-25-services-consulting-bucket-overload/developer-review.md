# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients, capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation (ID · kind) |
|---|---|---|---|
| **Capture** | The telehealth-wrapper convention (`Services / Consulting` primary + `Biotech / Pharma` secondary used as a *cohort tag*, not a literal category match) is undocumented in SCHEMA.md/TAXONOMIES.md — it lives only as a corpus pattern. A new capturer wouldn't know to replicate it, so the pair-discriminates rule could silently rot as mis-tagged entries accumulate. | read.md Market Pattern; no TAXONOMIES.md entry cites the convention. | DR3 · gap |
| **Structure** | State/Judgment boundary held cleanly — the read stayed in State (token + entity_type values) and confined Judgment to a named-condition verdict; no Judgment baked into the store. | read.md "reading failure, not a capture failure"; Gap Map "no new field." | DR1 · surprise |
| **Query / access** | The discriminating cut exists in State but only in the *full array*, not `offering_category[0]`. Any tool/recipe keying on the primary element silently over-merges 52 telehealth wrappers + the 9-residual. Whether an *existing* QUERYING.md recipe or render script already does this was not audited — that audit decides whether the fix is urgent or deferrable. | read.md Market Pattern; VR1 correction; W1. | DR2 · risk-miss |
| **Freshness / automation** | N/A — no freshness pressure this run. | — | — |
| **Synthesis** | Denominator instability (61 primary / 68 naïve-parse / 82 anywhere / 73 exact-token-frequency) is a repeatedly-fractured parsing surface: inline `# STRAIN` comments on a frontmatter array element break naïve grep/tooling. Same footgun family as L004's `parse-the-value-not-the-comment`, but on the *array-parse* side, not denominator reconciliation. | receipt C1; VR1 V1 (naïve parse → 68); run-notes G2. | DR4 · friction |
| **Guardrails** | Source rigor held — store-only, no spend, no mutation, absence said as "not found." The run also self-corrected a precision overreach via the adversarial evidence pass (VR1), the same verifier-catches-a-slip value as runs 042/045/047/048/049. | run-notes exit check; VR1. | (covered by VR1 row) |

## Lenses

**Steward** — System stayed honest: provenance cited, State/Judgment separated, uncertainty visible, and the overreach was caught and scoped rather than shipped. The one latent honesty risk is DR3: an undocumented capture convention that a structured query can't see.

**Dev Agent** — The repeatable toil is the array-parse footgun (DR4): any helper reading `offering_category` as structured data must strip inline comments first. Prefer a grep-verifiable note over a new helper. The lightest real fix for the headline finding is a one-line QUERYING/TAXONOMIES reading convention — not a sub-category, field, or config knob.

**Founder** — "No new primitive needed" is the right disposition and compounds the warm/cited asset without ontology gravity. The L005 connection is a genuine 2nd-sighting *with a new grain*: query-time grouping is enough, **but the grouping key must be the full array, not the first element** — a positional variable prior L005 sightings (015/027/028/031/032/035) never named. The L006 link is looser than the run first claimed (DR3 below): L006 is a token-*meaning* grain mismatch on two-sided entities; this is one token carrying two *unrelated conventions* — share the surface ("a clean field over-claims unless its scope is read with it") but differ in mechanism. A learning pass should keep them distinct.

## Recommendation

- **No-op / keep as observation:** Yes — record all rows; no build, no lesson proposed in-run.
- **Watch for recurrence:** `query-time-grouping-enough` (now with the array-position grain — candidate to sharpen L005), `schema-edge-entity-type`, `denominator-reconciliation` / `source-rigor` (the array-parse footgun, cousin to L004), `tooling-ergonomics`.
- **Severe `risk-miss` to surface now:** None severe. DR2 (an existing recipe may already over-merge on `offering_category[0]`) is the one worth a cheap future audit — but it is a deferred check, not a live data corruption.

## Raw learning to preserve

Appended to `learning/observations.md`: DR1 (L005 2nd-sighting with a *new array-position grain* — key on the full array, not element[0]), DR2 (the over-merge is a reading hazard on `offering_category[0]`; urgency hinges on an un-run audit of existing recipes), DR3 (the telehealth-wrapper pair convention is undocumented in the schema — a maintenance-rot risk; and the L006 link is looser than first claimed — distinct mechanism). The array-parse footgun (DR4) is logged via run-notes G2.

**Did not propose, graduate, spike, or implement system changes.**
