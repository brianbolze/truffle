# Receipt - audience × anchor_category cross-tab

Supports the audience-lean distribution and the audience × category whitespace grid for
run 020, derived entirely from local store `telehealth.md` frontmatter.

```yaml
receipt_type: store-query
created: 2026-06-20
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/*/telehealth.md` (54 files) `audience:` + `anchor_category:` frontmatter | store frontmatter, captures dated 2026-06 | local-store / store file | derived | none | no | C1, C2, C3, C4 |

## Method

```python
# For each store/*/telehealth.md:
#   read first `audience:` line, strip inline `# comment`, take the value verbatim
#   read first `anchor_category:` line, strip comment, take value verbatim
# Bucket audience into lean: men-only/men-first -> MEN; women-only/women-first -> WOMEN; all-genders -> ALL
# Cross-tab anchor_category (rows) × lean (cols)
```

`audience` value is taken **verbatim from the field**, never inferred from the brand name
(contract requirement; the field comments explicitly warn that several brand names mislead
about audience, e.g. "read from pages, not the name").

## Evidence

- **C1:** 54 files match `store/*/telehealth.md`; `grep -l "^audience:"` = 54 and
  `grep -l "^anchor_category:"` = 54. Both fields present on all 54.
- **C2 — audience buckets:** all-genders 34, men-first 8, men-only 7, women-only 3,
  women-first 2. Lean rollup: ALL 34 / MEN 15 / WOMEN 5.
- **C3 — cross-tab (category: MEN / WOMEN / ALL / total):**
  GLP-1 2/3/14/19 · TRT 7/0/1/8 · longevity-NAD 0/0/8/8 · multi-none 1/1/8/10 ·
  sexual-health 3/0/0/3 · peptides 1/0/1/2 · womens-HRT 0/1/0/1 · hair 1/0/0/1 ·
  labs 0/0/1/1 · primary-care 0/0/1/1. Column totals 15/5/34 = 54. ✓
- **C4 — women-leaning 5:** brellohealth (women-only/GLP-1), effecty (women-first/GLP-1),
  innerbalance (women-only/womens-HRT), nurx (women-only/multi-none), remedymeds
  (women-first/GLP-1). **TRT 8:** defymedical, getopt, getpetermd, marekhealth, maximustribe,
  trtnation (men-first), vitalityrx (men-only), hormonemd (all-genders). **sexual-health 3:**
  bluechew, rexmd, rugiet (all men-only).

## Limits

- Counts are **captured supply**, not market supply. The cohort is intentionally men's-
  hormone-tilted (prior lab runs), so the 15-vs-5 lean asymmetry is a selection artifact.
- Per-category cells are **floors**: the anchored-only `anchor_category` cut excludes
  `multi/none` generalists that serve a category without anchoring to it (MRL-001).
- `audience` is a supply-side positioning field (front-door framing), not a measured
  customer mix. Empty cells = "not captured," not "market absent."

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | 54/54 brands carry both fields | S1 | — |
| C2 | Audience buckets + 34/15/5 lean rollup | S1 | supply-side positioning, not customer mix |
| C3 | Full audience × category grid | S1 | per-category cells are floors (anchored-only) |
| C4 | Named women-leaning 5 + all-male TRT/ED cells | S1 | absence = not-captured, not market whitespace |
