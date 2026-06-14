export const meta = {
  name: 'visual-miner-calibration-ab',
  description: 'A/B the visual-evidence miner model (sonnet vs opus) on the same goinfusive-com tiles; judge inherits Opus both runs',
  phases: [
    { title: 'Sonnet miners' },
    { title: 'Opus miners' },
  ],
}

const SCRIPT = 'skills/visual-evidence/mine.workflow.js'
const TILES = [
  'store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-00-y00000.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-01-y01220.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-02-y02440.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-03-y03660.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-04-y04880.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-05-y06100.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-06-y07320.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-07-y08063.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-00-y00000.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-01-y01220.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-02-y02440.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-03-y03660.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-04-y04880.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-05-y06100.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-06-y07320.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-07-y08540.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-08-y09760.png',
  'store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-09-y10287.png',
]

log(`A/B miner calibration on ${TILES.length} goinfusive-com tiles`)

phase('Sonnet miners')
const t0 = budget.spent()
const sonnet = await workflow({ scriptPath: SCRIPT }, { tiles: TILES, minerModel: 'sonnet' })
const t1 = budget.spent()
log(`sonnet run done: ${sonnet.raw_cards?.length || 0} raw cards, ${sonnet.accepted_cards?.length || 0} accepted, ~${t1 - t0} out tokens`)

phase('Opus miners')
const opus = await workflow({ scriptPath: SCRIPT }, { tiles: TILES, minerModel: 'opus' })
const t2 = budget.spent()
log(`opus run done: ${opus.raw_cards?.length || 0} raw cards, ${opus.accepted_cards?.length || 0} accepted, ~${t2 - t1} out tokens`)

// per-family polarity tally over RAW miner cards
function tally(cards) {
  const fams = {}
  for (const c of (cards || [])) {
    const f = c.family || 'unknown'
    fams[f] = fams[f] || { strong: 0, mixed: 0, poor: 0 }
    if (fams[f][c.polarity] != null) fams[f][c.polarity]++
  }
  return fams
}

return {
  sonnet: {
    tokens_out: t1 - t0,
    raw_count: sonnet.raw_cards?.length || 0,
    accepted_count: sonnet.accepted_cards?.length || 0,
    rejected_count: sonnet.rejected_cards?.length || 0,
    raw_polarity_by_family: tally(sonnet.raw_cards),
    raw_cards: sonnet.raw_cards || [],
    rejected_cards: sonnet.rejected_cards || [],
  },
  opus: {
    tokens_out: t2 - t1,
    raw_count: opus.raw_cards?.length || 0,
    accepted_count: opus.accepted_cards?.length || 0,
    rejected_count: opus.rejected_cards?.length || 0,
    raw_polarity_by_family: tally(opus.raw_cards),
    raw_cards: opus.raw_cards || [],
    rejected_cards: opus.rejected_cards || [],
  },
}