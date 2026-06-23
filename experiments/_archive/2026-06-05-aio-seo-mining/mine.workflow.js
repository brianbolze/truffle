export const meta = {
  name: 'aio-seo-mining',
  description: 'Mine the company corpus for technical-SEO / AIO discoverability tactics, fan-out by vertical then synthesize a ranked catalog',
  phases: [
    { title: 'Extract tactics', detail: 'one agent per vertical batch reads harvested signals + raw llms/robots/json-ld, returns concrete tactics' },
    { title: 'Synthesize catalog', detail: 'dedupe + rank by prevalence×cleverness, flag vertical divergence, AIO-first' },
  ],
}

const A = (typeof args === 'string') ? JSON.parse(args) : (args || {})
const { outDir, storeDir, batches, rollups } = A
if (!Array.isArray(batches)) throw new Error('args.batches missing; got args=' + JSON.stringify(args).slice(0, 200))

const TACTIC = {
  type: 'object',
  required: ['tactic','layer','signal','what','example_company','vertical','example','citation','steal_this','cleverness'],
  additionalProperties: false,
  properties: {
    tactic: { type: 'string', description: 'short name for the technique' },
    layer: { type: 'string', enum: ['AIO','SEO','both'], description: 'AIO=helps LLM/AI-answer discoverability; SEO=classic search; both' },
    signal: { type: 'string', enum: ['llms.txt','json-ld','robots.txt','meta-tags','sitemap','content','other'] },
    what: { type: 'string', description: '1-2 sentences: the technique and why it aids discoverability' },
    example_company: { type: 'string', description: 'slug of the clearest example' },
    vertical: { type: 'string' },
    example: { type: 'string', description: 'VERBATIM snippet from the source file, <=320 chars, that proves the tactic' },
    citation: { type: 'string', description: 'real file path under outDir/raw or store/, or the live URL' },
    steal_this: { type: 'string', description: 'one imperative line we could copy' },
    cleverness: { type: 'integer', minimum: 1, maximum: 5, description: '1=table-stakes hygiene, 5=rare and ingenious' },
  },
}
const EXTRACT = { type: 'object', required: ['batch_label','tactics'], additionalProperties: false,
  properties: { batch_label: { type: 'string' }, batch_notes: { type: 'string' },
    tactics: { type: 'array', items: TACTIC } } }

const CATALOG_ITEM = {
  type: 'object',
  required: ['rank','tactic','layer','signal','what','prevalence','verticals','example_company','example','citation','steal_this','cleverness'],
  additionalProperties: false,
  properties: {
    rank: { type: 'integer' },
    tactic: { type: 'string' }, layer: { type: 'string', enum: ['AIO','SEO','both'] },
    signal: { type: 'string' }, what: { type: 'string' },
    prevalence: { type: 'string', description: 'how common, e.g. "11/22 SaaS" or "25/88 corpus" — use exact rollup counts where given' },
    verticals: { type: 'string', description: 'which verticals do this / skip it' },
    example_company: { type: 'string' }, example: { type: 'string' }, citation: { type: 'string' },
    steal_this: { type: 'string' }, cleverness: { type: 'integer', minimum: 1, maximum: 5 },
  },
}
const SYNTH = {
  type: 'object',
  required: ['headlines','catalog','divergence'],
  additionalProperties: false,
  properties: {
    headlines: { type: 'array', items: { type: 'string' }, description: '5-8 most actionable AIO-first takeaways' },
    catalog: { type: 'array', items: CATALOG_ITEM, description: 'deduped, ranked most-actionable-AIO-first' },
    divergence: { type: 'array', items: { type: 'object', additionalProperties: false,
      required: ['axis','telehealth','b2b_saas','luxury_watch','consumer','takeaway'],
      properties: { axis: { type: 'string' }, telehealth: { type: 'string' }, b2b_saas: { type: 'string' },
        luxury_watch: { type: 'string' }, consumer: { type: 'string' }, takeaway: { type: 'string' } } } },
  },
}

const LENS = `
You are a technical-SEO / "AIO" analyst. AIO = getting cited/surfaced by LLM answer engines
(ChatGPT, Claude, Perplexity, Google AI Overviews). Bias toward AIO over classic SEO where they diverge.

What counts as an AIO-native tactic (look hardest for these):
- **llms.txt**: presence, structure, and cleverness. Conventions to spot: an H1 + a ">" one-line summary
  the model can lift; curated topic link lists; pointing at .md versions of pages ("append .md"); a
  llms-full.txt single-file dump; ordering/wording that pre-chunks the site for retrieval.
- **JSON-LD / schema.org**: which @types and how rich. FAQPage/Question/Answer (feeds AI Q&A + Google
  "People also ask"), MedicalBusiness/Physician (E-E-A-T for health), Product/Offer (price in answers),
  AggregateRating/Review (self-reported proof), BreadcrumbList, SoftwareApplication, sameAs (entity graph
  linking the brand to Wikipedia/LinkedIn/Crunchbase so engines resolve the entity), VideoObject, HowTo.
- **robots.txt posture toward AI crawlers**: distinguish TRAINING bots (GPTBot, ClaudeBot, Google-Extended,
  CCBot, Bytespider, Amazonbot, Applebot-Extended) from RETRIEVAL/answer-time bots (OAI-SearchBot,
  ChatGPT-User, PerplexityBot, Claude-User/Claude-SearchBot). Blocking retrieval bots = an AIO own-goal
  (removed from live answers); explicitly ALLOWing AI bots, or blocking only scrapers while welcoming
  answer bots, is a deliberate clever posture. Note human-readable comments/easter-eggs too.
- **meta + content**: answer-shaped <meta description>/og patterns, definitional "X is a ..." opening
  sentences (snippet/citation bait), structured comparison/FAQ content.

Rules: examples MUST be verbatim from the cited file (don't paraphrase into the example field). Citations
must be real paths you actually read. Prefer clever/AIO over table-stakes SEO. Quality over quantity:
return your batch's 6-12 strongest, most citable tactics (dedupe near-identical ones into the best example).
`

phase('Extract tactics')
const extractResults = await parallel(batches.map(b => () => {
  const slugList = b.slugs.join(', ')
  return agent(
    `${LENS}

## Your batch: ${b.label} (vertical: ${b.vertical})
Companies (slugs): ${slugList}

## How to read each company (cwd is the project root)
For each slug, read the harvested signal record:
  ${outDir}/signals/<slug>.json
It embeds: vertical, robots.ai_posture (per-crawler: allowed/partial/blocked, a trailing "*" = inherited
from User-agent:* not a named rule, "default"=not named), robots.sitemaps, llms_txt.present, jsonld.types
+ jsonld.type_pages (counts), jsonld_examples (one raw block per interesting @type — your best citation
source), meta (homepage meta tags), canonical, hreflang_count, robots_body (truncated), llms_body (truncated).

For the FULL text of a present llms.txt or robots.txt (the truncated body isn't enough), read:
  ${outDir}/raw/<slug>.llms.txt   and   ${outDir}/raw/<slug>.robots.txt
For deeper JSON-LD than the stashed example, grep the payloads:
  ${storeDir}/<slug>/captures/*/.payloads/*.json   (rawHtml carries the <script type="application/ld+json"> blocks)
Profile context if useful: ${storeDir}/<slug>/profile.md

Extract the concrete discoverability tactics these companies actually use, each with a VERBATIM example,
a real citation path, and a one-line "steal this". Set cleverness honestly (most hygiene = 1-2; reserve 4-5
for genuinely rare/ingenious moves). Tag layer AIO vs SEO. Return JSON per the schema.`,
    { schema: EXTRACT, label: `extract:${b.label}`, phase: 'Extract tactics' }
  )
}))

const batchOut = extractResults.filter(Boolean)
const allTactics = batchOut.flatMap(r => (r.tactics || []).map(t => ({ ...t, _batch: r.batch_label })))
log(`extracted ${allTactics.length} tactics across ${batchOut.length}/${batches.length} batches`)

phase('Synthesize catalog')
const synthesis = await agent(
  `${LENS}

You are synthesizing one ranked tactics CATALOG from ${allTactics.length} raw tactics that ${batchOut.length}
per-vertical extractor agents found across an 88-company corpus (telehealth, B2B SaaS, luxury watches,
consumer/marketplace). Goal: a catalog of concrete, stealable tactics, MOST-ACTIONABLE-AIO-FIRST.

## Exact corpus prevalence (deterministic — use these counts, don't re-estimate when one applies)
${JSON.stringify(rollups, null, 1)}

## Raw tactics from the extractors (dedupe these)
${JSON.stringify(allTactics, null, 1)}

## Do
1. **Dedupe** near-identical tactics into one catalog entry, keeping the single best verbatim example +
   citation. Merge their steal-this lines.
2. **Rank** by (actionability for AIO) then (prevalence × cleverness). AIO-native tactics (llms.txt,
   answer-engine schema, AI-crawler posture, entity/sameAs graph, snippet-bait content) rank ABOVE classic
   SEO hygiene. Number rank 1..N.
3. Fill **prevalence** from the rollup counts where they map (llms.txt = 25/88; sitemaps-in-robots count;
   per-vertical llms split; names-AI-crawler = 12/88; etc.); otherwise give your best "seen in N of batch".
4. **verticals**: who does it / who conspicuously skips it.
5. **divergence**: 4-7 axes where telehealth vs B2B SaaS vs luxury vs consumer genuinely differ
   (e.g. llms.txt adoption, FAQPage/MedicalBusiness schema, schema minimalism in luxury, AI-crawler stance).
   Be concrete and cite the split.
6. **headlines**: 5-8 punchy, decision-useful lines, AIO-first.

Keep examples verbatim and citations real (pass them through from the raw tactics). Return JSON per the schema.`,
  { schema: SYNTH, label: 'synthesize', phase: 'Synthesize catalog' }
)

return { batches: batchOut.length, tacticsIn: allTactics.length,
         catalog: synthesis.catalog.length, synthesis }
