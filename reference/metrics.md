# Metric set and data access

## Two lanes

**Live lane, for working sessions.** Bounded JQL through an Atlassian connector, one question at a time, fields restricted to what the metric needs. The Rovo MCP connector for ChatGPT reads Jira and Confluence and supports writeback, but it runs against a request and response ceiling of roughly 100,000 characters with a round trip near 45 seconds. A query returning a few hundred issues with descriptions will truncate, and truncated input produces confident wrong totals rather than an error. Connector availability has also been reported as intermittent, so do not put it in front of a steering group without a fallback.

**Export lane, for anything reported.** Run a saved filter in Jira, export CSV, compute from the file. Deterministic, no truncation, no dependency on connector uptime.

Jira already draws sprint burndown, release burndown, cumulative flow and control charts. Do not rebuild them. The value here is the freeze-relative view Jira does not provide.

## Timeline position

Days elapsed, per cent of timeline consumed, days to freeze, days to launch. Derived from kickoff and launch dates with the freeze at the two thirds point.

## Scope integrity

The group that does not exist natively in Jira, and the reason this report is worth running.

- Items and points created after kickoff, as a percentage of originally committed scope
- Items and points created after the freeze date
- Scope change ratio: points added plus points removed over points originally committed
- Items still in Ready to start, with points, as the rollover candidate list

Fields: `created`, `Story Points`, `fixVersion`, `status`, `statusCategory`

## Completion outlook

- Per cent complete by points and by issue count, reported separately because the divergence is informative
- Remaining points against remaining capacity, where capacity is rolling velocity times sprints left
- Rolling velocity over the last three sprints
- Projected completion date at current velocity, stated against the freeze date

Fields: `Sprint`, `Story Points`, `resolutiondate`, `statusCategory`

## Flow health

- Cycle time and lead time, median and 85th percentile
- Aging work in progress: items open longer than twice the median cycle time
- Blocked items, count and age of the oldest flag
- Cumulative flow, watching for a widening In Progress band

Fields: `Flagged`, changelog status transitions, `created`, `resolutiondate`

## Quality

- Open defects by severity
- Defect arrival rate against closure rate, weekly. Arrival above closure through the final third is the most reliable signal that a date will move
- Defect density per epic, to locate where the problem sits
- Reopened defect count

Fields: `issuetype`, `priority`, `status`, `created`, `resolutiondate`, `parent`

## Outside the team

- Cross-team dependencies not confirmed, from issue links
- Review gates not booked: legal, compliance, accessibility, security, performance

Fields: issue links, `labels`, `components`

## Data quality preconditions

Check these before trusting any output. Story points populated across the release, or the capacity maths is fiction. A consistent definition of done, or per cent complete means different things in different squads. Defects raised in the same project as the work, or arrival rate measures the wrong population. Sprint field populated, or velocity cannot be calculated.

If two or more are missing, run on issue counts instead of points and state that in the output.
