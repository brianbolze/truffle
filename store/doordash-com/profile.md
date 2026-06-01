---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.0"

# Identity
domain: doordash.com
name: DoorDash
aliases: []
parent: []
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Next.js consumer SPA, Cloudflare + reCAPTCHA fronted (bare curl 403s — Firecrawl only). Contentful CMS (images.ctfassets.net). The three non-consumer sides live on separate subdomains, all reachable: merchant = get.doordash.com / merchants.doordash.com, business = work.doordash.com, driver = dasher.doordash.com. Homepage + /about render full positioning despite the app-shell hero (address-entry box). Carousels duplicate sections many times in the markdown — dedupe when reading. DashPass landing (/dashpass) is JS-walled/thin; its pricing lives in the /about FAQ instead. Map is ~all noise (help.doordash.com + /store/ + /products/ + /food-delivery city pages) — pull signal pages from homepage links/footer, not the map."
key_pages:
  about: /about
  dashpass: /dashpass
  merchant: https://get.doordash.com/en-us
  merchant_pricing: https://merchants.doordash.com/en-us/pricing
  business: https://work.doordash.com/en-us
  dasher: https://dasher.doordash.com/en-us
unverified_fields:
  - "Fonts — branding payload returned only generic fallbacks (Times New Roman/Arial/Roboto); the real brand typeface was not determinable from the capture."
  - "owns — DoorDash owns brands like Caviar, Wolt, and DashMart, but none was established as a separate store-key domain from the captured pages, so left empty."
  - "Headcount / revenue / funding — not on the marketing site (DoorDash is public, NYSE: DASH); a deep-research job, not capture."

description: "A local-commerce marketplace connecting consumers to restaurants, grocery, convenience, and retail stores, fulfilled by a gig network of independent 'Dasher' drivers and monetized via merchant commissions, DashPass subscriptions, ads, and business accounts."

# Classification
entity_type: Company
target_market: [B2C, B2B, B2B2C]
offering_category: [Marketplace / Platform, Software / SaaS]
portfolio_shape: Multi-product
business_model: Marketplace / Commission
primary_industry: Logistics & Supply Chain   # STRAIN: last-mile delivery network is the operating core; consumer-facing identity is on-demand retail/food e-commerce

# Visual identity
logo_url: https://cdn.doordash.com/static/img/favicon@2x.ico    # branding.images.logo was an inline data-URI wordmark SVG; favicon fallback
brand_colors: { primary: "#EB1700", background: "#FEF1EE" }      # DoorDash red on a warm off-white; verified against homepage screenshot
fonts: []
color_scheme: light
design_framework: next.js     # rawHtml: /_next/ (branding.designSystem said "custom" — the usual miss)
---

## Overview

DoorDash is an on-demand local-commerce platform — a multi-sided marketplace. Consumers order from restaurants and stores through the app or site; independent contractors ("Dashers") pick up and deliver; local merchants get discovered and fulfilled. What began as restaurant food delivery (founded 2013) has expanded into grocery, convenience, retail, alcohol, flowers, pets, and DoorDash's own DashMart stores. It bills itself as the "#1 Food and Drink App in the U.S." The mission, stated verbatim on /about: *"empower and grow local economies by opening the doors that connect us to each other."*

## What they offer

Four customer sides, each its own product surface (`portfolio_shape: Multi-product`):

- **Consumer marketplace:** order delivery/pickup across **Restaurants, Grocery, Convenience, Retail, Alcohol (21+, select markets), Flowers, and Pets**. New users get **"$0 delivery fee on first order"** (other fees apply).
- **DashPass (consumer subscription):** "$0 delivery fees and reduced service fee on eligible orders" + member-exclusive deals + **5% back on eligible pickup orders** + **5–10% off Lyft rides** (up to 4/mo). Price (per /about FAQ): **"$9.99/month (plus tax)"** or **"$96/year ($8/month, plus tax)"** with the Annual Plan; cancel anytime.
- **DashMart:** DoorDash's own first-party convenience/grocery store inside the app — "snacks, household essentials, and more." Plus **Package Pickup** (Dasher picks up prepaid packages, drops at UPS/FedEx/USPS) and **DoubleDash** (add items from a second nearby store, no extra delivery fee).
- **Merchant platform (get./merchants.doordash.com):** **Marketplace** (get listed/discovered), **Commerce Platform** (power your own branded app/website/direct channels — commission-free online ordering), **Reservations**, **Online Ordering**, **POS integrations**, and ads. Three Marketplace pricing plans (see below).
- **DoorDash for Business (work.doordash.com):** workplace meal programs — **Catering, Meal Manager, Group Orders, Vouchers, Gift Cards, DashPass for teams, Meal Budgets**.
- **Dasher platform (dasher.doordash.com):** gig delivery work — pay = **Base Pay + Promotions (Challenges, Peak Pay) + Tips**; cash out instantly with the **DoorDash Crimson Visa Debit Card**; "10% cash back on gas" (through June 30, 2026).

## How it works / model

Consumer places an order → a Dasher picks it up from the restaurant/store → delivers, tracked in real time. DoorDash makes money primarily by taking a **commission from merchants** on each marketplace order, plus consumer **DashPass subscriptions**, **merchant SaaS/ads**, **business accounts**, and consumer fees (delivery + service). Merchant Marketplace commission tiers (verbatim from /about-merchant FAQ):

- **Basic:** "15% delivery commission and 6% pickup commission" — core marketing (listing, search, algorithmic collections), 7-day free trial.
- **Plus:** "25% delivery commission and 6% pickup commission" — adds expanded delivery area + DashPass, 30-day free trial.
- **Premier:** "30% delivery commission and 6% pickup commission" — adds Growth Guarantee, automatic ads, photoshoot reimbursement, 30-day free trial.
- **Tablet (optional):** free during trial, then **"$6 per week in the US"** ($3 Canada, $0 AU/NZ); POS/email/fax order intake is free.

## Positioning & audience

Targets four constituencies simultaneously: **consumers** (convenience — "your go-to life assistant when you need more time in your day"), **merchants** (growth — "Your door to more profitable growth," commission-free direct channels as the upsell), **enterprises** (employee meals), and **Dashers** (flexible gig income — "Work when you want. Earn what you need."). Competes with Uber Eats, Instacart, Grubhub. Claimed edge: largest U.S. selection + delivery network, and a merchant pitch that frames DoorDash as a full commerce/growth stack, not just a delivery channel.

## Nav structure

```
- Consumer (www.doordash.com)
  - Restaurants — /restaurants-near-me
  - Grocery — /p/grocery-delivery
  - Convenience — /p/convenience-stores
  - Retail — /p/retail-stores-near-me
  - Beauty — /p/beauty-supply
  - Alcohol — /p/alcohol-delivery
  - Flowers — /p/flower-delivery
  - Pets — /p/pet-store-near-me
  - DashPass — /dashpass
  - Gift Cards — /gift-cards
  - Promotions — /promos
  - About Us — /about
- Doing Business
  - Become a Dasher — dasher.doordash.com/en-us
  - Become a Merchant — get.doordash.com/en-us · merchants.doordash.com/en-us
  - Get Dashers for Deliveries (Drive) — merchants.doordash.com/en-us/products/drive
  - DoorDash for Business — work.doordash.com/en-us
- Merchant products (merchants.doordash.com)
  - Marketplace — /en-us/products/marketplace
  - Commerce Platform — /en-us/products/commerce-platform
  - Reservations — /en-us/products/reservations
  - Online Ordering — /en-us/products/online-ordering
  - Pricing — /en-us/pricing
- Get to Know Us
  - Careers — careers.doordash.com
  - Investors — ir.doordash.com
  - Company Blog — blog.doordash.com · Engineering Blog — doordash.engineering
  - Newsroom — doordash.news
```

## Credibility & proof

- **Scale claim:** "550,000+ businesses are growing with DoorDash."
- **Merchant value claim:** "Since our founding in 2013, DoorDash has generated over $100 billion in sales for merchants."
- **Category claim:** "the #1 Food and Drink App in the U.S." (Dasher recruiting copy).
- **Merchant logo wall:** Chipotle, The Cheesecake Factory, Nando's, &pizza, Freshii, Hopdoddy, Smokey Bones, BonChon, and others.
- **Merchant testimonial:** Jamie Schrotberger, CEO, Spread Bagelry, on incremental-margin value of DoorDash revenue.
- **Community programs:** $1,000 small-business referral bonus; $10,000 disaster-relief grants for small restaurants.
- **Public company:** NYSE: DASH (investor site at ir.doordash.com).

## Visual & brand impression

Clean, mature consumer-marketplace design on a warm off-white (#FEF1EE) ground with **DoorDash red (#EB1700)** as the single dominant accent on every CTA. Photography-forward — bright, appetizing food and lifestyle shots — interleaved with simple flat illustrations (per-vertical icons). The homepage hero is a utilitarian address-entry box ("$0 delivery fee on first order"), signaling a get-to-the-app storefront rather than a brand-story landing. Light scheme throughout; confident, modern, broadly mainstream rather than premium or edgy.

## Strategic read

The captured site reveals DoorDash repositioning from "restaurant delivery app" to **horizontal local-commerce platform**: the consumer verticals now span grocery → retail → alcohol → pets, and the merchant pitch leads with **Commerce Platform** (help merchants drive *commission-free* direct orders on their own channels) — i.e. selling the underlying logistics/software stack, not just marketplace placement. That's a deliberate margin and lock-in play: own the delivery network (Drive), the merchant's storefront tech, *and* the consumer subscription (DashPass), across more than just food.

## Provenance

- **Pages:** 6 analyzed (Firecrawl, maxAge:0, location:US) — homepage, /about, /dashpass, merchant (get.doordash.com), DoorDash for Business (work.doordash.com), Dasher (dasher.doordash.com). Map captured but ~all noise; key pages pulled from homepage links/footer.
- **Verify:** all 6 sourceURLs matched; all body md5s unique (no §5.1 geo/cache contamination).
- **Credits:** 7 (1 map + 1 homepage + 5 key pages), all basic proxy, 1 cr each.
- **Couldn't get:** real brand typeface (branding gave generic fallbacks); DashPass landing page content (JS-walled — recovered pricing from /about FAQ); corporate financials/headcount (not on marketing surfaces).
