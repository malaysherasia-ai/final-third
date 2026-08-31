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
  version: "1.2.0"
---

# The Final Third

Split a fixed timeline into three equal parts. Build in the first two. Close in the last one.

## When this applies

Use it when the date cannot move, more than one team is involved, and at least one review gate sits outside the delivery team's control. Regulated environments usually meet all three.

Do not use it for discovery work where changing direction is the point, or for anything under about two weeks.

## Establish the mode before anything else

Two kinds of work turn up, and the framework behaves differently for each. Decide which one you are looking at before calculating anything.

**Fixed date.** There is a launch, a release, a go live or a regulatory deadline that will not move. The freeze applies and the rest of this skill runs as written.

**Continuous.** Sprint after sprint with no launch date. There is nothing to freeze, and inventing a date so the framework has something to work with would be dishonest. Say so plainly, then look for the nearest real commitment boundary, which is usually a quarterly goal, a PI boundary, a version due date or an external customer commitment. If one exists, apply the framework to that increment. If none exists, run the flow reporting described below instead and do not report a freeze at all.

**Flow reporting for continuous work.** Throughput per week, cycle time median and 85th percentile, work in progress, aging work in progress, defect arrival against closure, blocked count and oldest blocker age. Report trend across the last eight weeks. Say clearly that no freeze applies, because a stakeholder who half remembers this framework will otherwise assume one is being held.

## Long programmes

Anything running beyond about sixteen weeks should not have a single freeze. Four months of closing on a twelve month programme is too much, and nobody will follow it.

Closing duration does not scale with build duration. What sets it is the number of review gates, how long the slowest one takes, and how long a full regression cycle runs, all of which are close to fixed for a given system.

Split a long programme into delivery increments and apply the framework to each one, so a twelve month programme running six two month releases gets six freezes of roughly two weeks each. The programme level gets milestone governance. The increment level gets the freeze.

## The rule

Calculate the two thirds point of the timeline. That date is the scope freeze.

The first third is for setting up: requirements, design and architecture decisions, dependency mapping, environments, test data, access. Aim to reach a state where no later task is waiting on a decision nobody has made.

The second third is for building. Scope can still move, by trade. Something comes in, something else goes out, and the swap is recorded with a name against it.

The last third is for closing. Burn down open stories, run full regression, triage and fix defects, complete content and legal sign off, rehearse cutover and rollback. Nothing new enters.

## Finding the dates

Do not calculate a freeze from dates you inferred. Work down this ladder and stop at the first source that gives both a start and an end.

1. The fix version's start date and release date. Best source, because someone set it deliberately.
2. The parent epic or initiative's start date and due date.
3. The start of the first sprint and the end of the last sprint in the version, where sprints are planned out to the end.
4. Ask the user.

The earliest issue creation date may be offered as a start date, clearly labelled as a proxy, but only alongside a request to confirm it. Never treat scattered issue due dates as a launch date, and never estimate a launch date from velocity.

When the dates are not in Jira, ask for them directly rather than guessing:

> I could not find a start and end date for this work in Jira. I looked at the fix version, the parent epic and the sprint range.
>
> Two questions.
>
> One, does this work have a fixed end date that will not move, such as a launch, a go live, a contractual date or a regulatory deadline? If it does, what is it, and when did the work start?
>
> Two, if there is no fixed end date, is there a nearer commitment I should measure against instead, such as a quarterly goal, a PI boundary or a customer commitment? If there is neither, I will report flow health instead and will not report a freeze, because there would be nothing to freeze against.

State the dates back and say which source they came from before doing anything with them, so the person can correct a wrong version date before it propagates through every figure.

## Setting it up

When asked to plan against a date, do this:

1. Take the start and launch dates. Calculate the exact two thirds point and state it.
2. Name it as a milestone so it appears in status reporting.
3. Draft the kickoff note announcing it, phrased as how the project runs rather than as a restriction on stakeholders.
4. Hold capacity back in the final third for defects. Derive the figure from how much unplanned defect work the last three releases absorbed rather than taking a rule of thumb.
5. Get the definition of done agreed before the freeze, not during it.

Say the freeze date early. Announced late it reads as the delivery team defending itself and it invites an argument.

## Handling a late request

Do not refuse outright. Route it to the next release backlog with an owner and a place in the queue, so the requester leaves with a date. A request that leaves with nothing returns later through someone more senior.

Keep two terms apart. A scope change is agreed, traded and recorded. Scope creep is neither agreed nor traded.

Two things justify breaking the freeze: a regulatory or legal obligation with an external date, and a defect blocking the core journey. Both reopen the plan in front of stakeholders. Neither gets absorbed quietly, because a freeze absorbed once stops meaning anything.

## Reporting against the freeze

Read `reference/metrics.md` for the metric set, the Jira fields behind each one, and the two data lanes. Read `reference/prompts.md` for the working prompts.

**Read only.** This skill only ever reads. Use search and get operations to retrieve issues and fields. Never create, update, transition, assign, comment on, link or delete an issue, and never modify a board, sprint, filter or version. If someone asks for a change to be made in Jira, explain that this skill does not write and let them make the change themselves.

Rules that apply to every report:

- List the intended queries and fields before pulling anything, and keep field selection to what each metric needs.
- Every figure names the Jira field it came from.
- Where a field is not populated, say so and return nothing for that metric. Never estimate a missing value, infer it from issue titles, or substitute a typical figure.
- Report progress against the freeze date rather than the launch date. Reporting to launch hides slippage until there is no time to act on it.
- Move the burn down to daily once the freeze starts. The recovery window for a slipping story in the final third is a few days, so a weekly cadence finds out too late.

## Cadence

Once at kickoff to set the date. Weekly through the second third. Daily through the last third, where the figures that matter are the burn down, defect arrival against closure, and the blocked list.
