# Guide for agents

This file explains how to change The Final Third without breaking its package.

## What this repo contains

An agent skill written in Markdown. `SKILL.md` is the prompt agents read. There is no build step.

Keep the skill portable. Do not write instructions that tie it to one agent or one tool.

## Key files

- `SKILL.md` is the source of truth. It carries portable YAML metadata, the framework, and the reporting rules.
- `reference/metrics.md` and `reference/prompts.md` are loaded on demand, so keep detail there rather than in `SKILL.md`.
- `README.md` explains installation, use, and version history.
- `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` describe the plugin.
- `scripts/validate-package.py` checks files, names, versions, and style rules.

## Rules for changes

Keep `SKILL.md` and `README.md` in sync.

- **Version:** the same value goes in `SKILL.md` under `metadata.version`, `.claude-plugin/plugin.json`, and the first README version entry. Do not add a top-level `version` field to the skill.
- **Prose:** no em dashes or en dashes anywhere in the repo. The validator fails the build on either.
- **Numbers:** do not add a metric, threshold, or figure that the skill cannot derive from a named Jira field.
- **Compatibility:** keep install and use instructions neutral across agents. Claude Code, Codex and others are examples, not limits.

Run `python3 scripts/validate-package.py` before opening a pull request.
