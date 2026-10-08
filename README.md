# ASDify

![ASDify — Clearer AI writing. Meaning intact.](assets/readme/hero.svg)

[![CI checks](https://github.com/hevertonrodrigues/asdify/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/hevertonrodrigues/asdify/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-18283b?style=flat-square)](LICENSE)
[![Format: portable Markdown](https://img.shields.io/badge/format-portable%20Markdown-18283b?style=flat-square)](skills/asdify/SKILL.md)
[![Languages: 9](https://img.shields.io/badge/languages-9-dba44e?style=flat-square)](docs/LANGUAGES.md)

[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [Italiano](README.it.md) · [Русский](README.ru.md)

[Try it](#try-it-without-installing) · [Install](#install-for-your-agent) · [Supported environments](#supported-environments) · [Languages](docs/LANGUAGES.md) · [Support](#support-and-troubleshooting) · [Recipes](examples/recipes.md) · [Contribute](CONTRIBUTING.md)

Give your AI agent a repeatable editing routine: find the point, remove filler, and check that the important details survive. ASDify is a small, portable Markdown skill for answers, translations, status updates, reports, and documentation across supported coding agents and editors.

## See the difference

![An illustrative edit removes the introduction while preserving unaudited, preliminary subscription revenue in Brazil, 12% year-over-year growth, and the exclusion of refunds.](assets/readme/before-after.svg)

*Illustrative editorial example, not measured model output.* [Explore more before-and-after examples →](examples/before-after.md)

<details>
<summary><strong>Copy the illustrative edit</strong></summary>

```text
Unaudited, preliminary subscription revenue in Brazil grew 12% year over year,
excluding refunds.
```

</details>

## Try it without installing

1. Open [SKILL.md](skills/asdify/SKILL.md), copy its contents, and paste them as instructions into a chat, such as ChatGPT or Claude web.
2. Send this prompt:

```text
Use asdify full. Rewrite this update for an executive.
Return only the rewritten text. Preserve every fact and qualification.

We would like to highlight that preliminary subscription revenue grew 12%
year over year in Brazil, excluding refunds. These figures have not yet
been audited.
```

Compare the result with the details shown above. Wording can vary; the facts and qualifications must survive. This is a manual trial, with no automatic skill installation.

[See a real Codex run](docs/demos/codex-full-2026-10-08.md), with the exact prompt, output, and checks for preserved details.

## Install for your agent

ASDify is Markdown. Node.js and npm are needed only if you choose the optional Skills CLI. Choose the route your host supports:

| Route | Use it when | What you need |
| --- | --- | --- |
| [Skills CLI](#skills-cli) | You want discovery, agent selection, and managed installation | Node.js/npm and network access for downloads |
| [Local installer](#local-installer-without-npm) | You want checked file copying without npm | An ASDify clone or extracted ZIP, Bash, and POSIX utilities |
| [Manual copy](#manual-copy-or-project-instructions) | You want no installer, including on Windows | The complete skill folder and your host's documented path |
| [Project instructions / Cursor rule](#manual-copy-or-project-instructions) | Your host uses persistent instructions | Its instruction file or Cursor's project rule directory |
| [Claude Code plugin](#claude-code-plugin) | You use Claude Code's plugin manager | Claude Code with plugin support |
| [Manual chat](#try-it-without-installing) | You want to try the instructions without installing | A chat interface that accepts instructions |

### Skills CLI

Discover the skill, then install from your **target project**:

```bash
npx skills add hevertonrodrigues/asdify --list
npx skills add hevertonrodrigues/asdify --skill asdify --agent claude-code
```

Replace `claude-code` with a [Skills CLI agent ID](docs/HARNESSES.md), such as `codex`, `cursor`, `gemini-cli`, `github-copilot`, or `opencode`. Add `--global` for user scope; add `--copy` if you want independent copies instead of symlinks. You can target multiple agents with `--agent claude-code cursor codex`. See the [upstream options](https://github.com/vercel-labs/skills#options) and [full installation guide](INSTALL.md).

`Ok to proceed? (y)` asks permission to download the optional CLI into npm's cache. Enter `y`, or put `--yes` before `skills` to accept that download. A second `--yes` at the end accepts the Skills CLI's installation confirmations. [npm explains the first prompt](https://docs.npmjs.com/cli/v11/commands/npm-exec/#description).

For a user-wide Cursor copy with both confirmations accepted and CLI telemetry disabled:

```bash
DISABLE_TELEMETRY=1 npx --yes skills add hevertonrodrigues/asdify --skill asdify --agent cursor --global --copy --yes
```

This still downloads the CLI and repository when needed. For the local files you already have, the CLI also accepts `npx skills add /path/to/asdify --skill asdify --agent cursor`.

### Local installer without npm

```bash
git clone https://github.com/hevertonrodrigues/asdify.git
cd asdify
bash scripts/install.sh --list
bash scripts/install.sh --agent claude-code --scope user
```

You can use GitHub's **Code → Download ZIP** instead of cloning; extract it and run the same installer commands from that folder. After obtaining the files, the installer performs no downloads or telemetry. It copies the complete skill and references and preserves existing installations unless you pass `--force` after review. Use `--help` for all local options.

For native Cursor, use `cursor-skill` locally. Run the project command from your target project, replacing the source path:

```bash
bash "/path/to/asdify/scripts/install.sh" --agent cursor-skill --scope project
```

For your user account, run `bash scripts/install.sh --agent cursor-skill --scope user` from the ASDify folder. Project files go to `.agents/skills/asdify/`; user files go to `~/.cursor/skills/asdify/`. The local ID `cursor` installs the compact rule; the Skills CLI ID `cursor` installs the native skill. [Compare formats and paths](INSTALL.md#cursor-native-skill-or-compact-rule).

### Manual copy or project instructions

Copy the entire [skills/asdify/](skills/asdify/) folder, including `SKILL.md` and `references/`, into your host's [documented destination](docs/HARNESSES.md). Create parent directories as needed. If ASDify already exists, review it before replacing it. This works without npm, Git, or Bash once you have the files.

If your host uses project instructions, merge [AGENTS.md](AGENTS.md) into its existing instruction file, preserving unrelated rules. For Cursor's compact persistent rule, use `bash "/path/to/asdify/scripts/install.sh" --agent cursor-rule --scope project` from the target project, or copy [cursor-rule.mdc](integrations/cursor-rule.mdc) to `.cursor/rules/asdify.mdc`. The compact adapters contain fewer details than the full skill.

### Claude Code plugin

The repository includes plugin and marketplace manifests. In a Claude Code session:

```text
/plugin marketplace add hevertonrodrigues/asdify
/plugin install asdify@asdify
```

Choose the scope in the plugin manager. You can also add the marketplace from a [local clone](INSTALL.md#claude-code-plugin). The metadata passes repository validation; an actual plugin installation/activation session has not been verified. Follow [Claude Code's plugin guide](https://code.claude.com/docs/en/discover-plugins).

## Supported environments

The [complete harness table](docs/HARNESSES.md) lists **82 installer IDs: 79 upstream agent mappings and 3 compatibility IDs**. It covers coding CLIs and editors such as Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, OpenCode, Windsurf, Cline, Continue, and others. Each entry lists local/CLI IDs, project/user destinations, scope limits, and sources.

On Windows, use the Skills CLI or copy the folder manually. The local script needs Bash and POSIX utilities; if using WSL, install into the environment where your agent reads skills. Automated installer coverage is for Linux/macOS; Windows execution has not been verified. For remote or cloud agents, put project skills in the checkout and follow the host's instructions; local user settings are not proof of remote availability.

For a host outside the table, use its documented skill directory or the manual chat route. `universal` is a shared folder convention. It does not make every application discover skills. [Compatibility](docs/COMPATIBILITY.md) tracks file copying, host activation, and model quality separately.

After installation, start a fresh host session and request `Use asdify full`. In Cursor, inspect **Customize → Skills**; in Claude Code, use the skill or plugin listing available in your version. A successful copy alone does not prove activation.

## Updates and removal

| Installed with | Update | Remove |
| --- | --- | --- |
| Skills CLI | `npx skills update asdify` | `npx skills remove asdify --agent <id>`; add `--global` for a user installation |
| Local installer | Obtain the updated files, review changes, rerun for the same agent/scope with `--force` | Remove only the ASDify directory or rule shown by the installer |
| Manual copy / instructions | Review and replace the ASDify folder or merged text | Remove only that folder or the ASDify instructions |
| Claude Code plugin | Use the plugin manager's update action | Disable or uninstall `asdify@asdify` in the plugin manager |

For a Skills CLI user installation, add `--global` when updating as well as removing. Shared skill directories affect every host that reads them. Keep your own edits before replacing a copy. See [management commands and paths](INSTALL.md#removal-and-updates).

## How ASDify edits

![Four steps: identify the reader, mark the facts that must survive, make the smallest useful edit, and check that the meaning is intact.](assets/readme/how-it-works.svg)

Preserve numbers, dates, conditions, uncertainty, and necessary technical terms. Keep already-clear text. Do not invent advice, decisions, or deadlines during a rewrite.

| Mode | Choose it when… | What changes |
| --- | --- | --- |
| `lite` | You want a light edit | Wording; preserve the layout, order, and tone. |
| `full` · default | You want a clearer answer | Wording and structure, when useful. |
| `ultra` | Your draft has unnecessary framing or sections | More aggressive editing, with the same preservation rules. |

Request a mode with `Use asdify lite`, `full`, or `ultra`. Use `asdify off` to stop applying this optional workflow, subject to the host's other instructions. Modes are instructions; native command support varies by host.

## Languages and translation

English, Brazilian Portuguese, Spanish, French, German, Japanese, Simplified Chinese, Italian, and Russian have READMEs and regression inputs. Install the same canonical skill for every language; no language pack is needed. Rewrites keep the source language unless you request a translation.

```text
Use asdify full. Translate into Spanish (es).
Return only the translation. Preserve every fact and qualification.

Preliminary subscription revenue grew 12% year over year in Brazil,
excluding refunds. These figures are unaudited.
```

Name the target language or locale. ASDify preserves meaning, identifiers, placeholders, and requested formatting, while adapting grammar and register. See [multilingual examples](examples/multilingual.md) and [language coverage and support](docs/LANGUAGES.md). Translation quality depends on the host model; package tests do not verify it.

## Put it to work

| Task | What to protect | Copy a complete prompt |
| --- | --- | --- |
| Executive update | Status, ownership, tentative deadlines, conditions | [Try `full`](examples/recipes.md#1-executive-update-en) |
| Technical recommendation | Identifiers, actor, sequence, recommendation vs. requirement | [Try `lite` · PT-BR](examples/recipes.md#2-technical-recommendation-pt-br) |
| Dense decision brief | Estimates, exclusions, approval requirements | [Try `ultra`](examples/recipes.md#3-dense-decision-brief-en) |
| Already-clear message | The original wording, when no edit is useful | [Try the no-change case](examples/recipes.md#4-leave-clear-text-alone-en) |

## Built to be checked

A shorter answer that changes a material fact fails the evaluation. The repository includes rewrite and translation regression cases across nine languages, a human review rubric, and a [reproducible evaluation protocol](benchmarks/README.md). **Live-model quality gains have not yet been established.** See [package verification](docs/VERIFICATION.md) and [host compatibility](docs/COMPATIBILITY.md) for their separate checks.

## Support and troubleshooting

| Need help with | Start here |
| --- | --- |
| npm confirmation, wrong agent ID, paths, overwrite refusal, or discovery | [Installation troubleshooting](INSTALL.md#troubleshooting) · [Installation report](https://github.com/hevertonrodrigues/asdify/issues/new?template=bug_report.md) |
| Lost facts, changed obligations, wrong language, or invented claims | [Meaning-regression report](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml) |
| Incorrect or outdated translated documentation | [Documentation-translation report](https://github.com/hevertonrodrigues/asdify/issues/new?template=documentation_translation.yml) |
| Another language, host, example, or behavior improvement | [Feature request](https://github.com/hevertonrodrigues/asdify/issues/new?template=feature_request.md) · [Contribution steps](CONTRIBUTING.md) |
| Security or private vulnerability information | [Security policy and private reporting](SECURITY.md) |

Include the exact command or prompt, actual output, OS/host versions, mode, installation scope, and source/target languages where relevant. Remove private information. Already-clear text may stay unchanged. [Support guidance](SUPPORT.md) explains what to check and which evidence to include; [language support](docs/LANGUAGES.md) describes review limits. Use ASDify's issue forms for package problems; account, billing, and host-service problems belong with that provider.

[Roadmap](docs/ROADMAP.md) · [Changelog](CHANGELOG.md) · [MIT license](LICENSE)
