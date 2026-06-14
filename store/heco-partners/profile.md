---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: heco.partners
name: Heco Partners
aliases: ["Heco", "helloheco.com"]      # JSON-LD org email is info@helloheco.com; Instagram handle is @helloheco
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/helloheco/
external: {}

# Capture meta
captured_at: 2026-06-12
capture_method: firecrawl
site_notes: "Webflow site (cdn.prod.website-files.com); they self-describe as official Webflow Experts. Nav is in a bare div (no <header>/<nav>) — rebuild from screenshot. Hero logotype is a Lottie animation (Heco Logo_*_v3.json), not a static asset — only hostable mark is the favicon. branding.colors are Webflow defaults (#3898EC blue), NOT the real palette — read it off the screenshot. Two office clocks (Charleston SC / Chicago IL) render live on home/about/contact. Founding year conflicts across pages (see unverified)."
key_pages:
  about: /about
  faq: /faq
  contact: /contact
  work: /work
  work_proximie: /work/proximie
  work_manresa: /work/manresa-wilds
unverified_fields:
  - "Founding year conflicts: homepage + JSON-LD say 'Since 2016' / 'celebrates 10 years in 2026'; FAQ says 'doing this since 2014.' Both recorded verbatim, unreconciled."
  - "Typeface names not identifiable — branding.fonts empty; described visually only (high-contrast serif display + monospace labels)."
  - "Project pricing — 'custom-scoped,' no figures published ('not the cheapest... not bloated'). Engagement length 12-16 weeks is the only published quantum."
  - "No standalone static wordmark asset — hero logotype is a Lottie animation; wordmark logos slot omitted on that basis."

# Description
description: "A partner-led creative consultancy that turns complex, technical products into brand strategy, visual identity, messaging, and Webflow websites for enterprise, growth-stage, and early-stage teams."

# Classification
entity_type: Company
target_market: [B2B]
offering_category: [Services / Consulting]
portfolio_shape: Flagship + companions
business_model: Services / Project-based
primary_industry: Consulting & Professional Services

# Visual identity — branding payload colors are Webflow defaults; palette read off screenshots.
logo_url: https://cdn.prod.website-files.com/67f7d37bc7061541937b2258/69739221de5e37c786711ece_favicon-lg.png
logos:
  logomark: { src: "https://cdn.prod.website-files.com/67f7d37bc7061541937b2258/69739221de5e37c786711ece_favicon-lg.png", px: 256, transparent: false }   # clean "HECo" wordmark, white on solid black
  og:       { src: "https://cdn.prod.website-files.com/67f7d37bc7061541937b2258/697caf4b13b0d30953e40e11_3fd3200b84fc9520937dd9347be9b5b0_img-opengraph.jpg", w: 1200, h: 630 }
brand_colors: { primary: "#282828", accent: "#F45946" }   # near-black + warm paper; red-orange/yellow accents from testimonial cards (#F45946, #FBC145)
fonts: [Source Serif 4, ABC Favorit]   # branding re-scrape 2026-06-12 (.payloads/branding-refetch.json): heading slug "source-serif-4-display" (the big serif heroes), body "ABC Favorit" — unlike colors, the font payload matches the screenshot
color_scheme: light
design_framework: webflow
---

## Overview

Heco Partners is a partner-led creative consultancy specializing in branding and web design for "complex products" — companies whose offering is technical or hard to explain. The pitch is "We make the hard simple": distill a complicated product story into a sharp brand and a conversion-oriented website that "compel belief and action." Work spans brand strategy, visual identity, messaging, web design, Webflow development, and product-marketing/launch support, delivered hands-on by the two partners rather than handed to a junior team. Clients skew tech, healthcare, real estate, and mission-driven institutions, at inflection points — a raise, a scale-up, a launch, or a rebrand.

## What they offer

Custom-scoped service engagements (no published rate card) organized as eight capability areas, sold mostly as an integrated branding **+** web engagement plus two packaged on-ramps:

- **Brand Strategy:** brand positioning, naming, voice traits `[on-request]`
- **Visual Identity:** identity design, brand guidelines, creative direction `[on-request]`
- **Content & Messaging:** content strategy, strategic messaging, copywriting `[on-request]`
- **Web Design:** UX design, web design, interactive prototyping, motion graphics `[on-request]`
- **Web Development:** Webflow front-end builds, CMS implementation, lead-gen/conversion, SEO enablement — "one of [Webflow's] official Experts" `[on-request]`
- **Marketing & Activation:** campaign creative, marketing assets, internal comms, investor presentations `[on-request]`
- **Founder Sprint:** a packaged early-stage offering — "brand and product launch" + a "conversion-ready website," delivered fast `[on-request]`
- **Executive Consulting:** C-suite/founder work — strategic messaging, executive decks, keynote support, investor comms `[on-request]`

Typical branding + web engagement runs **"12-16 weeks depending on scope."** They'll take branding-only or web-only when the other half is already strong, and convert many clients into ongoing retainers. Explicitly **don't** do ongoing social-media management or off-the-shelf packages.

## How it works / model

Project-based, custom-scoped from the client's goals/timeline/team, billed per engagement (retainers for ongoing work). Two intake lanes split by stage: **enterprise@heco.partners** (enterprise) and **earlystage@/startup@heco.partners** (growth-stage), each with its own contact card. Process runs five phases — **Discovery → Branding → UX & Content → Visual Design → Development** — content-first for web ("structure, narrative, and messaging before we start designing"). Positioned as premium: "We're not the cheapest option, but we're not bloated, either."

## Positioning & audience

- **Target:** ambitious B2B teams "at inflection points" — startups pre-raise, early-stage companies scaling, enterprises launching something new; mostly tech, healthcare, real estate, mission-driven.
- **Claimed edge:** partner-led with "no layers, no B-team, no agency bloat" — every project gets the partners' direct attention; strategy-first creative tied to business outcomes ("Form follows strategy... cool means it works").
- **Named clients (verbatim, FAQ):** "companies like Google, Motorola Solutions, Identity Digital, Name.com, Core Spaces, and Cresco Labs, as well as cultural institutions like the Museum of Science and Industry and Kellogg School of Management."

## Nav structure

Rebuilt from the homepage screenshot (nav is a bare div, no `<header>`/`<nav>`):

```
- Work — /work
  - Proximie — /work/proximie
  - Core Spaces — /work/core-spaces
  - Hub on Campus — /work/hub-on-campus
  - Name.com — /work/name
  - Identity Digital — /work/identity-digital
  - Manresa Wilds — /work/manresa-wilds
- About — /about
- Contact — /contact
- FAQ — /faq
```

## Credibility & proof

- **Awards (self-reported, verbatim):** "recognized with over 11 awards from Awwwards.com, including Site of the Day and Mobile Excellence." Award badges shown: Awwwards, SiteInspire, Webflow, Communication Arts, CSS, Mindsparkle, OBIE.
- **Webflow Expert:** "one of its official Experts" — specializing in "interactive, narrative-driven sites."
- **Tenure (self-reported, conflicting):** "Since 2016" / "celebrates 10 years in 2026" (home + JSON-LD) vs. "doing this since 2014" (FAQ).
- **Testimonials (named, verbatim):** Rachel Sterling, CMO at Identity Digital ("the primary architects of our brand redesign"); Mitch Dalton, Chief Director of Design at Core Spaces; Jessica Vonashek, Executive Director, Manresa Island Corp.
- **Case-study proof point (Proximie):** "bounce rates dropped from 75% to 23%, session time increased, and lead volume rose month over month" post-launch (self-reported).
- **Press:** NYTimes coverage of the Manresa Wilds / Manresa Island project (Oct 2025, linked).

## Partners

Two named partners lead every project hands-on (about page, verbatim): **JT Helms, Partner** (Charleston, SC) and **Matt Cowen, Partner** (Chicago, IL). The firm operates from those two cities; no other staff are named.

## Visual & brand impression

Confident, design-forward, and deliberately playful — a studio showing off its own craft. The hero is an oversized, **hand-drawn distorted "HECO" logotype** (a Lottie animation) that wobbles against a warm near-white paper background; below it, a high-contrast modern **serif display** sets "We make the hard simple," paired with tiny **monospace** all-caps labels ("BRANDING AND WEB FOR COMPLEX PRODUCTS") and live city clocks for a precise, editorial feel. Whimsical single-line illustrations (a butterfly on water, a bee in sunglasses, a cat-and-bird riding a bike) run through the site and carry the "Maxims" section, signaling low-ego warmth ("proudly human-made"). Full-bleed dark sections punctuate the light paper. There's also a clean, geometric **"HECo" wordmark** (favicon + OG cover, tagline "A brand consultancy for complex products") — the buttoned-up counterpart to the messy hero mark. Accent pops of red-orange (#F45946) and yellow (#FBC145) appear on testimonial cards. Overall read: a senior, awards-shelf studio that pairs serious strategic positioning with handmade, anti-corporate texture.

## Strategic read

Heco is a **two-partner boutique** that competes on seniority and craft, not scale — the entire pitch is "you get the partners, not a B-team." The niche is sharp and defensible: branding + web for **complex/technical products** (surgical-OS software, domain registries, student housing, ecological land reclamation), where the core job is translation — making something hard feel simple and trustworthy. They're deeply tied to **Webflow** as the build platform (official Experts, content-first process), which both differentiates them and bounds them toward marketing-site work rather than product/app engineering. Revenue shape is classic agency: project engagements (12-16 wks) converting to retainers, segmented enterprise vs. early-stage with a productized **Founder Sprint** to capture pre-raise startups cheaply. The conflicting founding dates (2014 vs. 2016) are the only data crack worth noting.

## Provenance

- **Pages:** homepage, /about, /faq, /contact, /work/proximie, /work/manresa-wilds (6 pages, Firecrawl scrape + screenshots + homepage JSON-LD/branding signals).
- **Verify:** all 6 sourceURLs matched, all bodies md5-unique, no junk soft-404s; post-write lint clean.
- **Credits:** see `fc.py spend` — 8 calls (1 map + 7 scrapes).
- **Couldn't get:** project pricing (custom-scoped, never published); typeface names (branding.fonts empty); a static wordmark asset (hero is a Lottie animation).
- **Run profile:** guided — +logos module (logomark + og; wordmark omitted, no static asset).
- **Structured layer:** homepage JSON-LD (CollectionPage/Organization) supplied addresses (Chicago IL + Charleston SC), org email info@helloheco.com → aliases, and a generic instagram sameAs (resolved to @helloheco via footer). No alternateName/legalName/AggregateRating present. Nav rebuilt from screenshot (bare-div nav).
