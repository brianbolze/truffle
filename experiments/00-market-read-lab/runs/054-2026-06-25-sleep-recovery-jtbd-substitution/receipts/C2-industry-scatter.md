# Receipt - The sleep/recovery JTBD set scatters across industry & category

Supports C2/C3/C4: no single `primary_industry` or `offering_category` draw recovers
the cross-industry sleep/recovery substitute set.

```yaml
receipt_type: store-query
created: 2026-06-25
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C2, C3, C4, C5]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/{eightsleep,ouraring,whoop,apple,therabody,hyperice,nike,onepeloton}-com/profile.md` frontmatter | per-profile `captured_at` | local store file | primary (captured State) | none | no | C2, C3 |
| S2 | `store/{rexmd,rugiet,malemd}-com/profile.md` description + frontmatter | per-profile `captured_at` | local store file | primary | none | no | C4 |
| S3 | `grep -rlE "offering_category:.*Physical Products / Hardware" store/*/profile.md \| wc -l` | 2026-06-25 query | derived | derived | none | no | C3 |
| S4 | `grep -rilE "melatonin\|magnesium glycinate\|sleep aid\|circadian" store/*/profile.md` | 2026-06-25 query | derived | derived | none | no | C5 |

## Method

Pulled `primary_industry` / `offering_category` / `business_model` / `target_market`
for the 8 device/recovery members and the 3 telehealth Rx-sleep members. Counted the
breadth of the only shared structured tag. Grepped supplement-adjacency tokens for the
fuzzy edge.

## Evidence

`primary_industry` across the 8 device members:
- **Technology:** eightsleep, apple
- **Healthcare & Life Sciences:** ouraring, whoop, therabody
- **Sports & Recreation:** nike, hyperice, onepeloton

→ 3 distinct industries for the device set alone; add Healthcare & Life Sciences
(Services / Consulting + Biotech / Pharma) for the telehealth entrants.

`offering_category` shared value `[Physical Products / Hardware]` = **19 profiles**
store-wide (over-inclusive: includes watch brands, Casio, Apple catalog). Telehealth
entrants carry `[Services / Consulting, Biotech / Pharma Products]` — **zero overlap**
with the device members' tags.

`rexmd` description: "...ED, testosterone, GLP-1 weight loss, hair, **sleep**, PE..."
`rugiet`: "...sex, testosterone, **sleep**, longev[ity]..." `malemd`: "...sexual-health,
longevity/peptide, hair, **sleep** and pain..." — sleep is a buried minor Rx line.

## Limits

The member list is assembled by keyword grep on a small token set; it is partial by
construction (a sleep-serving brand without those tokens in description/body is missed).
"Not found" ≠ "not there."

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C2 | Device/recovery set scatters across 3 `primary_industry` values | S1 | Each tag individually defensible |
| C3 | The only shared tag is over-inclusive (19 profiles) and misses telehealth | S1, S3 | — |
| C4 | Telehealth Rx-sleep entrants are tag-disjoint from devices and buried in prose | S2 | — |
| C5 | Supplement adjacency surfaces only by full-text grep | S4 | Fuzzy, full-text-dependent |
