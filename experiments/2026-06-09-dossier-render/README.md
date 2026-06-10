# dossier-render — one dossier → one self-contained HTML brief

**Hypothesis.** The store already captures each company's brand identity (logos, brand_colors, fonts)
and a rich, cited dossier body — so a single script can render `store/<slug>/` into a one-page,
AirDrop-able HTML brief that (a) dresses itself in the company's *own* identity, (b) renders the
trust surface (capture clocks, unverified fields, enumeration floors) visibly instead of hiding it,
and (c) degrades honestly on sparse profiles ("not captured", never broken layout).

**Method.** `render.py <company>…` — resolves via `scripts/store.py`, parses profile/offerings/
telehealth markdown, embeds fonts (Google Fonts fetch + cache, classified fallback stacks when a
face isn't embeddable), inlines logo assets + the captured homepage screenshot (`sips`-compressed),
and emits `_out/<slug>.html`. Layout: hero identity band + capture record, icon spec strip
(taxonomy → lucide icons, `icons.py`, fetched once via the shadcn registry), four tabs
(Profile / Offer / Brand system / Provenance) with collapsible sections; print flattens it all.
No server, no build step; the markdown stays the source of truth — the brief is a regenerable
lens, same philosophy as the SQLite lens.

Extraction (`extract_model`) is deliberately separate from rendering (`render_html`) so the
follow-up N-company compare sheet can reuse the model without touching the template.

**Run.**

```
python3 render.py honehealth.com rolex.com stripe.com blueowl.com
open "_out/honehealth-com.html"
```

Outputs land in `_out/` (gitignored). `--no-fetch` skips network (fonts/logos fall back).

**Read.** [`FINDINGS.md`](FINDINGS.md) — what worked, and the list of things the renderer *wanted*
that the store doesn't capture (feeds the compare-sheet design).
