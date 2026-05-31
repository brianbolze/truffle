---
schema_version: 1

# Identity
domain: delighted.com
name: Delighted
aliases: ["Delighted, LLC", "Delighted, a Qualtrics Company"]
parent: [qualtrics.com]
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "WordPress (wp-content + wp-json + 'blankslate' theme in rawHtml); branding.designSystem reports 'custom' (wrong, per corpus rule). Light theme. Map is large (~373 URLs) and ~70% noise — /blog/* and /our-integrations/* dominate; real product pages came from homepage links + footer, not the map. WP mega-nav renders in markdown but extremely whitespace-padded. Off-domain surfaces: app.delighted.com (login, API docs, terms/privacy), help.delighted.com + surveys-help.delighted.com (support), demo.delighted.com (live demo), roadmap on airfocus. CRITICAL: product is being SUNSET — /sunset page announces shutdown 2026-06-30; /qualtrics is the migration ('graduation') page; annual renewals stopped 2025-07-01, monthly-only until final date. Pricing is one long page: tier cards + full feature comparison table (table user-counts disagree with card user-counts — trust the cards)."
key_pages:
  pricing: /pricing
  sunset: /sunset
  qualtrics: /qualtrics
  features: /features
  cx_solution: /customer-experience-solution
  customers: /customers
  integrations: /our-integrations
unverified_fields:
  - "Whether delighted.com / the brand persists in any form after the 2026-06-30 sunset — not stated."
  - "Headcount, revenue, funding — none on-site (Delighted is folded into Qualtrics)."
  - "Pricing comparison table lists user counts (1/5/10/20) that conflict with the tier cards (Free 1 / Starter 2 / Growth 3 / Advanced 5 / Premium 10); cards quoted as authoritative."

description: "A self-serve experience-management platform (a Qualtrics company) for collecting and analyzing customer and employee feedback through simple NPS, CSAT, and CES surveys — being sunset on June 30, 2026 as customers migrate to Qualtrics."

# Classification
entity_type: Company
target_market: [B2B]
offering_category: [Software / SaaS]
portfolio_shape: Single
business_model: Subscription
primary_industry: Technology

# Visual identity
logo_url: https://delighted.com/wp-content/uploads/2020/02/cropped-favicon-512-1.png   # branding.images.logo not exposed → favicon fallback
brand_colors: { primary: "#4460F6", accent: "#0F181E" }   # periwinkle-blue brand hue on off-white (#F7F7F6); near-black footer/text — verified against screenshot
fonts: [Lausanne, Helvetica Neue]
color_scheme: light
design_framework: wordpress
---

## Overview

Delighted is a self-serve **experience-management (XM) platform** for collecting and acting on
customer and employee feedback. Its wedge is simplicity and speed: prebuilt, best-practice survey
templates (NPS, CSAT, CES, eNPS, 5-star, Smileys, Thumbs, PMF) that a non-technical user can launch
in minutes across email, web, link, SDK, embed, or kiosk, then analyze with built-in dashboards.
Positioned as "the fastest and easiest way to gather actionable feedback," trusted by 75,000+ brands
and powering 300M+ surveys a year. **Delighted is a Qualtrics company (acquired 2018) and is being
sunset on June 30, 2026** — see *Strategic read*.

## What they offer

One platform, two product surfaces (bundled in every plan, not sold separately):

- **Delighted Surveys:** ad-hoc questionnaires (open-ended, rating-scale, multiple-choice) to ask an audience anything.
- **Delighted CX:** automated, ongoing feedback programs built on standard CX metrics: **NPS, CSAT, CES, eNPS, 5-star, Smileys, Thumbs, PMF**.

Delivery across Link, Email, Web, Embed, iOS SDK, and Kiosk; reporting/dashboards with tagging,
trends, and Smart Trends text analysis; "Delighted AI" enhancements; and 35+ free + premium
integrations (Slack, Shopify, Zendesk, Stripe, Square, Salesforce, Segment, HubSpot, and more) plus a REST API and webhooks.

## How it works / model

Product-led, self-serve **subscription** with a freemium entry. Plans (USD, tax-exclusive),
metered by monthly responses + users:

- **Free ($0):** 25 responses, 1 user, no card.
- **Starter ($19/mo):** 50 responses, 2 users.
- **Growth ($39/mo):** 100 responses, 3 users.
- **Advanced ($149/mo):** 250 responses, 5 users.
- **Premium ($249/mo, most popular):** 500 responses, 10 users; 6 premium integrations.
- Custom pricing above that (contact sales).

The model — **"Ask → Analyze → Act"** — survey, read results in dashboards, then route feedback to
the right people via digests and integrations. (Renewal note: annual renewals ended 2025-07-01;
only monthly plans remain, running out at the 2026-06-30 sunset.)

## Positioning & audience

Sells to businesses of all sizes, organized by **industry** (Ecommerce, Tech, Startups, Nonprofits)
and **team** (Customer Experience, Customer Service, Product, Marketing, HR). Claimed edge is
turnkey simplicity vs. heavyweight survey/research suites — best-practice questions baked in, live in
minutes, no technical skills. Explicitly framed as the on-ramp to its parent: *"Start with Delighted.
Grow into Qualtrics."*

## Nav structure

```
- Solutions
  - Industries: Ecommerce — /ecommerce · Tech — /product-survey-templates · Startups — /startups · Nonprofits — /nonprofit-survey
  - Teams: Customer Experience — /customer-experience-solution · Customer Service — /customer-service-surveys
           · Product — /product-survey-templates · Marketing — /marketing-survey-templates · Human Resources — /employee-survey-templates
- Survey Templates
  - NPS — /nps · CSAT — /csat · CES — /ces · Product/Market Fit — /pmf · eNPS — /enps
  - 5-star — /5-star · Smileys — /smiley-face-survey · Thumbs — /thumbs-survey · Custom surveys — /surveys
  - See all — /survey-templates
- Pricing — /pricing
- Resources
  - Resources — /resources · Help Center — help.delighted.com · Integrations — /our-integrations
  - REST API — app.delighted.com/docs/api · Case Studies — /customers · Blog — /blog
  - Community — /community · Product Roadmap (airfocus) · AI Enhancements — /ai
- Footer · Product: Free survey maker, Reporting — /reporting, Delighted AI — /ai, Testimonials — /testimonials,
  Features — /features, Mobile apps — /mobile-apps, Live demo — demo.delighted.com, Web — /web, Link — /link-survey,
  Email — /email, iOS SDK — /sdk, Embed — /embed-platform
- Footer · Company: Delighted + Qualtrics — /qualtrics · Blog — /blog · Jobs — /jobs
- Sign in — app.delighted.com/signin · Contact sales — /contact-sales
```

## Credibility & proof

Logo wall of well-known brands: Allbirds, Instacart, Google, OpenTable, TedX, Affirm, PayPal,
DoorDash, Peloton, Athletic Brewing. Ratings: **4.9 Capterra**, **4.7 G2**. Scale claims: **75,000+
brands**, **300M+ surveys/year**, "every second, 45 people answer a Delighted survey." Dedicated
`/customers` case studies (Bombas, Affirm, FIGS, Rakuten, Glassdoor, HotelTonight, Bonobos, etc.) and
`/security` + `/gdpr` + subprocessor pages. NPS trademark attribution to Bain/Satmetrix/Reichheld in footer.

## Visual & brand impression

Clean, friendly, confident SaaS aesthetic: off-white (`#F7F7F6`) canvas, periwinkle-blue (`#4460F6`)
accents, a dark-navy footer, and a script "Delighted" wordmark. Lausanne/Helvetica typography, warm
human photography (a smiling customer), and soft pastel-blue/pink product cards. Reads as a mature,
approachable, design-led tool — understated next to enterprise-research suites, by design. No visible
sunset banner on the homepage; the wind-down lives on dedicated `/sunset` and `/qualtrics` pages.

## Strategic read

This capture catches a product at end-of-life. **Delighted — acquired by Qualtrics in 2018 — is being
sunset on June 30, 2026**, ~one month after this capture (2026-05-31). Qualtrics framed it as aligning
to its "AI-powered Suites": new features stopped immediately, annual renewals ended July 1, 2025,
and remaining customers run on monthly plans until the cutoff, with self-serve + partner-led
"graduation" migration to Qualtrics (one-click copy of survey/dashboard/dataset). The public site still
markets Delighted as a live, free product with full pricing — but the durable state of this entity is
**a sunsetting on-ramp into its parent's platform**, not an independent growing business. Any downstream
consumer should treat delighted.com as effectively frozen and time-boxed.

## Provenance

- **Pages:** homepage (rich pass), /pricing, /sunset, /qualtrics, /features, /customer-experience-solution (6) — all Firecrawl (`maxAge:0`, `location:US`, `waitFor`); framework read from rawHtml (WordPress / blankslate theme).
- **Verify:** all sourceURL-matched, all md5-unique (clean; no geo/cache contamination).
- **Credits:** not recorded this run.
- **Couldn't get:** post-sunset plans; firmographics (off-site, Qualtrics subsidiary); clean reconcile of pricing table user counts vs. tier cards (conflict noted in unverified_fields).
