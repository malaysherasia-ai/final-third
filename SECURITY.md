# Using this with proprietary data

Written for the person who wants to run this against their employer's Jira and needs to know what they are agreeing to, and for the security reviewer they will have to satisfy.

## The skill itself is not a security surface

This repository is Markdown. There is no code, no install script, no dependency tree, no network call, no telemetry, and no credential of any kind. Nothing in it phones home. The author never sees your data and has no way to.

What it contains is instructions that a model reads. Every piece of data access happens through a connector your organisation set up, approved, and can revoke, and none of it flows through anything published here.

That is the whole trust argument, and it is worth stating plainly to a reviewer before anything else. The question is not whether this repository is safe. It is whether your organisation's existing AI and Jira controls are configured the way you think they are.

## What Atlassian controls on their side

Facts from Atlassian's own documentation, worth knowing because a reviewer will ask.

The Atlassian Rovo MCP server is not a Marketplace app. It installs just in time the first time a user completes the OAuth 2.1 consent flow, which means it does not appear under Manage apps and is easy to miss during a review. Site and organisation admins can review or revoke its access from the organisation's Marketplace and third party apps screen.

Access is granted only to data the user already has permission to view in Atlassian Cloud. Every action respects existing project and space level roles, under both OAuth and API token authentication. A connector cannot widen anyone's access.

Admins control which AI tools and domains may connect, through domain settings under Rovo MCP server in Atlassian Administration. Blocking a domain works for tools authenticating with OAuth 2.1, though not for tools using API tokens.

The organisation IP allowlist applies to MCP requests regardless of which tool made them. A call from outside the allowlist fails, even though the consent screen may still appear.

API token authentication has to be enabled by an organisation admin and is intended for headless or machine to machine use. For interactive work like this, OAuth 2.1 is the recommended path and the one to ask for.

Organisation admins grant and revoke at permission group level, and each tool inherits the access of its parent group.

## What OpenAI controls on the ChatGPT side

For Business, Enterprise and Edu workspaces, information accessed through apps and connectors is not used to train models. Chat and deep research data is processed transiently and is not indexed. Data is encrypted at rest and in transit, and ChatGPT Enterprise is SOC 2 compliant.

Apps are disabled by default on Enterprise and Edu plans, so a workspace owner or admin has to enable each one deliberately. Admins can also set action control per app to allow all actions, allow read actions only, or use a custom configuration, and can decide how actions added later are handled.

**Ask your admin to set the Atlassian app to read actions only.** This report never needs to write to Jira, and read only removes the entire category of risk where a model creates or transitions an issue by mistake.

## What this framework does to reduce exposure further

Three design choices, all of them deliberate.

**Field minimisation.** The metric dictionary lists every field the report reads. They are dates, statuses, issue types, priorities, points, sprints and links. Descriptions, comments and attachments are never requested, so the narrative content of your issues stays in Jira. Most of what a delivery report needs is metadata, and metadata carries far less than the text people write inside tickets.

**Query approval before retrieval.** The first prompt makes the model list the queries and fields it intends to run and wait for you to approve them. You see exactly what is about to leave Jira before it leaves.

**An export lane that needs no connector.** Anything going into a status pack should come from a saved Jira filter exported to CSV with only the columns the report needs. This avoids connector truncation, and it also means you choose the columns rather than a model choosing them.

## Residual risks, stated honestly

None of the above makes this risk free, and a reviewer who hears otherwise will stop believing the rest.

**Aggregation.** Permission inheritance means the report shows what you can already see. It does not mean the result is as safe as the parts, because a panel assembles scattered facts into one view. If your access is broad, the output is broader than anything you would normally look at in one place.

**Screenshots.** The panel is built to be shared, and the attention table carries issue summaries, epic names and team names. Those often include client names and unreleased product names. Redact before anything leaves your organisation, and treat the images in this repository as what they are, which is invented data.

**Version and epic naming.** Fix version and epic names frequently contain customer or partner names. They are metadata, so field minimisation does not protect them.

**Correctness, which is a different risk.** A connector that truncates a large result returns a confident wrong total rather than an error. A wrong number in front of a steering group causes real harm even though no data leaked. That is why the query approval step and the CSV lane exist.

**Your obligations do not change.** If you work somewhere regulated, an approved connector is not the same as an approved use case. Financial services, healthcare and public sector organisations usually require their own assessment before delivery data goes near an AI tool, whatever the vendor terms say.

## Before you run it

Six things to confirm, in order.

1. Your workspace admin has enabled the Atlassian app in ChatGPT, and it is set to read actions only.
2. Your organisation admin has the Rovo MCP server domain settings configured for the tool you are using.
3. You are on OAuth 2.1 rather than an API token, so the session runs under your own permissions.
4. You are connecting from inside the organisation IP allowlist.
5. You have checked which Jira projects your account can see, since the report reaches all of them.
6. Somebody who owns AI usage policy at your organisation knows you are doing this.

## A paragraph to send your security team

> I want to run a delivery reporting workflow in our approved ChatGPT workspace against Jira, using the Atlassian connector we already have enabled. The workflow is a Markdown instruction file with no code, no dependencies and no network access of its own, so it introduces no new vendor or supply chain relationship. All data access happens through the existing Atlassian Rovo MCP connector under OAuth 2.1, which is scoped to my own Jira permissions and subject to our domain settings and IP allowlist. It reads issue metadata only, meaning dates, statuses, issue types, priorities, story points and links, and never requests descriptions, comments or attachments. I would like the Atlassian app restricted to read actions. Happy to run the first pull with you watching, since the workflow lists its queries for approval before it retrieves anything.
