# Launch status and next steps

**ASDify v0.1.0 is public.** The launch record below was checked on **8 October 2026**. Use the [roadmap](ROADMAP.md) for product priorities and [compatibility record](COMPATIBILITY.md) for the limits of host verification.

## Completed

| Item | Recorded result |
| --- | --- |
| Public source | [`hevertonrodrigues/asdify`](https://github.com/hevertonrodrigues/asdify), with main code pushed through [`729b1b7`](https://github.com/hevertonrodrigues/asdify/commit/729b1b7). |
| CI | [Run 37842301297](https://github.com/hevertonrodrigues/asdify/actions/runs/37842301297) passed. This result applies to its recorded revision. |
| First release | [v0.1.0](https://github.com/hevertonrodrigues/asdify/releases/tag/v0.1.0) is live. |
| Repository presentation | Description and nine relevant topics applied, including `claude-skills`; [social preview](../assets/social-preview.png) uploaded. |
| Reproducible example | [One Codex CLI smoke check](demos/codex-full-2026-10-08.md) read the installed skill and retained seven material details after an explicit `full`-mode request. |
| Private reports | GitHub private vulnerability reporting enabled; [security policy](../SECURITY.md) updated. |
| Console.dev | Editorial pitch sent; selection has not been confirmed. |
| Curated skill list | [PR #560](https://github.com/heilcheng/awesome-agent-skills/pull/560) is open: one line in one file, awaiting maintainer review. |

The curated-list contribution uses [the project owner's fork](https://github.com/hevertonrodrigues/awesome-agent-skills) and has no merge conflicts at this check. Its Vercel check requires upstream team authorization to deploy. Separately, the local website build was blocked by Google Geist font downloads. Neither check is recorded as passing.

## Remaining distribution work

- **Changelog:** account setup is complete and the story is prepared. A browser-extension popup interrupted the submit action; receipt is not yet verified. See [submission text and channel notes](launch/submissions.md).
- **SkillsMP:** the `claude-skills` prerequisite topic is present. Indexing remains unverified.
- **skills.sh:** local discovery found one `asdify` skill. Remote discovery was blocked by child Git DNS resolution; installation through the external CLI and indexing remain unverified.
- **Community discussion:** a human author can share a relevant firsthand account where permitted. Follow current posting rules; no Hacker News or r/Codex post has been submitted through this launch work.

## Next 30 days

1. Collect installation reports and meaning-preservation failures. Add a real Portuguese demonstration and record the exact host, model identifier when available, date, and raw output.
2. Test additional hosts and activation modes. Treat the 79 upstream installation mappings as path coverage until a real host session supplies evidence.
3. Run the [comparative evaluation](../benchmarks/README.md) against ordinary and concise-only prompts. Publish settings, failures, and limits as well as favorable results.
4. Review external contributions, respond to editorial or directory feedback, and release fixes supported by reproducible cases.

## Positioning and progress

**Clearer AI writing. Meaning intact.** ASDify is a portable Markdown skill that asks agents to simplify writing while preserving facts, obligations, and uncertainty. Its examples cover English and Brazilian Portuguese. One successful smoke check does not establish broad quality gains or universal host behavior.

Track repeat use, useful external cases, verified installations, contributor activity, and issue response time. Use traffic, stars, forks, and referrals as discovery signals. Editorial selection, directory indexing, and repository rankings are not guaranteed.
