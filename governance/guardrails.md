---
type: guardrails
title: "agente-black-seller: guardrails"
status: active
version: "1.0.0"
---

# Guardrails: agente-black-seller

> Guardrails de contenido, conformidad y calidad. Nivel MUST bloquea; nivel SHOULD se justifica al violarse.

---

## Guardrails Activos

### Spec Conformance

| ID | Level | Guardrail | Verification | Derived from |
|----|-------|-----------|--------------|--------------|
| must-spec-001 | MUST | plugin.json existe en la raiz del repositorio y declara $schema igual a https://agent-plugins.org/schemas/1.0.0/plugin.schema.json y un name valido de 1 a 64 caracteres en minusculas | Validador de conformidad en CI | RF-04 |
| must-spec-002 | MUST | Toda skill vive como subdirectorio inmediato de skills/ y contiene un archivo llamado exactamente SKILL.md | Validador de conformidad en CI | RF-04 |
| must-spec-003 | MUST | Todo SKILL.md declara frontmatter YAML con los campos requeridos name y description por la especificacion Agent Skills | Validador de conformidad en CI | RF-03 |
| must-spec-004 | MUST | Las extensiones especificas de cliente viven exclusivamente bajo directorios con namespace de dominio invertido y nunca contienen contenido de metodo | Revision de estructura en CI | RF-06 |
| should-spec-005 | SHOULD | mcp.json solo se agrega si el plugin declara servidores MCP reales; no se versiona un manifiesto vacio | Revision en code review | RF-04 |

### Knowledge Integrity

| ID | Level | Guardrail | Verification | Derived from |
|----|-------|-----------|--------------|--------------|
| must-knowledge-001 | MUST | Ninguna skill ni archivo de conocimiento afirma contenido de metodo que no este respaldado por el corpus del curso | Revision de trazabilidad antes de merge | RF-05 |
| must-knowledge-002 | MUST | Cada archivo de conocimiento declara la referencia al fragmento del corpus del que proviene | Validador de citas en CI | RF-05 |
| must-knowledge-003 | MUST | Ante un vacio del corpus el agente declara el vacio y no lo rellena con conocimiento generico de ventas | Revision de prompts y pruebas de comportamiento | RF-07 |
| should-knowledge-004 | SHOULD | El corpus se versiona en el repositorio en formato de texto plano diffeable, no como binario opaco | Revision en code review | RF-01 |

### Content Quality

| ID | Level | Guardrail | Verification | Derived from |
|----|-------|-----------|--------------|--------------|
| must-quality-001 | MUST | Cada skill produce un artefacto usable en la venta real y no un resumen teorico del metodo | Revision de salida antes de merge | RF-03 |
| should-quality-002 | SHOULD | Las skills se escriben en el idioma del material fuente para preservar la voz y los terminos propios del metodo | Revision en code review | RF-07 |
| should-quality-003 | SHOULD | Ninguna skill supera un alcance que justifique dividirla en dos momentos distintos de la venta | Revision de diseno de skill | RF-03 |

### Security and Privacy

| ID | Level | Guardrail | Verification | Derived from |
|----|-------|-----------|--------------|--------------|
| must-security-001 | MUST | El repositorio es publico: no se versionan credenciales, rutas absolutas de estaciones de trabajo, ni datos personales de prospectos o clientes reales | Escaneo de secretos y revision antes de commit | RF-01 |
| must-security-002 | MUST | El material fuente de Alex Bobadilla solo se publica con su autorizacion explicita; sin ella el corpus permanece fuera del control de versiones publico | Confirmacion documentada del autor del metodo | RF-01 |
