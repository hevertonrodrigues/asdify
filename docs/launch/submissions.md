# Launch submissions

Status recorded **8 October 2026**. The [release](https://github.com/hevertonrodrigues/asdify/releases/tag/v0.1.0) is public; this page separates completed outreach from prepared or unverified work. See the [launch record](../LAUNCH.md) for publication and CI evidence.

## Changelog: submitted

The story below was sent through [Submit news](https://changelog.com/news/submit) on 8 October 2026. **The site confirmed receipt: “We received your submission!”** This establishes submission, not editorial acceptance or publication. Changelog accepts creators' own open-source work; selection is discretionary. This is an editorial submission, not a paid sponsorship.

**URL**

```text
https://github.com/hevertonrodrigues/asdify
```

**Title**

```text
ASDify: a portable clear-writing skill for AI agents
```

**What's interesting about it?**

```text
I'm ASDify's creator. It's an MIT-licensed Markdown skill for making AI-written updates, explanations, and documentation clearer while preserving facts, obligations, and uncertainty.

The repository includes English and Portuguese examples, a paste-and-try path, and a local installer with 79 upstream agent mappings plus 3 compatibility IDs. Those are installation paths, not a claim that every host has been tested.

One recorded Codex CLI 0.161.0 run read the installed skill after an explicit full-mode request and retained all seven material details in a revenue update. The command, output, and limits are public. Broad quality gains and automatic activation remain unverified; reproducible failure cases and additional host checks are welcome.

Demo: https://github.com/hevertonrodrigues/asdify/blob/main/docs/demos/codex-full-2026-10-08.md
Release: https://github.com/hevertonrodrigues/asdify/releases/tag/v0.1.0
```

## Sent or awaiting indexing

| Channel | Status | Next step |
| --- | --- | --- |
| Console.dev | Editorial pitch sent; no acceptance recorded. | Await a response. Its [selection criteria](https://console.dev/selection-criteria) distinguish editorial review from paid advertising; it does not sell reviews. |
| awesome-agent-skills | [PR #560](https://github.com/heilcheng/awesome-agent-skills/pull/560) is open, with no merge conflicts at this check. | Await maintainer review and upstream Vercel deployment authorization. Separately, the local website build was blocked by Google Geist downloads. |
| SkillsMP | `claude-skills` topic added; indexing unverified. | Check the [marketplace](https://skillsmp.com/) for the exact source repository before claiming a listing. A topic is not proof of indexing or endorsement. |
| skills.sh | Skills CLI 1.7.1 on Node 26.7.0 discovered exactly one skill from the local repository. Remote discovery failed on child Git DNS resolution. | Retry public-source discovery when networking permits, then separately verify an installation and any public listing. |

Public-source discovery command, following the [official CLI documentation](https://www.skills.sh/docs/cli):

```bash
npx skills add hevertonrodrigues/asdify --list
```

This lists discoverable skills; it does not install one or establish indexing. Record the CLI version and result before updating the launch status.

## Hacker News and r/Codex: human authorship only

Do not copy generated submission text into these channels. The owner should write any post personally and handle the discussion.

[Hacker News guidelines](https://news.ycombinator.com/newsguidelines.html), checked 8 October 2026, prohibit generated submission text, generated or AI-edited comments, and automated posting. They also prohibit soliciting votes. [Show HN rules](https://news.ycombinator.com/showhn.html) require something people can try, personally worked on by its author, who is available to discuss it. Whether this project fits is for the community to judge.

Before posting to r/Codex, read its [current community rules](https://www.reddit.com/r/codex/about/rules/) and inspect the [current community threads](https://www.reddit.com/r/codex/) for the allowed showcase format. No automated post or ready-to-submit Reddit copy is provided here.

Facts a human author can discuss in their own words:

- Their personal reason for building ASDify and the actual writing problems they encountered.
- The difference between a shorter sentence and a rewrite that preserves meaning; use a concrete case they checked.
- The recorded Codex command and output, including the explicit request, missing model identifier, and untested behavior.
- The manual trial and source files readers can inspect without an account.
- A specific request for counterexamples or host reports, with creator affiliation clear and no request for votes or stars.

No community post, editorial acceptance, or marketplace listing is implied by this preparation.
