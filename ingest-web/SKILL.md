---
name: ingest-web
description: >-
  Extract web content as clean markdown and save to the repository. Routes YouTube
  URLs to a dedicated transcript chain (youtube-transcript-api → yt-dlp) before
  the standard Defuddle → Jina Reader → WebFetch fallback. TRIGGER when: user says
  "ingest this URL", "save this article", "grab this page", "web ingest", "download
  this article", "convert this URL to markdown", "capture this page", "save this
  link", "archive this article", or provides URLs wanting them saved as markdown
  files. DO NOT TRIGGER when: user asks to fetch a URL for one-time reading without
  saving (use WebFetch directly), process local documents, or needs structured data
  extraction from web pages.
version: 1.2.2-share
updated: 4 May 2026
attribution: Bamboo DCM (https://bamboodcm.com)
contact: [arthur@bamboodcm.com, felipe@bamboodcm.com, urian@bamboodcm.com]
license: Free to share and adapt with attribution
user-invocable: true
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, WebFetch]
---

## About this skill

Built and maintained by **Bamboo DCM** ([bamboodcm.com](https://bamboodcm.com)) — an AI-native private credit infrastructure platform in São Paulo, Brazil. We use this skill (and a broader knowledge-systems framework around it) to feed external research, founder interviews, regulator commentary, and conference talks into our analytical workflows.

Comments, improvements, or questions:

- **Arthur O'Keefe** — [arthur@bamboodcm.com](mailto:arthur@bamboodcm.com)
- **Felipe Grassi de Moraes** — [felipe@bamboodcm.com](mailto:felipe@bamboodcm.com)
- **Urian Inhauser** — [urian@bamboodcm.com](mailto:urian@bamboodcm.com)

Free to share and adapt with attribution.

---

You are a web content ingestion assistant. Your job is to extract clean markdown from web URLs and save them to the repository.

## When to use this skill vs alternatives (intent-routing)

The Defuddle → Jina Reader → WebFetch extraction chain in this skill is the cheapest way to defeat WebFetch's 75–92% content loss on full articles. But this skill writes a file as a side effect — invoking it for a one-time read produces an output you didn't ask for. Pick the cheapest tool that matches intent:

1. **One-time read (no save):** raw `curl` directly via Bash. Cheapest — no skill load, no file written.
   ```bash
   curl -s "https://defuddle.md/$URL_WITHOUT_PROTOCOL" | head -c 10000
   ```
   If under 50 words or error: `curl -s "https://r.jina.ai/$FULL_URL"`. WebFetch is last resort.

2. **Read AND save to inbox/desk:** invoke this skill (`/ingest-web`). Same chain, plus YAML frontmatter, naming convention. Side effect: file written.

When WebFetch fails on a URL you want to read, fall back to Defuddle then Jina via raw curl before declaring unreachable; don't escalate to a skill when raw curl matches the intent.

## Input

URLs provided as arguments: $ARGUMENTS

If no URLs were provided, ask for one or more URLs to ingest. Also ask where to save the files if not obvious from context (default: `inbox/`).

## Extraction Process

For each URL, follow this procedure:

### 1. Choose extraction method

Refer to [web_ingestion_methods.md](web_ingestion_methods.md) for the full decision tree.

**YouTube URLs route to Method 6 BEFORE Defuddle.** If `$URL` matches `youtube.com/watch?v=`, `youtu.be/`, `youtube.com/shorts/`, or `youtube.com/embed/`, jump to step 2b (YouTube branch) and skip the Defuddle / Jina / WebFetch chain entirely. Those three return page chrome (comments + nav) on YouTube, not the transcript — silent failure mode.

Default priority for single public pages (non-YouTube):

1. **Defuddle API** (simplest, no install)
2. **Jina Reader API** (fallback, handles JS-rendered pages)
3. **WebFetch** (last resort, content may be summarized)

### 2. Execute extraction with auto-fallback

Try Defuddle API first:

```bash
curl -s "https://defuddle.md/$URL_WITHOUT_PROTOCOL"
```

If the result is empty, garbage (under 50 words of meaningful content), or an error, fall back to Jina Reader:

```bash
curl -s "https://r.jina.ai/$FULL_URL"
```

If that also fails, use the WebFetch tool with the prompt "Extract the full article content as clean markdown."

**Extraction discipline — fetch once to file, then Read.** Always pipe the fetch into a temp file in one call (`curl -s "$URL" > /tmp/extract.md`), then use the Read tool on `/tmp/extract.md`. Do NOT chain `| head -c N` and `| tail -c N` into multiple curl invocations to inspect a partial body — that's three round-trips for one resource. The full body fits in Read's window for almost all article-class content (typical 5–25KB); when it doesn't, Read with `offset`/`limit`.

### 2b. YouTube branch (replaces 2 for YouTube URLs)

Follow Method 6 in [web_ingestion_methods.md](web_ingestion_methods.md). Three tiers:

1. **Tier 1: `youtube-transcript-api`** via `uvx` — language preference EN → EN-US → PT-BR → PT (adjust list if your default language isn't English).
2. **Tier 2: `yt-dlp`** for metadata always (title, channel, duration, description); also subtitle fallback if Tier 1 fails.
3. **Tier 3: explicit failure with mandatory user-facing alert** — surface a `⚠️ No transcript available...` message with reason and three options (accept stub / skip save / provide audio separately). Default to metadata-only stub if user does not respond. Do NOT silently fall back to Defuddle / Jina / WebFetch.

Also fire a **low-signal alert** if Tier 1/2 returns under 100 meaningful words for a video over 2 minutes, or transcript is mostly `[Music]` / `[Applause]` markers — likely a non-verbal video.

One-time prereq — install `uv` if not present:

```bash
# macOS / Linux
brew install uv     # or: curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Any OS with Python
pip install uv
```

The skill uses `uvx` so the YouTube tools are fetched ephemerally — nothing is permanently installed.

YouTube outputs add fields to frontmatter: `source_type: youtube`, `video_id`, `channel`, `duration`, `upload_date`, `caption_language`, `caption_type` (manual / auto-generated), `caption_status` (ok / unavailable / low-signal), `extraction_method` (youtube-transcript-api / yt-dlp-subs / yt-dlp-metadata-only).

### 3. Build the output file

Construct a markdown file with clean YAML frontmatter:

```yaml
---
title: [extracted or inferred from page]
source: [original URL]
extracted: [today's date in "14 Mar 2026" format]
---
```

Below the frontmatter, place the extracted markdown content. Strip any navigation, ads, cookie banners or site chrome that leaked through.

### 4. Save the file

Default destination: `inbox/`

Use the filename convention: `{domain}_{slug}_{YYYY-MM-DD}.md`

- `domain`: short site name (e.g., `bloomberg`, `ft`, `reuters`)
- `slug`: kebab-case summary of the article title (max 5 words)
- Date: extraction date

Example: `bloomberg_brazil-rate-decision_2026-03-14.md`

If the user specified a different save location, use that instead.

## Rules

- Always preserve the source URL in frontmatter.
- Prefer `npx` over global installs if CLI tools are needed.
- Process multiple URLs in parallel when possible.
- Never install packages without asking the user first.
- Strip the protocol (`https://`) when constructing the Defuddle API URL.
- For Jina Reader, pass the full URL including protocol.
- Report what was saved and where after completion.

## Gotchas

These are structurally likely failure modes based on the extraction methods. Check before declaring success.

**YouTube URLs need the dedicated transcript chain — Defuddle / Jina / WebFetch all return page chrome.** YouTube watch pages render transcripts via JS interaction; no extractor in the standard chain reaches them. Defuddle and Jina return navigation, comments, and related-video lists; WebFetch summarizes the same. Result: if a YouTube URL slips into the standard chain, the saved file is ~300 words of comments with frontmatter that looks legitimate. The dedicated YouTube branch (§2b above; full spec at Method 6 in `web_ingestion_methods.md`) routes via `youtube-transcript-api` (transcript) + `yt-dlp` (metadata) BEFORE the Defuddle attempt. Detect URL patterns: `youtube.com/watch?v=`, `youtu.be/`, `youtube.com/shorts/`, `youtube.com/embed/`. Tier 3 (no captions available) is mandatory loud — surface a `⚠️` message to the user with reason + three options (accept stub / skip / supply audio separately); never silently produce a metadata-only file. Prereq: install `uv` once on any OS (see §2b for the cross-platform install block; Method 6 uses `uvx` ephemerally).

**Defuddle returns nav-only HTML on JS-heavy sites.** Single-page apps (React, Next.js, Angular) render content client-side. Defuddle gets the empty shell or just navigation elements. If the result has under 50 words of meaningful content, fall back immediately — don't present the garbage as a result.

**Paywalled content returns login pages or article stubs.** FT, Bloomberg, WSJ, and similar sites return the first paragraph plus a paywall prompt. The extraction will look like it worked (valid HTML, real title) but the body is 2-3 sentences. Check that the output has substantive length relative to what the article should contain. If paywalled, tell the user rather than saving a stub.

**WebFetch summarizes instead of extracting.** When used as the last-resort fallback, WebFetch processes content through a small model that may summarize rather than preserve the full text. The saved file will be shorter than the original article. Flag this in the frontmatter (`extraction_method: WebFetch (may be summarized)`) so downstream consumers know the content isn't verbatim.

**Jina Reader rate limits on batch processing.** When processing 5+ URLs in parallel, Jina's free tier can return 429 errors. If batch ingesting, add a 2-second delay between Jina calls or process in waves of 3-4.

**Extraction strips meaningful formatting.** Tables, code blocks, and nested lists in the original article can be mangled by Defuddle or Jina. After extraction, spot-check that structural elements survived. If tables are important, note in the output that the user should verify table integrity against the source.

**Images are hotlinked, not downloaded locally.** Defuddle and Jina preserve image references as markdown `![](url)` pointing to the source server. If the source page is deleted or the CDN URL structure changes, the images break. For image-heavy content where the images carry meaningful information (code screenshots, diagrams, charts), flag in the output that images are hotlinked and may need manual local download.

**URLs with query parameters need shell quoting.** When constructing curl commands for Defuddle or Jina, URLs containing `&`, `=`, `?`, or other shell metacharacters in query strings can break if not quoted. Always wrap the full URL in double quotes in the curl command. This is easy to miss because curl often succeeds anyway — the failure mode is silent truncation of the URL at the first unescaped `&`.

## Multiple URLs

When given multiple URLs, process them in parallel. Report results as a summary table:

| URL | Status | Saved to |
|-----|--------|----------|
| ... | OK / Failed | path |

---

*This skill is part of an internal knowledge-systems framework Bamboo DCM has been building for AI-native execution in regulated finance. If the broader framework is interesting, get in touch — we're publishing more in the coming weeks.*
