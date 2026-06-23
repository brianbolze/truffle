#!/usr/bin/env python3
"""Capture a page as deterministic viewport tiles with local Chrome.

This is a workaround for pages whose media renders correctly in a real browser
viewport but fails in Firecrawl or browser full-page screenshots.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


DEFAULT_CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def positions_for(scroll_height: int, viewport_height: int, overlap: int) -> list[int]:
    step = viewport_height - overlap
    positions: list[int] = []
    y = 0
    last_y = max(0, scroll_height - viewport_height)
    while y < last_y:
        positions.append(y)
        y += step
    if not positions or positions[-1] != last_y:
        positions.append(last_y)
    return positions


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--chrome", default=DEFAULT_CHROME)
    parser.add_argument("--width", type=int, default=1920)
    parser.add_argument("--height", type=int, default=1400)
    parser.add_argument("--overlap", type=int, default=180)
    parser.add_argument("--wait-ms", type=int, default=650)
    parser.add_argument("--headed", action="store_true")
    parser.add_argument("--unstick-header", action="store_true")
    parser.add_argument("--hide-chat", action="store_true")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=args.chrome,
            headless=not args.headed,
            args=["--autoplay-policy=no-user-gesture-required"],
        )
        context = browser.new_context(
            viewport={"width": args.width, "height": args.height},
            device_scale_factor=1,
            locale="en-US",
        )
        page = context.new_page()
        page.goto(args.url, wait_until="domcontentloaded", timeout=60000)
        try:
            page.wait_for_load_state("networkidle", timeout=30000)
        except PlaywrightTimeoutError:
            pass
        page.wait_for_timeout(3000)

        try:
            page.get_by_text("I understand", exact=True).click(timeout=3000)
            page.wait_for_timeout(500)
        except PlaywrightTimeoutError:
            pass

        if args.unstick_header:
            page.add_style_tag(
                content="""
                header, [class*="nav"], [class*="Nav"], [class*="header"], [class*="Header"] {
                  position: static !important;
                  top: auto !important;
                }
                """
            )

        if args.hide_chat:
            page.add_style_tag(
                content="""
                [class*="intercom"], iframe[src*="intercom"], [aria-label*="chat" i],
                [class*="chat"], [class*="Chat"] {
                  display: none !important;
                  visibility: hidden !important;
                }
                """
            )

        first_height = page.evaluate("document.documentElement.scrollHeight")
        for y in range(0, first_height, args.height):
            page.evaluate("(y) => window.scrollTo(0, y)", y)
            page.wait_for_timeout(250)

        page_info = page.evaluate(
            """() => ({
                url: location.href,
                title: document.title,
                width: innerWidth,
                height: innerHeight,
                scrollHeight: document.documentElement.scrollHeight,
                imageCount: document.images.length,
                loadedImages: Array.from(document.images)
                  .filter((img) => img.complete && img.naturalWidth > 0).length,
                badImages: Array.from(document.images)
                  .filter((img) => !img.complete || img.naturalWidth === 0)
                  .map((img) => img.currentSrc || img.src)
              })"""
        )

        captures = []
        for index, y in enumerate(
            positions_for(page_info["scrollHeight"], args.height, args.overlap)
        ):
            actual_y = page.evaluate("(y) => { window.scrollTo(0, y); return scrollY; }", y)
            page.wait_for_timeout(args.wait_ms)
            name = f"tile-{index:02d}-y{round(actual_y):05d}.png"
            page.screenshot(path=str(out_dir / name), full_page=False, type="png")
            captures.append({"index": index, "requestedY": y, "actualY": actual_y, "file": name})

        manifest = {
            "url": args.url,
            "viewport": {"width": args.width, "height": args.height},
            "overlap": args.overlap,
            "page": page_info,
            "captures": captures,
        }
        (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
        browser.close()

    print(json.dumps({"outDir": str(out_dir), **manifest}, indent=2))


if __name__ == "__main__":
    main()
