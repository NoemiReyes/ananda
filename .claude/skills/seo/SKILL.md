---
name: seo
description: SEO y búsqueda: palabras clave, anandavelas.com, Google Business Profile y Pinterest. Abre directo al agente `marketing-seo` (equipo de marketing digital) de Ananda Velas.
argument-hint: "[qué necesitas]"
---
Delega esta petición de Noemi al subagente `marketing-seo` usando la herramienta Agent con `subagent_type: "marketing-seo"`.

Petición de Noemi: $ARGUMENTS

Si la petición viene vacía, pregúntale a Noemi en una línea qué necesita de este agente antes de lanzarlo.

Al lanzarlo, pásale la petición tal cual, más el contexto de esta conversación que necesite (fechas, decisiones, archivos relevantes). Si la tarea toca a varios especialistas de marketing, mejor usa el flujo de `/marketing`. Cuando termine:
1. Muéstrale a Noemi un resumen corto en español de lo que hizo el agente y las preguntas que tenga.
2. Si creó o cambió archivos: `git pull --rebase origin claude/determined-fermat-0nfy34`, commit y push a esa rama.
