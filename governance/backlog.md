# Backlog: agente-black-seller

> **Status**: Active

## Epics

| ID | Epic | Status | Scope | Priority |
|----|------|--------|-------|----------|
| E1 | Ingesta y corpus del curso | Ready | Recibir el material del curso de tres horas, convertirlo en corpus versionado y citable, y decidir con Alex Bobadilla que parte es publicable | P0 |
| E2 | Destilacion del metodo | Blocked by E1 | Transformar el corpus en archivos de conocimiento estructurados: etapas, calificacion, guiones, objeciones, cierre, seguimiento | P0 |
| E3 | Esqueleto del plugin conforme al estandar | **Done (2026-09-05)** | plugin.json, layout skills/, validador de conformidad Agent Plugins v1.0.0 en CI | P0 |
| E4 | Catalogo de skills | Blocked by E2 | Escribir las skills invocables, cada una con SKILL.md conforme a Agent Skills y con citas al corpus | P1 |
| E5 | Portabilidad dual e instalacion | **Ready** | Extensiones con namespace para Claude Code y Codex, instrucciones de instalacion, prueba en ambos runtimes | P1 |

## Notas de Secuencia

- E1 y E3 pueden avanzar en paralelo: E3 no depende del contenido del curso, solo del estandar.
- E1 tiene un bloqueo externo: Eduardo entrega el material del curso. Hasta entonces E1 no arranca.
- E2 es el cuello de botella real del proyecto; su calidad determina la de E4.
- **E3 cerrado el 2026-09-05:** `plugin.json` conforme, `skills/` con contrato de
  layout y `tools/validate-plugin.py` como gate (pasa con exit 0, 0 skills
  descubribles todavia). Eso desbloquea E5, que ya no depende de nadie.
- **El unico bloqueo vivo del proyecto es E1**, y es externo: la entrega del
  material del curso. E4 espera a E2, y E2 espera a E1.

## Decisiones Abiertas

| ID | Decision | Estado | Impacto |
|----|----------|--------|---------|
| D3 | Granularidad del catalogo de skills | Abierta | Se resuelve al terminar E2, cuando se vea la forma real del metodo |

## Decisiones Cerradas

| ID | Decision | Resuelta | Resolucion |
|----|----------|----------|------------|
| D1 | Stack de implementacion del validador de conformidad | 2026-09-05 | **Python 3, sin dependencias.** Implementado en `tools/validate-plugin.py`; cubre must-spec-001..004 y should-spec-005 y sale con codigo 1, apto como gate de CI |
| D2 | Publicabilidad del corpus en repositorio publico | 2026-09-04 | **Publicable.** El curso se impartio en abierto y Alex Bobadilla permite subirlo y compartirlo, segun confirmacion de Eduardo. Satisface `must-security-002` |
