---
name: deepen-offerings
description: >
  Re-capture one company to make its offerings.md roster comprehensive — drive it to "complete at the
  indexed level" across ALL product lines, pulling in any line or subdomain a prior run left out of
  scope. Use when a roster looks incomplete: "deepen offerings for X", "enumerate more of X's catalog",
  "/deepen-offerings henrymeds", "make X's offerings comprehensive", "X's roster is missing SKUs". Takes
  any company form (slug / domain / name). A focused preset of research-company; it spends Firecrawl.
---

# /deepen-offerings — make a company's offerings roster comprehensive

A focused preset of [`/research-company`](../research-company/SKILL.md): re-capture a company with one goal —
drive its `offerings.md` to **complete at the indexed level across every product line**. It fixes a roster that
stopped early and now *reads* as a small catalog, so any count under-reports it. **Follow research-company's
`SKILL.md` + `firecrawl-capture.md` for all capture mechanics** (offerings ladder = §1.1; contract =
`OFFERINGS.md`) — this skill only presets the focus and the gap-targeting below.

## Steps

1. **Resolve → slug.** `python "$WEB_RESEARCH_HOME/scripts/store.py" find "$ARGUMENTS"` folds any form (domain /
   name / alias / slug) to the key. **NOT in store** → nothing to deepen; run `/research-company "$ARGUMENTS"`
   for a first capture instead, then stop.

2. **Find the gaps.** Read `store/<slug>/offerings.md` → `## Provenance` + `site_notes`, and chase only the
   **breadth** gaps: whole product lines, an off-host / sibling **subdomain** (a `shop.` storefront), categories
   priced but not rostered, anything "out of scope" last run. **Leave the by-design leaf omissions** (dose /
   quantity tiers, per-SKU PDP price depth, `Catalog` leaves) — chasing those just burns credits. No completeness
   note at all (common) → treat the whole roster as unverified and re-enumerate off the index pages.

3. **Re-capture for breadth.** Force a refresh (don't serve the warm dossier); drive `offerings.md` to complete
   at the indexed level across all lines + the step-2 gaps. Refresh the `## Provenance` scope note so the next
   run — and any consumer reading a count — sees how far this one got.

**Scope:** offerings only (a full refresh or first capture is `/research-company`); it spends Firecrawl, so
research-company's credit pre-flight applies.
