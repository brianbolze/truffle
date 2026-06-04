# Retro — offerings module, Warby Parker run (2026-06-04)

First **finite-physical-catalog** run — real PDPs, published per-SKU prices ($95/$145), `Catalog` shape → shape +
exemplars ([`store/warbyparker-com/offerings.md`](../../../store/warbyparker-com/offerings.md), lint-clean). The cleanest
spine fit of the non-telehealth runs so far.

- **Spine held *semantically*, not just structurally — the first non-Rx run where it did.** `Slug` = real attested PDP
  URLs (`/eyeglasses/durand/whiskey-tortoise`), not `(no PDP — …)` fictions; `Price (verbatim)` = real greppable
  **$95/$145**; `Visibility` = clean `published`/`on-request` with **no `partial` fudge** (a flat frame price genuinely
  *is* the all-in — insurance only lowers it). `Kind` family/buyable held honestly — everything rostered is actually
  purchasable. **The one stretch:** I rostered **price *tiers* as rows** ("$95 frames", "Premium frames") whose identity
  *is* their price, slugged to a filter view (`/eyeglasses?prices=95`) — true for a flat-priced catalog, but a
  row-as-price-band the contract doesn't anticipate.
- **Added nothing to the spine — right call** (vs Notion's `Category`). Families carried the grouping; no extra column
  earned. One improvised convention: an **`*(exemplar)*` marker** on rows that are representative samples, not complete
  lines — Catalog-specific, worth blessing so a reader doesn't read the roster as exhaustive. Reframed `What` (freeform
  descriptor) was already sanctioned, not an addition.
- **OFFERINGS.md silent spot — the roster contradicts itself for Catalog.** `## Roster` says "one row per offering,
  **complete at the indexed level**"; the capture/depth dial says "`Catalog` → **shape + exemplars only, never the
  SKUs**." The two halves disagree and the doc never reconciles them — I decided exemplars-in-the-roster *is* "complete"
  by redefining the indexed level as **line + tier + flagship**. (airbnb's retro flagged Catalog needs a note re:
  overview-as-main-content + `Kind`/`Slug`; this is the distinct, still-unflagged gap — the **completeness rule itself**.)
- **One change:** fold into airbnb's proposed `Catalog` note a single reconciling line — *for `portfolio_shape: Catalog`
  the roster is **intentionally non-exhaustive**: line + pricing-tier + marked flagship exemplars, and that satisfies the
  contract.* One sentence kills both the "complete vs exemplars-only" contradiction and the exemplar-marker guess —
  cheaper than any column or value change.
- **`molecule · form · access` did NOT become `spec · variant · availability` — and didn't need to.** I dropped the
  structured lead for prose. A physical catalog *could* carry spec·variant·availability (frame material/shape ·
  color/width · in-stock), but at the **exemplar grain** that detail already lives in the per-frame name + `What`;
  structuring it would be ceremony. (A small, enumerable **`Multi-product`** physical catalog is where that triple would
  earn its place — untested here.) **Deep-block quota did *not* creep back:** one block earned (the "$95 bundle" — a real
  ambiguity the `published` token can't carry), per-SKU dives explicitly declined, and the **3 hero renders rode as asset
  refs inside that one block**, not as a block-per-flagship. The pilot-triage lesson held.

**Verdict:** fit — **~90%, the truest spine fit of the non-Rx runs**; the only strain is a *doc* contradiction (roster
"complete" vs Catalog "exemplars"), not a spine failure. Didn't force it.

---

*Status (2026-06-04): **logged, not yet applied.** This run + airbnb are now **two `Catalog` seeds** — enough to
actually write the `Catalog`-shape note in [`OFFERINGS.md`](../../../OFFERINGS.md) instead of deferring: it should
(a) reconcile roster-"complete" with Catalog-"exemplars-only" (this run), (b) bless overview-as-main-content + family/leaf
`Kind` + non-URL `(no PDP — <id>)` keys (airbnb), and (c) sanction the `*(exemplar)*` marker. One paragraph, both seeds
cited.*
</content>
