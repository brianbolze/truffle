---
schema_version: 1

# Identity
domain: stripe.com
name: Stripe
aliases: []
parent: []
owns: []

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "Next.js (rawHtml __NEXT_DATA__/_next/; branding.designSystem says 'custom' — wrong per §5.4). stripe.com resolves clean (200, no www redirect). Marketing site is stripe.com; docs/dashboard/support live on separate subdomains (docs.stripe.com, dashboard.stripe.com, support.stripe.com) — out of scope for Tier-0. Map returned 498 URLs but is a heavy sample of a vast site (docs, blog, /resources, per-locale /xx-yy/ mirrors, /customers, /jobs) — the footer is the authoritative product/solution taxonomy, far cleaner than the map. Full pricing for every product lives on /pricing as one long page. Homepage is image/animation-dense; product mockups render as repeated UI-copy noise in markdown."
key_pages:
  pricing: /pricing
  payments: /payments
  billing: /billing
  connect: /connect
  enterprise: /enterprise
  agentic_commerce: /use-cases/agentic-commerce
  products_index: /pricing   # the long pricing page doubles as the most complete product roster
unverified_fields:
  - "Headcount, revenue, funding — not on the marketing site (deep-research job). Self-reported scale metrics ($1.9T 2025 volume, 99.999% uptime, 200M+ subscriptions) are marketing claims, captured as quotes, not independently verified."

description: "A financial-infrastructure platform whose APIs let businesses of any size accept payments, run billing and invoicing, move and store money, and embed financial services—spanning startups to global enterprises and platforms."

# Classification
entity_type: Company
target_market: [B2B, B2B2C]   # sells to businesses; B2B2C via Connect (platforms/marketplaces reaching end consumers)
offering_category: [Financial / Fintech Products, Software / SaaS]
portfolio_shape: Catalog
business_model: Usage-based / Consumption   # core = per-transaction/%-of-volume fees; many add-on products are Subscription (see body)
primary_industry: Finance & Fintech

# Visual identity
logo_url: https://images.stripeassets.com/fzn2n1nzq965/1hgcBNd12BfT9VLgbId7By/01d91920114b124fb4cf6d448f9f06eb/favicon.svg  # branding.images.logo was an inline data-URI SVG; favicon fallback
brand_colors: { primary: "#533AFD", dark: "#0D1738", secondary: "#E2E4FF" }  # STRAIN: branding labeled #0D1738 "primary" & #533AFD "accent" — inverted; the blurple #533AFD is the true brand hue (verified in hero gradient + links/CTAs)
fonts: [Sohne]   # branding: Sohne (body) + "SF Pro Display" (heading); Sohne is the signature brand face
color_scheme: light
design_framework: next.js
---

## Overview

Stripe is a financial-infrastructure platform that sells the building blocks of online and in-person money movement as APIs and prebuilt tools. The core is payment processing—accepting cards, wallets, bank debits, BNPL, and stablecoins across 135+ currencies/methods—but it has expanded into a broad suite covering recurring billing, invoicing, tax compliance, fraud prevention, embedded payments for platforms, business banking/treasury, card issuing, identity verification, analytics, and even company incorporation (Atlas). It serves the full size spectrum, from first-transaction startups to "50% of the Fortune 100," and positions itself as the programmable, developer-first layer beneath commerce. Tagline: *"Financial infrastructure to grow your revenue."*

## What they offer

A `Catalog`-shape portfolio—30+ distinct products, grouped (per their pricing IA) into four families:

- **Global payments** — Payments (online/in-person card processing), Checkout, Payment Links, Terminal (in-person/POS), Managed Payments (merchant-of-record), Radar (fraud), Connect (embedded payments for platforms).
- **Money management** — Treasury (banking-as-a-service), Issuing (card issuing), Global Payouts, Financial Connections.
- **Revenue & finance automation** — Billing (subscriptions/usage-based/metered), Invoicing, Tax, Revenue Recognition, Sigma (SQL analytics), Data Pipeline.
- **More** — Identity (KYC), Atlas (incorporation), Climate (carbon removal), Workflows (no-code automation), plus developer surfaces (Elements, Link, SDKs, MCP server).

Most products are independent but designed to compose. Too many to enumerate per-offering here; `/pricing` is the most complete roster. Pricing detail is captured below under *Model* and quoted verbatim from `/pricing`.

## How it works / model

Self-serve onboarding (create an account and integrate via API/SDK, no-code tools, or prebuilt UIs; "first payment in minutes") or a sales-assisted **Custom** package for high-volume/complex businesses. Two headline tiers:

- **Standard** — *"2.9% + 30¢ per successful transaction for domestic cards"*, "No setup fees, monthly fees, or hidden fees." Pay-as-you-go.
- **Custom** — IC+ pricing, volume discounts, multi-product discounts, country-specific rates ("Contact sales").

Revenue model is primarily **usage-based**: per-transaction or %-of-volume fees (e.g. Terminal *2.7% + 5¢*; Managed Payments *+3.5%*; stablecoin *1.5%*; ACH *0.8%, $5 cap*; Connect platform fees from *0.25%*; Issuing *$0.10/virtual card*; Identity *$1.50/verification*). A subset of software products are **subscription**-priced (Billing from *$620/mo, 1-yr*; Tax from *$90/mo*; Revenue Recognition from *$25/mo*; Sigma from *$15/mo*; Data Pipeline from *$65/mo*) and Atlas is a *$500 one-time* fee. So the model is usage-based at its core with a growing subscription-software layer on top.

## Positioning & audience

Targets businesses of every size and developers as the buyer, explicitly segmenting the site by **Enterprises** ("revolutionize their business—from Amazon's…expansion…to BMW's…customer experience"; 50% of Fortune 100), **Startups** ("78% of the Forbes AI 50"; Stripe Atlas + Startups program), and **Platforms/SaaS** (Connect: "world's most successful platforms…including Shopify and DoorDash…go live in weeks instead of quarters"). Cross-cutting solution plays: agentic commerce, crypto, embedded finance, finance automation, global businesses, marketplaces, in-app payments. The claimed edge is breadth + reliability + developer experience: one programmable platform spanning the entire money lifecycle, "engineered for growth." A notable forward bet is **agentic commerce**—an "Agentic Commerce Suite" with Shared Payment Tokens, the Machine Payments Protocol, and agent wallets—pitched as "the economic infrastructure for AI."

## Nav structure

Footer is the authoritative taxonomy (mega-menu is client-rendered; not in markdown):

```
- Products and pricing
  - Pricing — /pricing
  - Payments — /payments        (Checkout — /payments/checkout; Elements — /payments/elements;
                                  Payment links — /payments/payment-links; Payment methods — /payments/payment-methods;
                                  Link — /payments/link)
  - Billing — /billing          (Subscriptions — /billing/subscriptions; Usage-based billing — /billing/usage-based-billing)
  - Connect — /connect
  - Terminal — /terminal
  - Radar — /radar
  - Tax — /tax
  - Invoicing — /invoicing
  - Issuing — /issuing
  - Treasury — /treasury (+ /treasury/platforms)
  - Capital — /capital (+ /capital/platforms)
  - Global Payouts — /payouts
  - Financial Connections — /financial-connections
  - Identity — /identity
  - Sigma — /sigma
  - Data Pipeline — /data-pipeline
  - Revenue Recognition — /revenue-recognition
  - Managed Payments — /managed-payments
  - Atlas — /atlas
  - Climate — /climate
  - Crypto — /use-cases/crypto; Crypto Onramp — /crypto-onramp
  - Authorization Boost — /authorization-boost
- Solutions
  - Enterprises — /enterprise
  - Startups — /startups
  - By use case: Agentic commerce, Crypto, Ecommerce, Embedded finance, Finance automation,
    Global businesses, In-app payments, Marketplaces, Platforms, SaaS, AI companies, Creator economy
    — /use-cases/<slug>
  - By industry: Travel, Insurance, Media & entertainment, Nonprofits, Public sector, Retail
    — /industries/<slug>
- Developers
  - Documentation — docs.stripe.com; API reference — docs.stripe.com/api; API status — status.stripe.com;
    Changelog; Libraries & SDKs; Developer blog — stripe.dev
- Integrations and custom solutions
  - App Marketplace — marketplace.stripe.com; Partner ecosystem — /partners; Professional services — /professional-services
- Resources
  - Product roadmap — /roadmap; Guides — /guides; Customer stories — /customers; Blog — /blog;
    Sessions (annual conference) — /sessions; Privacy & terms; Licenses; Sitemap
- Company
  - Jobs — /jobs; Newsroom — /newsroom; Stripe Press — press.stripe.com; Contact sales — /contact/sales
- Support
  - Get support — support.stripe.com; Managed support plans — /support-plans
```

## Credibility & proof

Heavy enterprise proof: named customers with metrics (Hertz—160 countries/11K+ locations; URBN—$5B consolidated revenue; Amazon, BMW, Maersk, Twilio—10% authorization-rate lift; Instacart, Shopify, DoorDash, Substack, Lightspeed, Mindbody, Jobber). Startup/AI logos (Lovable, Supabase, ElevenLabs, Linear, Decagon, Browserbase). Self-reported scale: *"$1.9T in payments volume processed in 2025,"* *"99.999% historical uptime,"* *"200M+ active subscriptions,"* *"500M+ API requests per day."* Analyst recognition (Forrester—"named a Leader" for Billing; TEI study citing "more than 3x return"). Trust/compliance signaling via Radar, PCI vault, identity/KYC tooling, licenses page. Stripe Press / Works in Progress lend an intellectual brand halo.

## Visual & brand impression

Among the most polished sites in the corpus. The hero is Stripe's signature animated multi-color gradient (purple→orange→blue) against white; the page alternates crisp white sections with a deep-blurple band, all rendered with bespoke, photoreal product-UI mockups (checkout flows, dashboards, Connect ledgers) rather than stock imagery. The brand hue is unmistakably **blurple `#533AFD`** (links, CTAs, gradient core); `#0D1738` dark navy carries text and dark sections. Typography is the custom **Sohne** face. Tone reads as confident, technical, enterprise-credible but design-led—"infrastructure" framed as something beautiful. Very high design maturity.

## Strategic read

Stripe's distinctive move is its sheer surface area: it has expanded from a payments API into a near-complete financial operating system (processing → banking → issuing → tax → analytics → incorporation), letting it land on the per-transaction fee and then expand into subscription-software revenue across the customer's finance stack. The current strategic tell is the prominence of **agentic commerce / AI payments**—Stripe is racing to own the payment primitives for the agent economy (Shared Payment Tokens, Machine Payments Protocol, agent wallets, "economic infrastructure for AI"), positioning a decade of payments-ML as a moat as commerce shifts toward AI intermediaries.

## Provenance

- **Captured** 2026-05-30 via Firecrawl (`fc.py`, `maxAge:0` + `location:US` + `waitFor`), 7 pages, all sourceURL-matched and md5-unique (no §5.1 contamination).
- **Pages analyzed:** homepage (rich pass: markdown/html/rawHtml/links/branding/images/screenshot), `/pricing`, `/payments`, `/billing`, `/connect`, `/enterprise`, `/use-cases/agentic-commerce`.
- **Could not get / out of scope:** per-product deep dives beyond the six captured; docs/dashboard/support subdomains (separate properties); company financials/headcount (not on marketing site). Pricing reflects US/standard rates as displayed on 2026-05-30.
