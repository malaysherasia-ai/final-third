#!/usr/bin/env python3
"""Merge the 14 day traffic window into a permanent CSV history.

GitHub's traffic API only returns the last 14 days, so running this daily
and keying on the date makes the history additive rather than a rolling window.
"""
import csv
import json
from pathlib import Path

METRICS = Path("metrics")
METRICS.mkdir(exist_ok=True)


def load(name):
    return json.loads(Path(f"/tmp/{name}.json").read_text())


def merge_daily(filename, rows, key="date", fields=None):
    path = METRICS / filename
    existing = {}
    if path.exists():
        with path.open() as f:
            for row in csv.DictReader(f):
                existing[row[key]] = row
    for row in rows:
        existing[row[key]] = {k: str(v) for k, v in row.items()}
    fields = fields or list(next(iter(existing.values())).keys())
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for k in sorted(existing):
            w.writerow(existing[k])


views = [
    {"date": d["timestamp"][:10], "views": d["count"], "unique_visitors": d["uniques"]}
    for d in load("views").get("views", [])
]
merge_daily("views.csv", views, fields=["date", "views", "unique_visitors"])

clones = [
    {"date": d["timestamp"][:10], "clones": d["count"], "unique_cloners": d["uniques"]}
    for d in load("clones").get("clones", [])
]
merge_daily("clones.csv", clones, fields=["date", "clones", "unique_cloners"])

# Stars are aggregated to a daily count. The API returns usernames, but a
# count answers the same question without keeping a list of named people here.
stars = load("stars")
per_day = {}
for s in stars:
    if "starred_at" in s:
        day = s["starred_at"][:10]
        per_day[day] = per_day.get(day, 0) + 1
with (METRICS / "stars.csv").open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["date", "stars"])
    w.writeheader()
    for day in sorted(per_day):
        w.writerow({"date": day, "stars": per_day[day]})

repo = load("repo")
snapshot = {
    "stars": repo.get("stargazers_count"),
    "forks": repo.get("forks_count"),
    "watchers": repo.get("subscribers_count"),
    "open_issues": repo.get("open_issues_count"),
}
referrers = load("referrers")
paths = load("paths")

lines = ["# Metrics snapshot", ""]
lines.append(f"Stars {snapshot['stars']}  ·  Forks {snapshot['forks']}  ·  "
             f"Watchers {snapshot['watchers']}")
lines.append("")
lines.append("## Referrers, last 14 days")
lines.append("")
lines.append("| Source | Views | Unique |")
lines.append("|---|---|---|")
for r in referrers[:10]:
    lines.append(f"| {r['referrer']} | {r['count']} | {r['uniques']} |")
lines.append("")
lines.append("## Most viewed paths, last 14 days")
lines.append("")
lines.append("| Path | Views | Unique |")
lines.append("|---|---|---|")
for p in paths[:10]:
    lines.append(f"| {p['path']} | {p['count']} | {p['uniques']} |")
(METRICS / "SNAPSHOT.md").write_text("\n".join(lines) + "\n")

print("merged")
