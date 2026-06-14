---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: openloophealth.com
name: OpenLoop Health
aliases: ["OpenLoop", "OpenLoop Health, Inc."]
parent: []
owns: []
socials:
  linkedin: https://www.linkedin.com/company/openloophealth
  facebook: https://www.facebook.com/openloophealth
  instagram: https://www.instagram.com/openloophealth
external: {}

# Capture meta
captured_at: 2026-06-11
capture_method: firecrawl
site_notes: "Next.js marketing site, no bot defense. Map returns ~490 URLs, heavily blog noise — select from homepage links. branding.images.logo is junk (grabs the AICPA SOC footer badge; its own LLM reasoning says rejected) — the real wordmark is an inline <svg> in the header (Header_navbarLogo). JSON-LD logo URL (app.openloophealth.com) fetch-fails. Clinician-side content lives on clinician.openloophealth.com subdomain. No prices anywhere on the site — every CTA is Contact Sales."
key_pages:
  team: /team
  provider_staffing: /provider-staffing
  technology_platform: /technology-platform
  payer_coverage_rcm: /payer-coverage-rcm
  licensing_credentialing: /licensing-credentialing
  practice_management: /practice-management
  clinician_network: /clinicians/clinician-network
  vertical_weight_loss: /companies/medical-weight-loss
  vertical_health_plans: /companies/health-plans
unverified_fields:
  - "Pricing — no prices published anywhere; all offerings gated behind Contact Sales."
  - "business_model — B2B service contracts implied but the site never states how fees are structured (subscription vs usage vs project)."
  - "Funding/stage — only the press headline 'Telehealth Startup OpenLoop Raises $15 Million' (Series A, linked on /team) is on-site; no round details captured."
  - "Diagnostic Imaging and Regulatory + Legal service pages, and 6 of 8 'Who We Serve / What We Deliver' vertical pages, not captured this run."

# Description — one sentence (~160-220 chars): [what they do] + [how] + [focus/differentiator].
description: "Provides white-label telehealth infrastructure to healthcare organizations — clinician staffing, an EHR platform, payer coverage/RCM, licensing and compliance — so client brands launch and scale virtual care under their own name."

# Classification — closed sets (see TAXONOMIES.md). Leave empty if the site doesn't determine it.
entity_type: Company
target_market: [B2B, B2B2C]          # STRAIN: sells to healthcare orgs, who deliver OpenLoop-powered care to their end patients
offering_category: [Services / Consulting, Software / SaaS]
portfolio_shape: Multi-product       # 7 named, separately-positioned service lines
business_model:
primary_industry: Healthcare & Life Sciences

# Visual identity — Firecrawl `branding` is a hint to verify, never source-of-truth; confirm against the screenshot (see note).
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 219, h: 59 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=openloophealth.com&sz=256", px: 23, transparent: true }
  og:       { src: "https://openloophealth.com/_next/static/media/website-placeholder-main.dfaff54a.png", w: 1200, h: 670 }
brand_colors: { primary: "#192b58", accent: "#E90C54" }   # navy from the wordmark fill; magenta on logomark, CTAs, links — branding payload's #3E7A9C blue not visually dominant
fonts: [Inter]
color_scheme: light
design_framework: next.js
---

## Overview

OpenLoop is a B2B white-label telehealth infrastructure provider: healthcare organizations plug into its clinician network, EHR platform, payer coverage, and back-office services to launch and scale virtual care under their own brand. Self-described on the homepage JSON-LD as "a leading white-label telehealth infrastructure provider" founded 2020 (founder Dr. Jon Lensing; /team lists Jon Lensing, CEO & Co-Founder and Christian Williams, COO & Co-Founder). Headquartered in "OpenLoop Tower," 317 6th Ave, Des Moines, IA — a building the company says was renamed for it. The pitch is modular: "Scalable, white-label virtual care solutions—from a-la-carte to full-stack" (meta description); "Plug in what you need. Scale when you're ready."

## What they offer

Seven named service lines, sold to organizations; no prices published anywhere — every line's CTA is Contact Sales:

- **Provider Staffing:** NCQA-accredited clinician network across all 50 states — recruiting, licensing, credentialing, scheduling/payroll, malpractice coverage, CMO services; claims "fastest staffing in the industry" ("Lab Ordering & Approvals 1 Week", "Primary Care or Family Medicine 3 Weeks", "Specialty Care 5-7 Weeks") `[on-request]`
- **Technology Platform:** "Intuitive, HIPAA-compliant EHR/EMR platform" — private-label, sync + async, API integrations, booking/payments, ePrescribing/eLabs, iOS/Android; "48 hours out-of-box, no integrations", full launch "Weeks 5-7" `[on-request]`
- **Payer Coverage + RCM:** "600+ Nationwide insurance plans including medicare and medicaid", "250 million patient lives covered", end-to-end RCM with "98% accuracy rate on claims"; credentialing "2-4 weeks", enrollment "30-120 days" `[on-request]`
- **Licensing + Credentialing:** NCQA-certified — state board + DEA licensing ("6-8 weeks"), hospital/payer/Medicare/Medicaid credentialing ("2-4 weeks"), "12-month financing of OpenLoop fees", claims "lowest pricing in the industry" `[on-request]`
- **Practice Management:** outsourced admin — insurance verification, code capture, pre-auth, patient records, scheduling/registration `[on-request]`
- **Diagnostic Imaging:** in nav/footer; page not captured this run `[on-request]`
- **Regulatory + Legal:** in nav/footer ("End-to-end legal, financial & compliance setup" per homepage); page not captured this run `[on-request]`

Supply side: the **OpenLoop Clinician Network** (clinician.openloophealth.com) recruits NPs, MDs, and therapists into the network — "One 1099 & Paycheck," in-house licensing/credentialing, flexible scheduling across ~15 listed specialties.

## How it works / model

Client journey is sales-led: every page funnels to Contact Sales, then a managed implementation (platform: staging access week 1 → go-live weeks 5-7; RCM: compliance setup → testing → go-live). Care is delivered under the client's brand by OpenLoop's clinicians and PC groups ("Clinical staffing & PC groups"), with OpenLoop running the back office (licensing, credentialing, billing, patient support "24/7"). Services are positioned as modular — clients take one line or the full stack, with each service page cross-selling "Recommended add-ons." Revenue is B2B service contracts; fee structure is never stated (homepage: "Competitively priced solutions that scale with demand").

## Positioning & audience

Positions as "the Top White-Label Telehealth Platform" — the infrastructure behind "many of the fastest growing telehealth brands." Audiences (their nav's "Who We Serve"): health plans, diagnostic labs, retailers + pharmacies, hospitals + health systems, plus digital health companies; delivery verticals ("What We Deliver"): medical weight loss, mental + behavioral health, primary + urgent care, longevity. The weight-loss vertical page sells GLP-1 supply explicitly: "Gain access to low cost compounded and branded GLP-1 medications for your program" (compounded GLP-1s exclude Mississippi). The health-plans page leads with outcomes ("reduce readmittance rates by as much as 30%"). An "AI-Powered Operations" section claims AI-streamlined clinical workflows, patient support, and care pathways. Implicit contrast: "No more rigid, traditional telehealth solutions."

## Nav structure

```
- Companies
  - Our Services
    - Provider Staffing — /provider-staffing
    - Technology Platform — /technology-platform
    - Payer Coverage + RCM — /payer-coverage-rcm
    - Licensing + Credentialing — /licensing-credentialing
    - Diagnostic Imaging — /diagnostic-imaging
    - Regulatory + Legal — /regulatory-legal
    - Practice Management — /practice-management
  - Who We Serve
    - Health Plans — /companies/health-plans
    - Diagnostic Labs — /companies/diagnostic-labs
    - Retailers + Pharmacies — /companies/retailers-pharmacies
    - Hospitals + Health Systems — /companies/hospitals-health-systems
  - What We Deliver
    - Medical Weight Loss — /companies/medical-weight-loss
    - Mental + Behavioral Health — /companies/mental-behavioral-health
    - Primary + Urgent Care — /companies/primary-and-urgent-care
    - Longevity — /companies/longevity
- Clinicians
  - Clinician Jobs
    - Clinician Job Board — https://clinician.openloophealth.com/job-board/
  - Services
    - Clinician Network — https://clinician.openloophealth.com/
- Resources
  - Blog — /blog
  - Whitepapers — /whitepapers
  - News — /news
- About
  - Our Team — /team
  - Careers — /careers
  - Contact Us — /contact
- Contact Sales — /contact-sales
- Patient Support — /patient-support
```

## Credibility & proof

All self-reported unless noted:

- **Scale claims (homepage "Our achievements"):** "Trusted by 3M+ patients annually" · "20k Clinicians In Our Network" · "250K Patient visits per month" · "600+ Nationwide insurance plans including Medicare & Medicaid" · "Serving patients in ALL 50 states" · "30+ Specialties" · "24/7 Patient Support"
- **Clinician-count discrepancy:** the health-plans page says "NCQA-accredited network of 16,000+ clinicians spanning 30+ specialties and over 15 languages" vs the homepage's "20k" — both verbatim, captured same day.
- **Certifications/badges (footer):** LegitScript approved (linked seal) · Vanta SOC 2 badge · AICPA SOC badge · "NCQA accredited/certified" claimed across staffing and credentialing pages
- **Ratings:** BBB "A+ / BBB Accredited Business" (self-reported in homepage JSON-LD) · Trustpilot and Google review graphics on the homepage hero (static images, not live widgets)
- **Press (on /team, self-hosted):** "Telehealth Startup OpenLoop Raises $15 Million to Streamline Virtual Care Delivery" (Series A per the linked slug) · "Des Moines' Bank of America Building Renamed OpenLoop Tower"
- **Quality claims:** "98% accuracy rate on claims" (RCM page)

## Visual & brand impression

Polished, current B2B-SaaS aesthetic on a light ground: Inter throughout, navy (#192b58) wordmark and headings, and a signature magenta/pink (#E90C54) carrying the logomark (a knotted-loop mark), every CTA, and link accents — pastel blue-pink gradients soften section breaks. Imagery is upbeat stock-style lifestyle photography of clinicians and patients on video calls, plus product UI mockups in laptop frames. The site reads like a funded growth-stage company: consistent system, heavy section rhythm, conversion-oriented (a "Contact Sales" button recurs in nearly every section), with trust badges concentrated in the footer.

## Strategic read

OpenLoop is the arms-dealer of the telehealth cohort — it powers the D2C brands the rest of the store captures, selling staffing, GLP-1 supply access, compliance, and tech to them rather than competing for patients. The weight-loss vertical page is unusually explicit about compounded GLP-1 economics ("low cost compounded and branded GLP-1 medications," Mississippi carve-out), placing it squarely in that supply chain. Two-sided structure (client orgs on one side, a recruited 1099 clinician network on the other) plus speed-to-launch metrics ("48 hours out-of-box," "1 week" staffing) are the core differentiation story; "AI-Powered Operations" is the 2026 layer on top.

## Provenance

- **Pages:** 10 analyzed (homepage + team, provider-staffing, technology-platform, payer-coverage-rcm, licensing-credentialing, practice-management, clinicians/clinician-network, companies/medical-weight-loss, companies/health-plans), via firecrawl, 2026-06-11.
- **Verify:** all sourceURLs match, all bodies md5-unique, no junk soft-404s.
- **Credits:** 11 (1 map + 10 scrapes).
- **Couldn't get:** any pricing (none published — sales-gated); /diagnostic-imaging, /regulatory-legal, and 6 of 8 vertical pages (not scraped this run); round details behind the $15M press headline.
- **Run profile:** guided — emphasis "services/care-delivery model + who they power"; +logos.
- **Structured layer:** homepage JSON-LD read — Organization (founder Dr. Jon Lensing, foundingDate 2020-01-01, legalName-style "OpenLoop Health, Inc." → aliases, sameAs → socials, BBB A+ → Credibility); JSON-LD logo URL (app.openloophealth.com) fetch-failed, wordmark extracted from header inline SVG instead; nav region validated against the homepage screenshot.
