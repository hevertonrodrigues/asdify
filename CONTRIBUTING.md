# Contributing

Help people read and verify AI output more easily. A small example where simplification loses meaning is a useful first contribution.

## Report a meaning regression

Open a [meaning-regression report](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml). Include:

- The original input and the actual output, with private information removed.
- The exact fact, condition, obligation, uncertainty, or relationship that changed.
- The intended reader, requested task, and skill mode.
- For a translation, source and target languages and any regional or script variant.
- Host and version, model identifier, skill version or commit, and run date, where known.

For example: “The source recommends waiting before retrying; the output makes it mandatory.” An expected rewrite is helpful but optional. Describe the required meaning even if you do not know the best wording. Label invented demonstrations as illustrative; use actual model output when reporting a reproduced failure.

If the installer fails or the host cannot find the skill, use the [installation report](https://github.com/hevertonrodrigues/asdify/issues/new?template=bug_report.md) instead. Include the exact command, working directory, error, and OS/host versions.

## Make your first pull request

1. Choose one missing or failing case. Check existing issues and [`benchmarks/cases.jsonl`](benchmarks/cases.jsonl) for duplicates.
2. Add an original or anonymized case with a unique ID, language, complete task, explicit invariants, and the risk it tests. Describe meaning that must survive rather than requiring one exact rewrite.
3. If changing behavior, explain the failure first. Edit the canonical [`SKILL.md`](skills/asdify/SKILL.md); keep rules general enough to address the failure category. Open an issue before substantial behavior changes.
4. If adding an editorial demonstration, label it illustrative in [`examples/`](examples/). If reporting an experiment, follow the [evaluation protocol](benchmarks/README.md) and provide raw outputs and settings.
5. Run from the repository root:

   ```bash
   python3 scripts/validate.py
   python3 -m unittest discover -s tests -v
   ```

6. Submit a PR with the user problem, changed behavior, evidence, and possible regressions. Passing structural tests does not demonstrate improved model output.

### A case you can copy

Each line in `benchmarks/cases.jsonl` is a complete JSON object. Adapt this illustrative case with a unique ID, your task, the meaning to preserve, and the failure risk. Use a tag from [integrations/languages.json](integrations/languages.json) for the source `lang`. Add `target_lang` for a translation; omit it for same-language tasks.

```jsonl
{"id":"en-example","lang":"en","task":"Rewrite for a project update without changing certainty: The launch is expected on 20 November if the vendor approves testing.","invariants":["20 November is expected, not confirmed","launch depends on the vendor approving testing"],"risk":"turning a conditional estimate into a confirmed date"}
```

Keep it on one line when adding it to the file. The invariants describe meaning; they do not require exact output wording.

## Other useful contributions

- Complete [recipes](examples/recipes.md) for everyday tasks, with explicit preservation checks.
- Reproducible evaluations, including failures and concise-only comparisons.
- Installation evidence with host version, date, and the actions tested; see [compatibility](docs/COMPATIBILITY.md).
- Native-speaker review and corrections to the nine READMEs, keeping their factual claims aligned with the English source. Use the [documentation-translation report](https://github.com/hevertonrodrigues/asdify/issues/new?template=documentation_translation.yml) for incorrect or outdated wording.
- New languages with documentation, native-language cases, and bidirectional translation inputs; follow [language contribution steps](docs/LANGUAGES.md#add-or-review-a-language).
- Smaller, clearer skill instructions that preserve behavior.

See the [roadmap](docs/ROADMAP.md) for current priorities. Prefer a focused contribution over a large collection of untested rules.

Keep language inclusive and readable. Do not share private documents or secrets. Use original examples or material you have permission to contribute; record attribution when needed.

Contributions are licensed under the project's MIT license. Review [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and [SECURITY.md](SECURITY.md).
