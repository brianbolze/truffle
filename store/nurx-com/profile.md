---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: nurx.com
name: Nurx
aliases: ["NURX Inc.", "Nurx™"]
parent: [thirtymadison.com]
owns: []
socials:
  facebook: https://www.facebook.com/nurxapp
  x: https://x.com/nurxapp
  instagram: https://www.instagram.com/nurxapp/
  linkedin: https://www.linkedin.com/company/nurx
  youtube: https://www.youtube.com/channel/UCbPSriZYuAbZ68bknti_50w
  tiktok: https://www.tiktok.com/@nurxapp
external: {}

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "WordPress (theme nurx-theme-lazyload; gtranslate plugin). Image CDN nurx-www.imgix.net bot-blocks bare/headed fetch (fc.py hero/logos FETCH-FAIL) — download product renders/og with a browser UA + `Referer: https://www.nurx.com/`, and drop the `,compress` param. /map is ~all /faq/* + /blog content noise — select pages from the homepage mega-nav, not the map. Pricing is per-category: a consult fee + a per-medication out-of-pocket table on each condition page (no central /pricing). Branded GLP-1 pens are NOT shipped by Nurx — local-pharmacy pickup. OTC items (skincare, Nurx EC) sell at shop.nurx.com; patient intake/app at with.nurx.com + login.nurx.com. Parent = Thirty Madison (Terms/legals on patient.thirtymadison.com / with.nurx.com). Spanish site at /es/. Header wordmark is an inline SVG (extracted to assets/wordmark.svg); declared og:image 404s."
key_pages:
  birthcontrol: /birthcontrol/
  weight_management: /weight-management-treatment/
  glp1_injections: /weight-management/glp1-injections/
  our_services: /our-services
  team: /team/
  acne: /acne-treatment/
  mental_health: /mental-health/
  emergency_contraception: /emergencycontraception/
  womens_hair_loss: /womens-hair-loss/
unverified_fields:
  - "Per-treatment prices are page-stated estimates, explicitly 'not guaranteed' — final cost varies by insurance and pharmacy."
  - "Prices/IA are a point-in-time snapshot, not fixed — a sticky promo bar pushes weight management ('$0 with insurance') over the birth-control-led nav; no A/B tool fingerprinted, so treat the front-door anchor as rotating."
  - "Declared og:image (Nurx_App_OpenGraph_1200x630.jpg) returns 404 — og logo slot omitted."
  - "PrEP/HIV prevention: the App Store listing is still 'Nurx — birth control and PrEP', but PrEP is absent from the current site nav — not captured as a live line."

# Description — one sentence (~160-220 chars).
description: "A telehealth company for women's health that delivers birth control, weight management, mental health, dermatology, and sexual-health prescriptions 100% online via state-licensed clinicians, shipping most meds from its own pharmacy."

# Classification — closed sets (see TAXONOMIES.md).
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 1022, h: 332 }                                                          # inline-SVG header mark — serif "Nurx" wordmark
  logomark: { src: "https://www.google.com/s2/favicons?domain=nurx.com&sz=256", px: 180, transparent: false }     # "NURX." white on a baked BLACK square
  # og: omitted — declared og:image (Nurx_App_OpenGraph_1200x630.jpg) 404s
brand_colors: { primary: "#FFAD1E", secondary: "#FBE3C0", accent: "#000000" }   # amber/golden + cream; black wordmark/text. STRAIN: branding payload also flagged these; confirmed vs screenshot
fonts: [PP Pangram Sans, MabryPro]   # body / heading per branding payload; the "Nurx" wordmark itself is a separate custom serif
color_scheme: light
design_framework: wordpress           # rawHtml: wp-content + theme nurx-theme-lazyload + gtranslate plugin
---

## Overview

Nurx is a direct-to-consumer **telehealth company focused on women's health**, and a **Thirty Madison company**. Patients complete an online medical consultation, a clinician licensed in their state reviews it and (if appropriate) prescribes treatment, and Nurx ships the medication — "100% online—with free shipping, always." It spans an unusually broad set of women's-health lines for one brand: birth control, weight management, mental health, dermatology/skincare, sexual health, hair & scalp, and general/urgent care. The site claims **2M+ patients served** and offers care "for women at every phase of life." Most prescriptions are mailed from Nurx's own/partner pharmacy; branded GLP-1 pens are the exception (filled at a local pharmacy).

## What they offer

Seven condition lines, all telehealth (online consult → prescription → delivery). Bold-led, price verbatim + visibility token; per-SKU depth in [`offerings.md`](offerings.md):

- **Birth control:** "Over 50+ types" — the pill, patch, ring, shot. Pill **"As low as $0 with insurance, or as little as $15 per pill pack without"**; ring "$150"; patch "$50 per month"; morning-after "$45 per pill" `[published]`
- **Weight management:** GLP-1 injections + oral meds — **"Starts at $650/month"** (brand pens $650–1300/mo at a local pharmacy, **not shipped**), plus a **$79 consultation** + **$79/mo provider support fee**; orals "$60-329/month" cash `[partial]`
- **Mental health:** SSRIs/SNRIs/bupropion etc. — **"$59 for the initial consultation and $69 per month for ongoing medication management"**; meds "$0/month copay" with insurance or "$25" without `[published]` (no benzos/stimulants/controlled substances)
- **Skincare / dermatology:** acne, anti-aging, eyelash growth, melasma, rosacea — acne **"$40 for your medical consultation"** + per-med "$40–$90"; cosmetic skincare is cash-pay (no insurance) `[published]`
- **Sexual health:** emergency contraception (OTC Nurx EC **"$19.50 per pill"**; Ella **"$0 with insurance or $45 without (+ $15 medical consultation fee)"**), cold sore & genital herpes `[published]`
- **Hair & scalp:** women's hair loss — **"$80" initial consultation + "$20 per month"**; dandruff. Cash-pay (HSA/FSA accepted) `[partial]`
- **General health:** bacterial vaginosis, menopause, UTI, vaginitis, yeast infection (mostly insurance-billed); migraine routed to sibling brand Cove `[on-request]`

The site states **150+ prescription treatment options** in total ([/our-services](store/nurx-com/captures/2026-06-04/our_services.md)).

## How it works / model

- **Journey (async):** "Complete our online medical consultation" (health history, goals, photos for skin/hair) → "a provider licensed in your state will prescribe treatment (if clinically appropriate)" → "We'll send your prescription straight to your doorstep… Pause or cancel anytime." No scheduled video visit in the front-door flow.
- **Fulfillment:** "Our pharmacy fills your … prescription and sends a three-month supply straight to your doorstep" (birth control); "Certain medications are fulfilled by our partner pharmacy and mailed directly to your home"; "Branded GLP-1s are not available for shipment via our pharmacy … filled at the pharmacy of your choice." Free shipping; discreet/unmarked packaging.
- **How they make money:** medication (subscription, "billed monthly or quarterly"), per-line **consultation fees** ($40 acne, $59 mental health, $79 weight, $80 hair) and **recurring care/support fees** ($69/mo mental health, $79/mo weight), plus an **OTC storefront** at shop.nurx.com.
- **Payment:** bills most private insurance — "Aetna, Anthem, Blue Cross Blue Shield, Cigna, CVS Caremark, Express Scripts, OptumRx, United Health Care"; "FSA/HSA Eligible"; cash-pay where insurance doesn't cover (anti-aging, melasma, eyelash, women's hair loss; weight-care fees). "Free with insurance, or at affordable out-of-pocket prices."

## Positioning & audience

Targets **women across all life phases** — "specialty-level care for women at every phase of life." The entire nav, hero, and copy are women-framed; men seeking hair loss are pointed to sibling brand **Keeps** ("Our partner, Keeps, specializes in male pattern hair loss"). Claimed edge: breadth of women's-health categories in one place, affordability "with or without insurance," free shipping, and a women's-health-specialized clinical team. Sits in DTC women's-health telehealth (peers like Hers and category-specific players).

## Nav structure

```
- Birth control — /birthcontrol/
- Mental Health — /mental-health/
- Acne — /acne-treatment/
- More
  - SKINCARE
    - Acne — /acne-treatment/
    - Anti-aging — /anti-aging-treatment/
    - Eyelash growth serum — /eyelash-serum/
    - Melasma & dark spots — /melasma-treatment/
    - Rosacea — /rosacea-treatment/
    - View all — /skincare-treatments/
  - Mental health
    - Anxiety — /anxiety-treatment/
    - Depression — /depression-treatment/
    - Seasonal affective disorder (SAD) — /mental-health-sad/
    - Premenstrual dysphoric disorder (PMDD) — /mental-health-pmdd/
    - Postpartum depression — /mental-health-postpartum-depression/
    - Obsessive-compulsive disorder (OCD) — /mental-health-ocd
    - View all — /mental-health/
  - Weight Management
    - GLP-1 Injections — /weight-management/glp1-injections/
    - Prescription Pills — /weight-management/orals/
  - Sexual health
    - Emergency contraception — /emergencycontraception/
    - Cold sore — /oral-herpes-treatment/
    - Genital herpes — /genital-herpes-treatment/
  - Hair loss & scalp
    - Women's hair loss — /womens-hair-loss/
    - Dandruff — /dandruff-treatment/
  - General health
    - Bacterial vaginosis — /bacterial-vaginosis-treatment/
    - Menopause — /menopause-treatment/
    - Migraines — /cove/ (cross-sell to sibling brand Cove)
    - UTI — /uti-treatment/
    - Vaginitis — /vaginitis-treatment/
    - Yeast infection — /yeast-infection-treatment/
  - About Nurx
    - Help & FAQs — /faq/
    - Blog — /blog/
    - Contact — /contact/
    - Our team — /team/
    - Reviews — /reviews/
    - Our Services — /our-services
- HELP & FAQs — /faq/
- BLOG — /blog/
- LOGIN — https://login.nurx.com/
```
*(Mega-nav recovered from the `<header>` region and validated against the homepage screenshot. "Our services" ([/our-services](store/nurx-com/captures/2026-06-04/our_services.md)) adds an Insurance / FSA-HSA filter and a "General health" grid not all in the header.)*

## Credibility & proof

Self-reported unless noted — recorded, not endorsed:
- **Scale:** "2M+ patients served"; "Over 2 million people have entrusted us with their care."
- **Reviews:** "26k five-star reviews" / "26k+ reviews all time"; "1,874+ Nurx-wide reviews"; **Trustpilot** rating shown as **4.5** on the GLP-1 page. Dated patient testimonials surface on the homepage.
- **Named medical team** (/team — "Our independent medical organization"): **Dr. Peter Young** (Medical Director), **Cristin Hackel** (BS, RNC, MSN, WHNP), **Dr. Neil Zlatniski** (Medical Director), **Dr. Crystal Jacovino** (VP, Clinical Operations); **Dr. Marie Leger, MD, PhD, FAAD** credited on the hair page. Team described as "doctors, nurse practitioners, physician assistants, nurses and pharmacists."
- **Insurance acceptance:** seven payers named (above).
- **Corporate:** "Nurx is a Thirty Madison company" (legals/terms on patient.thirtymadison.com); © 2026 NURX Inc.

## Visual & brand impression

Warm and editorial: a cream/beige ground with a **golden-amber** (#FFAD1E) signature and soft terracotta accents, set against natural-light lifestyle photography of women outdoors. Friendly rounded sans body type (PP Pangram Sans / MabryPro) paired with a distinctive **serif "Nurx" wordmark** — the serif logo against the soft palette reads more "considered wellness" than clinical pharmacy. Generic illustrative packaging ("Nurx RX only" pill bottles/tubes) stands in for most products; only the weight-management line uses real branded product renders (GLP-1 pens). Overall: approachable, modern, women-first health brand with mature design execution.

## Strategic read

- **Breadth-as-strategy under a parent platform.** Nurx is the **women's-health storefront of Thirty Madison** (siblings Keeps for men's hair, Cove for migraine — the migraine line literally cross-sells to Cove). The wide women's-health catalog rides shared Thirty Madison infrastructure (pharmacy, patient app at patient.thirtymadison.com, careers via Thirty Madison's Greenhouse).
- **Two fulfillment economics in one brand.** Most lines are classic captive-pharmacy mail-order (high control, recurring). Branded GLP-1, by contrast, is *not* shipped — Nurx monetizes it via **$79 consult + $79/mo support fees** while the drug is filled and paid for at a third-party pharmacy. That's a margin/compliance choice worth noting: Nurx takes a clinician-fee position on GLP-1 rather than a dispensing one.
- **Heritage vs. promoted anchor diverge.** The structural/heritage anchor is **birth control** (still nav item #1; the app is "birth control and PrEP"), but the sticky promo bar pushes **weight management** ("$0 with insurance") — a live re-prioritization toward GLP-1 demand. Front-door classification is therefore volatile (see `unverified_fields`).

## Provenance

- **Pages:** 10 captured via Firecrawl (`maxAge:0`, `location:US`, `waitFor`) on 2026-06-04 — homepage, /birthcontrol/, /weight-management-treatment/, /weight-management/glp1-injections/, /our-services, /team/, /acne-treatment/, /mental-health/, /emergencycontraception/, /womens-hair-loss/. Structured layer via `fc.py signals` (JSON-LD Organization + `<header>` mega-nav).
- **Verify:** all 10 sourceURLs matched; all body md5s unique — no geo/cache contamination.
- **Credits:** 11 (1 map + 1 homepage + 9 key pages). Product renders, logos, and og fetched headed via curl (no credits).
- **Couldn't get:** the imgix CDN (nurx-www.imgix.net) bot-blocks fc.py's headed fetch — recovered product renders/og via curl with a browser UA + Referer. Declared og:image 404s. Per-medication final pricing sits behind the intake at with.nurx.com (not submitted).
- **Run profile:** express (caller-specified) — emphasis on full module set; **+offerings**, **+telehealth** cohort pack, **+logos** (2.5 module), **+PDP product images** (flagship GLP-1 render set promoted to `captures/2026-06-04/images/`).
