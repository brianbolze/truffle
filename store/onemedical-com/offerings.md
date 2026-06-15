---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: onemedical.com       # company key; each offering's slug (its relative url) is its key *within* the company
captured_at: 2026-06-15      # full re-capture across both hosts (onemedical.com + health.amazon.com)
enumeration: indexed-complete   # all access programs + named care lines rostered at the indexed level (Flagship + companions); only leaf care-categories rolled into the "Care breadth" family row
site_notes: "SERVICES roster, not per-SKU drugs — One Medical sells membership primary care, not priced products; no molecules/forms anywhere (service company). Published prices are membership/visit fees only: membership $199/yr standard, $9/mo-or-$99/yr via Amazon Prime (+$66/yr per extra family member, max 5); On-Demand Care (formerly Pay-per-visit) from $29 messaging / $49 video, self-pay; every care line is included-in-membership and the actual scheduled-visit/lab cost is billed to insurance (copays/deductibles apply) = on-request. Two surfaces: onemedical.com (membership + care lines) and health.amazon.com/onemedical (Amazon framing of membership + the On-Demand Care per-visit product, accessed via Amazon.com). Prices are stable (no A/B); a '$69 first year then $99/yr' Prime intro promo ($30 off) is point-in-time. The '$50 off' string in /services is an EXPIRED 2023 promo — do not roster."
---

## Portfolio overview

A **services roster, not a product catalog.** One Medical sells one core thing — **membership-based primary care** — to a few buyer segments, with named care sub-brands layered inside the membership, plus a no-membership **per-visit** option sold through Amazon. There are **no molecules, forms, or priced drug SKUs**: the published prices are the membership fee and the per-visit fee; everything else is care delivered under membership and **billed to insurance per visit**. So the roster enumerates the *access programs* (who you are → how you buy & pay) and the *included care lines* (what the membership covers), not a priced shelf.

**The shape finding — double monetization, now with an Amazon per-visit rail.** The defining structure is two stacked revenue streams: a **recurring membership fee** ($199/yr, or $9/mo–$99/yr via Amazon Prime) **plus** ordinary **fee-for-service insurance billing** on scheduled visits. Post-acquisition Amazon bolted on a third, parallel rail — **On-Demand Care** ($29 messaging / $49 video, self-pay, no membership) sold straight through Amazon.com. A price-consumer asking "what does One Medical cost?" gets published membership and per-visit floors, *plus* an unshown, insurance-dependent scheduled-visit cost — which is why the membership's own care lines read `on-request` even though access is "included," while the per-visit product reads `published`.

**Prominence read** (what the site foregrounds):
- **Membership / Adults-under-65** `[HIGH]` — the homepage hero + first nav item; the $99 Prime price is the lead CTA.
- **On-Demand Care (Pay-per-visit)** `[MED]` — the lead alternative on the health.amazon.com surface (a two-card Membership-vs-On-Demand comparison), but absent from the onemedical.com hero.
- **Seniors (65+) and For Business** `[MED]` — co-equal nav sections ("For You" / "For Business"), strong but secondary to the consumer membership.
- **Mindset · Impact · Kids · Lab services** `[MED→LOW]` — named sub-brands surfaced under /services and the mega-nav, positioned as membership inclusions rather than standalone buys.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (service · delivery · access) |
|---|---|---|---|---|---|---|
| One Medical membership | family | — | /membership/ | — | — | The core product — app-first membership primary care, sold to the buyer segments below · in-office + 24/7 virtual · membership fee **plus** insurance-billed scheduled visits |
| Adults under 65 (consumer) | buyable | /membership/ | /membership/ | **"$199 a year"** standard; **"$9/mo or $99/yr for Prime members"**; **"$66/year each"** add'l family member (max 5) | published | Individual/family consumer membership · "works with your insurance just like a regular doctor's office" · annual, "continues until canceled" |
| On-Demand Care (formerly Pay-per-visit) | buyable | — | https://health.amazon.com/onemedical/ppv | **"from $29"** messaging-only / **"$49"** video ("varies by state") | published | One-time virtual visit for 30+ common conditions · **no membership, self-pay, FSA/HSA eligible, no insurance** · accessed via Amazon.com (PDP not scraped; price attested on amazon_onemedical + amazon_prime) |
| Scheduled visits (in-office & video) | buyable | /membership/ | /membership/ | "billed to you/your insurance; copays and deductibles may apply" | on-request | The fee-for-service layer **on top of** membership — the second revenue stream; cost insurance-dependent, not shown |
| Adults 65+ (Medicare / seniors) | buyable | /membership/ | /sixty-five-plus/ | no separate fee shown | on-request | Value-based, relationship-based Medicare primary care (the Iora Health line) · "works with your insurance (yes, including Medicare)" · **no membership fee** |
| One Medical for Business | buyable | /membership/ | /business/ | "Get in touch" (enterprise) | on-request | Employer-sponsored benefit — same in-office + 24/7 virtual care, contracted per-employee |
| Small Business | buyable | /membership/ | /small-business/ | "Get in touch" | on-request | SMB-sized version of the employer benefit |
| Virtual care (24/7) | buyable | /membership/ | /virtual-care/ | "included in Membership" | published | 24/7 on-demand message + Video Chat + "Treat Me Now" · in all 50 states · **no extra cost, not billed to insurance** |
| One Medical Kids | buyable | /membership/ | /kids/ | included w/ membership | on-request | Pediatric & family care · 35+ family-practice offices · well-child, vaccines, lactation (billed to insurance) · free trial code NEWFAMILY30 + complimentary meet-and-greets |
| Mindset by One Medical | buyable | /membership/ | /services/mindset/ | included w/ membership | on-request | PCP-led mental health · medication management, curated referral network, virtual therapy & coaching program (select markets) |
| Impact by One Medical | buyable | /membership/ | /services/chronic-conditions/ | included, eligibility-gated | on-request | Chronic-condition management & prevention (diabetes, hypertension, obesity, lipids, heart disease) · provider-led team + wearables (Apple Health) · ask-your-PCC eligibility |
| Lab services (drop-in) | buyable | /membership/ | /services/lab-services/ | labs billed via third-party lab/insurance | on-request | On-site drop-in phlebotomy at every office · processed by **LabCorp / Quest** · member-gated (requires ≥1 prior appointment) · blood panels, STI, vaccines, PrEP monitoring |
| Care breadth (included) | family | /membership/ | /services/ | included w/ membership | — | The general primary-care surface: everyday care · wellness & prevention · Annual Wellness Visit · urgent concerns · sexual health/STI · LGBTQIA+ care |

## Verbatim anchors

- **Membership fee (standard):** "All for just **$199 a year**. Membership subscription continues until canceled." — `captures/2026-06-15/membership.md`
- **Membership fee (Amazon Prime, monthly or annual):** "**$9/mo or $99/yr for Prime members**" / "**$199/yr for non-Prime members**" / "Prime membership required" — `captures/2026-06-15/amazon_onemedical.md`. "Regular price without Prime: **$199/year for each member**." — `captures/2026-06-15/amazon_prime.md`. Intro promo (point-in-time): "$30 off … **$69 for one year, then $99/year**."
- **Family add-on:** "Add family members for only **$66/year each**" — `captures/2026-06-15/amazon_prime.md`; "$66/yr for each additional family member (maximum 5)" — `captures/2026-06-15/amazon_onemedical.md`.
- **On-Demand Care (formerly Pay-per-visit), self-pay floors:** "you pay an out-of-pocket fee\* starting at **$29 for a messaging only visit or $49 for a video visit** (\*Prices vary by condition and visit type … Messaging only visits are not available in some states)." — `captures/2026-06-15/amazon_prime.md`. "Self-pay visits – no insurance accepted or needed · FSA/HSA eligible" — `captures/2026-06-15/amazon_onemedical.md`.
- **Visits billed separately (why most lines are `on-request`):** "Like a typical doctor's office, these visits are scheduled and we bill you/your insurance; copays and deductibles may apply if billed to insurance." — `captures/2026-06-15/membership.md`. Membership fee itself is cash and "**not a covered benefit … such as the Health Saving Account or Flexible Spending Account**" — `captures/2026-06-15/insurance.md`.
- **24/7 virtual care, not billed:** "24/7 on-demand Video Chat and Treat Me Now — at no extra cost and we do not bill insurance for these services." — `captures/2026-06-15/insurance.md`
- **Labs → third-party processing:** "Your phlebotomist completes the lab work and sends it off for processing at a third-party lab … We work with third-party labs such as LabCorp and Quest." — `captures/_archive/2026-06-04/lab_services.md` (carried from prior run; line not re-scraped this run).
- **Molecule · form audit:** **N/A — service company.** No captured page states a molecule or drug form for any offering (correctly — One Medical delivers care and prescribes the patient's clinically-appropriate meds, it doesn't sell branded drug SKUs). Recorded `not stated` for the whole roster, by attestation, not omission.

## Deep blocks

**Membership pricing & the two-stream cost structure** *(earned — resolves the "what does it actually cost?" ambiguity a single roster row can't carry)*

One Medical's price is deliberately layered, and the published surface is just the entry fee:

1. **The membership fee** — verbatim **"$199 a year"** standard, or **"$9/mo or $99/yr"** for Amazon Prime members (Prime required; "up to 50% savings" vs $199), **+ "$66/year each"** for up to five additional family members. Self-contained, auto-renewing ("continues until canceled"). This is what the homepage and /membership advertise — the only membership-level `published` number. The **Amazon Prime** price is the post-acquisition distribution lever.
2. **The care itself** — every scheduled in-office or video visit is **"billed to you/your insurance; copays and deductibles may apply."** That cost is insurance-plan-dependent and **never shown**, which is why Kids, Mindset, Impact, Lab services, and scheduled visits all read `on-request` despite being "included" in membership access. The membership buys the *door and the app*; walking through it bills like any doctor's office.
3. **The Amazon per-visit rail** — **On-Demand Care (formerly Pay-per-visit)**, sold through Amazon.com with **no membership**: **"from $29"** for a messaging-only visit, **"$49"** for video, self-pay, FSA/HSA eligible, "no insurance accepted or needed," for 30+ common conditions. This is the one `published`, self-contained, all-in price in the whole company — and the line that most resembles the rest of the telehealth cohort.

The two carve-outs that *don't* bill on top: **24/7 virtual care** (Video Chat / Treat Me Now — "no extra cost," explicitly not billed to insurance) and the **seniors/Medicare** line (no separate membership fee — it runs on the value-based Iora economics). Net: the published-price surface is the two entry fees ($199/$99/$9-mo membership and $29/$49 per-visit); the real ongoing cost surface for members is insurance.

## Provenance

- **Pages read:** `captures/2026-06-15/` — homepage, membership, virtual_care, insurance, seniors, business, services, faq, mindset, kids (onemedical.com); amazon_onemedical, amazon_prime (health.amazon.com). Lab-services line carried from `captures/_archive/2026-06-04/lab_services.md` (not re-scraped this run; cited as archive).
- **Scope:** Enumerated the access programs + named care sub-brands at the indexed level (`indexed-complete` for a `Flagship + companions` shape). The general care categories under /services (everyday-care, wellness-and-prevention, urgent-concerns, lgbtq, annual-wellness) are rolled into the "Care breadth (included)" family row — leaf care surfaces, not separately-positioned offerings. The On-Demand Care PDP (/onemedical/ppv) itself was not scraped, but its price is attested on the two captured Amazon pages.
- **Gated / unreachable:** per-visit copay/deductible amounts (insurance-plan-dependent); enterprise/employer pricing ("Get in touch"); the On-Demand Care per-condition price variance ("varies by state/condition").
- **Snapshot caveat:** Prices captured point-in-time; the $9/$99 Prime price is an Amazon-channel offer, and the "$69 first year" is a promo. No A/B instrumentation observed. The "$50 off" string in /services is an **expired 2023 promo** — deliberately excluded from the roster.
- **Run profile:** offerings module run on a **Services / Consulting** company (normally shape-gated to skip), written because the company has **published prices + enumerable programs** (clears the hard-floor decline). This refresh **adds the health.amazon.com surface** — resolving the On-Demand Care fee the prior run gated as unknown, and the $9/mo + $66/yr-family tiers. Re-stamped 1.1→1.2 (added `enumeration`). **No hero/product images** — One Medical is a service; pages carry only lifestyle/illustration, no clean isolated product render.
