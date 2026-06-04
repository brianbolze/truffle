---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: stripe.com
name: Stripe
aliases: ["Stripe, LLC", "Stripe, Inc."]   # JSON-LD legalName "Stripe, LLC" (= ©2026 footer); "Stripe, Inc." per the Wikipedia record
parent: []
owns: []
socials: { x: "https://twitter.com/stripe", youtube: "https://youtube.com/@stripe", linkedin: "https://www.linkedin.com/company/stripe/", facebook: "https://www.facebook.com/StripeHQ", github: "https://github.com/stripe", instagram: "https://www.instagram.com/stripehq/" }   # JSON-LD sameAs (operated; took @stripe, not the @StripeDev dev channel)
external: { wikipedia: "https://en.wikipedia.org/wiki/Stripe,_Inc.", crunchbase: "https://www.crunchbase.com/organization/stripe", bloomberg: "https://www.bloomberg.com/profile/company/0170016D:US", wikidata: "https://www.wikidata.org/wiki/Q7624104", yahoo: "https://finance.yahoo.com/quote/STRI.PVT/" }   # JSON-LD sameAs — third-party records

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Next.js (rawHtml __NEXT_DATA__ + /_next/; branding.designSystem 'custom' is wrong, §5.4). stripe.com resolves clean (200, no www redirect). Marketing site is stripe.com; docs/dashboard/support live on separate subdomains (docs./dashboard./support.stripe.com) — out of Tier-0 scope. Map is a heavy SAMPLE of a vast site (jobs/guides/resources/newsroom + per-locale /xx-yy/ mirrors swamp it) — use the homepage links + footer as the authoritative product taxonomy. /pricing is ONE long page carrying verbatim per-product prices for the whole platform — the offerings backbone, and prices sit on-page (cheap to roster). Mega-nav is client-rendered: it's empty in the homepage rawHtml (flyout buttons only), but the /pricing capture DID render the full grouped flyout in markdown — read nav there. Homepage product mockups render as repeated multilingual UI-copy noise in markdown (Pay Roastery / Cartsy bezahlen / €/¥ demo amounts). No physical product to render (software/APIs) — hero-image module N/A; the only brand 'hero' asset is the og gradient cover."
key_pages:
  pricing: /pricing                       # the long pricing page = the most complete priced product roster
  payments: /payments
  billing: /billing
  connect: /connect
  enterprise: /enterprise
  agentic_commerce: /use-cases/agentic-commerce
  annual_letter: /annual-updates/2025
  products_index: /pricing
unverified_fields:
  - "Headcount, revenue, funding, valuation, ownership — not on the marketing site (deep-research job)."
  - "All scale metrics are self-reported marketing claims, captured verbatim, NOT independently verified: $1.9T 2025 payments volume (=1.6% of global GDP), $1.4T 2024 volume, 99.999% historical uptime, 200M+ active subscriptions, 500M+ API requests/day, '50% of Fortune 100', '78% of the Forbes AI 50', '100+ category leaders each process >$1B/yr', Forrester '326% ROI'."

# Description — one sentence (~160-220 chars): [what they do] + [how] + [focus/differentiator].
description: "A financial-infrastructure platform whose APIs and prebuilt tools let businesses of any size accept payments and run billing, money movement, and embedded financial services—from a startup's first transaction to global enterprise scale."

# Classification — closed sets (see TAXONOMIES.md).
entity_type: Company
target_market: [B2B, B2B2C]   # sells to businesses; B2B2C via Connect (platforms/marketplaces reaching end consumers)
offering_category: [Financial / Fintech Products, Software / SaaS]
portfolio_shape: Catalog
business_model: Usage-based / Consumption   # core = per-transaction / %-of-volume fees; a growing subscription-software layer rides on top (see body)
primary_industry: Finance & Fintech

# Visual identity — Firecrawl `branding` is a hint to verify, never source-of-truth.
logo_url: assets/wordmark.svg   # 2.5 canonicalizes to the WORDMARK — the inline brand SVG decoded from branding.images.logo (data-URI), committed as text
logos:
  wordmark: { src: assets/wordmark.svg, w: 60, h: 25 }                                                            # the "Stripe" wordmark, aria-label "Stripe logo", fill #061B31; extracted inline <svg>
  logomark: { src: "https://www.google.com/s2/favicons?domain=stripe.com&sz=256", px: 256, transparent: false }  # white parallelogram slash on a BAKED blurple rounded square (not transparent — colored tile on a dark slide)
  og:       { src: "https://images.stripeassets.com/fzn2n1nzq965/XtX984S1GJVsVOXFC7kMu/01988281e867728dfb09aa7793a6e3b9/Stripe.jpg?q=80", w: 2048, h: 1024 }   # white "stripe" wordmark on the signature gradient cover
brand_colors: { primary: "#533AFD", dark: "#061B31", secondary: "#E2E4FF" }   # STRAIN: branding labeled #061B31 "primary" & #533AFD "accent"/"textPrimary"/"link" — the blurple #533AFD is the true brand hue (verified: hero gradient, links/CTAs, the logomark square); #061B31 is the dark navy ink (also the wordmark fill)
fonts: [Sohne]   # branding: Sohne (body) + "SF Pro Display" (heading); Sohne is the signature brand face
color_scheme: light
design_framework: next.js
---

## Overview

Stripe is a financial-infrastructure platform that sells the building blocks of online and in-person money movement as APIs and prebuilt tools. The core is payment processing—cards, wallets, bank debits, BNPL, and stablecoins across 135+ currencies and payment methods—but it has expanded into a ~35-product suite spanning recurring billing, invoicing, tax compliance, fraud prevention, embedded payments for platforms, business banking/treasury, card issuing, identity verification, SQL analytics, and even company incorporation (Atlas). It serves the full size spectrum, from a first transaction to "your billionth," positioning itself as the programmable, developer-first layer beneath commerce. Founded by brothers **Patrick** and **John Collison** (JSON-LD `founders`). Tagline: *"Financial infrastructure to grow your revenue."*

## What they offer

A `Catalog`-shape portfolio—~35 distinct products, grouped (per the `/pricing` IA) into families. Family-grain here with verbatim headline prices; the complete priced per-SKU roster is in [`offerings.md`](offerings.md).

- **Global payments:** **Payments** (online card/wallet processing) — *"2.9% + 30¢ per successful transaction for domestic cards"* `[published]`; **Checkout / Payment Links / Elements / Link** — *Included with Payments* `[published]`; **Terminal** (in-person/POS) — *"2.7% + 5¢"* + readers *$59 / $299* `[published]`; **Managed Payments** (merchant-of-record) — *"3.5% … in addition to Payments fees"* `[published]`; **Radar** (fraud) — *Included*, *$0.05/txn* on custom `[published]`; **Authorization Boost**, **stablecoin acceptance** — *"1.5%"* `[published]`.
- **Money management:** **Connect** (embedded payments for platforms) — *Included*, *0.25%* starting platform fee `[published]`; **Treasury** (banking-as-a-service) — *Included*, *$2.00 per wire* `[published]`; **Global Payouts** — *$1.50 per payout* + % `[published]`; **Issuing** (card issuing) — *$0.10/virtual, $3.50/physical card* `[published]`; **Capital** (business financing) — no public rate `[on-request]`; **Crypto / Crypto Onramp**.
- **Revenue & finance automation:** **Billing** (subscriptions/usage-based) — *"from $620/mo, 1-yr"* or *0.7% of volume* `[published]`; **Invoicing** — *0.4%/paid invoice* `[published]`; **Tax** — *"from $90/mo"* `[published]`; **Revenue Recognition** — *from $25/mo* `[published]`; **Sigma** (SQL) — *from $15/mo* `[published]`; **Data Pipeline** — *from $65/mo* `[published]`.
- **More:** **Identity** (KYC) — *$1.50/verification* `[published]`; **Financial Connections** — *$1.50/verification* `[published]`; **Atlas** (incorporation) — *$500 one-time* `[published]`; **Climate** (carbon removal) — *3% of order* `[published]`; **Workflows** (no-code automation) — *10,000 steps free, then $0.018/step* `[published]`.
- **Agentic Commerce Suite** (the forward bet): **Shared Payment Tokens** — *$0.15 per SPT issued* `[published]`; **Machine Payments Protocol (MPP)**; **Link agent wallet / Issuing for agents**.

Most products are independent but designed to compose; the **Standard** flat rate is the on-ramp and most add-ons price per-use, with a subscription-software layer on top. `/pricing` is the authoritative roster.

## How it works / model

Two go-to-market motions: self-serve (create an account and integrate via API/SDK, no-code tools, or prebuilt UIs—*"up and running … in as little as 10 minutes"*) or a sales-assisted **Custom** package for high-volume/complex businesses. Two headline pricing tiers:

- **Standard:** *"2.9% + 30¢ per successful transaction for domestic cards"*, *"No setup fees, monthly fees, or hidden fees."* Pay-as-you-go. `[published]`
- **Custom:** *"IC+ pricing, Volume discounts, Multi-product discounts, Country-specific rates"* — *"Contact sales."* `[on-request]`

Revenue is primarily **usage-based**: per-transaction or %-of-volume fees (Terminal *2.7% + 5¢*; Managed Payments *+3.5%*; stablecoins *1.5%*; ACH *0.8%, $5 cap*; Connect platform fees from *0.25%*; Issuing *$0.10/virtual card*; Identity *$1.50/verification*; Climate *3%*). A subset of finance-automation products are **subscription**-priced (Billing from *$620/mo*; Tax from *$90/mo*; Data Pipeline from *$65/mo*; Revenue Recognition from *$25/mo*; Sigma from *$15/mo*), and Atlas is a *$500 one-time* fee. So: usage-based at the core, a growing subscription-software layer on top, with custom IC+ contracts for enterprises.

## Positioning & audience

Sells to businesses of every size, with developers as the buyer, and explicitly segments the site three ways:
- **Enterprises** — *"50% of Fortune 100 companies have used Stripe"*; *"100+ category leaders each process more than $1 billion per year on Stripe"*; named: Amazon (*"5+ … businesses including Prime, Audible, and Amazon Pay"*), BMW, Maersk, Twilio (*"increased authorization rates by 10%"*), Hertz, URBN (*"$5 billion … onto Stripe"*), Instacart, Le Monde, Airbnb, Unilever.
- **Startups** — *"78% of the Forbes AI 50"*; Stripe Atlas + the Startups program; named: Lovable, Supabase, ElevenLabs (*"$3B AI audio leader"*), Linear, Runway, Browserbase, Decagon.
- **Platforms/SaaS** — *"From the Fortune 100 to the Forbes Cloud 100, vertical SaaS platforms use Stripe"* (Connect).

Cross-cutting solution plays: agentic commerce, crypto, embedded finance, finance automation, global businesses, marketplaces, in-app payments, ecommerce. The claimed edge is **breadth + reliability + developer experience**—one programmable platform across the whole money lifecycle, *"engineered for growth."* The marquee forward bet is **agentic commerce**: an *"Agentic Commerce Suite"* with Shared Payment Tokens, the **Machine Payments Protocol**, **Link's agent wallet**, and open standards (Universal Commerce Protocol, x402), pitched as *"building the economic infrastructure for AI."*

## Nav structure

Mega-nav is client-rendered (empty in homepage rawHtml); recovered from the `/pricing` flyout + footer + screenshot:

```
- Products
  - Payments: Payments /payments · Managed Payments /managed-payments · Payment Links /payments/payment-links · Checkout /payments/checkout · Elements /payments/elements · Payment methods /payments/payment-methods · Terminal /terminal · Radar /radar · Authorization Boost /authorization-boost · Link /payments/link
  - Revenue: Billing /billing · Usage-based billing /billing/usage-based-billing · Subscriptions /billing/subscriptions · Invoicing /invoicing · Tax /tax · Revenue Recognition /revenue-recognition · Stripe Sigma /sigma · Data Pipeline /data-pipeline
  - Money Management: Treasury /treasury · Global Payouts /payouts · Capital /capital · Crypto /crypto · Crypto Onramp /crypto-onramp
  - Platforms and marketplaces: Connect /connect · Capital for platforms /capital/platforms · Treasury for platforms /treasury/platforms · Issuing /issuing
  - More: Product roadmap /roadmap · Atlas /atlas · Climate /climate · Identity /identity · Financial Connections /financial-connections
- Solutions
  - By stage: Enterprises /enterprise · Startups /startups
  - By use case: Agentic commerce /use-cases/agentic-commerce · Crypto /use-cases/crypto · Ecommerce /use-cases/ecommerce · Embedded finance /use-cases/embedded-finance · Finance automation /use-cases/finance-automation · Global businesses /use-cases/global-businesses · In-app payments /use-cases/in-app-payments · Marketplaces /use-cases/marketplaces · Platforms /use-cases/platforms · SaaS /use-cases/saas
  - By industry: AI companies /use-cases/ai · Creator economy /use-cases/creator-economy · Hospitality, travel, leisure /industries/travel · Insurance /industries/insurance · Media and entertainment /industries/media-entertainment · Nonprofits /industries/nonprofits · Public sector /industries/public-sector · Retail /industries/retail
- Developers: Documentation (docs.stripe.com) · API reference · Libraries and SDKs · Stripe Apps /apps
- Pricing /pricing
- Guide me /personalize
- Resources: Product roadmap · Guides · Customer stories · Blog · Sessions /sessions · Licenses /spc/licenses
- Company: Jobs · Newsroom · Stripe Press (press.stripe.com)
- Support: Get support (support.stripe.com) · Managed support plans /support-plans
```

## Credibility & proof

Trust signals lean on scale + marquee logos (all self-reported, captured verbatim, **flagged self-reported**):
- **Volume / scale:** *"$1.9T in payments volume processed in 2025"* (annual letter: *"equivalent to 1.6% of global GDP"*); *"$1.4T in 2024"* (enterprise page); *"99.999% historical uptime"*; *"200M+ active subscriptions managed on Stripe Billing"*; *"135+ currencies and payment methods"*; *"500M+ API requests per day"*, *"150K+ transactions per minute"*; BFCM 2025 *"more than $40B … 99.9999% uptime."*
- **Customer proof:** Amazon, BMW, Maersk, Twilio, Hertz, URBN, Instacart, Le Monde, Airbnb, Unilever (enterprise); Lovable, Supabase, ElevenLabs, Linear, Runway, Decagon (startups); testimonials from Mindbody, Jobber, Substack, Lightspeed, BigCommerce.
- **Third-party / compliance:** Forrester Total Economic Impact — *"326% return on investment"* (*"more than 3x"*); *"PCI compliant"*, *"Regulatory licenses globally"* (/spc/licenses); 24×7 support, in-person at global offices (JSON-LD lists ~30 offices incl. SSF, Seattle, NYC, Chicago, London, Dublin, Singapore, Tokyo, São Paulo, Bangalore).

## Visual & brand impression

A reference-grade fintech/developer marketing site. Light theme on white, anchored by Stripe's signature animated **blurple→pink→orange gradient** hero (the same gradient as the `og` cover and the brand's whole motion language), with one deep-navy "infrastructure" band near the footer for the developer story. Dense, high-fidelity product mockups—live-looking checkout flows, dashboards, Connect account tables—do the explaining; the parallelogram "slash" logomark is woven into editorial photography (crosswalks, kiosks, storefronts that *form* the logo). Polished, confident, engineering-led—it sets the bar competitors are measured against.

## Strategic read

The whole portfolio is a **breadth-as-moat** play: start a business on one product (Payments, or Atlas at incorporation) and Stripe is positioned to capture billing, payouts, banking, issuing, tax, and analytics as you grow—each priced per-use so spend scales with the customer. The loudest current bet is **agentic commerce**: Stripe is trying to own the payment rails for AI agents (Shared Payment Tokens, the Machine Payments Protocol, Link's agent wallet, the "Agentic Commerce Protocol") and is explicitly reframing itself as *"the economic infrastructure for AI"*—a land-grab on a payment surface that barely exists yet, leveraging its existing acceptance + fraud network. Worth watching: how much of the catalog any single customer actually adopts vs. uses Payments alone.

## Provenance

- **Pages:** Analyzed 8 captured pages (firecrawl, 2026-06-04) — homepage, /pricing (rich `--homepage` pass), /payments, /billing, /connect, /enterprise, /use-cases/agentic-commerce, /annual-updates/2025 — plus the homepage `branding`/`rawHtml` structured layer (`fc.py signals`), the full-page screenshots, and the homepage link inventory + footer for the product taxonomy.
- **Verify:** `fc.py verify` — all 8 sourceURLs matched; all bodies md5-unique (no §5.1 geo/cache contamination). `/annual-updates/2025` is thin (the letter is a linked PDF, not scraped); `/agentic-commerce` is lean but complete.
- **Credits:** 9 (1 map + 1 homepage + 7 key-page scrapes, all 1cr; `fc.py spend`).
- **Couldn't get:** Headcount / revenue / funding / valuation (not on a marketing site — deep-research). Agentic-commerce stat percentages render blank in markdown (live only in the screenshot). Mega-nav flyout is client-rendered (reconstructed from /pricing + footer + screenshot).
- **Run profile:** guided — forced re-capture over a still-warm (5-day) 2.2 profile, re-stamped to 2.5; `+logos` (wordmark extracted from inline SVG, logomark/og measured); `+offerings.md` (Catalog roster); flagship hero-images requested but **N/A** — a software/API company has no isolated product render (15 candidates were lifestyle photography / demo-merchant goods / UI mockups), so none promoted; the only brand hero asset is the `og` gradient cover.
