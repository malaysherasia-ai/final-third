# Working prompts

## 1. Set up the panel

> You have access to our Jira through the Atlassian connector. Project [KEY], fix version [RELEASE].
>
> Our timeline runs [start date] to [launch date]. Calculate the two thirds point and treat that as the scope freeze date.
>
> Before you pull anything, list the JQL queries you intend to run and the fields you will request for each. Restrict fields to what each metric needs and do not pull descriptions or comments. Wait for me to approve the list.

## 2. Pull the state

> Run the approved queries. Return a table with one row per metric: metric name, value, the JQL that produced it, and the field it read.
>
> Where a value depends on a field our project does not populate, say so in that row and return nothing for it. Do not estimate, do not infer from issue titles, and do not fill a gap with a typical value.

## 3. Read it against the freeze

> Using only the values from the table above, answer four questions.
>
> One, how many points are open against how much capacity remains before the freeze, and what is the gap.
> Two, at rolling three sprint velocity, what date does the remaining work complete, and how far is that from the freeze date.
> Three, how much scope was created after kickoff, and how much after the freeze date.
> Four, is defect arrival running above closure over the last six weeks.
>
> Then give me the shortest list of items that would have to move to the next release for the freeze to hold, ordered by points, with the epic each one belongs to.

## 4. Write the status note

> Draft a status update for the steering group covering the position against the freeze, the rollover recommendation, and the two decisions I need from them this week. State numbers plainly with no adjectives. Do not open with a summary of the framework. Under 250 words.

## 5. Build the visual

> From the values in the table, produce a single dashboard image. Include a timeline strip with the three parts marked and today's position, four headline figures across the top (days to freeze, scope added, remaining against capacity, projected completion), a release burn down with the ideal line and the freeze marked, a weekly defect arrival against closure chart, and a list of items needing a decision before the freeze with a recommended action against each.
>
> Colour anything that puts the freeze at risk in red. Put a line at the foot of the image stating that every figure comes from a named Jira field.

## 6. Handle a late request

> A stakeholder has asked for [describe request] and we are [x] days past scope freeze. Draft a reply that acknowledges the request, explains what accepting it would compress, and commits it to the next release with a specific date. Do not apologise and do not hedge. Offer one alternative if a smaller version could ship without touching the release.

## 7. Build the closing checklist

> We enter our final third on [date] for a [describe the project]. Build a closing checklist covering regression scope, defect triage thresholds, content and legal sign off, accessibility validation, cutover rehearsal, rollback plan, and go/no-go criteria. For each item give me the owner role, the latest date it can start, and what it blocks if it slips.
