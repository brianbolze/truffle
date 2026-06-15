---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: spero.vc
name: Spero Ventures
aliases: []
legal_entity: ""                     # site states "Spero Fund II, LP" (the fund vehicle), not a GP/management legal name; no JSON-LD legalName
parent: []
owns: []
socials:
  x: https://x.com/SperoVentures
  linkedin: https://www.linkedin.com/company/speroventures/
external: {}

# Capture meta
captured_at: 2026-06-14
capture_method: firecrawl
site_notes: "WordPress (wp-content/wp-json/wp-includes in rawHtml); Cloudflare-fronted. branding payload is wrong twice — framework 'tailwind' (it's WordPress) and colorScheme 'light' (site is predominantly dark-green #00460E canvas). Portfolio depth lives on /portfolio/ (active cards w/ stage+date+founder); full all-time roster on /full-portfolio. /insights posts proxy off-site writing (Medium/Substack) — the Fund II announcement body came back as Medium chrome wrapping Spero's own text. Favicon is a cyan-background sunburst (not transparent). No og:image declared. Wordmark is an inline data-URI SVG (88x36)."
key_pages:
  about: /about
  team: /team
  portfolio: /portfolio
  full_portfolio: /full-portfolio
  insights: /insights
unverified_fields:
  - "Fund I size / total AUM — only Fund II ($125M, 2024-vintage) is stated on-site."
  - "business_model — VC economics (mgmt fees + carry) aren't in the closed set and aren't stated on the site."
  - "Founding date / firm history — not on the captured pages (deep-research, not capture)."

# Description — one sentence (~160-220 chars)
description: "A boutique early-stage venture firm that leads and co-leads seed-to-Series-A rounds in purpose-led founders, backing companies building a healthier, more sustainable, and more fulfilling future."

# Classification — closed sets (see TAXONOMIES.md). Leave empty if the site doesn't determine it.
entity_type: Investor / Holding
target_market: [B2B]                 # portfolio companies + institutional/HNW LPs
offering_category: []                # STRAIN: a capital-allocating VC firm has no sellable product/service in the taxonomy; entity_type carries it. Left empty per the Investor/Holding gating rule.
portfolio_shape:                     # empty — Investor/Holding; its "portfolio" is investments, not offerings (TAXONOMIES rule)
business_model:                      # empty — VC economics (mgmt fees + carry) aren't in the closed set and aren't stated on the site
primary_industry: Finance & Fintech

# Visual identity — Firecrawl `branding` is a hint to verify, never source-of-truth.
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 88, h: 36 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=spero.vc&sz=256", px: 32, transparent: false }
brand_colors: { primary: "#00460E", accent: "#A5E8F7" }   # dark green canvas (also text/link) + light-cyan accent — confirmed against screenshot
fonts: [Helvetica Neue]              # branding resolved only the system fallback stack; large editorial display type drives headings (see Visual)
color_scheme: dark                   # branding said "light"; the site's dominant canvas (header, hero, body bands, footer) is dark green with light text
design_framework: wordpress          # read from rawHtml (wp-content x41, wp-json, wp-includes), not the branding payload ("tailwind")
---

## Overview

Spero Ventures is a boutique, early-stage venture capital firm investing in "purpose-led" / "mission-driven" founders. Its thesis: "tomorrow's most valuable companies will be the ones tackling today's most meaningful challenges." It backs companies "innovating at the edge of new industries and technologies to create a healthy, sustainable, and fulfilling future for everyone," organized around three investment areas — a **healthy future** (health information + access to care), a **sustainable future** (upgrading water, food, energy, transportation, manufacturing, and waste systems), and a **fulfilling future** (technology for learning, creating, and human agency). The firm runs a deliberately concentrated portfolio and positions on hands-on partnership: "we are here for transformations, not transactions."

## What they offer

What Spero offers founders is capital plus operating support; its terms are published openly:

- **Stage & position:** leads and co-leads — "We lead and co-lead seed and Series A rounds of $3-$10M" / "typically late Seed to early Series A … all of them from a lead or co-lead position."
- **Check size:** "a typical initial check size of $2-$4M and more in reserve for future raises" (fund_ii: "We write $2–4M initial checks into round sizes that range from $3–10M").
- **Fund:** **"Spero Fund II, LP: a $125M Fund"** — described as "a 2024-vintage fund" (announced Nov 2025).
- **Portfolio approach:** "Our concentrated portfolio approach allows us to engage deeply with our founders."
- **Founder support:** "operational and strategic guidance from people who believe in your purpose" — "on-call guidance when you're in the weeds, strategic perspective when you need to see the horizon."

Three investment themes (verbatim section heads on /about):
- **Healthy future:** "empower people with information and cutting-edge care to live healthier, longer lives."
- **Sustainable future:** "teams upgrading and reimagining these systems [water, food, energy, transportation, manufacturing, waste] to benefit people and the planet."
- **Fulfilling future:** "a smarter, self-directed future where everyone has the opportunity to create the life they want at home and at work."

## How it works / model

Lead/co-lead seed–Series A investor writing $2–4M initial checks into $3–10M rounds, reserving for follow-on. Concentrated portfolio → deep, hands-on engagement with each founder. Capital is deployed from **Spero Fund II, LP ($125M)**. The team frames its edge as operator experience — "As entrepreneurs and operators, we've built and scaled companies like Tesla, Stripe, and eBay. As investors, we've gone all in early on Carta, Tumblr, and Turo." (VC revenue economics — management fees + carry — are not stated on the site.)

## Team

A small partnership of investors and operators (from /team):

- **Shripriya Mahesh:** General Partner — frames herself as having built the firm ("We built Spero Ventures around a single idea: everyone deserves the opportunity to live a good life"); on /about tied to eBay (former VP Global Product / current board).
- **Andrew Parker:** General Partner — "drawn to entrepreneurs who are makers"; on /about tied to Carta (former board member).
- **Sara Eshelman:** General Partner — "starting with problems first and seeking out incredible founders working on them."
- **Marc Tarpenning:** Venture Partner — Tesla co-founder (on /about tied to Tesla's sustainable-energy mission).
- **Stephen Wemple:** Principal.
- **Nolan Shah:** Associate.

## Portfolio

A concentrated, sector-spanning book aligned to the three themes. The /portfolio page details **28 active holdings** (each with stage + date + founder), and **/full-portfolio lists ~52 companies** all-time (including exits/older names like Anchor, Skillshare, MetaMap, Gencove). Recent activity skews late-Seed / Series A (2024–2026). Representative holdings by theme:

- **Sustainable / climate & energy:** Euclid Power (renewable-energy OS), Wattch (grid monitoring/control), Singularity (grid carbon data), Sora Fuel (e-fuel from electricity + water, Seed Mar 2026), Mast Reforestation, Leaf, Tortuga AgTech.
- **Healthy:** Tiny Health (family gut health), Oova, Huckleberry Labs (family sleep), Juno (child disability insurance), Aralez Bio (noncanonical amino acids for therapeutics), Persist AI (drug-formulation discovery), Canopy (hospital-safety location intelligence).
- **Fulfilling / software & AI:** Hyro (healthcare conversational AI), Allie Systems (factory AI co-pilots), Pickaxe (no-code AI-tool builder), Remark (AI shopping personas), Corvus Robotics (autonomous inventory drones), Roam Robotics, Telo Trucks (urban EV pickup), TalkShopLive (live-video marketplace), Empowerly, Fiveable, Skillshare.

Full roster greppable in `captures/2026-06-14/full_portfolio.md`.

## Nav structure

```
- Portfolio — /portfolio/   (full list: /full-portfolio)
- About — /about/
- Team — /team/
- Insights — /insights/
  - Writing — /category/writing/
  - Speaking — /category/speaking/
  - Podcasts — /category/podcasts/
```
Flat top nav (no mega-menu), confirmed against the homepage screenshot.

## Credibility & proof

Self-reported, flagged as such:
- **Operator pedigree:** "we've built and scaled companies like Tesla, Stripe, and eBay" (Marc Tarpenning is a Tesla co-founder).
- **Prior investing track record:** "we've gone all in early on Carta, Tumblr, and Turo."
- **Fund scale:** "Spero Fund II, LP: a $125M Fund" (2024-vintage).
- **Portfolio as proof:** ~52 named companies with live website links; many show a "Why we Invested" post.

## Visual & brand impression

Sophisticated, editorial, mission-forward. The dominant canvas is a deep forest green (`#00460E`) — header, hero, body bands, and footer — with light text and a light-cyan (`#A5E8F7`) accent that carries the lowercase "spero" wordmark and a recurring animated sunburst motif. The hero pairs large display type ("Turn Purpose Into Progress") over industrial/founder photography (warehouse robotics, founder retreats), and a mid-page logo wall foregrounds the portfolio. Restrained palette, generous whitespace, and confident typography read as a serious, design-literate firm rather than a flashy one. (The branding payload resolved only a Helvetica Neue system fallback stack; the large editorial headings appear to use a custom display face it didn't catch.)

## Strategic read

A small, thesis-driven generalist VC unified by a "purpose" lens rather than a single vertical — the three futures (healthy / sustainable / fulfilling) let it range across climate, health, robotics/hardware, and applied AI while keeping a coherent story. Differentiation rests on operator credibility (Tesla/Stripe/eBay alumni) and a concentrated, high-touch model, not on capital scale ($125M Fund II is deliberately boutique). The "late Seed to early Series A, lead/co-lead, $2–4M check" lane is stated plainly, which makes the firm easy for founders to self-qualify against.

## Provenance

- **Pages:** homepage, /about, /team, /portfolio, /full-portfolio, /2025/11/spero-ventures-fund-ii (6 pages) — Firecrawl scrape (markdown + links + screenshot; homepage all-formats incl. rawHtml/branding).
- **Verify:** all sourceURLs matched, all 6 bodies md5-unique, no junk soft-404s.
- **Credits:** 7 (1 map + 1 homepage + 5 key pages).
- **Couldn't get:** Fund I size / total AUM; firm founding date & origin history; VC fee/carry economics — none on the captured marketing pages.
- **Run profile:** express — emphasis "including logos"; +logos module.
