# The Final Third

A delivery skill for work running to a date somebody else set. Split the timeline in three, freeze scope at the two thirds mark, and spend the last third closing. It is Markdown, so it works with any agent that supports skills.

## How it works

The skill does three jobs.

It sets the freeze. Give it a start and a launch date and it calculates the two thirds point, names it as a milestone, and drafts the kickoff note that puts it in front of stakeholders while the timeline still looks comfortable.

It handles late requests. Anything arriving after the freeze gets routed to the next release backlog with an owner and a date rather than refused, because a request that leaves with nothing comes back through someone more senior. Two things justify breaking the freeze: a regulatory obligation with an external date, and a defect blocking the core journey. Both reopen the plan in public.

It reports against the freeze. Reading Jira through an Atlassian connector or a CSV export, it produces standard agile SDLC metrics measured against the freeze date instead of the launch date. Velocity, cycle time, aging work in progress, cumulative flow, defect arrival against closure, blocked age. Plus the group Jira has no native view of: scope created after a given date, measured against originally committed scope.

Every figure names the Jira field it came from. Where a field is not populated the skill says so and returns nothing, rather than substituting a typical value.

Every query it runs is a read. It retrieves issues and fields and computes from them. It never creates, updates, transitions or deletes anything in Jira, and it never modifies a board, sprint or version. [SECURITY.md](SECURITY.md) covers how to have that enforced by your administrators rather than trusted.

## Work without a fixed date

Two kinds of work turn up. Where there is a launch, a go live or a regulatory deadline, the freeze applies and the framework runs as written. Where a team runs sprint after sprint with nothing to launch, there is nothing to freeze, and the skill says so instead of inventing a date. It looks for the nearest real commitment boundary, usually a quarterly goal, a PI boundary or a customer commitment, and applies the framework to that increment. If there is no boundary at all, it reports flow health and no freeze.

Long programmes get the same treatment. Anything past about sixteen weeks is split into delivery increments with a freeze on each, because four months of closing on a twelve month programme is not a rule anyone will follow.

## Install

**Business users, no install:** a copy-and-paste page with the prompts is at https://malaysherasia-ai.github.io/final-third/

**Claude:**

```
/plugin marketplace add malaysherasia-ai/final-third
/plugin install final-third
```

**ChatGPT Business or Enterprise:** there is no third party skill install. Create a Project, paste the contents of `SKILL.md` into its instructions, and attach `reference/metrics.md` and `reference/prompts.md` as project files. The prompts in `reference/prompts.md` also work pasted straight into a chat with the Atlassian app enabled.

**Any other agent that reads skills:** copy `SKILL.md` and the `reference/` folder into your skills directory.

**Inside a company that reviews external repositories:** fork it. The licence is MIT, the skill is Markdown with two small validation scripts alongside it, and vendoring a copy into your internal Git is a reasonable thing for a security team to ask for.

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

## Contributing

Issues are welcome, particularly reports that the skill did not resolve fields on your Jira, or that a metric produced a figure you know is wrong. Bug fixes and documentation corrections are welcome as pull requests. For changes to the methodology itself, open an issue first so the discussion happens before the work. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Version history

### 1.2.0

Added a hosted prompts page at `docs/index.html`, served through GitHub Pages, for people who want to run the framework without installing anything. Single file, no dependencies, no analytics.

### 1.1.1

Added `CONTRIBUTING.md` covering what is useful to report, how methodology changes are handled, and what will not be merged.

### 1.1.0

Added an explicit read only rule to the skill, and a section in `SECURITY.md` covering how administrators enforce it rather than trusting a prompt.

Added mode handling. Work with a fixed date runs the freeze as before. Continuous work with no launch date now looks for the nearest real commitment boundary, and reports flow health with no freeze where none exists.

Added a date resolution ladder, so the freeze is calculated from a fix version, an epic or a sprint range, and the skill asks the user when Jira holds no dates rather than inferring them.

Added guidance for programmes beyond about sixteen weeks, which get a freeze per delivery increment rather than one freeze across the whole thing.

Replaced the fixed capacity reserve figure with a method for deriving it from a team's own release history.

### 1.0.1

Corrected the opening of `SECURITY.md`. It described the repository as containing no code, which was wrong, since two Python scripts sit alongside the skill for package validation and repository traffic. The claim now applies to the skill itself and the scripts are described.

### 1.0.0

First release. The framework, the metric set, seven prompts, and the reporting rules.

## Licence

MIT
