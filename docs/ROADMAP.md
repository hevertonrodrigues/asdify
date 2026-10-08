# Roadmap

Make the skill useful enough that people keep using it and contribute the cases it gets wrong. Stars are a discovery signal, not an acceptance test.

## 1. A credible first release

- [x] Put a complete preservation example and copyable first-use prompt in both READMEs.
- [x] Add task recipes and separate meaning-regression and installation reports.
- [x] Add original SVG explanations in English and Portuguese, with copyable example text.
- [x] Make host installation choices independent and validate README image links.
- [x] Expand regression inputs for modality, negation, ordered steps, citations, contradictions, and already-clear text.
- [x] Reject malformed evaluation data and support repeated paired runs.
- [x] Select ASDify and `hevertonrodrigues/asdify`; put the product at the repository root and update clone URLs.
- [x] Publish [hevertonrodrigues/asdify](https://github.com/hevertonrodrigues/asdify).
- [ ] Verify a fresh clone using the public README.
- [x] Record one explicit Codex `full`-mode smoke check in [COMPATIBILITY.md](COMPATIBILITY.md).
- [ ] Add real host checks for other integrations and modes; keep untested installation mappings clearly labeled.
- [x] Run the configured GitHub Actions matrix on the published repository and publish [v0.1.0](https://github.com/hevertonrodrigues/asdify/releases/tag/v0.1.0) with exact limitations. See the [recorded CI result](LAUNCH.md).

**Done when:** a new user can follow the public README, invoke the skill, and inspect a concrete output without maintainer help. A fresh-clone check remains outstanding.

## 2. Evidence for the central claim

- [ ] Compare the skill against both an ordinary baseline and a concise-only instruction using the [evaluation protocol](../benchmarks/README.md).
- [ ] Freeze at least 24 held-out cases, balanced between English and Portuguese, before generating outputs. This is a pilot target, not a statistical power guarantee.
- [ ] Include long summaries and mixed failure cases, with at least two distinct models (recording each exact version) and two independent reviewers.
- [ ] Publish anonymized raw outputs, settings, reviewer scores, failures, and limitations in `benchmarks/results/`.
- [ ] Revise the skill only after examining failures, then evaluate a fresh held-out set.

**Done when:** a reader can reproduce the study and see whether clarity improved without a material-fidelity regression. If the concise-only prompt performs as well, publish that finding and revise the product's claim.

## 3. Useful contributions and discovery

- [x] Offer small first contributions: one anonymized failure case, one native-speaker review, or one verified host check.
- [ ] Review incoming cases, reproduce them, add regressions, and document the behavior change in the changelog.
- [x] Publish a [real Codex demonstration](demos/codex-full-2026-10-08.md) with command, output, host version, and date; disclose that the model identifier was not emitted.
- [ ] Add a Portuguese demonstration and further checks with exact model identifiers where available.
- [x] Add relevant GitHub topics and submit [one curated-list PR](https://github.com/heilcheng/awesome-agent-skills/pull/560), awaiting maintainer review.
- [ ] Verify marketplace indexing and complete remaining editorial submissions. See [launch status](LAUNCH.md).
- [ ] Consider a small static example gallery only after the README and install paths work for new users.

**Done when:** outside users submit useful counterexamples and evidence of repeat use. Review these signals monthly alongside issue response time and release reliability.

## Scope

Keep one canonical skill with optional references and small host adapters. Add a new language or integration when a contributor can verify it. A hosted editor, model gateway, telemetry service, and large plugin framework are outside the first release.

See the [launch record](LAUNCH.md) for completed publication work and remaining distribution steps. These milestones do not promise a ranking, star count, or release date.
