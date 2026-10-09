# Ananda Velas — empresa digital

Velas artesanales para eventos y Navidad. Meta: **$50,000 MXN/mes mínimo → $200,000 MXN/mes en 90 días**.

## Empieza aquí (hoy)
1. **Publicar en Mercado Libre:** `mercadolibre/publicaciones-navidad-eventos.md` → 8 publicaciones listas para copiar y pegar + checklist.
2. **Costos reales:** llena `costos/plantilla-costeo.csv` con lo que te cuestan los insumos. Sin esto no sabemos si cada precio deja ganancia.
3. **Moldes:** completa la tabla de moldes en `negocio/catalogo.md` (cuántos tienes, velas por colada, tiempo de curado).
4. **Impresoras:** `equipo/impresoras.md`.
5. **Plan completo:** `negocio/plan-90-dias.md`.

## El equipo de agentes (`.claude/agents/`)
| Agente | Para qué lo usas |
|---|---|
| `director-estrategia` | Experto en negocios digitales y orquestador: prioridades semanales, tablero, decisiones |
| `documentador-procesos` | Convierte cómo trabajas en manuales paso a paso (`procesos/`) |
| `tiktok-shop-lives` | TikTok Shop, guiones de lives, afiliados |
| `mercadolibre` | Publicaciones, precios por kit, reputación, Buen Fin, Ads |
| `tienda-online` | anandavelas.com, WhatsApp Business, Instagram, recompra |
| `ventas-eventos-mayoreo` | Regalos corporativos y recuerdos para eventos (la palanca más grande) |
| `estudio-mercado` | Competencia, tendencias, temporadas, qué moldes comprar |
| `costos-precios` | Costo unitario, precio por canal, márgenes |
| `contenido-tendencias` | Calendario de contenido, guiones, tendencias, fotos |
| `produccion-inventario` | Capacidad, plan de producción, inventario, ayudantes |
| `diseno-empaque-cricut` | Etiquetas personalizadas, Cricut, empaque de envío |
| `servicio-cliente` | Respuestas, reclamos, reseñas |
| `finanzas-fiscal` | Corte semanal, flujo de caja, SAT/RESICO, retenciones |

### Cómo usarlos
En Claude Code, dentro de esta carpeta, pide por nombre:
- "Usa el agente `mercadolibre` para preparar la publicación del kit de ángeles."
- "Que `director-estrategia` arme las prioridades de esta semana."
- "`documentador-procesos`: así hago las velas de soya: …"

Todos leen `CLAUDE.md` (contexto del negocio) y `negocio/catalogo.md`.

## Estructura
```
CLAUDE.md                    Contexto del negocio para todos los agentes
negocio/catalogo.md          Catálogo maestro, precios, mayoreo, aromas, moldes
negocio/plan-90-dias.md      Metas, mezcla por canal, plan semanal
mercadolibre/                Publicaciones listas y registro
costos/                      Fórmula de precios y plantilla de costeo
procesos/                    Manual de procesos (SOPs)
equipo/impresoras.md         Recomendación de impresoras
.claude/agents/              El equipo de agentes
```
