#!/usr/bin/env python3
"""Image-aware standard-chain extraction for the web-ingestion skills.

Runs the public-article standard chain (Defuddle -> Jina Reader) and keeps the
image layer, then reports how many image references the extractor emitted and
how many survived to the saved body. WebFetch stays with the caller: it is a
model tool, not a shell command, and it is the last resort either way.

WHY THIS IS CODE AND NOT PROSE
------------------------------
Two rules used to live as advisory prose in the skill and did not fire in
practice. Both are fully specifiable, so they belong in the cheapest executor:

  1. Harvest-and-count. Count the ``![](url)`` refs the extractor handed back
     BEFORE anything is stripped, screen out page chrome, and report both
     numbers. A missing count and a genuine zero are indistinguishable on
     disk, so ``0`` is always a real answer that gets written down.

  2. Image-aware fall-through. Defuddle's image emission is site-dependent:
     measured 2 Aug 2026 on six pages, it returned 0 refs where Jina returned
     4, 8 and 26 on three of them, and matched Jina on the other three. A
     Defuddle result carrying zero images is therefore not evidence the page
     has none - it is a reason to ask the other extractor. Falling through on
     that signal costs one extra fetch and only on pages that would otherwise
     have been saved image-free.

The fall-through adopts the Jina body only when Jina actually emits images AND
its text is not materially shorter than Defuddle's, so a page is never traded
for an image-bearing stub.

Usage
-----
    extract_web.py URL [--out PATH] [--json] [--no-fallthrough]
    extract_web.py --from-file PATH [--json]      # count/screen an existing body

Writes the chosen body to --out (default ``/tmp/extract.md``, the path contract
both skills already read from) and prints a JSON report to stdout.

Env: ``JINA_API_KEY`` + ``JINA_HIGH_VOLUME`` authenticate the Jina leg (500 RPM)
exactly as the skill's chain does. Neither is required - keyless Jina is free
and ample for single-URL work.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

# Inline markdown image refs. Both Defuddle and Jina emit this form.
IMG_RE = re.compile(r'!\[(?P<alt>[^\]]*)\]\((?P<url>[^)\s]+)(?P<tail>[^)]*)\)')

# Conservative, high-confidence page chrome. Deliberately narrow: a false
# exclusion silently loses a body diagram, which is the defect this whole
# thing exists to fix, whereas a false inclusion just carries one extra ref.
# Every exclusion is reported with its reason so the screen stays auditable.
CHROME_PATTERNS: list[tuple[str, str]] = [
    (r'/1x1[./]|pixel\.(gif|png)|/beacon|/open\.gif|/track(ing)?[./]', 'tracking-pixel'),
    (r'avatar|gravatar|headshot|author[-_]photo|/profile[-_]?(pic|image)', 'avatar'),
    (r'favicon|/sprite|apple-touch-icon|/badge[s]?[/.]', 'icon'),
    (r'(^|[/_-])logo([/_.-]|$)|logotype', 'logo'),
    (r'social[-_]?(icon|share)|/share[-_]?(button|icon)', 'social-chrome'),
    # Explicit small renditions in the URL: w_64 / 24x24 / -48x48.
    (r'[/_,]w_\d{1,2}(?=[,/_.])|[/_-]\d{1,2}x\d{1,2}(?=[./_-]|$)', 'thumbnail-size'),
]
CHROME_RE = [(re.compile(p, re.I), reason) for p, reason in CHROME_PATTERNS]

UA = 'curl/8.7.1'  # urllib's default UA is 403'd where curl is accepted
CONTENT_FLOOR = 50  # words; the skill's existing "garbage" threshold


def words(text: str) -> int:
    return len(text.split())


def fetch(cmd: list[str], timeout: int = 90) -> str:
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return r.stdout or ''
    except Exception:  # noqa: BLE001 - a failed leg is a fall-through signal, not a crash
        return ''


def defuddle(url: str) -> str:
    no_proto = re.sub(r'^https?://', '', url)
    return fetch(['curl', '-sL', '-A', UA, '--max-time', '80',
                  f'https://defuddle.md/{no_proto}'])


def jina(url: str) -> str:
    auth: list[str] = []
    key = os.environ.get('JINA_API_KEY')
    if key and os.environ.get('JINA_HIGH_VOLUME'):
        auth = ['-H', f'Authorization: Bearer {key}']
    return fetch(['curl', '-sL', '-A', UA, '--max-time', '80', *auth,
                  f'https://r.jina.ai/{url}'])


def classify(url: str) -> str | None:
    """Return the chrome reason for an image URL, or None to keep it."""
    for rx, reason in CHROME_RE:
        if rx.search(url):
            return reason
    return None


def harvest(body: str) -> dict:
    """Count emitted refs, screen chrome, dedup, and return the kept body.

    ``emitted`` counts DISTINCT image URLs as handed back, before any strip.
    """
    seen: list[str] = []
    for m in IMG_RE.finditer(body):
        u = m.group('url')
        if u not in seen:
            seen.append(u)

    excluded: list[dict] = []
    kept: list[str] = []
    for u in seen:
        reason = classify(u)
        (excluded.append({'url': u, 'reason': reason}) if reason else kept.append(u))

    dropped = {e['url'] for e in excluded}

    def repl(m: re.Match) -> str:
        return '' if m.group('url') in dropped else m.group(0)

    out = IMG_RE.sub(repl, body)
    # Collapse blank lines left behind by a removed standalone image line.
    out = re.sub(r'\n{3,}', '\n\n', out)

    return {
        'images_emitted': len(seen),
        'images_persisted': len(kept),
        'kept': kept,
        'excluded': excluded,
        'body': out,
    }


def run_chain(url: str, allow_fallthrough: bool = True) -> dict:
    d_body = defuddle(url)
    d_words = words(d_body)
    d_h = harvest(d_body)

    thin = d_words < CONTENT_FLOOR
    image_blind = d_h['images_emitted'] == 0

    if not allow_fallthrough or not (thin or image_blind):
        return {
            'method': 'defuddle',
            'fallthrough': None,
            'words': d_words,
            **{k: d_h[k] for k in ('images_emitted', 'images_persisted', 'kept', 'excluded')},
            'body': d_h['body'],
        }

    reason = 'content-thin' if thin else 'image-zero'
    j_body = jina(url)
    j_words = words(j_body)
    j_h = harvest(j_body)

    if thin:
        # Pre-existing rule: Defuddle produced garbage, take Jina if it is better.
        adopt = j_words >= CONTENT_FLOOR
    else:
        # Image-aware rule: only trade bodies if Jina genuinely adds an image
        # layer and does not cost material text.
        adopt = j_h['images_emitted'] > 0 and j_words >= max(CONTENT_FLOOR, int(0.6 * d_words))

    if adopt:
        return {
            'method': f'jina ({reason} fall-through from defuddle)',
            'fallthrough': reason,
            'words': j_words,
            **{k: j_h[k] for k in ('images_emitted', 'images_persisted', 'kept', 'excluded')},
            'body': j_h['body'],
            'defuddle_images_emitted': d_h['images_emitted'],
            'defuddle_words': d_words,
        }

    return {
        'method': 'defuddle',
        'fallthrough': f'{reason} (attempted, not adopted)',
        'words': d_words,
        **{k: d_h[k] for k in ('images_emitted', 'images_persisted', 'kept', 'excluded')},
        'body': d_h['body'],
        'jina_images_emitted': j_h['images_emitted'],
        'jina_words': j_words,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('url', nargs='?', help='URL to extract')
    ap.add_argument('--from-file', help='count/screen an already-fetched body instead of fetching')
    ap.add_argument('--out', default='/tmp/extract.md', help='where to write the chosen body')
    ap.add_argument('--json', action='store_true', help='print only the JSON report')
    ap.add_argument('--no-fallthrough', action='store_true',
                    help='disable the image-aware fall-through (diagnostic use)')
    a = ap.parse_args()

    if a.from_file:
        with open(a.from_file, encoding='utf-8', errors='replace') as f:
            body = f.read()
        h = harvest(body)
        report = {
            'method': 'from-file',
            'source': a.from_file,
            'words': words(body),
            **{k: h[k] for k in ('images_emitted', 'images_persisted', 'kept', 'excluded')},
        }
    elif a.url:
        r = run_chain(a.url, allow_fallthrough=not a.no_fallthrough)
        body = r.pop('body')
        with open(a.out, 'w', encoding='utf-8') as f:
            f.write(body)
        report = {'source': a.url, 'out': a.out, **r}
    else:
        ap.error('give a URL or --from-file')
        return 2

    print(json.dumps(report, indent=2))
    if not a.json and report['images_emitted'] == 0:
        print('\n⚠️  images_emitted: 0 — the extractor returned no image layer for this page.\n'
              '   Write the 0 into frontmatter; if the page is figure-bearing, flag it in the body.',
              file=sys.stderr)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
