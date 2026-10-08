#!/usr/bin/env python3
"""Check the skill, local package metadata, links, and benchmark fixtures."""
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/asdify/SKILL.md"
LINK = re.compile(r"\[[^\]]+\]\(([^)]*)\)")


class HTMLLinks(HTMLParser):
    """Collect links and images used by GitHub's Markdown renderer."""

    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if (tag, name) in {("a", "href"), ("img", "src"), ("source", "src")}:
                self.urls.append(value or "")
            elif tag == "source" and name == "srcset":
                self.urls.extend(part.strip().split()[0] for part in (value or "").split(",") if part.strip())


def validate_skill():
    content = SKILL.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    end = content.find("\n---\n", 4)
    if end == -1:
        raise ValueError("Missing end of YAML frontmatter")
    header = content[4:end]
    name = re.search(r"^name:\s*(.+)$", header, re.M)
    desc = re.search(r"^description:\s*>\s*\n((?:[ \t]+[^\n]+\n?)+)", header, re.M)
    if not name or name.group(1).strip() != SKILL.parent.name:
        raise ValueError("Skill name must match folder")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1).strip()):
        raise ValueError("Invalid skill name")
    if not desc or not (1 <= len(" ".join(desc.group(1).split())) <= 1024):
        raise ValueError("Missing or overlong description")
    if len(content.splitlines()) > 500:
        raise ValueError("SKILL.md should stay below 500 lines")
    for token in ("lite", "full", "ultra", "meaning", "uncertainty", "ASD-STE100"):
        if token not in content:
            raise ValueError(f"Missing required principle {token}")


def validate_links():
    errors = []
    for path in ROOT.rglob("*.md"):
        if any(part.startswith(".") and part != ".github" for part in path.relative_to(ROOT).parts):
            continue
        content = path.read_text(encoding="utf-8")
        html = HTMLLinks()
        html.feed(content)
        urls = [url.strip().split()[0] if url.strip() else "" for url in LINK.findall(content)]
        for url in urls + html.urls:
            if not url.strip():
                errors.append(f"{path.relative_to(ROOT)}: empty link destination")
                continue
            url = url.strip().strip("<>")
            target = urlsplit(url)
            if target.scheme or target.netloc or url.startswith("/"):
                continue
            local = unquote(target.path)
            if not local:
                continue
            if not (path.parent / local).exists():
                errors.append(f"{path.relative_to(ROOT)}: missing {local}")
    if errors:
        raise ValueError("Broken relative links:\n" + "\n".join(errors))


def validate_readme_assets():
    """Check that README SVGs are accessible, self-contained vector images."""
    paths = sorted((ROOT / "assets/readme").glob("*.svg"))
    for path in paths:
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError as exc:
            raise ValueError(f"{path.name}: invalid SVG XML: {exc}") from exc
        if root.tag != "{http://www.w3.org/2000/svg}svg":
            raise ValueError(f"{path.name}: expected an SVG root with its namespace")
        try:
            view_box = [float(value) for value in root.get("viewBox", "").replace(",", " ").split()]
        except ValueError:
            view_box = []
        if len(view_box) != 4 or not all(math.isfinite(value) for value in view_box) or min(view_box[2:]) <= 0:
            raise ValueError(f"{path.name}: viewBox must have four finite values and positive dimensions")
        for tag in ("title", "desc"):
            node = root.find(f"{{http://www.w3.org/2000/svg}}{tag}")
            if node is None or not "".join(node.itertext()).strip():
                raise ValueError(f"{path.name}: missing accessible {tag}")
        for node in root.iter():
            tag = node.tag.rsplit("}", 1)[-1]
            if tag in {"script", "foreignObject", "image"}:
                raise ValueError(f"{path.name}: use self-contained SVG vectors, found {tag}")
            for attr, value in node.attrib.items():
                attr = attr.rsplit("}", 1)[-1]
                if attr.startswith("on") or (attr == "href" and not value.startswith("#")):
                    raise ValueError(f"{path.name}: unsupported external or interactive attribute {attr}")
    return len(paths)


def validate_cases():
    path = ROOT / "benchmarks/cases.jsonl"
    ids = set()
    languages = set()
    for index, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"case {index}: invalid JSON: {exc.msg}") from exc
        if not isinstance(item, dict):
            raise ValueError(f"case {index}: expected a JSON object")
        for field in ("id", "lang", "task", "risk"):
            value = item.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"case {index}: {field} must be a nonempty string")
        invariants = item.get("invariants")
        if not isinstance(invariants, list) or not invariants or any(
            not isinstance(value, str) or not value.strip() for value in invariants
        ):
            raise ValueError(f"case {index}: invariants must be a nonempty list of nonempty strings")
        if item["id"] in ids:
            raise ValueError(f"case {index}: duplicate id {item['id']!r}")
        if item["lang"] not in ("en", "pt-BR"):
            raise ValueError(f"case {index}: lang must be en or pt-BR")
        ids.add(item["id"])
        languages.add(item["lang"])
    if len(ids) < 6:
        raise ValueError("Need at least 6 evaluation cases")
    if languages != {"en", "pt-BR"}:
        raise ValueError("Evaluation cases must cover both en and pt-BR")
    return len(ids)


def validate_manifests():
    """Validate this repository's local plugin entry, not the full host schema."""
    plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    if not isinstance(plugin, dict) or not isinstance(marketplace, dict):
        raise ValueError("Plugin and marketplace manifests must be JSON objects")
    if plugin.get("name") != SKILL.parent.name:
        raise ValueError("Plugin name must match the canonical skill folder")
    version = plugin.get("version")
    if not isinstance(version, str) or not re.fullmatch(
        r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?",
        version,
    ):
        raise ValueError("Plugin version must use a major.minor.patch format")
    for field in ("description", "license"):
        value = plugin.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Plugin {field} must be a nonempty string")
    entries = marketplace.get("plugins")
    if not isinstance(entries, list) or not all(isinstance(entry, dict) for entry in entries):
        raise ValueError("Marketplace plugins must be a list of objects")
    matching = [entry for entry in entries if entry.get("name") == plugin["name"]]
    if len(matching) != 1:
        raise ValueError("Marketplace must contain exactly one entry matching the plugin name")
    entry = matching[0]
    source = entry.get("source")
    if not isinstance(source, str) or not source.startswith("./") or (ROOT / source).resolve() != ROOT.resolve():
        raise ValueError("Marketplace plugin source must resolve to this repository root")
    if "version" in entry and entry["version"] != version:
        raise ValueError("Marketplace and plugin versions must match when both are specified")


def main():
    validate_skill()
    validate_links()
    validate_manifests()
    images = validate_readme_assets()
    count = validate_cases()
    print(f"Validation OK: core skill, local plugin metadata, relative links, {images} SVGs, and {count} bilingual cases")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        sys.exit(1)
