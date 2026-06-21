---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: maleexcel.com
name: Male Excel
aliases: []
legal_entity: "Male Excel Medical, P.A."   # homepage JSON-LD Organization name; footer also uses Excel Medical
parent: []                                 # footer links Excel Medical + Fem Excel, but captured pages do not explicitly attest ownership
owns: []
socials: { facebook: "https://www.facebook.com/MaleExcel", x: "https://x.com/maleexcelonline", instagram: "https://www.instagram.com/MaleExcel/", linkedin: "https://www.linkedin.com/company/excelmedical/", youtube: "https://www.youtube.com/@maleexcel7204" }
external: { trustpilot: "https://www.trustpilot.com/review/maleexcel.com" }

# Capture meta
captured_at: 2026-06-20
capture_method: firecrawl
site_notes: "WordPress + Elementor site (rawHtml: wp-content/wp-json; generator Elementor 4.0.7). Homepage is unusually rich and includes nav, offerings, labs, pricing FAQ, Trustpilot, LegitScript, and footer family links. Repeated Elementor blocks duplicate in markdown; dedupe mentally. Pricing is split: HRT medication + membership on /treatments/hrt-costs, ED medication on /ed-treatment. Logo module: canonical color wordmark is JSON-LD SVG; header uses reverse SVG; square favicon/logomark measures only 16px; declared og:image is 375x585. Footer links Excel Medical and Fem Excel, but ownership/parent relation is not explicitly attested in captured pages."
key_pages:
  trt: /treatments/trt-online
  pricing: /treatments/hrt-costs
  ed: /ed-treatment
  thyroid: /treatments/bioidentical-thyroid
  labs: /treatments/male-hormone-test
  story: /our-story
  providers: /our-hrt-specialists
  advantage: /the-excel-advantage-hormone-optimization-for-men
unverified_fields:
  - "Pharmacy ownership - pages state U.S. compounded / pharmacy-dispensed treatments and ED fulfillment by a US pharmacy, but do not name a pharmacy or claim ownership."
  - "Excel Medical / Fem Excel relationship - footer links the family and provider pages use Excel Medical, but captured pages do not explicitly state ownership or parent/subsidiary structure."
  - "Headcount, funding stage, revenue - not on the marketing site."

description: "Runs an online men's health clinic for hormone optimization, pairing at-home labs and licensed-provider consults with membership-based TRT/thyroid care, ED medication, and follow-up monitoring."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Flagship + companions
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: "https://maleexcel.com/wp-content/uploads/2023/02/MaleExcel_LogoCC.svg"   # 2.5 canonicalizes to the wordmark; color SVG from homepage JSON-LD
logos:
  wordmark: { src: "https://maleexcel.com/wp-content/uploads/2023/02/MaleExcel_LogoCC.svg", w: 984, h: 213 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=maleexcel.com&sz=256", px: 16, transparent: true }   # tiny red favicon mark; transparent background confirmed visually
  og:       { src: "https://static.maleexcel.com/wp-content/uploads/2025/04/07193851/run-header-video-1440x660-1m-1.png", w: 375, h: 585 }   # declared og:image; small/narrow but recorded with measurement
brand_colors: { primary: "#B4101A", text: "#262525", background: "#FFFFFF" }
fonts: [Oxygen, Poppins, Inter]
color_scheme: light
design_framework: "wordpress + elementor"   # rawHtml: wp-content/wp-json + Elementor generator; branding.designSystem ignored
---

## Overview

Male Excel is a direct-to-consumer online men's health clinic focused on hormone optimization. It leads with provider-led TRT, thyroid support, at-home hormone testing, and ongoing 60-day follow-ups; ED medication, metabolic/GLP-1 support, targeted supplements, NAD+, DHEA, and member-access longevity therapies sit around that core. The site says Male Excel launched in 2019, operates on a 100% online platform, and gives patients access to licensed medical providers without leaving home. Clinical leadership is anchored by Peter Fotinos, MD, and Lorna A. Brudie, DO, with the broader site using the Excel Medical name for its provider team and lab/family footer.

## What they offer

TRT is the flagship, with labs and membership as the front door. ED is a separate direct medication line; the newer metabolic/longevity layer is present in homepage copy but less fully productized in captured pages.

- **TRT / hormone optimization:** provider-led testosterone replacement therapy with daily microdosing, thyroid, and estrogen optimization; treatment formats include injections, cream, and tablets. HRT pricing page lists "Prices as low as $95 a month*" plus monthly Medical Membership `[partial]`.
- **Bioidentical testosterone cypionate injections with thyroid:** "Starting at" "$120/month*/ 60 day Supply"; billed bi-monthly; FSA/HSA eligible; price excludes shipping/handling and required Medical Membership `[partial]`.
- **Bioidentical testosterone Lipoderm cream with thyroid:** "Starting at" "$132/month*/ 60 day Supply"; billed bi-monthly; FSA/HSA eligible; price excludes shipping/handling and required Medical Membership `[partial]`.
- **Triclozene (clomiphene citrate with thyroid):** oral compound / proprietary testosterone formula; "$95/month* / 60 day Supply" on the same pricing page, with the membership exclusion footnote `[partial]`.
- **Medical Membership:** "$99/Month" for dedicated provider continuity, unlimited support-team messaging, and unlimited e-visits; homepage also says membership includes structured 60-day assessments and comprehensive blood testing every 6 months `[published]`.
- **At-home hormone testing:** finger-prick hormone panel measuring testosterone, estradiol, DHEA-S, Free T3, and PSA; the test page says order + online consultation + hormone test + personalized treatment plan are "all for one low cost: $99" `[published]`.
- **ED medications:** FDA-approved generic Viagra / sildenafil "100mg $65/month" ("$35 first month"), generic Cialis / tadalafil "20mg $65/month" ("$35 first month"), and generic daily Cialis / tadalafil "5mg $89/month" ("$29 first month") `[published]`.
- **Thyroid therapy:** Free T3-led thyroid assessment and bioidentical testosterone + thyroid treatment, positioned as Male Excel's "missing link" vs testosterone-only HRT clinics; standalone thyroid price is not stated outside HRT bundles `[partial]`.
- **Metabolic / longevity add-ons:** homepage lists GLP-1 metabolic therapies with B-12, targeted supplements, NAD+, and DHEA layered in based on symptoms and labs; dedicated public pricing was not captured `[on-request]`.

## How it works / model

For TRT, the journey is online assessment -> at-home lab test -> provider consultation -> personalized protocol -> ongoing monitoring. Male Excel says patients complete an at-home test covering testosterone, estradiol, thyroid function, DHEA-S, and PSA, then meet with a US-licensed medical provider to review symptoms, medical history, and results. Ongoing care is membership-based: $99/month for provider access, 60-day reviews, lab monitoring, and adjustments; medications are priced separately by protocol and dose. The cost page is explicit that testosterone is a Schedule III controlled substance and requires medical monitoring.

ED is lighter-weight: medical history form online, US-licensed provider review/prescription, and discreet two-day shipping from a US pharmacy. The ED page says some states may require an online consultation and that ED treatment is available in all states except Alaska, Arkansas, Connecticut, Hawaii, Idaho, Louisiana, Mississippi, New Hampshire, and Rhode Island. Homepage FAQ says Male Excel does not accept insurance, but FSA/HSA/HRA reimbursement may be available.

## Positioning & audience

Male Excel targets men who feel fatigue, brain fog, weight gain, low libido, or declining performance and frames those symptoms as hormone-related rather than simply aging. It positions against traditional care and "ordinary" online TRT clinics: the named difference is The Excel Advantage, a protocol built around daily microdosing, thyroid support, no estrogen blockers, regular symptom reviews, 60-day provider check-ins, and blood panels every 6 months. The tone is direct and performance-oriented: "Feel Better. Live Better. Excel." and "We do not just restore hormones. We rebuild men."

## Nav structure

```
- Men's Health — /
- Women's Health — femexcel.com
- Testosterone Therapy
  - TRT online — /treatments/trt-online/
  - Thyroid Therapy — /treatments/bioidentical-thyroid/
  - Testosterone Cypionate Injection — /treatments/testosterone-cypionate-injections/
  - Testosterone Lipoderm Cream — /treatments/testosterone-cream/
  - Triclozene Oral — /treatments/clomiphene-for-men/
  - Hormone / Testosterone Testing — /treatments/male-hormone-test/
  - Hormone Treatment Price — /treatments/hrt-costs/
  - Symptoms of Low T — /low-t-symptoms/
  - New to HRT? — /understanding-hrt/new-to-hrt/
  - Already Taking Testosterone? — /understanding-hrt/taking-testosterone/
  - Is TRT Right for Me? — go.maleexcel.com/hormone-assessment/ghrt
  - TRT FAQs — /faq/
- ED Medications
  - ED Medications — /ed-treatment/
  - Generic Daily Cialis — /ed-treatment/generic-daily-cialis/
  - Generic Cialis — /ed-treatment/generic-cialis/
  - Generic Viagra — /ed-treatment/generic-viagra/
  - Which ED Medication is Right for Me? — /ed-treatment/which-ed-medication/
  - ED Medication Costs — /ed-treatment/
  - ED FAQs — /ed-faq/
- Learn More
  - Our Story — /our-story/
  - Our Providers — /our-hrt-specialists/
  - The Excel Advantage — /the-excel-advantage-hormone-optimization-for-men/
  - About Dr. Peter Fotinos — /hormone-experts/dr-peter-fotinos/
  - Reviews — /reviews/
  - Request a Consultation — /free-hrt-consult/
  - Health Guide — /blog/
  - TRT Studies — /research/trt-studies/
- Member Login — member.maleexcel.com
```

## Credibility & proof

- **Trustpilot:** embedded widget says "TrustScore 4.5" and "5,360 reviews" on the captured pricing/provider/ED pages; flagged self-reported because it is site-embedded.
- **Scale claim:** homepage says "100,000+ patients treated" and later "100,000 members" for the 20-year protocol claim; site does not reconcile "patients" vs "members."
- **Clinical leadership:** homepage and TRT page name Peter Fotinos, MD, as Chief Medical Officer and Lorna A. Brudie, DO, FACOOG/FACOG/FACS, as Medical Director; provider page lists many named physicians and nurse practitioners.
- **Provider team:** homepage says care is "Not outsourced. Not rotated" and that providers receive "300+ hours of training in the first two years"; provider page says HRT providers are board-licensed and trained in The Excel Advantage.
- **Lab signal:** homepage says lab testing is processed through Excel Medical Labs, a CLIA-certified laboratory in North Carolina; 360 Blood Panel claims 54 biomarkers.
- **LegitScript:** footer shows a LegitScript seal image; no certificate number is visible in captured markdown.
- **Guarantee:** Excel Advantage page says "Follow our protocol for 90 days. You'll see results, or we'll refund your membership fees"; homepage footnote says three months of membership fees are refunded if symptoms do not improve.

## Visual & brand impression

Clinical-performance funnel with a premium gym/athlete flavor. The site uses a black/charcoal sticky header, white content bands, red CTAs and highlight strokes, rounded white/gray cards, and grayscale performance imagery. The brand mark is a compact Male Excel wordmark; the canonical color SVG is red/black, while the rendered header and footer use reverse/white variants. The layout is dense for a DTC clinic: product cards, app/mock lab panels, testimonial rails, provider cards, and repeated CTA sections make it feel conversion-heavy, but the medical/provider and lab claims keep it closer to a managed clinic than a pure supplement funnel.

## Provenance

- **Pages:** homepage (rich pass: markdown/html/rawHtml/links/branding/images/screenshot), `/treatments/trt-online`, `/treatments/hrt-costs`, `/ed-treatment`, `/treatments/bioidentical-thyroid`, `/treatments/male-hormone-test`, `/our-story`, `/our-hrt-specialists`, `/the-excel-advantage-hormone-optimization-for-men` - Firecrawl `maxAge:0`, `location:US`; map returned 109 URLs with blog/content noise.
- **Verify:** 9 pages - all sourceURLs matched, all bodies md5-unique, no junk soft-404s.
- **Credits:** 10 spent this run (1 map + 1 homepage + 8 key pages).
- **Couldn't get:** named pharmacy / ownership claim; explicit Excel Medical / Fem Excel ownership relation; per-SKU roster beyond profile-level anchors (offerings.md was not requested this run); financials/headcount.
- **Run profile:** express - +telehealth cohort pack, +logos.
- **Structured layer (schema 2.6):** homepage JSON-LD via `fc.py signals` supplied Organization name "Male Excel Medical, P.A.", logo URL, and Facebook/X/Instagram/LinkedIn sameAs; footer supplied YouTube and LegitScript image. Values were checked against rendered homepage/footer before landing.
- **Logos (schema 2.5):** `fc.py logos` measured color JSON-LD wordmark (984x213), reverse header wordmark (546x77, not used as canonical), 16px Google/Apple favicon logomarks, and declared og:image (375x585). Recorded the small marks with measurements so consumers can gate them.
