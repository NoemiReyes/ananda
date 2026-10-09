# Proyección realista de ventas: oct-2026 a mar-2027 (de abajo hacia arriba)

**Fecha:** 9-oct-2026 · **Versión 2** (ajustada con el levantamiento verificado de ML y TikTok del 8-oct; ver `competencia.md` v2) · **Autor:** agente estudio-mercado

> **Cambios de la v2:** ML base baja de 30/50 a 24/40 pedidos en nov/dic y el optimista de 90/157 a 60/105, porque ningún artesanal verificado vende al ritmo anterior. El ticket de ML en feb–mar baja de $470 a $430 porque el recuerdo Lume ($65/pza) cuesta 4 veces la mediana de ML ($16.50/pza). TikTok Shop queda igual pero **sin evidencia de competidores** (ninguno de los 10 videos más vistos usa el carrito).
**Insumos:** `mercado/competencia.md`, `mercado/demanda-y-temporalidad.md`, `negocio/catalogo.md`, `mercadolibre/publicaciones-navidad-eventos.md`, `ventas/propuesta-corporativa-navidad.md`, `negocio/plan-90-dias.md`, `produccion/calculadora-capacidad.md`.
Leyenda: **V** = dato verificado (URL) · **E** = estimación (con justificación) · **verificar** = falta confirmar

> **Esto es venta bruta (con IVA, si aplica), no utilidad.** De cada venta salen comisión de ML (~15%, E: verificar con el simulador), comisión de TikTok (6–15% según la fuente: verificar), envío (~$90 por paquete en ML, E), materiales, empaque y mano de obra. **`costos/plantilla-costeo.csv` está vacía**, así que hoy **no se puede calcular el margen**. Una venta alta con margen negativo es pérdida.

---

## 1. Supuestos por canal (cada uno con fuente o justificación)

### Mercado Libre
| Supuesto | Valor (conservador / base / optimista) | Fuente o justificación |
|---|---|---|
| Fecha en que las publicaciones quedan activas | ~13-oct (si se publica esta semana) | Interno: cuenta lista; 8 publicaciones redactadas. Octubre cuenta ~19 días. |
| Visitas totales por mes (8 publicaciones) | Oct 250/400/600 · Nov 800/1,200/2,000 · Dic 1,200/1,600/3,000 · Ene 500/800/1,500 · Feb 400/600/1,200 · Mar 450/700/1,400 | E. Una cuenta nueva sin reputación aparece poco en búsquedas; el optimista supone Product Ads y Buen Fin. El escenario base equivale a ~6–7 visitas al día por publicación en diciembre. Se bajó en la v2: los artesanales verificados acumulan decenas de ventas, no cientos (`competencia.md` §5). **Medir la primera semana y ajustar.** |
| Conversión (pedidos / visitas) | Oct 1.2/1.5/2.0% · Nov 1.5/2.0/3.0% · Dic 1.8/2.5/3.5% · Ene–Mar 1.8/2.5/3.0% | V parcial: e-commerce México 1.31% en promedio ([Merca2.0/Tiendanube](https://www.merca20.com/?p=12586985)); Nubimetrics pone las publicaciones con buen desempeño en ML por arriba de 9% y muestra un caso de 7% ([Nubimetrics](https://academia.nubimetrics.com/tasa-de-conversion)). Sin reputación (ML exige 10 ventas para calcularla: [Tiendanube](https://www.tiendanube.com/mx/blog/como-funciona-mercado-libre)) partimos cerca del promedio y subimos poco a poco. |
| Ticket promedio | $430 todo el periodo | Interno: los 8 kits cuestan $319–$649; la mezcla navideña pesa más los de $399–$529. **V2:** no se asume que el recuerdo Lume de $649 suba el ticket en feb–mar, porque cuesta $65/pza contra una mediana verificada de $16.50/pza en ML (`competencia.md` §4). |
| Velas por pedido | 6 | Borregos = 12; rompecabezas = 4 piezas; set = 3; nacimiento = 3; kits de 2 = 2; Lume = 10. Promedio ponderado (E). |
| Contraste con la competencia (V) | Base nov+dic = 64 pedidos (8 por publicación) · Optimista = 165 | `competencia.md` §5 (verificado el 8-oct): borregos y navideños artesanales acumulan **+5 a +100 vendidos en toda la vida de la publicación** (BCGF +25 a $500; ANDREA +100 a $200; Picky, tienda Platinum, 1 vendido). Solo recuerdos con Full llegan a +500/+1000. El base equivale a un BCGF en su primera temporada; el optimista ya supera a cualquier artesanal verificado. |

### TikTok Shop
| Supuesto | Valor | Fuente o justificación |
|---|---|---|
| Arranque | Conservador: dic (aprobación tardía o rechazo) · Base: ~1-nov · Optimista: últimos días de oct | Verificación de 2–5 días hábiles según un blog de terceros, sin fuente oficial ([dolphin-anty](https://dolphin-anty.com/blog/es/como-vender-en-tiktok-shop-guia-completa-para-principiantes/)). Se agrega margen por ser cuenta nueva. **Verificar** en Seller Center. |
| Alcance (vistas de video y lives por mes) | Nov 10k/30k/80k · Dic 25k/60k/150k · Ene 12k/30k/60k · Feb–Mar 10k/25k/50k | E: cuenta nueva sin seguidores con ~4–5 videos por semana y 1–2 lives. Un solo video viral rompe el optimista (y la capacidad). |
| Clic al producto | 3% de las vistas | E. Sin benchmark oficial. |
| Conversión del clic | 1.5–2% / 2.5% / 3–3.5% | V parcial (terceros): video corto 2–4%, pestaña Tienda 1.5–3%, LIVE 5–12% ([dashboardly](https://www.dashboardly.io/statistics/tiktok-shop-live-shopping-statistics), [emplicit](https://emplicit.co/social-media-benchmarks-study-summary-2026/)). Se usa la parte baja por ser cuenta nueva. |
| Ticket / velas por pedido | $350 ($330 en ene) / 4 velas | E: en TikTok se venden más los kits de entrada ($319–$399). |
| Evidencia de competidores (V, 8-oct) | **Ninguna venta visible en TikTok Shop** | En la web de México no se ve la Tienda. 3 cuentas están marcadas como vendedoras, pero **ninguno de los 10 videos más vistos usa el carrito**: todos mandan a WhatsApp, web o IG (`competencia.md` §3 y §8). Esto es el supuesto más débil del modelo; el contenido de TikTok probablemente alimente más al canal Directo y a Eventos que al carrito. **Verificar en la app.** |

### Tienda propia, WhatsApp e Instagram (menudeo directo)
| Supuesto | Valor | Fuente o justificación |
|---|---|---|
| Conversaciones de compra al mes | Oct 20/30/40 · Nov 40/60/100 · Dic 60/100/160 · Ene 30/50/80 · Feb 30/50/80 · Mar 35/60/90 | E: no hay histórico. La tienda web aún no existe, así que casi todo entra por WhatsApp e IG. |
| Cierre | 20% / 25–30% / 30% | E. Tiendanube reporta que la venta por chat convierte "hasta 10 veces" más que la web (dato de proveedor, [Merca2.0](https://www.merca20.com/?p=12586985)). Es venta conversacional con interés previo. |
| Ticket / velas | $450 ($420 en ene) / 5 velas | E: precios del catálogo de menudeo. |

### Mayoreo de eventos (bautizo, baby shower, comunión, boda, XV)
| Supuesto | Valor | Fuente o justificación |
|---|---|---|
| Solicitudes de cotización al mes | Oct 5/8/12 · Nov 8/12/18 · Dic 6/10/15 · Ene 10/15/22 · Feb 12/20/30 · Mar 15/25/35 | E. Demanda continua: 1.68 millones de nacimientos y 491,640 bodas al año ([INEGI ENR](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/enr/ENR2025_RR.pdf), [INEGI EMAT](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/emat/EMAT2025_RR.pdf)). Sube en feb–mar por las comuniones de abril a junio. |
| Cierre | 20% / 30% / 35% | E: cotización pedida por el cliente (contacto caliente). |
| Ticket / velas | $1,500 / 30 velas (optimista: $1,800 / 35) | Interno: mayoreo de 11–50 pzs a ~$50 por pieza; la competencia vende 20–30 pzs a $30–$70 por pieza (`competencia.md`). |

### Regalo corporativo
| Supuesto | Valor | Fuente o justificación |
|---|---|---|
| Contactos o propuestas enviadas | Oct 60 · Nov 60 (hasta el 20) · Dic 20 · Ene 20 · Feb 40 · Mar 40 | Plan interno: 20 por semana entre oct y nov; baja después por el cambio a eventos. |
| Cierre (pedidos / contactos en frío) | 2% / 4% / 8% | V parcial (benchmarks de proveedores B2B): respuesta en frío 3–6% ([The Digital Bloom](https://thedigitalbloom.com/learn/cold-outbound-reply-rate-benchmarks/), [Apollo](https://www.apollo.io/insights/what-is-a-good-benchmark-for-reply-rates-in-cold-outreach)); de reunión a cierre 3–8%; cierre de oportunidad calificada ~20% ([Martal](https://www.martal.ca/sales-statistics-lb/)). Una muestra física y contactos cálidos (conocidos, empresas locales) suben el cierre. Por eso el base de 4% es más alto que el email en frío puro. |
| Ticket / velas | $3,000 (60 pzs) / $4,000 (80 pzs) / $5,500 (110 pzs) | Interno: 100 borregos = $4,500; 100 venados = $6,200 (`ventas/propuesta-corporativa-navidad.md`). |
| Momento de la venta | Se registra en el mes de **cierre**; la producción y entrega de los cierres de noviembre ocurre entre nov y el 20-dic | Anticipo del 50% al cerrar y resto al entregar (interno). |

---

## 2. Proyección por canal: escenario BASE

| Canal | Oct (parcial) | Nov | Dic | Ene | Feb | Mar | Total 6 meses |
|---|---|---|---|---|---|---|---|
| **ML**: visitas → conv. → pedidos × ticket | 400 → 1.5% → 6 × $430 = **$2,580** | 1,200 → 2.0% → 24 = **$10,320** | 1,600 → 2.5% → 40 = **$17,200** | 800 → 2.5% → 20 = **$8,600** | 600 → 2.5% → 15 = **$6,450** | 700 → 2.5% → 17 = **$7,310** | **$52,460** |
| **TikTok**: vistas → clics (3%) → conv. → pedidos | 0 | 30k → 900 → 2.5% → 22 × $350 = **$7,700** | 60k → 1,800 → 45 = **$15,750** | 30k → 900 → 22 × $330 = **$7,260** | 25k → 750 → 18 = **$6,300** | 25k → 750 → 18 = **$6,300** | **$43,310** |
| **Directo** (WhatsApp/IG/web): conversaciones → cierre → pedidos | 30 → 25% → 7 × $450 = **$3,150** | 60 → 25% → 15 = **$6,750** | 100 → 30% → 30 = **$13,500** | 50 → 25% → 12 × $420 = **$5,040** | 50 → 12 = **$5,400** | 60 → 15 = **$6,750** | **$40,590** |
| **Eventos**: cotizaciones → 30% → pedidos × $1,500 | 8 → 2 = **$3,000** | 12 → 3 = **$4,500** | 10 → 3 = **$4,500** | 15 → 4 = **$6,000** | 20 → 6 = **$9,000** | 25 → 7 = **$10,500** | **$37,500** |
| **Corporativo**: pedidos × $4,000 | 1 = **$4,000** | 4 = **$16,000** | 1 = **$4,000** | 1 = **$4,000** | 1 = **$4,000** | 1 = **$4,000** | **$36,000** |
| **TOTAL BASE** | **$12,730** | **$45,270** | **$54,950** | **$30,900** | **$31,150** | **$34,860** | **$209,860** |
| Pedidos totales | 16 | 68 | 119 | 59 | 52 | 58 | 372 |

## 3. Total por escenario

| Escenario | Oct | Nov | Dic | Ene | Feb | Mar | Total 6 meses |
|---|---|---|---|---|---|---|---|
| **Conservador** | $4,590 | $17,660 | $21,180 | $11,040 | $10,110 | $15,490 | **$80,070** |
| **Base** | $12,730 | $45,270 | $54,950 | $30,900 | $31,150 | $34,860 | **$209,860** |
| **Optimista** | $29,810 | $113,800 | $141,700 | $70,850 | $71,030 | $84,060 | **$511,250** |
| *Plan actual (`plan-90-dias.md`)* | *$30,000* | *$115,000* | *$200,000* | *$160,000* | — | — | — |

<details><summary>Detalle por canal: conservador y optimista</summary>

| Canal | Cons. Oct | Nov | Dic | Ene | Feb | Mar | Opt. Oct | Nov | Dic | Ene | Feb | Mar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ML | 1,290 (3 ped.) | 5,160 (12) | 9,030 (21) | 3,870 (9) | 3,010 (7) | 3,440 (8) | 5,160 (12) | 25,800 (60) | 45,150 (105) | 19,350 (45) | 15,480 (36) | 18,060 (42) |
| TikTok | 0 | 1,400 (4) | 5,250 (15) | 1,650 (5) | 1,400 (4) | 1,400 (4) | 1,050 (3) | 25,200 (72) | 54,950 (157) | 17,820 (54) | 15,750 (45) | 15,750 (45) |
| Directo | 1,800 (4) | 3,600 (8) | 5,400 (12) | 2,520 (6) | 2,700 (6) | 3,150 (7) | 5,400 (12) | 13,500 (30) | 21,600 (48) | 10,080 (24) | 10,800 (24) | 12,150 (27) |
| Eventos | 1,500 (1) | 1,500 (1) | 1,500 (1) | 3,000 (2) | 3,000 (2) | 4,500 (3) | 7,200 (4) | 10,800 (6) | 9,000 (5) | 12,600 (7) | 18,000 (10) | 21,600 (12) |
| Corporativo | 0 | 6,000 (2) | 0 | 0 | 0 | 3,000 (1) | 11,000 (2) | 38,500 (7) | 11,000 (2) | 11,000 (2) | 11,000 (2) | 16,500 (3) |
| **Total** | **4,590** | **17,660** | **21,180** | **11,040** | **10,110** | **15,490** | **29,810** | **113,800** | **141,700** | **70,850** | **71,030** | **84,060** |

</details>

---

## 4. Contra las metas: ¿se alcanzan?

| Mes | Meta mínima $50k | Meta $200k | Conservador | Base | Optimista |
|---|---|---|---|---|---|
| Oct (parcial) | No en ningún escenario | No | 9% de $50k | 25% | 60% |
| Nov | **Base: no por poco** ($45.3k; faltan ~$5k: 1 corporativo y un poco más) · Optimista: sí | No | 35% | 91% | 228% de $50k · 57% de $200k |
| Dic | **Base: sí** ($55k) · Optimista: sí | **No** (optimista: $142k = 71%) | 42% | 110% | 71% de $200k |
| Ene | Solo optimista | No | 22% | 62% | 142% |
| Feb | Solo optimista | No | 20% | 62% | 142% |
| Mar | Solo optimista | No | 31% | 70% | 168% |

**Conclusión clara:**
- **$50k/mes:** en el **escenario base se alcanza solo en diciembre de 2026** ($55k; noviembre se queda en $45k). **De enero a marzo no se sostiene** (~$31–35k) mientras no se fortalezcan eventos y comuniones. Es alcanzable de forma sostenida solo en el optimista.
- **$200k/mes: no es alcanzable entre oct-2026 y mar-2027** con los canales y la capacidad actuales, **ni en el escenario optimista** (pico de $142k en diciembre). Para $200k harían falta ~2,700–2,900 velas al mes (ver sección 5), más de lo que da incluso el ejemplo hipotético con ayudante (~2,600). El plan de 90 días (nov $115k, dic $200k, ene $160k) **está por encima del optimista en diciembre y enero**. Se recomienda que el chat de Dirección lo ajuste.
- El escenario base queda en **~39% del plan en noviembre y ~27% en diciembre**.

---

## 5. Velas necesarias vs. capacidad

| Velas al mes | Oct | Nov | Dic | Ene | Feb | Mar |
|---|---|---|---|---|---|---|
| Conservador | 68 | 278 | 276 | 164 | 148 | 249 |
| **Base** | **211** | **717** | **740** | **468** | **482** | **539** |
| Optimista | 504 | 1,778 | 1,893 | 1,071 | 1,086 | 1,317 |
| Para la meta de $200k (a ~$74 por vela) | — | — | ~2,700 | — | — | — |

Detalle base de noviembre: ML 144 + TikTok 88 + directo 75 + eventos 90 + corporativo 320. Los corporativos de noviembre se fabrican entre nov y el 20-dic. Si se reparte la mitad a diciembre, quedan nov ~560 y dic ~900.

> **SUPUESTO CRÍTICO PENDIENTE: la capacidad real es DESCONOCIDA.** `produccion/cuestionario-capacidad.md` no está contestado y los moldes no se han contado. La única referencia es un **ejemplo HIPOTÉTICO** de `produccion/calculadora-capacidad.md`:
> - Noemi sola, 6 h/día, 24 días: **~1,368 velas buenas al mes** (hipotético)
> - Con ayudante ~5 h/día y más moldes: **~2,600 al mes** (hipotético)
>
> **Lectura con el hipotético:** el escenario base (máximo ~740–900 al mes) **cabe** en la capacidad de Noemi sola. El optimista **la rebasa en noviembre y diciembre** (~1,800–1,900), así que necesitaría ayudante desde inicios de noviembre. La meta de $200k (~2,700) **rebasa incluso el hipotético con ayudante**. Además, las velas pintadas a mano (borregos, rompecabezas) toman más tiempo por pieza que una figura lisa. Si la capacidad real resulta menor que la hipotética, el techo de ventas baja en la misma proporción.

---

## 6. Las 5 palancas que más mueven la proyección (sensibilidad sobre el escenario base)

| # | Palanca | Cambio | Impacto en ventas | Impacto en velas |
|---|---|---|---|---|
| 1 | **Cierre y tamaño de los pedidos corporativos** | Cada corporativo extra: +$4,000. Subir el cierre de 4% a 8% en los 120 contactos de oct–nov: +5 pedidos | **+$20,000** (nov–dic). Subir el ticket a $6,000 (120 pzs) en los 5 pedidos base: +$10,000 | +400 velas / +200 |
| 2 | **Tráfico en ML** (Product Ads, Buen Fin, más publicaciones) | +1,000 visitas al mes en nov y dic | **+$19,350** (+45 pedidos) | +270 |
| 3 | **Alcance y fecha de arranque de TikTok Shop** | Duplicar el alcance en nov–dic (30k→60k y 60k→120k) | **+$23,450** (+67 pedidos). Cada semana de retraso en noviembre: −$1,900 | +268 |
| 4 | **Conversión en ML** (fotos, reputación, precio) | +1 punto porcentual en nov–dic (2,800 visitas) | **+$12,040** (+28 pedidos) | +168 |
| 5 | **Ticket promedio** (bundles y mayor peso de borregos y rompecabezas; **no** subir precios por pieza, que ya están arriba del mercado) | +$70 por pedido en ML y TikTok en nov–dic (131 pedidos) | **+$9,170** sin producir más pedidos | ~0 (más piezas por kit, si aplica) |

Extra (ene–mar): **+10 cotizaciones de evento al mes** × 30% × $1,500 = **+$4,500 al mes**. Es la palanca que define si de enero a marzo se pasa de $50k.

**Cómo llegar a $50k sostenido de enero a marzo (E):** base ~$32k + 3 corporativos extra (8M y Día de las Madres) $12k + 10 cotizaciones extra de eventos $4.5k ≈ $48.5k. Todavía hay que sumar algo de TikTok o ML. Es factible con **trabajo comercial**, no con más capacidad.

---

## 7. Las 3 recomendaciones prioritarias

1. **Publicar los 8 kits en ML esta semana (antes del 15-oct) y conseguir las primeras 10 ventas antes del Buen Fin.** Esas 10 ventas activan la reputación ([Tiendanube](https://www.tiendanube.com/mx/blog/como-funciona-mercado-libre)). Para lograrlas: precio de arranque en los kits de entrada y mandar a ML a los clientes reales que hoy piden por WhatsApp (compras genuinas; nada de ventas simuladas, que ML sanciona: verificar políticas). Registrar Ananda en El Buen Fin antes del **12-nov** (es gratis y pide RFC: [adn40](https://www.adn40.mx/mexico/2026-09-01/buen-fin-2026-fechas-duracion-y-como-participar-en-el-sorteo/)). **No subir precios**: el levantamiento verificado muestra que nuestras navideñas ya cuestan el doble por pieza que la mediana de ML; hay que justificarlo con medidas, pintado a mano y video (`competencia.md` §4 y §6). Validar todo precio con el simulador de ML y la fórmula de `costos/README.md`.
2. **Hacer del corporativo la prioridad número 1 hasta el 20-nov**, porque es la palanca con más pesos por hora. 20 propuestas por semana, empezando por contactos cálidos (empresas de conocidos, proveedores, negocios locales), con **muestra física** a los 10 mejores prospectos. Registrar todo en `ventas/pipeline.md`. Meta base: 5 pedidos de ~$4,000. Cada punto de cierre arriba de 4% vale ~$5,000.
3. **Antes del 20-oct, contestar el cuestionario de capacidad y capturar los costos** de los 8 kits. Sin esto no se sabe si diciembre cabe ni si cada kit deja ganancia. Con el dato real, fijar un **tope de pedidos por semana** en ML y TikTok, y decidir si se contrata ayudante (solo vale la pena si el pipeline corporativo pasa de ~5 pedidos o si ML y TikTok rebasan el base en la semana del Buen Fin).

---

## 8. Decisiones que Noemi debe tomar (esta semana)

1. **¿Se ajusta la meta del plan?** La proyección dice que $200k/mes no se alcanza antes de abril de 2027. Propuesta: meta operativa = escenario base (nov ~$45k, dic ~$55k) con "meta estirada" = optimista.
2. **Presupuesto de Product Ads en ML** para nov–dic (monto por definir con el chat de Finanzas; el optimista lo supone).
3. **Ayudante sí o no, y desde cuándo.** Depende de la capacidad real y del pipeline corporativo al 31-oct.
4. **Tope de producción**: cuántas velas por semana se pueden prometer sin fallar entregas. Fallar en ML destruye la reputación (reclamos de máximo ~1.5% y envíos tarde de máximo ~10%, según [Nubimetrics](https://academia.nubimetrics.com/reputacion-baja-mercado-libre); verificar).
5. **¿Se crean ya moldes y línea de comunión** (cáliz, cruz, paloma) para cotizar en febrero? Sin ellos, enero a marzo queda debajo de $50k.
6. **RFC y régimen fiscal** para TikTok Shop y Buen Fin (persona física; a revisar con el chat de Finanzas).

> Toda vela que se venda debe llevar la advertencia: no dejar encendida sin supervisión; poner sobre superficie resistente al calor, lejos de niños, mascotas y material inflamable; no exponer la parafina al sol.
