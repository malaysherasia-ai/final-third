#!/usr/bin/env python3
"""Check that package files exist and share the same version and name."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = "final-third"
REQUIRED = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    "agents/openai.yaml",
    "reference/metrics.md",
    "reference/prompts.md",
]

errors = []

for rel in REQUIRED:
    if not (ROOT / rel).exists():
        errors.append(f"missing file: {rel}")

skill = (ROOT / "SKILL.md").read_text() if (ROOT / "SKILL.md").exists() else ""
m = re.search(r'^\s*version:\s*"([^"]+)"', skill, re.M)
skill_version = m.group(1) if m else None
if not skill_version:
    errors.append("SKILL.md has no metadata.version")

if re.search(r"^name:\s*(.+)$", skill, re.M):
    skill_name = re.search(r"^name:\s*(.+)$", skill, re.M).group(1).strip()
    if skill_name != NAME:
        errors.append(f"SKILL.md name is {skill_name}, expected {NAME}")

plugin_path = ROOT / ".claude-plugin/plugin.json"
if plugin_path.exists():
    plugin = json.loads(plugin_path.read_text())
    if plugin.get("version") != skill_version:
        errors.append(
            f"version mismatch: plugin.json {plugin.get('version')} vs SKILL.md {skill_version}"
        )
    if plugin.get("name") != NAME:
        errors.append(f"plugin.json name is {plugin.get('name')}, expected {NAME}")

market_path = ROOT / ".claude-plugin/marketplace.json"
if market_path.exists():
    market = json.loads(market_path.read_text())
    names = [p.get("name") for p in market.get("plugins", [])]
    if NAME not in names:
        errors.append(f"marketplace.json does not list {NAME}")

for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    text = path.read_text()
    if "\u2014" in text or "\u2013" in text:
        errors.append(f"{path.relative_to(ROOT)} contains an em or en dash")
    if "GH_USER" in text:
        errors.append(f"{path.relative_to(ROOT)} still contains the GH_USER placeholder")

for rel in [".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"]:
    p = ROOT / rel
    if p.exists() and "GH_USER" in p.read_text():
        errors.append(f"{rel} still contains the GH_USER placeholder")

if errors:
    print("FAIL")
    for e in errors:
        print(f"  {e}")
    sys.exit(1)

print(f"OK  {NAME} {skill_version}")
