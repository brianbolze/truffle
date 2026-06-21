# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

Do not default to "capture more data." Ask whether the run exposed a reusable system need: capture, structure, query, freshness, automation, access, or guardrails.
Record the gap as an observation first. Do not convert it into a recipe, field, tool,
or build proposal inside the run unless the review adds enough evidence for a triage
candidate.

Market reads may make judgments. When they do, ask whether the read clearly crossed from State or Signals into Judgment, and whether Truffle should support that boundary or leave the judgment downstream.

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Discovery disposition |
|---|---|---|---|
| **Capture** | No new capture gap. The discipline is excellent — every profile carries at least one `unverified_fields` item and caveats consistently use "not found" language, never "not true." | C1, C5 | Strength, no action. |
| **Structure** | `unverified_fields` is one prose bucket doing ≥6 structurally distinct jobs. The two highest-reader-value kinds (inferred ~11% / conflict ~12%) are not separable from the dominant completeness-note kind (~48%) by any greppable token. Confidence/provenance is also fragmented across five contract destinations (unverified_fields / Enriched / STRAIN / prose discrepancy / point-in-time literal) — none is a unified "how confident is field X" surface. The only queryable confidence token is point-in-time, and it is queryable only because SCHEMA gave it a literal string. | C2, C6, S1, SCHEMA.md:112 | Watch (single sighting). If a real cross-store agent consumer surfaces, the lightest structural fix is a prefix-token convention on the two high-value kinds — not a new field (see Founder lens below). |
| **Query / access** | `query-time-grouping-enough` is definitively FALSE for the question "retrieve all low-confidence or inferred facts at query grain." A reader can grep for point-in-time volatility but cannot mechanically separate inferred or conflicted values from completeness notes in the same bucket. | G1, C3 | Watch — but the fix is a convention, not a query primitive. No live consumer of cross-store confidence filtering exists. |
| **Freshness / automation** | Not load-bearing here. Corpus is uniformly recent (2026-05-30 → 2026-06-20); the gap is structural, not stale. | read.md Missing/Stale Coverage | No action. |
| **Synthesis** | The read correctly kept the six-kind taxonomy and its bucket shares as an explicitly labeled derived Judgment ("heuristic keyword classifier + sample-validation; shares are derived Judgment, not a captured field"). The State/Signals/Judgment boundary held throughout. STRAIN's characterization (70% branding, not confidence signal) was also reported as keyword-derived. | C2, C7, read.md Result | Strength — boundary management was clean and explicit. |
| **Guardrails** | F1 friction: every confidence read requires a fresh hand-rolled keyword parse over 424 free-text prose items because there is no structured field to group on. One sighting; mirrors the MRL-002 prose-parse friction family. Not a guardrail failure, but repeated toil if confidence reads recur. | F1, run-notes.md friction log | Recur-watch (MRL-002 family). |

## Lenses

**Steward** — The honesty discipline is real and clearly maintained. 130/130 profiles carry non-empty `unverified_fields`; absence language is consistently "not found," never "not there"; discrepancies are reported verbatim rather than silently reconciled. The State/Signals/Judgment line was held cleanly in the read: the six-kind taxonomy was labeled as a derived Judgment (Loop 1's own reasoning), not a captured field, and the 73%→70% STRAIN correction was folded correctly before evidence submission. No provenance drift observed. The structural observation — that the five confidence destinations don't compose as a unified trust surface — is an honest finding about the contract's current shape, not a failure of capture or of this run. Confidence is fragmented *by design* (five destinations in SCHEMA), not by accident.

**Dev Agent** — The one actionable convention the run surfaces is already present in embryo: the point-in-time literal (SCHEMA.md:112) proves a prefix token works for greppability with zero schema migration. If a second sighting justifies anything, the parallel is trivial — an `inferred:` / `conflict:` lead token on `unverified_fields` bullets that carry those kinds, routing scope-omissions to Provenance's `Couldn't get` / `Run profile` lines where the contract already wants them. That is the full scope of any potential convention. It costs nothing to hold until a real consumer demands it: there is no cross-store confidence-filter consumer today. Additionally, F1 (hand-rolled keyword parse) is one sighting of the MRL-002 prose-parse toil family — not actionable at one hit, but note it.

**Founder** — The anti-sprawl call is the right one. A per-fact `confidence:` field would be false-precise across 424 heterogeneous caveats (a branding capture-fail and an inferred founding date are both in `unverified_fields` but they carry completely different reader meaning), would impose a migration blast-radius across 130 profiles, and would rot as captures age. The existing point-in-time literal is the right template *and* the right ceiling — it exists because volatility is a single, homogeneous kind with a single consumer action (re-run before relying on it). Inferred/conflict are more heterogeneous and, more importantly, have no documented live consumer for cross-store aggregation. "No new primitive needed" is the honest outcome for a single sighting with no live consumer. The engine spends on durable conventions, not living infrastructure.

## Recommendation

- **No-op / keep as observation:** The read is internally clean. The six-kind taxonomy and bucket shares are one-run derived Judgment, correctly labeled. STRAIN's ~70% branding characterization (confirmed from run-027) needs no action.
- **Watch for recurrence:** `confidence-grain` tag (coined this run) — a second sighting, especially one where a real downstream consumer needs to filter facts by confidence at scale, would move the prefix-token convention from wish to justified candidate. F1 prose-parse friction — one sighting, recur-watch under MRL-002.
- **Submit triage evidence (limited scope):** Submit an Evidence Log branch on **MRL-008**, not a new MRL item. Reasoning below.

### New MRL item vs MRL-008 branch?

Run-031's finding is the meta-generalization of MRL-008's run-026 "bare State field isn't self-describing" branch — it extends the same insight from one relation field (`parent:[]`) to the whole self-uncertainty layer (`unverified_fields`). The mechanism is identical: a store surface that is populated and honest but whose prose content is not self-describing at query grain, so a naive consumer overcounts or misreads without knowing it. The run-026 branch is a precise ancestor.

A new MRL item is warranted when the pressure is **categorically** distinct from any existing item family. Here it is not: the "confidence layer doesn't compose as a query surface" observation belongs on the source-rigor / confound axis (MRL-008). The run itself names this in its pressure tags: `source-rigor` fired, and the triage note reads "submit Evidence Log entry to MRL-008 (new branch: the layer doesn't compose as confidence)."

**Recommendation: submit an Evidence Log branch on MRL-008.** The coined pressure tag `confidence-grain` is a useful handle for recurrence-tracking but does not by itself justify a new MRL item — it is a refinement of source-rigor on the meta-uncertainty axis. If a second run under the `confidence-grain` tag produces a new mechanism (e.g., a live consumer blocked by the gap, or a prefix-token convention that proves generalizable), a new item becomes justified. Until then, absorb into MRL-008 as a fourth branch: *"the whole uncertainty layer is a prose catch-all that doesn't compose into a trust signal, not just individual fields."*

## Optional triage evidence

Single sighting — hold, do not graduate. No-op on primitives and conventions. Three backlog-ready bullets for Loop 2 to route to triage:

- **[MRL-008 branch, Evidence Log]** Run-031 extends the run-026 "bare field isn't self-describing" flavor to the whole self-uncertainty layer: `unverified_fields` is populated and honest in 130/130 profiles but is a free-text catch-all doing ≥6 structurally distinct jobs — only the point-in-time kind is greppable (SCHEMA literal). The two highest-reader-value kinds (inferred ~11%, conflict ~12%) are prose-only and not separable by query. Confidence is additionally fragmented across five contract destinations (C6). This is a fourth branch on MRL-008: *surface sibling* (State/Signal) / *read prose, don't aggregate* (Judgment layer) / *disambiguate the empty* (relation State) / *the whole uncertainty layer doesn't compose as a trust surface* (meta). Tag: `confidence-grain`. Pointer: run-031 `read.md` + `run-notes.md` O1–O5, S1, G1. Hold; second sighting or live consumer before any convention graduates.
- **[MRL-008 branch, W1 — watch]** If a real cross-store agent consumer needs to filter facts by confidence, the lightest candidate fix is a greppable prefix-token convention on the two high-value `unverified_fields` kinds (e.g., `inferred:` / `conflict:` lead-token mirroring the point-in-time literal) plus routing scope-omissions to Provenance `Couldn't get`. Zero new schema, zero per-profile migration. "No new primitive needed" remains the honest outcome until a live consumer appears. Pointer: run-031 `run-notes.md` W1.
- **[MRL-002 family, F1 — recur-watch]** Confidence-read toil: every cross-store confidence-grain read requires a hand-rolled keyword classifier over 424 free-text prose strings (no structured field to group on). One sighting; mirrors MRL-002 prose-parse friction. Absorb into MRL-002's friction log; no action at one hit. Pointer: run-031 `run-notes.md` F1.
