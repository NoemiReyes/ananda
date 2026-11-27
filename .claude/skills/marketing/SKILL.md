---
name: marketing
description: Marketing digital completo: estrategia, campañas por temporada, presupuesto de ads y KPIs. Abre al agente líder `marketing-digital` y, si hace falta, lanza a su equipo (ads, creativos, SEO, CRM, influencers, analítica).
argument-hint: "[qué necesitas]"
---
Petición de Noemi: $ARGUMENTS

Si la petición viene vacía, pregúntale a Noemi en una línea qué necesita de marketing antes de lanzar nada.

Los subagentes no pueden lanzar a otros subagentes, así que **tú (el chat principal) coordinas al equipo**:

1. **Plan:** lanza `marketing-digital` (Agent, `subagent_type: "marketing-digital"`) con la petición y el contexto de esta conversación. Pídele que termine con el bloque `## ASIGNACIONES`.
2. **Ejecución:** si hay asignaciones, lanza **en paralelo** (en un mismo mensaje) a cada especialista listado — `marketing-ads`, `marketing-creativos`, `marketing-seo`, `marketing-crm`, `marketing-influencers`, `marketing-analitica` — con su tarea, el resumen del plan y la ruta del archivo de campaña. Si una tarea depende de otra (ej. creativos necesitan la estructura de ads), lánzalas en orden.
3. **Integración:** si los entregables se contradicen o falta cerrar números (presupuesto, ROAS, fechas), vuelve con `marketing-digital` (SendMessage al mismo agente si sigue disponible) para que integre y decida.
4. Si una petición es claramente de un solo especialista, puedes ir directo a él y saltarte el paso 1.

Al terminar:
1. Muéstrale a Noemi un resumen corto en español: decisiones, presupuesto, qué hace ella y cuándo, y las preguntas pendientes.
2. Si se crearon o cambiaron archivos: `git pull --rebase origin claude/determined-fermat-0nfy34`, commit y push a esa rama.
