---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: honehealth.com       # company key; each offering's slug (its relative url) is its key *within* Hone
captured_at: 2026-06-18
enumeration: indexed-complete   # 14 Rx lines + the 9-SKU shop. supplements line; new heart-health line for both genders; leaf/dedup omissions in Provenance
site_notes: "Two separate catalogs. (1) Rx telehealth — honehealth.com /mens/* /womens/* /hypothyroidism/* /heart-health/* (WordPress; prices on the category cards, suffixed '+ membership'; Optimizely A/B-live → price/order flicker). Nav now 7 treatment categories per sex: hormone therapy, weight-loss, longevity, sexual-function, thyroid, appearance, heart-health. (2) OTC supplements — shop.honehealth.com, a nopCommerce store with a real sitemap.xml (authoritative census) + server-rendered product grids, so a free curl enumerates the whole catalog (/supplements all=9, /mens-care=9, /womens-care=7). Supplement prices are PDP-only (a one-time price + a 10% subscribe-&-save 'subscription-price'); the grid shows only the one-time. The shop subdomain is ALSO the commerce backend for lab-tests / assessments / treatment-plans / Rx-subscriptions — nopCommerce categories that mirror the marketing-site Rx lines; don't re-roster them. /prenuvo is a dead sitemap entry (error page)."
---

## Portfolio overview

Hone Health (honehealth.com; legal entity Time Therapeutics, Inc.) is a diagnostics-gated DTC telehealth
clinic that brands itself a **longevity platform** ("Longevity engineered around your biology") but sells a
broad **Multi-product** catalog: **14 condition lines split across men and women** — hormone therapy, weight
loss, longevity/peptides, sexual health, thyroid, hair loss, and a new **heart health** line — all wrapped in
a recurring membership and fronted by a $65 biomarker test + physician consult. This doc enumerates **two
distinct catalogs**: (a) the **full prescription roster — 42 unique buyable Rx SKUs** (deduped by slug) across
all 14 Rx lines, plus the entry/membership SKUs and the in-person **Hone at Home** arm; and (b) the **9-SKU
OTC supplement line** sold through the separate `shop.honehealth.com` storefront — the 15th arm, **non-Rx and
ungated** (added 2026-06-04). Every Rx line sells the same way: a **category** page (non-buyable) lists
**product cards** → each card is a **SKU PDP** (its own slug + a `$X/mo + membership` price) → checkout routes
through the $65 biomarker test → physician review → prescription. The Rx pass was comprehensive (all category
pages + two flagship PDP deep-dives); the supplement line is enumerated **to the leaf** (sitemap ∩ rendered
grid agree on all 9, every PDP captured in 2026-06-04) — so both rosters are complete at the indexed level.

**Shape finding #1 — a symmetric men/women catalog, often the *same* SKU.** Hone mirrors most lines across
sexes, and the unisex lines literally reuse one SKU slug for both: **longevity** (`/longevity/nad`, `/metformin`,
`/glutathione`, `/b12`, `/omega-3-prescription`, `/low-dose-naltrexone`), **thyroid** (`/hypothyroidism/t3`,
`/synthroid`, `/desiccated-thyroid`), **hair loss** (`/hair-loss/finasteride-minoxidil`), four weight-loss
adjuncts at bare root (`/naltrexone`, `/buproprion` [sic], `/topiramate`, `/liraglutide`), and the **new heart
health line** (`/heart-health/colchicine`, `/heart-health/ezetimibe`, `/heart-health/rosuvastatin`). Only the
*hormone* lines are sex-specific — men's **TRT** vs women's **menopause HRT** — and a few weight-loss SKUs are
gendered (`/mens/sermorelin` vs `/womens/sermorelin`, `/mens/phentermine` vs `/womens/phentermine`). Net: many
slugs, but a lean ~42-SKU true catalog.

**Shape finding #2 — two price-visibility patterns, under one mandatory membership stack.** Every SKU shows a
medication price, but the displayed number is *med-only* and **"+ membership"** is always appended — a
separate, mandatory, **published** cost (**Hone Basic $25/month** = members-only pricing on *select* meds;
**Hone Premium $155/month**, "Chosen by 95% of patients" = full access to *all* meds). So the all-in is the
card price **plus** a membership tier. The per-SKU split:
- **`partial`** — the card shows **"From $X/mo"** (an explicit floor; the real per-dose/per-tier number is set
  at consult). The PDP confirms this with a **dose-tier badge** (e.g. testosterone = "Tiers 2-3"). Applies to
  8 hormone SKUs + Rosuvastatin (the only heart-health SKU with a "From" floor).
- **`published`** — the card shows a **flat "$X/mo"** (the med's price is fixed and fully shown; the only
  add-on is the published membership). All other Rx SKUs, plus both memberships and the biomarker test.

**Shape finding #3 — everything is compounded + diagnostics-gated, and the flagship TRT is *compounded*.**
Every Rx PDP carries the verbatim line *"This is a compounded product and has not been approved by the FDA…"*
and routes through *"Prescription products require an online consultation…"* + the $65 biomarker test. Notably
the flagship injectable — H1 **"Testosterone Cypionate Injections"** — is itself a **compounded** product
(cypionate is page-attested here, in the H1 and body, not inferred), priced **"From $28/mo"** at "Tiers 2-3".

**Shape finding #4 — a second, separate catalog: the OTC supplement storefront (non-Rx, ungated).** Beyond the
diagnostics-gated Rx catalog, Hone runs a **standalone supplement store at `shop.honehealth.com`** — a
**nopCommerce** storefront distinct from the WordPress marketing site — selling **9 OTC capsule supplements**
with **no biomarker test, no consult, no membership**: a direct **"Buy now" → add-to-cart**. Pricing is its own
model: a **one-time price** plus a **10%-off `subscription-price`** (subscribe-&-save autoship), both fully
shown → all `published`. The line spans wellness goals (gut, stress, focus, sleep), longevity, and **OTC analogs
of two Rx lines** (a `Longevity` supplement alongside the Rx longevity peptides; a `Thrive – Thyroid Complex`
alongside the Rx thyroid meds). Two SKUs are **men's-only** (Men's Performance Multivitamin, Mojo for Men) —
`/womens-care` lists 7, `/mens-care` and `/supplements` list all 9. This storefront was enumerated to the leaf
in the 2026-06-04 pass (sitemap.xml ∩ rendered grid → the same 9).

**Shape finding #5 — new Heart Health line (2026-06-18).** Both `/mens/heart-health` and `/womens/heart-health`
now appear as a 7th treatment category in the site nav. Three unisex Rx SKUs listed on both pages:
Colchicine, Ezetimibe (both flat `$37/mo`), and Rosuvastatin (`From $37/mo`). Colchicine and Ezetimibe are
**`published`**; Rosuvastatin is **`partial`** (the "From" floor signals dose/tier pricing). The page also
cross-links to existing hormone SKUs (Testosterone for men; Bi-est Cream for women) as cardiovascular support —
those aren't new roster rows, they're cross-sells within the existing TRT and menopause lines.

**Prominence (calibrated).** **Testosterone / hormone therapy is the commercial flagship [HIGH]** — it owns
the **"Trending Products"** slot in *both* nav columns (men → Testosterone `/mens/buy-testosterone`; women →
Testosterone Cream `/womens/testosterone-cream`) and is the origin line (Hone launched men's-only). **Nav/section
order [MED]:** both menus run hormone-therapy → weight-loss → longevity → sexual-function → thyroid →
appearance → heart-health, so weight-loss reads second and longevity third; heart-health lands last. **Women's
menopause is the single deepest line [HIGH within the women's franchise]** — 10 SKUs, the widest in the catalog.
**Card order within a category is [LOW]** — Optimizely A/B testing is live (the profile flags run-to-run
flicker), so intra-page ranking and exact prices are a point-in-time snapshot, not a fixed truth.

## Roster

Complete at the indexed (card) level across all 14 lines. Within-company key = **Slug** (the relative URL,
quoted exactly — including Hone's own typos `/buproprion/` and `/mens/tesosterone-troches/`). Price quoted
verbatim with its on-card marker; the universal **"+ membership"** is the mandatory separate cost (see anchors).
Molecule/form is **page-attested only** (card description or PDP), never inferred from the brand. Unisex SKUs
(one slug serving men + women) are listed **once**. An offering here is never asserted equal to a same-molecule
offering at another brand.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Entry & membership** | family | — | (the funnel + subscription that gate every Rx SKU) | — | — | The risk-free first step + the two recurring tiers; medication is priced separately "+ membership." |
| Biomarker Test + Consult | buyable | Entry & membership | (no PDP — funnel entry: `start.honehealth.com/hermes/landing`) | `$65 per Biomarker Test` | published | not a drug — 40+ biomarker blood panel + physician consult + personalized plan · at-lab (2,000+ labs) or free at-home draw where available · the universal entry. |
| Hone Basic | buyable | Entry & membership | `/membership-pricing` | `$25/month` | published | subscription · biomarker testing every 6 months, ability to *purchase* consults, members-only pricing on *select* meds & supplements. |
| Hone Premium | buyable | Entry & membership | `/membership-pricing` | `$155/month` | published | subscription · "Chosen by 95% of patients"; biomarker testing + included consults + personalized protocols + full access to *all* meds, retest/follow-ups every 90 days. |
| **Testosterone (TRT, men)** | family | — | `/mens/testosterone-replacement-therapy` | — | — | Men's hormone flagship; "the foundation for Hone's testosterone replacement therapy plans." |
| Testosterone Cypionate Injections | buyable | Testosterone (TRT, men) | `/mens/buy-testosterone` | `From $28/mo + membership` | partial | **testosterone cypionate** (H1 + body; **compounded**) · injectable · biomarker + consult gated; PDP badge "Tiers 2-3." The men's "Trending Products" pick. [anchor: tiers] [anchor: molecule] |
| Testosterone (Cream) | buyable | Testosterone (TRT, men) | `/mens/testosterone-cream` | `From $60/mo + membership` | partial | testosterone (ester not stated) · topical cream, applied externally · gated. "Alternative to injection." |
| Testosterone (Troches) | buyable | Testosterone (TRT, men) | `/mens/tesosterone-troches` [sic] | `From $60/mo + membership` | partial | testosterone (ester not stated) · oral dissolvable troche · gated. |
| Clomiphene Citrate | buyable | Testosterone (TRT, men) | `/mens/clomiphene` | `From $38/mo + membership` | partial | clomiphene citrate ("generic Clomid®") · oral · gated. "Boosts your body's production of testosterone… while preserving fertility." |
| Enclomiphene | buyable | Testosterone (TRT, men) | `/mens/enclomiphene` | `From $42/mo + membership` | partial | enclomiphene · oral · gated. "Stimulating your body's natural testosterone production… while supporting fertility." |
| Anastrozole | buyable | Testosterone (TRT, men) | `/mens/anastrozole` | `$22/mo + membership` | published | anastrozole ("generic Arimidex") · oral · gated. Estrogen control — "reduces… conversion of testosterone to estrogen." |
| **Weight Loss (men)** | family | — | `/mens/weight-loss` | — | — | Men's weight-loss line; GLP-1 adjunct + appetite/peptide meds (no branded GLP-1 — compounded liraglutide is the only GLP-1). |
| Sermorelin (men) | buyable | Weight Loss (men) | `/mens/sermorelin` | `$130/mo + membership` | published | **sermorelin** — "synthetic peptide that stimulates the release of growth hormone" (**compounded**) · injectable · gated; PDP badge "Premium Tier." [anchor: molecule] |
| Phentermine (men) | buyable | Weight Loss (men) | `/mens/phentermine` | `$65/mo + membership` | published | phentermine · oral · gated. Appetite suppressant. |
| Naltrexone | buyable | Weight Loss (men) | `/naltrexone` | `$60/mo + membership` | published | naltrexone · oral · gated · **unisex slug (also in women's WL)**. "Normalizing metabolism and reducing cravings." |
| Bupropion | buyable | Weight Loss (men) | `/buproprion` [sic] | `$60/mo + membership` | published | bupropion · oral · gated · **unisex slug (also in women's WL)**. "Increasing… norepinephrine and dopamine." |
| Topiramate | buyable | Weight Loss (men) | `/topiramate` | `$65/mo + membership` | published | topiramate · oral · gated · **unisex slug (also in women's WL)**. "Decreasing appetite and hunger signals." |
| Compounded Liraglutide | buyable | Weight Loss (men) | `/liraglutide` | `$160/mo + membership` | published | **compounded liraglutide** (GLP-1) · daily injection · gated · **unisex slug (also in women's WL)**. "Mimicking the GLP-1 hormone." The catalog's only GLP-1. |
| **Menopause (HRT, women)** | family | — | `/womens/menopause-treatment` | — | — | Women's hormone flagship and the **deepest single line (10 SKUs)** — testosterone, estrogen, progesterone, DHEA. |
| Testosterone (Injections, women) | buyable | Menopause (HRT, women) | `/womens/testosterone-injection` | `From $28/mo + membership` | partial | testosterone (ester not stated) · injectable · gated. "Decreased libido, bone loss, irregular periods." |
| Testosterone (Cream, women) | buyable | Menopause (HRT, women) | `/womens/testosterone-cream` | `From $60/mo + membership` | partial | testosterone (ester not stated) · topical cream · gated. The women's "Trending Products" pick. |
| Estradiol Patch | buyable | Menopause (HRT, women) | `/womens/estradiol-patches` | `$58/mo + membership` | published | estradiol · transdermal patch · gated. Hot flashes, vaginal dryness, osteoporosis. |
| Bi-est Cream | buyable | Menopause (HRT, women) | `/womens/bi-est-cream` | `$80/mo + membership` | published | estradiol + estriol ("50/50 or 80/20 compound") · topical cream · gated. |
| Progesterone | buyable | Menopause (HRT, women) | `/womens/progesterone` | `$49/mo + membership` | published | progesterone · oral tablet · gated. |
| Progesterone Cream | buyable | Menopause (HRT, women) | `/womens/progesterone-cream` | `$79/mo + membership` | published | progesterone · topical cream · gated. Peri/menopause symptoms. |
| Estrace® Estradiol Cream | buyable | Menopause (HRT, women) | `/womens/estradiol-vaginal-cream` | `$40/mo + membership` | published | estradiol (Estrace®) · vaginal cream · gated. |
| Vagifem | buyable | Menopause (HRT, women) | `/womens/vagifem` | `$65/mo + membership` | published | estradiol ("Vagifem and Yuvafem… containing estradiol") · vaginal insert/suppository · gated. |
| DHEA Cream | buyable | Menopause (HRT, women) | `/womens/dhea` | `$56/mo + membership` | published | DHEA · topical cream · gated. "Increase levels of estrogen and testosterone." |
| Estriol Vaginal Cream | buyable | Menopause (HRT, women) | `/womens/estriol-vaginal-cream` | `$58/mo + membership` | published | estriol ("gentler than estradiol") · vaginal cream · gated. |
| **Weight Loss (women)** | family | — | `/womens/weight-loss` | — | — | Women's weight-loss line; gendered Sermorelin + Phentermine, plus the 4 unisex adjuncts listed under Weight Loss (men). |
| Sermorelin (women) | buyable | Weight Loss (women) | `/womens/sermorelin` | `$130/mo + membership` | published | sermorelin (synthetic GH-releasing peptide) · injectable · gated. Identical copy to the men's SKU; own slug. |
| Phentermine (women) | buyable | Weight Loss (women) | `/womens/phentermine` | `$65/mo + membership` | published | phentermine · oral · gated. (Naltrexone, Bupropion, Topiramate, Compounded Liraglutide are the same unisex slugs as men's WL.) |
| **Longevity / peptides** | family | — | `/mens/longevity` · `/womens/longevity` | — | — | Unisex anti-aging line; both sexes' category pages list the same `/longevity/*` SKUs. |
| NAD+ | buyable | Longevity / peptides | `/longevity/nad` | `$165/mo + membership` | published | NAD+ · injectable · gated · unisex. "Your body's fight against aging." |
| Vitamin B12 | buyable | Longevity / peptides | `/longevity/b12` | `$60/mo + membership` | published | vitamin B12 · injectable · gated · unisex. |
| Glutathione | buyable | Longevity / peptides | `/longevity/glutathione` | `$90/mo + membership` | published | glutathione (antioxidant) · injectable · gated · unisex. |
| Metformin | buyable | Longevity / peptides | `/longevity/metformin` | `$25/mo + membership` | published | metformin (FDA-approved) · oral · gated · unisex. Insulin sensitivity / healthy aging. |
| Omega-3-Acid Ethyl Esters | buyable | Longevity / peptides | `/longevity/omega-3-prescription` | `$20/mo + membership` | published | omega-3-acid ethyl esters (Rx; EPA + DHA) · oral · gated · unisex. |
| Low Dose Naltrexone (LDN) | buyable | Longevity / peptides | `/longevity/low-dose-naltrexone` | `$38/mo + membership` | published | naltrexone, low-dose · oral · gated · unisex. Immune/inflammation, endorphins. |
| **Sexual function (ED, men)** | family | — | `/mens/erectile-dysfunction-treatment` | — | — | Men's ED line. |
| Tadalafil | buyable | Sexual function (ED, men) | `/mens/tadalafil` | `From $25/mo + membership` | partial | tadalafil ("generic for Cialis®") · oral · gated. |
| Sildenafil | buyable | Sexual function (ED, men) | `/mens/sildenafil` | `$25/mo + membership` | published | sildenafil ("generic for Viagra®") · oral · gated. |
| PT-141 (men) | buyable | Sexual function (ED, men) | `/mens/pt-141` | `$130/mo + membership` | published | PT-141 (molecule named only as "PT-141") · injectable/peptide · gated. "Boost in sex drive… within 30-60 minutes." |
| **Sexual function (low libido, women)** | family | — | `/womens/low-libido-treatment` | — | — | Women's libido line. |
| Arousal Cream | buyable | Sexual function (low libido, women) | `/womens/clitoral-cream` | `$70/mo + membership` | published | molecule **not stated** ("Hone's proprietary arousal cream") · topical cream · gated. |
| PT-141 (women) | buyable | Sexual function (low libido, women) | `/womens/pt-141` | `$130/mo + membership` | published | PT-141 (named only "PT-141") · injectable/peptide · gated. "For both men and women." |
| **Thyroid (hypothyroidism)** | family | — | `/hypothyroidism/men` · `/hypothyroidism/women` | — | — | Unisex thyroid line; both sexes' category pages list the same `/hypothyroidism/*` SKUs. |
| T3 (Liothyronine) | buyable | Thyroid (hypothyroidism) | `/hypothyroidism/t3` | `$25/mo + membership` | published | liothyronine ("synthetic… T3… also known as Cytomel") · oral · gated · unisex. |
| T4 (Levothyroxine) | buyable | Thyroid (hypothyroidism) | `/hypothyroidism/synthroid` | `$15/mo + membership` | published | levothyroxine (T4) · oral · gated · unisex. The catalog's cheapest med. |
| Natural Desiccated Thyroid | buyable | Thyroid (hypothyroidism) | `/hypothyroidism/desiccated-thyroid` | `$52/mo + membership` | published | desiccated thyroid (naturally-derived T3 + T4) · oral · gated · unisex. |
| **Hair loss** | family | — | `/mens/hair-loss` · `/womens/hair-loss` | — | — | Unisex hair line; one shared SKU. |
| Finasteride + Minoxidil | buyable | Hair loss | `/hair-loss/finasteride-minoxidil` | `$38/mo + membership` | published | finasteride + minoxidil ("FDA-approved, two-in-one") · topical solution · gated · unisex. |
| **Heart Health** | family | — | `/mens/heart-health` · `/womens/heart-health` | — | — | Unisex cardiovascular line (new 2026-06-18); same 3 SKUs listed on both men's and women's category pages under `/heart-health/*` slugs. |
| Colchicine | buyable | Heart Health | `/heart-health/colchicine` | `$37/mo + membership` | published | colchicine (molecule named; flat price) · oral · gated · unisex. "Helps calm inflammation inside blood vessels, where heart disease often starts years before symptoms appear." |
| Ezetimibe | buyable | Heart Health | `/heart-health/ezetimibe` | `$37/mo + membership` | published | ezetimibe (molecule named; flat price) · oral · gated · unisex. "Lowers cholesterol by reducing how much is absorbed in the gut." |
| Rosuvastatin | buyable | Heart Health | `/heart-health/rosuvastatin` | `From $37/mo + membership` | partial | rosuvastatin (molecule named; "From" floor → partial) · oral · gated · unisex. "Lowers cholesterol by reducing how much the liver produces." [anchor: tiers] |
| **Hone at Home** | family | — | `/hone-at-home` | — | — | The **in-person concierge arm** (Orlando, Denver, Phoenix, NY metro) — distinct from the telehealth Rx catalog. |
| Botox | buyable | Hone at Home | (no PDP — `/hone-at-home`) | `$350+` | partial | aesthetic injectable · in-person · concierge-nurse visit; "+" = starting price, final set in person. |
| IV Therapy | buyable | Hone at Home | (no PDP — `/hone-at-home`) | `$249+` | partial | IV infusion · in-person · concierge-nurse visit; starting price. |
| At-Home 40+ Biomarker Draw | buyable | Hone at Home | (no PDP — `/hone-at-home`) | `$65` | published | not a drug — at-home blood draw (40+ biomarkers) · in-person nurse · feeds the same telehealth intake. |
| **Supplements (OTC)** | family | — | `/supplements` (`shop.honehealth.com`) | — | — | The **non-Rx storefront line** — 9 OTC capsule supplements, no biomarker/consult/membership gate; direct add-to-cart. Each shows a **one-time price** + a 10% subscribe-&-save `subscription-price` (in parens below). `/mens-care` + `/supplements` = all 9; `/womens-care` = 7 (drops the 2 men's-only). All prices ← `captures/_archive/2026-06-04/`. |
| Biome – Gut Health Support | buyable | Supplements (OTC) | `/biome-gut-health-support` | `$40` (sub `$36`) | published | gut/probiotic — L-glutamine · Butyragen® (tributyrin) · GutGard® DGL licorice · Optibiome® *Bacillus subtilis* · 60 capsules (30-day) · OTC, ungated. |
| Calm – Stress Relief Complex | buyable | Supplements (OTC) | `/stress-relief-complex` | `$40` (sub `$36`) | published | stress — Ashwagandha (Shoden®) · L-theanine · GABA · Huperzine-A · 60 capsules (60-day) · OTC. |
| Focus | buyable | Supplements (OTC) | `/focus` | `$35` (sub `$31.50`) | published | cognition — citicoline (Cognizin®) · L-theanine · lion's mane · Bacopa · ginkgo · B12 · caffeine · 60 capsules (30-day) · OTC. |
| Longevity | buyable | Supplements (OTC) | `/longevity-supplement` | `$80` (sub `$72`) | published | longevity — nicotinamide riboside chloride · trans-resveratrol · Urolithin-A · calcium α-ketoglutarate · spermidine · fisetin · quercetin · berberine · 180 capsules (30-day) · OTC. The OTC analog to the Rx longevity line. |
| Men's Performance Multivitamin | buyable | Supplements (OTC) | `/mens-performance-multivitamin` | `$25` (sub `$22.50`) | published | men's daily multivitamin — 33-nutrient blend (full vitamin/mineral panel + CoQ10, alpha-lipoic acid, quercetin, lutein, boron) · 60 capsules (30-day) · **men's-only** · OTC. |
| Mojo for Men | buyable | Supplements (OTC) | `/mojo-for-men` | `$25` (sub `$22.50`) | published | male performance — zinc · *Eurycoma longifolia* · tribulus · maca · yohimbe (5 mg yohimbine) · saw palmetto · 60 capsules (30-day) · **men's-only** · OTC. |
| Slumber – Rest & Refresh Support | buyable | Supplements (OTC) | `/slumber-rest-refresh-support` | `$30` (sub `$27`) | published | sleep — sustained-release melatonin · magnesium · GABA · L-theanine · Ashwagandha (Shoden®) · reishi/cordyceps · 60 capsules (30-day) · OTC. |
| Thrive – Thyroid Complex | buyable | Supplements (OTC) | `/thrive-thyroid-complex` | `$30` (sub `$27`) | published | thyroid support — selenium · zinc · vitamin D · inositol · L-glutathione (Setria®) · turmeric · 60 capsules (30-day) · OTC. The OTC analog to the Rx thyroid line. |
| Vitamin D&K | buyable | Supplements (OTC) | `/vitamin-dk` | `$30` (sub `$27`) | published | bone/calcium — vitamin D3 (cholecalciferol, 5,000 IU) + K2 (menaquinone-7) · 60 capsules (60-day) · OTC. |

**Buyable count (in scope): 57** — 42 unique Rx SKUs (6 men's TRT + 6 men's WL incl. 4 unisex adjuncts +
10 women's menopause + 2 women's-gendered WL + 6 longevity + 3 men's ED + 2 women's libido + 3 thyroid +
1 hair + **3 heart health [new]**) + 3 entry/membership + 3 Hone at Home services + **9 OTC supplements**.
The `family` rows are non-buyable groupings, not counted. Unisex slugs counted once.

### Verbatim anchors

The footnotes the roster's Price/Visibility columns point at — they decide `partial` vs `published` and carry
the molecule-sourcing audit. Quoted exactly from the cited captures.

- **The universal "+ membership" (the mandatory stack):** every card price is med-only and suffixed
  "+ membership." FAQ (verbatim, on every page): *"Hone offers two memberships: **Basic** – $25/month for
  advanced lab testing every 6 months, the ability to purchase physician consults, and members-only pricing on
  select medications and supplements. **Premium** – $155/month for everything Hone offers: regular lab testing,
  physician consults, and full access to our medications. No commitments. Cancel anytime."* → the displayed
  price is real but never the all-in; all-in = med price + a membership tier. Membership itself is `published`.
- **[anchor: tiers] The dose-tier badge = the `partial` signal.** Each PDP's third icon badge names a price/
  access tier. **Testosterone Cypionate** shows *"Tiers 2-3"* with a *"From $28/mo"* floor (a range → real
  number set at consult → `partial`); **Sermorelin** shows *"Premium Tier"* with a flat *"$130/mo"* (single
  tier, fixed → `published`). **Rosuvastatin** shows *"From $37/mo + membership"* (floor → `partial`).
  Rule applied across the roster: card reads **"From $X"** → `partial`; flat **"$X"** → `published`.
- **Gating (verbatim, every PDP):** *"Prescription products require an online consultation with a healthcare
  provider who will determine if a prescription is appropriate."* The cart module repeats on each PDP:
  *"Optimal Health Biomarker Test — 40+ biomarkers — Test at 2,000+ lab locations — FSA/HSA eligible —
  $165 $65 … Physician Consultation … Included … Personalized Treatment Plan … Included … Subtotal: $165 $65."*
  So the $65 biomarker test (reg. $165) is the gate; consult + plan are bundled into it.
- **Compounded disclaimer (verbatim, on the captured Rx PDPs):** *"This is a compounded product and has not
  been approved by the FDA. The FDA does not verify the safety or effectiveness of compounded drugs."*
- **[anchor: molecule] Molecule sourcing (page-attested-only, audited):**
  - **Testosterone → "cypionate" IS attested** on `/mens/buy-testosterone` — H1 *"Testosterone Cypionate
    Injections"* + body *"Online prescriptions for testosterone cypionate injections are available…"* and
    *"Hone offers testosterone cypionate injections as part of a monthly care plan…"* (Contrast Maximus, where
    cypionate was alt-text-only and recorded "not stated" — here the H1 carries it.)
  - **Testosterone cream / troches (men) and testosterone injection/cream (women) → "testosterone," ester NOT
    stated.** Those PDPs weren't captured; the cards say only "testosterone … cream/troches/injections." Not
    asserted "cypionate."
  - **Sermorelin → "synthetic peptide… growth hormone"** attested: *"Sermorelin is a synthetic peptide that
    stimulates the release of growth hormone from the pituitary gland."* (GHRH analog; injectable.)
  - **Compounded liraglutide → GLP-1** attested: *"…mimicking the GLP-1 hormone."* It is the catalog's *only*
    GLP-1 (no Wegovy/Ozempic/Zepbound/tirzepatide/semaglutide anywhere on Hone).
  - **Estrogens → attested:** Bi-est *"50/50 or 80/20 compound of estradiol and estriol"*; Estrace/Vagifem/
    patch *"estradiol"*; Estriol cream *"Estriol… gentler than estradiol."* DHEA → "DHEA"; progesterone →
    "progesterone."
  - **PT-141 → named only "PT-141"** (bremelanotide not stated) — recorded as PT-141. **Arousal Cream →
    molecule "not stated"** (*"Hone's proprietary arousal cream"*).
  - **Heart health SKUs → molecule attested by product name** on both category pages: Colchicine (card title
    "Colchicine"), Ezetimibe (card title "Ezetimibe"), Rosuvastatin (card title "Rosuvastatin"). Molecule names
    self-identify here and appear verbatim in the card text, not inferred from brand names.
  - Self-naming molecules (card = molecule), all attested: clomiphene citrate (Clomid®), enclomiphene,
    anastrozole (Arimidex), naltrexone, bupropion, phentermine, topiramate, metformin, vitamin B12,
    glutathione, NAD+, omega-3-acid ethyl esters, low-dose naltrexone, tadalafil (Cialis®), sildenafil
    (Viagra®), liothyronine/T3 (Cytomel), levothyroxine/T4, desiccated thyroid (T3+T4), finasteride + minoxidil.
- **[anchor: supplements] The OTC supplement pricing model (verbatim, every supplement PDP):** each PDP shows a
  **one-time price** and a **`subscription-price`** at a flat **10% off** — labelled *"One time purchase"* /
  *"Subscribe & Save SAVE 10%"* / *"Save 10% when you sign up for auto-refills."* Both numbers are fully shown
  and self-contained (no membership, no biomarker gate) → every supplement is `published`. The roster quotes the
  one-time price with the subscription price in parens (e.g. `$40` (sub `$36`)); **both are greppable in the
  cited PDP.** Supplement actives are **page-attested from each PDP's Ingredients table**, never inferred —
  e.g. Vitamin D&K → *"Vitamin D (vegan cholecalciferol) … Vitamin K2 (menaquinone-7)"*; Longevity →
  *"Nicotinamide riboside chloride … trans-Resveratrol … Urolithin-A … Spermidine HCl (Yüth™)"*; Mojo for Men →
  *"Eurycoma longifolia root extract … Yohimbe bark extract (providing 5 mg yohimbine)."*

## Deep blocks

Three blocks earn their place: the **PDP anatomy** (a cross-SKU structural finding the user asked for, that no
roster row carries), and the two requested flagship deep-dives — **Testosterone Cypionate** and **Sermorelin** —
where a verbatim H1 / molecule attestation / price-tier resolves what the roster cell can only flag.

### Hone's PDP template — the anatomy

Every Hone SKU PDP is the **same rigid WordPress template**, in this order (verified identical across the two
captured PDPs and consistent with the category-card shells). Reading one teaches all 42:

1. **Global mega-nav** — Men / Women columns (**7 treatments each** as of 2026-06-18: Increase Testosterone /
   Relieve Menopause, Lose Weight, Live Longer & Better, Improve Sexual Function, Manage Thyroid, Improve
   Appearance, Heart Health) + a **"Trending Products"** highlight per column (men → Testosterone; women →
   Testosterone Cream), + How It Works + The Edge Blog + Get Started / Sign In.
2. **Breadcrumb** — `Home › [Category] › [Product]` (e.g. *"Home › Low Testosterone › Testosterone Cypionate
   Injections"*; *"Home › Weight Loss › Sermorelin Injections"*).
3. **H1 = the specific product name** — usually molecule + form (*"Testosterone Cypionate Injections,"*
   *"Sermorelin Injections"*).
4. **Price line** — `From $X/mo + membership` (floor) or flat `$X/mo + membership`.
5. **One-line value prop** — what it is + how the Hone Rx works.
6. **Three icon badges** — *[benefit] · [route/form] · [price-access tier]* (TRT: *"Balance Hormones ·
   Injectable · Tiers 2-3"*; Sermorelin: *"Stimulate Growth Hormone · Support Lean Body Mass · Premium Tier"*).
7. **CTA** *"Start with a deeper look"* + the Rx-gating disclaimer.
8. **"_[Verb]_ [Outcome]" benefit bullets** (italicized outcomes — *Increase energy/focus/muscle mass…*).
9. **Educational Q&A** — *"What is X?," "What is X Prescribed For?," "How Does X Work?," "What to Expect."*
10. **"Learn More About X"** — Contraindications · Possible Side Effects · Warnings · (sometimes) **Sources**
    with NCBI/PMC citations → then the **compounded/FDA disclaimer**.
11. **Stat band** — the same three figures on every PDP: **92%** quality-of-life improvement in 6 mo · **85%**
    PHQ-9 mood improvement · **70%** still with Hone after 1 year.
12. **"Get Your Consultation for Medications"** cart — Biomarker Test `$165` `$65` + Physician Consultation
    *Included* + Personalized Treatment Plan *Included*, Subtotal `$165` `$65`.
13. **Cross-sell** — sibling SKU cards from the same family ("Explore [Other] Treatment Options").
14. **Edge-blog article cards** (SEO interlink) → **"Real People. Real Stories."** compensated testimonials
    (named, age) → repeat `$65` CTA → FAQ accordion (Getting Started / Consult & Plan / During Treatment /
    Membership & Pricing) → footer (LegitScript seal + Trustpilot **4.8/5, ~11,677 reviews**).

**Takeaway:** the PDP is a content-marketing + trust shell wrapped around a thin commerce core. The only
SKU-distinguishing cells are **H1, price line, and the three badges** (esp. the tier badge); steps 9–14 are
near-identical boilerplate. A reader who wants the real per-SKU facts reads lines 2–6 and stops.

### Testosterone Cypionate Injections — the flagship (compounded, tier-priced)

- **Parent:** Testosterone (TRT, men) · **slug:** `/mens/buy-testosterone` · **price:** `From $28/mo + membership`
  · **visibility:** `partial` (floor + "Tiers 2-3") · **the men's "Trending Products" pick.**

> **Breadcrumb / H1:** "Home › Low Testosterone › Testosterone Cypionate Injections" → **"Testosterone
> Cypionate Injections."**
> **Badges:** "Balance Hormones · Injectable · **Tiers 2-3**."
> **Molecule (verbatim, page-attested):** "Online prescriptions for **testosterone cypionate injections** are
> available to patients based on hormone levels measured via blood panel and consultation with a Hone
> physician." · "Hone offers **testosterone cypionate injections** as part of a monthly care plan with a
> licensed physician via telehealth appointments."
> **Compounded (verbatim):** "This is a compounded product and has not been approved by the FDA. The FDA does
> not verify the safety or effectiveness of compounded drugs."
> **Benefit bullets (verbatim):** "Increases _energy_ · Increases _focus_ · Improves _mood_ · Improves _bone
> density_ · Increases _muscle mass_ · Decreases _abdominal belly fat_."
> **Education (verbatim):** "Testosterone is the primary male sex hormone… If your testosterone levels are too
> low, you may need testosterone replacement therapy…" · prescribed for "hypogonadism, normal male
> development, and low testosterone levels."
> **Contraindications (verbatim):** "Breast cancer, Polycythemia, Prostate cancer, Prostate-specific antigen
> (PSA) >4 ng/mL, Nodules upon digital rectal examination (DRE)."
> **Gating / cart (verbatim):** "Prescription products require an online consultation…" + cart "Optimal
> Health Biomarker Test … $165 $65 … Physician Consultation … Included … Subtotal: $165 $65."
> **Sources:** six NCBI/PMC citations (mood, energy/focus, bone density, muscle mass, belly fat, libido).

**Why it earns a block:** (1) the **cypionate ester is page-attested** here — H1 + body — so it's recorded as
cypionate, *not* "not stated" (the opposite of the Maximus injectable, where cypionate lived only in alt-text);
(2) the flagship is **compounded**, a real positioning fact a roster cell can't carry; (3) "From $28/mo" +
"Tiers 2-3" is the literal evidence for the `partial` call — a floor, with the real number tier/dose-set at
consult. The cream, troches, and women's injection share this family but their PDPs weren't captured, so their
esters stay "not stated."

### Sermorelin Injections — the requested peptide (flat-priced, "Premium Tier")

- **Parent:** Weight Loss (men) · **slug:** `/mens/sermorelin` · **price:** `$130/mo + membership` ·
  **visibility:** `published` (flat + "Premium Tier"). Women's twin: `/womens/sermorelin`, identical copy.

> **Breadcrumb / H1:** "Home › Weight Loss › Sermorelin Injections" → **"Sermorelin Injections."**
> **Badges:** "Stimulate Growth Hormone · Support Lean Body Mass · **Premium Tier**."
> **Value prop (verbatim):** "When included as part of a comprehensive weight loss plan, sermorelin can help
> improve body composition, break down stored fat, and avoid the loss of muscle mass, which can be a
> detrimental effect of weight loss programs."
> **Molecule (verbatim, page-attested):** "Sermorelin is a **synthetic peptide that stimulates the release of
> growth hormone** from the pituitary gland. It's often prescribed as part of hormone replacement therapy,
> particularly for individuals with growth hormone deficiency." · "Sermorelin can significantly promote the
> synthesis and release of growth hormone (GH)… and subsequently insulin-like growth factor 1 (IGF-1)…"
> **Benefit bullets (verbatim):** "Increases _fat metabolism_ · Improves _body composition_ · Improves
> _strength_ · Improves _sleep quality_ · Increases _energy levels_." · "Effects are usually felt in 2 to 6 months."
> **Contraindications / warnings (verbatim):** "Men with a history or [sic] epilepsy, untreated
> hypothyroidism, or hyperglycemia should avoid sermorelin." · "Sermorelin may worsen insulin resistance or
> contribute to fluid retention and joint pain."
> **Compounded (verbatim):** "This is a compounded product and has not been approved by the FDA…"

**Why it earns a block:** it's the user's requested deep-dive and the clean **`published`** counter-example to
TRT — a **flat $130/mo** with a single **"Premium Tier"** badge (no "From," no dose range), so the med price is
fully shown. The molecule is a **synthetic GH-releasing peptide** (page-attested, not inferred), and it sits
under **Weight Loss** (`Home › Weight Loss`), not Longevity — Hone files its only peptide under fat-loss/body-
composition framing, with the *cross-sell* pointing at the appetite meds (Naltrexone, Phentermine, Topiramate,
Bupropion), not at GLP-1s.

## Provenance

- **Pages read (24 fresh, all `captures/2026-06-18/`):** 16 category/hub pages — `mens_hub`, `mens_trt`,
  `mens_weight_loss`, `mens_longevity`, `mens_ed`, `mens_thyroid`, `mens_hair_loss`, `mens_heart_health`,
  `womens_hub`, `womens_menopause`, `womens_weight_loss`, `womens_longevity`, `womens_low_libido`,
  `womens_thyroid`, `womens_hair_loss`, `womens_heart_health` — plus `homepage`, `hone_at_home`,
  `about`, `clinical_policy`, `consults`, `how_it_works`, `physicians`, `womens_testosterone_cream`.
  Prices for **Hone at Home** (`$350+`, `$249+`, `$65`) confirmed live in `captures/2026-06-18/hone_at_home.md`.
- **Pages read — supplements line (11, all `captures/_archive/2026-06-04/`):** 2 storefront category pages
  (`supplements` = `shop.honehealth.com/supplements`, all 9; `supplements-womens` = `/womens-care`, 7) + all
  **9 supplement PDPs** (`supp-biome`, `supp-calm`, `supp-focus`, `supp-longevity`, `supp-mens-multi`,
  `supp-mojo`, `supp-slumber`, `supp-thrive`, `supp-vitamin-dk`). All 11 verified — sourceURLs match, bodies
  md5-unique. Catalog cross-checked **sitemap.xml ∩ rendered grid** (both → the same 9).
- **Scope — enumerated:** all **14 Rx condition lines** (men + women, including the new Heart Health line for
  both sexes) at the card/SKU level = 42 unique buyable Rx SKUs, plus entry/membership and Hone at Home; **and
  the full 9-SKU OTC supplement line** at `shop.honehealth.com` (each PDP captured → price + form + actives
  page-attested to the leaf). **Not enumerated (PDP not captured):** every *Rx* SKU PDP except the two
  flagships — the roster's molecule/form/price for the other Rx SKUs comes from category-card descriptions
  (page-attested), so non-flagship esters (cream/troches/women's-injection testosterone) stay "ester not
  stated." Heart health SKU PDPs not captured — molecules attested via card text on the line pages. **Noted
  but deliberately not re-rostered:** the `shop.honehealth.com` commerce backend for lab-tests / assessments /
  treatment-plans / Rx-subscription categories — nopCommerce groupings that mirror the marketing-site Rx lines
  already rostered above (re-rostering them would duplicate, not add). `/prenuvo` is a dead sitemap entry.
- **Gated / unreachable:** the real all-in for any SKU (med price + a membership tier + dose/tier set at
  consult on `start.`/`app.honehealth.com`); which membership (Basic vs Premium) unlocks a given med ("select"
  vs "full access"); `/membership-pricing` renders client-side (empty markdown body) — membership prices come
  from the universal FAQ block + PDP cart; Hone at Home final pricing ("+" starting prices, set in person);
  heart health PDP pages not captured (individual SKU PDPs at `/heart-health/colchicine`, etc. — card prices
  are page-attested from the category pages but tier-badge details are not available without PDP capture).
- **Point-in-time snapshot, not fixed:** **Optimizely A/B testing is live** on the *Rx* marketing site
  (profile-flagged) — captured Rx prices, card order, and which modules render flicker run-to-run. The
  `shop.honehealth.com` supplement storefront shows no such instrumentation (stable server-rendered nopCommerce
  prices), but supplement pricing still runs promos — both rosters' `captured_at` + a short freshness TTL are
  the guard; re-capture before trusting a price as current.

### Run profile

Deep roster refresh (2026-06-18): added the **Heart Health line** (new, both `/mens/heart-health` and
`/womens/heart-health`) — 1 new `family` row + 3 new unisex buyable SKUs (Colchicine, Ezetimibe, Rosuvastatin).
Nav confirmed at 7 treatment categories per sex (up from 6). All other Rx prices confirmed unchanged vs
2026-06-04 from the fresh 2026-06-18 category page captures. Hone at Home prices confirmed live in this run's
captures. Supplement roster carried forward unchanged from `captures/_archive/2026-06-04/` (prices are still
grep-verifiable in that subdirectory; no supplement-specific re-capture in this run). PDP-anatomy block updated
to reflect 7-treatment nav. Prior flagship deep-dive blocks (Testosterone Cypionate, Sermorelin) carried
forward without re-capture — PDPs not re-scraped. The opt-in PDP-anatomy block was present in prior runs and
is retained as the seed exemplar per the OFFERINGS.md contract.
