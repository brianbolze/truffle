---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: 1

# Identity
domain: notion.com
name: Notion
aliases: [notion.so]                  # legacy primary domain; still backs the app, help, and legal URLs
parent: []                            # legal entity is "Notion Labs, Inc." — operating co, not a parent owner
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Next.js (__NEXT_DATA__ + /_next/). notion.com 302→www.notion.com (marketing); app lives at app.notion.com, devs at developers.notion.com / notion.dev. Map is locale-heavy and polluted with /blog + app.notion.com/p/<user-page> noise — filter hard; homepage mega-nav is the reliable offering map. branding.images.logo is a data-URI → favicon fallback. Pricing renders fully client-side, captured clean. Terms/privacy + some help links still resolve to legacy notion.so."
key_pages:
  product: /product
  pricing: /pricing
  ai: /product/ai
  agents: /product/agents
  enterprise: /enterprise
  about: /about
unverified_fields:
  - "Headcount, funding, revenue — not on the marketing site (deep-research job). Press links cite a 2024 $10B valuation but that's an event, out of scope."

description: "An all-in-one AI workspace where teams run docs, wikis, projects, and databases in one connected tool, now layered with AI agents that search across apps, take meeting notes, and automate recurring work."

# Classification
entity_type: Company
target_market: [B2B, B2C]
offering_category: [Software / SaaS]
portfolio_shape: Flagship + companions
business_model: Subscription
primary_industry: Technology

# Visual identity
logo_url: https://www.notion.com/front-static/favicon.ico   # branding.images.logo was an inline data-URI
brand_colors: { primary: "#02093A", accent: "#0075DE" }     # near-black navy + Notion blue; verified against hero/CTAs
fonts: [Inter]                        # branding reports "NotionInter" (a custom Inter cut) + Inter
color_scheme: light
design_framework: next.js
---

## Overview

Notion is a single connected workspace that absorbs the tools a team would otherwise scatter across tabs — docs, wikis, project management, and flexible databases — built from composable "blocks." The 2026 positioning has shifted hard toward AI: the homepage hero is "Meet the night shift" and the site now frames Notion as "Your AI workspace" where **Notion Agents** "keep work moving 24/7." It sells to both individuals (free, personal use) and businesses, with an explicit enterprise push. Claims **over 100M users worldwide** and trust from **98% of the Forbes Cloud 100**.

## What they offer

One flagship — the Notion workspace (Docs, Knowledge Base/Wikis, Projects, Databases) — with a companion set, all bundled under one per-seat plan rather than sold as separate SKUs:

- **Notion AI:** chat, generate/edit docs, autofill databases, translate; plus **Research mode** (deep-reasoning reports) and **Enterprise Search** across connected apps (Slack, GitHub, etc.).
- **Agents:** Notion Agent (multi-step work) + **Custom Agents** that run repetitive work autonomously, metered — "Free to try, then **$10 per 1,000 monthly Notion credits**"
- **AI Meeting Notes:** auto-transcription + summaries.
- **Notion Calendar & Notion Mail:** standalone companion apps (Mail syncs with Gmail) that sync into the workspace.
- **Developer platform:** public API, webhooks, and **Workers** (Beta) to run custom code; surfaced separately at notion.dev / developers.notion.com.

The site also runs a large **Templates**, **Connections**, and **Consultants** ecosystem. Per-offering detail is a Tier-1 `offerings.md` job (not captured here).

## How it works / model

Per-seat SaaS subscription with a freemium on-ramp. Four tiers (monthly, per member):

- **Free ($0):** individuals; trial of Notion AI, basic forms/sites, Calendar + Mail, databases.
- **Plus ($10):** small teams; custom forms/sites, unlimited blocks/uploads, basic connections.
- **Business ($20, "Recommended"):** Notion Agent, AI Meeting Notes, Enterprise Search (Beta), SAML SSO, private teamspaces, premium connections.
- **Enterprise (Custom):** zero data retention with LLM providers, SCIM, audit log, advanced security/DLP/SIEM, CSM.

Two **usage-based** add-ons ride on top of any plan: **Custom Agents** ($10 / 1,000 credits) and **Workers** (Beta, credit-metered from Aug 11). The Plus plan is **free for students and educators**. Refunds: full within 3 days (monthly) / 30 days (annual).

## Positioning & audience

Pitch is consolidation: "**More productivity. Fewer tools.**" — an on-page calculator tallies the per-user cost of the point tools Notion claims to replace (AI search $35, AI meeting notes $18, project mgmt $24, basic CRM $20, etc.) into a "monthly savings" figure. Quotes Forbes' "**Your AI everything app.**" Audience spans personal/individual through startup, small business, and enterprise, sliced by team (Eng & Product, Design, Marketing, IT) and by use case. The competitive frame is implicitly the entire SaaS stack (Google Docs, Confluence, Asana, Slack search, plus standalone AI tools), now reframed as an AI-native single platform.

## Nav structure

```
- Product
  - Notion — Your AI workspace — /product
  - Notion Calendar — /product/calendar
  - Notion Mail — /product/mail
  - Notion AI — /product/ai
  - Agents — /product/agents
  - AI Meeting Notes — /product/ai-meeting-notes
  - Enterprise Search — /product/enterprise-search
  - Knowledge Base — /product/wikis
  - Docs — /product/docs
  - Projects — /product/projects
  - Connections — /connections
  - Security — /security
- AI
  - AI features: Notion AI, Agents, AI Meeting Notes, Enterprise Search
  - Explore use cases: For work — /product/ai/use-cases?type=work · For life — ?type=life
- Solutions
  - Teams: Eng & Product — /product/notion-for-product-development · Design — /product/notion-for-design · Marketing · IT
  - Company size: Startups — /startups · Small businesses — /teams · Enterprise — /enterprise
  - Use Cases: Education — /product/notion-for-education · Personal — /personal · Professional — /use-case · AI use cases
- Resources
  - Browse: Templates — /templates · Consultants — /explore-consultants · Connections
  - Discover: What's New — /releases · Customer stories — /customers · Blog · Webinars
  - Learn: Developers — developers.notion.com · Academy · Product tours — /product/demos · Help
- Developers — notion.dev
- Enterprise — /enterprise
- Pricing — /pricing
- Request a demo — /contact-sales
```

## Credibility & proof

- **Scale:** Over 100M users worldwide; 1.4M+ community members.
- **Logos:** OpenAI, Figma, Ramp, Cursor, Vercel, Nvidia, Volvo, L'Oréal, Discord, Toyota, Riot Games, Affirm, 1Password — "Trusted by 98% of the Forbes Cloud 100," "62% of Fortune 100," "Over 50% of YC companies."
- **Analyst:** "#1 knowledge base 3 years running (G2)," "#1 AI enterprise search (G2)," "#1 rated AI writing (G2)."
- **Customer stories** with named quotes (OpenAI, Ramp, Toyota — "reduce timelines by 3x," Vercel, Cursor, Figma, Match).
- **Press:** Forbes ($10B "AI everything app"), Fast Company, TechCrunch, NYT, WSJ, The Verge.
- **Trust/security** surface (SAML, SCIM, audit log, DLP/SIEM, zero-data-retention) anchors the enterprise claim.

## Visual & brand impression

Confident, polished, design-forward — the product the screenshots are selling looks like the brand itself. The homepage opens on a **deep near-black navy** hero ("Meet the night shift") with a glowing circuit motif, then drops into a long scroll of **clean white "bento" cards** showing real product UI (agents, search, meeting notes, docs, calendar, mail). Type is Notion's signature Inter-family sans; accents are a bright **Notion blue (#0075DE)**. The palette is essentially monochrome-plus-one-blue — restrained and modern, letting the colorful product screenshots and customer logos carry the energy. Reads as a mature, category-leading SaaS brand mid-pivot to an AI-first story.

## Strategic read

The capture caught Notion mid-repositioning: the durable "all-in-one workspace" identity (still the spine of the About page's tools-and-history narrative) is now wrapped in an aggressive **AI/agents** front end — agents are the hero, AI is in the meta title and every plan tier, and a new **credit-based usage layer** (Custom Agents, Workers) sits on top of the per-seat model. That's a notable business-model wrinkle: subscription remains primary, but Notion is grafting consumption pricing onto AI compute. The "fewer tools" savings calculator shows the strategy plainly — Notion is no longer pitching a doc tool but a **stack-replacement platform**, betting that an AI-native single workspace out-competes a federation of point SaaS tools.

## Provenance

- **Pages:** homepage, `/product`, `/pricing`, `/product/ai`, `/product/agents`, `/enterprise`, `/about` (7) — all Firecrawl, US geo, all-formats; `design_framework` from `rawHtml` (`__NEXT_DATA__`), colors/fonts cross-checked vs screenshots (branding logo was a data-URI → favicon fallback).
- **Verify:** all HTTP 200, all bodies md5-unique (clean).
- **Credits:** not recorded this run.
- **Couldn't get:** per-product deep pages (Calendar, Mail, Docs, Projects), Templates/Connections catalogs, developer docs; financials/headcount (out of scope).
