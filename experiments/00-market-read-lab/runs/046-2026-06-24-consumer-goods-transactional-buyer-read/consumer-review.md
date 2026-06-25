# Consumer Review

Question: **Where did Truffle create reader value, and where did it fall short?**

## Verdict

- **Valuable? Partly — leaning yes.** A shopper comparing these four brands gets a real,
  cited price-and-revenue-shape answer with per-SKU prices; they do *not* get a
  structured non-price comparison (returns/warranty/channel) and must read prose.
- **Why:** The read is honest about a split — the price layer is decision-grade and
  reusable, the purchase-protection layer is prose-only and uneven. It resists the easy
  over-claim ("the frame handles transactional retail") by isolating exactly which buyer
  needs the spine carries and which it doesn't.
- **Where Truffle added value:** per-SKU `[published]` prices already captured (no
  re-browsing), a clean `business_model` cut that separates these from subscription/hybrid
  peers, and the price-visibility token correctly flagging each brand's `[on-request]`
  services leg. A buyer gets a warm, cited price table for free.
- **Where Truffle added little or fell short:** the non-price retail decision (returns,
  warranty, shipping threshold, FSA/HSA, channel) — the things a catalog shopper *actually*
  agonizes over once price is known — exists only as prose across four documents, several
  cells "not quoted." No structured handle, so no diff.
- **What the consumer can do now:** build a price/breadth shortlist immediately; assemble a
  purchase-protection comparison only by hand, accepting holes.
- **What made it safer / better than generic Claude + web search:** the prices are
  captured-and-dated (verbatim per SKU), not hallucinated or pulled from a stale listicle;
  the sale-snapshot caveat is explicit. Generic search would miss that Therabody/Hyperice
  prices were a Prime Day capture.
- **Biggest limit:** n=4, all price-publishers — can't see the gated/quote-only
  physical-product case; and Nike's breadth is understated by recovery-line-only
  enumeration.
- **Human follow-up needed:** a buyer wanting current (post-sale) prices must re-check;
  Nike full-catalog breadth needs a wider capture.

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Clear answer / decision aid. | Yes for price/revenue shape; partial for the full buyer decision (Gap Map). |
| **Judgment-ready** | Cited ingredients to reason from. | Per-SKU prices + business_model are clean ingredients (C1, C2). Non-price factors are prose, harder to consume programmatically (W1). |
| **Sourced & cited** | Traces to dated captures. | Every claim cites a store path + `captured_at`; sale-snapshot flagged (C6). |
| **Deep enough** | Covers the set, not examples. | Covers all 4 named seeds; honest that the wider Transactional pool is out of scope and Nike breadth is partial. |
| **Fresh enough** | Stale assumptions visible. | Therabody/Hyperice prices flagged as Prime Day snapshot; Warby capture is 2026-06-04 (older). |
| **Kept / reusable** | Warm files for next ask. | offerings.md rosters already warm — a re-ask is cheap for price; not for warranty/returns. |
| **Shortfall mapped** | Names what it can't support. | Gap Map + Source Gaps name the unfielded retail factors and the uneven enumeration precisely. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Compare a whole field** | Partial — price/revenue/breadth comparable; purchase-protection not. | A structured retail-factor block would close it; too thin to mandate at n=4. |
| **Five-second brief input** | Yes for "what they sell + how priced + one-time-buy." | Returns/warranty/channel need prose-reading, not 5-second-glanceable. |
| **Build on top without re-capturing** | Yes for prices (warm offerings rosters). | Non-price factors aren't queryable; a downstream agent would re-parse prose. |

## Lens check

- **Strategist:** lands fast on the price/revenue story; the genuinely useful insight is
  the *inversion* — the frame's strain is on non-price factors, not on price as expected.
- **The Pantry / downstream system:** prices + business_model are usable ingredients;
  warranty/returns/channel are not (prose-locked) — an agent would have to re-extract.
- **First Contact:** would trust it — claims are cited to store files with clocks, and the
  read says "not found," not "not there," on every absence.

## Raw learning to preserve

Observations W1, G1, S1, G2 are in `run-notes.md`. The consumer lens reinforces **W1** (the
prose-only non-price factors are exactly the buyer-value gap) and **S1** (the price layer
is the value Truffle genuinely adds over generic search). No new consumer-side sighting
beyond those four.

**No lessons proposed, nothing graduated, no system change implemented.**
