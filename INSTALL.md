# Installation

ASDify is one portable Markdown skill. Choose the Skills CLI, the local installer, or manual chat instructions. The [harness table](docs/HARNESSES.md) lists every destination in the supported registry snapshot; [compatibility](docs/COMPATIBILITY.md) separates installation checks from real host sessions.

ASDify itself does not require Node.js, npm, or the Skills CLI. The local installer copies the same complete skill without an npm package download.

## Cursor without Node.js or npm

From an ASDify clone, install the native skill for your user account:

```bash
bash scripts/install.sh --agent cursor-skill --scope user
```

This copies the skill and all references to `~/.cursor/skills/asdify/`. For a project-only installation, run from the target project:

```bash
bash "/path/to/asdify/scripts/install.sh" --agent cursor-skill --scope project
```

That writes `.agents/skills/asdify/` beneath the current directory. Both locations are supported by [Cursor's skill documentation](https://cursor.com/docs/skills#skill-directories). The local installer uses `cursor-skill` for the complete native skill; its `cursor` ID installs the earlier compact rule.

You can also copy the entire `skills/asdify/` folder into either location yourself. Keep its references, and review an existing installation before replacing it. The installer handles destination checks and overwrite protection for you.

To check discovery, open **Customize → Skills** in Cursor and look for ASDify, then start a new agent session and request `Use asdify full`. Cursor's [viewing-skills guide](https://cursor.com/docs/skills#viewing-skills) describes the UI. Discovery and copying alone do not establish model quality.

## Skills CLI

With `npx` available, list the skill without installing ASDify into an agent:

```bash
npx skills add hevertonrodrigues/asdify --list
```

If you see `Need to install the following packages: skills@…` followed by `Ok to proceed? (y)`, npm is asking to download the optional Skills CLI into its cache before running it. This is expected; it is not an ASDify dependency or an installation error. [npm documents this prompt](https://docs.npmjs.com/cli/v11/commands/npm-exec/#description).

From the project that should receive the skill, select an agent:

```bash
npx skills add hevertonrodrigues/asdify --skill asdify --agent claude-code
```

The general form is `npx skills add hevertonrodrigues/asdify --skill asdify --agent <id>`. Replace `<id>` with a **Skills CLI ID** from the [table](docs/HARNESSES.md), for example `codex`, `cursor`, `gemini-cli`, `github-copilot`, `opencode`, or `windsurf`.

The CLI defaults to project scope. Add `--global` for user scope where the agent supports it. Interactive installation offers symlinks or copies; use `--copy` to request copies. Review the destinations the CLI displays before confirming. These options follow the [upstream CLI documentation](https://github.com/vercel-labs/skills#options), checked on 8 October 2026.

The Skills CLI downloads the repository and has its own [telemetry policy](https://skills.sh/docs/cli#telemetry); set `DISABLE_TELEMETRY=1` to opt out. The local installer below copies only files already on your machine.

To accept only npm's package-download prompt in advance, put `--yes` before `skills`:

```bash
DISABLE_TELEMETRY=1 npx --yes skills add hevertonrodrigues/asdify --skill asdify --agent cursor
```

This still downloads the CLI when needed. `--yes` after the skill command is a separate [Skills CLI option](https://github.com/vercel-labs/skills#options) that skips its own installation confirmations. `DISABLE_TELEMETRY=1` affects telemetry, not either confirmation.

## Local installer

Clone once, then list available IDs and scopes:

```bash
git clone https://github.com/hevertonrodrigues/asdify.git
cd asdify
bash scripts/install.sh --list
```

Install for your user account, choosing an ID from that list:

```bash
bash scripts/install.sh --agent claude-code --scope user
```

For a project installation, replace both paths and run from the destination project:

```bash
cd "/path/to/your-project" && \
  bash "/path/to/asdify/scripts/install.sh" --agent codex --scope project
```

The installer requires Bash and standard POSIX utilities. It copies the full `skills/asdify/` directory, including references, for native skill targets. It performs no downloads or telemetry. The compact Cursor rule is the one exception to a full skill copy.

- `--scope project` writes beneath the current working directory.
- `--scope user` uses the target's configured user directory. Unsupported scopes fail without installing.
- Existing destinations are preserved unless you pass `--force`, which replaces that ASDify installation.
- Some agents share the same skill directory. An existing ASDify copy in that directory can serve those agents; it does not need to be copied again for each ID.

## Cursor: native skill or compact rule

Choose the format you intend to use:

| Format | Skills CLI ID | Local installer ID | Project destination | Default user destination |
| --- | --- | --- | --- | --- |
| Native skill with references | `cursor` | `cursor-skill` | `.agents/skills/asdify/` | `~/.cursor/skills/asdify/` |
| Compact persistent rule | Not a Skills CLI target | `cursor` or `cursor-rule` | `.cursor/rules/asdify.mdc` | Project-only |

For a native Cursor skill using the local installer:

```bash
bash scripts/install.sh --agent cursor-skill --scope user
```

For the earlier compact rule, run from your target project:

```bash
cd "/path/to/your-project" && \
  bash "/path/to/asdify/scripts/install.sh" --agent cursor --scope project
```

The local `cursor` command preserves its original behavior. The local `claude` ID remains an alias for `claude-code`. Avoid installing both Cursor formats unless you intend to apply both instruction sources.

## User paths and overrides

See all paths in [HARNESSES.md](docs/HARNESSES.md). The following rules describe the **local installer**:

- XDG-based entries use an absolute `$XDG_CONFIG_HOME`, falling back to `$HOME/.config` when it is empty, unset, or relative. Only entries marked with this root use it; a literal `~/.config/...` path stays literal.
- `CLAUDE_CONFIG_DIR`, `AUTOHAND_HOME`, `GROK_HOME`, `HERMES_HOME`, and `VIBE_HOME` override their respective roots. Empty values use defaults. Nonempty overrides must be absolute; relative values are rejected. Surrounding whitespace is trimmed.
- `CODEX_HOME` does not change the Codex destination in this snapshot: user skills go to `~/.agents/skills/asdify/`.
- OpenClaw uses an existing `~/.openclaw`, then `~/.clawdbot`, then `~/.moltbot`, in that order; if none exists, it uses `~/.openclaw`. The registry's OpenClaw root marker is not an environment-variable override.
- Project installations ignore user-root overrides. Eve, PromptScript, and the compact Cursor rule have no user-scope destination in this registry.

## ChatGPT, Claude web, and other chat interfaces

Paste the contents of [SKILL.md](skills/asdify/SKILL.md) into the conversation as instructions, then send a complete [recipe](examples/recipes.md). For detailed checks, also provide the relevant text from [the skill's references](skills/asdify/references/).

This is manual use of the writing instructions, not a native skill installation or evidence that the application automatically discovers skills. Conversation context and the application's other instructions still apply.

For an unlisted native skill host, copy the entire `skills/asdify/` folder to the path documented by that host. The `universal` installer target is a shared layout convention, not automatic compatibility with every AI application. If a host only supports persistent instructions, merge [AGENTS.md](AGENTS.md) into its existing instruction file without replacing unrelated rules.

## Activation and modes

Start a new agent session and ask it to use `asdify full`, `lite`, or `ultra`; use its native invocation mechanism if available. `asdify off` disables this optional workflow subject to the host's other instructions. Modes are semantic instructions, not global slash commands.

Try a complete [recipe](examples/recipes.md) and check the output against its material facts and qualifications. Successful copying alone does not establish discovery, activation, or writing quality.

## Removal and updates

For a Skills CLI installation, use its removal workflow in the same scope:

```bash
npx skills remove asdify --agent claude-code
```

Add `--global` if you installed globally. The CLI also provides `npx skills update asdify`; see its [management commands](https://github.com/vercel-labs/skills#other-commands).

For a local installation, remove only the ASDify directory or rule printed by the installer and listed in the [harness table](docs/HARNESSES.md). Reinstall from an updated clone with `--force` after reviewing differences. Shared destinations affect every agent that reads that same copy.

Earlier installations under the former project name are not removed automatically. Review and remove those old copies when switching to ASDify so both sets of instructions do not apply.

## Troubleshooting

- **`Ok to proceed? (y)` before the CLI starts?** This is npm's optional CLI-download confirmation. Enter `y` to use that route, add `npx --yes` to accept the download in advance, or use the local installer to avoid npm entirely.
- **Wrong ID?** The local installer and Skills CLI have separate ID lists. In particular, native Cursor is `cursor-skill` locally and `cursor` in the Skills CLI.
- **Skill not discovered?** Check the destination, start a new session, and explicitly request ASDify. Report the host/version and actual behavior in an [installation issue](https://github.com/hevertonrodrigues/asdify/issues/new?template=bug_report.md).
- **Existing file blocked?** Review it before using `--force`; it may be the shared copy already used by another agent.
- **No text changed?** Already-clear text may correctly stay unchanged.
- **Facts changed or lost?** [Report a meaning regression](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml) with private information removed.
