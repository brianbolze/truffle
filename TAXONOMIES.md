# TAXONOMIES — the closed value sets

> **What this is.** The exact, closed value lists for the classification fields in [`SCHEMA.md`](SCHEMA.md). A capturing agent picks from these strings verbatim.

> **Why closed (read this first).** These fields exist so companies can be **grouped and filtered across the whole store** — "all B2C subscription brands," "every Software / SaaS company in Finance." That only works if everyone uses the *same* strings. A near-miss value (`SaaS` vs `Software / SaaS`, `D2C` vs `B2C`) silently fragments a group and the aggregation quietly under-counts. So treat these as a fixed vocabulary, not a suggestion. Free, expressive description belongs in the `profile.md` body — not here.

*Scope: commercial companies + products. Every field allows `Other` and allows empty — see the rules at the bottom.*

---

## `entity_type`

*What kind of entity this is — usually `Company`. The other values are graceful flags for non-standard entities, and they gate which other fields apply (an investor has no products; a nonprofit has no business model). Single-select.*

| Value | Means |
|---|---|
| `Company` | An operating business selling products/services (the default) |
| `Investor / Holding` | VC/PE firm, holding company, or conglomerate parent |
| `Nonprofit` | Operates for social benefit, not profit |
| `Government` | Government or public-sector body |
| `Education` | School, university, or research institution |
| `Individual / Creator` | Personal brand, solo creator, or independent |

## `target_market`

*Who the company sells to — the cleanest grouping axis there is, evident from almost any site. Multi-select, best-fit first.*

| Value | Means |
|---|---|
| `B2B` | Sells to businesses |
| `B2C` | Sells to consumers |
| `B2B2C` | Sells through a business to reach end consumers |
| `B2G` | Sells to government / public sector |

## `offering_category`

*What the company sells. **List the primary first**; add a second only for a genuine hybrid (e.g. telehealth = `Services / Consulting` + `Biotech / Pharma Products`). Set `is_multi_product: true` when they span lines.*

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
| `Retail / E-Commerce` | Sells products direct to consumers, online or in-store |
| `Industrial / Manufacturing` | Industrial goods, machinery, large-scale production |
| `Energy / Utilities` | Generates, distributes, or services energy |
| `Non-Profit / NGO` | Operates for social benefit, not profit |

## `is_multi_product`

*Boolean — does the company offer 2+ **distinct** offerings a customer would choose between or buy separately? Distinct in name, page, and positioning — not plans, tiers, or variants of one thing. The test: would someone comparison-shop between them?*

- `true`: Apple (iPhone, Mac, Watch…), Microsoft (Office, Azure, Xbox…).
- `false`: a single-product SaaS, even with Standard/Plus tiers.
- Judgment call: Notion — historically `false` (one app), trending `true` as Notion Mail / Calendar become separately-named offerings, not features.

## `business_model` *(optional)*

*How the company makes money — the primary model if several apply. Often inferable from pricing pages; leave empty if not.*

| Value | Means |
|---|---|
| `Subscription` | Recurring fee (SaaS, membership, DTC refills) |
| `Transactional / One-time` | Pay per purchase, no recurring commitment |
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
2. **`Other` is always allowed**, and better than a forced wrong fit. When you use it, add a one-line note in the body so a human can see what didn't fit — repeated `Other`s are the signal to evolve the taxonomy.
3. **Empty is always allowed.** If the captured site doesn't determine a field, leave it empty and note it in `unverified_fields`. Don't guess from prior knowledge.
4. **Classify from what you captured**, not from memory. The site is the evidence.
5. **Multi-select fields are ranked.** For `target_market` and `offering_category`, list the best-fit first — most relevant / biggest share of the business. Position 1 is treated as primary.

*No `lifecycle_stage` field on purpose — it's a funding/financials signal you can't read off a marketing site (a deep-research job, not capture).*

*Evolving this list: resist additions. Prefer `Other` + a body note; promote to a real value only when the same gap recurs across companies (per [`BACKLOG.md`](BACKLOG.md)). A new value is missing from every prior profile.*
