# Receipt C1 — Services / Consulting denominator + telehealth/non-telehealth split

- **Local path:** `store/*/profile.md` frontmatter (`offering_category`, `entity_type`)
- **Store clock:** per-profile `captured_at` (varies; no live evidence)
- **Source type:** local store frontmatter
- **Source grade:** primary (the store's own captured State)
- **Source family:** store-only
- **Spend note:** none
- **Snippet-only:** no
- **Claim IDs supported:** C1, C2 (read.md)

## Method

Iterated all 145 `store/*/profile.md`. Extracted the **first** element of the
`offering_category` array as the *primary* token (stripping inline `# ...` comments and
quoting). Counted profiles where the primary token is `Services / Consulting`. Then split
those by whether `Biotech / Pharma Products` appears anywhere in the same array.

## Findings

- **Primary `Services / Consulting`:** 61 of 145.
- **Of those 61:** 52 carry a `Biotech / Pharma Products` secondary (DTC telehealth
  care-wrapper convention); 9 do not (genuine professional / B2B services).
- **`Services / Consulting` anywhere in array:** ~82 of 145.
- **Raw exact-token frequency (a different count):** 73 — diverges from 82 because inline
  `# STRAIN`/qualifier comments on the token line break naïve exact-string matching. The
  denominator is method-sensitive (L004); the number you get depends on primary-only vs
  anywhere vs exact-token-frequency counting.

## The 9 non-telehealth primaries (the discriminating set)

| Domain | entity_type | Sub-shape |
|---|---|---|
| bullish-co | Company | creative + capital + consulting hybrid agency |
| heco-partners | Company | creative consultancy (branding/web) |
| ideo-com | Company | global design & innovation consultancy |
| parlance-cc | Company | one-person brand studio/consultancy |
| redantler-com | Company | brand-building agency |
| lsvp-com | Investor / Holding | multi-stage venture capital firm |
| openloophealth-com | Company | B2B white-label telehealth infrastructure |
| onemedical-com | Company | membership primary care (Amazon-owned) |
| euclidpower-com | Company | renewable-energy project execution services + software |

Secondary-token holders (not in the 61) add more shapes: SaaS-led (alpha-sense,
usertesting, goinfusive, mdintegrations, noom), pharma/compounding-led (anazaohealth,
hallandalerx, hellopepti, niagenplus, strivepharmacy), hardware-makers with a service
line (warbyparker, therabody, beta-team), legal-doc software (clerky), marketplace
(sesamecare), more VC (firstround, sequoiacap).
