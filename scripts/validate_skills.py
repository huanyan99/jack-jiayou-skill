"""Validate skill entrypoints without executing skill resources."""
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]


def validate(folder):
    errors = []
    entry = folder / "SKILL.md"
    if not entry.is_file():
        return [f"{folder.name}: missing SKILL.md"]
    text = entry.read_text(encoding="utf-8-sig")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)(.*)", text, re.S)
    if not match:
        return [f"{folder.name}: missing YAML frontmatter"]
    try:
        meta = yaml.safe_load(match[1])
    except yaml.YAMLError as exc:
        return [f"{folder.name}: invalid YAML: {exc}"]
    if not isinstance(meta, dict):
        return [f"{folder.name}: frontmatter must be a mapping"]
    name = meta.get("name")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append(f"{folder.name}: invalid name")
    if name != folder.name:
        errors.append(f"{folder.name}: name must match directory")
    description = meta.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        errors.append(f"{folder.name}: description must contain 1–1024 characters")
    if not match[2].strip():
        errors.append(f"{folder.name}: instruction body is empty")
    if "replace-with-skill-name" in text or "替换为" in text or re.search(r"\bTODO\b", text):
        errors.append(f"{folder.name}: unfinished template content")
    return errors


def main():
    folders = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir() and not p.name.startswith("."))
    errors = [error for folder in folders for error in validate(folder)]
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print(f"Validated {len(folders)} skill(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
