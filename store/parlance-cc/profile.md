---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: parlance.cc
name: Parlance
aliases: ["Parlance | A Creation & Advisory Studio"]
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/scottwitt/
  linkedin: https://www.linkedin.com/in/scottwitt/
external: {}

# Capture meta
captured_at: 2026-06-10
capture_method: firecrawl
site_notes: "Framer site (all assets on framerusercontent.com; no JSON-LD on homepage). Engagement models + the only published pricing live on the /news/* article pages (faq, cc=Creative Capital, fte, sprints) and /scottwitt, not the homepage. Booking via Calendly; Office-Hours payment via Stripe. Map paths are mixed-case (/Projects/<x> vs /projects/casestudies) — copy the captured casing, don't normalize. Display headlines deliberately run words together (no spaces) as a type device — markdown shows them glued."
key_pages:
  about: /scottwitt
  faq: /news/faq
  creative_capital: /news/cc
  fte: /news/fte
  sprints: /news/sprints
  work: /projects/casestudies
  news: /news
unverified_fields:
  - "Fractional-retainer and advisory dollar figures — charged value-based / equity (FAST protocol), no rate published."

# Description — one sentence.
description: "A solo-operator venture-creation and advisory studio whose founder embeds as a fractional brand, creative, and marketing executive — naming, positioning, narrative — for founders and investors building iconic companies."

# Classification — closed sets (see TAXONOMIES.md).
entity_type: Company
target_market: [B2B]
offering_category: [Services / Consulting]
portfolio_shape: Flagship + companions
business_model: Services / Project-based
primary_industry: Consulting & Professional Services

# Visual identity — Firecrawl `branding` is a hint to verify, never source-of-truth.
logo_url: "https://framerusercontent.com/images/iJK4Yp8FC78lyxV8NJzYe85assk.png"
logos:
  wordmark: { src: "https://framerusercontent.com/images/iJK4Yp8FC78lyxV8NJzYe85assk.png", w: 811, h: 130 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=parlance.cc&sz=256", px: 256, transparent: true }
  og:       { src: "https://framerusercontent.com/assets/lnfCZyzXEI4RbIaruATJsNCorA.png", w: 1200, h: 630 }
brand_colors: { primary: "#000000", accent: "#047A8C" }   # STRAIN: brand reads monochrome black-on-off-white (#F3F3F3); accent = teal CTA. branding's "primary #0000EE" is a default-link artifact, discarded.
fonts: [Switzer]
color_scheme: light
design_framework: framer
---

## Overview

Parlance is the one-person studio of **Scott Witt**, founded **2023** — described on its own pages as "part brand studio, part consultancy with a dash of venture studio." Rather than invest financial capital, it deploys what it calls **"Creative Capital"**: embedding as a fractional brand, marketing, and creative operator to "turn conviction into clarity" for founders and investors. The work is the "messy, critical" brand jobs — naming a venture, repositioning a product, distilling a narrative, building investor stories — done "at all altitudes, with no ego," from IC trenches to the boardroom. Positioned around a single thesis: *"It's never been easier to start a company. And it's never been harder to explain one."*

## What they offer

A flagship fractional-operator practice with several companion engagement models (bold-led, pricing verbatim + visibility token):

- **Fractional embed (FTE — "Fractional Tactical Executive"):** acts as interim CMO / Head of Brand / Head of Creative; **value-based retainer, 3-month minimum, up to 4 days/week** `[on-request]`
- **Advisory:** **equity-based, guided via the FAST protocol** `[on-request]`
- **Sprints:** flat, value-based engagements — **"Starting at just $15k"** `[published]`. Named types: **Naming Sprint** (company / product / system / process), **Story Sprint**, **MVVs Sprint** (mission-vision-values), **Verbal Design Sprint** (brand voice, narrative tune-ups, TOV guides), **Brand Spruce-Up Sprint** (strategy / naming / story / verbal / MVV / visual refresh)
- **Office Hours:** **$225 / 30 mins** — pitch-deck review, creative feedback, presentation prep, consultative POV (paid via Stripe) `[published]`
- **Mentorship:** **"First Session is Free for Anyone"** (45-min session) — transitions, professional story, CV feedback `[published]`
- **Venture incubation / co-founder support:** named as one of the three concurrent slots `[on-request]`

Three self-described service buckets frame the work: **Extend your leadership capacity** (advisory, exec thought-partnership, new-venture incubation), **Clarify & re-position your brand** (naming, positioning, voice/messaging systems, investor narratives, brand architecture), and **Build a world around your story** (full-stack creative direction — narrative/visual/content, film/photography, AI-native production, identity systems).

## How it works / model

"Clarity begins with a Conversation" — intake via a Calendly booking, then an engagement under one of the models above. Compensation is **value-based / equity, not rate-card**: advisory in equity (FAST protocol), Sprints at flat value-based fees, fractional embeds on retainers. **Equity can substitute for up to 50% of a fee**, with "a value multiplier to the equity's current valuation" to share risk. Operationally it's **a one-person boutique (+ an EA)** plus "a trusted network of specialists when additional expertise is needed." Capacity is deliberately capped at **typically three concurrent engagements**: one fractional embed (≤50% of time), one advisory role, and one venture incubation / co-founder support.

## Positioning & audience

- **Who it sells to:** founders, operators, and investors — explicitly **VC firms and their portfolio companies** (embedding / targeted projects / founder mentorship) and **PE firms** (brand value in due diligence, distressed-asset revitalization, turnarounds, post-acquisition integration).
- **Focus categories (verbatim):** Responsible AI · HealthTech · Public Impact ("PACs… to advance moderate center-left policies") · Consumer Lifestyle · Future of Food · Future of Work · Future of Media. The FAQ restates these as Health & Wellness, Consumer Lifestyle, Sustainable Consumption, Public Impact, Future of Food/Work/Media.
- **Claimed edge:** *"Provocation and simplification"* — simplifying the complex in "regulated industries, sensitive cultural arenas, or moments of transformation." Tagline: **"Creating breakthroughs is what you do. Helping people understand them is what I do."** Differentiator vs. a classic consultancy: *"we don't write jargon-laced decks; we implement solutions alongside you"* (operators, not advisors).

## Nav structure

```
- Work — /projects/casestudies
  - The Marque Longevity Lab — /Projects/the-marque-longevity-lab
  - Naming — /Projects/naming
  - Aescape — /Projects/aescape
  - WelcomePAC — /Projects/welcomepac
  - Fisher Wallace Labs (fwl) — /Projects/fwl
  - Constellation — /Projects/constellation
  - Cars & Bids — /Projects/cars-bids
  - Uptrade — /Projects/uptrade
  - Reporter — /Projects/reporter
- Info — /news
  - CC (Creative Capital) — /news/cc
  - Sprints — /news/sprints
  - FTE — /news/fte
  - Mentorship — /news/mentorship
  - The Genagraph — /news/genagraph
  - FAQ — /news/faq
  - AI You Can Feel (TIME 2024) — /news/time2024
- Contact — /scottwitt
  - Book Time (Calendly) — https://calendly.com/scott-parlance/30min
```

## Credibility & proof

All self-reported (founder bio + client roster on owned pages):

- **Founder pedigree (verbatim):** "former Apple Creative Director," "Chief Brand & Creative Officer at venture-backed startups," "Cannes Titanium Lion and D&AD Black Pencil winner," "For over two decades, Scott has built brands, teams, products, and market value."
- **Mentorship volume (verbatim):** "Since 2023, I've delivered over 350 hours of free Mentorship."
- **Organizations Supported (verbatim list):** Constellation · Aescape · Harlowe · Eidra · Fisher Wallace Labs · Welcome PAC · Reporter · Uptrade · AXS TV · Pedal · TCG · Since Tomorrow.
- **Featured engagements (verbatim role tags):** The Marque Longevity Lab (Re-Branding / New Category Creation) · Aescape (HealthTech, Fractional CBO) · WelcomePAC (Public Impact, Fractional CBO) · Fisher Wallace Labs (HealthTech, Advisor) · "AI You Can Feel" — credits leading brand/narrative/creative for "the world's most advanced massage" (Aescape, TIME 2024).

## Visual & brand impression

Minimal, editorial, and confidently monochrome: an off-white **#F3F3F3** ground, black **Switzer** headlines and wordmark, with pill-shaped **teal (#047A8C) / dark-green (#023F33)** CTA buttons the only saturated color. The signature type device is display headlines with the **spaces removed** ("It'sneverbeeneasiertostartacompany") — words run together as a deliberate motif. The hero is a macro photograph of **tangled threads resolving into ordered knit** — a literal "untangle the complexity → clarity" metaphor that mirrors the Creative Capital thesis. The logomark is an abstract **single-continuous-line figure** (reads as a stylized person/needle) inside a thin circle. Footer carries dual locale clocks (**Menlo Park / Stockholm**) and "Made in California," signaling a US–Sweden axis. High design maturity; restrained, founder-as-craftsman tone.

## Strategic read

A **personal-brand consultancy productized as a studio** — the entity (Parlance) is kept distinct from the person (Scott Witt, the Contact page), but it is one operator. The core conceit is the triple meaning of **"CC"**: the domain (`parlance.cc`), **"Creative Capital,"** and (per the FAQ) **"Consultative Capital"** — and the explicit non-offer is financial investment: *"Do you invest financial capital in startups? We don't."* Instead it invests operator labor, optionally converting up to half a fee into equity. The deliberate **~3-engagement cap** makes scarcity part of the positioning. Demand-side tilt is heavily **early-stage founder/investor brand work in complex or regulated categories** (healthtech, responsible AI, food, media, center-left public impact). *(Project context: Scott Witt is also the brief consumer for this web-research engine — see memory.)*

## Provenance

- **Pages:** homepage + 5 key pages (`/scottwitt`, `/news/faq`, `/news/cc`, `/news/fte`, `/news/sprints`) via Firecrawl; homepage full-page screenshot, `branding` payload, and logo candidates (wordmark / s2 logomark / og) read for visual identity.
- **Verify:** all sourceURLs matched, all bodies md5-unique, no junk soft-404s; post-write lint clean.
- **Credits:** 7 (1 map + 6 scrapes); logos module added no credits (cached homepage payload + headed icon fetches).
- **Couldn't get:** per-project case-study detail (individual `/Projects/*` pages not captured — breadth taken from the homepage roster + nav); dollar figures for fractional/advisory retainers (value-based / equity, not published).
- **Run profile:** express — +logos module (wordmark/logomark/og measured and written).
