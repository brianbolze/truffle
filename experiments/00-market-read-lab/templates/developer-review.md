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
| **Capture** | Source type, capture grain, receipt shape, or external tool need. |  |  |
| **Structure** | State / Signals / Judgments boundary, fields, modules, relation shape. |  |  |
| **Query / access** | Query recipe, helper, routing, MCP/API surface, or denominator ergonomics. |  |  |
| **Freshness / automation** | Refresh, enrichment, expansion, monitoring, or budget gate pressure. |  |  |
| **Synthesis** | Read template, judgment labeling, caveat language, market lens, or repeatable output shape. |  |  |
| **Guardrails** | Source rigor, status gates, no-auto-graduation, spend/live-browse approval. |  |  |

## Lenses

**Steward** — Is the system still honest? Provenance, freshness, grain, State / Signals / Judgments separation, and visible uncertainty.

**Dev Agent** — Can repeated toil be removed with a convention, recipe, or tiny helper? Prefer grep-verifiable contracts and fewer knobs.

**Founder** — Does the response compound the warm / cited / cheap-to-reask asset while staying light? Avoid ontology gravity and one-off surfaces.

## Recommendation

- No-op / keep as observation:
- Watch for recurrence:
- Submit triage evidence only if mature:

## Optional triage evidence

Submit queue candidates only when the review adds new evidence. No-op is acceptable.
Raw builder observations, wishes, frictions, surprises, and singletons should first be
preserved in `run-notes.md` Discovery ledger and `discovery-ledger.md`.
Keep any triage text to 1-3 backlog-ready bullets with pointers to the run or
`discovery-ledger.md`; do not use triage as the narrative home.

**Do not graduate, spike, or implement system changes.**
