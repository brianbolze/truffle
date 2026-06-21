# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Discovery disposition |
|---|---|---|---|
| **Capture** | `captured_at` is present 130/130 (strength) but format-inconsistent: 4 quoted, 126 bare. A volatility-flag *coverage* question is open — the token's recall (is it applied to every volatile profile?) was not measured. | G3; receipt; C2 token=57 | Submit Evidence Log → MRL-008 (parse-hazard family) on the format; coverage = capture-discipline note, no-op. |
| **Structure** | The State/Signals/Judgment boundary held cleanly. Freshness-risk is a Judgment derived from two State surfaces (`captured_at` + the point-in-time token); the read labeled it as such and did **not** invent a `staleness:`/`confidence:` field. The token itself is correctly scoped to capture-volatility (SCHEMA-112), not staleness. | O1, O3, S1; SCHEMA.md:112 | No-op — a clean boundary hold; reinforces "no new freshness marker." |
| **Query / access** | No MRL-002 recipe covers a cross-company *freshness-risk* read; the age×token×signals-clock cross was hand-rolled Python. Third grain (after Signals-read, traction-enumeration) where the same multi-grep machinery recurs. | F1; DEV-R29-A lineage | Watch for recurrence; fold into MRL-002 evidence as a freshness-read recipe variant on a 2nd sighting. |
| **Freshness / automation** | The core finding: **signals do not refresh State** (0/49 newer than capture) and there is **no drift surface**. Staleness-*risk* is computable; actual *change-detection* requires a re-capture+diff cadence that does not run today. | O2, G1; C5 | Submit Evidence Log → MRL-012 (generalizes change-pulse from Signals to State). |
| **Synthesis** | The read template carried a genuinely-two-sided calibration well (Result + Gap Map + verdict). The "two surfaces answering different questions" framing is a reusable shape for trust-metadata reads (sibling to 031). | read.md Result/Gap Map | No-op — synthesis worked; note the shape. |
| **Guardrails** | Source-rigor guardrail *fired and held*: the run reproduced its named failure mode twice (loose-grep over-count to 57; quoted-date drop) and the discipline (literal token + quote-aware parse) + the Loop-2 verifier caught both. The verifier also corrected the health denominator 65→69 (same quoted-date bug leaking into the vertical cut). | V1; C4; verifier verdict | No-op — the adversarial gate did its job; a healthy data point. |

## Lenses

**Steward** — The system stayed honest. Provenance is dated per-profile; the read never claimed
"not stale" where it could only show "not old + not flagged volatile"; absence framed as
"unobservable store-only," not "no drift exists." The State/Signals/Judgment separation survived a
read whose whole subject is trust-metadata. The one honesty wrinkle the run *exposed* (not caused):
the `captured_at` format split means the store's own freshness field isn't uniformly greppable — a
small provenance-legibility nick worth a lint.

**Dev Agent** — The repeated toil is real but recipe-level, not helper-level: "staleness-risk = age
× point-in-time token" is a one-line grep-verifiable contract, exactly the MRL-002 shape. Prefer
documenting that cross + normalizing `captured_at` quoting over any new field. No new knobs. The
token's grep-verifiability (literal SCHEMA string) is the model to preserve — it's *why* this read
was cheap where 031's prose-only confidence kinds were not.

**Founder** — This compounds the warm asset without ontology gravity: the answer fell out of two
fields that already exist, and the verdict is "no new primitive." The temptation to add a durable
`volatility:` or `staleness_score:` field is exactly the ontology-gravity the anti-Doro line refuses
— and the read resisted it. The only spend-worthy item (drift detection) is correctly deferred to
the parked, approval-gated re-capture cadence, not smuggled in as a field.

## Recommendation

- **No-op / keep as observation:** the Structure/Synthesis/Guardrails rows (clean boundary hold,
  working template, adversarial gate fired) — all strengths, no build.
- **Watch for recurrence:** the MRL-002 freshness-read recipe gap (F1, 1 sighting on this grain);
  the point-in-time token *coverage/recall* question (capture-discipline).
- **Submit triage evidence (mature):** two Evidence-Log appends, below — to existing items, no new IDs.

## Optional triage evidence

- **MRL-012** (change-pulse / re-capture readiness): append — this run generalizes change-pulse from
  the Signals axis to the **State** axis. Two new data points: signals do not refresh State (0/49
  newer than capture), and staleness-*risk* is query-time-derivable (`captured_at` × point-in-time
  token, 34 high-risk) while actual *drift* needs the parked re-capture+diff cadence. Pointer:
  discovery-ledger O2/G1/S1, run 032.
- **MRL-008** (source-rigor / parse-hazard family): append — `captured_at` format inconsistency (4
  quoted / 126 bare) silently drops profiles from a naive freshness grep; reproduced by this run's
  own Loop-1 parser and the Loop-2 health-denominator (65→69). One-line normalization or a
  `querycheck` lint. Pointer: discovery-ledger G3/V1, run 032.

**Do not graduate, spike, or implement system changes.**
