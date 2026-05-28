---
title: Web Ingestion Methods
companion-to: SKILL.md
attribution: Bamboo DCM (https://bamboodcm.com)
contact: [arthur@bamboodcm.com, felipe@bamboodcm.com, urian@bamboodcm.com]
license: Free to share and adapt with attribution
version: 1.3.0-share
updated: 19 May 2026
---

# Web Ingestion Methods

## About this skill

Built and maintained by **Bamboo DCM** ([bamboodcm.com](https://bamboodcm.com)) — an AI-native private credit infrastructure platform in São Paulo, Brazil. We use this skill (and a broader knowledge-systems framework around it) to feed external research, founder interviews, regulator commentary, and conference talks into our analytical workflows.

Comments, improvements, or questions:

- **Arthur O'Keefe** — [arthur@bamboodcm.com](mailto:arthur@bamboodcm.com)
- **Felipe Grassi de Moraes** — [felipe@bamboodcm.com](mailto:felipe@bamboodcm.com)
- **Urian Inhauser** — [urian@bamboodcm.com](mailto:urian@bamboodcm.com)

*Companion to `SKILL.md`. Either file can stand alone; both travel together by design.*

---

Reference for downloading and converting web content to markdown for ingestion into the knowledge base. Choose by situation, then follow the relevant method.

## Decision Tree

**YouTube video URL** → Method 6 below (youtube-transcript-api + yt-dlp). Defuddle / Jina / WebFetch ALL return page chrome on YouTube URLs — never use the standard chain on `youtube.com/watch?v=...` or `youtu.be/...`.
**Archive / feed URL** → Method 7 below (RSS extraction). Defuddle / Jina / WebFetch return menu chrome / post listings on archive URLs (`/archive`, `/feed`, `/rss`, Substack bare-domain) — same failure shape as YouTube.
**Single public page, quick grab** → Defuddle API or Jina Reader API
**Single page, need full control** → Defuddle CLI
**JS-heavy or SPA page** → Jina Reader API (runs headless Chrome)
**Already in a Claude Code session** → WebFetch tool
**Multi-page site crawl** → Crawl4AI
**Authenticated/private content** → Defuddle browser extension (Obsidian Web Clipper) or manual save + Defuddle CLI on local HTML
**Dead / 404 / paywalled URL** → try Archive.org Wayback snapshot before giving up (see "Source-layer fallbacks" below)
**arXiv paper** → use the `/html/{id}` endpoint directly (cleaner than abstract page)

## Method 1: Defuddle API

No install. Returns clean markdown with YAML frontmatter (title, author, published, domain, word count).

```bash
curl -s "https://defuddle.md/example.com/article" > output.md
```

Replace `example.com/article` with the target URL path. The API fetches, extracts main content and strips clutter.

**Best for:** quick single-page grabs of public content.
**Limitations:** no JS rendering, no authentication, server-side fetch only.

Source: https://defuddle.md/

## Method 2: Defuddle CLI

Local execution with more options. Install globally or use npx.

```bash
# Parse URL to markdown
npx defuddle parse https://example.com/article --markdown

# Output as JSON (includes all metadata)
npx defuddle parse https://example.com/article --json

# Save to file
npx defuddle parse https://example.com/article --markdown --output result.md

# Extract single property
npx defuddle parse https://example.com/article --property title

# Parse local HTML file
npx defuddle parse page.html --markdown
```

Key CLI flags: `--markdown` (`-m`), `--json` (`-j`), `--output <file>` (`-o`), `--property <name>` (`-p`), `--debug`.

**Programmatic (Node.js):**

```javascript
import { Defuddle } from 'defuddle/node';
import { parseHTML } from 'linkedom';

const html = await fetch('https://example.com/article').then(r => r.text());
const { document } = parseHTML(html);
const result = await Defuddle(document, 'https://example.com/article', { markdown: true });
// result.content, result.title, result.author, result.published, etc.
```

Configuration options worth knowing: `contentSelector` (CSS selector to force main content area), `removeImages: true` (strip all images), `separateMarkdown: true` (return both HTML and markdown).

**Best for:** batch processing, local HTML files, custom content selectors.

Source: https://defuddle.md/docs

## Method 3: Jina Reader API

Free, stable, handles JavaScript-rendered pages via headless Chrome.

```bash
# Basic -- prepend r.jina.ai/ to any URL
curl -s "https://r.jina.ai/https://example.com/article"

# Force markdown output (skip readability)
curl -s -H "x-respond-with: markdown" "https://r.jina.ai/https://example.com/article"

# Use ReaderLM-v2 model for higher quality
curl -s -H "x-respond-with: readerlm-v2" "https://r.jina.ai/https://example.com/article"
```

Response headers: `x-respond-with` accepts `markdown`, `html`, `text`, `screenshot`, `readerlm-v2`.

**Best for:** JS-heavy SPAs, pages that need browser rendering, quick one-liners.
**Limitations:** rate limits on free tier, content may be truncated on very long pages.

Source: https://jina.ai/reader/

## Method 4: Claude Code WebFetch (Built-in)

Already available in any Claude Code session. No setup.

The WebFetch tool fetches a URL, converts HTML to markdown, and processes it with a prompt. Useful when you need extraction + summarization in one step.

**Best for:** ad-hoc extraction during a working session, when you need AI processing on the content immediately.
**Limitations:** content may be summarized for very large pages, 15-minute cache, read-only.

## Method 5: Crawl4AI (Open-Source)

Python library built specifically for AI/LLM content extraction. Runs locally.

```bash
pip install crawl4ai

# Quick extract
crawl4ai https://example.com/article --output markdown
```

Supports async crawling, custom extraction strategies and LLM-optimized markdown output by default.

**Best for:** bulk ingestion pipelines, Python workflows, zero cost.

Source: https://github.com/unclecode/crawl4ai

## Method 6: YouTube transcript extraction

YouTube URLs route here BEFORE the Defuddle / Jina chain. Defuddle, Jina, and WebFetch all return page chrome (comments, navigation, related videos) instead of the actual transcript — silent failure. Do not fall back to them on YouTube URLs.

**URL detection.** Any URL matching `youtube.com/watch?v=`, `youtu.be/`, `youtube.com/shorts/`, or `youtube.com/embed/` triggers this branch. Extract the 11-character video ID:

```bash
# Portable across macOS / Linux / Windows. The `sed -nE` equivalent fails on
# macOS BSD sed ("RE error: parentheses not balanced") because of how `\?` and
# alternation `|` interact inside `()` in `-E` mode.
VIDEO_ID=$(python3 -c "
import re, sys
m = re.search(r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/|youtube\.com/shorts/)([A-Za-z0-9_-]{11})', sys.argv[1])
print(m.group(1) if m else '')
" "$URL")
```

**One-time prerequisite.** `uv` must be installed. If `uv --version` (macOS/Linux/PowerShell) or `where uv` (Windows CMD) returns nothing, install it once:

```bash
# macOS / Linux
brew install uv     # or: curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Any OS with Python
pip install uv
```

The chain uses `uvx` so the YouTube tools are fetched ephemerally — nothing is permanently installed.

### Tier 1 — youtube-transcript-api (transcript)

```bash
uvx --quiet --from youtube-transcript-api python3 -c "
from youtube_transcript_api import YouTubeTranscriptApi
import sys, json
api = YouTubeTranscriptApi()
try:
    fetched = api.fetch(sys.argv[1], languages=['en','en-US','pt-BR','pt'])
    print(json.dumps({
        'language': fetched.language_code,
        'is_generated': fetched.is_generated,
        'text': ' '.join(s.text for s in fetched.snippets),
    }))
except Exception as e:
    print(json.dumps({'error': type(e).__name__, 'detail': str(e)}))
    sys.exit(1)
" "$VIDEO_ID"
```

Language preference: EN → EN-US → PT-BR → PT. If none match, the call falls back to the first available language; flag in frontmatter.

Output fields used downstream:
- `language` → `caption_language` frontmatter (`en`, `pt-BR`, etc.)
- `is_generated` → `caption_type` frontmatter (`auto-generated` if true, else `manual`)
- `text` → body of the markdown file

### Tier 2 — yt-dlp (metadata always; transcript fallback)

Always run yt-dlp for metadata regardless of Tier 1 result — it gives title, channel, duration, upload date, description:

```bash
uvx --quiet yt-dlp --skip-download \
  --print "%(title)s	%(channel)s	%(duration_string)s	%(upload_date)s" \
  --print "DESC:%(description)s" \
  "$URL" 2>/dev/null
```

If Tier 1 fails (NoTranscriptFound, TranscriptsDisabled, RequestBlocked, etc.), use yt-dlp's subtitle download as backup transcript source:

```bash
uvx --quiet yt-dlp --skip-download \
  --write-auto-sub --sub-lang "en,en-US,pt-BR,pt" --convert-subs vtt \
  -o "/tmp/%(id)s" "$URL" 2>/dev/null
# Strip VTT headers/timestamps to plain text:
for lang in en en-US pt-BR pt; do
  if [ -f "/tmp/${VIDEO_ID}.${lang}.vtt" ]; then
    sed -E '/^WEBVTT/d; /^[0-9]+$/d; /-->/d; /^$/d; s/<[^>]+>//g' "/tmp/${VIDEO_ID}.${lang}.vtt"
    break
  fi
done
```

If both Tier 1 and Tier 2 produce no transcript text, fall through to Tier 3.

### Tier 3 — explicit failure with user-facing alert (mandatory)

If no transcript is available (captions disabled, region-locked, music-only video, etc.), do NOT fall back to Defuddle / Jina / WebFetch — those return page chrome that looks legitimate but isn't.

**Surface a visible warning to the user before proceeding.** Do not silently produce a stub. Format:

```
⚠️ No transcript available for "[video title]" ([channel], [duration]).
   Reason: [TranscriptsDisabled | NoTranscriptFound | RequestBlocked | other]
   Saving metadata-only stub. Options:
     (a) accept stub
     (b) skip save
     (c) provide audio transcription separately (e.g. via /ingest with a downloaded audio file)
```

Default to (a) if the user does not respond — save a metadata-only stub (yt-dlp description + title + channel + duration), with frontmatter `caption_status: unavailable` and `extraction_method: yt-dlp metadata only`. The skill must NOT silently continue as if extraction succeeded.

For `/assess-link`: render verdict as **tentative** explicitly — the description is ~5% of content and the verdict cannot stand on it alone. Mark in the verdict header.

### Low-signal detection (between Tier 1/2 and Tier 3)

If Tier 1 or Tier 2 returns a transcript but it's mostly silence-markers (`[Music]`, `[Applause]`, `[Laughter]`) or under 100 meaningful words for a video over 2 minutes, treat as low-signal and surface:

```
⚠️ Transcript captured but content is sparse (~[N] words for [duration] video).
   Likely a music video, vlog without speech, or non-verbal content.
   Save anyway? (y/n)
```

### Frontmatter additions for YouTube outputs

```yaml
source_type: youtube
video_id: dQw4w9WgXcQ
channel: Rick Astley
duration: 3:33
upload_date: 2009-10-25
caption_language: en              # absent if Tier 3
caption_type: manual              # or auto-generated; absent if Tier 3
caption_status: ok                # or unavailable, low-signal
extraction_method: youtube-transcript-api  # or yt-dlp-subs, yt-dlp-metadata-only
```

### Gotchas

**Rate limiting on batch.** YouTube throttles after ~100 calls/min. For batch ingestion of 5+ YouTube URLs, add a 2s delay between calls.

**Auto-generated captions carry ASR artifacts; manual cleanup at extraction time is required before downstream citation.** Manual captions are reliable. Auto-generated tracks have proper-noun and technical-term mishearings that propagate as nonsense quotes if downstream consumers (content production, citation, briefing) trust the file. Validated 4 May 2026 on a 10-min EN talk: clean speaker audio still produced "DM's" → DeepMind, "Steve Jay" → Steve Yegge, "anch manager" → line manager, "DRRI" → DRI, "highle plans" → high-level plans, "in orchards" → in your codebase — i.e. the proper nouns and technical terms a downstream brief would actually quote. Strengthened 5 May 2026 at scale on a 1h28m podcast (18,137 words): 13+ proper-noun mishearings caught (Thoma Bravo / Manus / Netskope / Wrexham / oligopoly / CoreWeave / Trainium / Marketo / Salesloft / agentic / Aentic). PT-BR auto-generated captions on casual / informal content (founder interviews, podcasts) degrade further. **At extraction time**, when `caption_type: auto-generated`, do a manual artifact-cleanup pass before saving — re-listen to suspect proper-noun stretches against the source video, replace mishearings with their intended forms, and note the cleanup in the transcript-section preamble so downstream readers know it happened. The consumer reads the file, not the metadata.

**Long lecture transcripts may exceed downstream Read-tool token limits.** A 60–90+ minute talk produces 15–25k words. youtube-transcript-api returns the body as a single text blob (sentences space-joined), and Claude Code's Read tool has a ~25K-token limit per call — line-based pagination via `limit` does not subdivide a one-line blob usefully. **Pre-format at extraction time** when transcript exceeds ~12K words (or video duration > 30 min): split on sentence-ending punctuation (`. ! ?`) and group into ~4-sentence paragraphs in Python before saving. The body becomes paginatable by line / offset; downstream consumers can read it incrementally without scrambling. The frontmatter `duration` lets downstream skills budget accordingly. Validated 5 May 2026 on a 1h28m 20VC podcast (18,137 words, 95KB) — initial Read calls failed with "29754 tokens > 25000 limit" until paragraph-formatting was applied.

**YouTube `timedtext` IP-class block — STOP and surface; do NOT exhaust the fallback chain on the same IP.** Cloud-IP ranges (AWS / GCP / Azure) are blocked by default; **residential IPs are NOT immune** after sustained scraper-class load. Symptoms vary by tier: `youtube-transcript-api` returns silent `no-captions` even when captions exist; `yt-dlp --write-auto-subs` returns HTTP 429 on first attempt with no prior request volume; OR `yt-dlp` returns `"Video unavailable. This video is restricted. Please check the Google Workspace administrator and/or the network administrator restrictions."` with no prior load (broader-scope variant — blocks `--list-subs` too). **Diagnostic when captions appear present:** `yt-dlp --list-subs {video_id}` showing `en` / `en-orig` available + simultaneous failure on `--write-auto-subs` confirms IP-class block at the `timedtext` subtitle endpoint (caption availability OK; subtitle-fetch endpoint blocked for this IP). When `--list-subs` itself fails with "Video unavailable. This video is restricted," same root cause at broader scope. **Do NOT exhaust the fallback chain on the same IP** — multiple player clients × subtitle formats × cookies × throttling all hit the same blocked endpoint and will all fail. **Recovery:** cross-machine workflow — fetch from a different residential IP (different ISP if possible). Empirical pattern: one residential IP blocked across 3 sequential extraction methods × 6 player clients × 4 subtitle formats × cookies × throttling; same workload on a different residential ISP IP captured all 12 transcripts first-try. Same diagnostic pattern likely applies to other scraper-class workloads against X / LinkedIn / Bloomberg / WSJ / CAPTCHA-fronted sites.

**yt-dlp JS-runtime warning is non-fatal for transcripts/metadata.** yt-dlp warns about needing a JS runtime (deno) for some video formats. The warning is harmless for the transcript + metadata paths used here. Install deno only if you want to silence it (not required) — `brew install deno` (macOS/Linux), `winget install DenoLand.Deno` (Windows), or per the [official deno docs](https://deno.com/).

**Music videos, vlogs without substantive speech, shorts <60s.** Often produce useful-sounding metadata but empty / silence-marker transcripts. The low-signal alert (above) catches this. Don't pretend a `[Music]`-only transcript is content.

## Method 7: RSS archive extraction (archive-shape URLs)

Archive pages — `*.substack.com/archive`, blog indexes, bare domains — defeat the Defuddle → Jina → WebFetch chain the same way YouTube does. Defuddle on `diegocbarreto.substack.com/archive` (16 May 2026) returned 210 words of post listings (titles + dates, no article body); Jina degrades similarly; WebFetch returns chrome. Same silent-failure shape as YouTube; needs a dedicated branch.

**URL detection.** Any URL matching one of these triggers Method 7:
- Path contains `/archive`, `/feed`, `/rss`, `/atom`, `/atom.xml`, `/posts/`, `/all`.
- Bare domain with no article path: `https://example.substack.com/`, `https://example.com/`.
- Substack URL with no `/p/{slug}`: `*.substack.com` or `*.substack.com/archive`.

**Behavioral fallback** (when URL pattern doesn't match but extraction returns archive shape): if Defuddle returns under 300 words AND the body contains multiple post-title markers (multiple `<title>` tags or repeated `/p/{slug}` links to same domain), retry as Method 7.

### Tier 1 — RSS feed fetch + parse

```bash
# Construct feed URL — for Substack, replace any path with /feed
URL_INPUT="$URL"
base=$(echo "$URL_INPUT" | sed -E 's|(https?://[^/]+).*|\1|')

# Try /feed, /rss, /atom.xml, /feed/ in order — stop at first 200 with valid feed markup
feed_url=""
for candidate in "${base}/feed" "${base}/rss" "${base}/atom.xml" "${base}/feed/"; do
  http_code=$(curl -s -o /tmp/archive_feed.xml -w "%{http_code}" "$candidate")
  if [ "$http_code" = "200" ] && grep -q "<rss\|<feed" /tmp/archive_feed.xml; then
    feed_url="$candidate"
    break
  fi
done

# Parse RSS or Atom with Python
python3 << 'PYEOF'
import re, json
with open('/tmp/archive_feed.xml') as f:
    content = f.read()

is_atom = '<feed' in content[:500] and 'xmlns="http://www.w3.org/2005/Atom"' in content[:500]
item_tag, date_tag = ('entry', 'published') if is_atom else ('item', 'pubDate')

items = re.findall(rf'<{item_tag}>(.*?)</{item_tag}>', content, re.DOTALL)
out = []
for item in items:
    title_m = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', item, re.DOTALL)
    date_m = re.search(rf'<{date_tag}>(.*?)</{date_tag}>', item)
    link_m = re.search(r'<link>(.*?)</link>', item) or re.search(r'<link[^/>]*href="([^"]+)"', item)
    content_m = (re.search(r'<content:encoded>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</content:encoded>', item, re.DOTALL)
                 or re.search(r'<content[^>]*>(.*?)</content>', item, re.DOTALL))
    body_words = len(re.sub(r'<[^>]+>', ' ', content_m.group(1)).split()) if content_m else 0
    out.append({
        'title': (title_m.group(1) if title_m else '').strip(),
        'date': (date_m.group(1) if date_m else '')[:16],
        'link': link_m.group(1) if link_m else '',
        'words': body_words,
    })

with open('/tmp/archive_items.json', 'w') as f:
    json.dump(out, f, indent=2)
print(f"Parsed {len(out)} items ({'Atom' if is_atom else 'RSS'} feed)")
PYEOF
```

Output: per-item title, publication date, article URL, body word count. Saved to `/tmp/archive_items.json` for downstream consumption.

### Tier 2 — fallback to scraping the archive HTML

If no feed URL returns 200 with valid feed markup, fall back to scraping the archive page HTML via Defuddle and parsing the post-listing structure. Substack archive pages render post titles as `<a>` tags with `/p/{slug}` paths. Extract these via regex. Less reliable than RSS — only use as fallback.

### Tier 3 — explicit failure with user-facing alert

If neither RSS nor HTML scraping yields items, surface to user:

```
⚠️ Archive enumeration failed for {URL}.
   Reason: no RSS feed at /feed, /rss, /atom.xml; archive HTML did not match post-listing patterns.
   Options:
     (a) provide individual article URLs separately
     (b) supply the feed URL explicitly if you know it
     (c) skip
```

### What gets saved (bulk-capture variant)

For `/ingest-web` invocations on an archive URL: by default, enumerate the feed and **ingest every item** as a separate markdown file in `inbox/` (or the user-specified destination). Each item goes through Methods 1-3 (Defuddle / Jina / WebFetch) on its individual article URL. The archive page itself is not saved.

If a per-invocation cap is supplied by the consuming workflow (e.g., an autonomous-loop cap), respect it as a maximum item count.

For relevance-assessment routing skills (where they exist): each enumerated item gets a verdict; only items the user picks get routed.

### Frontmatter additions for archive-sourced ingestions

```yaml
source_type: archive-rss
archive_url: https://example.substack.com/archive
feed_url: https://example.substack.com/feed
item_count: 4              # total items found in feed
item_position: 3           # this item's position in the feed (1-based, newest = 1)
```

### Gotchas

**Substack RSS is truncated to recent N items.** Substack RSS feeds default to ~20-25 most recent posts. For older archives (e.g., a Substack with 200+ posts), RSS misses everything older than the cutoff. Fall back to scraping the archive HTML pagination (Substack uses `/archive?sort=new&offset=N`) — but this is much more fragile. For one-time exhaustive ingestion, the Substack data export via account settings is the right tool, not this skill.

**Atom feeds (`<feed>` namespace) need different parse logic.** Most Substacks use RSS; many institutional blogs use Atom. The detection block in Tier 1 routes based on root tag (`<rss>` vs `<feed>`). Item tag is `<item>` in RSS, `<entry>` in Atom; date tag is `<pubDate>` in RSS, `<published>` in Atom. Link in Atom is `<link href="..."/>` (attribute), not text content like RSS.

**LinkedIn and X.com don't have public RSS.** Substacks, WordPresses, Ghost blogs, and most institutional research sites do. LinkedIn Pulse, X.com author feeds, Slack/Discord/proprietary platforms don't — these need different ingestion paths (manual paste, OAuth-authenticated scrape, etc.). For source-registry-style entries on these platforms, mark `Feed URL: —` (no feed available) rather than guessing.

**Substack `/feed` does not require authentication for free posts.** Paid-only posts in a Substack feed appear with title + description but the `<content:encoded>` block is empty or truncated. Body word count will be 0 or near-0 for paid-only posts — flag these in the candidate list so the user knows they can't be fully ingested without a subscription.

*Source: 16 May 2026 archive routing — Defuddle on a Substack archive URL returned 210 words of post listings (no article body); manual workaround was RSS fetch + Python parse. Codifying so future archive combs route deterministically. Sibling of Method 6 (YouTube transcript chain) — same failure shape at a different URL pattern.*

### Per-architecture extraction patterns (catalog)

Empirical catalog of per-architecture Jina-extraction primitives — captured 28 May 2026 after a multi-source archive enumeration sweep revealed that Jina's behavior varies wildly by site framework. **Tier 1 RSS routine (above) is still the default**; this catalog covers the cases where RSS is missing, capped, or hides the bulk of the archive. Save the re-discovery cost on novel sources by matching the publisher's stack to the entry below.

| Architecture | Working primitive (Jina) | Expected output shape |
|---|---|---|
| **Substack** | `curl -s "https://r.jina.ai/https://{subdomain}.substack.com/archive"` | 30-50 post links with titles + dates inline; one anchor per post; reverse-chrono. Homepage is sparser (returns image-only or 5-10 most-recent links). |
| **Squarespace** | `curl -s "https://r.jina.ai/https://{site}/{author}?format=rss"` | XML feed; **20-item cap** is hard structural limit per Squarespace platform spec — deeper archive requires HTML pagination on `/essays` or category pages. |
| **Hugo blog (static site)** | `curl -s "https://r.jina.ai/https://{site}/"` (homepage) | 100-200+ post links with date + title + abstract per post in single ~10K-line response. Often covers ~6-12 months of cadence in one fetch. RSS at `/index.xml` is typically capped to most-recent 10. |
| **Next.js publisher-style** | `curl -s "https://r.jina.ai/https://{site}/{section}"` | Full index in ~10 lines with all post titles + dates inline (one anchor per post; Featured + reverse-chrono). No RSS, no sitemap — Jina extracts the JSX-rendered DOM cleanly. |
| **Framer SPA** | `curl -s "https://r.jina.ai/https://{site}/{section}/"` | Article cards with title + author + abstract inline; sitemap at `/sitemap.xml` is the durable fallback for older archive (reverse-chrono URL list, no per-piece dates). |
| **NextJS-SPA (sitemap-fallback)** | `curl -s "https://r.jina.ai/https://{site}/library"` (or equivalent index page; `/posts/all` often 404s) | ~50 post links; sitemap.xml at `/sitemap.xml` is the structural enumeration source for deeper archive. Direct `/feed`, `/rss`, `/atom.xml` typically all 404. |
| **LinkedIn Pulse aggregator** | `curl -s "https://r.jina.ai/https://{corporate-domain}/rss"` (when corporate exposes one) | RSS feed; broad-topic aggregator across all author/employee Pulse content; **high dedup-heavy** — most items off-topic for narrow-domain consumption. |

**The two failure modes to defend against** (named here so future agents don't waste round-trips re-discovering them):

1. **Sparse-homepage trap.** Some Substack-class sites return only image/header chrome on the bare homepage; the `/archive` path is the actual enumeration surface. Test: if homepage Jina returns <500 words and you expect a real archive, switch to `/archive` before giving up.

2. **RSS-cap-hides-the-archive trap.** Substack default 20-item cap, Squarespace 20-item cap, Hugo `/index.xml` ~10-item cap. **The cap is invisible from the feed itself** — assuming "feed = archive" silently misses 90%+ of recent cadence on a high-frequency publisher. When in doubt, fetch the homepage / `/archive` path as the source of truth on archive completeness.

**Per-source documentation discipline.** When discovering a working primitive for a new source, document it inline on that source's row in your source registry per your project's access-mechanics-documentation convention. The catalog above is the pattern-class generalization; the registry row is the per-source application.

*Source: 28 May 2026 multi-source enumeration sweep — Jina primitive worked first-try on 5 of 8 publisher sources with the obvious path; required `/archive` retry on 2; required `/library` retry on 1. Per-architecture pattern catalog landed during a multi-session content-ingestion retrospective.*

## Source-layer fallbacks (when the URL itself is the problem)

If the live URL is dead, 404s, or is fully paywalled with no bypass:

- **Archive.org Wayback** — prepend `https://web.archive.org/web/*/` to the URL, or grab the latest snapshot: `curl -sL "https://web.archive.org/web/2026/https://target.com/article"`. Then run the normal Defuddle → Jina chain on the snapshot URL.
- **arXiv** — always prefer the HTML endpoint (`arxiv.org/html/{id}`) over the abstract page (`arxiv.org/abs/{id}`). The HTML version gives the full paper; the abstract page only gives the abstract.
- **GitHub** — for raw file content, use `raw.githubusercontent.com/user/repo/branch/path` directly. For gists, the raw endpoint works too.
- **Nitter mirrors** — for X/Twitter when the main site rate-limits or paywalls. Public instance list at `github.com/zedeus/nitter/wiki/Instances`.

These are source-routing changes, not parser swaps — they change *which URL you fetch*, not *how you parse it*.

## Publisher-class blockers (silent extraction failures)

Some publisher classes systematically defeat Defuddle → Jina → WebFetch with **no error code surfacing to the orchestrator** — the fetch returns "successfully" but the body is null / chrome / 30-word error page. Pre-flight at fetch-batch composition time matters more than recovery after the surprise.

- **CNBC, WSJ, FT, and similar large-publisher news sites** run Varnish / Cloudflare bot-detection that returns 503 Service Unavailable to BOTH Defuddle AND Jina. The extraction looks "available" but the body is null / 30-word error page. **Plan B at composition time:** identify corroborating coverage from extraction-friendly sources (Fortune, Reuters, Wired, Bloomberg articles often cover the same story); use that as the substrate-primary URL with the bot-blocked URL retained in registry as `corroborating_source_url` only. Validated 13 May 2026: a CNBC piece returned 503 via both Defuddle and Jina; recovered via Fortune coverage of the same story.

- **Marketing landing pages with PDF-gated reports** (agency-style report landings, consulting-firm research portals) return menu chrome only via Defuddle — a few hundred words of navigation links / year selectors / "Download the report" CTAs, no actual report content. **Plan B at composition time:** check for a companion Substack / blog narrative version (firm Substacks frequently publish the narrative essay same-day as the gated report; consulting-firm reports often have community-side narrative coverage from analysts who summarized them); the narrative substrate is often denser than the landing-page chrome. Validated 13 May 2026: a research-firm landing page returned 144 words of menu chrome via Defuddle; recovered via the same firm's companion Substack narrative at 566 words.

**First signal** that you've hit one of these: the word-count of the extraction is anomalously low (CNBC: ~30 words; marketing landing: ~140 words; vs. expected 1,500–4,000 words for a real article). Treat low word-count as the silent-failure indicator and check the body for either a Varnish/error response (publisher bot-block) or menu navigation only (landing page).

**Fire moment:** any parallel-fetch batch that includes URLs from CNBC / WSJ / FT / Reuters.com / Bloomberg.com or marketing landing pages with PDF-gated reports. Compose the batch with named-fallback URLs at composition time, not as recovery after the surprise.

## Workflow Integration

After extracting content, drop the resulting markdown file into `inbox/` and process per the `/inbox-triage` skill. For deal-related content, follow the `/deal-ingest` skill instead.

Suggested filename convention: `{domain}_{slug}_{YYYY-MM-DD}.md` (e.g., `bloomberg_brazil-rate-decision_2026-03-14.md`).

---

*This skill is part of an internal knowledge-systems framework Bamboo DCM has been building for AI-native execution in regulated finance. If the broader framework is interesting, get in touch — we're publishing more in the coming weeks.*
