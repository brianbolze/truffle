---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: cfs.energy
name: Commonwealth Fusion Systems
aliases: []
legal_entity: ""
parent: []
owns: []
socials:
  x: http://twitter.com/cfs_energy
  linkedin: https://www.linkedin.com/company/11076301/
  youtube: http://youtube.com/c/CommonwealthFusionSystems
  instagram: https://www.instagram.com/cfs.energy/
external: {}

# Capture meta
captured_at: 2026-06-14
capture_method: firecrawl
site_notes: "Next.js site (`/_next`, Next.js headers) with Prismic image assets and CloudFront in front. Homepage has no JSON-LD; nav dropdown contents are not exposed in the static `<nav>`, so reconstruct deeper IA from homepage links + map. Header wordmark is inline SVG symbol + rendered text, not a single hostable image; committed reconstructed SVG assets under assets/. No declared og:image; favicon fetch failed during logo helper. Commercial proof lives on /company/commercial-partners; first ARC plant model lives on /technology/arc + /chesterfield/info."
key_pages:
  technology: /technology
  hts_magnets: /technology/hts-magnets
  sparc: /technology/sparc
  arc: /technology/arc
  mission: /company/our-mission
  story: /company/story
  commercial_partners: /company/commercial-partners
  chesterfield_info: /chesterfield/info
unverified_fields:
  - "Public pricing/tariffs and full PPA terms for ARC power are not shown; the site only states partner/offtake facts and the intended private-contract model."
  - "Legal suffix, headcount, revenue, and ownership/cap-table details are not on the captured marketing pages; capital raised is self-reported as 'over $2 billion'."
  - "Logo wordmark is reconstructed from the captured inline symbol plus rendered header text because the site exposes no single hostable wordmark image."

# Description — one sentence
description: "Builds commercial fusion energy systems using high-temperature superconducting magnets, moving from the SPARC net-energy demonstration machine toward ARC grid-scale fusion power plants."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2B]
offering_category: [Energy / Utilities, Industrial / Manufacturing]
portfolio_shape: Flagship + companions
business_model:
primary_industry: Energy & Utilities

# Visual identity
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 560, h: 165 }
  logomark: { src: assets/logomark.svg, px: 163, transparent: true }
brand_colors: { primary: "#152536", accent: "#CF6D46", background: "#CCC8C3" }
fonts: [nbInternational, nbInternationalMono, madSans]
color_scheme: light
design_framework: next.js
---

## Overview

Commonwealth Fusion Systems is a commercial fusion energy company spun out of MIT in 2018 to commercialize tokamak-based fusion using high-temperature superconducting magnets. Its path runs from SPARC, a net-energy demonstration machine being built at its 60-acre Devens, Massachusetts campus, to ARC, a grid-scale fusion power plant the company says will deliver about 400 megawatts of clean power. The site self-describes CFS as "the world's largest and leading commercial fusion energy company" and says it has raised "over $2 billion in capital."

## What they offer

No public product pricing or tariff table is shown; the commercial model is partner/offtake driven.

- **ARC fusion power plants / power offtake:** Grid-scale fusion plants designed to provide "about 400 megawatts" of zero-carbon electricity; first plant planned at the Fall Line Fusion Power Station in Chesterfield County, Virginia, with power expected to be sold through private power-purchase agreements `[on-request]`
- **HTS magnets, cable technology, and magnet systems:** High-temperature superconducting magnet technology used in SPARC/ARC and offered through partner arrangements, including Realta Fusion magnet systems and Type One Energy licensing of CFS' HTS cable technology `[on-request]`
- **SPARC demonstration machine:** Commercially relevant net-energy fusion machine intended to prove Q>1 and refine technology for ARC; not a customer-facing product, but the central proof asset for the commercial platform `[on-request]`

## How it works / model

CFS' technical sequence is HTS magnets -> SPARC -> ARC. The company manufactures HTS magnets, builds SPARC to demonstrate net fusion energy, then uses that core technology in ARC plants intended for grid-connected electricity. For the first ARC project, CFS says it will "finance, build, own, and operate" the plant in Chesterfield County; the site says residential and business ratepayers are not expected to pay for the plant because CFS expects ARC power to be sold to large industrial/commercial customers through private power-purchase agreements. A secondary commercial line is partner access to its magnet technology through licensing, design/build partnerships, and integrated magnet-system supply.

## Positioning & audience

CFS targets energy buyers, utilities, industrial/commercial load customers, fusion developers, suppliers, researchers, and policy stakeholders. Its claimed edge is speed to commercial fusion through mature tokamak science, MIT-linked plasma physics, and HTS magnets that make smaller, lower-cost fusion systems possible. The site frames ARC as firm, safe, dispatchable or baseload clean power that can use familiar grid infrastructure and support rising demand from critical infrastructure.

## Nav structure

```
- Technology — /technology
  - SPARC — /technology/sparc
  - ARC — /technology/arc
  - HTS Magnets — /technology/hts-magnets
  - Publications — /technology/publications
- Company — /company/story
  - Our story — /company/story
  - Mission — /company/our-mission
  - Commercial Partners — /company/commercial-partners
  - Open Innovation — /company/open-innovation
  - FAQ — /company/frequently-asked-questions
- News & Media
  - Press Releases — /news-and-media
  - Blog — https://blog.cfs.energy/
  - Journal — /journal
- Locations
  - Devens Campus — /devens-campus/overview
  - Devens site information — /devens-campus/devens-info
  - Chesterfield overview — /chesterfield/overview
  - Chesterfield site information — /chesterfield/info
- Suppliers — /suppliers
- Careers — /careers
```

## Credibility & proof

- **MIT origin:** CFS says it spun out of MIT in 2018 and is collaborating with MIT's Plasma Science and Fusion Center on SPARC.
- **Capital:** The story page says CFS has raised "over $2 billion in capital - more than any other fusion energy company" (self-reported).
- **Magnet milestone:** The HTS page says CFS built a "20 tesla, large-bore magnet" and that its high-field magnets are "the largest of their kind in the world by a factor of 100-1000 in magnet performance" (self-reported).
- **SPARC validation:** The SPARC page points to peer-reviewed Journal of Plasma Physics papers predicting SPARC will achieve net energy and Q>1 "with a considerable margin."
- **ARC plant plan:** The Chesterfield page says CFS will finance, build, own, and operate the first grid-scale ARC plant; it is scheduled for early-2030s grid generation, designed for "20 years or more," and expected to produce enough power for "150,000 homes in the state."
- **Commercial partners:** Google signed a "200 megawatts (MW)" offtake agreement and increased its investment stake; Eni signed an agreement to purchase power from the first ARC plant, described as "worth more than $1 billion"; Dominion Energy Virginia will lease land and provide development/technical expertise; Realta Fusion and Type One Energy are partner channels for CFS' HTS magnet technology.

## Visual & brand impression

High-maturity industrial energy site: a dark translucent nav over full-bleed fusion-hardware photography, then warm gray section bands, precise grids, and dense engineering imagery of magnets, tokamak halls, and plant renders. The palette pairs deep blue-navy (#152536) with a burnt orange accent (#CF6D46) and a muted stone background (#CCC8C3). The logo system is a radial magnetic-field/sunburst symbol plus a narrow technical wordmark; typography mixes nbInternational with monospaced labels, giving the site a serious engineering-lab feel rather than a consumer cleantech pitch. The visual story foregrounds manufacturing scale and scientific credibility more than climate lifestyle imagery.

## Strategic read

CFS' site reads less like a research lab and more like an energy-infrastructure developer moving from proof to project finance: SPARC is the credibility engine, but ARC, PPAs, utility land access, and Google/Eni offtake are the commercial story. The magnet business is strategically important because it creates near-term partner relevance even before owned ARC plants produce power.

## Provenance

- **Pages:** Analyzed 9 captured pages (firecrawl) — homepage, /technology, /technology/hts-magnets, /technology/sparc, /technology/arc, /company/our-mission, /company/story, /company/commercial-partners, /chesterfield/info, plus the map. Homepage `branding`, `rawHtml`, nav, screenshot, signals, and logos were read from the saved payload.
- **Verify:** sourceURL match + md5-unique across all 9 scrapes; no junk soft-404s.
- **Credits:** 10 (1 map + 9 scrapes). Logo helper reused saved homepage payload; no Firecrawl credits.
- **Couldn't get:** Public ARC price/tariff terms, full PPA contract terms, legal suffix, headcount/revenue, cap table/ownership, a hostable wordmark image, favicon bytes, or an og:image.
- **Run profile:** guided — +logos module added after initial standard capture began.
