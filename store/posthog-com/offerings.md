---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: posthog.com
captured_at: 2026-06-16
enumeration: indexed-complete
site_notes: "The whole roster lives inline on /pricing (markdown-clean, no JS wall) — all 13 metered products with full tiered rate cards + the platform add-on packages on one page; /pricing IS the backbone, no per-SKU sweep needed (prices are NOT PDP-gated). /products carries the taxonomy + labels but is client-rendered (labels in text; not every slug is linked). Several product PDP slugs aren't linked in captured markdown but resolve (curl-verified 200): /web-analytics /error-tracking /logs /workflows /endpoints /cdp /llm-analytics /heatmaps. Gotcha: /data-pipelines 404s — the marketing slug for Data Pipelines is /cdp. Platform packages (Boost/Scale/Enterprise) on /platform-packages. Pricing is volume-tiered (rate drops with scale) — roster quotes the entry 'From $X' rate + the monthly free tier; full ladders are in captures/2026-06-16/pricing.md."
---

## Portfolio overview

PostHog sells **one platform ("Product OS") metered as ~13 individual products**, each with its own generous monthly free tier and pay-as-you-go usage rate after it. There are no seats/plan tiers on the products themselves — billing is per-unit (event, recording, request, row, exception, GB, credit…), the rate **drops with volume**, and you only add a card when you exceed a free tier. The only fixed-fee items are the three **platform packages** (Boost/Scale/Enterprise) — org-level governance/support add-ons layered on top of usage.

**Pricing is fully public** — every product's complete tiered rate card is on `/pricing` (PostHog's transparency posture), so the roster is `published` end-to-end; the lone exception is the **Enterprise** package (bespoke, "Contact us"). This is the rare company where `offerings.md` is trivially completable from a single page.

**Prominence read:**
- **The flagship trio — `[HIGH]`:** Product Analytics, Session Replay, Feature Flags. They are the four "most popular products" PostHog showcases on the homepage + the top of the pricing examples (with Managed warehouse), and they're #1–3 in the rate-card order.
- **Core supporting line — `[MED]`:** Web Analytics, Experiments, Surveys, Error Tracking, Managed warehouse, Data Pipelines/CDP — established, nav-prominent, ordered mid-card.
- **Newer / AI line — `[MED→LOW]`:** PostHog AI (cross-product agent, heavily promoted on the homepage hero), AI Observability (LLM analytics), Logs, Workflows — newer entrants, lower in the rate card; Logs + Workflows are the newest.

## Roster

One row per metered product (parent = **Product OS**), then the platform add-on packages. Prices are the entry "From" rate; the monthly free tier is in the same cell. Full volume ladders → `captures/2026-06-16/pricing.md`.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (metric · billing unit · access) |
|---|---|---|---|---|---|---|
| Product OS | family | — | /products | — | — | The all-in-one platform; ~13 products on shared data, one install · — · self-serve |
| Product Analytics | buyable | Product OS | /product-analytics | From **$0.00005**/event (first 1 million events/mo Free); identified events from **$0.000248**/event | published | Events, funnels, trends, paths, retention · per analytics event · self-serve |
| Web Analytics | buyable | Product OS | /web-analytics | _Billed with Product analytics_ (anonymous events) | published | GA-style site analytics dashboard · per (anonymous) event · self-serve |
| Session Replay | buyable | Product OS | /session-replay | Web from **$0.005**/recording (first 5,000/mo Free); mobile from **$0.0100**/mobile recording (first 2.5k Free) | published | Watch real user sessions · per recording (web + mobile metered separately) · self-serve |
| Feature Flags | buyable | Product OS | /feature-flags | From **$0.0001**/request (first 1 million requests/mo Free) | published | Flag management + rollouts · per flag request · self-serve |
| Experiments | buyable | Product OS | /experiments | _Billed with Feature flags_ | published | A/B + multivariate testing, no-code A/B · per flag request · self-serve |
| Surveys | buyable | Product OS | /surveys | From **$0.10**/response (first 1.5k responses/mo Free) | published | In-product surveys · per response · self-serve |
| Error Tracking | buyable | Product OS | /error-tracking | From **$0.00037**/exception (first 100k exceptions/mo Free) | published | Exception capture + alerts · per exception · self-serve |
| Logs | buyable | Product OS | /logs | From **$0.25**/GB (first 50 GB/mo Free) | published | Search & analyze logs in PostHog · per GB ingested · self-serve |
| Managed warehouse | buyable | Product OS | /data-stack/managed-warehouse | From **$0.000015**/row (first 1 million rows/mo Free) | published | Built-in data warehouse, SQL editor + BI, 120+ sources · per row synced · self-serve |
| Data Pipelines (CDP) | buyable | Product OS | /cdp | Realtime destinations from **$0.000500**/trigger event (first 10k Free); batch exports from **$0.00001500**/row (first 1 million Free) | published | ELT import + reverse-ETL/export, CDP · per trigger event / exported row · self-serve |
| PostHog AI | buyable | Product OS | /ai | From **$0.01**/credit (first 500 credits/mo Free, worth $5) | published | NL agent across the suite (insights, HogQL, replays, flags) · per AI credit (≈20% markup on inference) · self-serve |
| AI Observability | buyable | Product OS | /llm-analytics | From **$0.00006**/event (first 100k events/mo Free) | published | LLM traces, generations, evals, costs · per LLM event · self-serve |
| Workflows | buyable | Product OS | /workflows | Emails from **$0.003000**/email (first 10k Free); destinations from **$0.0007500**/dispatch (first 10k Free) | published | Automations / messaging · per email + per destination dispatch · self-serve |
| Group analytics (add-on) | buyable | Product Analytics | /product-analytics | From **$0.000071**/event | published | Account/group-level analytics · per event add-on · self-serve subscribe |
| Boost (platform package) | buyable | Platform packages | /platform-packages | **$250**/mo | published | Unlimited projects, white-labeling, HIPAA BAA, SSO enforcement · flat monthly add-on · self-serve subscribe |
| Scale (platform package) | buyable | Platform packages | /platform-packages | **$750**/mo | published | Priority support (8h target), SAML, approvals + all Boost · flat monthly add-on · self-serve subscribe |
| Enterprise (platform package) | buyable | Platform packages | /platform-packages | "Contact us" (bespoke) | on-request | RBAC, dedicated account manager, SCIM, custom MSA, invoicing + all Scale · bespoke pricing · sales contact |

### Verbatim anchors

- **Usage model (pricing.md):** "All our paid products are pay-per-use with generous monthly free tiers." · "You can set a billing limit for each product so you never get an unexpected bill." · "Prices reduce with scale."
- **Free-tier table (pricing.md):** Analytics 1M events · Session replay 5K recordings · Feature flags 1M requests · Error tracking 100K exceptions · Surveys 1500 responses · Data warehouse 1M rows + FREE historical · Data pipelines 10K events + 1M rows · AI Observability 100K events · PostHog AI 500 credits (worth $5) · Workflows 10K messages per channel · Logs 50 GB ingested.
- **PostHog AI credit basis (ai.md):** "We apply a simple, consistent 20% markup over the underlying LLM provider's cost: So 1 PostHog AI credit equals $0.008333 of raw inference, and 100 credits cost $1." (Note: the pricing.md free tier reads "500 credits (worth $5)"; the homepage hero reads "2K credits/mo free (worth $20)" — captured discrepancy, both quoted; treat as point-in-time, re-check next run.)
- **Platform packages (platform_packages.md):** Boost "$250/mo" — "Unlimited projects, white labeling, HIPAA BAA, SSO enforcement…"; Scale "$750/mo" — "Priority support, SAML…Includes all features in the Boost package"; Enterprise "Contact us" — "RBAC, dedicated support, training…Includes all features in the Scale and Boost packages."
- **Billed-with notes (pricing.md):** Web Analytics "_Billed with Product analytics_"; Experiments "_Billed with Feature flags_" — no separate meter, so `published` (the parent's rate is the all-in).
- **Molecule/spec audit:** N/A — software products, no molecule/form. "What" descriptors are taken from the product labels + pricing meters on `/pricing` and `/products`; billing units quoted from the rate cards.

## Deep blocks

**None earned — the roster carries this company.** The whole catalog is one transparent rate-card page with no gated prices, no dose/molecule ambiguity, and no PDP-only figures to disambiguate. The one genuine ambiguity (PostHog AI free-tier credits: 500 vs 2K) is captured inline in the Verbatim anchors, not worth a block.

## Provenance

- **Pages read (cited captures, 2026-06-16):** `pricing.md` (the full rate cards — backbone), `products.md` (Product OS taxonomy + labels), `platform_packages.md` (Boost/Scale/Enterprise), `homepage.md` (most-popular-products examples + free tiers), `ai.md` (PostHog AI credit basis). Slugs not linked in markdown were curl-verified to resolve (200) before rostering — none constructed.
- **Scope note (`enumeration: indexed-complete`):** every metered product line + every platform package is rostered at the line grain with its verbatim entry rate. **Sub-indexed leaf detail deliberately not expanded into rows:** the full volume ladders (each product's per-tier rate steps — e.g. Product Analytics' 7 tiers from $0.00005 down to $0.0000090) live in `pricing.md`; the roster quotes the entry "From" rate + free tier. No line/category omitted (`portfolio_shape: Multi-product` target met).
- **Visibility:** 17 of 18 rows `published` (complete public rate cards — PostHog's transparency posture); only **Enterprise** is `on-request` (bespoke "Contact us"). No `partial` — there are no hidden mandatory add-on costs; billing limits are opt-in caps, not gates.
- **Point-in-time caveat:** usage prices + free tiers are a 2026-06-16 snapshot; PostHog publicly states it cuts prices over time and the AI free-tier credit figure already disagrees across two pages — re-capture to refresh, don't bake.
- **Run profile:** part of a deep capture — `offerings.md` + `logos:{}` module + visual-evidence layer requested alongside the `profile.md` refresh.
