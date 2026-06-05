---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: onemedical.com       # company key; each offering's slug (its relative url) is its key *within* the company
captured_at: 2026-06-04      # membership/virtual/seniors/business/services reused from captures/2026-06-02; +mindset, chronic-conditions, kids, lab-services 2026-06-04
site_notes: "SERVICES roster, not per-SKU drugs — One Medical sells membership primary care, not priced products; no molecules/forms anywhere (service company). Only the membership fee is published ($199 a year standard; $99/year via Amazon Prime); every care line is included-in-membership and the actual visit/lab cost is billed to insurance (copays/deductibles apply) = on-request. Pay-per-visit flat fee gated to /amazon/pay-per-visit/ (not captured). Prices are stable (no A/B). The '$50 off' string in /services is an EXPIRED 2023 promo (valid until Nov 1 2023) — do not roster."
---

## Portfolio overview

A **services roster, not a product catalog.** One Medical sells one core thing — **membership-based primary care** — to a few buyer segments, with named care sub-brands layered inside the membership. There are **no molecules, forms, or priced SKUs**: the only published price is the membership fee, and everything else is care delivered under that membership and **billed to insurance per visit**. So the roster's job here is to enumerate the *access programs* (who you are → how you buy & pay) and the *included care lines* (what the membership covers), not to price a shelf.

**The shape finding — double monetization.** The defining structure is two stacked revenue streams: a **recurring membership fee** ($199/yr, or $99/yr via Amazon Prime) **plus** ordinary **fee-for-service insurance billing** on visits. A price-consumer asking "what does One Medical cost?" gets a published membership fee *and* an unshown, insurance-dependent visit cost on top — which is why most care lines read `on-request` even though access is "included."

**Prominence read** (what the site foregrounds):
- **Membership / Adults-under-65** `[HIGH]` — the homepage hero + first nav item; the $99 Prime price is the lead CTA.
- **Seniors (65+) and For Business** `[MED]` — co-equal nav sections ("For You" / "For Business"), strong but secondary to the consumer membership.
- **Mindset · Impact · Kids · Lab services** `[MED→LOW]` — named sub-brands surfaced under /services and the mega-nav, positioned as membership inclusions rather than standalone buys.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (service · delivery · access) |
|---|---|---|---|---|---|---|
| One Medical membership | family | — | /membership/ | — | — | The core product — app-first membership primary care, sold to the buyer segments below · in-office + 24/7 virtual · membership fee **plus** insurance-billed visits |
| Adults under 65 (consumer) | buyable | /membership/ | /membership/ | **"$199 a year"** standard; **"$99/year"** (Amazon Prime) | published | Individual consumer membership · "works with your insurance just like a regular doctor's office" · annual, "continues until canceled" |
| Scheduled visits (in-office & video) | buyable | /membership/ | /membership/ | "billed to you/your insurance; copays and deductibles may apply" | on-request | The fee-for-service layer **on top of** membership — the second revenue stream; cost insurance-dependent, not shown |
| Adults 65+ (Medicare / seniors) | buyable | /membership/ | /sixty-five-plus/ | no separate fee shown | on-request | Value-based, relationship-based Medicare primary care (the Iora Health line) · "works with your insurance (yes, including Medicare)" · **no membership fee** |
| One Medical for Business | buyable | /membership/ | /business/ | "Get in touch" (enterprise) | on-request | Employer-sponsored benefit — same in-office + 24/7 virtual care, contracted per-employee |
| Small Business | buyable | /membership/ | /small-business/ | "Get in touch" | on-request | SMB-sized version of the employer benefit |
| Pay-per-visit (one-time virtual) | buyable | — | /amazon/pay-per-visit/ | "for a flat fee" (amount not shown) | on-request | A single one-time virtual visit **without** membership · Amazon-branded · flat fee gated (page not captured) |
| Virtual care (24/7) | buyable | /membership/ | /virtual-care/ | "included in Membership" | published | 24/7 on-demand message + Video Chat + "Treat Me Now" · in all 50 states · **no extra cost, not billed to insurance** |
| One Medical Kids | buyable | /membership/ | /services/kids/ | included w/ membership | on-request | Pediatric & family care · 35+ family-practice offices · well-child, vaccines, lactation (billed to insurance) · free trial code NEWFAMILY30 + complimentary meet-and-greets |
| Mindset by One Medical | buyable | /membership/ | /services/mindset/ | included w/ membership | on-request | PCP-led mental health · medication management, curated referral network, virtual therapy & coaching program (select markets) |
| Impact by One Medical | buyable | /membership/ | /services/chronic-conditions/ | included, eligibility-gated | on-request | Chronic-condition management & prevention (diabetes, hypertension, obesity, lipids, heart disease) · provider-led team + wearables (Apple Health) · ask-your-PCC eligibility |
| Lab services (drop-in) | buyable | /membership/ | /services/lab-services/ | labs billed via third-party lab/insurance | on-request | On-site drop-in phlebotomy at every office · processed by **LabCorp / Quest** · member-gated (requires ≥1 prior appointment) · blood panels, STI, vaccines, PrEP monitoring |
| Care breadth (included) | family | /membership/ | /services/ | included w/ membership | — | The general primary-care surface: everyday care · wellness & prevention · Annual Wellness Visit · urgent concerns · sexual health/STI · LGBTQIA+ care |

## Verbatim anchors

- **Membership fee (standard):** "All for just **$199 a year**. Membership subscription continues until canceled." — `captures/2026-06-02/membership.md`
- **Membership fee (Amazon Prime):** "Now **Amazon Prime members** can purchase One Medical membership for **$99/year**." / "Membership costs only **$99/year**." — `captures/2026-06-02/homepage.md`
- **Visits billed separately (why most lines are `on-request`):** "Like a typical doctor's office, these visits are scheduled and we bill you/your insurance; copays and deductibles may apply if billed to insurance." — `captures/2026-06-02/membership.md`. Membership fee itself is cash and "**not a covered benefit … such as the Health Saving Account or Flexible Spending Account**" — `captures/2026-06-02/insurance.md`.
- **24/7 virtual care, not billed:** "24/7 on-demand Video Chat and Treat Me Now — at no extra cost and we do not bill insurance for these services." — `captures/2026-06-02/insurance.md`
- **Pay-per-visit:** "book a one-time virtual visit for a flat fee with Pay-per-visit" → /amazon/pay-per-visit/ (flat fee not shown) — `captures/2026-06-02/virtual_care.md`
- **Labs → third-party processing:** "Your phlebotomist completes the lab work and sends it off for processing at a third-party lab … We work with third-party labs such as LabCorp and Quest." — `captures/2026-06-04/lab_services.md`
- **Molecule · form audit:** **N/A — service company.** No captured page states a molecule or drug form for any offering (correctly — One Medical delivers care and prescribes the patient's clinically-appropriate meds, it doesn't sell branded drug SKUs). Recorded `not stated` for the whole roster, by attestation, not omission.

## Deep blocks

**Membership pricing & the two-stream cost structure** *(earned — resolves the "what does it actually cost?" ambiguity a single roster row can't carry)*

One Medical's price is deliberately two-part, and only the first part is published:

1. **The membership fee** — verbatim **"$199 a year"** standard, or **"$99/year"** for Amazon Prime members. Self-contained, annual, auto-renewing ("continues until canceled"). This is what the homepage and /membership advertise, and it's the only `published` number in the company. The **Amazon Prime $99/year** is the post-acquisition distribution lever — half the standard price, funneling Prime's base into membership.
2. **The care itself** — every scheduled in-office or video visit is **"billed to you/your insurance; copays and deductibles may apply."** That cost is insurance-plan-dependent and **never shown**, which is why Kids, Mindset, Impact, Lab services, and scheduled visits all read `on-request` despite being "included" in membership access. The membership buys the *door and the app*; walking through it bills like any doctor's office.

The two carve-outs that *don't* bill on top: **24/7 virtual care** (Video Chat / Treat Me Now — "no extra cost," explicitly not billed to insurance) and the **seniors/Medicare** line (no separate membership fee — it runs on the value-based Iora economics). Net: the published-price surface is tiny ($199 / $99); the real cost surface is insurance.

## Provenance

- **Pages read:** `captures/2026-06-02/` — membership, homepage, virtual_care, insurance, seniors, business, services (reused, 2-day-warm); `captures/2026-06-04/` — mindset, chronic_conditions, kids, lab_services (new this run).
- **Scope:** Enumerated the access programs + named care sub-brands at the indexed level. The general care categories under /services (everyday-care, wellness-and-prevention, urgent-concerns, lgbtq, annual-wellness) are rolled into the "Care breadth (included)" family row, not separate leaves — they're membership-included care surfaces, not separately-positioned offerings.
- **Gated / unreachable:** Pay-per-visit flat fee (gated to /amazon/pay-per-visit/, not captured); per-visit copay/deductible amounts (insurance-plan-dependent); enterprise/employer pricing ("Get in touch").
- **Snapshot caveat:** Prices captured point-in-time; the $99 Prime price is an Amazon-channel offer. No A/B instrumentation observed. The "$50 off" string in /services is an **expired 2023 promo** — deliberately excluded from the roster.
- **Run profile:** guided/express — offerings module run on a **Services / Consulting** company (normally shape-gated to skip). Written because the company has a **published price ($199/$99) and enumerable programs** — it clears the hard-floor decline — but the roster is a *services* roster (programs + care lines), not a per-SKU/molecule drug roster; visibility skews `on-request` because care bills to insurance. **No hero/product images** — One Medical is a service; pages carry only lifestyle/illustration (exam rooms, phlebotomist, family), no clean isolated product render to capture.
</content>
