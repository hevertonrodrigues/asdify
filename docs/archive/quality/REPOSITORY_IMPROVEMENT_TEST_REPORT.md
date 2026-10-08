# Repository improvement verification

Date: 8 October 2026. This report is historical and covers the research and implementation pass before the rename; paths have been updated to the current layout. `TEST_REPORT.md` preserves the earlier packaging-time result. See [ASDify release checks](ASDIFY_RELEASE_CHECK.md) for current verification.

## Results

Executed from the then-nested product directory (now the repository root) on Darwin 27.0.0 with Python 3.14.6:

| Check | Result |
| --- | --- |
| `python3 scripts/validate.py` | PASS: core skill, local plugin metadata, relative links, 16 bilingual cases |
| `python3 -m unittest discover -s tests -v` | PASS: 30 tests, exit code 0 |
| `bash -n scripts/install.sh` | PASS, exit code 0 |
| New issue-form YAML and required fields | Parsed and checked during documentation review |
| Recipe section links and whitespace/conflict-marker checks | PASS during documentation review |
| Original v0.1 ZIP checksum | Matches the original package manifest; archive unchanged |
| Independent research/documentation review | No blockers; clarified the two-distinct-model target |

The regression suite checks malformed and duplicate CSV headers, truncated/extra rows, valid score ranges, missing identities, pairing, repetition IDs, descriptive numeric results, fixture types/language coverage, manifest consistency, and safe local installer behavior. Installer tests use temporary projects and include complete Codex skill/reference copying, overwrite refusal, and symlink refusal.

## What these checks establish

The local tooling accepts valid inputs and rejects the covered malformed inputs. Documentation links resolve within the repository. The test data contains eight English and eight Brazilian Portuguese scenarios.

These checks do not evaluate live AI writing. The new preservation scenarios are inputs awaiting model outputs and human review, not assertions that a model already passes them. The validator checks this repository's local structure and manifests; it is not a full implementation of every host's plugin schema or the entire Agent Skills specification.

## Remaining verification

- GitHub Actions is configured for Linux/macOS and Python 3.12/3.13. That remote matrix has not been executed in this local workspace; the passing local environment is listed above.
- Real Claude Code, Codex, Cursor, and marketplace activation remain unverified. No global/user installation was performed.
- No live model evaluation, independent human rating study, statistical significance test, or performance measurement was performed.
- No repository had been created, pushed, tagged, or published during that review. Git metadata was absent then; Git was initialized and commits added afterward.
- The owner was not selected during that review. The subsequent ASDify publication target is `hevertonrodrigues/asdify`.

See the [research and implementation review](../strategy/GITHUB_REPOSITORY_REVIEW.md) and the [public roadmap](../../ROADMAP.md) for priorities.
