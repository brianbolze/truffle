export const meta = {
  name: 'cohort-discovery',
  description: 'Race discovery + ranking techniques to fill out a market cohort (store-first, then net-new). Validated on menopause telehealth.',
  phases: [
    { title: 'Discover', detail: 'one isolated agent per discovery technique (barrier)' },
    { title: 'Verify', detail: 'dedupe + adversarial real/in-cohort check -> verified pool' },
    { title: 'Signals', detail: 'gather formidability signals for the verified pool' },
    { title: 'Rank', detail: 'LLM tournament (reference) + cheap-signal rankings' },
    { title: 'Capture', detail: 'auto /research-company the top-K net-new (arg-gated, default off)' },
  ],
}

// ---------- inputs (override via Workflow `args`) ----------
const a = args || {}
const COHORT = a.cohort ||
  'Menopause / perimenopause telehealth: direct-to-consumer brands that sell HRT or compounded hormone Rx and menopause-symptom care (hot flashes, sleep, mood, vaginal/sexual health) via online intake, cash-pay. A care-delivery BRAND, not a payer, pharmacy-only, retailer, or content site.'
const SEEDS = a.seeds || ['midihealth.com', 'joinwinona.com', 'gennev.com']
const CATEGORY_QUERIES = a.category_queries || [
  'best menopause telehealth 2026',
  'online HRT for menopause',
  'perimenopause treatment online prescription',
  'menopause doctor online',
]
const TOPK = a.topK || 8
const CAPTURE = !!a.capture // default OFF — dry discovery+rank first

// ---------- helpers ----------
const norm = (d) => String(d || '').trim().toLowerCase()
  .replace(/^https?:\/\//, '').replace(/^www\./, '').replace(/\/.*$/, '').replace(/\s+/g, '')

// ---------- schemas ----------
const DISCOVERY_SCHEMA = {
  type: 'object', additionalProperties: false, required: ['technique', 'candidates'],
  properties: {
    technique: { type: 'string' },
    candidates: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false, required: ['name', 'domain', 'evidence'],
        properties: {
          name: { type: 'string' },
          domain: { type: 'string', description: 'bare registrable domain, lowercase, no scheme/www/path' },
          evidence: { type: 'string', description: 'one line: why it is in the cohort + where you saw it' },
        },
      },
    },
  },
}

const VERIFY_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['canonical_domain', 'is_real', 'in_cohort', 'reason'],
  properties: {
    canonical_domain: { type: 'string', description: 'corrected bare apex domain' },
    is_real: { type: 'boolean', description: 'is this an actually-existing operating company' },
    in_cohort: { type: 'boolean', description: 'does it match the cohort definition' },
    reason: { type: 'string', description: 'one line; if excluded, name the confound (payer / pharmacy-only / retailer / adjacent / defunct / hallucinated)' },
  },
}

const RANK_SCHEMA = {
  type: 'object', additionalProperties: false, required: ['ranking'],
  properties: {
    ranking: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false, required: ['domain', 'rank', 'rationale'],
        properties: {
          domain: { type: 'string' },
          rank: { type: 'number', description: '1 = most formidable' },
          rationale: { type: 'string', description: 'one line on formidability (scale, traction, brand, funding, breadth)' },
        },
      },
    },
  },
}

const SIGNAL_SCHEMA = {
  type: 'object', additionalProperties: false, required: ['domain', 'ads_active', 'note'],
  properties: {
    domain: { type: 'string' },
    ads_active: { type: 'boolean' },
    ads_last_seen: { type: 'string' },
    note: { type: 'string' },
  },
}

// =====================================================================
// PHASE 1 — DISCOVER (fan-out, isolated; barrier so dedupe sees all)
// =====================================================================
phase('Discover')

const brief = (technique, how) => `You are a market-research scout running ONE discovery technique to help fill out a company cohort.

<cohort>
${COHORT}
</cohort>

<your_technique>
${technique}
${how}
</your_technique>

<rules>
- Return ONLY companies you have concrete evidence belong to the cohort. Do not pad the list.
- A cohort member is a care-delivery BRAND. Exclude insurers/payers, pharmacy-only fulfillers, pure retailers, content/affiliate sites, and adjacent-but-different businesses. If unsure, include it but say so in evidence — the verify stage adjudicates.
- domain = bare registrable apex, lowercase, no scheme/www/path (e.g. "midihealth.com").
- evidence = one line: what makes it in-cohort + where you saw it.
- You are blind to the other techniques. Maximize what YOUR technique surfaces.
</rules>

Return the structured DISCOVERY result.`

const TECHNIQUES = [
  {
    key: 'store', model: 'sonnet',
    how: `Search the LOCAL web-research store ONLY — no web. From the repo root:
- \`python3 scripts/store.py find "<name>"\` to resolve known brands, and
- grep the corpus: \`grep -ril "menopause\\|perimenopause\\|HRT\\|estrogen\\|hot flash" store/*/telehealth.md store/*/profile.md\` then read the hits.
Return only store companies that match the cohort. This is the store-first baseline.`,
  },
  {
    key: 'llm', model: 'sonnet',
    how: `Use ONLY your own training knowledge. No tools, no web, no store. List the menopause/perimenopause telehealth D2C brands you already know. This is the parametric floor — we want to see how far cheap recall gets with zero retrieval.`,
  },
  {
    key: 'listicle', model: 'sonnet',
    how: `Run the listicle coverage-radar recipe. Use \`python3 tools/serpapi.py "<query>"\` (see tools/serpapi.md) for 2-4 "best menopause telehealth / online HRT 2026" style queries across DIFFERENT authoritative publishers. Extract each list's named brand set, then return the UNION — and in evidence, note cross-source recurrence (named on >=2 authoritative lists is a strong signal; single low-authority affiliate names are weak). Exclude payers/retailers at extraction time.`,
  },
  {
    key: 'exa', model: 'sonnet',
    how: `Use Exa /findSimilar (see tools/exa_similar.md). Run \`python3 tools/exa_similar.py <seed> --num-results 25\` for EACH seed: ${SEEDS.join(', ')}. Pool the neighbors, fold mirror/i18n subdomains to the apex, and return those that are in-cohort.`,
  },
  {
    key: 'websearch', model: 'sonnet',
    how: `Enumerate via web search. Use the firecrawl_search MCP tool (load it via ToolSearch with query "firecrawl_search" first). Run category queries (e.g. ${CATEGORY_QUERIES.slice(0, 2).map((q) => '"' + q + '"').join(', ')} plus your own variants) and pull brand names from the result pages. Prefer brand sites over listicles.`,
  },
  {
    key: 'demand', model: 'sonnet',
    how: `Find demand-side cross-shop evidence (what buyers actually compare). Use firecrawl_search (load via ToolSearch) for "alternatives to <seed>" and "<seed> vs" for seeds ${SEEDS.join(', ')}, and look for owned /compare or /vs pages on the seed brands. Return the competitor brands named there. This surfaces the substitute set the supply-side techniques miss.`,
  },
]

const discoveryResults = await parallel(
  TECHNIQUES.map((t) => () =>
    agent(brief(t.key, t.how), { label: `discover:${t.key}`, phase: 'Discover', model: t.model, schema: DISCOVERY_SCHEMA })
      .then((r) => ({ technique: t.key, candidates: (r && r.candidates) || [] }))
      .catch(() => ({ technique: t.key, candidates: [] }))
  )
)

// ---- dedupe into a union map: domain -> { techniques:Set, evidence:[] } ----
const union = new Map()
for (const res of discoveryResults) {
  for (const c of res.candidates) {
    const d = norm(c.domain)
    if (!d) continue
    if (!union.has(d)) union.set(d, { domain: d, name: c.name, techniques: new Set(), evidence: [] })
    const e = union.get(d)
    e.techniques.add(res.technique)
    e.evidence.push(`[${res.technique}] ${c.evidence}`)
  }
}
const uniqueDomains = [...union.keys()]
log(`Discovery: ${discoveryResults.map((r) => r.technique + '=' + r.candidates.length).join('  ')}  ->  ${uniqueDomains.length} unique domains`)

// =====================================================================
// PHASE 2 — VERIFY (adversarial; barrier so we can build the pool)
// =====================================================================
phase('Verify')

const verifyResults = await parallel(
  uniqueDomains.map((d) => () =>
    agent(
      `Adversarially verify ONE candidate for a market cohort. Be skeptical — your job is to keep the pool clean.

<cohort>
${COHORT}
</cohort>

<candidate>
domain: ${d}
seen_as: ${union.get(d).name}
evidence_from_scouts:
${union.get(d).evidence.join('\n')}
</candidate>

Decide: (1) is_real — is this a genuine, currently-operating company (not a hallucinated or defunct name)? (2) in_cohort — does it match the cohort definition, NOT a payer/pharmacy-only/retailer/adjacent? Correct the domain to its real apex if wrong. Use firecrawl_search or a quick fetch only if you genuinely need to confirm existence; otherwise judge from the evidence. Return the structured verdict.`,
      { label: `verify:${d}`, phase: 'Verify', model: 'sonnet', schema: VERIFY_SCHEMA }
    )
      .then((v) => ({ src: d, ...v }))
      .catch(() => ({ src: d, canonical_domain: d, is_real: false, in_cohort: false, reason: 'verify failed' }))
  )
)

// ---- build verified pool (re-dedupe by canonical domain) ----
const pool = new Map() // canonical -> { domain, techniques:Set, evidence:[] }
for (const v of verifyResults) {
  if (!v.is_real || !v.in_cohort) continue
  const c = norm(v.canonical_domain) || v.src
  const srcEntry = union.get(v.src)
  if (!pool.has(c)) pool.set(c, { domain: c, techniques: new Set(), evidence: [] })
  const e = pool.get(c)
  if (srcEntry) { srcEntry.techniques.forEach((t) => e.techniques.add(t)); e.evidence.push(...srcEntry.evidence) }
}
const poolDomains = [...pool.keys()]
const inStore = new Set([...pool.values()].filter((e) => e.techniques.has('store')).map((e) => e.domain))
log(`Verified pool: ${poolDomains.length} in-cohort companies (${inStore.size} already in store, ${poolDomains.length - inStore.size} net-new)`)

// ---- RECALL RACE scoring (in-script; union-as-pool) ----
const poolSet = new Set(poolDomains)
const recallTable = TECHNIQUES.map((t) => {
  const raw = new Set()
  for (const res of discoveryResults) if (res.technique === t.key) res.candidates.forEach((c) => raw.add(norm(c.domain)))
  const found = [...raw].filter((d) => poolSet.has(d))
  const novel = found.filter((d) => !inStore.has(d))
  return {
    technique: t.key,
    raw: raw.size,
    found: found.length,
    recall: poolDomains.length ? +(found.length / poolDomains.length).toFixed(2) : 0,
    precision: raw.size ? +(found.length / raw.size).toFixed(2) : 0,
    novel: novel.length,
  }
})
log('RECALL RACE  ' + recallTable.map((r) => `${r.technique}: R=${r.recall} P=${r.precision} new=${r.novel}`).join('  |  '))

// =====================================================================
// PHASE 3 — SIGNALS (formidability inputs for the verified pool)
// =====================================================================
phase('Signals')

// ads presence per domain (bounded by pool size)
const adsResults = await parallel(
  poolDomains.map((d) => () =>
    agent(
      `Run \`python3 tools/ads_transparency.py ${d} --region US\` from the repo root and report whether this advertiser is actively running Google paid ads and the most recent activity you can see. See tools/ads_transparency.md. Return the structured signal (domain=${d}).`,
      { label: `ads:${d}`, phase: 'Signals', model: 'sonnet', schema: SIGNAL_SCHEMA }
    ).then((s) => ({ ...s, domain: d })).catch(() => ({ domain: d, ads_active: false, note: 'ads check failed' }))
  )
)
const adsByDomain = new Map(adsResults.map((s) => [norm(s.domain), s]))

// serp visibility: run the category SERPs ONCE, match the pool against them
const serpAgent = await agent(
  `Measure category SERP visibility for a verified company set. From the repo root run \`python3 tools/serpapi.py "<query>" --organic-only\` (see tools/serpapi.md) for these queries: ${CATEGORY_QUERIES.map((q) => '"' + q + '"').join(', ')}.
For EACH of these domains, report how many of the queries it appears in (organic) and its best rank seen: ${poolDomains.join(', ')}.
Return JSON only: {"visibility":[{"domain":"x.com","hits":N,"best_rank":N}]}.`,
  { label: 'serp:visibility', phase: 'Signals', model: 'sonnet' }
)
let serpVis = new Map()
try {
  const m = String(serpAgent).match(/\{[\s\S]*\}/)
  if (m) JSON.parse(m[0]).visibility.forEach((v) => serpVis.set(norm(v.domain), v))
} catch (e) { log('serp visibility parse failed — continuing with listicle+ads signals') }

// =====================================================================
// PHASE 4 — RANK (LLM tournament = reference; cheap signals compared)
// =====================================================================
phase('Rank')

const dossier = poolDomains.map((d) => {
  const e = pool.get(d)
  const ads = adsByDomain.get(d)
  const sv = serpVis.get(d)
  return `- ${d} | found_by=${[...e.techniques].join(',')} | listicle_recurrence=${e.techniques.size} | serp_hits=${sv ? sv.hits : '?'} | ads_active=${ads ? ads.ads_active : '?'}\n    evidence: ${e.evidence.slice(0, 3).join(' ; ')}`
}).join('\n')

const tournament = await agent(
  `You are a market analyst ranking companies in a cohort by FORMIDABILITY (scale, traction, brand strength, funding, category breadth, durability) — not just relevance.

<cohort>
${COHORT}
</cohort>

<companies>
${dossier}
</companies>

Rank ALL of them, most formidable first. Reason comparatively (pairwise) rather than scoring each in isolation — comparative judgment is more reliable. Use the signals provided plus your own knowledge. One-line rationale each. Return the structured ranking.`,
  { label: 'rank:tournament', phase: 'Rank', schema: RANK_SCHEMA }
)
const judgmentOrder = (tournament.ranking || []).slice().sort((x, y) => x.rank - y.rank).map((r) => norm(r.domain))

// cheap-signal orderings, computed in-script
const byListicle = poolDomains.slice().sort((x, y) => pool.get(y).techniques.size - pool.get(x).techniques.size)
const bySerp = poolDomains.slice().sort((x, y) => ((serpVis.get(y) || {}).hits || 0) - ((serpVis.get(x) || {}).hits || 0))
const byAds = poolDomains.slice().sort((x, y) => ((adsByDomain.get(y) || {}).ads_active ? 1 : 0) - ((adsByDomain.get(x) || {}).ads_active ? 1 : 0))

const topKoverlap = (order) => {
  const j = new Set(judgmentOrder.slice(0, TOPK))
  return order.slice(0, TOPK).filter((d) => j.has(d)).length
}
const rankComparison = {
  judgment_topK: judgmentOrder.slice(0, TOPK),
  agreement_with_judgment: {
    listicle_recurrence: topKoverlap(byListicle),
    serp_visibility: topKoverlap(bySerp),
    ads_presence: topKoverlap(byAds),
  },
}
log('RANK RACE  top-' + TOPK + ' agreement with judgment  ' +
  Object.entries(rankComparison.agreement_with_judgment).map(([k, v]) => `${k}=${v}/${TOPK}`).join('  '))

// =====================================================================
// PHASE 5 — CAPTURE top-K net-new (arg-gated; default OFF)
// =====================================================================
const topNetNew = judgmentOrder.filter((d) => !inStore.has(d)).slice(0, TOPK)
let captured = []
if (CAPTURE && topNetNew.length) {
  phase('Capture')
  log(`Capturing ${topNetNew.length} net-new brands via /research-company (spends Firecrawl)`)
  captured = await parallel(
    topNetNew.map((d) => () =>
      agent(
        `Capture the company at ${d} into the web-research store. Follow the /research-company skill and its firecrawl-capture playbook (skills/research-company/). Produce store/${d}/profile.md and the standard modules per the SCHEMA contract. Report the path written and any blockers.`,
        { label: `capture:${d}`, phase: 'Capture' }
      ).then(() => ({ domain: d, ok: true })).catch(() => ({ domain: d, ok: false }))
    )
  )
} else if (!CAPTURE) {
  log(`Capture skipped (capture:false). ${topNetNew.length} net-new brands queued for capture: ${topNetNew.join(', ')}`)
}

// ---------- return summary (orchestrator writes FINDINGS) ----------
return {
  cohort: COHORT,
  verified_pool: poolDomains,
  in_store: [...inStore],
  net_new: poolDomains.filter((d) => !inStore.has(d)),
  recall_race: recallTable,
  rank_race: rankComparison,
  top_k_net_new: topNetNew,
  captured,
}
