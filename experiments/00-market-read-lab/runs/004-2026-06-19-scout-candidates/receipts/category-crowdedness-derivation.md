# Receipt - category-crowdedness-derivation

Supports the front-door and breadth-aware crowdedness counts in `read.md`.

```yaml
receipt_type:          store-query
created:               2026-06-19
evidence_mode:         store-only
source_grade:          derived
snippet_only:          no
claim_ids_supported: [C1, C2, C3]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source type | Grade | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|
| S1 | `store/*/telehealth.md` frontmatter (`value_chain_role`, `anchor_category`) | captures 2026-05-30..06-18, oldest ~20d | store file | derived (from primary captures) | no | C1, C3 |
| S2 | `store/*/offerings.md` `## Roster` rows (buyable SKU molecule/name cells) | captures 2026-06-03..06-18, oldest ~16d | store file | derived (from primary captures) | no | C2, C3 |

## Method

1. Parsed `telehealth.md` frontmatter across all 54 `store/*/telehealth.md` packs
   (strip inline `#` comments). Gated to `value_chain_role == "DTC brand"` → **53**
   brands. Excluded functionhealth-com (`diagnostics/labs`).
2. **Front-door count (C1):** `Counter(anchor_category)` over the 53 gated brands.
3. **Breadth count (C2):** for each gated brand, extracted `## Roster` rows from
   `offerings.md`, kept pipe-delimited rows that are not `family` header rows, and
   matched a fixed per-category molecule/brand regex against the lowercased row text
   (which includes the `Offering` name and the `What (molecule · form · access)` cell).
   Counted *distinct brands* with ≥1 matching buyable row per category.
4. **Spillover (C3):** intersected the GLP-1 breadth set with the GLP-1 front-door set.

Molecule regexes used (roster-cell match only):
- GLP-1: `semaglutide|tirzepatide|liraglutide|retatrutide|orforglipron|wegovy|ozempic|zepbound|mounjaro`
- sexual/ED: `sildenafil|tadalafil|vardenafil|viagra|cialis|avanafil`
- TRT: `testosterone|enclomiphene|clomiphene|\btrt\b|androgel`
- hair: `finasteride|minoxidil|dutasteride`
- peptides: `bpc-?157|sermorelin|ipamorelin|cjc-?1295|tesamorelin|pt-?141|\bpeptide`
- longevity/NAD: `\bnad\b|nad\+|rapamycin|nicotinamide|niagen|\bnmn\b`
- mental health: `escitalopram|sertraline|bupropion|fluoxetine|citalopram|lexapro|zoloft|wellbutrin|buspirone`
- women's HRT: `estradiol|progesterone|estrogen`

## Evidence

**Front-door (C1, n=53):** GLP-1 19 · multi/none 10 · longevity/NAD 8 · TRT 8 ·
sexual-health 3 · peptides 2 · hair 1 · womens-HRT 1 · primary-care 1.

**Breadth (C2, n=53):** GLP-1/weight 41 · peptides 30 · longevity/NAD 30 ·
TRT 27 · sexual health/ED 24 · hair 23 · women's HRT 22 · mental health 10.

**Spillover (C3):** 41 sell GLP-1 / 19 anchor GLP-1 / 22 sell-but-don't-anchor:
agelessrx-com, gethealthspan-com, getopt-com, getpetermd-com, gogeviti-com,
hellopepti-com, hellowisp-com, hevahealth-com, honehealth-com, hormonemd-com,
hydramed-com, invigormedical-com, joiandblokes-com, kingsbergmedical-com, lifemd-com,
maximustribe-com, mylifeforce-com, nurx-com, prohealth-com, rexmd-com, struthealth-com,
trtnation-com.

All 53 DTC packs had ≥1 parsed roster row (no enumeration-floor zeros).

## Limits

- **Derived, not stored.** There is no normalized per-SKU category field; the breadth
  count is a query-time molecule-string match. A rejected whole-file grep returned
  TRT 53/53 and labs 53/53 (inflated by prose/FAQ) — the roster-cell match is the
  corrective, but mid-band ranks (peptides/longevity/TRT, 27–30) are close enough that
  molecule-set choices could reorder them. The GLP-1 lead and mental-health floor are
  robust to method.
- **Captured floor, not census.** Telehealth is the store's one deep cohort; counts say
  nothing about the real market and "thin" means "few captured brands," not "thin market."
- Molecule match is page-attested via the roster cell; a brand that sells a category but
  whose roster cell names only a brand-name (not a molecule) in a form the regex misses
  would undercount. No price magnitude or value is used or claimed.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | Front-door crowdedness: GLP-1 (19) leads; long thin tail | S1 | one value/brand; undercounts multi/none's spread |
| C2 | Breadth crowdedness: GLP-1 (41) leads, mental health (10) floor | S1+S2 | derived molecule match; mid-band ranks soft |
| C3 | 22 brands sell GLP-1 without anchoring it (bolt-on pattern) | S1∩S2 | roster-cell attested only |
