---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.0"

# Identity
domain: uber.com
name: Uber
aliases: []
parent: []
owns: [ubereats.com, uberfreight.com, uberhealth.com]   # sub-brands on their own domains; not separately captured here

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Homepage is an app-shell (ride-booking widget); positioning lives on /us/en/about/ + /us/en/about/uber-offerings/. Geo-personalized — injects a detected city via ?city= (capture saw 'Wichita'). Map is dominated by /global/<locale>/ and /<cc>/<lang>/ paths — filter to /us/en/. Many products live off uber.com: ubereats.com, uberfreight.com, uberhealth.com, business.uber.com, m.uber.com (rider app), drivers.uber.com, investor.uber.com. Framework via rawHtml = Fusion.js + Base Web (__fusion, data-baseweb); branding.designSystem ignored. CAPTURE QUIRK: back-to-back fc.py scrapes in a shell loop returned HTTP 400 every time; running each scrape as a separate invocation succeeded — serialize one-at-a-time, don't loop."
key_pages:
  about: /us/en/about/
  offerings: /us/en/about/uber-offerings/
  how_it_works: /us/en/about/how-does-uber-work/
  business: /us/en/business/
  uber_one: /us/en/uber-one
  driver_earnings: /us/en/drive/how-much-drivers-make/
  autonomous: /us/en/autonomous/
  founding: /us/en/newsroom/ubers-founding
unverified_fields:
  - "Financials, headcount, revenue, market share — not on the marketing site (public-company deep-research job, not capture)."
  - "Consumer ride/delivery prices are dynamic (surge, per-city, per-trip) and geo-personalized — no fixed price captured. Uber One is the one fixed price ($9.99/month)."
  - "branding.colors.primary reported #1A73E8 (a blue UI/map-chrome artifact); the real brand color is black (#000000), confirmed against the screenshot."

description: "Operates a global technology platform that matches consumers with independent drivers, couriers, and merchants for rides, food and grocery delivery, and freight — plus enterprise travel, advertising, and autonomous-vehicle services."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C, B2B]
offering_category: [Marketplace / Platform]
portfolio_shape: Multi-product
business_model: Marketplace / Commission
primary_industry: Automotive & Mobility

# Visual identity
logo_url: https://www.uber.com/_static/99c4bc580c8b57b7.ico   # branding.images.logo was null → favicon fallback
brand_colors: { primary: "#000000", background: "#FFFFFF" }   # see unverified_fields re: the #1A73E8 misfire
fonts: [UberMove, UberMoveText]              # proprietary typefaces (heading / body)
color_scheme: light
design_framework: fusion.js (Base Web)       # rawHtml: __fusion + data-baseweb; Uber's own React stack
---

## Overview

Uber is a technology company that runs multisided marketplaces matching demand with independent supply: riders with drivers, eaters with restaurants/grocers and couriers, shippers with carriers. Its self-description: *"reimagine the way the world moves for the better."* The platform spans **70+ countries and 15,000+ cities**, with rides at **700+ airports**. What began as on-demand black-car booking (San Francisco launch, 2010) is now a portfolio spanning mobility, delivery, freight, enterprise travel, advertising, and autonomous-vehicle enablement. The consumer-facing `uber.com` homepage is an app shell (a pickup→destination ride widget); the company's self-positioning lives on its About and Offerings pages.

## What they offer

Several distinct, separately-positioned lines (Multi-product). Consumer ride/delivery pricing is dynamic and per-city, so no fixed prices except where noted:

- **Mobility (Rides):** the core marketplace. Tiers include **UberX** ("affordable rides, all to yourself"), **UberX Share** (shared, up to one co-rider), **Uber Comfort** (newer cars, extra legroom), **Uber Black** (premium luxury), **Uber WAV** (wheelchair-accessible), and **Scooters** (micromobility). Reserve (schedule-ahead) and city/airport coverage layer on top.
- **Uber Eats:** on-demand food, grocery, and retail delivery from restaurants and merchants (lives on `ubereats.com`).
- **Earn (the supply side):** **Drive** (rideshare) and **Deliver** (courier) — positioned as flexible independent earning on "the largest network of active riders."
- **Uber One:** consumer membership — **"$9.99/month"** (4-week free trial for eligible first-timers). Benefits: **$0 Delivery Fee** on eligible orders, **6% back on rides** as credits, **up to 10% off** delivery/pickup, automatic surge savings, **10% back on hotel bookings** and car rentals, cancel anytime.
- **Uber for Business:** enterprise dashboard for managing employee travel, meal programs, courtesy rides, and vouchers — "no upfront costs," T&E compliance, CO₂ tracking. Used by **200,000+ companies, including more than half of the Fortune 500**.
- **Uber Freight:** free app matching carriers with shippers, with upfront pricing (lives on `uberfreight.com`).
- **Uber Health:** ride-scheduling for healthcare orgs to get patients/caregivers to care from one dashboard (`uberhealth.com`).
- **Uber Transit:** integrates public-transit options into the app.
- **Uber Advertising:** ad inventory across the app (sponsored listings, journey ads, etc.) — separate success-stories/specs pages.
- **Uber Autonomous Solutions:** a B2B platform giving AV developers mapping, training data, regulatory reach, fleet ops, remote assistance, and demand to commercialize **Level 4** autonomy at scale (mobility, delivery, freight).

Per-SKU depth (every ride tier, ad format) defers to `offerings.md`.

## How it works / model

Two-sided (often multi-sided) marketplace: Uber doesn't own the cars, kitchens, or trucks — it matches independent providers to consumers and **takes a commission** on the facilitated transaction. Demand side requests via app; supply side (drivers/couriers/carriers) accepts. **Driver economics:** drivers see **Upfront Fares** (amount + destination before accepting) in most cities, or per-minute + per-mile base fares elsewhere; earnings stack with surge (shown as purple on an in-app heatmap), **Quest**/**Boost+** promotions, wait-time fees, tolls, cancellation fees, and rider tips. Payout via weekly statements or Instant Pay. Layered on the marketplace core: a **subscription** (Uber One), **advertising** revenue, and **enterprise** (Uber for Business) contracts.

## Positioning & audience

Positions as *the* global movement platform — "the largest mobility platform in the world," "the largest on-demand mobility and delivery platform." Consumer tone (per `branding.personality`) is "modern," aimed at "urban commuters and travelers." Three audiences served simultaneously: **consumers** (riders/eaters — convenience, breadth, safety), **earners** (drivers/couriers — flexible income, control), and **businesses** (enterprises — control, insight, compliance; AV developers — commercialization infrastructure). Differentiators it leans on: global footprint, marketplace/fleet-management expertise, operational data (billions of trips informing mapping/ETAs), and safety ("99.9% of trips completed without any reported safety incident").

## Nav structure

```
- Ride — m.uber.com (rider web app)
- Earn
  - Drive — /us/en/drive/
  - Deliver — /us/en/deliver/
- Business — /us/en/business/
- Uber Eats — ubereats.com
- About
  - About us — /us/en/about/
  - Our offerings — /us/en/about/uber-offerings/
  - How Uber works — /us/en/about/how-does-uber-work/
  - Sustainability — /us/en/about/sustainability/
  - Newsroom — /us/en/newsroom/
  - Investor relations — investor.uber.com
  - Autonomous — /us/en/autonomous/
  - Uber Advertising — /us/en/advertising/
  - Merchants — merchants.ubereats.com
  - Blog — /us/en/blog/
  - Careers — jobs.uber.com
- Help — help.uber.com
- Log in / Sign up — auth.uber.com
```
(Top-level "Explore the Uber platform" CTAs on the homepage: Ride · Earn · Uber Eats · Business.)

## Credibility & proof

- **Scale:** 70+ countries, 15,000+ cities, 700+ airports; 200,000+ business customers incl. >50% of the Fortune 500.
- **Public company:** full Investor Relations site (financials, SEC filings, quarterly earnings), CEO Dara Khosrowshahi letter.
- **Safety:** published U.S. Safety Report; "99.9% of Uber trips are completed without any reported safety incident."
- **Enterprise proof:** "3 out of 4 customers globally would recommend Uber for Business"; named customer testimonial (Parachute Media).
- **Sustainability commitment:** pledge to be a fully electric, zero-emission platform by **2040**.
- **AV partnerships:** autonomous program with named partner activity (e.g., Baidu Apollo Go in the newsroom).

## Visual & brand impression

High design maturity — a confident, minimalist black-and-white system (proprietary **UberMove**/**UberMoveText** type, black primary buttons, 8px radii) punctuated by flat, colorful spot illustrations for each platform module. The homepage leads with a stark "Go anywhere with Uber" headline over a functional ride-booking form, then steps through illustrated cards (Reserve, Drive, Business, app download QR codes) on a clean white canvas closing in a dense black footer. Reads as a mature, utility-first global tech brand: restrained, systematized, and instantly recognizable — not flashy, but polished and engineered.

## Strategic read

The throughline is **asset-light orchestration**: Uber monetizes matching and routing across an ever-widening set of "things that move" (people, food, packages, freight) without owning the underlying assets, then captures additional margin via subscription (Uber One as the cross-sell flywheel between Rides and Eats), advertising, and enterprise. The most forward-leaning bet is **Uber Autonomous Solutions** — rather than build its own self-driving stack, Uber is repositioning as the demand/operations/data layer *for* AV developers, turning the existential threat of autonomy into a platform play (mobility + delivery + freight). The breadth is enumerable but real; the risk is the same as any marketplace conglomerate — supply-side labor/regulatory exposure (driver classification, insurance reform) sits underneath the whole model.

## Provenance

- **Pages:** 8 analyzed via Firecrawl (`maxAge:0`, `location:US`) — homepage, about, offerings, business, uber-one, driver-earnings, autonomous, founding. Map (1 call, 396 URLs, mostly locale/funnel noise) + homepage links drove key-page selection.
- **Verify:** all 8 sourceURLs matched; all body md5s unique (no geo/cache contamination).
- **Credits:** 9 attributed (1 map + 8 scrapes; transient HTTP-400 rejected calls billed nothing). Per `fc.py spend`.
- **Couldn't get:** financials/headcount (deep-research, not on site); dynamic consumer pricing (per-city/surge — not a fixed value); product detail living on off-domain sites (ubereats.com, uberfreight.com, uberhealth.com) was not separately captured.
