---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.3"

# Identity
domain: mdintegrations.com
name: MD Integrations
aliases: [MDI]                       # "MDI" is the company's own shorthand throughout the site; legal name not stated
parent: []
owns: []
socials: {}                          # looked, none found — no JSON-LD sameAs and no social anchors anywhere in the site
external: {}                         # looked, none found

# Capture meta
captured_at: 2026-06-02
capture_method: firecrawl
site_notes: "HubSpot CMS (hubfs/, hs-fs/, _hcms, cta-na2.hubspot.com, portalId 242063962, hubspotusercontent-na2.net) — branding.designSystem='custom' is wrong, ignore. No JSON-LD on homepage; no social links anywhere. Flat nav, no mega-menu. Pricing is demo-gated (on-request) — FAQ #10 confirms no published price. Partner app at partners.mdintegrations.com; status at status.mdintegrations.com; careers via Rippling ATS. Blog (/md-integrations-blog) is ~30 of the 44 mapped URLs — content noise, filter."
key_pages:
  solutions: /solutions
  about: /about
  clinicians: /clinicians
  faq: /faq
  ecommerce: /ecommerce
  contact: /contact
unverified_fields:
  - "Pricing — demo-gated (on-request); FAQ #10: custom 'fair and competitive' pricing after a demo, no published figure. Exact structure (platform fee vs per-consult) not stated."
  - "Client/partner names — not disclosed by policy (FAQ #2); all testimonials anonymized as '— MDI Client'."
  - "Funding stage, headcount, revenue — not on the marketing site (deep-research job)."

# Description — one sentence
description: "A physician-led telehealth infrastructure company: it gives consumer-health and DTC brands a white-label telemedicine API, branded patient apps, and a 50-state board-certified physician network to launch compliant async virtual care in days."

# Classification
entity_type: Company
target_market: [B2B, B2B2C]
offering_category: [Software / SaaS, Services / Consulting]
portfolio_shape: Single
business_model: Subscription          # STRAIN: recurring B2B partner contracts inferred; exact pricing demo-gated (see unverified_fields)
primary_industry: Healthcare & Life Sciences

# Visual identity
logo_url: https://mdintegrations.com/hubfs/logo.svg
brand_colors: { primary: "#188077", secondary: "#354C47" }   # teal #188077 is the true brand hue (CTAs/links/headings); branding payload mis-ranked #354C47 dark-green as primary
fonts: [Poppins, Martel]              # Poppins body, Martel headings
color_scheme: light
design_framework: HubSpot CMS         # rawHtml: _hcms ×16, hubspot ×14, hubfs ×46 — not the 'custom' from branding payload
---

## Overview

A doctor-founded telehealth **infrastructure** company (founded 2021 by Dr. Marc Serota). It supplies the physician network plus the technology layer that lets consumer-health and DTC brands stand up their own *branded* virtual-care service without building clinical operations. The product is a telemedicine API and white-label patient apps backed by a board-certified, **physician-only** clinical network licensed across all 50 states (plus DC and Guam). Positions explicitly as physician-first and compliance-ready — "built by doctors," in contrast to generic telehealth SaaS. Tagline: *"You control the brand, we power the medicine."*

## What they offer

One integrated white-label platform + clinical network, surfaced a few ways. **All pricing is demo-gated** — every line is `[on-request]`:

- **White-label telehealth platform & telemedicine API:** the core product — branded patient intake forms, full messaging (text/audio/video), e-prescribing, physician portal, plus a proprietary "AI assist care" layer; integrate via full-featured APIs & webhooks *or* off-the-shelf white-label apps `[on-request]`
- **50-state physician network ("PC network"):** board-certified MDs/DOs licensed in all 50 states, DC & Guam; the partner contracts with MDI's national Professional Corporation network, so it needs **no medical director or its own PC** — MDI handles physician licensing, credentialing, and supervision `[on-request]`
- **eCommerce plug-ins (Shopify & WooCommerce):** "care that starts at checkout" — install plug-in, configure workflows, go live; Shopify (apps.shopify.com/md-integrations-connect) + WooCommerce (wordpress.org plugin), built with integration partners `[on-request]`
- **Specialty clinical coverage:** "12+ specialties" incl. Weight Loss, Metabolic Health, Longevity, Women's Health (OB/GYN), Men's Health, Erectile Dysfunction, Dermatology, Urgent Care, Internal/Family Medicine, Allergy & Immunology, Pediatrics, Peptide Therapy `[on-request]`
- **Native mobile apps:** iOS + Android, "built for the physician experience first" `[on-request]`

Stated capability boundary: **"We do not prescribe controlled substances"** (FAQ #13) — rules out Schedule II–V workflows (e.g. TRT) on this network.

## How it works / model

- **Three-step flow:** 01 Connect (telemedicine API or white-label apps) → 02 Intake & Consult (patient completes a simple intake form, MDI's physician network handles the consult) → 03 Easy Flow (the applicable Rx is sent to the **patient's pharmacy of choice**).
- **Async-first** (also synchronous/hybrid), **24/7/365** coverage. A "proprietary assignment algorithm" reassigns cases after ~4 hours (the SLA); **"52 mins" average doctor response**; follow-up visits route back to the same doctor (continuity of care).
- **~7-day integration** from service mapping to go-live; "launch in days, not months."
- **Pharmacy-agnostic & fulfillment-flexible:** supports e-prescribing and connecting to pharmacy partners (branded, generic, or subscription treatment plans); can facilitate **patient insurance** for consults and prescription meds. Patient ID verification via custom tech or **Vouched™** integration.
- **Revenue (inferred, opaque):** recurring B2B partner contracts; pricing is custom after a demo ("fair and competitive," "low startup fees to engage"). Engagement perks: "No charge for the Professional Corporation aka 'Medical Group'" and "Free messaging and refills for one year." Post-integration dev+medical support capped at ~4 hrs/month, more by surcharge.
- **Clinician side:** physicians are recruited directly (no competitive case-claiming), paid on a **pay-per-case** structure, working through a physician portal with Face ID + 2FA.

## Positioning & audience

- **Sells to:** DTC brands, digital health companies, labs & diagnostics, pharmaceutical companies, weight-loss companies, retailers, pharmacies, and wellness companies — "easy for startups and flexible for larger enterprises."
- **Claimed edge:** *"the only white-label telemedicine platform powered exclusively by physicians"*; doctor-founded/doctor-led; partners "work directly with the doctors who can effectuate the work. No middle men, no sales people, no empty promises." Framed as a physician-first **thought partner**, not a generic vendor.

## Nav structure

Flat top nav (no mega-menu; validated against the homepage screenshot):

```
- Home — /
- Company — /about
- Clinicians — /clinicians
- Solutions — /solutions
- Get in Touch — /contact
- FAQ — /faq
- Resources — /resources-1
- Login — https://partners.mdintegrations.com/login
```

Footer adds: Careers (Rippling ATS), Status (status.mdintegrations.com), Terms (/tos), Data Requests, Security Controls, and iOS/Android app-store links.

## Credibility & proof

All metrics are **self-reported** (verbatim):
- **"3M+ patient visits completed"** / "3M+ consults completed"
- **"Trusted by 200+ healthcare companies"** / "200+ brands supported"
- **Compliance:** SOC 2 (Type II), HIPAA, ISO certified, and **LegitScript approved** (footer seal links to legitscript.com verification — the one third-party-verifiable badge).
- **">99.9%" uptime**, **"100K" visits per month**, "24/7/365" availability.
- **Founder credibility:** Dr. Marc Serota — quadruple board-certified (obesity medicine, dermatology, pediatrics, allergy/immunology), "licensed in 45 states," practicing telemedicine since 2014, national speaker.
- **Named leadership:** Marc Serota MD (CEO & Founder), Ramin Zacharia (President & COO), Felipe Tadra (CTO), Ben Clement (SVP Finance), Tia Bedoya (SVP HR).
- **Testimonials** are present but **anonymized** ("— MDI Client") — client names withheld by policy.

## Visual & brand impression

Clean, corporate **healthcare-infrastructure** aesthetic — reads as a credible B2B platform, not a consumer brand. Near-white background (#F4FCFB) with a teal (#188077) + dark slate-green (#354C47) palette, pill-shaped CTAs, Poppins/Martel type pairing. Trust scaffolding throughout: a US coverage map graphic (50 states), product-UI screenshots of the portal/intake, a "previously worked for" logo wall, the founder's headshot, compliance seals, and a full-bleed teal proof section. Mature, professionally designed; tone is clinical and reassuring, balancing medical legitimacy with technical capability.

## Strategic read

The **picks-and-shovels layer beneath DTC telehealth brands** — the explicit "buy, don't build" alternative for launching branded virtual care (clinical network + compliance + tech in one contract). Three distinctive facts:
1. **Controlled-substances exclusion is a hard line** — "we do not prescribe controlled substances," which bars Schedule III workflows like TRT on this network. The single most decision-relevant constraint for any regulated-molecule brand.
2. **Pharmacy-agnostic** — routes Rx to the patient's/partner's pharmacy of choice and connects to pharmacy partners; it sits *upstream* of fulfillment rather than owning it, so it pairs with (rather than replaces) a compounding/dispensing partner.
3. **Contracted national PC network** removes the partner's need for its own medical group/medical director — MDI owns licensing, credentialing, and supervision, which is the heaviest regulatory lift it absorbs.

Minor discrepancy worth flagging: the homepage markets a network "powered **exclusively** by physicians," but the clinician-recruiting page invites "physician, nurse practitioner, or clinician" — reported, not reconciled.

## Provenance

- **Pages:** homepage, /solutions, /about, /clinicians, /faq, /ecommerce — Firecrawl scrape (markdown + full-page screenshot), 2026-06-02. /map returned 44 URLs (~30 were /md-integrations-blog content) used for inventory only.
- **Verify:** all 6 sourceURLs matched the requested URLs; all 6 body md5s unique — no geo/cache contamination.
- **Credits:** 7 (1 map + 1 all-formats homepage + 5 key pages). No enhanced-proxy or PDF spend.
- **Couldn't get:** pricing (demo-gated, FAQ #10); client names (withheld by policy, FAQ #2); funding/headcount/revenue (not on site).
