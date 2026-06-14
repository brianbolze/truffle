---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: redantler.com
name: Red Antler
aliases: []
parent: ["Red Antler Group"]   # STRAIN: umbrella family of partner studios (no standalone domain) — its page lives on this same site; JB Osborne is its CEO
owns: []
socials:
  instagram: https://www.instagram.com/redantler
  linkedin: https://www.linkedin.com/company/red-antler
external: {}

# Capture meta
captured_at: 2026-06-12
capture_method: firecrawl
site_notes: "Next.js front end, Sanity CMS (cdn.sanity.io images). No JSON-LD on homepage. Flat top nav (no mega-menu). All content public — no pricing anywhere (project-based agency, contact-gated). Sibling studios on own domains: fat-earth.com, wildfruit.co. Extra subdomains: play.redantler.com (interactive easter egg), stateofbrand.redantler.com (annual report). Leadership/founding/awards live on /about (#fast-facts, #leadership)."
key_pages:
  about: /about        # What We Do (service lines) · Fast Facts · Leadership
  clients: /clients    # Launch / Transform engagement modes
  ai: /ai              # AI-company positioning + testimonials
  work: /work          # full portfolio
  careers: /careers
unverified_fields:
  - "Pricing — none published; agency engagements are project/retainer-based and contact-gated (no rate card on site)."
  - "Headcount, revenue, ownership/funding — not on the marketing site (deep-research job)."

# Description — one sentence
description: "A New York brand-building agency that partners with startups and category leaders — from pre-launch founders to incumbents reinventing — across strategy, naming, visual/verbal identity, advertising, and performance media."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2B]
offering_category: [Services / Consulting]
portfolio_shape: Single   # one integrated brand-building service sold in phases (Foundation/Strategy → Brand/Digital → Advertising → Media)
business_model: Services / Project-based
primary_industry: Consulting & Professional Services

# Visual identity — branding payload is a hint; confirmed against homepage screenshot
logo_url: assets/wordmark.svg   # canonical wordmark — extracted from the inline data-URI <svg>, cream fill normalized to currentColor
logos:
  wordmark: { src: assets/wordmark.svg, w: 150, h: 27 }                                                              # rectangle "Red Antler" wordmark; committed SVG text (was an inline data-URI)
  logomark: { src: "https://www.google.com/s2/favicons?domain=redantler.com&sz=256", px: 256, transparent: true }   # the antler symbol; bg index alpha=0 (genuinely transparent, verified by palette tRNS)
  og:       { src: "https://cdn.sanity.io/images/6q3eaif3/production/ea96e60f6210e731b2a1fec77a2e0dd5d650f250-1200x630.png?fm=webp&w=1200&q=75", w: 1200, h: 630 }  # on-brand cover: flowering-antler render on cream
brand_colors: { primary: "#FF0000", accent: "#E9EBDC" }   # signature bright red (full-bleed red footer) over a charcoal #222222 + cream #E9EBDC editorial palette
fonts: [ABC Favorit]
color_scheme: light   # cream (#E9EBDC) ground, charcoal text; alternates into dark charcoal + red full-bleed sections
design_framework: next.js
---

## Overview

Red Antler is a New York brand-building agency (founded 2007) whose homepage leads "We partner with rule-breakers and future-makers" — ambitious startups and established companies at pivotal moments; its pre-launch team turns brand-new ideas into "brands you can't live without." It made its name branding the DTC/startup generation (Casper, Allbirds, Cotopaxi) and now works across consumer, B2B, and deep-tech. Co-founded by Emily Heyward (Co-Founder & CEO) and JB Osborne (now Co-Founder & CEO of the parent Red Antler Group). The agency sits at the head of **Red Antler Group**, a family of three partner studios spanning brand, performance media, and presentation design.

## What they offer

Sold as integrated, done-for-you engagements organized into four practice areas — no published rates (agency, project/retainer-based). Service lists verbatim from `/about` "What We Do":

- **Foundation & Strategy:** Research, Naming, Brand Strategy, Brand Architecture, Change Management — establishing a "differentiated North Star." `[on-request]`
- **Brand & Digital:** Visual Identity, Verbal Identity, Sonic Identity, User Experience Design, Visual Design, Packaging Design, Apps + Product Design, Physical Experience Design, Engineering & Technology. `[on-request]`
- **Advertising:** Campaign Strategy, Channel + Comms Planning, Integrated Brand Campaigns, Experiential, Brand Films / Video (OTT, CTV, OLV), OOH/DOOH, Social, Direct Marketing, Influencer, Shopper. `[on-request]`
- **Media:** Growth Strategy, Media Planning and Management, Lifecycle and CRM Marketing, Creative Strategy, Performance Creative, Landing Page Strategy and Design — "creative performance marketing and media for brand-led businesses" (delivered via sibling studio Fat Earth). `[on-request]`

## How it works / model

Project-based and retainer agency engagements; the only CTA is "Get in touch" / Contact — no self-serve or pricing. From `/clients`, two engagement modes:

- **Launch:** "Our dedicated pre-launch team works directly with founders to turn brand new ideas into brands you can't live without." Pre-launch incubation/naming/identity for new ventures.
- **Transform:** "From campaigns to brand evolutions to incubation, we work with businesses seeking to defend or claim category leadership." Rebrands, campaigns, and evolution for incumbents.

Tagline framing: *"The higher the stakes, the better we work."*

## Positioning & audience

Targets founders and brand-led businesses — startups at launch and category leaders reinventing. Positions itself as "the leading creative partner shaping what's next." Current heavy emphasis on **AI companies** (dedicated `/ai` page): "helping AI-driven companies tell stories of innovative optimism… strike the right balance of technology and humanity and ensure you get credit for innovation" — AI clients include Figure, Pika, Ori, Matic, Duckbill, Amori, Raft, Fyxer. Competes with other top creative/brand agencies (not named on site).

## Nav structure

Flat top nav (no flyouts) — confirmed against screenshot:

- [Work](https://www.redantler.com/work) — portfolio (~80+ case studies)
- [About](https://www.redantler.com/about) — What We Do · Fast Facts · Leadership
- [Clients](https://www.redantler.com/clients) — Launch / Transform engagement modes
- [News](https://www.redantler.com/news) — Perspective + Press
- [Careers](https://www.redantler.com/careers) — open roles via breezy.hr
- [Contact](https://www.redantler.com/contact)

Off-nav properties: [play.redantler.com](https://play.redantler.com/) (interactive easter egg), [stateofbrand.redantler.com](https://stateofbrand.redantler.com/) (annual "State of Brand" report).

## Credibility & proof

- **Founded / base:** 2007, New York, NY; "clients all over the world." (`/about` Fast Facts)
- **Awards (self-reported):** Fast Company's "Most Innovative"; Inc's "Top 10 Entrepreneurs of the Decade"; Entrepreneur's "Most Powerful Women in Business."
- **Book:** *Obsessed: Building a Brand People Love From Day One* by co-founder Emily Heyward (Portfolio/Penguin) — "We wrote the book on the New Rules of Branding."
- **Client outcome claims (self-reported, homepage):** Hinge — "Fastest-growing dating app"; AllTrails — "iPhone App of the Year"; Ramp — "$32B valuation"; Archer — "$1B order from United Airlines"; Chime — "Named to TIME's 2024 World's Best Brands list."
- **Testimonials (verbatim, `/ai`):** Tim Brown (CEO/Co-Founder, Allbirds) — "simply the best at what they do"; Diego Zaks (VP Design, Ramp) — "a brilliant extension of our own"; Brett Adcock (CEO Figure) — "couldn't imagine a better partner"; Philip Krim (Casper co-founder) — "like a cofounder to us"; plus Coatue and Lerer Hippeau (Ben Lerer).
- **Notable clients (from Work/AI/homepage):** Casper, Allbirds, Cotopaxi, Ramp, Hinge, AllTrails, Chime, Eight Sleep, Knix, Bonobos, Prose, Clear, Google Fiber, McKinsey, Tech:NYC, USAFacts, Onnit, Sheertex, Supergoop, Furby, Petlibro, Figure, Pika, Ori, Matic, Duckbill, Amori, Fyxer, Daydream, Elm Biosciences, Folx, Levain, ThredUp.

## Leadership

(Prose — deep-research edge, from `/about` #leadership.) **Emily Heyward** — Co-Founder & CEO, Red Antler. **JB Osborne** — Co-Founder & CEO, Red Antler Group. **Kiser Barnes** — Partner & Chief Creative Officer. **Blake Lyon** — Partner & Chief Business Officer. **Andrea Palacios** — Managing Director. **Erin Collis** — Executive Creative Director. **Liz Rosenbaum** — Executive Strategy Director. **Jason Moran** — Group Creative Director. **Julie Helgesen** — Executive Director of Project & Resource Management.

## Visual & brand impression

Confident, editorial, high-craft — the site reads as its own portfolio piece. Palette is charcoal (#222222) and a warm cream/sage (#E9EBDC) punctuated by a **signature bright red** (#FF0000), including a full-bleed red footer block. Hero leads with a surreal, tactile 3D render (a pink, furry antler/claw) over dark charcoal; sections alternate dark, cream, and pale-lavender grounds with a dense case-study image grid. Typeface is **ABC Favorit** (a contemporary neo-grotesque). Tone is playful and irreverent (copy: "robot butlers (more or less)," "Create Futuremagic\* With Us," "LIVE ANTLERISTS" Instagram feed) but the underlying craft is premium. Motion/interactive flourishes throughout (the `play.` subdomain easter egg).

## Strategic read

The headline is the **Red Antler Group** structure: the agency has expanded from a pure brand-identity shop (the DTC era — Casper, Allbirds, Warby-adjacent darlings) into a three-studio family covering the full funnel — **Red Antler** (brand strategy + identity + advertising), **Fat Earth** ([fat-earth.com](https://www.fat-earth.com/), creative performance marketing & media), and **Wild Fruit** ([wildfruit.co](https://www.wildfruit.co/), presentation/pitch-deck design "driving hundreds of millions in capital and new business"). That lets them hold a client from naming through performance media rather than handing off downstream. Second signal: a deliberate pivot to **AI-company branding** as the next wave of marquee clients, mirroring how they rode the DTC wave a decade ago.

## Provenance

- **Pages:** homepage, /about, /clients, /ai, /careers (5 scrapes + map) — Firecrawl, 2026-06-12. Synthesized across all five + homepage screenshot + branding payload.
- **Verify:** sourceURLs match, all 5 bodies md5-unique, no junk soft-404s. Post-write lint passed.
- **Credits:** 6 (1 map + 1 homepage + 4 key pages). Logos module added 0 credits (measured from the existing homepage payload).
- **Couldn't get:** Pricing (none published — project-based, contact-gated); headcount/revenue/funding (not on marketing site).
- **Run profile:** +logos module (follow-up request) — wordmark extracted from inline data-URI SVG, logomark/og measured from the homepage capture.
