---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: blueenergy.co
name: Blue Energy
aliases: []
legal_entity: ""
parent: []
owns: []
socials:
  linkedin: https://www.linkedin.com/company/blue-energy-co/
  x: https://x.com/Blue_Energy_Co
external: {}

# Capture meta
captured_at: 2026-06-14
capture_method: firecrawl
site_notes: "WordPress custom theme (/wp-content/themes/blue-energy/) behind Cloudflare/WP Engine. Map is team/news-heavy; homepage links expose the durable nav, and the news index exposes milestone articles. Homepage embeds the wordmark as an inline SVG; logomark and declared og:image fetches failed during the logos module, so only the wordmark slot is recorded. No public PPA/customer pricing."
key_pages:
  homepage: /
  about: /about/
  news: /news/
  ge_vernova: /blue-energy-and-ge-vernova-accelerate-gas-plus-nuclear-approach/
  financing: /april-2026-financing/
  nrc_milestone: /blue-energy-achieves-key-u-s-nrc-licensing-milestone-paving-the-way-for-power-in-48-months-or-less-with-natural-gas-bridge/
unverified_fields:
  - "Customer PPA pricing, contract length, and signed offtaker names — not published on captured pages."
  - "Registered legal entity — not stated in JSON-LD, footer, or captured page copy."

description: "Develops financeable, prefabricated nuclear power plants built in shipyards and fab yards, then finances, owns, and operates them to sell baseload power through long-term PPAs."

# Classification
entity_type: Company
target_market: [B2B]
offering_category: [Energy / Utilities]
portfolio_shape: Single
business_model: Usage-based / Consumption
primary_industry: Energy & Utilities

# Visual identity
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 798, h: 272 }
brand_colors: { primary: "#2424FF", accent: "#222222" }
fonts: [Staff]
color_scheme: light
design_framework: wordpress
---

## Overview

Blue Energy is a nuclear power plant developer/operator focused on making new nuclear financeable by changing construction and delivery, not by selling a proprietary reactor. It says it develops "financeable, turnkey nuclear power plants compatible with leading reactor technology," uses shipyard/fab-yard prefabrication, and plans to finance, build, own, and operate plants. The homepage frames the wedge as the "other 93%" of nuclear plant cost: construction, overhead, and interest during construction, rather than the reactor itself.

Founded in 2023, the company stems from MIT's Nuclear Science & Engineering Department and describes its team as experienced in nuclear construction, licensing, engineering, and development. Its first planned site is in Texas, with a GE Vernova collaboration around GE Vernova Hitachi's BWRX-300 SMR and gas turbines for early site energization.

## What they offer

- **Firm baseload power from prefabricated nuclear plants:** Blue Energy says it "finances, builds, owns, and operates its power plants" and customers purchase "reliable baseload power through long-term, risk-managed power purchase agreements"; PPA economics are not published `[on-request]`.
- **Gas-to-nuclear bridge deployment:** The company says plant/turbine infrastructure can be energized with gas while the nuclear island is licensed and installed, aiming for "48 months or less" time to power; customer pricing is not published `[on-request]`.
- **Turnkey plant delivery model:** The company describes "financeable, turnkey nuclear power plants compatible with leading reactor technology" using offsite prefabrication, fixed-price contracting, and existing fab yards/shipyards; no plant sale price is published `[on-request]`.

Captured cost/timeline claims are comparative proof points, not customer prices: homepage shows Traditional Nuclear at "10+yrs" and "$13K/kW" versus Blue Energy at "3yrs" and "$5K/kW."

## How it works / model

The customer-facing model is energy offtake rather than plant purchase. Blue Energy says customers need "No upfront capital investment," while Blue Energy finances, builds, owns, and operates the plants and sells baseload power through long-term PPAs. Construction is pushed offsite into existing fab yards and shipyards, with fixed-price contracting intended to reduce schedule/cost risk. The gas-to-nuclear bridge resequences the project so non-nuclear, non-safety-significant infrastructure can be built and energized before the nuclear components finish licensing/construction.

The business model is classified as `Usage-based / Consumption` because the site describes customers buying power output through PPAs; the exact commercial structure is unpublished.

## Positioning & audience

Blue Energy targets large-scale electricity customers that need firm, dispatchable power: industry, AI/data centers, advanced manufacturing, and communities facing near-term load growth. Its positioning is financeability: predictable cost, reliable timelines, guaranteed performance, and project-finance compatibility. It competes more against conventional nuclear construction risk and fossil-fuel baseload alternatives than against a single reactor-vendor category.

## Nav structure

```
- Home — /
  - Safe — /#Safe
  - Reliable — /#Reliable
  - Scalable — /#Scalable
- About — /about/
- Careers — /careers/
- News — /news/
  - GE Vernova gas-plus-nuclear collaboration — /blue-energy-and-ge-vernova-accelerate-gas-plus-nuclear-approach/
  - $380M financing — /april-2026-financing/
  - NRC licensing milestone — /blue-energy-achieves-key-u-s-nrc-licensing-milestone-paving-the-way-for-power-in-48-months-or-less-with-natural-gas-bridge/
- Contact — /contact/
- Follow
  - LinkedIn — https://www.linkedin.com/company/blue-energy-co/
  - Twitter/X — https://x.com/Blue_Energy_Co
```

## Credibility & proof

- **Funding claim (self-reported):** "$380 million in financing" announced Apr 21, 2026, led by VXI Capital with Engine Ventures and participation from At One Ventures and Tamarack Global.
- **GE Vernova collaboration (self-reported):** "2.5 GW collaboration" announced May 5, 2026; planned Texas site would use GE Vernova Hitachi's BWRX-300 SMR, with two GE Vernova 7HA.02 gas turbines reserved for site delivery in 2029.
- **NRC milestone (self-reported):** Blue Energy says the NRC approved its licensing topical report, supporting resequencing of plant construction and a "48 months or less" gas-to-nuclear pathway.
- **ADVANCE Act savings claim (self-reported/projected):** Jake Jurewicz says Blue Energy has projected "over $20 million in savings on licensing fees."
- **Team signal:** About page lists board/team members with nuclear, power, finance, Exelon/GE, NRC, MIT, shipyard/manufacturing, and infrastructure backgrounds; CEO/co-founder Jake Jurewicz is described as having MIT nuclear engineering degrees.
- **Homepage partner wall:** The screenshot shows a partner-logo row including MPR, Rizzo, NEI, World Nuclear Association, Energy for Growth Hub, GNA, and Pillsbury.

## Visual & brand impression

Industrial but polished. The site uses a pale gray/off-white background, black typography, and a sharp electric blue (`#2424FF`) as the main accent for highlighted numbers, diagrams, and engineering callouts. The homepage mixes worksite photography with clean 3D plant-section renders and blueprint-style line art, giving it an infrastructure/engineering feel rather than a glossy climate-tech SaaS feel. The typography is compact and technical, with a circular monogram + wordmark that can render black on light or white on dark.

## Strategic read

The captured story is not "new reactor company"; it is "project-finance wrapper around proven reactor technology." Blue Energy foregrounds a construction/finance system: offsite prefabrication, fixed-price contracting, concurrent gas/nuclear staging, and own-operate PPAs. The GE Vernova and NRC announcements reinforce that positioning: the company is trying to turn nuclear into something large power buyers and project financiers can underwrite on timeline, not just technology promise.

## Provenance

- **Pages:** 6 via Firecrawl (`fc.py`, maxAge:0 + location:US + waitFor) — homepage rich pass (markdown/html/rawHtml/links/branding/images/full-page screenshot), /about/, /news/, GE Vernova collaboration, Apr 2026 financing, and NRC milestone. Map returned 85 URLs, dominated by team bios and news; key pages came from homepage/news links.
- **Verify:** all sourceURLs matched; all body md5s unique; no junk soft-404s.
- **Credits:** 7 (1 map, 1 homepage, 5 key pages).
- **Couldn't get:** customer PPA terms/pricing, signed offtaker names, registered legal entity, independent verification of self-reported funding/regulatory/partner claims; logomark and declared og:image failed fetch in the logos module.
- **Run profile:** guided — +logos requested mid-run.
- **Structured layer:** ran `fc.py signals` on the persisted homepage rawHtml. JSON-LD Organization provided name, URL, logo candidate, and X sameAs; LinkedIn came from footer/header links. JSON-LD `logo` was an OG-style 1200x630 share image, so the inline SVG wordmark was extracted instead.
