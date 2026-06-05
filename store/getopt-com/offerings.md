---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: getopt.com           # company key; each offering's slug (its relative url) is its key *within* Opt Health
captured_at: 2026-06-04       # own freshness; roster ← captures/2026-06-04/
enumeration: lines-omitted    # men's memberships + TRT/ED/peptides reached; women's-vertical pricing/protocols + dedicated weight-loss/hair-loss pages NOT captured — see scope note
site_notes: "Membership-centric catalog, NOT a per-SKU storefront (contrast Hone). The 3 priced tiers live on /memberships (server-rendered, clean). Treatments are gated: TRT's price IS the Optimization/Longevity membership floor ($245/$645 + a one-time lab fee); peptides/ED/weight-loss are 'contact us to inquire' or in-app (on-request); supplements/micronutrients are bundled by tier (Foundation ≤2, Optimization ≤3). NO per-SKU PDPs with prices exist — molecules come from the /learn/protocols/* education pages + the /memberships 'Unique treatments' grid. The parallel WOMEN'S vertical (/women/*) mirrors the model with its own /women/memberships + protocols — not captured this run. Live commerce + per-treatment pricing sit behind app.getopt.com (signup). WordPress/WP Engine; no A/B-test instrumentation observed, but treatment availability/pricing is gated so treat the public roster as a floor."
---

## Portfolio overview

Opt Health (getopt.com) is a **concierge, membership-based** men's-led telehealth optimization clinic, and its
catalog is shaped unlike a typical DTC pharmacy: **the priced unit is a 3-tier membership**, and specific
treatments are **personalized and tier-gated** rather than sold as individually-priced SKUs. So the roster has
two layers: (a) the **3 membership tiers** — the only fully **published** prices — and (b) a **treatment menu**
(TRT, peptides, ED, weight-loss, supplements, women's HRT) that is **`on-request` / `partial`**, gated behind a
membership + a video physician consult, with medication pricing exposed only in-app (`app.getopt.com`) or via
"contact us." There are **no per-SKU PDPs** here (the contrast with the Hone twin, whose every SKU has a priced
PDP) — molecule/form is page-attested from the `/learn/protocols/*` education pages and the `/memberships`
"Unique treatments" grid.

**Shape finding #1 — the membership IS the product; the treatment is the gate's reward.** Three tiers, each
priced med-exclusive with a **one-time intake + lab fee** on top, and each *unlocks* a widening treatment scope
rather than itemizing it: **Foundation $95/mo** (labs + consult + up to 2 supplements; med *ordering* at extra
fees), **Optimization $245/mo** ("MOST POPULAR"; adds *included* specialized prescriptions + 2 membership meds +
3 supplements), **Longevity $645/mo** (adds epigenetic/biological-age testing + a 90-min consult). The flagship
**TRT is explicitly gated to Optimization+** — its quoted price *is* the membership floor ("starting at $245 per
month plus a $195 initial lab fee"), so it's `partial`, not a standalone SKU price.

**Shape finding #2 — peptides are the deepest line, and they're all `on-request`.** The peptide menu is the most
enumerable treatment line — **"over a dozen peptides," 9 named on the page** (Sermorelin, PT-141, Semaglutide,
Oxytocin, GHK-Cu, VIP, Pinealon, Hexarelin, 5-amino-1MQ) — but it carries **no prices** ("please contact us to
inquire about pricing"). Notably Opt files **Semaglutide (GLP-1) under *peptides*, not a separate weight-loss
SKU line**, and **PT-141 under peptides** rather than sexual-health. This is the compounded/specialty lane of
the `both` compounding posture (see telehealth.md).

**Shape finding #3 — molecules are thinly attested.** Because there are no PDPs, molecule grain is coarse:
**testosterone** with **ester not stated** (no cypionate/enanthate named anywhere), **ED = "PDE5 inhibitors"**
with **no specific molecule** (sildenafil/tadalafil never named), and the supplement/micronutrient grid names
items without dose. Only the peptide names and **Semaglutide → GLP-1** are cleanly page-attested.

**Prominence (calibrated).** **Optimization is the pushed tier [HIGH]** — the only one badged **"MOST POPULAR."**
**TRT is the flagship treatment [HIGH]** — the #1 "Popular" footer link, the first Protocols nav entry, and the
men's-health core. **Peptides read second [MED]** (the #2 "Popular" link; the deepest named menu). **Longevity
tier is positioned as the premium ceiling [MED]** (highest price, epigenetics). Card order within the treatment
grid is **[LOW]** (a rotating/illustrative grid, not a ranked catalog).

## Roster

Complete at the indexed level for the **men's** memberships + TRT/ED/peptides; the women's vertical and the
weight-loss/hair-loss program-goal lines are present but under-enumerated (see Provenance). Within-company key =
**Slug** (relative URL, quoted; the membership tiers share `/memberships` as there are no per-tier URLs).
Prices quoted verbatim; **every `$` here is greppable** in `captures/2026-06-04/memberships.md` or `…/trt.md`.
Molecule/form is **page-attested only**, never inferred. An offering here is never asserted equal to a
same-molecule offering at another brand.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Memberships** | family | — | `/memberships` | — | — | The 3-tier concierge subscription — the priced core that gates all treatment. Each is med-exclusive, "+ a one-time intake + lab fee." |
| Foundation | buyable | Memberships | `/memberships` | `$95` `/month` (after a one-time `$195` intake + lab fee) | published | not a drug — concierge membership · 55+ biomarker labs + a 60-min MD consult + plan + up to 2 supplements shipped 4×/yr + Performance-Score app; medication *ordering* available at "additional fees." |
| Optimization | buyable | Memberships | `/memberships` | `$245` `/month` (after a one-time `$195` intake + lab fee) | published | "MOST POPULAR" · everything in Foundation + up to 3 supplements + 2 membership medications + **specialized prescriptions included** (hormones, weight loss, fertility, sleep/energy); 4×/yr follow-up labs. This is the tier TRT requires. |
| Longevity | buyable | Memberships | `/memberships` | `$645` `/month` (after a one-time `$695` intake + lab fee) | published | everything in Optimization + 65+ biomarkers + **epigenetic / biological-age testing 2×/yr** + a 90-min consult + discounted CAC/cognitive/leaky-gut/heavy-metal tests. |
| **Hormone optimization / TRT** | family | — | `/learn/protocols/testosterone-replacement-therapy` | — | — | Men's flagship treatment line; gated to Optimization+ tiers. |
| Testosterone Replacement Therapy | buyable | Hormone optimization / TRT | `/learn/protocols/testosterone-replacement-therapy` | `starting at $245 per month plus a $195 initial lab fee` | partial | **testosterone** (ester **not stated**) · injection / oral pill / topical cream · membership-gated (Optimization or Longevity) + labs + video consult; the quoted price is the membership floor, med fees may sit on top. [anchor: trt-price] [anchor: molecule] |
| **Peptide therapy** | family | — | `/learn/protocols/peptide-therapy` | — | — | "Over a dozen peptides," 9 named on the page; **"contact us to inquire about pricing"** → all `on-request`. Administered via injection, nasal spray, or oral. [anchor: peptide-price] |
| Sermorelin | buyable | Peptide therapy | `/learn/protocols/peptide-therapy` | — | on-request | **sermorelin** — "directly stimulates growth hormone production" (GHRH-analog peptide) · injectable or oral · gated. |
| PT-141 | buyable | Peptide therapy | `/learn/protocols/peptide-therapy` | — | on-request | **PT-141** (named only "PT-141"; bremelanotide **not stated**) · nasal spray · "works for both men and women to enhance sexual drive." |
| Semaglutide | buyable | Peptide therapy | `/learn/protocols/peptide-therapy` | — | on-request | **semaglutide** — "mimics… glucagon-like peptide-1 (GLP-1)" · weight loss / type-2 diabetes · gated. Opt files its only GLP-1 under *peptides*. |
| Oxytocin | buyable | Peptide therapy | `/learn/protocols/peptide-therapy` | — | on-request | **oxytocin** (peptide hormone) · "improve social behavior, reduce stress/anxiety, enhance sexual function." |
| GHK-Cu | buyable | Peptide therapy | `/learn/protocols/peptide-therapy` | — | on-request | **GHK-Cu** (non-injectable) · anti-aging / skin — "stimulate collagen production, improve skin elasticity." |
| VIP | buyable | Peptide therapy | `/learn/protocols/peptide-therapy` | — | on-request | **VIP** (vasoactive intestinal peptide) · metabolism/immune/anti-inflammatory · gated. |
| Pinealon | buyable | Peptide therapy | `/learn/protocols/peptide-therapy` | — | on-request | **pinealon** · neuroprotection / circadian / memory (acts on the pineal gland) · gated. |
| Hexarelin | buyable | Peptide therapy | `/learn/protocols/peptide-therapy` | — | on-request | **hexarelin** · GH secretagogue — "amplifying the natural growth hormone-releasing signal." |
| 5-amino-1MQ | buyable | Peptide therapy | `/learn/protocols/peptide-therapy` | — | on-request | **5-amino-1MQ** (methylquinoline / NNMT inhibitor) · investigational for obesity & diabetes · gated. |
| **Erectile dysfunction** | family | — | `/learn/protocols/erectile-dysfunction` | — | — | Men's ED line — diagnosed and prescribed online. |
| ED medication | buyable | Erectile dysfunction | `/learn/protocols/erectile-dysfunction` | — | on-request | **PDE5 inhibitors** ("ED medications that block PDE5 enzymes"; specific molecule — sildenafil/tadalafil — **not stated**) · oral · online diagnosis + Rx, gated. |
| **Membership treatment menu (à la carte / included)** | family | — | `/memberships` | — | — | The "Unique treatments" grid — supplements + select hormones bundled by tier (Foundation ≤2 supplements; Optimization ≤3 supplements + 2 meds) or added at in-app fees. Page-named, no per-item prices shown. |
| Supplements & micronutrients | buyable | Membership treatment menu | `/memberships` | — | partial | page-named items — **Vitamin D3, D3 with K2, Omega-3, Zinc, Magnesium** (supplements) · oral · included up to the tier cap; the displayed "membership" price is the all-in floor, item count tier-set. |
| Hormone / metabolic add-ons | buyable | Membership treatment menu | `/memberships` | — | on-request | page-named — **Testosterone, Thyroid (T3/T4), DHEA, Clomiphene** · form not stated · physician-prescribed within a tier, priced in-app. |
| Hair-loss & weight-loss meds | buyable | Membership treatment menu | `/memberships` | — | on-request | hair-loss medication + weight-loss (semaglutide, see Peptides) referenced in membership benefits ("ordering medications, including peptides, hair loss medication, ED medication, and more on the Opt app") · molecule not enumerated beyond semaglutide · in-app fees. |
| **Women's vertical (parallel)** | family | — | `/women` | — | — | A full parallel membership for peri/menopause at `/women/*` — own memberships + medical team + protocols. **Not deeply captured this run** (overview only). |
| Women's HRT | buyable | Women's vertical | `/learn/protocols/hrt` | — | on-request | hormone replacement therapy ("restoring sex hormone levels"; specific molecules **not enumerated** on captured pages) · membership-gated. |
| Women's Longevity Medicine | buyable | Women's vertical | `/program-goals/women-longevity` | — | on-request | longevity/anti-aging protocol · gated. |
| Women's Peptide Therapy | buyable | Women's vertical | `/learn/protocols/women-peptide-therapy` | — | on-request | peptide therapy, women's track · gated. |

**Buyable count (in scope): 21** — 3 membership tiers + 1 TRT + 9 named peptides + 1 ED + 3 membership-menu
bundles + 3 women's-vertical lines + 1 (TRT family is non-buyable). The `family` rows are non-buyable groupings.
**Only the 3 membership prices are `published`; everything else is `partial`/`on-request`** — the public catalog
is a floor, not a priced census.

### Verbatim anchors

The footnotes the Price/Visibility columns point at, quoted exactly from the cited captures.

- **[anchor: membership-fixed] Membership pricing footnote (verbatim, /memberships):** *"All plan pricing is
  fixed. Foundation plan includes up to 2 supplements. Optimization plan includes up to 2 prescriptions and up
  to 3 supplements. ** Medications prescribed only after physician review and approval."* Each tier card reads
  *"After a one-time initial intake and lab fee of $195"* (Foundation, Optimization) / *"…of $695"* (Longevity).
- **[anchor: trt-price] TRT price = the membership floor (verbatim, /trt FAQ):** *"Opt Health offers TRT to
  clients who qualify as part of our Optimization and Longevity plans, **starting at $245 per month plus a $195
  initial lab fee**."* → TRT has no standalone price; its floor is the Optimization tier → `partial`.
- **[anchor: peptide-price] Peptides are quote-only (verbatim, /peptides):** *"Life-changing peptide therapy is
  just a phone call away, please contact us to inquire about pricing."* + *"Over a dozen peptides available,
  including Sermorelin, and PT-141."* + *"Peptide therapy administered via injection, nasal spray, or orally."*
  → every peptide `on-request`.
- **[anchor: molecule] Molecule sourcing (page-attested-only, audited):**
  - **Testosterone → ester NOT stated.** /trt names only "testosterone… in the form of topical creams,
    injections, or oral pills" — no cypionate/enanthate anywhere. Recorded "testosterone, ester not stated."
  - **Semaglutide → GLP-1 attested** (/peptides): *"Semaglutide is a peptide that mimics the effects of a
    hormone called glucagon-like peptide-1 (GLP-1)."* It is the only GLP-1 named on the site.
  - **PT-141 → named only "PT-141"** (bremelanotide not stated). **ED → "PDE5 inhibitors"** as a class only —
    no sildenafil/tadalafil named on /ed.
  - Self-naming peptides (page = molecule), all page-attested: Sermorelin, Oxytocin, GHK-Cu, VIP, Pinealon,
    Hexarelin, 5-amino-1MQ. Body copy also names **Ipamorelin, CJC-1295, Kisspeptin, Thymosin Alpha-1,
    Epithalon** in benefit/FAQ prose (not the menu cards) — not rostered as menu items.
  - Supplement/hormone grid items (Vitamin D3, D3+K2, Omega-3, Zinc, Magnesium, Testosterone, Thyroid T3/T4,
    DHEA, Clomiphene) are page-named in the /memberships "Unique treatments" grid, no dose/form stated.

## Deep blocks

One block earns its place: the **tier-gating model** — the commerce logic that the roster's flat rows can't
carry (which tier unlocks which treatment, and where the *real* price hides). No per-SKU deep-dive is earned —
there are no per-SKU PDPs to distill (the structural contrast with Hone, whose PDP template earned a block).

### The tier-gating model — where the price actually lives

Opt Health prices a **membership**, then gates treatments *inside* it; the displayed med-treatment "prices" are
almost all the membership floor or "contact us." Reading the three tiers against the treatment menu:

> **Foundation ($95/mo + $195 one-time):** the *diagnostic* tier — 55+ biomarker labs, one 60-min consult, up
> to 2 supplements, and the app. Crucially it grants only the **ability to *order*** medications "at additional
> fees" — TRT/specialized Rx are **not included** here.
> **Optimization ($245/mo + $195 one-time) — "MOST POPULAR":** the *treatment* tier — **"specialized
> prescriptions included"** (hormones, weight loss, fertility, sleep/energy) + 2 membership medications + 3
> supplements + 4×/yr labs. **This is the floor TRT requires** ("…as part of our Optimization and Longevity
> plans, starting at $245/mo + $195 lab fee").
> **Longevity ($645/mo + $695 one-time):** the *anti-aging* tier — everything in Optimization + 65+ biomarkers,
> **epigenetic/biological-age testing 2×/yr**, a 90-min consult, and discounted advanced diagnostics.

**Takeaway:** a consumer asking "what does TRT cost at Opt Health?" gets **$245/mo + a $195 lab fee** (the
Optimization membership), not a med price — and a consumer asking "what do peptides / ED / weight-loss cost?"
gets **"contact us"** (in-app, post-consult). The only honest public prices are the three membership numbers;
the medication economics live behind `app.getopt.com`. That gating is the company's model, not a capture gap —
but it makes the roster a **floor**, and the cohort-comparison question ("who's cheapest for compounded
semaglutide?") is **unanswerable from the public site** for Opt Health.

## Provenance

- **Pages read (5 fresh, all `captures/2026-06-04/`):** `memberships` (the 3 priced tiers + the treatment grid
  + the public FAQ), `trt` (TRT forms + the tier-gated price), `peptides` (the 9-named peptide menu + the
  quote-only pricing), `ed` (PDE5-class), `women` (the parallel vertical, overview). Context: homepage +
  `medical_team` + `about` (per `store/getopt-com/profile.md`). All verified — sourceURLs match, bodies
  md5-unique, no junk soft-404s.
- **Method / cost:** part of the 11-credit profile capture (1 map + 10 rich `--homepage`/standard scrapes,
  `maxAge:0`, `location:US`, `waitFor:3500`); **no extra credits** beyond the profile run (the offerings rode
  the same pages).
- **Scope — enumerated:** the **3 membership tiers** (the only published prices), the **TRT** line, the **9
  page-named peptides**, **ED**, and the **/memberships treatment grid** (supplements + hormone add-ons) at the
  grain the site exposes. **`enumeration: lines-omitted`** — deliberately **not captured this run:** (1) the
  entire **women's vertical's pricing + protocols** (`/women/memberships`, women's `/learn/protocols/*`) — only
  the `/women` overview was pulled, so the women's lines are rostered as families without prices; (2) dedicated
  **weight-loss and hair-loss** protocol pages (characterized from the peptides page + membership benefits
  instead). A `/deepen-offerings` pass on `/women/*` + the weight-loss/hair-loss protocols would close these.
- **Gated / unreachable:** **all** medication/treatment pricing except the 3 membership tiers — TRT med cost on
  top of the tier, peptide pricing ("contact us"), ED/weight-loss/hair-loss pricing, and women's tier pricing
  all sit behind `app.getopt.com` (post-consult) or a phone call. Esters/specific molecules for testosterone
  and ED meds are not on the public pages.
- **Point-in-time snapshot, not fixed:** no A/B-test instrumentation was observed (WordPress/WP Engine, stable
  server-rendered membership prices), but treatment availability + the in-app pricing are gated and personalized
  — re-capture (and an in-app pass) before trusting any treatment price as current; the membership tiers carry
  their own `captured_at` + a short freshness TTL.

### Run profile

Express `/research-company` invocation with **+offerings** (this file), **+telehealth**, **+logos** — module
intent pre-carried, step-2.5 question batch skipped. The roster is **membership-centric by necessity**: Opt
Health exposes no per-SKU PDPs, so this captures the 3 published membership prices + a page-attested treatment
menu at `on-request`/`partial` grain, rather than a priced SKU census. `enumeration: lines-omitted` records the
deliberately-skipped women's vertical + weight-loss/hair-loss protocol detail.
