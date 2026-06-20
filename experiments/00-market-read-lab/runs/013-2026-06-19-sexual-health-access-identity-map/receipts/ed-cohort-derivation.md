# Receipt - ED / sexual-health cohort derivation

Documents how the 6-brand ED-identity cohort and the 24-brand ED-selling tail were drawn
from the store, supporting the read's denominator and the anchored-vs-all-offerers caveat.

```yaml
receipt_type:          store-query
created:               2026-06-19
evidence_mode:         store-only
source_grade:          derived
source_family:         local-store
spend_note:            none
snippet_only:          no
claim_ids_supported: [C-denominator, C-undercount, C-structural-cells]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `grep -rl "anchor_category: sexual-health" store/*/telehealth.md` | store, run 2026-06-19 | local-store / store file | derived | none | no | C-denominator |
| S2 | `grep -rli "erectile\|sexual health\|sildenafil\|tadalafil\|\bED\b" store/*/telehealth.md` | store, run 2026-06-19 | local-store / store file | derived | none | no | C-undercount |
| S3 | `telehealth.md` frontmatter blocks for rugiet/rexmd/bluechew/hims/keeps/ro.co | 2026-06-04 → 2026-06-18 (per row) | local-store / store file | primary (store-captured) | none | no | C-structural-cells |

## Method

1. **S1 — anchored set:** `anchor_category: sexual-health` returns exactly **3** domains
   (bluechew, rexmd, rugiet).
2. **S2 — ED-selling set:** an ED-term grep across all `store/*/telehealth.md` returns **24**
   domains. The 18 beyond the cohort anchor to TRT (6) or GLP-1/`multi/none` (12) and list a
   sildenafil/tadalafil line without an ED front-door identity.
3. **Cohort (6):** the 3 anchored + 3 ED-as-named-franchise brands anchored elsewhere —
   hims (ED origin), keeps (ED companion to hair), ro (Roman ED origin). These three were
   added by reading their anchor_category inline justification + audience note, which name ED
   as origin/companion; the 18 straddlers were not.
4. **S3 — structural cells:** for each of the 6, the read quotes the verbatim frontmatter
   values for `pay_model`, `modality`, `compounding_posture`, `access_model`, `audience`,
   `anchor_category`. No field was re-derived from body prose (MRL-009/010 guard).

## Evidence

- S1 (3): `store/bluechew-com`, `store/rexmd-com`, `store/rugiet-com`.
- S2 (24): the 6 cohort + agelessrx, defymedical, eden-health, getopt, getpetermd,
  goodlifemeds, henrymeds, home-medvi, hydramed, invigormedical, joiandblokes, lifemd,
  malemd, marekhealth, mydrhank, struthealth, trtnation, vitalityrx.
- S3 (`pay_model`): rugiet=HSA/FSA eligible · rexmd=cash-pay only · bluechew=**unclear** ·
  hims=HSA/FSA eligible · keeps=**unclear** · ro=bills insurance. (2 of 6 unclear.)

## Limits

- The 3-tier cohort (anchored / ED-franchise / straddler) is a **hand-drawn boundary**, not a
  store field. The "ED-franchise" tier especially is a judgment call (hims/keeps/ro lead
  elsewhere today). A different operator could place ro or keeps in the straddler tier.
- The ED-term grep is a recall net, not a precision filter — it would miss an ED brand using
  only brand names (e.g. "Viagra"/"Cialis" without the molecule) and would catch incidental
  mentions. Treat 24 as a floor on store ED-sellers, not an exact count.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C-denominator | The ED-identity cohort is 6 brands (3 anchored + 3 ED-franchise) | S1, S3 | Franchise tier is a hand-drawn judgment |
| C-undercount | `anchor_category: sexual-health` grep (3) silently under-counts the ED-selling store set (24) | S1, S2 | 24 is a recall-net floor, not exact |
| C-structural-cells | Each access/identity cell is a verbatim store-captured frontmatter value | S3 | pay_model `unclear` for 2 of 6 |
