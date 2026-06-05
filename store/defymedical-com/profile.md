---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: defymedical.com
name: Defy Medical
aliases: []
parent: []
owns: []
socials: { facebook: "https://www.facebook.com/DefyMedical/", x: "https://x.com/DefyMedical", instagram: "https://www.instagram.com/defymedical/" }   # JSON-LD sameAs (all three also in footer)
external: { trustpilot: "https://www.trustpilot.com/review/defymedical.com" }   # third-party record; the 5/5 rating itself is in Credibility & proof

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "WordPress (rawHtml: wp-content ×53 + wp-json; theme `defy-medical`; branding.designSystem said 'bootstrap' — ignored per §5.4). Commerce is split across sibling surfaces, NOT this marketing host: Patient Portal/store = defymedicalstore.com, order lookup = patients.defymedical.com, on-demand lab store (with published lab prices) = testdefy.com. Treatment/`/services/*` pages are MARKETING-ONLY — medication prices live behind a paid consult + the gated Patient Portal; the lone on-site published price is Trimix ($1.39–$3.30/injection + $99 consult). Map is ~majority /faq/* content noise (100+ FAQ URLs) — select from homepage links + the /services mega-nav, which fully serializes into homepage markdown (no flyout recovery needed). 'Popular' spans in the nav are the company's own prominence labels."
key_pages:
  services_index: /services
  trt: /services/trt
  hormone_therapy: /services/hormone-therapy
  semaglutide: /services/semaglutide-for-weight-loss
  tirzepatide: /tirzepatide-online
  trimix: /services/trimix-injections
  lab_tests: /services/lab-tests-online   # ordering lives on testdefy.com
  about: /about-us
  team_bios: /about-us/team-bios
  get_started: /get-started
  vendor_information: /about-us/about-us-vendor-information
  tampa_clinic: /tampa-clinic
unverified_fields:
  - "Medication & lab pricing — gated behind a paid consult + the Patient Portal (defymedicalstore.com); only Trimix publishes per-injection pricing on-site. Lab prices live on the separate testdefy.com store (not captured this run)."
  - "Compounded-vs-FDA-brand lane per-SKU — not explicitly labeled; the site says 'FDA-approved active ingredients / USP / GMP' yet offers custom formulations (Trimix/Bimix/Quadmix, BHRT) that are compounded by nature. No 503A/503B statement on captured pages."
  - "LegitScript certification / pharmacy accreditation seals (PCAB/NABP/ACHC) — not found on captured pages."
  - "Headcount, funding, revenue — not on the marketing site (deep-research job)."

description: "A telemedicine clinic delivering TRT, bioidentical hormone therapy, weight-loss GLP-1s, sexual-health, and integrative treatments to men and women, using extended provider consults and comprehensive lab testing to personalize each protocol."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Transactional / One-time   # STRAIN: cohort outlier — markets "No subscriptions or contracts… only pay for what you need"; revenue = per-consult fees + à-la-carte med/lab/supplement purchases, no membership
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; verified against screenshots + the wordmark raster
logo_url: https://www.defymedical.com/wp-content/themes/defy-medical/dist/img/logo.svg   # canonicalized to the wordmark (2.5)
logos:
  wordmark: { src: "https://www.defymedical.com/wp-content/themes/defy-medical/dist/img/logo.svg", w: 1044, h: 239 }                       # "Defy" (blue cursive) + "MEDICAL" (green) — real brand mark, transparent
  logomark: { src: "https://www.google.com/s2/favicons?domain=defymedical.com&sz=256", px: 192, transparent: true }                       # the cursive "D"; renders clean on a dark tile (no baked box). apple-touch = 180px, smaller
  og:       { src: "https://www.defymedical.com/wp-content/uploads/2022/05/Def-003_HomepageHero.jpg", w: 1228, h: 1114 }                   # declared og:image — a lifestyle homepage hero (couple + laptop), not a branded cover
brand_colors: { primary: "#0E75BB", accent: "#8CC63F" }   # STRAIN: blue "Defy" + green "MEDICAL" of the wordmark (sampled); orange #FFA500 is a hexagon-motif accent. branding payload missed the green
fonts: [Poppins, Lora]   # Poppins body, Lora serif headings (branding.typography)
color_scheme: light
design_framework: wordpress   # rawHtml: wp-content + wp-json; branding said "bootstrap" (ignored, §5.4)
---

## Overview

Defy Medical is a Tampa, FL–based telemedicine clinic ("more than a decade" in operation) specializing in **hormone restoration and integrative medicine** for both men and women. It anchors on TRT and bioidentical HRT but its menu is broad — weight loss (GLP-1s), sexual health, thyroid, ketamine, IV/nutrition, aesthetics, joint pain, and primary care. The model is consult-led: a Patient Advocate intake → an **extended (1-hour) telemedicine consult** with a licensed provider plus **comprehensive blood testing** → a customized protocol, with prescriptions, supplements, and supplies ordered through an online Patient Portal and shipped to the door. Distinctively for the cohort, it markets **"No subscriptions or contracts — only pay for what you need."** It also runs an in-person Tampa clinic (accepts walk-ins). Medical director: **Dr. Justin Saya, MD**.

## What they offer

Many co-equal lines (grouped as the site groups them). Treatment pricing is almost entirely gated behind a paid consult + the Patient Portal, so most lines tag `[on-request]`; **Trimix is the published exception**. Per-SKU/molecule depth → `offerings.md`; telehealth-specific cuts → `telehealth.md`.

- **Testosterone Replacement Therapy (TRT):** injectable, topical, pellet, and nasal-gel testosterone + supplemental meds (testicular health, fertility, estrogen control) — *price behind consult + portal* `[on-request]`
- **Erectile Dysfunction / Trimix:** compounded penile injection (Phentolamine + Alprostadil + Papaverine) and variants (Super Trimix, Bimix, Super Bimix, Quadmix, Super Quadmix); also Sildenafil, Tadalafil — **"Trimix Injections from $1.39 to $3.30 per Injection"** + **"$99" Trimix consult** `[partial]`
- **Bioidentical Hormone Therapy (BHRT, women):** estradiol/estriol, progesterone, testosterone, DHEA, pregnenolone — injectable / topical / capsule / pellet — *price behind consult + portal* `[on-request]`
- **Weight Loss (GLP-1):** Semaglutide, Tirzepatide, Liraglutide + adjuncts (B12, lipotropic injections, appetite suppressants, topical spot treatments) — *price behind consult + portal* `[on-request]`
- **Lab Testing:** on-demand panels via the testdefy.com store — Men's/Women's Complete Hormone Health, Thyroid Function, B12, CBC, STD, allergen — *prices on the lab store, not captured* `[on-request]`
- **Other lines (nav-attested):** Anabolic/androgenic therapies, Menopause, Female sexual dysfunction, Thyroid disease, Ketamine therapy, IV therapy, Vitamins & supplements (Fullscript), Joint pain, Primary care, Hair loss (incl. PRP), Cosmetic injections, Skin care, Advice-only consultations (international), Performance consultations — `[on-request]`

## How it works / model

Three steps (per `/get-started`): **(1)** connect with a **Patient Advocate** (handles new-patient requirements — blood testing, recent physical, history); **(2)** **consult via telemedicine** with an experienced provider (extended 1-hour consults) to develop a customized protocol; **(3)** **order online** through the Patient Portal (medications if prescribed, plus supplements and supplies) for direct-to-door delivery. Revenue is **transactional, not subscription** — "prescription management is included in the overall cost of care," and patients "only pay for what you need." Fulfillment runs on a **third-party pharmacy network** ("a network of pharmacies… that meet high standards, follow USP and GMP, and utilize FDA-approved active ingredients"), a **partner laboratory cooperative** (national labs at "an average of 92% off the retail price"), and **wholesale supplement contracts**. Licensed to prescribe in most US states; international patients get **advice-only** consults (no overseas shipping). Telemedicine nationwide + an in-person Tampa clinic.

## Positioning & audience

Serves **both men and women** but **leads with men's health and TRT** — "The World's Leading Hormone Replacement Clinic," and "Our care team specializes in Men's Health and uses the latest research and advancements in TRT." The pitch is against rushed traditional care: **root-cause / whole-patient integrative** treatment, **extended 1-hour consults** ("our providers listen"), comprehensive lab-driven protocols, a decade-plus track record, and **no subscriptions or contracts**. Women's health is a full, parallel line (BHRT, menopause, female sexual dysfunction) rather than an afterthought.

## Nav structure

```
- Services — /services
  - Men's Health
    - Testosterone Therapy (TRT) — /services/trt  [Popular]
    - Erectile Dysfunction — /services/erectile-disfunction  [Popular]
    - Trimix — /services/trimix-injections  [Popular]
    - Anabolic Therapies — /services/anabolic-androgenic-therapies
    - Men's Questionnaire — /take-the-quiz/male
  - Women's Health
    - Hormone Therapy — /services/hormone-therapy  [Popular]
    - Menopause — /services/menopause
    - Sexual Dysfunction — /services/female-sexual-dysfunction  [Popular]
    - Women's Questionnaire — /take-the-quiz/female
  - Weight Loss
    - Semaglutide — /services/semaglutide-for-weight-loss  [Popular]
    - Tirzepatide — /tirzepatide-online  [Popular]
    - Weight Management — /services/weight-loss
  - General Healthcare
    - Lab Testing — /services/lab-tests-online  [Popular]
    - Primary Care — /services/primary-care
    - Ketamine Therapy — /services/ketamine-therapy  [Popular]
    - Thyroid Disease — /services/thyroid-therapy
    - Vitamins & Supplements — /services/vitamins-and-supplements
    - IV Therapy — /services/iv-therapy
    - Joint Pain — /services/joint-pain
    - Advice-Only Consultations — /services/services-advice-only-consultation
    - Performance Consultations — /services/sexual-performance-consults
  - Aesthetics
    - Hair Loss — /services/hair-loss  [Popular]
    - Cosmetic Injections — /services/cosmetic-injections
    - Skin Care — /services/skin
- About Us — /about-us
- Clinic Location — /tampa-clinic
- Health Articles and Resources — /blog
Utility: Take the Quiz · Check My Order (patients.defymedical.com) · Help Center ·
  Patient Login (defymedicalstore.com) · Buy Lab Tests (testdefy.com) · Get Started · Patient Portal
```

## Credibility & proof

- **Trustpilot:** "TrustScore 5 out of 5", "See All **3784** Reviews" — links to trustpilot.com/review/defymedical.com (third-party platform; the rating display is self-embedded — record, don't endorse).
- **Tenure / scale:** "We've offered telemedicine care for more than a decade and helped thousands of patients" (self-reported, verbatim).
- **Named clinicians:** care team "led by **Dr. Justin Saya**, our medical director and lead practicing physician"; full provider roster at /about-us/team-bios.
- **Physical clinic:** 4809 N. Armenia Ave. Suite #220, Tampa, FL 33603 (in-office services + walk-ins).
- **Standards:** CFR- and HIPAA-compliant platform; pharmacy partners "follow USP and Good Manufacturing Practices, and utilize FDA-approved active ingredients."
- **Not shown on captured pages:** LegitScript certification, pharmacy accreditation seals (PCAB/NABP/ACHC).

## Visual & brand impression

Clean, professional, light theme. A **blue + green** identity (blue cursive "Defy", green "MEDICAL") with an **orange-accented hexagon / honeycomb motif** running through the pages — a "molecular / science" cue. Imagery is **lifestyle stock photography** (couples on couches, active older adults, people on laptops) plus flat **category-icon illustrations**; no isolated product renders (it's a services clinic). Overall read: established, trustworthy, clinical-but-approachable — closer to a medical practice than a trendy DTC startup.

## Strategic read

The cohort's **pricing-model outlier**: where the telehealth field defaults to membership/subscription, Defy explicitly rejects it ("no subscriptions or contracts") and runs **pay-per-consult + à-la-carte** meds/labs/supplements. It pairs that with the **broadest service menu** in the set (~20 lines) and a **legacy posture** — a decade-plus of operation, a named medical director, and a physical Tampa clinic — versus the newer VC-backed DTC entrants. The trade-off is **price opacity**: nearly every treatment price sits behind a paid consult + the gated portal, a friction point against published-price competitors. Diagnostics (comprehensive labs, 92%-off co-op) and extended consults are the wedge.

## Provenance

- **Pages:** homepage, /services (rich index), /about-us, /get-started, /about-us/about-us-vendor-information, /services/trt, /services/hormone-therapy, /services/semaglutide-for-weight-loss, /tirzepatide-online, /services/lab-tests-online, /services/trimix-injections — 11 pages, Firecrawl, 2026-06-04.
- **Verify:** all sourceURLs matched; all 11 bodies md5-unique (no §5.1 geo/cache contamination).
- **Credits:** 12 (1 map + 11 scrapes); ~803 remaining.
- **Couldn't get:** medication/lab pricing (gated behind paid consult + Patient Portal / the testdefy.com store, not scraped); LegitScript/pharmacy-accreditation seals (not on captured pages); per-SKU compounded-vs-FDA lane (not explicitly labeled).
- **Run profile:** guided — modules: +offerings.md, +telehealth.md cohort pack, +logos:{}, +product-page images. Services clinic → no isolated photographic product renders exist (lifestyle/icon imagery); the one product-style asset (the Trimix medication icon) was promoted to `captures/2026-06-04/images/trimix-medication.webp`.
