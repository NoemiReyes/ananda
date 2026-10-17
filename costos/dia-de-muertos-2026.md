# Costos y precios: Día de Muertos 2026 (DM-1 a DM-6)

Responsable: Producción y costos · `costos-precios`. **Versión 3: sáb 17-oct-2026, noche** (tarea DM-c de `direccion/dia-de-muertos-2026.md`). Reemplaza las versiones 1 y 2 del mismo día.
Fórmula y reglas: `costos/README.md` (margen bruto ≥ 45% en menudeo). Cálculo reproducible: script en el anexo al final de este archivo.

> **Decisiones y datos reales de Noemi (17-oct) incluidos en la v3**
> - **Cempasúchil:** aroma 6 g a $50/30 ml, colorante ¼ de sobre de $5, **3 velas por hora**. Precio vigente **$75 la pieza y 3 por $200** (decisión de Noemi), **por confirmar**: Noemi escribió después "$47". A $75 y 3 velas por hora deja 26% y 17%; **a $47 sería negativo** (sección 1).
> - **Veladoras DM-1/DM-2:** se **compran ya hechas a $21** (vaso, cera y mecha); papel adhesivo $6/hoja con 4 etiquetas. La mano de obra es solo personalizar y empacar. **Decisión final: DM-1 con foto a $79.**
> - **Excepción de margen:** Noemi fija **35% como objetivo en las veladoras DM-1 y DM-2, solo esta temporada** (la regla general sigue en 45%). Referencia que dio: veladoras chicas sin personalizar a ~$50.
> - **Papel picado DM-3:** opalina **$3 por hoja (real)**. Precios propuestos a 35%: chico $25, mediano $35, agregado a una veladora $29 (sección 3).

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
| Opalina blanca 225 g, carta | **$3.00/hoja** | **REAL** (Noemi, 17-oct). Reemplaza el estimado de $2 |
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
| **Margen objetivo** | **45%** en todo (README) · **excepción: 35% en veladoras DM-1 y DM-2 (y papel picado DM-3, según los precios propuestos), solo temporada Día de Muertos 2026** | **Decisión de Noemi (17-oct)**. Referencia que dio: veladoras más chicas sin personalizar a ~$50 en el mercado (**verificar** con 3 precios) |
| Impuestos | Márgenes **antes** de ISR/IVA. Si Noemi factura con IVA trasladado, el margen baja ~13.8 puntos | Revisar con `finanzas-fiscal` |

### Tiempos de mano de obra

| Paso | Minutos | Estatus |
|---|---|---|
| **Vela de cempasúchil (vaciar, desmoldar y empacar)** | **20 (3 por hora por persona)** · escenario 10 (6 por hora, colada en varios moldes a la vez) | **REAL** (Noemi, 17-oct) · el de 6/h es escenario |
| **Veladora comprada: solo personalizar y empacar** (atención + prueba digital, diseño, imprimir, laminar, cortar, pegar etiqueta, embolsar) | **DM-1 con foto: 15 min · DM-2 con nombre: 10 min** (supuesto de trabajo con plantillas de Canva y por lotes) · pieza por pieza sin plantilla: ~22 min | **estimado**: cronometrar los primeros 5 pedidos |
| Papel picado DM-3 (cambiar el nombre en la plantilla + corte + retirar recortes) | **5 o 10 min** (se calculan los dos); en sets y agregado se usa 5 min porque el nombre ya está capturado | estimado: cronometrar |

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
| Bolsa de celofán $0.90 + listón $0.50 + tag en opalina $0.55 | bolsa y listón estimado; opalina REAL | — | $1.95 | — | $1.95 |
| **Mano de obra** (20 min a 3/h · 10 min a 6/h) | REAL (3/h) · escenario (6/h) | **$26.67** | **$26.67** | $13.33 | $13.33 |
| Merma 5% | | $2.56 | $2.64 | $1.90 | $1.97 |
| **Costo unitario** | | **$53.82** | **$55.45** | **$39.82** | **$41.45** |
| Peso de la mano de obra en el costo | | 52% | 51% | 35% | 34% |
| Precio mínimo para 45% | | $98 | $101 | $73 | $76 |

**Lectura:**
- **La mano de obra domina el costo: $26.67 de $55.45 (51%).** Todos los insumos juntos suman $24.19; el aroma ($10.00) es el insumo más caro.
- **Colada en varios moldes a la vez (6 por hora)** baja el costo $14 por vela. Es la palanca más grande de todo Día de Muertos. Cada molde extra se paga con unas 20 velas (precio del molde: **verificar**).

### Precio del cempasúchil: **$75 la pieza y 3 por $200** (decisión de Noemi; **por confirmar**)

Noemi escribió después "$47". **No se cambia hasta que confirme**; se deja $75 / 3 por $200. 3 por $200 = $66.67 por vela.

| Precio | Productividad | Empaque | Costo | Margen transferencia | Con link de pago | Si absorbes empaque de envío ($15) | ¿Llega a 45%? |
|---|---|---|---|---|---|---|---|
| $75 (1 pieza) | 3 por hora | sin bolsa | $53.82 | **28.2%** | 24.1% | 8.2% | **NO ⚠️** |
| $75 (1 pieza) | 3 por hora | con bolsa + tag | $55.45 | **26.1%** | 21.9% | 6.1% | **NO ⚠️** |
| $75 (1 pieza) | 6 por hora | sin bolsa | $39.82 | 46.9% | 42.7% ⚠️ | 26.9% ⚠️ | Sí (solo con transferencia) |
| $75 (1 pieza) | 6 por hora | con bolsa + tag | $41.45 | **44.7%** | 40.6% | 24.7% | **NO ⚠️** (por 0.3 puntos) |
| 3 por $200 | 3 por hora | sin bolsa | $161.46 | **19.3%** | 15.1% | 11.8% | **NO ⚠️** |
| 3 por $200 | 3 por hora | con bolsa + tag | $166.35 | **16.8%** | 12.6% | 9.3% | **NO ⚠️** |
| 3 por $200 | 6 por hora | sin bolsa | $119.46 | **40.3%** | 36.1% | 32.8% | **NO ⚠️** |
| 3 por $200 | 6 por hora | con bolsa + tag | $124.35 | **37.8%** | 33.6% | 30.3% | **NO ⚠️** |

> ⚠️ **Nota sobre "$47":** a $47 por pieza el margen sería **NEGATIVO a 3 velas por hora: −18.0% en bolsa (pierdes $8.45 por vela) y −14.5% sin bolsa**. A 6 por hora quedaría en 11.8% (bolsa) / 15.3% (sin bolsa): positivo pero muy abajo de 35% y 45%. Costos **rechaza $47** (regla 3 de CLAUDE.md: nunca vender con margen negativo).

**Lectura de costos (para Dirección):**
- A 3 velas por hora, $75 deja 26% y 3 por $200 deja 17%: margen positivo, pero abajo de 45% (y de 35%). Precios que sí llegarían a 45%: 1 pieza $101 (3/h) o $76 (6/h); 3 piezas $302 (3/h) o $226 (6/h).
- Para que $75 funcione, **pasar a 6 por hora es obligatorio**, no opcional.
- Vender abajo de 45% requiere **aprobación escrita de Dirección**: dejar registrada la decisión de Noemi en `direccion/`.
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

**Decisión final de Noemi: DM-1 a $79.** Recomendación de costos para DM-2: **$69**. Cumplen el 35% de Noemi con 15 y 10 min. Condición: **cronometrar los primeros 5 pedidos**. Si DM-1 pasa de ~17 min o DM-2 pasa de ~12 min, el margen cae abajo de 35% (DM-1 a 22 min deja 25.7%); en ese caso subir a DM-1 $89 / DM-2 $79. Comparado con la referencia de ~$50 por una veladora chica sin personalizar, $69–$79 cobra $19–$29 por la personalización.

---

## 3. DM-3 Papel picado personalizado (opalina 225 g, $3 por hoja REAL)

Caben **2 chicos (14 × 10 cm)** o **1 mediano (19 × 14 cm)** por hoja carta en el área de Imprimir y cortar (17.1 × 23.5 cm). Mano de obra: cambiar el nombre en la plantilla + corte + retirar recortes, calculada con **5 y 10 min** a $80/h.

| Concepto | Chico (2 por hoja) | Mediano (1 por hoja) | Mediano agregado a una veladora | Estatus |
|---|---|---|---|---|
| Opalina | $1.50 | $3.00 | $3.00 | **REAL** |
| Tinta cobertura alta | $1.25 | $2.50 | $2.50 | estimado |
| +10% reimpresión (papel + tinta) | $0.28 | $0.55 | $0.55 | estimado |
| Cuchilla y tapete | $0.25 | $0.50 | $0.50 | estimado |
| Sobre de celofán plano | $0.90 | $0.90 | $0.90 | estimado |
| **Materiales** | **$4.18** | **$7.45** | **$7.45** | |
| Costo con 5 min ($6.67 + merma 5%) | **$11.38** | **$14.82** | **$14.82** | |
| Costo con 10 min ($13.33 + merma 5%) | **$18.38** | **$21.82** | **$21.82** | |
| Precio mínimo 35% (5 min · 10 min) | $18 · $28 | $23 · $34 | $23 · $34 | |
| Precio mínimo 45% (5 min · 10 min) | $21 · $33 | $27 · $40 | $27 · $40 | |

### Precios propuestos (35%) y comparación con Pixé Design

| Producto | Precio | Margen con 5 min | Margen con 10 min | Pasa 35% hasta… | Pixé Design | Margen nuestro al precio de Pixé (5 min · 10 min) |
|---|---|---|---|---|---|---|
| **Chico 14 × 10** | **$25** | 54.5% | **26.5% ⚠️** | ~8.5 min | $10 | **−13.8% · −83.8%** (pérdida) |
| **Mediano 19 × 14** | **$35** | 57.7% | 37.7% | ~10.5 min | $22 | 32.6% · 0.8% |
| **Mediano agregado a una veladora** | **$29** | 48.9% | **24.8% ⚠️** | ~8 min | — | — |
| Agregado a $25 (alternativa) | $25 | 40.7% | **12.7% ⚠️** | ~6 min | — | — |

**Confirmación de los precios propuestos:**
- **Mediano $35: confirmado** con 5 y con 10 min (57.7% / 37.7%).
- **Chico $25 y agregado $29: confirmados solo si el corte toma ≤8 min.** Con 10 min caen a 26.5% y 24.8%. El agregado se calcula con 5 min porque el nombre ya está en la plantilla de la veladora: ahí deja 48.9%.
- **Agregado a $25:** con 5 min deja 40.7% (sí pasa 35%); con 10 min deja 12.7%. La cifra de "~27%" que traía la propuesta corresponde a ~8–9 min; con nuestros supuestos depende totalmente del tiempo. Mantener **$29**.
- **Pixé:** el chico a $10 nos hace perder dinero aunque se haga en 5 min (el material solo cuesta $4.18). No competimos en precio suelto; el papel picado se vende como complemento de la veladora y en sets.

---

## 4. Sets DM-5 y DM-6 (recalculados)

Precios por separado: DM-1 $79 · DM-2 $69 · papel picado agregado $29 · cempasúchil $75 (por confirmar). Papel picado del set con 5 min (mismo nombre de la veladora).

### Costeo

| Concepto | DM-5 foto | DM-5 nombre | DM-6 foto · 3/h | DM-6 nombre · 3/h | DM-6 foto · 6/h | DM-6 nombre · 6/h |
|---|---|---|---|---|---|---|
| Veladora comprada + etiqueta + sticker (+ bolsa en DM-5) | $26.54 | $26.54 | $24.84 (sin bolsa, va en caja) | $24.84 | $24.84 | $24.84 |
| Mano de obra veladora (15 min foto · 10 min nombre) | $20.00 | $13.33 | $20.00 | $13.33 | $20.00 | $13.33 |
| Papel picado mediano (opalina $3 + tinta + cuchilla, sin sobre) | $6.55 | $6.55 | $6.55 | $6.55 | $6.55 | $6.55 |
| Mano de obra papel picado (5 min) | $6.67 | $6.67 | $6.67 | $6.67 | $6.67 | $6.67 |
| 2 velas de cempasúchil sin bolsa (con su mano de obra) | — | — | $101.72 | $101.72 | $75.05 | $75.05 |
| Caja kraft + viruta + tag del set | — | — | $10.55 | $10.55 | $10.55 | $10.55 |
| Merma 5% | $2.98 | $2.65 | $8.50 | $8.17 | $7.17 | $6.84 |
| **Costo del set** | **$62.74** | **$55.74** | **$178.83** | **$171.83** | **$150.83** | **$143.83** |
| Precio mínimo 35% | $97 | $86 | $275 | $264 | $232 | $221 |

### Precio

| Set | Por separado | Precio del set | Ahorro | Margen transferencia | Con link | Si absorbes empaque | Decisión |
|---|---|---|---|---|---|---|---|
| **DM-5 Set Recuerdo con foto** | $79 + $29 = $108 | **$99** | $9 | **36.6%** | 32.4% ⚠️ | 21.5% ⚠️ | **Recomendado** |
| **DM-5 Set Recuerdo con nombre** | $69 + $29 = $98 | **$89** | $9 | **37.4%** | 33.2% ⚠️ | 20.5% ⚠️ | **Recomendado** |
| DM-5 con ahorro de $15 ($93 / $83) | $108 / $98 | $93 / $83 | $15 | 32.5% / 32.8% ⚠️ | 28.4% / 28.7% | 16.4% / 14.8% | Abajo de 35% (positivo) |
| **DM-6 Set Ofrenda con foto** | $79 + 2 × $75 + $29 = $258 | **$249** | $9 | **28.2% ⚠️ (3/h)** · 39.4% (6/h) | 24.0% · 35.2% | 18.1% · 29.4% | Recomendado; pasa 35% solo a 6/h |
| **DM-6 Set Ofrenda con nombre** | $69 + 2 × $75 + $29 = $248 | **$239** | $9 | **28.1% ⚠️ (3/h)** · 39.8% (6/h) | 23.9% · 35.6% | 17.6% · 29.4% | Recomendado; pasa 35% solo a 6/h |
| DM-6 con ahorro de $15 ($243 / $233) | $258 / $248 | $243 / $233 | $15 | 26.4% / 26.3% (3/h) · 37.9% / 38.3% (6/h) | | | Número poco redondo; 3/h abajo de 35% |

**Lectura:**
- Con el papel picado agregado a $29, **todos los sets quedan $9 más baratos** que por separado y en números redondos ($99 / $89 / $249 / $239). Con ahorro de $15 el Set Recuerdo baja a 32%, abajo del 35% de Noemi.
- **Set Ofrenda:** pasa 35% **solo si el cempasúchil se hace a 6 por hora**; a 3 por hora deja 28% (positivo). A 3 por hora no hay precio que pase 35% y siga siendo más barato que las piezas sueltas ($275 > $258).
- **Si el cempasúchil baja a $47:** por separado el Set Ofrenda sumaría $202 / $192 y el set tendría que costar menos que eso, **por debajo de su costo de $172–$179 a 3/h: margen negativo**. Recalcular el set en cuanto Noemi confirme el precio.
- Ningún set llega al 45% del README; el 35% de la excepción se está aplicando a los sets (pregunta 3).
- Cobrar los sets **solo por transferencia o efectivo** y **envío aparte**.

---

## 5. Mercado Libre: DM-6 Set Ofrenda, **sigue sin publicarse**

Supuestos (todos **verificar en el simulador de costos de la publicación**): ML Clásica 15% + IVA = 17.4% efectivo; Premium 19.5% + IVA = 22.6%; cargo fijo abajo de $299 (no incluido, empeora el resultado); envío ≈ $80; empaque de envío $25.

| Escenario | Precio $249 | Precio $299 | Precio $349 | Precio mínimo para 45% |
|---|---|---|---|---|
| DM-6 con foto (3/h, costo $178.83), ML Clásica | −31.4% ⚠️ | −12.3% ⚠️ | 1.3% ⚠️ | **$755** |
| DM-6 con foto (3/h), ML Premium | −36.6% ⚠️ | −17.5% ⚠️ | −3.9% ⚠️ | **$876** |
| Kit genérico sin personalizar (costo $163.43), ML Clásica | −25.2% ⚠️ | −7.2% ⚠️ | 5.7% ⚠️ | **$714** |

**Decisión de costos: RECHAZADO para ML** (pierde dinero a $249–$299). Vender el Set Ofrenda **solo por WhatsApp/IG/FB**.

---

## 6. Precios para los estados de WhatsApp (listos para copiar)

Margen con pago por transferencia/efectivo y envío por paquetería cobrado aparte. Veladoras con 15 min (foto) y 10 min (nombre); papel picado con 5 min; cempasúchil a 3 velas por hora (real) y 6 por hora (escenario).

| Producto | Texto para el estado | Costo | Margen | Objetivo | ¿Cumple? |
|---|---|---|---|---|---|
| Veladora con foto (DM-1) y versión mascota | **$79** (decisión final de Noemi) | $48.86 | 38.2% | 35% (decisión de Noemi) | Sí |
| Veladora papel picado con nombre (DM-2) | **$69** | $41.86 | 39.3% | 35% | Sí |
| "Desde [precio]" (estado del sáb 17, 14:00) | **Desde $69** | — | — | — | — |
| Papel picado con nombre (DM-3) | **Desde $25** (chico $25 · mediano $35 · agrégalo a tu veladora por $29) | $11.38 · $14.82 · $14.82 | 54.5% · 57.7% · 48.9% (con 10 min: 26.5% ⚠️ · 37.7% · 24.8% ⚠️) | 35% | Sí con ≤8 min |
| Vela de cempasúchil (DM-4), en bolsa con tag | **$75** · **3 por $200** (**por confirmar**; a $47 sería margen negativo) | $55.45 (3/h) · $41.45 (6/h) | **26.1% · 16.8% ⚠️ (3/h)** · 44.7% · 37.8% (6/h) | 45% | **No** (decisión de Noemi) |
| Set Recuerdo (DM-5) | **Desde $89** (con nombre $89 · con foto $99) | $55.74 · $62.74 | 37.4% · 36.6% | 35% | Sí |
| Set Ofrenda (DM-6) | **Desde $239** (con nombre $239 · con foto $249) | $171.83 · $178.83 (3/h) · $143.83 · $150.83 (6/h) | **28.1% · 28.2% ⚠️ (3/h)** · 39.8% · 39.4% (6/h) | 35% | Solo a 6/h |
| Nota para todos | Envío por paquetería: se cobra aparte (guía + empaque). Pago 100% por adelantado en personalizados. Pago por transferencia o efectivo | | | | |

**No publicar el cempasúchil ni el Set Ofrenda hasta que Noemi confirme el precio del cempasúchil** ($75 o $47).

---

## 7. Validación rápida
- **Ningún precio vigente tiene margen negativo** (el más bajo: cempasúchil 3 por $200 a 3/h, 16.8%). **$47 por cempasúchil: rechazado, margen negativo a 3/h (−18.0%).**
- Cumplen la excepción de 35%: DM-1 $79 (15 min), DM-2 $69 (10 min), papel picado $25 / $35 / $29 (con ≤8 min), Set Recuerdo $99 / $89.
- ⚠️ **Abajo del objetivo por decisión de Noemi:** cempasúchil $75 (26.1% a 3/h) y 3 por $200 (16.8% a 3/h). Set Ofrenda $249 / $239: 28% a 3/h, 39–40% a 6/h.
- ⚠️ La excepción de 35% es **solo para Día de Muertos 2026** (decisión de Noemi, 17-oct). No usar estos precios para Navidad ni mayoreo. Anotar en `direccion/` y avisar a `documentador-procesos`.
- ⚠️ Con link de pago, DM-1 baja a 34.0% y los sets a 24–35%: pedir transferencia.
- ⚠️ No ofrecer "envío gratis": las piezas sueltas bajan a 6–28%.
- Recalcular si: la personalización tarda más de 15 min (foto) / 10 min (nombre), el papel picado tarda más de 8 min, el colorante resulta ser por tanda, o cambia el precio del cempasúchil.

---

## 8. Preguntas para Noemi (en orden de impacto)

1. **Precio del cempasúchil:** ¿se queda en $75 / 3 por $200 o es $47? A $47 pierdes $8.45 por vela con 3 velas por hora. Y ¿puedes colar en varios moldes para sacar 6 por hora? (eso sube el Set Ofrenda de 28% a 39%).
2. **Tiempos reales:** cronometra 5 veladoras con foto, 5 con nombre y 5 papeles picados (cambiar nombre + corte + retirar recortes). Los precios aguantan hasta ~17 min (foto), ~12 min (nombre) y ~8 min (papel picado chico o agregado).
3. **Sets:** ¿aceptas ahorro de $9 ($99 / $89 / $249 / $239) para quedar arriba de 35%, o prefieres ahorro de $15 con 32% en el Set Recuerdo?

Pendientes abiertos (menor impacto): precio real del laminado, la tinta y la bolsa de celofán; colorante por vela o por tanda; densidad del aroma; costo de paquetería y entrega local.

---

## Anexo: script del cálculo (reproducible, v3)

Copiar a un archivo `.py` y ejecutar con `python3`. Cambiar los valores de la parte de arriba cuando Noemi mande datos reales.

```python
# Costeo Dia de Muertos 2026 v3 - Ananda Velas (17-oct-2026, datos reales y decisiones de Noemi)
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
# OPALINA $3/hoja: REAL (Noemi, 17-oct)
OPALINA = 3.00; LAMINADO = 4.00; TINTA_ALTA = 2.50; TINTA_BAJA = 1.00; DESP = 1.10  # estimado
TAG = (OPALINA + TINTA_BAJA)/8*DESP
ETIQUETA = (ADH + TINTA_ALTA + LAMINADO)/ETQ_POR_HOJA*DESP   # $3.44
PP_MAT = (OPALINA + TINTA_ALTA)*DESP + 0.50      # papel picado mediano sin sobre (materiales)
CUCHILLA = 0.50                                  # desgaste cuchilla+tapete por hoja, estimado
MIN_PP_SET = 5                                   # papel picado con el mismo nombre de la veladora: cambiar nombre + corte + retirar recortes

def picado(por_hoja, minutos, sobre=True):
    d = {'opalina + tinta alta +10%': (OPALINA + TINTA_ALTA)/por_hoja*DESP, 'cuchilla': CUCHILLA/por_hoja,
         'mano de obra': mo(minutos)}
    if sobre: d['sobre celofan'] = CELOFAN
    return d
PRECIO_CEMPA = 75; PRECIO_CEMPA_3 = 200          # decision de Noemi; POR CONFIRMAR (escribio $47)
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
    d = veladora(min_vel); d['papel picado mat'] = PP_MAT; d['mo papel picado'] = mo(MIN_PP_SET); return d

def set_ofrenda(min_vel, vel_hora):
    d = veladora(min_vel, bolsa=False); c = cempa(vel_hora, False); c.pop('sticker base')
    d.update({'2 cempasuchil': 2*sum(c.values()), 'papel picado mat': PP_MAT, 'mo papel picado': mo(MIN_PP_SET),
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
    PV1, PV2, PP_AGR = 79, 69, 29
    F = [('DM-1 foto 15 min', costo(veladora(15)), PV1, 15), ('DM-1 foto 10 min', costo(veladora(10)), PV1, 15),
         ('DM-1 foto 22 min (sin lotes)', costo(veladora(22)), PV1, 15),
         ('DM-2 nombre 10 min', costo(veladora(10)), PV2, 15), ('DM-2 nombre 15 min', costo(veladora(15)), PV2, 15),
         ('DM-4 en bolsa 3/h a $47 (no confirmado)', costo(cempa(3, True)), 47, 15),
         ('DM-4 en bolsa 3/h', costo(cempa(3, True)), PRECIO_CEMPA, 15), ('DM-4 3x200 en bolsa 3/h', 3*costo(cempa(3, True)), PRECIO_CEMPA_3, 15),
         ('DM-4 en bolsa 6/h', costo(cempa(6, True)), PRECIO_CEMPA, 15), ('DM-4 3x200 en bolsa 6/h', 3*costo(cempa(6, True)), PRECIO_CEMPA_3, 15)]
    for m in (5, 10):
        F += [(f'DM-3 chico {m} min', costo(picado(2, m)), 25, 0), (f'DM-3 chico {m} min vs Pixe', costo(picado(2, m)), 10, 0),
              (f'DM-3 mediano {m} min', costo(picado(1, m)), 35, 0), (f'DM-3 mediano {m} min vs Pixe', costo(picado(1, m)), 22, 0),
              (f'DM-3 agregado {m} min', costo(picado(1, m)), PP_AGR, 0), (f'DM-3 agregado {m} min a $25', costo(picado(1, m)), 25, 0)]
    sep5f, sep5n = PV1 + PP_AGR, PV2 + PP_AGR
    sep6f, sep6n = PV1 + 2*PRECIO_CEMPA + PP_AGR, PV2 + 2*PRECIO_CEMPA + PP_AGR
    print('por separado: DM-5 foto', sep5f, 'nombre', sep5n, '| DM-6 foto', sep6f, 'nombre', sep6n)
    F += [('DM-5 foto', costo(set_recuerdo(MIN_FOTO)), sep5f - 9, 15), ('DM-5 nombre', costo(set_recuerdo(MIN_NOMBRE)), sep5n - 9, 15)]
    for v in (3, 6):
        F += [(f'DM-6 foto {v}/h', costo(set_ofrenda(MIN_FOTO, v)), sep6f - 9, 25),
              (f'DM-6 nombre {v}/h', costo(set_ofrenda(MIN_NOMBRE, v)), sep6n - 9, 25)]
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
