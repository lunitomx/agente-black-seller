# skills/

Cada subdirectorio **inmediato** de `skills/` que contenga un archivo llamado
exactamente `SKILL.md` es una skill. Esa ubicacion no es configurable: la fija
Agent Plugins v1.0.0 y de ahi la descubren los clientes.

```
skills/
└── cual-es-mi-negocio/
    ├── SKILL.md          requerido — frontmatter YAML con name y description
    ├── references/       opcional — material de apoyo que la skill consulta
    └── scripts/          opcional — ejecutables que la skill invoca
```

## Contrato de cada skill

1. **Resuelve un momento concreto de la venta**, no un tema. Si abarca dos
   momentos distintos, son dos skills (`should-quality-003`).
2. **Entrega un artefacto usable** —un mapa, un guion, un calculo— nunca un
   resumen teorico del metodo (`must-quality-001`).
3. **Cita su fuente.** Toda afirmacion de metodo referencia el punto del corpus
   que la respalda (`must-knowledge-002`). Sin fuente, no se afirma.
4. **Declara el vacio cuando el corpus no cubre el caso.** No se rellena con
   conocimiento generico de ventas (`must-knowledge-003`).
5. **Se escribe en el idioma del material fuente** para preservar la voz y los
   terminos propios del metodo (`should-quality-002`).

## Modo 360

Cualquier skill puede ejecutarse en modo 360: en vez de entregar una respuesta,
genera dieciocho alternativas antes de elegir. Es la Filosofia 360 de Alex
Bobadilla aplicada al artefacto que la skill produce.

No es una skill aparte. Se documenta en cada `SKILL.md` que lo soporte.

## Estado

Vacio. Las skills no pueden escribirse hasta que el corpus este ingerido — ver
`corpus/README.md`. El catalogo propuesto vive en
`knowledge/DRAFT-mapa-del-metodo.md`.
