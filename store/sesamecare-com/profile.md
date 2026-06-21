---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: sesamecare.com
name: Sesame
aliases: []
legal_entity: "Sesame, Inc."          # footer © 2026 Sesame, Inc. across captured pages
parent: []
owns: []
socials:
  x: https://x.com/Sesamecare
  linkedin: https://www.linkedin.com/company/sesamecare/
  instagram: https://instagram.com/sesamecare
  facebook: https://www.facebook.com/sesamecare
  youtube: https://www.youtube.com/@sesame614
external: {}                          # JSON-LD sameAs carried only operated social channels; no third-party records

# Capture meta
captured_at: 2026-06-20
capture_method: firecrawl
site_notes: "Next.js homepage with large client-rendered menu; service pages scrape clean as markdown. Map is noisy with doctor, medication, and blog URLs; select signal pages from homepage links. Homepage payload carries the data-URI SVG wordmark, JSON-LD MedicalOrganization/socials, and the full nav/menu; use screenshot for visual read. Prices/provider counts are location- and time-sensitive; homepage defaulted to New York City, NY."
key_pages:
  about: /about
  team: /team
  join_doctors: /join/doctors
  membership: /join/membership
  telehealth_visit: /service/telehealth-visit
  weight_loss: /service/online-weight-loss-program
  mental_health: /complaint/online-mental-health-medication
  menopause: /service/menopause-treatment
  prescription_refill: /service/online-prescription-refill-visit
  faq: /faq
unverified_fields:
  - "Per-provider prices, availability, ratings, and 'within 2 hours' inventory are a point-in-time snapshot, not fixed — captured homepage/provider lists were rendered for New York City, NY on 2026-06-20."
  - "Medication costs vary by insurance status and pharmacy; the profile records published floors and posture, not all-in per-medication costs."
  - "Insurance posture differs by layer: Sesame does not bill health insurance for visits, but medication/lab coverage may depend on the patient's plan."

description: "Runs a direct-to-consumer healthcare marketplace where patients book video or in-person visits with independent licensed clinicians at upfront cash prices, plus optional memberships and subscriptions for ongoing care."

# Classification
entity_type: Company
target_market: [B2C, B2B]
offering_category: [Marketplace / Platform, Services / Consulting, Biotech / Pharma Products]
portfolio_shape: Catalog
business_model: Transactional / One-time
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 87, h: 28 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=sesamecare.com&sz=256", px: 150, transparent: false }
  og:       { src: "https://sesamecare.com/assets/sesame-twitter.png", w: 756, h: 756 }
brand_colors: { primary: "#5921CF", accent: "#EEE9FA", background: "#FFFFFF" }
fonts: [Saans, Inter]
color_scheme: light
design_framework: next.js
---

## Overview

Sesame is a direct-pay healthcare marketplace that lets patients find, book, and pay licensed clinicians directly for telehealth and in-person care. It positions the model as "Half-Price Health Care": no insurance billing, no surprise bills, upfront cash prices, and doctors available across all 50 states. The care is delivered by independent medical professionals and Sesame-affiliated provider practices using the Sesame telehealth platform, while Sesame supplies the consumer marketplace, provider tools, booking, payments, e-prescribing, and app layer.

## What they offer

- **Telehealth and urgent care visits:** same-day virtual doctor visits, urgent care, prescription refills, UTI/BV, dermatology, anxiety, ED, ADHD, pediatrics, and more; homepage says "Visits start at $34," with common tiles at **"From $35/visit"** and telehealth page "upfront prices as low as $34" `[published]`
- **Provider marketplace:** 383 services in the captured homepage search/menu and 36+ to 45+ specialties across telehealth, in-person care, labs, imaging, dentistry, primary care, mental health, dermatology, sexual health, women's health, and pediatrics; providers set their own prices and patients pay upfront `[partial]`
- **Sesame Plus:** optional discount membership, **"$10.99 per month or $99 per year"**, with "$10 off" telehealth/primary-care visits, "$10 off" in-person specialists/dentists, and one annual free lab/blood test `[published]`
- **Success by Sesame weight loss:** GLP-1-oriented ongoing program with video visits, messaging, labs, and provider care **"as low as $59/mo"** with annual subscription; cash-pay GLP-1 medications **"as low as $149/mo"** and medication costs are not included in the subscription price `[partial]`
- **Mental Health Rx:** medication-management subscription **"$79/mo."** with same-day refills, medication management, provider messaging, and prescriptions sent to a pharmacy of choice; medication is not included `[partial]`
- **Menopause subscription:** online menopause/perimenopause care **"$59/mo."** with video visit, ongoing messaging, same-day prescriptions, and basic lab work if necessary; medication costs are not included `[partial]`
- **Prescription refill visits:** online prescription/refill visits for adults 18+, HSA/FSA-eligible, with same-day prescriptions sent to local pharmacy or delivery; visit price starts **"as low as $34 per visit"** `[published]`
- **Provider-side platform:** clinicians can list virtual care, in-person care, or both; Sesame markets to patients, collects upfront payments, provides e-prescribing/note/lab tools, and pays providers weekly; "No provider fees or other costs" and providers "set their own rates" `[published]`

## How it works / model

Patients search by symptom, specialty, service, doctor, or medication; choose a provider by price, availability, credentials, and reviews; pay online upfront; complete medical history; then join a video appointment or visit in person. A clinician may prescribe medication, order labs, issue referrals/notes, or recommend in-person care. Prescriptions go to a local or online pharmacy; Sesame states that the visit price does not include medication cost.

Money model is mixed but starts with direct-pay transactions: patients pay for visits/services upfront, providers set rates, and Sesame says it does not bill health insurance for visits. Optional recurring layers sit on top: Sesame Plus discounts the marketplace, while condition programs like weight loss, Mental Health Rx, and menopause are subscriptions. Provider-side, Sesame markets practices, supplies tools, and handles weekly provider payouts while saying providers list for free and pay no provider fees.

## Positioning & audience

Sesame leads with affordability and speed for people with high deductibles, no insurance, or coverage gaps: "care without insurance," "care with no surprises," and "no deductibles, no surprise bills, no problem." It targets broad consumer healthcare needs rather than one gender or single condition: urgent care, prescriptions, GLP-1 weight loss, mental health, women's health, ED, skin, pediatrics, primary care, labs, imaging, and more. The provider-side pitch is a direct-pay practice builder: Sesame markets the practice, lets clinicians control pricing and availability, and removes insurance middlemen.

## Nav structure

```
Header:
- Urgent care — /complaint/online-urgent-care
- Prescription refill — /service/online-prescription-refill-visit
- Weight loss — /service/online-weight-loss-program
- Download the app — /join/mobile-app
- Refer a friend — share.sesamecare.com/header
- Search — symptom, service, doctor name, specialty, med

Homepage menu:
- See a doctor urgently
  - Urgent care visit — /complaint/online-urgent-care
  - Cold and flu · Sinus infection · COVID · UTI · Allergies · Asthma · Gastrointestinal · Rashes
- Refill a prescription
  - Prescription refill — /service/online-prescription-refill-visit
  - Mental Health prescriptions — /complaint/online-mental-health-medication
  - Medication cards: metformin, escitalopram, prednisone, finasteride, sertraline, sildenafil, trazodone, lisinopril, propranolol, Paxlovid
- Lose weight
  - Online weight loss — /service/online-weight-loss-program
  - Wegovy pill, Wegovy pen, Zepbound, Ozempic, Mounjaro, Rybelsus
- Improve mental health
  - Mental Health prescriptions — /complaint/online-mental-health-medication
  - Anxiety · Bipolar disorder · Depression · Performance anxiety · PTSD · Sleep
- Women's health
  - Menopause treatment — /service/menopause-treatment
  - PCOS treatment — /service/pcos-treatment
  - Birth control · Fertility · UTI · Vaginal infection · Yeast infection
- Treat ED — /service/online-ed-consult
- Improve skin — /service/prescription-skincare
- Care for children — /service/online-pediatric-visit-new-patient
- More from Sesame
  - SesamePlus membership — /join/membership
  - Download the app — /join/mobile-app
  - Sesame @ Work — /join/employee
  - Help — /faq

Footer:
- Find a doctor/provider: Online Doctors, Urgent Care, Prescription Refill, Weight Loss, UTI, BV, Dermatology, Anxiety, ED, ADHD
- Company: About, Team, Careers, Blog, Terms, Privacy, List your practice, Sesame @ Work, Affiliate, Partners, Newsroom, Help
```

## Credibility & proof

- **Scale/proof, page-stated:** about/team claim "500K+ Patients treated," "$47M+ Saved by patients," "60% Saved per appointment," "95% Patient satisfaction," "10K+ Doctors & specialists," and "80+ Specialties"; homepage separately says "$50M+ saved by patients," "95% patient satisfaction," "1M+ patients agree," and "10K+ board-certified providers." These are self-reported and differ by page, so both are snapshot proof points, not reconciled facts.
- **Ratings/reviews:** homepage and service pages show **"4.5 on Trustpilot"** / "4.5/5 stars" and patient testimonials.
- **Certifications/seals:** Better Business Bureau accreditation and LegitScript seal in the footer.
- **Provider trust:** Sesame says every publicly listed clinician shares active licensure, years of practice, education, training, and specializations; clinicians are independent and "do not work for Sesame," per FAQ.
- **Awards/press:** about page shows Healthline "Best Overall Telehealth," OnlineDoctor.com "Best Price Per Visit," NYC Digital Health 100, plus press logos/links including Bloomberg, NYT, Forbes, Yahoo Finance, Fox News, Entrepreneur, and Healthline.
- **Leadership:** team page names co-founders David Goldhill, Michael Botta, and John Fontein; Medical Director Dr. Allison Edwards; CTO Max Metral.

## Visual & brand impression

Bright consumer-health marketplace, centered on Sesame purple (`#5921CF`) over white and pale lavender blocks. The header mark is a compact purple wordmark; the square icon is a stylized "S." on a baked white tile, and the OG/social image uses the same symbol large on white. The homepage combines a polished app/search surface, provider cards, service tiles, and lifestyle photography. Typography reads as Saans-led UI with an editorial headline treatment in the hero, making the site feel friendly and access-oriented rather than clinical.

## Strategic read

Sesame is broader than most vertical DTC telehealth brands in this store. It is closer to a cash-pay marketplace and provider operating layer: broad service inventory, independent clinician supply, upfront prices, optional membership discounts, and condition-specific subscription programs. The cohort-relevant edge is not pharmacy ownership or a single medication lane; it is the marketplace's ability to route many health intents into the same search/booking/payment surface while preserving direct-pay transparency.

## Provenance

- **Pages:** 11 captured via Firecrawl — homepage rich pass (markdown/html/rawHtml/links/branding/images/screenshot), about, team, join_doctors, membership, telehealth_visit, weight_loss, mental_health, menopause, prescription_refill, faq. Map returned 126 URLs, mostly doctor/medication/blog noise; key pages selected from homepage links.
- **Verify:** all 11 sourceURLs matched requested URLs; all 11 body md5s unique; no junk soft-404s.
- **Credits:** 12 (1 map + 11 scrapes), basic proxy throughout.
- **Couldn't get:** exact current full pricing for all 383 services; per-provider price availability beyond the captured New York City snapshot; all-in medication pricing across every condition and pharmacy/insurance combination; pharmacy ownership/503A/503B lane beyond the page-stated preferred-pharmacy/local-pharmacy posture.
- **Structured layer (schema 2.6):** homepage JSON-LD carried MedicalOrganization/WebSite identity, address, support phone, logo, and operated social channels; `legal_entity` comes from the captured footer © line; no external third-party records in JSON-LD. Raw HTML confirms Next.js (`__NEXT_DATA__`, `/_next/`) and Saans font asset. Header `<nav>` was slim, so the nav structure was reconstructed from the rendered homepage menu/links and screenshot.
- **Run profile:** express capture requested by user — +logos and +telehealth cohort pack. Logos measured from cached homepage payload: extracted data-URI SVG wordmark to `assets/wordmark.svg`, logomark 150px Google/Apple icon on baked white background, OG 756x756 social image.
