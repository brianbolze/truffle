---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: waldo.fyi
captured_at: 2026-06-18
enumeration: indexed-complete
site_notes: "Pricing backbone is /pricing (markdown-clean): Strategize $49/100 credits; Pitch & Monitor 'As low as $249' per pitch/report with volume discounts; Build 'Platform fee, based on company size'. Monitor's four scan types are anchors on /monitor (#scan-brand/-trend/-audience/-category) — attested, not constructed. Build is early-access/waitlist and credit-metered on top of the platform fee. Product pages (/strategize /pitch /monitor /build) carry the deliverable detail. No separately-priced feature SKUs — this is product/plan grain, not feature soup. Prices are consumption-metered floors ('as low as'), so re-check before quoting."
---

## Portfolio overview

Waldo sells one agent platform over a shared, normalized brand-data layer, packaged as **four products** that ladder the agency workflow: **Strategize** (research), **Pitch** (new business), **Monitor** (always-on briefs), and **Build** (the API/MCP data layer). This `offerings.md` is intentionally **product/plan grain** — it rosters the buyable products and Monitor's four named scan types, while the underlying data sources, agent fleet, workflows, and API endpoints stay in the `What` cells and in `profile.md`. Pricing is consumption-metered (credits, per-pitch, per-report, platform fee), not per-seat.

**Prominence read:**
- **Strategize `[HIGH]`:** the self-serve entry product — listed first in the product grid, cheapest ($49/100 credits), buy-now CTA, and the only line with no demo gate.
- **Pitch `[HIGH]`:** heavily featured (own product video, repeated "win the pitch" hero), fully self-serve at `/quick-pitch`, "no subscription required."
- **Monitor `[MED]`:** prominent but demo-gated on the pricing grid ("Book a demo"); the four scans are the depth here.
- **Build `[MED]`:** present across nav and pricing but **early-access/waitlist** — the least-finished line (signal: order-last, "Join the waitlist" rather than a buy/CTA).

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (capability · billing basis · access) |
|---|---|---|---|---|---|---|
| Waldo platform | family | — | /overview | — | — | Agentic brand-intelligence platform: a normalized data layer (live social, Meta/Google ad libraries, GWI panels, trends, events, open web) + "10,000+" AI agents · — · self-serve + sales; usable in-app or in Claude/ChatGPT via connector + MCP |
| Strategize | buyable | Waldo platform | /strategize | **"$49 / 100 credits"** (reload anytime) | published | On-demand research: Strategy Agent (AI strategist) + one-click workflows (brand audits, four C's, audience/competitor profiles) · credit pack · self-serve (buy → /subscribe/strategize); connects to Claude/ChatGPT |
| Pitch | buyable | Waldo platform | /pitch | **"As low as $249 / pitch"** (volume discounts) | partial | New-business pitch playbook: go/no-go verdict, decoded brief, 3–4 ranked angles, room intelligence, sourced proof; +100 Strategize credits · per-pitch, "No subscription required" · self-serve (buy → /quick-pitch) |
| Monitor | family | Waldo platform | /monitor | **"As low as $249 / report"** (volume discounts) | partial | Recurring interactive intelligence briefs with Strategy Agent inside; four scan types (below); any cadence; white-labelable · per-report or subscription · buyable on-site or "Book a demo" |
| Monitor — Brand Scan | buyable | Monitor | /monitor#scan-brand | **"As low as $249 / report"** | partial | A brand's paid/owned media + social mentions, a read on what's landing, and say/receive gaps · per-report · on-site or demo |
| Monitor — Trend Scan | buyable | Monitor | /monitor#scan-trend | **"As low as $249 / report"** | partial | What's trending + lifecycle stage (emerging/accelerating/peaking/declining/dead) + what to do · per-report (trends cadence: daily) · on-site or demo |
| Monitor — Audience Scan | buyable | Monitor | /monitor#scan-audience | **"As low as $249 / report"** | partial | What an audience cares about outside your brand, how you stack up, ideas to activate · per-report · on-site or demo |
| Monitor — Category Scan | buyable | Monitor | /monitor#scan-category | **"As low as $249 / report"** | partial | The whole category: competitor moves, signal-vs-noise, white space · per-report · on-site or demo |
| Build | buyable | Waldo platform | /build | **"Platform fee, based on company size"** (+ credit-metered usage) | on-request | Unified brand-intelligence API + MCP server — raw / aggregated / analyzed data across brand, audience & category endpoints, for agents and teams · platform fee + usage credits · **early access (waitlist)** → /build#get-key |

## Verbatim anchors

- **Strategize price:** `/pricing` — "Reload anytime · $49/ 100 credits". Self-contained, self-serve → `published`.
- **Pitch price:** `/pricing` — "As low as · Volume discounts · $249/ pitch · No subscription required." The shown number is a volume **floor** (single-pitch all-in not stated), so `partial`, not `published`.
- **Monitor price:** `/pricing` — "As low as · Volume discounts · $249/ report." Same floor logic → `partial`. `/monitor` FAQ: "You can buy a single briefing on the website, or talk to us about a subscription if you want recurring delivery"; first report "in under two hours."
- **Build price:** `/pricing` — "Based on company size · Platform fee · Book a demo" (no figure). `/build` FAQ: "It's credit-metered, so you pay for what you use, with volume discounts as you scale… Raw list endpoints are inexpensive (1 credit per ~20 results), and analysis endpoints… cost more (typically ~5 credits). Activating a custom brand, category, or audience… is an annual fee on top… no per-seat pricing." `/build` hero: "Build is in early access. Join our waitlist." → `on-request`.
- **Pitch verdict labels (verbatim):** "Full Send / Toss-Up / Walk Away" (`/pitch`).
- **Bundled credits:** both Pitch and Monitor cards list "+100 Strategize credits to go deeper" (`/pricing`).
- **Molecule/spec audit:** N/A — software platform. `What` descriptors use capability/billing language from `/pricing`, `/strategize`, `/pitch`, `/monitor`, and `/build`.

## Deep blocks

**None earned — the roster carries this company.** The only real ambiguity is pricing *visibility* (consumption floors vs. the gated Build platform fee), which the roster's verbatim prices + anchors already resolve. Monitor's four scans are rostered at the indexed level; Build's data domains (brand/audience/category) × analysis modes (raw/aggregated/analysis) and endpoint families are platform features, not separately-priced SKUs, so they stay in the `What` cell rather than inflating into rows.

## Provenance

- **Pages read (cited captures, 2026-06-18):** `pricing.md` (backbone — all four products' prices), `strategize.md`, `pitch.md`, `monitor.md` (four scan anchors), `build.md` (API model + credit metering + waitlist), `overview.md` (platform framing).
- **Scope note (`enumeration: indexed-complete`):** all four product lines rostered at product grain; Monitor expanded to its four named scans. Deliberately not row-expanded: Strategize's individual workflows ("50+"/"100+"), Build's individual API endpoints and analysis modes, and per-line data sources — these are sub-indexed features, not separately-priced offerings.
- **Visibility:** Strategize `published`; Pitch + Monitor `partial` (consumption floors with volume discounts, single-unit all-in not shown); Build `on-request` (platform fee, no figure, waitlist).
- **Point-in-time caveat:** prices are consumption-metered floors and a 2026-06-18 snapshot — Pitch/Monitor "as low as $249" move with volume; re-capture before comparing current prices.
- **Run profile:** express full pack — `offerings.md` requested ("deep offerings") for a B2B SaaS company; kept at product/scan indexed grain rather than feature-SKU inflation. No hero product images (software platform). Captured with `fc.py --shot none` (Firecrawl screenshots 500 on this SPA; see `profile.md` site_notes).
