# Developer Review

Question: **What Truffle system behavior does this run pressure?**

Do not default to "capture more data." Ask whether the run exposed a reusable system need: capture, structure, query, freshness, automation, access, or guardrails.

Market reads may make judgments. When they do, ask whether the read clearly crossed from State or Signals into Judgment, and whether Truffle should support that boundary or leave the judgment downstream.

## Capability pressure

| Capability | What did the run expose? | Smallest useful response |
|---|---|---|
| **Capture** | Source type, capture grain, receipt shape, or external tool need. |  |
| **Structure** | State / Signals / Judgments boundary, fields, modules, relation shape. |  |
| **Query / access** | Query recipe, helper, routing, MCP/API surface, or denominator ergonomics. |  |
| **Freshness / automation** | Refresh, enrichment, expansion, monitoring, or budget gate pressure. |  |
| **Synthesis** | Read template, judgment labeling, caveat language, market lens, or repeatable output shape. |  |
| **Guardrails** | Source rigor, status gates, no-auto-graduation, spend/live-browse approval. |  |

## Lenses

**Steward** — Is the system still honest? Provenance, freshness, grain, State / Signals / Judgments separation, and visible uncertainty.

**Dev Agent** — Can repeated toil be removed with a convention, recipe, or tiny helper? Prefer grep-verifiable contracts and fewer knobs.

**Founder** — Does the response compound the warm / cited / cheap-to-reask asset while staying light? Avoid ontology gravity and one-off surfaces.

## Recommendation

- No-op / keep as observation:
- Watch for recurrence:
- Submit triage candidate:

## Triage submissions

Submit queue candidates only when the review adds new evidence. No-op is acceptable.

**Do not graduate, spike, or implement system changes.**
