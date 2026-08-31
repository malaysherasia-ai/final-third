# The Final Third

A delivery skill for work running to a date somebody else set. Split the timeline in three, freeze scope at the two thirds mark, and spend the last third closing. It is Markdown, so it works with any agent that supports skills.

## How it works

The skill does three jobs.

It sets the freeze. Give it a start and a launch date and it calculates the two thirds point, names it as a milestone, and drafts the kickoff note that puts it in front of stakeholders while the timeline still looks comfortable.

It handles late requests. Anything arriving after the freeze gets routed to the next release backlog with an owner and a date rather than refused, because a request that leaves with nothing comes back through someone more senior. Two things justify breaking the freeze: a regulatory obligation with an external date, and a defect blocking the core journey. Both reopen the plan in public.

It reports against the freeze. Reading Jira through an Atlassian connector or a CSV export, it produces standard agile SDLC metrics measured against the freeze date instead of the launch date. Velocity, cycle time, aging work in progress, cumulative flow, defect arrival against closure, blocked age. Plus the group Jira has no native view of: scope created after a given date, measured against originally committed scope.

Every figure names the Jira field it came from. Where a field is not populated the skill says so and returns nothing, rather than substituting a typical value.

## Install

**Claude:**

```
/plugin marketplace add malaysherasia-ai/final-third
/plugin install final-third
```

**ChatGPT Business or Enterprise:** there is no third party skill install. Create a Project, paste the contents of `SKILL.md` into its instructions, and attach `reference/metrics.md` and `reference/prompts.md` as project files. The prompts in `reference/prompts.md` also work pasted straight into a chat with the Atlassian app enabled.

**Any other agent that reads skills:** copy `SKILL.md` and the `reference/` folder into your skills directory.

**Inside a company that reviews external repositories:** fork it. The licence is MIT, the whole thing is Markdown, and vendoring a copy into your internal Git is a reasonable thing for a security team to ask for.

Before running this against your employer's Jira, read [SECURITY.md](SECURITY.md). It covers what the Atlassian and OpenAI admin controls actually do, what this framework reads and does not read, the residual risks, and a paragraph you can send to your security team.

## Usage

Set up a plan:

```
/final-third

Our release runs 1 July to 3 October. Set the freeze and draft the kickoff note.
```

Handle a request:

```
Marketing has asked for a second banner variant and we are four days past freeze. What do I send back?
```

Report status:

```
Pull our Jira for project ABC, fix version 4.2, and show me where we stand against the freeze.
```

## Files

- `SKILL.md` is the source of truth and the prompt agents read
- `reference/metrics.md` holds the metric set, the Jira fields behind each one, and the two data lanes
- `reference/prompts.md` holds the seven working prompts
- `.claude-plugin/plugin.json` describes the plugin and points the skill loader at the root `SKILL.md`
- `.claude-plugin/marketplace.json` lets people add this repo as a marketplace
- `SECURITY.md` covers running this against proprietary data
- `scripts/validate-package.py` checks the package files and shared version

## A note on the connector

The Atlassian Rovo MCP connector for ChatGPT reads Jira and Confluence and supports writeback. It also runs against a request and response ceiling near 100,000 characters, so a JQL query returning a few hundred issues with descriptions attached will truncate, and truncated input gives you confident wrong totals rather than an error. Availability has been reported as intermittent.

Use the connector for working sessions and a CSV export from a saved filter for anything that goes into a status pack.

## Why this is not on npm

The artefact is prose. An npm package implies executable code, install scripts and a dependency tree, which is exactly the surface enterprise security teams are trained to scrutinise, and publishing a Markdown file there would invite a review it does not need. Claude plugin marketplaces install from a Git repository, so this is already the native path, and anyone who needs an internal copy can fork it.

## Version history

### 1.0.0

First release. The framework, the metric set, seven prompts, and the reporting rules.

## Licence

MIT
