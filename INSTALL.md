# Installation

See [compatibility and verification](docs/COMPATIBILITY.md) for the evidence behind each integration. Local copy tests do not establish that a particular host version loads or follows the skill.

The canonical skill is `skills/asdify/`. Install from a trusted clone of this repository. Review the text before adding always-on instructions to your agent.

## Clone once, then choose your host

```bash
git clone https://github.com/hevertonrodrigues/asdify.git
cd asdify
```

### Claude Code

From the cloned repository, install for your user account:

```bash
bash scripts/install.sh --agent claude --scope user
```

### Codex

From the cloned repository, install for your user account:

```bash
bash scripts/install.sh --agent codex --scope user
```

### Cursor

Install in the project that should receive the rule. Replace both paths below:

```bash
cd "/path/to/your-project" && \
  bash "/path/to/asdify/scripts/install.sh" --agent cursor --scope project
```

### Project-only installation for Claude Code or Codex

Use `--scope project` from your target project, with the installer's absolute path. Replace both paths; change `claude` to `codex` for Codex:

```bash
cd "/path/to/your-project" && \
  bash "/path/to/asdify/scripts/install.sh" --agent claude --scope project
```

`--scope project` always writes into the current working directory. `--force` replaces an existing install; without it, the script refuses to overwrite. The script requires Bash and common POSIX commands.

Start a new agent session and try a complete [recipe](examples/recipes.md). If installation or discovery fails, [report an installation problem](https://github.com/hevertonrodrigues/asdify/issues/new?template=bug_report.md).

## Paths and activation

| Host | User | Project | Activation |
| --- | --- | --- | --- |
| Claude Code | `~/.claude/skills/asdify/SKILL.md` | `.claude/skills/asdify/SKILL.md` | Skill discovery, or `/asdify` where supported |
| Codex | `~/.agents/skills/asdify/SKILL.md` | `.agents/skills/asdify/SKILL.md` | Skill discovery; invocation syntax depends on client |
| Cursor | Use project installation | `.cursor/rules/asdify.mdc` | Project rule (always applied per file rule metadata) |

The Cursor adapter is a **compact rule**, not a full skill copy. For full skill semantics, also install it using Cursor's supported Agent Skills path according to your Cursor version. Instruction-file behavior and names may change by host/version.

## Portable manual install

Copy the entire skill folder (not just `SKILL.md`) into the Agent Skills directory recognized by the host. The package has no runtime scripts or external dependencies.

```bash
# Example: Claude Code per-project
mkdir -p .claude/skills
cp -R /path/to/asdify/skills/asdify .claude/skills/
```

For agents that do not load skills, copy the compact instructions from [AGENTS.md](AGENTS.md) into the applicable agent rules file (e.g. project `AGENTS.md`, `CLAUDE.md`, or equivalent). Note: project `AGENTS.md` may already exist; **merge** with existing project rules rather than overwriting.

## Modes

Tell the agent `Use asdify lite/full/ultra`, or invoke the skill in clients that expose it as a direct command. Mode switching and `off` are semantic instructions; this repository does **not** install a background daemon, event hooks, or global slash-command dispatcher.

## Uninstall

If you installed the earlier draft under its former name, review and remove that old skill or Cursor rule after installing ASDify so both copies do not apply. This installer creates the `asdify` paths listed above and does not delete earlier installations.

Remove only the installed skill folder/rule shown above. Do not delete a pre-existing folder unless you are sure it was installed by this project.

## Troubleshooting

- **Skill not available?** Verify the path, restart your agent session, and explicitly ask the agent to use `asdify`.
- **No change in output?** Request `full` or `ultra`; already-clear text intentionally receives few edits.
- **Facts removed?** [Report a meaning regression](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml) with the source and incorrect output, removing private data.
- **Existing file blocked?** Review differences before rerunning with `--force`.
