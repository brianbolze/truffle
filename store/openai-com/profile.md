---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: 1

# Identity
domain: openai.com
name: OpenAI
aliases: [chatgpt.com]
parent: [openaifoundation.org]
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Next.js SPA. A plain curl HEAD 403s, but Firecrawl `basic` proxy + location:US scrapes clean (HTTP 200) — no geo/bot wall, no enhanced proxy needed. Pricing DOES land in markdown: /chatgpt/pricing/ is a long (~990-line) page whose plan cards ($0/$8/$20/$100) and full feature-comparison matrix all render server-side — grep '\\$' and 'Plan:' to read it. /about is a thin AGI-mission hub; the durable corporate facts (2015 founding, Oct-2025 recap, equity splits, board) live on /our-structure/. /sora/ now serves only a discontinuation FAQ (Sora wound down). Site map is a 472-URL firehose dominated by /index blog posts, /careers, and community.openai.com — use homepage links for product discovery. Separate domains: app=chatgpt.com, nonprofit=openaifoundation.org, docs=developers.openai.com."
key_pages:
  company: /about
  structure: /our-structure
  chatgpt: /chatgpt/overview
  chatgpt_pricing: /chatgpt/pricing
  business: /business
  api: /api
  api_pricing: /api/pricing
unverified_fields:
  - "ChatGPT Business & Enterprise dollar prices — page states they are 'priced per user per month' (monthly for Business; annual for Business & Enterprise) but shows no public number for those two tiers (contact-sales / quote)."
  - "Headcount, revenue, total funding raised, HQ address — not on the captured marketing pages (deep-research job). NB: the equity/valuation figures below are self-published on /our-structure/, not independently verified."

description: "An AI research-and-deployment company that builds frontier GPT models and ships them as ChatGPT, a developer API platform, and the Codex coding agent, under a stated mission to ensure AGI benefits all of humanity."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2C, B2B]
offering_category: [Software / SaaS]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Technology

# Visual identity
logo_url: https://openai.com/favicon.ico
brand_colors: { primary: "#000000", accent: "#005CC5", background: "#ffffff" }
fonts: [OpenAI Sans]
color_scheme: light
design_framework: next.js
---

## Overview
OpenAI is "an AI research and deployment company" whose mission is "to ensure that artificial general intelligence benefits all of humanity" [about]. It turns frontier research into a product portfolio: the consumer/prosumer assistant **ChatGPT**, a developer **API platform**, and the **Codex** coding agent, sold to consumers, developers, and businesses. The current flagship model is **GPT-5.5** [chatgpt_overview][chatgpt_pricing]. Governance is unusual — the nonprofit **OpenAI Foundation** controls the for-profit **OpenAI Group PBC** that operates openai.com [about][structure].

## What they offer
Several distinct, separately-positioned lines (Multi-product):

- **ChatGPT:** AI assistant for writing, coding, analysis, image generation, voice, web search, and "agent mode," on web/iOS/Android/Windows/macOS; "Now with GPT-5.5, our most capable and efficient frontier model for professional work" [chatgpt_overview].
- **API platform:** "Build leading AI products on OpenAI's platform" — GPT-5.5 / GPT-5.4 / GPT-5.4-mini, plus the Agents SDK, Responses API, and Realtime (voice) API; built-in tools (web search, file search, remote MCP) for agents [api].
- **Codex:** OpenAI's coding agent (CLI, IDE, and app), bundled into ChatGPT paid tiers and pushed hard for enterprise software teams [chatgpt_pricing][business].
- **ChatGPT Business / Enterprise:** workforce tier — "Unlimited chats and access to advanced models," workspace agents, app integrations (Google Drive, SharePoint, GitHub, Dropbox), "Enterprise-grade security, admin controls, SAML SSO, and compliance" [business].
- **Sora (being discontinued):** the video-generation product is winding down — "The Sora web and app experiences were discontinued on April 26, 2026. The Sora API will be discontinued on September 24, 2026" [sora].

## How it works / model
Primary motion is **subscription** on a **freemium funnel**, with per-user ChatGPT plans [chatgpt_pricing]:

- **Free:** **$0**
- **Go:** **$8 / month** — note: "This plan may include ads" (OpenAI is rolling out advertising; an Ads API exists at developers.openai.com/ads)
- **Plus:** **$20 / month**
- **Pro:** **from $100 / month** ("Pro reasoning with GPT-5.5 Pro," unlimited messages, 10–20× Codex usage)
- **Business / Enterprise:** "priced per user per month" — monthly plans for Go/Plus/Business; annual plans for Business/Enterprise (no public number for these two; see `unverified_fields`)

Alongside this, the **API platform** is a usage/consumption line ("GPT-5, GPT-5 mini, and GPT-5 nano now available at different price points") [business], and Enterprise is sales-assisted (`/contact-sales`). Delivery is fully digital across web, desktop, mobile, and API.

## Positioning & audience
The throughline is **"frontier models"** + the AGI mission, segmented by audience: consumers ("Get answers. Find inspiration. Be more productive."), developers ("Build leading AI products on OpenAI's platform"), and businesses ("Create, code, and innovate with OpenAI's tools and APIs… frontier AI" for "your entire workforce") [chatgpt_overview][api][business]. For enterprise the lead is capability + trust/compliance; proof points are named logos (Notion, Zendesk, Booking.com, Estée Lauder) — "The AI platform behind thousands of companies" [business].

## Nav structure
```
- Research — /research/
- Products
  - ChatGPT — /chatgpt/overview
  - Codex — (developers.openai.com/codex)
  - Pricing — /chatgpt/pricing , /api/pricing
- Business — /business
  - Customer stories — /business/customer-stories
- Developers (API Platform) — /api
- Company — /about
  - Our Structure — /our-structure
  - Charter — /charter
  - News — /news
  - Stories — /stories
  - Safety — /safety
  - Careers — /careers
- Foundation — https://openaifoundation.org/
- Try ChatGPT — https://chatgpt.com/
```

## Credibility & proof
- **Compliance:** "CCPA, CSA STAR, and SOC 2 Type 2 compliance, HIPAA compliance support" [business]; API adds "Business Associate Agreements (BAA) for HIPAA," "Data encryption at rest (AES-256) and in transit (TLS 1.2+)," IP allowlist/mTLS, SSO/MFA [api].
- **Data posture:** "No customer data or metadata in training pipeline for API, ChatGPT Business, or ChatGPT Enterprise customers" [business].
- **Customers:** Notion, Zendesk, Booking.com, Estée Lauder; "the AI platform behind thousands of companies" [business].
- **Distribution:** "At WWDC in June 2024, we announced a partnership with Apple to integrate ChatGPT into iOS, iPadOS, and macOS" [chatgpt_overview].

## Governance / structure
Self-published on `/our-structure/`:
- **Founded 2015 as a nonprofit; in 2019 created a for-profit subsidiary** governed/controlled by the nonprofit [structure].
- **Recapitalized 28 October 2025:** the nonprofit is now the **OpenAI Foundation**; the for-profit is now **OpenAI Group PBC**, a public benefit corporation [structure].
- **The OpenAI Foundation holds a 26% equity stake in OpenAI Group, "worth approximately $130B based on OpenAI Group's current valuation,"** plus a warrant for more equity if value rises >10× over 15 years [structure].
- **"Microsoft holds roughly 27% of OpenAI Group, and the remaining 47% is held by current and former employees and investors"** [structure].
- **Board (OpenAI Foundation):** Bret Taylor (Chair), Sam Altman (CEO), Adam D'Angelo, Sue Desmond-Hellmann, Zico Kolter, Paul M. Nakasone, Adebayo Ogunlesi, Nicole Seligman [structure].
- Recorded as `entity_type: Company` (the operating PBC) with `parent: openaifoundation.org` (the controlling nonprofit).

## Visual & brand impression
Stark, confident **monochrome** identity — black (`#000000`) on white (`#ffffff`), set in the proprietary **OpenAI Sans**, with blue (`#005CC5`) reserved for links. The homepage leads not with a marketing hero but with a live ChatGPT prompt box ("What can I help with?") cycling multilingual example prompts — foregrounding the product itself over copy. Minimalist, editorial, research-lab restraint; almost no decorative color. (Firecrawl's `branding.colors` flagged a light-grey `#C9D1D9` "primary," which is UI chrome — the real brand hue is the black confirmed in the screenshot.)

## Provenance
- **Pages:** homepage, /about, /our-structure, /chatgpt/overview, /chatgpt/pricing, /business, /api, /sora — all via Firecrawl (`basic` proxy, `location:US`), HTTP 200.
- **Verify:** all 8 pages `sourceURL` ✓ and md5-unique — no geo/cache contamination.
- **Credits:** 9 total (1 map + 1 homepage + 7 key pages). ~1417 remaining at run start (shared key).
- **Couldn't get:** Business/Enterprise dollar prices (quote-only); headcount, revenue, funding, HQ (not on captured pages). /api/pricing was in the inventory but not scraped this run (API $ live on developers.openai.com).
- `design_framework` from `rawHtml` (`/_next/` → Next.js); `logo_url` is the favicon (branding logo was an inline data-URI SVG).
