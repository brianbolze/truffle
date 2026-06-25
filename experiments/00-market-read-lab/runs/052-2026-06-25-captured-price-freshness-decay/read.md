# Market Read

## Question

For a small panel of store brands whose pricing was captured on the open marketing page
(Oura, Eight Sleep, Therabody, Hyperice, Peloton — several captured mid-promotion), does
the live marketing-page price still match the captured price, and what does the divergence
say about how fast captured pricing State rots?

## Result

**Gap-probe result: captured pricing State did not rot on its own over days-to-weeks —
it rotted exactly where a *dated promotion lapsed* between capture and re-check. Two
sub-findings, plus a tooling surprise.**

This was scoped as a freshness *floor* test, not a multi-week decay study, because the
store's panel captures turned out fresh: 4/5 panel brands were captured **2026-06-24**
(1 day before re-check) and only Peloton was captured **2026-06-10** (15 days). So the
read measures (a) "do even ~1-day-old promotional snapshots already diverge?" and (b)
one real 15-day data point — not a decay curve.

Re-checking 3 of the 5 (stop rule fired at 3 open-page-verifiable brands):

| Brand | Capture age | Captured headline | Live (2026-06-25) | Verdict |
|---|---|---|---|---|
| **Oura** | 1 day | Ring 4 "From $244" (flash sale); Ceramic "$279" | "From $244"; "$279"; flash sale **"through June 26th" still live** | **Match** — dated sale still inside its own window |
| **Eight Sleep** | 1 day † | Pod 5 Queen $2,749 (~~$2,999~~), "4th July Sale" | $2,749 / $2,999 / "4th July Sale" | **Match** † (cache caveat) |
| **Peloton** | 15 days | Refurb Original Bike **"from $695"** (~~$1,145~~), **"ends June 15, 2026"**; Cross-Train Bike+ $2,695; refurb Bike+ $1,395 | **No "$695"**; refurb Original Bike priced **$1,145** (Affirm footnote); Cross-Train Bike+ $2,695; refurb Bike+ $1,395 | **Partial divergence** — the dated promo expired; durable prices match |

**(1) Of the 3 re-checked brands, the only price that rotted was a promo with a printed
expiry that had passed.** (Therabody + Hyperice were not re-checked — stop rule at 3 — so
their Prime-Day prices are unverified, not "unchanged"; corrected per VR1.)
Peloton's refurb Original Bike was captured at a "$695, ends June 15, 2026" limited-time
promo on 06-10; re-checked on 06-25 (10 days after that printed expiry) the $695 is gone
and the price has reverted to **$1,145** — exactly the struck-through regular price the
capture already recorded. Everything *not* on a dated promo (Cross Training Bike+ MSRP
$2,695; refurb Bike+ $1,395; All-Access $49.99/mo from the capture) matched. (C3, C4)

**(2) Promotional captures did *not* spontaneously rot at 1-day age — and a dated sale
stayed valid inside its own stated window.** Oura's flash sale, captured 06-24 as running
"through June 26th," was still live and still priced "From $244"/"$279" on 06-25 (C1).
Eight Sleep's Pod 5 "4th July Sale" price matched (C2). So a captured promo price is not
self-evidently stale; its trustworthiness is bounded by the **promo's own printed end
date**, which the capture often records verbatim and which is the real freshness signal —
not the bare `captured_at`.

**(3) Tooling surprise: a "live re-check" silently returned a cached scrape.** The Eight
Sleep fetch came back as a Firecrawl **cache hit dated 2026-06-24** (same day as the
original store capture), not an independent 06-25 fetch. Oura was fetched fresh today and
Peloton was a fresh cache-miss, but the Eight Sleep "unchanged" cell is trivially same-day.
A freshness-verification routine that doesn't bust the fetch cache can silently re-confirm
stale data as "still current." (See G2.)

## Gap Map

- **Answered cleanly (live-verified):** Whether 3 panel brands' captured headline prices
  still match live, and the mechanism of the one divergence (expired dated promo, not
  drift). The capture's verbatim promo-window text ("ends June 15, 2026"; "through June
  26th") was the load-bearing freshness signal in every case.
- **Where Truffle fell short (the structural gap, restated empirically):** The store has
  **no structured expiry/promo-window field**. The single fact that predicted decay —
  "this price is a dated promo that ends on DATE" — lives only in `offerings.md` prose /
  `site_notes` ("ends June 15, 2026", "Flash Sale through June 26th", "4th July Sale"),
  never in frontmatter or a price cell. So a reader (or a staleness monitor) cannot
  *query* "which captured prices have a promo window that has already lapsed" — the exact
  query that would have flagged Peloton's $695 as expired without any live fetch. This is
  the 041/048 "no change-detection home" gap, now localized to a fillable, dated, mostly-
  already-captured datum: the promo end date. (G1)
- **What would change the answer:** A panel with more mid-age captures (the store was too
  freshly captured to show multi-week organic drift); or a brand that changed an
  *evergreen* (non-promo) price, which none of the three did.

## Evidence Used

Lines up with `run-notes.md` `live_evidence_used` and receipt `C1-live-price-recheck.md`.

- **C1** — Oura captured vs live (match; dated flash sale still live). S1 `ouraring.com`
  (fresh 06-25) + L1 `store/ouraring-com/offerings.md` (06-24).
- **C2** — Eight Sleep captured vs live (match; cache-hit caveat). S2
  `eightsleep.com/product/pod-cover` (cache 06-24) + L2 `store/eightsleep-com/offerings.md`.
- **C3** — Peloton refurb Original Bike $695 promo expired → live $1,145. S3
  `onepeloton.com/exercise-bikes` (fresh 06-25) + L3 `store/onepeloton-com/offerings.md`
  (06-10).
- **C4** — Peloton durable MSRPs match live. S3 + L3.

Source-grade: all three live pages are vendor first-party (primary), plain-markdown,
not snippets. Spend: 3 paid credits (ceiling 8); 3 outside sources (ceiling 5); 1 source
family (vendor pages). No PDF/JSON-extraction, no funnel/login.

## Companies Seen

Panel (store): ouraring-com, eightsleep-com, therabody-com, hyperice-com, onepeloton-com.
Re-checked live: ouraring, eightsleep, onepeloton. **Not re-checked** (stop rule at 3):
therabody, hyperice — both captured 06-24 mid-"Prime Day"; their sale-persistence is
unverified, recorded as a coverage limit, not a finding.

## Missing / Stale Coverage

- **Peloton refurb Original Bike $695** is now a **stale captured price** (promo expired
  06-15; capture 06-10 predates expiry). The capture is honest — it recorded the expiry
  date and the struck regular price — but a reader trusting the headline "$695" without
  reading the promo-window note would be wrong by ~$450 today.
- The store's freshest panel captures (06-24) are too recent to test organic, non-promo
  price drift; that question is unanswered, not answered negatively.

## Source Gaps

None beyond plan. The vendor-marketing source family was sufficient and cheap (1 credit/
page, plain markdown). The only friction was within the source tool: cache behavior (G2).

## Raw Learning to Preserve

For Loop 2 to append to `learning/observations.md`:

- **G1** (gap) — decay concentrated at expired dated promos; the predictive datum (promo
  end date) is captured-in-prose but unstructured/unqueryable. Empirical instance of the
  041/048 no-change-detection gap.
- **S1** (surprise) — captured promo prices did not spontaneously rot at 1-day age; a
  dated sale stayed valid inside its own printed window. Freshness is bounded by the
  promo's own end date, not bare `captured_at`.
- **S2** (surprise) — the one diverging price was *already self-flagged* in the capture
  (struck regular price $1,145 + verbatim expiry), so the store had everything needed to
  predict the rot **without** a live fetch.
- **G2** (gap / tooling) — a "live re-check" via Firecrawl silently returned a cached
  06-24 scrape for Eight Sleep; freshness verification needs explicit cache-busting or it
  can re-confirm stale data as current.
- **S3** (surprise) — a stale Affirm footnote ($1,995 basis for refurb Bike+ vs displayed
  $1,395) persisted from the 06-10 capture to the live 06-25 page — a vendor-side internal
  inconsistency that is itself durable, captured honestly in 06-10 `unverified_fields`.

## External Completeness Check

Not load-bearing here — the denominator is a hand-picked 5-brand panel, explicitly
partial; no completeness claim is made about "all store brands with open prices."

## Market Pattern

Across connected-hardware DTC, headline prices are **promotion-dominated** (flash sales,
"4th July", "Prime Day", limited-time refurb) rather than evergreen. That makes captured
pricing State decay-prone **but predictably so**: the decay event is the promo's printed
end date, which the capture tends to record verbatim. The durable layer (MSRP, membership
$/mo, struck regular price) is stable across days-to-weeks. So "is this captured price
still good?" reduces to "is there a promo window on it, and has it passed?" — a question
the store can almost answer from existing prose but cannot answer from a query.

## What Would Change This Answer

- A second mid-age (2–4 week) capture cohort showing organic non-promo price drift would
  move this from "only dated promos rot" toward "evergreen prices drift too."
- If a captured *evergreen* price (not promo) had diverged at 15 days, the gap would point
  at a general re-capture cadence rather than a promo-expiry flag.
- A larger panel where promo-window text was *absent* from captures (so expiry couldn't be
  predicted from prose) would strengthen the case for a structured field over a reading
  convention. Here, prose carried the expiry every time — so "no new primitive needed"
  stays live; the lightest path is a reading/monitor convention keyed on already-captured
  promo-window text, not a new schema field.
