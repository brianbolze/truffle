---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: ideo.com
name: IDEO
aliases: ["IDEO LLC"]                 # legal entity per site privacy/marketing copy
parent: []                            # independent; "© 2026 IDEO" / IDEO LLC, no parent on site
owns: []                              # IDEO U (ideou.com) + IDEO.org (ideo.org) are framed as "Collective" affiliates — ownership not established on site; see Strategic read
socials:
  linkedin: https://www.linkedin.com/company/ideo/
  instagram: https://www.instagram.com/ideo
external: {}                          # no JSON-LD sameAs / no third-party record links on site

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Webflow build (cdn.prod.website-files.com; framework read from rawHtml, not branding.designSystem which says 'custom'). Mega-nav lives in a real <nav> — recovered cleanly via signals. Header wordmark = 4 per-letter inline SVGs (toggled-layer 43x43 boxes, i_/d_/e_/o_); no single combined wordmark asset exists, so reconstructed to assets/wordmark.svg. Brand palette = dark #151F27 + signature lime #D9FF00. NO JSON-LD on homepage (signals empty). NO pricing anywhere (bespoke consulting). Editorial 'Edges'/'Emerging Wave' lives at edges.ideo.com (subdomain, map-dropped). IDEO U (ideou.com) + IDEO.org (ideo.org) are separate affiliated domains, not on this site."
key_pages:
  about: /about
  design_services: /design-services
  work: /work
  health: /health
  ai: /ai
  playlab: /playlab
  iq: /iq
  leaders: /leaders
  contact: /contact
  careers: /careers
unverified_fields:
  - "Headcount / revenue / funding — not on a marketing site (deep-research job)."
  - "Studio vs. office count — 5 studios named in nav (Cambridge, Chicago, London, San Francisco, Shanghai); total office footprint not stated."
  - "IDEO U (ideou.com) and IDEO.org (ideo.org) ownership vs. affiliation — site groups them as 'Collective' without ownership detail; not captured (separate domains)."
  - "Font family — branding payload names 'Fhoscar' as display; could not confirm the name from screenshots (geometric grotesque visible, name not legible)."

# Description
description: "A global design and innovation consultancy that helps organizations research, prototype, and bring new products, services, brands, and capabilities to market — using the human-centered design and design-thinking practice it pioneered."

# Classification
entity_type: Company
target_market: [B2B, B2G]
offering_category: [Services / Consulting]
portfolio_shape: Flagship + companions   # flagship = bespoke design/innovation consulting; companions = the named Labs (Health, AI, Play)
business_model: Services / Project-based
primary_industry: Consulting & Professional Services

# Visual identity
logo_url: store/ideo-com/assets/wordmark.svg
logos:
  wordmark: { src: store/ideo-com/assets/wordmark.svg, w: 172, h: 43 }                                                        # reconstructed from header per-letter SVGs — the boxed [I][D][E][O] mark, dark on transparent
  logomark: { src: "https://www.google.com/s2/favicons?domain=ideo.com&sz=256", px: 256, transparent: false }                 # the IDEO 2x2 grid mark, black-on-white (opaque); on-domain twin at .../69375a9ab7d2ba7920eeeb01_ideo_favicon_large.png
  og:       { src: "https://cdn.prod.website-files.com/67cb2dd62d5110e2973d39d7/694084b0cebf86476a5b4e1e_IDEO_opengraph.png", w: 2577, h: 1349 }   # lime banner: "Human centered design" + grid mark
brand_colors: { primary: "#151F27", accent: "#D9FF00" }   # dark navy canvas + signature electric lime (the distinctive hue)
fonts: [Fhoscar]                      # branding.fonts[0] (display); name unconfirmed from screenshots — see unverified_fields
color_scheme: dark
design_framework: Webflow             # rawHtml: Webflow x6, wf- x18, data-wf x4, website-files.com CDN
---

## Overview

IDEO is a global design and innovation consultancy. Founded in **Palo Alto in 1991** by **David Kelley, Bill Moggridge, and Mike Nuttall**, it pioneered and popularized **human-centered design** and **design thinking** (the latter named and spread by former CEO **Tim Brown** via his 2009 book *Change by Design* and TED talk). IDEO partners with enterprises, startups, governments, and nonprofits to research human needs, build strategy, prototype, and bring products, services, brands, and whole organizations to market. It works through **five studios** — Cambridge, Chicago, London, San Francisco, and Shanghai — and is known for iconic early work such as Apple's first usable mouse (1990) and PillPack.

## What they offer

Bespoke design & innovation engagements — **no published pricing** (every offering is consult-gated; all lines `[on-request]`). Breadth, not per-SKU depth (no `offerings.md` — a services firm has no SKU grain; see Provenance):

- **Design Services — Strategy & growth:** purpose articulation, organizational transformation, vision activation, experiential prototypes — *"Build your next frontier of serious growth"* `[on-request]`
- **Design Services — Human-centered strategy:** customer & employee research, emerging-tech audit and planning, futuring and strategy design, organizational change `[on-request]`
- **Design Services — Get to market:** rapid prototyping and research, industrial design, digital product design, go-to-market strategies `[on-request]`
- **IDEO Health (Lab):** healthcare & life-sciences design — *"Making. Healthier. Human. Futures."*; patient care, digital health, medical devices `[on-request]`
- **IDEO AI / Emerging Tech Lab:** human-centered AI products + org-wide AI adoption — *"Design for agency, before agents."* `[on-request]`
- **IDEO Play (Play Lab):** play, games, and facilitation applied to org/product design — *"Applying the power of play far beyond the world of toys."* `[on-request]`
- **Editorial / thought-leadership IP:** *The IDEO IQ* (Innovation Quotient) report + 8-min self-assessment survey; *Thinking* journal; *Edges* / *Emerging Wave* (edges.ideo.com) — lead-gen + brand, not sold

Adjacent **"Collective"** entities on separate domains (not part of IDEO's own engagements): **IDEO U** (ideou.com — online creative-leadership courses, B2C) and **IDEO.org** (ideo.org — nonprofit social-impact design).

## How it works / model

Project-based consulting: a client engages IDEO for a bespoke engagement, scoped through one of three contact paths the site funnels everything to — **Partner on a project**, **Media Inquiry**, or **Careers and Internships**. Delivery follows IDEO's human-centered design process — **Inspiration → Ideation → Implementation** — emphasizing field research, rapid prototyping, and iteration with real users. Revenue is project/retainer-based (no subscription, no published rates); multidisciplinary teams ("not just designers — registered nurses to magicians, architects to chefs") staff engagements out of the five global studios.

## Positioning & audience

Targets *"the world's most imaginative leaders"* — large enterprises (Ford, Moderna, H&M, Sephora, IHG, FEMSA, Eli Lilly), venture-backed startups (Teal Health, Omada, Willow, Kooth), and the public/social sector (LA County, NHSx, Massachusetts DMH, Planned Parenthood). Claimed edge: it *"pioneered human-centered design and design thinking"* and *"designs the conditions for innovation itself,"* not just products — interdisciplinary teams, prototyping-led, with ~decades of cross-industry range. Competes against other design/innovation consultancies and strategy/transformation firms. Current emphasis: defending design's ROI in the AI era (the IDEO IQ report) and an AI/emerging-tech practice.

## Nav structure

```
- About
  - About IDEO — /about
  - Our leaders — /leaders
  - Careers — /careers
  - Contact — /contact
- Studios
  - Cambridge — /cambridge
  - Chicago — /chicago
  - London — /london
  - San Francisco — /sanfrancisco
  - Shanghai — /china
- Services
  - Overview — /design-services
  - Case studies — /work
- Labs
  - IDEO Health — /health
  - IDEO AI — /ai
  - IDEO Play — /playlab
- Editorial
  - The IDEO IQ — /iq
  - Thinking — /thinking
  - Edges — https://edges.ideo.com/
  - Emerging Wave — https://edges.ideo.com/
  - Subscribe — /subscribe
- Collective
  - IDEO U — https://www.ideou.com/
  - IDEO.org — https://www.ideo.org/
- Footer adds: Design services, Work, About us, Our leaders, DEIB (/deib), IDEO Thinking, Careers, Subscribe, IDEO U, China (/china), Privacy, Terms
```

## Credibility & proof

All proof points below are **self-reported** (company site), recorded verbatim, not independently verified:

- **Tenure:** *"For nearly 50 years…"* (the firm itself dates to the 1991 merger; the ~50-yr claim counts predecessor practices). Founders named: David Kelley, Bill Moggridge, Mike Nuttall.
- **Design-thinking origin:** *"then-IDEO CEO Tim Brown put into words a process IDEO had been practicing for decades"* — *Change by Design* (2009) + 2009 TED talk.
- **Marquee testimonials (verbatim title):** Jim Hackett (*Former CEO, Ford Motor Company*); Kara Egan (*CEO & Co-Founder, Teal Health*); Carlos Rodríguez-Pastor (*Chairman of Intercorp*); Najoh Tita-Reid (*Global Chief Growth Officer, Mars Petcare*); Aaron Sefi (*Chief Product & Research Officer, Kooth*); Sean Duffy (*Co-Founder & CEO, Omada Health*).
- **Iconic outcomes (self-reported):** Apple's first usable mouse (1990); PillPack *"would later be purchased by Amazon for $750M+"*; Omada Health *"grows from an IDEO research project to a $1 billion company"*; Eli Lilly — *"Nearly 40 years of designing pharmaceutical excellence."*
- **IDEO IQ research:** *"surveyed leaders from 100 of the world's largest companies"*; methodology — B2B firm NewtonX surveyed **266 leaders** across Healthcare, Media & Technology, and Consumer Goods (companies with *"$1 billion in revenue and 10,000 employees"*), Dec 2025–Jan 2026; company-level scores reported only where n≥3 (n=59 companies). Findings (verbatim): top-20% scorers reported *"nearly 3x the revenue growth… and over $5 billion more in annual profits than average."*
- **Press contact:** press@ideo.com · general: hello@ideo.com.

## Visual & brand impression

High design maturity, as expected. The site runs a **dark charcoal `#151F27`** canvas punched with **electric lime `#D9FF00`** — the distinctive, signature hue (headlines, CTAs, the IQ graphics). The hero is a single line, *"Human-centered…"*, whose final word cycles (design → breakthroughs → futures → growth → intelligence → ingenuity → leadership…). Type is a confident geometric grotesque set large; case studies fill an editorial, gallery-like grid of client logos and hero imagery. The mark itself is iconic: **four boxed letters `[I][D][E][O]`**, rendered as a horizontal wordmark in the header and a 2×2 staircase grid in the OG/share image. Overall feel: premium, playful-but-serious, design-forward — a studio comfortable foregrounding craft.

## Strategic read

Two visible bets. **(1) Proving design's ROI in the AI era:** the inaugural *IDEO IQ* report explicitly ties "human-centered design behaviors" (the POWER Dynamic: Perspective, Ownership, Wavelength, Experimentation, Resonance) to revenue, profit, and AI adoption — a data play to defend high-end design consulting against "AI will do it cheaper." **(2) Productizing domain expertise** into separately-branded **Labs** (Health, AI/Emerging Tech, Play), each with its own page, leaders, and positioning — a way to package bespoke services into recognizable practice areas. The **"Collective"** (IDEO U education, IDEO.org nonprofit) extends the brand past consulting into learning and social impact. Leadership has fully transitioned past the founders: **Mike Peng is CEO (Global)**, with David Kelley as *Founder & Partner Emeritus* and Tim Brown as *Chair Emeritus* — IDEO is now run by a next-generation C-suite (Becca Carroll, CSO; Margo Husted, CFO; Mina Seetharaman, Head of New Ventures).

## Provenance

- **Pages:** 9 captured + analyzed via Firecrawl (all-formats), with screenshots + homepage `branding`/`rawHtml`: homepage, /about, /design-services, /work, /health, /ai, /playlab, /iq, /leaders. Map sampled 485 URLs (journal/* blog filtered out).
- **Verify:** `fc.py verify` — all 9 sourceURLs matched, all 9 bodies unique (md5). Post-write lint re-run.
- **Credits:** 10 (1 map + 1 homepage + 8 key pages); 0 enhanced-proxy retries.
- **Run profile:** guided — output scope "all modules" requested. Built: `+logos:{}` (multi-ratio; wordmark reconstructed to assets/wordmark.svg). **Skipped with reason:** `offerings.md` and the flagship-hero-images module — a bespoke design consultancy has no per-SKU grain and no sellable flagship product to render (its "products" are confidential client work); the family-line breadth in *What they offer* is the right altitude. Emphasis: none.
- **Couldn't get:** any pricing (none published — bespoke engagements); headcount/revenue/funding (not on a marketing site); IDEO U / IDEO.org ownership vs. affiliation; the display font name (Fhoscar per branding payload, unconfirmed visually).
