---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: honehealth.com       # company key; each offering's slug (its relative url) is its key *within* Hone
captured_at: 2026-06-03      # own freshness; captures/2026-06-03/ holds the source pages
---

## Portfolio overview

Hone Health (honehealth.com; legal entity Time Therapeutics, Inc.) is a diagnostics-gated DTC telehealth
clinic that brands itself a **longevity platform** ("Longevity engineered around your biology") but sells a
broad **Multi-product** catalog: **12 condition lines split across men and women** — hormone therapy, weight
loss, longevity/peptides, sexual health, thyroid, and hair loss — all wrapped in a recurring membership and
fronted by a $65 biomarker test + physician consult. This doc enumerates **the full prescription roster:
39 unique buyable Rx SKUs** (deduped by slug) across all 12 lines, plus the entry/membership SKUs and the
in-person **Hone at Home** arm. Every Rx line sells the same way: a **category** page (non-buyable) lists
**product cards** → each card is a **SKU PDP** (its own slug + a `$X/mo + membership` price) → checkout routes
through the $65 biomarker test → physician review → prescription. This was a comprehensive pass (all category
pages + a URL census + two flagship PDP deep-dives), so the roster is complete at the indexed (card) level.

**Shape finding #1 — a symmetric men/women catalog, often the *same* SKU.** Hone mirrors most lines across
sexes, and the unisex lines literally reuse one SKU slug for both: **longevity** (`/longevity/nad`, `/metformin`,
`/glutathione`, `/b12`, `/omega-3-prescription`, `/low-dose-naltrexone`), **thyroid** (`/hypothyroidism/t3`,
`/synthroid`, `/desiccated-thyroid`), **hair loss** (`/hair-loss/finasteride-minoxidil`), and **four weight-loss
adjuncts** at bare root (`/naltrexone`, `/buproprion` [sic], `/topiramate`, `/liraglutide`). Only the *hormone*
lines are sex-specific — men's **TRT** vs women's **menopause HRT** — and a few weight-loss SKUs are gendered
(`/mens/sermorelin` vs `/womens/sermorelin`, `/mens/phentermine` vs `/womens/phentermine`). Net: many slugs,
but a lean ~39-SKU true catalog.

**Shape finding #2 — two price-visibility patterns, under one mandatory membership stack.** Every SKU shows a
medication price, but the displayed number is *med-only* and **"+ membership"** is always appended — a
separate, mandatory, **published** cost (**Hone Basic $25/mo** = members-only pricing on *select* meds; **Hone
Premium $155/mo**, "Chosen by 95% of patients" = full access to *all* meds). So the all-in is the card price
**plus** a membership tier. The per-SKU split:
- **`partial`** — the card shows **"From $X/mo"** (an explicit floor; the real per-dose/per-tier number is set
  at consult). The PDP confirms this with a **dose-tier badge** (e.g. testosterone = "Tiers 2-3"). 8 SKUs,
  all hormone: men's + women's testosterone (injection/cream), troches, clomiphene, enclomiphene, tadalafil.
- **`published`** — the card shows a **flat "$X/mo"** (the med's price is fixed and fully shown; the only
  add-on is the published membership). The other 31 Rx SKUs, plus both memberships and the biomarker test.

**Shape finding #3 — everything is compounded + diagnostics-gated, and the flagship TRT is *compounded*.**
Every Rx PDP carries the verbatim line *"This is a compounded product and has not been approved by the FDA…"*
and routes through *"Prescription products require an online consultation…"* + the $65 biomarker test. Notably
the flagship injectable — H1 **"Testosterone Cypionate Injections"** — is itself a **compounded** product
(cypionate is page-attested here, in the H1 and body, not inferred), priced **"From $28/mo"** at "Tiers 2-3".

**Prominence (calibrated).** **Testosterone / hormone therapy is the commercial flagship [HIGH]** — it owns
the **"Trending Products"** slot in *both* nav columns (men → Testosterone `/mens/buy-testosterone`; women →
Testosterone Cream `/womens/testosterone-cream`) and is the origin line (Hone launched men's-only). **Nav/section
order [MED]:** both menus run hormone-therapy → weight-loss → longevity → sexual-function → thyroid →
appearance, so weight-loss reads second and longevity third. **Women's menopause is the single deepest line
[HIGH within the women's franchise]** — 10 SKUs, the widest in the catalog. **Card order within a category is
[LOW]** — Optimizely A/B testing is live (the profile flags run-to-run flicker), so intra-page ranking and
exact prices are a point-in-time snapshot, not a fixed truth.

## Roster

Complete at the indexed (card) level across all 12 lines. Within-company key = **Slug** (the relative URL,
quoted exactly — including Hone's own typos `/buproprion/` and `/mens/tesosterone-troches/`). Price quoted
verbatim with its on-card marker; the universal **"+ membership"** is the mandatory separate cost (see anchors).
Molecule/form is **page-attested only** (card description or PDP), never inferred from the brand. Unisex SKUs
(one slug serving men + women) are listed **once**. An offering here is never asserted equal to a same-molecule
offering at another brand.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Entry & membership** | family | — | (the funnel + subscription that gate every Rx SKU) | — | — | The risk-free first step + the two recurring tiers; medication is priced separately "+ membership." |
| Biomarker Test + Consult | buyable | Entry & membership | (no PDP — funnel entry: `start.honehealth.com/hermes/landing`) | `$165` `$65` (PDP cart) / `$65 per Biomarker Test` | published | not a drug — 40+ biomarker blood panel + physician consult + personalized plan · at-lab (2,000+ labs) or free at-home draw where available · the universal entry. |
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
| **Hone at Home** | family | — | `/hone-at-home` | — | — | The **in-person concierge arm** (Orlando, Denver, Phoenix, NY metro) — distinct from the telehealth Rx catalog. Prices from the 2026-05-31 capture. |
| Botox | buyable | Hone at Home | (no PDP — `/hone-at-home`) | `$350+` | partial | aesthetic injectable · in-person · concierge-nurse visit; "+" = starting price, final set in person. |
| IV Therapy | buyable | Hone at Home | (no PDP — `/hone-at-home`) | `$249+` | partial | IV infusion · in-person · concierge-nurse visit; starting price. |
| At-Home 40+ Biomarker Draw | buyable | Hone at Home | (no PDP — `/hone-at-home`) | `$65` | published | not a drug — at-home blood draw (40+ biomarkers) · in-person nurse · feeds the same telehealth intake. |

**Buyable count (in scope): 45** — 39 unique Rx SKUs (6 men's TRT + 6 men's WL incl. 4 unisex adjuncts +
10 women's menopause + 2 women's-gendered WL + 6 longevity + 3 men's ED + 2 women's libido + 3 thyroid +
1 hair) + 3 entry/membership + 3 Hone at Home services. The 10 `family` rows are non-buyable groupings, not
counted. Unisex slugs counted once.

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
  tier, fixed → `published`). Rule applied across the roster: card reads **"From $X"** → `partial`; flat
  **"$X"** → `published`.
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
  - Self-naming molecules (card = molecule), all attested: clomiphene citrate (Clomid®), enclomiphene,
    anastrozole (Arimidex), naltrexone, bupropion, phentermine, topiramate, metformin, vitamin B12,
    glutathione, NAD+, omega-3-acid ethyl esters, low-dose naltrexone, tadalafil (Cialis®), sildenafil
    (Viagra®), liothyronine/T3 (Cytomel), levothyroxine/T4, desiccated thyroid (T3+T4), finasteride + minoxidil.

## Deep blocks

Three blocks earn their place: the **PDP anatomy** (a cross-SKU structural finding the user asked for, that no
roster row carries), and the two requested flagship deep-dives — **Testosterone Cypionate** and **Sermorelin** —
where a verbatim H1 / molecule attestation / price-tier resolves what the roster cell can only flag.

### Hone's PDP template — the anatomy

Every Hone SKU PDP is the **same rigid WordPress template**, in this order (verified identical across the two
captured PDPs and consistent with the category-card shells). Reading one teaches all 39:

1. **Global mega-nav** — Men / Women columns (6 treatments each) + a **"Trending Products"** highlight per
   column (men → Testosterone; women → Testosterone Cream), + How It Works + The Edge Blog + Get Started / Sign In.
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
    Membership & Pricing) → footer (LegitScript seal + Trustpilot **4.8/5, ~11,547 reviews**).

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

- **Pages read (16 fresh, all `captures/2026-06-03/`):** 14 category/hub pages — `mens-hub`, `mens-trt`,
  `mens-weight-loss`, `mens-longevity`, `mens-ed`, `mens-thyroid`, `mens-hair-loss`, `womens-hub`,
  `womens-menopause`, `womens-weight-loss`, `womens-longevity`, `womens-low-libido`, `womens-thyroid`,
  `womens-hair-loss` — plus 2 flagship PDPs `pdp-buy-testosterone` (`/mens/buy-testosterone`) and
  `pdp-sermorelin` (`/mens/sermorelin`). Hone at Home prices reuse `captures/2026-05-31/hone-at-home.md`.
  Context: `store/honehealth-com/profile.md`. All 16 fresh scrapes verified — sourceURLs match, bodies md5-unique.
- **Method / cost:** 1 URL census map (53 product URLs enumerated → confirmed the card roster is complete) +
  16 rich `--homepage` scrapes (`maxAge:0`, `location:US`, `waitFor:3500`). **~19 credits** (17 recorded +
  2 `site:`-path map searches that billed but failed to persist — the `/` in the search term broke fc.py's
  filename, a known tag-sanitization gap; the census map already carried the catalog).
- **Scope — enumerated:** all 12 Rx condition lines (men + women) at the card/SKU level = 39 unique buyable
  Rx SKUs, plus entry/membership and Hone at Home. **Not enumerated (PDP not captured):** every SKU PDP except
  the two flagships — the roster's molecule/form/price for the other 37 comes from category-card descriptions
  (page-attested), so non-flagship esters (cream/troches/women's-injection testosterone) stay "ester not stated."
  The `shop.honehealth.com` supplements storefront (separate subdomain, non-Rx) is out of scope.
- **Gated / unreachable:** the real all-in for any SKU (med price + a membership tier + dose/tier set at
  consult on `start.`/`app.honehealth.com`); which membership (Basic vs Premium) unlocks a given med ("select"
  vs "full access"); `/membership-pricing` renders client-side (empty markdown body) — membership prices come
  from the universal FAQ block + PDP cart; Hone at Home final pricing ("+" starting prices, set in person).
- **Point-in-time snapshot, not fixed:** **Optimizely A/B testing is live** (profile-flagged) — captured
  prices, card order, and which modules render flicker run-to-run. This module's own `captured_at` + a short
  freshness TTL are the guard; re-capture before trusting a price as current.
</content>
</invoke>
