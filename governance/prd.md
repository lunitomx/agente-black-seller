# PRD: agente-black-seller

> Product Requirements Document

---

## Problem

Eduardo Munoz Luna tomo un curso de tres horas con Alex Bobadilla sobre su metodo de venta. Ese conocimiento existe hoy en tres estados, todos inoperables en el momento de la venta: en la grabacion del curso, en notas dispersas y en la memoria de quien lo tomo. Cuando llega una conversacion real de venta, el metodo no esta a la mano — y lo que si esta a la mano es el conocimiento generico de ventas de un modelo de lenguaje, que no es el metodo de Alex y contradice partes de el.

El costo es doble: el curso pierde valor cada semana que pasa sin operacionalizarse, y el trabajo de venta se hace con un metodo distinto al que se decidio adoptar.

## Goals

- Convertir el material del curso en un plugin de agente instalable y portable.
- Que el metodo se invoque en el flujo de trabajo real, no en una sesion aparte de consulta.
- Que toda afirmacion del agente sea rastreable al material fuente.
- Que el paquete cumpla Agent Plugins v1.0.0 y funcione en Claude Code y Codex sin bifurcarse.

## Non-Goals

- Agente autonomo de venta a clientes finales.
- Producto comercializable a terceros o a alumnos de Alex Bobadilla.
- Generacion de metodologia de venta no presente en el material fuente.

---

## Requirements

### RF-01: Ingesta del material fuente

El sistema debe aceptar el material del curso de tres horas — grabacion, transcripcion o notas — y convertirlo en un corpus versionado dentro del repositorio, con marcas de tiempo o referencias de seccion que permitan citar cualquier fragmento. El corpus es la unica fuente de verdad del proyecto: ninguna skill puede afirmar algo que no este en el.

### RF-02: Destilacion del metodo en base de conocimiento

El sistema debe transformar el corpus en archivos de conocimiento estructurados que separen el metodo en sus partes operables: etapas del proceso de venta, criterios de calificacion de prospecto, estructuras de guion, taxonomia de objeciones con sus respuestas, senales de cierre y cadencia de seguimiento. Cada archivo debe declarar de que parte del corpus proviene.

### RF-03: Catalogo de skills invocables

El sistema debe exponer el metodo como skills discretas, cada una en su propio directorio bajo skills/ con un archivo SKILL.md conforme a la especificacion Agent Skills. Cada skill resuelve un momento concreto de la venta y produce un artefacto usable, no un resumen teorico.

### RF-04: Conformidad con Agent Plugins v1.0.0

El paquete debe cumplir la especificacion Agent Plugins v1.0.0: plugin.json en la raiz con los campos requeridos $schema y name, skills descubribles como subdirectorios inmediatos de skills/ que contengan SKILL.md, mcp.json en la raiz si se declaran servidores MCP, y extensiones especificas de cliente confinadas a directorios con namespace de dominio invertido.

### RF-05: Trazabilidad a la fuente

Cada skill y cada archivo de conocimiento debe citar el punto del corpus que lo respalda. El sistema debe permitir responder, para cualquier afirmacion del agente, de que parte del curso proviene. Lo que no tiene fuente no se afirma.

### RF-06: Portabilidad entre Claude Code y Codex

El contenido portable — skills, conocimiento, manifiestos — debe ser identico para ambos runtimes. Las diferencias de cliente (hooks, comandos, configuracion de permisos) deben vivir exclusivamente en directorios de extension con namespace, sin duplicar contenido de metodo.

### RF-07: Salvaguarda de voz y anti-generico

El sistema debe impedir que el agente sustituya el metodo de Alex Bobadilla por conocimiento generico de ventas cuando el corpus no cubre un caso. Ante un vacio del corpus, el comportamiento correcto es declarar el vacio, no rellenarlo.

### RF-08: Validacion automatizada de conformidad

El sistema debe incluir una validacion ejecutable que verifique la conformidad estructural con Agent Plugins v1.0.0 y la presencia de citas de fuente en cada skill. La validacion debe correr como gate antes de cualquier publicacion del plugin.
