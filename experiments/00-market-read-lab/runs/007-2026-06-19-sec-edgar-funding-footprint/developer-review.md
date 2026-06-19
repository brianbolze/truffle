# Developer Review — Run 007 (SEC EDGAR Funding Footprint)

**Question: What Truffle system behavior does this run pressure?**

## Capability pressure

| Capability | What did the run expose? | Smallest useful response |
|---|---|---|
| **Capture** | The `sec_edgar` tool already captures match-quality grades, `is_vehicle`, `distinct_ciks`, and `existence_only`/`material_filing` flags alongside the headline fields — the right things travel. The one honest ceiling: `amount: null` everywhere (Form-D primary-doc bodies aren't fetched). Deliberate scope call, not a bug. | No-op. Signal is well-structured. Live Form-D body fetch is approval-gated and out of scope for store-only; the boundary works as designed. |
| **Structure** | (a) **State/Signals/Judgment boundary** handled cleanly (filing dates/match quality = Signal; "funded/mature" = labeled Judgment). (b) **CIK-as-entity-key dedup** — two domains sharing CIK `0001386570` was caught by eye, not a structural join; the domain-keyed store has no native way to see it. | Watch. Real, but one collision pair in 20 is thin. No CIK entity table (anti-Doro swamp). A 2nd collision pair earns a one-line QUERYING note ("when a CIK spans >1 domain's sec_edgar signal, verify before counting issuers"). |
| **Query / access** | **MRL-002 trigger crossed.** 3rd Signals-grain read (005 Trustpilot → 006 Wayback → 007 SEC) to hand-roll the identical loop: glob `signals/<type>/*.json`, latest-per-dir, extract headline + integrity fields, join `telehealth.md`. Run 006 named the 3rd sighting as the threshold. Met — across three *distinct* grains, not three repeats. | Submit MRL-002 evidence append. A *documented* QUERYING signals-read recipe (latest-per-dir idiom, field extraction, confound-sibling rule). Pattern-level only; no helper script. Human graduation call. |
| **Freshness / automation** | Captures 1–4 days old, current. No freshness pressure. 20/54 coverage floor is a standard opt-in capture gap. | No-op. |
| **Synthesis** | The 4-bucket match-quality classification (public issuer / confirmed Form-D / name-collision / no footprint) is a reusable output shape, derived at query time from the signal's own `form_d.match` field — no durable object needed. | No-op. Good QUERYING recipe note; emerges from the captured field, not a new primitive. |
| **Guardrails** | All Loop 1 exit checks passed; no live fetch / no store mutation. The `total_hits` false-positive trap was caught by the run. **3rd captured-signal-confound sighting** for MRL-008: family now spans 3 signal types (reputation/score, tenure/days, funding/match-quality) with 3 distinct root causes. The adversarial Loop 2 pass additionally caught 2 supporting-detail errors (issuer name, flag universality) that were corrected pre-sign-off. | Submit MRL-008 evidence append. 3rd sighting strengthens graduation; but the heterogeneous root-cause spread means a convention must name *how* confounds differ, not just that they exist. Human call. |

## Lenses

**Steward** — Cleanest State/Signals/Judgment boundary in any run so far: dates, match quality, CIK,
names all in Signal; "maturity tier"/"funded" labeled Judgment and kept out of the panel. The honest
provenance gap (filing dates are *entity* raise dates, not brand/product age) mirrors Run 006's
Wayback domain-history-≠-brand-history trap and was flagged proactively. The 20/54 floor was bounded
consistently ("not found" vs "not there" vs "no signal captured" all kept distinct). The two
verification-stage corrections were precision slips in *supporting* language, not judgment errors —
and the adversarial pass caught them, which is the system working.

**Dev Agent** — The 3rd hand-rolled Signals loop is the mechanical signal. It's simple (glob → sort →
extract → join), which is why it was never broken into a helper — but simple-and-repeated is exactly
where a *documented recipe* (not code) earns its keep: a QUERYING entry covering latest-per-dir, field
selection, and the confound-sibling rule would stop the nth run re-inventing it. The
`is_vehicle`+`distinct_ciks`+`form_d.match` cluster is a reusable filter idiom that already travels in
the JSON; it needs one sentence ("always project these alongside `total_hits`"), not a tool. CIK dedup
is a one-liner candidate *only* on a 2nd collision pair.

**Founder** — Two outputs compound the warm/cited/cheap asset, both note-level not primitive-level:
the Niagen one-issuer/two-domain dedup (a relation fact that survives in a QUERYING note) and the
4-bucket match-quality taxonomy (a reusable SEC read shape). The CIK-entity-table path is clearly
anti-Doro — a domain-keyed store is the decision that *deletes* the reconciliation swamp; one manual
dedup eyeball per run is orders of magnitude cheaper. The cross-signal 2x2 (sec_edgar × trustpilot) is
the highest-value follow-up — both grains are now characterized, so the composition is query-ready.
That's the next read, not a structural change.

## Recommendation

- **No-op / keep as observation:** State/Signals/Judgment boundary (clean); synthesis bucket shape
  (emerges from captured field); freshness; capture (well-structured).
- **Watch for recurrence:** CIK-as-entity-key dedup — one collision pair (Niagen) in 20 domains; note
  it, build nothing. A 2nd pair earns a one-sentence QUERYING note. MRL-007 unmoved (3rd consecutive
  Signals run with a cleanly per-domain signal — no homeless category-level signal).
- **Submit triage candidate:** MRL-002 (3rd Signals-grain sighting — recipe earned at pattern level)
  and MRL-008 (3rd captured-signal-confound sighting — root-cause flavor: collision-inflated count).

## Triage submissions

**MRL-002 evidence append (3rd Signals-grain sighting — 007 SEC-EDGAR):** third consecutive
Signals-consumption read (005 Trustpilot, 006 Wayback, 007 SEC) to hand-roll the identical
latest-per-dir + field-extract + frontmatter-join loop — the exact threshold Run 006 named. Sightings
span distinct grains, not one repeated query. A documented QUERYING signals-read recipe (latest-per-dir
selection, field extraction, confound-sibling rule — "always pull
`form_d.match`/`is_vehicle`/`distinct_ciks`/`existence_only` alongside `total_hits`") looks earned at
pattern level. Not a built helper. Human graduation call.

**MRL-008 evidence append (3rd captured-signal-confound sighting — 007 SEC-EDGAR):** `total_hits`
reads as a headline (maximustribe 45) but is collision-inflated and resolves to zero real filings; the
trustworthy discriminators are captured correctly but must be pulled deliberately. Root-cause flavor:
*collision-inflated count* — distinct from Trustpilot's intrinsic-ambiguity and Wayback's
correct-fact-naive-read flavors. Three sightings strengthens the "confounds travel with the field"
graduation case; caveat: the three flavors are heterogeneous enough that a single rule may need to name
the confound *type*, not just its existence. Human call on graduate-now vs sharpen-with-a-4th-sighting.
