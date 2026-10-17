# Costos y precios: Día de Muertos 2026 (DM-1 a DM-6)

Responsable: Producción y costos · `costos-precios`. **Versión 3: sáb 17-oct-2026, noche** (tarea DM-c de `direccion/dia-de-muertos-2026.md`). Reemplaza las versiones 1 y 2 del mismo día.
Fórmula y reglas: `costos/README.md` (margen bruto ≥ 45% en menudeo). Cálculo reproducible: script en el anexo al final de este archivo.

> **Decisiones y datos reales de Noemi (17-oct) incluidos en la v3**
> - **Cempasúchil:** aroma 6 g a $50/30 ml, colorante ¼ de sobre de $5, **3 velas por hora**. Precio **fijo por decisión de Noemi: $75 la pieza y 3 por $200**. A 3 velas por hora deja 26% y 17%: **abajo de 45%** (sección 1).
> - **Veladoras DM-1/DM-2:** se **compran ya hechas a $21** (vaso, cera y mecha); papel adhesivo $6/hoja con 4 etiquetas. La mano de obra es solo personalizar y empacar.
> - **Excepción de margen:** Noemi fija **35% como objetivo en las veladoras DM-1 y DM-2, solo esta temporada** (la regla general sigue en 45%). Referencia que dio: veladoras chicas sin personalizar a ~$50.

---

## 0. Supuestos generales

| Concepto | Valor usado | Estatus |
|---|---|---|
| Mano de obra | $80/hora ($1.33/min), igual que `costos/calculo_costos.py` | Supuesto de la empresa |
| Merma | 5% sobre (materiales + mano de obra) | Regla README |
| Soya alto punto de fusión | $150/kg = $0.150/g | **REAL** (Noemi, 17-oct) |
| Parafina china | $80/kg = $0.080/g | **REAL** (Noemi, 17-oct). Solo cempasúchil (la veladora se compra hecha) |
| Aroma | $50 por 30 ml → **$1.667/ml ≈ $1.667/g** | Precio **REAL** (Noemi, 17-oct). Densidad 1 g/ml: **verificar** (pesar 10 ml en la báscula; los aceites de fragancia pesan ~0.9–1.05 g/ml) |
| Dosis de aroma, cempasúchil | **6 g por vela** (máximo) = 5.7% de 106 g de cera | **REAL** (Noemi, 17-oct). Reemplaza los escenarios (a)/(b) de la v1 |
| Pabilo | 3 m = $25 → $0.083/cm | **REAL** |
| Colorante, cempasúchil | **$1.25 por vela** (máximo: "ni una cuarta parte" de un sobre de $5) | **REAL como tope**. Si el cuarto de sobre rinde para una tanda de varias velas, el costo por vela baja (pregunta 1) |
| Bolsa de celofán / listón de cierre | $0.90 / $0.50 | **estimado** (`insumos-referencia.md`); medida de bolsa del cempasúchil: **verificar** |
| Opalina blanca 225 g, carta | $2.00/hoja | **estimado** con referencia: 100 hojas Copamex $151–155 en Cyberpuerta, $168–245 en ML (búsqueda del 17-oct, **verificar**) + envío |
| Papel adhesivo, carta | **$6.00/hoja, 4 etiquetas por hoja → $1.50 por etiqueta** | **REAL** (Noemi, 17-oct) |
| Laminado transparente en frío, carta | $4.00/hoja | **estimado** (ya comprado: falta el precio real) |
| Tinta Epson L3560 | $2.50/hoja cobertura alta · $1.00/hoja cobertura baja (tag) | **estimado** |
| Reimpresiones | +10% de hojas | **estimado** |
| Desgaste de cuchilla y tapete Cricut | $0.50 por hoja de papel picado | **estimado** |
| **Veladora en vaso (DM-1, DM-2)** | **$21.00 c/u, se compra ya hecha** (vaso + cera + mecha). Sin costo de cera, mecha, aroma ni vaciado | **REAL** (Noemi, 17-oct) |
| Etiqueta envolvente de la veladora | Papel $1.50 + tinta $0.63 + laminado $1.00 (¼ de hoja cada uno) +10% reimpresión = **$3.44** | Papel **REAL**; tinta y laminado **estimado** |
| Sticker de advertencias en la base | $0.40 | **estimado** (regla 6 de CLAUDE.md: toda vela lleva aviso) |
| Caja kraft + viruta (Set Ofrenda) | $10.00 | **estimado** |
| Empaque de envío por paquetería (caja + burbuja + relleno + cinta) | $15 una pieza · $25 un set | **estimado** |
| Pago | Transferencia o efectivo: 0%. Link de pago o terminal: ~4.2% (3.6% + IVA, **verificar** con tu proveedor) | Se muestra el margen en ambos casos |
| **Margen objetivo** | **45%** en todo (README) · **excepción: 35% en veladoras DM-1 y DM-2, solo temporada Día de Muertos 2026** | **Decisión de Noemi (17-oct)**. Referencia que dio: veladoras más chicas sin personalizar a ~$50 en el mercado (**verificar** con 3 precios) |
| Impuestos | Márgenes **antes** de ISR/IVA. Si Noemi factura con IVA trasladado, el margen baja ~13.8 puntos | Revisar con `finanzas-fiscal` |

### Tiempos de mano de obra

| Paso | Minutos | Estatus |
|---|---|---|
| **Vela de cempasúchil (vaciar, desmoldar y empacar)** | **20 (3 por hora por persona)** · escenario 10 (6 por hora, colada en varios moldes a la vez) | **REAL** (Noemi, 17-oct) · el de 6/h es escenario |
| **Veladora comprada: solo personalizar y empacar** (atención + prueba digital, diseño, imprimir, laminar, cortar, pegar etiqueta, embolsar) | **DM-1 con foto: 15 min · DM-2 con nombre: 10 min** (supuesto de trabajo con plantillas de Canva y por lotes) · pieza por pieza sin plantilla: ~22 min | **estimado**: cronometrar los primeros 5 pedidos |
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

### Costeo (veladora comprada ya hecha)

| Concepto | 10 min | 15 min | 22 min (pieza por pieza) | Estatus |
|---|---|---|---|---|
| Veladora en vaso comprada | $21.00 | $21.00 | $21.00 | **REAL** |
| Etiqueta: papel ¼ hoja $1.50 + tinta $0.63 + laminado $1.00, +10% | $3.44 | $3.44 | $3.44 | papel **REAL**, tinta y laminado estimado |
| Sticker de advertencias en la base | $0.40 | $0.40 | $0.40 | estimado |
| Bolsa de celofán + listón | $1.70 | $1.70 | $1.70 | estimado |
| **Subtotal materiales** | **$26.54** | **$26.54** | **$26.54** | |
| Mano de obra de personalización + empaque ($80/h) | $13.33 | $20.00 | $29.33 | estimado |
| Merma 5% | $1.99 | $2.33 | $2.79 | |
| **Costo unitario** | **$41.86** | **$48.86** | **$58.66** | |
| Peso de la mano de obra | 33% | 43% | 53% | |
| **Precio mínimo 35%** (excepción de Noemi) | **$64.40** | **$75.17** | $90.25 | |
| Precio mínimo 45% (regla general) | $76.11 | $88.84 | $106.65 | |

Lectura: la veladora comprada deja los materiales en $26.54; **la mano de obra es lo que más mueve el costo** (cada 5 minutos son ~$7). Por eso el precio depende de que la personalización salga en 10–15 min con plantillas de Canva y trabajo por lotes.

### Precio recomendado

| Producto | Minutos supuestos | Costo | **Precio** | Margen transferencia | Con link de pago | Si absorbes empaque ($15) | Pasa 35% | Pasa 45% |
|---|---|---|---|---|---|---|---|---|
| **DM-1 Veladora con foto (y mascota)** | 15 | $48.86 | **$79** | **38.2%** | 34.0% ⚠️ | 19.2% ⚠️ | Sí | No |
| DM-1 si sale en 10 min | 10 | $41.86 | $79 | 47.0% | 42.8% | 28.0% | Sí | Sí |
| DM-1 si tarda 22 min | 22 | $58.66 | $79 | **25.7% ⚠️** | 21.6% | 6.8% | **No** | No |
| **DM-2 Veladora papel picado con nombre** | 10 | $41.86 | **$69** | **39.3%** | 35.2% | 17.6% ⚠️ | Sí | No |
| DM-2 si tarda 15 min | 15 | $48.86 | $69 | **29.2% ⚠️** | 25.0% | 7.4% | **No** | No |

**Recomendación: DM-1 a $79 y DM-2 a $69.** Cumplen el 35% de Noemi con 15 y 10 min. Condición: **cronometrar los primeros 5 pedidos**. Si DM-1 pasa de ~17 min o DM-2 pasa de ~12 min, el margen cae abajo de 35% (DM-1 a 22 min deja 25.7%); en ese caso subir a DM-1 $89 / DM-2 $79. Comparado con la referencia de ~$50 por una veladora chica sin personalizar, $69–$79 cobra $19–$29 por la personalización.

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

## 4. Sets DM-5 y DM-6 (recalculados con la veladora comprada)

Precios por separado: DM-1 $79 · DM-2 $69 · papel picado agregado $35 · cempasúchil $75 (decisión de Noemi).

### Costeo

| Concepto | DM-5 foto | DM-5 nombre | DM-6 foto · 3/h | DM-6 nombre · 3/h | DM-6 foto · 6/h | DM-6 nombre · 6/h |
|---|---|---|---|---|---|---|
| Veladora comprada + etiqueta + sticker (+ bolsa en DM-5) | $26.54 | $26.54 | $24.84 (sin bolsa, va en caja) | $24.84 | $24.84 | $24.84 |
| Mano de obra veladora (15 min foto · 10 min nombre) | $20.00 | $13.33 | $20.00 | $13.33 | $20.00 | $13.33 |
| Papel picado mediano, mismo nombre (materiales) | $5.45 | $5.45 | $5.45 | $5.45 | $5.45 | $5.45 |
| Mano de obra papel picado (9 min) | $12.00 | $12.00 | $12.00 | $12.00 | $12.00 | $12.00 |
| 2 velas de cempasúchil sin bolsa (con su mano de obra) | — | — | $101.72 | $101.72 | $75.05 | $75.05 |
| Caja kraft + viruta + tag del set | — | — | $10.41 | $10.41 | $10.41 | $10.41 |
| Merma 5% | $3.20 | $2.87 | $8.72 | $8.39 | $7.39 | $7.05 |
| **Costo del set** | **$67.19** | **$60.19** | **$183.13** | **$176.13** | **$155.13** | **$148.13** |
| Precio mínimo 35% | $103 | $93 | $282 | $271 | $239 | $228 |

### Precio

| Set | Por separado | Precio del set | Ahorro | Margen transferencia | Con link | Si absorbes empaque | Decisión |
|---|---|---|---|---|---|---|---|
| **DM-5 Set Recuerdo con foto** | $79 + $35 = $114 | **$104** | $10 | **35.4%** | 31.2% ⚠️ | 21.0% ⚠️ | **Recomendado** |
| DM-5 con foto, ahorro $15 | $114 | $99 | $15 | 32.1% ⚠️ | 28.0% | 17.0% | Abajo de 35% (positivo) |
| **DM-5 Set Recuerdo con nombre** | $69 + $35 = $104 | **$94** | $10 | **36.0%** | 31.8% ⚠️ | 20.0% ⚠️ | **Recomendado** |
| DM-5 con nombre, ahorro $15 | $104 | $89 | $15 | 32.4% ⚠️ | 28.2% | 15.5% | Abajo de 35% (positivo) |
| **DM-6 Set Ofrenda con foto** | $79 + 2 × $75 + $35 = $264 | **$249** | $15 | **26.5% ⚠️ (3/h)** · 37.7% (6/h) | 22.3% · 33.5% | 16.4% · 27.7% | Recomendado; pasa 35% solo a 6/h |
| **DM-6 Set Ofrenda con nombre** | $69 + 2 × $75 + $35 = $254 | **$239** | $15 | **26.3% ⚠️ (3/h)** · 38.0% (6/h) | 22.1% · 33.8% | 15.8% · 27.6% | Recomendado; pasa 35% solo a 6/h |

**Lectura:**
- **Set Recuerdo:** con ahorro de $15 queda en 32%; propongo **ahorro de $10 ($104 / $94)** para quedar arriba de 35%. Si Noemi prefiere el número redondo ($99 / $89), el margen es positivo (32%) pero abajo de su propio objetivo.
- **Set Ofrenda:** a $249 / $239 conserva el ahorro de $15 y pasa 35% **solo si el cempasúchil se hace a 6 por hora**. A 3 por hora deja 26% (positivo, pero abajo de 35% y de 45%): el cempasúchil a $75 es lo que jala el margen hacia abajo. A 3 por hora no hay precio que pase 35% y siga siendo más barato que las piezas sueltas ($282 > $264).
- Todos los sets: **margen positivo en todos los escenarios**, pero ninguno llega al 45% del README. Al aplicar el 35% de la excepción a los sets se extiende la decisión de Noemi: confirmarlo (pregunta 3).
- Cobrar los sets **solo por transferencia o efectivo** y **envío aparte**: con link o con envío absorbido bajan a 16–33%.

---

## 5. Mercado Libre: DM-6 Set Ofrenda, **sigue sin publicarse**

Supuestos (todos **verificar en el simulador de costos de la publicación**): ML Clásica 15% + IVA = 17.4% efectivo; Premium 19.5% + IVA = 22.6%; cargo fijo abajo de $299 (no incluido, empeora el resultado); envío ≈ $80; empaque de envío $25.

| Escenario | Precio $249 | Precio $299 | Precio $349 | Precio mínimo para 45% |
|---|---|---|---|---|
| DM-6 con foto (3/h, costo $183.13), ML Clásica | −33.1% ⚠️ | −13.8% ⚠️ | 0.0% ⚠️ | **$766** |
| DM-6 con foto (3/h), ML Premium | −38.3% ⚠️ | −19.0% ⚠️ | −5.2% ⚠️ | **$889** |
| Kit genérico sin personalizar (costo $162.13), ML Clásica | −24.7% ⚠️ | −6.7% ⚠️ | 6.1% ⚠️ | **$710** |

**Decisión de costos: RECHAZADO para ML** (pierde dinero a $249–$299). Vender el Set Ofrenda **solo por WhatsApp/IG/FB**.

---

## 6. Precios para los estados de WhatsApp (listos para copiar)

Margen con pago por transferencia/efectivo y envío por paquetería cobrado aparte. Veladoras con 15 min (foto) y 10 min (nombre); cempasúchil a 3 velas por hora (real) y a 6 por hora (escenario).

| Producto | Texto para el estado | Costo | Margen | Objetivo | ¿Cumple? |
|---|---|---|---|---|---|
| Veladora con foto (DM-1) y versión mascota | **$79** | $48.86 | 38.2% | 35% (decisión de Noemi) | Sí |
| Veladora papel picado con nombre (DM-2) | **$69** | $41.86 | 39.3% | 35% (decisión de Noemi) | Sí |
| "Desde [precio]" (estado del sáb 17, 14:00) | **Desde $69** | — | — | — | — |
| Papel picado con nombre (DM-3) | **Desde $45** (chico $45 · mediano $55 · agrégalo a tu veladora por $35) | $22.01 · $27.67 · $17.87 | 51.1% · 49.7% · 48.9% | 45% | Sí |
| Vela de cempasúchil (DM-4), en bolsa con tag | **$75** · **3 por $200** (decisión de Noemi) | $55.30 (3/h) · $41.30 (6/h) | **26.3% · 17.1% ⚠️ (3/h)** · 44.9% · 38.1% (6/h) | 45% | **No** (precio fijo por decisión de Noemi) |
| Set Recuerdo (DM-5) | **Desde $94** (con nombre $94 · con foto $104) | $60.19 · $67.19 | 36.0% · 35.4% | 35% | Sí |
| Set Ofrenda (DM-6) | **Desde $239** (con nombre $239 · con foto $249) | $176.13 · $183.13 (3/h) · $148.13 · $155.13 (6/h) | **26.3% · 26.5% ⚠️ (3/h)** · 38.0% · 37.7% (6/h) | 35% | Solo a 6/h |
| Nota para todos | Envío por paquetería: se cobra aparte (guía + empaque). Pago 100% por adelantado en personalizados. Pago por transferencia o efectivo | | | | |

---

## 7. Validación rápida
- **Ningún precio tiene margen negativo** en ningún escenario calculado (el más bajo: cempasúchil 3 por $200 a 3/h, 17.1%).
- Cumplen 45% (README): papel picado DM-3. Cumplen la excepción de 35%: DM-1 $79 (15 min), DM-2 $69 (10 min), Set Recuerdo $104 / $94.
- ⚠️ **Abajo del objetivo por decisión de Noemi:** cempasúchil $75 (26.3% a 3/h) y 3 por $200 (17.1% a 3/h). Set Ofrenda $249 / $239: 26% a 3/h, 38% a 6/h.
- ⚠️ La excepción de 35% es **solo para la temporada de Día de Muertos 2026** (decisión de Noemi, 17-oct). No usar estos precios como base para Navidad ni mayoreo. Avisar a `documentador-procesos` / anotar en `direccion/`.
- ⚠️ Con link de pago, DM-1 baja a 34.0% y los sets a 22–34%: pedir transferencia.
- ⚠️ No ofrecer "envío gratis": todo baja a 7–28%.
- Recalcular si: la personalización tarda más de 15 min (foto) / 10 min (nombre), el colorante resulta ser por tanda (baja ~$1.20 por vela) o el laminado/tinta real difiere del estimado.

---

## 8. Preguntas para Noemi (en orden de impacto)

1. **Cempasúchil, moldes y colorante:** ¿cuántos moldes tienes y puedes colar varios a la vez para sacar 6 por hora? A $75 eso separa 26% de 45% de margen, y hace que el Set Ofrenda pase de 26% a 38%. El cuarto de sobre de colorante, ¿es para una vela o para toda la tanda?
2. **Tiempo real de personalización:** cronometra 5 veladoras con foto y 5 con nombre (prueba digital, diseño, imprimir, laminar, cortar, pegar, embolsar). Los precios de $79 / $69 aguantan hasta ~17 y ~12 min.
3. **Sets:** ¿el 35% también aplica a los sets? Si sí, Set Recuerdo $104 / $94 (ahorro $10); si prefieres el ahorro de $15 ($99 / $89), queda en 32%.

Pendientes que siguen abiertos (menor impacto): precio real del laminado, la tinta, la opalina y la bolsa de celofán; densidad del aroma; costo de paquetería y entrega local.

---

## Anexo: script del cálculo (reproducible, v3)

Copiar a un archivo `.py` y ejecutar con `python3`. Cambiar los valores de la parte de arriba cuando Noemi mande datos reales. Los costos de DM-3 vienen de la v1 (sin cambios).

```python
# Costeo Dia de Muertos 2026 v3 - Ananda Velas (17-oct-2026, datos reales de Noemi)
MO_H = 80.0; MERMA = 0.05
SOYA = 0.150; PARAF = 0.080                      # REAL $/g
AROMA = 50/30                                    # REAL $50 por 30 ml = $1.667/ml; densidad 1 g/ml: verificar
AROMA_G_CEMPA = 6.0                              # REAL: maximo 6 g por vela de cempasuchil
PABILO_CM = 25/300                               # REAL
COLOR_CEMPA = 1.25                               # REAL-tope: 1/4 de sobre de $5 (por vela o por tanda: preguntar)
VELADORA = 21.00                                 # REAL: veladora en vaso COMPRADA YA HECHA (vaso + cera + mecha) $21 c/u
MIN_FOTO = 15; MIN_NOMBRE = 10                   # supuesto de trabajo: personalizar + empacar (sin vaciado); cronometrar
MIN_FOTO_SIN_LOTES = 22                          # estimado si se hace pieza por pieza (5 atencion + 10 diseno + 5 etiqueta + 2 empaque)
MARGEN_VEL = 0.35                                # decision de Noemi (17-oct): objetivo 35% en veladoras DM, solo esta temporada
ADH = 6.00; ETQ_POR_HOJA = 4                     # REAL: papel adhesivo $6/hoja, 4 etiquetas por hoja
CELOFAN = 0.90; LISTON = 0.50                    # estimado
OPALINA = 2.00; LAMINADO = 4.00; TINTA_ALTA = 2.50; TINTA_BAJA = 1.00; DESP = 1.10  # estimado
TAG = (OPALINA + TINTA_BAJA)/8*DESP
ETIQUETA = (ADH + TINTA_ALTA + LAMINADO)/ETQ_POR_HOJA*DESP   # $3.44
PP_MAT = (OPALINA + TINTA_ALTA)*DESP + 0.50      # papel picado mediano sin sobre (materiales)
PRECIO_CEMPA = 75; PRECIO_CEMPA_3 = 200          # decision de Noemi (fijo)
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
    d = {'veladora en vaso (REAL)': VELADORA, 'etiqueta 1/4 hoja': ETIQUETA, 'sticker base': 0.40,
         'mano de obra': mo(minutos)}
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
    print(f'etiqueta {ETIQUETA:.2f}')
    for v in (3, 6):
        for b in (False, True):
            c = costo(cempa(v, b))
            print(f'DM-4 {v}/h bolsa={b}: costo {c:.2f} | $75 {mg(75,c):.1f}% | 3x$200 {mg(200,3*c):.1f}%')
    for m in (22, 15, 12, 10):
        d = veladora(m); c = costo(d)
        print(f'veladora {m} min: costo {c:.2f} MO {d["mano de obra"]:.2f} ({d["mano de obra"]*1.05/c*100:.0f}%) min35 {c/(1-MARGEN_VEL):.2f} min45 {c/0.55:.2f} '
              + ' '.join(f'${p}:{mg(p,c):.1f}%' for p in (69, 75, 79, 89, 99)))
    PV1, PV2, PP_AGR = 79, 69, 35
    F = [('DM-1 foto 15 min', costo(veladora(15)), PV1, 15), ('DM-1 foto 10 min', costo(veladora(10)), PV1, 15),
         ('DM-1 foto 22 min (sin lotes)', costo(veladora(22)), PV1, 15),
         ('DM-2 nombre 10 min', costo(veladora(10)), PV2, 15), ('DM-2 nombre 15 min', costo(veladora(15)), PV2, 15),
         ('DM-3 agregado', 17.87, PP_AGR, 0),
         ('DM-4 en bolsa 3/h', costo(cempa(3, True)), PRECIO_CEMPA, 15), ('DM-4 3x200 en bolsa 3/h', 3*costo(cempa(3, True)), PRECIO_CEMPA_3, 15),
         ('DM-4 en bolsa 6/h', costo(cempa(6, True)), PRECIO_CEMPA, 15), ('DM-4 3x200 en bolsa 6/h', 3*costo(cempa(6, True)), PRECIO_CEMPA_3, 15)]
    sep5f, sep5n = PV1 + PP_AGR, PV2 + PP_AGR
    sep6f, sep6n = PV1 + 2*PRECIO_CEMPA + PP_AGR, PV2 + 2*PRECIO_CEMPA + PP_AGR
    print('por separado: DM-5 foto', sep5f, 'nombre', sep5n, '| DM-6 foto', sep6f, 'nombre', sep6n)
    F += [('DM-5 foto', costo(set_recuerdo(MIN_FOTO)), sep5f - 15, 15), ('DM-5 nombre', costo(set_recuerdo(MIN_NOMBRE)), sep5n - 15, 15)]
    for v in (3, 6):
        F += [(f'DM-6 foto {v}/h', costo(set_ofrenda(MIN_FOTO, v)), sep6f - 15, 25),
              (f'DM-6 nombre {v}/h', costo(set_ofrenda(MIN_NOMBRE, v)), sep6n - 15, 25)]
    print('producto | costo | precio | transferencia | link 4.2% | empaque absorbido | min45')
    for n, c, p, emp in F:
        print(f'| {n} | ${c:.2f} | ${p} | {mg(p,c):.1f}% | {mg(p,c,0.0418):.1f}% | {mg(p,c+emp):.1f}% | min35 ${c/0.65:.0f} | min45 ${c/0.55:.0f} |')
    gen = {'veladora': VELADORA + ETIQUETA + 0.40, 'mo vel 5 min (etiqueta generica)': mo(5),
           '2 cempa 3/h': 2*sum(v for k, v in cempa(3, False).items() if k != 'sticker base'),
           'pp generico': PP_MAT, 'mo pp 4 min': mo(4), 'caja': 10.0, 'tag': TAG}
    for n, c in [('DM-6 foto 3/h', costo(set_ofrenda(MIN_FOTO, 3))), ('kit generico', costo(gen))]:
        for com, lab in [(0.174, 'ML Clasica'), (0.226, 'ML Premium')]:
            print(n, f'{c:.2f}', lab, [round(mg(p, c + 105, com), 1) for p in (249, 299, 349)],
                  'min45', round((c + 105)/(1 - com - 0.45)))
```

Fuentes de referencia consultadas el 17-oct-2026 (precios de terceros, **verificar**): [Cyberpuerta, opalina Copamex 225 g 100 hojas](https://www.cyberpuerta.mx/Impresion-y-Copiado/Papeles-para-Impresoras/Papel-Opalina/Copamex-Papel-Opalina-225g-m-100-Hojas-de-Tamano-Carta-Blanco.html), [ML, paquetes de opalina](https://listado.mercadolibre.com.mx/paquete-de-100-hojas-de-opalina), [Walmart, papel adhesivo para inyección](https://www.walmart.com.mx/browse/oficina-y-papeleria/papeleria/papel/264672_264673_264677), [Cosmos, proveedores de vasos para veladora](https://www.cosmos.com.mx/producto/vasos-4jc7/vasos-para-veladoras-4szf/). Comisiones de ML: ver fuentes en `costos/margenes-por-canal.md`.
