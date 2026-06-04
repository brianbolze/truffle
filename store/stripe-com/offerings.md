---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: stripe.com
captured_at: 2026-06-04
site_notes: "Roster source is ONE page: /pricing carries verbatim per-product prices for the whole platform (the cheap backbone — no per-PDP sweep needed). Stripe indexes at the PRODUCT level there (~30 products in 4 priced families + the agentic suite); sub-fees (manual-entry +0.5%, intl +1.5%, FX +1%) are leaves folded into the parent's Price/What, not rows. Big shape fact: many products are 'Included with Payments' — the 2.9%+30¢ rate buys a wide bundle (Checkout, Link, Payment Links, Elements, Radar base, Connect base, Authorization Boost, 3DS, Adaptive Pricing); standalone prices appear mainly for the finance-automation SaaS (Billing/Tax/Sigma/Data Pipeline/Rev Rec) and money-movement add-ons. Molecule/form columns are telehealth-specific — N/A here; What carries category + pricing basis. Prices are list/standard-tier; Custom (enterprise) is IC+/contact-sales and not shown."
---

## Portfolio overview

Stripe is a `Catalog`-shape platform; this roster is **complete at Stripe's own indexed level** — the ~30 named products `/pricing` enumerates across four priced families (**Global payments**, **Money management**, **Revenue & finance automation**, **More**) plus the **Agentic Commerce Suite**. It is *not* an exhaustive fee schedule: each product's secondary fees (international/manual-entry surcharges, dispute fees, P2PE) stay folded into the parent row, the level a buyer comparison-shops at.

**The defining shape fact — "Included with Payments."** A large share of the catalog has *no standalone price*: Checkout, Payment Links, Elements, Link, Radar (base), Connect (base), Authorization Boost, 3D Secure, and Adaptive Pricing are all *"Included … for businesses on standard payments pricing."* The headline **2.9% + 30¢** buys the whole acceptance + optimization surface. Standalone prices cluster in two places: the **finance-automation SaaS** (Billing, Tax, Sigma, Data Pipeline, Revenue Recognition — subscription, $15–$620/mo) and **money-movement add-ons** (Payouts, Issuing, Treasury, Financial Connections — per-use). So the platform monetizes the *core* by volume and the *edges* by subscription/per-call.

**Prominence (calibrated):**
- **Payments** — the lead, unambiguously `[HIGH]`: it's the first product, the headline rate, and the site's entire "accept payments" frame; every enterprise case study lists it first.
- **Connect · Terminal · Radar · Billing** — repeatedly foregrounded `[MED]`: they recur across the enterprise case-study product lists (Hertz, URBN, Instacart: *"Payments, Terminal, Connect, Radar, Sigma…"*) and have their own pricing sections.
- **Agentic Commerce Suite** — the loudest *forward* push `[MED]`: a dedicated solution page + the Sessions 2026 *"economic infrastructure for AI"* hero, but the products themselves (SPT, MPP) are new primitives, not yet case-study-proven.
- Everything else (Atlas, Climate, Identity, Workflows, Financial Connections) sits in the **More** bucket `[LOW]` — real, priced, but not foregrounded.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (category · pricing basis · access) |
|---|---|---|---|---|---|---|
| Global payments | family | — | /pricing#global-payments | — | — | Acceptance + optimization; online and in-person |
| Payments | buyable | Global payments | /payments | **2.9% + 30¢** per successful transaction for domestic cards (+0.5% manual, +1.5% international, +1% FX) | published | Online card/wallet processing · per-txn · self-serve |
| Link | buyable | Global payments | /payments/link | **2.9% + 30¢** domestic; **2.6% + 30¢** Instant Bank Payments; **5.99% + 30¢** Klarna | published | Accelerated one-click checkout · per-txn · self-serve |
| Checkout | buyable | Global payments | /payments/checkout | **Included** with Payments (custom domain $10.00/mo) | published | Prebuilt payment form · bundled · self-serve |
| Payment Links | buyable | Global payments | /payments/payment-links | **Included** with Payments (post-payment invoice 0.4%, $2.00 cap) | published | No-code payment links · bundled · self-serve |
| Elements | buyable | Global payments | /payments/elements | **Included** with Payments | published | Flexible UI components · bundled · self-serve |
| Payment methods | buyable | Global payments | /payments/payment-methods | per-method (Access to 100+) | published | 100+ local/global payment methods · per-method · self-serve |
| Terminal | buyable | Global payments | /terminal | **2.7% + 5¢** domestic (+$0.10 Tap to Pay, +$0.05 P2PE); readers **$59.00** (M2) / **$299.00** (S700/S710); cellular **$10.00**/reader/mo | published | In-person/POS payments · per-txn + hardware · self-serve |
| Managed Payments | buyable | Global payments | /managed-payments | **3.5%** per transaction in addition to Payments fees | published | Merchant-of-record (tax/fraud/disputes in 75+ countries) · per-txn · self-serve |
| Radar | buyable | Global payments | /radar | **Included** (base); **$0.05**/txn on custom pricing; Radar for Fraud Teams **$0.02**–**$0.07**/screened txn | published | ML fraud prevention · bundled / per-screen · self-serve |
| Authorization Boost | buyable | Global payments | /authorization-boost | **Included** with Payments; **0.2%**/txn on custom pricing | published | AI acceptance optimization · bundled · self-serve |
| Money management | family | — | /pricing#money-management | — | — | Embed financial services — accounts, payouts, cards, financing |
| Connect | buyable | Money management | /connect | **Included** with Payments; from **0.25%** platform fee for platforms deploying their own pricing | published | Embedded payments for platforms/marketplaces · bundled / platform fee · self-serve |
| Treasury | buyable | Money management | /treasury | **Included** (no storage fee / min balance); **$2.00** per wire | published | Banking-as-a-service business account · bundled + per-wire · self-serve |
| Global Payouts | buyable | Money management | /payouts | **$1.50** per payout (+0.75% domestic, min 50¢; +0.25% cross-border +0.5% FX intl) | published | Payouts to third parties · per-payout + % · self-serve |
| Issuing | buyable | Money management | /issuing | **$0.10** per virtual card; **$3.50** per physical card | published | Physical/virtual card issuing · per-card + interchange · contact (BaaS) |
| Capital | buyable | Money management | /capital | no public rate | on-request | Business financing · revenue-share/contact · gated |
| Crypto | buyable | Money management | /crypto | stablecoin acceptance **1.5%** of USD amount | published | Wallet · stablecoin issuing · card infra · per-txn · self-serve |
| Crypto Onramp | buyable | Money management | /crypto-onramp | no price shown on /pricing | on-request | Embeddable crypto purchases · contact/docs · gated |
| Revenue & finance automation | family | — | /pricing#revenue-and-finance-automation | — | — | Billing, tax, invoicing, revenue reporting, analytics |
| Billing | buyable | Revenue & finance automation | /billing | Pay monthly from **$620.00**/mo (1-yr contract, volume tier) **or** pay-as-you-go **0.7%** of Billing volume | published | Subscriptions/usage-based/one-time billing · subscription or % · self-serve |
| Usage-based billing | buyable | Revenue & finance automation | /billing/usage-based-billing | within Billing | published | Metered billing · within Billing · self-serve |
| Subscriptions | buyable | Revenue & finance automation | /billing/subscriptions | within Billing | published | Subscription management · within Billing · self-serve |
| Invoicing | buyable | Revenue & finance automation | /invoicing | Starter **0.4%** per paid invoice | published | Global invoicing software · per-invoice · self-serve |
| Tax | buyable | Revenue & finance automation | /tax | Tax Complete from **$90.00**/mo (1-yr); Tax Basic **0.5%**/txn (no-code) or **$0.50**/txn (API) | published | Sales-tax/VAT/GST automation · subscription or per-txn · self-serve |
| Revenue Recognition | buyable | Revenue & finance automation | /revenue-recognition | **$25.00**/mo (monthly); annual from **$190.00**/mo (higher volume) | published | ASC 606 / IFRS 15 accrual automation · subscription · self-serve |
| Stripe Sigma | buyable | Revenue & finance automation | /sigma | **$15.00**/mo (monthly); annual from **$10.00**/mo (1-yr) | published | SQL/AI reporting on Stripe data · subscription · self-serve |
| Data Pipeline | buyable | Revenue & finance automation | /data-pipeline | **$65.00**/mo (monthly); annual from **$50.00**/mo (1-yr); includes Sigma | published | Warehouse/cloud data sync · subscription · self-serve |
| More | family | — | /pricing#more | — | — | Identity, financial-data, incorporation, climate, automation |
| Financial Connections | buyable | More | /financial-connections | **$1.50**/instant verification; balances **$0.10**/call; account owners **$1.50**/call; transactions **$0.30**/institution/account/mo | published | Linked bank-account data · per-call · self-serve |
| Identity | buyable | More | /identity | **$1.50** per ID+selfie verification; **$0.50** per ID number lookup | published | KYC identity verification · per-verification · self-serve |
| Atlas | buyable | More | /atlas | **$500.00** one-time setup (incl. govt fees + first year registered agent) | published | Startup incorporation software · one-time · self-serve |
| Climate | buyable | More | /climate | **3%** of order value | published | Permanent carbon removal (Frontier portfolio) · % of order · self-serve |
| Workflows | buyable | More | /pricing#workflows | **Included** 10,000 steps/mo; **$0.018** per additional step | published | No-code automation (600+ triggers) · bundled + per-step · self-serve |
| Agentic Commerce Suite | family | — | /use-cases/agentic-commerce | — | — | Payment + discovery primitives for AI agents (see Deep block) |
| Shared Payment Tokens | buyable | Agentic Commerce Suite | /use-cases/agentic-commerce | **$0.15** per SPT issued | published | Secure agent-purchase primitive · per-token · self-serve (priced on /pricing) |
| Machine Payments Protocol | buyable | Agentic Commerce Suite | /use-cases/agentic-commerce | no separate price (rides payment fees) | on-request | Accept payments from agents (cards/stablecoin/BNPL) · open protocol (mpp.dev) · self-serve |

### Verbatim anchors

The footnotes the Price/Visibility cells lean on (quoted exactly from `/pricing` unless noted):

- **Standard vs. Custom (the two tiers).** Standard: *"2.9% + 30¢ per successful transaction for domestic cards … No setup fees, monthly fees, or hidden fees."* Custom: *"IC+ pricing · Volume discounts · Multi-product discounts · Country-specific rates"* → *"Contact sales."* All roster prices are **Standard-tier**; Custom is enterprise IC+ and not shown → that tier alone is `on-request`.
- **"Included with Payments" (decides `published`, not `partial`).** Repeated verbatim across Checkout, Payment Links, Elements, Link, Radar, Connect, Authorization Boost, 3D Secure: *"Included … Included at no additional charge for businesses on standard payments pricing."* The all-in IS shown (it's the 2.9% + 30¢), so these are `published`, not `partial` — the bundle price is self-contained.
- **Billing.** *"Pay monthly — Annual subscription. Paid monthly. Based on a volume tier… **Starting at $620.00 per month, 1-year contract**"* and *"Pay as you go — **0.7% of Billing volume**… Includes Billing transactions processed on and off Stripe."* Marked `published` because the 0.7% PAYG option is fully self-contained (the $620 floor moves with volume tier, but the buyer has a shown flat alternative).
- **Managed Payments.** *"**3.5%** per successful Managed Payments transaction **in addition to Payments fees**"* — additive but fully shown → `published`.
- **Capital / Crypto Onramp (`on-request`).** Capital is *"Business financing"* in nav with no rate on `/pricing` (revenue-share, *"qualify for a revenue share"*); Crypto Onramp has a nav/footer entry but no price section on `/pricing`.
- **Molecule sourcing audit.** N/A — Stripe sells software/APIs, not molecules; the telehealth `molecule · form · access` lead is replaced by `category · pricing basis · access`. No molecule was inferred or asserted.

## Deep blocks

Only one earns a block — the **Agentic Commerce Suite**, because a single roster row collapses a set of distinct new primitives that are Stripe's marquee strategic bet and don't price uniformly. No per-SKU deep-dives are otherwise earned: the roster + anchors carry the rest (the "Included with Payments" pattern is the one cross-cutting subtlety, and it's captured above).

**Agentic Commerce Suite** — `/use-cases/agentic-commerce`. *"Agents are changing how we buy and sell. Stripe's Agentic Commerce Suite connects businesses, agents, and buyers."* Three primitives, three roles:
- **Shared Payment Tokens (SPTs)** — **$0.15 per SPT issued** `[published]`. *"a secure payment primitive that helps agents facilitate purchases on behalf of customers"*; carries Radar risk signals so a business stays merchant-of-record without handling PCI data.
- **Machine Payments Protocol (MPP)** — no separate price (rides payment fees) `[on-request]`. *"Accept payments from agents using the Machine Payments Protocol (MPP) with just a few lines of code. MPP supports cards, stablecoins, and buy now, pay later"* (open standard at mpp.dev).
- **Link agent wallet / Issuing for agents** — *"Give agents a way to pay on your behalf with Link's agent wallet or Issuing for agents. Agents spend within built-in guardrails, every transaction is visible in real time."* Plus open standards: the **Universal Commerce Protocol** and **x402**.
- Named adopters (self-reported, the page's logo wall): Etsy, Best Buy, Wix, URBN, Browserbase, Parallel, Coach, Quince.

## Provenance

- **Pages read:** `/pricing` (the rich `--homepage` backbone — full product list + verbatim prices + prominence screenshot), plus `homepage`, `/payments`, `/billing`, `/connect`, `/use-cases/agentic-commerce` for cross-checks (all `captures/2026-06-04/`).
- **Scope:** Enumerated = every product `/pricing` indexes (4 priced families + agentic suite, ~30 rows). Noted-but-not-enumerated = each product's secondary fee schedule (intl/manual surcharges, dispute fees, reader variants, per-country FX) — folded into the parent row, not exploded. Custom-tier (enterprise IC+) pricing is gated and not shown.
- **Completeness:** roster cross-checked against three blind sources that agree — the `/pricing` sections, the homepage footer product list, and the `/pricing` mega-nav flyout. No SKU slug was constructed; each is an attested URL from a captured page.
- **Point-in-time caveat:** prices are the US **Standard**-tier list as shown 2026-06-04; enterprise Custom pricing differs, and Stripe runs country-specific rates. No A/B instrumentation observed, but treat figures as a dated snapshot.
- **### Run profile:** guided opt-in — `+offerings.md` requested for a `Catalog`-shape company (off the usual telehealth use case), kept at Stripe's product-grain indexed level rather than an exhaustive fee table. Flagship **hero product images** were requested but are **N/A**: a software/API company has no isolated product render — the 15 path-scored candidates were lifestyle photography, demo-merchant goods, and UI mockups, so none was promoted (the brand's only "hero" asset, the gradient `og` cover, lives in `profile.md`'s `logos.og`).
