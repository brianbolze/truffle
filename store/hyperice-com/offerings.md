---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: hyperice.com
captured_at: 2026-06-24
enumeration: indexed-complete
site_notes: "Shopify storefront. Collection grids expose 59 visible product handles across shop-all, line collections, accessories, sale, outlet, and gift card; /products.json?limit=250 is the catalog backbone and exposes 65 handles total. Six handles are registry-only/hidden from captured US collections: Premier Pack, Normatec Premier Legs/Hips, Normatec Lower Legs, Hyperice Contrast 2 Knee/Shoulder. Hidden PDP scrapes for Premier handles returned duplicate homepage bodies, so cite products_json for hidden rows. Gift card denominations live on /products/gift-card."
---

## Portfolio overview

Hyperice's 2026-06-24 catalog is a multi-line recovery-hardware portfolio at SKU grain. The captured US storefront/card surfaces expose **59 buyable product handles**; the captured Shopify registry exposes **65 handles total**, adding six hidden/legacy handles not surfaced in the captured US collection grids. Rows marked "registry-only" are included for full catalog breadth but should not be read as currently merchandised US storefront offers.

Prominence read:
- **Hyperboot by Nike × Hyperice / Prime Day sale** — `[HIGH]`: top homepage hero and sale banner; `sale.md` leads with Warm Up Pack, Hyperboot, Elite Pack, and Hypervolt 3 Pro.
- **Hypervolt 3 Pro / Normatec Elite Legs** — `[HIGH]`: top product-card placement in shop-all/sale and repeated line-page emphasis.
- **Hyperice X 2 and Venom 2** — `[MED]`: line collections are surfaced in nav and homepage therapy sections, with current sale pricing.
- **Outlet/open-box** — `[MED]`: explicit nav item and 17 captured open-box rows, but separated from the main shop-all product count.
- **Registry-only Premier/Contrast legacy handles** — `[LOW]`: present in products_json and locale-prefixed map results, absent from captured US collection pages; most are unavailable in the registry.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Hypervolt | family | — | /collections/hypervolt | — | — | percussion · massage-gun family · surfaced US collection |
| Hypervolt 3 Pro | buyable | Hypervolt | /products/hypervolt-3-pro | $299.00 (reg ~~$349.00~~) | published | percussion · handheld massage gun · open purchase — 6 speeds, 5 head attachments |
| Hypervolt 3 | buyable | Hypervolt | /products/hypervolt-3 | $209.00 (reg ~~$249.00~~) | published | percussion · handheld massage gun · open purchase — everyday model |
| Hypervolt Go 3 | buyable | Hypervolt | /products/hypervolt-go-3 | $119.00 (reg ~~$149.00~~) | published | percussion · lightweight massage gun · open purchase — USB-C |
| Hypervolt 2 | buyable | Hypervolt | /products/hypervolt-2-black | $183.00 (reg ~~$229.00~~) | published | percussion · handheld massage gun · open purchase — prior generation |
| Hypervolt Go 2 | buyable | Hypervolt | /products/hypervolt-go-2-black | $109.00 (reg ~~$139.00~~) | published | percussion · lightweight massage gun · open purchase — prior generation |
| Heated Head Attachment 3 | buyable | Hypervolt | /products/heated-head-attachment-3 | $59.00 | published | accessory · heated percussion attachment · open purchase |
| Hypervolt Applicator Set | buyable | Hypervolt | /products/hypervolt-applicator-set | $25.00 | published | accessory · replacement head kit · open purchase |
| Hypervolt 2 Pro Battery | buyable | Hypervolt | /products/hypervolt-2-pro-battery | $79.00 | published | accessory · spare battery · open purchase |
| Open Box Hypervolt 2 Pro | buyable | Hypervolt / Outlet | /products/open-box-hypervolt-2-pro | $199.00 (reg ~~$329.00~~) | published | percussion · open-box massage gun · outlet purchase |
| Open Box Hypervolt 2 Black | buyable | Hypervolt / Outlet | /products/open-box-hypervolt-2-black | $129.00 (reg ~~$199.00~~) | published | percussion · open-box massage gun · outlet purchase |
| Open Box Hypervolt Go 2 | buyable | Hypervolt / Outlet | /products/open-box-hypervolt-go-2 | $99.00 (reg ~~$129.00~~) | published | percussion · open-box lightweight gun · outlet purchase |
| Normatec | family | — | /collections/normatec | — | — | dynamic air compression · recovery systems and attachments · surfaced US collection plus registry-only legacy handles |
| Normatec Elite Legs | buyable | Normatec | /products/normatec-elite | $999.00 (reg ~~$1,099.00~~) | published | air compression · hoseless leg boots · open purchase |
| Normatec Elite Hips | buyable | Normatec | /products/normatec-elite-hips | $549.00 (reg ~~$599.00~~) | published | air compression · hoseless hip/IT-band/back wrap · open purchase |
| Normatec 3 Legs | buyable | Normatec | /products/normatec-3-legs | $719.00 (reg ~~$899.00~~) | published | air compression · leg boots + control unit · open purchase |
| Normatec 3 Lower Body | buyable | Normatec | /products/normatec-3-lower-body | $919.00 (reg ~~$1,149.00~~) | published | air compression · legs + hips package · open purchase |
| Normatec 3 Full Body | buyable | Normatec | /products/normatec-3-full-body | $1,349.00 (reg ~~$1,549.00~~) | published | air compression · arms + hips + legs system · open purchase |
| Normatec Go | buyable | Normatec | /products/normatec-go | $299.00 (reg ~~$379.00~~) | published | air compression · portable calf sleeves · open purchase |
| Normatec Lower Legs | buyable | Normatec / Registry-only | /products/normatec-lower-legs | 379.00 (registry; available=false) | published | air compression · lower-leg sleeves · registry-only, not surfaced in captured US collections |
| Normatec Premier Legs | buyable | Normatec / Registry-only | /products/normatec-premier-legs | 1099.00 (registry; available=false) | published | air compression · Premier leg boots · registry-only, not surfaced in captured US collections |
| Normatec Premier Hips | buyable | Normatec / Registry-only | /products/normatec-premier-hips | 599.00 (registry; available=true) | published | air compression · Premier hip wrap · registry-only, not surfaced in captured US collections |
| Elite Pack | buyable | Normatec | /products/elite-pack | $1,548.00 (reg ~~$1,698.00~~) | published | bundle · Normatec Elite Legs + Elite Hips · open purchase |
| Premier Pack | buyable | Normatec / Registry-only | /products/premier-pack | 1698.00 (registry; available=false) | published | bundle · Normatec Premier Legs + Premier Hips · registry-only, not surfaced in captured US collections |
| Normatec Leg Attachments | buyable | Normatec | /products/leg-attachment | $350.00 (reg ~~$400.00~~) | published | part · pair of leg attachments · open purchase |
| Normatec Leg Attachment Single | buyable | Normatec | /products/normatec-3-leg-attachment-single | $200.00 | published | part · single leg attachment · open purchase |
| Normatec Arm Attachments | buyable | Normatec | /products/arm-attachment | $350.00 (reg ~~$400.00~~) | published | part · pair of arm attachments · open purchase |
| Normatec Arm Attachment Single | buyable | Normatec | /products/normatec-3-arm-attachment-single | $200.00 | published | part · single arm attachment · open purchase |
| Normatec Hip Attachment | buyable | Normatec | /products/hip-attachment | $200.00 (reg ~~$250.00~~) | published | part · hip attachment · open purchase |
| Open Box Normatec Hip Attachment | buyable | Normatec / Outlet | /products/normatec-hip-attachment-copy | $175.00 (reg ~~$250.00~~) | published | part · open-box hip attachment · outlet purchase |
| Normatec 3 Control Unit | buyable | Normatec | /products/normatec-3-control-unit | $549.00 | published | part · control unit · open purchase |
| Normatec Backpack | buyable | Normatec | /products/normatec-backpack | $180.00 | published | accessory · carry backpack · open purchase |
| Normatec Carry Case | buyable | Normatec | /products/normatec-carry-case | $180.00 | published | accessory · carry case · open purchase |
| Normatec Hose | buyable | Normatec | /products/normatec-hose | $50.00 | published | part · connector hose · open purchase |
| 15V Normatec Charger | buyable | Normatec | /products/normatec-charger | $30.00 | published | part · charger for Normatec 2.0 / 3 products · open purchase |
| Normatec Elite Legs Charger | buyable | Normatec | /products/normatec-elite-12v-dual-charger | $40.00 | published | part · replacement charger for Normatec Elite Legs · open purchase |
| Open Box Normatec Elite | buyable | Normatec / Outlet | /products/open-box-normatec-elite | $849.00 (reg ~~$1,099.00~~) | published | air compression · open-box Elite legs · outlet purchase |
| Open Box Normatec 3 Legs | buyable | Normatec / Outlet | /products/open-box-normatec-3-legs | $699.00 (reg ~~$899.00~~) | published | air compression · open-box Normatec 3 legs · outlet purchase |
| Open Box Normatec Go | buyable | Normatec / Outlet | /products/open-box-normatec-go | $299.00 (reg ~~$399.00~~) | published | air compression · open-box calf sleeves · outlet purchase |
| Open Box Normatec 2 Legs | buyable | Normatec / Outlet | /products/open-box-normatec-2-legs | $499.00 | published | air compression · open-box legacy leg system · outlet purchase |
| Hyperboot by Nike × Hyperice | family | — | /collections/hyperboot-by-nike-hyperice | — | — | heat + Normatec compression · Nike co-branded boot line |
| Hyperboot by Nike × Hyperice | buyable | Hyperboot | /products/hyperboot-nike-hyperice | $699.00 (reg ~~$799.00~~) | published | heat + air compression · wearable boot · open purchase — Nike co-brand |
| Warm Up Pack | buyable | Hyperboot / Venom | /products/warm-up-pack | $899.00 (reg ~~$1,068.00~~) | published | bundle · Hyperboot + Venom 2 Back · open purchase |
| Hyperice X | family | — | /collections/hyperice-x | — | — | contrast therapy · hot/cold/air-compression wraps |
| Hyperice X 2 Knee | buyable | Hyperice X | /products/hyperice-x-2-knee | $359.00 (reg ~~$449.00~~) | published | contrast · knee wrap · open purchase |
| Hyperice X 2 Shoulder | buyable | Hyperice X | /products/hyperice-x-2-shoulder | $359.00 (reg ~~$449.00~~) | published | contrast · shoulder wrap · open purchase |
| Hyperice Contrast 2 Knee | buyable | Hyperice X / Registry-only | /products/hyperice-contrast-2-knee | 449.00 (registry; available=false) | published | contrast · legacy knee wrap · registry-only, not surfaced in captured US collections |
| Hyperice Contrast 2 Shoulder | buyable | Hyperice X / Registry-only | /products/hyperice-contrast-2-shoulder | 449.00 (registry; available=false) | published | contrast · legacy shoulder wrap · registry-only, not surfaced in captured US collections |
| Open Box Hyperice X 2 Knee | buyable | Hyperice X / Outlet | /products/open-box-hyperice-x-2-knee | $329.00 (reg ~~$449.00~~) | published | contrast · open-box X 2 knee wrap · outlet purchase |
| Open Box Hyperice X 2 Shoulder | buyable | Hyperice X / Outlet | /products/open-box-hyperice-x-2-shoulder | $329.00 (reg ~~$449.00~~) | published | contrast · open-box X 2 shoulder wrap · outlet purchase |
| Open Box Hyperice X Knee | buyable | Hyperice X / Outlet | /products/open-box-hyperice-x-knee | $199.00 (reg ~~$399.00~~) | published | contrast · open-box legacy knee wrap · outlet purchase |
| Open Box Hyperice X Shoulder | buyable | Hyperice X / Outlet | /products/open-box-hyperice-x-shoulder | $199.00 (reg ~~$399.00~~) | published | contrast · open-box legacy shoulder wrap · outlet purchase |
| Venom | family | — | /collections/venom | — | — | heat + vibration · wearable wraps and spot treatment |
| Venom 2 Back | buyable | Venom | /products/venom-2-back | $215.00 (reg ~~$269.00~~) | published | heat + vibration · back wrap · open purchase |
| Venom 2 Shoulder | buyable | Venom | /products/venom-2-shoulder | $239.00 (reg ~~$269.00~~) | published | heat + vibration · shoulder wrap · open purchase |
| Venom 2 Leg | buyable | Venom | /products/venom-2-leg | $239.00 (reg ~~$269.00~~) | published | heat + vibration · leg wrap · open purchase |
| Venom Go | buyable | Venom | /products/venom-go | $99.00 (reg ~~$129.00~~) | published | heat + vibration · adhesive-pad spot treatment · open purchase |
| Venom Go Pack | buyable | Venom | /products/venom-go-pack | $149.00 (reg ~~$187.00~~) | published | bundle · Venom Go + case + refill pack · open purchase |
| Venom Go Case | buyable | Venom | /products/venom-go-case | $29.00 | published | accessory · Venom Go case · open purchase |
| Venom Go Refill Pack | buyable | Venom | /products/venom-go-refill-pack | $29.00 | published | accessory · replacement adhesive pads · open purchase |
| Open Box Venom Go | buyable | Venom / Outlet | /products/open-box-venom-go | $79.00 (reg ~~$129.00~~) | published | heat + vibration · open-box spot treatment · outlet purchase |
| Open Box Venom 2 Back | buyable | Venom / Outlet | /products/open-box-venom-2-back | $179.00 (reg ~~$249.00~~) | published | heat + vibration · open-box back wrap · outlet purchase |
| Open Box Venom 2 Shoulder | buyable | Venom / Outlet | /products/open-box-venom-2-shoulder | $179.00 (reg ~~$249.00~~) | published | heat + vibration · open-box shoulder wrap · outlet purchase |
| Open Box Venom 2 Leg | buyable | Venom / Outlet | /products/open-box-venom-2-leg | $179.00 (reg ~~$249.00~~) | published | heat + vibration · open-box leg wrap · outlet purchase |
| Vyper + Hypersphere | family | — | /collections/vyper-hypersphere | — | — | vibration · roller and massage ball |
| Vyper 3 | buyable | Vyper + Hypersphere | /products/vyper-3 | $209.00 | published | vibration · foam roller · open purchase |
| Hypersphere Go | buyable | Vyper + Hypersphere | /products/hypersphere-go | $109.00 | published | vibration · massage ball · open purchase |
| Open Box Vyper 3 | buyable | Vyper + Hypersphere / Outlet | /products/open-box-vyper-3 | $100.00 (reg ~~$199.00~~) | published | vibration · open-box foam roller · outlet purchase |
| Accessories / cards | family | — | /collections/accessories | — | — | parts, chargers, cases, attachments, and gift cards |
| 18V Wall Charger | buyable | Accessories | /products/wall-charger | $25.00 | published | part · wall charger for Hypervolt/Venom/Vyper/Hypersphere · open purchase |
| Gift Cards | buyable | Accessories / cards | /products/gift-card | $25.00 (denominations: $25, $50, $100, $200, $500, $1000) | published | digital gift card · selectable denominations · open purchase |
| Legacy Pack | buyable | Bundles | /products/legacy-pack | $1,328.00 (reg ~~$1,428.00~~) | published | bundle · Hypervolt 3 Pro + Normatec 3 Legs + Normatec Backpack · open purchase |

### Verbatim anchors

- **Shop-all count:** `shop_all.md` says "Filters 44 Items44 Items"; after adding line-specific accessories, outlet, sale, gift-card, and products_json registry rows, the reconciled captured roster is 65 product handles.
- **Prime Day sale:** Homepage and `sale.md` say "We're matching all of our best Amazon Prime Day deals. Save up to $230 across our entire suite of technology."
- **Warm Up Pack:** `products_json.md` body says "The Warm Up Pack pairs the Hyperboot by Nike × Hyperice with the Venom 2 Back"; sale card says "The Warm Up Pack: Prime your body from the ground up with the Hyperboot by Nike × Hyperice & the Venom 2 Back."
- **Elite Pack:** Collection cards say "The ultimate portable recovery bundle, including Normatec Elite Legs and Normatec Elite Hips."
- **Legacy Pack:** Collection cards say "Unleash your full potential with this pro-level recovery bundle that includes: ⁠Hypervolt 3 Pro, Normatec 3 Legs⁠, and Normatec Backpack."
- **Registry-only rows:** `products_json.md` is the source for Premier Pack, Normatec Premier Legs/Hips, Normatec Lower Legs, and Hyperice Contrast 2 Knee/Shoulder. Its variant records carry `available=true/false` and price strings without a dollar sign, so those rows preserve the registry's numeric price format.
- **Gift cards:** `gift_card.md` lists denominations `$25`, `$50`, `$100`, `$200`, `$500`, and `$1000`; the default displayed price is `$25.00`.
- **No molecules:** Hardware catalog; no pharma molecule applies. The `What` column leads with therapy modality instead.

## Deep blocks

None earned. The collection-card grids plus the Shopify product registry carry the roster and price evidence; the only ambiguity is merchandising scope, captured as surfaced-US rows vs. registry-only hidden/legacy rows.

## Provenance

- **Pages read:** `captures/2026-06-24/` — `shop_all.md`, six line collections (`hypervolt`, `normatec`, `hyperboot`, `hyperice_x`, `venom`, `vyper_hypersphere`), `accessories.md`, `outlet.md`, `sale.md`, `gift_card.md`, and `products_json.md`. Prices are grep-verifiable in these files; registry-only rows use the exact numeric price strings in `products_json.md`.
- **Scope:** Enumerated **indexed-complete** at Shopify product-handle grain: 65 product handles total; 59 surfaced in captured US storefront/card pages; 6 registry-only hidden/legacy handles included from the captured Shopify registry. No product-line/subdomain was left out of the indexed roster.
- **Visibility:** every row is `published` because a price/floor is present either on a captured rendered card/PDP or in the captured Shopify registry. Registry-only rows are not currently merchandised in captured US collections and should not be treated as active storefront emphasis.
- **Point-in-time caveat:** prices are a 2026-06-24 snapshot during a Prime Day sale; many mainline SKUs show sale prices below struck regular prices. Registry availability on hidden handles is also point-in-time.
- **Run profile:** express `/research-company` with full-offerings emphasis; added outlet, sale, gift-card, and products_json reconciliation beyond the prior roster. Two hidden PDP attempts returned duplicate homepage bodies and were quarantined; they are not cited as product evidence.
