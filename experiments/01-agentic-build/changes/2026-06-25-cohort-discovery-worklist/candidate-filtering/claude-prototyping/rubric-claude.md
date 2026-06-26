# Sorting rubric (define-by-description)

You sort names pulled from "best X" / "alternatives" listicles and SERPs in a given market (the **cohort**). For each candidate, pick a **kind**, then a **route**, with a short cited reason. When unsure and a homepage is fetchable, peek it.

## The one rule that matters most

Promote to **`capture`** ONLY when the evidence shows the entity selling **its own product/service in the cohort's market**. If the entity only ranks / reviews / compares OTHERS, it is a list-writer → **`preserve`**.

A company that publishes its own *"best X"* / *"alternatives"* page is **still a real company** — judge by whether *its own offering* is described, **not** by whether its website hosted the page. (This is the trap: do not route to `preserve` just because the candidate's domain equals the source page's domain.)

## Kinds — what is it? (pick the best single fit)

- **company** — sells its own product/service in the cohort. Signals: snippet describes its *own* product, pricing, plans, features ("$99/month", "Pro plans start at…", "our platform", "we offer"); first-person; a clear own domain.
- **publisher** — its role here is to evaluate/rank/list OTHER companies. Signals: "we analyzed N data points on M providers", "best … in 2026", author/editor bylines, blog/article/`/best-`/`/alternatives` URLs, affiliate or review framing; no own in-cohort product described.
- **directory** — aggregates many third-party sellers/listings; not a single seller, not an editorial ranking.
- **product_or_feature** — a named product/tool/feature that lives INSIDE a larger platform, not a standalone company. Signals: "X, a [feature] in [Platform]", "formerly [Product]", a capability/SKU of a broader company. Record the parent.
- **reference** — academic / government / non-commercial pages, nav fragments, junk. Signals: .gov/.edu/journal archives, disclaimers, navigation text, social links.
- **uncertain** — plausibly a real company but evidence too thin to tell. Peek the homepage if available.

## Routes — what do we do?

- **capture** — `company` with its own in-cohort offering, evidence supports it. Worth a full profile.
- **preserve** — `publisher` / `directory` / `reference`. Keep the page as market evidence; do NOT capture the publisher as a company.
- **product** — `product_or_feature`. Tag + preserve; record the parent as a possible separate `capture`.
- **review** — `uncertain`; OR a real company known only second-hand (named only inside someone else's comparison) worth a quick look; OR a clear name with an unknown website. This is where the homepage peek happens.
- **drop** — `reference` / junk with no market value.

## Two reminders

- **"Real company" ≠ "capture target for THIS cohort."** A real company that here is only the list's author (e.g. an automation platform hosting a meeting-tools roundup) → `preserve` for this cohort.
- **Cohort fit matters:** the own product must be in THIS market, not merely "a company."

## Output — one JSON line per candidate

```json
{"name":"","domain":"","cohort":"","kind":"","route":"","confidence":"high|med|low","reason":"<=140 chars, quote the deciding snippet","parent":null,"peeked":false}
```
