#!/usr/bin/env python3
"""Valida conformidad con Agent Plugins v1.0.0 y con los guardrails del proyecto.

Cubre must-spec-001..004 y should-spec-005. Sale con codigo 1 si algo falla,
para poder usarse como gate en CI.

Uso:  python3 tools/validate-plugin.py [ruta-del-plugin]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SCHEMA_URL = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
NAME_PATTERN = re.compile(r"^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")
MANIFEST_FIELDS = {
    "$schema", "name", "version", "description", "author",
    "homepage", "repository", "license", "keywords", "extensions",
}
AUTHOR_FIELDS = {"name", "email", "url"}

failures: list[str] = []


def check(condition: bool, message: str, guardrail: str = "") -> None:
    tag = f" [{guardrail}]" if guardrail else ""
    print(f"  {'PASS' if condition else 'FAIL'}  {message}{tag}")
    if not condition:
        failures.append(message)


def validate_manifest(root: Path) -> None:
    print("plugin.json")
    manifest_path = root / "plugin.json"
    if not manifest_path.is_file():
        check(False, "plugin.json existe en la raiz", "must-spec-001")
        return

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        check(False, f"plugin.json es JSON valido ({exc})", "must-spec-001")
        return

    check(manifest.get("$schema") == SCHEMA_URL, "$schema apunta a la version 1.0.0", "must-spec-001")

    name = manifest.get("name")
    check(isinstance(name, str) and bool(name), "name presente", "must-spec-001")
    if isinstance(name, str):
        check(bool(NAME_PATTERN.match(name)), f"name '{name}' cumple el patron", "must-spec-001")
        check(1 <= len(name) <= 64, "name entre 1 y 64 caracteres", "must-spec-001")

    extra = set(manifest) - MANIFEST_FIELDS
    check(not extra, f"sin propiedades fuera del esquema {sorted(extra) or ''}", "must-spec-001")

    author = manifest.get("author")
    if author is not None:
        check(isinstance(author, dict), "author es objeto, no cadena", "must-spec-001")
        if isinstance(author, dict):
            bad = set(author) - AUTHOR_FIELDS
            check(not bad, f"author sin propiedades extra {sorted(bad) or ''}", "must-spec-001")

    keywords = manifest.get("keywords", [])
    check(
        isinstance(keywords, list) and all(isinstance(k, str) for k in keywords),
        "keywords es lista de cadenas",
        "must-spec-001",
    )


def validate_skills(root: Path) -> None:
    print("\nskills/")
    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        print("  INFO  skills/ no existe todavia — es opcional en el estandar")
        return

    discovered = []
    for child in sorted(skills_dir.iterdir()):
        if not child.is_dir():
            continue
        skill_file = child / "SKILL.md"
        if not skill_file.is_file():
            check(False, f"'{child.name}/' no contiene SKILL.md", "must-spec-002")
            continue
        discovered.append(child.name)
        validate_skill_frontmatter(child.name, skill_file)

    print(f"  INFO  skills descubribles: {len(discovered)}")


def validate_skill_frontmatter(name: str, path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        check(False, f"{name}: SKILL.md abre con frontmatter YAML", "must-spec-003")
        return

    end = text.find("\n---", 3)
    if end == -1:
        check(False, f"{name}: frontmatter sin cierre", "must-spec-003")
        return

    frontmatter = text[3:end]
    for field in ("name", "description"):
        present = re.search(rf"^{field}\s*:", frontmatter, re.MULTILINE) is not None
        check(present, f"{name}: frontmatter declara '{field}'", "must-spec-003")

    body = text[end + 4 :]
    cites = re.search(r"\[S\d+\]|@\d{2}:\d{2}", body) is not None
    check(cites, f"{name}: cita al menos una fuente del corpus", "must-knowledge-002")


def validate_extras(root: Path) -> None:
    print("\notros")
    mcp = root / "mcp.json"
    if mcp.is_file():
        try:
            servers = json.loads(mcp.read_text(encoding="utf-8")).get("mcpServers", {})
        except json.JSONDecodeError:
            servers = {}
            check(False, "mcp.json es JSON valido", "must-spec-001")
        check(bool(servers), "mcp.json declara servidores reales", "should-spec-005")
    else:
        print("  INFO  sin mcp.json — correcto mientras no haya servidores MCP")


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    print(f"Validando {root.name} contra Agent Plugins v1.0.0\n")

    validate_manifest(root)
    validate_skills(root)
    validate_extras(root)

    print()
    if failures:
        print(f"NO CONFORME — {len(failures)} problema(s)")
        return 1
    print("CONFORME")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
