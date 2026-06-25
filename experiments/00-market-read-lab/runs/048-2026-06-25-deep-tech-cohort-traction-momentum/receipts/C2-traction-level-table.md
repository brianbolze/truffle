# Receipt - C2 traction-level-table

The per-company capital / round / milestone level read, derived from the 8 static profiles.

```yaml
receipt_type: store-query
created: 2026-06-25
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C2]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/electra-aero/profile.md:97-100` | 2026-06-14 | owned/official (store) | secondary (self-reported) | none | no | C2 |
| S2 | `store/cfs-energy/profile.md:61,109-113` | 2026-06-14 | owned/official (store) | secondary (self-reported) | none | no | C2 |
| S3 | `store/blueenergy-co/profile.md:97-99` | 2026-06-14 | owned/official (store) | secondary (self-reported) | none | no | C2 |
| S4 | `store/evoloh-com/profile.md:96-98` | 2026-06-14 | owned/official (store) | secondary (self-reported) | none | no | C2 |
| S5 | `store/sorafuel-com/profile.md:96-97` | 2026-06-14 | owned/official (store) | secondary (self-reported) | none | no | C2 |
| S6 | `store/verdegoaero-com/profile.md:106-111` | 2026-06-14 | owned/official (store) | secondary (self-reported) | none | no | C2 |
| S7 | `store/beta-team/profile.md:119,123` | 2026-06-14 | owned/official (store) | secondary (self-reported); 10-Q is auditable | none | no | C2 |
| S8 | `store/euclidpower-com/profile.md:94-101` | 2026-06-14 | owned/official (store) | secondary (self-reported) | none | no | C2 |

## Method

Read the funding / milestone / demand prose blocks from each of the 8 cohort profiles
(`Credibility & proof` / company-history sections + `unverified_fields`). No external
source; figures are quoted verbatim from the captured profile, which quotes the company's
own site. Stage anchor is carried over from run-042's maturity read.

## Evidence

- **electra-aero** (S1): "$115 million in Series B funding" (Apr 2025); USAF SFP "up to
  $85M" (Jan 2023); "2,200 pre-orders", pipeline "valued at nearly $9 billion", ">60
  operators"; EL2 first flew Nov 11 2023; FAA Part-23 application Dec 2025.
- **cfs-energy** (S2): "over $2 billion in capital - more than any other fusion energy
  company" (cumulative, undated); 20-tesla magnet; Google 200 MW offtake + investment; Eni
  offtake ">$1 billion"; Dominion land lease.
- **blueenergy-co** (S3): "$380 million in financing" (Apr 21 2026, VXI Capital lead); GE
  Vernova "2.5 GW collaboration" (May 5 2026); NRC licensing milestone.
- **evoloh-com** (S4): "over forty million dollars ($40 million)" (cited Dec 2024); "0.5 GW"
  supply agreement (Dec 2024, non-refundable deposit) atop "16 GW of signed intent"; "500MW
  of binding orders" (Sept 2025 brochure); 3M S440 pilot operational 2027.
- **sorafuel-com** (S5): "$14.6 million round" (Apr 8 2026, Spero/Inspired co-lead); pilot
  in "18 to 24 months"; FEG offtake LoI for "first 10 million gallons" (future).
- **verdegoaero-com** (S6): **no $ figure** — investor logos only (RTX Ventures,
  DiamondStream, Seyer, Florida Opportunity Fund, Avfuel…); AFWERX contracts since 2022;
  USAF work since 2024; founded 2017.
- **beta-team** (S7): "2025 IPO raised over $1 billion", NYSE ticker "BETA", Q1 2026 10-Q
  (auditable); ">800 aircraft in the backlog"; UL-listed Charge Cubes sold; EXIM financing.
- **euclidpower-com (foil)** (S8): **no $ figure** — investor logos (Spero, Coalition, Toba,
  Designer Fund…); Thresh Power acquisition Apr 30 2026; "22 GW / 26 GW supported"
  (conflicting across pages); customer case studies.

## Limits

7/8 figures are self-reported on the company's own marketing site (secondary grade); only
beta-team's IPO size / 10-Q is independently auditable, and that is not captured as a Signal.
All figures are **levels** at a single capture (2026-06-14) — this table supports a
size/stage ordering, **not** a momentum/velocity read.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C2 | Static State carries a per-company capital/round/milestone level read sufficient for a size/stage ranking | S1–S8 | Self-reported (7/8), unit-incommensurable, single-capture levels; not deltas. |
