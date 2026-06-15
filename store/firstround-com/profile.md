---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: firstround.com
name: First Round
aliases: [First Round Capital]
legal_entity: ""                     # site doesn't state a registered legal name (footer is "First Round 2026 ©"); no JSON-LD legalName
parent: []
owns: []
socials:
  linkedin: https://www.linkedin.com/company/first-round-capital
  x: https://x.com/firstround
  youtube: https://www.youtube.com/@FirstRoundCapital
  instagram: https://www.instagram.com/firstroundcapital
external: {}                         # no JSON-LD sameAs on homepage; no third-party records surfaced on captured pages

# Capture meta
captured_at: 2026-06-14
capture_method: firecrawl
site_notes: "Next.js on Vercel; content via Sanity CMS (cdn.sanity.io). No JSON-LD on homepage. Flat top-nav, no mega-menu. 'The Review' (their content publication) lives on the review.firstround.com subdomain; careers on jobs.firstround.com (Ashby). /companies and /team are client-rendered filterable grids — a scrape captures the loaded/featured subset, NOT the full 500+ portfolio or full team roster. Homepage hero is seasonal/rotating (a Mother's Day 'imagine if' variant was live at capture)."
key_pages:
  how_we_work: /how-we-work
  who_we_back: /who-we-back
  companies: /companies
  team: /team
  pmf_method: /pmf
  angel_track: /angel-track
  manifesto: /news/manifesto
  the_review: https://review.firstround.com/
unverified_fields:
  - "Portfolio list is a featured SAMPLE from the client-rendered /companies grid — not the full roster (the site cites '500+ companies' / '500+ early teams')."
  - "Homepage hero is seasonal/rotating (a Mother's Day 'imagine if' variant captured) — point-in-time snapshot, not fixed."
  - "Fund size / fund number / AUM and fee–carry economics not stated on captured marketing pages (deep-research, not capture)."
  - "Founding year not explicitly stated on captured pages (site cites 'two decades' / '20 years' of early-stage experience)."

# Description
description: "A seed-stage venture capital firm that backs founders at the very earliest stage of company building — often pre-product — pairing first-check capital with hands-on recruiting, go-to-market, and fundraising support."

# Classification
entity_type: Investor / Holding
target_market: [B2B]                 # founders/portfolio companies + institutional LPs (endowments, hospitals, charities)
offering_category: [Financial / Fintech Products, Services / Consulting]   # STRAIN: "investing" sense of Financial + the heavy hands-on partnership/platform they sell founders; no dedicated VC/asset-management value in the set
portfolio_shape:                     # empty — Investor/Holding; the "portfolio" is its investments, not an offering catalog (TAXONOMIES rule)
business_model:                      # empty — VC economics (mgmt fee + carried interest) fit none of the closed set; site doesn't state it
primary_industry: Finance & Fintech

# Visual identity
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 36, h: 76 }                                                                 # the stylized "1" with "First Round" knocked out vertically — mark+name in one; portrait orientation
  logomark: { src: "https://www.google.com/s2/favicons?domain=firstround.com&sz=256", px: 256, transparent: true }     # the black "1" numeral, transparent bg confirmed on a magenta tile
  og:       { src: "https://cdn.sanity.io/images/m6i10uln/production/aef48c10a5038779888ea7fce62cc85e923827d2-1107x630.jpg?fm=webp", w: 1107, h: 630 }
brand_colors: { primary: "#E4ADFF", accent: "#3B1044" }   # lavender hero/CTA + deep-purple text/link; bold secondary blocks (sky #89BAFF, mint green) noted in Visual
fonts: [Store Norske Skandia, Store Norske Leif]          # custom display family (Arial fallback); confirmed in branding.fonts + typography stacks
color_scheme: light                  # cream (#FBFBF6) canvas dominant; black hero + footer are sections, not the base
design_framework: next.js            # rawHtml /_next/ ×32 + Vercel server header; Sanity-backed content
---

## Overview

First Round is a venture capital firm that invests **exclusively at the earliest stage** of company building — "often when all they have is an 'imagine if.'" It positions as the first money in (pre-seed/seed, ahead of product-market fit) and pairs the check with an unusually hands-on services team: recruiting, go-to-market, marketing, and fundraising help delivered directly to portfolio founders. The site frames two decades (20 years) of early-stage experience across 500+ teams, with marquee early bets in Notion, Roblox, Square, Uber, and Looker (most entered at seed; Square's listed initial partnership is Series A). Beyond investing it runs free founder/investor programs (PMF Method, Angel Track) and a widely-read content publication (The Review).

## What they offer

What founders (and aspiring angels) get from First Round — investment plus a services platform plus free programs:

- **Seed-stage investment:** initial checks **"typically range from $1 million to $7 million"**, **"average initial investment is right around $3.5 million"**; rounds **"as small as $100,000 and as large as $20 million"**; ideal ownership **"roughly 14% after your seed round … but rarely below 10%"** (vs. the traditional 20–25%). Stage is angel / pre-seed / seed — "we're named First Round for a reason"; not a fit past a few million raised or at Series B/C. `[published]`
- **The platform — hands-on operating help to portfolio founders** (the four building blocks of "How we work") `[published]` (bundled with investment):
  - **Build your team:** First Round acts as a founding recruiter — "we source, run outreach, and connect you directly with qualified candidates."
  - **Position your product:** an early marketer "until you have your own in place," finding language to scale the story.
  - **Get to repeatable revenue:** open doors to key accounts, game-tape feedback on customer calls, interview your first sales leader.
  - **Raise your next round:** shape the Series A narrative, "craft each slide, line up investor intros, and practice until it's pitch perfect."
- **PMF Method:** a **free**, intensive **4-day** retreat (Sonoma) for early B2B SaaS founders who've **"raised less than $2M"** — 6 sessions on their PMF framework (discovery/4Ps, market selection, founder-led sales, positioning, iteration/pivots). "We give you $0 and take 0% of your company." `[published]` (free, no equity)
- **Angel Track:** a **free** education-and-community program for promising angels (400+ alumni; typically 5–15 investments in); in-person cohort retreat; covers assessing teams, sizing markets, portfolio construction, tax/estate. "We do not provide capital to participants." `[published]` (free, no capital)
- **The Review:** a free content publication ("Tactical 0-1 breakdowns") at review.firstround.com, plus the "Levels of PMF" framework at /levels. `[published]` (free)

## How it works / model

Founders reach First Round by referral or cold outreach ("our investment team reviews every single investment opportunity"). The diligence process is **3–5+ hours minimum** over days to months: initial meeting → follow-up with a point partner (and a domain-expert partner) → a pitch to the full partnership at their **twice-weekly investment meeting** → a same-day decision; **"we fund about half of the companies that make it to our partner meeting."** They don't require leading the round and have no strict ownership minimums. Post-investment, partners often take a board seat (later relinquished to new investors) and run **"working sessions" every 4–6 weeks** in place of traditional board reporting. They won't invest in directly competing companies and set up an information firewall if a portfolio company pivots into a conflict. They won't sign NDAs. Capital comes **"from university endowments, hospitals, and a wide variety of charities"** — and explicitly **no sovereign wealth funds or governments**. (Fund/fee economics aren't disclosed on the site.)

## Positioning & audience

Target: exceptional, "contrarian" founders at the absolute beginning — pre-traction, pre-PMF, sometimes pre-name, U.S.-based (concentrations in SF and New York; also Philadelphia, with nationwide and occasional distributed/ex-U.S. exceptions). The pitch against larger multistage firms: maximal alignment and effort at the start — "the most closely aligned investor on your cap table—and outwork everyone else, too," contrasted with "an industry that's moved to call options and traded focus for footprint." They claim no sector mandate ("we don't think VCs predict the future — founders do") but note investments cluster in **enterprise, AI, hardware, healthcare, fintech, and consumer**. Founder selection emphasizes "the art of the pick," "extreme" (spiky, not well-rounded) talent, and going "unreasonably deep."

## Nav structure

```
- Home — /
- Companies — /companies
- How we work — /how-we-work
- Team — /team           (sub: /team/investing, /team/board-partners, /team/operating, /team/finance-and-administration)
- Who we back — /who-we-back
- PMF Method — /pmf       (related: /levels — the "Levels of PMF" framework)
- The Review — https://review.firstround.com/   (external content publication)
Footer — FIRST ROUND: Companies · How we work · Who we back · Team · The Review · News (/news) · Careers (jobs.firstround.com)
Footer — PROGRAMS: PMF Method (/pmf) · Angel Track (/angel-track)
Footer — SOCIAL: LinkedIn · X · YouTube · Instagram
Footer — LEGAL: Terms (/terms) · Privacy (/privacy)
```

## Credibility & proof

- **Track record (self-reported):** **"We've worked with 500+ early teams"**; **"part of many important imagine ifs"** over **"two decades" / "20 years."** Named marquee investments shown: **Notion, Roblox, Square, Uber, Looker** (plus a featured portfolio incl. Clay, Upstart, Verkada, Flatiron Health, Persona, Flexport, Clover Health, Loyal, K2 Space, Pomelo Care, Fal, Omni, EvolutionIQ). The grid labels each company's "Initial Partnership" stage — mostly Seed, with some Pre-Seed (K2 Space) and Series A (Square, Clover Health, Assort Health).
- **Program scale (self-reported):** Angel Track **"over 400 top founders, builders and creators"**; alumni testimonials from operators at Linear, OpenAI, Cloudflare, Vanta, Instacart, plus Lenny Rachitsky.
- **Founder testimonials:** named quotes on /how-we-work and /pmf (Marta Bralic Kerns/Pomelo, Kareem Amin/Clay, Michael Chime/Prepared, Karan Kunjur/K2 Space) and PMF-Method founder quotes (anonymized "second-time founder," etc.).
- **Offices:** San Francisco (921 Front Street, 94111), New York (165 Mercer Street, Floor 2, 10012), Philadelphia (2400 Market St, Suite 237, 19103).
- All proof is self-reported on the firm's own site — recorded, not independently verified.

## Visual & brand impression

Confident, design-forward, and playful for a VC. A cream (#FBFBF6) canvas is punctuated by full-bleed **bold color blocks** — lavender (#E4ADFF), sky blue (#89BAFF), mint green — and dramatic black hero/footer sections. Headlines use a custom display family (Store Norske) mixing an **italic serif** ("_Beginnings_ Matter") with a heavy sans, leaning literary/editorial. The signature mark is a tall stylized **"1"** with "First Round" knocked out vertically inside its stem — doubling as logomark (the bare "1") and wordmark. Imagery centers founders and their companies; motion and rotating heroes (a Mother's Day variant was live) signal an actively-maintained, content-rich site. Overall read: premium, opinionated, founder-first — the antithesis of buttoned-up institutional finance.

## Strategic read

The whole site is an argument that **early-stage VC is a service business, not just a capital business.** Where the offering would be one line for most funds ("we write seed checks"), First Round foregrounds an operating team — recruiters, GTM/marketing experts, a pitch-design lead — and codifies its method into productized, equity-free programs (PMF Method, Angel Track) and a flagship content engine (The Review). That content+programs flywheel is a deliberate top-of-funnel and brand moat: it generates deal flow, trains the angels who fill out their rounds, and broadcasts the "we do the work with you" differentiation. The explicit constraints — first-money-only, no Series B/C, ~14% target ownership, no sovereign/government LPs, no NDAs — read as a focused, values-signaling identity rather than a generalist multistage platform.

## Provenance

- **Pages:** 8 analyzed via Firecrawl (maxAge:0, US geo) — homepage + /how-we-work, /who-we-back, /companies, /team, /pmf, /angel-track, /news/manifesto; plus the homepage `branding`/`rawHtml`/screenshot and `fc.py signals` (nav region; no JSON-LD present). The Review (subdomain) noted but not captured.
- **Verify:** all 8 sourceURLs matched; all bodies md5-unique; no junk soft-404s.
- **Credits:** 9 (1 map + 8 scrapes). Logos module rode the cached homepage payload (no re-scrape).
- **Couldn't get:** full 500+ portfolio and full team roster (client-rendered filterable grids return only the loaded/featured subset); fund size/number and fee–carry economics (not on marketing pages); founding year (site states "two decades"/"20 years" only).
- **Run profile:** +logos (multi-ratio brand-mark set captured at user request — wordmark extracted from the inline header SVG, logomark + og measured).
- **Enriched (model knowledge):** Josh Kopelman is First Round's founder (he authored the manifesto and is listed as "Partner," but the captured pages don't state "founder").
