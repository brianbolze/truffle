# V3 blind rating instructions

You are rating ONE company's observable marketing-site presentation quality from cached capture artifacts only.

Output field:

```yaml
site_presentation_quality: excellent | strong | solid | basic | weak | broken | unknown
confidence: low | medium | high
key_evidence:
  - "<2-6 concrete observations from screenshots/artifacts>"
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

Do not score company legitimacy, competitive threat, funding, headcount, traffic, SEO, truth of claims, clinical quality, or market strength. A dated site is not evidence of a fake business, and trust badges are not evidence of polish.

Scale:

- `excellent`: unusually high-quality, distinctive, polished marketing presentation.
- `strong`: clearly professional and well-executed.
- `solid`: competent, credible, no major presentation issues.
- `basic`: usable but generic, thin, dated, or lightly polished.
- `weak`: visibly amateur, inconsistent, sloppy, low-trust, or poorly maintained.
- `broken`: broken rendering, missing CSS/images, junk page, or unusable site presentation.
- `unknown`: artifacts are insufficient or capture quality prevents a fair read.

Excellent cap (from v2):

A site should only get `excellent` if it has both distinctiveness and execution discipline. Major placeholder blocks, low-contrast sections, broken media panels, repeated overlays, generic stock-template execution, or visibly unfinished sections should usually cap the rating at `strong`.

Known calibration traps (from v1/v2 misses — apply them):

- Coherent-but-generic execution is `solid` at most, and generic stock-template execution, dated components, or cluttered trust badges read `basic` — coherent structure plus credentials does not make a site `strong`.
- Distinctive art direction without execution discipline is not `excellent`.
- Clear information architecture prevents `weak`/`broken`; it does not by itself raise a site to `strong`.
- Tech stack, metadata maturity, and route structure are NOT rating inputs.

Evidence to weigh (reliable families first):

- Render/capture integrity: broken media, blank panels, clipped text, sticky widgets, consent overlays.
- Media asset sophistication: commissioned photography/video, product renders, app screenshots vs. generic stock, icon-only/text-heavy, AI-ish or placeholder-looking assets.
- Cross-page consistency: whether key pages retain the homepage's polish and visual system.
- Design-system consistency: typography, spacing, color, cards/forms/CTAs, iconography reuse.
- Information architecture and visitor clarity: what they sell, for whom, what next action is (false-negative guard only).

Method (v3 — raw artifacts, no packets):

1. List the company's capture directory: `store/<slug>/captures/<date>/`.
2. Read EVERY screenshot under `.payloads/*.png` (skip `_archive/`). Screenshots are the primary surface.
3. You may also read the captured page `.md` files in the same capture dir for copy/IA clarity.
4. Rate using the scale above, citing concrete evidence.

Blindness rules (hard):

- Do NOT open `store/<slug>/profile.md` or any other file in the store root for this or any company.
- Do NOT open anything under `experiments/` except this instructions file.
- Do NOT use the web, Notion, Firecrawl, or any external tool.
- Do NOT use prior knowledge of the company; rate only what the artifacts show.
