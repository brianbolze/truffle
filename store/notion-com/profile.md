---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: notion.com
name: Notion
aliases: [notion.so]                  # legacy primary domain; still backs the app, help, and legal (Terms & privacy → notion.so)
parent: []                            # legal entity is "Notion Labs, Inc." — operating co, not a parent owner
owns: []                              # Calendar / Mail are product surfaces on notion.com, not separately-domained sub-brands
socials:
  linkedin: https://www.linkedin.com/company/notionhq/
  x: https://x.com/NotionHQ
  instagram: https://www.instagram.com/notionhq/
  youtube: https://www.youtube.com/channel/UCoSvlWS5XcwaSzIcbuJ-Ysg
  facebook: https://www.facebook.com/NotionHQ/
external: {}                          # no JSON-LD on the homepage → no company-declared crunchbase/wikipedia/etc. record to seed

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Next.js (__NEXT_DATA__ + /_next/image + front-static). notion.com 302→www.notion.com (marketing); app at app.notion.com, devs at developers.notion.com / notion.dev. Map is locale-heavy + polluted with /blog + /templates noise — filter hard; homepage mega-nav (flattened into markdown) is the reliable offering map. No application/ld+json on homepage (signals returns nothing). branding.images.logo is null/data-URI → wordmark extracted from inline rawHtml SVG (class=wordmark_wordmark__*); logomark = apple-touch logo-ios.png (black N on baked white). Pricing renders client-side but captures clean. Terms/privacy + some help links still resolve to legacy notion.so."
key_pages:
  product: /product
  pricing: /pricing
  ai: /product/ai
  agents: /product/agents
  ai_meeting_notes: /product/ai-meeting-notes
  enterprise_search: /product/enterprise-search
  calendar: /product/calendar
  mail: /product/mail
  wikis: /product/wikis
  docs: /product/docs
  projects: /product/projects
  connections: /connections
  enterprise: /enterprise
  security: /security
  about: /about
unverified_fields:
  - "Headcount, funding, revenue — not on the marketing site (deep-research job). Press cites a 2024 $10B valuation, but that's an event, out of scope."
  - "Founders / founding date — the About page tells an origin story but names neither; left to deep research."
  - "Prices/IA are a point-in-time snapshot, not fixed — Custom Agents began metering on May 4, 2026; Workers start using credits Aug 11; the homepage 'savings' total is a function of the team-size slider."

description: "An all-in-one AI workspace where teams run docs, wikis, projects, and databases in one connected tool, now fronted by AI agents that search across apps, take meeting notes, and automate recurring work."

# Classification
entity_type: Company
target_market: [B2B, B2C]
offering_category: [Software / SaaS]
portfolio_shape: Flagship + companions
business_model: Subscription          # per-seat SaaS primary; a usage-based Notion-credits layer (Custom Agents, Workers) rides on top
primary_industry: Technology

# Visual identity
logo_url: assets/wordmark.svg         # canonicalized to the wordmark (2.5); extracted from the inline header SVG
logos:
  wordmark: { src: assets/wordmark.svg, w: 105, h: 30 }                                                                  # N-sticker + "Notion" in black; viewBox 0 0 105 30
  logomark: { src: "https://www.notion.com/front-static/logo-ios.png", px: 512, transparent: false }                     # the black N-sticker on a BAKED WHITE square — needs a treatment on dark
  og:       { src: "https://www.notion.com/front-static/meta/custom-agents-og.png", w: 2400, h: 1260 }                   # current campaign cover ("Your 24/7 AI team" + wordmark) — rotates
brand_colors: { primary: "#02093A", accent: "#0075DE" }   # near-black navy hero/text + Notion blue CTAs; an AI-era indigo (#455DD3) appears in gradients (verified vs screenshots)
fonts: [Inter]                        # branding reports "NotionInter" (a custom Inter cut) + Inter
color_scheme: light                   # product canvas + most of the page is white; only the 2026 "night shift" hero is dark navy
design_framework: next.js             # rawHtml: __NEXT_DATA__, /_next/image, front-static (not branding.designSystem)
---

## Overview

Notion is a single connected workspace that absorbs the tools a team would otherwise scatter across tabs — docs, wikis, project management, and flexible databases — built from composable "blocks." The 2026 positioning has shifted hard to AI: the homepage hero is "**Meet the night shift,**" framing Notion as an AI workspace where **Notion agents keep work moving 24/7**. It sells to individuals (free, personal use) and businesses alike, with an explicit enterprise push. Claims **over 100M users worldwide** and that it is **trusted by 98% of the Forbes Cloud 100**. The company is Notion Labs, Inc., based in San Francisco.

## What they offer

One flagship — the Notion workspace — surrounded by AI features and two standalone companion apps, all bundled under one per-seat plan rather than sold as separate SKUs. Family-grain here; per-item depth (and the full feature/app roster Brian asked for) is in [`offerings.md`](offerings.md).

- **Notion workspace (flagship):** Docs, Knowledge Base/Wikis, Projects, and Databases in one connected tool — per seat, **Free $0 · Plus $10 · Business $20 · Enterprise custom** (per member/month) `[published]`
- **Notion AI:** chat, generate/edit docs, autofill databases, translate, **Research Mode** (deep-reasoning reports), and AI blocks — included on Business/Enterprise, trial on lower tiers `[published]`
- **Agents:** **Notion Agent** (personal, on-demand, all users) + **Custom Agents** (team-wide, scheduled/triggered) — "Free to try, then **$10 per 1,000 monthly Notion credits**" (metering began **May 4, 2026**) `[partial]`
- **AI Meeting Notes:** auto-transcription + summaries, records system audio (no bots), 19 languages — Business+ `[published]`
- **Enterprise Search:** answers across connected apps (Slack, Drive, GitHub, Jira…) — Business+ (Beta) `[published]`
- **Notion Calendar:** standalone app, syncs Google Calendar + Apple iCloud — **free** `[published]`
- **Notion Mail:** standalone AI inbox that syncs with Gmail — **free** `[published]`
- **Developer platform:** Public API, webhooks, **Workers** (Beta — start using credits Aug 11), and a CLI `[partial]`
- **Templates · Connections · Consultants:** a large free template gallery, app integrations, and a consultant marketplace `[published]`

Two **usage-based** add-ons ride on top of any qualifying plan: **Custom Agents** ($10 / 1,000 credits) and **Workers** (Beta). The Plus plan is **free for students and educators**.

## How it works / model

Per-seat SaaS subscription with a freemium on-ramp; **yearly billing saves up to 20%**. Four tiers (verbatim, per member/month):

- **Free — $0:** individuals; trial of Notion AI, basic forms/sites, Notion Calendar + Mail, databases.
- **Plus — $10:** small teams; custom forms/sites, unlimited charts/blocks/file uploads, basic connections.
- **Business — $20 ("Recommended"):** Notion Agent, AI Meeting Notes, Enterprise Search (Beta), SAML SSO, granular database permissions, private teamspaces, premium connections.
- **Enterprise — Custom:** zero data retention with LLM providers, SCIM, audit log, advanced security/DLP/SIEM, customer success manager.

On top of the seat price, **Custom Agents** run on metered **Notion credits** — "$10 per 1,000 credits," shared across the workspace, reset monthly, no rollover (an add-on for Business/Enterprise). **Workers** (Beta) move onto credits Aug 11. Custom domains/branding cost "**$8/month/domain paid annually, or $10/month per domain paid monthly**." Refunds: full within **3 days** (monthly) / **30 days** (annual). Seats are billed per member with prorated mid-cycle changes; guests are free.

## Positioning & audience

The pitch is consolidation: "**More productivity. Fewer tools.**" — an on-page calculator tallies the per-user cost of the point tools Notion claims to replace (AI Search $35, AI Chatbot $20, AI Meeting Notes $18, AI Writing Assistant $20, AI Email App $30, AI Research $40, Calendar Scheduling $15, Team Wiki $10, Project Management Tool $24, Basic CRM $20, Site Builder $20, Forms $15) into a "monthly savings" figure (the total flexes with a team-size slider). Quotes Forbes' "**Your AI everything app.**" Audience spans personal/individual → startup → small business → enterprise, sliced by team (Eng & Product, Design, Marketing, IT) and use case (Education, Personal, Professional). The competitive frame is implicitly the entire SaaS stack (Google Docs, Confluence, Asana, Slack search, plus standalone AI point tools), now reframed as one AI-native platform.

## Nav structure

```
- Product
  - Notion — Your AI workspace — /product
  - Notion Calendar — /product/calendar
  - Notion Mail — /product/mail
  - Notion AI — AI tools for work — /product/ai
  - Agents — Automate busywork — /product/agents
  - AI Meeting Notes — Perfectly written by AI — /product/ai-meeting-notes
  - Enterprise Search — Find answers instantly — /product/enterprise-search
  - Knowledge Base — Centralize your knowledge — /product/wikis
  - Docs — Simple and powerful — /product/docs
  - Projects — Manage any project — /product/projects
  - Connections — Connect your apps — /connections
  - Security — Safe and scalable — /security
- AI
  - AI features: Notion AI · Agents · AI Meeting Notes · Enterprise Search
  - Explore use cases: For work — /product/ai/use-cases?type=work · For life — ?type=life
- Solutions
  - Teams: Eng & Product — /product/notion-for-product-development · Design — /product/notion-for-design · Marketing · IT
  - Company size: Startups — /startups · Small businesses — /teams · Enterprise — /enterprise
  - Use Cases: Education — /product/notion-for-education · Personal — /personal · Professional — /use-case · AI use cases — /product/ai/use-cases
- Resources
  - Browse: Templates — /templates · Consultants — /explore-consultants · Connections — /connections
  - Discover: What's New — /releases · Customer stories — /customers · Blog — /blog · Webinars — /webinars
  - Learn: Developers — developers.notion.com · Academy — academy.notion.com · Product tours — /product/demos · Help — /help
- Developers — notion.dev
- Enterprise — /enterprise
- Pricing — /pricing
- Request a demo — /contact-sales
```

## Credibility & proof

- **Scale (self-reported, verbatim):** "Over 100M users worldwide," "1.4M+ community members."
- **Adoption claims (self-reported):** "Trusted by 98% of the Forbes Cloud 100," "62% of Fortune 100," "Over 50% of YC companies."
- **Analyst (self-reported, G2):** "#1 knowledge base 3 years running," "#1 AI enterprise search," "#1 rated AI writing."
- **Customer logos + named quotes:** OpenAI, Figma, Ramp, Cursor, Vercel, Nvidia, Volvo, L'Oréal, Discord, 1Password, Affirm, Riot Games, Toyota ("reduce timelines by 3x"), Match, Clay, Remote, Faire.
- **Press:** Forbes ($10B "AI everything app," 2024), Fast Company, TechCrunch, NYT, WSJ, The Verge.
- **Security/compliance (enterprise page):** SOC 2 Type 2, BSI C5, ISO 27001/27701/27017/27018, GDPR/CCPA/HIPAA, AES-256 at rest + TLS 1.2+ in transit, EU/US data residency, zero data retention for Enterprise.

## Visual & brand impression

Confident, polished, design-forward — the product the screenshots sell looks like the brand itself. The homepage opens on a **deep near-black navy** hero ("Meet the night shift") with a glowing circuit motif, then drops into a long scroll of **clean white "bento" cards** showing real product UI (agents, search, meeting notes, docs, calendar, mail). Type is Notion's signature Inter-family sans (a custom "NotionInter" cut); accents are a bright **Notion blue (#0075DE)**, with an **indigo (#455DD3)** turning up in AI-era gradients. The palette is essentially monochrome-plus-blue — restrained and modern, letting the colorful product screenshots and customer logos carry the energy. The brand mark is the instantly recognizable **N-sticker**; reads as a mature, category-leading SaaS brand mid-pivot to an AI-first story.

## Strategic read

The capture caught Notion mid-repositioning. The durable "all-in-one workspace" identity (still the spine of the About page's tools-and-history narrative) is now wrapped in an aggressive **AI/agents** front end — agents are the hero, AI is in the page title and every paid tier, and a new **credit-based usage layer** (Custom Agents, now live; Workers, Aug 11) sits on top of the per-seat model. That's a real business-model wrinkle: subscription remains primary, but Notion is grafting consumption pricing onto AI compute, and metering Custom Agents at "$10 per 1,000 credits" turns automation volume into a revenue lever. The "fewer tools" savings calculator shows the strategy plainly — Notion no longer pitches a doc tool but a **stack-replacement platform**, betting an AI-native single workspace out-competes a federation of point SaaS tools. Two standalone apps (Calendar, Mail) extend the surface area beyond the core canvas, and an MCP-based agent platform (Linear, Figma, HubSpot, Stripe, GitHub…) positions Notion as a hub other tools plug into.

## Provenance

- **Pages:** homepage, `/pricing`, `/product`, `/product/ai`, `/product/agents`, `/product/ai-meeting-notes`, `/product/enterprise-search`, `/product/calendar`, `/product/mail`, `/enterprise`, `/about` (11) — all Firecrawl, US geo, all-formats on homepage+pricing; `design_framework` from `rawHtml`, colors/fonts cross-checked vs screenshots.
- **Verify:** all HTTP 200, all 11 bodies md5-unique (clean — no geo/cache contamination).
- **Credits:** 13 (2 map calls + 11 scrapes); logos pass free (cached payload). 1025 remaining.
- **Couldn't get:** Docs/Wikis/Projects/Connections own pages not separately scraped (rostered from homepage + /product attestation); Templates/Consultants catalogs not enumerated; financials/headcount/founders (out of scope, deep-research).
- **Run profile:** guided — re-capture forced over a 4-day-warm 2.2 capture; +logos; +offerings (downloadable products + marketed features); heaviest scope.
- **Structured layer (2.5):** ran `fc.py signals` — no `application/ld+json` on the homepage, so `socials` seeded from footer anchors (verified), `external` empty (none declared); nav rebuilt from flattened mega-nav markdown + footer, validated vs the homepage screenshot.
