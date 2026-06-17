---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: linear.app
name: Linear
legal_entity: ""   # not site-derivable from the captured pages (no ©/legalName surfaced)
aliases: []
parent: []
owns: []

# Capture meta
captured_at: 2026-06-17
capture_method: firecrawl
site_notes: "Next.js app (/_next/ in rawHtml; branding payload present under data.branding — colors/fonts/logo all populated). Homepage is a heavy client-rendered marketing page (17K md) with a numbered product pipeline (1.0 Intake → 5.0 Monitor) rendered as interactive mockups; H1 reads thrice ('The product development system for teams and agents'). /pricing markdown is compact (3.5K) but carries the full tier prices + the complete feature matrix inline — no JS wall. /security carries the trust seals (SOC2/ISO/GDPR/HIPAA) cleanly. /integrations (26K) is a categorized third-party app directory with a 'Build your own… submit it to the directory' mechanism — the app-platform tell. Brand logo is an inline SVG data-URI wordmark (decoded to assets/wordmark.svg). Carries the productivity_saas cohort pack."
key_pages:
  pricing: /pricing
  security: /security
  integrations: /integrations
  customers: /customers
  product: /homepage
modules:
  productivity_saas: productivity_saas.md   # cohort pack, captured 2026-06-17
unverified_fields:
  - "Headcount, revenue, funding, legal entity — not on the captured marketing pages (deep-research job). Self-reported social proof only: 'Trusted by more than 33,000 companies'."
  - "Hero H1 + AI framing are A/B/rotation-prone (the 2026 AI-rebrand churn) — point-in-time snapshot, not fixed."

# Description
description: "A fast, keyboard-driven project and issue-tracking system for software product teams — issues, projects, cycles, roadmaps, and customer requests in one app, increasingly built around AI agents that triage, draft, and ship work alongside humans."

# Classification
entity_type: Company
target_market: [B2B]
offering_category: [Software / SaaS]
portfolio_shape: Single
business_model: Subscription
primary_industry: Technology

# Visual identity
logo_url: assets/wordmark.svg   # inline-SVG wordmark decoded from branding.images.logo (white "Linear" wordmark + geometric mark)
brand_colors: { primary: "#5E6AD2", accent: "#E4F222" }   # signature indigo (link/brand) + lime accent on a near-black canvas (#08090A); branding payload ranks the light-grey text #D0D6E0 as "primary" — that's the on-dark text color, not the brand hue
fonts: [Inter]
color_scheme: dark
design_framework: next.js   # /_next/ in rawHtml, not branding.designSystem
---

## Overview

Linear is a project- and issue-tracking tool for software product teams — it bills itself as **"the product development system."** A single fast, keyboard-driven app holds issues, projects, cycles, initiatives, roadmaps, documents, and customer requests, and the 2026 product leans hard into AI: agents that triage incoming work, draft PRDs, and open pull requests inside Linear. It's a **single product** sold per-seat to teams, positioned as the opinionated, high-craft alternative to Jira-style trackers.

## What they offer

One product, organized as a pipeline (the homepage numbers it **1.0 Intake → 5.0 Monitor**):

- **Intake** — turn conversations/customer feedback into routed, labeled issues; Linear Asks (Slack/email/web-form intake), customer requests
- **Plan** — projects, documents, initiatives, roadmaps, PRDs, sub-initiatives
- **Build** — issues, cycles, Git/PR automations, releases
- **AI & agents** — **Linear Agent** (beta), **Coding Sessions** (the "New" hero CTA), **Triage Intelligence**, **Code Intelligence** (beta), plus an Agents integration category that runs third-party coding agents (Codex, Cursor, Copilot, Devin) inside Linear
- **Monitor** — Pulse, Insights, dashboards, progress reports, data-warehouse sync
- **Platform** — public API + webhooks, **MCP access**, and a categorized **integration directory** you can submit your own integration to

## How it works / model

Self-serve, product-led, **per-seat subscription** with a free tier. Four plans (billed yearly): **Free $0** (unlimited members, 2 teams, 250 issues, Agent platform, Linear Agent) → **Basic $10/user/mo** (5 teams, unlimited issues) → **Business $16/user/mo** (unlimited teams, Triage/Code Intelligence, Insights, Asks) → **Enterprise** (Custom, annual-only, SAML/SCIM, advanced controls). A usage meter sits *under one feature* — Coding Sessions "** Requires AI credits" — but plan billing is per-seat. Install is sign-up + web/desktop/mobile apps; the platform surface (API, MCP, integration directory) lets third parties build on it.

## Positioning & audience

Targets **software product-development teams** — engineers, PMs, designers — with a craft/performance wedge: speed, keyboard-first UX, and opinionated workflow. The 2026 repositioning is explicitly AI-native: *"Designed for the AI era"*, *"for teams and agents"*, *"Purpose-built for planning and building products with AI agents."* Social proof leans on high-end tech logos (OpenAI, Ramp, Opendoor) and scale ("more than 33,000 companies").

## Nav structure

```
- Product (mega-nav: Intake, Plan, Build, Agents, Insights, …)
- Resources (Integrations — /integrations, Developers/API — /developers, Docs — /docs, Download — /download)
- Customers — /customers
- Pricing — /pricing
- Now — /now   ·   Contact — /contact
- Open app / Log in / Sign up — /login, /signup
```

## Credibility & proof

- **Scale claim:** "Trusted by more than **33,000** companies" (/pricing) / "Linear powers over 33,000 product teams" (homepage).
- **Named customers:** OpenAI, Ramp, Opendoor (homepage + /customers quotes).
- **Security/compliance (/security):** SOC 2 Type II, ISO/IEC 27001:2022 certified, GDPR, HIPAA (Request BAA); separate trust portal at trust.linear.app; Enterprise lists an Uptime SLA; status page linearstatus.com.
- **Platform openness:** public API + webhooks (Core feature on /pricing), MCP access, an integration directory that invites third-party submissions.

## Visual & brand impression

A confident, high-craft dark UI brand. Near-black canvas (#08090A) with a signature indigo (#5E6AD2) and a sharp lime accent (#E4F222), set in Inter — restrained, engineering-led, fast-feeling. The homepage foregrounds live-looking product mockups (issues, agent activity, PRs) over marketing illustration, signaling "the tool is the pitch." Reads as premium, opinionated, and aimed squarely at technical teams. Dark color scheme throughout.

## Strategic read

Linear is making a deliberate bet that the 2026 product-development loop is **human + agent**, and is rebuilding its category position around it — from "a faster issue tracker" to "the system where teams and AI agents plan and ship together." The numbered pipeline (Intake→Monitor) frames Linear as the connective tissue across the whole dev lifecycle, while the agent surface (Linear Agent, Coding Sessions, third-party agents via the directory) tries to make Linear the place agents *act*, not just the place work is logged. The risk and the wedge are the same: craft and opinion in a category where incumbents (Jira) win on breadth and lock-in.

## Provenance

- **Pages:** 5 analyzed via Firecrawl (maxAge:0, location:US, waitFor) — homepage, /pricing, /security, /integrations, /customers; map used for inventory only.
- **Verify:** all 5 sourceURLs matched; all body md5s unique; no junk soft-404s.
- **Credits:** 6 (1 map + 5 scrapes; no enhanced-proxy retries, no PDFs).
- **Couldn't get:** legal entity (no ©/legalName on captured pages); headcount/revenue/funding (not on a marketing site).
- **Structured layer (schema 2.6):** branding under `data.branding` populated (colors/fonts/Inter/dark/inline-SVG wordmark); framework `next.js` from rawHtml `/_next/`. No JSON-LD parsed.
- **Run profile:** seed capture for the **productivity_saas** cohort pack (first live store instance) — `productivity_saas.md` written alongside this profile.
