# Compatibility and verification

The repository supplies a portable skill and a compact Cursor rule. A successful file copy confirms installation layout; it does not confirm that a host loads or follows the instructions.

## Evidence as of 8 October 2026

| Integration | Package checks | Actual host session |
| --- | --- | --- |
| Claude Code skill | Local installer tests; canonical skill and references copied | Not verified; record client/model versions before claiming support |
| Codex skill | Local installer tests; canonical skill and references copied | Not verified; record client/model versions before claiming support |
| Cursor project rule | Local installer test; compact adapter copied | Not verified; test rule loading and interaction with other project rules |
| Claude plugin / marketplace | Local JSON and relative-path validation | Not verified; plugin discovery and activation still need a real host check |
| Other Agent Skills hosts | Portable folder follows the documented format | No host-specific verification recorded |

Automated checks use temporary projects. User-scope installations, discovery, activation, mode changes, and actual response quality need separate evidence. The CI workflow is configured for Linux/macOS with Python 3.12/3.13; a workflow definition alone is not a passing CI run.

The current fixture set covers English and Brazilian Portuguese. Applying the principles to other languages is a design intention, not validated language coverage.

## Record a host check

Add a dated row below after a real test, including a link to anonymized evidence:

| Date | OS | Host + version | Model + version | Install path / scope | Activation and mode check | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| — | — | No completed host checks | — | — | — | — |

1. Install using [INSTALL.md](../INSTALL.md) in an isolated project.
2. Confirm the host discovers the skill or rule and loads its references.
3. Run a complete [recipe](../examples/recipes.md), then check each invariant in the source against the output.
4. Try `lite`, `full`, `ultra`, and `off`. Record what the host actually does; these modes are instructions, not guaranteed native commands.
5. Check overwrite refusal and removal of only the installed project files.
6. Record failures as well as successes. Keep installation evidence separate from [model evaluation](../benchmarks/README.md).

Host behavior changes. Recheck the relevant official host documentation and current client version before advertising a new installation method.
