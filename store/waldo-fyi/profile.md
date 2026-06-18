---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: waldo.fyi
name: Waldo
aliases: []
legal_entity: ""                     # site states no legal name (footer is just "Copyright 2026 • All Rights Reserved"); no JSON-LD
parent: []
owns: []
socials: { linkedin: "https://www.linkedin.com/company/waldofyi", x: "https://x.com/waldofyi" }   # footer anchors (no JSON-LD sameAs); both resolve to Waldo
external: {}                         # no third-party records (crunchbase/wikipedia/etc.) surfaced on site

# Capture meta
captured_at: 2026-06-18
capture_method: firecrawl
site_notes: "Next.js on Vercel (metadata `next-size-adjust`, /_next/); tall animated SPA (~9,650px homepage). FIRECRAWL SCREENSHOTS FAIL on this site — fullPage 500s (SCRAPE_ALL_ENGINES_FAILED) and ANY screenshot+content combo 500s; content-only 200s. Capture with `fc.py scrape --shot none`; get visuals via Tier-B browser render (scripts/shoot.py renders it clean). Content scrapes also throw intermittent 500s — just retry. No JSON-LD on homepage. 'Products' mega-nav is client-rendered (only a <button> in <header>) — reconstruct the four products from the body. og:image misconfigured to http://localhost:3000/og.png (fetch-fails — no og logo slot). Pricing public on /pricing for Strategize/Pitch/Monitor; Build is platform-fee + waitlist."
key_pages:
  pricing: /pricing
  strategize: /strategize
  pitch: /pitch
  monitor: /monitor
  build: /build
  overview: /overview
  customer_stories: /customer-stories
  contact: /contact
unverified_fields:
  - "Pitch/Monitor pricing — both shown as 'As low as $249' with unspecified volume discounts; Build is a 'Platform fee, based on company size' (on-request). Exact figures not published."
  - "Headcount, revenue, funding, founding date, founders — not on the marketing site (deep-research job)."
  - "Internal inconsistencies: workflow count '+50' (/strategize) vs '100+' (FAQ); Pitch turnaround 'in an hour' (home/overview) vs 'in 2 hours' (/pitch, /monitor)."
  - "og:image is misconfigured to http://localhost:3000/og.png (production bug) — no working share card."
  - "Homepage client/agency logo wall read off the rendered screenshot (dentsu/Havas/Golin/ATTN: approximate); Crossmedia + PETERMAYER are text-confirmed via named case studies."

# Description — one sentence (~160-220 chars)
description: "An agentic brand-intelligence platform for agencies and brands: AI agents over a proprietary social, ads, audience, and trends data layer turn raw signals into strategy research, pitch playbooks, and intelligence briefs."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2B]
offering_category: [Software / SaaS]
portfolio_shape: Multi-product
business_model: Usage-based / Consumption   # STRAIN: credits ($49/100) + per-pitch + per-report + Build platform fee — "pay for what you use, volume discounts, no per-seat"; Monitor subscription optional
primary_industry: Technology         # a software/AI company serving the marketing & advertising vertical

# Visual identity — Firecrawl `branding` was unreliable here (see notes); confirmed against a Tier-B browser render
logo_url: assets/wordmark.svg        # canonicalized to the wordmark (2.5+)
logos:
  wordmark: { src: assets/wordmark.svg, w: 70, h: 18 }                                                            # inline data-URI SVG extracted from branding.images.logo (the "WALDO" mark, currentColor)
  logomark: { src: "https://www.google.com/s2/favicons?domain=waldo.fyi&sz=256", px: 256, transparent: false }    # magenta "W" on a baked near-black square (s2 == apple-icon, both 256)
  # og: omitted — TRUE absence: the declared og:image is http://localhost:3000/og.png and fetch-fails
brand_colors: { primary: "#D40A60", accent: "#080A0A" }   # STRAIN: magenta logomark + an iridescent pink→blue→green→orange gradient is the signature, on a near-black (#080A0A) canvas with #D2D3D3 light text/buttons; Firecrawl branding payload returned generic Google-blue (#1A73E8/#4285F4) defaults — discarded (§5.4)
fonts: [Inter]                       # branding.fonts + the rendered UI; the WALDO wordmark itself is a bespoke letterform
color_scheme: dark
design_framework: next.js            # rawHtml/metadata: `next-size-adjust`, /_next/ (Vercel-hosted)
---

## Overview

Waldo is an "agentic brand intelligence" platform purpose-built for marketing — sold to agencies (from "six-person shops to global holding company networks") and in-house brand teams. It pairs a proprietary, normalized data layer — live social across Instagram, TikTok, Reddit, X, YouTube, Meta/Facebook and LinkedIn, plus Meta/Google paid-ad libraries, GWI audience panels, a proprietary trends database, events, and the open web — with a fleet of "10,000+" AI agents trained by agency strategists, turning raw signal into sourced, presentation-ready strategy output. Four products span the agency workflow: **Strategize** (on-demand research + a chat "Strategy Agent"), **Pitch** (new-business playbooks), **Monitor** (recurring intelligence briefs), and **Build** (an API/MCP data layer). Waldo runs in its own web app, by email, or inside Claude/ChatGPT via a connector and MCP. It positions as the marketing-purpose-built alternative to generic LLMs and fragmented point tools, with every output source-linked ("with receipts"). Founders and founding date are not stated on the site.

## What they offer

Four products over one shared data layer + agent platform — Strategy Agent rides inside every product, and the proprietary data layer is the wedge. Per-SKU/tier detail in `offerings.md`.

- **Strategize:** Strategy Agent (AI strategist) + one-click research workflows (brand audits, four C's, audience profiles…), usable standalone or wired into Claude/ChatGPT — **"$49 / 100 credits"**, reload anytime `[published]`
- **Pitch:** a new-business pitch playbook in ~1–2 hours — go/no-go verdict ("Full Send / Toss-Up / Walk Away"), decoded brief, 3–4 ranked angles, "room intelligence," sourced proof points; +100 Strategize credits — **"As low as $249 / pitch"**, volume discounts, "No subscription required" `[partial]`
- **Monitor:** recurring interactive intelligence briefs across four scans (Brand / Trend / Audience / Category), delivered to inbox on any cadence, white-labelable, with Strategy Agent inside each — **"As low as $249 / report"**, volume discounts; buyable on-site or by subscription `[partial]`
- **Build:** a unified brand-intelligence API + MCP server (raw / aggregated / analyzed data across brand, audience, and category surfaces) for agents and teams — **"Platform fee, based on company size"** + credit-metered usage; in **early access (waitlist)** `[on-request]`

## How it works / model

Mixed self-serve + sales motion. Strategize (buy credits) and Pitch (buy a playbook at `/quick-pitch`, no subscription) are self-serve; Monitor can be bought as a single briefing on-site or as a recurring subscription (the pricing CTA is "Book a demo"); **Build** is waitlist/sales-gated (a platform fee scaled to company size plus usage credits). The pricing philosophy is consumption/credit-metered — "you pay for what you use, with volume discounts as you scale," no per-seat pricing (raw API endpoints ~1 credit/~20 results, analysis endpoints ~5 credits; activating an untracked brand/category/audience is an annual fee on top). Delivery is in-app, by email (Monitor), or inside Claude/ChatGPT via connector + MCP; work exports to PDF, Google Docs/Suite, MS365, Slack, and Teams. Data refreshes daily (24-hour cycle); enrichment/discovery endpoints hit platforms live (real-time). Customers own the IP they produce. Money: credits + per-unit purchases (pitch/report) + Build's platform fee.

## Positioning & audience

Targets marketing **agencies of every size** (independent shops to global holding-company networks) and in-house **brand teams**; named roles are strategists, new-business teams, account/strategy teams, and leadership/product. Deployed across financial services, healthcare, and B2B tech (claims category-adaptable agents). Claimed edge: AI **purpose-built for marketing** + proprietary data "generic AI can't access" + structured, source-linked rigor ("our agents don't freeform generate"). The recurring framing is augment-not-replace: Waldo "gives Claude and ChatGPT superpowers."

- **Tagline (hero):** "Agentic Brand Intelligence"
- **Meta description:** "The world's first AI that thinks about your brand while you sleep."
- **Closing line:** "See everything. Miss nothing. Move first."

## Nav structure

```
- Products (mega-flyout — client-rendered; reconstructed from body)
  - Strategize — /strategize        (Get started → /subscribe/strategize)
  - Pitch — /pitch                  (Get started → /quick-pitch)
  - Monitor — /monitor              (Book a demo → /contact)
  - Build — /build                  (Join waitlist → /build#get-key)
- Customer Stories — /customer-stories
- Pricing — /pricing
- (utility) Sign in — /start · Get started — /?product-select
- (footer) Terms — /tos · Privacy — /privacy · LinkedIn · X
```

## Credibility & proof

- **Security:** "SOC-2 Type II certified" (AICPA SOC 2 badge), repeated on every product page; "fully firewalled," "nothing you upload is ever used for model training," isolated per-workspace, custom enterprise contract terms.
- **Named case studies (verbatim):** **Crossmedia** — "1,000+ strategist hours reclaimed … across a 20-brand pitch"; **PETERMAYER** — "$30K saved in tool sprawl, plus 100+ hours reclaimed every month."
- **Client/agency logo wall (homepage, read off screenshot):** Crossmedia and PETERMAYER (text-confirmed) plus dentsu, Havas, Golin, ATTN: and others (approximate — visual only).
- **Testimonials (self-reported, verbatim):** Michelle Edelman (CEO & CSO, PETERMAYER); on `/pitch`: Michelle Gordon (Mike Worldwide/MWW), Tim Whirledge ("Ex-McCann, Droga5, BBDO"), Dennis Hahn (Liquid Agency). Several site-wide quotes carry generic attribution only — "Tracey Faux-Pattani, CEO" (no company; reads placeholder), Anita Schillhorn (Exec. Director of Strategy), Leah Swalling (Director of Brand Management).
- **Self-reported metrics (verbatim, unverified):** "10,000+ AI agents"; Strategize — "150hrs saved per strategist, per year," "$30K average tool savings," "85% reduction in research time"; Pitch — "$6K saved per pitch," "4 pitches pursued per month," "40hrs saved per pitch team"; Monitor — "20 hrs saved per week," "$30K saved per month," "80% [of users] report finding insights they'd have missed."
- **Trust mechanics:** every output "links directly to its source"; **GWI** named as "a data partner of ours."

## Visual & brand impression

Polished, premium dark AI-SaaS craft *(lightweight read — superseded by `visual.md` when the visual-evidence layer is present)*. A near-black canvas (#080A0A) carries a signature **iridescent aurora gradient** (magenta → blue → green → orange) on the hero orb and a giant footer "WALDO" wordmark; a magenta (#D40A60) "W" logomark and #D2D3D3 light text/buttons round out the palette, with Inter type throughout. Dark, rounded product-UI screenshots, an isometric data-layer illustration, and an agency logo wall reinforce a confident, high-end feel. One tell behind the polish: the og:image points at `localhost:3000` (a shipped production gap).

## Strategic read

The wedge is the **proprietary, normalized brand-data layer** (live social + ad libraries + GWI + trends), not the AI per se — the same "owned data is the moat" thesis as an AlphaSense, aimed at *marketing* rather than finance. The distribution bet is to meet strategists where they already work — Claude/ChatGPT via connector + MCP — rather than forcing yet another dashboard ("gives Claude/ChatGPT superpowers"). Pricing is deliberately consumption/credit-metered with no per-seat charge, so it can land in agencies of any size, and the four products ladder the agency lifecycle: win work (Pitch) → service & retain (Monitor, Strategize) → build proprietary capability (Build). Watch items signalling a young, fast-moving company: **Build is still early-access/waitlist**, and several production-polish gaps sit behind the slick design — the localhost og:image, a likely-placeholder "Tracey Faux-Pattani" testimonial, and the "+50" vs "100+" workflow-count discrepancy. Defensibility rests on keeping the data layer ahead as foundation models add native web/social access.

## Provenance

- **Pages:** 8 captured via Firecrawl (`maxAge:0`, `location:US`, `waitFor:3500`, `--shot none`) — homepage (all non-screenshot formats), pricing, strategize, pitch, monitor, build, overview, customer_stories; nav reconstructed from the body (the "Products" flyout is client-rendered).
- **Verify:** all 8 sourceURLs matched requested; all body md5s unique (no §5.1 geo/cache contamination); no junk soft-404s.
- **Credits:** 9 attributed (1 map + 8 scrapes, 1 credit each; `fc.py spend`). Failed fullPage/screenshot+content attempts 500'd at $0; ~5 more credits went to off-manifest diagnostic curls isolating the screenshot-500 root cause.
- **Couldn't get:** Firecrawl screenshots (engine fails on this SPA — visuals rendered via Tier-B browser instead); public figures for Pitch/Monitor volume discounts and Build's platform fee; headcount/revenue/funding/founders (not on site).
- **Run profile:** guided — express full pack: `+offerings` (deep), `+logos`, `+visual-evidence`. Non-vanilla capture mechanics: `fc.py --shot none` + a new `--shot {full|viewport|none}` flag (added this run) because Firecrawl fullPage/any-screenshot 500s on this SPA; homepage Tier-B rendered via `scripts/shoot.py`.
- **Structured layer (schema 2.6):** homepage carried no JSON-LD (`fc.py signals` — 0 blocks); `socials` filled from footer anchors (linkedin/x, both verified to Waldo); `legal_entity` empty (site states none); `external` empty. Branding payload colors were generic Google-blue defaults — discarded after a Tier-B render confirmed the true palette.
