---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: hellowisp.com
captured_at: 2026-06-16
enumeration: indexed-complete
site_notes: "Catalog lives at /products/<slug> on a Next.js + Strapi (cms.hellowisp.io) storefront. The /shop/<category> INDEX pages are the authoritative priced backbone — each product card carries name + a 'Category | Prescription/Over-The-Counter/Supplements' tag + verbatim 'Starting at $X' price + slug, so the roster builds off index pages with NO per-PDP sweep. The map's ~200 /products URLs over-count: the surplus is paid-media / A-B landing-page DUPLICATES of core SKUs (slug suffixes -hgs / -paidmedia / -vwo / -statc), merch (hats/totes), and quiz entry points — dedupe to the index-surfaced slug. Prices A/B-flicker (VWO on the Herpes line: care-*-vwo) and run under rotating promo codes (WELCOME15, TREAT 25%) — re-check next run. Wisp resells brand-partner SKUs (Stripes Beauty, TBD, Daye, Proov, PherDal, Tru Niagen) alongside its own line; these are excluded from the Wisp+ discount."
---

## Portfolio overview

Wisp is a broad women's-and-partners telehealth **catalog** — **141 distinct SKUs** across 14 lines, spanning prescription treatment, OTC/supplements, at-home diagnostic kits, sexual-wellness products, and resold brand-partner goods. Shape finding: this is an **e-commerce storefront wearing a clinic's coat** — products are merchandised like a DTC shop (badges, bundles, "Starting at $X" cards, subscribe-to-save) rather than gated behind a consult; the consult is bundled into the Rx price and runs **async**.

Pricing is almost entirely **`published`** (140/141 carry a shown price/floor) — only **NAD+ Injections** is `partial` (the page shows just *"Consult: $25"*, with the injection's all-in set after the consult). Most Rx lines read *"Starting at $X"* because price scales with dose/quantity/cadence (one-time vs subscription) — the shown number is a real published **floor**, not a gated quiz.

**Prominence read** (calibrated): the homepage + shop-home hero grid consistently leads with **Vaginal Health — BV, Yeast, UTI** `[HIGH]` (origin wedge; first cards in every grouping). **Birth control / emergency contraception** and **STD / at-home testing** are the next tier `[MED]` (large dedicated lines, deep nav). Newer pushes — **Longevity & Healthy Aging, Weight Care (GLP-1), Menopause** — carry "NEW" hero/"What's New" placement `[MED]`. Wellness Essentials is the largest line by count (44) but is mostly low-prominence add-on/cross-sell `[LOW]`. *(A/B-tested hero — VWO present — so prominence is point-in-time.)*

## Roster

141 SKUs, complete at the indexed (PDP-slug) level, one row each, grouped by the project-local **Line** column (an added within-company grouping; the 7-column spine precedes it). **What** leads with `molecule · form · access`: molecule is page-attested from the card/title only (else `not stated` — generic birth-control SKUs name the brand, not the molecule); **access** is filled only where the index card's `| Prescription / Over-The-Counter / Supplements` tag was captured, else `not stated` (never inferred). **Parent** is `—` throughout (this catalog has no family→buyable nesting). Prices verbatim, greppable in `captures/2026-06-16/`.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) | Line |
|---|---|---|---|---|---|---|---|
| BV Antibiotics (Tablets or Gel) | buyable | — | `/products/bv-antibiotics` | Starting at $15 | published | not stated · gel · not stated | Vaginal Health |
| Calm Down! Instant Itch Relief for BV & Yeast | buyable | — | `/products/bv-yeast-itch-relief-cream` | $36 | published | not stated · — · not stated | Vaginal Health |
| Clindamycin Cream (Cleocin) | buyable | — | `/products/clindamycin-cream` | Starting at $100 | published | Clindamycin · cream · not stated | Vaginal Health |
| Diflucan, Generic Fluconazole (Yeast Antifungals) | buyable | — | `/products/yeast-antifungals` | Starting at $45 | published | Fluconazole · — · not stated | Vaginal Health |
| Estradiol Vaginal Cream | buyable | — | `/products/estradiol` | Starting at $20 | published | Estradiol · cream · not stated | Vaginal Health |
| Metronidazole Gel (Metrogel) | buyable | — | `/products/metronidazole-gel` | Starting at $90 | published | Metronidazole · gel · not stated | Vaginal Health |
| Non-Hormonal Vaginal Moisturizer | buyable | — | `/products/non-hormonal-moisturizer` | Starting at $60 | published | not stated · topical · not stated | Vaginal Health |
| Online BV Treatment for Men (Metronidazole & Clindamycin) | buyable | — | `/products/bv-male-support` | $99 | published | Metronidazole + Clindamycin · — · not stated | Vaginal Health |
| UTI Antibiotics Online Prescription | buyable | — | `/products/uti-antibiotics` | Starting at $65 | published | not stated · — · not stated | Vaginal Health |
| Vaginitis Treatment | buyable | — | `/products/vaginitis` | Starting at $45 | published | not stated · — · not stated | Vaginal Health |
| Azurette® Birth Control (generic) | buyable | — | `/products/azurette-birth-control` | Starting at $15 | published | not stated · — · not stated | Reproductive Health |
| Birth Control Patch | buyable | — | `/products/birth-control-patch` | Starting at $12 | published | not stated · patch · not stated | Reproductive Health |
| Cyred EQ® Birth Control (generic) | buyable | — | `/products/cyred-eq-birth-control` | Starting at $15 | published | not stated · — · not stated | Reproductive Health |
| Errin® Birth Control (generic) | buyable | — | `/products/errin-birth-control` | Starting at $15 | published | not stated · — · not stated | Reproductive Health |
| Find My Birth Control | buyable | — | `/products/birth-control-quiz-statc` | Starting at $5 | published | not stated · — · not stated | Reproductive Health |
| Junel FE 1/20® Birth Control (generic) | buyable | — | `/products/junel-fe-birth-control` | Starting at $15 | published | not stated · — · not stated | Reproductive Health |
| Kurvelo Birth Control (generic) | buyable | — | `/products/levora-birth-control` | Starting at $15 | published | not stated · — · not stated | Reproductive Health |
| Low-Ogestrel® Birth Control (generic) | buyable | — | `/products/low-ogestrel-birth-control` | Starting at $15 | published | not stated · — · not stated | Reproductive Health |
| Lutera® Birth Control (generic) | buyable | — | `/products/lutera-birth-control` | Starting at $15 | published | not stated · — · not stated | Reproductive Health |
| Microgestin Fe 1.5/30® Birth Control (generic) | buyable | — | `/products/microgestin-fe-birth-control` | Starting at $15 | published | not stated · — · not stated | Reproductive Health |
| Ocella® Birth Control (generic) | buyable | — | `/products/ocella-birth-control` | Starting at $15 | published | not stated · — · not stated | Reproductive Health |
| Ortho Tri-Cyclen Lo® Birth Control (generic) | buyable | — | `/products/ortho-tri-cyclen-lo-birth-control` | Starting at $15 | published | not stated · — · not stated | Reproductive Health |
| Seasonique® Birth Control (generic) | buyable | — | `/products/seasonique-birth-control` | Starting at $15 | published | not stated · — · not stated | Reproductive Health |
| Slynd Birth Control | buyable | — | `/products/slynd-birth-control` | Starting at $25 | published | not stated · — · not stated | Reproductive Health |
| Sprintec® Birth Control (generic) | buyable | — | `/products/sprintec-birth-control` | Starting at $15 | published | not stated · — · not stated | Reproductive Health |
| Tri-Sprintec® Birth Control (generic) | buyable | — | `/products/tri-sprintec-birth-control` | Starting at $15 | published | not stated · — · not stated | Reproductive Health |
| Trivora-28® Birth Control (generic) | buyable | — | `/products/trivora-28-birth-control` | Starting at $15 | published | not stated · — · not stated | Reproductive Health |
| Vaginal Birth Control Ring (Generic NuvaRing®) | buyable | — | `/products/nuvaring` | Starting at $22 | published | not stated · vaginal ring · not stated | Reproductive Health |
| Yaz® Birth Control (generic) | buyable | — | `/products/yaz-birth-control` | Starting at $15 | published | not stated · — · not stated | Reproductive Health |
| 3-Panel Essential STI Test | buyable | — | `/products/essential-sti-urine-test` | $99 | published | not stated · blood/urine panel · at-home test | STD/STI Treatment |
| 3-Site STI Test | buyable | — | `/products/chlamydia-gonorrhea-test` | $149 | published | not stated · test kit · at-home test | STD/STI Treatment |
| 5-Panel STI Test | buyable | — | `/products/5-panel-sti-test` | $179 | published | not stated · blood/urine panel · at-home test | STD/STI Treatment |
| At-Home Vaginal Microbiome Screen by Daye | buyable | — | `/products/vaginal-screening` | $125 | published | not stated · — · at-home test | STD/STI Treatment |
| Chlamydia Treatment Online | buyable | — | `/products/chlamydia` | $39 | published | not stated · — · not stated | STD/STI Treatment |
| DoxyPEP | buyable | — | `/products/doxy-pep` | Starting at $22 | published | not stated · — · not stated | STD/STI Treatment |
| Gonorrhea Treatment | buyable | — | `/products/gonorrhea` | $39 | published | not stated · — · not stated | STD/STI Treatment |
| Herpes (HSV) Test | buyable | — | `/products/hsv-swab-home-test` | $169 | published | not stated · test kit · at-home test | STD/STI Treatment |
| HIV 1 & 2 Blood Test | buyable | — | `/products/hiv-1-2-test` | $99 | published | not stated · test kit · at-home test | STD/STI Treatment |
| HPV At-Home Test Kit by TBD | buyable | — | `/products/hpv-test-kit` | $99 | published | not stated · test kit · at-home test | STD/STI Treatment |
| HPV Test | buyable | — | `/products/hpv-swab-test` | $105 | published | not stated · test kit · at-home test | STD/STI Treatment |
| M. Hominis Treatment | buyable | — | `/products/mhominis` | $39 | published | not stated · — · not stated | STD/STI Treatment |
| Mycoplasma Genitalium (Mgen) Treatment | buyable | — | `/products/mgen` | $39 | published | not stated · — · not stated | STD/STI Treatment |
| Mycoplasma Genitalium Test | buyable | — | `/products/mycoplasma-genitalium-test` | $125 | published | not stated · test kit · at-home test | STD/STI Treatment |
| STI & STD Consult | buyable | — | `/products/std-consult` | $39 | published | not stated · — · consult | STD/STI Treatment |
| Syphilis Test | buyable | — | `/products/syphilis-home-test` | $79 | published | not stated · test kit · at-home test | STD/STI Treatment |
| Trichomoniasis Treatment | buyable | — | `/products/trichomoniasis` | $39 | published | not stated · — · not stated | STD/STI Treatment |
| Ureaplasma Treatment | buyable | — | `/products/ureaplasma` | $39 | published | not stated · — · not stated | STD/STI Treatment |
| Vaginitis Test | buyable | — | `/products/bv-yeast-test` | $159 | published | not stated · test kit · at-home test | STD/STI Treatment |
| At-Home: Anemia Blood Panel | buyable | — | `/products/anemia-panel-at-home` | $194 | published | not stated · blood/urine panel · at-home test | Testing & Diagnostics |
| Mycoplasma & Ureaplasma Test | buyable | — | `/products/mycoplasma-ureaplasma-swab-test` | $149 | published | not stated · test kit · at-home test | Testing & Diagnostics |
| Walk-In: Anemia Blood Panel | buyable | — | `/products/anemia-panel-walk-in` | $119 | published | not stated · blood/urine panel · at-home test | Testing & Diagnostics |
| Wisp Female Hormone Health Panel | buyable | — | `/products/female-hormone-health-panel` | Starting at $229 | published | not stated · blood/urine panel · at-home test | Testing & Diagnostics |
| Wisp Gut Health Panel | buyable | — | `/products/gut-health-panel` | Starting at $279 | published | not stated · blood/urine panel · at-home test | Testing & Diagnostics |
| Acyclovir Cream for Genital Herpes / HSV-1 & HSV-2 | buyable | — | `/products/care-acyclovir-cream-oral-genital` | Starting at $30 | published | Acyclovir · cream · not stated | Herpes |
| AV Defender Herbal Supplement for HSV-1 & HSV-2 | buyable | — | `/products/care-antiviral-all-natural-herbals-hsv` | Starting at $27 | published | not stated · — · not stated | Herpes |
| First Herpes Outbreak Consult / Oral & Genital | buyable | — | `/products/care-herpes-first-outbreak-vwo` | $65 | published | not stated · — · consult | Herpes |
| Genital Herpes / Outbreak & Preventative Treatment for HSV-1 & HSV-2 | buyable | — | `/products/care-valacyclovir-and-acyclovir-genital` | Starting at $10/ month | published | not stated · — · not stated | Herpes |
| Herpes Quiz: Online Treatment & Diagnosis for Oral & Genital Herpes | buyable | — | `/products/care-herpes-quiz` | Starting at $10/month | published | not stated · — · not stated | Herpes |
| L-Lysine for HSV-1 & HSV-2 | buyable | — | `/products/care-l-lysine-hsv` | Starting at $27 | published | L-Lysine · — · not stated | Herpes |
| Lidocaine-Amitriptyline Cream / HSV-1 & HSV-2 | buyable | — | `/products/care-lidocaine-pain-cream-oral-genital` | Starting at $30 | published | Lidocaine · cream · not stated | Herpes |
| Oral & Genital Herpes / Outbreak & Preventative Treatment for HSV-1 & HSV-2 | buyable | — | `/products/care-valacyclovir-and-acyclovir-oral-genital` | Starting at $10/ month | published | not stated · — · not stated | Herpes |
| Oral Herpes / Outbreak & Preventative Treatment for HSV-1 & HSV-2 | buyable | — | `/products/care-valacyclovir-and-acyclovir-oral` | Starting at $10/ month | published | not stated · — · not stated | Herpes |
| Preventative Treatment for HSV-1 & HSV-2 | buyable | — | `/products/care-valacyclovir-and-acyclovir-prevention` | Starting at $10/ month | published | not stated · — · not stated | Herpes |
| Compounded Sublingual Semaglutide Drops 15mL | buyable | — | `/products/compounded-sublingual-semaglutide` | $225/month | published | Semaglutide · sublingual drops · Rx | Weight Care |
| Metformin Prescription for PCOS | buyable | — | `/products/metformin` | Starting at $24 | published | Metformin · — · not stated | Weight Care |
| Weight Care Consult | buyable | — | `/products/weight-care-consult` | $99 | published | not stated · — · consult | Weight Care |
| Wisp Metabolic Support & GLP-1 Boost Capsules | buyable | — | `/products/metabolic-glp-support-capsules` | Starting at $54/ month | published | not stated · capsules · not stated | Weight Care |
| Menopause Consult Online | buyable | — | `/products/menopause-consult` | $99 | published | not stated · — · consult | Menopause |
| Glutathione Injection | buyable | — | `/products/glutathione-injections` | Starting at $125/ month | published | Glutathione · injection · not stated | Longevity |
| Glutathione Nasal Spray | buyable | — | `/products/glutathione-nasal-spray` | Starting at $130 | published | Glutathione · nasal spray · not stated | Longevity |
| Low-Dose Naltrexone Capsules | buyable | — | `/products/naltrexone-hci-capsules` | Starting at $75 | published | Naltrexone · capsules · not stated | Longevity |
| NAD+ Injections | buyable | — | `/products/nad-injection-solution` | Consult: $25 | partial | NAD+ · injection · not stated | Longevity |
| NAD+ Nasal Spray | buyable | — | `/products/nad-nasal-spray` | Starting at $150 | published | NAD+ · nasal spray · not stated | Longevity |
| Complete Testing System by Proov | buyable | — | `/products/proov-complete-testing-system` | $99.99 | published | not stated · test kit · at-home test | Fertility |
| Fertility Thermometer | buyable | — | `/products/fertility-thermometer` | $39.99 | published | not stated · device · not stated | Fertility |
| Hers & His Advanced Fertility Kit by Proov | buyable | — | `/products/proov-hers-and-his-fertility-starter-kit` | $169.99 | published | not stated · multi-item · bundle | Fertility |
| The PherDal® At Home Insemination Kit | buyable | — | `/products/the-pherdal-kit` | $199 | published | not stated · multi-item · bundle | Fertility |
| Wisp Prenatal Vitamins | buyable | — | `/products/prenatal-vitamins` | Starting at $14 | published | not stated · supplement · not stated | Fertility |
| Migraine Care Consult | buyable | — | `/products/migraine-consult` | $60 | published | not stated · — · consult | Migraine |
| Bachelorette Bundle Pack | buyable | — | `/products/better-together-multipack` | Starting at $75 | published | not stated · multi-item · bundle | Wellness Essentials |
| Bimatoprost (generic Latisse) | buyable | — | `/products/latisse` | Starting at $28 | published | Bimatoprost · — · not stated | Wellness Essentials |
| Boric Acid Suppositories | buyable | — | `/products/boric-acid` | Starting at $27 | published | Boric Acid · suppository · not stated | Wellness Essentials |
| Brighten Up! Hydroquinone Face Cream (5%) | buyable | — | `/products/hydroquinone-cream` | $90 | published | Hydroquinone · cream · not stated | Wellness Essentials |
| Clear Up! Prescription Acne Cream (Clindamycin + Retin A) | buyable | — | `/products/acne-cream` | Starting at $75 | published | Clindamycin · cream · not stated | Wellness Essentials |
| D-Mannose Capsules | buyable | — | `/products/d-mannose` | Starting at $27 | published | D-Mannose · capsules · not stated | Wellness Essentials |
| Daily Urinary Tract Health Support Capsules | buyable | — | `/products/daily-urinary-tract-support` | Starting at $51 | published | not stated · capsules · not stated | Wellness Essentials |
| Delay & Vacay Bundle | buyable | — | `/products/delay-vacay-bundle` | $70 | published | not stated · multi-item · bundle | Wellness Essentials |
| Estriol Face Cream | buyable | — | `/products/estriol-face-cream` | $99 | published | Estriol · cream · not stated | Wellness Essentials |
| Even Out! Hydroquinone Cream (5%) for Body | buyable | — | `/products/hydroquinone-cream-body` | $90 | published | Hydroquinone · cream · not stated | Wellness Essentials |
| Firm Up! Wrinkle Cream / Tretinoin (.04%) | buyable | — | `/products/tretinoin-cream` | Starting at $75 | published | Tretinoin · cream · not stated | Wellness Essentials |
| Hemorrhoid Treatment with Lidocaine | buyable | — | `/products/hemorrhoid-treatment` | Starting at $39 | published | Lidocaine · — · not stated | Wellness Essentials |
| Menopause Survival Kit by Stripes Beauty | buyable | — | `/products/menopause-survival-kit` | $108 | published | not stated · multi-item · bundle | Wellness Essentials |
| OMG! Cream for Female Arousal | buyable | — | `/products/omg-cream` | Starting at $11 | published | not stated · cream · not stated | Wellness Essentials |
| Oral Minoxidil | buyable | — | `/products/oral-minoxidil` | Starting at $36 | published | Minoxidil · — · not stated | Wellness Essentials |
| Oral Spironolactone | buyable | — | `/products/spironolactone` | Starting at $24 | published | Spironolactone · supplement · not stated | Wellness Essentials |
| Original Harmonizing Lube | buyable | — | `/products/harmonizing-lube` | Starting at $10 | published | not stated · lubricant · not stated | Wellness Essentials |
| pH Balanced Wipes | buyable | — | `/products/ph-balancing-wipes` | Starting at $42 | published | not stated · wipes · not stated | Wellness Essentials |
| pH Balancing Feminine Wash | buyable | — | `/products/balancing-wash` | Starting at $14 | published | not stated · wash · not stated | Wellness Essentials |
| Pleasure Bundle (OMG!) | buyable | — | `/products/omg-bundle` | $55.20 | published | not stated · multi-item · bundle | Wellness Essentials |
| Prescription Whole Body Deodorant | buyable | — | `/products/whole-body-deodorant` | Starting at $132 | published | not stated · topical · not stated | Wellness Essentials |
| SiderAL® Forte Iron Supplement | buyable | — | `/products/sucrosomial-iron` | Starting at $80/ month | published | not stated · supplement · not stated | Wellness Essentials |
| Slow the Grow! Prescription Facial Hair Reduction Cream (Eflornithine Hydrochloride 13.9%) | buyable | — | `/products/eflornithine-facial-hair-cream` | Starting at $58/ month | published | Eflornithine · cream · not stated | Wellness Essentials |
| The Crown Pleaser by Stripes Beauty | buyable | — | `/products/the-crown-pleaser` | $40 | published | not stated · — · not stated | Wellness Essentials |
| The Full Monty by Stripes Beauty | buyable | — | `/products/full-monty` | $65 | published | not stated · — · not stated | Wellness Essentials |
| The Inside Addition by Stripes Beauty | buyable | — | `/products/the-inside-addition` | $40 | published | not stated · — · not stated | Wellness Essentials |
| Toy-Safe Harmonizing Lube | buyable | — | `/products/toy-safe-harmonizing-lube` | Starting at $12 | published | not stated · lubricant · not stated | Wellness Essentials |
| Tru Niagen® 300mg | buyable | — | `/products/tru-niagen` | $127 | published | not stated · — · not stated | Wellness Essentials |
| Urinary Tract Cleansing Mix | buyable | — | `/products/urinary-tract-cleansing-mix` | Starting at $60 | published | not stated · — · not stated | Wellness Essentials |
| Urinary Tract Duo | buyable | — | `/products/urinary-tract-duo` | Starting at $90 | published | not stated · — · not stated | Wellness Essentials |
| Vag of Honor by Stripes Beauty | buyable | — | `/products/vag-of-honor` | $50 | published | not stated · — · not stated | Wellness Essentials |
| Vulva Coco Cream | buyable | — | `/products/vulva-coco-cream` | Starting at $15 | published | not stated · cream · not stated | Wellness Essentials |
| Wisp Basic Probiotics | buyable | — | `/products/daily-probiotics` | Starting at $9 | published | not stated · capsules · not stated | Wellness Essentials |
| Wisp Dream Sleep Aid | buyable | — | `/products/sleep-supplements` | Starting at $35/ month | published | not stated · — · not stated | Wellness Essentials |
| Wisp Equalizing Probiotics | buyable | — | `/products/equalizing-probiotics` | Starting at $18/ month | published | not stated · capsules · not stated | Wellness Essentials |
| Wisp Lift for Couples | buyable | — | `/products/lift-for-her-him-bundle` | $115 | published | not stated · — · not stated | Wellness Essentials |
| Wisp Lift For Her | buyable | — | `/products/lift-for-her` | Starting at $66 | published | not stated · — · not stated | Wellness Essentials |
| Wisp Lift For Him | buyable | — | `/products/lift-for-him` | Starting at $66 | published | not stated · — · not stated | Wellness Essentials |
| Wisp Mist Toy Cleaning Spray | buyable | — | `/products/wisp-mist-toy-cleaning-spray` | Starting at $12 | published | not stated · spray · not stated | Wellness Essentials |
| Wisp Revive Collagen Tablets | buyable | — | `/products/revive-collagen` | Starting at $22/ month | published | not stated · tablets · not stated | Wellness Essentials |
| Wisp Thrive Creatine Tablets | buyable | — | `/products/thrive-creatine` | Starting at $15/ month | published | Creatine · tablets · not stated | Wellness Essentials |
| Wisp Topical Spironolactone Prescription (Acne Treatment) | buyable | — | `/products/topical-spironolactone` | Starting at $39 | published | Spironolactone · supplement · not stated | Wellness Essentials |
| Wisp Vaginal Health Probiotics | buyable | — | `/products/vaginal-probiotics` | Starting at $30/ month | published | not stated · capsules · not stated | Wellness Essentials |
| Zofran (Ondansetron) / Nausea Relief | buyable | — | `/products/zofran` | Starting at $24 | published | Ondansetron · — · not stated | Wellness Essentials |
| AV Defender Herbal Supplement / HSV-2 | buyable | — | `/products/antiviral-all-natural-herbals` | Starting at $27 | published | not stated · — · not stated | Prevention |
| L-Lysine / HSV-2 | buyable | — | `/products/l-lysine` | Starting at $27 | published | L-Lysine · — · not stated | Prevention |
| Sexual Health Consult | buyable | — | `/products/wispcare-consult` | Starting at $69 | published | not stated · — · consult | Complete Care |
| Banish BV Bundle | buyable | — | `/products/treat-relieve-prevent-bv` | Starting at $64 | published | not stated · multi-item · bundle | Bundles |
| Beat the Yeast Bundle | buyable | — | `/products/treat-relieve-prevent-yeast` | Starting at $64 | published | not stated · multi-item · bundle | Bundles |
| Buh-Bye UTI Bundle | buyable | — | `/products/treat-relieve-prevent-uti` | Starting at $60 | published | not stated · multi-item · bundle | Bundles |
| BV & Yeast Bundle | buyable | — | `/products/bv-yeast-bundle` | $74.40 | published | not stated · multi-item · bundle | Bundles |
| cUTIe Emergency Kit - Symptom Relief | buyable | — | `/products/cutie-kit` | $35 | published | not stated · multi-item · bundle | Bundles |
| Delay Your Period & Zofran Bundle | buyable | — | `/products/norethindrone-zofran-bundle` | $52.80 | published | not stated · multi-item · bundle | Bundles |
| DoxyPEP & Zofran Bundle | buyable | — | `/products/doxypep-zofran-bundle` | $57.60 | published | not stated · multi-item · bundle | Bundles |
| Essentials Bundle | buyable | — | `/products/essentials-bundle` | Starting at $27 | published | not stated · multi-item · bundle | Bundles |
| Herpes Hero (HSV-1 & HSV-2) - Episodic Bundle | buyable | — | `/products/treat-relieve-prevent-herpes-episodic` | Starting at $60 | published | not stated · multi-item · bundle | Bundles |
| Herpes Hero (HSV-1 & HSV-2) - Suppressive Bundle | buyable | — | `/products/treat-relieve-prevent-herpes-suppressive` | Starting at $66.40 | published | not stated · multi-item · bundle | Bundles |
| No Thank You, Nausea Bundle | buyable | — | `/products/treat-relieve-prevent-zofran` | $24 | published | not stated · multi-item · bundle | Bundles |
| Wisp Lift for Him & DoxyPEP Bundle | buyable | — | `/products/lift-for-him-doxypep-bundle` | $110.40 | published | not stated · multi-item · bundle | Bundles |
| Delay Your Period (Norethindrone Acetate Tablets) | buyable | — | `/products/norethindrone` | Starting at $39 | published | Norethindrone · tablets · not stated | Other |
| Levonorgestrel (Generic PLAN B) | buyable | — | `/products/plan-b` | Starting at $12.50 | published | Levonorgestrel · — · not stated | Other |
| wisp-plus-membership | buyable | — | `/products/wisp-plus-membership` | Starting at $30 | published | not stated · — · membership | Other |

### Verbatim anchors

Footnotes / exact strings the roster points at (quoted from captured pages):

- **Wisp+ discount tiers** (`/products/wisp-plus-membership`): *"15% off one item · 20% off two items · 25% off three or more items"*; *"Starting at $30 — Choose from a 3 or 12 month subscription."* Exclusions: *"Offer excludes the medical abortion product, menopause & weight care consults and products, and products offered on hellowisp.com by brand partners (TBD, Pherdal, Tru Niagen)."*
- **Herpes pricing ladder** (`/pricing`, verbatim): *"Acyclovir (taken just during outbreaks) $15/Month · Valacyclovir (taken just during outbreaks) $20/Month · Acyclovir (taken everyday) $20/Month · Valacyclovir (taken everyday) $25/Month."* (The roster's *"Starting at $10/ month"* herpes floor is the index-card A/B/VWO variant; /pricing shows the $15–$25 ladder.)
- **Vaginal treatment pricing** (`/pricing`, verbatim): *"Sulfamethoxazole-Trimethoprim (Bactrim) $65 · Nitrofurantoin (Macrobid) $65 · Metronidazole (Flagyl, Nuvessa) $15/Month · Metronidazole Gel (MetroGel) $60/Month · Fluconazole 150mg (Diflucan) $15/Month."*
- **Compounded Sublingual Semaglutide** (`/products/compounded-sublingual-semaglutide`): *"$225/ month"*, *"In Stock"*, *"Available for delivery only."* Compounding footnote: *"Compounded drugs are not FDA approved and do not undergo FDA safety, efficacy, or quality review… it has not yet been tested within the human body."*
- **NAD+ Injections** (`/longevity-healthy-aging`): only price shown is *"Consult: $25"* → `partial` (injection all-in set post-consult).
- **Molecule audit (`not stated` rows):** generic birth-control SKUs (Yaz, Sprintec, Lutera, etc.) name the **brand** on the card, not the molecule → `not stated` per the no-brand-inference rule. Test kits, bundles, consults, and Wisp-branded wellness SKUs (Lift, OMG!, probiotics, Dream, Thrive) likewise name no molecule on the index card.

## Deep blocks

**One earned** — the rest of the catalog is carried by the roster.

- **Compounded Sublingual Semaglutide (`/products/compounded-sublingual-semaglutide`)** — a genuine disambiguation a roster row can't hold: this is **not** brand Wegovy/Ozempic and **not** the usual subcutaneous compounded semaglutide. It is a **sublingual drop** the page flags as experimental: *"formulated with a base that may help improve absorption through the lining of the mouth. While lab tests using human-derived tissues suggest it may begin working within 15-30 minutes, it has not yet been tested within the human body. Because of this, the effectiveness of this formulation in patients may vary."* + *"Compounded drugs are not FDA approved."* Delivery-only, **$225/month**, lowest dose auto-added then provider-adjusted. Brand GLP-1s (Wegovy, Zepbound, Saxenda) are referenced as alternatives but were not rostered as priced SKUs (consult-gated).

## Provenance

- **Pages read:** the 14 priced `/shop/<category>` + landing index pages (vaginal-health, reproductive-health, std, herpes, weight-care, wellness-essentials, fertility, wisp-care, prevention, menopause, migraine-care, bundles, at-home-testing-kits, longevity-healthy-aging) + `/shop-home` (cross-category master, prominence read) + 3 PDPs (bv-antibiotics, wisp-plus-membership, compounded-sublingual-semaglutide) + `/pricing`. All in `store/hellowisp-com/captures/2026-06-16/`.
- **Scope note — enumerated:** every line rostered at SKU grain off its index page → `enumeration: indexed-complete`. **Not separately rostered (by design):** paid-media / A-B landing-page **duplicate slugs** of rostered SKUs (suffixes -hgs / -paidmedia / -vwo / -statc — same product, different funnel URL); **merch** (stigma/vulva hats, clit tote); **quiz/EC entry points** (ec-quiz, control-your-cycle-quiz, intimate-care-quiz, at-home-testing-quiz, longevity-quiz) which funnel into rostered SKUs; and dose/quantity/cadence **leaf tiers** within a SKU (the "Starting at" floor stands for the line). Brand GLP-1s (Wegovy/Zepbound/Saxenda) appear in copy but are consult-gated, not priced cards — noted, not rostered.
- **Point-in-time caveat:** pricing/IA is a snapshot — **VWO A/B instrumentation** (care-*-vwo) + active promo codes (WELCOME15, TREAT 25%). Per-SKU floors and which modules render can shift run-to-run; /pricing shows a different (higher) herpes ladder than the index-card $10 floor.
- **Run profile:** guided/express — FULL telehealth path; emphasis "vast catalog — enumerate full roster at indexed level." Full 141-SKU roster built off priced index pages (no per-PDP sweep); +telehealth.md cohort pack + logos module written alongside.
