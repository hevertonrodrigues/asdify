# Launch playbook (no ranking guarantees)

Use the [roadmap](ROADMAP.md) to prioritize the work and the [compatibility record](COMPATIBILITY.md) to distinguish package checks from verified host behavior. The product files live at the repository root. Development history and research are preserved in the [project archive](archive/INDEX.md).

## Positioning

**Name:** ASDify

**Owner:** `hevertonrodrigues`

**Publication target:** [hevertonrodrigues/asdify](https://github.com/hevertonrodrigues/asdify). The owner and name are selected; this checklist does not establish that publication or remote CI has completed.

**Repository description (copy/paste):** `Clearer AI writing. Meaning intact. A portable agent skill for Claude Code, Codex, and Cursor, with English and Portuguese examples.`

ASDify is independently authored and inspired by public controlled-language principles associated with ASD-STE100. It does not claim compliance, certification, affiliation, or endorsement.

**Suggested topics** (within GitHub's 20-topic limit): `agent-skills`, `ai-agents`, `prompt-engineering`, `plain-language`, `technical-writing`, `writing-assistant`, `claude-code`, `codex`, `cursor`, `llm`, `communication`, `documentation`, `open-source`, `business-writing`, `simplification`.

**Social tagline:** `Clearer AI writing. Meaning intact.`

## T-minus release

1. Configure a maintainer contact or private vulnerability reporting channel for `hevertonrodrigues/asdify`.
2. Publish the prepared root and verify the documented clone command against the public repository.
3. Test on actual current versions of Claude Code, Codex, and Cursor. Mark tested dates in docs. Confirm the Claude marketplace manifest works before advertising plugin commands.
4. Enable GitHub Actions, Issues, Discussions (if you can moderate), and private vulnerability reporting where available.
5. Publish a tagged `v0.1.0` after validation. Include examples, compatibility and limitations in release notes.
6. Add the short description and topics in GitHub settings. Use the original SVGs in `assets/readme/` as the visual source for a social preview. Export a preview to a GitHub-supported raster format before upload.

## First 30 days

**Week 1:** publish one real, reproducible before/after demo in EN and PT-BR; release installation notes and collect issue reports. Demonstrate number/uncertainty preservation, not just shorter text.

**Week 2:** run and publish a blinded A/B evaluation with model version, cases, and counterexamples. Update rules only after analyzing failure cases.

**Week 3:** test alternative model/agent hosts; accept integration PRs only with installation evidence; share substantive demos in relevant GitHub/Agent Skills communities, following each community's posting rules.

**Week 4:** package the first stable release based on the public regression suite. Publish failures and the fixes as openly as successes.

## Distribution, responsibly

- Submit to Agent Skills/community directories that accept open submissions and where the package matches requirements. Follow directory rules; do not spam.
- Publish practical technical posts, including preservation failures and how they were resolved. Link to the source and methodology.
- Keep README search terms accurate and natural; avoid keyword stuffing or fake star/review campaigns.
- Encourage contributions and external reproduction rather than incentivized stars.

## Differentiation vs Ponytail

Ponytail minimizes implementation complexity in code. ASDify minimizes reader effort across AI writing tasks. Share its philosophy of minimum sufficient work and reproducible evidence, but use independent examples, copy, rules and visual identity.

## Success metrics to monitor

- Monthly unique external contributors, issue resolution time, install instructions tested, and documented compatibility.
- Reproducible quality/fidelity gains and hard-failure rate on held-out tasks.
- Repository traffic, stars, forks and referrals as interest signals, **not** proof of quality.

No listing, search position or virality is guaranteed.
