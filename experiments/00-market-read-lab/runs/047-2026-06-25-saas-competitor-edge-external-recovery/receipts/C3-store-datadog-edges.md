# Receipt - Store baseline: Datadog edges + rival node coverage

Supports the store-side claim: edges are prose-only, no structured relation, 0/5 rivals
captured.

```yaml
receipt_type: store-query
created: 2026-06-25
evidence_mode: bounded-live
source_grade: primary
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C3]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | store/datadoghq-com/profile.md (lines 74, 120; frontmatter parent/owns) | store clock 2026-05-31 | store file | primary | none | no | C3 |
| S2 | `ls store/` filtered for newrelic/dynatrace/splunk/grafana/elastic | 2026-06-25 | store query | derived | none | no | C3 |

## Method

`grep` of datadoghq-com/profile.md for competitor/rival lines; `ls store/` to test which
named rivals have captures.

## Evidence

- `:74` — "**Competes with:** New Relic, Dynatrace, Splunk, Grafana, Elastic, plus
  cloud-native tools and security point vendors — depending on pillar."
- `:120` — security adjacency: "Wiz/CrowdStrike/Splunk."
- Frontmatter: `parent: []`, `owns: []` — vertical relation only; no competes-with field.
- `ls store/` returns only `datadoghq-com` for the observability set → 0/5 rivals captured.

## Limits

Single-anchor; the "no horizontal relation" point is a store-wide schema fact (confirmed in
run-039), not unique to Datadog.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C3 | Datadog rivals are prose-only, unstructured, 0/5 captured | S1, S2 | — |
