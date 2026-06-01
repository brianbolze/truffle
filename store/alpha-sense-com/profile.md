---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: 1

# Identity
domain: alpha-sense.com
name: AlphaSense
aliases: []
parent: []
owns: ["Tegus", "Sentieo", "BamSEC", "Canalyst"]   # STRAIN: acquired companies folded into the platform (about page) — names, not domain-joined (domains now redirect)

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Next.js (/_next/image) + Sanity CMS (cdn.sanity.io) for all imagery; blog subtree carries a wp-content marker but the marketing site is Next.js. Full mega-nav renders in markdown — no client-nav recovery needed. Pricing is sales-gated (Marketo form, no public price). A/B: Mutiny — Mutiny personalization (cdn.mutinyhq.io) + a Qualified 'Alphred' chatbot leak into the markdown as noise and may vary hero/CTA copy run-to-run. Map returned 472 URLs (heavy /earnings/<ticker>, /blog, /compare, /resources funnel noise); product catalog came from homepage links."
key_pages:
  platform: /platform/
  pricing: /pricing/
  about: /about/
  why_alphasense: /why-alphasense/
  expert_insights: /platform/expert-insights/
  solutions: /solutions/
  security: /security/
  compare: /compare/
unverified_fields:
  - "Pricing — sales-gated quote only; site states annual subscriptions, per-seat to enterprise-wide, but no dollar figures are public."
  - "Headcount, revenue, funding/valuation — not on the marketing site (deep-research job)."
  - "Hero/CTA copy is a point-in-time snapshot, not fixed — Mutiny personalization on the site."

description: "An AI-powered market-intelligence platform that surfaces insights across 500M+ premium documents — filings, broker research, news, and expert transcripts — plus a firm's own internal content, for enterprises and financial institutions."

# Classification
entity_type: Company
target_market: [B2B]
offering_category: [Software / SaaS, Services / Consulting]
portfolio_shape: Flagship + companions
business_model: Subscription
primary_industry: Technology

# Visual identity
logo_url: https://cdn.sanity.io/images/ewv2vq7j/production/33be7939d26d9ad17d653bfbbadfdd0736539333-133x23.svg
brand_colors: { primary: "#0040FF", accent: "#FFFF52" }   # STRAIN: electric blue is the dominant brand hue (screenshot-confirmed); yellow is a sparing secondary
fonts: [ES Klarheit Kurrent, Inter]
color_scheme: light
design_framework: next.js
---

## Overview

AlphaSense is an AI-powered market-intelligence and search platform for enterprises and financial institutions. It indexes a curated library of 500M+ premium business documents — SEC and global filings, earnings transcripts, broker/equity research from 1,000+ firms, news, regulatory content, and proprietary expert-call transcripts — and layers purpose-built generative AI (Generative Search, Deep Research agents, monitoring) on top so analysts can extract cited, auditable answers in seconds. Customers can also fold in their own internal content (Enterprise Intelligence). Founded 2011 by ex-banker Jack Kokko after the "CTRL+F across thousands of PDFs" research grind; positioned as the trusted, no-hallucination alternative to generic AI search and fragmented point tools.

## What they offer

One integrated platform (the flagship) sold as two packages plus content/service companions and add-ons — all subscription, pricing sales-gated:

- **Market Intelligence:** core package — GenAI workflows over the curated external library (research, broker content, expert transcripts, news, regulatory, financial data), 24/7 support, ETL integration
- **Enterprise Intelligence:** everything in Market Intelligence + AI search/summarization over the firm's *internal* content, private-cloud hosting for confidential data, API/third-party uploads, custom training & IT support
- **Tegus Expert Insights (companion):** the expert-network line — Expert Transcript Library (250,000+ investor-led transcripts, 8K+ added monthly across 29K+ companies; Channel Checks, Voice of Customer) plus bespoke Expert Calls (AI-Led via an AI Interviewer, or Human-Led), "savings of up to 70% over traditional expert networks"
- **Financial Data (companion):** screening, industry comparables, M&A/funding/valuation metrics, Excel integration, pre-built models
- **Expert calls (add-on):** on-demand access to a network of "one million pre-qualified experts," with a dedicated compliance portal
- **Canalyst financial models (add-on):** AI-generated, auditable financial models with industry-specific KPIs and non-GAAP metrics, Excel tooling

Platform modules surfaced on `/platform/`: **Generative Search** (multi-agent reasoning across qualitative + structured + internal data), **Deep Research** (autonomous agent that "compresses weeks of analysis into minutes"), **Monitoring** (dashboards, alerts, mobile app), **Enterprise Intelligence**, **Financial Data**, and **Workflow Agents** (custom/scheduled agents). A developer API exists (`developer.alpha-sense.com`).

## How it works / model

B2B SaaS sold by sales motion — there is no self-serve checkout; the path is "Get Started for Free" / free trial → sales contact → annual subscription, priced per-seat for small teams up to enterprise-wide deals. Add-ons (Expert calls, Canalyst models) and the Enterprise Intelligence tier expand the contract. Revenue is recurring subscription; the moat is the proprietary, hard-to-replicate content set (esp. Tegus expert transcripts and broker research) combined with the AI layer over it.

## Positioning & audience

Targets knowledge professionals at the world's largest enterprises and financial firms — investment banking, hedge funds, private equity, asset management, VC on the buy/sell side; and corporate strategy, competitive intelligence, corporate development, and IR teams in life sciences, TMT, energy, industrials, consumer/retail, consulting, law firms, and insurance. Claimed edge: the broadest *curated* premium content set in one place + "purpose-built" AI that "thinks like an analyst" and delivers **sentence-level citations and no hallucinations** — explicitly contrasted against generic search tools and fragmented workflows.

- **Tagline (homepage):** "Accelerate your workflow with AI insights you can trust"
- **Tagline (why-alphasense):** "Every insight. One platform. Zero blind spots."

## Nav structure

```
- Platform — /platform/
  - The AlphaSense Platform — /platform/
  - Financial Data — /platform/financial-data/
  - Content & Partners — /content-and-partners/
  - Enterprise Intelligence — /platform/enterprise/
  - Tegus Expert Insights — /platform/expert-insights/
  - Tegus Expert Call Services — /platform/expert-insights/expert-call-services/
  - Why AlphaSense — /why-alphasense/
  - How AlphaSense Compares — /compare/
  - Security — /security/
- Solutions — /solutions/
  - Financial Services:
    - Investment Banking — /solutions/financial-services/investment-and-corporate-banking/
    - Hedge Funds — /solutions/financial-services/hedge-funds/
    - Private Equity — /solutions/financial-services/private-equity/
    - Asset Management — /solutions/financial-services/asset-management/
    - Venture Capital — /industries/venture-capital/
  - Corporations:
    - Life Sciences & Healthcare — /industries/life-sciences/
    - Tech, Media & Telecom — /industries/tech-media-telecom/
    - Energy — /industries/energy/
    - Industrials — /industries/industrials/
    - Consumer Goods & Retail — /industries/consumer-cpg/
  - Consulting & Professional Services:
    - Consulting — /industries/consulting/
    - Law Firms — /industries/law-firms/
    - Insurance — /industries/insurance/
- Resources — /resources/
  - Research & Insights — /resources/?types=product-articles,research-articles,reports
  - Case Studies — /resources/?types=case-studies
  - Events & Webinars — /resources/?types=events,webinars
  - Sentiment Indexes — /sentiment-index/
- About — /about/
  - About AlphaSense — /about/
  - Newsroom — /newsroom/
  - Careers — /careers/
  - Contact Us — /contact/
- Pricing — /pricing/
- (utility) Log In — research.alpha-sense.com · Customer Support — help.alpha-sense.com · Developer Portal — developer.alpha-sense.com · Trust Center — trust.alpha-sense.com
```

## Credibility & proof

- **Customers:** "Trusted by 6,500+ of the world's largest enterprises" (FAQ says "over 6,000"); **85% of the S&P 100** and **70% of the top 50 hedge funds**
- **Named logos:** Pfizer, Microsoft, J.P. Morgan, McKesson, Salesforce, Dow, Goldman Sachs, Cisco, Siemens, UBS, Deloitte, Baillie Gifford, ODDO BHF
- **Analyst recognition:** Leader in the **2026 Gartner® Magic Quadrant™ for Competitive & Market Intelligence Platforms** (positioned highest on Ability to Execute, furthest on Completeness of Vision per its own claim)
- **Awards:** Fast Company Most Innovative Companies 2026, Forbes Cloud 100 2025, CNBC Disruptor 50 2025
- **Content scale:** 500M+ premium documents; 10,000+ curated data sources; 200K+/250K+ expert transcripts across 29K+ companies; filings from 1.4M+ companies; 1M+ pre-qualified experts
- **Proof points:** customer quote (Salesforce VP of Competitive Intelligence: a benchmark that "would have taken us multiple days … now we can find the answer within 10 minutes"); case studies (Salesforce, Dow, ODDO BHF, YH2 Capital, Recurve Capital, Royalty Pharma); a Trust Center (trust.alpha-sense.com) and dedicated Security pages

## Visual & brand impression

Polished, mature enterprise-B2B SaaS aesthetic. Light background dominated by a single bold electric blue (#0040FF) used for the hero, CTAs, and product imagery, with crisp dark text (#1D1D1D) and a sparing bright-yellow secondary (#FFFF52). Clean grid, generous whitespace, abstract data/AI motifs and product-UI screenshots, and embedded Cloudflare Stream video thumbnails. Display type reads as a confident geometric sans (ES Klarheit Kurrent) over Inter body. Tone is professional, authoritative, and "trust"-forward — consistent with selling six-figure intelligence subscriptions to financial and corporate decision-makers.

## Strategic read

AlphaSense's durable advantage is **owned content, not the AI**: it has rolled up the category through acquisition — Tegus (expert transcripts/calls), Sentieo (modeling & search), BamSEC (SEC filings), Canalyst (financial models) — so the GenAI layer reasons over a corpus competitors can't legally or practically replicate, which is exactly the "no hallucination, sentence-level citation" pitch that lets it sell into compliance-sensitive finance. The 2026 strategic thrust is agentic: a "next generation" multi-agent Generative Search, autonomous Deep Research, and customer-deployable Workflow Agents that push from "search tool" toward "automate the whole research process, discovery to deliverable." The 2025 Cerebras partnership (inference speed) and a Due Diligence Workspace launch reinforce the speed-and-depth story. Watch item: as foundation-model "deep research" commoditizes the reasoning layer, AlphaSense's bet is that proprietary content + compliance + workflow integration is the defensible moat.

## Provenance

- **Pages:** 6 captured via Firecrawl (`maxAge:0`, `location:US`, `waitFor:3500`) — homepage (all-formats), platform, pricing, about, why-alphasense, expert-insights; nav reconstructed from homepage mega-menu + map (472 URLs).
- **Verify:** all 6 sourceURLs matched requested; all body md5s unique (no §5.1 geo/cache contamination).
- **Credits:** 7 (1 map + 6 scrapes; all basic proxy, 1 credit each).
- **Couldn't get:** public pricing (sales-gated Marketo form); headcount/revenue/funding (not on site); acquired-brand domains not verified to resolve (recorded as names in `owns`).
