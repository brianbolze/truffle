# Retro — notion.com: first non-telehealth (non-SKU) offerings.md

First SaaS run of the module. The shape is plan × app × feature, not SKU — so the storefront assumptions strained predictably.

- **Bent the contract — where it strained.**
  - **Price = `incl. (Business $20)` / `incl. (seat)`** — invented token. The contract gives *verbatim price* or `—` (family umbrella); it has no slot for "bundled into a paid plan, no standalone price." ~12 feature rows used `incl.` → **strained** (neither verbatim nor `—`, lint-silent so it passed, but it's a convention I made up).
  - **Slug** — the 4 plan rows all share `/pricing` (no per-plan URL exists), and **6 rows** used the `(no PDP — …)` escape (Databases, Forms/Sites, Workers, API, CLI, custom-domains). "Slug = within-company key, never blank" held *structurally* but the key is fiction for a non-storefront. **Strained.**
  - **Kind = family/buyable** — kept the values, but "buyable" quietly became "any line you get" — a *free* app (Calendar/Mail), a *bundled* feature, and a *not-yet-billed* line (Workers) are all `buyable`. The family/leaf distinction **held**; the purchasable semantics **didn't**.
  - **Visibility = published** on bundled features — the *plan* price is shown, the *feature* has none. Stretches "can I get a price?" but held loosely.

- **Added: the `Category` column** (`app` / `AI feature` / `workspace feature` / `plan` / `developer` / `add-on` / `ecosystem`) — Brian's downloadable-product-vs-marketed-feature axis. **Keep local for now.** But the product-vs-feature-vs-plan-vs-add-on cut will recur for *any* bundled-SaaS company; it's a real **candidate for an optional universal column** — promote only if a 2nd SaaS run confirms the same need (don't generalize on n=1). Reframed `What` (dropped the `molecule · form · access` lead) was already sanctioned, not an addition.

- **Where OFFERINGS.md was silent — the exact guesses.**
  1. **Price of a bundled-but-not-free feature.** Verbatim-or-`—` only; nothing for "included in a $20 plan." → guessed `incl.`.
  2. **Slug for tier rows sharing one pricing page.** "Never blank, never constructed, a real URL" — silent on 4 plans that legitimately live at one `/pricing`. → reused `/pricing` ×4 (degenerate keys).
  3. **Kind vocabulary for non-SKU.** `family|buyable` is storefront-shaped; silent on plan/app/feature/add-on. → kept `buyable` as a catch-all.

- **One change for the next non-Rx run.** Add a short **"Non-SKU / bundled shapes"** note to OFFERINGS.md that blesses the three patterns instead of leaving them ad hoc: (a) an **`incl.`** (or `bundled`) price token for plan-included features; (b) explicitly **allow a shared slug** for tier rows on one pricing page (or a `/pricing#tier` convention); (c) state **Kind values are advisory** — a vertical may relabel. One paragraph kills all three guesses and makes the next SaaS file reproducible rather than re-improvised.

- **Verdict.** It **fit, with mild forcing** — the 7-column spine + closed visibility set held (lint clean, cross-company `rg` still works), but ~⅓ of the signal lives in the added `Category` column and the price/slug semantics are largely fictional for a non-storefront. Good enough to keep; worth one contract note before the next bundled-SaaS run so it isn't re-derived from scratch.
