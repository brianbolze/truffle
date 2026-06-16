#!/usr/bin/env python3
"""Tier-B dismissal probe harness. Experiment-grade, not committed.

Renders a URL under several candidate dismissal mechanisms and records, for each, the
structural overlay signature + scroll-lock state + a first-viewport screenshot — so the
diff against the FAITHFUL (as-served, no dismissal) render is the evidence for both probe
directions: does the mechanism CLEAR overlays, and does it ever HIDE real content?

Variants under test (each a fresh browser context — no cookie carryover):
  faithful     — warm-scroll + settle, no dismissal. The baseline.
  affordance   — Escape + click dismiss-labels *inside overlay-shaped elements* + scroll
                 release. Uses the site's own dismiss affordances; structurally cannot hide
                 content (it only clicks the page's buttons / presses Escape).
  constrained  — affordance + CSS-hide of *edge-pinned banner-shaped* elements only
                 (never a top-nav strip, never a full-viewport element). The fallback for
                 banners with no recognized button.
  naive        — affordance + CSS-hide of EVERY detected overlay (the dumb version, to show
                 why the constraints matter — it nukes fullscreen heroes + nav).

Usage:
  probe.py recon  <url> <out-dir>                      # faithful only
  probe.py probe  <url> <out-dir> [variant ...]        # default: all four
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError as PWTimeout

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W, H = 1920, 1400

# Dismiss-label set: negative-first (decline a newsletter), then affirmative (accept cookies),
# then close. Matched case-insensitively against button/link text + aria-label, ONLY inside
# overlay-shaped elements. No cookie/consent vendor strings anywhere — pure generic.
DISMISS_LABELS = [
    "no thanks", "no, thanks", "not now", "maybe later", "decline", "reject all", "reject",
    "deny", "accept all", "accept", "agree", "i agree", "i understand", "i consent",
    "got it", "ok", "okay", "continue", "close", "dismiss", "allow all",
]

VARIANTS = ["faithful", "affordance", "constrained", "naive"]

DETECT_OVERLAYS = """
() => {
  const vw = innerWidth, vh = innerHeight, area = vw*vh;
  const out = [];
  for (const el of document.querySelectorAll('body *')) {
    const cs = getComputedStyle(el);
    if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
    if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) continue;
    const r = el.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) continue;
    const ix = Math.max(0, Math.min(r.right, vw) - Math.max(r.left, 0));
    const iy = Math.max(0, Math.min(r.bottom, vh) - Math.max(r.top, 0));
    const cover = (ix*iy)/area;
    if (cover < 0.02) continue;
    out.push({
      tag: el.tagName, id: el.id || '',
      cls: (el.getAttribute('class')||'').slice(0,70),
      pos: cs.position, z: parseInt(cs.zIndex)||0, cover: +cover.toFixed(3),
      rect: [r.left|0, r.top|0, r.width|0, r.height|0],
      text: (el.innerText||'').replace(/\\s+/g,' ').trim().slice(0,80),
      kind: classify(r, cover, vw, vh),
    });
  }
  function classify(r, cover, vw, vh) {
    const topPinned = r.top <= 5, fullWidth = r.width >= 0.6*vw, shortStrip = r.height <= 0.18*vh;
    if (topPinned && fullWidth && shortStrip) return 'nav';      // top header strip -> KEEP
    if (cover >= 0.6) return 'fullscreen';                       // modal backdrop OR real splash
    return 'banner';                                             // edge/corner partial -> cookie-ish
  }
  return out.sort((a,b)=>b.cover-a.cover).slice(0,15);
}
"""

# Clickable dismiss affordances *inside* an overlay-shaped ancestor. Returns click points.
FIND_DISMISS_TARGETS = """
(labels) => {
  const vw = innerWidth, vh = innerHeight;
  const inOverlay = (el) => {
    let e = el;
    while (e && e !== document.body) {
      const cs = getComputedStyle(e);
      if (cs.position === 'fixed' || cs.position === 'sticky') {
        const r = e.getBoundingClientRect();
        const cover = (Math.max(0, Math.min(r.right,vw)-Math.max(r.left,0)) *
                       Math.max(0, Math.min(r.bottom,vh)-Math.max(r.top,0)))/(vw*vh);
        const top = r.top <= 5, shortNav = top && r.width>=0.6*vw && r.height<=0.18*vh;
        if (!shortNav && ((parseInt(cs.zIndex)||0) >= 1 || cover > 0.04)) return true;
      }
      e = e.parentElement;
    }
    return false;
  };
  const out = [];
  const clickables = document.querySelectorAll(
    "button,a[role=button],[role=button],a,[aria-label]");
  for (const el of clickables) {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const r = el.getBoundingClientRect();
    if (r.width < 4 || r.height < 4) continue;
    const txt = (el.innerText||'').replace(/\\s+/g,' ').trim().toLowerCase();
    const aria = (el.getAttribute('aria-label')||'').toLowerCase();
    const isX = txt === '×' || txt === 'x' || /close|dismiss/.test(aria);
    const match = labels.find(l => txt === l) || (isX ? 'close(x)' : null);
    if (!match) continue;
    if (!inOverlay(el)) continue;
    out.push({x: (r.left+r.right)/2, y: (r.top+r.bottom)/2, label: match, text: txt.slice(0,30)});
  }
  return out;
}
"""

SCROLL_STATE = """
() => {
  const before = window.scrollY;
  window.scrollTo(0,0); const top = window.scrollY; window.scrollTo(0, before);
  const b = getComputedStyle(document.body), h = getComputedStyle(document.documentElement);
  return {topY: top, bodyOverflow: b.overflow, bodyPosition: b.position,
          bodyTop: b.top, htmlOverflow: h.overflow};
}
"""

# Force-release a scroll lock (overflow:hidden / position:fixed;top:-Y trick), then verify.
RELEASE_SCROLL_LOCK = """
() => {
  for (const el of [document.documentElement, document.body]) {
    el.style.setProperty('overflow', 'visible', 'important');
    el.style.setProperty('position', 'static', 'important');
    el.style.setProperty('top', 'auto', 'important');
    el.style.setProperty('height', 'auto', 'important');
  }
  window.scrollTo(0,0);
  return window.scrollY;
}
"""

PAGE_INFO = """
() => ({url: location.href, title: document.title,
        scrollHeight: document.documentElement.scrollHeight,
        imageCount: document.images.length,
        loadedImages: Array.from(document.images).filter(i=>i.complete&&i.naturalWidth>0).length,
        textLen: (document.body.innerText||'').length})
"""


def settle(page) -> None:
    try:
        page.wait_for_load_state("networkidle", timeout=30000)
    except PWTimeout:
        pass
    page.wait_for_timeout(2500)
    h = page.evaluate("document.documentElement.scrollHeight")
    for y in range(0, h, 600):
        page.evaluate("(y)=>window.scrollTo(0,y)", y)
        page.wait_for_timeout(80)
    page.evaluate("()=>window.scrollTo(0,0)")
    page.wait_for_timeout(600)


def css_sel(ov: dict) -> str | None:
    if ov["id"]:
        return "#" + escape_ident(ov["id"])
    cls = ov["cls"].split()
    if cls:
        return "." + escape_ident(cls[0])
    return None


def escape_ident(s: str) -> str:
    return "".join(ch if (ch.isalnum() or ch in "-_") else "\\" + ch for ch in s)


def dismiss(page, structural: str) -> dict:
    """Run the mechanism. `structural` ∈ {'none','constrained','naive'}.

    Layers: Escape → click dismiss-affordances inside overlays → release scroll-lock →
    (structural) CSS-hide remaining overlays per mode. Returns an audit of what each touched.
    """
    audit: dict = {"escape": 0, "clicked": [], "scroll_released": None, "hidden": []}

    for _ in range(2):
        page.keyboard.press("Escape")
        page.wait_for_timeout(180)
    audit["escape"] = 2

    # click dismiss affordances, re-detecting after each (stop once overlays stop shrinking)
    for _ in range(4):
        targets = page.evaluate(FIND_DISMISS_TARGETS, DISMISS_LABELS)
        if not targets:
            break
        t = targets[0]
        try:
            page.mouse.click(t["x"], t["y"])
            page.wait_for_timeout(350)
            audit["clicked"].append({"label": t["label"], "text": t["text"]})
        except Exception:
            break
    page.keyboard.press("Escape")
    page.wait_for_timeout(150)

    # scroll-lock release + verify
    s = page.evaluate(SCROLL_STATE)
    if s["topY"] > 50 or s["bodyOverflow"] == "hidden" or s["bodyPosition"] == "fixed":
        after = page.evaluate(RELEASE_SCROLL_LOCK)
        audit["scroll_released"] = {"before": s, "after_topY": after,
                                    "released": after <= 50}

    if structural != "none":
        remaining = page.evaluate(DETECT_OVERLAYS)
        sels = []
        for ov in remaining:
            if structural == "constrained" and ov["kind"] != "banner":
                continue  # constrained: only edge-pinned banners; never nav/fullscreen
            sel = css_sel(ov)
            if sel:
                sels.append((sel, ov))
        if sels:
            page.add_style_tag(content=",".join(s for s, _ in sels) + "{display:none!important}")
            page.wait_for_timeout(200)
            audit["hidden"] = [{"sel": s, "kind": ov["kind"], "cover": ov["cover"],
                                "z": ov["z"], "text": ov["text"][:40]} for s, ov in sels]
    return audit


def signature(page) -> dict:
    return {"info": page.evaluate(PAGE_INFO), "scroll": page.evaluate(SCROLL_STATE),
            "overlays": page.evaluate(DETECT_OVERLAYS)}


def render(url: str, out: Path, variant: str) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME, headless=True,
                                    args=["--autoplay-policy=no-user-gesture-required"])
        ctx = browser.new_context(viewport={"width": W, "height": H}, device_scale_factor=1,
                                  locale="en-US", reduced_motion="reduce")
        page = ctx.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        settle(page)
        result = {"url": url, "variant": variant}
        if variant != "faithful":
            result["audit"] = dismiss(page, {"affordance": "none", "constrained": "constrained",
                                             "naive": "naive"}[variant])
            page.wait_for_timeout(300)
        result["sig"] = signature(page)
        page.evaluate("()=>window.scrollTo(0,0)")
        page.wait_for_timeout(300)
        page.screenshot(path=str(out / f"{variant}.png"), full_page=False, type="png")
        browser.close()
    return result


def main() -> None:
    mode, url, out = sys.argv[1], sys.argv[2], Path(sys.argv[3])
    variants = ["faithful"] if mode == "recon" else (sys.argv[4:] or VARIANTS)
    reports = {}
    for v in variants:
        reports[v] = render(url, out, v)
    with open(out / "report.json", "w", encoding="utf-8") as fh:
        json.dump(reports, fh, indent=2)
    # compact stdout
    summary = {"url": url}
    for v, r in reports.items():
        sig = r["sig"]
        summary[v] = {
            "topY": sig["scroll"]["topY"], "bodyOverflow": sig["scroll"]["bodyOverflow"],
            "textLen": sig["info"]["textLen"], "scrollH": sig["info"]["scrollHeight"],
            "overlays": [[o["kind"], o["id"] or o["cls"][:24], o["cover"], o["z"]]
                         for o in sig["overlays"][:6]],
        }
        if "audit" in r:
            summary[v]["audit"] = {"clicked": [c["label"] for c in r["audit"]["clicked"]],
                                   "scroll_released": r["audit"]["scroll_released"],
                                   "hidden": [(h["kind"], h["sel"]) for h in r["audit"]["hidden"]]}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
