---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: kingsbergmedical.com
captured_at: 2026-06-17
enumeration: indexed-complete
site_notes: "Indexed catalog is /product/; homepage repeats the medication carousel/details. Public product prices are not shown on captured PDPs; cost ranges live on FAQ/cost pages. Testosterone Cypionate, Propionate, and Enanthate nav URLs returned duplicate /testosterone-injections/ bodies, so keep one canonical injection page and record the aliases in Provenance."
---

## Portfolio overview

Kingsberg Medical is a **Multi-product** hormone clinic catalog, not a single-drug telehealth funnel. The indexed `/product/` page carries 12 product cards: semaglutide, sermorelin, 6 HGH brands, and 4 hormone panels. The broader nav adds testosterone therapy/injections and cost/insurance explainers. Growth hormone and testosterone are co-led on the homepage and nav [MED]; semaglutide is present as a product-card line but is not the dominant front door [LOW].

Price visibility is mostly **partial** or **on-request**. HGH and testosterone have public family-level cost ranges on cost/FAQ pages, but PDP-specific all-in pricing is not published. Lab panels and compounded sermorelin/semaglutide pages did not show prices in the captured packet.

## Roster

Complete at the indexed product/service level surfaced by `/product/`, the homepage medication carousel, and the testosterone injection/category pages. Slug is the page-attested within-company key.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Growth hormone therapy** | family | — | `/growth-hormone/` | — | — | HGH treatment family; lab/physical exam and physician prescription pathway. |
| Omnitrope | buyable | Growth hormone therapy | `/product/omnitrope/` | `$500.00 to $1000.00 or more per month` (family-level HGH estimate) | partial | somatropin / recombinant human growth hormone · injectable vial/diluent, 5.8mg vial surfaced · doctor prescription only. |
| Zomacton | buyable | Growth hormone therapy | `/product/zomacton/` | `$500.00 to $1000.00 or more per month` (family-level HGH estimate) | partial | somatropin / recombinant human growth hormone · injectable vials 5mg and 10mg, 5mg pen also mentioned · doctor prescription only. |
| Genotropin | buyable | Growth hormone therapy | `/product/genotropin/` | `$500.00 to $1000.00 or more per month` (family-level HGH estimate) | partial | somatropin / recombinant human growth hormone · MiniQuick injectors 0.4mg, 0.6mg, 0.8mg, 1.0mg · doctor prescription only. |
| Norditropin | buyable | Growth hormone therapy | `/product/norditropin/` | `$500.00 to $1000.00 or more per month` (family-level HGH estimate) | partial | somatropin · FlexPro Pen injectors 5mg, 10mg, 15mg, 30mg · doctor prescription only. |
| Humatrope | buyable | Growth hormone therapy | `/product/humatrope/` | `$500.00 to $1000.00 or more per month` (family-level HGH estimate) | partial | somatropin · injectable 5mg vial surfaced in carousel; cartridges also described on PDP · doctor prescription only. |
| Saizen | buyable | Growth hormone therapy | `/product/saizen/` | `$500.00 to $1000.00 or more per month` (family-level HGH estimate) | partial | somatropin · injectable vials 5mg and 8.8mg · doctor prescription only. |
| **Peptide / GH secretagogue** | family | — | `/product/sermorelin/` | — | — | Sermorelin line; positioned as related to growth-hormone deficiency and HGH alternatives. |
| Sermorelin | buyable | Peptide / GH secretagogue | `/product/sermorelin/` | — | on-request | sermorelin acetate · subcutaneous injection, vials/pen/cartridges; compounded on homepage carousel · prescription only. |
| **Medical weight loss** | family | — | `/product/semaglutide/` | — | — | GLP-1 line in the product index; virtual pre-screening/consultation before prescription. |
| Semaglutide | buyable | Medical weight loss | `/product/semaglutide/` | — | on-request | semaglutide / GLP-1 receptor agonist · weekly subcutaneous injectable, vials/pen; compounded on homepage carousel · prescription only. |
| **Testosterone therapy** | family | — | `/testosterone/` | — | — | Low-testosterone treatment family; labs and physician review before TRT prescription. |
| Testosterone injections | buyable | Testosterone therapy | `/testosterone-injections/` | `$70-$100/month without insurance` | partial | testosterone cypionate named as common injection; cypionate, propionate, enanthate, Depo Testosterone, and Watson Testosterone surfaced as routes/links · prescription only; medication-only quote excludes labs/visits/supplies. |
| **Hormone testing** | family | — | `/hormone-testing/` | — | — | Lab testing family for hormone, thyroid, metabolic, lipid, IGF-1, and sex-hormone markers. |
| Super Male Panel | buyable | Hormone testing | `/product/super-panel-male/` | — | on-request | diagnostics · blood panel with CMP, CBC, lipid panel, PSA, IGF-1, estradiol, thyroid hormones, free/total testosterone, vitamin D · LabCorp, results in 24-72 business hours. |
| Super Female Panel | buyable | Hormone testing | `/product/super-panel-female/` | — | on-request | diagnostics · blood panel with CMP, CBC, lipid panel, DHEA-S, IGF-1, progesterone, testosterone free/total, estradiol, thyroid hormones, vitamin D · LabCorp. |
| Complete Male Panel | buyable | Hormone testing | `/product/complete-panel-male/` | — | on-request | diagnostics · CMP, CBC, lipid panel, PSA, IGF-1, testosterone serum, estradiol, thyroid hormones · LabCorp. |
| Complete Female Panel | buyable | Hormone testing | `/product/complete-panel-female/` | — | on-request | diagnostics · CMP, CBC, lipid panel, progesterone, IGF-1, testosterone serum, estradiol, thyroid hormones · LabCorp. |

### Verbatim anchors

- **HGH public range:** "you could expect to pay anywhere from $500.00 to $1000.00 or more per month for growth hormone therapy" — repeated on the homepage and HGH cost pages. This is a family-level estimate, not a brand-specific buy box.
- **TRT public range:** "A typical male patient should expect to pay anywhere from $200.00 to $350.00 per month for testosterone therapy." The same paragraph says some costs "may be covered by insurance" and says to include supporting medications, syringes, sharps container, alcohol wipes, and shipping.
- **Testosterone injections drug-only warning:** "Generic testosterone cypionate injections typically cost $70-$100/month without insurance." The same page warns that lab work, doctor visits, and supplies can add costs; it names blood work as "($80-$200)".
- **Prescription gate:** Product carousel availability is "By doctor`s prescription only" for HGH brands, sermorelin, and semaglutide.
- **Lab panel turnaround:** Panel pages say results are "typically available within 24-72 business hours" and "We only use highly skilled and qualified labs like LabCorp for our test panels."

## Deep blocks

### Semaglutide

- **Hero image:** `store/kingsbergmedical-com/captures/2026-06-17/images/semaglutide.webp`
- **Why it earns a block:** It is the indexed catalog's GLP-1/weight-loss SKU, but the site does not publish a price. The PDP describes semaglutide as a prescription GLP-1 receptor agonist, says it is only available with a doctor's prescription, and routes users through pre-screening plus an initial consultation that can be done virtually.
- **Dosing note:** The captured PDP says patients will likely start at "0.25 mg once a week" and increase every 4 weeks until the full dose.

### Sermorelin

- **Hero image:** `store/kingsbergmedical-com/captures/2026-06-17/images/sermorelin.webp`
- **Why it earns a block:** The roster cell needs disambiguation: Kingsberg presents sermorelin as a growth-hormone-releasing hormone/GHRF analog, not direct HGH replacement. The PDP says it is a synthetic version of a human growth hormone-releasing hormone, an injectable prescription medication, and "only available with a doctor's prescription."
- **Forms:** Homepage carousel says manufacturer "Compounded," delivery form "Injectable," forms "Vials, Pen, Cartridges"; PDP lists 0.5 mg and 3.0 mg vials.

### Omnitrope

- **Hero image:** `store/kingsbergmedical-com/captures/2026-06-17/images/omnitrope.webp`
- **Why it earns a block:** It is a clean example of the branded HGH SKU template. The PDP says "Omnitrope® is the prescription human growth hormone made by Sandoz" and identifies it as recombinant DNA/somatropin. Homepage carousel records manufacturer Sandoz Inc, injectable form, 5.8mg vials, prescription-only access, and mixing/refrigeration requirements.

## Provenance

- **Pages read:** `/product/` plus all 12 product/panel PDPs, homepage medication carousel, `/growth-hormone/`, `/growth-hormone-injections/`, `/testosterone/`, `/testosterone-injections/`, `/hormone-testing/`, and six cost/insurance pages.
- **Scope:** Indexed-complete at the product-card/service-family level. Leaf dose strengths and every SEO article route were not separately rostered.
- **Gated/unpriced:** No captured PDP buy box published a final SKU price for sermorelin, semaglutide, HGH brands, or lab panels; family cost ranges are public but final cost is patient/prescription dependent.
- **Duplicate aliases:** Testosterone Cypionate, Propionate, and Enanthate nav URLs were probed during the run and returned the same body as `/testosterone-injections/`; they are recorded as aliases in the testosterone row, not as separate active captures.
- **Run profile:** guided — full `/research-company` capture requested `+offerings`, with flagship hero images promoted for semaglutide, sermorelin, and omnitrope. The Super Male Panel image candidate was skipped because it was a generic microscope banner, not a product render.
