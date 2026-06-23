# Evidence family analysis

## Most reliable

- **Render / capture integrity:** Repeated privacy overlays, cookie banners, blank media blocks, clipped marquees, low-contrast sections, and placeholder-looking blocks were concrete and useful. These directly corrected Geviti and Pepti from `excellent` to `strong`, and kept Hallandale capped.
- **Media asset sophistication:** Commissioned-feeling imagery, product/app screenshots, clinician/team imagery, and polished product renders helped separate Function/Ro/Nurx/Hallandale from generic/template surfaces. Generic stock and placeholder-looking assets were especially useful downgrade cues for Belmar, Amble, Geviti, and Pepti.
- **Cross-page consistency:** Key-page screenshots helped distinguish real systems from homepage-only polish. Function, Ro, Nurx, Hallandale, and Geviti stayed coherent across pages; Pepti's secondary pages were much thinner; Belmar stayed coherent but template-like.
- **Design-system consistency:** Typography, card/CTA discipline, spacing rhythm, and repeated component quality were useful, especially when paired with cap rules.
- **Information architecture / visitor clarity:** Useful for avoiding false negatives. Even lower-rated sites often had clear IA, so this should support "not broken/basic" reads, not automatically raise to `strong`.

## Weak or secondary proxies

- **Tech stack / framework:** Mostly secondary. Webflow, WordPress, Next.js, and custom React/Vite all appeared across different quality buckets. Next.js did not make Pepti or Geviti excellent; WordPress covered both Nurx/Hallandale and lower-rated Belmar; Webflow covered Function and noisy Amble hints.
- **Metadata maturity:** Weak correlation. Function/Ro/Nurx/Geviti/Pepti had mature metadata, but Hallandale rated 8 despite missing homepage description/OG image, while Belmar had adequate titles/descriptions and still rated 4. Metadata is useful for web-operation maturity, not visual polish.
- **Route/page-structure maturity:** Useful context, but a weak rating proxy alone. Belmar had coherent patient/clinician/order routes but lower presentation quality. Amble had clear treatment/PDP routes but remained over-rated in blind scoring.
- **Trust-surface presence:** Needs caution. Credentials, badges, testimonials, and footer density can make a site feel credible without making the presentation polished. This was the Belmar failure mode in both runs.

## Correlations observed

- Professional media assets correlated better with Brian's ratings than framework hints.
- Metadata maturity did not reliably correlate with Brian's ratings.
- Cross-page consistency was more reliable than homepage distinctiveness.
- Render defects and unfinished-looking sections were the strongest `excellent` cap triggers.

## Calibration read

The v2 checklist made evaluators more disciplined about `excellent`; no company except Function received it. That is the important improvement.

The remaining problem is the `strong`/`solid` boundary. Evaluators still over-reward sites that are coherent and visually ambitious, even when Brian's calibration treats generic stock, repeated panels, visible overlays, or unfinished-looking sections as a bigger penalty.
