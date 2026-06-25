# Receipt - deep-tech slice denominator

Defines which captured profiles form the pre-revenue deep-tech cohort and which are foils.

```yaml
receipt_type: store-query
created: 2026-06-24
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/{electra-aero,verdegoaero-com,blueenergy-co,cfs-energy,euclidpower-com,evoloh-com,sorafuel-com,beta-team}/profile.md` | all captured_at 2026-06-14 | store file (owned/official capture) | primary (for what each site states) | none | no | C1 |
| S2 | `grep "^primary_industry:" store/*/profile.md` | store snapshot 2026-06-24 | local-store derived | derived | none | no | C1 |

## Method

Scout named the candidate slice. Confirmed each profile's `description` + body to classify
pre-revenue deep-tech (hardware/energy company whose flagship is not yet generating
commercial revenue) vs operating foil. Cross-checked `primary_industry` to show the slice is
not recoverable from a single industry value.

## Evidence

- Pre-revenue deep-tech (n=7): electra-aero, verdegoaero-com, blueenergy-co, cfs-energy,
  evoloh-com, sorafuel-com, beta-team.
- Operating foil (in-slice by industry, not pre-revenue): **euclidpower-com** — renewable-energy
  services + SaaS, "22 GW supported / 1,100+ projects" (homepage), Thresh Power acquisition
  2026-04-30 — a commercially operating firm, not an "is it real yet" case.
- Excluded foils named by the Scout contract: ford-com, uber-com (mature operating cos).
- `primary_industry` scatter for the 8: Automotive & Mobility (electra) · Manufacturing &
  Industrial (verdego, beta) · Energy & Utilities (blueenergy, cfs, euclid, evoloh, sorafuel).

## Limits

The slice is a **known-partial, capture-biased** set (whatever deep-tech happens to be in
the store), not a census of the deep-tech market. Cannot support any "N deep-tech companies
do X" completeness claim. "Pre-revenue" is read from each site's own disclosures (no audited
financials captured), so it reflects what the site attests, not verified revenue status.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | The captured deep-tech cohort is 7 pre-revenue cos + 1 operating-services foil (euclid); an industry/category draw does not recover it | S1, S2 | Partial slice; "pre-revenue" is site-attested, not audited |
