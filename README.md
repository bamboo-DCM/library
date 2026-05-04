# Bamboo DCM — Claude Code skills

Open-source [Claude Code](https://www.anthropic.com/claude-code) skills published by [**Bamboo DCM**](https://bamboodcm.com), an AI-native private credit infrastructure platform in São Paulo, Brazil.

These are the same skills we use internally to feed external research, founder interviews, regulator commentary, and conference talks into our analytical workflows. We're publishing them as we go because the firm's competitive surface is the operating model, and the operating model gets stronger when others can pressure-test it.

## Available skills

| Skill | Purpose |
|---|---|
| [`/ingest-web`](./ingest-web/) | Extract web content as clean markdown — including a dedicated YouTube transcript chain (youtube-transcript-api → yt-dlp → explicit fallback alert). Routes YouTube URLs separately from the standard Defuddle / Jina Reader / WebFetch chain because the standard chain returns page chrome (comments, navigation) on YouTube, not the actual transcript. |

More skills will land here as we package them. If you're curious about the broader knowledge-systems framework around these skills, get in touch.

## Install

Each skill folder is a self-contained Claude Code skill. To install one:

**1. One-time prerequisites** — install `uv` if a skill needs it (the YouTube branch in `/ingest-web` does):

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
git clone https://github.com/bamboo-DCM/claude-code-skills.git
cp -r claude-code-skills/ingest-web ~/.claude/skills/
```

```powershell
# Windows (PowerShell)
git clone https://github.com/bamboo-DCM/claude-code-skills.git
Copy-Item -Recurse claude-code-skills\ingest-web $env:USERPROFILE\.claude\skills\
```

**3. Verify** by listing your skills directory and confirming the skill folder is present. Then in Claude Code: `/ingest-web https://...` (or whichever skill).

## Contact

Comments, improvements, bug reports, or questions:

- **Arthur O'Keefe** — [arthur@bamboodcm.com](mailto:arthur@bamboodcm.com)
- **Felipe Grassi de Moraes** — [felipe@bamboodcm.com](mailto:felipe@bamboodcm.com)
- **Urian Inhauser** — [urian@bamboodcm.com](mailto:urian@bamboodcm.com)

Issues and pull requests are welcome. We don't promise SLAs on either, but we read everything.

## License

[CC-BY 4.0](./LICENSE) — free to share and adapt with attribution to Bamboo DCM. Commercial use is permitted; we ask that you keep the attribution intact and link back to this repository (or to [bamboodcm.com](https://bamboodcm.com)) when you do.

---

*These skills are part of an internal knowledge-systems framework Bamboo DCM has been building for AI-native execution in regulated finance. We're publishing more in the coming weeks — if the broader framework is interesting, get in touch.*
