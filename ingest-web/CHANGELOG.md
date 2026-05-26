---
skill: ingest-web
updated: 26 May 2026
---

# ingest-web — CHANGELOG

Public mirror of the `/ingest-web` skill. Pointer: [SKILL.md](SKILL.md) · [web_ingestion_methods.md](web_ingestion_methods.md).

Repo-wide notes live at [../CHANGELOG.md](../CHANGELOG.md); this file documents per-version delta narrative for the skill specifically.

---

## [1.5.1-share] — 25 May 2026

### Changed

- `web_ingestion_methods.md` Method 6 § Gotchas — replaces the outdated `Cloud-IP blocking does not apply at single-user volume on residential IPs` bullet with the full YouTube `timedtext` IP-class block gotcha. Diagnostic + cross-machine recovery. Symptoms vary by tier: `youtube-transcript-api` returns silent `no-captions` even when captions exist; `yt-dlp --write-auto-subs` returns HTTP 429 on first attempt with no prior request volume; OR `yt-dlp` returns "Video unavailable. This video is restricted. Please check the Google Workspace administrator and/or the network administrator restrictions." with no prior load (broader-scope variant — blocks `--list-subs` too).
- Diagnostic when captions appear present: `yt-dlp --list-subs {video_id}` showing `en`/`en-orig` available + simultaneous failure on `--write-auto-subs` confirms IP-class block at the `timedtext` subtitle endpoint (caption availability OK; subtitle-fetch endpoint blocked for this IP). Cloud-IP ranges (AWS/GCP/Azure) blocked by default; residential IPs NOT immune after sustained scraper-class load.
- **Do NOT exhaust the fallback chain on the same IP** — multiple player clients × subtitle formats × cookies × throttling all hit the same blocked endpoint and will all fail.
- **Recovery:** cross-machine workflow — fetch from a different residential IP (different ISP if possible). Empirical pattern: one residential IP blocked across 3 sequential extraction methods × 6 player clients × 4 subtitle formats × cookies × throttling; same workload on a different residential ISP IP captured all 12 transcripts first-try. Same diagnostic pattern likely applies to other scraper-class workloads against X / LinkedIn / Bloomberg / WSJ / CAPTCHA-fronted sites.

---

## [1.5.0-share] — 19 May 2026

### Added

- **Method 7: RSS archive extraction.** Archive-shape URLs (`*.substack.com/archive`, blog feeds, bare-domain post indexes) share the same silent-failure shape as YouTube on the Defuddle → Jina → WebFetch chain — Defuddle returns ~200 words of post listings, not article body. Method 7 detects archive-shape URLs (URL pattern OR Defuddle <300w + feed markers) and routes to a fetch-RSS-feed-and-parse branch (Python regex parsing for both RSS and Atom formats), with HTML scraping fallback, before Tier 3 explicit-failure surface.
- Bulk-capture variant: enumerate feed, save every item as separate markdown file in your inbox folder.
- Frontmatter additions on RSS-extracted items: `source_type: rss`, `feed_url`, `rss_pub_date`, `rss_guid`.
- **Publisher-class blockers** pre-flight discipline. CNBC / WSJ / FT / Reuters / Bloomberg.com return Varnish 503 silently to both Defuddle and Jina; marketing-landing pages with PDF-gated reports return menu chrome only. Recovery via corroborating-coverage routing at fetch-batch composition time rather than after-the-surprise. First-signal indicator: anomalously low word-count (~30 for bot-block; ~140 for chrome vs. 1500-4000 expected).
- URL-routing additions in both Decision Tree (`web_ingestion_methods.md`) and § Choose extraction method (`SKILL.md`) so archive-shape URLs route to Method 7 before the standard chain.

### Notes

- Net additions: ~120 lines covering Method 7 (URL detection / RSS feed parse via Python / fallback to HTML scraping / Tier 3 explicit-failure surface / bulk-capture variant / frontmatter additions / Substack RSS gotchas) + ~12 lines Publisher-class blockers (2 publisher classes with named-fallback recovery patterns + low-word-count silent-failure signal).
- Catch-up from public-share v1.4.1 (5 May 2026) to v1.5.0-share — 4 internal versions absorbed in one mirror sync (v1.4.2 added Publisher-class blockers; v1.5.0 added Method 7). All content generalizable — no internal-tool references, no proprietary paths.
- Landed via [library#1](https://github.com/bamboo-DCM/library/pull/1).

---

## [1.4.1-share] — 5 May 2026

### Added

- Method 6 cross-platform fix — replaces macOS-BSD-incompat sed video-ID extraction with portable `python3 -c` regex helper. The original `sed -nE` with `\?` + `|` inside `()` raises 'parentheses not balanced' on BSD sed (macOS default), making YouTube URL parsing silently fail outside GNU sed environments.

### Changed

- Strengthens 'Long lecture transcripts' gotcha with the Read-tool 25K-token limit and paragraph-format-at-extraction recommendation.
- Companion `web_ingestion_methods.md` bumped v1.2.3-share → v1.2.4-share.

### Notes

- Validated 5 May 2026 on a 1h28m podcast (18,137 words, 95KB → 29,754 tokens, exceeded 25K limit).

---

## [1.4.0-share] — 4 May 2026

### Added

- §5 "Report and summarize" — after each save, prints a 3–5 sentence executive summary of what the article argues. Suppressed in batch mode, parallel mode with ≥ 5 URLs, failed extractions, and YouTube Tier 3 metadata-only stubs.

### Changed

- 4 May 2026 audit-driven sweep folded in 4 gotchas previously workstation-only into the public mirror: paywalled-subscription-archive paired-local lookup, polished WebFetch 75-92%-loss block, Defuddle 403/Medium fallback discipline, X/Twitter multi-tweet thread chain-incomplete pattern.

---

## [1.2.3-share] — 4 May 2026

### Changed

- Strengthens the auto-generated caption gotcha in Method 6 § Gotchas — prior scope was PT-BR degradation only; now covers EN proper-noun and technical-term ASR artifacts (validated on a 10-min YC Startup School talk: "DM's"→DeepMind, "Steve Jay"→Steve Yegge, "anch manager"→line manager, "DRRI"→DRI, "highle plans"→high-level plans, "in orchards"→in your codebase) and recommends a manual cleanup pass at extraction time when `caption_type: auto-generated`.

---

## [1.3.0-share] — 3 May 2026

### Added

- YouTube transcript chain — Method 6 in `web_ingestion_methods.md` (youtube-transcript-api → yt-dlp metadata + subtitle fallback → explicit Tier 3 alert with `⚠️` chat-visible message + three options). YouTube URLs route BEFORE Defuddle/Jina/WebFetch (which return only page chrome).
- Frontmatter additions: `source_type: youtube`, `video_id`, `channel`, `duration`, `caption_language`, `caption_type`, `caption_status`, `extraction_method`.
- One-time prereq: `brew install uv` (cross-platform variants per v1.3.1+; see install instructions in the repo README for Windows / Linux equivalents).

---

## [1.2.1-share] — 4 May 2026

### Added

- Initial public release. Skill packages clean web content extraction (Defuddle primary → Jina Reader fallback → WebFetch fallback) into a single trigger-on-URL workflow with markdown save + frontmatter convention. CC-BY 4.0 license.
