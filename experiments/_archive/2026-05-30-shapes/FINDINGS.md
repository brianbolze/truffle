# Findings — Experiment 3 (more shapes): Nike, AWS, Benadryl

> **Verdict: the lifecycle and the *body* of the SCHEMA held across three deliberately awkward shapes, but this round found the SCHEMA's first real structural GAP — there is no home for an entity's parent / sub-entity / brand-of relationship, and all three captures needed it (AWS→Amazon, Benadryl→Kenvue, Nike→Jordan/Converse).** Two classification fields also broke on these shapes in *new* ways: `business_model` has no value for usage-based/consumption pricing (AWS), and `offering_category` has no value for apparel/footwear (Nike). The two known recurring strains both recurred and are now well-characterized: `is_multi_product` is **only hard in the middle** (trivial at the Nike/AWS scale extremes; the hard case is single-brand-many-forms, Benadryl), and `brand_colors` produced a **third and fourth distinct failure mode** (AWS: the true hue absent from the payload; Nike: ephemeral campaign colors captured as identity). The fed-in playbook again eliminated all self-inflicted waste — **18 credits across all three, zero contamination, zero re-scrapes.**

Run: hand-captures of **nike.com**, **aws.amazon.com**, **benadryl.com**, 2026-05-30. Profiles at [`store/nike-com/profile.md`](../../store/nike-com/profile.md), [`store/aws-amazon-com/profile.md`](../../store/aws-amazon-com/profile.md), [`store/benadryl-com/profile.md`](../../store/benadryl-com/profile.md); payloads + screenshots + cleaned markdown in each `captures/2026-05-30/`. Companion to [first-capture (linear)](../2026-05-30-first-capture/FINDINGS.md) and [breadth (AG1)](../2026-05-30-breadth/FINDINGS.md). **Corpus is now five.**

---

## The five-company corpus

| Company | Shape | entity_type | is_multi_product | What it stress-tested |
|---|---|---|---|---|
| **linear.app** | clean B2B SaaS | Company | `false` (one app, many surfaces) | baseline; JS-walled pricing; client nav |
| **drinkag1.com** | DTC multi-SKU CPG | Company | `true` (flagship + companions) | geo/cache contamination; map noise; offerings.md |
| **nike.com** | enormous catalog, media/JS-heavy | Company | `true` (scale extreme) | **un-enumerable catalog; parent-of sub-brands; apparel has no offering_category** |
| **aws.amazon.com** | 240+ services, deep nav, a division | Company | `true` (scale extreme) | **subsidiary boundary; usage-based has no business_model; IaaS strains "SaaS"** |
| **benadryl.com** | single product brand, marketing-only | **Other** | `false` (one molecule, many forms) | **brand-of-a-parent; non-transacting site; entity_type itself** |

The first two were "does it generalize?" (yes). These three were "where does it *break*?" — and they broke in informative, mostly-structural places, not in the body prose, which held everywhere.

---

## THE headline finding: no home for parent / sub-entity / brand-of relationships

All three captures are non-top-level entities, and the SCHEMA could not express the link to their parent. This is the experiment's main result.

| Capture | Relationship | Kind | entity_type call |
|---|---|---|---|
| **AWS → Amazon** | `subsidiary-of` (legal entity *Amazon Web Services, Inc.*) | operating subsidiary | **Company** (it runs as a business — own P&L/brand/domain) |
| **Benadryl → Kenvue** | `brand-of` (*"published by Kenvue Brands LLC"*) | product brand, not a company | **Other** (a brand is not an operating company) |
| **Nike → Jordan / Converse / ACG / NikeSKIMS** | `parent-of` (inverted) | parent owning child brands | **Company** (clean top-level parent) |

**The gap.** There is **no frontmatter field** for a parent / subsidiary / brand-of / owns relationship. `aliases` is the wrong tool (it's for alt *names/domains of the same entity* — a rebrand/M&A escape hatch — not a different entity). So the link to Amazon / Kenvue / Jordan exists nowhere queryable.

**How I worked around it (per the brief — flagged, not invented):**
- A commented `# NOTE — parent: … relationship: …` block at the top of the identity frontmatter (human-readable, not a real field).
- Stated in `description`, an **Overview** paragraph, and `site_notes`.
- Verified from the page, not memory: each parent came straight from the footer (`© Amazon Web Services, Inc.`; `© Kenvue Brands LLC`; `NIKE, Inc.` on investors/about subdomains).

**Why it matters / two-sided.** The relationship is missing in **both directions**: a consumer querying "what does Kenvue own?" or "is aws.amazon.com part of amazon.com?" gets nothing structural. And **domain-as-key holds but can't express containment**: the store could hold `amazon.com` *and* `aws.amazon.com` (or `kenvue.com` and `benadryl.com`) as distinct, valid, unique keys with **nothing linking them**. The key discipline is fine; the relational expression is the hole. This is exactly the "relations follow the same rule — markdown is the ledger" idea in the architecture doc, but there is **no frontmatter convention for it yet** (the architecture *describes* relations-as-frontmatter-reference-lists; the SCHEMA doesn't *define one*). That's the actionable gap. (Not inventing the field here — logged to BACKLOG as a `[weakness]` with 3 sightings.)

**entity_type is the secondary casualty.** The closed set (`Company / Investor / Nonprofit / Government / Education / Individual`) has **no "Brand"**. Benadryl is genuinely not a company, so it took `Other` — a deliberate, documented use of the escape hatch (per TAXONOMIES, "repeated `Other`s are the signal to evolve the taxonomy"). The useful nuance the corpus reveals: **a subsidiary that operates as a business (AWS) is cleanly `Company`; a product brand (Benadryl) is not** — same parent-gap, different entity_type answers. Don't collapse them.

---

## Two NEW classification-field strains (beyond the known recurring ones)

1. **`business_model` has no value for usage-based / consumption pricing — AWS.** AWS is pay-as-you-go metered consumption (+ optional Savings Plans / Reserved commitments). None of the closed values fit: `Subscription` implies a *fixed* recurring fee; `Transactional / One-time` implies *no* recurrence. Used **`Other`** + a note. This isn't AWS-specific — it's the whole consumption-priced cohort (Snowflake, Twilio, OpenAI/Anthropic APIs, most cloud infra). A recurring gap worth a `Usage-based / Consumption` value *if it shows up again* (1 sighting so far — flag, don't add).

2. **`offering_category` has no value for apparel / footwear / fashion — Nike.** A global apparel & footwear maker-brand-retailer has nowhere clean to land: `Hardware / Physical Products` means *devices/equipment*; `CPG` means *frequently-replaced packaged consumables*; `Retail / E-Commerce` describes the *channel*, not the *goods*. Led with `Retail / E-Commerce` (what `nike.com` literally is) + `CPG` as a consumer-goods proxy, and flagged the missing "Apparel & Footwear / Consumer Durables" value. This is a **worse version of AG1's CPG↔Retail straddle** — there, both proxies were defensible; here, *neither* names what Nike makes.

   - **Adjacent minor strain (Nike):** `primary_industry` single-select forces a choice between the structural sector (`Consumer Goods`) and the domain flavor (`Sports & Recreation`) — both true, only one slot. Chose Consumer Goods, noted the alternative.
   - **Adjacent minor strain (AWS):** `offering_category: Software / SaaS` is the closest value but AWS is **infrastructure (IaaS/PaaS)**, not application-SaaS — no "Cloud Infrastructure" value. Minor; noted.

---

## The two known recurring strains — now well-characterized

### `is_multi_product` — confirmed: only hard in the middle

Five data points now map the whole field:

| Resolution | Companies | Why |
|---|---|---|
| `false` | linear (one app, many *surfaces*) · **benadryl (one molecule, many *forms*)** | one thing, expressed many ways |
| `true` | AG1 (flagship + *named companions*) · **nike & AWS (*scale extremes*)** | distinct, separately-bought offerings |

**The lesson:** the field is **trivial at the extremes** — Nike (thousands of SKUs) and AWS (240+ services) are obviously `true`; a one-product SaaS is obviously `false`. It is **only genuinely hard in the middle**, and the corpus now has both middle cases: AG1's *flagship-plus-companions* (`true`) and **Benadryl's *single-brand-many-forms* (`false`)** — one antihistamine molecule (diphenhydramine) sold as oral tablets/gels/liquids *and* topical creams/sprays/sticks. Benadryl is the **closest-to-the-line `false`** in the corpus: oral-vs-topical are arguably distinct product types, but they share one active ingredient, one brand, no sub-brand split (contrast AG1→AGZ earning its own name). The TAXONOMIES test ("would you comparison-shop them?") resolved it, but the tie-breakers it leans on (Notion precedent for SaaS surfaces; "flagship + named companions ⇒ true" for AG1) now want a **third cue: "one brand / one core ingredient, many delivery forms ⇒ `false`."**

### `brand_colors` — a third and fourth distinct failure mode

The instability is now overwhelming — five captures, **four different ways `branding.colors` misleads:**

| Capture | `primary` is… | Failure mode |
|---|---|---|
| linear | body **text** gray (#D0D6E0) | brand hue hidden in `accent` |
| AG1 | a **true** brand green (#0C3D3D) | inverts linear — `primary` *is* the hue |
| benadryl | a **true** brand hue (#D21F62 magenta) | (confirms AG1 — no positional rule) |
| **AWS** | dark-slate UI chrome (#232B37) | **the true brand hue (#FF9900 Smile orange) is ABSENT from the payload entirely** |
| **Nike** | the real brand color (#111 black) | **`secondary`/`accent` are EPHEMERAL campaign colors (volt #BAD168, orange #FF7334), not identity** |

**The two new modes are the worst yet.** AWS shows `branding.colors` can **omit the actual brand color** (the orange Swoosh-equivalent never appears — it captured only the slate+blue UI). Nike shows `branding.colors` is a **snapshot of the current page**, so a brand that re-skins seasonally (the "TOMA" volt event, a red Jordan hero) gets ephemeral campaign colors recorded as if they were brand identity. **Conclusion (strengthening AG1's open question): there is no positional *or* presence guarantee** — `branding.colors` is neither reliably "the brand color in slot X" nor reliably "contains the brand color at all." The only safe approach is the current one: **retain the palette, vision-confirm against the screenshot, and write the real read in prose.** Any heuristic that auto-picks a slot is wrong.

---

## Where the SCHEMA generalized cleanly (the reassuring half)

- **The entire body** (Overview, What they offer, How it works, Positioning, Nav structure, Credibility, Visual & brand impression, Strategic read, Provenance) carried all three shapes without strain — prose flexes exactly where the enums can't. The "describe the company, not what it means to you" line held: nothing tempted a judgment/vertical field.
- **`is_multi_product` body-note discipline** absorbed every hard call.
- **Breadth-first offering capture** (the doro rule) is the right and *only* tool at Nike/AWS scale — capture the **shape** (gender × type × sport × franchise for Nike; category × flagship-service for AWS), never the SKU list. This is where `offerings.md` would matter most and where it must stay breadth-first.
- **`aliases`, `key_pages`, `unverified_fields`, capture-meta, `description`** all generalized. `unverified_fields` did real work flagging *by-design* absences (Benadryl has no pricing; AWS's catalog is JS-walled) — distinguishing "couldn't get" from "doesn't exist here," which matters.
- **`color_scheme`, `fonts`** were reliable (notably `fonts[0]` was *correct* for AWS/Nike, *wrong* for Benadryl where generic `sans-serif` ranked first — so still verify, but it's usually right).

---

## New capture hazards (beyond the linear + AG1 punch lists)

1. **Map explosion at extreme scale — now with two new flavors.** AG1's 485-URL funnel-noise was just the start. **AWS (~300 URLs)** is dominated by a *separate docs host* (`docs.aws.amazon.com`), `/blogs/*`, `/marketplace/*`, and ~15 locale prefixes — the map is **near-useless for key-page selection**; navigate by *known paths* instead. **Nike (~286 URLs)** returns a *random PDP/browse sample* across ~12 locale prefixes (`/be/ /ph/ /ie/ /ro/ /au/ ...`) + corporate subdomains (`about.` `investors.` `careers.` `niketeam.`) + sitemap XMLs — **useless for completeness but GOLD for revealing the taxonomy** (the `/w/` facet URLs *are* the browse tree). **New guidance:** for hyperscale sites, treat map as a *taxonomy-revealer*, not a page-inventory; select key pages by known path + the footer.

2. **JS-walled *catalog* at scale (new — distinct from linear's JS-walled *pricing*).** Both big sites hide the catalog behind client-side rendering: **AWS `/products/`** renders only the first alphabetical page (Amplify…AppSync) behind a "Search All AWS Products" filter; **Nike** browse pages lazy-load (one franchise hub = 73 tiles, partial). **You cannot scrape the full catalog** — and shouldn't try. Capture the **category/franchise shape**, grounded in the footer + facet links + a couple of representative pages. The homepage **footer** was again the most reliable taxonomy source (true for linear, AG1, AWS, *and* Nike).

3. **`branding.colors` can omit the brand color entirely (AWS).** See the table above — a real failure mode, not just slot-ambiguity. Always confirm against the screenshot; be willing to *add* the true hue from the visual with provenance (I added Nike/AWS orange manually, noted).

4. **Non-transacting marketing site (Benadryl).** A CPG/OTC brand site that **sells nothing** — no cart, no prices, "Where to Buy" → a (client-rendered) retailer locator. There is simply **no pricing or business-model signal to capture**, and that's *correct*, not a miss — record it in `unverified_fields` as by-design. A genuinely different site-type from the DTC (AG1) and SaaS (linear) storefronts where the site *is* the store.

5. **`branding.designSystem.framework` is reliably wrong — now 4/5.** linear "custom" (Next.js), AG1 "bootstrap" (Next.js), AWS "custom" (React), **Nike "bootstrap" (Next.js)**, benadryl "unknown" (Next.js). It has **never once been right** across the corpus. Hard rule, not a quirk: **ignore `branding.designSystem.framework`; read the framework from `rawHtml`** (`__NEXT_DATA__`, `/_next/`, react markers). `branding.images.logo` was also an inline data-URI SVG or empty on 4/5 (linear, AWS, Nike, benadryl) — the favicon fallback chain is load-bearing every time.

---

## Firecrawl credits

**18 total, all clean** (zero wasted — the playbook eliminated every self-inflicted re-scrape that cost linear and AG1):

| Capture | Credits | Breakdown |
|---|---|---|
| **benadryl.com** | 7 | 1 map + 6 scrapes (homepage full pass + products hub + adult + topical + compare + where-to-buy) |
| **aws.amazon.com** | 7 | 1 map + 6 scrapes (homepage + /products + /what-is-aws + /pricing + /ec2 + /s3) |
| **nike.com** | 4 | 1 map + 3 scrapes (homepage + /men + Air Force 1 hub) — economical *because* the mandate was shape-not-SKUs |

- **Zero contamination, zero re-scrapes, zero geo-misroutes.** Applied `location:{country:US}` + `maxAge:0` + `waitFor:3000-5000` + **serial** (no parallel bursts) prophylactically from the start — the AG1 hazard never fired. The content-md5 dedup check ran on every batch and was clean throughout.
- **Nike proves the shape-first discipline is also cheap:** a 4-credit capture produced a complete portfolio shape for a company with thousands of SKUs. The cost lever for huge catalogs is *not scraping more* — it's the breadth-first mandate.
- All formats rode the 1-credit/page base (markdown + links + screenshot together; homepage added html/rawHtml/branding for free).

---

## Caveats

- Five fixtures now, all hand-run, all on 2026-05-30 (US locale). The lifecycle holds across SaaS / DTC-CPG / mega-catalog-retail / cloud-platform / OTC-brand. The relationship gap is confirmed at **3 independent sightings** (well past the BACKLOG ≥2 bar) — the strongest system-level signal the project has produced.
- I **deliberately used `Other`** twice (Benadryl `entity_type`, AWS `business_model`) rather than forcing a wrong closed value — consistent with the TAXONOMIES rule that `Other` + a note is better than a bad fit and that repeated `Other`s are the evolution signal. Both are flagged, not yet promoted (per "resist additions").
- Per the brief, I **flagged the relationship gap, did not invent a field.** A candidate convention (frontmatter `parent:` / `owns:` as domain-keyed reference lists, exactly mirroring a Notion relation property and the architecture's "markdown is the ledger" line) is the obvious next step but belongs in a SCHEMA decision, not this probe. Logged to [`BACKLOG.md`](../../BACKLOG.md).
- Nike's catalog is intentionally **not enumerated**; women's/kids' sub-structure was inferred from the men's hub + footer (the footer Kids block confirms the mirror). AWS's 240+ services are **not enumerated** (JS-walled); only the category shape + flagship services, grounded in captured pages.
