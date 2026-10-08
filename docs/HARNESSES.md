# Supported harness layouts

The local installer accepts **82 IDs: 79 upstream agent mappings and 3 compatibility IDs**. The table records installation layouts, including coding CLIs, editor integrations, and the generic `universal` target. It does not certify that every host loads or follows ASDify.

**Snapshot:** 8 October 2026, Vercel [agent registry commit `05bf93879366fa21c5a4df7482a96adf13beabd2`](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts). This table is generated from [integrations/agents.tsv](../integrations/agents.tsv), the local installer's source of truth. Each host links to its mapping source.

Use `bash scripts/install.sh --list` from the repository root to list local IDs and scopes. For the external CLI, use the **Skills CLI ID** column with `npx skills add hevertonrodrigues/asdify --skill asdify --agent <id>`. See [INSTALL.md](../INSTALL.md) for complete commands and [COMPATIBILITY.md](COMPATIBILITY.md) for test evidence.

## Reading the paths

- Project destinations are relative to the current working directory. User destinations use the roots below. Each skill directory contains `SKILL.md` and `references/`.
- `~` means the current user's home. `$XDG_CONFIG_HOME` uses an absolute configured value or defaults to `~/.config` if empty, unset, or relative.
- Other configurable roots default to: `$CLAUDE_CONFIG_DIR` → `~/.claude`; `$AUTOHAND_HOME` → `~/.autohand`; `$GROK_HOME` → `~/.grok`; `$HERMES_HOME` → `~/.hermes`; `$VIBE_HOME` → `~/.vibe`. The local installer trims whitespace, treats empty values as unset, and rejects nonempty relative values.
- `{OpenClaw root}` selects an existing `~/.openclaw`, then `~/.clawdbot`, then `~/.moltbot`; otherwise it defaults to `~/.openclaw`. It is a directory-selection rule, not an environment variable.
- `—` means that scope or CLI target is unavailable. A literal `~/.config/...` path does not inherit the XDG override. Project scope ignores user-root configuration.
- Shared paths mean shared skill files. Installing the same skill again through another ID may correctly trigger overwrite protection.

## Complete registry

The local `claude` alias maps to `claude-code`. Local `cursor` and `cursor-rule` retain the compact persistent rule; local `cursor-skill` maps to the upstream native `cursor` skill target. These aliases do not add three new hosts.

<!-- Table generated from integrations/agents.tsv; preserve one row per local ID. -->
| Harness | Local ID | Skills CLI ID | Project destination | User destination |
| --- | --- | --- | --- | --- |
| [AdaL](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L809) | `adal` | `adal` | `.adal/skills/asdify/` | `~/.adal/skills/asdify/` |
| [AiderDesk](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L81) | `aider-desk` | `aider-desk` | `.aider-desk/skills/asdify/` | `~/.aider-desk/skills/asdify/` |
| [Amp](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L90) | `amp` | `amp` | `.agents/skills/asdify/` | `$XDG_CONFIG_HOME/agents/skills/asdify/` |
| [Antigravity](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L99) | `antigravity` | `antigravity` | `.agents/skills/asdify/` | `~/.gemini/antigravity/skills/asdify/` |
| [Antigravity CLI](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L109) | `antigravity-cli` | `antigravity-cli` | `.agents/skills/asdify/` | `~/.gemini/antigravity-cli/skills/asdify/` |
| [AstrBot](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L119) | `astrbot` | `astrbot` | `data/skills/asdify/` | `~/.astrbot/data/skills/asdify/` |
| [Augment](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L137) | `augment` | `augment` | `.augment/skills/asdify/` | `~/.augment/skills/asdify/` |
| [Autohand Code CLI](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L128) | `autohand-code` | `autohand-code` | `.autohand/skills/asdify/` | `$AUTOHAND_HOME/skills/asdify/` |
| [IBM Bob](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L146) | `bob` | `bob` | `.bob/skills/asdify/` | `~/.bob/skills/asdify/` |
| [Claude Code (alias)](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L155) | `claude` | `claude-code` | `.claude/skills/asdify/` | `$CLAUDE_CONFIG_DIR/skills/asdify/` |
| [Claude Code](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L155) | `claude-code` | `claude-code` | `.claude/skills/asdify/` | `$CLAUDE_CONFIG_DIR/skills/asdify/` |
| [Cline](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L179) | `cline` | `cline` | `.agents/skills/asdify/` | `~/.agents/skills/asdify/` |
| [CodeArts Agent](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L188) | `codearts-agent` | `codearts-agent` | `.codeartsdoer/skills/asdify/` | `~/.codeartsdoer/skills/asdify/` |
| [CodeBuddy](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L197) | `codebuddy` | `codebuddy` | `.codebuddy/skills/asdify/` | `~/.codebuddy/skills/asdify/` |
| [Codemaker](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L206) | `codemaker` | `codemaker` | `.codemaker/skills/asdify/` | `~/.codemaker/skills/asdify/` |
| [Code Studio](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L215) | `codestudio` | `codestudio` | `.codestudio/skills/asdify/` | `~/.codestudio/skills/asdify/` |
| [Codex](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L224) | `codex` | `codex` | `.agents/skills/asdify/` | `~/.agents/skills/asdify/` |
| [Command Code](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L233) | `command-code` | `command-code` | `.commandcode/skills/asdify/` | `~/.commandcode/skills/asdify/` |
| [Continue](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L242) | `continue` | `continue` | `.continue/skills/asdify/` | `~/.continue/skills/asdify/` |
| [Cortex Code](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L251) | `cortex` | `cortex` | `.cortex/skills/asdify/` | `~/.snowflake/cortex/skills/asdify/` |
| [Crush](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L260) | `crush` | `crush` | `.crush/skills/asdify/` | `~/.config/crush/skills/asdify/` |
| [Cursor (legacy rule)](https://cursor.com/docs/rules) | `cursor` | — | `.cursor/rules/asdify.mdc` | — |
| [Cursor (rule alias)](https://cursor.com/docs/rules) | `cursor-rule` | — | `.cursor/rules/asdify.mdc` | — |
| [Cursor (native skill)](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L269) | `cursor-skill` | `cursor` | `.agents/skills/asdify/` | `~/.cursor/skills/asdify/` |
| [Deep Agents](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L278) | `deepagents` | `deepagents` | `.agents/skills/asdify/` | `~/.deepagents/agent/skills/asdify/` |
| [Devin for Terminal](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L288) | `devin` | `devin` | `.devin/skills/asdify/` | `$XDG_CONFIG_HOME/devin/skills/asdify/` |
| [Dexto](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L297) | `dexto` | `dexto` | `.agents/skills/asdify/` | `~/.agents/skills/asdify/` |
| [Droid](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L307) | `droid` | `droid` | `.agents/skills/asdify/` | `~/.factory/skills/asdify/` |
| [Eve](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L320) | `eve` | `eve` | `agent/skills/asdify/` | — |
| [Firebender](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L332) | `firebender` | `firebender` | `.agents/skills/asdify/` | `~/.firebender/skills/asdify/` |
| [ForgeCode](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L342) | `forgecode` | `forgecode` | `.forge/skills/asdify/` | `~/.forge/skills/asdify/` |
| [fx](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L351) | `fx` | `fx` | `.fx/skills/asdify/` | `~/.fx/skills/asdify/` |
| [Gemini CLI](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L360) | `gemini-cli` | `gemini-cli` | `.agents/skills/asdify/` | `~/.gemini/skills/asdify/` |
| [GitHub Copilot](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L369) | `github-copilot` | `github-copilot` | `.agents/skills/asdify/` | `~/.copilot/skills/asdify/` |
| [Goose](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L378) | `goose` | `goose` | `.goose/skills/asdify/` | `$XDG_CONFIG_HOME/goose/skills/asdify/` |
| [Grok Build](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L387) | `grok` | `grok` | `.grok/skills/asdify/` | `$GROK_HOME/skills/asdify/` |
| [Hermes Agent](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L396) | `hermes-agent` | `hermes-agent` | `.hermes/skills/asdify/` | `$HERMES_HOME/skills/asdify/` |
| [iFlow CLI](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L432) | `iflow-cli` | `iflow-cli` | `.iflow/skills/asdify/` | `~/.iflow/skills/asdify/` |
| [inference.sh](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L405) | `inference-sh` | `inference-sh` | `.inferencesh/skills/asdify/` | `~/.inferencesh/skills/asdify/` |
| [Jazz](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L414) | `jazz` | `jazz` | `.jazz/skills/asdify/` | `~/.jazz/skills/asdify/` |
| [Junie](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L423) | `junie` | `junie` | `.junie/skills/asdify/` | `~/.junie/skills/asdify/` |
| [Kilo Code](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L441) | `kilo` | `kilo` | `.agents/skills/asdify/` | `~/.kilo/skills/asdify/` |
| [Kimchi](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L452) | `kimchi` | `kimchi` | `.kimchi/skills/asdify/` | `~/.config/kimchi/harness/skills/asdify/` |
| [Kimi Code CLI](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L461) | `kimi-code-cli` | `kimi-code-cli` | `.agents/skills/asdify/` | `~/.agents/skills/asdify/` |
| [Kiro CLI](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L470) | `kiro-cli` | `kiro-cli` | `.kiro/skills/asdify/` | `~/.kiro/skills/asdify/` |
| [Kode](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L479) | `kode` | `kode` | `.kode/skills/asdify/` | `~/.kode/skills/asdify/` |
| [Lingma](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L488) | `lingma` | `lingma` | `.lingma/skills/asdify/` | `~/.lingma/skills/asdify/` |
| [Loaf](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L497) | `loaf` | `loaf` | `.agents/skills/asdify/` | `~/.agents/skills/asdify/` |
| [MCPJam](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L507) | `mcpjam` | `mcpjam` | `.mcpjam/skills/asdify/` | `~/.mcpjam/skills/asdify/` |
| [MiniMax Code](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L516) | `minimax-code` | `minimax-code` | `.minimax/skills/asdify/` | `~/.minimax/skills/asdify/` |
| [Mistral Vibe](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L525) | `mistral-vibe` | `mistral-vibe` | `.vibe/skills/asdify/` | `$VIBE_HOME/skills/asdify/` |
| [Moxby](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L534) | `moxby` | `moxby` | `.moxby/skills/asdify/` | `~/.moxby/skills/asdify/` |
| [Mux](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L543) | `mux` | `mux` | `.mux/skills/asdify/` | `~/.mux/skills/asdify/` |
| [Neovate](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L778) | `neovate` | `neovate` | `.neovate/skills/asdify/` | `~/.neovate/skills/asdify/` |
| [Ona](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L570) | `ona` | `ona` | `.ona/skills/asdify/` | `~/.ona/skills/asdify/` |
| [OpenClaw](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L166) | `openclaw` | `openclaw` | `skills/asdify/` | `{OpenClaw root}/skills/asdify/` |
| [OpenCode](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L552) | `opencode` | `opencode` | `.agents/skills/asdify/` | `$XDG_CONFIG_HOME/opencode/skills/asdify/` |
| [OpenHands](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L561) | `openhands` | `openhands` | `.openhands/skills/asdify/` | `~/.openhands/skills/asdify/` |
| [Pi](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L579) | `pi` | `pi` | `.agents/skills/asdify/` | `~/.agents/skills/asdify/` |
| [Pochi](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L787) | `pochi` | `pochi` | `.pochi/skills/asdify/` | `~/.pochi/skills/asdify/` |
| [Posit Assistant](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L591) | `posit-assistant` | `posit-assistant` | `.posit/assistant/skills/asdify/` | `~/.posit/assistant/skills/asdify/` |
| [PromptScript](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L796) | `promptscript` | `promptscript` | `.agents/skills/asdify/` | — |
| [Qoder](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L600) | `qoder` | `qoder` | `.qoder/skills/asdify/` | `~/.qoder/skills/asdify/` |
| [Qoder CN](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L609) | `qoder-cn` | `qoder-cn` | `.qoder/skills/asdify/` | `~/.qoder-cn/skills/asdify/` |
| [Qwen Code](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L618) | `qwen-code` | `qwen-code` | `.qwen/skills/asdify/` | `~/.qwen/skills/asdify/` |
| [Reasonix](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L637) | `reasonix` | `reasonix` | `.reasonix/skills/asdify/` | `~/.reasonix/skills/asdify/` |
| [Replit](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L627) | `replit` | `replit` | `.agents/skills/asdify/` | `$XDG_CONFIG_HOME/agents/skills/asdify/` |
| [Roo Code](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L655) | `roo` | `roo` | `.roo/skills/asdify/` | `~/.roo/skills/asdify/` |
| [Rovo Dev](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L646) | `rovodev` | `rovodev` | `.rovodev/skills/asdify/` | `~/.rovodev/skills/asdify/` |
| [Sarvam Code](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L664) | `sarvam-code` | `sarvam-code` | `.agents/skills/asdify/` | `~/.agents/skills/asdify/` |
| [Tabnine CLI](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L674) | `tabnine-cli` | `tabnine-cli` | `.tabnine/agent/skills/asdify/` | `~/.tabnine/agent/skills/asdify/` |
| [Terramind](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L683) | `terramind` | `terramind` | `.terramind/skills/asdify/` | `~/.terramind/skills/asdify/` |
| [Tinycloud](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L692) | `tinycloud` | `tinycloud` | `.tinycloud/skills/asdify/` | `~/.tinycloud/skills/asdify/` |
| [Trae](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L701) | `trae` | `trae` | `.trae/skills/asdify/` | `~/.trae/skills/asdify/` |
| [Trae CN](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L710) | `trae-cn` | `trae-cn` | `.trae/skills/asdify/` | `~/.trae-cn/skills/asdify/` |
| [Universal](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L818) | `universal` | `universal` | `.agents/skills/asdify/` | `$XDG_CONFIG_HOME/agents/skills/asdify/` |
| [Warp](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L719) | `warp` | `warp` | `.agents/skills/asdify/` | `~/.agents/skills/asdify/` |
| [Windsurf](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L728) | `windsurf` | `windsurf` | `.windsurf/skills/asdify/` | `~/.codeium/windsurf/skills/asdify/` |
| [ZCode](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L751) | `zcode` | `zcode` | `.zcode/skills/asdify/` | `~/.zcode/skills/asdify/` |
| [Zed](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L737) | `zed` | `zed` | `.agents/skills/asdify/` | `~/.agents/skills/asdify/` |
| [Zencoder](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L760) | `zencoder` | `zencoder` | `.zencoder/skills/asdify/` | `~/.zencoder/skills/asdify/` |
| [Zenflow](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts#L769) | `zenflow` | `zenflow` | `.zencoder/skills/asdify/` | `~/.zencoder/skills/asdify/` |

## Coverage boundaries

Mappings are versioned snapshots of supported layouts, not promises about future versions, automatic activation, or every model. The local installer copies files only; it does not launch the target host or configure its permissions.

ChatGPT, Claude web, and other ordinary chat interfaces use the [manual instructions](../INSTALL.md#chatgpt-claude-web-and-other-chat-interfaces). For an unlisted skill host, follow that host's documented path and submit a mapping with primary-source documentation and installation evidence.
