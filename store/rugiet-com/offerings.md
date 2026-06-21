---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: rugiet.com          # company key; each offering's slug is its key within Rugiet
captured_at: 2026-06-21     # own freshness; captures/2026-06-21/ holds the source pages
enumeration: indexed-complete
site_notes: "Catalog enumerated from /all-treatments, /sex, /testosterone, /longevity, homepage links, and current PDP recommendation links. Longevity is new vs 2026-06-07 and adds NAD+, Sermorelin, L-Carnitine, Lipo-C, Glutathione. Oral TRT is not on /all-treatments but is still linked from current PDP recommendation cards, so it remains rostered. Prices remain quiz-gated except Ready and TRT: Ready public prices live on /bm/n1/shopping and /trimix; TRT public price is $69 initial labs/evaluation + plans starting at $139/month. Cost articles are comparative/general, not Rugiet price sheets."
---

## Portfolio overview

Rugiet is **Multi-product** and now broader than the prior capture: **15 buyable SKUs** across Sexual Performance, Testosterone, Sleep, Longevity, and Weight, with Hair folded into the Grower ED+hair combo. Ready is still the flagship [HIGH] — homepage hero, best-seller labeling, top catalog position, SEM landers, and public price anchors all point there. Longevity is the meaningful new line [HIGH] because it appears in the top nav and has its own hub plus five PDPs.

**Visibility rule.** Rugiet still gates most all-in pricing behind the intake funnel. Only two price surfaces are public:
- **Ready:** `/bm/n1/shopping` publishes **"Buy Now - $139"** and **"Subscribe $79/mo (40% off)"**; `/trimix` publishes a **"$10/dose"** floor plus strength ladder.
- **TRT:** captured pages publish **"$69"** initial labs/evaluation and plans starting at **"$139/month"**, with labs/monitoring included.

Everything else is `on-request`: no public Rugiet-specific price on the PDPs, landers, or current cost articles.

## Roster

Complete at the indexed level across current product cards, current PDP links, and the Longevity hub. Price quoted verbatim with the page where it appears; molecule/form is page-attested only.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Sexual Performance** | family | — | `/sex` | — | — | ED, premature-ejaculation, daily ED/testosterone support, and ED/hair combo; mostly compounded prescriptions through online intake. |
| Ready | buyable | Sexual Performance | `/erectile-dysfunction/ready` | `Buy Now - $139` · `Subscribe $79/mo (40% off)` · `Starts as low as $10/dose*` · `Low Strength:$14/dose` · `Medium Strength:$17/dose` · `High Strength:$20/dose` · `Max Strength:$24/dose` | published | sildenafil + tadalafil + apomorphine · sublingual troche, as-needed · compounded; public price appears on `/bm/n1/shopping` and `/trimix`, not the main PDP. |
| Go Long | buyable | Sexual Performance | `/premature-ejaculation/go-long` | (no price on page or captured landers — quiz-gated) | on-request | paroxetine + tadalafil · oral dissolving tablet · compounded; 2-in-1 premature-ejaculation + ED. |
| Daily Boost | buyable | Sexual Performance | `/erectile-dysfunction/boost` | (no price on page or captured lander — quiz-gated) | on-request | tadalafil + DHEA · daily chewable · compounded; daily ED + testosterone support. |
| Grower | buyable | Sexual Performance / Hair | `/erectile-dysfunction/grower` | (no price on page — quiz-gated) | on-request | tadalafil + minoxidil · daily pill · compounded; ED + hair growth. |
| **Testosterone (TRT)** | family | — | `/testosterone` | — | — | Four forms at one flat plan price; labs and monitoring included once on treatment; current pages carry controlled-substance/live-video language for TRT forms and enclomiphene. |
| Enclomiphene | buyable | Testosterone (TRT) | `/testosterone/enclomiphene` | `$69 gets you accurate testosterone testing` · `Plans start at just $139/month` | published | enclomiphene · daily oral tablet · compounded; fertility-preserving testosterone support. |
| Injectable TRT | buyable | Testosterone (TRT) | `/testosterone/injectable-trt` | `$69 gets you accurate testosterone testing` · `Plans start as low as $139/month` | published | testosterone cypionate · injection 1-2x/week · controlled-substance prescription; page does not carry the compounded disclaimer. |
| Topical TRT | buyable | Testosterone (TRT) | `/testosterone/topical-trt` | `$69` lab/evaluation · `Plans start as low as $139/month` | published | testosterone · daily cream · compounded controlled-substance prescription. |
| Oral TRT | buyable | Testosterone (TRT) | `/testosterone/oral-trt` | `$69` lab/evaluation · `Plans start as low as $139/month` | published | testosterone · daily capsule / oral TRT · compounded controlled-substance prescription. |
| **Recharge** | buyable | Sleep | `/sleep/recharge` | (no price on page or captured lander — quiz-gated) | on-request | ramelteon + doxylamine + valerian root · oral sleep Rx · compounded, non-controlled sleep treatment. |
| **Longevity** | family | — | `/longevity` | — | — | Five personalized longevity treatments; public pages show forms/benefits but no Rugiet-specific price. |
| NAD+ | buyable | Longevity | `/longevity/nad` | (no Rugiet-specific price on page or cost article — quiz-gated) | on-request | NAD+ · nasal spray or subcutaneous injection · compounded prescription. |
| Sermorelin | buyable | Longevity | `/longevity/sermorelin` | (no Rugiet-specific price on page or cost article — quiz-gated) | on-request | sermorelin · subcutaneous injection 5x/week at bedtime · compounded peptide prescription. |
| L-Carnitine | buyable | Longevity | `/longevity/l-carnitine` | (no Rugiet-specific price on page or cost article — quiz-gated) | on-request | L-carnitine · subcutaneous injection 2-3x/week · prescription; page carries controlled-substance/live-video language. |
| Lipo-C | buyable | Longevity | `/longevity/lipo-c` | (no Rugiet-specific price on page or cost article — quiz-gated) | on-request | methionine + inositol + choline + vitamin B5 + vitamin C · injection typically 1-2x/week · compounded prescription. |
| Glutathione | buyable | Longevity | `/longevity/glutathione` | (no Rugiet-specific price on page or cost article — quiz-gated) | on-request | glutathione · subcutaneous injection multiple times per week · compounded prescription. |
| **Weigh In** | buyable | Weight | `/weight-loss/weigh-in` | (no price on page — quiz-gated) | on-request | bupropion + naltrexone + metformin · daily oral medication stack · compounded; non-GLP-1 weight treatment. |

### Verbatim anchors

- **Ready price, current paid/shopping path:** `/bm/n1/shopping` says **"Buy Now - $139"** and **"Subscribe $79/mo (40% off)"**, with the same note: **"Price shown with 3 month shipping option."** `/bm/n1` also says Ready starts **"at about $7 per dose"** but points to the online checkout; the more concrete shopping-card price is the stronger anchor.
- **Ready dose ladder, `/trimix`:** **"The price of Rugiet Ready depends on your selected dosage strength, number of packs, and delivery option, with doses starting as low as about $10 per dose. Each strength comes in a pack that contains 6 doses."** Standard pricing: **"Low Strength:$14/dose"**, **"Medium Strength:$17/dose"**, **"High Strength:$20/dose"**, **"Max Strength:$24/dose"**. `/trimix` is a Ready lander, not a Trimix SKU.
- **TRT public price:** `/blog/how-much-does-trt-cost-online` says **"Get started for $69 to cover your initial labs and evaluation"** and **"Rugiet's all-inclusive TRT care starts at $139/month, with labs, clinician oversight, medication, and monitoring all included."** PDP FAQs echo **"Plans start at just $139/month"** or **"Plans start as low as $139/month"**.
- **Longevity price audit:** `/blog/longevity-therapy-cost` names NAD+, Sermorelin, Glutathione, Lipo-C, and L-Carnitine, but it stays qualitative: "pricing varies dramatically" by format/provider, "at-home" is more accessible, and no Rugiet SKU price is published. The five Longevity rows stay `on-request`.
- **Molecule/form audit:** Ready = sildenafil + tadalafil + apomorphine; Go Long = paroxetine + tadalafil; Daily Boost = tadalafil + DHEA; Grower = tadalafil + minoxidil; Recharge = ramelteon + doxylamine + valerian root; Weigh In = bupropion + naltrexone + metformin; Lipo-C = methionine + inositol + choline + vitamin B5 + vitamin C. NAD+, Sermorelin, L-Carnitine, and Glutathione are self-named active products/forms on their PDPs.
- **Compounded / controlled lane:** all non-injectable-TRT compounded rows carry the compounded-disclaimer text except L-Carnitine, whose current PDP instead says it is a controlled substance and requires a live audio-video consultation. Injectable TRT carries controlled-substance language but not the compounded disclaimer.

## Deep blocks

Two blocks earned: Ready, because pricing lives off the main PDP and now has two public price surfaces; and Longevity, because it is the new line that changed roster breadth.

### Ready — public price split across shopping + dose landers (`/erectile-dysfunction/ready`)

- **Parent:** Sexual Performance · **visibility:** `published` · **form:** sublingual troche

The main PDP is still a product/clinical page with no price. Public pricing is split:

> **Shopping card (`/bm/n1/shopping`):** "Buy Now - $139" · "Subscribe $79/mo (40% off)" · "Price shown with 3 month shipping option."
> **Dose ladder (`/trimix`):** "Starts as low as $10/dose*" plus "Low Strength:$14/dose" / "Medium Strength:$17/dose" / "High Strength:$20/dose" / "Max Strength:$24/dose."

Why it earns a block: a consumer reading only `/erectile-dysfunction/ready` would mark Ready `on-request`, but the site publishes Ready prices on paid/shopping paths. Capture must keep the URL distinction because `/trimix` is not a Trimix product and `/bm/n1/shopping` is a Ready shopping lander.

### Longevity — new line, five new buyable SKUs (`/longevity`)

- **Parent:** Longevity · **visibility:** all five rows `on-request` · **forms:** nasal spray / subcutaneous injections

The Longevity hub is now first-class in top nav and lists five products:

> **Hub cards:** NAD+; Sermorelin; L-Carnitine; Lipo-C; Glutathione.
> **Outcome routing:** Recovery and muscle mass -> Sermorelin; Energy and mental sharpness -> NAD+; Weight and metabolism -> Lipo-C; Fat burning and endurance -> L-Carnitine; Detox, immunity, and recovery -> Glutathione.
> **Cost article caveat:** Rugiet publishes a "How Much Does Longevity Therapy Cost?" article, but it gives provider/format cost drivers rather than Rugiet prices.

Why it earns a block: this line changes breadth from the old 10-buyable roster to 15. Its price visibility is also easy to over-read: "cost" content exists, but no Rugiet-specific price is published.

## Provenance

- **Sources reconciled (this run, all `captures/2026-06-21/`):**
  - **Backbone:** homepage links, `/all-treatments` (`--homepage`), `/sex`, `/testosterone`, and `/longevity`. Firecrawl map returned 161 URLs; blog/author noise filtered out.
  - **PDPs:** ed_ready, pe_go_long, ed_daily_boost, ed_grower, trt_enclomiphene, trt_injectable, trt_topical, trt_oral, sleep_recharge, weight_weigh_in, longevity_nad, longevity_sermorelin, longevity_l_carnitine, longevity_lipo_c, longevity_glutathione.
  - **Pricing chases:** `/trimix`, `/bm/n1`, `/bm/n1/shopping`, `/go-long-lander`, `/go-long-lander-g`, `/daily-boost-lander`, `/recharge-lander`, `/blog/longevity-therapy-cost`, `/blog/how-much-does-trt-cost-online`.
  - **Verify:** `fc.py verify` — all 31 sourceURLs match, all bodies md5-unique, no junk soft-404s.
- **Completeness verdict — HIGH confidence the roster is complete at the indexed level.** Current category/index surfaces plus PDP links expose 15 buyable SKUs across 5 lines. `enumeration: indexed-complete`. Sub-indexed detail intentionally not rostered: dose/quantity variants behind the quiz, Ready strength/pack combinations beyond the published ladder, and clinician-set TRT/longevity protocols.
- **Couldn't reach / not enumerated:** all-in prices behind the quiz for Go Long, Daily Boost, Grower, Recharge, Weigh In, and all Longevity SKUs; pharmacy partner identity / 503A-503B lane.
- **Credits:** part of the 32-credit `profile.md` recapture (1 map + 31 scrapes); the offerings module drove the extra product/price chase pages.
- **Point-in-time snapshot, not fixed:** captured during a Father's Day promo banner (**"20% off with DAD20"**). Public Ready pricing and quiz-gated offers can change; re-capture before treating price as current.
- **Run profile:** Express recapture with `offerings.md` included; no hero product images requested. Major delta vs prior run: Longevity line added; Ready price source improved via `/bm/n1/shopping`; Oral TRT retained because current PDP recommendation cards still link it.
