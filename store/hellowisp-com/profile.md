---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: hellowisp.com
name: Wisp
aliases: []
legal_entity: "wisp, Inc."            # © 2026 wisp, Inc. (footer)
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/hellowisp/
  facebook: https://www.facebook.com/hellowisp/
  youtube: https://www.youtube.com/channel/UCZJouhIxnJpFa9QBjvdehpA
  tiktok: https://www.tiktok.com/@hellowisp
  spotify: https://open.spotify.com/show/2XRlYXyHKH1JpC5HozXvZk   # "Wispers" podcast — a channel they operate
external:
  trustpilot: https://www.trustpilot.com/review/hellowisp.com

# Capture meta
captured_at: 2026-06-16
capture_method: firecrawl
site_notes: "Next.js + Strapi CMS (cms.hellowisp.io). Catalog lives at /products/<slug> (~140 priced SKUs); the /shop/<category> index pages carry the product cards WITH verbatim prices (Starting at $X) + category tags + slugs — roster off the index pages, no need to scrape 200 PDPs. Map returns ~200 /products URLs but the surplus is paid-media/A-B landing-page DUPLICATES of core SKUs (slug suffixes -hgs / -paidmedia / -vwo / -statc) + merch (hats/totes) + quiz entry points; dedupe to the index-surfaced slug. Full shop taxonomy lives in the FOOTER (the header <nav> 'Shop' is a radix client-rendered flyout — its tree is NOT in the header HTML; rebuild nav from footer + screenshot). A/B: VWO (care-*-vwo slugs on the Herpes line). /pricing is a thin page (herpes + a few vaginal SKUs only)."
key_pages:
  shop_home: /shop-home
  how_it_works: /how-it-works
  about: /about
  pricing: /pricing
  provider_credentials: /provider-credentials
  testing_diagnostics: /at-home-testing-kits
  membership: /products/wisp-plus-membership
  vaginal_health: /shop/vaginal-health
  reproductive_health: /shop/reproductive-health
  std: /shop/std
  herpes: /shop/herpes
  weight_care: /shop/weight-care
  wellness_essentials: /shop/wellness-essentials
  menopause: /shop/menopause
  longevity: /longevity-healthy-aging
unverified_fields:
  - "Founding year / founders — not stated on captured pages (deep-research edge)."
  - "Pharmacy structure — site says 'independent physician', 'pharmacy of your choice', and 'partner pharmacies', but also 'ships directly from our pharmacy' for home delivery; ownership not reconciled, so pharmacy_model recorded as third-party posture only (telehealth.md Fulfillment carries the verbatim claims)."
  - "Prices/IA are a point-in-time snapshot, not fixed — VWO A/B instrumentation (care-*-vwo slugs) + active promo codes (WELCOME15, TREAT, TREAT 25%); per-SKU floors and which modules render can shift run-to-run."

# Description
description: "A women's-and-partners telehealth brand delivering prescription, OTC, and at-home-test care across vaginal, reproductive, sexual, menopause, weight, and longevity health via an asynchronous model, with same-day pharmacy pickup or free discreet delivery."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://hellowisp.com/images/logo/wisp.svg
logos:
  wordmark: { src: https://hellowisp.com/images/logo/wisp.svg, w: 563, h: 240 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=hellowisp.com&sz=256", px: 180, transparent: false }   # inverted-triangle "v" mark on a baked white square
  og:       { src: "https://cms.hellowisp.io/uploads/Meta_Hero_1500x1000_f538e24836.jpg", w: 1500, h: 1000 }
brand_colors: { primary: "#F24F46", accent: "#F5BFE7", background: "#FFF6EE" }   # coral logotype on cream; pink secondary. (branding payload mislabels primary as the cream bg + accent as a #E72323 CTA red — true mark hue is the #F24F46 from the wordmark SVG)
fonts: [Work Sans]                   # heading (branding payload); body ranks a generic Arial/Verdana fallback first — not trusted
color_scheme: light
design_framework: next.js            # __NEXT_DATA__ + /_next/ in rawHtml (branding payload not consulted)
---

## Overview

Wisp (legally **wisp, Inc.**) is a direct-to-consumer telehealth brand positioned as a "complete health platform built for women, their partners, and allies," available in all 50 states and **"trusted by over 1.8 million people nationwide"** (self-reported). It pairs prescription treatment, evidence-based OTC/supplement products, and at-home diagnostic kits across a wide women's-health catalog — its origin and still-leading wedge is **vaginal health** (BV, yeast, UTI), extended outward into reproductive health, STDs/STIs, herpes, menopause, weight care (GLP-1), longevity, migraine, skincare, and sexual wellness.

The model is explicitly **asynchronous** ("our asynchronous care model means no appointments and no waiting rooms"): a customer picks a treatment or takes a Symptoms Quiz, a licensed provider reviews the intake (and follows up by phone/secure chat only "if needed"), and an approved prescription is **sent same-day to a local pharmacy for pickup (avg. 3–5 hrs)** or **shipped free + discreet** to the home. Most products are HSA/FSA-eligible.

## What they offer

Roster-grade per-SKU detail (≈140 SKUs) lives in [`offerings.md`](offerings.md); breadth + shape here. Lines, each with verbatim entry prices (one-time or subscription; an optional **Wisp+** discount membership layers 15–25% off):

- **Vaginal health (the wedge):** BV antibiotics **from $15** `[published]`, yeast antifungals (Fluconazole) **from $45** `[published]`, UTI antibiotics **from $65** `[published]`, vaginitis, Metronidazole/Clindamycin creams, vaginal dryness (Estradiol **from $20**)
- **Reproductive health:** ~16 generic **birth control** pills **from $15** `[published]`, the patch **from $12**, NuvaRing **from $22**, emergency contraception (generic Plan B **from $12.50**, Ella), "Delay Your Period" (Norethindrone **from $39**)
- **STD/STI treatment & at-home testing:** chlamydia/gonorrhea/trich/Mgen/ureaplasma treatments **$39 each** `[published]`, DoxyPEP **from $22**, plus at-home test kits — 3-Panel STI **$99**, 5-Panel STI **$179**, HIV/HPV/syphilis/herpes swabs `[published]`
- **Herpes (oral & genital):** Valacyclovir/Acyclovir outbreak & suppressive **from $10/mo** `[published]`, antiviral herbals, L-Lysine (note: VWO A/B-tested line)
- **Weight care (GLP-1):** Compounded Sublingual Semaglutide **$225/mo** `[published]`, Weight Care Consult **$99**, brand GLP-1s referenced (Wegovy, Zepbound, Saxenda); Metformin **from $24**
- **Menopause & longevity:** menopause consult **$99**, Estriol face cream, NAD+ injections/spray, Glutathione, Low-Dose Naltrexone, Tru Niagen **$127**, Metformin/Spironolactone for healthy aging
- **Wellness essentials (largest line, ~44 SKUs):** sexual wellness (Lift for Her/Him **from $66**, OMG! arousal cream, lubes), skincare (Tretinoin, Hydroquinone, acne creams), probiotics, hair (oral Minoxidil, Latisse), supplements, Zofran anti-nausea **from $24**
- **Diagnostics, fertility, migraine, bundles:** at-home hormone/gut/anemia panels (**$119–$279**), Proov/PherDal fertility kits, migraine consult **$60**, and treat-relieve-prevent bundles **from $55–$74**

Brand-partner products are resold alongside Wisp's own: **Stripes Beauty** (menopause), **TBD** (HPV), **Daye** (microbiome), **Proov / PherDal** (fertility), **Tru Niagen** (longevity).

## How it works / model

1. **Explore care** — browse a treatment or take the **Symptoms Quiz**.
2. **Provider review** — a licensed MD or NP reviews the medical intake; in 8 states (AR, DC, DE, KS, MS, RI, VT, WV) a **video visit is required by law**, otherwise async; provider follows up "if needed" by phone/secure chat.
3. **Fulfillment** — Rx sent to the patient's chosen local **pharmacy for same-day pickup** (avg 3–5 hrs), or **shipped free + discreet** from the fulfillment pharmacy; compounded/weight-care items are delivery-only.
4. **Pay** — per-product (one-time or subscription); **HSA/FSA accepted** on most products; insurance can be applied at pharmacy pickup; a **Wisp GoodRx discount card** lowers out-of-pocket pharmacy cost. The consult fee is **included** in the prescription price.

Money is made on product/Rx margin + subscription refills + the optional **Wisp+** membership ($30 for a 3- or 12-month term → 15%/20%/25% off for 1/2/3+ items; excludes the abortion product, menopause & weight-care consults/products, and brand-partner goods).

## Positioning & audience

Targets **women and their partners** across every life stage ("your body, your timeline, your terms"), against in-person OB/GYN waits and lighter wellness-telehealth. Claimed edge: speed (same-day Rx), continuity ("care that evolves with you"), breadth (one platform for urgent + ongoing needs), and a **zero-judgment, stigma-breaking** brand voice. Tone is modern, candid, and sex-positive.

## Nav structure

Top nav: **Shop** (mega-flyout, client-rendered) · Symptoms Quiz — /symptoms-quiz · How It Works — /how-it-works · Blog — /blog · About — /about · Login · Cart. Shop taxonomy (from footer, the complete tree):

```
- Vaginal Health — /shop/vaginal-health
  - UTI — /shop/vaginal-health/uti
  - Bacterial Vaginosis — /shop/vaginal-health/bacterial-vaginosis
  - Yeast Infection — /shop/vaginal-health/yeast-infection
  - Vaginal Dryness — /shop/vaginal-health/vaginal-dryness
- Herpes — /shop/herpes
  - Cold Sores — /shop/herpes/cold-sores
  - Genital Herpes — /shop/herpes/genital-herpes
- Reproductive Health — /shop/reproductive-health
  - Emergency Contraception — /shop/reproductive-health/emergency-contraception
  - Birth Control — /shop/reproductive-health/birth-control
  - Control Your Cycle — /shop/reproductive-health/control-your-cycle
- Prevention — /shop/prevention   (Equalizing/Basic Probiotics, Boric Acid, D-Mannose, Zofran)
- Weight Care — /shop/weight-care   (Weight Care Consult, Anti-Nausea)
- Wellness Essentials — /shop/wellness-essentials
  - Better Sex — /shop/wellness-essentials/better-sex
  - Skincare — /shop/wellness-essentials/skincare
  - Supplements — /shop/wellness-essentials/supplements
  - Balancing Wash — /products/balancing-wash
- STD Treatment & Prevention — /shop/std   (Chlamydia, Gonorrhea, Trichomoniasis, DoxyPEP, At-Home STI/STD Testing)
- Fertility — /shop/fertility   (Prenatal Vitamins, Fertility Thermometer, Proov kits, PherDal insemination)
- Complete Care — /shop/wisp-care   (At-Home Testing, Sexual Health Consult, STD Consult, Menopause Consult, Wisp+ Membership, Subscribe & Save)
```

Additional landing hubs: At-Home Testing & Diagnostics — /at-home-testing-kits · Longevity & Healthy Aging — /longevity-healthy-aging · PCOS Support — /pcos-support · Menopause — /shop/menopause · Migraine Care — /shop/migraine-care · Bundles — /shop/bundles.

## Credibility & proof

- **LegitScript-certified** (footer seal #3454890); states "HIPAA compliant" data handling and "PCI compliant" payment processing (self-reported, FAQ).
- **Named clinicians:** Dr. Shannon Chatham, DO (Medical Director, board-certified family medicine); Andrea Sleeth, WHNP-BC, MSCP. A `/provider-credentials` page lists per-state medical-license numbers for prescribing physicians (e.g. Justin Allen, M.D. across all 50 states).
- **Press logos (self-presented):** Inc. Best in Business 2025, CNN, Time Best Inventions 2025, New York Times, Forbes, Fast Company, Healthline.
- **Self-reported scale:** "trusted by over 1.8 million people nationwide" / "1.8M+."
- **Reviews:** embedded Trustpilot widget shows **"4.3 out of 5"** (membership/PDP pages) and **"4 out of 5"** (homepage) — self-embedded, verbatim, not independently verified here.
- **Cause partners (affiliation, not ownership):** SIECUS, NY Birth Control Access Project, Abortion Freedom Fund, WRRAP.

## Visual & brand impression

Soft, editorial DTC aesthetic: warm **cream (#FFF6EE)** canvas, a **coral/red (#F24F46)** brand mark and CTAs, with a pink secondary and motion-blur lifestyle photography of women. The lowercase "wisp" wordmark and a minimal inverted-triangle "v" logomark read modern and approachable; iconography is thin-line and friendly. Overall the design feels polished, premium-DTC, and intentionally de-stigmatizing — clinical credibility delivered in a calm, body-positive wrapper rather than a sterile medical one.

## Strategic read

Wisp is unusually **broad for a women's-health DTC** — ~140 SKUs spanning Rx, OTC, supplements, devices, and resold third-party kits — using a fast **async** engine and a catalog-storefront (Next.js + Strapi) more like an e-commerce brand than a single-condition clinic. The wedge is the high-recurrence vaginal-health complaints (BV/UTI/yeast) that drive urgent, repeat demand; the platform then cross-sells into ongoing categories (menopause, weight, longevity) for continuity revenue. Notable nuances: it is **women-and-partners** (it sells men's BV partner therapy and men's sexual-wellness, not men-only), it **resells partner brands** alongside its own line, and it carries an explicit reproductive-justice/abortion-access posture rare in the cohort. The VWO A/B testing and dense promo machinery confirm a marketing-led growth motion.

## Provenance

- **Pages:** 23 captured via Firecrawl (homepage rich pass + 14 /shop & landing index pages + /how-it-works, /about, /pricing, /provider-credentials + 4 PDPs: bv-antibiotics, wisp-plus-membership, compounded-sublingual-semaglutide). Catalog enumerated off the priced /shop index pages.
- **Verify:** all sourceURLs matched; all 23 body md5s unique; no junk soft-404s.
- **Credits:** 24 (1 map + 23 scrapes); all base 1cr, no enhanced-proxy/PDF overage.
- **Couldn't get:** founding year/founders (not on site); definitive pharmacy ownership structure (mixed page language — see unverified_fields + telehealth.md).
- **Run profile:** guided/express — FULL telehealth path: +telehealth.md cohort pack, +offerings.md (full ~140-SKU roster), +logos module; emphasis "vast catalog — enumerate full roster at indexed level."
