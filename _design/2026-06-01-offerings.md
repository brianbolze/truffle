# Design: `offerings.md` — the per-offering record

> **What this is.** The design for the Tier-1, opt-in `offerings.md` module — a company's product /
> service index, one record per offering. It fills the stub in [`../SCHEMA.md`](../SCHEMA.md) ("Tier-1
> modules"). Grounded in a 5-shape hand-capture probe
> ([`../experiments/2026-05-31-offerings-design/`](../experiments/2026-05-31-offerings-design/)) and in
> Doro's product schema ([`references/doro-product-analysis-prompt.md`](references/doro-product-analysis-prompt.md)
> + `core/schemas/products.py`), pruned to the anti-Doro line. **Not yet codified into SCHEMA or the
> verb** — this is the contract; activation is §6.

> **⤳ Superseded on activation (2026-06-03).** The [tournament](../experiments/2026-06-03-offerings-tournament/FINDINGS.md)
> resolved §Activation (**build it**, store-only) and **revised the body shape**: roster-first, deep
> blocks *earned* not default, molecule kept in `What` (the molecule-pivot was probed and rejected). The
> 9-field core + `portfolio_shape` dial below still hold — read this for the field derivation, then
> [`2026-06-03-offerings-module.md`](2026-06-03-offerings-module.md) for the current shape, recipe, and verdict.

*Companion to [`2026-05-29-frame.md`](2026-05-29-frame.md) (scope) and [`2026-05-30-architecture.md`](2026-05-30-architecture.md)
(lifecycle). Pricing rationale is settled separately in
[`../experiments/2026-05-31-consumption-affordance/FINDINGS.md`](../experiments/2026-05-31-consumption-affordance/FINDINGS.md);
this doc treats price as **one field of nine**.*

## The frame: offerings are state, keyed within the company

An offering is durable **state** — what the company sells, from its own pages — not events or
judgments. The engine owns it; relevance/threat/"is this a competitor" stay consumer-side (the
`competitor_list` cut, below).

**Identity — keyed within the company by slug; grouped across companies at query time.** A company is
easy: the domain is a unique, free key. An offering has no such global key — so we don't invent one. A
dedicated marketing page gives an offering a stable key *within* the company (`domain` + its **slug**,
the same slug stored as the relative `url`). What's genuinely missing is a *cross-company canonical* key,
and we make **no claim** that hims's `/weight-loss/wegovy-pill` is Eden's "Wegovy." Cross-company
grouping ("semaglutide across brands") is **query-time**, on a shared attribute (the molecule), by the
consumer/project — never stored or reconciled. An offering with no page of its own (a feature named only
in prose, a catalog leaf) has no key and lives inline. This is the same move that let us skip company
entity-resolution: **decline the problem rather than build the machinery.**

> **Why no `granularity_class`** (Doro's suite/model/sku/plan enum). Doro needed it to resolve product
> *references from unstructured sources* (a transcript's "Office" vs "Excel"); that's the
> entity-resolution the Frame refuses. We capture one company's own site in one pass and never
> reconcile, so "what level" is a capture-time judgment recorded by `parent` + heading nesting, not a
> stored resolution key. The one useful distinction it carried — **family vs buyable** — survives as a
> `notes`/roster annotation, not a regulated field (mostly derivable from `parent` + nesting anyway).

## Granularity, breadth, completeness vs depth

Offering breadth varies by orders of magnitude (Nike's thousands vs Linear's one). Three rules tame it:

**1. Breadth reduces to one binary — is the offering set enumerable? — and `portfolio_shape` already
encodes it.** `Single` / `Flagship + companions` / `Multi-product` → enumerable, capture the set
(Linear, Eden, Tesla, hims). `Catalog` → not, capture the *shape*: categories + flagship exemplars
(Nike, AWS, Rolex), never the SKUs. The dial is upstream, already on the company. **Treat it as
directional, not strict** — the agent uses judgment, and if a deep dive contradicts the field it
**writes the correction back to `profile.md`** (capture improving classification, like `site_notes`
carry-forward).

**2. Completeness and depth are two independent dials, not one.** A *roster* of existence
(name/slug/url) and a set of *rich blocks* move separately: hims → want **every** SKU's existence but
deep detail on only ~top 10; Linear → "one product," but the signal is its **features / surfaces**
(Issues, Projects, Cycles…), which a single block would throw away.

**3. The unit of a deep block is the marketed component worth understanding** — at whatever level holds
the signal (a product, a line, *or* a feature/surface), not strictly a buyable SKU. The comparison-shop
test ("would a buyer treat these as different things?") draws the boundary, accepted as fuzzy because
nothing reconciles captures into canonical entities.

## The record

A separate opt-in doc, own `captured_at` (pricing goes stale fast — the reason it's its own module).
Because it holds **N offerings**, **frontmatter is doc-meta only**; the offerings live in the body in
three parts — **rich content first, the long list last**: `## Portfolio overview` → `## Deep blocks` →
`## Roster`.

```markdown
---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: hims.com            # company key; each offering's slug (the relative url) is its key *within* hims
captured_at: 2026-06-01     # → captures/<date>/ holds the source pages + payloads (provenance lives there)
---

## Portfolio overview
<interpretive, once: how the lines relate + the breadth-first hierarchy. For `Catalog` this is the
main content; for `Single` a sentence or skipped.>

## Deep blocks
<selective — a rich block for the top N (flagships / most-compared). A short bold-led spine anchors it;
then structure LOOSENS and verbatim snippets are the point.>

### Wegovy® (Pill)
- **parent:** Weight Loss
- **url:** /weight-loss/wegovy-pill          # relative to domain; base derived, never repeated
- **price:** From $149/mo†
- **price_visibility:** published

> **H1:** "The GLP-1 pill is here." — "Weight loss that works"
> **Price (verbatim):** "From $149/mo† — † Price includes medication only, if prescribed. An active Hims
> Weight Loss Membership is required ($39 for the first month, auto-renews at $149/month thereafter)."

Oral semaglutide GLP-1 for chronic weight management. Branded (Novo Nordisk), FDA-approved, Rx, not in
all states. Includes Care Team + nutrition guidance via membership. ("From" = starting dose, not fixed.)

## Roster
<complete *at the indexed level*, light — one row per offering. A table, below the deep blocks because
it can run long. Add `Visibility`/short `Price` columns to make those complete across *all* offerings.>

| Offering | Kind | Parent | Slug | What |
|---|---|---|---|---|
| Weight Loss | family | — | /weight-loss | GLP-1 weight-loss program |
| Wegovy Pill | buyable | Weight Loss | /weight-loss/wegovy-pill | oral semaglutide |
| Zepbound Vial | buyable | Weight Loss | /weight-loss/zepbound-vial | tirzepatide injection |
```

### The generic core — 9 fields

The first six are the **spine** (always present — they are the roster columns and lead every deep
block); the last three are **earned** (only with signal — they live in the deep-block prose). All are
**body** lines, never frontmatter. `Kind` (family | buyable) is a roster annotation, not a field.

| Field | | What | Notes |
|---|---|---|---|
| `name` | spine | the offering's name (the `###` heading / roster row) | what the company calls it; not globally unique |
| `parent` | spine | the line/family it belongs to within the company | hierarchy; `—` if top-level |
| `url` | spine | relative slug — **the within-company key** | relative to `domain`; absolute only cross-host (Uber Eats → `ubereats.com`) |
| `price` | spine | verbatim price string, or `—` | never normalized; footnotes quoted in the block |
| `price_visibility` | spine | `published \| on-request \| partial` | the one closed set; the universal queryable axis (§ Price) |
| `what` | spine | one-line description | the existence value (roster) / lede (block) |
| `includes` | earned | what's bundled — features / specs / components | the "what else beyond price" meat |
| `audience` | earned | who this offering targets | **per-offering ≠ company `target_market`** (Uber: rider/driver/merchant/business) |
| `notes` | earned | verbatim catch-all for shape-specific detail | molecule/form, material/size, rate-card, A/B caveat, family-vs-buyable |

**Deep blocks: spine anchors, then verbatim is gold.** Below the spine the structure is the agent's
call, and the value lives there — quote the page **H1 verbatim**, the **exact price string with its
footnotes**, taglines, regulated claims, key `includes`/`audience` (SCHEMA: *"quote verbatim anything
claim- or price-bearing"*). A blockquote per snippet keeps it source-exact and greppable.
`rg '^- \*\*price_visibility:'` enumerates visibility across the deep blocks.

**Roster completeness is bounded by enumerability, not absolute** — "complete" means complete *at the
level the company is indexed at*, never every leaf. hims's SKUs are ~enumerable, so list them all; Nike
/ Amazon are not — their roster is complete at the *category/line* (Amazon: *business-unit*) level +
exemplars, and per-SKU leaves stay on the page. The roster stops where the catalog begins.

**`portfolio_shape` only suggests the mix** — completeness fills the Roster, depth fills the Deep blocks:

| Shape | Overview | Roster | Deep blocks |
|---|---|---|---|
| `Single` (Linear) | brief | the surfaces/features, light | deep on the **surfaces**, not "one product" |
| `Flagship + companions` (Notion) | brief | flagship + companions | flagship big, companions small |
| `Multi-product` (hims, Tesla) | maps the lines | **every** product/SKU | top-N rich |
| `Catalog` (Nike, AWS, Amazon) | **the main content** | categories/units + exemplars | a few flagship exemplars |

## Price is one field of nine

The earlier cohorts retired any company-level pricing field: the price *value* never generalizes (watch
MSRP vs SaaS seat vs telehealth all-in share no unit), so it stays a **verbatim** body string, with
heavy numeric normalization left **project-side, per messy vertical**. The one thing that does
generalize is per-offering **`price_visibility`** (`published | on-request | partial`) — the answer to
"can I even get a price?", common to SaaS sales-gating, telehealth quiz-walls, and luxury price-on-
request. It must be **per-offering, never a company scalar** (Cartier publishes jewelry, gates watches).
Full rationale: the [consumption-affordance findings](../experiments/2026-05-31-consumption-affordance/FINDINGS.md).

**Deliberately absent:** no `pricing_model`, no `{unit,value,cadence}` struct, no per-SKU catalog rows,
no `competitors` / `status` / `launched_year` / `granularity_class` fields, no YAML offerings list, no
`source_pages` list (per-offering urls + `captures/<date>/` are the provenance). Tiers are *price detail
on one offering* (Doro: "a pricing plan is not a product"). A parse-clean YAML offerings list buys
little while the price value is a verbatim string anyway — revisit only if a rung-3 index consumer
appears (it can parse the bold-led body, or we add YAML then).

## Activation — open

The schema above is the contract; *whether to write the file* is not yet settled. The likely shape:
**single-offering companies** fold a `price_visibility` token into `profile.md`'s *What they offer* line
(no `offerings.md`); the doc earns its existence for **multi-offering companies where
price/visibility/audience vary** (Cartier, Uber, hims, Twilio), written when a project enables the
module or offering-comparison is the live query (telehealth cohort first). "Earn every piece of
structure": the convention is worth defining now; the 40 files are not, yet. When activated, wire the
pointer from SCHEMA's Tier-1 stub here and add `offerings.md` linting to `fc.py` / `querycheck.py`.

## Deferred
- **`archetype`** (per-offering `offering_category`) — revisit only for a multi-archetype conglomerate.
- **molecule / `alt_names` per offering** — the cross-brand join key is vertical-specific → `notes` for now.
- **Catalog per-SKU depth** — out of scope by design; index at model/category level.
- **family vs buyable as a real field** — a `notes`/roster annotation unless a consumer query needs it machine-separable.

---

<sub>**Sources** — the 5-shape capture probe ([experiment](../experiments/2026-05-31-offerings-design/FINDINGS.md));
Doro `core/schemas/products.py` + the product-analysis prompt ([reference](references/doro-product-analysis-prompt.md));
the price conclusions ([consumption-affordance](../experiments/2026-05-31-consumption-affordance/FINDINGS.md)).
Authored 2026-06-01.</sub>
