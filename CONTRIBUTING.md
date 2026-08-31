# Contributing

Thanks for looking. Here is what is useful and how the project handles changes.

## Issues are welcome

Open one for any of these, and do not worry about whether it is worth reporting.

**It broke on your Jira.** The most useful reports by a distance. Custom field names, workflow statuses and project configurations vary enormously, and something that works on one instance will fail on another. Tell me what did not resolve and what your setup looks like.

**A figure came out wrong.** If a metric produced a number you know is incorrect, say which metric and what you expected. Wrong output matters more here than missing features, because a delivery report that looks right and is wrong causes real harm.

**The framework did not fit your work.** Programmes without dates, teams that do not estimate, regulated environments with unusual gates. Version 1.1.0 exists because someone ran it against an eighteen month project with no start or end date and told me what happened.

**Something in the documentation is unclear or wrong.** Including anything in `SECURITY.md`, which people rely on when talking to their own security teams.

## Pull requests

Bug fixes, corrections and documentation improvements are welcome as pull requests. Send them directly.

Changes to the methodology itself are different. Open an issue first and let us talk it through before you write anything. The framework is deliberately small and most of the work in maintaining it is deciding what not to add, so a discussion first saves you effort on a change that might not be merged.

Before opening a pull request:

```
python3 scripts/validate-package.py
```

That checks the package files, the version consistency across `SKILL.md`, `plugin.json` and the README, and a few style rules. `AGENTS.md` covers the conventions in more detail, including the em dash rule, which the validator enforces.

## What will not be merged

Metrics that do not help answer whether the date can be protected. The framework has stayed useful by being narrow, and a general purpose agile analytics dashboard already exists in several forms.

A single composite risk score. The freeze status is a set of explicit rules on purpose, because a rule can be explained to a steering group and argued with, and a weighted score cannot.

Any figure the skill cannot derive from a named Jira field.

Anything that adds a network call, a dependency or telemetry to the skill itself. `SECURITY.md` makes a specific promise about this and the promise is worth more than any feature.

## Licence

Contributions are accepted under the MIT licence, the same terms as the rest of the repository.
