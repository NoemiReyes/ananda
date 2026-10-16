---
name: director
description: Dirección y estrategia: prioridades de la semana, tablero, decisiones y reparto de trabajo. Abre directo al agente `director-estrategia` de Ananda Velas.
argument-hint: "[qué necesitas]"
---
Delega esta petición de Noemi al subagente `director-estrategia` usando la herramienta Agent con `subagent_type: "director-estrategia"`.

Petición de Noemi: $ARGUMENTS

Si la petición viene vacía, pregúntale a Noemi en una línea qué necesita de este agente antes de lanzarlo.

Al lanzarlo, pásale la petición tal cual, más el contexto de esta conversación que necesite (fechas, decisiones, archivos relevantes). Cuando termine:
1. Muéstrale a Noemi un resumen corto en español de lo que hizo el agente y las preguntas que tenga.
2. Si creó o cambió archivos: `git pull --rebase origin claude/determined-fermat-0nfy34`, commit y push a esa rama.
