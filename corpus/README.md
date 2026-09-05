---
type: corpus-index
status: vacio
---

# Corpus — material fuente de Alex Bobadilla

Este directorio es la **unica fuente de verdad** del proyecto. Ninguna skill ni
archivo de `knowledge/` puede afirmar contenido de metodo que no este aqui
(`must-knowledge-001`).

## Estado

| Fuente | Estado | Nota |
|--------|--------|------|
| Sesion de ventas en comunidad EO | **Pendiente de ingerir** | Eduardo la compartio en chat el 2026-09-04. Es todo el material capturado de la sesion |
| Columna en Expansion, 2024-02-12 | **Consultada, no ingerida** | Fuente publica que define la Filosofia 360, los cinco dominios, las tres A y los KPIs. Resolvio el hueco que bloqueaba E2 |
| `Guia del vendedor profesional` (2021) | No consultado | Libro del autor. Probable origen del detalle de tecnicas y objeciones |
| Podcast `El mundo de las ventas` | No consultado | Fuente viva y extensa |

## Como agregar una fuente

El archivo original lo deposita Eduardo directamente. **El agente no transcribe ni
retipea el material**: cualquier reescritura deja de ser verbatim y rompe la
garantia de fidelidad que hace citable al corpus.

1. Deja el archivo aqui como `sesion-NN-descripcion.md` (o `.txt`, `.vtt`, `.srt`).
2. Si viene de video o audio, prefiere el formato con marcas de tiempo: `.vtt` y
   `.srt` ya traen la citabilidad resuelta.
3. Avisa al agente. El se encarga de insertar las marcas de seccion `[S##]` **sin
   tocar una sola palabra del texto**, y de escribir la cabecera de procedencia.

Para fuentes publicas de terceros —articulos, notas de prensa— no se copia el
texto: se guarda la referencia (URL, fecha, autor) y la sintesis propia en
`knowledge/`. El corpus verbatim se reserva para el material que Alex compartio
directamente.

## Esquema de citas

Cada fuente se marca por secciones tematicas `[S01]`, `[S02]`, ... Una cita en
`knowledge/` o en una skill se escribe como `sesion-01[S09]`.

Cuando la fuente traiga marcas de tiempo, la cita las usa directamente:
`sesion-01@00:14:32`.

Para fuentes publicas referenciadas, la cita es la URL con su fecha.

## Fidelidad

Las transcripciones automaticas llegan con errores de reconocimiento de voz
—nombres propios deformados, cifras dudosas, frases truncadas—. **No se corrigen en
el corpus**: el corpus guarda lo que se dijo tal como se capturo.

Las correcciones viven aparte, en `corpus/erratas.md`, como pares
`lo que dice la transcripcion → lo que en realidad se dijo`, y solo se agregan
cuando Eduardo o Alex confirman el dato. Asi se preserva el original y a la vez se
evita que una cifra mal transcrita termine dentro de una skill.
