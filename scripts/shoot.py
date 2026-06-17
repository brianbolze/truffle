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
import subprocess
import sys
import tempfile
from pathlib import Path

from playwright.sync_api import Page, sync_playwright
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

# System Chrome (not Playwright's bundled Chromium) — it ships real GPU/WebGL, which is the
# whole point: it renders the marketing media Firecrawl's browser can't.
DEFAULT_CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Matches tile.py — the recipe-time `magick` shell-out resizes a full-page PNG to this width.
OVERVIEW_WIDTH = 480

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
    "reject all, except strictly necessary", "reject all except strictly necessary",
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

# Max viewport-coverage of any non-nav fixed/sticky element — the footprint an overlay occupies.
# Measured before and after dismiss so a no-op dismissal (footprint didn't shrink) fails loud
# instead of silently emitting tiles that still carry the overlay. The silent miss this catches:
# goodlifemeds' Transcend CMP behind a *closed shadow root* — unreachable by the affordance
# finder's querySelectorAll, so --dismiss was a verified no-op yet reported dismissed=true with no
# warning (2026-06-16 dogfood). Same overlay scope as FIND_DISMISS_TARGETS: a top-pinned
# full-width short strip is nav, not an overlay.
OVERLAY_COVERAGE = """
() => {
  const vw = innerWidth, vh = innerHeight, area = vw*vh;
  let max = 0;
  for (const el of document.querySelectorAll('body *')) {
    const cs = getComputedStyle(el);
    if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
    if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) continue;
    const r = el.getBoundingClientRect();
    const cover = (Math.max(0, Math.min(r.right,vw)-Math.max(r.left,0)) *
                   Math.max(0, Math.min(r.bottom,vh)-Math.max(r.top,0)))/area;
    if (cover < 0.02) continue;
    const shortNav = r.top <= 5 && r.width >= 0.6*vw && r.height <= 0.18*vh;
    if (shortNav) continue;
    if (cover > max) max = cover;
  }
  return max;
}
"""

FIND_OVERLAY_BOXES = """
() => {
  const vw = innerWidth, vh = innerHeight, area = vw*vh;
  const out = [];
  for (const el of document.querySelectorAll('body *')) {
    const cs = getComputedStyle(el);
    if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
    if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) continue;
    const r = el.getBoundingClientRect();
    const w = Math.max(0, Math.min(r.right,vw)-Math.max(r.left,0));
    const h = Math.max(0, Math.min(r.bottom,vh)-Math.max(r.top,0));
    const cover = (w*h)/area;
    if (cover < 0.04) continue;
    const shortNav = r.top <= 5 && r.width >= 0.6*vw && r.height <= 0.18*vh;
    if (shortNav) continue;
    out.push({left: Math.max(r.left,0), top: Math.max(r.top,0),
              right: Math.min(r.right,vw), bottom: Math.min(r.bottom,vh), cover});
  }
  return out.sort((a,b) => b.cover - a.cover);
}
"""

# Forced scroll-lock release: overflow/position/top reset on both html + body. alange-soehne
# (2026-06-16 dogfood) exercised this live and it FAILED to release — so it's a best-effort flag,
# not a fix: when it can't unlock, `scroll_locked` stays true and the page should fall back to
# cached / be excluded, never trusted. (The probe's 8 sites never had to fire it at all.)
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


def emit_overview(page: Page, out_dir: Path, url: str) -> bool:
    """Write `overview-480w.png` beside the tiles via a full-page screenshot + `magick -resize`.

    Mirrors tile.py's overview shape so the QA gate reads re-rendered pages the same way it
    reads cached ones — without this, Tier-B was blind-flying and the hand-rolled montage
    workaround once double-rendered a footer and manufactured a false defect (functionhealth
    retro). Warns + returns False on failure; never breaks the tile write.
    """
    dst = out_dir / "overview-480w.png"
    tmp_path: str | None = None
    try:
        page.evaluate("() => window.scrollTo(0, 0)")
        page.wait_for_timeout(300)
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            tmp_path = tmp.name
        page.screenshot(path=tmp_path, full_page=True, type="png")
        subprocess.check_call(
            ["magick", tmp_path, "-resize", f"{OVERVIEW_WIDTH}x", str(dst)],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError, OSError) as err:
        print(
            f"WARNING [{url}]: overview-480w emission failed ({err}) — QA falls back to "
            "tile spot-check on this page. Check that `magick` (ImageMagick) is on PATH.",
            file=sys.stderr,
        )
        return False
    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.unlink(tmp_path)


def reachable_top(page: Page) -> int:
    """The y the page actually lands on after scrollTo(0, 0) — a non-zero value means scroll is locked."""
    return page.evaluate("() => { window.scrollTo(0, 0); return window.scrollY; }")


def max_overlay_coverage(page: Page) -> float:
    """Largest viewport fraction covered by a non-nav fixed/sticky element (0.0 if none ≥ 2%)."""
    return page.evaluate(OVERLAY_COVERAGE)


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
    # Some CMPs render their buttons inside open Shadow DOM, where the structural JS finder
    # cannot see them but Playwright's text locators can. Keep this exact-text and dismiss-label
    # only; broad text clicking was the class of harm the Tier-B probe rejected.
    for label in DISMISS_LABELS:
        try:
            page.get_by_text(label, exact=True).first.click(timeout=800)
            page.wait_for_timeout(350)
            break
        except Exception:
            continue
    # Closed-shadow CMPs can expose only the host rectangle to DOM/locators. If a large overlay is
    # still present, click where a visible close affordance normally sits: top-right inside the box.
    # This is still scoped to overlay-shaped fixed/sticky elements, never arbitrary page chrome.
    for box in page.evaluate(FIND_OVERLAY_BOXES)[:2]:
        try:
            page.mouse.click(max(box["left"] + 8, box["right"] - 34), box["top"] + 34)
            page.wait_for_timeout(350)
        except Exception:
            continue
    page.keyboard.press("Escape")
    page.wait_for_timeout(150)


def release_scroll_lock(page: Page) -> bool:
    """Dismiss-then-reverify, with a forced overflow/position reset as fallback. True if the top is reachable.

    In the probe, dismissal released both locked sites' locks for free (bodyOverflow:
    hidden → visible the instant the overlay closed). The forced reset is *best-effort, not a
    fix*: alange-soehne (2026-06-16 dogfood) exercised it live and it failed to release. So a
    False return is a genuine "still locked" — the caller flags `scroll_locked` and the page
    should fall back to cached / be excluded, never trusted as correctly-tiled.
    """
    if reachable_top(page) <= 50:
        return True
    page.evaluate(RELEASE_SCROLL_LOCK)
    return reachable_top(page) <= 50


def capture(url: str, out_dir: Path, width: int, height: int, overlap: int,
            settle_ms: int, chrome: str, do_dismiss: bool,
            dismiss_points: list[tuple[float, float]]) -> dict:
    """Drive system Chrome to warm-scroll `url`, settle motion, then write viewport tiles to out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    # Clear our own prior artifacts so a re-render with different tile geometry can't leave orphans
    # (a taller Tier-B page writes tile-07-y07874 without overwriting a stale tile-07-y07546, seen on
    # ro-co). Scoped to the files shoot.py/tile.py own — never the whole dir, so a mis-passed
    # --out-dir can't nuke unrelated content.
    for stale in (*out_dir.glob("tile-*.png"), out_dir / "overview-480w.png"):
        stale.unlink(missing_ok=True)
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

        overlay_before = 0.0
        dismiss_cleared: bool | None = None
        if do_dismiss:
            overlay_before = max_overlay_coverage(page)
            dismiss(page)
            for x, y in dismiss_points:
                page.mouse.click(x, y)
                page.wait_for_timeout(350)

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

        # Thin-page / interstitial guard. A real marketing page is tall with many images; a bot-wall
        # challenge, login gate, or coming-soon splash is ~1 viewport with almost none. Structural,
        # no vendor strings — a Cloudflare challenge captured *as* the page on doordash www was the
        # silent miss this catches (2026-06-16 dogfood). Non-fatal: warn so QA excludes it.
        if info["scrollHeight"] < 2000 and info["imageCount"] < 3:
            print(
                f"WARNING [{url}]: page looks thin/interstitial (scrollHeight={info['scrollHeight']}px, "
                f"{info['imageCount']} images) — likely a bot-wall, login gate, or coming-soon splash, "
                "not the real page. Verify before mining; capture via a non-walled path or exclude.",
                file=sys.stderr,
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

        # No-op-dismiss guard. `dismissed` says --dismiss *ran*; this says whether it *worked*.
        # Measured as a footprint delta (relative, not an absolute px size) so a corner CMP below
        # any fixed threshold still trips it: a real dismissal shrinks or clears the overlay
        # (stripe's proactive bubble → small launcher; mydrhank's banner → gone), a no-op leaves it
        # unchanged (goodlifemeds' shadow-root CMP). Catches a re-arm during warm-scroll too.
        if do_dismiss:
            overlay_after = max_overlay_coverage(page)
            dismiss_cleared = overlay_after < 0.02 or overlay_after <= 0.5 * overlay_before
            if not dismiss_cleared:
                print(
                    f"WARNING [{url}]: --dismiss did not clear the overlay — a fixed element still "
                    f"covers {overlay_after:.0%} of the viewport (was {overlay_before:.0%}). It may sit "
                    "behind a closed shadow root or use off-list button labels; the tiles still carry "
                    "it. Compare against the cached/faithful view and exclude or caveat this page.",
                    file=sys.stderr,
                )

        tiles: list[dict] = []
        for index, y in enumerate(tile_offsets(info["scrollHeight"], height, overlap)):
            actual_y = page.evaluate("(y) => { window.scrollTo(0, y); return window.scrollY; }", y)
            page.wait_for_timeout(settle_ms)
            name = f"tile-{index:02d}-y{round(actual_y):05d}.png"
            page.screenshot(path=str(out_dir / name), full_page=False, type="png")
            tiles.append({"index": index, "y": round(actual_y), "file": name})

        overview_made = emit_overview(page, out_dir, url)

        browser.close()

    manifest = {
        "url": url,
        "source": "shoot",  # Tier-B browser re-render (vs tile.py's cached crop)
        "viewport": {"width": width, "height": height},
        "overlap": overlap,
        "dismissed": do_dismiss,  # --dismiss ran affordance-only overlay dismissal
        "dismiss_cleared": dismiss_cleared,  # did it WORK (footprint dropped)? null when --dismiss didn't run
        "scroll_locked": scroll_locked,  # tile-00 ≠ top when true → tiles mislabeled, QA before mining
        "overview": "overview-480w.png" if overview_made else None,
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
    parser.add_argument(
        "--dismiss-point", action="append", default=[],
        help="extra viewport click as x,y after generic dismiss, for visible overlay close affordances",
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

    dismiss_points: list[tuple[float, float]] = []
    for raw in args.dismiss_point:
        try:
            x_raw, y_raw = raw.split(",", 1)
            dismiss_points.append((float(x_raw), float(y_raw)))
        except ValueError:
            parser.error(f"--dismiss-point must be x,y, got {raw!r}")

    manifest = capture(
        args.url, out_dir, args.width, args.height,
        args.overlap, args.settle_ms, args.chrome, args.dismiss, dismiss_points,
    )
    page = manifest["page"]
    print(json.dumps({
        "outDir": str(out_dir),
        "loaded": f"{page['loadedImages']}/{page['imageCount']}",
        "scrollHeight": page["scrollHeight"],
        "tiles": len(manifest["tiles"]),
        "dismissed": manifest["dismissed"],
        "dismissCleared": manifest["dismiss_cleared"],
        "scrollLocked": manifest["scroll_locked"],
        "title": page["title"],
    }, indent=2))


if __name__ == "__main__":
    main()
