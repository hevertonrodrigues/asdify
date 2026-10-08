#!/usr/bin/env python3
"""Check the skill, package metadata, language coverage, links, and fixtures."""
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
LANGUAGE_TAG = re.compile(r"[a-z]{2,3}(?:-[A-Z][a-z]{3})?(?:-(?:[A-Z]{2}|\d{3}))?")
AGENT_ROOTS = {
    "{HOME}", "{XDG_CONFIG_HOME}", "{CLAUDE_CONFIG_DIR}", "{AUTOHAND_HOME}",
    "{GROK_HOME}", "{HERMES_HOME}", "{VIBE_HOME}", "{OPENCLAW_HOME}",
}


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


def load_languages():
    """Load the project's language/script/region tags, not all of BCP 47."""
    path = ROOT / "integrations/languages.json"
    entries = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(entries, list) or not entries:
        raise ValueError("languages.json must contain a nonempty list")
    languages = {}
    for index, entry in enumerate(entries, 1):
        prefix = f"language {index}"
        if not isinstance(entry, dict) or set(entry) != {"tag", "name", "readme"}:
            raise ValueError(f"{prefix}: expected tag, name, and readme fields")
        for field, value in entry.items():
            if (
                not isinstance(value, str) or not value.strip() or value != value.strip()
                or any(ord(character) < 32 for character in value)
            ):
                raise ValueError(f"{prefix}: {field} must be a nonempty string without padding or control characters")
        tag = entry["tag"]
        if not LANGUAGE_TAG.fullmatch(tag):
            raise ValueError(f"{prefix}: tag must use language[-Script][-REGION] casing")
        if tag in languages:
            raise ValueError(f"{prefix}: duplicate language tag {tag!r}")
        expected = "README.md" if tag == "en" else f"README.{tag}.md"
        if entry["readme"] != expected:
            raise ValueError(f"{prefix}: readme must be {expected}")
        languages[tag] = entry
    if "en" not in languages:
        raise ValueError("languages.json must include the canonical en README")
    return languages


def validate_languages():
    """Require a nonempty README and language navigation for each locale."""
    languages = load_languages()
    readmes = {entry["readme"] for entry in languages.values()}
    for entry in languages.values():
        path = ROOT / entry["readme"]
        if not path.is_file():
            raise ValueError(f"{entry['tag']}: missing README {entry['readme']}")
        content = path.read_text(encoding="utf-8")
        if not content.strip():
            raise ValueError(f"{entry['tag']}: README must be nonempty")
        destinations = {unquote(urlsplit(url.strip()).path) for url in LINK.findall(content)}
        missing = readmes - {entry["readme"]} - destinations
        if missing:
            raise ValueError(f"{entry['tag']}: README language navigation missing {', '.join(sorted(missing))}")
    return len(languages)


def validate_cases():
    supported = set(load_languages())
    path = ROOT / "benchmarks/cases.jsonl"
    ids = set()
    rewrites = set()
    translation_sources = set()
    translation_targets = set()
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
        if item["lang"] not in supported:
            raise ValueError(f"case {index}: lang must be a registered language tag")
        if "target_lang" in item:
            target = item["target_lang"]
            if not isinstance(target, str) or target not in supported:
                raise ValueError(f"case {index}: target_lang must be a registered language tag")
            if target == item["lang"]:
                raise ValueError(f"case {index}: target_lang must differ from the source lang")
            translation_sources.add(item["lang"])
            translation_targets.add(target)
        else:
            rewrites.add(item["lang"])
        ids.add(item["id"])
    if len(ids) < 6:
        raise ValueError("Need at least 6 evaluation cases")
    for label, covered in (
        ("rewrite", rewrites),
        ("translation source", translation_sources),
        ("translation target", translation_targets),
    ):
        missing = supported - covered
        if missing:
            raise ValueError(f"Evaluation cases missing {label} coverage: {', '.join(sorted(missing))}")
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


def validate_agent_registry():
    """Check the local host map, without claiming that host loading was tested."""
    path = ROOT / "integrations/agents.tsv"
    identifiers = set()
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line or line.startswith("#"):
            continue
        columns = line.split("\t")
        prefix = f"agents.tsv line {line_number}"
        if len(columns) != 6 or any(not value or value != value.strip() for value in columns):
            raise ValueError(f"{prefix}: expected six nonempty tab-separated fields")
        agent, display_name, project_path, user_path, kind, source = columns
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", agent):
            raise ValueError(f"{prefix}: invalid agent id {agent!r}")
        if agent in identifiers:
            raise ValueError(f"{prefix}: duplicate agent id {agent!r}")
        identifiers.add(agent)
        if any(ord(character) < 32 for character in display_name):
            raise ValueError(f"{prefix}: invalid display name")
        if kind not in {"skill", "rule"}:
            raise ValueError(f"{prefix}: kind must be skill or rule")
        if project_path == user_path == "-":
            raise ValueError(f"{prefix}: at least one install scope is required")
        for scope, destination in (("project", project_path), ("user", user_path)):
            if destination == "-":
                continue
            parts = destination.split("/")
            if scope == "user":
                if parts[0] not in AGENT_ROOTS:
                    raise ValueError(f"{prefix}: user destination needs a supported root placeholder")
                parts = parts[1:]
            if not parts or any(
                part in {".", ".."} or not re.fullmatch(r"[A-Za-z0-9_.-]+", part)
                for part in parts
            ):
                raise ValueError(f"{prefix}: unsafe {scope} destination {destination!r}")
            if kind == "skill" and parts[-1] != "skills":
                raise ValueError(f"{prefix}: skill destination must be a skills directory")
            if kind == "rule" and parts[-1] != "asdify.mdc":
                raise ValueError(f"{prefix}: rule destination must name asdify.mdc")
        url = urlsplit(source)
        if (
            url.scheme != "https" or not url.hostname or not url.path.strip("/")
            or url.username or url.password or any(character.isspace() for character in source)
        ):
            raise ValueError(f"{prefix}: source must be a documentation HTTPS URL")
    if not identifiers:
        raise ValueError("agents.tsv must list at least one agent")
    return len(identifiers)


def main():
    validate_skill()
    validate_links()
    validate_manifests()
    agents = validate_agent_registry()
    images = validate_readme_assets()
    languages = validate_languages()
    count = validate_cases()
    print(f"Validation OK: core skill, local plugin metadata, {agents} agent destinations, relative links, {images} SVGs, {languages} languages, and {count} multilingual cases")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        sys.exit(1)
