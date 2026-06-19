# Receipt - <short name>

One sentence on what this receipt supports.

```yaml
receipt_type:          # store-query | local-file | source-panel | external-source | operator-observation
created:               # YYYY-MM-DD
evidence_mode:         # store-only | local-existing | bounded-live | live-external-needs-approval
source_grade:          # primary | secondary | derived | direction-finding
source_family:         # owned/official | SERP/listicle | review/forum | ads/social | Wayback/dated-signal | news/regulatory/manufacturer | local-store
spend_note:            # none | free | paid-credit
snippet_only:          # yes | no
claim_ids_supported: []
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 |  |  | owned/official / store file / regulator / manufacturer / news / search result / review/forum / operator observation | primary / secondary / derived / direction-finding | none/free/paid-credit | yes/no | C1 |

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
