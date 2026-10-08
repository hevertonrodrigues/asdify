# A recorded ASDify run in Codex

On 8 October 2026, Codex CLI 0.161.0 loaded ASDify from an isolated project's `.agents/skills/asdify/SKILL.md` and produced the response below. This is one observed run, not evidence of average quality gains.

## Input

```text
Use the installed asdify skill in full mode. Rewrite this update for an executive. Return only the rewritten text, preserving every fact and qualification: We would like to highlight that preliminary subscription revenue grew 12% year over year in Brazil, excluding refunds. These figures have not yet been audited.
```

## Actual final response

> Preliminary subscription revenue in Brazil grew 12% year over year, excluding refunds. These figures have not yet been audited.

All seven material details survived: preliminary status, subscription revenue, 12% growth, year-over-year comparison, Brazil, refund exclusion, and unaudited status.

## How it was checked

The JSON event stream recorded `cat .agents/skills/asdify/SKILL.md` completing with exit code 0 before the final response. The skill was explicitly requested in `full` mode. The CLI used its default model; the exact model identifier was not emitted in this JSON stream. The CLI also emitted a progress message before loading the skill, so the full interaction was not limited to the rewrite.

Reproduce from an isolated project after installing ASDify for Codex:

```bash
codex exec --ignore-user-config --ephemeral --sandbox read-only \
  --skip-git-repo-check --json \
  'Use the installed asdify skill in full mode. Rewrite this update for an executive. Return only the rewritten text, preserving every fact and qualification: We would like to highlight that preliminary subscription revenue grew 12% year over year in Brazil, excluding refunds. These figures have not yet been audited.'
```

CLI authentication is required. This run does not establish automatic activation, optional reference loading, other modes, or behavior in other hosts. The [structured record](codex-full-2026-10-08.json) preserves the prompt, observed file read, output, and review. For comparative studies, use the [evaluation protocol](../../benchmarks/README.md).
