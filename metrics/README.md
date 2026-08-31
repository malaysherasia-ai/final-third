# Tracking usage

What GitHub can tell you, what it cannot, and what each signal is worth.

## Nothing goes in the skill

The first rule is that no measurement lives inside `SKILL.md`. No pixel, no call home URL, no analytics of any kind.

`SECURITY.md` tells readers this repository has no code, no network calls and no telemetry, and that claim is the reason anyone at a bank or an insurer will run it. Adding a tracking ping to count installs would trade the only argument that gets it through a security review for a number on a dashboard. Everything below happens outside the artefact, on GitHub's side, using data GitHub already collects about the repository rather than about the reader.

## What GitHub gives you

**Clones.** The closest thing to an install count. A Claude plugin install runs a git clone, so `/plugin marketplace add` shows up here. Unique cloners is the number to watch rather than total clones, since CI systems and mirrors clone repeatedly.

**Views and unique visitors.** People reading the repository on github.com. Does not include fetches of raw files, so anyone who curls `SKILL.md` directly is invisible.

**Referrers.** Where visitors arrived from over the last fourteen days. This is how you find out whether a LinkedIn post actually sent anyone, or whether the traffic came from somewhere you did not know about.

**Popular paths.** Which files people open. Useful signal here: if `reference/metrics.md` gets opened often, readers are checking your work rather than skimming, which is the audience worth having.

**Stars with timestamps.** The stargazers endpoint returns `starred_at` when you send the `application/vnd.github.star+json` accept header, which turns a running total into a dated series you can line up against posts.

**Forks.** Under-rated for this repository. A fork is often an enterprise vendoring a copy internally, which `SECURITY.md` recommends they do. Forks are a stronger adoption signal than stars.

**Release asset downloads.** Counted per uploaded asset, not for the automatically generated source archives. If you want a download number, attach a zip to the release.

## What GitHub cannot tell you

Whether anyone ran it. Whether a fork was used or abandoned. Anything about people who pasted `SKILL.md` into a ChatGPT Project, which is the whole ChatGPT Enterprise path and leaves no trace by design. Anything about internal mirrors behind a corporate firewall.

Accept that the ChatGPT audience is unmeasurable. Trying to fix it is what leads people to add telemetry.

## The fourteen day problem

GitHub keeps traffic data for fourteen days and then drops it. Miss two weeks and that period is gone permanently.

`.github/workflows/traffic.yml` runs daily, pulls the current window, and merges it into dated CSVs in this folder, keyed on date so re-running is safe. The history becomes permanent and lives in the repository.

Traffic endpoints need push access. The default `GITHUB_TOKEN` is often refused, so if the job returns 403, create a fine grained personal access token with read access to repository administration and metadata, and save it as a repository secret named `TRAFFIC_TOKEN`.

## Files here

- `views.csv` daily views and unique visitors
- `clones.csv` daily clones and unique cloners
- `stars.csv` one row per star with the date it was given
- `SNAPSHOT.md` current totals plus referrers and popular paths for the last fourteen days

## Reading the numbers

Watch unique cloners against unique visitors. A high ratio means people are installing rather than browsing, and that is the whole point of publishing this.

Watch referrers in the days after you post about it. A post that generates views but no clones told a good story about a thing nobody wanted. A post that generates clones from a referrer you did not expect is worth understanding.

Watch forks separately from stars. Stars are approval, forks are use.

For the purpose this repository actually serves, the metric that matters is not in GitHub at all. It is whether someone credible references the framework without you being in the room. Set up an alert for the phrase and check who is linking in, because one delivery lead at a real company citing it in their own writing is worth more than a thousand stars.
