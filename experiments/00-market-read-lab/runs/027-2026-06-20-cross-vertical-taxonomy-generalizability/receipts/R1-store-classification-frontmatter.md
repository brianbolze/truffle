# Receipt - R1 store classification frontmatter

Supports the whole read: the classification-field behavior of the non-telehealth slice,
derived entirely from `store/*/profile.md` frontmatter and the two contract docs.

```yaml
receipt_type: store-query
created: 2026-06-20
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4, C5, C6]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/*/profile.md` (frontmatter: entity_type, offering_category, business_model, portfolio_shape, primary_industry + inline `# STRAIN` comments) | per-profile `captured_at` (2026-05/06 era) | store file | derived | none | no | C1–C6 |
| S2 | `TAXONOMIES.md`, `SCHEMA.md` | repo HEAD 2026-06-20 | local-store / contract | primary | none | no | C4, C5 |

## Method

- Roster: looped `store/*/`, read `primary_industry` from each `profile.md`; bucketed
  Healthcare vs non-Healthcare. Cross-checked entity_type store-wide
  (`grep ^entity_type:` → 119 `Company`, 7 `Investor / Holding`; 126 profiled rows).
- Strain inventory: `grep -rn "STRAIN" store/*/profile.md` (full store), then partitioned
  markers into classification-field strains vs brand/logo/design capture-fidelity strains.
- Investor/Holding deep read: pulled the 5 classification fields for all 7
  `Investor / Holding` firms + a Finance-industry control set (stripe, runway).
- Clean-carry confirmation: pulled the same 5 fields for the 7 watch brands and a 6-row
  Tech/SaaS sample.
- `Other` census: `grep "business_model: Other"` and category-field `Other` store-wide
  → 1 hit (blueowl).
- Stub detection: the 9 empty-`primary_industry` rows resolved to dirs with `captures/`
  but no `profile.md` (`ls store/<dir>/`).

## Evidence

- **entity_type store-wide:** 119 `Company`, 7 `Investor / Holding`. Profiled N = 126;
  store dirs = 135 → 9 capture-only stubs.
- **Investor/Holding offering_category (7 firms):** `[]` ×3 (spero, thrivecap,
  standishspring); `[Financial, Services]` ×2 (firstround, sequoia); `[Financial]` ×1
  (blueowl); `[Services]` ×1 (lsvp). Gating rule ("leave empty") honored 3/7.
- **business_model `Other`:** exactly 1 store-wide — blueowl
  (`# management + performance/incentive fees on AUM; no taxonomy value fits`).
- **Watches (7):** all `[Physical Products / Hardware]` + `Transactional / One-time`;
  industry `Consumer Goods` ×6, `Technology` ×1 (casio); portfolio_shape `Catalog` ×5,
  `Flagship + companions` ×1 (AP), `Multi-product` ×1 (A. Lange).
- **SaaS sample (6):** all `[Software / SaaS]` (snowflake adds `Marketplace / Platform`);
  business_model `Usage-based / Consumption` ×3 (datadog, aws, snowflake) vs
  `Subscription` ×3 (linear, notion, openai); portfolio_shape spread Single→Catalog.
- **9 stubs:** belmarpharmasolutions, ddpmedical, dewittpharma, exaveyra, mdpep,
  medsupplysolutions, norexi, pfizerpro, stemnova — `captures/` only, no `profile.md`.

## Limits

- The Tech/SaaS rows are an illustrative sample, not a full enumeration; the headline
  *counts* (7 investors, 7 watches, 9 stubs, 1 `Other`) are complete store-wide
  enumerations.
- A profile's classification reflects the capturing agent's call at capture time; this
  receipt audits *consistency of encoding*, not whether each individual call is the
  single best fit.
- store-only: says nothing about market completeness — only about how the schema behaves
  on what was captured.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | 126 profiled cos (119 Company / 7 Investor-Holding); ~54 non-Healthcare operators | S1 | "non-telehealth slice" sized by primary_industry bucket |
| C2 | Watch slice classifies uniformly + correctly | S1 | casio industry = Technology (defensible) |
| C3 | SaaS slice classifies cleanly, well-differentiated | S1 | 6-row sample, illustrative |
| C4 | 7 Investor/Holding → 4 offering_category encodings; gating rule 3/7 | S1, S2 | the core break |
| C5 | `business_model: Other` = blueowl only, store-wide | S1, S2 | AUM fee economics |
| C6 | 9 capture-only stubs lack profile.md → profiled N=126 not 135 | S1 | denominator caveat (MRL-001 flavor) |
