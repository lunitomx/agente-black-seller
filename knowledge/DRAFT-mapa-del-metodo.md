---
type: knowledge-draft
status: draft
source_pending: "corpus/sesion-01-eo-ventas.md (aun no ingerido — ver corpus/README.md)"
author_of_method: "Alex Bobadilla"
drafted_at: "2026-09-04"
revised_at: "2026-09-05"
---

# Mapa del metodo — lectura estructural (BORRADOR)

> **BORRADOR SIN VALIDAR.** La sesion de EO aun no esta versionada en `corpus/`,
> asi que las referencias `[S##]` apuntan a secciones que todavia no existen.
> Nada de este archivo pasa a una skill hasta que el corpus se ingiera y cada
> afirmacion quede citada (`must-knowledge-002`).

---

## Black Seller: la filosofia que le da nombre al proyecto

**Black Seller no es un apodo, es la filosofia de Alex Bobadilla.** Su definicion,
de su propio sitio: un Black Seller es un vendedor con historial de resultados
sobresalientes de forma sostenida, sin importar la industria.

## Los cinco dominios

Confirmados por tres fuentes publicas independientes —su sitio oficial, una
entrevista en prensa y su columna en Expansion—:

| # | Dominio | Contenido |
|---|---------|-----------|
| 1 | **Desarrollo personal** | Confianza y seguridad propia por via integral: emocional, espiritual, fisico |
| 2 | **Conocimiento del mercado / producto** | Entenderlo a fondo para saber hacia donde va el negocio |
| 3 | **Tecnicas de venta** | Cierres y metodologias |
| 4 | **Networking** | Red de relaciones que produce oportunidades y estrategia |
| 5 | **Procesos administrativos y financieros** | Fundamentos de negocio y finanzas |

## Filosofia 360 — una cuota de alternativas, no una lista de pasos

Fuente: columna de opinion del propio autor en Expansion, 2024-02-12.

La Filosofia 360 es un enfoque de gestion que consiste en **producir 18 acciones o
soluciones distintas ante cada problema o estrategia**, con el proposito de forzar
la creatividad. **El 18 es una cuota, no un indice.** No hay dieciocho pasos
ordenados que memorizar: hay una exigencia de no detenerse en la primera respuesta.

> **Consecuencia de diseno.** Esto no debe implementarse como una skill que recite
> dieciocho pasos. Es un **modo generativo transversal**: cualquier skill del
> catalogo puede ejecutarse "en modo 360", obligando a generar dieciocho salidas
> antes de elegir. Una skill de objeciones en modo 360 no entrega la respuesta
> correcta — entrega dieciocho y despues se escoge.
>
> Decision pendiente de confirmar con Eduardo: modo transversal (recomendado)
> contra skill suelta.

## Las tres A

Exigidas a todo empleado, del CEO al puesto de entrada: **Actitud, Aptitud,
Accion**. Alimentan el dominio 1 y son criterio de contratacion, no solo de
desempeno. Coincide con lo que cuenta en la sesion sobre haber despedido a alguien
con todos los certificados y credenciales por tener mala actitud.

## KPIs que el mismo declara

- Actividad de prospeccion mensual.
- Tasa de conversion por encima del **50%** — cinco de cada diez prospectos
  convertidos en clientes.

Estos numeros son suyos y publicos, asi que sirven de vara para las skills del
dominio 5. Su tesis de fondo: perseguir crecimiento exponencial —2 o 3X anual— en
vez de metas modestas, sostenido por un equipo de Black Sellers.

## Los dos triangulos — no confundirlos

La sesion y las fuentes publicas contienen **dos triangulos distintos**:

- **Triangulo del crecimiento** (asi lo llama en la sesion, lo atribuye a su primer
  libro): *mercado — producto — tu*. Aqui aplica Pareto: tu eres el 80%.
- **Triangulo del equilibrio** (asi aparece en su ficha de conferencista): los tres
  pilares de la persona, *espiritual — emocional — fisico*. Es el contenido del
  dominio 1.

El primero ordena el negocio, el segundo ordena a la persona. Confundirlos romperia
la fidelidad de dos skills a la vez.

> **A verificar con Alex:** que sean efectivamente dos y no uno renombrado.

## La tesis central

El metodo esta invertido respecto al entrenamiento de ventas convencional. Casi
todos arrancan en tecnicas de cierre; aqui las tecnicas son el dominio 3 de 5, y el
dominio 1 es la persona. Cuando en la sesion le piden tecnicas, responde que si,
que van a hablar de todo, pero que si la persona no vende, la tecnica no tiene
sobre que aplicarse.

No es relleno motivacional: es una decision de arquitectura, y explica el orden de
todo lo demas.

## Los movimientos caracteristicos

Aqui vive la voz. Es lo que hay que preservar con mas cuidado al destilar:

- **Subir de nivel hasta llegar al deseo.** Taladro → hoyo → tornillo → sala
  confortable → la reaccion del compadre. La venta ocurre en el ultimo eslabon.
- **Preguntar "¿cual es tu negocio?" hasta que incomode.** Repetido tres o cuatro
  veces sobre la misma persona hasta que la respuesta cambia.
- **Buscar al vendedor detras del gigante.** No compites contra el corporativo;
  compites contra la persona que manda. Ese si es de tu tamano.
- **Vender el resultado economico del cliente, no la especificacion.**
- **Calcular el ahorro del otro antes de hablar de tu precio.** Si su ahorro es un
  orden de magnitud mayor que tu factura, el precio deja de ser tema.
- **Asumir el riesgo para eliminar la objecion.** Piloto, prueba, devolucion.
- **Diagnosticar por personaje.** Al tecnico, soporte. Al usuario, facilidad. Al
  financiero, retorno. Al que decide en casa, tranquilidad.

## Catalogo de skills propuesto

Organizado por los cinco dominios, para que la estructura del plugin sea la de Alex
y no una invencion nuestra. Cada skill entrega un artefacto usable
(`must-quality-001`). La granularidad final se decide con el corpus ingerido (D3).

| Dominio | Skill | Artefacto que entrega |
|---------|-------|----------------------|
| 1. Personal | `diagnostico-black-seller` | Estado del triangulo del equilibrio y de las tres A, con plan de correccion |
| 2. Mercado/producto | `cual-es-mi-negocio` | Redefinicion del negocio por lo que provoca, no por lo que produce |
| 2. Mercado/producto | `descomoditizar` | Ejes de diferenciacion y nichos con potencial de volumen |
| 3. Tecnicas | `personajes-de-la-venta` | Mapa de decisores con el argumento especifico de cada uno |
| 3. Tecnicas | `dolor-real` | Traduccion del producto al dolor, miedo u obligacion del cliente |
| 3. Tecnicas | `pitch-dos-minutos` | Guion corto de apertura construido sobre lo que el otro quiere |
| 3. Tecnicas | `objeciones` | Respuestas desde el valor, no desde el descuento |
| 3. Tecnicas | `protocolo-vendedor` | Guion repetible para que el equipo venda con el mismo criterio |
| 4. Networking | `mapa-de-relaciones` | Plan de relacionamiento con quien decide en el sector |
| 5. Admin/finanzas | `dimension-mercado` | Tamano estimado, participacion actual, meta y brecha |
| 5. Admin/finanzas | `negociar-valor` | Caso de ahorro o retorno cuantificado, mas oferta de piloto |
| 5. Admin/finanzas | `scorecard` | Prospeccion mensual y tasa de conversion contra la vara del 50% |
| **Transversal** | **modo 360** | Dieciocho alternativas para el problema que tenga enfrente cualquier skill |

## Huecos restantes

| Hueco | Estado | Impacto |
|-------|--------|---------|
| Tecnicas de cierre, paso a paso | Anunciadas en la sesion, no desarrolladas | Dominio 3 incompleto |
| Procedimiento de objeciones | Solo el principio (no negociar precio) | Dominio 3 |
| Anclajes y programacion neurolinguistica | Mencionados como necesarios | Dominio 3 |
| Sus libros | `Guia del vendedor profesional` (2021) y los otros dos | Fuente primaria no consultada — probable origen del detalle que falta |
| Podcast `El mundo de las ventas` | No consultado | Fuente viva y extensa |

Filosofia 360 sale de la lista de huecos: **resuelta el 2026-09-05.**

## Nota de fidelidad

La transcripcion de la sesion es automatica y trae errores densos de reconocimiento
de voz: nombres propios deformados, cifras dudosas y frases truncadas. Antes de
citar cualquier dato duro —cifras, marcas, nombres— hay que verificarlo. Los
ejemplos numericos de este borrador se tomaron como ilustrativos, no como datos
confirmados.

Los datos de esta pagina que **si** estan confirmados por fuente publica del autor
son: los cinco dominios, la definicion de Filosofia 360, las tres A y los KPIs.
