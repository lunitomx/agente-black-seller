---
type: architecture_design
title: "agente-black-seller: system design"
project: "agente-black-seller"
status: draft
layers:
  - name: manifest
    description: "Manifiestos normativos que hacen descubrible el paquete segun Agent Plugins v1.0.0"
    modules: [plugin-json, mcp-json]
  - name: corpus
    description: "Material fuente del curso de Alex Bobadilla, versionado y citable. Unica fuente de verdad"
    modules: [transcripcion, indice-de-referencias]
  - name: knowledge
    description: "Destilacion estructurada del corpus en partes operables del metodo"
    modules: [etapas, calificacion, guiones, objeciones, cierre, seguimiento, glosario]
  - name: skills
    description: "Skills invocables conformes a Agent Skills, una por momento de la venta"
    modules: [skill-diagnostico, skill-guion, skill-objeciones, skill-cierre, skill-seguimiento]
  - name: extensions
    description: "Capacidades especificas de cliente bajo namespace de dominio invertido; sin contenido de metodo"
    modules: [claude-code-extension, codex-extension]
  - name: validation
    description: "Gate ejecutable de conformidad con el estandar y de trazabilidad de citas"
    modules: [validador-spec, validador-citas]
---

# System Design: agente-black-seller

> C4 Level 2 — Descomposicion en componentes

## Architecture Overview

El diseno sigue una direccion unica de dependencia: corpus -> knowledge -> skills. Nada fluye en sentido contrario. Una skill no puede introducir metodo que no exista en knowledge, y knowledge no puede introducir metodo que no exista en corpus. Esa direccionalidad es lo que hace verificable la trazabilidad exigida por RF-05.

Las capas manifest y extensions son ortogonales al contenido: existen para que el paquete sea descubrible y portable, y deliberadamente no contienen metodo. La capa validation cruza todas las demas como gate, no como dependencia de ejecucion.

La estructura fisica del repositorio es la que impone Agent Plugins v1.0.0 — plugin.json en la raiz, skills/ con un subdirectorio por skill — y no es negociable ni configurable.

## Components

| Component | Responsibility | Technology |
|-----------|---------------|------------|
| plugin.json | Declara $schema, name y metadatos del plugin. Punto de entrada del descubrimiento | JSON conforme a plugin.schema.json 1.0.0 |
| mcp.json | Declara servidores MCP si el plugin llega a necesitarlos. Ausente mientras no haya ninguno | JSON conforme a mcp.schema.json 1.0.0 |
| corpus | Guarda el material del curso en texto diffeable con referencias de seccion o tiempo | Markdown versionado |
| knowledge | Destila el metodo en archivos por dominio, cada uno citando su origen en corpus | Markdown con referencias de fuente |
| skills | Un directorio por skill con SKILL.md, y scripts/ o references/ cuando aplique | Agent Skills (SKILL.md + frontmatter YAML) |
| extensions | Hooks y configuracion propios de Claude Code y de Codex, aislados por namespace | Directorios con dominio invertido |
| validation | Verifica estructura contra el estandar y presencia de citas en cada skill | Por decidir — ver D1 en backlog |

## Key Decisions

| Decision | Estado | Nota |
|----------|--------|------|
| Cumplir Agent Plugins v1.0.0 como estandar de empaquetado | Cerrada | Requisito explicito del proyecto. Fija el layout fisico del repositorio |
| El repositorio es el plugin — plugin.json vive en la raiz | Cerrada | Evita anidamiento innecesario; el paquete distribuible es el repositorio |
| Stack del validador de conformidad | Abierta (D1) | Candidato natural Python por alineacion con las reglas de RaiSE |
| Publicabilidad del corpus en repositorio publico | Abierta (D2) | Requiere autorizacion explicita de Alex Bobadilla — ver must-security-002 |
| Granularidad del catalogo de skills | Abierta (D3) | Se resuelve al terminar la destilacion; la forma del metodo la dicta |

<!-- ADRs pendientes: governance/adrs/ -->
