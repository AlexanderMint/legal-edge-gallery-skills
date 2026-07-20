#!/usr/bin/env python3
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
skill_files = sorted(ROOT.glob("*/SKILL.md"))
errors = []

if not skill_files:
    errors.append("No SKILL.md files found")

names = set()

for path in skill_files:
    raw = path.read_bytes()

    if raw.startswith(b"\xef\xbb\xbf"):
        errors.append(f"{path}: UTF-8 BOM is not allowed")
    if b"\r" in raw:
        errors.append(f"{path}: CR/CRLF found; LF required")

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        errors.append(f"{path}: invalid UTF-8: {exc}")
        continue

    lines = text.splitlines()
    if not lines or lines[0] != "---":
        errors.append(f"{path}: first line must be exactly ---")
        continue

    try:
        end = lines.index("---", 1)
    except ValueError:
        errors.append(f"{path}: closing frontmatter delimiter missing")
        continue

    try:
        fm = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError as exc:
        errors.append(f"{path}: invalid YAML: {exc}")
        continue

    if not isinstance(fm, dict):
        errors.append(f"{path}: frontmatter must be a mapping")
        continue

    name = fm.get("name")
    description = fm.get("description")

    if name in names:
        errors.append(f"{path}: duplicate skill name {name}")
    names.add(name)

    if name != path.parent.name:
        errors.append(f"{path}: name must match folder")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append(f"{path}: invalid kebab-case name")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{path}: missing description")
    if len(description) > 500:
        errors.append(f"{path}: description is over 500 characters")

    body = "\n".join(lines[end + 1:]).strip()
    if not body:
        errors.append(f"{path}: empty instruction body")

    scripts_dir = path.parent / "scripts"
    if scripts_dir.exists():
        index = scripts_dir / "index.html"
        if not index.exists():
            errors.append(f"{path.parent}: scripts/index.html missing")
        else:
            html = index.read_text(encoding="utf-8")
            if "ai_edge_gallery_get_result" not in html:
                errors.append(f"{index}: entry function missing")
            if "JSON.stringify" not in html or "result:" not in html or "error:" not in html:
                errors.append(f"{index}: result/error contract missing")

required = {"legal-text-simplifier", "russian-law-search", "legal-contract-auditor"}
missing = required - names
if missing:
    errors.append(f"Required skills missing: {sorted(missing)}")

if not (ROOT / ".nojekyll").exists():
    errors.append(".nojekyll missing")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Validation passed: {len(skill_files)} skills")
for path in skill_files:
    print(f"- {path.parent.name}")
