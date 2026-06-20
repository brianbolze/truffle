# Receipt - Third-party GLP-1 "best of" leaderboard panel

The bounded-live SERP/listicle named-set captured to compare against Truffle's GLP-1 cohort.

```yaml
receipt_type:          source-panel
created:               2026-06-19
evidence_mode:         bounded-live
source_grade:          secondary   # editorial listicles; affiliate/commission-disclosed
source_family:         SERP/listicle
spend_note:            paid-credit
snippet_only:          no          # S1/S2 fully scraped; S3/S4/S5 are SERP-snippet direction-finding
claim_ids_supported: [C1, C2, C3, C4, C5]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | https://health.usnews.com/best-diet/medication/top-glp-1-weight-loss-medication-providers | scraped 2026-06-19; page updated 2026-06-12 | SERP/listicle — U.S. News (high authority) | secondary | paid-credit | no | C1, C2, C3, C4 |
| S2 | https://www.forbes.com/health/weight-loss/best-affordable-online-glp1-providers/ | scraped 2026-06-19; page audited 2026-06-10 | SERP/listicle — Forbes Health (high authority, affiliate-disclosed) | secondary | paid-credit | no | C1, C2, C3 |
| S3 | https://healingmaps.com/best-glp1-telehealth-programs-2026/ | SERP snippet 2026-06-19 | SERP/listicle — low-authority affiliate | secondary | free | yes | C5 |
| S4 | https://www.vaccinealliance.org/semaglutide/cheapest-online/ | SERP snippet 2026-06-19 | SERP/listicle — low-authority affiliate | secondary | free | yes | C5 |
| S5 | firecrawl_search "best GLP-1 telehealth providers 2026 online semaglutide" (8 web results) | 2026-06-19 | SERP result set | direction-finding | paid-credit (1 net after refund) | yes | C2, C5 |
| S6 | `grep -l "anchor_category: GLP-1" store/*/telehealth.md` (19 domains) | store clock 2026-05-30…06-18 | local-store | primary (captured State) | none | no | C1, C2, C3, C4 |
| S7 | `store/{lifemd-com,altrx-com,nurx-com,hellowisp-com}` anchor_category checks | store clock | local-store | primary | none | no | C3, C4 |

## Method

1. SERP query `best GLP-1 telehealth providers 2026 online semaglutide` (S5) → ranked the candidate listicles by authority. Submitted `firecrawl_search_feedback` (refunded 1 credit).
2. Scraped the two highest-authority listicles in full: U.S. News (S1, JSON extraction of every named provider + headline price) and Forbes Health (S2, markdown; award→brand mapping recovered by locating the brand card immediately preceding each "Best …" award badge).
3. Derived the store cohort with `grep -l "anchor_category: GLP-1" store/*/telehealth.md` (S6 → 19 domains) and spot-checked four store-captured brands that offer GLP-1 but are *not* GLP-1-anchored (S7).
4. Computed set membership three ways: third-party-named ∩ store-anchored, third-party-named ∉ store, store-anchored ∉ third-party-named. Read S3/S4 as snippet-only direction-finding for cross-listicle tail divergence.

## Evidence

**S1 — U.S. News "23 Top GLP-1 … Providers in 2026" (updated 2026-06-12), 23 named:**
AltRX, Amazon On-Demand Care, BetterMe Rx, Bodybuilding Health+, **Eden**, **Found**, **Fridays**, GoodRx, **Hers**, **Ivim Health**, LifeMD, **MEDVi**, **Mochi**, MyStart Health, **Noom**, PlushCare, **Remedy Meds**, **Ro**, SkinnyRX, Sprout Health, Sunlight, TrimRx, WeightWatchers. (**bold** = present in store's 19 anchored GLP-1 brands.)

**S2 — Forbes "6 Best Affordable Online GLP-1 Providers (2026)" (audited 2026-06-10):** award→brand badges resolve to ≈ **Hims & Hers** (Best Program Overall / Best Versatile), **Remedy Meds** (Best Customer Support), **Henry Meds** (Best User Experience), **Ro** (Best Chat-Based), **Mochi** (Best for Additional Resources), **Found** (heavily featured). 5 of these 6 are store-anchored; only Mochi is absent.

**Store anchored GLP-1 cohort (S6, 19):** brellohealth, directmeds, eden-health, effecty, goodlifemeds, henrymeds, hims, home-medvi, ivimhealth, ivyrx, joinamble, joinfound, joinfridays, mydrhank, noom, remedymeds, ro, telolife, tryshed.

**S7 store-captured but not GLP-1-anchored:** lifemd-com (`multi/none`), altrx-com (no `telehealth.md` — GLP-1-led by profile but unqueryable on cohort cuts, see MRL-003), nurx-com (`multi/none`, promo bar pushes GLP-1), hellowisp-com (`multi/none`).

**Set math:**
- Third-party-named ∩ store-anchored = **9** via S1 (Eden, Found, Fridays, Hers/hims, Ivim, MEDVi, Noom, Remedy Meds, Ro) + Henry Meds via S2 = **10 distinct store-anchored brands named by an authoritative listicle**.
- Authoritative-listicle names **absent from store entirely (11; only Mochi on both listicles):** Mochi (×2), PlushCare, WeightWatchers, SkinnyRX, Amazon On-Demand Care, BetterMe Rx, Bodybuilding Health+, MyStart Health, Sprout Health, Sunlight, TrimRx — all ×1 except Mochi (GoodRx = aggregator, excluded). LifeMD + AltRX are store-captured but not GLP-1-queryable.
- Store-anchored brands **not named by either authoritative listicle (9):** brellohealth, directmeds, effecty, goodlifemeds, ivyrx, joinamble, mydrhank, telolife, tryshed (long-tail compounding brands).

## Limits

- **Affiliate/SEO confound (load-bearing).** Both S1 and S2 carry commission disclosures; listicle *inclusion and order* reflect partner relationships and SEO, not an objective market ranking. Only the *head* (Ro, Hims/Hers, Mochi, Remedy Meds, Found) is stable across the two authoritative sources; the tail diverges. S3/S4 (low-authority) name an entirely different tail (SkinnyRx, Embody, ShedRx, GobyMeds) — none on S1/S2.
- **Partial third-party panel.** Two authoritative listicles + SERP titles; not a census of "best of" pages. A wider panel would add names but, per the head-stability above, likely not change the head.
- **Mochi is the one unambiguous gap:** named by *both* authoritative listicles, absent from store.
- S3/S4/S5 are snippet-only (`snippet_only: yes`); they support only the *tail-divergence* claim (C5), not any membership conclusion.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | The store's GLP-1 cohort and the third-party "default" set overlap on ~10 mid-market compounded-GLP-1 brands (Ro, Hims/Hers, Remedy Meds, Found, Eden, Ivim, MEDVi, Noom, Fridays, Henry Meds). | S1, S2, S6 | "Default" = listicle-named, affiliate-confounded |
| C2 | 11 brands the authoritative listicles treat as default are absent from the store (excl. GoodRx aggregator); only Mochi is named by both and is the highest-priority gap — the rest are single-listicle nominees. | S1, S2, S5, S6 | Partial panel; some absentees (Amazon) are marketplaces; single-source names are weak signals |
| C3 | The store's *affordable/compounding* tier is well-covered (5 of Forbes' 6 affordable picks are store-anchored); the *big-brand/insurance* tier (Mochi, PlushCare, WeightWatchers, LifeMD) is the store's blind spot. | S2, S6, S7 | LifeMD is captured but multi/none-anchored |
| C4 | 9 store-anchored GLP-1 brands appear on neither authoritative listicle — store depth in the long-tail compounding segment exceeds "market default" coverage. | S1, S2, S6 | Absence from a listicle ≠ unimportant; ≠ low-traffic |
| C5 | The third-party named set is head-stable / tail-divergent: authoritative sources agree on the head; low-authority affiliate pages name a disjoint tail. | S1, S2, S3, S4 | S3/S4 snippet-only |
