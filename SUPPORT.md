# Support

Use ASDify's issue forms for problems with the skill files, local installer, adapters, documentation, and regression fixtures. Account access, billing, outages, and bugs in a host or third-party CLI belong with that provider.

| Problem | Help and reporting |
| --- | --- |
| Install command, scope, path, overwrite refusal, or missing skill | [Installation guide](INSTALL.md) · [Installation report](https://github.com/hevertonrodrigues/asdify/issues/new?template=bug_report.md) |
| A rewrite or translation changes meaning, language, obligations, or certainty | [Meaning-regression form](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml) |
| Incorrect or outdated translated README | [Documentation-translation form](https://github.com/hevertonrodrigues/asdify/issues/new?template=documentation_translation.yml) |
| New language, host mapping, recipe, or behavior | [Feature request](https://github.com/hevertonrodrigues/asdify/issues/new?template=feature_request.md) · [Contributing](CONTRIBUTING.md) |
| Vulnerability or information that must stay private | [Security policy](SECURITY.md) and its private reporting route |

Reports may use any of the [nine covered languages](docs/LANGUAGES.md). A reply in the same language is not guaranteed. The new translations still need independent native-speaker review.

## Check installation and discovery

1. Identify the method and scope: Skills CLI, local Bash installer, manual copy, project instructions, Cursor rule, or Claude plugin; project/user scope, or a plugin's local scope.
2. Compare the destination with [HARNESSES.md](docs/HARNESSES.md) or your host's documentation. A full skill needs `asdify/SKILL.md` and its complete `references/` folder. The compact Cursor rule is a separate format.
3. Check your host's listing or plugin manager, then start a fresh session and explicitly request `Use asdify full`. Check which filesystem the host uses on Windows, WSL, remote, or cloud setups.
4. Run a [complete recipe](examples/recipes.md). Distinguish a copying failure, discovery failure, and wrong output; they need different evidence.

An npm `Ok to proceed? (y)` prompt is the optional Skills CLI download confirmation. It is expected. `npx --yes` accepts that download; the CLI's final `--yes` accepts its own installation prompts. To avoid the CLI download, use local Bash installation or manual copy. See [prompt details](INSTALL.md#skills-cli).

Existing files are preserved by the local installer unless you choose `--force`. Review an existing copy first; it may be shared by several hosts. Already-clear text can correctly remain unchanged, and native commands or automatic activation vary by host.

## Include useful evidence

For installation reports, include the exact command, working directory with private path segments removed, error output, method, scope, OS/host versions, and ASDify version or commit. Say whether the files were copied, whether the host lists the skill, and what you tried in a fresh session. For a plugin, include its manager's status and scope.

For meaning or translation reports, include the complete prompt, anonymized source, actual output, requested mode, source/target languages and variant, model/host versions where known, and the exact fact or relationship that changed. Describe the required meaning; one exact preferred sentence is optional. Label constructed examples as illustrative rather than reproduced model failures.

For translated documentation, identify the README and section, current wording, proposed correction if known, and the corresponding English source. For a new host or language, contribute a documented path or original cases and say what you have actually verified.

Remove secrets and private source documents before filing public issues. Use [SECURITY.md](SECURITY.md) for private vulnerability information.

## Verification limits

The [compatibility record](docs/COMPATIBILITY.md) separates registry mappings, installation checks, actual host activation, and model effectiveness. Package validation and the installer matrix do not establish that every host loads the skill or that translations are accurate. See [VERIFICATION.md](docs/VERIFICATION.md), [language review limits](docs/LANGUAGES.md), and the [evaluation protocol](benchmarks/README.md) for the evidence available.
