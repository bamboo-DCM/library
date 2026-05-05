# Changelog

This changelog tracks substantive changes to the Bamboo DCM library repo. Updated at commit time for changes touching `README.md`, asset folders, or repo-level configuration.

---

## 5 May 2026

- **[pitch-deck-audit]** Added `/pitch-deck-audit` v0.1.0-beta — Claude Code skill + standalone playbook for auditing fundraise decks, structurer proposals, and M&A teasers using a sector-tuned lens. Phase 3a of the [pitch-deck-audit-kit project](https://github.com/bamboo-DCM/bamboo-marketing/blob/main/active/pitch-deck-audit-kit/pitch-deck-audit-kit.md) ships four core files: `SKILL.md` (Claude Code orchestration with three install paths — manual macOS/Linux + Windows + Cowork no-install), `playbook.md` (~6,500 words, 38 numbered sections in 8 parts; standalone-readable methodology synthesizing FI / Sequoia / Tottman / Rotman / Belenzon / Thiel + a 2026 AI-era extension on AI-native vs AI-applied / Service-as-Software / Wave-1 copilot anti-pattern / agent-speed infrastructure framings), `cowork_workflow.md` (~2,500 words, 9 sections; reads identically on Claude Code or Claude.ai Cowork), and `lens_template.md` (13-section blank Mad Libs schema for sectors not covered). README "Available now" table updated. Versioned-beta marker prominent — narrow distribution while substrate gets pressure-tested. Five worked sector lens annexes (credit-fintech / regulated structured-product / hard-tech / M&A teaser / structurer-to-counterparty) land in Phase 3b. — @arthur-bamboo
- **[repo, README.md]** Renamed repo `claude-code-skills` → `library` to hold both Claude Code skills and doc-only assets (playbooks, frameworks, templates) under one URL. GitHub auto-redirects the old URL. Top-level README rewritten to a "Bamboo DCM — Library" framing with a typed "Available now" table (Asset / Type / What it is) so future non-skill assets compose cleanly. `/ingest-web` install instructions retained verbatim under a "Claude Code skills" subsection; new "Playbooks and frameworks" subsection describes the standalone-readable shape future assets follow. Header positioning paragraph + italicized footer + three-founder mailto + CC-BY 4.0 license preserved from the prior README. — @arthur-bamboo

---

## 4 May 2026

- **[repo creation]** Public repo created under `bamboo-DCM/claude-code-skills` with first asset `/ingest-web` (v1.2.1-share). CC-BY 4.0 license. Top-level README, LICENSE, .gitignore, `/ingest-web/` folder. Companion convention captured at [`bamboo-marketing/strategy/external_tool_publication.md`](https://github.com/bamboo-DCM/bamboo-marketing/blob/main/strategy/external_tool_publication.md). — @arthur-bamboo
