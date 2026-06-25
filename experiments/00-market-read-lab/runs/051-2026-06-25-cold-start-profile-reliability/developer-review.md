# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients, capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation (ID · kind) |
|---|---|---|---|
| **Capture** | **Strength** — the capture contract enforces a uniform 9-section skeleton + a uniform trust surface (`unverified_fields`/`site_notes`/`STRAIN`) regardless of entity weirdness (asset manager → nuclear dev → luxury watch). This is *why* cold-start is structure-shaped. | read.md Result; header-skeleton grep across 6 | S1 · surprise |
| **Structure** | **Weak spot (known):** single-valued `business_model` is the one lead field that fails cold-start for non-standard monetizers (blueowl `Other`, eightsleep `Subscription`, blueenergy `Usage-based`); prose rescues. Reuses run-037 S1 / run-044 G2 on the cold-start lens. | blueowl:35, eightsleep:44, blueenergy:39; How-it-works prose | S2 · surprise |
| **Query / access** | A cold reader / delegated agent keying on `business_model` frontmatter alone is mis-served; the reliable monetization surface is prose, not a field. Not a new gap — a re-confirmation that the field is a fast-read trap on hybrid/non-standard shapes. | read.md What Would Change; S2 | S2 · surprise |
| **Freshness / automation** | Vintage spread (05-30→06-24, schema 2.2→2.6) showed the cold-start *core* is version-robust; only peripheral identity modules (`socials`/`legal_entity`/`logos`/`modules`) are absent on 2.2 captures. Benign, flagged not hidden. | blueowl/alange (2.2) vs others; verifier G1 confirm | G1 · gap |
| **Synthesis** | **Strength** — the `Strategic read` section delivers genuine per-entity "so what" synthesis for all 6, clearly the run's own Judgment layer riding on labeled State. Boundary stayed clean. | the 6 Strategic read sections | S1 · surprise |
| **Guardrails** | The adversarial evidence-verifier caught a real precision overreach ("identical" skeleton → airtable uses title case) and a soft note (agelessrx `business_model` also a mild simplification); both corrected in read/run-notes. 6th consecutive run (042/045/047/048/049/050) where the verifier earns its keep. | VR1; read.md Result (pre/post); run-notes S1 | VR1 · risk-miss |

## Lenses

**Steward** — System stayed honest. State (skeleton, fields, flags) vs Judgment (cold-start verdict, Strategic read) stayed separable; uncertainty is visible *in the State itself* via `unverified_fields`. The one honesty risk is salience, not content: the trust block is present 6/6 but off the forced path (S3) — the same relay-dependence as 038-R1/042-R1/049-G1, now confirmed on the raw `profile.md` surface (where it's mildest — it bites harder on the rendered brief).

**Dev Agent** — No new toil to remove. The cold-start question itself is a cheap, reproducible **store-health check** (the C1 slot rule re-runs in seconds) — worth noting as a reusable diagnostic shape, not a build. The grep-verifiable contract (uniform skeleton) is exactly the kind of thing that makes cold-start work; nothing to add.

**Founder** — The run compounds the warm asset (reproducible sample, reusable cold-start probe) while staying light. The disposition is squarely "no new primitive needed": the cold-start scaffold + trust surface already exist and work; the two residuals are a fast-read field (fix, *if ever*, = run-037 W1 ranked multi-select `business_model`, and only for a filtering consumer) and a salience discipline (no field). Avoid the temptation to read "cold-start works" as license to add a "completeness score" or a "cold-start-ready" flag — that would be exactly the ontology gravity the lab refuses.

## Recommendation

- **No-op / keep as observation:** the cold-start scaffold is a strength to record, not a thing to change. S1–S4 / G1 / CR1 / VR1 are sightings for the stream.
- **Watch for recurrence** (`learning_tags`): `query-time-grouping-enough` (cold-start needs no new object), `schema-edge-entity-type` (`business_model` single-valued lossiness — now n≥3 across 037/044/051), `source-rigor` (`unverified_fields` salience/relay-dependence — recurs across 038/042/049/051), `confidence-grain` (the run's axis), `coverage-caveat` (vintage drift).
- **Severe `risk-miss` to surface now:** none. VR1 is a caught-and-corrected precision slip, not a shipped error.

## Raw learning to preserve

Run-notes Observations S1–S4, G1; plus consumer-review CR1 and this review's VR1. All lifted to `learning/observations.md` this pass.

**No lessons proposed, nothing graduated, spiked, or implemented.**
