---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: 1

# Identity
domain: clari.com
name: Clari
aliases: [salesloft.com]              # merged with Salesloft (2025) into one combined company branded "Clari + Salesloft" — see Strategic read
parent: []
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "EPiServer/Optimizely CMS (contentassets/ + /Static/ paths, EPiServer markers in rawHtml) — NOT a JS framework. Logo: /Static/img/logo-white.svg (white variant, dark hero). Map is ~80% blog/glossary/author/customer-story noise (495 URLs → ~88 signal); the real product + solution IA comes from homepage links (mega-nav), not the map. Pricing page is sales-gated — no public numbers, only ROI stats + a 'Get a quote' Marketo form. Mega-nav is fully present in homepage markdown. Product subsites on subdomains: app.clari.com (main app), copilot.clari.com, engine.groove.clari.com."
key_pages:
  platform: /products/revenue-orchestration-platform/
  products_overview: /products/product-overview/
  ai_agents: /products/revenue-ai-agents-for-enterprise/
  pricing: /pricing/
  about: /about/
  why_clari: /why-clari/
  salesloft_merge: /press/clari-and-salesloft-announce-agreement-to-merge

unverified_fields:
  - "Pricing — sales-gated (quote-only). No public list price, tier prices, or seat costs; only ROI stats (448% ROI, etc.) and a 'Get a quote' form."
  - "Founding year, headcount, funding, revenue — not on captured marketing pages (deep-research job)."
  - "Whether legacy Clari + Salesloft product lines remain separately branded/SKU'd post-merger — site brands everything as one combined company; product-level integration state not determinable from these pages."

description: "An enterprise AI Revenue Orchestration Platform that unifies sales, RevOps, and post-sales workflows on one time-series 'Revenue Context' data model, using AI agents to forecast, inspect deals, and guide go-to-market execution end-to-end."

# Classification
entity_type: Company
target_market: [B2B]
offering_category: [Software / SaaS]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Technology

# Visual identity
logo_url: https://www.clari.com/Static/img/logo-white.svg
brand_colors: { primary: "#00D7B8", secondary: "#71FFEB", link: "#0280FF" }  # signature mint/teal on near-black; verified against screenshot
fonts: [Faktum Con, Maison Neue]     # Faktum (condensed) headings; Maison Neue / Helvetica Neue body (branding payload)
color_scheme: light                  # page bg #FEFEFE; but the hero + several feature bands are near-black with mint accent (see Visual)
design_framework: episerver          # EPiServer / Optimizely CMS — contentassets/ + /Static/ paths + EPiServer markers in rawHtml (NOT read from branding payload)
---

## Overview

Clari sells an enterprise **AI Revenue Orchestration Platform** — software that ingests every revenue-related signal (CRM, email, calendar, calls, ERP) into a single time-series data model it calls **Revenue Context™** ("who did what, when, with what outcome"), then uses AI and agents to forecast revenue, inspect deal/pipeline health, and guide the next action across the full go-to-market cycle: create → convert → close → retain. It targets large enterprises and serves every revenue-facing role (Sales, RevOps, Marketing, Post-Sales/CS, Finance, Sales Engineering) in one system. As of this capture the site presents Clari as a **combined company with Salesloft** (merger announced Aug 2025, since completed), positioning the joint entity as "the industry's first Predictive Revenue System."

## What they offer

A single platform decomposed into named products + capability layers, all enterprise SaaS (subscription, quote-priced). Core products:

- **Revenue AI Agents:** new class of AI assistants + agents operating on Revenue Context — AI deal inspection (Advanced Opportunity Scores, Smart Topics, Smart Feed, Deal Inspection Agent [Early Access], Trend Analysis Agent [Early Access]) and AI seller productivity (Smart Email Summaries, Smart Follow-Up Emails)
- **Forecast:** forecasting and pipeline management — "complete, tailored view of performance" + inspection analytics
- **Inspect:** opportunity/account management and deal inspection with AI-driven health scores
- **Copilot:** revenue conversation intelligence and call coaching (own subdomain, copilot.clari.com)
- **Groove:** sales engagement and prospecting / top-of-funnel cadences (own subdomain, engine.groove.clari.com)
- **Capture:** activity autocapture + data quality (auto-cleanse email/calendar/calls, match to records)
- **Align:** mutual action plans and buyer collaboration
- **Guide:** "AI Action Hub for Revenue Strategy" — personalized sales action hub

Capability / platform layers (not standalone products): **Revenue Cadences** (workflow/governance engine), **Revenue Database (RevDB)** (the unified data layer + integrations), **Analyze** (analytics/dashboards/reporting), **Integrations**.

Packaged for buyers as four solution bundles: **Pipeline Management & Prospecting**, **Sales Engagement & Productivity**, **Forecasting & Revenue Insights**, **Customer Retention & Growth**.

## How it works / model

- **Data model is the moat:** Capture ingests all human- and machine-generated revenue activity into one time-series model (Revenue Context); products and AI agents read/write against it. "World's largest of its kind," per their copy.
- **Sales-led enterprise GTM:** no self-serve signup or public pricing — every path is "Get a demo" / "Get a quote" via a Marketo form. Land-and-expand across revenue teams.
- **Revenue model:** subscription SaaS (enterprise seats/platform), quote-based. Pricing page touts "no extra platform fees for integrations or continuous support."
- **AI-agent direction:** strategy is explicitly shifting toward agentic execution — "Autonomous Revenue System" / "Predictive Revenue System" framing, with several agents in Early Access / Coming Soon.

## Positioning & audience

- **Who:** global enterprises and their entire revenue org (CRO, CIO, CMO, CCO down to front-line seller). Customers cited: Okta, Adobe, Zoom, Cisco, IBM, 3M, Databricks, UiPath, Fortinet.
- **Category claim:** "The only Revenue Orchestration Platform built for the enterprise" with **Revenue Context™** as the named differentiator; "#1 Revenue Platform for Your Go-To-Market Team."
- **Against:** point tools and CRM (positions one platform vs. "combining three technology solutions"); the post-merger pitch frames it as unifying sales engagement + revenue intelligence + SFA into one system.
- **Tagline / mark:** "Run Revenue®"; "See and Act on Every Revenue Signal."

## Nav structure

```
- Why Clari — /why-clari/
- Products — /products/product-overview/
  - Revenue Orchestration Platform — /products/revenue-orchestration-platform/
  - Revenue AI Agents — /products/revenue-ai-agents-for-enterprise/
  - Capture — /products/capture/
  - Inspect — /products/inspect/
  - Groove — /products/groove/
  - Align — /products/align/
  - Copilot — /products/copilot/
  - Forecast — /products/forecast/
  - Guide — /products/guide/
  - Capabilities:
    - Revenue Cadences — /products/revenue-cadences/
    - Revenue Database (RevDB) — /products/revdb/
    - Analytics — /products/analyze/
    - Integrations — /products/integrations/
- Solutions — /solutions/use-cases/
  - By Use Case:
    - Sales Engagement & Productivity — /solutions/ai-sales-engagement-productivity/
    - Pipeline Management & Prospecting — /solutions/ai-pipeline-management-prospecting/
    - Forecasting & Revenue Insights — /solutions/ai-sales-forecasting-revenue-insights/
    - Customer Retention & Growth — /solutions/ai-customer-retention/
  - By Team:
    - RevOps — /solutions/teams/revenue-operations/
    - Sales — /solutions/teams/sales/
    - Marketing — /solutions/teams/marketing/
    - Post-Sales — /solutions/teams/post-sales/
    - Finance — /solutions/teams/finance/
    - Sales Engineering — /solutions/teams/sales-engineering/
  - By Industry:
    - Technology — /solutions/industries/technology/
    - Healthcare & Life Sciences — /solutions/industries/healthcare-life-sciences/
    - Business Services — /solutions/industries/business-services/
    - Financial Services — /solutions/industries/financial-services/
    - Manufacturing — /solutions/industries/manufacturing/
- Resources — /resources/downloads/ (About Us, Customer Stories, Downloads, Customer Videos, Partnerships, Blog, Careers, Events, Clari Cares, Press)
- Pricing — /pricing/
- Login — app.clari.com / copilot.clari.com / engine.groove.clari.com
```

## Credibility & proof

- **Scale claims:** "Managing $5T in revenue for 1,500+ customers" (Clari standalone); combined Clari + Salesloft cited at "$10 trillion in annual revenue under management" and "over 5,000 organizations."
- **Analyst:** named a **Leader in the inaugural Gartner® Magic Quadrant™ for Revenue Action Orchestration (RAO)** (Salesloft a Visionary in the same report). 2025 G2 Best Sales Software Winner.
- **ROI:** Forrester Total Economic Impact™ study cited at **448% ROI** (pricing page) / **398% ROI** (why-clari) — figures vary by page; supporting stats: +30% first meetings booked, 15% faster deal cycles, 90% less time on forecasting for RevOps, 22% lower onboarding time.
- **Named customers / testimonials:** Okta, Checkout.com, BirchStreet, Fortinet, Dialpad, Amplitude, Sumo Logic, KOFAX, Brooksource — named execs with quotes.
- **Trust:** dedicated /security/ page, GDPR page, MSA/terms.

## Visual & brand impression

Polished, high-budget enterprise B2B identity. The hero and several feature bands are **near-black** with a signature bright **mint/teal (#00D7B8, secondary #71FFEB)** accent and white type; interleaved with clean white sections. Pill-shaped buttons (35px radius), condensed bold display headings (Faktum), confident data-viz product screenshots (bubble charts, forecast/pipeline dashboards) composited with professional photography of revenue leaders. Reads as a mature, category-defining enterprise vendor — premium, data-forward, and AI-forward — not a scrappy startup. The mint-on-black is the memorable, consistent brand signature across the site.

## Strategic read

The defining fact is the **Clari + Salesloft merger** (announced Aug 7, 2025; the /about page now presents one combined company, so it has since closed). The merge announcement framed it as a "merger of equals" forming a Revenue AI powerhouse with **$10T revenue under management** and 5,000+ orgs, betting that the combined revenue dataset ("10B+ revenue actions, 1T+ data signals") is the training moat for agentic AI — the "Autonomous / Predictive Revenue System." Note a **leadership shift**: the Aug 2025 announcement said co-founder **Andy Byrne** (CEO of Clari) would lead the combined company, but the current /about leadership lists **Steve Cox as CEO** — suggesting a post-merger leadership change worth verifying downstream. The whole site has been re-pointed around "Revenue Context™" as the proprietary, defensible substrate beneath the AI-agent push — the strategic answer to commoditized LLMs. `salesloft.com` is recorded as an alias (same combined entity); whether the two product portfolios stay separately branded is not determinable from these pages.

## Provenance

- **Pages:** 8 analyzed via Firecrawl (`maxAge:0` + `location:US` + all-formats homepage) — homepage, platform, products_overview, ai_agents, pricing, about, why_clari, salesloft_merge. Nav reconstructed from homepage mega-nav links (map was ~80% blog/glossary noise).
- **Verify:** all 8 sourceURLs matched; all body md5s unique — no geo/cache contamination.
- **Credits:** 9 (1 map + 8 scrapes), 0 add-ons. ~1558 remaining on the shared key.
- **Couldn't get:** public pricing (sales-gated, quote-only); firmographics (founding/headcount/funding — not on marketing pages); post-merger product-integration state.
