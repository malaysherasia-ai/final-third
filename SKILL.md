---
name: final-third
description: |
  Plan and control delivery against a fixed date by splitting the timeline in
  three and freezing scope at the two thirds mark. Use when setting up a release,
  migration, platform implementation or launch plan, when deciding what to do
  with a late scope request, or when reporting delivery status against a freeze.
  Reads Jira through an Atlassian connector or a CSV export and reports standard
  agile SDLC metrics against the freeze date.
license: MIT
metadata:
  version: "1.0.0"
---

# The Final Third

Split a fixed timeline into three equal parts. Build in the first two. Close in the last one.

## When this applies

Use it when the date cannot move, more than one team is involved, and at least one review gate sits outside the delivery team's control. Regulated environments usually meet all three.

Do not use it for continuous delivery with no release date, for discovery work where changing direction is the point, or for anything under about two weeks.

## The rule

Calculate the two thirds point of the timeline. That date is the scope freeze.

The first third is for setting up: requirements, design and architecture decisions, dependency mapping, environments, test data, access. Aim to reach a state where no later task is waiting on a decision nobody has made.

The second third is for building. Scope can still move, by trade. Something comes in, something else goes out, and the swap is recorded with a name against it.

The last third is for closing. Burn down open stories, run full regression, triage and fix defects, complete content and legal sign off, rehearse cutover and rollback. Nothing new enters.

## Setting it up

When asked to plan against a date, do this:

1. Take the start and launch dates. Calculate the exact two thirds point and state it.
2. Name it as a milestone so it appears in status reporting.
3. Draft the kickoff note announcing it, phrased as how the project runs rather than as a restriction on stakeholders.
4. Hold twenty to thirty per cent of final third capacity unbooked for defects.
5. Get the definition of done agreed before the freeze, not during it.

Say the freeze date early. Announced late it reads as the delivery team defending itself and it invites an argument.

## Handling a late request

Do not refuse outright. Route it to the next release backlog with an owner and a place in the queue, so the requester leaves with a date. A request that leaves with nothing returns later through someone more senior.

Keep two terms apart. A scope change is agreed, traded and recorded. Scope creep is neither agreed nor traded.

Two things justify breaking the freeze: a regulatory or legal obligation with an external date, and a defect blocking the core journey. Both reopen the plan in front of stakeholders. Neither gets absorbed quietly, because a freeze absorbed once stops meaning anything.

## Reporting against the freeze

Read `reference/metrics.md` for the metric set, the Jira fields behind each one, and the two data lanes. Read `reference/prompts.md` for the working prompts.

Rules that apply to every report:

- List the intended queries and fields before pulling anything, and keep field selection to what each metric needs.
- Every figure names the Jira field it came from.
- Where a field is not populated, say so and return nothing for that metric. Never estimate a missing value, infer it from issue titles, or substitute a typical figure.
- Report progress against the freeze date rather than the launch date. Reporting to launch hides slippage until there is no time to act on it.
- Move the burn down to daily once the freeze starts. The recovery window for a slipping story in the final third is a few days, so a weekly cadence finds out too late.

## Cadence

Once at kickoff to set the date. Weekly through the second third. Daily through the last third, where the figures that matter are the burn down, defect arrival against closure, and the blocked list.
