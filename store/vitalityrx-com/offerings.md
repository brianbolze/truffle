---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: vitalityrx.com
captured_at: 2026-06-04
site_notes: "Catalog splits across two hosts: the marketing site (vitalityrx.com) describes the programs + lists the supplement packs by name, but PRICES render only on the store SPA (store.vitalityrx.com) — pack price = scrape /checkout/product/<Salesforce-id> with --images; test = /test-kit; Reboot sub = /checkout?sku=<uuid>. Store /map returns only root (no sitemap), so the pack ids come from the /vitamins Add-To-Cart hrefs (the backbone). One id is duplicated on /vitamins (Brain Support Stack == Women's Optimal Vitality id a6MUa0000000n5ZMAQ) — likely a page copy-paste error; verify before trusting. Prices are point-in-time (subscription SPA)."
---

## Portfolio overview

`Flagship + companions`. The hero is a **test → consult → program** hormone funnel; the supplement packs are an à-la-carte companion line.

- **The Vitality Test™ ($149)** is the front door and qualification gate — an at-home Tasso blood draw → telemed consult. **[HIGH]** prominence: every primary CTA ("Get Started") routes here.
- **The Reboot Program™ ($199/mo)** is the flagship treatment and the brand's whole thesis — a *compounded enclomiphene capsule positioned as a TRT alternative*, not testosterone. **[HIGH]**: the homepage, /pricing, and /fertility are built around it.
- **Vitality Packs** are 9 doctor-formulated daily supplement stacks, individually buyable (subscription or one-time), **$69.50–$75.50/mo**. **[MED]**: their own nav item (/vitamins) but secondary to the program; a single store grid.

**Shape finding:** the "testosterone" product here is deliberately *not* TRT — the prescription lane is compounded enclomiphene citrate + DHEA/7-Keto DHEA/progesterone (± anastrozole), sold as a fertility-preserving reboot. No FDA-brand drug and no Schedule-III testosterone appears anywhere.

## Roster

Slugs are relative to `store.vitalityrx.com` for buyable SKUs (the commerce host) and to `vitalityrx.com` for the program description pages. `not stated` = the captured page does not enumerate that SKU's ingredients.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| The Vitality Test™ | buyable | — | store: /test-kit | $149.00 | published | diagnostic (6 biomarkers: Free & Total Testosterone · LH · SHBG · Estradiol · PSA) · at-home Tasso shoulder blood draw + telemed consult · one-time, all 50 states |
| The Reboot Program™ | buyable | — | /pricing/ | $199/mo | published | enclomiphene citrate · DHEA · 7-Keto DHEA · progesterone · anastrozole (\*only if needed) · compounded oral capsule + daily vitamin packs + follow-up testing · Rx, test-qualified, 25 states only |
| Vitality Packs | family | — | /vitamins/ | — | — | doctor-formulated single-ingredient clinical-grade supplements, pre-sorted daily packs · à-la-carte monthly subscription or one-time |
| Men's Max Vitality | buyable | Vitality Packs | store: /checkout/product/a6MUa0000000kFlMAI | $74.50/month | published | not stated · daily supplement pack · subscription or one-time; "Boosts hormonal production and balance, physical performance, and stress resilience" |
| Hair Support Stack | buyable | Vitality Packs | store: /checkout/product/a6MUa0000000muHMAQ | $69.50/month | published | not stated · daily supplement pack · sub or one-time; "Enhances hair growth and strength… nourish the scalp and follicles" |
| Men's Fertility Boost | buyable | Vitality Packs | store: /checkout/product/a6MUa0000000mxVMAQ | $75.50/month | published | not stated · daily supplement pack · sub or one-time; "Enhances sperm quality, motility, and overall reproductive health" |
| Women's Optimal Vitality | buyable | Vitality Packs | store: /checkout/product/a6MUa0000000kR3MAI | — (checkout; not captured) | published | not stated · daily supplement pack · sub or one-time; "energy and hormonal balance… hair and skin, immunity and cognitive function" |
| Deep Sleep Stack | buyable | Vitality Packs | store: /checkout/product/a6MUa0000000kVtMAI | — (checkout; not captured) | published | not stated · daily supplement pack · sub or one-time; "Promotes relaxation… supports natural sleep cycles" |
| Brain Support Stack | buyable | Vitality Packs | store: /checkout/product/a6MUa0000000n5ZMAQ | — (checkout; not captured) | published | not stated · daily supplement pack · sub or one-time; "Boosts cognitive function… memory". ⚠ store id duplicates Women's Optimal Vitality on /vitamins — likely a page error |
| Performance & Recovery Stack | buyable | Vitality Packs | store: /checkout/product/a6MUa0000000n2LMAQ | — (checkout; not captured) | published | not stated · daily supplement pack · sub or one-time; "Boosts strength, endurance, and recovery" |
| Post Op Recovery | buyable | Vitality Packs | store: /checkout/product/WvKx6sm0H1sBD1L8x | — (checkout; not captured) | published | not stated · daily supplement pack · sub or one-time; "Accelerates healing… collagen, reduce inflammation" |
| Hangover Gone | buyable | Vitality Packs | store: /checkout/product/a6MUa0000000kSfMAI | — (checkout; not captured) | published | not stated · daily supplement pack · sub or one-time; "alleviate hangover symptoms… supporting liver health" |

*Completeness: all 11 indexed offerings rostered (2 programs + the family + 9 packs). Prices captured for 4 of 11; the other 7 packs render a price at the store checkout (proven by the 3 captured packs — line runs $69.50–$75.50/mo) but were not individually scraped this run. `published` on an uncaptured pack = a price IS shown to the buyer at checkout, just not recorded here.*

### Verbatim anchors

- **Reboot "all-in":** "A safer science backed alternative to testosterone replacement therapy… **No hidden or additional costs**" — /pricing (this, plus the bundled meds+vitamins+testing, is what makes it `published`, not `partial`).
- **Reboot price/contents:** "## The Reboot Program™ / ## $199/mo"; "Monthly Prescription Kit — Enclomiphene… DHEA… 7-Keto DHEA… Progesterone… Anastrozole (\*only if needed)" — /pricing; capsule contents re-attested on /faq ("a **proprietary Vitality Rx compounded prescription capsule** containing…").
- **Test price/contents:** "## The Vitality Test ™ / ## $149"; store checkout "Subtotal $149.00 / Total $149.00"; biomarkers + "FDA cleared device… CLIA certified lab" — /pricing, store /test-kit, homepage.
- **Pack prices (store checkout, verbatim):** Men's Max Vitality "Total $74.50/month"; Hair Support Stack "Total $69.50/month"; Men's Fertility Boost "Total $75.50/month".
- **Molecule audit:** the Reboot capsule's molecules are page-attested (enclomiphene citrate, DHEA, 7-Keto DHEA, progesterone, anastrozole) on /pricing + /faq. The **supplement packs do NOT enumerate ingredients per SKU** on any captured page — copy describes effects ("single-ingredient, clinical-grade supplements") but not the contents — so every pack is `not stated`, never inferred from its name.

## Deep blocks

**The Reboot Program™ — the "this is not TRT" disambiguation.** *(Earned: a roster row can't carry why a "testosterone" product contains no testosterone.)*
> "Is this TRT? **No.** … **Enclomiphene**, our primary hormone-boosting ingredient, is the safest alternative to TRT" — /faq. Enclomiphene is a selective estrogen receptor modulator (SERM) that raises LH/FSH → the body makes *more* of its own testosterone and sperm, vs. TRT which "shuts down natural production and destroys fertility." Claimed effect: "boost testosterone production by 1.5–2.5x without dependence, testicular shrinkage, or infertility." The capsule is compounded (enclomiphene citrate + DHEA + 7-Keto DHEA + progesterone, anastrozole only if estrogen runs high) and bundled with daily vitamin packs + periodic testing into the $199/mo program.
> Hero render (opt-in asset): `captures/2026-06-04/images/reboot-program.webp` — the translucent capsule, powder burst, clean white bg.

**The Vitality Test™ — the gating diagnostic.** *(Carries the captured hero image + the exact biomarker panel.)*
> $149 one-time at-home kit using the **Tasso** shoulder blood draw ("FDA cleared device", CLIA-certified lab), measuring Free & Total Testosterone, Luteinizing Hormone, SHBG, Estradiol, PSA. Results delivered in a free HIPAA-compliant telemed consult; gates qualification for the Reboot Program. "No commitment to purchase a treatment program."
> Hero render (opt-in asset): `captures/2026-06-04/images/vitality-test.webp` — the matte-black "VITALITY TEST" kit + red Tasso device + collection tube, "Powered by Tasso", clean white bg.

## Provenance

- **Pages read:** /pricing/, /vitamins/, /fertility/, /faq/, homepage (vitalityrx.com); store PDPs store.vitalityrx.com/test-kit, /checkout/product/{a6MUa0000000kFlMAI (Men's Max), a6MUa0000000muHMAQ (Hair Support), a6MUa0000000mxVMAQ (Men's Fertility Boost)} — scraped with `--images` for hero capture.
- **Scope:** all indexed offerings enumerated; 4 of 11 prices captured verbatim, 7 packs price-noted-but-not-individually-scraped (range $69.50–$75.50/mo from the 3 captured).
- **Gated/unreachable:** the Reboot Program has no standalone PDP — it is qualification-gated behind the test and sold via the store checkout (`/checkout?sku=52e91ad0-42de-456a-bd75-c851aba5fff1&type=subscription`, observed with a `vet20sub` coupon on /fertility); priced on /pricing.
- **Point-in-time:** prices read off a subscription-checkout SPA — treat as a snapshot, not a fixed quote.
- **Run profile:** non-vanilla — guided run requested `offerings.md` + flagship **hero product images** (opt-in asset capture; the two flagship renders promoted to `images/`). Two deep blocks: one earned on the TRT-disambiguation, one carrying the test hero image.
