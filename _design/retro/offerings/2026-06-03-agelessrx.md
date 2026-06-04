# Retro — AgelessRx offerings run (2026-06-03)

One of the first `offerings.md` runs after the module shipped that morning. The artifact landed clean —
[`store/agelessrx-com/offerings.md`](../../../store/agelessrx-com/offerings.md), 51 SKUs + 5 families, lint-pass,
60 credits, every price grep-verified. The contract and lint held up well; what follows is the **generalizable**
stuff worth feeding back, not AgelessRx trivia.

## What worked (validate, don't touch)

- **Roster-first + verbatim-price-grep is the right spine.** The lint fired exactly where it should (see #3) and
  the roster carried the whole answer without leaning on deep blocks.
- **`published | partial | on-request` mapped cleanly.** The "$50 access fee + brand drug bought separately from
  NovoCare/LillyDirect" GLP-1 pattern → `partial` is the same archetype as Hims's membership-stack. Reusable
  across the cohort: *a telehealth access/monitoring fee with the medication priced elsewhere is always partial —
  quote both halves.*

## Generalizable learnings

**1. The enumeration ladder is missing a rung: the CMS REST API.** *(→ recipe)*
The recipe's ladder is index-scrape → `site:` search → `/map`. None of those gave the true catalog here: the
rendered `/treatments/` grid lazy-loaded 47 of "48" cards and carried **zero prices**. The authoritative census
was the WordPress custom-post-type endpoint — `/wp-json/wp/v2/agelessrx_product?per_page=100` — scraped through
Firecrawl (1 credit; raw `curl` ate a Cloudflare 403). It returned the real registry and surfaced **4 offerings
the grid never shows** (BPC-157, TruDiagnostic, Nutrisense, the consult). Takeaway: **when a site is CMS-backed
(WordPress `/wp-json`, Shopify `/products.json`, etc.), the structured backend beats the rendered catalog for
enumeration** — add it as a rung. Caveat in #5.

**2. Price-on-PDP-only sites break the recipe's cost model.** *(→ recipe)*
The module doc estimates ~10–20 credits for a 20-SKU company because "most rows read off 1–2 index + a /pricing
page." That assumes index/category pages carry prices. AgelessRx's index carried none — prices live *only* on
PDPs — so a complete verbatim-priced roster *required* a per-PDP sweep, and cost scaled with SKU count (60
credits). Add a decision rule: **glance at the index — prices present → cheap path; prices absent → budget ≈ one
scrape per SKU.** Family/category pages partly bridge this (they list per-card prices) but didn't cover the flat
tail (peptides, sleep, skin, supplements).

**3. Don't extract price by position or formatting — the canonical price is the hero, not the first bold `$`.** *(→ recipe + capture rules)*
The newest of AgelessRx's **three concurrent PDP template generations** renders the hero "Starting at $99/mo" as
*plain text*, while the first **bolded** dollar amount on the page is a cross-sell carousel card ("NAD+ Nasal
Spray — $125"). Any "first `**$…**`" heuristic misattributes $125 to the $99 SKU. Generalizable: **cross-sell
carousels and "other treatments" modules poison positional extraction; anchor price to the hero block near the
H1, and treat template heterogeneity as expected, not exceptional.** The grep-back lint is what catches the slip
— I hit it live and the lint held.

**4. Two lint sharp-edges, cheap to document.** *(→ lint / authoring note)*
Cost me two fix cycles: (a) a literal `|` inside any roster cell breaks the stdlib column parser **even escaped as
`\|`** — use `·` or `;` between sub-values, never a pipe; (b) a `$N` immediately followed by a letter (`$101M`,
a verbatim XPRIZE prize purse) can't satisfy the lint's `\b`-anchored price-grep, so non-price dollar figures trip
it — elide or avoid quoting `$<num><letter>`. Worth a line in the contract's authoring notes; optionally relax
the lint's `\b` for a trailing `[MmKkBb]`.

**5. The REST/registry census over-returns — dedup is judgment the lint can't enforce.** *(→ recipe)*
69 registry entries → 51 offerings required recognizing **marketing-URL families**: `-mexp###` ad-experiment
landing pages, `shopping-*` Google-feed dupes, `*-direct-to-triage` funnel variants, `*-2` clones. These are the
same SKU at different URLs — counting them would violate "complete at the indexed level, *never every leaf*."
Budget an explicit dedup pass keyed on URL-suffix patterns + duplicate titles before you count.

**6. Don't force a hierarchy a flat catalog doesn't have.** *(→ contract, minor)*
A broad-catalog generalist with two cross-cutting nav axes (by molecule *and* by need) has no clean tree. I used
`family` rows only for the 5 groupings with a real category page and `Parent: —` for the rest. Forcing every SKU
under a synthetic parent would have been false precision.

---

*Status: **discussion, not applied.** Highest-leverage feedback for the module: #1 (CMS-REST rung) and #2
(price-on-PDP cost rule) — both belong in [`firecrawl-capture.md` §1.1](../../../skills/research-company/firecrawl-capture.md).
#3–#5 are smaller capture/lint refinements; #6 is a one-line contract note. Propose to Brian before editing the
shipped recipe/contract.*
