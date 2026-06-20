# Receipt - non-GLP-1 backend-counterparty derivation

Supports the cross-brand backend-recurrence and entity-resolution claims (C1–C11) of the
non-GLP-1 backend-relations read.

```yaml
receipt_type:          store-query
created:               2026-06-20
evidence_mode:         store-only
source_grade:          derived
source_family:         local-store
spend_note:            none
snippet_only:          no
claim_ids_supported: [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/*/telehealth.md` + `store/*/profile.md` (35 non-GLP-1 brands + supplier profiles) | store clock 2026-06-04 → 2026-06-18 | store file (derived query) | derived | none | no | C1–C11 |

## Method

1. **Cohort:** `grep -m1 anchor_category store/*/telehealth.md`, then **parse the value
   field, stripping the inline `#` comment** (`sed 's/.*anchor_category: *//; s/ *#.*//'`)
   before excluding `GLP-1` → 35 brands (C1). **Method caveat (Loop-2 verifier):** a naive
   `grep -v GLP-1` on the *full line* drops nurx-com and prohealth-com because "GLP-1"
   appears in their inline comment — that yields 33, not 35. The value-parse is the correct
   method; 35 is independently verified.
2. **Corporate relations:** `grep -hiE '^(parent|owns):' store/*/profile.md` over the cohort
   (C2).
3. **Pharmacy/clinical frontmatter:** `grep -hiE '^(pharmacy_model|value_chain_role):'` per
   `telehealth.md` to find the brands whose comments flag a *named* partner.
4. **Named-entity extraction:** read the Fulfillment + Clinical-entity body prose for those
   brands; record only explicitly *named* third parties (skip possessive "our pharmacy" per
   the run-001 guard).
5. **Recurrence:** `grep -rilE "<name>" store/*/telehealth.md` per entity, store-wide (not
   just the cohort), counting distinct brands (C3–C9).
6. **Resolution:** `ls -d store/*<slug>*` per named entity (C10); reverse check for captured
   suppliers no brand names (C11).

## Evidence

Store-wide brand-count per named pharmacy (telehealth.md citations):

| Pharmacy | # brands | Brands | Store profile? |
|---|---|---|---|
| Strive (Pharmacy / Compounding) | 2 | hevahealth, invigormedical | **joinable** — `strivepharmacy-com` has `profile.md` |
| Curexa | 2 | bluechew, malemd | no store entry (dangles) |
| Tailor Made (Compounding) | 2 | invigormedical, mylifeforce | no store entry (dangles) |
| Olympia (Pharmaceuticals / Pharmacy) | 2 | hydramed, invigormedical | no store entry (dangles) |
| Empower | 1 | hydramed | no store entry |
| Belmar Pharma Solutions | 1 | invigormedical | **captured, not joinable** — `belmarpharmasolutions-com` has `captures/` only, **no `profile.md`** |
| Precision Pharmacy | 1 | mylifeforce | no store entry |
| Valiant / Casa Pharma / Meds Health LLC / National Treatment Delivery LLC / Stryker | 1 each | hydramed / hydramed / bluechew / bluechew / hevahealth | no store entry |

Three join-readiness tiers (Loop-2 verifier refinement): **joinable** (`profile.md`) =
`strivepharmacy-com`, `hallandalerx-com`; **captured-but-no-profile** =
`belmarpharmasolutions-com`; **no store entry** = all others above.

Clinical: Beluga Health → prohealth only (singleton, C8). No OpenLoop/SteadyMD/Wheel/Curai
outside GLP-1; OpenLoop citers home-medvi + joinfridays are both GLP-1 (C9).
Reverse dangle: `hallandalerx-com` (503A compounder, `profile.md` in store) cited by 0
brands (C11).

## Limits

- Cannot prove a name variant ("Olympia Pharmaceuticals" vs "Olympia Pharmacy") is one
  entity — inferred, not adjudicated (C6).
- Counts are **floors**: owned-page self-report; anchored-only denominator; unnamed partner
  pharmacies are common and invisible here.
- 2-brand co-occurrence is a recurrence *lead*, not concentration — no market-structure claim
  is drawn from it.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C3/C7/C10 | Strive recurs across 2 non-GLP-1 brands and resolves to a store profile | S1 | floor; owned-page self-report |
| C4/C5/C6 | Curexa, Tailor Made, Olympia each recur across 2 brands but dangle | S1 | name-variant for Olympia inferred |
| C8/C9 | No shared clinical network outside GLP-1; Beluga singleton | S1 | absence = not found, not "none exists" |
| C11 | Captured supplier (hallandalerx) cited by no brand | S1 | join fails from both directions |
