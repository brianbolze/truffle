# Findings — `offerings.md`, grounded in 5 real product pages

> **What this probe contributed.** Hand-captured one product page across five shapes and read Doro's
> product field-menu (`core/schemas/products.py`) down against them. Empirical result: **"beyond price,"
> the attributes that recur on a real offering page are a small generic core of ~9** (`name` · `parent`
> · `url` · `what` · `price` · `price_visibility` · `includes` · `audience` · `notes`); **price is one
> of nine, not the point.** The rest of Doro's menu either **doesn't generalize** (specs are
> shape-specific) or **fails our line** (judgments/events). And **`price_visibility` survived two shapes
> the earlier cohorts hadn't tested** (marketplace, usage-metered).
>
> *The full design synthesized from these findings (+ the breadth/identity/structure discussion + Doro
> prior art) lives in [`../../_design/2026-06-01-offerings.md`](../../_design/2026-06-01-offerings.md).
> This file is just the evidence.*

*Method: one fresh Firecrawl page per shape (5 credits) — telehealth (hims `/weight-loss`), luxury
catalog (rolex Daytona), usage-metered (twilio SMS pricing), marketplace (uber offerings), SaaS (notion
pricing). Cleaned captures in [`captures/`](captures/). Pricing conclusions **not re-derived** — settled
in [`../2026-05-31-consumption-affordance/FINDINGS.md`](../2026-05-31-consumption-affordance/FINDINGS.md).*

---

## 1. The attribute matrix — what generalizes, what doesn't, what's cut

Reading Doro's ~15 product fields down the five real pages, attributes sort into three tiers:

**Generic core — generalizes across all 5.** `name`, `parent` (hierarchy within the company), `url`,
`what` (one-line), `price` (verbatim; the *field* is universal even when the value is absent),
`price_visibility`, `includes` (bundle/features/specs as a list), `audience` (**per-offering ≠ company
`target_market`** — Uber's one page targets rider/driver/merchant/business), `notes` (verbatim
catch-all). These nine are the answer to "what besides price."

**Shape-specific — does NOT generalize → `notes` / project-side.** telehealth: molecule, pill/pen/vial,
dose, branded-vs-compounded, FDA status, the two-part membership stack. watch: case size, material,
reference #, `launched_year` (1963 — on Rolex, absent on the other four). usage: the rate card itself
(per-unit table + CSV). The matrix proves these share **no column** — they're the "heavy per messy
vertical" detail the consumption findings already scoped project-side.

**Cut — Doro fields that fail our line.** `competitor_list` (a **judgment** — consumer-owned); `status`
(a marketing site only shows "active"; deprecation is an **events** signal — Notion's "Beta" tag →
`notes`, not a field); `launched_year` (shape-specific); `granularity_class` (capture discipline, not a
stored attribute); `icon_url` (low query value). `archetype` (a per-offering `offering_category`)
deferred until a multi-archetype conglomerate needs it.

Net: Doro's ~15 → **9 generic-core**, rest cut/deferred.

## 2. `price_visibility` survives the two new shapes

The earlier cohorts (SaaS/telehealth/watches) settled `price_visibility` (`published | on-request |
partial`) as the one universal per-offering field. The two shapes they hadn't tested confirm it:
**marketplace (Uber)** — rides carry no list price → `price` empty, `on-request` is the honest fact (a
take-rate is a `business_model` fact, not an offering price); **usage-metered (Twilio)** — `published`
as a rate card with a `Contact sales` enterprise tail. Three states absorb both without a fourth. Still
per-offering, still not inferable from frontmatter: Rolex (`on-request`) and Notion (`published`) are
identical up top; only the offering field separates them.

## 3. Breadth ranged from 1 to un-enumerable — the variance the design must absorb

Across the five, the offering set ranged from one thing (Notion's product, tiers as price detail) to a
hub indexing many (Uber's `/about/uber-offerings/` is itself an offerings index) to un-enumerable
(Rolex is a catalog of references with no per-item price). This is the empirical seed for the design's
breadth handling — capture the **set** when enumerable, the **shape** when not — and for keying
offerings by their page **slug** (every captured page had one; it's the natural within-company key). The
worked-out model is in the design doc.

---

*Captures: [`captures/`](captures/) (5 cleaned pages). Spend: 5 credits. Throwaway `_exp-*` store slugs
used for capture, since removed.*
