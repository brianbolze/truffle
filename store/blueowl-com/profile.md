---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.2"

# Identity
domain: blueowl.com
name: Blue Owl Capital
aliases: ["Blue Owl Capital Inc.", "NYSE: OWL"]
parent: []
owns: []                             # manages, but does not "own", separately-traded fund vehicles (OBDC, OTF, etc.) — see body

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "Drupal (custom theme /themes/custom/blueowl/; drupal-settings-json, /sites/default/files/ asset paths). Mega-menu nav, fully captured from homepage markdown. No consumer pricing — asset manager. Offering = 3 investment platforms (/credit, /real-assets, /gp-strategic-capital); fund products on /our-products link out to separate domains (blueowlcapitalcorporation.com, blueowltechnologyfinance.com) + hubs.li short links. Sub-sites: ir.blueowl.com (shareholders/SEC), wealth.blueowl.com (advisor/private-wealth portal), docs.blueowl.com (fund docs). CAPTURE QUIRK: /about-us history timeline renders year labels with a Japanese 年 suffix (e.g. '2009年') despite location:US — a Drupal date-format/locale artifact, body copy otherwise English."
key_pages:
  about: /about-us
  credit: /credit
  real_assets: /real-assets
  gp_strategic_capital: /gp-strategic-capital
  products: /our-products
  who_we_serve: /who-we-serve
  insurance_solutions: /insurance-solutions
unverified_fields:
  - "Fonts — Firecrawl branding returned only system generics (Arial, Noto Sans, Roboto, Helvetica Neue); the distinctive headline face wasn't resolved. Left empty."
  - "Headcount/AUM figures are the firm's own marketing stats (as of 2026-03-31), not independently verified."

description: "An alternative asset manager investing in private markets across three platforms—Credit, Real Assets, and GP Strategic Capital—deploying ~$315B AUM for institutional, private wealth, and insurance investors."

# Classification
entity_type: Investor / Holding      # alternative asset management firm (NYSE: OWL); invests on behalf of others
target_market: [B2B, B2C]            # institutions/insurers/other GPs (B2B) + financial advisors & individual investors via the wealth channel (B2C)
offering_category: [Financial / Fintech Products]
portfolio_shape:                     # STRAIN: empty per taxonomy (Investor/Holding — its "portfolio" is investments); the 3-platform offering structure is in the body
business_model: Other                # management + performance/incentive fees on AUM; no taxonomy value fits asset-management fee economics
primary_industry: Finance & Fintech

# Visual identity
logo_url: https://www.blueowl.com/themes/custom/blueowl/favicon.ico   # branding.images.logo is an inline data-URI SVG (white owl + "BLUE OWL" wordmark) → favicon fallback
brand_colors: { primary: "#091D35", accent: "#94D2FF" }   # deep navy dominant; light-blue + a green motif as accents (screenshot-confirmed)
fonts: []
color_scheme: dark
design_framework: drupal             # rawHtml: drupal-settings-json + /themes/custom/blueowl/ + /sites/default/files/
---

## Overview

Blue Owl Capital (NYSE: OWL) is a publicly-traded alternative asset manager focused exclusively on private markets, with ~$315B in assets under management (as of 2026-03-31). It deploys capital across three platforms — **Credit** ($159.2B AUM), **Real Assets** ($85.1B), and **GP Strategic Capital** ($70.6B) — and markets the brand line "Redefining alternatives®." The firm positions itself as a "partner of choice for businesses seeking private capital solutions" while offering investors differentiated alternatives aimed at strong risk-adjusted returns, current income, and capital preservation. It emphasizes permanent capital ($224B+) and long-term, relationship-driven investing.

## What they offer

Three distinct investment platforms (each comparison-shopped separately by LPs), plus a cross-platform Insurance Solutions capability and a set of registered/retail-accessible fund products:

- **Credit ($159.2B AUM; $195B gross originations, 825+ direct-lending deals):** direct lending to PE-sponsored and non-sponsored companies. Strategies: **Direct Lending** (Diversified, Technology, First Lien, Opportunistic), **Alternative Credit** (asset-based finance, specialty finance, equipment leasing), **Investment Grade Credit** (insurance-tailored), **Liquid Credit** (CLO management).
- **Real Assets ($85.1B AUM; 6,145+ properties, 865+ tenant relationships):** credit-first real-assets investing. Strategies: **Net Lease** (single-tenant industrial/healthcare/essential-retail/data-center), **Real Estate Credit**, **Digital Infrastructure** (data centers / hyperscaler partnerships).
- **GP Strategic Capital ($70.6B AUM; 70+ partnerships, 15-yr track record):** minority equity & financing to other alternative managers. Strategies: **GP Minority Stakes**, **GP Debt Financing**, **Professional Sports Minority Stakes**. Backed by a 55+ person **Business Services Platform** (NY/Menlo Park/London/Hong Kong) providing partner managers strategy, M&A, human-capital, AI/data-science, and procurement support.
- **Insurance Solutions:** cross-platform capability tailoring alternatives strategies for insurers.
- **Registered products:** access to the Credit platform: BDCs — **OBDC** (NYSE: OBDC), **OTF** (NYSE: OTF), **OCIC** (non-traded), **OTIC** (non-traded), **OBDC II** (non-traded); plus interval fund **OWLCX** (Blue Owl Alternative Credit Fund). These trade/host on separate domains, not blueowl.com.

## How it works / model

Blue Owl is the management company that raises and manages private-markets funds and earns fees on the capital it manages (management + performance/incentive fees on AUM) — distinct from the consumer/subscription models in the taxonomy, hence `business_model: Other`. It raises across two channels: **institutional** (pensions, endowments, sovereign wealth, insurers) and **private wealth** (via financial advisors, with a dedicated wealth.blueowl.com portal). It stresses **permanent capital** ($224B+) — capital not subject to redemption — as a structural differentiator. Borrowers/portfolio companies are the "users of capital" on the other side.

## Positioning & audience

Targets five named audiences (per /who-we-serve): **alternative asset managers** (GP stakes + portfolio-company financing), **financial advisors & individual investors** (accessible alternatives), **growth tech companies** (equity/debt for venture-backed founders), **institutional investors**, and **insurance companies**. Claimed edge: scale, certainty/speed of execution, a credit-first / downside-mitigation discipline, permanence, and "maximally aligned, minimally invasive" partnership (esp. in GP Strategic Capital). Stated values: mutual respect, excellence, constructive dialogue, "one team." Co-CEO Doug Ostrover framing: "offer investors some of the best risk-adjusted returns they can find in the marketplace."

## Nav structure

```
- What we do
  - Our investment platforms
    - Credit — /credit
    - Real Assets — /real-assets
    - GP Strategic Capital — /gp-strategic-capital
  - Our cross-platform capabilities
    - Insurance Solutions — /insurance-solutions
  - Our products
    - OBDC — https://www.blueowlcapitalcorporation.com/
    - OTF — https://www.blueowltechnologyfinance.com/
    - OCIC — hubs.li short link
    - OTIC — hubs.li short link
    - OWLCX — https://wealth.blueowl.com/solutions-product-owlcx
    - View all — /our-products
- Who we serve — /who-we-serve
  - Alternative asset managers — /alternative-asset-managers
  - Financial advisors — /financial-advisors
  - Growth tech companies — /growth-tech-companies
  - Institutional investors — /institutional-investors
  - Insurance companies — /insurance-solutions
- Who we are — /about-us
  - About us — /about-us
  - Our team — /our-team
  - Sustainability — /sustainability
- Insights — /insights
- News — /news
- (utility) Shareholders — ir.blueowl.com · Investor Portal — /portals · Careers — /careers · Contact — /contact
```

## Credibility & proof

- **Public listing:** NYSE: OWL; full IR/SEC-filings presence at ir.blueowl.com (quarterly results, dividends, governance).
- **Scale:** ~$315B AUM, $224B+ permanent capital, 1,390+ employees, 15+ markets.
- **Awards:** "Seven 2025 PERE and Infrastructure Investor Awards."
- **Press / peer signals:** Active press cadence (fund closes, mergers, executive hires); a Blackstone co-investment (Atlas Holdings, Mar 2026) signals peer credibility.
- **Sponsorship:** "Redefining the game" — sponsors professional tennis players (a visible homepage banner).

## Visual & brand impression

Institutional, restrained, and confident. The homepage opens on a full-bleed **deep navy (#091D35)** hero with the serif/clean wordmark "Redefining alternatives®" in white — the palette is overwhelmingly navy + white, with **light blue (#94D2FF)** and a single **green** circular motif used sparingly as accents. Heavy whitespace, large AUM stat blocks ($315B), and editorial "market commentary" cards convey a premium, mature financial-services brand built for trust rather than flash. The owl mark is a minimal white line glyph. Overall: corporate-blue-chip alternatives manager, deliberately understated.

## Strategic read

Blue Owl is a roll-up success: the 2020 merger of **Owl Rock** (direct lending, est. 2016) and **Dyal Capital** (GP stakes, est. 2010) created the firm; **Oak Street** (net-lease real assets, est. 2009) joined in 2022. It has since acquired Wellfleet, Cowen Healthcare Investments, Prima Capital, Kuvare Asset Management, Atalaya Capital Management, and IPI Partners — a deliberate platform-assembly strategy across credit, real assets, and insurance. Notable strategic tilt toward **digital infrastructure / data centers** (Real Assets) and **software/technology lending** (Credit), riding AI-driven demand. Permanent capital and the insurance channel (Kuvare) are the durable-AUM bets.

## Provenance

- **Pages:** 7 via Firecrawl (`fc.py`, maxAge:0 + location:US + waitFor) — homepage (rich pass: markdown/html/rawHtml/links/branding/images/screenshot), /about-us, /credit, /real-assets, /gp-strategic-capital, /who-we-serve, /our-products. Map returned 436 URLs, dominated by /our-team/* bios + ir./docs./wealth. subdomain pages; key pages came from homepage links.
- **Verify:** all sourceURLs matched, all body md5s unique (clean — no §5.1 contamination).
- **Credits:** not recorded this run.
- **Couldn't get:** subdomain fund sites (OBDC/OTF own domains), ir.blueowl.com financials, /our-team, /sustainability, /insights — out of Tier-0 scope. Per-fund terms/fees live in SEC filings + fund prospectuses, not on blueowl.com.
- **Structured layer (schema 2.2):** ran `fc.py signals` on the persisted 2026-05-30 homepage rawHtml — JSON-LD present (3 blocks) but no `sameAs`/`logo`/`alternateName`, so no new structured-layer fields. Re-stamped 2.0→2.2.
