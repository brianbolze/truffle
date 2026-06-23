# V2 blind rating instructions

Working field:

```yaml
site_presentation_quality: excellent | strong | solid | basic | weak | broken | unknown
confidence: low | medium | high
key_evidence:
  - "<2-5 concrete observations from screenshots/artifacts>"
cap_rule_notes: "<why excellent is allowed or capped>"
```

Rate only observable marketing-site presentation quality:

- render integrity
- layout discipline
- typography hierarchy
- imagery/media quality
- iconography consistency
- brand-system coherence
- CTA/form/card/component polish
- visible copy polish
- navigation clarity
- information clarity
- trust-surface presentation

Do not score company legitimacy, competitive threat, funding, headcount, traffic, SEO, truth of claims, clinical quality, or market strength.

Scale:

- `excellent`: unusually high-quality, distinctive, polished marketing presentation.
- `strong`: clearly professional and well-executed.
- `solid`: competent, credible, no major presentation issues.
- `basic`: usable but generic, thin, dated, or lightly polished.
- `weak`: visibly amateur, inconsistent, sloppy, low-trust, or poorly maintained.
- `broken`: broken rendering, missing CSS/images, junk page, or unusable site presentation.
- `unknown`: artifacts are insufficient or capture quality prevents a fair read.

V2 excellent cap:

A site should only get `excellent` if it has both distinctiveness and execution discipline. Major placeholder blocks, low-contrast sections, broken media panels, repeated overlays, generic stock-template execution, or visibly unfinished sections should usually cap the rating at `strong`.

Evidence checklist:

- Render/capture integrity: broken media, blank panels, clipped text, sticky widgets, consent overlays, repeated overlays.
- Metadata maturity: specific titles/descriptions, OG title/description/image, canonical/source URL, favicon/logo hints.
- Tech stack/web-operation maturity: framework/CMS hints from cached raw HTML; treat as secondary, not a rating by itself.
- Route/page-structure maturity: coherent product/pricing/about/service URLs vs. generic campaign/content sprawl.
- Media asset sophistication: commissioned photography/video, product renders, app screenshots, team/clinician imagery, generic stock, icon-only/text-heavy, AI-ish or placeholder-looking assets.
- Design-system consistency: typography, spacing, color, cards/forms/CTAs, iconography, cross-page reuse.
- Information architecture and visitor clarity: what they sell, for whom, and what next action is.
- Cross-page consistency beyond homepage: whether key pages retain the same polish and visual system.

Blindness rule:

- Use only the v2 packet and referenced screenshot paths.
- Do not open `profile.md`.
- Do not use Notion, Brian's ratings, or existing `Visual & brand impression` prose.
