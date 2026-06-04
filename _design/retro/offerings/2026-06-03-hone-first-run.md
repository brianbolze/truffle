# Retro — offerings module, Hone Health run (2026-06-03)

One of the first real `offerings.md` runs after the module shipped — a deliberately *comprehensive* pass on a
broad catalog ([`store/honehealth-com/offerings.md`](../../../store/honehealth-com/offerings.md): 12 condition
lines, 39 unique Rx SKUs, ~19 credits, lint-clean). The artifact landed cleanly; this captures what generalizes
to the next run, not Hone trivia.

## What worked — keep doing

1. **The category page *is* the roster; PDPs are near-identical boilerplate.** Every Hone PDP was the same
   rigid template — only **H1, price line, and three icon-badges** differ per SKU; the other ~14 sections
   (stat band, Q&A, cart, testimonials, FAQ) are byte-identical. So the category-card grid (name + slug + floor
   price + description) carried the *entire* roster, and per-PDP scrapes were needed only for the two earned
   deep-dives. **Generalizable:** on templated DTC catalogs, enumerate off the index pages and resist scraping
   every PDP — the recipe's "deepen only flagships" dial is correct, and it's what kept a 39-SKU pass at ~19cr
   instead of 50+. Read a PDP's top six lines and stop.

2. **The plain census map was the best completeness tool.** `fc.py map` with *no* search enumerated 53 product
   URLs and caught longevity SKUs (`/longevity/b12`, `/omega-3-prescription`, `/low-dose-naltrexone`) that the
   category-card grep missed. **Generalizable:** for a "complete SKU list" ask, run the no-search census as
   insurance *and* cross-check it against the card roster — neither alone is exhaustive, together they close.

3. **Page-attested molecule discipline produced visibly different, defensible calls.** Hone's TRT H1 literally
   reads "Testosterone Cypionate Injections" → recorded **cypionate**. Maximus's injectable hid "cypionate" in
   image alt-text only → recorded **not stated**. Same molecule, opposite call, *because the evidence differed*.
   The cream/troches (PDPs uncaptured) stayed "ester not stated." **Generalizable:** the rule isn't pedantry —
   it makes the roster's confidence legible, and the grep-the-price lint makes a fabricated number unable to pass.

## Frictions + fixes

4. **`fc.py map --search "site:domain/path"` is broken.** The `/` in the search term lands in the payload
   filename (`map_site:honehealth.com/mens.json`) → `FileNotFoundError` *after* the API already billed. I lost
   ~2 credits to it. **Fix:** sanitize the manifest/file tag in [`fc.py`](../../../skills/research-company/scripts/fc.py)
   `do_map` (slugify `search` — replace `/` and `:`). Low effort, removes a silent credit leak. Until then, the
   no-search census (#2) is the reliable path and the `site:` search is skippable.

5. **"Warm profile ≠ warm offerings."** Hone had a 3-day-old `profile.md` but **zero PDP/SKU captures** — the
   module needed a full fresh capture pass regardless. **Generalizable:** the module owns its own `captured_at`
   *and* its own (deeper, per-SKU) capture set; a fresh profile doesn't discount an offerings run. Worth a line
   in the recipe so future runs don't assume the profile capture covers it.

6. **The visibility token needs a per-brand *stated* rule — it's a judgment, not a mechanism.** I split
   `partial` ("From $X" floor, dose/tier-set later) vs `published` (flat "$X" shown), under a universal
   mandatory-membership stack. This **diverges from the Hims seed**, which marks any med-price-plus-mandatory-
   membership as `partial`. Both are defensible; the divergence is real. **Generalizable:** the closed set is
   principled but its *application* is brand-shaped — document the rule inline (overview + a verbatim anchor) so
   it's auditable and one-edit-overrulable. Consider a note in [`OFFERINGS.md`](../../../OFFERINGS.md) that the
   per-SKU visibility call is an explicit, stated judgment, and that cross-brand consistency is a *query-time*
   concern, not something to force at capture.

## Structural gotchas (small, but they bite)

- **One roster table, family rows inline.** The linter's `parse_roster` collects every `|…|` row between
  `## Roster` and the next `##`; a second sub-table's header row becomes a junk data row and trips the
  visibility check. For a large roster, use **one continuous table** with `family` rows as section breaks
  (the Hims/Maximus pattern), never H3-split sub-tables.
- **Count distinct slugs, not pages.** Hone's symmetric men/women catalog reuses one unisex slug for both sexes
  (longevity, thyroid, hair-loss, 4 weight-loss adjuncts): 53 URLs → 39 SKUs. List shared SKUs **once** with a
  "unisex/shared" note, or the roster inflates.

## Meta

The module held up well on its first comprehensive stress-test: the recipe's depth dial, the grep-verifiable-
price lint, and the page-attested-molecule rule all earned their place. The only true defect is the fc.py
`site:`-search filename bug (#4); everything else is a *documentation* nudge (#5, #6) rather than a design miss.

---

*Status (2026-06-03): **logged, not yet applied.** Action items: (#4) fix `fc.py` `do_map` tag sanitization;
(#5) add "warm profile ≠ warm offerings" to [`firecrawl-capture.md` §1.1](../../../skills/research-company/firecrawl-capture.md);
(#6) note in [`OFFERINGS.md`](../../../OFFERINGS.md) that per-SKU visibility is a stated judgment. Seed exemplars:
[`hims-com`](../../../store/hims-com/offerings.md), this run.*
