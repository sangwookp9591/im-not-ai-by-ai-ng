# im-not-ai-by-ai-ng

Personal Writing **0.3.6** is a Korean writing skill package derived from im-not-ai. It shares one core contract across five purpose-specific skills, preserving meaning and facts while reducing formulaic AI wording.

| Skill | Purpose |
|---|---|
| `my-writing-base` | Shared rules, general editing, task routing |
| `my-planning` | Plans and requirements |
| `my-slides` | On-screen slide copy |
| `my-presentation` | Presentation structure and narrative |
| `my-speech` | Spoken scripts |
| `my-application` | Job application essays |

## Install in Claude Code

```sh
claude plugin install personal-writing --marketplace sangwookp9591/im-not-ai-by-ai-ng --scope user
claude plugin list
```

If replacing an installed original plugin, disable it after the custom installation succeeds:

```sh
claude plugin disable humanize-korean@im-not-ai --scope user
```

Restart Claude Code, then invoke `/personal-writing:my-planning` or another skill from the table.

To update:

```sh
claude plugin marketplace update im-not-ai-by-ai-ng
claude plugin update personal-writing@im-not-ai-by-ai-ng --scope user
```

Restart Claude Code after updating.

## Install in Codex

Ask Codex's `skill-installer` to install all six directories under `extensions/personal-writing/skills/` from `sangwookp9591/im-not-ai-by-ai-ng`. They must remain siblings so derived skills can read `my-writing-base/references/core.md`.

The default destination is `$CODEX_HOME/skills`, falling back to `~/.codex/skills`. Orca uses the active account's CODEX_HOME. Skills are available on the next turn; invoke them with names such as `$my-planning`.

For reinstalls, back up the existing six directories outside the skill discovery path, then install all six from the same revision. Repository changes do not automatically update installed copies. Pin a tested commit with `--ref` when sharing a version with teammates.

## Scope and maintenance

See the [package guide](extensions/personal-writing/README.md) for installation details, customization, and validation; see the [Korean README](README.md) for the main project guide.

Actual Sol 6.1 and Opus 5.5 runs are documented in the [evaluation report](evals/2026-10-11-v036-release/REPORT.md). Synthetic inputs and explicit skill calls do not establish universal quality or automatic discovery. PPTX creation, design, and rendering are outside this package's scope. Speech timing and job-specific suitability need validation with real user material.

Original files are retained for comparison. Use `extensions/personal-writing`, not the legacy root `install.sh` or root plugin. The [upstream README archive](README.upstream.md) describes the original package.
