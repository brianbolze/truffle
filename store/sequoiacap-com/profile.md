---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: sequoiacap.com
name: Sequoia Capital
aliases: []
legal_entity: "Sequoia Capital Operations LLC"   # STRAIN: site states the firm is NOT a single entity — this LLC operates the website & holds the © ; the funds are separate legal entities
parent: []
owns: []
socials: {}                          # looked (JSON-LD sameAs + footer) — none found; press-shy, no social links on site
external: {}                         # looked — none found

# Capture meta
captured_at: 2026-06-14
capture_method: firecrawl
site_notes: "WordPress multisite (wp-content/uploads/sites/6/). Homepage is an editorial content feed — thin firm positioning; the firm's self-description lives on /our-ethos/ + /our-history/. Nav is flat (no mega-menu flyouts). Arc (/arc/) is a separate Webflow microsite (cdn.prod.website-files.com). /scge/ index returns a junk soft-404 though /scge/people/* subpages exist in the map. No social links in the footer. Wordmark is an inline data-URI SVG in branding.images.logo."
key_pages:
  ethos: /our-ethos/
  history: /our-history/
  founders: /our-founders/
  companies: /our-companies/
  team: /our-team/
  arc: /arc/
  legal: /legal/
  stories: /stories/
  podcasts: /podcasts/
unverified_fields:
  - "AUM, fund sizes, fee structure, returns — not on the marketing site (deep-research, not capture)."
  - "Full portfolio — site states the company list is illustrative and 'does not include a complete list of all Sequoia Capital portfolio companies.'"
  - "SCGE (Sequoia Capital Global Equities) — /scge/ index returns a 404 stub; the SCGE overview could not be captured."

# Description — one sentence
description: "A venture capital firm that backs founders from idea to IPO across seed, early, and growth stages — investing primarily on behalf of nonprofit and school endowments, and framing itself as a long-term partner rather than an investor chasing exits."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Investor / Holding
target_market: [B2B]
offering_category: [Financial / Fintech Products, Services / Consulting]   # STRAIN: "investing" sense of Financial; + Services for the hands-on partnership they emphasize — no dedicated asset-management value
portfolio_shape:                     # empty — Investor/Holding; the "portfolio" is investments, not an offering catalog
business_model:                      # empty — VC economics (mgmt fee + carried interest) fit none of the closed set; site doesn't state it
primary_industry: Finance & Fintech

# Visual identity — branding payload is a hint; confirmed against screenshot + captures
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 180, h: 24 }                                                                # rectangle "Sequoia Capital" wordmark — extracted inline data-URI SVG (near-black #1B1917)
  logomark: { src: "https://www.google.com/s2/favicons?domain=sequoiacap.com&sz=256", px: 192, transparent: false }   # square green LEAF mark — baked white background (no alpha), flag for dark slides
  og:       { src: "https://sequoiacap.com/wp-content/uploads/sites/6/2025/03/Sequoia-OG.jpg", w: 1201, h: 630 }       # declared og:image, verified 1201px actual width
brand_colors: { primary: "#007354", accent: "#B06300" }   # forest-green leaf on cream; amber as secondary accent (bg #FBF7F0)
fonts: [Rosart, Georgia]             # Rosart custom serif (headings), Georgia (body fallback) — serif identity
color_scheme: light
design_framework: wordpress          # rawHtml: 43 wp-content, 5 wp-includes, 5 wp-json (Arc microsite is Webflow, but the main site is WordPress)
---

# Sequoia Capital

## Overview
Sequoia Capital is a venture capital firm founded in 1972 that partners with founders "from idea to IPO and beyond," typically entering early — "sometimes when a company is no more than an idea." It works across seed/early and growth stages, and deliberately positions itself as a *partner* rather than an investor: on its own pages the terms "deal" and "exit" are "forbidden." A distinctive structural fact, stated repeatedly on the site: it invests "primarily on behalf of nonprofits and schools," so portfolio gains flow back to charitable and educational endowments. The site itself reads less like a fund's marketing page and more like an editorial publication — portfolio stories, founder spotlights, podcasts, and perspectives.

## What they offer
The "offering" is capital + hands-on partnership to founders, plus structured access programs. As bold-led lines:

- **Stage coverage:** Seed/Early and Growth investing — the team is organized into **Seed/Early**, **Growth**, and **Operator** role groups (per /our-team/) `[on-request]`
- **Arc:** a "bi-annual open call for outlier early stage founders" — pre-seed and seed; includes **"The Arc Intensive"** ("Four days. Five decades of insights."), run in the Americas and Europe (Spring / Fall cohorts) `[on-request]`
- **Editorial / community:** **Stories**, **Podcasts** (e.g. *Training Data*, *Long Strange Trip*), and perspectives — the firm's brand-building surface, free `[published]`
- **SCGE (Sequoia Capital Global Equities):** a public-equities arm referenced via /scge/people/* subpages — the /scge/ overview page 404'd, so scope unverified `[on-request]`

Pricing is not a concept here (a VC firm doesn't "charge"); offering lines are tagged `[on-request]` to reflect that engagement is by selection/application, not a published price.

## How it works / model
Sequoia raises capital from limited partners — stated to be "primarily nonprofits and schools" (e.g. the Ford Foundation, Boston Children's Hospital) — and invests it in startups across stages, taking equity. It makes money the way venture firms do (management fees + carried interest on fund gains), though the site does not describe its economics. Founders enter the portfolio "in many ways, including Arc, our bi-annual open call." The legal page clarifies the corporate structure: there is **no single "Sequoia Capital" entity** — the website is run by **Sequoia Capital Operations LLC**, which "provides administrative and other services to various Sequoia Capital entities," each with "their own separate legal existence."

## Positioning & audience
Audience is **founders** (the buyer of its capital/partnership) — explicitly "the creative spirits, the underdogs, the resolute… the outsiders, the defiant." Claimed edge is the network: "Our advantage comes from five decades of legendary founders helping each other," and "The right start makes all the difference." It is candid that "our style is not for everyone… We push when we see potential. We are direct. Some don't like our approach." Positions against a transactional VC norm by rejecting "deal"/"exit" language and the "investor" frame.

## Nav structure
Flat primary nav (no flyouts — validated against the homepage screenshot), plus utility/footer links:
```
- Our Founders — /our-founders/
- Our Companies — /our-companies/
- Our Team — /our-team/
- Stories — /stories/
- Podcasts — /podcasts/
- Arc — /arc/
Utility / footer:
- Our Ethos — /our-ethos/
- Our History — /our-history/
- Jobs — /jobs/
- Legal — /legal/
- mySequoia (LP/portfolio login) — /mysequoiacapital/
- SCGE — /scge/ (index 404; /scge/people/* live)
```

## Credibility & proof
- **Tenure:** Founded **1972** by Don Valentine; "For 50+ years, we've backed founders at the earliest stages." First fund of **"$3 million"** backed **Apple and Atari**.
- **Legendary backed companies (verbatim, self-reported):** "Cisco to Google to Instagram to Airbnb and Stripe"; Arc page adds "Apple pre-revenue, Nvidia with just the founding team, Wiz when there wasn't a clear idea."
- **Portfolio breadth (live category counts on /our-companies/):** AI(119), Consumer(87), Fintech(41), Security(35), Hardware(35), Developer Tools(34), Healthcare(34), Operations(32), Data & Analytics(30), GTM(30), Productivity(25), Crypto(22), Infrastructure(22), Marketplace(16), Legal(9), Climate(6), Defense(4). Founder directory facets run larger: Enterprise(291), Consumer(158), AI(140), AI/ML(124), FinTech(96), Healthcare(49).
- **LP base as a trust signal:** "Sequoia invests primarily on behalf of nonprofits and schools" — named: the Ford Foundation, Boston Children's Hospital.
- **Trademark:** "SEQUOIA CAPITAL and the LEAF logo are among our registered trademarks in the United States and/or other countries."
- **Self-reported standing (flagged):** "Sequoia Capital is one of the world's leading venture capital firms" (from the legal fraud-warning) — recorded, not endorsed.
- **Founder testimonials (Arc):** Anish Agarwal (Traversal), Viraj Bindra (Finch).
- **Fraud notice:** an "Online Fraud Warning" disclaiming imposter investment scams; contact secteam@sequoiacap.com.

## Visual & brand impression
Restrained, literary, and confident. A warm cream background (#FBF7F0), serif typography (custom **Rosart** headings), and the dark forest-green **leaf** mark read as old-money permanence over startup flash. The homepage is a full-bleed editorial grid — a video takeover ("Ad Astra, SpaceX"), then a mosaic of photographed founder spotlights, podcast cards, and large pull-quote typography ("now"). There is almost no sales chrome: the design embodies the ethos line "we're skittish about the first person singular, and don't care to see our names in the press." It presents as a publisher of ideas and portfolio stories, not a fund pitching itself.

## Strategic read
The "we invest for nonprofits and schools" framing is doing real strategic work — it reframes Sequoia from financial actor to mission-aligned steward, a recruiting and founder-trust edge competitors can't easily copy. The editorial-site strategy (Stories, Podcasts, perspectives, Arc) is a top-of-funnel brand engine: it makes Sequoia the *destination* for ambitious founders rather than one bidder among many. The deliberately austere corporate surface (no team bios beyond a grid, no AUM, "deal/exit forbidden") is itself positioning — scarcity and selectivity as brand.

## Provenance
- **Pages:** 8 analyzed via Firecrawl (homepage + our-ethos, our-history, our-founders, our-companies, our-team, arc, legal). 9th attempt /scge/ returned a junk soft-404 and was dropped.
- **Verify:** all sourceURLs matched; all body md5s unique; no junk soft-404s among retained pages (scge stub removed pre-write).
- **Credits:** 10 spent this run (1 map + 1 homepage + 8 key pages; scge counted). ~1985 remaining.
- **Couldn't get:** AUM/fund/fee data (not on site); complete portfolio (site states it's illustrative/incomplete); SCGE overview (/scge/ index 404).
- **Run profile:** +logos (multi-ratio brand-mark module captured; wordmark extracted from inline data-URI SVG).
- **Enriched (model knowledge):** sequoiacap.com is the **US/Europe** Sequoia Capital; the 2024 global split spun India/SEA into **Peak XV Partners** and China into **HongShan** — separate firms, not page-attested here. Recorded only to disambiguate which "Sequoia" this profile is.
