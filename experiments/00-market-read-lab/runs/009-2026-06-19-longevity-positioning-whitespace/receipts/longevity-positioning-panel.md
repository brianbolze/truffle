# Receipt - Longevity/NAD positioning & proof panel

Supports the per-brand positioning read, the supply↔diagnostic axis assignment, and the
Schedule-III-behind-the-longevity-banner tell.

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
| S1 | `store/truniagen-com/telehealth.md` + `profile.md` | 2026-06-16 | store file | primary | no | C1, C2 |
| S2 | `store/niagenplus-com/telehealth.md` | 2026-06-04 | store file | primary | no | C1, C2 |
| S3 | `store/prohealth-com/telehealth.md` | 2026-06-07 | store file | primary | no | C1, C2 |
| S4 | `store/agelessrx-com/telehealth.md` + `profile.md` | 2026-05-31 | store file | primary | no | C1, C2 |
| S5 | `store/gethealthspan-com/telehealth.md` + `profile.md` | 2026-06-04 | store file | primary | no | C1, C2, C3 |
| S6 | `store/mylifeforce-com/telehealth.md` + `offerings.md` | 2026-06-04 | store file | primary | no | C1, C2, C3 |
| S7 | `store/honehealth-com/telehealth.md` + `profile.md` | 2026-06-18 | store file | primary | no | C1, C2, C3 |
| S8 | `store/gogeviti-com/telehealth.md` | 2026-06-04 | store file | primary | no | C1, C2, C3 |
| S9 | `store/getopt-com/telehealth.md` (straddler) | (per file) | store file | primary | no | C3 |

## Method

1. Derived the cohort by grepping `store/*/telehealth.md` frontmatter for
   `anchor_category: longevity/NAD` → 8 brands (S1–S8). getopt (S9) surfaced as a
   `TRT`-anchored straddler with a longevity front door and is scored separately, not in the core 8.
2. For each brand, read the `telehealth.md` frontmatter (`anchor_category`, `access_model`,
   `compounding_posture`), the `## Credibility & access` block (named clinicians, labs posture,
   controlled-substance Rx), and the `## Notes` positioning read; pulled the verbatim hero/positioning
   line and the lead proof device. Cross-checked hero/proof against `profile.md` / `offerings.md` where
   the telehealth note pointed to them.
3. Placed each brand on a **supply-access ↔ diagnostic-first** axis (C2) from two captured signals:
   whether a biomarker panel is a *required* front-door step (`Labs: required-step` vs `none/optional`)
   and whether access is **membership-required** vs **à-la-carte/per-visit**.
4. Flagged the **Schedule-III** tell (C3) from each `## Credibility & access` "Controlled-substance Rx"
   line: which "longevity" brands sell page-attested testosterone/HRT.

## Evidence

**Axis placement (C2) — required-labs + access model:**

| Brand | Labs (captured) | Access (captured) | Pole |
|---|---|---|---|
| truniagen | none | à-la-carte/Subscribe&Save | supply (OTC) |
| niagenplus | none | per-visit ($299 one-time) | supply (Rx) |
| prohealth | optional | à-la-carte/Subscribe&Save | supply (+Rx arm) |
| agelessrx | per-Rx | à-la-carte, no membership | catalog-under-banner |
| gethealthspan | optional (incl. in protocols) | à-la-carte/both; HRT/GLP-1/TRT need membership $99–129 | diagnostic-first (by positioning) |
| mylifeforce | required-step | membership $149 | diagnostic-first |
| honehealth | required-step | membership $25/$155 | diagnostic-first |
| gogeviti | required-step (Plus) | membership-required | diagnostic-first |

**Schedule-III-behind-longevity-banner (C3) — verbatim from "Controlled-substance Rx" lines:**
- gethealthspan: *"offers Schedule-III (testosterone) … both men's TRT 'delivered through Membership.'"*
- mylifeforce: *"offers Schedule-III (testosterone) — … injectable testosterone cypionate, bio-identical testosterone cream, and Kyzatrex® oral testosterone SKUs."*
- honehealth: *"offers Schedule-III (testosterone injections/cream/troches — TRT)"* — flagship treatment line.
- gogeviti: *"offers Schedule-III (testosterone/HRT) … the gender-neutral HRT line and 'Enclomiphene Citrate'"* (app-walled).
- getopt (straddler): front door = longevity/optimization membership; *"most-foregrounded specific vertical is TRT."*
- **Supply pole carries no scheduled Rx:** truniagen / niagenplus / prohealth all
  *"non-scheduled only … no TRT/testosterone SKU."* agelessrx likewise *"non-scheduled only — no testosterone/TRT SKU."*

**Lead proof devices (C1):** science pedigree (truniagen: Nobel laureates + Brenner); single-molecule Rx
access (niagenplus: $299 kit); heritage (prohealth: BBB A+ 35 yrs); research identity (agelessrx: XPRIZE
semi-finalist, "70,000+ NAD+ users"); named MD/PhD board + "12K patients" (gethealthspan); "largest program"
+ 50+ biomarker diagnostic (mylifeforce); $65 biomarker entry + Trustpilot 4.8/11,677 (honehealth); 100+
biomarker body-mapping (gogeviti).

## Limits

- **Partial cohort, not a census.** The 8 are the store's current `longevity/NAD`-anchored population;
  uncaptured longevity brands (Novos, Tally Health, Modern Age, etc.) are out of frame.
- **Point-in-time heroes.** agelessrx (coupon instrumentation) and honehealth (Optimizely A/B live) heroes
  are captured-floor snapshots; positioning *labels* are stable but exact hero copy may flicker.
- **gogeviti Rx grain is inferred from page-attested catalog references**, not a PDP (app-walled).
- The axis placement and pole labels are a **derived [J] reading** of captured State, not a store field.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | Per-brand positioning + lead proof device | S1–S8 | Heroes point-in-time for S4/S7 |
| C2 | Brands sort on a supply-access ↔ diagnostic-first axis (required-labs + access model) | S1–S8 | Derived label, not a store field; partial cohort |
| C3 | **All four (4/4)** diagnostic-first "longevity" brands sell Schedule-III testosterone/HRT; supply pole sells none | S5–S9 | gogeviti app-walled; absence on supply pole = "no SKU captured", not proof of policy |

**Loop 2 correction (2026-06-19):** an adversarial evidence verifier caught two field-read errors, both
corrected above and in `read.md`: (1) the narrative said "three of four" diagnostic-first brands carry
Schedule-III testosterone — the correct count is **four of four** (gogeviti was already in the evidence
table); the correction *strengthens* C3. (2) gethealthspan's row overstated access/labs as
"required/membership" — store frontmatter is `access_model: à-la-carte/both` + `Labs: optional` (only
HRT/GLP-1/TRT are membership-gated); the Diagnostic-first label holds by **positioning**, not by access.
