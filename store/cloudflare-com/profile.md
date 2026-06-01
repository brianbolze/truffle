---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: 1

# Identity
domain: cloudflare.com
name: Cloudflare
aliases: ["NET"]                     # NYSE ticker
parent: []
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Map is ~96% developers.cloudflare.com docs noise (480/499 URLs) — useless for positioning; pull the marketing surface from HOMEPAGE LINKS, not the map. Homepage carries the FULL pricing matrix for all 3 axes (Application Services tiers, SASE per-user, Developer Platform usage). Framework is Astro (56 /_astro/ asset refs + data-astro-cid attrs; React islands + Tailwind) — branding.designSystem said 'tailwind' (the CSS layer, ignore per playbook §5.4). Logo is an inline data-URI SVG → favicon fallback. Customer testimonials render as run-together text with no spaces (markdown artifact, not real copy). Hero/build sections are video, captured in 'Low preview' still."
key_pages:
  products: /products/
  plans: /plans/
  about: /about/
  network: /network/
  solutions: /solutions/
  sase: /sase/
unverified_fields:
  - "Headcount / revenue / funding — not on the marketing site. Cloudflare is public (NYSE: NET, IPO 13 Sep 2019); financials are a deep-research / SEC-filing job, not capture."
  - "Subsidiaries / acquisitions (owns) — not surfaced on captured pages; left empty."

description: "A cloud platform running security, performance, and developer compute for roughly 20% of the web across 330+ cities — CDN, DDoS/WAF, Zero Trust/SASE, DNS, and serverless Workers, all on one global network billed as a single platform."

# Classification
entity_type: Company
target_market: [B2B, B2C]
offering_category: [Software / SaaS]
portfolio_shape: Catalog
business_model: Subscription
primary_industry: Technology

# Visual identity
logo_url: https://www.cloudflare.com/favicon.ico   # STRAIN: branding.images.logo is an inline data-URI SVG — favicon fallback per SCHEMA
brand_colors: { primary: "#FF5E1F", accent: "#FF7038", secondary: "#FFCFBC" }   # the iconic Cloudflare orange — visually confirmed as the true brand hue
fonts: [FT Kunst Grotesk]
color_scheme: light
design_framework: Astro
---

## Overview

Cloudflare is a global cloud platform that sits in front of customers' Internet properties to make them faster, safer, and more reliable — and increasingly, a place to *build and run* applications. What began as a service to find the source of email spam grew into a CDN + DDoS/WAF shield, then a "connectivity cloud" of **60+ services** spanning network/CDN, application security, SASE/Zero Trust, and a full-stack developer platform (Workers serverless compute, storage, AI). The throughline is one network: every service runs in every data center across **330+ cities in 120+ countries**, within 50ms of 95% of Internet users. Cloudflare says it powers **~20% of the web** and **42% of the Fortune 500**. It is publicly traded (NYSE: NET).

## What they offer

A `Catalog`-shape platform — 60+ products grouped into eight families on `/products/` (representative items, not exhaustive):

- **Network & CDN:** CDN, DNS, Load Balancing, Argo Smart Routing, Bot Management, Analytics, API Shield, Waiting Room, Spectrum, China Network
- **Security:** WAF, DDoS Protection, Magic Transit, SSL, Turnstile (CAPTCHA replacement), Rate Limiting, Page Shield, Network Firewall
- **SASE / Zero Trust:** Access, Gateway (Secure Web Gateway), Browser Isolation, DLP, Email Security, WAN, Mesh, AI Security for Apps
- **Compute (Developer Platform):** Workers (global serverless), Durable Objects, Containers, Pages, Workflows, Workers for Platforms, Browser Rendering, Sandboxes
- **Storage:** R2 (egress-free object storage), D1 (serverless SQL), KV, Queues, Hyperdrive, Data Platform, Cache Reserve
- **AI:** Workers AI (edge inference), AI Gateway, AI Search, Vectorize (vector DB), Agents
- **Media:** Stream (video), Images, RealtimeKit, TURN/SFU
- **Adjacent:** Registrar (at-cost domains, "Starting at $7.85"), Cloudflare Radar, Speed test

**Pricing — three independent axes**, all visible on `/plans/`:
- **Application Services (per-domain tiers):** **Free $0/mo** · **Pro "$20/mo billed annually, or $25/mo billed monthly"** · **Business "$200/mo billed annually, or $250/mo billed monthly"** · **Contract "Custom"** (enterprise, network priority, 100% uptime SLA)
- **SASE / Zero Trust (per-seat):** **Free** (under 50 users) · **Pay-as-you-go "$7 /user/month"** · **Contract "Custom"**. First 50 users free.
- **Developer Platform (usage-based):** **Workers** free 100k req/day, then **"$0.30 / million requests"** + **"$0.02 / million CPU ms"**; **R2** **"$0.015 / GB-month"**, egress-free; **D1**, **KV**, **Workers AI** **"$0.011 / thousand neurons"**, etc. Headline pitch: *"Pay only when your code runs"* — billed on CPU time, not wall-clock.

Per-SKU depth defers to `offerings.md` (not enabled at v1).

## How it works / model

Self-serve, freemium-led funnel: sign up free with no credit card, add a domain (or deploy a Worker), upgrade by plan tier or scale by usage; enterprises move to custom annual **Contract** plans with an SSO/SLA/support step-up. Three monetization shapes coexist — **subscription** tiers (Application Services), **per-seat subscription** (SASE), and **usage/consumption** metering (Developer Platform) — with a **freemium** free tier feeding all three. Delivery is the network itself: traffic is proxied through the nearest of 330+ data centers, inspected single-pass, and (for Workers) executed at the edge. One dashboard, one bill across networking, security, and compute.

## Positioning & audience

Audience spans the full range — independent/hobby developers (free tier) through the world's largest enterprises and governments. The 2026 framing is **"Everything we learned from powering 20% of the Internet—yours by default"** and **"One platform for your apps, agents, and workforce"** — an explicit pivot toward the **AI/agent era** (Agents, Workers AI, AI Gateway, MCP, "Build for the agent era" page title). Claimed edge vs. hyperscalers (AWS/Azure/GCP): **every service in every data center** (no regions, no backhaul), **single-pass inspection**, **no egress fees** (R2), **predictable usage pricing without surprises**, and **no cold starts / no capacity planning**. Against point security vendors (Zscaler, Akamai), the pitch is one integrated network instead of stitched-together tools. Deep voice/tone work defers to `brand.md`.

## Nav structure

```
- Products — /products/   (mega-menu, 8 groups)
  - Compute — Workers, Durable Objects, Containers, Pages, Workflows, Browser Rendering, Sandboxes, Workers for Platforms, Workers Observability, Email Service
  - Storage — R2, D1, KV, Queues, Hyperdrive, Data Platform, Cache Reserve, Artifacts
  - AI — Agents, Workers AI, AI Gateway, AI Search, Vectorize, Web3
  - Media — Stream, Images, RealtimeKit
  - Security — WAF, DDoS Protection, Magic Transit, SSL, Turnstile, Rate Limiting, Network Firewall, Client-Side Security
  - Network — CDN, DNS, Load Balancing, Argo Smart Routing, Bot Management, API Shield, Spectrum, Analytics, China Network, Waiting Room, …
  - SASE / Zero Trust — Access, Gateway, Browser Isolation, DLP, Email Security, WAN, Mesh, Secure Web Gateway
- Solutions — /solutions/
  - SSE and SASE platform — /sase/
  - Cloudflare AI Cloud — /solutions/ai/
  - Frontend Development Platform — /solutions/frontends/
  - Multi-Tenant Platform Development — /solutions/platforms/
  - Web Security Platform — /solutions/security/
- Resources — /resource-hub/  (Radar, Case studies, Blog, Learning center, Docs)
- Pricing — /plans/
- Under attack? — /under-attack-hotline/
- Login — dash.cloudflare.com/login  ·  Start building — dash.cloudflare.com/sign-up  ·  Contact sales
Footer adds: Company (About, Careers, Investors→cloudflare.net, Press, Global network),
  Public interest (Project Galileo, Athenian Project, Cloudflare for Campaigns, Project Fair Shot, Impact/ESG),
  Compliance (Trust Hub, GDPR, Responsible AI, Transparency report).
```

## Credibility & proof

- **Scale claims:** "powers ~20% of the web" / "1 in 5 sites" · **102 million HTTP requests/second** average · **42% of the Fortune 500** · "thousands of new customers sign up every day"
- **Network proof:** **330+ cities (337 listed), 120+ countries, 8 regions** · **13,000+ network interconnections** · **50ms to 95%** of Internet users (most within 20ms) · GPUs rolling out across the network
- **Named customers (logo wall + quotes):** Shopify, Character.AI, Intercom, DoorDash, Discord, Zendesk, Lovable, npm, L'Oréal, Labcorp, Uber, Wix, Fossil, Canva, U.S. Department of Commerce. Quoted: Duncan Davidson (VP Dev Productivity, Shopify); John Griffin (Co-founder/CTO, Seated)
- **Trust/compliance:** PCI DSS 4.0, 100% uptime SLA (Business+), SSO, Trust Hub, GDPR, Responsible AI, public Transparency report
- **Public company:** NYSE: NET since 13 Sep 2019; investor site cloudflare.net
- **Corporate:** HQ 101 Townsend St, San Francisco; 18 offices worldwide; public-interest programs (Galileo, Athenian, Fair Shot, Campaigns)

## Visual & brand impression

Highly polished, confident, developer-forward. The identity is built almost entirely around **Cloudflare orange** (#FF5E1F → #FF7038 gradients), anchored by the signature sunrise/orange-globe "Region: Earth" motif. Layout is a clean white canvas punctuated by bold full-bleed orange hero and footer CTA bands, with restrained typography (custom **FT Kunst Grotesk**). Notable is the use of animated, slightly playful technical illustrations to dramatize pain ("Fighting infra with 'cloud'" incident cards: egress spikes, DDoS, credential stuffing) and relief ("Shipping with Cloudflare" deploy counters). High design maturity — reads as a top-tier enterprise infrastructure brand that still speaks fluent developer.

## Strategic read

The capture catches Cloudflare mid-pivot from "security/performance proxy" to **"the platform for the agent era."** The homepage leads not with CDN/WAF but with apps + **agents** + workforce, and the AI product family (Agents, Workers AI, AI Gateway, Vectorize, AI Search, MCP portals) is now front-and-center. The durable strategic asset is the **uniform global network** — every service in every PoP, single-pass, no egress fees — which it wields as the differentiator against both hyperscalers (regions, egress, cold starts) and point security vendors (tool sprawl). The three-axis pricing (per-domain subscription, per-seat SASE, usage-based dev compute) is itself the strategy: a freemium top-of-funnel that lets a hobby developer and a Fortune 500 enter the same platform and expand along whichever axis fits.

## Provenance

- **Pages:** 5 analyzed via Firecrawl (`maxAge:0`, US geo, all-formats homepage) — homepage, /about/, /products/, /plans/, /network/. Plus a map (1 call, 499 URLs, ~96% developers.cloudflare.com docs — discarded for positioning). Key-page set drawn from homepage links, not the map.
- **Verify:** all 5 sourceURLs matched; all 5 body md5s unique (no §5.1 geo/cache contamination). All HTTP 200.
- **Credits:** 6 (1 map + 1 homepage + 4 key pages 1cr each). Per `fc.py spend`.
- **Couldn't get:** per-SKU/per-product pages (Catalog shape — captured the catalog map + pricing, not 60 product pages); financials/headcount (public-company / SEC job, not on marketing site); subsidiaries (not surfaced).
