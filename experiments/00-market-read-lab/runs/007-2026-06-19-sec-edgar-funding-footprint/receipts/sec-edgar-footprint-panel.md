# Receipt - SEC EDGAR funding-footprint panel

Derived panel of the 20 captured `sec_edgar` signals, classified by match quality and joined to
store role/category — supports the read's bucket split, the Niagen dedup, and the existence-only caveat.

```yaml
receipt_type:          store-query
created:               2026-06-19
evidence_mode:         store-only
source_grade:          derived
snippet_only:          no
claim_ids_supported: [C1, C2, C3, C4, C5, C6]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source type | Grade | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|
| S1 | `store/*/signals/sec_edgar/<latest>.json` (20 domains, 24 raw files) | 2026-06-15 (19), 2026-06-18 (waldo) | store file (captured SEC signal) | derived | no | C1–C6 |
| S2 | `store/*/telehealth.md` frontmatter (`value_chain_role`, `anchor_category`) | 2026-05/06 store clock | store file | derived | no | join only |

## Method

Globbed `store/*/signals/sec_edgar/*.json`; kept the lexically-last file per domain (ISO-Z names =
chronological; also matches `captured_at`). For each: read `state.is_public/cik/registered_name`,
`form_d.{match,total_hits,distinct_ciks,candidates[].is_vehicle}`, `filings[].{form,date}`, and
`funding_signals[].{amount,flags}`. Joined `value_chain_role`/`anchor_category` from each domain's
`telehealth.md` (1:1, no `store.py` needed). No live SEC fetch; no `store/` write.

## Evidence

**Match-quality split (20 captured):** 6 `confirmed`, 1 `no_issuer_form_d` (hims), 3
`name_match_unconfirmed`, 10 `no_match`. *(C1)*

**Confirmed / public issuers:**

| Domain(s) | CIK | Public? | Forms | Filing dates | Note |
|---|---|---|---|---|---|
| niagenplus-com **+** truniagen-com | 0001386570 | yes | 10-K,10-Q,8-K | 2025-11-04 → 2026-05-06 (≥10, capped) | **One issuer behind two brand domains** — `registered_name` "Niagen Bioscience, Inc.", filer string "ChromaDex Corp. (CDXC)" (ChromaDex → Niagen Bioscience rename; public, ticker CDXC) (C2,C3) |
| hims-com | …3751 | yes | 10-K,10-Q,8-K | 2025-11-17 → 2026-06-02 (≥10, capped) | `no_issuer_form_d` — public-market raiser, correct (C3) |
| eden-health | 0001721728 | no | D ×3 | 2017-11-27, 2018-12-28, 2021-02-19 | only serial private filer (C4) |
| mylifeforce-com | 0001911639 | no | D | 2022-02-17 | "Lifeforce Digital Inc." (C4) |
| agelessrx-com | 0002109810 | no | D | 2026-03-17 | (C4) |
| waldo-fyi | 0002137951 | no | D | 2026-06-09 | "Curiosities Inc."; no telehealth pack (C4) |

**Name-collision noise (NOT funding):** maximustribe 45 hits / 19 CIKs / `is_vehicle:true`;
joinamble 34 / 10 / `is_vehicle:true`; honehealth 2 / 2 — all 0 filings attached. *(C5)*

**No footprint found (10):** defymedical, directmeds, getpetermd, gogeviti, hydramed, joinfridays,
marekhealth, sermorelin, struthealth, trtnation.

**Amount:** every `funding_signals[]` entry → `amount: null` (no raise size, universally). `flags`
vary by event: `form_d` events → `existence_only`; public `filing` events (hims, Niagen) →
`material_filing`. *(C6)*

## Limits

- Existence-only: proves a filing/match *exists*, never an amount or investor.
- Captured floor: 20 of 54 telehealth packs; the other ~34 have no SEC signal captured (≠ no filing).
- Public `filings` arrays capped at 10 → counts are floors.
- `no_match` = "no filing found under the resolved name," not "confirmed never raised."

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | 20 captured; 4-bucket match split | S1 | — |
| C2 | niagenplus + truniagen share CIK …6570 (1 issuer, 2 domains) | S1 | dedup only visible via CIK, not domain |
| C3 | hims + Niagen Bioscience are public reporters; hims correctly `no_issuer_form_d` | S1 | filing counts capped |
| C4 | 4 confirmed private Form-D issuers + dates; Eden serial | S1 | dates = entity raise, not brand age |
| C5 | 3 `name_match_unconfirmed` are collisions, not funding | S1 | high distinct_ciks + is_vehicle |
| C6 | no captured SEC signal carries an amount (all null) | S1 | amounts exist in Form-D body, not captured; `existence_only` is the Form-D flag, public filings carry `material_filing` |
