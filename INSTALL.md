# Installation

ASDify is one portable Markdown skill. Choose the Skills CLI, the local installer, or manual chat instructions. The [harness table](docs/HARNESSES.md) lists every destination in the supported registry snapshot; [compatibility](docs/COMPATIBILITY.md) separates installation checks from real host sessions.

ASDify itself does not require Node.js, npm, or the Skills CLI. The local installer copies the same complete skill without an npm package download.

## Choose an installation route

| Route | Dependencies | Installation behavior |
| --- | --- | --- |
| [Skills CLI](#skills-cli) | Node.js/npm; network for uncached CLI/repository downloads | Agent selection, project/user scope, symlinks or copies |
| [Local installer](#local-installer) | Clone or extracted ZIP; Bash and POSIX utilities | Checked local copies; no downloads or telemetry |
| [Manual copy](#manual-copy-and-windows) | Skill files and the host's documented directory | Full skill without a package manager or shell |
| [Project instructions](#persistent-project-instructions) | A host that reads instruction files | Merge the compact rules or use Cursor's rule adapter |
| [Claude Code plugin](#claude-code-plugin) | Claude Code with plugin support | Plugin-manager registration, scopes, updates, and removal |
| [Manual chat](#chatgpt-claude-web-and-other-chat-interfaces) | A chat that accepts instructions | Paste instructions; no native installation |

Use one instruction source per host unless you intend to apply several. Filesystem layouts, actual activation, and writing effectiveness have separate evidence in [COMPATIBILITY.md](docs/COMPATIBILITY.md).

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

### Scope, copies, and multiple agents

For an unattended user-wide Cursor installation using copies:

```bash
DISABLE_TELEMETRY=1 npx --yes skills add hevertonrodrigues/asdify --skill asdify --agent cursor --global --copy --yes
```

For multiple selected agents in the current project:

```bash
npx skills add hevertonrodrigues/asdify --skill asdify --agent claude-code cursor codex
```

The CLI also accepts a local source: `npx skills add /path/to/asdify --skill asdify --agent cursor`. A local source avoids downloading the repository, but `npx` may still need to fetch the CLI. Use the Bash installer or manual copy for installation entirely from files already on your machine.

| Skills CLI option | Effect |
| --- | --- |
| `--list` | List repository skills without installing them into an agent |
| `--skill asdify` | Select this skill |
| `--agent <id>…` | Select one or more agent destinations |
| `--global` | Use user scope instead of the default project scope |
| `--copy` | Copy instead of creating symlinks |
| `--yes` after the command | Accept the CLI's installation confirmations |
| `--all` | Install all repository skills to all CLI agent targets; choose only if that is your intended scope |

The external CLI also documents temporary use with `npx skills use hevertonrodrigues/asdify --skill asdify`: it prints a generated prompt without registering a permanent skill. That route still needs the CLI and source downloads when uncached; it has not been tested here. See the [upstream command reference](https://github.com/vercel-labs/skills#use-a-skill-without-installing) for supported interactive-agent options. Manual chat instructions remain the simplest trial without this CLI.

## Local installer

Clone once, then list available IDs and scopes:

```bash
git clone https://github.com/hevertonrodrigues/asdify.git
cd asdify
bash scripts/install.sh --list
```

Without Git, use **Code → Download ZIP** on the [repository](https://github.com/hevertonrodrigues/asdify), extract it, and open a terminal in the extracted ASDify folder. Both approaches provide the same `skills/asdify/` and installer files for that revision. Choose a [tagged release](https://github.com/hevertonrodrigues/asdify/releases) when you need a fixed version; use `main` for unreleased changes.

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

| Local installer option | Effect |
| --- | --- |
| `--list` | List all IDs and available scopes; use on its own |
| `--agent <id>` | Select one registry destination |
| `--scope project` / `--scope user` | Select the installation scope |
| `--force` | Replace that ASDify installation after you review it |
| `--help` / `-h` | Show usage and the Cursor alias distinction |

Run the installer separately for distinct local targets. If several IDs share a destination, install once; the other hosts can read the same files if they support that layout. The registry lists destinations, not applications detected on your machine.

## Manual copy and Windows

1. Download a ZIP or clone the repository. Locate `skills/asdify/`.
2. Choose a project or user destination from [HARNESSES.md](docs/HARNESSES.md), or the host's own documentation if it is not listed.
3. Create the destination's parent directories and copy the **whole `asdify` folder**, preserving `SKILL.md` and every file under `references/`. Use your file manager or copy tool; do not copy only the entrypoint.
4. Review an existing ASDify copy before replacing it. Start a fresh host session and check discovery, then run a [recipe](examples/recipes.md).

For native Cursor, the resulting project file is `.agents/skills/asdify/SKILL.md` and the user file is `~/.cursor/skills/asdify/SKILL.md`. Keep the adjacent `references/` directory. `~` means the user's home; a Windows native application needs those files in its own Windows project/user directories.

Windows users can choose manual copy or the Skills CLI. The Bash installer needs a Bash/POSIX environment; with WSL or a remote session, install where that agent reads its files. Installing into a WSL home does not demonstrate that a Windows-native application can see the skill. The project's automated installer matrix covers Linux/macOS; Windows execution is unverified.

For cloud or remote hosts, follow their supported distribution mechanism or include project skills in the checkout. A local user installation alone does not make them available remotely.

## Persistent project instructions

If a host reads project instruction files instead of native skills, merge [AGENTS.md](AGENTS.md) into its existing instructions, preserving unrelated rules. Use the filename and scope documented by that host. This compact version includes the modes and preservation rules but fewer details than the canonical skill.

For Cursor's compact rule, copy [integrations/cursor-rule.mdc](integrations/cursor-rule.mdc) to `.cursor/rules/asdify.mdc`, or use the `cursor-rule` installer ID. The rule is project-only and always applies under Cursor's rule mechanism; `asdify off` disables the optional style workflow, not the host's instruction-loading mechanism.

## Claude Code plugin

The repository already includes `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`; both plugin and marketplace names are `asdify`. Inside an interactive Claude Code session:

```text
/plugin marketplace add hevertonrodrigues/asdify
/plugin install asdify@asdify
```

For a local clone, replace the first command with `/plugin marketplace add /path/to/asdify`. Choose user, project, or local scope in the plugin manager. From a shell, the equivalent commands are:

```bash
claude plugin marketplace add hevertonrodrigues/asdify
claude plugin install asdify@asdify --scope user
```

Start a new session and inspect `/plugin` or `claude plugin list`. Avoid duplicating a manually installed skill unless you intend to load both sources. The manifests pass local validation, but a real Claude plugin installation/activation has not been verified. See [Claude Code's official plugin instructions](https://code.claude.com/docs/en/discover-plugins) for supported versions and UI behavior.

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
Use `npx skills update asdify --global` for a user installation or `npx skills update asdify --project` for project scope where supported by your CLI version. `npx skills list --agent <id>` and `--global` let you inspect the corresponding installed scope before changing it.

For a local installation, remove only the ASDify directory or rule printed by the installer and listed in the [harness table](docs/HARNESSES.md). Reinstall from an updated clone with `--force` after reviewing differences. Shared destinations affect every agent that reads that same copy.

For a manual copy, obtain the updated revision, compare your local edits, and replace only the ASDify folder. For merged project instructions, update or remove just that text. For the Claude plugin, use its manager to update, disable, or uninstall `asdify@asdify` in the same scope. An extracted ZIP does not use `git pull`; download the updated archive instead.

Earlier installations under the former project name are not removed automatically. Review and remove those old copies when switching to ASDify so both sets of instructions do not apply.

## Troubleshooting

- **`Ok to proceed? (y)` before the CLI starts?** This is npm's optional CLI-download confirmation. Enter `y` to use that route, add `npx --yes` to accept the download in advance, or use the local installer to avoid npm entirely.
- **Wrong ID?** The local installer and Skills CLI have separate ID lists. In particular, native Cursor is `cursor-skill` locally and `cursor` in the Skills CLI.
- **Skill not discovered?** Check the destination, start a new session, and explicitly request ASDify. Report the host/version and actual behavior in an [installation issue](https://github.com/hevertonrodrigues/asdify/issues/new?template=bug_report.md).
- **Existing file blocked?** Review it before using `--force`; it may be the shared copy already used by another agent.
- **No text changed?** Already-clear text may correctly stay unchanged.
- **Facts changed or lost?** [Report a meaning regression](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml) with private information removed.
- **Windows, WSL, remote, or cloud host?** Check which filesystem the host reads, not just where the installer ran. Use [manual-copy guidance](#manual-copy-and-windows) and the host's supported distribution method.
- **Plugin installed but unavailable?** Check the plugin manager's status, scope, and errors; start a fresh session and include that evidence in an installation report.

See [SUPPORT.md](SUPPORT.md) for reporting routes, language/documentation help, and the difference between package support and host-provider support.
