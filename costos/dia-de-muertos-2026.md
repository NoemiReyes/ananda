# Costos y precios: Día de Muertos 2026 (DM-1 a DM-6)

Responsable: Producción y costos · `costos-precios`. **Versión 2: sáb 17-oct-2026, tarde** (tarea DM-c de `direccion/dia-de-muertos-2026.md`). La versión 1 (mañana del 17-oct) queda reemplazada.
Fórmula y reglas: `costos/README.md` (margen bruto ≥ 45% en menudeo; ticket mínimo ML $299). Cálculo reproducible: script en el anexo al final de este archivo.

> **Qué cambió en la v2 (datos reales de Noemi, 17-oct).** Aroma: máximo 6 g por vela de cempasúchil, a $50 por 30 ml. Colorante: un cuarto de sobre de $5. Productividad del cempasúchil: **3 velas por hora por persona** (vaciar, desmoldar y empacar). Con esto **el cempasúchil sube de ~$37 a $55.30 de costo y a $75 ya no llega a 45%** (queda en 26%). **Noemi decidió mantener $75 la pieza y 3 por $200** (precio fijo; ver margen real en la sección 1). Las veladoras bajan de precio a petición de Noemi ($199 se le hace caro) y los sets se recalculan.

---

## 0. Supuestos generales

| Concepto | Valor usado | Estatus |
|---|---|---|
| Mano de obra | $80/hora ($1.33/min), igual que `costos/calculo_costos.py` | Supuesto de la empresa |
| Merma | 5% sobre (materiales + mano de obra) | Regla README |
| Soya alto punto de fusión | $150/kg = $0.150/g | **REAL** (Noemi, 17-oct) |
| Parafina china | $80/kg = $0.080/g | **REAL** (Noemi, 17-oct). También se usa para la veladora en vaso |
| Aroma | $50 por 30 ml → **$1.667/ml ≈ $1.667/g** | Precio **REAL** (Noemi, 17-oct). Densidad 1 g/ml: **verificar** (pesar 10 ml en la báscula; los aceites de fragancia pesan ~0.9–1.05 g/ml) |
| Dosis de aroma, cempasúchil | **6 g por vela** (máximo) = 5.7% de 106 g de cera | **REAL** (Noemi, 17-oct). Reemplaza los escenarios (a)/(b) de la v1 |
| Dosis de aroma, veladora | 7.4 g por vaso (misma proporción 5.7% sobre 130 g) | **estimado**: confirmar si la veladora lleva el mismo aroma y la misma dosis (pregunta 2) |
| Pabilo | 3 m = $25 → $0.083/cm | **REAL** |
| Colorante, cempasúchil | **$1.25 por vela** (máximo: "ni una cuarta parte" de un sobre de $5) | **REAL como tope**. Si el cuarto de sobre rinde para una tanda de varias velas, el costo por vela baja (pregunta 1) |
| Bolsa de celofán / listón de cierre | $0.90 / $0.50 | **estimado** (`insumos-referencia.md`); medida de bolsa del cempasúchil: **verificar** |
| Opalina blanca 225 g, carta | $2.00/hoja | **estimado** con referencia: 100 hojas Copamex $151–155 en Cyberpuerta, $168–245 en ML (búsqueda del 17-oct, **verificar**) + envío |
| Papel adhesivo mate (o glossy), carta | $5.00/hoja | **estimado** (A4 glossy en Walmart salía a ~$15.70/hoja: **verificar** lo que pagó Noemi) |
| Laminado transparente en frío, carta | $4.00/hoja | **estimado** (ya comprado: falta el precio real) |
| Tinta Epson L3560 | $2.50/hoja cobertura alta · $1.00/hoja cobertura baja (tag) | **estimado** |
| Reimpresiones | +10% de hojas | **estimado** |
| Desgaste de cuchilla y tapete Cricut | $0.50 por hoja de papel picado | **estimado** |
| Vaso de veladora (~6 cm, apto para calor) | $12.00 | **estimado** (**verificar** precio real) |
| Cera del vaso | 130 g de parafina | **estimado**: medir con el método del agua (`produccion/formulas/punto-de-partida-soya.md`, sección 3) |
| Mecha de veladora + porta-pabilo | $1.50 | **estimado** |
| Sticker de advertencias en la base | $0.40 | **estimado** (regla 6 de CLAUDE.md: toda vela lleva aviso) |
| Caja kraft + viruta (Set Ofrenda) | $10.00 | **estimado** |
| Empaque de envío por paquetería (caja + burbuja + relleno + cinta) | $15 una pieza · $25 un set | **estimado** |
| Pago | Transferencia o efectivo: 0%. Link de pago o terminal: ~4.2% (3.6% + IVA, **verificar** con tu proveedor) | Se muestra el margen en ambos casos |
| Impuestos | Márgenes **antes** de ISR/IVA. Si Noemi factura con IVA trasladado, el margen baja ~13.8 puntos | Revisar con `finanzas-fiscal` |

### Tiempos de mano de obra

| Paso | Minutos | Estatus |
|---|---|---|
| **Vela de cempasúchil (vaciar, desmoldar y empacar)** | **20 (3 por hora por persona)** · escenario 10 (6 por hora, colada en varios moldes a la vez) | **REAL** (Noemi, 17-oct) · el de 6/h es escenario |
| Atención + prueba digital (1 ronda de cambios) | 5 por pedido | estimado |
| Diseño con **foto** (recortar, ajustar, nombre) | 10 | estimado |
| Diseño con **nombre** en plantilla | 3 | estimado |
| Imprimir, laminar, cortar y pegar etiqueta en el vaso | 5 | estimado |
| Hacer la veladora (vaciar, mecha, enfriar, recortar) | 4 | estimado |
| Embolsar veladora + tag + listón | 2 | estimado |
| **Total veladora** | **DM-1 con foto 26 min · DM-2 papel picado 19 min** · meta con plantillas de Canva y lotes: **12–15 min** | estimado: cronometrar los primeros 5 pedidos |
| Papel picado del set (mismo nombre, adaptar + cortar + desbarbar) | 9 | estimado |

En el cempasúchil, los 20 min incluyen el empacado; en el Set Ofrenda la vela va sin bolsa, pero se dejan los mismos 20 min (acomodar en la caja), para no quedarse cortos.

---

## 1. DM-4 Vela de Cempasúchil (datos reales del 17-oct)

**Receta:** 106 g de cera por vela = 53 g de soya alto punto de fusión + 53 g de parafina china. Pabilo 9 cm. Aroma 6 g. Colorante ¼ de sobre.

### Costeo unitario

| Concepto | Estatus | Sin bolsa · 3/h | Con bolsa + tag · 3/h | Sin bolsa · 6/h | Con bolsa + tag · 6/h |
|---|---|---|---|---|---|
| Soya 53 g × $0.150 | REAL | $7.95 | $7.95 | $7.95 | $7.95 |
| Parafina china 53 g × $0.080 | REAL | $4.24 | $4.24 | $4.24 | $4.24 |
| Aroma 6 g × $1.667 | REAL (densidad: verificar) | $10.00 | $10.00 | $10.00 | $10.00 |
| Pabilo 9 cm | REAL | $0.75 | $0.75 | $0.75 | $0.75 |
| Colorante (¼ de sobre de $5) | REAL, tope | $1.25 | $1.25 | $1.25 | $1.25 |
| **Subtotal insumos reales** | | **$24.19** | **$24.19** | **$24.19** | **$24.19** |
| Sticker de advertencias en la base | estimado | $0.40 | — | $0.40 | — |
| Bolsa de celofán + listón + tag en opalina | estimado | — | $1.81 | — | $1.81 |
| **Mano de obra** (20 min a 3/h · 10 min a 6/h) | REAL (3/h) · escenario (6/h) | **$26.67** | **$26.67** | $13.33 | $13.33 |
| Merma 5% | | $2.56 | $2.63 | $1.90 | $1.97 |
| **Costo unitario** | | **$53.82** | **$55.30** | **$39.82** | **$41.30** |
| Peso de la mano de obra en el costo | | 52% | 51% | 35% | 34% |
| Precio mínimo para 45% (venta directa, transferencia) | | $98 | **$101** | $73 | **$76** |

**Lectura:**
- **La mano de obra domina el costo: $26.67 de $55.30 (51%).** Todos los insumos juntos suman $24.19; el aroma real ($10.00) es el insumo más caro, más que la soya.
- **A $75 la vela ya no llega a 45%:** con 3 por hora deja **26.3%** (22% con link de pago). Costos lo marcó como rechazado por la regla de 45% y propuso $105; **Noemi decidió quedarse en $75** (siguiente tabla).
- **Colada en varios moldes a la vez (6 por hora)** baja el costo $14 por vela ($55.30 → $41.30). Es la palanca más grande de todo el catálogo de Día de Muertos: vale más que cualquier ahorro en insumos. Cada molde extra se paga solo con unas 20 velas (ahorro de $14 por vela; precio del molde: **verificar**).
- Con 6 por hora, $75 queda en 44.9%: tampoco pasa. El precio mínimo es $76.

### Precio del cempasúchil: **decisión de Noemi (17-oct): $75 la pieza y 3 por $200** (reemplaza "2 por $139")

Precio fijo: no se cambia en este documento. Aquí solo se muestra su margen real. 3 por $200 = $66.67 por vela.

| Precio | Productividad | Empaque | Costo | Margen transferencia | Con link de pago | Si absorbes empaque de envío ($15) | ¿Llega a 45%? |
|---|---|---|---|---|---|---|---|
| $75 (1 pieza) | 3 por hora | sin bolsa | $53.82 | **28.2%** | 24.1% | 8.2% | **NO ⚠️** |
| $75 (1 pieza) | 3 por hora | con bolsa + tag | $55.30 | **26.3%** | 22.1% | 6.3% | **NO ⚠️** |
| $75 (1 pieza) | 6 por hora | sin bolsa | $39.82 | 46.9% | 42.7% ⚠️ | 26.9% ⚠️ | Sí (solo con transferencia) |
| $75 (1 pieza) | 6 por hora | con bolsa + tag | $41.30 | **44.9%** | 40.8% | 24.9% | **NO ⚠️** (por 0.1 puntos) |
| 3 por $200 | 3 por hora | sin bolsa | $161.46 | **19.3%** | 15.1% | 11.8% | **NO ⚠️** |
| 3 por $200 | 3 por hora | con bolsa + tag | $165.90 | **17.1%** | 12.9% | 9.6% | **NO ⚠️** |
| 3 por $200 | 6 por hora | sin bolsa | $119.46 | **40.3%** | 36.1% | 32.8% | **NO ⚠️** |
| 3 por $200 | 6 por hora | con bolsa + tag | $123.90 | **38.1%** | 33.9% | 30.6% | **NO ⚠️** |

**Lectura de costos (para Dirección):**
- **Con la productividad real de hoy (3 por hora), el cempasúchil a $75 deja 26% y el 3 por $200 deja 17%.** Ninguno pasa la regla de 45% del README. No hay pérdida (margen positivo), pero cada vela paga la hora de Noemi y casi nada más.
- **Con colada en varios moldes (6 por hora), $75 queda en el límite (44.9% en bolsa, 46.9% sin bolsa)**; el 3 por $200 sigue abajo (38%).
- Para que estos precios funcionen, **pasar a 6 por hora es obligatorio**, no opcional. Precios que sí llegarían a 45% como referencia: 1 pieza $101 (3/h) o $76 (6/h); 3 piezas $302 (3/h) o $226 (6/h).
- Por la regla del README, vender abajo de 45% requiere **aprobación escrita de Dirección**: dejar registrada la decisión de Noemi en `direccion/`.
- No cobrar con link de pago ni absorber envío en el cempasúchil: baja a 6–24%.

---

## 2. Veladoras DM-1 (con foto) y DM-2 (papel picado con nombre)

### Costeo (aroma recalculado a $1.667/g, dosis 5.7% como el cempasúchil: **estimado**)

| Concepto | DM-1 foto | DM-2 papel picado | Estatus |
|---|---|---|---|
| Parafina 130 g × $0.080 | $10.40 | $10.40 | precio REAL, gramos estimado |
| Aroma 7.4 g × $1.667 | $12.26 | $12.26 | precio REAL, dosis estimado |
| Mecha + porta-pabilo | $1.50 | $1.50 | estimado |
| Vaso apto para calor | $12.00 | $12.00 | estimado |
| Etiqueta envolvente (½ hoja adhesivo + tinta + laminado, +10%) | $6.33 | $6.33 | estimado |
| Sticker de advertencias en la base | $0.40 | $0.40 | estimado |
| Bolsa de celofán + listón | $1.70 | $1.70 | estimado |
| **Subtotal materiales** | **$44.59** | **$44.59** | |
| Mano de obra | $34.67 (26 min) | $25.33 (19 min) | estimado |
| Merma 5% | $3.96 | $3.50 | |
| **Costo unitario** | **$83.22** | **$73.42** | v1: $81.26 / $71.46 (sube ~$2 por el aroma real) |
| Peso de la mano de obra | 44% | 36% | |
| Precio mínimo 45% | **$152** | **$134** | |

Si la veladora lleva 8% de aroma (10.4 g) en vez de 5.7%, el costo sube $5.10 más (DM-1 $88.54, mínimo $161).

### Cuánto baja con plantillas de Canva y trabajo por lotes

Plantilla fija (foto o nombre se cambian en 1–2 min), imprimir varias etiquetas por hoja y colar varias veladoras a la vez:

| Minutos por veladora | Mano de obra | Costo | Ahorro vs DM-1 (26 min) | Ahorro vs DM-2 (19 min) | Precio mínimo 45% |
|---|---|---|---|---|---|
| 26 (DM-1 hoy) | $34.67 | $83.22 | — | — | $152 |
| 19 (DM-2 hoy) | $25.33 | $73.42 | — | — | $134 |
| **15** | $20.00 | $67.82 | −$15.40 | −$5.60 | $124 |
| **12** | $16.00 | $63.62 | −$19.60 | −$9.80 | $116 |

### Opciones de precio

| Opción | Costo | Precio | Margen transferencia | Con link | Si absorbes empaque ($15) | Decisión |
|---|---|---|---|---|---|---|
| DM-1 $199 (v1) | $83.22 | $199 | 58.2% | 54.0% | 50.7% | A Noemi se le hace caro |
| **DM-1 $169** | $83.22 | **$169** | **50.8%** | 46.6% | 41.9% | **Recomendado** |
| DM-1 $159 | $83.22 | $159 | 47.7% | 43.5% ⚠️ | 38.2% | Pasa justo con 26 min; deja sin espacio el descuento del Set Ofrenda (ver sección 4). Viable cuando se cronometren ≤15 min (57.3%) |
| **DM-2 $149** | $73.42 | **$149** | **50.7%** | 46.5% | 40.7% | **Recomendado** |

**Recomendación: DM-1 con foto (y mascota) a $169 y DM-2 papel picado a $149.** Las dos dejan ~51% con los tiempos estimados de hoy, siguen arriba de 45% con link de pago y dejan espacio para que los sets ahorren $15. Si después de los primeros 5 pedidos la veladora con foto sale en 15 min o menos, DM-1 puede bajar a $159.

---

## 3. DM-3 Papel picado (sin cambios desde la v1)

Opalina 225 g.

Caben **2 chicos (14 × 10 cm)** o **1 mediano (19 × 14 cm)** por hoja en el área de Imprimir y cortar (17.1 × 23.5 cm).

| Concepto | Chico suelto | Mediano suelto | Mediano agregado a una veladora (mismo nombre) |
|---|---|---|---|
| Opalina + tinta alta, +10% reimpresión | $2.48 | $4.95 | $4.95 |
| Cuchilla y tapete | $0.25 | $0.50 | $0.50 |
| Sobre de celofán plano | $0.90 | $0.90 | $0.90 |
| Mano de obra | $17.33 (13 min) | $20.00 (15 min) | $10.67 (8 min: el diseño ya está hecho) |
| Merma 5% | $1.05 | $1.32 | $0.85 |
| **Costo unitario** | **$22.01** | **$27.67** | **$17.87** |
| Precio mínimo 45% | $40 | $50 | $32 |

El material cuesta menos de $6: **lo caro es el tiempo** (atender, diseñar y desbarbar). Con nuestro costo no podemos igualar a Pixé Design ($10 chico, $22 mediano) sin perder dinero.


---

## 4. Sets DM-5 y DM-6 (recalculados)

Regla: el set debe salir **$15–$24 más barato** que comprar las piezas por separado **y** dejar ≥ 45%.

### Costeo

| Concepto | DM-5 nombre | DM-5 foto | DM-6 nombre · 3/h | DM-6 foto · 3/h | DM-6 nombre · 6/h | DM-6 foto · 6/h |
|---|---|---|---|---|---|---|
| Veladora (materiales) | $44.59 | $44.59 | $42.89 (sin bolsa, va en caja) | $42.89 | $42.89 | $42.89 |
| Mano de obra veladora | $25.33 | $34.67 | $25.33 | $34.67 | $25.33 | $34.67 |
| Papel picado mediano, mismo nombre (materiales) | $5.45 | $5.45 | $5.45 | $5.45 | $5.45 | $5.45 |
| Mano de obra papel picado (9 min) | $12.00 | $12.00 | $12.00 | $12.00 | $12.00 | $12.00 |
| 2 velas de cempasúchil sin bolsa (con su mano de obra) | — | — | $101.72 | $101.72 | $75.05 | $75.05 |
| Caja kraft + viruta + tag del set | — | — | $10.41 | $10.41 | $10.41 | $10.41 |
| Merma 5% | $4.37 | $4.84 | $9.89 | $10.36 | $8.56 | $9.02 |
| **Costo del set** | **$91.74** | **$101.54** | **$207.69** | **$217.49** | **$179.69** | **$189.49** |
| Precio mínimo 45% | $167 | $185 | $378 | $395 | $327 | $345 |

### Precio

Cempasúchil al precio fijo de Noemi: **$75 la pieza** (2 piezas por separado = $150).

| Set | Por separado | Precio del set | Ahorro | Margen 3/h | Margen 6/h | Con link (6/h) | Si absorbes empaque (6/h) | Pasa 45% |
|---|---|---|---|---|---|---|---|---|
| **DM-5 Set Recuerdo con nombre** (DM-2 + papel picado agregado) | $149 + $35 = $184 | **$169** | $15 | 45.7% (no lleva cempasúchil) | 45.7% | 41.5% ⚠️ | 36.8% ⚠️ | **Sí** con transferencia |
| **DM-5 Set Recuerdo con foto** (DM-1 + papel picado agregado) | $169 + $35 = $204 | **$189** | $15 | 46.3% (no lleva cempasúchil) | 46.3% | 42.1% ⚠️ | 38.3% ⚠️ | **Sí** con transferencia |
| DM-6 Set Ofrenda con foto, ahorro $15 | $169 + $150 + $35 = $354 | $339 | $15 | **35.8% ⚠️** | **44.1% ⚠️** | 39.9% ⚠️ | 36.7% ⚠️ | **NO** |
| **DM-6 Set Ofrenda con foto, ahorro $5** | $354 | **$349** | $5 | **37.7% ⚠️** | 45.7% | 41.5% ⚠️ | 38.5% ⚠️ | Solo a 6/h |
| DM-6 Set Ofrenda con nombre, ahorro $15 | $149 + $150 + $35 = $334 | $319 | $15 | **34.9% ⚠️** | **43.7% ⚠️** | 39.5% ⚠️ | 35.8% ⚠️ | **NO** |
| **DM-6 Set Ofrenda con nombre, ahorro $5** | $334 | **$329** | $5 | **36.9% ⚠️** | 45.4% | 41.1% ⚠️ | 38.0% ⚠️ | Solo a 6/h |

**Conflicto en el Set Ofrenda:** con el cempasúchil a $75, **no existe un precio que cumpla las dos reglas** (ahorro de $15–$24 y ≥45%). Para llegar a 45% con 3 velas por hora el set tendría que costar $395 (foto) o $378 (nombre), más caro que comprar las piezas sueltas ($354 / $334): nadie lo compraría.

**Propuesta de costos:** Set Ofrenda **$349 con foto / $329 con nombre** (ahorro de $5; el valor del set está en la caja de regalo armada, no en el descuento). Pasa 45% **solo si el cempasúchil se hace a 6 por hora**; a 3 por hora deja 37–38% y necesita la aprobación de Dirección. Alternativa si se quiere conservar el ahorro de $15 ($339 / $319): pasa solo si además la veladora con foto baja a 15 min (DM-6 foto a $339 con 6/h y 15 min = 48.6%); la de nombre a $319 no pasa en ningún escenario calculado (43.7%).

Los sets se cobran **solo por transferencia o efectivo** (con link de pago bajan a 41–43%).

---

## 5. Mercado Libre: DM-6 Set Ofrenda, **sigue sin publicarse**

Supuestos (todos **verificar en el simulador de costos de la publicación**): ML Clásica 15% + IVA = 17.4% efectivo; Premium 19.5% + IVA = 22.6%; sin cargo fijo desde $299; envío gratis absorbido por el vendedor ≈ $80; empaque de envío $25.

| Escenario | Precio $299 | Precio $349 | Precio $499 | Precio mínimo para 45% |
|---|---|---|---|---|
| DM-6 con foto (3/h, costo $217.49), ML Clásica | −25.3% ⚠️ | −9.8% ⚠️ | 18.0% ⚠️ | **$858** |
| DM-6 con foto (3/h), ML Premium | −30.5% ⚠️ | −15.0% ⚠️ | 12.8% ⚠️ | **$995** |
| Kit genérico sin personalizar (costo $186.69), ML Clásica | −15.0% ⚠️ | −1.0% ⚠️ | 24.1% ⚠️ | **$776** |

**Decisión de costos: RECHAZADO para ML** (con los costos nuevos está peor que en la v1). Vender el Set Ofrenda **solo por WhatsApp/IG/FB**. Publicarlo con margen menor a 45% solo con aprobación escrita de Dirección (regla README).

---

## 6. Precios para los estados de WhatsApp (listos para copiar)

Margen con pago por transferencia/efectivo y envío por paquetería cobrado aparte. Cempasúchil al precio fijo decidido por Noemi.

| Producto | Texto para el estado | Costo | Margen 3/h | Margen 6/h | ¿≥45%? |
|---|---|---|---|---|---|
| Veladora con foto (DM-1) y versión mascota | **$169** | $83.22 | 50.8% | 50.8% | Sí |
| Veladora papel picado con nombre (DM-2) | **$149** | $73.42 | 50.7% | 50.7% | Sí |
| "Desde [precio]" (estado del sáb 17, 14:00) | **Desde $149** | — | — | — | — |
| Papel picado con nombre (DM-3) | **Desde $45** (chico $45 · mediano $55 · agrégalo a tu veladora por $35) | $22.01 · $27.67 · $17.87 | 51.1% · 49.7% · 48.9% | igual | Sí |
| Vela de cempasúchil (DM-4), en bolsa con tag | **$75** · **3 por $200** (decisión de Noemi) | $55.30 (3/h) · $41.30 (6/h) | **26.3% · 17.1% ⚠️** | **44.9% · 38.1% ⚠️** | **NO** (decisión de Noemi; requiere aprobación de Dirección) |
| Set Recuerdo (DM-5) | **Desde $169** (con nombre $169 · con foto $189) | $91.74 · $101.54 | 45.7% · 46.3% | igual | Sí |
| Set Ofrenda (DM-6) | **Desde $329** (con nombre $329 · con foto $349) | $207.69 · $217.49 (3/h) · $179.69 · $189.49 (6/h) | **36.9% · 37.7% ⚠️** | 45.4% · 45.7% | Solo a 6/h |
| Nota para todos | Envío por paquetería: se cobra aparte (guía + empaque). Pago 100% por adelantado en personalizados. Cempasúchil y sets: pago por transferencia o efectivo | | | | |

---

## 7. Validación rápida
- Veladoras, papel picado y Set Recuerdo: ≥45% con transferencia y envío cobrado aparte.
- ⚠️ **Abajo de 45% por decisión de Noemi:** cempasúchil $75 (26.3% a 3/h; 44.9% a 6/h) y 3 por $200 (17.1% a 3/h; 38.1% a 6/h). Margen positivo, pero fuera de la regla del README: registrar la aprobación en `direccion/`.
- ⚠️ Set Ofrenda $349 / $329: pasa solo con el cempasúchil a 6 por hora. Mientras se haga a 3 por hora queda en 37–38%.
- ⚠️ Rechazados por costos: Set Ofrenda con ahorro de $15 ($339 / $319) mientras la veladora tarde 26/19 min; DM-1 a $159 mientras tarde 26 min (47.7% suelta, pero el Set Recuerdo con foto quedaría sin margen para su descuento).
- ⚠️ Con link de pago quedan debajo de 45%: cempasúchil, papel picado agregado ($35, 44.8%) y todos los sets (41–43%). Con link, sumar la comisión o pedir transferencia.
- ⚠️ No ofrecer "envío gratis": el cempasúchil baja a 6–25% y los sets a 37–40%.
- Recalcular si: el colorante resulta ser por tanda (baja hasta ~$1.20 por vela), la veladora lleva 8% de aroma (+$5.10), el vaso cuesta más de $18 o los tiempos cronometrados salen arriba de lo estimado.

---

## 8. Preguntas para Noemi (en orden de impacto)

1. **Cempasúchil, moldes y colorante:** ¿cuántos moldes de cempasúchil tienes y puedes colar varios a la vez para sacar 6 por hora? Con $75 y 3 por $200 eso es lo que separa 26% de 45% de margen. El cuarto de sobre de colorante, ¿es para **una vela o para toda la tanda** (y cuántas velas salen por tanda)?
2. **Veladora:** ¿lleva el mismo aroma de $50/30 ml y cuántos gramos le pones? ¿Cuánto pagaste por vaso y cuántos gramos de cera le caben?
3. **Tiempos de la veladora:** cronometra la primera veladora con foto completa (diseño + prueba + imprimir + laminar + pegar + vela + empaque). Si sale en 15 min o menos, DM-1 puede bajar a $159 y el Set Ofrenda con foto puede volver a ahorrar $15.

Pendientes de la v1 que siguen abiertos (menor impacto): precio real del papel adhesivo, opalina y laminado; medida y precio de la bolsa de celofán; costo de paquetería y entrega local.

---

## Anexo: script del cálculo (reproducible, v2 con precio de cempasúchil decidido por Noemi)

Copiar a un archivo `.py` y ejecutar con `python3`. Cambiar los valores de la parte de arriba cuando Noemi mande los datos reales. Los costos de DM-3 vienen de la v1 (sin cambios).

```python
# Costeo Dia de Muertos 2026 v2 - Ananda Velas (17-oct-2026, datos de Noemi)
MO_H = 80.0; MERMA = 0.05
SOYA = 0.150; PARAF = 0.080                      # REAL $/g
AROMA = 50/30                                    # REAL $50 por 30 ml = $1.667/ml; densidad 1 g/ml: verificar
AROMA_G_CEMPA = 6.0                              # REAL: maximo 6 g por vela (106 g de cera = 5.7%)
PABILO_CM = 25/300                               # REAL
COLOR_CEMPA = 1.25                               # REAL-maximo: 1/4 de sobre de $5 (por vela o por tanda: preguntar)
CELOFAN = 0.90; LISTON = 0.50                    # estimado
OPALINA = 2.00; ADH = 5.00; LAMINADO = 4.00; TINTA_ALTA = 2.50; TINTA_BAJA = 1.00; DESP = 1.10  # estimado
TAG = (OPALINA + TINTA_BAJA)/8*DESP
PP_MAT = (OPALINA + TINTA_ALTA)*DESP + 0.50      # papel picado mediano sin sobre (materiales)
def mo(minutos): return MO_H*minutos/60
def costo(d): return round(sum(d.values())*(1+MERMA), 2)
def mg(p, c, com=0.0): return (p*(1-com) - c)/p*100

def cempa(vel_hora, bolsa):
    d = {'soya 53 g': 53*SOYA, 'parafina 53 g': 53*PARAF, 'aroma 6 g': AROMA_G_CEMPA*AROMA,
         'pabilo 9 cm': 9*PABILO_CM, 'colorante': COLOR_CEMPA, 'mano de obra': mo(60/vel_hora)}
    if bolsa: d.update({'celofan': CELOFAN, 'liston': LISTON, 'tag': TAG})
    else: d['sticker base'] = 0.40
    return d

def veladora(minutos, bolsa=True):
    g = 130; frag = g*AROMA_G_CEMPA/106          # misma proporcion que el cempasuchil (5.7%), estimado
    d = {'parafina 130 g': g*PARAF, f'aroma {frag:.1f} g': frag*AROMA, 'mecha': 1.50, 'vaso': 12.00,
         'etiqueta 1/2 hoja': (ADH + TINTA_ALTA + LAMINADO)/2*DESP, 'sticker base': 0.40, 'mano de obra': mo(minutos)}
    if bolsa: d['bolsa + liston'] = 1.20 + LISTON
    return d

def set_recuerdo(min_vel):
    d = veladora(min_vel); d['papel picado mat'] = PP_MAT; d['mo papel picado 9 min'] = mo(9); return d

def set_ofrenda(min_vel, vel_hora):
    d = veladora(min_vel, bolsa=False); c = cempa(vel_hora, False); c.pop('sticker base')
    d.update({'2 cempasuchil': 2*sum(c.values()), 'papel picado mat': PP_MAT, 'mo papel picado 9 min': mo(9),
              'caja kraft + viruta': 10.00, 'tag set': TAG})
    return d

if __name__ == '__main__':
    print('== DM-4 ==')
    for v in (3, 6):
        for b in (False, True):
            d = cempa(v, b); c = costo(d)
            print(f'{v}/h bolsa={b}: materiales {sum(x for k,x in d.items() if k!="mano de obra"):.2f} '
                  f'MO {d["mano de obra"]:.2f} costo {c:.2f} (MO {d["mano de obra"]*1.05/c*100:.0f}%) min45 {c/0.55:.2f}')
    print('== Veladoras ==')
    for m in (26, 19, 15, 12):
        d = veladora(m); c = costo(d)
        print(f'{m} min: costo {c:.2f} MO {d["mano de obra"]:.2f} ({d["mano de obra"]*1.05/c*100:.0f}%) min45 {c/0.55:.2f}')
    F = [('DM-1 foto', costo(veladora(26)), 169, 15), ('DM-2 papel picado', costo(veladora(19)), 149, 15),
         ('DM-4 en bolsa 3/h', costo(cempa(3, True)), 75, 15), ('DM-4 sin bolsa 3/h', costo(cempa(3, False)), 75, 15),
         ('DM-4 3x200 en bolsa 3/h', 3*costo(cempa(3, True)), 200, 15), ('DM-4 3x200 sin bolsa 3/h', 3*costo(cempa(3, False)), 200, 15), ('DM-3 chico', 22.01, 45, 0), ('DM-3 mediano', 27.67, 55, 0),
         ('DM-3 agregado', 17.87, 35, 0), ('DM-5 nombre', costo(set_recuerdo(19)), 169, 15),
         ('DM-5 foto', costo(set_recuerdo(26)), 189, 15), ('DM-6 foto 3/h', costo(set_ofrenda(26, 3)), 349, 25),
         ('DM-6 nombre 3/h', costo(set_ofrenda(19, 3)), 329, 25)]
    F += [('DM-4 en bolsa 6/h', costo(cempa(6, True)), 75, 15), ('DM-4 sin bolsa 6/h', costo(cempa(6, False)), 75, 15),
          ('DM-4 3x200 en bolsa 6/h', 3*costo(cempa(6, True)), 200, 15), ('DM-4 3x200 sin bolsa 6/h', 3*costo(cempa(6, False)), 200, 15),
          ('DM-6 foto 6/h', costo(set_ofrenda(26, 6)), 349, 25), ('DM-6 nombre 6/h', costo(set_ofrenda(19, 6)), 329, 25)]
    print('== Precios: producto | costo | precio | transferencia | link 4.2% | empaque absorbido ==')
    for n, c, p, emp in F:
        print(f'| {n} | ${c:.2f} | ${p} | {mg(p,c):.1f}% | {mg(p,c,0.0418):.1f}% | {mg(p,c+emp):.1f}% | min45 ${c/0.55:.0f} |')
    for n, c in [('DM-6 foto 3/h', costo(set_ofrenda(26, 3)))]:
        for com, lab in [(0.174, 'ML Clasica'), (0.226, 'ML Premium')]:
            print(n, lab, 'precio min 45% con envio $80 + empaque $25:', round((c+105)/(1-com-0.45)))
```

Fuentes de referencia consultadas el 17-oct-2026 (precios de terceros, **verificar**): [Cyberpuerta, opalina Copamex 225 g 100 hojas](https://www.cyberpuerta.mx/Impresion-y-Copiado/Papeles-para-Impresoras/Papel-Opalina/Copamex-Papel-Opalina-225g-m-100-Hojas-de-Tamano-Carta-Blanco.html), [ML, paquetes de opalina](https://listado.mercadolibre.com.mx/paquete-de-100-hojas-de-opalina), [Walmart, papel adhesivo para inyección](https://www.walmart.com.mx/browse/oficina-y-papeleria/papeleria/papel/264672_264673_264677), [Cosmos, proveedores de vasos para veladora](https://www.cosmos.com.mx/producto/vasos-4jc7/vasos-para-veladoras-4szf/). Comisiones de ML: ver fuentes en `costos/margenes-por-canal.md`.
