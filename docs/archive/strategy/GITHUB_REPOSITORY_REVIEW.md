# ASDify: repository review and adoption plan

Reviewed 8 October 2026. Scope: the complete context package, its original references, the editable repository, and eight public GitHub comparators. Local improvements are implemented in `./`; no GitHub publication or live model evaluation was performed.

## Decision

Build **the small, verifiable skill for making AI writing clearer while keeping its meaning**. The useful distinction is fidelity: amounts, dates, exclusions, recommendations, uncertainty, and source attribution must survive. Lead with that distinction, let people try it immediately, and make every failure a contribution opportunity.

The original draft already had most repository scaffolding: license, contribution guide, security policy, issue templates, a portable skill, installer, examples, and a benchmark protocol. The highest-value work is better first use, stronger checks, and credible behavioral evidence. More boilerplate or a large application would not address the main gaps.

Popularity is an outcome to pursue through usefulness and maintenance. The comparisons below show observable practices, not a formula for GitHub Trending or evidence that a particular README causes stars.

## What was reviewed

The product intent and references came from `READ_ME_FIRST.md`, `history/`, `strategy/`, and `quality/SOURCES_AND_ATTRIBUTION.md`. The engineering review covered the canonical skill and references, both READMEs, installer, adapters, manifests, fixtures, scoring, tests, and CI.

At the time of this review, the package had no Git metadata and the product was nested inside it. The later ASDify rename moved the product to the repository root and retained the surrounding history and original ZIP as context. The review findings below describe the initial draft; current release checks are recorded separately.

### References supplied with the project

- **Ponytail:** inspected its current README, installation model, and evaluation/test material. Transfer its inspectable core, examples, and evidence discipline. Its coding persona, benchmarks, and feature inventory belong to that project. [Source](https://github.com/DietrichGebert/ponytail)
- **Agent Skills specification:** keep the `SKILL.md` package, focused metadata, and optional reference files. The existing small core fits the documented progressive-loading structure. [Specification](https://agentskills.io/specification)
- **ASD-STE100:** preserve the attribution and explicit non-compliance statement. The official site returned a fetch error/403 during this review, so no current specification details or dictionary content were verified or imported. [Official site](https://www.asd-ste100.org/)
- **Original Reel:** used the user-supplied transcript in the package as historical context. The audiovisual source was not independently verified.

## What prominent repositories actually do

This is a purposive sample of large educational repositories and directly relevant skill/prompt projects, not the eight highest-starred repositories on GitHub. Stars were fetched from GitHub's public REST API on 8 October 2026; the [machine-readable snapshot](../quality/github-research-snapshot.json) records sources and counts. README pages may show rounded or cached totals.

| Repository | Stars at collection | Observed structure and behavior | Application here |
| --- | ---: | --- | --- |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 516,251 | Categorized navigation, explicit acceptance criteria, contributor instructions, automated linting | Curate useful examples and require one reproducible failure with preserved facts per behavior contribution |
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 456,725 | Direct paths into a usable learning product, topic-based entry points, visible contribution and support routes | Give visitors complete task recipes and a clear first contribution |
| [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 368,971 | Task/role navigation, interactive content, small Markdown contribution units, documented content structure | Organize by executive updates, technical writing, decision briefs, and minimal editing; make one case easy to improve |
| [obra/superpowers](https://github.com/obra/superpowers) | 296,498 | A documented behavioral workflow, host-specific installation, real-agent activation tests | Distinguish files copied, skill activated, and behavior verified; test each separately |
| [anthropics/skills](https://github.com/anthropics/skills) | 179,976 | Self-contained skill folders, templates, marketplace manifests, comparative skill evaluation | Keep a portable canonical skill and small adapters; evaluate both appropriate activation and output |
| [f/prompts.chat](https://github.com/f/prompts.chat) | 172,164 | Multiple immediate ways to use prompts, plain-text access, contributor guidance | Allow a manual no-install trial and complete copyable prompts before requiring setup |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 158,208 | One memorable promise, concrete transformations, canonical prompt, adapters, published evaluation | Show the meaning-preservation benefit first and attach measured evidence to future claims |
| [openai/skills](https://github.com/openai/skills) | 27,941 | Current README marks the repository deprecated and points to OpenAI Plugins | Make lifecycle and compatibility status visible; recheck distribution advice instead of copying historical installation instructions |

The developer-roadmap URL supplied under `kamranahmedse` redirects to `nilbuild`; the former `f/awesome-chatgpt-prompts` project is now `f/prompts.chat`. Current locations are used above.

### Specific implementation patterns worth borrowing

**Small core, optional depth.** Keep `skills/asdify/SKILL.md` canonical, with focused references loaded as needed. Validate manifests and relative links instead of multiplying manually maintained copies. Anthropic's [marketplace manifest](https://github.com/anthropics/skills/blob/main/.claude-plugin/marketplace.json) is an example of a wrapper pointing at skill folders.

**Test behavior and activation independently.** Superpowers tests an explicit skill request by launching the host and inspecting a transcript. Borrow the principle at a much smaller scale: install, confirm discovery, invoke, inspect the output, record host/model versions. [Activation test](https://github.com/obra/superpowers/blob/main/tests/explicit-skill-requests/run-test.sh), [integration PR requirements](https://github.com/obra/superpowers/blob/main/.github/PULL_REQUEST_TEMPLATE.md).

**Make bad outputs visible.** Ponytail's grader tests include known-good and known-bad responses. This project should eventually calibrate reviewers or any automated evaluator against dropped exceptions, changed obligations, reversed negation, and invented certainty. [Behavior tests](https://github.com/DietrichGebert/ponytail/blob/main/tests/behavior.test.js).

**Evaluate the real differentiator.** Ponytail's October 7 report itself says shorter replies did not produce a statistically significant blinded quality advantage over the no-skill baseline. That is its reported result, not one reproduced here. Our study needs both task-only and concise-only controls, and fidelity must constrain any readability win. [Reported study and limitations](https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/results/2026-10-07-agentic.md).

**Keep contribution units small.** A case plus its expected facts is easier to review than a broad style rewrite. Awesome publishes [acceptance criteria](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md); prompts.chat asks for tested contributions in its [contribution guide](https://github.com/f/prompts.chat/blob/main/CONTRIBUTING.md). This project now has a specific meaning-regression form.

## Findings and changes made

| Priority | Finding in the initial draft | Implemented response |
| --- | --- | --- |
| P0 | First-use prompt ended in `...`; the generic filler example concealed the distinctive value | Preservation-sensitive examples first, complete EN/PT prompts, manual trial, task recipes |
| P0 | Portuguese example changed a recommendation into an imperative | Corrected the example and added a regression input preserving recommendation, client, header, and ordering |
| P0 | Truncated ratings could produce an uncaught `int(None)` error | Validate headers and row widths before parsing; provide clean input errors and regression tests |
| P0 | Fixture validation accepted boolean tasks, non-string invariants, and English-only sets | Require valid field types and both languages; test malformed fixtures |
| P1 | Repeated experiments were described but duplicate pair keys prevented repeated runs | Optional `run_id` support with complete pairing per reviewer/case/run; legacy single-run files still work |
| P1 | Benchmark only compared task-only baseline against the skill | Separate baseline-vs-skill and concise-vs-skill studies, held-out guidance, metadata template, publication location |
| P1 | Eight short fixtures missed several central fidelity risks | Sixteen balanced EN/PT inputs, adding no-op, negation, order, citations, conflicts, exact quote, voice, and recommendation cases |
| P1 | Support wording could be mistaken for demonstrated host compatibility | A visible compatibility table separates package checks from actual host evidence |
| P1 | Generic issue forms made semantic failures harder to reproduce | Dedicated meaning-regression form and contribution guidance |
| P1 | CI checked only one Linux/Python configuration | Linux/macOS × Python 3.12/3.13 workflow, shell syntax check, broader local regression coverage |

The core skill and its public claims remain deliberately small. Script tests verify tooling behavior; they do not prove that a model preserves meaning. See the [current verification report](../quality/REPOSITORY_IMPROVEMENT_TEST_REPORT.md).

## Next work, in order

| Stage | Concrete deliverable | Acceptance criterion |
| --- | --- | --- |
| First public prerelease | Use the selected owner and root layout, test hosts, publish repository and tagged release | A new user completes README installation and a recipe unaided; compatibility evidence is recorded |
| Behavioral pilot | At least 24 frozen held-out cases, two languages, two models, two independent reviewers; two comparison studies | Raw outputs, failures, metadata and blinded ratings published; no unsubstantiated winner claims |
| Community iteration | Recruit target users with real writing tasks; accept anonymized failures and native-language reviews | Each confirmed failure becomes a fixture and any behavior change gets a documented regression check |
| Focused distribution | Short real-output demonstration, honest release notes, relevant topics, allowed directory submissions | Visitors can reach an example and working install directly from every announcement |
| Optional gallery | A simple browsable example page after repeated demand | Helps users find applicable examples; adds no account or model-service requirement |

These are recommended targets, not commitments or statistically powered sample sizes. The public [roadmap](../../ROADMAP.md) and [launch playbook](../../LAUNCH.md) carry the next steps into the repository.

## How to tell whether this is working

Measure usefulness before popularity:

- **Activation:** fraction of observed new-user trials that complete installation, invocation, and one checked example. Use opt-in user reports; this package adds no telemetry.
- **Fidelity:** material-failure rate per output, with reviewer disagreement visible; track by case type and language.
- **Reader value:** blinded preference and clarity scores against both controls, plus the cases where the skill loses.
- **Retention:** evidence that pilot users return for a second real task, collected with their consent.
- **Community health:** actionable external counterexamples, contributor follow-through, response time, and verified host reports.
- **Reach:** traffic and stars as secondary indicators after publication. Download or clone totals alone cannot establish active use.

Avoid copying a large framework, creating a hosted editor before demand, broadening language claims without native review, importing another project's benchmark numbers, or decorating the README with unsupported badges. GitHub's [community profile](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories) identifies useful contribution files; it does not certify product quality or confer ranking.
