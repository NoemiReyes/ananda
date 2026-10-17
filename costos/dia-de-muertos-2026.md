# Costos y precios: Día de Muertos 2026 (DM-1, DM-3 a DM-6)

Responsable: Producción y costos · `costos-precios`. **Versión 4 (final): sáb 17-oct-2026, noche** (tarea DM-c de `direccion/dia-de-muertos-2026.md`). Reemplaza las versiones 1 a 3 del mismo día.
Fórmula y reglas: `costos/README.md` (margen bruto ≥ 45% en menudeo). Cálculo reproducible: script en el anexo al final de este archivo.

> **Decisiones finales de Noemi (17-oct)**
> - **DM-4 Vela de cempasúchil: $75 la pieza y 3 por $200 (confirmado).** Datos reales: aroma 6 g a $50/30 ml, colorante ¼ de sobre de $5, 3 velas por hora. A 3 velas por hora deja 26% y 17%: **abajo de 45%** (sección 1).
> - **DM-1 Veladora con foto: $79.** La veladora se **compra ya hecha a $21** (vaso, cera y mecha); papel adhesivo $6/hoja con 4 etiquetas. La mano de obra es solo personalizar y empacar.
> - **DM-2 Veladora papel picado con nombre: EN PAUSA.** Fuera de la tabla de precios.
> - **DM-3 Papel picado: solo tamaño grande 26 × 19 cm**, en opalina **de color**, solo corte en Cricut, sin impresión ni tinta. Dos versiones: **genérico $35** y **personalizado con nombre $45**. Ya no hay chico ni mediano.
> - **Sets:** Set Recuerdo = veladora con foto + papel picado grande personalizado. Set Ofrenda = veladora con foto + 2 cempasúchil + papel picado grande personalizado.
> - **Excepción de margen:** objetivo **35%** en veladoras (y papel picado, sets) solo esta temporada; la regla general sigue en 45%.

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
| Opalina carta (blanca y de color) | **$3.00/hoja** | **REAL** (Noemi, 17-oct): la opalina de color del papel picado también cuesta $3 |
| Sobre de celofán para papel picado 26 × 19 | $1.20 | **estimado** (medida: verificar) |
| Papel adhesivo, carta | **$6.00/hoja, 4 etiquetas por hoja → $1.50 por etiqueta** | **REAL** (Noemi, 17-oct) |
| Laminado transparente en frío, carta | $4.00/hoja | **estimado** (ya comprado: falta el precio real) |
| Tinta Epson L3560 | $2.50/hoja cobertura alta (etiqueta con foto) · $1.00/hoja cobertura baja (tag). El papel picado no lleva tinta | **estimado** |
| Reimpresiones | +10% de hojas | **estimado** |
| Desgaste de cuchilla y tapete Cricut | $0.50 por hoja de papel picado | **estimado** |
| **Veladora en vaso (DM-1)** | **$21.00 c/u, se compra ya hecha** (vaso + cera + mecha). Sin costo de cera, mecha, aroma ni vaciado | **REAL** (Noemi, 17-oct) |
| Etiqueta envolvente de la veladora | Papel $1.50 + tinta $0.63 + laminado $1.00 (¼ de hoja cada uno) +10% reimpresión = **$3.44** | Papel **REAL**; tinta y laminado **estimado** |
| Sticker de advertencias en la base | $0.40 | **estimado** (regla 6 de CLAUDE.md: toda vela lleva aviso) |
| Caja kraft + viruta (Set Ofrenda) | $10.00 | **estimado**; la caja debe caber el papel picado de 26 × 19 sin doblar: **verificar** medida |
| Empaque de envío por paquetería (caja + burbuja + relleno + cinta) | $15 una pieza · $25 un set | **estimado** |
| Pago | Transferencia o efectivo: 0%. Link de pago o terminal: ~4.2% (3.6% + IVA, **verificar** con tu proveedor) | Se muestra el margen en ambos casos |
| **Margen objetivo** | **45%** en todo (README) · **excepción: 35% en veladora DM-1, papel picado DM-3 y sets, solo temporada Día de Muertos 2026** | **Decisión de Noemi (17-oct)**. Referencia que dio: veladoras más chicas sin personalizar a ~$50 en el mercado (**verificar** con 3 precios) |
| Impuestos | Márgenes **antes** de ISR/IVA. Si Noemi factura con IVA trasladado, el margen baja ~13.8 puntos | Revisar con `finanzas-fiscal` |

### Tiempos de mano de obra

| Paso | Minutos | Estatus |
|---|---|---|
| **Vela de cempasúchil (vaciar, desmoldar y empacar)** | **20 (3 por hora por persona)** · escenario 10 (6 por hora, colada en varios moldes a la vez) | **REAL** (Noemi, 17-oct) · el de 6/h es escenario |
| **Veladora con foto, comprada: personalizar y empacar** (atención + prueba digital, diseño, imprimir, laminar, cortar, pegar etiqueta, embolsar) | **15 min** (supuesto con plantillas de Canva y por lotes) · pieza por pieza: ~22 min | **estimado**: cronometrar los primeros 5 pedidos |
| **Papel picado grande 26 × 19** (solo corte en Cricut + retirar recortes; el personalizado incluye poner el nombre) | **Genérico 10 min · personalizado 15 min** | dato de trabajo de Noemi; cronometrar |

En el cempasúchil, los 20 min incluyen el empacado; en el Set Ofrenda la vela va sin bolsa, pero se dejan los mismos 20 min (acomodar en la caja), para no quedarse cortos.

---

## 1. DM-4 Vela de Cempasúchil — **$75 y 3 por $200 (confirmado)**

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
| Bolsa de celofán $0.90 + listón $0.50 + tag en opalina $0.55 | bolsa y listón estimado; opalina REAL | — | $1.95 | — | $1.95 |
| **Mano de obra** (20 min a 3/h · 10 min a 6/h) | REAL (3/h) · escenario (6/h) | **$26.67** | **$26.67** | $13.33 | $13.33 |
| Merma 5% | | $2.56 | $2.64 | $1.90 | $1.97 |
| **Costo unitario** | | **$53.82** | **$55.45** | **$39.82** | **$41.45** |
| Peso de la mano de obra en el costo | | 52% | 51% | 35% | 34% |
| Precio mínimo 35% · 45% | | $83 · $98 | $85 · $101 | $61 · $72 | $64 · $75 |

- **La mano de obra domina el costo: $26.67 de $55.45 (51%).** El aroma ($10.00) es el insumo más caro.
- **Colada en varios moldes (6 por hora)** baja el costo $14 por vela. Es la palanca más grande de Día de Muertos; cada molde extra se paga con unas 20 velas (precio del molde: **verificar**).

### Margen real al precio confirmado

3 por $200 = $66.67 por vela.

| Precio | Productividad | Empaque | Costo | Margen transferencia | Con link de pago | Si absorbes empaque de envío ($15) | ¿35%? | ¿45%? |
|---|---|---|---|---|---|---|---|---|
| $75 | 3 por hora | sin bolsa | $53.82 | **28.2% ⚠️** | 24.1% | 8.2% | No | No |
| $75 | 3 por hora | con bolsa + tag | $55.45 | **26.1% ⚠️** | 21.9% | 6.1% | No | No |
| $75 | 6 por hora | sin bolsa | $39.82 | 46.9% | 42.7% | 26.9% | Sí | Sí |
| $75 | 6 por hora | con bolsa + tag | $41.45 | 44.7% | 40.6% | 24.7% | Sí | No (por 0.3 puntos) |
| 3 por $200 | 3 por hora | sin bolsa | $161.46 | **19.3% ⚠️** | 15.1% | 11.8% | No | No |
| 3 por $200 | 3 por hora | con bolsa + tag | $166.35 | **16.8% ⚠️** | 12.6% | 9.3% | No | No |
| 3 por $200 | 6 por hora | sin bolsa | $119.46 | 40.3% | 36.1% | 32.8% | Sí | No |
| 3 por $200 | 6 por hora | con bolsa + tag | $124.35 | 37.8% | 33.6% | 30.3% | Sí | No |

**Lectura de costos (para Dirección):** margen siempre positivo, pero a 3 velas por hora el cempasúchil queda en 26% (pieza) y 17% (3 por $200). **Con 6 por hora pasa el 35%** en todos los casos. Pasar a colada en varios moldes es lo que hace funcionar este precio. Vender abajo de 45% requiere aprobación escrita de Dirección: dejar registrada la decisión de Noemi en `direccion/`. No cobrar con link ni absorber envío en el cempasúchil.

---

## 2. DM-1 Veladora con foto — **$79 (decisión de Noemi)** · DM-2 en pausa

### Costeo (veladora comprada ya hecha)

| Concepto | 10 min | **15 min (base)** | 22 min (pieza por pieza) | Estatus |
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
| Precio mínimo 35% · 45% | $64 · $76 | **$75 · $89** | $90 · $107 | |
| **Margen a $79** (transferencia · link · empaque absorbido) | 47.0% · 42.8% · 28.0% | **38.2% · 34.0% · 19.2%** | **25.7% ⚠️** · 21.6% · 6.8% | |

**$79 cumple el 35% si la personalización sale en ~17 min o menos.** Si se hace pieza por pieza (22 min) cae a 25.7%: trabajar con plantilla de Canva e imprimir/laminar por lotes. La mano de obra es lo que más mueve el costo (cada 5 minutos son ~$7).

**DM-2 (veladora papel picado con nombre): EN PAUSA** por decisión de Noemi. Si se reactiva, su costo con 10 min sería $41.86 (a $69 dejaba 39.3%).

---

## 3. DM-3 Papel picado grande 26 × 19 cm (opalina de color, solo corte)

1 por hoja carta, **solo corte en Cricut** (no cabe en el área de Imprimir y cortar), **sin tinta**.

| Concepto | Genérico (diseño fijo) | Personalizado (con nombre) | Estatus |
|---|---|---|---|
| Opalina de color, 1 hoja +10% cortes fallidos | $3.30 | $3.30 | $3/hoja **REAL** (opalina de color, Noemi 17-oct) |
| Cuchilla y tapete | $0.50 | $0.50 | estimado |
| Sobre de celofán grande | $1.20 | $1.20 | estimado |
| **Materiales** | **$5.00** | **$5.00** | |
| Mano de obra ($80/h) | $13.33 (10 min) | $20.00 (15 min) | dato de trabajo de Noemi |
| Merma 5% | $0.92 | $1.25 | |
| **Costo unitario** | **$19.25** | **$26.25** | |
| Peso de la mano de obra | 73% | 80% | |
| Precio mínimo 35% | $29.62 | $40.38 | |
| Precio mínimo 45% | $35.00 | $47.73 | |

### Precio (sugerido por Noemi) y comparación con Pixé Design

| Producto | **Precio** | Margen transferencia | Con link | Si absorbes empaque ($15) | ¿35%? | ¿45%? | Pixé Design grande | Nuestro margen al precio de Pixé |
|---|---|---|---|---|---|---|---|---|
| **Genérico** | **$35** | **45.0%** | 40.8% | 2.1% ⚠️ | Sí | Sí (justo) | — | $30: 35.8% · $25 mayoreo: 23.0% |
| **Personalizado con nombre** | **$45** | **41.7%** | 37.5% | 8.3% ⚠️ | Sí | No | $30 con nombre · $25 mayoreo | $30: **12.5% ⚠️** · $25: **−5.0% (pérdida)** |

**Confirmados: genérico $35 y personalizado $45** (≥35%). Precios redondos alternativos para llegar a 45% en el personalizado: $49 (46.4%). El material cuesta $5: **el 73–80% del costo es tiempo**. Contra Pixé ($30 con nombre) no competimos en precio: a $30 nos queda 12.5% y a $25 perdemos. El papel picado se empuja como parte del Set Recuerdo y del Set Ofrenda. **No vender el papel picado suelto con envío absorbido** (queda en 2–8%).

---

## 4. Sets DM-5 y DM-6

Precios por separado: veladora con foto $79 · papel picado grande personalizado $45 · cempasúchil $75.

### Costeo

| Concepto | Set Recuerdo (DM-5) | Set Ofrenda (DM-6) · 3/h | Set Ofrenda (DM-6) · 6/h |
|---|---|---|---|
| Veladora con foto: materiales | $26.54 (con bolsa) | $24.84 (sin bolsa, va en caja) | $24.84 |
| Mano de obra veladora (15 min) | $20.00 | $20.00 | $20.00 |
| Papel picado grande personalizado: materiales | $5.00 | $5.00 | $5.00 |
| Mano de obra papel picado (15 min) | $20.00 | $20.00 | $20.00 |
| 2 velas de cempasúchil sin bolsa (con su mano de obra) | — | $101.72 | $75.05 |
| Caja kraft + viruta + tag del set | — | $10.55 | $10.55 |
| Merma 5% | $3.58 | $9.11 | $7.77 |
| **Costo del set** | **$75.11** | **$191.21** | **$163.21** |
| Precio mínimo 35% | $115.55 | $294.17 | $251.09 |

### Precio

| Set | Por separado | **Precio del set** | Ahorro | Margen transferencia | Con link | Si absorbes empaque | Decisión |
|---|---|---|---|---|---|---|---|
| **Set Recuerdo** (veladora con foto + papel picado grande personalizado) | $79 + $45 = $124 | **$119** | $5 | **36.9%** | 32.7% ⚠️ | 24.3% ⚠️ | **Recomendado** (≥35%) |
| Set Recuerdo, alternativa | $124 | $115 | $9 | 34.7% ⚠️ | 30.5% | 21.6% | Positivo, 0.3 puntos abajo de 35% |
| Set Recuerdo, alternativa | $124 | $109 | $15 | 31.1% ⚠️ | 26.9% | 17.3% | Positivo, abajo de 35% |
| **Set Ofrenda** (veladora con foto + 2 cempasúchil + papel picado grande personalizado) | $79 + 2 × $75 + $45 = $274 | **$259** | $15 | **26.2% ⚠️ (3/h)** · **37.0% (6/h)** | 22.0% · 32.8% | 16.5% · 27.3% | **Recomendado**; pasa 35% solo a 6/h |
| Set Ofrenda, alternativa | $274 | $265 | $9 | 27.8% (3/h) · 38.4% (6/h) | 23.7% · 34.2% | 18.4% · 29.0% | Número menos redondo |

**Lectura:**
- **Set Recuerdo $119:** más barato que por separado y arriba de 35%. Con ahorro de $9–$15 baja a 31–35%: positivo, pero abajo del objetivo.
- **Set Ofrenda $259:** ahorra $15 y **pasa 35% solo si el cempasúchil se hace a 6 por hora**; a 3 por hora deja 26.2% (positivo). A 3 por hora no hay precio que pase 35% y siga siendo más barato que las piezas sueltas ($294 > $274).
- Ningún set llega al 45% del README. **Ningún set tiene margen negativo**.
- Cobrar los sets **solo por transferencia o efectivo** y **envío aparte**.

---

## 5. Mercado Libre: Set Ofrenda, **sigue sin publicarse**

Supuestos (todos **verificar en el simulador de costos de la publicación**): ML Clásica 15% + IVA = 17.4% efectivo; Premium 19.5% + IVA = 22.6%; cargo fijo abajo de $299 (no incluido, empeora el resultado); envío ≈ $80; empaque de envío $25.

| Escenario | Precio $259 | Precio $299 | Precio $349 | Precio mínimo para 45% |
|---|---|---|---|---|
| Set Ofrenda (3/h, costo $191.21), ML Clásica | −31.8% ⚠️ | −16.5% ⚠️ | −2.3% ⚠️ | **$788** |
| Set Ofrenda (3/h), ML Premium | −37.0% ⚠️ | −21.7% ⚠️ | −7.5% ⚠️ | **$914** |
| Kit genérico sin personalizar (costo $170.21), ML Clásica | −23.7% ⚠️ | −9.4% ⚠️ | 3.7% ⚠️ | **$732** |

**Decisión de costos: RECHAZADO para ML** (pierde dinero de $259 a $349). Vender los sets **solo por WhatsApp/IG/FB**.

---

## 6. Precios para los estados de WhatsApp (listos para copiar)

Margen con pago por transferencia/efectivo y envío por paquetería cobrado aparte. Veladora con 15 min; papel picado 10 min genérico / 15 min personalizado; cempasúchil a 3 velas por hora (real) y 6 por hora (escenario).

| Producto | Texto para el estado | Costo | Margen | Objetivo | ¿Cumple? |
|---|---|---|---|---|---|
| Veladora con foto (DM-1) y versión mascota | **$79** | $48.86 | 38.2% | 35% | Sí |
| Papel picado grande 26 × 19 (DM-3) | **Desde $35** (genérico $35 · con nombre $45) | $19.25 · $26.25 | 45.0% · 41.7% | 35% | Sí |
| Vela de cempasúchil (DM-4) | **$75** · **3 por $200** | $55.45 · $166.35 (3/h, en bolsa) | **26.1% · 16.8% ⚠️** (3/h) · 44.7% · 37.8% (6/h) | 35% / 45% | Solo a 6/h |
| Set Recuerdo (DM-5): veladora con foto + papel picado con nombre | **$119** | $75.11 | 36.9% | 35% | Sí |
| Set Ofrenda (DM-6): veladora con foto + 2 cempasúchil + papel picado con nombre | **$259** | $191.21 (3/h) · $163.21 (6/h) | **26.2% ⚠️** (3/h) · 37.0% (6/h) | 35% | Solo a 6/h |
| "Desde [precio]" | **Desde $35** | — | — | — | — |
| Nota para todos | Envío por paquetería: se cobra aparte (guía + empaque). Pago 100% por adelantado en personalizados. Pago por transferencia o efectivo | | | | |

DM-2 (veladora papel picado con nombre): **en pausa, no se publica**.

---

## 7. Validación rápida
- **Ningún precio tiene margen negativo** (el más bajo: cempasúchil 3 por $200 a 3/h, 16.8%).
- Cumplen 35%: veladora con foto $79 (≤17 min), papel picado $35 / $45, Set Recuerdo $119. El papel picado genérico llega justo a 45%.
- ⚠️ **Abajo de 35% a 3 velas por hora (decisión de Noemi):** cempasúchil $75 (26.1%), 3 por $200 (16.8%) y Set Ofrenda $259 (26.2%). Los tres pasan 35% a 6 por hora.
- ⚠️ La excepción de 35% es **solo para Día de Muertos 2026**. No usar estos precios para Navidad ni mayoreo. Anotar en `direccion/` y avisar a `documentador-procesos`.
- ⚠️ Con link de pago la veladora baja a 34.0% y los sets a 22–33%: pedir transferencia.
- ⚠️ No ofrecer "envío gratis": las piezas sueltas bajan a 2–28%.
- Recalcular si: la veladora tarda más de ~17 min, el papel picado tarda más de lo supuesto, o el colorante resulta ser por tanda (bajaría el costo).

---

## 8. Preguntas para Noemi (en orden de impacto)

1. **Moldes del cempasúchil:** ¿cuántos moldes tienes y puedes colar varios a la vez para sacar 6 por hora? Es lo que lleva el cempasúchil de 26% a 45% y el Set Ofrenda de 26% a 37%.
2. **Tiempos reales:** cronometra 5 veladoras con foto y 5 papeles picados de cada versión. $79 aguanta hasta ~17 min; el papel picado con nombre a $45 aguanta hasta ~17 min.
3. **Caja del Set Ofrenda:** ¿la caja kraft deja meter el papel picado de 26 × 19 sin doblarlo, y cuánto cuesta? (hoy está estimada en $10 con viruta).

Pendientes abiertos (menor impacto): precio real del laminado, la tinta y la bolsa de celofán; colorante por vela o por tanda; densidad del aroma; costo de paquetería y entrega local.

---

## Anexo: script del cálculo (reproducible, v4)

Copiar a un archivo `.py` y ejecutar con `python3`. Cambiar los valores de la parte de arriba cuando Noemi mande datos reales.

```python
# Costeo Dia de Muertos 2026 v4 - Ananda Velas (17-oct-2026, datos reales y decisiones finales de Noemi)
MO_H = 80.0; MERMA = 0.05
SOYA = 0.150; PARAF = 0.080                      # REAL $/g
AROMA = 50/30                                    # REAL $50 por 30 ml = $1.667/ml; densidad 1 g/ml: verificar
AROMA_G_CEMPA = 6.0                              # REAL: maximo 6 g por vela de cempasuchil
PABILO_CM = 25/300                               # REAL
COLOR_CEMPA = 1.25                               # REAL-tope: 1/4 de sobre de $5 (por vela o por tanda: preguntar)
VELADORA = 21.00                                 # REAL: veladora en vaso COMPRADA YA HECHA (vaso + cera + mecha)
ADH = 6.00; ETQ_POR_HOJA = 4                     # REAL: papel adhesivo $6/hoja, 4 etiquetas por hoja
OPALINA = 3.00                                   # REAL: opalina carta $3/hoja, blanca y de color (Noemi, 17-oct)
CELOFAN = 0.90; LISTON = 0.50                    # estimado
SOBRE_GRANDE = 1.20                              # estimado: sobre de celofan para papel picado 26x19 (verificar medida)
LAMINADO = 4.00; TINTA_ALTA = 2.50; TINTA_BAJA = 1.00; DESP = 1.10  # estimado
CUCHILLA = 0.50                                  # desgaste cuchilla+tapete por hoja, estimado
MIN_FOTO = 15                                    # veladora con foto: personalizar + empacar (estimado, cronometrar)
MIN_PP_GEN = 10; MIN_PP_PERS = 15                # papel picado grande: generico / personalizado (dato de trabajo)
PRECIO_CEMPA = 75; PRECIO_CEMPA_3 = 200          # CONFIRMADO por Noemi (17-oct)
PV_FOTO = 79                                     # CONFIRMADO por Noemi (17-oct)
PP_GEN, PP_PERS = 35, 45                         # precios sugeridos por Noemi (17-oct)
SET_RECUERDO, SET_OFRENDA = 119, 259             # recomendacion de costos
TAG = (OPALINA + TINTA_BAJA)/8*DESP
ETIQUETA = (ADH + TINTA_ALTA + LAMINADO)/ETQ_POR_HOJA*DESP
def mo(minutos): return MO_H*minutos/60
def costo(d): return round(sum(d.values())*(1+MERMA), 2)
def mg(p, c, com=0.0): return (p*(1-com) - c)/p*100

def cempa(vel_hora, bolsa):
    d = {'soya 53 g': 53*SOYA, 'parafina 53 g': 53*PARAF, 'aroma 6 g': AROMA_G_CEMPA*AROMA,
         'pabilo 9 cm': 9*PABILO_CM, 'colorante': COLOR_CEMPA, 'mano de obra': mo(60/vel_hora)}
    if bolsa: d.update({'celofan': CELOFAN, 'liston': LISTON, 'tag': TAG})
    else: d['sticker base'] = 0.40
    return d

def veladora(minutos=MIN_FOTO, bolsa=True):
    d = {'veladora comprada': VELADORA, 'etiqueta 1/4 hoja': ETIQUETA, 'sticker base': 0.40, 'mano de obra': mo(minutos)}
    if bolsa: d['bolsa + liston'] = 1.20 + LISTON
    return d

def picado_grande(personalizado):
    # 26x19 cm, opalina de color, 1 por hoja carta, solo corte en Cricut, sin tinta
    return {'opalina de color +10%': OPALINA*DESP, 'cuchilla': CUCHILLA, 'sobre grande': SOBRE_GRANDE,
            'mano de obra': mo(MIN_PP_PERS if personalizado else MIN_PP_GEN)}

def set_recuerdo():
    d = veladora(); d.update({f'pp {k}': v for k, v in picado_grande(True).items()}); return d

def set_ofrenda(vel_hora):
    d = veladora(bolsa=False); c = cempa(vel_hora, False); c.pop('sticker base')
    d.update({'2 cempasuchil': 2*sum(c.values()), 'caja kraft + viruta': 10.00, 'tag set': TAG})
    d.update({f'pp {k}': v for k, v in picado_grande(True).items()}); return d

if __name__ == '__main__':
    for v in (3, 6):
        for b in (False, True):
            c = costo(cempa(v, b))
            print(f'DM-4 {v}/h bolsa={b}: costo {c:.2f} | $75 {mg(75,c):.1f}% link {mg(75,c,0.0418):.1f}% emp {mg(75,c+15):.1f}% '
                  f'| 3x$200 {mg(200,3*c):.1f}% link {mg(200,3*c,0.0418):.1f}% emp {mg(200,3*c+15):.1f}% | min45 {c/0.55:.2f}')
    c = costo(veladora()); print(f'DM-1 costo {c:.2f} ${PV_FOTO}: {mg(PV_FOTO,c):.1f}% link {mg(PV_FOTO,c,0.0418):.1f}% emp {mg(PV_FOTO,c+15):.1f}%')
    print('== Papel picado grande 26x19 (opalina de color, solo corte) ==')
    for pers in (False, True):
        d = picado_grande(pers); c = costo(d); p = PP_PERS if pers else PP_GEN
        mat = sum(v for k, v in d.items() if k != 'mano de obra')
        print(f'{"personalizado 15 min" if pers else "generico 10 min"}: mat {mat:.2f} costo {c:.2f} min35 {c/0.65:.2f} min45 {c/0.55:.2f} '
              f'| ${p}: {mg(p,c):.1f}% link {mg(p,c,0.0418):.1f}% emp {mg(p,c+15):.1f}% | Pixe $30: {mg(30,c):.1f}% | Pixe mayoreo $25: {mg(25,c):.1f}%')
    sep_r = PV_FOTO + PP_PERS; sep_o = PV_FOTO + 2*PRECIO_CEMPA + PP_PERS
    print('por separado: Recuerdo', sep_r, 'Ofrenda', sep_o)
    c = costo(set_recuerdo())
    print(f'Set Recuerdo costo {c:.2f} min35 {c/0.65:.2f} ' + ' '.join(f'${p}: {mg(p,c):.1f}% link {mg(p,c,0.0418):.1f}% emp {mg(p,c+15):.1f}% |' for p in (109, 115, SET_RECUERDO)))
    for v in (3, 6):
        c = costo(set_ofrenda(v))
        print(f'Set Ofrenda {v}/h costo {c:.2f} min35 {c/0.65:.2f} ' + ' '.join(f'${p}: {mg(p,c):.1f}% link {mg(p,c,0.0418):.1f}% emp {mg(p,c+25):.1f}% |' for p in (SET_OFRENDA, 265)))
    gen = veladora(5, bolsa=False); c2 = cempa(3, False); c2.pop('sticker base')
    gen.update({'2 cempa': 2*sum(c2.values()), 'caja': 10.0, 'tag': TAG}); gen.update({f'pp {k}': v for k, v in picado_grande(False).items()})
    for n, c in [('Set Ofrenda 3/h', costo(set_ofrenda(3))), ('kit generico 3/h', costo(gen))]:
        for com, lab in [(0.174, 'ML Clasica'), (0.226, 'ML Premium')]:
            print(n, f'{c:.2f}', lab, 'margen @259/299/349', [round(mg(p, c + 105, com), 1) for p in (259, 299, 349)],
                  'min45', round((c + 105)/(1 - com - 0.45)))
```

Fuentes de referencia consultadas el 17-oct-2026 en la v1 (precios de terceros, **verificar**; la opalina y el papel adhesivo ya tienen precio real de Noemi): [Cyberpuerta, opalina Copamex 225 g 100 hojas](https://www.cyberpuerta.mx/Impresion-y-Copiado/Papeles-para-Impresoras/Papel-Opalina/Copamex-Papel-Opalina-225g-m-100-Hojas-de-Tamano-Carta-Blanco.html), [ML, paquetes de opalina](https://listado.mercadolibre.com.mx/paquete-de-100-hojas-de-opalina), [Walmart, papel adhesivo para inyección](https://www.walmart.com.mx/browse/oficina-y-papeleria/papeleria/papel/264672_264673_264677), [Cosmos, proveedores de vasos para veladora](https://www.cosmos.com.mx/producto/vasos-4jc7/vasos-para-veladoras-4szf/). Comisiones de ML: ver fuentes en `costos/margenes-por-canal.md`.
