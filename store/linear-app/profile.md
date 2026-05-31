---
schema_version: 1

# Identity
domain: linear.app
name: Linear
aliases: []
parent: []
owns: []

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "JS-heavy (Next.js); mega-nav 'Product'/'Resources' flyouts render client-side and do NOT appear in scrape markdown even with onlyMainContent:false + waitFor — reconstruct nav from the footer + /v2/map instead. Pricing $ values are NOT in markdown; recover from the pricing screenshot or an html-format scrape. /product and /features both resolve to the Features page; bare /product without trailing context can return the login wall (md ~217 chars) — use /features. /method markdown is thin (~1KB), mostly client-rendered. MUST request the `branding` format explicitly — it is not included by default; once requested it is rich (colors/fonts/typography/components). branding.designSystem reports 'custom' though the site is Next.js — use rawHtml __NEXT_DATA__ for framework."
key_pages:
  pricing: /pricing
  features: /features
  customers: /customers
  about: /about
  enterprise: /enterprise
  method: /method
  security: /security
  integrations: /integrations
  changelog: /now            # /now is the live changelog; archive at /changelog
  # Product surfaces (each its own marketing page):
  intake: /intake
  plan: /plan
  build: /build
  diffs: /diffs
  monitor: /monitor
unverified_fields:
  - "Pricing $ values were recovered from the pricing screenshot + an html-format scrape, not the default markdown (markdown rendered the price node as a JS scrambler artifact). Tiers + amounts are confirmed; treat as screenshot-sourced."
  - "logo_url — Firecrawl `branding.images.logo` returns the Linear wordmark as an inline data-URI SVG (in .payloads/homepage.json), not a hostable URL; favicon (derivable from domain) and og image (https://linear.app/static/og/homepage.jpg) are the URL alternatives."

# Description — one sentence
description: "A purpose-built SaaS for software product teams that unifies issue tracking, planning, and build/review workflows — increasingly oriented around shared human-and-AI-agent work — in one fast, opinionated app billed per seat."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2B]
offering_category: [Software / SaaS]
portfolio_shape: Single      # one unified system with many surfaces/features, not separately-bought products — see body
business_model: Subscription
primary_industry: Technology

# Visual identity — lifted from Firecrawl `branding` (homepage pass)
logo_url:                    # branding.images.logo is an inline data-URI SVG (in payload), not a hostable URL; favicon derivable from domain
brand_colors: { primary: "#D0D6E0", accent: "#5E6AD2", secondary: "#E4F222", background: "#08090A" }   # copied from branding.colors — NB its "primary" is the light text color; the brand hue is accent #5E6AD2 (Linear violet); secondary #E4F222 is the acid-yellow testimonial-card accent
fonts: [Inter, SF Pro Display]   # branding.fonts: Inter=body, SF Pro Display=heading (Roboto/Open Sans are fallback-stack noise)
color_scheme: dark           # verified from screenshot + branding.colorScheme
design_framework: next.js    # from rawHtml __NEXT_DATA__ + /_next/ (branding.designSystem reported "custom" — wrong)
---

## Overview

Linear is a product-development tool for software teams — issue tracking at its core, extended into planning (projects, roadmaps, initiatives, PRDs), code review (Diffs), and progress monitoring (Pulse, Insights, dashboards). It markets itself as **"the product development system for teams and agents,"** and its current positioning leans hard into the AI era: drafting PRDs, triaging and routing work, and running coding agents (Cursor, Codex, GitHub Copilot, Claude) alongside human teammates inside the same tool. It is sold per seat to product, engineering, and design teams — from "ambitious startups to major enterprises" — and positions on speed, opinionated craft, and a unified workflow rather than breadth of configuration.

## What they offer

One unified product, organized as a sequence of **surfaces** (each with its own marketing page) wrapping a deep **feature** set:

- **Intake** (`/intake`) — turn conversations/customer feedback into routed, labeled, prioritized issues. Sub-features: Linear Agent, Triage, Customer Requests, Linear Asks.
- **Plan** (`/plan`) — projects, documents, initiatives, visual planning; roadmaps and PRDs.
- **Build** (`/build`) — issues, AI agents, Linear MCP, Git automations, cycles.
- **Diffs** (`/diffs`) — structural code-review of human *and* agent output, in-app.
- **Monitor** (`/monitor`) — Pulse, Insights, dashboards; project updates and analytics.

Cross-cutting features surfaced separately: **Asks**, **Agents**, **Customer Requests**, **Insights**, **Mobile**, **Integrations**, **Changelog**. This is **`is_multi_product: false`** by the TAXONOMIES test — you don't comparison-shop or separately buy "Plan" vs. "Build"; they're modules of one app on one per-seat price. (Same judgment call as the Notion example in TAXONOMIES — worth re-checking as Linear's surface count grows.)

## How it works / model

Self-serve, per-seat subscription with a sales-assisted Enterprise tier. Sign up → use free → upgrade by seats/features; Enterprise is "contact sales." Pricing (verbatim, from the pricing page, billed yearly):

- **Free — $0** — "Free for everyone." Unlimited members, 2 teams, 250 issues, Agent platform, Linear Agent (beta).
- **Basic — $10 per user/month** — All Free features +, 5 teams, unlimited issues, unlimited file uploads, admin roles.
- **Business — $16 per user/month** — All Basic features +, unlimited teams, private teams & guests, Triage Intelligence, Linear Agent automations (beta), Code Intelligence (beta), Linear Insights, Linear Asks, Zendesk & Intercom integrations.
- **Enterprise — Custom** — "Annual billing only." All Business features +, invoice/PO billing, SAML & SCIM, granular admin controls, enterprise-grade security, advanced org modeling, migration & onboarding support, priority support, account management.

Monthly billing is offered at a higher per-seat rate (the page defaults to a "Billed yearly" toggle). Delivery is a web + desktop + mobile app; value compounds via deep integrations and an agent/MCP platform.

## Positioning & audience

- **Who:** software product teams — engineering, product, design — explicitly spanning startups → enterprise (dedicated `/enterprise` and `/startups` pages).
- **Against:** legacy issue trackers. The homepage runs a banner reading **"Issue tracking is dead"** (→ `/next`), an unusually direct shot at the Jira-era category it grew out of. A `/switch` page targets migrations; `/compare` exists.
- **Claimed edge:** opinionated, fast, craft-forward ("the right opinions for fast moving teams"), and **AI-native** — "A new species of product tool… with AI workflows at its core." Three stated pillars: *Built for purpose*, *Powered by AI agents*, *Designed for speed*.

## Nav structure

Top bar: **Product** ▾, **Resources** ▾, Customers, Pricing, Now, Contact · Docs · Log in · Sign up. (The two ▾ flyouts are client-rendered and weren't in the scrape; structure below is reconstructed from the footer + map.)

```
- Product
  - Intake — /intake
  - Plan — /plan
  - Build — /build
  - Diffs — /diffs
  - Monitor — /monitor
  - Pricing — /pricing
  - Security — /security
- Features
  - Asks — /asks
  - Agents — /agents
  - Customer Requests — /customer-requests
  - Insights — /insights
  - Mobile — /mobile
  - Integrations — /integrations
  - Changelog — /changelog
- Company
  - About — /about
  - Customers — /customers
  - Careers — /careers
  - Blog — /blog
  - Method — /method        (The Linear Method)
  - Quality — /quality
  - Brand — /brand
- Resources
  - Switch — /switch
  - Download — /download
  - Documentation — /docs
  - Developers — /developers
  - Status — linearstatus.com
  - Enterprise — /enterprise
  - Startups — /startups
- Connect
  - Contact us — /contact
  - Community (Slack) — /join-slack
  - X (Twitter) — x.com/linear
  - GitHub — github.com/linear
  - YouTube — youtube.com/@linear
- Legal: Privacy /privacy · Terms /terms · DPA /dpa
- Top-level utility: Now — /now (live changelog)
```

## Credibility & proof

- **Scale claim:** "Linear powers over **33,000** product teams."
- **Logo wall (pricing page):** Vercel, Cursor, Oscar, OpenAI, Coinbase, Cash App, BOOM, Ramp.
- **Named testimonials (homepage):** Gabriel Peal (OpenAI), Nik Koblov (Head of Engineering, Ramp), Kaz Nejatian (Opendoor).
- **Customer case studies (`/customers/*`):** Brex ("data-driven pilot"), Scale ("compressed bug resolution time by 52%"), Semgrep, Pulley, Dandelion Chocolate.
- **Trust/compliance signals:** dedicated `/security`, `/enterprise`, HIPAA compliance + SOC-style controls in the Enterprise tier, EU data hosting (changelog), a Trust Center (trust.linear.app), DPA, SAML/SCIM/SSO, audit log.

## Visual & brand impression

Confident, minimalist, **dark-mode-first**: a near-black canvas (`#08090A`) with high-contrast off-white type (`#D0D6E0`) and a single restrained blue-violet accent (`#5E6AD2`, the Linear brand hue). Type is Inter (body) + SF Pro Display (headings); buttons are fully-rounded pills (9999px radius) on an 8px spacing grid — tight, system-native. The page is built almost entirely around **live, pixel-accurate product UI** (issue panels, roadmap timelines, agent threads, code diffs) rather than stock illustration — the product *is* the hero image. Section labels use an engineering-document affectation ("FIG 0.2", "1.0 Intake", "2.0 Plan") reinforcing a precise, technical, craft register. Two deliberately loud testimonial cards (one pale lavender, one acid yellow `#E4F222`) break the monochrome for contrast. Overall read: extremely high design maturity, taste-led, developer-native — the visual language itself is a positioning claim.

## Strategic read

The capture caught Linear mid-repositioning from "best-in-class issue tracker" to **"the product development system for teams and agents."** Agents are no longer a feature bolt-on but the organizing thesis — Intake auto-routes work, Build runs coding agents end-to-end, Diffs exists specifically to *review agent output*, and the homepage demo stars Cursor/Codex/Copilot as named teammates. The blunt "Issue tracking is dead" banner signals they're willing to obsolete their own origin category to own the AI-native frame. For a competitor/market read, the durable state here is: single unified per-seat SaaS, upmarket motion (Enterprise + 33k teams + marquee AI-lab logos), differentiating on craft/speed/opinion and now agent-orchestration.

## Provenance

- **Pages analyzed (all Firecrawl `/v2/scrape`, 2026-05-30):** homepage (`/`, full pass: markdown + html + rawHtml + links + branding + full-page screenshot), `/pricing` (markdown + screenshot, + a follow-up html pass to recover $ values), `/features`, `/about`, `/customers`, `/enterprise`, `/method`. Site inventory via `/v2/map` (149 URLs).
- **Raw payloads + screenshots:** `captures/2026-05-30/.payloads/`; cleaned page markdown: `captures/2026-05-30/*.md`.
- **Visual identity** lifted from the homepage `branding` payload (colors, fonts, typography, components).
- **Couldn't get cleanly:** mega-nav flyout contents (client-rendered); pricing $ from markdown (recovered via screenshot/html); `/method` body (client-rendered, thin); a hostable `logo_url` (branding returns an inline SVG — see `unverified_fields`).
