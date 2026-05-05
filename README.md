# Bamboo DCM — Library

Open-source assets — Claude Code skills, playbooks, and frameworks — published by [**Bamboo DCM**](https://bamboodcm.com), an AI-native private credit infrastructure platform in São Paulo, Brazil.

These are pieces of the operating model we use internally. We're publishing them as we go because the firm's competitive surface is the operating model itself, and the operating model gets stronger when others can pressure-test it.

## Available now

| Asset | Type | What it is |
|---|---|---|
| [`/ingest-web`](./ingest-web/) | Claude Code skill | Extract web content as clean markdown. Includes a dedicated YouTube transcript chain (youtube-transcript-api → yt-dlp → explicit fallback alert) that routes YouTube URLs separately from the standard Defuddle / Jina Reader / WebFetch chain — the standard chain returns page chrome on YouTube, not the actual transcript. |
| [`/pitch-deck-audit`](./pitch-deck-audit/) | Claude Code skill + standalone playbook | Audit a fundraise deck (or structurer proposal, M&A teaser) using a sector-tuned lens. Ships `SKILL.md` + a standalone playbook (38 sections, 8 parts) + a fillable lens template + a Cowork (no-install) workflow guide + five worked sector [`examples/`](./pitch-deck-audit/examples/) (credit-fintech / regulated structured-product / hard-tech / M&A teaser / structurer-to-counterparty). **`v0.1.0-beta` — versioned beta, narrow distribution while the substrate gets pressure-tested.** |

More assets land here as we package them. If the broader knowledge-systems framework around these is interesting, get in touch.

## Using the assets

### Claude Code skills

Each skill folder is self-contained. Drop the folder into your Claude Code skills directory and use the trigger.

**1. One-time prerequisite** — install `uv` if a skill needs it (the YouTube branch in `/ingest-web` does):

```bash
# macOS / Linux
brew install uv     # or: curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Any OS with Python
pip install uv
```

**2. Drop the skill folder into your Claude Code skills directory:**

- macOS / Linux: `~/.claude/skills/`
- Windows: `%USERPROFILE%\.claude\skills\`

For example, to install `/ingest-web`:

```bash
# macOS / Linux
git clone https://github.com/bamboo-DCM/library.git
cp -r library/ingest-web ~/.claude/skills/
```

```powershell
# Windows (PowerShell)
git clone https://github.com/bamboo-DCM/library.git
Copy-Item -Recurse library\ingest-web $env:USERPROFILE\.claude\skills\
```

**3. Verify** by listing your skills directory and confirming the skill folder is present. Then in Claude Code: `/ingest-web https://...` (or whichever skill).

### Playbooks and frameworks

Each has its own usage notes inside its folder. They're written to be useful standalone — readable straight on GitHub, paste-ready into a Claude.ai project, or printable — and to compose with the skills when both apply to the same job.

## Contact

Comments, improvements, bug reports, or questions:

- **Arthur O'Keefe** — [arthur@bamboodcm.com](mailto:arthur@bamboodcm.com)
- **Felipe Grassi de Moraes** — [felipe@bamboodcm.com](mailto:felipe@bamboodcm.com)
- **Urian Inhauser** — [urian@bamboodcm.com](mailto:urian@bamboodcm.com)

Issues and pull requests are welcome. We don't promise SLAs on either, but we read everything.

## License

[CC-BY 4.0](./LICENSE) — free to share and adapt with attribution to Bamboo DCM. Commercial use is permitted; we ask that you keep the attribution intact and link back to this repository (or to [bamboodcm.com](https://bamboodcm.com)) when you do.

---

*These assets are part of an internal knowledge-systems framework Bamboo DCM has been building for AI-native execution in regulated finance. We're publishing more in the coming weeks — if the broader framework is interesting, get in touch.*
