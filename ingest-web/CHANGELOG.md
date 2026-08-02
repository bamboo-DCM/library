---
skill: ingest-web
updated: 2 Aug 2026
---

# ingest-web — CHANGELOG

Public mirror of the `/ingest-web` skill. Pointer: [SKILL.md](SKILL.md) · [web_ingestion_methods.md](web_ingestion_methods.md).

Repo-wide notes live at [../CHANGELOG.md](../CHANGELOG.md); this file documents per-version delta narrative for the skill specifically.

---

## 1.9.0-share — 2 Aug 2026

**Adds § Image completeness contract, and corrects a claim the previous two releases got wrong.**

v1.7.0 made `images_emitted` / `images_persisted` mandatory; v1.8.0 made them true by shipping `extract_web.py`. Neither said how to *read* them. This does.

**The load-bearing idea: a web page has no expected image count.** The transcript contract in the same file scores against `duration_min × 150`, so `partial` is a computable verdict. A page has no denominator — nothing says how many figures it should have had. So image completeness cannot be **scored**, only **corroborated**: a zero is trustworthy when a *second, independent extractor* returned zero on the same page. The image-aware fall-through already produces that at write time. Adds `images_rechecked:` (optional — what makes a later zero corroborated rather than merely inherited), a six-state reading table, and **append-never-splice** for recovered image layers: a re-fetch returns a *different document* from the one captured, so splicing today's refs into yesterday's text would place them at positions the text never had and overwrite any annotation added since.

⚠️ **Correction — emission is a per-PAGE property, not a per-site one.** v1.7.0 and v1.8.0 described a specific publisher as one this chain could not read, and called emission "site-dependent," on the strength of a sample that took **one page per site**. That does not survive contact with a corpus: **every site sampled at more than one page is mixed**, and the publisher in question **emits images on 12 of its 17 pages** — the five that don't are its five shortest posts. **The site-level claims are struck from the live guidance in both files** (the per-page measurement table stays — each row was always one article, and those numbers are correct; the entries below keep their original wording, because a changelog is a record). The transferable lesson is not about that publisher: **a one-page-per-site sample cannot support a site-level verdict**, and `images_emitted: 0` is never a fact about a publisher.

**Numbers now corpus-scale rather than sample-scale:** 86 previously image-free saves re-run, 0 errors, **56 recovered, 154 images**; chrome screen 7 exclusions of 161 emitted with zero body diagrams lost. ⚠️ Also worth knowing if you adopt this: **the image-zero trigger is the smaller half** — 6 of the 56 recoveries — while the harvest accounts for the rest, mostly on pages where the pre-existing content-thin fall-through had already reached the second extractor and the images simply were not kept. And the 60% word-count floor guarding against trading a page for an image-bearing stub **has never once fired** in practice, so treat it as untested.

---

## 1.8.0-share — 2 Aug 2026

**The image harvest and the fall-through that makes it reachable are now code — [`extract_web.py`](extract_web.py), shipped with the skill.**

1.7.0-share made the *counts* mandatory. This makes the counts true: it harvests the refs, screens page chrome, and — the load-bearing half — asks the second extractor when the first returns none.

**Defuddle's image emission is site-dependent.** Measured on six pages, same day, same URLs:

| page | Defuddle | Jina |
|---|---:|---:|
| nfx.com | **0** | 8 |
| a16z.news | **0** | 26 |
| latent.space | **0** | 4 |
| tomtunguz.com | 1 | 1 |
| anthropic.com | 2 | 2 |
| ben-evans.com | 0 | 0 |

On the first three, Defuddle returns a **full-length, perfectly good article body** with the figure layer simply absent — so it clears the `<50 words` fall-back and the saved file looks clean. **A word-count check cannot see a missing figure layer.**

**Two fall-through triggers now, not one:**
- **content-thin** (pre-existing) — under 50 words / error JSON / CDN block → take Jina.
- **image-zero** (new) — Defuddle emitted no image refs → fetch Jina, adopt **only if** it emits images *and* its body is ≥ 60% of Defuddle's word count. A page is never traded for an image-bearing stub.

**Verified by re-run, not inspection.** The ten-domain sample from the gap audit, put back through the built pipeline: **7 of 10 now persist body images; the same 3 that emitted nothing before still emit nothing.** The image-zero trigger specifically rescued 3 domains the word-count rule would have passed straight through. On one worked page, Defuddle returned 2,191 words and 0 images; the fall-through recovered all 4 body diagrams with 0 chrome false-positives.

⚠️ **This is also what makes the 1.7.0 zero mean what it claims.** Without the fall-through, a Defuddle-only save reports a truthful `images_emitted: 0` for the **wrong reason** — the page had figures, the extractor was blind to them — so the record is honest about the count and wrong about the cause. Take a zero at face value only when `extraction_method` shows the chain reached Jina.

🔑 **The transferable part is the shape, not the extractor.** The advice to flag missing images was *already written in the skill*, and the audit still found the overwhelming majority of a working corpus saved image-free. Advisory prose aimed at an actor already mid-task is not a control; a deterministic step whose numbers land in mandatory frontmatter is. The old gotcha is kept, annotated with its own failure, as a caution against writing your next control as a sentence.

---

## 1.7.0-share — 2 Aug 2026

**`images_emitted` / `images_persisted` are now MANDATORY frontmatter on every web extraction.**

Count the `![](...)` refs the extractor returned *before* stripping anything; record that number and how many survived into the saved file.

**Measured, not assumed.** A gap audit of **103 web-page extractions** in one desk's ingested-source corpus found **87% had saved zero images**. A live re-fetch of ten separated two failure modes that are **indistinguishable on disk**: **7 of 10** emitted images that the save discarded (recoverable), and **3 of 10** emitted *nothing at all* — one a chart-dense author whose pages return zero images even with `X-Retain-Images: all`.

⚠️ **`0` must be written, never omitted.** A missing field and a genuine zero look identical, so an absent field reads as *"no images on this page"* when it may mean *"this extractor is blind to this site."* That second class is invisible to any emitted-vs-persisted ratio — when the numerator is 0 the metric reads clean — which is exactly why the field, not the ratio, is the control.


## [1.6.0-share] — 13 Jul 2026

### Added — optional Jina Reader API key (higher rate limit)

- **Method 3 now documents the optional API key.** The keyless Reader endpoint is free (~20 RPM); authenticating with a free key from jina.ai raises the limit to ~500 RPM for batch/parallel fetching. Keyless requests are unmetered, so reserve the key for genuine volume — a single one-off fetch stays keyless. Generalizable guidance; no change to the keyless default behavior.

## [1.5.2-share] — 28 May 2026

### Added

- **`web_ingestion_methods.md` Method 7 — NEW § Per-architecture extraction patterns (catalog).** Empirical catalog of per-architecture Jina-extraction primitives by publisher site framework. Each row pairs the architecture (Substack / Squarespace / Hugo blog / Next.js publisher-style / Framer SPA / NextJS-SPA sitemap-fallback / LinkedIn Pulse aggregator) with the working `curl` primitive against Jina and the expected output shape. Save the re-discovery cost on novel sources by matching the publisher's stack to the catalog entry.
- **Two failure modes named explicitly:** (a) sparse-homepage trap — Substack-class sites return image/header chrome on the bare homepage; the `/archive` path is the actual enumeration surface (test: if homepage Jina returns <500 words, switch to `/archive`); (b) RSS-cap-hides-the-archive trap — Substack 20-item / Squarespace 20-item / Hugo `/index.xml` ~10-item caps are invisible from the feed itself; assuming "feed = archive" silently misses 90%+ of recent cadence on high-frequency publishers.
- **Per-source documentation discipline pointer** — when discovering a working primitive for a new source, document it inline on that source's row in your source registry per your project's access-mechanics-documentation convention. The catalog is the pattern-class generalization; the registry row is the per-source application.

### Source

28 May 2026 multi-source enumeration sweep across 8 Tier-1 publisher sources — Jina primitive worked first-try on 5 of 8 with the obvious path; required `/archive` retry on 2; required `/library` retry on 1. Codified during a multi-session content-ingestion retrospective. Substrate-only edit (no `SKILL.md` change); patch-version bump on this CHANGELOG sibling.

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
