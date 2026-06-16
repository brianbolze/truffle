#!/usr/bin/env python3
"""shoot — Tier-B browser re-render for the visual-evidence module.

Firecrawl's headless browser exposes no WebGL and fires its full-page screenshot before
lazy media and scroll-triggered animations settle — so a WebGL hero renders as a grey
block, count-ups read 0.0, and reveals stay half-faded (proven on Function Health). This
is the escalation the QA gate reaches for when a cached payload can't be trusted: drive
*system Chrome* (real WebGL via ANGLE Metal), warm-scroll to fire lazy media, then ask the
page for reduced motion and settle so animations finish before tiling.

Faithful by default. `--dismiss` opts in to the affordance-only overlay dismissal validated
in experiments/2026-06-16-tier-b-dismissal/ — Escape + click the page's *own* dismiss
controls scoped to overlay-shaped elements + release any scroll-lock. No vendor denylist,
no CSS-hide of "junk-looking" fixed boxes (every content-harm event in the probe came from
the hide-by-force layer; affordance-only cleared 5/5 dismissable overlays with 0/8 harm).

It writes native-resolution viewport tiles + a manifest fragment to --out-dir, the same
tile shape `tile.py` emits for the cached path, so downstream blind mining reads either
uniformly. No Firecrawl spend; the only dependency the module earns (quarantined here).

CLI:  python3 scripts/shoot.py <url> --out-dir store/<slug>/captures/<date>/tiles/<page> [--dismiss]
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path

from playwright.sync_api import Page, sync_playwright
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

# System Chrome (not Playwright's bundled Chromium) — it ships real GPU/WebGL, which is the
# whole point: it renders the marketing media Firecrawl's browser can't.
DEFAULT_CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Injected only after the warm scroll: forces any lingering opacity/transform reveal to its
# resting state and zeroes transition/animation time, so a tile never catches mid-animation.
FINAL_STATE_CSS = """
*, *::before, *::after {
  animation-duration: 0s !important; animation-delay: 0s !important;
  transition-duration: 0s !important; transition-delay: 0s !important;
}
[class*="fade"], [class*="reveal"], [data-aos], [class*="inview"], [class*="in-view"] {
  opacity: 1 !important; transform: none !important; filter: none !important;
}
"""

# Dismiss-label set — negative-first (decline a newsletter) → affirmative (accept cookies) →
# close. Matched case-insensitively against button/link text + aria-label, ONLY inside
# overlay-shaped elements (see FIND_DISMISS_TARGETS). No cookie/consent vendor strings — pure
# generic; that's the whole point of the affordance path.
DISMISS_LABELS = [
    "no thanks", "no, thanks", "not now", "maybe later", "decline", "reject all", "reject",
    "deny", "accept all", "accept", "agree", "i agree", "i understand", "i consent",
    "got it", "ok", "okay", "continue", "close", "dismiss", "allow all",
]

# Return click points for any dismiss-affordance INSIDE an overlay-shaped ancestor. The
# overlay scope (fixed/sticky with z>=1 or cover>4%, excluding top-nav strips) is the
# guardrail the probe's `reshoot.py` lacked — without it a footer "Accept Terms" was fair
# game. See experiments/2026-06-16-tier-b-dismissal/probe.py for the validated reference.
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
    out.push({x: (r.left+r.right)/2, y: (r.top+r.bottom)/2, label: match});
  }
  return out;
}
"""

# Forced scroll-lock release: overflow/position/top reset on both html + body. The probe
# never had to fire this — dismissal always sufficed — so it's unproven belt-and-suspenders
# for the "locked but un-dismissable" edge, not a validated path.
RELEASE_SCROLL_LOCK = """
() => {
  for (const el of [document.documentElement, document.body]) {
    el.style.setProperty('overflow', 'visible', 'important');
    el.style.setProperty('position', 'static', 'important');
    el.style.setProperty('top', 'auto', 'important');
    el.style.setProperty('height', 'auto', 'important');
  }
  window.scrollTo(0, 0);
  return window.scrollY;
}
"""


def tile_offsets(scroll_height: int, viewport_height: int, overlap: int) -> list[int]:
    """Top y-offset of each viewport tile, overlapping by `overlap` and pinning the last to the floor."""
    step = viewport_height - overlap
    offsets: list[int] = []
    y = 0
    last = max(0, scroll_height - viewport_height)
    while y < last:
        offsets.append(y)
        y += step
    if not offsets or offsets[-1] != last:
        offsets.append(last)
    return offsets


def reachable_top(page: Page) -> int:
    """The y the page actually lands on after scrollTo(0, 0) — a non-zero value means scroll is locked."""
    return page.evaluate("() => { window.scrollTo(0, 0); return window.scrollY; }")


def dismiss(page: Page) -> None:
    """Affordance-only overlay dismissal — Escape + click the page's *own* dismiss controls scoped to overlays.

    Validated across 8 live sites in experiments/2026-06-16-tier-b-dismissal/: cleared 5/5
    dismissable overlays (cookie banners + custom CMPs + a newsletter modal + a fullscreen
    splash+cookie combo) with 0/8 content-harm. The probe rejected every structural CSS-hide
    alternative (4/8 harm naive, 1/8 harm constrained) — z-index is no guard (Sequoia's nav
    and its cookie banner are both z=9999), so this path never hides fixed boxes; it only
    presses keys and clicks the page's own buttons, and therefore has no mechanism to delete
    real content. A banner with unrecognized button text + no Escape handler is the intended
    safe ceiling — it slips through; the kept-faithful tiles + agent compare catch it.
    """
    for _ in range(2):
        page.keyboard.press("Escape")
        page.wait_for_timeout(180)
    for _ in range(4):
        targets = page.evaluate(FIND_DISMISS_TARGETS, DISMISS_LABELS)
        if not targets:
            break
        target = targets[0]
        try:
            page.mouse.click(target["x"], target["y"])
            page.wait_for_timeout(350)
        except Exception:
            break
    page.keyboard.press("Escape")
    page.wait_for_timeout(150)


def release_scroll_lock(page: Page) -> bool:
    """Dismiss-then-reverify, with a forced overflow/position reset as fallback. True if the top is reachable.

    In the probe, dismissal released both locked sites' locks for free (bodyOverflow:
    hidden → visible the instant the overlay closed). The forced reset is the unproven
    belt-and-suspenders for the "locked but un-dismissable" edge that didn't occur in 8 sites.
    """
    if reachable_top(page) <= 50:
        return True
    page.evaluate(RELEASE_SCROLL_LOCK)
    return reachable_top(page) <= 50


def capture(url: str, out_dir: Path, width: int, height: int, overlap: int,
            settle_ms: int, chrome: str, do_dismiss: bool) -> dict:
    """Drive system Chrome to warm-scroll `url`, settle motion, then write viewport tiles to out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=chrome,
            headless=True,
            args=["--autoplay-policy=no-user-gesture-required"],
        )
        # reduced_motion=reduce: a well-built site shortcuts its animations to final state for us.
        context = browser.new_context(
            viewport={"width": width, "height": height},
            device_scale_factor=1,
            locale="en-US",
            reduced_motion="reduce",
        )
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        try:
            page.wait_for_load_state("networkidle", timeout=30000)
        except PlaywrightTimeoutError:
            pass
        page.wait_for_timeout(2500)

        if do_dismiss:
            dismiss(page)

        # Finer warm scroll (600px steps) so every intersection-observer fires and lazy media loads.
        scroll_height = page.evaluate("document.documentElement.scrollHeight")
        for y in range(0, scroll_height, 600):
            page.evaluate("(y) => window.scrollTo(0, y)", y)
            page.wait_for_timeout(120)
        page.evaluate("() => window.scrollTo(0, document.documentElement.scrollHeight)")
        page.wait_for_timeout(settle_ms)
        page.add_style_tag(content=FINAL_STATE_CSS)
        page.wait_for_timeout(400)

        info = page.evaluate(
            """() => ({
                url: location.href,
                title: document.title,
                scrollHeight: document.documentElement.scrollHeight,
                imageCount: document.images.length,
                loadedImages: Array.from(document.images)
                  .filter((img) => img.complete && img.naturalWidth > 0).length
              })"""
        )

        # Scroll-lock guard. Under --dismiss the probe showed dismissal releases the lock for
        # free; we run the forced reset only as a fallback and flag `scroll_locked` if both
        # paths fail. Without --dismiss we only detect and warn — unchanged from today.
        if do_dismiss:
            scroll_locked = not release_scroll_lock(page)
        else:
            scroll_locked = reachable_top(page) > 100
        if scroll_locked:
            print(
                f"WARNING [{url}]: scrollTo(0,0) won't reach the top — page scroll looks locked "
                "(modal/overlay?). tile-00 will NOT be the page top and the tiles will be mislabeled. "
                "QA this page before mining; re-run with --dismiss or exclude the page.",
                file=sys.stderr,
            )

        tiles: list[dict] = []
        for index, y in enumerate(tile_offsets(info["scrollHeight"], height, overlap)):
            actual_y = page.evaluate("(y) => { window.scrollTo(0, y); return window.scrollY; }", y)
            page.wait_for_timeout(settle_ms)
            name = f"tile-{index:02d}-y{round(actual_y):05d}.png"
            page.screenshot(path=str(out_dir / name), full_page=False, type="png")
            tiles.append({"index": index, "y": round(actual_y), "file": name})

        browser.close()

    manifest = {
        "url": url,
        "source": "shoot",  # Tier-B browser re-render (vs tile.py's cached crop)
        "viewport": {"width": width, "height": height},
        "overlap": overlap,
        "dismissed": do_dismiss,  # --dismiss ran affordance-only overlay dismissal
        "scroll_locked": scroll_locked,  # tile-00 ≠ top when true → tiles mislabeled, QA before mining
        "page": info,
        "tiles": tiles,
    }
    with open(out_dir / "manifest.json", "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Tier-B browser re-render → native-resolution tiles.")
    parser.add_argument("url")
    parser.add_argument("--out-dir", required=True, help="tile dir, e.g. store/<slug>/captures/<date>/tiles/<page>")
    parser.add_argument("--width", type=int, default=1920)
    parser.add_argument("--height", type=int, default=1400)
    parser.add_argument("--overlap", type=int, default=180)
    parser.add_argument("--settle-ms", type=int, default=1600)
    parser.add_argument("--chrome", default=DEFAULT_CHROME)
    parser.add_argument(
        "--dismiss", action="store_true",
        help="affordance-only overlay dismissal (Escape + the page's own dismiss buttons)",
    )
    args = parser.parse_args()

    # Tier-B's one footgun: launched from the iCloud project dir, a getcwd() deep in Chrome/Playwright
    # can hit a path the harness sandbox doesn't allow — which once tempted a sandbox-disable that
    # bricked a whole run. Resolve --out-dir while the launch cwd is still valid, then move cwd to a
    # neutral temp dir so getcwd() always succeeds. The skill passes --out-dir absolute, so the
    # cwd-dependent branch below never fires in normal use.
    out_dir = Path(args.out_dir)
    if not out_dir.is_absolute():
        out_dir = Path.cwd() / out_dir
    os.chdir(tempfile.gettempdir())

    manifest = capture(
        args.url, out_dir, args.width, args.height,
        args.overlap, args.settle_ms, args.chrome, args.dismiss,
    )
    page = manifest["page"]
    print(json.dumps({
        "outDir": str(out_dir),
        "loaded": f"{page['loadedImages']}/{page['imageCount']}",
        "scrollHeight": page["scrollHeight"],
        "tiles": len(manifest["tiles"]),
        "dismissed": manifest["dismissed"],
        "scrollLocked": manifest["scroll_locked"],
        "title": page["title"],
    }, indent=2))


if __name__ == "__main__":
    main()
