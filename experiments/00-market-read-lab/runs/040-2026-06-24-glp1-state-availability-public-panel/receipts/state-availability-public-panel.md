# Receipt - GLP-1 state-availability public panel

Supports the bounded-live finding that a non-gated public panel partially recovers
state-level availability — the legal/ToS surface recovers the all-50 binary, the precise
per-state list stays funnel/picker-gated.

```yaml
receipt_type: source-panel
created: 2026-06-24
evidence_mode: bounded-live
source_grade: mixed   # C1 primary; C2 primary-qualifier; C3 secondary; C4 gated/social
source_family: owned/official + SERP/listicle
spend_note: paid-credit
snippet_only: no   # C1 scraped in full; C2-C4 SERP-snippet leads
claim_ids_supported: [C1, C2, C3, C4]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | https://remedymeds.com/remedymeds/documents/terms-of-service.pdf | 2026-06-24 (doc "Last Updated 12/5/2025") | owned/official (legal PDF) | primary | paid-credit (15) | no (full scrape) | C1 |
| S2 | ivimhealth.com home + /terms-and-conditions/ + /your-first-visit-with-ivim-2/ (SERP) | 2026-06-24 | owned/official | primary (qualifier) | paid-credit (2) | yes (snippet) | C2 |
| S3 | https://www.forbes.com/health/weight-loss/henry-meds-review/ (SERP) | 2026-06-24 | SERP/listicle (3rd-party review) | secondary | paid-credit (2) | yes (snippet) | C3 |
| S4 | https://joinfound.com/insurance (SERP) + joinfoundhealth FB ad | 2026-06-24 | owned/official (picker) + ads/social | direction-finding | paid-credit (2) | yes (snippet) | C4 |
| S5 | henrymeds.com SERP (home, /legal/programs) | 2026-06-24 | owned/official | direction-finding | paid-credit (2) | yes (snippet) | C3 (brand pages don't enumerate) |

## Method

Scout-bounded panel of 5 run-038-blind brands. One SERP query per blind brand
(henry/remedy/found/ivim) via Firecrawl search; one full scrape of the single
load-bearing primary positive (remedymeds ToS PDF). hellowisp not re-probed (already the
captured exception). SERP snippets treated as leads; only S1 read in full and used for a
confident primary claim. No intake funnel entered; no state-picker operated.

## Evidence

- **C1 (remedymeds, primary):** ToS §1(e) Availability — "The Services are available in
  all fifty (50) states plus the District of Columbia. The Company is based in the United
  States." Same doc names MSO backend (OpenLoop / Rezilient / JMP / J.P. Medical PCs).
- **C2 (ivimhealth, primary qualifier):** "Not available in all states" repeated verbatim
  across home, /terms-and-conditions/, /your-first-visit-with-ivim-2/, /glp1id-hfd-a/.
  No enumerated state list on any non-gated page surfaced.
- **C3 (henrymeds, secondary):** Forbes Health review — "currently available in 40
  states, as well as Washington, D.C." with named exclusions. Brand pages
  (henrymeds.com, /legal/programs) state "one of the states we support," no list.
- **C4 (joinfound):** /insurance presents an interactive state-picker ("Select state,
  Alabama, Arizona…"); a joinfoundhealth Facebook ad claims "available in all states"
  (social, unreliable). No clean non-gated list.

## Limits

- C1 is n=1 primary positive; ToS-states-disclosure may be a remedymeds idiosyncrasy.
- C2/C3/C4 are SERP-snippet leads (not full scrapes) — C2's negative qualifier is
  low-risk; C3 is third-party secondary; C4 is gated/social, used only as direction.
- The precise per-state list for partial-coverage brands was NOT obtained from any
  non-gated public surface — funnel/picker only (disallowed to enter).
- **Spend breach:** the S1 PDF parse cost 15 credits (15 pp); total run spend ~23 paid
  credits against a 10-credit ceiling. See run-notes R1 + Loop 1 exit check (failed).

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | remedymeds operates in all 50 states + DC | S1 | brand-owned ToS, primary; binary only, not a per-state operational nuance |
| C2 | ivimhealth is NOT in all states; no public list | S2 | primary qualifier; snippet-grade; absence = "not found," not "not there" |
| C3 | henrymeds ≈40 states + DC | S3 | secondary (Forbes); no brand-owned enumeration found |
| C4 | joinfound state list is picker/funnel-gated | S4 | non-gated surface is an interactive picker; FB "all states" is social/unreliable |
