---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.2"

# Identity
domain: usertesting.com
name: UserTesting
aliases: []
parent: []
owns:                                # acquired/combined sub-brands — each keeps its own sign-in portal or co-branding on-site
  - userzoom.com
  - enjoyhq.com
  - userinterviews.com               # STRAIN: site shows "UserTesting plus User Interviews" / "Powered by User Interviews" integration; whether acquisition/merger/partnership isn't stated

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Drupal marketing site (/sites/default/files, /themes/custom/usertesting). Full mega-nav + footer DO render in markdown — no client-nav recovery needed. About-page stat counters are JS-animated and scrape as literal '0' (real numbers need the rendered page, not the markdown). Pricing is quote-only ('Request pricing') — no public dollar figures anywhere. Participant-count claim varies by page: 7M (homepage/network) vs 6M+ (AI page). Marketo forms, Qualified chat ('Tess'), Wistia/Arcade embeds present as markdown noise. No A/B tool fingerprinted."
key_pages:
  platform: /platform
  plans: /plans
  about: /company/about-us
  network: /platform/network
  ai: /platform/AI
  services: /services
  feedback_engine: /platform/feedback-engine
  analytics: /platform/analytics-visualizations
  amplify: /platform/amplify-insights
unverified_fields:
  - "Pricing — all editions are 'Request pricing' / annual sales quote; no public dollar amounts."
  - "Founding year, headcount, revenue, funding/ownership — not on captured pages (about-page numeric counters render as JS '0'; corporate parent not stated)."
  - "Relationship type to User Interviews / UserZoom / EnjoyHQ — site shows combined/integrated branding but never states acquisition vs merger vs partnership."

description: "An enterprise UX-research (\"human insight\") SaaS platform that recruits from a 7M+ participant network so product, design, marketing, and CX teams can test concepts and live experiences with real people and get AI-summarized video feedback in hours."

# Classification
entity_type: Company
target_market: [B2B]
offering_category: [Software / SaaS, Services / Consulting]
portfolio_shape: Flagship + companions
business_model: Subscription
primary_industry: Technology

# Visual identity
logo_url: https://www.usertesting.com/themes/custom/usertesting/logo.svg
brand_colors: { primary: "#315CFD", accent: "#0C163D" }   # vivid "UserTesting blue" CTAs over dark-navy text/bands — confirmed against screenshot; branding.colors.primary (#96A3B4 grey) is UI chrome, not the hue
fonts: [Proxima Nova, Cocogoose]      # Proxima Nova body; Cocogoose display/headings
color_scheme: light
design_framework: drupal              # rawHtml: /sites/default/files, /themes/custom/usertesting/, drupal-settings (branding.designSystem not trusted)
---

## Overview

UserTesting is an enterprise "human insight" platform — UX/experience research software paired with a large on-demand participant network. Product, design, marketing, UX-research, product-management, and CX teams use it to put concepts, prototypes, and live experiences in front of real people and get back first-person video, transcripts, and AI-synthesized themes "in hours, not weeks." The pitch is wrapped in an AI-era narrative: "When AI can build anything, knowing what to build is everything" — i.e. creation got cheap, so knowing what's worth building is the new bottleneck. Headquartered in Bellevue, Washington; remote-first with collaboration spaces in ~12 cities worldwide (SF Bay Area, London, Manchester, Edinburgh, Barcelona, Paris, Denver, NYC, Singapore, Atlanta, Berlin, Sydney). Serves 3,000+ customers including **75 of the Fortune 100**.

## What they offer

One flagship platform (the "human insight engine") sold in editions, plus a professional-services arm and a recruitment network as companions. Pricing is quote-only — no public dollars.

- **The platform — four pillars:** marketed as **Target** (audience/recruiting → `/platform/network`), **Gather** (testing/"Feedback Engine" → `/platform/feedback-engine`), **Analyze** (analytics & visualizations → `/platform/analytics-visualizations`), and **Amplify** (share/scale insights → `/platform/amplify-insights`).
- **Test types:** unmoderated (surveys, interaction tests, think-out-loud), **moderated "Live Conversation,"** card sorting & tree testing, interactive path flows & click maps, sentiment analysis, transcripts.
- **UserTesting AI:** AI-generated test creation, AI-powered analysis/insight summaries, smart tags, Insights Hub + "AI-powered Insight Discovery"; positioned as "transparent, inspectable, linked back to evidence."
- **Insights Hub:** repository for storing/searching past research (the acquired EnjoyHQ lineage).
- **Embedded / in-workflow:** UserTesting for **Figma** plugin, an **MCP Server** ("recruit, test, and validate from supported AI workflows"), and integrations with **Slack, Teams, Jira, Figma, FigJam, Miro**.
- **Professional Services (companion):** **Consulting Services**, **Insights Services** (done-for-you / full-service research delivery), **Audience Services** (hard-to-reach recruiting), **Support Services**; **QXscore** — a proprietary experience-measurement methodology. "Over 200 years of cumulative UX expertise."
- **Editions:** **Advanced** (entry), **Ultimate** ("popular"; adds AI test creation/analysis, Insights Hub, card sort/tree test, custom audiences), **Ultimate+** (adds Team-based Unlimited, Figma plugin, custom insights services, Premier Support+).

## How it works / model

Customer journey: **Ask** any question → **Learn** from real people in the network → **Act** on insight at scale. A team defines an audience and test, the network supplies vetted participants ("80% of sessions in just a few hours"), sessions are captured as video, and AI surfaces themes/summaries for sharing. Monetization is **annual subscription**, on one of two plan structures:

- **Test-based Consumption:** pay by test usage; unlimited users (no per-seat charges); best for variable needs.
- **Team-based Unlimited:** unlimited tests within a defined enterprise scope; predictable pricing for scaling across teams/geographies.

The **participant network is the moat** ("the network advantage no one else can replicate") — and User Interviews now powers the recruiting/"Target" half of it (recruit in User Interviews, run studies in UserTesting).

## Positioning & audience

Targets **enterprise** experience/research teams (Product, Design, UX Research, Marketing, CX, Digital). Positions as **the** end-to-end, enterprise-grade human-insight platform — leaning on scale (75 of Fortune 100), network quality ("lowest participant fraud rate in the industry," every participant vetted), speed ("hours, not weeks"), and ROI ("415% ROI over three years," Forrester TEI). Tagline: **"Human understanding. Human experiences."** Differentiates against lighter "wellness"-grade feedback tools and DIY panels on rigor + breadth + white-glove services.

## Nav structure

```
- Platform & Services
  - Platform
    - Platform overview — /platform
    - Target (Reach the right audience) — /platform/network
    - Gather (Comprehensive testing capabilities) — /platform/feedback-engine
    - Analyze (Identify insights and measure performance) — /platform/analytics-visualizations
    - Amplify (Share and scale insights) — /platform/amplify-insights
    - Pricing Plans — /plans
  - Services
    - Services overview — /services
    - Consulting Services — /services/consulting
    - Audience Services — /services/audience
    - Insights Services — /services/insights
    - Support Services — /services/support
  - Popular features
    - MCP Server — /platform/mcp-server
    - Advanced Targeting — /usertesting-user-interviews-better-together
    - Embedded Insights (UserTesting for Figma plugin) — /solutions/teams/product-design/Figma
    - UserTesting AI — /platform/AI
    - Insights Hub — /insights-hub
    - Integrations — /solutions/integrations
    - Templates — /resources/templates
- Solutions
  - Use cases
    - AI experiences — /solutions/use-cases/ai-products-best-practices
    - Audience insights — /solutions/use-cases/audience-insights
    - Mobile testing — /solutions/use-cases/mobile-testing
    - Pricing & packaging — /solutions/use-cases/pricing-and-packaging
    - Usability testing — /solutions/use-cases/usability-and-digital-experience-testing
    - See other use cases — /solutions/use-cases
  - Teams
    - Customer experience — /solutions/teams/customer-experience
    - Design — /solutions/teams/design
    - Digital experience — /solutions/teams/digital-experience
    - Marketing — /solutions/teams/marketing
    - Product management — /solutions/teams/product-management
    - UX research — /solutions/teams/ux-research
  - Industries
    - Retail — /solutions/industry/retail
    - High-tech — /solutions/industry/consumer-technology
    - Fin-serv — /solutions/industry/financial-services
    - Media & entertainment — /solutions/industry/media-entertainment
    - Healthcare — /solutions/industry/hospitals-and-healthcare-systems
    - Travel & hospitality — /solutions/industry/travel-hospitality
- Customers
  - View all customer stories — /resources/customers
  - Ratings & Reviews — /resources/customers/ratings-reviews
  - Featured: Burberry, Costa Coffee, Panera Bread, Canva, Adobe
  - UserTesting University — /learn · CommUnity — community.usertesting.com
- Company
  - About us — /company/about-us
  - Careers — /company/careers
  - Newsroom — /company/newsroom
  - Partners — /partners
  - Executive team — /company/about-us/executive-team
  - Charitable giving — /company/programs-initiatives/charitable-giving
  - Education partner program — /education-partner-program
  - Insights for Impact — /company/insights-impact
- Resources
  - All resources / Insight+ / Blog / Guides / Industry Reports / Podcast / Templates / Webinars
  - Events: Crafted (events.usertesting.com/crafted)
  - Product Releases — /resources/product-releases
- Utility: Get Paid to Test — /get-paid-to-test  ·  Contact Us — /contact-us  ·  Sign in (UserTesting / UserZoom / EnjoyHQ / Participant)
```

## Credibility & proof

- **Logo wall:** Walmart, Microsoft, Zendesk, Canva, Subway, GoDaddy, HelloFresh, ATB Financial, Alaska Airlines, AWS/Amazon, Ancestry, HP, Adobe, Philips, AAA, Burberry, Panera, Costa Coffee.
- **Scale claims (verbatim):** "TRUSTED BY 75 OF THE FORTUNE 100"; "3,000+ enterprise customers in 40+ countries"; "7M+ authenticated participants across 34 countries" (homepage/network) — note the AI page says "6M+ participants" and Plans says "60+ countries."
- **Network quality:** "Lowest participant fraud rate in the industry"; "80% of sessions in just a few hours"; "Every participant is vetted."
- **Analyst / awards:** "Forrester names UserTesting a Leader in the Experience Research Platforms Wave"; Forrester TEI "415% ROI"; "Rated #1 by G2"; TrustRadius Buyer's Choice / Top Rated; G2 Leader (Enterprise/Mid-Market) across many quarters; Proddy "Top UX Research Product."
- **Self-reported rating:** **"4.25 / 5"** across **1,034 reviews** (homepage `AggregateRating`, also shown on the page; self-reported).
- **Security/compliance:** SOC2, ISO 27001, GDPR, HIPAA, CSA.
- **Guarantee/trial:** free single test ("a video of a real person reviewing your website, typically in less than an hour"); Education Partner Program (free for qualifying institutions); OneWorld program (free/discounted for nonprofits).

## Visual & brand impression

Polished, confident enterprise-B2B design. Light scheme, generous whitespace, a vivid cobalt **#315CFD** ("UserTesting blue") carrying every CTA, set against deep-navy **#0C163D** text and full-bleed dark section bands. Multi-color flat illustrations and rounded product screenshots (teal/yellow/orange accent cards) keep it warm rather than corporate-cold. Display headings in **Cocogoose** (geometric, friendly-bold) over **Proxima Nova** body. Heavy use of customer logos, analyst badges, and short autoplay video — the visual language of a category leader selling trust at enterprise scale.

## Strategic read

UserTesting is consolidating the experience-research category by absorption: the captured site co-brands or hosts sign-in for **UserZoom** (manager.userzoom.com), **EnjoyHQ** (app.enjoyhq.com, now "Insights Hub"), and most recently **User Interviews** ("UserTesting plus User Interviews" / "Powered by User Interviews"), which now powers the recruiting/"Target" pillar. The participant network — not the software — is framed as the un-replicable moat. The whole 2026 message is re-platformed around AI ("knowing what to build is the new bottleneck"; AI test creation + insight summaries + an MCP server + a Figma plugin) while explicitly hedging on trust ("responsible AI," "grounded in real human feedback," AI used to *detect* fraud) — selling AI speed without conceding the human-insight premise the brand is built on.

## Provenance

- **Pages:** 7 captured & analyzed via Firecrawl (markdown + full-page screenshot; homepage also html/rawHtml/links/branding) — homepage, /platform, /plans, /company/about-us, /platform/network, /platform/AI, /services. Map returned 496 URLs (heavily /author + /blog noise); key pages picked from homepage mega-nav links.
- **Verify:** all 7 sourceURLs matched; all 7 body md5s unique — no §5.1 geo/cache contamination.
- **Credits:** 8 (1 map + 7 scrapes, all basic proxy, 1cr each).
- **Couldn't get:** public pricing (quote-only); founding year / headcount / revenue / corporate owner (not on captured pages — about-page stat counters are JS-animated and scrape as "0"); exact nature of the UserZoom/EnjoyHQ/User Interviews relationships (co-branded on-site but type not stated).
- **Structured layer (schema 2.2):** read this capture's homepage JSON-LD via `fc.py signals` ($0 re-enrichment from the persisted 2026-05-31 rawHtml, hint-to-verify) — JSON-LD has no `sameAs`; its self-reported `AggregateRating` (4.25/5, 1,034 reviews) → Credibility (verbatim, flagged self-reported); `logo_url` already matched the JSON-LD `logo`. Re-stamped 2.0→2.2.
