---
type: architecture_context
title: "agente-black-seller: system context"
project: "agente-black-seller"
status: draft
tech_stack:
  spec: Agent Plugins v1.0.0
  skill_format: Agent Skills (SKILL.md + YAML frontmatter)
  manifest: JSON (plugin.json, mcp.json)
  knowledge: Markdown versionado en git
  governance: RaiSE
external_dependencies:
  - Agent Plugins Specification v1.0.0
  - Agent Skills Specification
  - Claude Code runtime
  - Codex CLI runtime
  - GitHub (lunitomx/agente-black-seller)
users:
  - eduardo-munoz-luna
  - alex-bobadilla
  - claude-code-agent
  - codex-agent
governed_by: []
---

# System Context: agente-black-seller

> C4 Level 1 — Contexto de sistema

## Overview

agente-black-seller es un paquete de contenido, no un servicio. No expone red, no persiste estado propio y no tiene tiempo de ejecucion independiente: se instala dentro de un cliente de agente conforme al estandar Agent Plugins, y es ese cliente quien lo descubre, lo carga y ejecuta sus skills.

El sistema tiene una unica entrada de conocimiento — el material del curso de Alex Bobadilla — y una unica salida — artefactos de venta producidos dentro de la sesion de trabajo del operador.

## Context Diagram

```
  Alex Bobadilla                                       Claude Code
  (autor del metodo)                                   (cliente conforme)
        |                                                     ^
        | material del curso (3h)                             |
        v                                                     |
  +-----------------+        instala        +--------------------------+
  |   Eduardo       | --------------------> |   agente-black-seller    |
  |   Munoz Luna    |                       |   (Agent Plugin v1.0.0)  |
  |   (operador)    | <-------------------- |                          |
  +-----------------+   artefactos de venta +--------------------------+
                                                          |
                                                          v
                                                    Codex CLI
                                                 (cliente conforme)
```

## External Interfaces

| System | Direction | Protocol | Description |
|--------|-----------|----------|-------------|
| Claude Code | Inbound | Descubrimiento de plugin y skills segun Agent Plugins v1.0.0 | El cliente lee plugin.json, descubre skills/*/SKILL.md y expone las skills al operador |
| Codex CLI | Inbound | Descubrimiento de plugin y skills segun Agent Plugins v1.0.0 | Mismo paquete portable; las diferencias de cliente viven en directorios con namespace |
| Material del curso | Inbound | Entrega manual de grabacion, transcripcion o notas | Fuente unica de verdad del metodo; entra al repositorio como corpus versionado |
| GitHub | Outbound | HTTPS / git | Distribucion publica del plugin en lunitomx/agente-black-seller |
| Agent Plugins Specification | Inbound | Documento normativo | Define plugin.json, layout de skills/, mcp.json y namespacing de extensiones |
| Agent Skills Specification | Inbound | Documento normativo | Define el formato de SKILL.md y su frontmatter |

## Actores

| Actor | Rol |
|-------|-----|
| Alex Bobadilla | Autor del metodo y fuente de autoridad. Autoriza que material es publicable |
| Eduardo Munoz Luna | Operador y mantenedor. Toma el curso, entrega el material y usa las skills en venta real |
| Cliente de agente | Claude Code o Codex. Descubre y ejecuta el plugin; gestiona permisos e instalacion |
