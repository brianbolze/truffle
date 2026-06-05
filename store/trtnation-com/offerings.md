---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: trtnation.com       # company key; each offering's slug is its key *within* TRT Nation
captured_at: 2026-06-04     # own freshness; captures/2026-06-04/ holds the source pages
site_notes: "No per-SKU PDPs — every product is an inline CARD on its category page (/testosterone-therapy/, /weight-loss-therapy/, /anti-aging/, /sexual-health/); 'Select' routes to the /trtlw/ /wllw/ /aalw/ /shlw/ funnels (no per-product URL). So slugs are category-page-keyed + '(no PDP — card)'. Prices sit ON the category page (no intake wall) → cheap to roster, ~1 scrape per line. /popular-treatments/ is a POPULAR SUBSET — the dedicated category pages are complete (Tesamorelin + IGF1-LR3 appear only on /anti-aging/). Clean isolated product renders at wp-content/uploads/.../<Name>-Product.png, one per SKU (1024×1024). No A/B instrumentation seen, but card sets/prices can change — re-check next run."
---

## Portfolio overview

TRT Nation is **Multi-product**: four distinct, separately-positioned therapy lines — **Testosterone, Weight
Loss, Sexual Health, Anti-Aging** — plus an à-la-carte **Labs** line, 16 buyable SKUs in all. The defining shape
finding for this cohort is **radical price transparency**: every SKU shows a flat verbatim price *on the category
page itself* (no quiz/intake wall, no membership stacked on top), so the entire roster is `published` — the rare
all-`published` telehealth file. The catch lives in footnotes, not gates: most lines carry a **minimum-purchase
commitment** (2.5 months on testosterone/HCG/NAD+, 3 months on tirzepatide/tesamorelin) — a term, not a hidden
fee, so it doesn't downgrade visibility. Two molecules are **cross-listed** across lines (Enclomiphene under both
Testosterone and Sexual Health; HCG standalone in Sexual Health *and* bundled as TRT + HCG) — listed once each
with the cross-reference noted.

**Visibility rule (stated once, applied to every row).** `published` = the displayed `$X/mo` is the complete,
self-contained medication price you subscribe at — no mandatory membership, no separate platform fee (TRT Nation
markets "no hidden fees and no restrictive monthly subscriptions"). Labs are a *separate, often-required*
diagnostic ($129/$179) but can be satisfied **bring-your-own** (outside bloodwork up to ~120 days accepted), so
they're rostered as their own Labs line rather than making each med `partial`. No SKU is `on-request` — nothing is
price-hidden behind the intake.

**Prominence (calibrated).**
- **Testosterone is the flagship [HIGH]** — the brand namesake, the homepage hero ("#1 IN THE NATION," "$99/mo"),
  the first nav item, and the first tile in the "full treatment lineup."
- **Weight Loss is the strong #2 [HIGH]** — the second homepage hero slot ("MOST AFFORDABLE… Any dose same price,
  $219/mo") and a co-equal nav item.
- **Sexual Health + Anti-Aging are companions [MED]** — full nav items and dedicated pages, but secondary in hero
  emphasis; Labs is positioned as a cross-cutting enabler ("BRING YOUR OWN LABS").
- TRT Nation does **not** badge individual SKUs ("Best seller" etc.) — emphasis is category-level hero copy only.

## Roster

Complete at the indexed level (TRT Nation's product cards) across all five lines. Price quoted verbatim with its
on-page footnote markers; molecule/form page-attested from the card heading + copy (never inferred from a brand
name — see the molecule audit under Verbatim anchors). Slugs are category-page-keyed (`(no PDP — card)`) because
no per-product URL exists. A slug here is never asserted equal to another brand's.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Testosterone Therapy** | family | — | `/testosterone-therapy/` | — | — | Flagship hormone line — injectable T + oral alternatives + combos. |
| Testosterone | buyable | Testosterone Therapy | `/testosterone-therapy/ (no PDP — card)` | **$99.99/mo** | published | testosterone · injectable · "2.5 months minimum purchase," CA pricing may vary. Render label: "Testosterone Cypionate 10ml." |
| Enclomiphene | buyable | Testosterone Therapy | `/testosterone-therapy/ (no PDP — card)` | **$99.99/mo** | published | enclomiphene · oral (30ct · 25mg capsules) · 30-day supply; "preserves fertility." Cross-listed under Sexual Health. |
| TRT + HCG | buyable | Testosterone Therapy | `/testosterone-therapy/ (no PDP — card)` | **$180/mo** | published | testosterone + HCG · injectable combo · "2.5 months minimum"; maintains testicular function/fertility. |
| **Weight Loss Therapy** | family | — | `/weight-loss-therapy/` | — | — | GLP-1/GIP + oral appetite-suppressant line. |
| Tirzepatide | buyable | Weight Loss Therapy | `/weight-loss-therapy/ (no PDP — card)` | **$219/mo** | published | tirzepatide · injectable (compounded) · "any dose same price," "3 months minimum." Render label: "Compounding Injection 2.5mg." |
| Phentermine | buyable | Weight Loss Therapy | `/weight-loss-therapy/ (no PDP — card)` | **$99.99/mo** | published | phentermine · oral (30ct · 37.5mg tablets) · 30-day supply. |
| **Sexual Health Therapy** | family | — | `/sexual-health/` | — | — | ED + libido line (PDE5 inhibitors + hormone support). |
| Tadalafil | buyable | Sexual Health Therapy | `/sexual-health/ (no PDP — card)` | **$99.99\*** | published | tadalafil · oral · "generic Cialis," daily-low-dose or on-demand (per FAQ). |
| Sildenafil | buyable | Sexual Health Therapy | `/sexual-health/ (no PDP — card)` | **$99.99\*** | published | sildenafil · oral · fast-acting ED treatment. |
| Enclomiphene | buyable | Sexual Health Therapy | `/sexual-health/ (no PDP — card)` | **$99.99/mo** | published | enclomiphene · oral · same SKU as the Testosterone line (cross-listed). |
| HCG | buyable | Sexual Health Therapy | `/sexual-health/ (no PDP — card)` | **$80/mo** | published | HCG · injectable · "2.5 months minimum." Also bundled as TRT + HCG. |
| **Anti-Aging Therapy** | family | — | `/anti-aging/` | — | — | Longevity + peptide line (injectables). |
| NAD+ | buyable | Anti-Aging Therapy | `/anti-aging/ (no PDP — card)` | **$120/mo** | published | NAD+ · injectable · "2.5 months minimum." |
| Glutathione | buyable | Anti-Aging Therapy | `/anti-aging/ (no PDP — card)` | **$80/mo** | published | glutathione · injectable. |
| Sermorelin | buyable | Anti-Aging Therapy | `/anti-aging/ (no PDP — card)` | **$199.99/mo** | published | sermorelin · injectable peptide · "peptide therapy" (render label "15mg"); GH-secretagogue. |
| Tesamorelin | buyable | Anti-Aging Therapy | `/anti-aging/ (no PDP — card)` | **$233/mo** | published | tesamorelin · injectable peptide · "3 months minimum." Only on /anti-aging/, not the popular subset. |
| IGF1-LR3 | buyable | Anti-Aging Therapy | `/anti-aging/ (no PDP — card)` | **$159.99/mo** | published | IGF1-LR3 · injectable peptide · 30-day supply. Only on /anti-aging/, not the popular subset. |
| **Labs** | family | — | `/lab-orders/` | — | — | À-la-carte diagnostic panels (LabCorp / Quest); BYO outside labs also accepted. |
| TRT Bloodwork | buyable | Labs | `/lab-orders/` | **$129** | published | panel · TT, CBC, CMP, E2, *PSA · new or existing patient. |
| Weight Loss Bloodwork | buyable | Labs | `/lab-orders/` | **$129** | published | panel · TSH, CBC, CMP. |
| TRT and Weight Loss Bloodwork | buyable | Labs | `/lab-orders/` | **$179** | published | panel · TT, CBC, CMP, E2, TSH, *PSA. |

### Verbatim anchors

The footnotes the Price column points at (the commitment terms + supply quantities), quoted exactly:

- **Testosterone:** "$99.99/mo" · "\*2.5 months minimum purchase" · "\*California pricing may vary"
- **Enclomiphene:** "$99.99/mo" · "\*Includes 30 day supply (30ct | 25mg capsules)"
- **TRT + HCG:** "$180/mo" · "\*2.5 months minimum purchase"
- **Tirzepatide:** "$219/mo" · "\*3 months minimum purchase" · homepage: "Any dose same price, $219/mo"
- **Phentermine:** "$99.99/mo" · "\*Includes 30 day supply (30ct | 37.5mg tablets)"
- **Tadalafil / Sildenafil:** "$99.99\*" (the \* footnote on the sexual-health page mirrors the 30-day-supply note)
- **HCG:** "$80/mo" · "\*2.5 months minimum purchase"
- **NAD+:** "$120/mo" · "\*2.5 months minimum purchase" · **Glutathione:** "$80/mo" · **Sermorelin:** "$199.99/mo"
- **Tesamorelin:** "$233/mo" · "\*3 months minimum purchase" · **IGF1-LR3:** "$159.99/mo" · "\*Includes 30 day supply"
- **Labs:** "TRT Bloodwork - $129 (includes TT, CBC, CMP, E2, \*PSA)" · "Weight Loss Bloodwork - $129 (includes TSH, CBC, CMP)" · "TRT and Weight Loss Bloodwork - $179 (includes TT, CBC, CMP, E2, TSH, \*PSA)"

**Molecule-sourcing audit.** Every product's molecule is its **card heading**, page-attested (Tirzepatide,
Phentermine, Tadalafil, Sildenafil, Enclomiphene, NAD+, Glutathione, Sermorelin, Tesamorelin, IGF1-LR3, HCG are
molecule names as written). Form is from card copy: "injections"/"injectable" vs "oral"/"capsules"/"tablets."
The product-render **labels** add corroborating detail the markdown omits — "Testosterone **Cypionate** 10ml,"
"Tirzepatide **Compounding Injection** 2.5mg," "Sermorelin Peptide Therapy 15mg" — but these are *rendered image
text*, flagged as such, not relied on as the primary attestation (markdown stays the source of truth per the
contract). No FDA brand-name drug (e.g. Ozempic®/Wegovy®) is named; the FAQ states all meds are "sourced from
licensed U.S. compounding pharmacies."

## Deep blocks

Earned only on ambiguity — the roster carries the rest.

- **Hero product renders (opt-in asset — this run).** TRT Nation publishes a clean isolated product render per
  SKU (branded vial/bottle on white, color-coded by category). All **13 medication renders** were captured to
  `captures/2026-06-04/images/<sku>.png` (1024×1024): `testosterone`, `enclomiphene`, `trt-hcg`, `tirzepatide`,
  `phentermine`, `tadalafil`, `sildenafil`, `hcg`, `nad`, `glutathione`, `sermorelin`, `tesamorelin`, `igf1-lr3`.
  The flagship reference is `images/testosterone.png` — a navy-capped clear 10ml vial, gold label panel reading
  "Testosterone Cypionate," TRT Nation "America's Clinic" wordmark. Source: the `<Name>-Product.png` assets on
  each category page (headed-downloaded; the CDN 403s a bare fetch).
- **No per-SKU deep-dive earned** — there's no gated/FAQ-only price or "this isn't actually X" disambiguation to
  resolve; every price is on its card and every molecule is its heading. The cross-listings (Enclomiphene,
  HCG/TRT+HCG) are noted inline in the roster, which suffices.

## Provenance

- **Pages read:** /popular-treatments/ (catalog index), /testosterone-therapy/, /weight-loss-therapy/, /anti-aging/, /sexual-health/, /lab-orders/ — captured 2026-06-04, plus homepage for hero prices. Prices grep-verified against these captures.
- **Scope:** all 16 buyable SKUs enumerated (no leaf below the card). Cross-listed molecules listed once per line they appear on. The /trtlw/ /wllw/ /aalw/ /shlw/ "customize" funnels were not entered (they gate dosing/checkout, not new SKUs).
- **Gated/unreachable:** none — pricing is fully published pre-intake.
- **Point-in-time caveat:** card sets and prices are a 2026-06-04 snapshot; no A/B instrumentation was observed, but a DTC catalog can change — re-check on next capture.
- **Run profile:** non-vanilla — flagship/product **hero images** requested and captured (all 13 SKU renders, not just the flagship; see Deep blocks). Otherwise a standard roster.
