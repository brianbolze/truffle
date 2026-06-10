# Blind rating instructions

Working field:

```yaml
site_presentation_quality: excellent | strong | solid | basic | weak | broken | unknown
confidence: low | medium | high
evidence:
  - "<2-5 concrete observations from screenshot/artifacts>"
```

Rate only observable marketing-site presentation quality:

- render integrity
- layout discipline
- typography hierarchy
- imagery / asset quality and relevance
- iconography / illustration consistency
- brand-system coherence
- CTA, form, card, and component polish
- visible copy polish
- navigation clarity
- information clarity: can a visitor understand what they sell and for whom?
- trust-surface presentation: how badges, reviews, press, clinicians, certifications, legal/footer material are presented

Scale:

- `excellent`: unusually high-quality, distinctive, polished marketing presentation.
- `strong`: clearly professional and well-executed.
- `solid`: competent, credible, no major presentation issues.
- `basic`: usable but generic, thin, or lightly polished.
- `weak`: visibly amateur, inconsistent, dated, sloppy, or low-trust presentation.
- `broken`: capture shows broken rendering, missing CSS/images, junk page, or unusable site presentation.
- `unknown`: artifacts are insufficient or capture quality prevents a fair read.

Do not score company legitimacy, competitive threat, funding, headcount, traffic, SEO, press reputation, truth of claims, clinical/regulatory quality, CMS/framework quality, or market strength.

Blindness rule:

- Use only the packet and referenced capture artifacts.
- Do not open `profile.md`.
- Do not use Notion, Brian's ratings, or existing `Visual & brand impression` prose.
