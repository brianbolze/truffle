# TAXONOMIES — the closed value sets

> **What this is.** The exact, closed value lists for the classification fields in [`SCHEMA.md`](SCHEMA.md). A capturing agent picks from these strings verbatim.

> **Why closed (read this first).** These fields exist so companies can be **grouped and filtered across the whole store** — "all B2C subscription brands," "every Software / SaaS company in Finance." That only works if everyone uses the *same* strings. A near-miss value (`SaaS` vs `Software / SaaS`, `D2C` vs `B2C`) silently fragments a group and the aggregation quietly under-counts. So treat these as a fixed vocabulary, not a suggestion. Free, expressive description belongs in the `profile.md` body — not here.

*Scope: commercial companies + products. All fields allow empty; most allow `Other` — the ordinal `portfolio_shape` is the exception (empty, never `Other`). See the rules at the bottom.*

---

## `entity_type`

*What kind of entity this is — usually `Company`. The other values are graceful flags for non-standard entities, and they gate which other fields apply (an investor has no products; a nonprofit has no business model). Single-select.*

| Value | Means |
|---|---|
| `Company` | An operating business selling products/services (the default) |
| `Brand` | A product brand owned by a parent (e.g. a CPG/OTC brand) — not itself an operating company; record the owner in `parent:` |
| `Investor / Holding` | VC/PE firm, holding company, or conglomerate parent |
| `Nonprofit` | Operates for social benefit, not profit |
| `Government` | Government or public-sector body |
| `Education` | School, university, or research institution |
| `Individual / Creator` | Personal brand, solo creator, or independent |

*`Brand` vs `Company` when there's a parent: use **`Brand`** only when the entity does **not** transact independently — a pure marketing/education site, no cart, revenue booked at the parent (e.g. Benadryl → Kenvue). If it runs its own P&L and sells directly, it's **`Company`** even with a parent (e.g. AWS → Amazon, Hims → Hims & Hers). Record the owner in `parent:` either way. `parent` says *who owns it*; `Brand` says *it isn't an operating business* — different facts, so both can apply.*

## `target_market`

*Who the company sells to — the cleanest grouping axis there is, evident from almost any site. Multi-select, best-fit first.*

| Value | Means |
|---|---|
| `B2B` | Sells to businesses |
| `B2C` | Sells to consumers |
| `B2B2C` | Sells through a business to reach end consumers |
| `B2G` | Sells to government / public sector |

## `offering_category`

*What the company sells. **List the primary first**; add a second only for a genuine hybrid (e.g. telehealth = `Services / Consulting` + `Biotech / Pharma Products`). Breadth across lines is captured by `portfolio_shape`, not here.*

| Value | Means |
|---|---|
| `Software / SaaS` | Software / cloud services, usually subscription or licensed |
| `Hardware / Physical Products` | Manufactured devices or equipment |
| `Services / Consulting` | Human-delivered expertise, advisory, or done-for-you services |
| `Marketplace / Platform` | Connects buyers and sellers; commission / network effects |
| `Media / Content` | Produces or distributes content (news, video, music, streaming) |
| `Financial / Fintech Products` | Payments, banking, lending, investing, insurance |
| `Biotech / Pharma Products` | Drugs, therapeutics, medical devices, diagnostics |
| `Consumer Packaged Goods (CPG)` | Frequently-replaced consumer goods (food, beauty, household) |
| `Apparel & Footwear` | Clothing, footwear, and accessories (incl. athletic & fashion brands) |
| `Retail / E-Commerce` | Sells products direct to consumers, online or in-store |
| `Industrial / Manufacturing` | Industrial goods, machinery, large-scale production |
| `Energy / Utilities` | Generates, distributes, or services energy |
| `Non-Profit / NGO` | Operates for social benefit, not profit |

## `portfolio_shape` *(optional)*

*The shape of what the company offers, by breadth (low→high). Single-select. Doubles as the capture instruction for `offerings.md` — how deep vs. how broad to go.*

| Value | Means | Capture |
|---|---|---|
| `Single` | One core offering — tiers, surfaces, or forms/variants of *one thing* | the one product, deeply |
| `Flagship + companions` | A dominant hero plus a small companion set | flagship first, then companions |
| `Multi-product` | Several distinct, *enumerable* product lines | enumerate the lines, breadth-first |
| `Catalog` | Too many to enumerate — capture the shape, not the list | shape only (e.g. category × flagship) |

**Tie-breaker (the field is only hard in the middle).** Count *distinct, separately-positioned* offerings, not variants. One brand/molecule in many forms, or one app with many surfaces, is `Single` (Benadryl, Linear). A clear hero + a few named add-ons is `Flagship + companions` (AG1). Several co-equal lines you could list is `Multi-product`. Un-enumerable scale is `Catalog` (Nike, AWS). *Would a buyer comparison-shop them as different things?* If no, collapse toward `Single`.

**Optional, and no `Other`.** Leave empty when a portfolio shape doesn't apply — an `Investor / Holding` (whose "portfolio" is investments) or a non-offering entity — and note why. If an offering-selling company fits none of the four, still leave it empty rather than force it; repeated empties are the signal to *extend these values*, not an `Other` to lean on.

## `business_model` *(optional)*

*How the company makes money — the primary model if several apply. Often inferable from pricing pages; leave empty if not.*

| Value | Means |
|---|---|
| `Subscription` | Recurring fee (SaaS, membership, DTC refills) |
| `Transactional / One-time` | Pay per purchase, no recurring commitment |
| `Usage-based / Consumption` | Metered pay-as-you-go (cloud, APIs); often with committed-use discounts |
| `Marketplace / Commission` | Takes a cut of facilitated transactions |
| `Freemium` | Free tier funnels to paid upgrade |
| `Advertising` | Monetizes attention / ad inventory |
| `Services / Project-based` | Bills for time, retainers, or projects |
| `Licensing` | Licenses IP, technology, or content |

## `primary_industry` *(optional — heaviest taxonomy)*

*The sector the company operates **in** — distinct from what it sells. A fintech SaaS is `primary_industry: Finance & Fintech`, `offering_category: Software / SaaS`. A medical-device maker is `Healthcare & Life Sciences` + `Hardware / Physical Products`. Pick the single best fit; use `Other` rather than forcing a poor one.*

| | | |
|---|---|---|
| `Technology` | `Energy & Utilities` | `Finance & Fintech` |
| `Healthcare & Life Sciences` | `Retail & E-Commerce` | `Media & Entertainment` |
| `Manufacturing & Industrial` | `Automotive & Mobility` | `Logistics & Supply Chain` |
| `Agriculture & Food` | `Real Estate & Construction` | `Education & Training` |
| `Consulting & Professional Services` | `Consumer Goods` | `Telecommunications` |
| `Environmental & Sustainability` | `Defense & Security` | `Hospitality & Tourism` |
| `Cryptocurrency & Blockchain` | `Sports & Recreation` | |

---

## Rules for the agent

1. **Use the exact strings above.** Consistency is the entire point — a value that isn't on the list (outside `Other`) breaks grouping for every reader.
2. **`Other` is allowed on the category fields** (`entity_type`, `offering_category`, `business_model`, `primary_industry`) and beats a forced wrong fit — add a one-line body note; repeated `Other`s signal the taxonomy needs a value. *Exception:* the ordinal `portfolio_shape` takes no `Other` — leave it empty instead.
3. **Empty is always allowed.** If the captured site doesn't determine a field, leave it empty and note it in `unverified_fields`. Don't guess from prior knowledge.
4. **Classify from what you captured**, not from memory. The site is the evidence.
5. **Multi-select fields are ranked.** For `target_market` and `offering_category`, list the best-fit first — most relevant / biggest share of the business. Position 1 is treated as primary.

*No `lifecycle_stage` field on purpose — it's a funding/financials signal you can't read off a marketing site (a deep-research job, not capture).*

*Evolving this list: resist additions. Prefer `Other` + a body note; promote to a real value only when the same gap recurs across companies (per [`BACKLOG.md`](BACKLOG.md)). A new value is missing from every prior profile.*
