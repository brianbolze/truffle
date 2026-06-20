# Receipt - proof-device-sweep

Supports the cohort-wide proof-device tallies and the by-category device join: that the
`telehealth.md` pack already carries a standardized credibility checklist, and how the four
device families distribute (C1–C5).

```yaml
receipt_type: store-query
created: 2026-06-20
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4, C5]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/*/telehealth.md` — "Health-merchant credibility" + "Payment & commitment" lines across all 56 cohort packs | per-pack `captured_at` ~2026-05-30 → 2026-06-20 | local-store / cohort-pack | derived (from owned/official capture) | none | no | C1, C2, C3, C4, C5 |

## Method

1. Denominator: `find store -name telehealth.md` → 56 packs. `grep -rl "Credibility"` → 54
   carry the literal cut; 2 phrase it differently (read by hand).
2. Device-marker frequency: for each marker (LegitScript, PCAB, ACHC, NABP, 503A, 503B,
   board-certified, money-back, guarantee, FDA-approved, cancel anytime, CLIA) counted packs
   matching, case-insensitive.
3. Positive-vs-negated classification: separated "LegitScript-certified … (y)" from
   "no LegitScript" / "not shown (n)"; same for named clinicians (`yes`/MD/Dr. vs
   `not shown`/`(n)`/`no /physicians`) and accreditation (`shown on` / `NABP, PCAB` vs
   `not shown` / `N/A`).
4. By-category join: per domain, extracted `anchor_category` (frontmatter) + LegitScript flag
   + named-clinician flag into a TSV, sorted by category.

All steps are read-only greps over already-captured local files. No fetch, no Firecrawl, no
`store/` mutation.

## Evidence

Marker frequency (packs matched, /56):

```
54  LegitScript      53  503A      50  503B      47  PCAB      47  NABP      42  ACHC
26  FDA-approved     24  cancel anytime     13  board-certified
 8  FDA-registered    6  guarantee     6  CLIA     5  money-back
```

Positive vs negated **(corrected by Loop 2 re-derivation; first-pass figures had a
positive/negated polarity error — "…not shown / not observed" lines were miscounted positive)**:
- LegitScript: **~33/54 positive** ("-certified", seal→legitscript.com); ~21 absent / N-A.
  Absent set (corrected, full): genuine N/A — truniagen, prohealth (supplement), onemedical
  (insurance), functionhealth (non-pharmacy); not-shown-on-captured-pages — defymedical,
  gethealthspan, hellopepti, ivimhealth, joinfridays, lifemd, nurx, getopt, gogeviti,
  goodlifemeds, joinamble, keeps, kingsbergmedical, niagenplus, struthealth, vitalityrx.
- Named clinicians: **~38 shown / ~16 not-shown** (corrected from ~29/~25).
- Pharmacy accreditation (PCAB/ACHC/NABP): **~6 positively shown** (eden-health, struthealth,
  hydramed, gethealthspan, mylifeforce, innerbalance); ~38 explicitly "not shown."
  *(defymedical, brellohealth, maximustribe, ro-co were wrongly listed positive on the first
  pass — their packs read "not shown.")*
- Commercial-trust: ~28 cancel-anytime; ~5 money-back/outcome guarantee (innerbalance 6-mo,
  sermorelin 180-day, prohealth 100-day supplement refund, tryshed outcome guarantee, vitalityrx
  generic). The first-pass "struthealth 180-day" was a **ghost citation** — struthealth's pack
  has only a cancel/pause clause, no refund language — removed.

By-category LegitScript (shown/absent), corrected from the domain join:
- GLP-1 (19): ~14 shown / 5 absent (brellohealth, goodlifemeds, joinamble, joinfridays, ivimhealth)
- TRT (8): ~5 / 3 absent (defymedical, getopt, vitalityrx)
- longevity/NAD (9): ~6 / 3 absent (gogeviti, prohealth N/A, truniagen N/A)
- multi/none (11): ~9–10 / 1–2 absent (kingsbergmedical, nurx)
- sexual-health (3): shown · peptides (2): shown · onemedical (primary-care): absent (N/A) ·
  keeps (hair): absent · functionhealth (labs): N/A non-pharmacy

Named-clinician skew (illustrative): shown in TRT/longevity/peptides (defymedical, getpetermd,
maximustribe, gethealthspan, niagenplus, sermorelin, hellopepti); not-shown in commodity GLP-1
(directmeds, henrymeds, remedymeds, telolife, ivyrx, home-medvi).

## Limits

- Counts are **prose-grep classifications**. The first pass treated the error as ±2–3, but Loop 2
  found a **systematic polarity error** (negated "not shown / not observed" lines miscounted as
  positive) worth up to ~9 on three tallies; figures above are the corrected re-derivation. The
  *pattern* (LegitScript majority floor, accreditation rare, clinicians model-dependent) was
  independently confirmed; read the integers as "majority / minority / rare," not exact.
- Every count is **device-presence on captured pages**. It proves what a brand *surfaces*, not
  whether the claim is true, and "not shown" is "not found on captured pages," never "absent."
- Capture dates differ across the cohort; a seal could change between a pack's capture and now.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | 56-pack cohort denominator; 54 carry the explicit credibility cut; category distribution | S1 | 2 packs phrased differently; selection-bias caveat (MRL-001) applies to the cohort itself |
| C2 | LegitScript surfaced on ~33/54 (~61%); absence splits N/A vs not-shown-on-captured-pages | S1 | corrected from ~42/56 (Loop 2 polarity fix); split grep-classified |
| C3 | Pharmacy accreditation (PCAB/ACHC/NABP) least-surfaced; ~6 positive, ~38/54 "not shown" | S1 | positive set corrected (4 brands moved to "not shown"); "not shown" ≠ absent |
| C4 | Named clinicians ~38 shown / ~16 not-shown; not-shown set tracks model | S1 | corrected from ~29/~25; model attribution labelled Judgment in read |
| C5 | ~28 cancel-anytime; ~5 money-back/outcome guarantee | S1 | "struthealth 180-day" ghost citation removed; most "guarantees" are plan-adjustment |
