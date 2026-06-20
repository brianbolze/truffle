# Receipt - Store owned-page trust State (panel brands)

What the store already holds on the panel brands' owned-page trust devices and billing posture — the "what the brand says about itself" side of the trust gap.

```yaml
receipt_type:          store-query
created:               2026-06-19
evidence_mode:         bounded-live   # run is bounded-live; this receipt is the local-store half
source_grade:          derived        # extracted from captured profile.md State
source_family:         local-store
spend_note:            none
snippet_only:          no
claim_ids_supported: [C5]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S5 | store/hims-com/profile.md (Credibility & proof) | captured 2026 | store file | derived | none | no | C5 |
| S6 | store/remedymeds-com/profile.md (Credibility; revenue model line) | captured 2026 | store file | derived | none | no | C5 |
| S7 | store/henrymeds-com/profile.md (Credibility; Trustpilot widget; revenue model) | captured 2026-06-04 | store file | derived | none | no | C5 |

## Method

`grep`/`sed` over the panel brands' captured `profile.md` Credibility blocks and revenue-model
lines. No live fetch of owned pages was needed — the captured State already holds the trust
devices and the billing structure the reviews object to.

## Evidence

**Owned-page trust devices the store captures (the "credibility" surface):**
- hims: LegitScript-certified seal; "Verified review" testimonials; named clinical bench (Dr. Craig Primack et al.); public-company status; "2.4M+ subscribers"; heavy regulatory disclaiming.
- remedymeds: "Forbes Best of 2026" badge; "Trustpilot Excellent 4.7" *badge image* (self-reported); LegitScript seal #145059; "365-Day Money-Back Guarantee / Weight Loss Warranty"; named care team; "every batch passes four independent tests."
- henrymeds: "Trustpilot TrustScore 4.4 · 12,482 reviews" *self-reported widget*; flat-monthly bundle framing; "no long-term contracts."

**Billing structure the store captures (the surface the reviews object to):**
- remedymeds: "flat subscription auto-billed every 28 days, month-to-month, cancel anytime — **but no refund once a prescription has been written.**"
- henrymeds: "multi-month plans exist… early cancellation may owe the balance"; "no insurance accepted or billed."

**What the store does NOT capture:** the review *bodies* themselves. Trustpilot/badge *scores*
appear in Credibility blocks; the objection *content* (billing-after-cancel, CS ghosting,
dose-step price jumps) has no home in captured State.

## Limits

Derived from captured State; captures range to ~2026-06-04 and may lag the live site. Proves
what the store holds, not current owned-page copy. The gap claim (review bodies absent from
State) is an absence-in-this-store statement, not a claim that the content is unfindable.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C5 | Owned-page trust devices (seals, guarantees, named clinicians, scores) answer legitimacy/credibility, not the actual objection clusters (billing/cancellation, reachability), which the store cannot surface because it holds scores not bodies | S5,S6,S7 | derived from captured State; capture lag |
