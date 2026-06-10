# FINDINGS — dossier-render

**The bet holds.** One script renders any `store/<slug>/` into a self-contained brief dressed in
the company's own captured identity, with the trust surface (capture clocks, unverified fields,
enumeration floors, field notes) rendered as a first-class tab — not fine print. Rendered across
five deliberately contrasting companies: honehealth (rich telehealth, chartreuse/near-black,
offerings + cohort pack), rolex (2.2 luxury, no logos module, remote PNG wordmark), stripe (2.5
SaaS, dark-fill SVG wordmark), hims (warm palette, sparse-ish), blueowl (worst case: no fonts,
favicon-only logo, dark scheme) — degradation is honest ("not captured", typographic wordmark,
classified fallback type stacks), never broken layout.

**Structure (post-feedback v2):** hero identity band + capture record → icon spec strip
(taxonomy values → lucide icons via the shadcn registry, `icons.py`) → four tabs
(Profile / Offer architecture / Brand system / Provenance & limits) → collapsible sections with
one-line peeks. Print opens every disclosure and flattens tabs into labeled blocks.

## What the renderer wanted that the store doesn't capture

Feeds the compare-sheet design — each of these was worked around with a heuristic or omission:

1. **Wordmark ink/ground facts.** `logos.wordmark` records `w/h` but not what the mark needs to
   sit on. The renderer parses SVG fills and guesses (luminance < .55 → paper plate); for raster
   wordmarks it can't know and always plates. A measured `fill:` hex (or `ground: dark|light`)
   per slot would delete the guess. Hone's white-fill wordmark is exactly the case the comment
   in profile.md warns about — structured, it wasn't.
2. **Brand-color roles are ad-hoc.** Keys vary per profile (`primary/accent` vs
   `primary/text/background` vs `primary/dark/secondary`). The renderer derives "dark ground" /
   "usable accent" by luminance+saturation heuristics that mostly land on-brand but can't be
   guaranteed. A tiny stable role vocabulary in SCHEMA would make briefs exactly on-brand.
3. **Founded / HQ.** The hero wants "Founded 2021 · New York" chips; both live only in Overview
   prose. (JSON-LD often carries `foundingDate` — already mined for socials/aliases.)
4. **The company's own tagline, verbatim.** `description` is the engine's sentence (right for the
   hero), but a brand strategist wants the brand's own line ("Longevity engineered around your
   biology") — currently buried in prose. A one-line verbatim `tagline:` would be cheap.
5. **Structured proof numbers.** Trustpilot 4.8/11,526 lives in body prose; `external` holds only
   the URL. A compare sheet ranking trust signals needs the rating + count + as-of structured.
6. **Font roles are a convention, not a contract.** `fonts[0]`=display works for most profiles but
   nothing marks it; single-font and empty lists are common. Role tags (`display:`/`body:`) or
   keeping order-as-meaning documented in SCHEMA would firm up the type specimen.
7. **Screenshots are gitignored sidecars.** The homepage "field specimen" is the brief's best
   moment for this audience and exists only on machines that ran the capture. If briefs become a
   real consumer, a small committed hero crop earns its bytes.
8. **Price magnitude (known, by design).** The stat band can't say "from $15 to $165/mo" without
   violating the verbatim contract. Fine for one company; the compare sheet must compare
   *visibility* and quote verbatim strings, not sort magnitudes — same wall Recipe 4 documents.

## Renderer-side notes (for the compare sheet)

- `extract_model(query)` returns a plain dict (identity, palette decisions, fonts w/ embed status,
  logo kind+plate, sections, offerings groups, telehealth cuts, trust surface) — reuse it directly;
  `render_html()` is the only single-company-specific part.
- Roster parsing is **header-keyed** (eden-health's extra `Form`/`Category` columns survive).
- Google-Fonts embedding caches per family under `_out/.fontcache/` (incl. remembered misses);
  commercial faces (Söhne, Sofia Pro, Helvetica Now) fall back to classified system stacks and the
  type specimen says "substituted" out loud.
- Self-contained outputs run ~1–2.2 MB; the embedded screenshot dominates (sips-recompressed to
  1200w jpeg). Without it (fresh clone), briefs are ~300–600 KB.
