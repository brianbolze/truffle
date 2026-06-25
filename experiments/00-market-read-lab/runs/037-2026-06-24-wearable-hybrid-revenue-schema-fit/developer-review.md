# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation (ID · kind) |
|---|---|---|---|
| **Capture** | Strength: pure one-time foils (Therabody/Hyperice/Nike) captured cleanly — the field is accurate when revenue is single-leg. | read.md Foils paragraph | S1 · surprise (boundary) |
| **Structure** | Gap: single-valued `business_model` drops one leg of a co-primary hardware+subscription structure; the split survives only in prose / inline `STRAIN:` comments, and `offering_category` is an inconsistent proxy (Eight Sleep's mandatory sub absent from it). | read.md Result(1); eightsleep profile:42-44 | S1 · surprise; G1 · gap |
| **Query / access** | Gap: no single structured field draws the connected-hardware cohort. `Hardware ∧ Subscription` recovers the 4 pure-plays (C1) but is a homogeneity artifact — it wrongly excludes Apple. `primary_industry` scatters across 3 values. | read.md Companies Seen; C1 grep | G2 · gap |
| **Freshness / automation** | Note: prices are promo-snapshots; structure-only read is unaffected, but a live cost read would need refresh. | read.md Missing/Stale Coverage | (evidence-limits, not a system gap) |
| **Synthesis** | Strength: State/Judgment stayed clean — the captor's primary-leg pick is flagged non-reproducible, never called wrong. The device-as-a-service spectrum synthesizes structure without a "better model" verdict. | read.md Result(2); Market Pattern | (no leak) |
| **Guardrails** | Strength: store-only, no spend, no schema-change proposal, denominator framed "within the captured store" per L004. The schema itself fail-loud-flagged the strain (3/4 STRAIN markers) — but Peloton had none, so STRAIN is an unreliable second channel. | run-notes exit check; read.md Result(1) | DR2 · gap (STRAIN reliability) |

## Lenses

**Steward** — System stays honest. Provenance, grain, and State/Judgment separation hold;
the one integrity nuance is that the schema's own fail-loud channel (`STRAIN:` comments) is
applied inconsistently (Peloton none, Eight Sleep on `business_model`, Oura/Whoop on
`offering_category`), so a reader can't rely on STRAIN to find every hybrid.

**Dev Agent** — No toil to remove; one grep settled the denominator. The reusable contract
insight is that a `business_model` filter must be treated as lossy on hybrids — a reading
caveat, not a helper.

**Founder** — Compounds the warm asset (cohort draw + denominator are reusable) and stays
light: the run resists ontology gravity, landing "no new primitive needed" with two
specific, testable graduation triggers.

## Recommendation

- **No-op / keep as observation:** yes — "no new primitive needed" is the right disposition
  at n=4 with no filter-needing consumer. W1 names the lightest path (ranked multi-select
  `business_model`) *if* it ever graduates.
- **Watch for recurrence** (`learning_tags`): `schema-edge-entity-type` now spans three
  shapes (035 subtractive gate, 036 off-site economics grain, 037 co-primary revenue) — a
  learning pass may cluster these into one "single-valued `business_model` loses *composite*
  revenue structures" lesson. That is the pass's call, not this run's.
- **Severe `risk-miss` to surface now:** R1 (non-reproducible primary-leg tag) is real but
  scoped as surfaced risk, not proven defect — surfaced, not escalated. Review adds **DR1**:
  the same flip is also a *future-capture* reproducibility risk (a new wearable tagged
  Transactional silently exits the C1 cohort), which the run named only as a hardening
  condition. And **DR2**: STRAIN markers are an unreliable second channel (Peloton none).
  And a tighter scope on S2/L006 captured as **DR3**.

## Raw learning to preserve

Appended to `learning/observations.md` this pass: the run's own rows (S1, G1, R1, G2, S2,
W1) plus three developer-discovered rows — **DR1** (R1 is also a future-capture
reproducibility risk), **DR2** (STRAIN is an unreliable second channel for the hybrid
split), **DR3** (L006 scope is tighter than "two-sided": the trap fires when primary
monetization runs through an intermediary leg with no consumer-facing price).

**Did not propose lessons, graduate, spike, or implement system changes.**
