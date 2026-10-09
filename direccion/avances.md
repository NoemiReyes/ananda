# Avances del equipo de agentes: corte al 9-oct-2026

Índice de todo lo que ya existe, por chat y por agente. Lo mantiene el chat Dirección y se actualiza en cada corte semanal. Todo está guardado en la rama `claude/determined-fermat-0nfy34`.

Las definiciones de los 13 agentes están en `.claude/agents/`.

## Equipo humano
- **Noemi:** dueña, producción, ventas y redes.
- **Angélica:** tiempo completo desde el dom 11-oct. Aprende producción, graba contenido y busca tendencias.

## Avance por chat

| Chat | Agente | Lo que ya está hecho (archivos) | Lo que sigue (semana 9–16 oct) |
|---|---|---|---|
| **Dirección** | `director-estrategia` | `direccion/semana-2026-10-12.md` (prioridades, agenda de Noemi y Angélica, tablero), `direccion/dia-de-muertos-2026.md` (lanzamiento de veladoras y papel picado personalizados), `direccion/decisiones.md` (decisiones tomadas en chat), este archivo | Línea base del tablero (lun 12), cierre de la semana y plan de la semana 2 (vie 16) |
| | `finanzas-fiscal` | `finanzas/presupuesto-inicial.md` (mínimo $13,789, recomendado $42,079, completo $95,549; todo estimado), `finanzas/guia-fiscal.md` (RFC, RESICO, retenciones de plataformas, CFDI) | Ajustar el presupuesto con el pago de Angélica y la compra de la impresora. Corte semanal (vie 16). Primer pago al SAT: 17-nov |
| **Mercado Libre** | `mercadolibre` | `mercadolibre/publicaciones-navidad-eventos.md` (8 kits listos), `mercadolibre/competencia.md`, `mercadolibre/registro-publicaciones.md` | Precio en el simulador y 8 kits publicados (lun 12). Kit Ofrenda Familiar de Día de Muertos (jue 15) |
| | `servicio-cliente` | `servicio/respuestas-rapidas.md` | Respuestas para pedidos personalizados de Día de Muertos |
| **TikTok** | `tiktok-shop-lives` | `tiktok/checklist-verificacion.md`, `tiktok/productos.md`, `tiktok/lives/live-01.md` | Plan de activación cuando aprueben la tienda |
| | `contenido-tendencias` | `contenido/calendario.md` (10 al 23 oct), `contenido/guiones-semana-1.md`, `contenido/guia-fotos.md` | Guía de grabación para Angélica (sáb 10). Guiones de Día de Muertos (mar 13) |
| **Mayoreo y eventos** | `ventas-eventos-mayoreo` | `ventas/propuesta-corporativa-navidad.md`, `ventas/mensajes-prospeccion.md`, `ventas/plantilla-cotizacion.md`, `ventas/pipeline.md` | Lista de 100 empresas (mar 13). 30 contactos (mié 14 a vie 16) |
| | `diseno-empaque-cricut` | `diseno/sistema-etiquetas.md` (Imprimir y cortar), `diseno/empaque-envio.md` | Plantillas de veladora con foto y de papel picado con nombre (mar 13) |
| **Producción y costos** | `produccion-inventario` | `produccion/inventario.md`, `produccion/cuestionario-capacidad.md`, `produccion/calculadora-capacidad.md` | Día cronometrado (mar 13) → capacidad y compra de moldes (jue 15 y vie 16) |
| | `costos-precios` | `costos/README.md` (fórmula), `costos/insumos-referencia.md`, `costos/margenes-por-canal.md`, `costos/plantilla-costeo.csv`, `costos/calculo_costos.py` | Costos reales de Noemi (lun 12 → mié 14). Precios de Día de Muertos (mar 13) |
| | `documentador-procesos` | `procesos/001-publicar-mercadolibre.md`, `procesos/002-surtir-enviar-mercadolibre.md`, `procesos/cuestionario-fabricacion.md`, `procesos/pendientes.md`, `procesos/plantilla-sop.md` | Checklist de capacitación y seguridad de Angélica (sáb 10). SOP de fabricación (vie 16). SOP de pedido personalizado de Día de Muertos |
| **Estudio de mercado** | `estudio-mercado` | `mercado/competencia.md`, `mercado/demanda-y-temporalidad.md`, `mercado/proyeccion-realista.md` (ya incluye a Angélica), `mercado/fuentes/` | Corregir Día de Muertos en la temporalidad: ya hay producto (vie 16) |
| **Sin chat asignado** | `tienda-online` | Todavía no hay archivos | Catálogo de WhatsApp Business. Falta que Noemi decida en qué chat corre |

Otros archivos base: `negocio/catalogo.md`, `negocio/plan-90-dias.md`, `equipo/impresoras.md`.

## Datos que todavía faltan de Noemi (bloquean a varios agentes)
1. Costos reales de insumos y pesos por SKU → `costos-precios`.
2. Tabla de moldes (piezas, velas por colada, curado) → `produccion-inventario`.
3. RFC y régimen fiscal → `finanzas-fiscal` y precios en plataformas.
4. Pago y horario de Angélica → presupuesto.
5. Ciudad y contactos de empresas → `ventas-eventos-mayoreo`.
