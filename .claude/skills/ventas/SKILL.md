---
name: ventas
description: Mayoreo y eventos: regalos corporativos, recuerdos de evento, cotizaciones y seguimiento. Abre directo al agente `ventas-eventos-mayoreo` de Ananda Velas.
argument-hint: "[qué necesitas]"
---
Delega esta petición de Noemi al subagente `ventas-eventos-mayoreo` usando la herramienta Agent con `subagent_type: "ventas-eventos-mayoreo"`.

Petición de Noemi: $ARGUMENTS

Si la petición viene vacía, pregúntale a Noemi en una línea qué necesita de este agente antes de lanzarlo.

Al lanzarlo, pásale la petición tal cual, más el contexto de esta conversación que necesite (fechas, decisiones, archivos relevantes). Cuando termine:
1. Muéstrale a Noemi un resumen corto en español de lo que hizo el agente y las preguntas que tenga.
2. Si creó o cambió archivos: `git pull --rebase origin claude/determined-fermat-0nfy34`, commit y push a esa rama.
