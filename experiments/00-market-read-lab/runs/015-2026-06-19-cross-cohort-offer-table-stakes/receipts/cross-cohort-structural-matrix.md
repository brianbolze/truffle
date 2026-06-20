# Receipt - cross-cohort structural matrix

Supports the cross-cohort table-stakes read: per-cohort distributions of the load-bearing
`telehealth.md` structural fields across 54 brands.

```yaml
receipt_type:          store-query
created:               2026-06-19
evidence_mode:         store-only
source_grade:          derived
source_family:         local-store
spend_note:            none
snippet_only:          no
claim_ids_supported: [C1, C2, C3, C4, C5]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/*/telehealth.md` frontmatter (54 files) | captured 2026-06-04 → 2026-06-18 | store file | derived (from primary store State) | none | no | C1, C2, C3, C4, C5 |

## Method

```python
# For each store/*/telehealth.md, parse the YAML frontmatter block and extract
# anchor_category, pay_model, access_model, compounding_posture, modality, audience
# (regex on the first ---...--- block, stripping trailing # comments).
# Group rows by anchor_category; tabulate value distributions per cohort.
# 54 files carried the full structured field set.
```

Cohort claims made only for `anchor_category` groups with n ≥ 3 (GLP-1 19, multi/none 10,
longevity/NAD 8, TRT 8, sexual-health 3). peptides (n=2) and singletons (labs, womens-HRT,
hair, primary-care) reported as too thin.

## Evidence

**pay_model (all 54):** HSA/FSA eligible 31, cash-pay only 11, unclear 7, bills insurance 5.
- bills insurance (C1): `joinfound-com, lifemd-com, nurx-com, onemedical-com, ro-co`.

**compounding_posture (all 54):** both 38, compounded-only 12, FDA-brand-only 2, OTC 1, N/A 1.
- FDA-brand-only (C2): `nurx-com, onemedical-com`.
- compounded-only by cohort: GLP-1 4 (`brellohealth, directmeds, mydrhank, telolife`),
  TRT 2 (`maximustribe, vitalityrx`), longevity 2 (`gogeviti, niagenplus`),
  sexual-health 1 (`bluechew`), multi/none 1 (`hydramed`).

**modality (C3):** GLP-1 async 12 / hybrid 5 / sync 2; **TRT async 0 / hybrid 2 / sync 6**;
longevity hybrid 3 / async 3 / sync 1 / N/A 1; sexual-health hybrid 2 / async 1;
multi/none async 6 / hybrid 4.

**access_model (C4):** GLP-1 all-in 12 / membership 4 / à-la-carte 3; TRT à-la-carte 3 /
membership 3 / all-in 2; longevity à-la-carte 4 / membership 3 / per-visit 1; sexual-health
all-in 3; multi/none à-la-carte 7 / all-in 2 / membership 1.

**audience (C5):** GLP-1 all-genders 14 / women-first 2 / women-only 1 / men-only 1 /
men-first 1; TRT men-first 6 / all-genders 1 / men-only 1; longevity all-genders 8;
sexual-health men-only 3; multi/none all-genders 8 / men-only 1 / women-only 1.

**Cross-axis overlap:** `nurx-com` and `onemedical-com` appear in BOTH the bills-insurance
set (C1) and the FDA-brand-only set (C2) — the "real clinic" outliers on both agnostic axes.

## Limits

- **Anchored-only denominator (MRL-001):** each cohort's n is the `anchor_category`-grep
  set; generalists selling into a cohort without anchoring fall only under `multi/none`.
  Cohort-specific n's are floors; the cohort-agnostic claims (C1/C2) are if anything
  strengthened by the excluded generalists.
- **`pay_model: unclear` 7/54** — cash-pay claim is "not stated otherwise," reported as a
  captured value, not absence.
- Field-only read: does NOT cover price-publication (per-SKU `offerings.md` Visibility
  column, deliberately out of scope this run — see read.md C6).
- 81 of 135 store companies lack structured `telehealth.md` and are not in this matrix.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | Cash-pay is the cross-cohort rail; only 5/54 bill insurance | S1 | anchored-only denominator; `unclear` 7/54 |
| C2 | Compounding-capable is table-stakes; FDA-brand-only 2/54 | S1 | `compounded-only` clusters in GLP-1 |
| C3 | Modality is cohort-determined (TRT 6/8 sync vs GLP-1 12/19 async) | S1 | cohort n's are floors |
| C4 | Bundling/membership wedge is cohort-shaped (GLP-1 all-in) | S1 | mixed within longevity/multi |
| C5 | Audience restates the condition | S1 | singleton cohorts excluded |
