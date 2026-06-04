---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: clerky.com
captured_at: 2026-06-04
site_notes: "Pricing is two one-time PACKAGES ($427 Pay Per Use / $819 Company Lifetime), not per-SKU — individual product prices are never shown as a number. In the pricing table a checkmark = included in that package, 'Pay Per Use' = à-la-carte (price revealed in-app), '+ 3rd party fees' = state/IRS pass-through. The comparison table is on the HOMEPAGE (static); /pricing itself is a JS wall (thin scrape). Products are anchor sections on /startups/products (#formation … #maintenance) — no individual PDPs, so every sub-product slugs to its line anchor '(no PDP — …)'. No molecules (legal docs); What leads with the document type."
---

## Portfolio overview

Clerky sells **standard startup legal paperwork**, organized into five product lines — **Formation** (the flagship), **Fundraising**, **Hiring**, **Commercial**, **Maintenance** — plus a free **Attorney Account** surface. The shape finding that matters for a price consumer: **there is no per-SKU price**. Everything is sold through **two one-time packages** — *Pay Per Use* **$427** and *Company Lifetime Package* **$819** — and the individual products are either *included* in a package (a checkmark), *à-la-carte* ("Pay Per Use", number shown only in-app), or *state-fee pass-through* ("+ 3rd party fees"). So most rows below are `partial` by necessity, not by gating choice.

**Prominence:** Formation is the unambiguous hero `[HIGH]` — the company's own label ("The standard for startup formation"), the homepage hero ("Ready to Incorporate?"), the "20,000+ Startups Incorporated" proof point, and the structural fact that the other four lines are framed as "Go Further" *after* you form. Within Formation, **Incorporation** is the entry product; the rest of the lines are companions that unlock once you've formed on Clerky `[MED]` (section order + the "form, then go further" framing).

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (form · access) |
|---|---|---|---|---|---|---|
| Pay Per Use | buyable | — | /pricing#pay-per-use | **$427** "One-Time Fee" · "Best for most startups" | published | Entry package: Incorporation + Post-Incorporation Setup, pay-per-use thereafter · online self-serve |
| Company Lifetime Package | buyable | — | /pricing#company-lifetime-package | **$819** "One-Time Fee" | published | Full package: everything, with unlimited fundraising / hiring / NDAs / maintenance · online self-serve |
| Formation | family | — | /startups/products#formation | — | — | Delaware C-corp formation line — "The standard for startup formation" |
| Incorporation | buyable | Formation | (no PDP — /startups/products#formation) | incl. in **$427** / **$819**; "Includes $203 Delaware expedited filing fees" + "Includes $125 first-year Delaware registered agent fee" | published | Delaware C-corporation · DE Sec. of State filing, 2-3 business days · self-serve |
| Post-Incorporation Setup | buyable | Formation | (no PDP — /startups/products#formation) | "Pay Per Use" (incl. in $819) | partial | Action of Incorporator, bylaws, initial board consent, restricted-stock issuance + vesting, 83(b) support, CIIAA · doc gen + e-sign |
| Foreign Qualification | buyable | Formation | (no PDP — /startups/products#formation) | "Pay only 3rd party fees" ($819) / "Pay Per Use + 3rd party fees" | partial | Register to do business in home state · CA & NY direct, other states via partners |
| Stock Plan Adoption | buyable | Formation | (no PDP — /startups/products#formation) | "Pay Per Use" (incl. in $819) | partial | Adopt a stock plan to issue restricted stock / options to employees, consultants, advisors |
| EIN Application (non-US founders) | buyable | Formation | (no PDP — /startups/products#formation) | incl. in **$427** / **$819** | published | IRS EIN obtained by fax, "100% in-house, not outsourced" |
| Corporate Bank Account Application | buyable | Formation | (no PDP — /startups/products#formation) | incl. in **$427** / **$819** | published | Pre-filled applications to popular startup banks · "No EIN Needed" |
| Fundraising | family | — | /startups/products#fundraising | — | — | Financing instruments — "Over $5 billion raised from over 1,000 top seed investors" |
| Safes | buyable | Fundraising | (no PDP — /startups/products#fundraising) | "Pay Per Use" / "Unlimited!" in $819 | partial | SAFE issuance — valuation cap / discount / cap + discount · financing checklist + signature escrow |
| Convertible Notes | buyable | Fundraising | (no PDP — /startups/products#fundraising) | "Pay Per Use" / "Unlimited!" in $819 | partial | Convertible note issuance — valuation cap / discount / both |
| Hiring | family | — | /startups/products#hiring | — | — | Employee / consultant / advisor paperwork + equity compensation |
| New Hire Paperwork | buyable | Hiring | (no PDP — /startups/products#hiring) | "Pay Per Use" / "Unlimited!" in $819 | partial | Offer letters, consulting agreements, advisor agreements, CIIAA |
| Equity Compensation | buyable | Hiring | (no PDP — /startups/products#hiring) | "Pay Per Use" / "Unlimited!" in $819 | partial | Restricted stock; regular + early-exercisable stock options; 83(b) reminders |
| Commercial | family | — | /startups/products#commercial | — | — | Inter-company agreements |
| NDAs | buyable | Commercial | (no PDP — /startups/products#commercial) | "Pay Per Use" / "Unlimited!" in $819 | partial | One-way and mutual non-disclosure agreements |
| Maintenance | family | — | /startups/products#maintenance | — | — | Post-formation corporate changes |
| Charter Amendments | buyable | Maintenance | (no PDP — /startups/products#maintenance) | "Pay only 3rd party fees" ($819) / "Pay Per Use + 3rd party fees" | partial | Company-name change; increase authorized shares |
| Board Consents | buyable | Maintenance | (no PDP — /startups/products#maintenance) | "Pay Per Use" / "Unlimited!" in $819 | partial | Change directors / officers; add new co-founders |
| Attorney Account | buyable | — | /attorneys | Free | published | Private workspace for startup attorneys + "over 40 advanced products that are not publicly available" |

### Verbatim anchors

The price footnotes the table points at (all greppable in `captures/2026-06-04/homepage.md` unless noted):

- **Pay Per Use:** "$427" · "One-Time Fee" · "Best for most startups"
- **Company Lifetime Package:** "$819" · "One-Time Fee"
- **Incorporation bundled fees:** "Includes $203 Delaware expedited filing fees" · "Includes $125 first-year Delaware registered agent fee"
- **Table tokens** (decide `partial` vs `published`): a blue checkmark = included in that package; "Pay Per Use" = à-la-carte, no number shown; "Unlimited!" = unlimited in the $819 package; "Pay only 3rd party fees" / "Pay Per Use + 3rd party fees" = Clerky fee not separately quantified, state pass-through.
- **Prerequisite note:** "Some items above may have prerequisites. Don't worry, we'll help you do everything in the right order!"
- **Scale claims** (self-reported): "20,000+ Startups Incorporated!" (homepage); "Over $5 billion raised from over 1,000 top seed investors" (`products.md`).
- **Molecule audit:** N/A — these are legal documents, not pharma SKUs; no molecule field applies, so `What` leads with the document type.

## Deep blocks

**One earned — the pricing model, because no roster row can carry a per-SKU number.** Spine: *Clerky doesn't price products; it prices two packages and bundles products into them.*

- **Pay Per Use — "$427" "One-Time Fee":** covers Incorporation + Post-Incorporation Setup outright; every other line is then **à-la-carte "Pay Per Use"** (the price appears only once you start that product in the app — never on the marketing site). This is why eight rows above read `partial`: the all-in is real but not shown standalone.
- **Company Lifetime Package — "$819" "One-Time Fee":** the same Formation base, plus **"Unlimited!"** fundraising (safes/convertible notes), hiring (offer letters/equity comp), NDAs, and board-consent maintenance — converting the à-la-carte lines to included. Charter amendments and foreign qualification stay **"Pay only 3rd party fees"** (state filing pass-through) even here.
- **Consequence for a price consumer:** "what does a SAFE / an NDA / a stock-option grant cost on Clerky?" has **no published answer** — it's either no marginal charge inside the $819 package or an in-app pay-per-use number. The only firm public prices are **$427** and **$819** (+ the bundled **$203** / **$125** Delaware fees inside formation).

## Provenance

- **Pages read:** `captures/2026-06-04/homepage.md` (the full pricing-comparison table — the authoritative price source), `captures/2026-06-04/products.md` (the line/sub-product taxonomy + the "$5 billion / 1,000 investors" claim), with `/startups/products` nav anchors as the slug source. `/pricing` was captured but is a JS wall (thin — only the H1 rendered, even with `--proxy enhanced`).
- **Scope:** enumerated **complete at the indexed level** — the 5 product lines and every named sub-product the products page lists, plus the 2 packages and the attorney surface (21 rows). Sub-products have **no individual PDPs** (anchor sections only), so each slugs to its line anchor.
- **Gated / not shown:** every individual product's standalone price (à-la-carte "Pay Per Use" numbers live in the signed-in app at `app.clerky.com`, never on the marketing site); "+ 3rd party fees" amounts (state/IRS, unquantified).
- **Point-in-time caveat:** package prices ($427 / $819) and the bundled Delaware fees ($203 / $125) are a 2026-06-04 snapshot; no A/B instrumentation observed, but legal/state fees drift — re-check on next capture.
- **Run profile:** opt-in `offerings.md` requested in the guided pre-flight ("All the above"). No emphasis, no hero-image capture, no PDP-anatomy block.
