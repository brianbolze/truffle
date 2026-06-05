---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: tryshed.com
captured_at: 2026-06-04
site_notes: "Prices live on PDPs as 1/6/12-month plan grids (per-month drops with longer prepay) — there is no /pricing page. Category cards under-state vs the PDP: cards say 'Starting at $399/$299' for Tirzepatide/Semaglutide, the PDP 1-month tiers are $349/$249 — quote both, treat the PDP grid as authoritative. Foundayo and 'zepbound-shed-membership' layer a separate $125/mo Shed Membership on top of the med price. Women's-hair + several longevity/hair PDPs were not individually scraped this run — their per-SKU prices are unenumerated."
---

## Portfolio overview

Shed sells three priced, prescription-led lines — **Weight Loss** (the hero), **Longevity + Vitality**, and **Hair** — plus a not-yet-live **Skin** line and standalone **Health Coaching**. A separate **Shed Supplements** brand (OTC protein/greens/collagen and GLP-1 companion powders) lives off-site on shednutrition.com / shedsupplements.com and is out of scope for this Rx roster (see `profile.md` `owns:`).

Shape finding: this is a **multi-line GLP-1 telehealth catalog**, indexed at the SKU. Weight Loss carries the prominence — it owns the homepage hero, the member-count proof, and the money-back guarantee `[HIGH]` (the company's own framing). Within it, **compounded Semaglutide/Tirzepatide are the value wedge** and **Foundayo® (orforglipron) is the featured launch** `[MED]` (repeated hero banner "Foundayo® Is Here. The FDA-Approved GLP-1 Pill"). Two pricing patterns matter for any consumer: (1) category cards quote a **higher "Starting at" than the PDP 1-month tier**, and (2) Foundayo and the Zepbound membership slug layer a **mandatory $125/month membership** the headline med price omits → `partial`, not `published`.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Weight Loss | family | — | /products/category/weight-loss | — | — | GLP-1 + adjunct weight-loss line |
| Compounded Tirzepatide Injections | buyable | Weight Loss | /products/compounded-tirzepatide-injections | "Starting at $399/month" (card); PDP plan: "1 Month $349" / "6 Months $279" / "12 Months $245" | published | tirzepatide · weekly subcutaneous injection · async Rx; "dual-action GLP-1 and GIP receptor agonist" |
| Compounded Semaglutide Injections | buyable | Weight Loss | /products/compounded-semaglutide-injections | "Starting at $299/month" (card); PDP plan: "1 Month $249" / "6 Months $199" / "12 Months $175" | published | semaglutide · weekly injection · async Rx; "GLP-1 receptor agonist" |
| Foundayo® | buyable | Weight Loss | /products/foundayo | "Starting at $149/month + additional $125/month Shed Membership" | partial | orforglipron · once-daily oral pill · async Rx; FDA-approved; "$125 Shed membership and provider fee" separate (see anchors) |
| Wegovy® | buyable | Weight Loss | /products/product/wegovy | "Starting at $349/month" | published | molecule not stated on captured pages ("GLP-1 receptor agonist FDA-approved") · injection · Rx |
| Zepbound® | buyable | Weight Loss | /products/product/zepbound-shed-membership | "Starting at $349/month" | partial | molecule not stated ("dual-action GLP-1 receptor agonist FDA-approved") · injection · Rx; slug implies bundled Shed membership |
| GLP-1 Liquid Drops | buyable | Weight Loss | /products/product/glp-1-liquid-drops | "Starting at $229/month" | published | "oral semaglutide GLP-1" · sublingual drops · Rx |
| GLP-1 Lozenges | buyable | Weight Loss | /products/product/glp-1-lozenges | "Starting at $199/month" | published | "oral GLP-1" · mouth-dissolving lozenge · Rx |
| Metformin + Naltrexone + Topiramate | buyable | Weight Loss | /products/product/metformin-naltrexone-topiramate | "Starting at $169/month" | published | metformin + naltrexone + topiramate · oral capsule · Rx |
| MIC + B12 | buyable | Weight Loss | /products/product/mic-b12-injections | "Starting at $115/month" | published | MIC + B12 · injection · Rx |
| Naltrexone + Bupropion | buyable | Weight Loss | /products/product/naltrexone-bupropion | "Starting at $115/month" | published | naltrexone + bupropion · oral · Rx |
| Ozempic® | buyable | Weight Loss | /products/ozempic | — (not shown on captured pages) | on-request | brand-name GLP-1 · injection · Rx; listed in nav, PDP not scraped |
| Mounjaro® | buyable | Weight Loss | /products/mounjaro | — (not shown on captured pages) | on-request | brand-name GLP-1 · injection · Rx; listed in nav, PDP not scraped |
| Longevity + Vitality | family | — | /products/category/longevity | — | — | longevity / vitality Rx line |
| Microdose GLP-1 | buyable | Longevity + Vitality | /products/microdose | "Starting at $149/month" | published | "low-dose semaglutide or tirzepatide" · injection or tablet · Rx |
| NAD+ | buyable | Longevity + Vitality | /products/nad | "Starting at $144/month" | published | NAD+ · injection, tablet, or nasal spray · Rx |
| Glutathione | buyable | Longevity + Vitality | /products/glutathione-injections | "Starting at $119/month" | published | glutathione · injection · Rx |
| Sermorelin | buyable | Longevity + Vitality | /products/product/sermorelin | "Starting at $199/month" | published | sermorelin · injection (growth-hormone-releasing peptide) · Rx |
| Low-Dose Naltrexone (LDN) | buyable | Longevity + Vitality | /products/product/ldn | "Starting at $89/month" | published | low-dose naltrexone · oral · Rx |
| Methylene Blue | buyable | Longevity + Vitality | /products/product/methylene-blue | "Starting at $99/month" | published | methylene blue · oral · Rx |
| Hair | family | — | /products/mens-hair-solutions · /products/womens-hair-solutions | — | — | men's & women's hair-loss line |
| Men's Minoxidil + Finasteride Serum | buyable | Hair | /products/product/mens-2-1-hair-solution | "Starting at $43/month" | published | minoxidil + finasteride · topical serum · Rx |
| Men's 3-in-1 Hair Tablet | buyable | Hair | /products/product/mens-3-1-hair-tablet | "Starting at $43/month" | published | minoxidil + finasteride + biotin · oral tablet · Rx |
| Men's 5-in-1 Hair Serum | buyable | Hair | /products/product/mens-5-1-hair-solution | "Starting at $46.33/month" | published | minoxidil + finasteride + tretinoin + vitamin E + fluocinolone · topical serum · Rx |
| Men's Copper Peptide Hair Serum | buyable | Hair | /products/product/ghk-cu-scalp-peptide-solution | "Starting at $76.33/month" | published | "copper peptide–based topical treatment" (GHK-Cu) · topical serum · OTC/cosmetic |
| Women's 3-in-1 Hair (Serum/Capsule) | buyable | Hair | /products/product/womens-3-1-hair-capsule | — (PDP not scraped) | on-request | molecule not stated · women's hair · Rx |
| Women's 5-in-1 Hair Serum | buyable | Hair | /products/product/womens-5-1-hair-solution | — (PDP not scraped) | on-request | molecule not stated · women's hair · Rx |
| Women's Copper Peptide Hair Serum | buyable | Hair | /products/product/womens-ghk-cu-scalp-peptide-solution | — (PDP not scraped) | on-request | copper peptide (GHK-Cu) · topical serum · OTC/cosmetic |
| Health Coaching | buyable | — | /products/health-coaching | — (price not captured) | on-request | non-Rx human health coaching · standalone |
| Skin (Custom Skin Treatment) | family | — | (coming soon — no live PDP) | — | on-request | not launched; nav placeholder slots only |

## Verbatim anchors

- **Foundayo membership (decides `partial`):** *"Foundayo® pricing starts at $149/month for new patients using cash pay. Price does not include the $125 Shed membership and provider fee, paid directly to Shed. Medication costs are paid separately to the dispensing pharmacy."* — `/products/foundayo`. Also: *"Foundayo® (orforglipron) is a once-daily oral GLP-1 receptor agonist, FDA-approved for chronic weight management… Foundayo® is a registered trademark of Eli Lilly and Company. Shed is not affiliated with or endorsed by Eli Lilly and Company."*
- **Semaglutide plan grid (verbatim):** "Plan / Per Month — 1 Month **$249** · 6 Months **$199** (Save $300) · 12 Months **$175** (Save $888)" — `/products/compounded-semaglutide-injections`.
- **Tirzepatide plan grid (verbatim):** "1 Month **$349** · 6 Months **$279** ($420 Savings) · 12 Months **$245** ($1,248 Savings)" — `/products/compounded-tirzepatide-injections`.
- **Card-vs-PDP discrepancy:** the weight-loss category card reads "Compounded Tirzepatide Injections — **Starting at $399/month**" and "Compounded Semaglutide Injections — **Starting at $299/month**," each sitting above the matching PDP's 1-month tier ($349 / $249 respectively). Both quoted; PDP grid treated as authoritative.
- **Molecule sourcing audit (`not stated`):** Wegovy® and Zepbound® show only the brand + "GLP-1 receptor agonist / dual-action … FDA-approved" on captured pages — semaglutide/tirzepatide were **not page-stated for those SKUs**, so molecule = `not stated` (never inferred from the brand). Ozempic®/Mounjaro® and all women's-hair SKUs: PDPs not scraped this run.

## Deep blocks

Earned only where the roster row can't resolve a real ambiguity — one block here; the roster carries the rest.

- **Foundayo® — the "$149" headline is not the all-in.** Foundayo is the site's featured launch (orforglipron, the FDA-approved once-daily oral GLP-1 pill — Eli Lilly's brand, which Shed routes a prescription for, not affiliated). The hero quotes **"Starting at $149/month,"** but the PDP and footnote make the real cost **$149 (cash-pay medication) + $125/month Shed membership & provider fee**, with *"Medication costs… paid separately to the dispensing pharmacy."* So the GLP-1 pill's true monthly floor stacks the **$149 medication on top of the $125 membership + provider fee** — materially different from the compounded injections, whose plan price appears self-contained. Visibility = **`partial`** (a mandatory same-seller membership sits on top of the shown med price). The clinical claim — *"Lose up to 12.4% of your body weight"* — is sourced to "ATTAIN-1 Phase 3 … highest dose … 72 weeks," per the Foundayo Prescribing Information, not Shed's own data.

## Provenance

- **Pages read:** homepage + `/products/category/weight-loss` + `/products/category/longevity` + `/products/mens-hair-solutions` + PDPs `/products/compounded-semaglutide-injections`, `/products/compounded-tirzepatide-injections`, `/products/foundayo` (all `captures/2026-06-04/`).
- **Scope:** Weight-Loss and Longevity lines enumerated at the SKU with PDP/card prices; Men's-Hair enumerated with category-card prices. **Not enumerated:** Women's-Hair per-SKU prices, Ozempic®/Mounjaro® prices, Health-Coaching price (PDPs not scraped) — listed as rows with `on-request` so the gap is explicit, not silent.
- **Point-in-time caveat:** prices are a 2026-06-04 snapshot and run promo/plan-tier variance; the category-card vs PDP gap (above) is live, not a capture error.
- **Run profile:** `offerings.md` written because the guided run requested it (telehealth cohort, enumerable priced SKUs) — vanilla roster, no added columns or opt-in PDP-anatomy block; no hero images.
