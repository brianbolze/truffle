---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: getopt.com           # company key; each offering's slug (its relative url) is its key *within* Opt Health
captured_at: 2026-06-16       # own freshness; roster ← captures/2026-06-04/ (men's core) + captures/2026-06-16/ (women's vertical + hair/weight breadth)
enumeration: indexed-complete # every line reached at the indexed level: men's memberships + TRT/ED/peptides/hair-loss/weight-loss, AND the women's vertical's published tier prices + its HRT/peptide/longevity/weight-loss protocols. Residual leaves (women's per-goal landing pages; per-SKU in-app prices) are by-design omissions — see scope note
site_notes: "Membership-centric catalog, NOT a per-SKU storefront (contrast Hone). The 3 priced tiers live on /memberships (server-rendered, clean). Treatments are gated: TRT's price IS the Optimization/Longevity membership floor ($245/$645 + a one-time lab fee); peptides/ED/weight-loss are 'contact us to inquire' or in-app (on-request); supplements/micronutrients are bundled by tier (Foundation ≤2, Optimization ≤3). NO per-SKU PDPs with prices exist — molecules come from the /learn/protocols/* education pages + the /memberships 'Unique treatments' grid. The parallel WOMEN'S vertical (/women/*) mirrors the model at IDENTICAL published tier prices ($95/$245/$645 + the same intake fees) but is WAITLIST-gated (/women/waitlist) — published prices, not-yet-open commerce — with its own HRT (incl. vaginal form), peptide, longevity + weight-loss protocols (captured 2026-06-16; women's tier footnote shows a higher supplement cap than men's, ≤3/≤4 vs ≤2/≤3). Dedicated hair-loss (men's androgenic alopecia → DHT-blocker, molecule not named) + weight-loss (TRT/HRT + lifestyle; the only weight-loss *drug* is semaglutide, filed under peptides) program lines now captured. Live commerce + per-treatment pricing sit behind app.getopt.com (signup). WordPress/WP Engine; no A/B-test instrumentation observed, but treatment availability/pricing is gated so treat the public roster as a floor."
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

Complete at the indexed level across **all lines** — men's memberships + TRT/ED/peptides/hair-loss/weight-loss
**and** the women's parallel vertical (its published tier prices + HRT/peptide/longevity/weight-loss protocols),
captured 2026-06-16 (see Provenance). Within-company key =
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
| **Hair loss** | family | — | `/learn/protocols/hair-loss` | — | — | Dedicated men's hair-loss protocol — its own education/treatment page (the membership-menu "hair loss medication" of the row above lands here). |
| Hair-loss treatment | buyable | Hair loss | `/learn/protocols/hair-loss` | — | on-request | **DHT-blocker** ("blocking DHT, the hormone responsible for androgenic alopecia"; specific molecule — finasteride/minoxidil — **not stated**, described as "a potent formula of densifying active ingredients") · targets male-pattern baldness / androgenic alopecia · online Rx, in-app. Women's hair growth is addressed via peptides instead (see Women's Peptide Therapy). |
| **Weight management** | family | — | `/program-goals/lose-weight` | — | — | Goal-framed weight-loss programs (men's `/program-goals/lose-weight`, women's `/program-goals/women-weight-loss`) — **not a standalone drug SKU**: the page route is TRT/HRT + nutrition/behavioral/fitness coaching; the only weight-loss *medication* named anywhere is **semaglutide**, filed under Peptide therapy. |
| Weight-loss program (men) | buyable | Weight management | `/program-goals/lose-weight` | — | on-request | doctor-guided weight management · components: customized nutrition + behavioral coaching + fitness guidance + **TRT** "if low T is a contributing factor"; semaglutide via Peptides · in-app (app.getopt.com signup). |
| Weight-loss program (women) | buyable | Weight management | `/program-goals/women-weight-loss` | — | on-request | women's track, same structure · nutrition + behavioral coaching + fitness + **HRT** "if low hormone levels are a contributing factor" · **waitlist-gated** (`/women/waitlist`). |
| **Women's vertical (parallel)** | family | — | `/women/memberships` | `$95` / `$245` / `$645` `/month` (the same 3 tiers + intake fees as men's) | published | A full parallel membership for peri/menopause at `/women/*` — own memberships + medical team + protocols, at **identical published tier prices** to men's, but **WAITLIST-gated** (`/women/waitlist`): published prices, not-yet-open commerce. Tier footnote shows a higher supplement cap than men's (Foundation ≤3, Optimization ≤4 + 2 Rx). [anchor: women-price] |
| Women's HRT | buyable | Women's vertical | `/learn/protocols/hrt` | the women's tier floor (`$95`–`$645`/mo + intake) | partial | **sex hormones** — estrogen page-named ("Regulating your estrogen levels"); specific molecules otherwise **not enumerated** · **injectable / oral / topical (creams, patches) / vaginal (tablets, creams, rings)** · membership-gated + physician Rx; waitlist. |
| Women's Peptide Therapy | buyable | Women's vertical | `/learn/protocols/women-peptide-therapy` | — | on-request | women's peptide track for anti-aging / weight management / sexual function / hair growth · molecules page-named in copy: **PT-141, Thymosin Alpha-1, Epithalon, GHK-Cu** (+ "HGH peptides") · gated; waitlist. |
| Women's Longevity Medicine | buyable | Women's vertical | `/program-goals/women-longevity` | — | on-request | longevity / anti-aging protocol · gated; waitlist. (Women's weight-loss is rostered under Weight management above.) |

**Buyable count (in scope): 23** — 3 membership tiers + 1 TRT + 9 named peptides + 1 ED + 3 membership-menu
bundles + 1 hair-loss + 2 weight-loss programs + 3 women's-vertical treatment lines. The `family` rows are
non-buyable groupings. **The only `published` prices are the 3 men's membership tiers + the 3 mirrored women's
tiers** (identical numbers; the women's behind a `/women/waitlist` gate) — everything else is `partial`/`on-request`,
so the public catalog is a floor, not a priced census.

### Verbatim anchors

The footnotes the Price/Visibility columns point at, quoted exactly from the cited captures.

- **[anchor: membership-fixed] Membership pricing footnote (verbatim, /memberships):** *"All plan pricing is
  fixed. Foundation plan includes up to 2 supplements. Optimization plan includes up to 2 prescriptions and up
  to 3 supplements. ** Medications prescribed only after physician review and approval."* Each tier card reads
  *"After a one-time initial intake and lab fee of $195"* (Foundation, Optimization) / *"…of $695"* (Longevity).
- **[anchor: women-price] Women's tiers = identical to men's, waitlist-gated (verbatim, /women/memberships):**
  *"Foundation … $95 /month \* … After a one-time initial intake and lab fee of $195"*; *"MOST POPULAR …
  Optimization … $245 /month \* … fee of $195"*; *"Longevity … $645 /month \* … fee of $695."* Footnote (note
  the higher supplement cap vs men's): *"All plan pricing is fixed. Foundation plan includes up to 3 supplements.
  Optimization plan includes up to 2 prescriptions and up to 4 supplements."* The page's every CTA is
  *"[Get Started]"* → `/women/waitlist` (the vertical is waitlisted, not open commerce).
- **[anchor: hair-loss] Hair loss = DHT-blocker, molecule unnamed (verbatim, /learn/protocols/hair-loss):**
  *"Androgenic alopecia (otherwise known as male pattern baldness) is the most common cause of hair loss in
  men."* + *"Block DHT — A potent formula of densifying active ingredients that promotes hair growth by blocking
  DHT, the hormone responsible for androgenic alopecia."* → no finasteride/minoxidil named; `on-request`.
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

- **Pages read — base (5 fresh, all `captures/2026-06-04/`):** `memberships` (the 3 priced tiers + the treatment
  grid + the public FAQ), `trt` (TRT forms + the tier-gated price), `peptides` (the 9-named peptide menu + the
  quote-only pricing), `ed` (PDE5-class), `women` (the parallel vertical, overview). Context: homepage +
  `medical_team` + `about` (per `store/getopt-com/profile.md`).
- **Pages read — deepen pass (6 fresh, all `captures/2026-06-16/`):** `women_memberships` (the women's 3 priced
  tiers + treatment grid — the published-price gap closed), `women_hrt` (the 4 HRT forms incl. vaginal),
  `women_peptides` (the named-molecule women's peptide track), `hair_loss` (the dedicated men's androgenic-alopecia
  / DHT-blocker page), `weight_loss` + `women_weight_loss` (the TRT/HRT + lifestyle program-goal pages). All
  verified — sourceURLs match, bodies md5-unique, no junk soft-404s (`fc.py verify` clean).
- **Method / cost:** base offerings rode the 11-credit `2026-06-04` profile capture (no extra credits then). This
  **`/deepen-offerings` pass (2026-06-16)** spent **8 Firecrawl credits** — 2 `map --search` (1 redundant, an
  early downstream parse error) + 6 standard/`--homepage` scrapes, `maxAge:0`, `location:US`, `waitFor:3500`,
  serialized (no burst). Tagged `--verb deepen-offerings` for `runcost.py`.
- **Scope — enumerated (`indexed-complete`):** every line is now reached at the indexed level — men's **3
  membership tiers** + **TRT** + **9 peptides** + **ED** + the **/memberships treatment grid**, plus the dedicated
  **hair-loss** (androgenic alopecia → DHT-blocker) and **weight-loss** (TRT/HRT + lifestyle) program lines, and
  the **women's parallel vertical** — its **published tier prices** ($95/$245/$645, identical to men's, behind a
  `/women/waitlist` gate) + its **HRT / peptide / longevity / weight-loss** protocols. **`enumeration:
  indexed-complete`.** By-design leaves still not rostered (not breadth gaps): the women's per-goal landing pages
  (`/program-goals/women-{better-sleep,mental-clarity,more-energy,improved-physique}`, goal-framings not distinct
  SKUs) and all per-SKU in-app prices.
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
Health exposes no per-SKU PDPs, so this captures the published membership prices + a page-attested treatment
menu at `on-request`/`partial` grain, rather than a priced SKU census. A **`/deepen-offerings` pass on 2026-06-16**
(8 credits) then closed the original `lines-omitted` gap — the women's parallel vertical (now with its published,
waitlist-gated tier prices + HRT/peptide/longevity/weight-loss protocols) and the dedicated hair-loss + weight-loss
program lines — graduating the file to **`enumeration: indexed-complete`**.
