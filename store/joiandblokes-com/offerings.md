---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: joiandblokes.com        # company key; each offering's slug (its relative url) is its key within the company
captured_at: 2026-06-04         # own freshness; captures/2026-06-04/ holds the source pages
site_notes: "Roster backbone = the `/shop/men/` & `/shop/women/` 'All Products' catalog pages (cards carry price + 'Best Seller'/'Lab Required' badges); deeper pricing (TRT commitment tiers, GLP-1 first-month, HRT form matrix, lab packs) lives on the flagship PDPs. Men's & women's catalogs MIRROR most SKUs (same product, gendered slug) — this roster lists the distinct product once with a gender note + one canonical attested slug, not 2× duplicates. Site exposes duplicate category-aliased PDP URLs (TRT /hormone-health/ vs /testosterone/; HRT /hormone-health/ vs /menopause-care/) — both resolve. Prices are LIST; a sitewide 'MENSHEALTH 25% OFF' code applies only at checkout (point-in-time). NY/NJ see different pricing via a geo modal (not enumerated)."
---

## Portfolio overview

A `Multi-product` dual-brand telehealth catalog (Blokes/men + Joi/women) spanning **eleven lines**: diagnostic labs, hormone health (TRT/enclomiphene/BHRT/thyroid), weight loss (GLP-1), the $1/mo ED+hair add-on program, sexual health, longevity/peptides, supplements, skin care, and gear. Most non-gender-specific SKUs **mirror across `/shop/men/` and `/shop/women/`** (same product, gendered slug); the roster lists each distinct product once with a gender tag.

**Shape finding:** this is a **diagnostics-first** catalog — labs are the deliberate low-friction wedge ($149 entry), and nearly every Rx therapy card carries a "Lab Required" tag, so the lab panel is the gateway SKU, not a side product. Pricing model varies by line: TRT and compounded GLP-1 are **all-in subscriptions** (meds + labs + consults in one monthly price); HRT/BHRT splits a **$50/mo care fee from per-form medication**; Zepbound® is a program fee **plus** meds bought elsewhere.

**Prominence** (calibrated): the catalog tags ~13 SKUs **"Best Seller"** — the company's own label, so `[HIGH]`: GLP-1, Advanced Panel, Complete Hormone Panel, Enclomiphene, Levels/Balance, Liraglutide, NAD+, Sermorelin, Smart Supplements, TRT, VIP, (women) Scream Cream + Luxe + BHRT. Hero/positioning foregrounds **labs + hormone health** `[MED]` (diagnostics-first hero imagery; "Popular Products" leads with the lab panels). The **$1/mo add-on** is the loudest *differentiator* `[HIGH]` — named head-on against Hims/Hone/Maximus on the TRT page. Brand product-system render (the full packaging family): `captures/2026-06-04/images/product-family.jpg`.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Diagnostic Labs | family | — | /shop/men/diagnostic-labs/ | — | — | The wedge; mirrored women's at /shop/women/diagnostic-labs/ |
| Complete Hormone Panel | buyable | Diagnostic Labs | /shop/men/diagnostic-labs/complete-hormone-panel/ | $149 (2-pack $298, 4-pack $596) | published | blood panel · 56 biomarkers + 30-min clinician visit · both genders; +$99–$100 optional in-home phlebotomy |
| Advanced Panel | buyable | Diagnostic Labs | /shop/men/diagnostic-labs/advanced-panel/ | $399 | published | blood panel · 71 biomarkers + full thyroid + biological age · both |
| Comprehensive Panel | buyable | Diagnostic Labs | /shop/men/diagnostic-labs/comprehensive-panel/ | $699 | published | blood panel · 110 biomarkers + 60-min visit · both |
| At Home Blood Test | buyable | Diagnostic Labs | /shop/men/diagnostic-labs/tasso-panel/ | Starting at $129 / month | published | not stated · at-home Tasso device draw · both |
| Food Sensitivity | buyable | Diagnostic Labs | /shop/men/diagnostic-labs/food-sensitivity/ | $249 | published | IgG immune response to 96 foods · lab test · both |
| Hormone Health (Men) | family | — | /shop/men/hormone-health/ | — | — | TRT, enclomiphene, thyroid |
| Testosterone Replacement Therapy | buyable | Hormone Health (Men) | /shop/men/testosterone/testosterone-replacement-therapy/ | $99/mo (12-mo) · $129/mo (6-mo) · $149/mo (3-mo); "Start now for $75" | published | testosterone cypionate · injection · men · Lab Required; all-in (meds+consults+quarterly labs). See deep block. |
| Enclomiphene | buyable | Hormone Health (Men) | /shop/men/testosterone/enclomiphene/ | $99/mo | published | enclomiphene · oral capsule · men · Lab Required |
| Thyroid Care | buyable | Hormone Health | /shop/men/hormone-health/thyroid-care/ | $99/mo | published | not stated (functional thyroid Rx) · both |
| Hormone Health (Women) — BHRT | family | — | /shop/women/menopause-care/hrt/ | — | — | bioidentical HRT; see deep block |
| Hormones (BHRT) | buyable | Hormone Health (Women) — BHRT | /shop/women/menopause-care/hrt/ | $50/mo care fee + meds separate; forms $49–$89/mo; catalog "from $59/mo" | partial | bioidentical estrogen·progesterone·testosterone · injection/cream/capsule/patch/suppository · women · Lab Required |
| Weight Loss / GLP-1 | family | — | /glp-1/ | — | — | compounded + FDA-brand; both genders |
| Compounded GLP-1 | buyable | Weight Loss / GLP-1 | /glp-1/ | $199/mo (first month $99) billed quarterly | published | semaglutide · injection · both · medication included. See deep block. |
| Compounded GLP-1 / GIP | buyable | Weight Loss / GLP-1 | /glp-1/ | $299/mo (first month $149) billed quarterly | published | tirzepatide · injection · both · medication included |
| Liraglutide | buyable | Weight Loss / GLP-1 | /shop/men/weight-loss/liraglutide/ | $299/mo | published | liraglutide · injection · both |
| Zepbound® Weight Loss Program | buyable | Weight Loss / GLP-1 | /shop/men/weight-loss/zepbound/ | $99/mo billed quarterly (plus the cost of meds) | partial | not stated for SKU · FDA brand (Eli Lilly), injection · both · program fee only, meds bought separately |
| $1/mo ED + Hair Add-ons | family | — | (no PDP — TRT/Enclomiphene member add-on) | — | — | members-only; the headline differentiator. See deep block. |
| Sildenafil (oral) | buyable | $1/mo ED + Hair Add-ons | /shop/men/testosterone/testosterone-replacement-therapy/ | $1/mo | partial | sildenafil · oral · men · requires active TRT/Enclomiphene sub + state-eligible + clinically appropriate |
| Tadalafil (oral) | buyable | $1/mo ED + Hair Add-ons | /shop/men/testosterone/testosterone-replacement-therapy/ | $1/mo | partial | tadalafil · oral · same gating as above |
| Finasteride (oral) | buyable | $1/mo ED + Hair Add-ons | /shop/men/testosterone/testosterone-replacement-therapy/ | $1/mo | partial | finasteride · oral · same gating |
| Minoxidil (oral) | buyable | $1/mo ED + Hair Add-ons | /shop/men/testosterone/testosterone-replacement-therapy/ | $1/mo | partial | minoxidil · oral · same gating |
| Sexual Health | family | — | /shop/men/sexual-health/ | — | — | mirrored women's at /shop/women/sexual-health/ |
| The Mood | buyable | Sexual Health | /shop/men/sexual-health/mood/ | Starting at $119 / month | published | not stated · Rx · both |
| Oxytocin Peptide Therapy | buyable | Sexual Health | /shop/men/sexual-health/oxytocin/ | $159/mo | published | oxytocin · nasal spray · both |
| (!) Scream Cream | buyable | Sexual Health | /shop/women/sexual-health/scream-cream/ | $37/mo | published | not stated (compounded topical) · cream · women |
| vFit® Gold+ Device | buyable | Sexual Health | /shop/women/sexual-health/vfit-gold-device/ | $395 + shipping | published | n/a · light+heat device · women · one-time purchase |
| Sexual Performance | buyable | Supplements | /shop/men/supplements/sexual-performance/ | Starting at $74 / month | published | not stated · supplement · both |
| Longevity / Peptides | family | — | /shop/men/longevity/ | — | — | mirrored women's at /shop/women/longevity/ |
| NAD+ | buyable | Longevity / Peptides | /shop/men/longevity/nad/ | $150/mo | published | NAD+ · injection/nasal spray · both |
| Sermorelin Peptide Therapy | buyable | Longevity / Peptides | /shop/men/longevity/sermorelin/ | $199/mo | published | sermorelin · peptide/injection · both |
| VIP Peptide Therapy | buyable | Longevity / Peptides | /shop/men/longevity/vip/ | $159/mo | published | VIP · peptide · both |
| Rapamycin (Sirolimus) | buyable | Longevity / Peptides | /shop/men/longevity/rapamycin-sirolimus/ | $83/mo | published | rapamycin/sirolimus · oral · both · Lab Required |
| Glutathione | buyable | Longevity / Peptides | /shop/men/longevity/glutathione/ | $69/mo | published | glutathione · injection · both · Lab Required |
| B12 + MIC Injection | buyable | Longevity / Peptides | /shop/men/longevity/b12-mic/ | $50/mo | published | B12 + methionine·inositol·choline · injection · both |
| Low Dose Naltrexone (LDN) | buyable | Longevity / Peptides | /shop/men/longevity/ldn/ | $63/mo | published | naltrexone (low-dose) · oral · both |
| Pain Cream | buyable | Longevity / Peptides | /shop/men/longevity/pain-cream/ | Starting at $149 / month | published | not stated (compounded topical) · cream · both · Lab Required |
| Supplements | family | — | /shop/men/supplements/ | — | — | mirrored women's at /shop/women/supplements/ |
| Smart Supplements | buyable | Supplements | /shop/men/supplements/smart-supplements/ | $149/mo | published | not stated · personalized daily packs · both · Lab Required |
| Levels (men) / Balance (women) | buyable | Supplements | /shop/men/supplements/levels/ | $74/mo | published | not stated · daily capsule · gendered (Levels men / Balance women) |
| Focus | buyable | Supplements | /shop/men/supplements/focus/ | $74/mo | published | not stated · nootropic capsule · both |
| Sleep | buyable | Supplements | /shop/men/supplements/sleep-supplement/ | $74/mo | published | not stated · capsule · both |
| GLP-1 Assist | buyable | Supplements | /shop/men/supplements/glp-1-assist/ | $74/mo | published | not stated · supplement · both |
| Gut Health | buyable | Supplements | /shop/men/supplements/gut-health/ | Starting at $74 / month | published | not stated · supplement · both |
| Longevity (supplement) | buyable | Supplements | /shop/men/supplements/longevity-supplement/ | Starting at $89 / month | published | not stated · supplement · both |
| Thyroid Support | buyable | Supplements | /shop/men/supplements/thyroid-support/ | Starting at $66 / month | published | not stated · supplement · both |
| Hair Support | buyable | Supplements | /shop/men/supplements/hair-support/ | Starting at $66 / month | published | not stated · supplement · both |
| Creatine Powder | buyable | Supplements | /shop/men/supplements/creatine/ | Starting at $45 / month | published | creatine · powder · both |
| Skin Care (Women) | family | — | /shop/women/skin-care/ | — | — | Joi skin line |
| Luxe Skin Cream | buyable | Skin Care (Women) | /shop/women/skin-care/luxe-skin-cream/ | $99/mo | published | not stated (hormone-informed) · cream · women |
| GHK-Cu Peptide Skin Cream | buyable | Skin Care (Women) | /shop/women/skin-care/ghk-cu-skin-cream/ | $79/mo | published | GHK-Cu peptide · cream · women |
| Essentials Skin Cream | buyable | Skin Care (Women) | /shop/women/skin-care/essentials-skin-cream/ | $59/mo | published | estriol · cream · women |
| Gear / Merch | family | — | /gear/shop/clothing/ | — | on-request | Hoodies, T-Shirts, Sweatpants (/gear/shop/clothing/); Water Bottle, Duffle Bag (/gear/shop/extras/) — prices not captured |
| Fertility | buyable | — | /fertility/ | — | on-request | coming soon (teased, not yet purchasable) |

## Verbatim anchors

- **TRT inclusion + tiers** (trt_men.md): *"Monthly subscription starts from just **$99** and includes all medications, clinician consults and follow-up labs. No hidden fees. Easy cancellations."* — Tiers: $149/mo @ 3 months (upfront $447) · $129/mo @ 6 months (upfront $774) · $99/mo @ 12 months (upfront $1,188). *"Start now for $75."*
- **$1/mo add-on gating** (trt_men.md): *"Access to the $1 add on program for oral sildenafil, oral tadalafil, oral finasteride, and oral minoxidil is only available to patients who have an active TRT or Enclomiphene subscription and only if a licensed clinician determines the medication is medically appropriate… only available in the following states: AK, AZ, CA, CO, DC, FL, HI, ID, IL, IA, KS, KY, ME, MD, MA, MI, MN, MS, MO, MT, NE, NH, NJ, NM, NY, ND, OH, OR, PA, RI, SD, TN, TX, UT, VT, VA, WA, WV, WI, WY."* Competitor contrast on same page: sildenafil $20–$50/mo, tadalafil $30–$80/mo, finasteride $20–$40/mo, minoxidil $20–$90/mo elsewhere → **decides `partial`** (the $1 is real but gated behind the TRT/Enclo subscription).
- **Compounded GLP-1** (glp1.md): semaglutide *"$199/mo (first month $99) billed quarterly. Includes your medication, dosing support, clinician consultations, and health coaching"*; tirzepatide *"$299/mo (first month $149) billed quarterly. Includes your medication…"* → meds included = **`published`**. *"Joi + Blokes provides access to GLP-1s exclusively through U.S.-licensed pharmacies… compounded… not been evaluated by the FDA."*
- **Zepbound®** (glp1.md / catalog): *"$99/mo billed quarterly (plus the cost of meds)"* + *"Zepbound® and Mounjaro® are not compounded and are registered trademarks of Eli Lilly."* The "plus the cost of meds" = **decides `partial`** (program fee only). **Molecule audit:** the captured /glp-1/ page discusses tirzepatide and names Zepbound as an Eli Lilly brand but does **not** explicitly bind "Zepbound = tirzepatide" for this SKU → recorded `not stated for SKU`, not inferred from the brand.
- **HRT/BHRT model** (hrt_women.md): *"For $50/month (billed quarterly), all follow-up labs and clinician visits are included. Medications are billed separately and are delivered to your door."* Forms: Estrogen Injection $59/mo · Cream $69/mo; Progesterone Capsule $49/mo · Cream $69/mo · Patch $89/mo; Testosterone Cream $69/mo · Suppository $89/mo; (also) Capsule $54/mo. *"Cancel anytime after the first 3 months."* → care fee + separate med cost = **decides `partial`**.
- **Lab packs + phlebotomy** (complete_panel.md): *"Single Lab $149 · Lab Two Pack $298 · Lab Four Pack $596"*; *"upgrade to an in-home blood draw for a $100 fee"* (FAQ) / *"mobile phlebotomy option for an additional $99"* (NY/NJ/RI). Outside-lab review consult $59.

## Deep blocks

Earned where a roster row can't carry the structure. (No per-flagship PDP-anatomy block — not requested this run.)

### Testosterone Replacement Therapy — the commitment-tier ladder
Spine: one therapy, three prices set by lock-in length, all **all-in** (meds + consults + quarterly labs in the monthly figure). $149/mo (3-mo, $447 upfront) → $129/mo (6-mo, $774) → $99/mo (12-mo, $1,188); a "$75 start" entry. testosterone cypionate, injection, men only; cannot ship to AL/AR/CT/DE/GA/HI/LA/MN/MO/MS/NC/ND/OK/PA/RI/SC. The TRT (or Enclomiphene) subscription is the **key that unlocks the $1/mo add-ons** — the retention lever below. Hero render: `captures/2026-06-04/images/trt.png` (black "TESTOSTERONE CYPIONATE" vial).

### Compounded GLP-1 vs Zepbound® — two pricing architectures in one line
The weight-loss line splits cleanly. **Compounded** semaglutide ($199/mo, first month $99) and tirzepatide ($299/mo, first month $149) are **all-in** — *"Includes your medication"* → `published`. **Zepbound®** is a $99/mo *program fee* with meds bought **separately** ("plus the cost of meds") → `partial`. The distinction matters: a price-shopper comparing "$99/mo" Zepbound against "$199/mo" compounded is comparing a program fee to an all-in price. Compounded = not FDA-approved, dispensed via U.S.-licensed pharmacies; brand GLP-1s may be insurance-eligible. Hero render: `captures/2026-06-04/images/compounded-glp-1.png` (white "COMPOUNDED GLP-1" vial).

### Hormones (BHRT) — why it's `partial`
Unlike TRT's single all-in number, BHRT shows a **$50/mo care fee** (labs + visits, billed quarterly) with **medications billed separately** per chosen form. The catalog's "from $59/mo" is one form (estrogen injection), not the all-in. Full form matrix: estrogen (injection $59 / cream $69), progesterone (capsule $49 / cream $69 / patch $89), testosterone (cream $69 / suppository $89). Bioidentical estrogen·progesterone·testosterone; women; cancel anytime after the first 3 months. So the true cost = $50 care + form price → the roster's `partial` token.

### The $1/mo ED + hair add-on program — the differentiator
Active TRT/Enclomiphene members can add **oral sildenafil, tadalafil, finasteride, and minoxidil for $1/mo each** (clinically-gated, 39-state list). The TRT page benchmarks these at **$20–$90/mo elsewhere** and names **Hims, Hone, Maximus** directly. Economically it's a near-free LTV/retention lever bolted onto the hormone subscription — the reason these rows are `partial` (the $1 is real but only exists *inside* an active TRT/Enclo plan), not `published` standalone SKUs.

### Diagnostic labs — the wedge, with pack pricing
The Complete Hormone Panel anchors at **$149** (56 biomarkers + 30-min clinician visit) and is sold in **multi-packs** for ongoing monitoring: Two-Pack $298, Four-Pack $596 (no per-unit discount — straight multiples). Step-up panels: Advanced $399 (71 biomarkers + full thyroid + biological age), Comprehensive $699 (110). Draw via at-home Tasso kit or Quest/BioReference; optional in-home phlebotomist +$99–$100 (NY/NJ/RI). Most Rx cards carry "Lab Required," so a panel is the practical first purchase. No clean isolated product render exists for the panels (the PDP uses results/lifestyle imagery) — hero skipped on true absence.

## Provenance

- **Pages read (cited captures, all `store/joiandblokes-com/captures/2026-06-04/`):** shop_men.md + shop_women.md (roster backbone — every catalog price), complete_panel.md (lab packs + phlebotomy), trt_men.md (TRT tiers + $1 add-on), glp1.md (compounded vs Zepbound, molecules), hrt_women.md (BHRT $50+meds matrix), mens_labs.md + womens_labs.md (panel tiers).
- **Scope:** all distinct buyable products enumerated at the indexed (product) level; men's/women's mirrored SKUs collapsed to one row + gender tag (a project-local de-dup decision — see `### Run profile`). Gear/merch noted but not price-enumerated (no PDP captured); per-state (NY/NJ) price variants noted, not enumerated.
- **Verify:** every `$` figure is greppable in a cited 2026-06-04 capture (offeringscheck pass condition).
- **Point-in-time:** prices are LIST; the sitewide "MENSHEALTH 25% OFF + 65% OFF LABS" promo applies only at checkout via code; a NY/NJ geo modal serves different pricing.
- **Run profile:** non-vanilla — express opt-in `offerings.md` for a telehealth company, with **flagship hero product images** captured (`captures/2026-06-04/images/`: trt.png, compounded-glp-1.png, enclomiphene.png, luxe-skin-cream.png, product-family.jpg) and referenced from the deep blocks/overview. One project-local convention used: gendered mirror-SKUs collapsed to a single product row.
