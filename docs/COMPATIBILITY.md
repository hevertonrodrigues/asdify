# Compatibility and verification

ASDify's canonical skill is portable Markdown. Its local registry covers **79 upstream agent mappings plus 3 compatibility IDs**. That is installation coverage for a recorded snapshot, not a claim that every host or model has been tested.

## Registry snapshot

Checked **8 October 2026** against Vercel's [agent registry at commit `05bf93879366fa21c5a4df7482a96adf13beabd2`](https://github.com/vercel-labs/skills/blob/05bf93879366fa21c5a4df7482a96adf13beabd2/src/agents.ts). The complete paths, scope restrictions, and local-versus-CLI IDs are in [HARNESSES.md](HARNESSES.md), derived from [integrations/agents.tsv](../integrations/agents.tsv).

This includes coding CLIs and editor integrations. The generic `universal` entry supplies a conventional directory; it cannot make an arbitrary proprietary host read skills.

## What each check establishes

| Layer | Coverage | Evidence and limits |
| --- | --- | --- |
| Local installer | 82 IDs: 79 upstream mappings and 3 compatibility IDs | Automated checks passed for 160 supported ID/scope installations and rejected 4 unsupported scopes. Includes destinations, full skill/reference copying, path overrides, and overwrite behavior. Copying is not a host session. |
| Skills CLI | Local repository discovery with version 1.7.1 on Node 26.7.0 | `add <local repository> --list` found exactly one skill, `asdify`. Remote discovery was blocked by child Git DNS resolution; installation and skills.sh indexing are unverified. |
| Actual host activation | Codex CLI 0.161.0, explicit ASDify request in `full` mode | One recorded smoke check below. Other hosts, implicit activation, other modes, and reference loading remain unverified. |
| Cursor compact rule | Earlier `.cursor/rules/asdify.mdc` adapter | Separate from Cursor's native skill; no real Cursor session recorded. |
| Claude plugin / marketplace | Local metadata and relative-path validation | No plugin discovery or activation session recorded. |
| ChatGPT / Claude web / other chat interfaces | Manual paste of the instructions and optional references | No native CLI installation or automatic discovery implied; application behavior has not been tested here. |
| Writing effectiveness | Two earlier 100-case paired runs, a 900-case primary study, and a 100-case development subset; nine locales, injected canonical skill/references | [Primary results](../benchmarks/results/2026-10-09-multilingual-modes-four-workers/report.md) and [development decision](../benchmarks/results/2026-10-09-language-guards-development/development-decision.md). Automated synthetic-case comparisons; not general reliability or native host verification. |

The primary study records 100 new cases per language in all four modes: 4,500 answers and 9,000 model ratings. Strict passes are baseline 93.22%, lite 98.22%, full 98.33%, ultra 97.56%, and off 97.67%. Earlier full-mode runs recorded [97/100 versus 92/100](../benchmarks/results/2026-10-08-reliability-100/report.md) and [99/100 versus 91/100](../benchmarks/results/2026-10-09-reliability-100-revised/report.md) on reused cases. Failures, disputed checklist requirements, structural uncertainty, and raw judgments remain visible.

The separate development retest supports retaining the current role/uncertainty rules under its frozen criteria: lite 97→97, full 96→97, and ultra 91→96 strict passes, with six of seven targeted errors absent. The primary table describes the earlier frozen skill; the retest reuses known cases and includes remaining errors and Chinese lite/full declines. One model alias, same-family review, and synthetic samples do not establish general reliability, other models, native activation, or native reference loading; see [language review limits](LANGUAGES.md).

Unknown or newly added hosts should use their documented skill format or the manual instructions until a mapping is reviewed. Upstream registry changes do not automatically update this repository's snapshot.

## Cursor installation paths

Cursor's [current skill documentation](https://cursor.com/docs/skills#skill-directories) confirms `.agents/skills/` for project skills and `~/.cursor/skills/` for user skills, matching the local `cursor-skill` mapping. The installer matrix checks complete skill/reference copying in both scopes. No Cursor host activation session is recorded.

Use the [native Cursor instructions without npm](../INSTALL.md#cursor-without-nodejs-or-npm) to install from a clone. The Skills CLI is optional; npm's package-download confirmation is separate from skill installation. Cursor's [Customize → Skills view](https://cursor.com/docs/skills#viewing-skills) lets users check discovery.

## Recorded host check

| Date | Environment | Host | Model | Scope and activation | Result |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Isolated temporary project on `macOS-27.0.1-arm64` | Codex CLI 0.161.0 | CLI default; model ID not emitted | Project `.agents/skills/asdify/`; explicit request for `full` mode | Read the installed `SKILL.md` and produced a rewrite retaining all seven details in the supplied revenue example. |

See the [command, output, and limits](demos/codex-full-2026-10-08.md). The observed output was:

> Preliminary subscription revenue in Brazil grew 12% year over year, excluding refunds. These figures have not yet been audited.

This check did not establish automatic activation, `lite`/`ultra`/`off` behavior, reference loading, or improvement over a baseline. It does not transfer host-test status to other registry entries.

## Recorded Skills CLI discovery

On 8 October 2026, Skills CLI **1.7.1** on Node **26.7.0** discovered exactly one skill, `asdify`, with `add <local repository> --list`. This checks the repository's skill layout without installing it.

The public-source command, `add hevertonrodrigues/asdify --list`, could not complete because its child Git process could not resolve `github.com` in the sandbox. That is an environment failure, not evidence of package incompatibility. No installation through the external CLI or skills.sh indexing was verified. See the [official CLI documentation](https://www.skills.sh/docs/cli) for the separate discovery and installation commands.

## Add a host check

1. Install using [INSTALL.md](../INSTALL.md) in an isolated project; record installer or CLI version, scope, destination, OS, and host version.
2. Confirm whether the host reads `SKILL.md` and its references. Distinguish an explicit request from automatic discovery.
3. Run a complete [recipe](../examples/recipes.md), recording the exact model identifier where available and the raw output.
4. Check every material invariant, plus any modes you actually test. Record failures and untested behavior.
5. Add dated evidence and update only the claims that evidence supports.

Local package checks, remote CI, host activation, and model quality are separate results. Refer to the [verification report](VERIFICATION.md) for the recorded package/CI status; a configured workflow alone is not a completed run.
