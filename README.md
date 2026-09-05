# agente-black-seller

Skills de venta para **Claude Code** y **Codex**, destiladas de la filosofia
**Black Seller** de [Alex Bobadilla](https://www.alexbobadilla.mx/).

Empaquetado conforme a [Agent Plugins v1.0.0](https://agent-plugins.org/specification).

> **Estado: en construccion.** Todavia no hay skills publicadas. Lo que existe hoy
> es la gobernanza del proyecto, el mapa del metodo y el manifiesto del plugin.
> Ver [Estado real](#estado-real) antes de intentar instalarlo.

---

## Que es

Un metodo de venta solo sirve en el momento en que estas vendiendo. El de Alex
Bobadilla vive hoy en sus libros, su podcast y las sesiones que imparte — lugares
donde no puedes consultarlo mientras preparas una cita o escribes una propuesta.

Este plugin lo vuelve invocable: skills que resuelven un momento concreto de la
venta y devuelven algo usable —un mapa de decisores, un guion de apertura, un caso
de ahorro cuantificado— en vez de un resumen teorico.

**El metodo es de Alex Bobadilla. Este repositorio es solo el vehiculo.**

## Quien es Alex Bobadilla

Ingeniero industrial con MBA por la UNAM y mas de 35 anos en areas comerciales.
Dirigio empresas como Levadura Azteca, del Grupo Modelo, coordinando cientos de
vendedores en la industria de la panificacion. Hoy es CEO de XL1, dedicada a
comercializacion de equipo medico, y lider en distribucion de equipos laser para
urologia en Latinoamerica.

Es autor de *Guia del vendedor profesional* y conduce el podcast
*El mundo de las ventas*.

## La filosofia Black Seller

Un **Black Seller** es, en su definicion, un vendedor con historial de resultados
sobresalientes de forma sostenida, sin importar la industria.

La filosofia se organiza en **cinco dominios**: desarrollo personal, conocimiento
del mercado y del producto, tecnicas de venta, networking, y procesos
administrativos y financieros.

Lo que la distingue del entrenamiento de ventas convencional es el orden. Casi
todos arrancan en tecnicas de cierre; aqui las tecnicas son el dominio 3 de 5, y
el primero es la persona que vende. La tesis: puedes tener el mejor producto y el
mejor mercado, pero si quien vende no esta preparado, no hay tecnica que lo salve.

A eso se suma la **Filosofia 360**, su enfoque de gestion: ante cada problema o
estrategia, producir dieciocho acciones o soluciones distintas para forzar la
creatividad y no quedarse en la primera respuesta. En este plugin no es una skill
suelta sino un **modo transversal** — cualquier skill puede ejecutarse "en modo
360" y devolver dieciocho alternativas antes de elegir.

## Estructura

```
agente-black-seller/
├── plugin.json          manifiesto Agent Plugins v1.0.0
├── skills/              una skill por directorio, cada uno con SKILL.md
├── corpus/              material fuente de Alex — unica fuente de verdad
├── knowledge/           destilacion del corpus en partes operables
└── governance/          vision, PRD, guardrails, backlog y arquitectura (RaiSE)
```

La dependencia es unidireccional: **corpus → knowledge → skills**. Una skill no
puede afirmar metodo que no exista en `knowledge/`, y `knowledge/` no puede
afirmar metodo que no exista en `corpus/`. Eso es lo que hace verificable la
trazabilidad: para cualquier cosa que diga el agente se puede senalar de donde
salio.

Ante un vacio del corpus, el comportamiento correcto es **declarar el vacio**, no
rellenarlo con conocimiento generico de ventas.

## Estado real

| Componente | Estado |
|------------|--------|
| Gobernanza (vision, PRD, guardrails, backlog, arquitectura) | Completa |
| Manifiesto `plugin.json` | Conforme a v1.0.0 |
| Mapa del metodo | Borrador, sin citas — `knowledge/DRAFT-mapa-del-metodo.md` |
| Corpus | **Vacio.** Bloquea la escritura de skills |
| Skills | Ninguna todavia |
| Validador de conformidad | Pendiente |

El corpus vacio es el bloqueo real. Hasta que el material fuente este versionado y
sea citable, ninguna skill puede escribirse sin violar la trazabilidad que el
proyecto se impuso.

## Instalacion

Todavia no. Cuando haya skills, cualquier cliente conforme a Agent Plugins v1.0.0
las descubrira leyendo `plugin.json` y recorriendo `skills/`.

## Atribucion y licencia

El metodo, los marcos y los ejemplos son obra de **Alex Bobadilla**. Este
repositorio los organiza para hacerlos operables; no los reclama como propios ni
sustituye su formacion, sus libros ni sus sesiones.

**La licencia esta sin definir a proposito.** Publicar bajo una licencia abierta
tendria consecuencias sobre material que no nos pertenece, asi que la decision le
corresponde a Alex. Hasta que la tome, este repositorio se comparte sin
otorgamiento expreso de derechos sobre el metodo.
