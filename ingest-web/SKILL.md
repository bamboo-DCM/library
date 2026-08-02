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
version: 1.9.0-share
updated: 19 May 2026
attribution: Bamboo DCM (https://bamboodcm.com)
contact: [arthur@bamboodcm.com, felipe@bamboodcm.com, urian@bamboodcm.com]
license: Free to share and adapt with attribution
user-invocable: true
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, WebFetch]
---

## About this skill

Built and maintained by **Bamboo DCM** ([bamboodcm.com](https://bamboodcm.com)) — the independent infrastructure for Brazil's corporate and structured credit market, with an intelligence layer on top. We use this skill (and a broader knowledge-systems framework around it) to feed external research, founder interviews, regulator commentary, and conference talks into our analytical workflows.

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

**Archive-shape URLs route to Method 7 BEFORE Defuddle.** If `$URL` matches archive patterns — path with `/archive`, `/feed`, `/rss`, `/atom`, `/atom.xml`, `/posts`, `/all`; bare domain with no article path (`https://example.substack.com/`, `https://example.com/`); or Substack URL with no `/p/{slug}` — jump to Method 7 (RSS archive extraction in [web_ingestion_methods.md](web_ingestion_methods.md)). The Defuddle / Jina / WebFetch chain returns ~200 words of post-listing chrome on archive URLs, not article content — same silent-failure shape as YouTube. Behavioral fallback: if Defuddle returns under 300 words with feed-shape markers (multiple `<title>` tags or repeated `/p/{slug}` links to same domain), retry as Method 7. For bulk-capture mode, Method 7 enumerates the feed and ingests every item as a separate markdown file.

Default priority for single public pages (non-YouTube, non-archive):

1. **Defuddle API** (simplest, no install)
2. **Jina Reader API** (fallback, handles JS-rendered pages)
3. **WebFetch** (last resort, content may be summarized)

### 2. Execute extraction with auto-fallback

**Run the chain through [`extract_web.py`](extract_web.py) (shipped with this skill), not by hand:**

```bash
python3 "$SKILL_DIR/extract_web.py" "$FULL_URL" --out /tmp/extract.md
```

It executes Defuddle → Jina with **both** fall-through triggers and hands back the counts §3 needs:

- **Content-thin** (the long-standing rule) — Defuddle returned under 50 words, an error JSON or a CDN block → take Jina.
- **Image-zero** — Defuddle returned a good body with **no image refs at all** → fetch Jina and adopt it if Jina emits images without costing material text.

**Why the second trigger exists.** Defuddle's image emission is site-dependent. Measured across six pages on the same day, it returned **0** image refs where Jina returned **8, 26 and 4** on three of them, and matched Jina on the other three. On those three it hands back a *full-length, perfectly good article body* with the figure layer simply absent — so it clears the `<50 words` test and the saved file looks clean. **A word-count check cannot see a missing figure layer.** A zero from Defuddle is a reason to ask the other extractor, not a finding about the page.

The JSON report gives `method`, `fallthrough`, `images_emitted`, `images_persisted` and every chrome exclusion with its reason. Full mechanics: [web_ingestion_methods.md](web_ingestion_methods.md) § Image-aware chain.

If both legs fail, use the WebFetch tool with the prompt "Extract the full article content as clean markdown."

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
extraction_method: [the report's `method` verbatim — e.g. defuddle, or
                    jina (image-zero fall-through from defuddle)]
images_emitted: [count of ![](...) refs the extractor returned — 0 is a real answer]
images_persisted: [count you actually kept in the saved file]
---
```

Below the frontmatter, place the extracted markdown content. Strip any navigation, ads, cookie banners or site chrome that leaked through.

#### `images_emitted` / `images_persisted` are MANDATORY on every web extraction (added 2 Aug 2026)

**Copy both numbers straight from the `extract_web.py` report (§2) — it counts before stripping, so don't recount by eye.** They exist to make a *silent* partial capture into a *visible* one.

**Why this is not optional.** A 2 Aug 2026 audit of 103 web-page extractions in one desk's ingested-source corpus found **87% had saved zero images**. Re-running all 86 fetchable ones through the built chain recovered **56 of them (154 images)** — the loss was real and most of it was recoverable. Two failure modes look identical on disk:

- **The extractor emitted images and the save discarded them.** Recoverable; `images_emitted: 4, images_persisted: 0` makes it obvious.
- **The extractor emitted nothing at all.** Nothing to harvest; `images_emitted: 0` is the only signal that the page may have an unread visual layer.

⚠️ **The second case is why `0` must be written rather than omitted.** A missing field and a genuine zero are indistinguishable, so an absent field reads as "no images on the page" when it may mean "nobody looked." **Write `images_emitted: 0` explicitly; never leave the field off.**

⚠️ **Emission is a per-PAGE property — never generalize it to a site.** An earlier version of this file named a specific publisher as one the extractor could not read. That was wrong, and the way it went wrong is the transferable lesson: the sample took **one page per site**, so a site-level verdict was never supported by it. At corpus scale every site sampled at more than one page is mixed — the publisher in question **emits images on 12 of its 17 pages**, the five exceptions being its five shortest posts. A single page tells you about that page.

**When they differ, say so in the body.** `images_emitted > images_persisted` means content was dropped — note which refs and why (the tool reports each chrome exclusion with its reason, which is legitimate; "I didn't carry them" is not). When `images_emitted: 0` on a page you have reason to believe is figure-bearing, add a one-line `⚠️ visual layer not captured` note under the frontmatter so a downstream consumer does not verdict on partial substrate.

⚠️ **`images_emitted: 0` only means what it claims if the image-aware fall-through actually ran.** A Defuddle-only save can report a truthful zero for the wrong reason — the page had figures, the *extractor* was blind to them. Take the zero at face value only when `extraction_method` shows the chain reached Jina. That is the whole basis on which a zero is trustworthy: not the count, but **a second extractor having independently agreed with it**.

**Full contract** — how to read the two numbers, when a zero is trustworthy, and how a recovered image layer is written back: [web_ingestion_methods.md](web_ingestion_methods.md) § Image completeness contract.

This convention came out of a measured gap audit on the authoring desk's own source corpus (Bamboo DCM reference implementation, Aug 2026) — adapt the thresholds to your own if they differ; the two fields, the write-`0`-explicitly rule and the corroboration rule are the transferable part.

### 4. Save the file

Default destination: `inbox/`

Use the filename convention: `{domain}_{slug}_{YYYY-MM-DD}.md`

- `domain`: short site name (e.g., `bloomberg`, `ft`, `reuters`)
- `slug`: kebab-case summary of the article title (max 5 words)
- Date: extraction date

Example: `bloomberg_brazil-rate-decision_2026-03-14.md`

If the user specified a different save location, use that instead.

### 5. Report and summarize

After saving each URL's file, print to chat:

1. **Save path** (e.g., `Saved → inbox/{domain}_{slug}_{YYYY-MM-DD}.md`).
2. **Executive summary (3–5 sentences)** of what the article actually argues — content-level, not metadata. Lets the user decide whether to read in full now, batch later, or skip.

**When to suppress the summary:**

- **Multiple URLs in parallel mode** with ≥ 5 URLs: print the summary table only; skip exec summaries.
- **Failed extraction:** no summary possible — print the error.
- **YouTube Tier 3 metadata-only stub:** flag explicitly that the summary is description-only (~5% of content), or skip entirely.

The summary describes WHAT the article says, not whether it's relevant — keep it factual.

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

**Paywalled subscription-archive sites may have a paired local archive.** Some sites publish recent entries free but paywall older entries. Before reporting a paywall failure, check whether the consuming workstation has a paired local archive of the same source (cloud-mounted folder, local repo) — extract from the local copy instead and note `source_pdf:` (or equivalent) in the output frontmatter. Pattern fires on subscription-research sites with a downloadable archive component; consuming workstation defines the lookup paths.

**WebFetch is a summarizer, not an extractor.** Empirically loses 75–92% of content on full articles (measured 15 Apr 2026 across multiple sources — Simon Willison, Medium, arXiv HTML, Anthropic blog). Some sites (e.g., X.com) 402 on WebFetch where Defuddle and Jina both succeed. Treat WebFetch as "get me something to read right now," not "archive this page." Only use as last resort when both Defuddle and Jina fail, and always flag in frontmatter (`extraction_method: WebFetch (summarized, ~80% content loss)`) so downstream consumers don't mistake it for verbatim.

**Defuddle returns 403 on some bot-protected sites (e.g., Medium).** Jina handles these — its managed browser penetrates anti-bot detection that plain HTTP fetches can't. The existing `<50 words → fall back to Jina` rule catches this, but don't conclude a site is unreachable just because Defuddle fails — always run Jina before declaring failure.

**X/Twitter multi-tweet threads return only the opener via all three tiers.** Defuddle, Jina Reader, and WebFetch all serve the single-post page metadata plus the opening tweet (~20–40 words ending in 🧵) on thread URLs. The substance — subsequent tweets by the same author — is not in the response from any of the three. Specific to thread structure; single tweets with long-form article-style content extract fully via Jina. Symptom: extracted markdown has <200 chars of body content, contains 🧵 or "Read N replies," and is surrounded by nav/trending-topics boilerplate. If detected: (1) escalate beyond the chain — search for a GitHub mirror or community archive that captured the thread verbatim, try a dedicated thread-reader service (`twitter-thread.com/t/{id}`), or prompt the user to paste the body; (2) if saving anyway, flag in frontmatter (`extraction_method: chain-incomplete; opener only — body not captured`) so downstream consumers know not to treat the opener as the full thread.

**Jina Reader rate limits on batch processing.** When processing 5+ URLs in parallel, Jina's free tier can return 429 errors. If batch ingesting, add a 2-second delay between Jina calls or process in waves of 3-4.

**Extraction strips meaningful formatting.** Tables, code blocks, and nested lists in the original article can be mangled by Defuddle or Jina. After extraction, spot-check that structural elements survived. If tables are important, note in the output that the user should verify table integrity against the source.

**Images are hotlinked, not downloaded locally.** Defuddle and Jina preserve image references as markdown `![](url)` pointing to the source server. If the source page is deleted or the CDN URL structure changes, the images break. The skill does not download images — if the user explicitly requests it, fetch them into an `assets/` subdirectory alongside the saved file and rewrite the markdown references.

> **This gotcha used to end in "flag it in the output," and that is precisely what failed.** An audit found the overwhelming majority of a working source corpus had been saved with no images at all — the advice was here, in this file, and did not fire once. Advisory prose aimed at the actor who is already mid-task is not a control. The harvest and the count are now a deterministic step in §2 ([`extract_web.py`](extract_web.py)) whose numbers land in mandatory frontmatter, which is the part that actually holds. Worth keeping in mind before writing your next gotcha as a sentence.

**URLs with query parameters need shell quoting.** When constructing curl commands for Defuddle or Jina, URLs containing `&`, `=`, `?`, or other shell metacharacters in query strings can break if not quoted. Always wrap the full URL in double quotes in the curl command. This is easy to miss because curl often succeeds anyway — the failure mode is silent truncation of the URL at the first unescaped `&`.

## Multiple URLs

When given multiple URLs, process them in parallel. Report results as a summary table:

| URL | Status | Saved to |
|-----|--------|----------|
| ... | OK / Failed | path |

---

*This skill is part of an internal knowledge-systems framework Bamboo DCM has been building for AI-native execution in regulated finance. If the broader framework is interesting, get in touch — we're publishing more as we package them.*
