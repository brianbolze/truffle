---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: airtable.com
name: Airtable
legal_entity: "Formagrid Inc, dba Airtable"
aliases: []
parent: []
owns: []
socials: { facebook: "https://facebook.com/airtableapp", linkedin: "https://linkedin.com/company/airtable", x: "https://twitter.com/airtable", instagram: "https://instagram.com/airtable", youtube: "https://www.youtube.com/c/AirtableApp" }
external: {}

# Capture meta
captured_at: 2026-06-17
capture_method: firecrawl
site_notes: "Next.js/Vercel marketing site (/_next/ assets, Vercel headers; no JSON-LD on homepage). Map is noisy with developer/API docs and share/app URLs; choose structural pages from homepage nav. Pricing is markdown-clean on /pricing (plans, AI-credit packs, Portals add-on, API limits). Header exposes a logomark only; official wordmark/logomark assets live behind the linked trademark-guidelines Airtable share captured as logo_lockups. Homepage sets a marketing segment cookie; treat hero AI positioning/IA as a dated snapshot."
key_pages:
  homepage: /
  platform: /platform
  pricing: /pricing
  integrations: /integrations
  marketplace: /marketplace
  ai: /platform/ai
  api: /developers/web/api/introduction
  about: /about
  trust_security: /company/trust-and-security
  trademark_guidelines: /company/trademark-guidelines
  logo_lockups: /appiyS5IzOTBBj0el/shrxP0DqMdbLVY7fd/tblcRB6iqKxlYNrlV
  status: https://status.airtable.com/
modules:
  offerings: offerings.md
  productivity_saas: productivity_saas.md
  visual: visual.md
unverified_fields:
  - "Homepage AI positioning / IA are a point-in-time snapshot, not fixed — captured under the marketing-new-site-segment=control response and likely to rotate with Airtable's AI-rebrand messaging."
  - "Revenue, ARR, current valuation, and ownership/cap table are not site-derived beyond Airtable's self-reported funding/valuation statements on /about."

# Description
description: "A no-code database and app-building platform for teams and enterprises, turning shared operational data into custom apps, interfaces, automations, AI agents, and cross-tool workflows."

# Classification
entity_type: Company
target_market: [B2B]
offering_category: [Software / SaaS]
portfolio_shape: Flagship + companions
business_model: Subscription
primary_industry: Technology

# Visual identity
logo_url: assets/wordmark.png
logos:
  wordmark: { src: assets/wordmark.png, w: 1350, h: 294 }
  logomark: { src: assets/logomark.png, px: 165, transparent: true }
  og:       { src: assets/og.jpg, w: 1200, h: 630 }
brand_colors: { primary: "#181D26", accent: "#FCB400", secondary: "#F82B60", tertiary: "#18BFFF", background: "#FFFFFF" }
fonts: [Haas]
color_scheme: light
design_framework: next.js
---

## Overview

Airtable is a B2B no-code app platform: teams build applications, interfaces, automations, and reporting layers on top of shared relational data. The current site leads with AI - the homepage promises "AI-powered workflows," while `/platform` calls Airtable an "AI-native app platform" and `/platform/ai` names Omni and Field Agents as the new app-building/agent layer. The company still grounds the product in database/spreadsheet familiarity: shared data, bases, views, sync, interfaces, automations, and cross-tool integrations.

The company page says Airtable was founded in 2012, is used by more than 500,000 organizations, including 80% of the Fortune 100, has raised $1.4B, and has a team of 700+ people. Those are self-reported site claims, recorded as page-attested state rather than independently verified facts.

## What They Offer

One flagship platform plus a few paid add-ons; the full priced plan/add-on roster is in [`offerings.md`](offerings.md).

- **Airtable app platform:** Free, Team, Business, and Enterprise Scale plans; Team is "$20USD per seat/month billed annually," Business is "$45USD per seat/month billed annually," Enterprise Scale is "Custom pricing." `[published]`
- **AI app building and agents:** Omni, Airtable AI, and Field Agents; plan allowances run from "500 AI credits per editor each month" on Free to "25,000 AI credits per paid user each month" on Enterprise Scale, with AI-credit packs starting at "$120/month for 10k credits." `[published]`
- **Data/app-building surface:** relational databases, Interface Designer, automations, views, reporting, sync, governance/security, HyperDB, App Library, Web API, Enterprise API, templates, and marketplace extensions. Pricing is plan-gated rather than separately priced. `[published]`
- **Portals:** guest-user access add-on; pricing grid shows "Starts at $120/month for 15 guests" and "Starts at $150/month for 15 guests," while Enterprise Scale says "Contact Sales." `[published]`
- **Professional services / partner services:** qualified Business and Enterprise Scale customers can buy Airtable professional service packages; the public page points to partners and does not publish a price. `[on-request]`

## How It Works / Model

Self-serve entry is free: "Our Free plan is available at no cost," and signup CTAs run across the site. Paid packaging is per-seat SaaS: pricing FAQ says Team and Business plans charge users with edit permissions, while read-only collaborators, form submissions, and share links are not charged. Enterprise Scale moves to sales-led custom pricing and adds governance/admin controls, Enterprise API, HyperDB, audit logs, DLP, EKM, data residency, HIPAA compliance, and invoicing.

The product model is platform-led rather than per-feature checkout. Teams create bases and apps, connect data through integrations/API/sync, build interfaces and automations, then optionally add AI credits and Portals. Marketplace extensions and templates broaden the ecosystem, while Airtable's services/partners handle heavier implementation needs.

## Positioning & Audience

Airtable targets business teams and enterprise organizations that need custom workflow software without a traditional software build. It positions against spreadsheets and rigid single-purpose tools: the platform page contrasts Airtable with spreadsheets by saying spreadsheets track information, while Airtable "makes your data actionable." The audience examples are operational teams - product, marketing, project management, operations, sales, design/creative, HR, finance, retail, education, technology, and agencies.

The 2026 positioning is AI-forward: "Don't just ask AI. Deploy it." The pitch is not just chatbot assistance; Airtable says teams can build production-ready apps with Omni and embed Field Agents into workflows that act across records and connected systems.

## Nav Structure

```
- Platform
  - Airtable Platform — /platform
  - AI App Building — /platform/app-building
  - AI Agents — /platform/ai-agents
  - Portals — /platform/portals
  - Scale / HyperDB — /platform/hyperdb
  - Features: Automations, Databases, Interfaces, Reporting, Views, Governance and Security, Airtable AI, What's New
  - Tools: Integrations, Download
- Solutions
  - Teams: Product, Marketing, Project Management, Operations, Sales, Design & Creative, Human Resources, Finance
  - Industries: Media & Entertainment, Retail, CPG Manufacturing, Education, Technology, Agency & Professional Services
  - Customer Story: Code and Theory
- Resources
  - Resources Hub: Reports, eBooks, Webinars, Quick Reads, Demos
  - Templates: Project Management, Content Calendar, Event Planning, Product Roadmap, Resource Allocation, Product Catalog, and more
  - AI Plays, Blog, Customer Stories, Builders & Breakthroughs, Videos, Events
  - Learn & Support: Academy, Community, Developer Docs, Help Center
  - Ecosystem: Marketplace, Partners, Services
- Enterprise — /solutions/enterprise
- Pricing — /pricing
- Company footer: About, Careers, Status, Newsroom, Security, API, Privacy, Terms, Accessibility
```

## Credibility & Proof

- **Scale claims:** about page states "500,000 organizations use Airtable"; platform page says "Used by more than 500,000 organizations around the world"; Howie Liu bio says "more than 500,000 organizations, including 80% of the Fortune 100."
- **Funding / company facts:** about page "Key Facts" states "$1.36B total funding to date" and the CEO bio says Airtable "has raised $1.4B total in funding, with a last funding valuation of $11.6B." Treat the discrepancy as two self-reported site phrasings, not a reconciliation.
- **Named customer proof:** homepage/platform/about show enterprise logos and testimonials, including AWS, Walmart, HBO, Schaeffler, Shopify, Code and Theory, AWS, and West Elm; customer stories include OpenAI.
- **Security/compliance:** trust page names SOC 2 Type 2, ISO/IEC 27001:2022, ISO/IEC 27701:2019, HIPAA, TX-RAMP Level 2, GDPR/UK GDPR, CCPA/CPRA, CAIQ, SIG Lite, HECVAT, Enterprise Key Management, EU data residency, and HackerOne bug bounty.
- **Status:** `status.airtable.com` is linked from the homepage footer and captured as a public service-status surface.
- **Brand assets:** trademark page says Airtable's "primary logo includes an icon and our full wordmark" and links an Airtable-hosted logo-lockup share; color primary wordmark/logomark assets were saved locally under `assets/`.

## Visual & Brand Impression

Polished enterprise SaaS with a white, high-contrast, product-led surface: dark ink (#181D26), rounded product screenshots, dense nav flyouts, soft peach/yellow accent panels, and the signature Airtable block icon in yellow, pink, and blue. The current homepage makes AI the first-viewport story and uses UI mockups/cards rather than abstract illustration; the product screenshots repeatedly show dashboards, grids, app cards, and automation/agent flows. The brand feels more operational and enterprise than playful: substantial whitespace, clean typography, many customer proof strips, and black pill CTAs.

## Strategic Read

Airtable is repositioning from no-code spreadsheet/database into an AI-native operations platform. The old center of gravity - bases, records, views, automations, and interfaces - is still visible in the nav and pricing limits, but the homepage and platform pages now foreground Omni and Field Agents. The strongest capture signal is the packaging tension: pricing remains classic per-seat SaaS, while the AI layer adds a visible usage overlay through monthly AI credits and paid credit packs.

## Provenance

- **Pages:** 12 Firecrawl pages analyzed on 2026-06-17: homepage, platform, pricing, integrations, marketplace, AI, API, about, trust/security, trademark guidelines, logo lockups, and status. Map plus one targeted logo/brand map search informed page choice.
- **Verify:** all sourceURLs matched, all bodies were unique, and no junk soft-404s were detected after the final 12-page verify.
- **Credits:** 14 Firecrawl credits (2 maps + 12 page scrapes). Logos were measured from the captured logo-lockup share plus local saved assets, with no Firecrawl logo add-on credit; visual-evidence tiling used cached screenshots with zero Firecrawl spend.
- **Couldn't get:** no JSON-LD identity block on the homepage. Current revenue/ARR/cap table are not site-derived. The Google S2 favicon fetch returned HTML in local headed fetch, so the official Airtable color mark from the logo-lockup share is used for `logos.logomark`.
- **Run profile:** express full-pack request — +productivity_saas cohort pack, +offerings.md, +logos, +visual-evidence requested; flagship product-image capture is N/A for a software platform, so visual evidence will use screenshots instead.
