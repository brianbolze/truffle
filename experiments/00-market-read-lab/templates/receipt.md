# Receipt - <short name>

One sentence on what this receipt supports.

```yaml
receipt_type:          # store-query | local-file | source-panel | external-source | operator-observation
created:               # YYYY-MM-DD
evidence_mode:         # store-only | local-existing | live-external-needs-approval
source_grade:          # primary | secondary | derived | direction-finding
snippet_only:          # yes | no
claim_ids_supported: []
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source type | Grade | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|
| S1 |  |  | company page / store file / regulator / manufacturer / news / search result / operator observation | primary / secondary / derived / direction-finding | yes/no | C1 |

## Method

How the source list, denominator, query, or observation was produced.

## Evidence

Short excerpts, rows, counts, or source notes needed to audit the read.

## Limits

What this receipt cannot prove. If `snippet_only: yes`, this receipt is a lead, not
decision-grade evidence.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 |  | S1 |  |
