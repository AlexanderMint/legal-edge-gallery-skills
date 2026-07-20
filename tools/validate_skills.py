#!/usr/bin/env python3
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIRS = sorted(path.parent for path in ROOT.glob("*/SKILL.md"))
errors = []

if not SKILL_DIRS:
    errors.append("No SKILL.md files found")

for skill_dir in SKILL_DIRS:
    path = skill_dir / "SKILL.md"
    raw = path.read_bytes()

    if raw.startswith(b"\xef\xbb\xbf"):
        errors.append(f"{path}: UTF-8 BOM is not allowed")

    if b"\r" in raw:
        errors.append(f"{path}: contains CR/CRLF; LF is required")

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
        errors.append(f"{path}: closing --- not found")
        continue

    if end < 3:
        errors.append(f"{path}: frontmatter is incomplete")
        continue

    frontmatter_text = "\n".join(lines[1:end])

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as exc:
        errors.append(f"{path}: invalid YAML: {exc}")
        continue

    if not isinstance(frontmatter, dict):
        errors.append(f"{path}: frontmatter must be a mapping")
        continue

    name = frontmatter.get("name")
    description = frontmatter.get("description")

    if name != skill_dir.name:
        errors.append(f"{path}: name '{name}' must match folder '{skill_dir.name}'")

    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append(f"{path}: name must use kebab-case")

    if not isinstance(description, str) or not description.strip():
        errors.append(f"{path}: description must be a non-empty string")

    if len(description) > 500:
        errors.append(f"{path}: description should not exceed 500 characters")

    metadata = frontmatter.get("metadata")
    if metadata is not None and not isinstance(metadata, dict):
        errors.append(f"{path}: metadata must be a mapping")

    body = "\n".join(lines[end + 1:]).strip()
    if not body:
        errors.append(f"{path}: instruction body is empty")

calculator = ROOT / "legal-calculator" / "scripts" / "index.html"
if not calculator.exists():
    errors.append(f"{calculator}: missing")
else:
    html = calculator.read_text(encoding="utf-8")
    if "ai_edge_gallery_get_result" not in html:
        errors.append(f"{calculator}: missing ai_edge_gallery_get_result")
    if "JSON.stringify({ result:" not in html:
        errors.append(f"{calculator}: success result contract not found")
    if "JSON.stringify({" not in html or "error:" not in html:
        errors.append(f"{calculator}: error result contract not found")

if not (ROOT / ".nojekyll").exists():
    errors.append(".nojekyll is missing")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Validation passed: {len(SKILL_DIRS)} skills")
for skill_dir in SKILL_DIRS:
    print(f"- {skill_dir.name}")
