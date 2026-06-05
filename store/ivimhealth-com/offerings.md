---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: ivimhealth.com
captured_at: 2026-06-04
enumeration: indexed-complete
site_notes: "Two catalogs, two backbones: clinical Rx on the WordPress host (prices on /glp1-pricing/ + program PDPs; branded/oral/microdosing/injectable PDPs quiz-gated, not captured), supplements on a Shopify storefront (shop.ivimhealth.com/products.json?limit=250 = full 25-SKU catalog + verbatim prices, free). GLP-1 prices carry a med-floor + separate $74.99/mo program fee + 'membership required thereafter' → partial. Pricing is promo-framed ('first month free') and 'subject to change' — re-check next run."
---

## Portfolio overview

Weight-loss-anchored, multi-line, expanding outward. The brand indexes its catalog as **clinical Rx programs** (membership-gated, WordPress host) plus a **physician-formulated supplement store** (Shopify, cash). The "shape" finding worth flagging: despite the cardiometabolic/hormone framing, **there is no live testosterone/TRT SKU — Men's Hormone Health and physician-prescribed peptides are both "coming soon" waitlists**, so a reader should not assume a men's-TRT offering yet.

Prominence (calibrated):
- **GLP-1 weight loss [HIGH]** — homepage hero + first nav + the intake form defaults to `/glp-1`; the company's own anchor.
- **Women's Hormone Optimization [MED]** — homepage tile + nav, a full priced ($199/mo) program.
- **Supplements [MED]** — large nav footprint + a "20% off for members" hook, but a separate cash storefront, not the clinical front door.
- **Energy/Metabolism + Sleep injectables (NAD+/B12/Lipotropic/Sermorelin) [LOW]** — nav sub-items, no dedicated hero, prices not surfaced.
- **Men's HRT + Peptides [LOW / pre-launch]** — explicitly "coming soon."

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| GLP-1 ID Weight Loss | family | — | /glp1idwt/ | — | — | compounded + branded GLP-1 weight-loss program; individualized weekly dosing; membership-gated |
| Compounded Semaglutide | buyable | /glp1idwt/ | /compounded-semaglutide/ | "$499 (4-month)" · "$600 (6-month)"; floor "starting at $75/mo" + "$74.99/mo Program Fee" | partial | semaglutide · subcutaneous injection, weekly · membership-required ($75/mo thereafter); 1/2/4/6-mo terms, non-cancellable once started |
| Compounded Tirzepatide | buyable | /glp1idwt/ | /compounded-tirzepatide/ | "$900 (4-month)" · "$1100 (6-month)"; floor "starting at $133/mo" + "$74.99/mo Program Fee" | partial | tirzepatide (GLP-1+GIP) · subcutaneous injection, weekly · membership-required; 1/2/4/6-mo terms |
| GLP-1 Microdosing | buyable | /glp1idwt/ | /microdosing/ | not captured | on-request | low-dose GLP-1 · injection · (PDP quiz-gated, not captured) |
| Compounded Liraglutide | buyable | /glp1idwt/ | /compounded-liraglutide/ | not captured | on-request | liraglutide · injection · (PDP not captured) |
| Oral GLP-1 | buyable | /glp1idwt/ | /oral-glp1-medication/ | not captured | on-request | oral GLP-1 · not stated · (PDP not captured) |
| Wegovy (branded) | buyable | /glp1idwt/ | /wegovy/ | not captured | on-request | semaglutide (branded, Novo) · injection · "traditional GLP-1 program" |
| Ozempic (branded) | buyable | /glp1idwt/ | /ozempic/ | not captured | on-request | semaglutide (branded, Novo) · injection |
| Zepbound (branded) | buyable | /glp1idwt/ | /zepbound/ | not captured | on-request | tirzepatide (branded, Lilly) · injection |
| Mounjaro (branded) | buyable | /glp1idwt/ | /mounjaro/ | not captured | on-request | tirzepatide (branded, Lilly) · injection |
| Saxenda (branded) | buyable | /glp1idwt/ | /saxenda/ | not captured | on-request | liraglutide (branded, Novo) · injection |
| Wegovy Pill | buyable | /glp1idwt/ | /wegovypill/ | not captured | on-request | oral semaglutide · pill · "first month of membership on us" promo |
| Foundayo Pill | buyable | /glp1idwt/ | /foundayopill/ | not captured | on-request | oral GLP-1 · not stated · pill |
| Women's Hormone Optimization | buyable | — | /women-hormone-optimization/ | "$199/month* (4 Month Commitment)" | published | estradiol/estriol + progesterone · oral capsule / transdermal patch · all-inclusive of meds + membership; 4-mo min; at-home labs optional |
| HRT sexual-wellness add-ons | buyable | /women-hormone-optimization/ | (no PDP — HRT add-on) | "billed in addition to your… Program" | on-request | DHEA (vaginal cream) · PT-141/bremelanotide (troche) · apomorphine/oxytocin (troche) · prescribed-only add-ons |
| NAD+ | buyable | — | /nad/ | not captured | on-request | NAD+ · injection · provider-prescribed (PDP not captured) |
| B12 | buyable | — | /b12/ | not captured | on-request | vitamin B12 · injection · (PDP not captured) |
| Lipotropic | buyable | — | /lipotropic/ | not captured | on-request | lipotropic (fat-metabolism) · injection · (PDP not captured) |
| Sermorelin | buyable | — | /sermorelin/ | not captured | on-request | sermorelin · peptide · provider-prescribed (PDP not captured) |
| Men's Hormone Health | family | — | (no PDP — pre-launch) | — | on-request | "coming soon" — no live SKU at capture |
| Peptide therapies | family | — | (no PDP — pre-launch) | — | on-request | "coming soon," waitlist — energy/sleep/body-comp/immune/longevity peptides |
| Supplements & wellness | family | — | https://shop.ivimhealth.com/ | "$30.00"–"$105.00"; 20% off for members | published | physician-formulated supplement catalog (Shopify); 20 health SKUs below |
| Multí-[V] | buyable | shop | shop.ivimhealth.com/products/multi-v | "$50.00" | published | multivitamin · capsule · subscription/one-time |
| Rénu (NMN) | buyable | shop | shop.ivimhealth.com/products/renu | "$84.00" | published | NMN · capsule · longevity |
| Akkermansía+ | buyable | shop | shop.ivimhealth.com/products/akkermansia | "$40.00" | published | akkermansia probiotic · capsule |
| Gréens+ | buyable | shop | shop.ivimhealth.com/products/greens | "$60.00" | published | greens blend · powder |
| Vítamin D3+K2 | buyable | shop | shop.ivimhealth.com/products/vitamin-d3-k2 | "$30.00" | published | vitamin D3+K2 · capsule |
| Hídrate Electrolyte Blend | buyable | shop | shop.ivimhealth.com/products/hidrate | "$35.00" | published | electrolytes · powder |
| Whéy+ Protein Powder | buyable | shop | shop.ivimhealth.com/products/whey | "$65.00" | published | whey protein · powder |
| Glycíne | buyable | shop | shop.ivimhealth.com/products/glycine | "$37.00" | published | glycine · powder · sleep |
| Collágen+ | buyable | shop | shop.ivimhealth.com/products/collagen | "$40.00" | published | collagen · powder |
| Amíno+ | buyable | shop | shop.ivimhealth.com/products/amino | "$47.00" | published | amino acids · powder |
| Kríll | buyable | shop | shop.ivimhealth.com/products/krill | "$35.00" | published | krill oil · softgel |
| Magnesíum+ | buyable | shop | shop.ivimhealth.com/products/magnesium | "$40.00" | published | magnesium · capsule · sleep |
| Hepatíc | buyable | shop | shop.ivimhealth.com/products/hepatic | "$45.00" | published | liver support · capsule |
| Berberíne | buyable | shop | shop.ivimhealth.com/products/berberine | "$47.00" | published | berberine · capsule |
| Colostrum Complex | buyable | shop | shop.ivimhealth.com/products/colostrum | "$70.00" | published | colostrum · capsule · immune |
| Prebiotic Fiber Gummies | buyable | shop | shop.ivimhealth.com/products/fiber | "$30.00" | published | prebiotic fiber · gummy |
| Creatine | buyable | shop | shop.ivimhealth.com/products/creatine | "$48.00" | published | creatine · powder · body-comp |
| Cu Skin | buyable | shop | shop.ivimhealth.com/products/cu-cream | "$90.00" | published | copper-peptide skin cream · topical |
| Cu Hair | buyable | shop | shop.ivimhealth.com/products/cu-hair | "$105.00" | published | copper-peptide hair spray · topical |
| GLP-1 Support Bundle | buyable | shop | shop.ivimhealth.com/products/glp-1-essentials | "$125.00" | published | GLP-1 companion supplement bundle |

## Verbatim anchors

- **GLP-1 plan totals (/glp1-pricing/):** "Compounded semaglutide: $600 (6-month) | $499 (4-month)"; "Compounded tirzepatide: $1100 (6-month) | $900 (4-month)". Breakdown e.g. "Semaglutide 4-month: Ivím Membership: $75 / Free First Month: -$75 / Total Due Today: $499."
- **GLP-1 floor + program fee (/glp1idwt/):** "Compounded Semaglutide (GLP-1) starting at* $75/mo"; "Compounded Tirzepatide (GLP-1 + GIP) starting at* $133/mo"; "+ $74.99/mo Program Fee."
- **Membership footnote (/glp1-pricing/):** "Prices include compounded medication and your first month of Ivím Membership ($75/mo required thereafter)." → drives the `partial` token on the GLP-1 SKUs.
- **HRT (/women-hormone-optimization/):** "$199/month* (4 Month Commitment)"; "The cost of the Hormone Optimization Program is $199 a month with an initial 4-month commitment, including all provider-prescribed hormone replacement therapy medications and Ivim membership benefits." Add-ons "billed in addition to your Hormone Optimization Program."
- **Molecule sourcing audit:** semaglutide/tirzepatide/liraglutide attested on /glp1-pricing/ + /glp1idwt/ (incl. the Novo/Lilly trademark disclaimer). Branded-SKU molecules (Wegovy=semaglutide, etc.) inferred from the disclaimer's named pairings, **not** from a captured PDP — `on-request`, PDP not scraped. Oral GLP-1 / Foundayo Pill molecule **not stated** in captured pages. Supplement "molecules" are the product name itself (storefront titles).

## Deep blocks

None earned — the roster carries this company. (The clinical PDPs that would deepen the branded/injectable rows are quiz-gated and were not captured; the supplement leaves are self-describing storefront SKUs.)

## Provenance

- **Pages read:** /glp1-pricing/, /glp1idwt/, /why-membership/, /women-hormone-optimization/, /our-services/ (Firecrawl markdown); `shop.ivimhealth.com/products.json` (durable copy at `captures/2026-06-04/shop_products.json`, rendered to `captures/2026-06-04/shop_catalog.md` in storefront `$`-price format for the supplement rows). Homepage + nav for the line/slug census.
- **Scope note:** all lines rostered at the indexed level — clinical Rx at SKU grain, supplements at SKU grain (full 20-SKU health catalog; non-therapeutic merch — water bottles, shaker, travel case — deliberately excluded). **Leaf detail skipped by design:** branded/oral/microdosing/liraglutide GLP-1 and injectable (NAD+/B12/Lipotropic/Sermorelin) prices live on quiz-gated PDPs not captured this run → those rows are `on-request`, not absent. No whole line omitted ⇒ `indexed-complete`.
- **Gated/unreachable:** branded-GLP-1 + injectable prices (quiz-gated PDPs); Men's HRT + Peptides (pre-launch waitlists, no SKU).
- **Point-in-time:** pricing is promo-framed ("first month free") and carries "subject to change" footnotes; membership shown as both $75/mo and $74.99/mo. Treat the roster as a 2026-06-04 snapshot.
- **Run profile:** Express invocation — offerings.md captured alongside profile.md + telehealth.md cohort pack; supplement catalog enumerated off products.json (no hero-image asset capture).
