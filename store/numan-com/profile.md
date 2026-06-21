---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: numan.com
name: Numan
aliases: []
legal_entity: "Vir Health Limited"   # JSON-LD legalName + footer trading-name line
parent: []
owns: []
socials: {}                          # homepage carries twitter:site @getnuman but no verified social URL in the captured footer/header
external: { trustpilot: "https://uk.trustpilot.com/review/numan.com" }   # footer Trustpilot record; rating itself is in Credibility & proof

# Capture meta
captured_at: 2026-06-20
capture_method: firecrawl
site_notes: "Next.js site (`/_next/`, x-powered-by Next.js). CookieYes consent modal pollutes the first ~750 markdown lines on every capture; actual page content starts below it. Homepage Firecrawl `metadata`/`branding` returned null, but rawHtml carried JSON-LD, full mega-nav, footer legal text, and the inline Numan SVG wordmark. Map returned 497 URLs with heavy `/numankind`, article, and condition-education noise; select key pages from homepage nav, not map. UK/GB locale (`NEXT_PUBLIC_COUNTRY=GB`). `numan.co.uk` redirects to garynuman.com, a different live entity — collision, not an alias. No declared og:image on homepage."
key_pages:
  all_treatments: /all-treatments
  weight_loss: /weight-loss
  trt: /low-testosterone/trt
  erectile_dysfunction: /erectile-dysfunction
  hair_loss: /hair-loss
  diagnostics: /diagnostics
  about: /about-us
  patient_outcomes: /patient-outcomes
  safety: /mens-health/patient-safety-numan-regulatory-compliance
unverified_fields:
  - "Per-SKU roster intentionally not written this run — user requested profile + telehealth cohort pack + logos, not offerings.md."
  - "Prices and promo discounts are a point-in-time snapshot, not fixed — captured pages carry first-month and promotional prices across several lines."
  - "Company number appears inconsistent on captured pages: /about-us says 11440237, while the footer says 11449267."
  - "Insurance/NHS/private-payment mechanics not stated on captured pages; pay model left unclear in telehealth.md."

description: "Runs a UK digital clinic for weight loss, TRT, sexual health, hair loss, blood tests, supplements, and menopause-related care, combining online assessments with licensed clinicians, diagnostics, coaching, and home delivery."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg        # 2.5 canonicalizes to the wordmark — extracted inline footer SVG from rawHtml
logos:
  wordmark: { src: assets/wordmark.svg, w: 119, h: 22 }                                                             # purple Numan wordmark, extracted from footer SVG
  logomark: { src: "https://www.google.com/s2/favicons?domain=numan.com&sz=256", px: 256, transparent: false }       # white "n" on baked dark rounded square; judged visually on dark composite
brand_colors: { primary: "#454592", accent: "#5252E6", background: "#F4F3FB", text: "#29235C" }  # verified from screenshot/raw SVG/cookie CTA colors
fonts: []                            # Firecrawl branding null; local-font names not exposed in captured markdown
color_scheme: light
design_framework: next.js            # rawHtml + headers: /_next assets, Next.js-powered response
---

## Overview

Numan is a UK-based, CQC-regulated online healthcare provider and digital clinic trading under Vir Health Limited. Its site frames the company around healthspan — "Live healthier, happier, and longer" — and says it was founded in 2018 to integrate personalised medical treatments, advanced diagnostics, and clinical coaching. The captured front door is broad: long-term weight loss, sexual support, testosterone treatment, personalised blood tests, supplements, and health coaching, with women's health/menopause routes also present in nav.

## What they offer

Multiple condition lines, mostly online-assessment or programme-led. Representative priced lines only; this run did not write `offerings.md`.

- **Weight loss:** programme with clinician-backed care, a dedicated health coach, app support, and medication "as a daily pill or weekly injection" where appropriate; homepage line "From£57.20/ month" first-month price, while all-treatments lists Wegovy from "£169.00 / month", Mounjaro from "£249.00 / month", Alli from "£50.00 / month", and weight-loss blood test from "£78.00 / kit" `[published]`.
- **TRT / low testosterone:** diagnostic pathway with venous blood tests and doctor consultation; TRT programme prices: injectable TRT "From £129/month", oral TRT "From £89/month", topical TRT "From £99/month"; diagnostic cost table says "Up to £149" `[published]`.
- **Sexual health:** ED treatments and premature-ejaculation routes; ED page hero says "From£0.69/ tablet", and captured cards include Sildenafil "From£1.10 / tablet", Tadalafil "From£1.16 / tablet", Viagra Connect "From£6.04 / tablet", and Cialis Together "From£5.83 / tablet" `[published]`.
- **Hair loss:** finasteride, minoxidil plan/spray, Regaine, hair-support supplements, and rosemary oil; hero says "From£1.00/ tablet", with cards including minoxidil plan "From£30.00 / bottle" and Regaine "From£65.00£51.67 / bottle" `[published]`.
- **Diagnostics / blood tests:** at-home blood-test line, results in "3-5 days", with routes for full check-up, sexual performance, metabolic, heart, nutritional, male hormone, and female hormone panels; diagnostics hero says "From£68.00£47.60/ kit", and all-treatments lists many panels from "£58.00 / kit" to "£168.00£142.80 / kit" `[published]`.
- **Supplements:** broad dietary-supplement catalog for testosterone support, libido, metabolic/weight support, meal replacement, B12, omega-3, sleep, beetroot, and related lines; representative prices from "£12.33 / bottle", "£12.66 / bottle", "£20.66 / box", "£24.91 / kit", and "£48.00 / bag" `[published]`.
- **Doctor consultations:** one-off phone consultation with a Numan UK doctor, "From£60.00 / consultation" `[published]`.

## How it works / model

The customer journey is online-first: choose a condition/test, complete an assessment or buy a kit, get reviewed by UK-based clinicians, receive prescribed treatment or test results where appropriate, then manage treatment through delivery, app support, coaching, and clinician follow-up. TRT is the clearest hybrid journey: blood test → doctor review/video consultation → treatment → regular monitoring. Hair loss describes a "simple online consultation," discreet delivery, repeat prescriptions, and phone/email access to the medical team. Diagnostics are at-home blood tests with app/clinical follow-up. Revenue appears mixed subscription/programme plus transactional kit/consult/supplement sales; the universal best fit remains `Subscription` because major treatment journeys are recurring monthly programmes or repeat-prescription care.

## Positioning & audience

Numan positions as convenient, regulated, clinical healthcare for people who want to improve long-term health rather than only treat symptoms. The origin and much of the product depth remain men's health (TRT, ED, hair loss), but the captured site now carries co-equal top-level women's health routes, menopause/perimenopause tests, female hormone tests, and women's supplements. The homepage lead is **weight loss / metabolic health**, not TRT: long-term weight loss is first in the hero and first in the main nav, while TRT and sexual health are prominent companion lines.

## Nav structure

Captured from the homepage header/footer rawHtml and validated against the screenshot.

```
- Weight loss
  - Programme: Weight loss programme — /weight-loss; BMI calculator; Our approach; Health coaching; Meet the experts; Understanding obesity
  - Medication: Mounjaro — /weight-loss/mounjaro; Wegovy — /weight-loss/wegovy; Wegovy Pill; Alli
  - Supplements: Weight loss supplements
  - Diagnostics: Weight loss blood test; Metabolic health test; Full check-up; All blood tests
- Men's health
  - Testosterone: Low testosterone; Testosterone replacement therapy — /low-testosterone/trt; Testosterone blood test
  - Sexual health: Erectile dysfunction; Premature ejaculation; Sildenafil; Viagra Connect; Tadalafil; Tadalafil Daily
  - Diagnostics: Men's health tests; Male hormone blood test; Complete hormone test; Full check-up; All blood tests
  - Hair loss: Hair loss treatments; Hair loss pills; Hair loss spray; Men's health supplements
- Women's health
  - Perimenopause & Menopause: Menopause; Menopause test; Perimenopause test
  - Diagnostics: Women's health tests; Female hormone test; Full check-up; All blood tests
  - Supplements: Women's health supplements
  - Weight loss: Weight loss programme
- Diagnostics
  - General health: Full check-up; Complete blood test; Core blood test; Metabolic health test; Weight loss blood test; All blood tests
  - Hormone health: Men's hormone test; Complete hormone test; Testosterone blood test; Women's hormone test; Menopause test; Perimenopause test
  - I want to: Get a health overview; Support my weight loss; Understand my health: Men; Understand my health: Women
- Why Numan
  - Our approach: About Numan; Clinical research; Meet the experts; Health coaching
  - Patient safety: Our regulated standards; How safe prescribing works; CQC inspection results; GPhC pharmacy register
  - Support: Advice & guides; Help centre; Contact us; Book a consultation; Trustpilot reviews
- Footer: All treatments; Book a consultation; Advice & guides; Help & support; app store links; terms/privacy/cookies/complaints/sitemap
```

## Credibility & proof

- **Regulation:** homepage/footer badges show "CQC Regulated" and "GPhC licensed pharmacy"; safety page says Numan is regulated by the CQC for the care around prescription medicines and diagnostic results, regulated by MHRA as a marketer/advertiser of healthcare solutions/programmes, and that Numan Operational Limited (NOL) is registered with and inspected by the GPhC, premises registration number **9011408**.
- **Legal / pharmacy:** footer says "Numan is a trading name of Vir Health Limited" and lists Registered Pharmacy: "Numan Operations Limited (9011408)" plus Superintendent Pharmacist Sarah Morgan, GPhC Registration Number **2049981**.
- **Scale claims:** about page self-reports "> 800,000 patients", "> 33,000 reviews", "37% of our employees have a clinical background", and "18 research materials and abstracts submitted over the past year."
- **Trustpilot:** embedded widgets claim "Rated Excellent. 4.6 out of 5" and "34,368 reviews"; footer micro-widget rounds to "34.4K reviews" (self-embedded third-party widget).
- **Named clinicians:** homepage/diagnostics pages display named medical professionals including Danielle Brightman (Clinical Director), Zoe Griffiths (VP of Behavioural Medicine), Abby Watts (Senior Nurse Prescriber), Dr Aisha Jinnah, and Dr Michael Lacey; several pages are medically reviewed by Hassan Thwaini, Clinical Pharmacist and Copywriter, GPhC **2221320**.
- **Clinical standards:** about page says every treatment pathway follows NICE guidelines and that prescriptions are reviewed against the individual health profile, cross-checked against clinical standards, and approved by a qualified clinician "not an algorithm."

## Visual & brand impression

Clinical but consumer-polished. The homepage uses pale lavender/white space, vivid blue-purple watercolor clouds, dark-purple block typography, and compact treatment cards rather than a pharmacy-style grid. Product renders, app screens, named clinician cards, and trust badges do the work of making it feel medical without looking institutional. The huge footer wordmark and repeated purple CTAs make Numan feel like a digital health brand first and a clinic second.

## Strategic read

This capture reads as a broadened UK telehealth player whose front door has shifted from men's-health origins toward **weight loss + diagnostics + healthspan**. TRT remains a strong, priced line and likely why Numan surfaced as a Hone/TRT-side capture lead, but the live homepage is led by weight-loss programming, GLP-1/Alli medication options, health coaching, and app-based longitudinal care. The regulatory/safety page is unusually explicit, suggesting the brand is responding to scrutiny around online prescribing, pharmacy operations, and advertising compliance.

## Provenance

- **Pages (10 + map, all `captures/2026-06-20/`, Firecrawl `fc.py`, `maxAge:0`, `location:US`):** homepage rich pass (+ rawHtml/links/images/screenshot); all-treatments; weight-loss; TRT; erectile-dysfunction; hair-loss; diagnostics; about-us; patient-outcomes; patient-safety/regulatory-compliance. Map returned 497 URLs, mostly article/education/catalog noise.
- **Verify:** all 10 sourceURLs matched, all bodies md5-unique, no junk soft-404s.
- **Credits:** 11 Firecrawl credits (1 map + 10 scrapes, all 1cr; no enhanced-proxy escalations).
- **Couldn't get:** per-SKU roster/offering depth (not requested); stable non-promotional price book; insurance/NHS/HSA/private-payment posture; homepage OG image (none declared); exact font family names (Firecrawl branding null and local font names not exposed).
- **Structured layer (schema 2.6):** read this capture's homepage JSON-LD via `fc.py signals` ($0, hint-to-verify) — `legalName` → `legal_entity: "Vir Health Limited"`; JSON-LD employee Sarah Morgan matched footer superintendent pharmacist; no JSON-LD `sameAs` socials/external records; mega-nav recovered from rawHtml; inline footer SVG extracted to `assets/wordmark.svg`.
- **Run profile:** Express — +telehealth.md cohort pack · +logos.
