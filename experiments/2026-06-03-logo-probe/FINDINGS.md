# Probe 1 — logomark resolution audit

**Question:** does a reliable ≥128px "deck-quality" square logomark exist for the D2C telehealth
competitor set, and which source wins — Google `s2/favicons?sz=256` or `apple-touch-icon`?

**Run:** `python3 probe.py` (2026-06-03). 16 competitors. Icon `<link>`s parsed offline from
cached `.payloads` rawHtml; image bytes fetched live; actual px via macOS `sips`. Raw → `results.json`.

## Verdict

**13/16 (81%) clear the 128px bar — but only if you measure actual pixels and take the larger of
{google-s2-256, apple-touch-icon}. Neither source alone is enough** (google 12/16, apple 10/16;
union 13/16), and **`sz=256` is a request, not a promise** — Google silently returned 32px for
ro.co, gogeviti, marekhealth despite asking for 256. Brian's "check the *actual* resolution" was load-bearing.

| competitor | google256 | appleTouch | today (logo_url) | winner | px | ≥128 |
|---|---|---|---|---|---|---|
| hims | 180 | — | fail | google | 180 | ✅ |
| ro.co | **32** | 144 | fail | apple | 144 | ✅ |
| lifemd | 180 | 180 | 32 | google | 180 | ✅ |
| maximustribe | 256 | **512** | 32 | apple | 512 | ✅ |
| honehealth | 256 | 300 | 660×485 | apple | 300 | ✅ |
| getpetermd | 256* | — | fail | google | 256* | ✅ |
| remedymeds | 256* | — | fail | google | 256* | ✅ |
| joiandblokes | 192 | 192 | fail | google | 192 | ✅ |
| agelessrx | 100 | 100 | fail | — | 100 | ❌ |
| gogeviti | **32** | 32 | fail | — | 32 | ❌ |
| mylifeforce | 180 | 180 | 32 | google | 180 | ✅ |
| gethealthspan | 256 | 180 | (empty) | google | 256 | ✅ |
| marekhealth | **32** | 32 | 294×44 (wordmark) | — | 32 | ❌ |
| functionhealth | 256 | 256 | 32 | google | 256 | ✅ |
| eden.health | 256 | 256 | 32 | google | 256 | ✅ |
| onemedical | 152 | 192 | 16 | apple | 192 | ✅ |

\* google returned 256 but no apple-touch to cross-check → size is real but **crispness unverified**
(could be an upscale). The slide test (Probe 3) is the crispness check, not pixel count.

## Reads

- **Source chain locked:** logomark = `max(actual_px of {apple-touch-icon, google-s2-256})`, both
  measured, never trusting the requested size. The two are complementary — apple-touch rescues
  ro.co/onemedical (google too small); google rescues hims/getpetermd/remedymeds (no apple-touch present).
- **Big upgrade over today.** Current `logo_url` is favicon-grade for nearly all (16–32px or unmeasurable
  `.ico`); maximus 32→512, onemedical 16→192, gethealthspan empty→256, function/eden 32→256.
- **3 real misses — no hi-res *square* mark anywhere:** agelessrx (100px ceiling), gogeviti (32px only),
  marekhealth (32px — but it's **wordmark-first**: ships a 294×44 wordmark). For these the consumer should
  fall back to the wordmark. So the logomark slot is "empty/low-res ~19% of the time," and that's fine if
  wordmark covers it.

## Implication for the schema (logomark)

- Logomark is reliably solvable, deterministic, no vision. Worth the slot.
- Don't store the requested size — store the **measured** px so the consumer can reject low-res.

---

# Probe 2 — wordmark fill

**Question:** for each competitor, is the wordmark a **hostable URL** we can store, or only an
**inline `<svg>`/data-URI** (→ asset extraction, Tier 2)? And do the 3 logomark-misses have one?

**Method correction (kept as the lesson):** v1 scanned only `<head>` (SPA bodies missed). v2 scanned
the whole doc and "picked widest image" — and **grabbed press/endorser/payment logos**: hims→a
`zdassets.com` Zendesk asset, agelessrx→`newyorktimes-logo.png`, function→`Time100.webp`, eden→
`afterpay.png`, onemedical→`logo-airbnb.jpg`, marek→`mark-manson-logo.webp`. v2's "12/16 hostable"
was inflated noise. **A naive image scan cannot distinguish a brand wordmark from a logo wall.**
v3 trusts only the pre-vetted `logo_url` (real on-domain mark, not favicon) + *on-domain* JSON-LD.

## Verdict

**7/16 have a hostable wordmark URL; 9/16 ship it as inline `<svg>` (8) or client-rendered (1) → no
URL → needs asset extraction or a screenshot-crop.** For this design-forward DTC cohort, ~56% of
wordmarks are un-hostable — the data-URI/inline gap is real and is a slim *majority*, not an edge case.

| hostable wordmark url (7) | needs extraction (9) |
|---|---|
| lifemd, getpetermd, remedymeds, joiandblokes, agelessrx, gogeviti, marek | hims, ro, maximus, honehealth, mylifeforce, gethealthspan, functionhealth, eden, onemedical |

## The payoff: complementary coverage = 16/16

The two slots cover each other's gaps **perfectly**:
- All **3 logomark-misses** (agelessrx, gogeviti, marek) have a **hostable wordmark**. ✅
- All **9 wordmark-extract** brands have a **≥128px logomark** (hims 180, maximus 512, function 256, eden 256…). ✅

So **every competitor has ≥1 deck-quality asset with zero manual work.** What's *not* free is getting
*both* ratios for the 9 inline-SVG brands — the second ratio needs extraction.

## Implication for the schema (wordmark)

- **logomark** = deterministic, build it (Probe 1).
- **wordmark** = hostable URL for ~44%; the rest need **vision/agent-in-the-loop**, NOT a scrape —
  the contamination proves automated selection is unsafe. Cheapest universal path: crop the header
  from the full-page screenshot the capture already has (raster, deck-fine). Crisp path: extract the
  inline-SVG markup (infinite res) — but only the agent can pick the *right* svg.
- **og** = free (`metadata.ogImage`, present on every payload) → Notion cover. Not re-probed; trivial.

---

# Probe 3 — pixel acceptance test (Claude workflow, 16 brands)

**Method:** a fan-out-and-synthesize workflow — 16 Sonnet agents (one per competitor) each
materialized all three ratios as PNGs and judged them by *looking* (vision), against a skeptical
deck-quality rubric; one Opus synthesizer did an independent leniency check, aggregated, and built a
contact sheet. Assets + `contact-sheet.html` in `_out/` (gitignored). 17 agents, ~974k tokens, ~12.5 min.

## Verdict: GO. Per-slot deck-ready = logomark 13/16 · wordmark 16/16 · og 11/16 · union 16/16.

Every brand is deck-renderable because **wordmark is the near-guaranteed slot (16/16)** that backstops
the three logomark resolution-fails (agelessrx 100px, gogeviti 32px, marek 32px — all carry a clean
hostable wordmark). The independent pass flipped **zero** builder verdicts (1 calibration override on
agelessrx: low-res, not "blurry") — self-bias produced no false passes worth catching.

## What the measurements couldn't tell us, now answered

- **Google S2 `sz=256` returns the TRUE native size — never a fake upscale** (independently re-measured:
  getpetermd/gethealthspan/function/eden = real 256² & crisp; gogeviti/marek = real 32² & small).
  So **reading actual pixels is a sufficient quality gate.** A `>=128px native` bar auto-fails all 3 small marks.
- **Wordmark extraction works for all 16** — svg-extract 8, hostable 6, screenshot-crop 1, og-crop 1.
  The "hard slot" is solvable, but only with the **capture agent's eyes** (extract the right inline-SVG /
  crop the header) — never a blind scrape (Probe 2's press-logo contamination proved that).

## Three auto-gates the run surfaced (would flag 6 of 7 fails before a human looks)

1. **logomark:** keep only if native short-side `>=128px` (measure the bytes, not the URL's `sz=`).
2. **baked-background flag:** `hasAlpha` is NOT a transparency test — 5 marks report alpha-yes yet carry an
   opaque color box (checkerboard tile exposed them). ~7/16 marks have one → fine on light slides, a colored
   square on dark. Derive `safe_on_dark` by sampling corner pixels, not the alpha channel.
3. **og:** require a *declared* `og:image` verified at `>=600px actual width` — the declared meta size LIES
   (marek declares 600×315, serves 30×34; getpetermd's "og" is just a Firecrawl homepage screenshot).

## Caveats to carry as data, not bury

onemedical's wordmark is the post-acquisition **"amazon one medical" co-brand**; hone's wordmark is
white-on-baked-dark (unusable on a dark slide); eden's og is the weakest pass (500×263, no logotype).

## Net (3-probe arc)

The BACKLOG idea is **de-risked → GO**, reshaped: not three equal slots but a **tiered set** —
**wordmark = primary/reliable**, **logomark = best-effort + `>=128px` & baked-bg gates**, **og =
best-effort gated on a real `>=600px` og:image**. Logos are pure State; wordmark needs vision-in-the-loop
(fits "AI at ingestion"). Next: the dedicated schema-design session (additive `logos:{}` MINOR; assets to
a gitignored sidecar like screenshots; `logo_url` stays canonical).
