---
schema_version: 1

# Identity
domain: dovetail.com
name: Dovetail
aliases: ["Dovetail Research Pty. Ltd."]   # Australian legal entity (footer ©)
parent: []
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Gatsby SSG (___gatsby + /page-data/ in rawHtml); branding.designSystem reports 'custom' (wrong, per the corpus rule). Dark theme. Mega-nav (Product/Solutions/Resources/Company flyouts) renders fully in homepage markdown — no client-rendered-nav recovery needed. Pricing is TWO tiers only: Free ($0) and Enterprise (custom, USD-only, invoiced) — no public mid-tier price; seat-based ('user/month'). Customers page is heavy (~127k md, logo wall + story cards). Docs live off-domain: docs.dovetail.com (help/academy), developers.dovetail.com (API), trust.dovetail.com (trust center)."
key_pages:
  pricing: /pricing/
  enterprise: /enterprise/
  ai_analysis: /product/ai-analysis/
  voice_of_customer: /solutions/voice-of-customer/
  customers: /customers/
  research_role: /roles/research/
  integrations: https://docs.dovetail.com/integrations/
unverified_fields:
  - "Exact paid price — only Free ($0) and Enterprise (custom, contact-sales) are public; no per-seat dollar figure shown."
  - "Headcount, funding, revenue — not on the marketing site (deep-research job)."

description: "An AI-native customer intelligence platform that unifies calls, support tickets, surveys, and research into one searchable source, using AI to surface trends, themes, and answers for product, research, CX, and go-to-market teams."

# Classification
entity_type: Company
target_market: [B2B]
offering_category: [Software / SaaS]
portfolio_shape: Single
business_model: Subscription
primary_industry: Technology

# Visual identity
logo_url: https://dovetail.com/favicon.ico   # branding.images.logo is an inline data-URI SVG mark → favicon fallback
brand_colors: { primary: "#0044FF", accent: "#0FCCCE" }   # electric blue hero/brand hue + teal secondary; verified dark against screenshot
fonts: [Inter, Roboto, JetBrains Mono]   # heading / body / mono
color_scheme: dark
design_framework: gatsby
---

## Overview

Dovetail is a B2B SaaS "Customer Intelligence Platform." It ingests every customer signal an
organization generates — sales calls, support tickets, NPS, reviews, research interviews, surveys,
documents — into one searchable repository, then uses AI to classify, summarize, and surface trends
so any team can act on them. The pitch is org-wide: what began as a research-repository / qualitative-
analysis tool is now positioned as the single intelligence layer feeding product, design, research,
customer experience, sales/CS, and marketing. Tagline: **"Build with facts, not vibes."**

## What they offer

One platform, sold as a stack of AI surfaces (not separately-purchased products):

- **AI Analysis:** *Channels* (auto-classify high-volume tickets/reviews/feedback in real time, trend
  digests) and *Projects* (research-grade investigation of calls, docs, surveys → summaries, reports, reels).
- **AI Chat & Search:** semantic/keyword + RAG search; chat with your data, including via Slack/Teams (`@Dovetail`).
- **AI Dashboards (Beta):** turn qualitative data into quantitative charts / sentiment over time.
- **AI Docs (Beta):** shareable outputs combining structured insights with customer clips.
- **AI Agents (Beta):** autonomous monitoring, doc generation, and risk/opportunity alerts.
- **API & integrations:** 38 native integrations, open API, CLI, and an **MCP server** (connects to Claude, ChatGPT, Copilot).

## How it works / model

Product-led growth into enterprise. **Free** ($0, no card) gives an individual one channel + one
project + basic chat/summaries. **Enterprise** (custom pricing, contact-sales, invoiced) unlocks
unlimited agents/channels/projects/docs, org governance (global tags, fields, templates), advanced
AI, security/compliance, and dedicated success. Pricing is **seat-based** ("user/month"), **USD only**,
tax-exclusive; no public mid-tier dollar figure. Money is recurring subscription; the free tier is the
acquisition wedge. AI runs on **AWS Bedrock** in a private environment (data never trains models).

## Positioning & audience

Targets product-and-customer teams at large enterprises — explicitly organized by **role**
(Design, Product Management, Research, Customer Experience, Sales & CS, Marketing) and **use case**
(Voice of Customer, Product Research, Research Repository). Claimed edge: AI grounded in evidence —
"every AI-generated insight links back to its source. No black-box answers." ROI claims (Forrester
TEI): **2.3x ROI**, **30hrs/week saved per user**, **66% faster shipping**, **30% team-capacity increase**.
Maintains head-to-head comparison pages vs. Condens, Looppanel, and Marvin (the research-repository competitive set).

## Nav structure

```
- Product
  - Platform overview
  - AI Analysis — /product/ai-analysis/
  - AI Chat and search — /product/ai-chat-and-search/
  - API and integrations — https://docs.dovetail.com/integrations/
  - AI Dashboards (Beta) — /product/ai-dashboards/
  - AI Docs (Beta) — /product/ai-docs/
  - AI Agents (Beta) — /product/ai-agents/
- Solutions
  - Roles
    - Design — /roles/design/
    - Product Management — /roles/product-management/
    - Research — /roles/research/
    - Customer Experience — /roles/customer-experience/
    - Sales & Customer Success — /roles/sales-and-cs/
    - Marketing — /roles/marketing/
  - Use cases
    - Voice of Customer — /solutions/voice-of-customer/
    - Product Research — /solutions/product-research/
    - Research Repository — /solutions/research-repository/
- Resources
  - Blog — /blog/   · Live demos — /live-demos/   · Outlier — /outlier/
  - Help center — docs.dovetail.com/help/   · Academy — docs.dovetail.com/academy/   · Changelog — /changelog/
  - ROI calculator — /roi-calculator/   · Podcast (B2B SaaSy) — /b2bsaasy/
- Company
  - Events — /events/   · Careers — /careers/   · Trust center — trust.dovetail.com
- Enterprise — /enterprise/
- Customers — /customers/
- Pricing — /pricing/
- Log in / Go to app — /start/   · Contact sales — /contact-sales/
```

## Credibility & proof

Large enterprise logo wall, repeated across pages: Mercedes-Benz, Qantas, AWS, Toyota, Canva, Volvo,
Notion, Salesforce, Milwaukee, Visa, KPMG, Wise, McKinsey & Company, Ford, Walgreens, Shopify, Breville,
Atlassian, Okta, NCR Voyix, ASML, Zapier, Airwallex, Itaú Unibanco. Named customer stories (Breville,
Atlassian, Canva, Qantas, Itaú Unibanco). Ratings: **4.5/5 G2**, **4.6/5 Capterra**. Compliance is a
headline trust signal: **SOC 2 Type II**, **ISO 27001**, **ISO/IEC 42001:2023** (AI management standard),
**HIPAA** (paid add-on), **GDPR**; SSO, audit logs, automatic PII redaction, custom data retention.
Third-party validation via a **Forrester Total Economic Impact™** study.

## Visual & brand impression

Confident, modern dev-tool aesthetic: a near-black (`#0A0A0A`) canvas with electric-blue (`#0044FF`)
and teal (`#0FCCCE`) accents, Inter headings over a Roboto body with JetBrains Mono flourishes — the
mono and the "facts, not vibes" line lean engineering-credible. Dense, screenshot-rich scrolling page
with numbered narrative sections (Centralize → Analyze → Query → Act) and animated product imagery.
Reads as a mature, well-funded category leader repositioning from "research tool" to "enterprise AI
intelligence platform."

## Strategic read

The capture catches a deliberate category move: Dovetail no longer sells itself as a UX-research
repository but as the **org-wide "Customer Intelligence Platform"** — every signal, every team. Two
tells reinforce it: (1) pricing collapsed to **Free + Enterprise** only, dropping public self-serve
mid-tiers in favor of a PLG-into-enterprise motion; (2) the entire surface is **AI-native** (Analysis,
Chat, Dashboards, Docs, Agents) with an MCP server and AWS Bedrock private inference — betting that
"AI grounded in cited evidence" is the wedge against both legacy research tools and general-purpose LLMs.

## Provenance

- **Pages:** homepage (rich pass — markdown/html/rawHtml/links/branding/screenshot), /pricing/, /enterprise/, /product/ai-analysis/, /solutions/voice-of-customer/, /customers/ (6) — Firecrawl, `maxAge:0`, `location:US`, `waitFor`; `design_framework` from rawHtml (Gatsby).
- **Verify:** all sourceURL-matched, all bodies md5-unique (clean; no geo/cache contamination).
- **Credits:** not recorded this run.
- **Couldn't get:** per-seat dollar pricing (Enterprise is contact-sales only); firmographics — headcount/funding/revenue not on the marketing site (off-site, deep-research job).
