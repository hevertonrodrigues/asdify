# ASDify release check

Date: 8 October 2026. Target: `https://github.com/hevertonrodrigues/asdify`.

The product has been moved to the repository root and renamed to **ASDify**, with `asdify` as the skill, plugin, repository, and installation identifier. Original quoted requests and archive contents remain historical records.

## Local verification

- `python3 scripts/validate.py`: PASS; skill, local manifests, relative links, and 16 bilingual cases.
- `python3 -m unittest discover -s tests -v`: PASS; 30 tests, including renamed installation destinations and complete skill/reference copies.
- `bash -n scripts/install.sh`: PASS.
- Skill-creator `quick_validate.py skills/asdify`: PASS.
- Independent review of the active product files: no stale identifiers or path blockers.
- Original draft ZIP: byte-for-byte checksum matches the archive in the earlier Git commit; only its filename changed.

Test environment: Darwin 27.0.0, Python 3.14.6. No global installation was performed.

## Publication

The repository is prepared for creation through GitHub CLI under `hevertonrodrigues/asdify`. Public availability and remote CI are not yet verified.

Real-host activation and live model quality remain unverified. Local installer tests use temporary directories and do not establish host behavior.
