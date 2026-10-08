# ASDify

![ASDify — Clearer AI writing. Meaning intact.](assets/readme/hero.svg)

[![License: MIT](https://img.shields.io/badge/license-MIT-18283b?style=flat-square)](LICENSE)
[![Format: portable Markdown](https://img.shields.io/badge/format-portable%20Markdown-18283b?style=flat-square)](skills/asdify/SKILL.md)
[![Examples: EN and PT-BR](https://img.shields.io/badge/examples-EN%20%2B%20PT--BR-dba44e?style=flat-square)](examples/before-after.md)

[Português (Brasil)](README.pt-BR.md) · [Try it](#try-it-without-installing) · [Install](#install-for-your-agent) · [Recipes](examples/recipes.md) · [Contribute](CONTRIBUTING.md)

Give your AI agent a repeatable editing routine: find the point, remove filler, and check that the important details survive. ASDify is a small, portable Markdown skill for answers, status updates, reports, and documentation across supported coding agents and editors.

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

## Install for your agent

Use the [Skills CLI](https://github.com/vercel-labs/skills) to discover ASDify and install it for your agent:

```bash
npx skills add hevertonrodrigues/asdify --list
npx skills add hevertonrodrigues/asdify --skill asdify --agent claude-code
```

Replace `claude-code` with your [supported agent ID](docs/HARNESSES.md), such as `codex`, `cursor`, `gemini-cli`, or `opencode`. Run from your target project; add `--global` for user-wide installation where supported. See the [full installation guide](INSTALL.md) for scopes, paths, and removal.

<details>
<summary><strong>Prefer the local installer?</strong></summary>

```bash
git clone https://github.com/hevertonrodrigues/asdify.git
cd asdify
bash scripts/install.sh --list
bash scripts/install.sh --agent claude-code --scope user
```

Choose an ID from `--list`. This installer copies the complete skill and its references from the clone, without downloading anything, and refuses to overwrite existing files unless you pass `--force`.

For native Cursor skills, its local ID is `cursor-skill`; `cursor` preserves the earlier compact project-rule adapter. The Skills CLI uses `cursor` for native skills. [See the distinction and paths](INSTALL.md#cursor-native-skill-or-compact-rule).

</details>

The [harness table](docs/HARNESSES.md) covers the supported registry snapshot. Installation layout checks and actual host sessions are tracked separately in [compatibility](docs/COMPATIBILITY.md). For a host outside the table, use its documented skill path or the manual chat trial above.

## How ASDify edits

![Four steps: identify the reader, mark the facts that must survive, make the smallest useful edit, and check that the meaning is intact.](assets/readme/how-it-works.svg)

Preserve numbers, dates, conditions, uncertainty, and necessary technical terms. Keep already-clear text. Do not invent advice, decisions, or deadlines during a rewrite.

| Mode | Choose it when… | What changes |
| --- | --- | --- |
| `lite` | You want a light edit | Wording; preserve the layout, order, and tone. |
| `full` · default | You want a clearer answer | Wording and structure, when useful. |
| `ultra` | Your draft has unnecessary framing or sections | More aggressive editing, with the same preservation rules. |

Request a mode with `Use asdify lite`, `full`, or `ultra`. Use `asdify off` to stop applying this optional workflow, subject to the host's other instructions. Modes are instructions; native command support varies by host.

## Put it to work

| Task | What to protect | Copy a complete prompt |
| --- | --- | --- |
| Executive update | Status, ownership, tentative deadlines, conditions | [Try `full`](examples/recipes.md#1-executive-update-en) |
| Technical recommendation | Identifiers, actor, sequence, recommendation vs. requirement | [Try `lite` · PT-BR](examples/recipes.md#2-technical-recommendation-pt-br) |
| Dense decision brief | Estimates, exclusions, approval requirements | [Try `ultra`](examples/recipes.md#3-dense-decision-brief-en) |
| Already-clear message | The original wording, when no edit is useful | [Try the no-change case](examples/recipes.md#4-leave-clear-text-alone-en) |

## Built to be checked

A shorter answer that changes a material fact fails the evaluation. The repository includes English and Portuguese regression cases, a human review rubric, and a [reproducible evaluation protocol](benchmarks/README.md). **Live-model quality gains have not yet been established.** See [package verification](docs/VERIFICATION.md) and [host compatibility](docs/COMPATIBILITY.md) for their separate checks.

Found a lost condition, changed number, or invented promise? [Report a meaning regression](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml). A small anonymized example makes a useful first contribution. See [CONTRIBUTING.md](CONTRIBUTING.md) for the steps.

[Roadmap](docs/ROADMAP.md) · [Changelog](CHANGELOG.md) · [MIT license](LICENSE)
