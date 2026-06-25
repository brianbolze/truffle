# Receipt - No JTBD / use-case field exists

Supports the claim that the store has no structured field encoding the buyer goal a
company serves.

```yaml
receipt_type: store-query
created: 2026-06-25
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/*/profile.md` frontmatter (145 profiles) | per-profile `captured_at` | local store file | derived | none | no | C1 |

## Method

```
grep -riE "^(use_case|job_to_be_done|jtbd|condition|use_cases|tags|vertical):" store/*/profile.md
```

Returns zero matches across all 145 profiles.

## Evidence

Empty result set. The frontmatter contract (`SCHEMA.md`) carries `primary_industry`,
`offering_category`, `business_model`, `target_market`, `price_visibility` — all
producer-shaped — and no buyer-goal / condition-served field.

## Limits

Proves no *frontmatter* field encodes JTBD. It does not prove the job is unrecoverable —
body prose carries it (that is the whole point: it's prose, not a queryable field).

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | No structured field encodes the buyer goal / use-case a company serves | S1 | Job is recoverable from prose, just not from a field |
