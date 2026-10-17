# Costos y precios: Día de Muertos 2026 (DM-1 a DM-6)

Responsable: Producción y costos · `costos-precios`. **Versión 1: sáb 17-oct-2026** (tarea DM-c de `direccion/dia-de-muertos-2026.md`).
Fórmula y reglas: `costos/README.md` (margen bruto ≥ 45% en menudeo; ticket mínimo ML $299). Cálculo reproducible: script en el anexo al final de este archivo.

> **Qué es real y qué es estimado.** Solo la vela de cempasúchil (DM-4) tiene datos reales de Noemi (17-oct): gramos de cera, precio de soya, parafina, aroma y pabilo. Todo lo demás está marcado **estimado** y se recalcula en cuanto Noemi mande los datos de la sección 6. Los precios de venta de abajo están puestos para que **sigan dejando ≥ 45% aunque el aroma real sea el escenario caro (b)**.

---

## 0. Supuestos generales

| Concepto | Valor usado | Estatus |
|---|---|---|
| Mano de obra | $80/hora ($1.33/min), igual que `costos/calculo_costos.py` | Supuesto de la empresa |
| Merma | 5% sobre (materiales + mano de obra) | Regla README |
| Soya alto punto de fusión | $150/kg = $0.150/g | **REAL** (Noemi, 17-oct) |
| Parafina china | $80/kg = $0.080/g | **REAL** (Noemi, 17-oct). También se usa para la veladora en vaso |
| Aroma | Frasco 250 ml = $250 → **$1.00/ml ≈ $1.00/g** | Precio **REAL**; densidad 1 g/ml: **verificar** (los aceites de fragancia pesan ~0.9–1.05 g/ml); dosis por vela: **pregunta 1** |
| Pabilo | 3 m = $25 → $0.083/cm | **REAL** |
| Colorante | $0.015 por g de cera | **estimado** (`insumos-referencia.md`, SUNHUI) |
| Bolsa de celofán / listón de cierre | $0.90 / $0.50 | **estimado** (`insumos-referencia.md`); la medida de bolsa del cempasúchil: **verificar** |
| Opalina blanca 225 g, carta | $2.00/hoja | **estimado** con referencia: 100 hojas Copamex $151–155 en Cyberpuerta, $168–245 en ML (búsqueda del 17-oct, **verificar**) + envío |
| Papel adhesivo mate (o glossy), carta | $5.00/hoja | **estimado** (no se encontró precio carta mate en México; A4 glossy en Walmart salía a ~$15.70/hoja: **verificar** lo que pagó Noemi) |
| Laminado transparente en frío, carta | $4.00/hoja | **estimado** (ya comprado: falta el precio real) |
| Tinta Epson L3560 | $2.50/hoja con cobertura alta (etiqueta con foto o papel picado a color) · $1.00/hoja con cobertura baja (tag) | **estimado** (depende de la cobertura; se mide con el nivel de los tanques) |
| Reimpresiones | +10% de hojas (pruebas de color, cortes fallidos) | **estimado** (ver `diseno/tecnico/impresion-colores-vivos.md`: hoy todavía se están ajustando colores) |
| Desgaste de cuchilla y tapete Cricut | $0.50 por hoja de papel picado | **estimado** |
| Vaso de veladora (~6 cm, apto para calor) | $12.00 | **estimado** (no se encontró precio público; Cosmos solo da proveedores: **verificar**) |
| Cera del vaso | 130 g de parafina (vaso Ø int ~5.6 cm, llenado ~6 cm × 0.9 g/cm³) | **estimado**: medir con el método del agua (`produccion/formulas/punto-de-partida-soya.md`, sección 3) |
| Mecha de veladora + porta-pabilo | $1.50 | **estimado** (la que apruebe la prueba de mecha) |
| Sticker de advertencias en la base | $0.40 | **estimado** (regla 6 de CLAUDE.md: toda vela lleva aviso) |
| Caja kraft + viruta (Set Ofrenda) | $10.00 | **estimado** (igual que los kits navideños) |
| Empaque de envío por paquetería (caja + burbuja + relleno + cinta) | $15 una pieza · $25 un set | **estimado** |
| Pago | Transferencia o efectivo: 0% de comisión. Con link de pago o terminal: ~4.2% (3.6% + IVA, **verificar** con tu proveedor) | Se muestra el margen en ambos casos |
| Impuestos | Márgenes **antes** de ISR/IVA. Si Noemi factura con IVA trasladado, el margen baja ~13.8 puntos | Revisar con `finanzas-fiscal` |

### Tiempos de mano de obra (todos **estimados**; cronometrar los primeros 5 pedidos)

| Paso | Minutos | Aplica a |
|---|---|---|
| Atención + prueba digital (1 ronda de cambios) | 5 por pedido | DM-1, DM-2, DM-3, sets |
| Diseño con **foto** (recortar, ajustar, nombre) | 10 | DM-1 y sets con foto |
| Diseño con **nombre** en plantilla | 3 | DM-2, DM-3 |
| Adaptar el mismo nombre al papel picado del set | incluido en 9 min del papel picado del set | DM-5, DM-6 |
| Imprimir, laminar, cortar y pegar etiqueta en el vaso | 5 | Veladora |
| Hacer la veladora (vaciar, mecha, enfriar, recortar) | 4 (15 por hora) | Veladora |
| Cortar y desbarbar papel picado | 4 chico · 6 mediano | DM-3 |
| Vela de cempasúchil (vaciar, desmoldar, limpiar) | 6 (10 por hora) | DM-4 |
| Embolsar + tag + listón | 2 | DM-4 en bolsa, veladora |

---

## 1. DM-4 Vela de Cempasúchil (datos reales del 17-oct)

**Receta:** 106 g de cera por vela = 53 g de soya alto punto de fusión + 53 g de parafina china. Pabilo 9 cm.

**Aroma: dos escenarios (no está claro qué significa "50 gr de aroma").**
- **(a)** 50 g de aroma por kg de cera (≈ 5%) → 5.3 g por vela → **$5.30**.
- **(b)** 8% sobre el peso de la cera (punto de partida de `produccion/formulas/punto-de-partida-soya.md`) → 8.5 g por vela → **$8.48**.

Densidad del aroma 1 g/ml: **verificar** (pesar 10 ml del frasco en la báscula).

### Costeo unitario

| Concepto | Estatus | Sin bolsa (a) | Sin bolsa (b) | Con bolsa + tag (a) | Con bolsa + tag (b) |
|---|---|---|---|---|---|
| Soya 53 g × $0.150 | REAL | $7.95 | $7.95 | $7.95 | $7.95 |
| Parafina china 53 g × $0.080 | REAL | $4.24 | $4.24 | $4.24 | $4.24 |
| Aroma (a) 5.3 g / (b) 8.5 g × $1.00 | precio REAL, dosis **por confirmar** | $5.30 | $8.48 | $5.30 | $8.48 |
| Pabilo 9 cm | REAL | $0.75 | $0.75 | $0.75 | $0.75 |
| **Subtotal datos reales** | | **$18.24** | **$21.42** | **$18.24** | **$21.42** |
| Colorante (106 g × $0.015) | **estimado** | $1.59 | $1.59 | $1.59 | $1.59 |
| Sticker de advertencias en la base | **estimado** | $0.40 | $0.40 | — | — |
| Bolsa de celofán | **estimado** | — | — | $0.90 | $0.90 |
| Listón o cierre | **estimado** | — | — | $0.50 | $0.50 |
| Tag en opalina (8 por hoja, con aviso de seguridad) | **estimado** | — | — | $0.41 | $0.41 |
| Mano de obra (6 min sin bolsa · 8 min con bolsa) | **estimado** | $8.00 | $8.00 | $10.67 | $10.67 |
| Merma 5% | | $1.41 | $1.57 | $1.62 | $1.77 |
| **Costo unitario** | | **$29.64** | **$32.98** | **$33.93** | **$37.26** |
| Precio mínimo para 45% (venta directa, transferencia) | | $54 | $60 | $62 | $68 |

Lectura rápida: la cera y el pabilo cuestan **$12.94** por vela; el aroma es el dato que más mueve el costo después de la mano de obra (de $5.30 a $8.48). Sin bolsa solo se usa dentro del Set Ofrenda (la caja lleva el aviso de seguridad en el tag del set).

---

## 2. Costeo **estimado** de DM-1, DM-2, DM-3, DM-5 y DM-6

Aroma de la veladora con el escenario (b), 8%, para no quedarse corto. Con el escenario (a) la veladora cuesta ~$4 menos.

### DM-1 Veladora con foto y DM-2 Veladora papel picado

| Concepto | DM-1 foto | DM-2 papel picado | Estatus |
|---|---|---|---|
| Parafina 130 g × $0.080 | $10.40 | $10.40 | precio REAL, gramos **estimado** |
| Aroma 10.4 g (8%) × $1.00 | $10.40 | $10.40 | precio REAL, dosis **estimado** |
| Mecha + porta-pabilo | $1.50 | $1.50 | **estimado** |
| Vaso apto para calor | $12.00 | $12.00 | **estimado** |
| Etiqueta envolvente: ½ hoja de adhesivo + tinta + laminado, +10% reimpresión | $6.33 | $6.33 | **estimado** (2 etiquetas por hoja, plan v3) |
| Sticker de advertencias en la base | $0.40 | $0.40 | **estimado** |
| Bolsa de celofán + listón | $1.70 | $1.70 | **estimado** |
| Mano de obra | $34.67 (26 min) | $25.33 (19 min) | **estimado** |
| Merma 5% | $3.87 | $3.40 | |
| **Costo unitario** | **$81.26** | **$71.46** | |
| Precio mínimo 45% | $148 | $130 | |

La **versión mascota** (huellas) cuesta lo mismo que DM-1: lleva foto.

### DM-3 Papel picado personalizado (opalina 225 g)

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

### DM-5 Set Recuerdo y DM-6 Set Ofrenda

| Concepto | DM-5 con foto | DM-5 con nombre | DM-6 con foto | DM-6 con nombre |
|---|---|---|---|---|
| Veladora (materiales) | $42.73 | $42.73 | $41.03 (sin bolsa, va en caja) | $41.03 |
| Mano de obra veladora | $34.67 | $25.33 | $34.67 | $25.33 |
| Papel picado mediano, mismo nombre (materiales) | $5.45 | $5.45 | $5.45 | $5.45 |
| Mano de obra papel picado (9 min) | $12.00 | $12.00 | $12.00 | $12.00 |
| 2 velas de cempasúchil sin bolsa (escenario b, con su mano de obra) | — | — | $62.02 | $62.02 |
| Caja kraft + viruta + tag del set | — | — | $10.41 | $10.41 |
| Merma 5% | $4.74 | $4.28 | $8.28 | $7.81 |
| **Costo del set** | **$99.58** | **$89.79** | **$173.85** | **$164.05** |
| Precio mínimo 45% (directo) | $181 | $163 | $316 | $298 |

---

## 3. Precio sugerido por canal

### 3.1 Venta directa: WhatsApp, Instagram y Facebook

**Cómo se cobra:**
- **Entrega local:** el precio de la tabla, sin cargos extra (zona y costo de entrega local: los define Noemi).
- **Envío por paquetería: se cobra aparte** = costo real de la guía según el código postal **+ $25 de empaque** (caja, burbuja y relleno). No conviene absorberlo: con empaque absorbido el cempasúchil suelto baja a ~30% y el papel picado suelto a ~20% (columna de la derecha).
- **Pago:** transferencia o efectivo. Si se cobra con link de pago o terminal, el margen baja ~4 puntos (columna "con link").

| Producto | Costo | **Precio** | Margen (transferencia) | Margen con link de pago | Margen si absorbes el empaque de envío | Pasa 45% |
|---|---|---|---|---|---|---|
| DM-4 Cempasúchil, 1 pieza en bolsa con tag (aroma b) | $37.26 | **$75** | 50.3% | 46.1% | 30.3% | Sí |
| DM-4 Cempasúchil, 1 pieza (aroma a) | $33.93 | $75 | 54.8% | 50.6% | 34.8% | Sí |
| DM-4 Cempasúchil, 2 piezas (aroma b) | $74.52 | **$139** | 46.4% | 42.2% ⚠️ | 35.6% | Sí con transferencia |
| DM-1 Veladora con foto (o mascota) | $81.26 | **$199** | 59.2% | 55.0% | 51.6% | Sí |
| DM-2 Veladora papel picado con nombre | $71.46 | **$179** | 60.1% | 55.9% | 51.7% | Sí |
| DM-3 Papel picado chico 14 × 10 | $22.01 | **$45** | 51.1% | 46.9% | 17.8% | Sí (envío aparte) |
| DM-3 Papel picado mediano 19 × 14 | $27.67 | **$55** | 49.7% | 45.5% | 22.4% | Sí (envío aparte) |
| DM-3 mediano **agregado** a una veladora (mismo nombre) | $17.87 | **+$35** | 48.9% | 44.8% ⚠️ | — (va en el mismo paquete) | Sí con transferencia |
| DM-5 Set Recuerdo con nombre (DM-2 + mediano) | $89.79 | **$199** | 54.9% | 50.7% | 47.3% | Sí |
| DM-5 Set Recuerdo con foto (DM-1 + mediano) | $99.58 | **$219** | 54.5% | 50.3% | 47.7% | Sí |
| DM-6 Set Ofrenda (veladora con foto o nombre + 2 cempasúchil + papel picado mediano) | $164–$174 | **$349** | 50.2% (foto) · 53.0% (nombre) | 46.0% · 48.8% | 43.0% ⚠️ · 45.8% | Sí (envío aparte) |

Por qué estos precios:
- **Los sets ahorran $15–$24 frente a comprar por separado** (Set Recuerdo con foto: $199 + $35 = $234 → $219; Set Ofrenda: $199 + $139 + $35 = $373 → $349). Así el set es la compra lógica y sube el ticket.
- **Cempasúchil $75** en vez de $69: a $69 el escenario (b) queda en 46% y con link de pago baja a 42%. $75 deja margen para el aroma caro.
- **Veladora $199 / $179:** el mínimo para 45% es $148 / $130; el precio deja espacio para el tiempo de diseño real, que todavía no se ha cronometrado. Falta el precio de la competencia en veladora personalizada (tarea DM-e de Angélica): si la competencia anda en $150–$180, DM-1 puede bajar a $179 (54% de margen) sin problema; **no bajar de $149**.

### 3.2 Comparación contra la competencia del plan

| Producto | Ananda | Competencia | Lectura |
|---|---|---|---|
| Papel picado chico 14 × 10 | $45 | Pixé Design $10 ($8 por 12+) | 4.5 veces más caro. **No competimos suelto**: es para quien ya compra la veladora o el set |
| Papel picado mediano 19 × 14 | $55 suelto · **$35 agregado** | Pixé $22 ($18 por 12+); con rostro $26 | Agregado a la veladora queda en $35: más cerca, y con el mismo nombre que la vela |
| Papel picado con rostro | No se ofrece hasta cronometrarlo | Pixé $14–$35 | Con 20–30 min de dibujo de línea costaría $40–$55 solo de mano de obra |
| Veladora con foto | $199 | Singular, PassionRosa: precio no visible | **Dato pendiente (DM-e)**. Nuestro diferencial: vela hecha a mano con aroma |
| Vela de cempasúchil | $75 | Sin referencia en el plan | Pedir 3 precios de referencia a Angélica |

Conclusión: igual que el plan, **el valor está en la veladora y los sets**; el papel picado suelto se publica solo como "desde $45" y se empuja como agregado de $35.

### 3.3 Mercado Libre: DM-6 Set Ofrenda — **no publicar**

Supuestos (todos **verificar en el simulador de costos de la publicación**): ML Clásica 15% + IVA = 17.4% efectivo; Premium 19.5% + IVA = 22.6%; sin cargo fijo desde $299; envío gratis absorbido por el vendedor ≈ $80; empaque de envío $25.

| Escenario | Precio $299 | Precio $349 | Precio $499 | Precio mínimo para 45% |
|---|---|---|---|---|
| DM-6 con foto, ML Clásica | −10.7% ⚠️ | 2.7% ⚠️ | 26.7% ⚠️ | **$742** |
| DM-6 con foto, ML Premium | −15.9% ⚠️ | −2.5% ⚠️ | 21.5% ⚠️ | **$861** |
| Kit genérico sin personalizar (veladora papel picado genérica + 2 cempasúchil + papel picado genérico; costo $143), ML Clásica | −0.4% ⚠️ | 11.5% ⚠️ | 32.9% ⚠️ | **$660** |

**Decisión de costos: RECHAZADO para ML.** A $299 pierde dinero y para llegar a 45% tendría que costar $660–$860, fuera de mercado. Además, el último envío por paquetería es el sáb 24 y un pedido personalizado de ML exige pedir foto y nombre por mensajes, con riesgo de no llegar antes del 1-nov. Alternativa: vender el Set Ofrenda **solo por WhatsApp/IG/FB a $349**, y en ML quedarse con los kits navideños. Publicarlo con margen menor a 45% solo con aprobación escrita de Dirección (regla README).

---

## 4. Precios para los estados de WhatsApp (listos para copiar)

| Producto | Texto para el estado |
|---|---|
| Veladora con foto (DM-1) y versión mascota | **$199** |
| Veladora papel picado con nombre (DM-2) | **$179** |
| "Desde [precio]" (estado del sáb 17, 14:00) | **Desde $179** |
| Papel picado con nombre (DM-3) | **Desde $45** (chico $45 · mediano $55 · agrégalo a tu veladora por $35) |
| Vela de cempasúchil (DM-4) | **$75** · 2 por **$139** |
| Set Recuerdo (DM-5) | **Desde $199** (con nombre $199 · con foto $219) |
| Set Ofrenda (DM-6) | **$349** |
| Nota para todos | Envío por paquetería: se cobra aparte (guía + empaque). Pago 100% por adelantado en personalizados |

---

## 5. Validación rápida
- Ningún precio queda con margen negativo ni menor a 45% con pago por transferencia y envío cobrado aparte.
- ⚠️ Con link de pago, **2 cempasúchil ($139)** y **papel picado agregado ($35)** quedan en 42–45%. Si se cobra con link, sumar la comisión o pedir transferencia.
- ⚠️ No ofrecer "envío gratis" en ningún producto: el cempasúchil y el papel picado sueltos bajan a 18–35%.
- Si el aroma real es más de 8% o el vaso cuesta más de $18, recalcular antes del lunes 19.

---

## 6. Preguntas para Noemi (en orden de impacto)

1. **Aroma por vela:** cuando escribiste "50 gr de aroma", ¿es por cada kilo de cera, por cada tanda (¿de cuántos gramos?) o por cada vela? Y ¿cuántos gramos pesa 10 ml de tu aroma en la báscula? (con eso fijamos si el cempasúchil cuesta $33.93 o $37.26).
2. **Vaso de la veladora:** ¿cuánto pagaste por vaso (y cuántos venían), cuánto mide por dentro y cuántos gramos de cera le caben? (método del agua: gramos de agua hasta la línea de llenado).
3. **Papel y laminado:** precio y número de hojas del papel adhesivo mate/glossy, de la opalina de 225 g y del laminado que ya compraste.
4. **Tiempos reales:** cronometra la primera veladora con foto (diseño + prueba digital + imprimir + laminar + cortar + pegar) y el primer papel picado mediano (diseño + corte + desbarbar). ¿Cuántas velas de cempasúchil salen por colada y cuánto tardas por colada?
5. **Bolsa y colorante del cempasúchil:** ¿qué medida de bolsa de celofán le queda y cuánto te costó el paquete? ¿Qué colorante usas y cuánto rinde un frasco?
6. **Envío y entrega local:** ¿cuánto te cobra la paquetería que usas por un paquete chico (y ya tienes cajas y burbuja)? ¿Cobras la entrega local o es gratis, y en qué zona?

---

## Anexo: script del cálculo (reproducible)

Copiar a un archivo `.py` y ejecutar con `python3`. Cambiar los valores de la parte de arriba cuando Noemi mande los datos reales.

```python
# Costeo Dia de Muertos 2026 - Ananda Velas (17-oct-2026)
MO_H = 80.0; MERMA = 0.05
# precios ($/unidad)
SOYA = 0.150; PARAF = 0.080; AROMA = 1.00          # REAL Noemi (aroma: $250/250 ml, densidad 1 g/ml verificar)
PABILO_CM = 25/300                                  # REAL: 3 m $25
COLOR_G = 0.015                                     # estimado insumos-referencia
CELOFAN = 0.90; LISTON = 0.50                       # estimado insumos-referencia
OPALINA = 2.00; ADH_MATE = 5.00; LAMINADO = 4.00     # $/hoja carta, estimado
TINTA_ALTA = 2.50; TINTA_BAJA = 1.00                 # $/hoja, estimado
DESP = 1.10                                         # +10% hojas reimpresas / prueba
CUCHILLA = 0.50                                     # desgaste cuchilla+tapete por hoja papel picado, estimado
def mo(minutos): return MO_H*minutos/60

def total(d):
    sub = sum(d.values()); m = round(sub*MERMA,2)
    return sub, m, round(sub+m,2)

# DM-4 cempasuchil
def cempa(esc, bolsa):
    frag_g = 106*0.05 if esc=='a' else 106*0.08   # (a) 50 g/kg ; (b) 8%
    d = {'soya 53 g (REAL)': 53*SOYA, 'parafina 53 g (REAL)': 53*PARAF,
         f'aroma {frag_g:.1f} g (REAL $/ml, dosis ?)': frag_g*AROMA,
         'pabilo 9 cm (REAL)': 9*PABILO_CM, 'colorante (est.)': 106*COLOR_G}
    if bolsa:
        d['celofan (est.)']=CELOFAN; d['liston/cierre (est.)']=LISTON
        d['tag opalina 1/8 hoja (est.)']=(OPALINA+TINTA_BAJA)/8*DESP
        d['mano de obra 8 min (est.)']=mo(8)
    else:
        d['sticker advertencias base (est.)']=0.40
        d['mano de obra 6 min (est.)']=mo(6)
    return d

# Veladora en vaso (parafina 130 g estimado)
def veladora(foto, esc='b'):
    g=130; frag=g*(0.05 if esc=='a' else 0.08)
    d={'parafina 130 g (REAL $/kg, g est.)':g*PARAF, f'aroma {frag:.1f} g':frag*AROMA,
       'mecha + porta-pabilo (est.)':1.50,'vaso apto calor (est.)':12.00,
       'etiqueta 1/2 hoja adhesivo+tinta+laminado (est.)':(ADH_MATE+TINTA_ALTA+LAMINADO)/2*DESP,
       'sticker advertencias base (est.)':0.40,'bolsa celofan + liston (est.)':1.20+LISTON}
    mins = 5 + (10 if foto else 3) + 5 + 4 + 2   # atencion+prueba, diseno, imprimir/laminar/cortar/pegar, vela, empacar
    d[f'mano de obra {mins} min (est.)']=mo(mins)
    return d

def picado(tam, con_diseno=True):
    porhoja = 2 if tam=='chico' else 1
    d={'opalina+tinta alta (est.)':(OPALINA+TINTA_ALTA)/porhoja*DESP,'cuchilla/tapete (est.)':CUCHILLA/porhoja,
       'sobre celofan plano (est.)':CELOFAN}
    corte = 4 if tam=='chico' else 6
    mins = (5+3 if con_diseno else 1) + corte + 1
    d[f'mano de obra {mins} min (est.)']=mo(mins)
    return d

def suma(*ds):
    out={}
    for i,d in enumerate(ds):
        for k,v in d.items(): out[f'{i}:{k}']=v
    return out

prods = {
 'DM-4 sin bolsa (a)':cempa('a',False),'DM-4 sin bolsa (b)':cempa('b',False),
 'DM-4 con bolsa+tag (a)':cempa('a',True),'DM-4 con bolsa+tag (b)':cempa('b',True),
 'DM-1 foto (b)':veladora(True),'DM-1 foto (a)':veladora(True,'a'),'DM-2 papel picado (b)':veladora(False),
 'DM-3 chico':picado('chico'),'DM-3 mediano':picado('mediano'),
 'DM-3 mediano agregado':picado('mediano',False),
}
# Set Recuerdo: veladora foto + mediano mismo nombre (diseno compartido, empaque conjunto)
sr = veladora(True); sr.update({'papel picado mediano sin diseno':sum(v for k,v in picado('mediano',False).items() if 'mano' not in k)-CELOFAN,
     'mano de obra papel picado 9 min':mo(9)})
prods['DM-5 Set Recuerdo (foto)']=sr
srn = veladora(False); srn.update({'papel picado mediano sin diseno':sum(v for k,v in picado('mediano',False).items() if 'mano' not in k)-CELOFAN,
     'mano de obra papel picado 9 min':mo(9)})
prods['DM-5 Set Recuerdo (nombre)']=srn
# Set Ofrenda: veladora foto + 2 cempasuchil sin bolsa + mediano; caja kraft $10 en vez de bolsas
so = veladora(True); so.pop('bolsa celofan + liston (est.)')
c = cempa('b',False); c.pop('sticker advertencias base (est.)')
so.update({'2 cempasuchil (b) sin bolsa':2*sum(c.values()),
           'papel picado mediano sin diseno':sum(v for k,v in picado('mediano',False).items() if 'mano' not in k)-CELOFAN,
           'mano de obra papel picado 9 min':mo(9),'caja kraft + viruta (est.)':10.0,'tag set opalina (est.)':(OPALINA+TINTA_BAJA)/8*DESP})
prods['DM-6 Set Ofrenda (foto, b)']=so

COST={}
for n,d in prods.items():
    sub,m,t=total(d); COST[n]=t
    print(f'\n## {n}')
    for k,v in d.items(): print(f'  {k:55s} {v:7.2f}')
    print(f'  subtotal {sub:.2f}  merma {m:.2f}  COSTO {t:.2f}  precio min 45% directo {t/0.55:.2f}')

EMP_1=15.0; EMP_SET=25.0  # empaque de envio (caja+burbuja+relleno) estimado
def mg(p,c,extra=0,com=0.0): return (p*(1-com)-c-extra)/p*100
print('\n=== PRECIOS DIRECTOS ===')
for n,p,emp in [('DM-4 con bolsa+tag (b)',69,EMP_1),('DM-4 con bolsa+tag (a)',69,EMP_1),('DM-4 sin bolsa (b)',59,EMP_1),
                ('DM-1 foto (b)',199,EMP_1),('DM-1 foto (a)',199,EMP_1),('DM-2 papel picado (b)',179,EMP_1),
                ('DM-3 chico',35,0),('DM-3 mediano',49,0),('DM-3 mediano agregado',29,0),
                ('DM-5 Set Recuerdo (foto)',229,EMP_1),('DM-5 Set Recuerdo (nombre)',229,EMP_1),('DM-6 Set Ofrenda (foto, b)',329,EMP_SET)]:
    c=COST[n]
    print(f'{n:32s} costo {c:7.2f} precio {p} margen local {mg(p,c):5.1f}%  paqueteria(empaque absorbido {emp}) {mg(p,c,emp):5.1f}%  link pago 4.2% {mg(p,c,0,0.0418):5.1f}%')
print('\n=== ML DM-6 ===')
c=COST['DM-6 Set Ofrenda (foto, b)']
for com,lab in [(0.174,'Clasica 15%+IVA'),(0.226,'Premium 19.5%+IVA')]:
    for env in (80,120):
        pmin=(c+EMP_SET+env)/(1-com-0.45)
        for p in (299,329,449):
            print(f'{lab} envio {env}: precio {p} margen {mg(p,c,EMP_SET+env,com):5.1f}%', end=' | ')
        print(f'  precio min 45% = {pmin:.0f}')

print('\n=== FINALES ===')
c = cempa('b',False); c.pop('sticker advertencias base (est.)')
# DM-6 version nombre
son = veladora(False); son.pop('bolsa celofan + liston (est.)')
son.update({'2 cempa':2*sum(c.values()),'pp':sum(v for k,v in picado('mediano',False).items() if 'mano' not in k)-CELOFAN,
            'mo pp':mo(9),'caja':10.0,'tag':(OPALINA+TINTA_BAJA)/8*DESP})
COST['DM-6 nombre']=total(son)[2]
print('DM-6 nombre costo', COST['DM-6 nombre'])
dos = 2*COST['DM-4 con bolsa+tag (b)']; dosa=2*COST['DM-4 con bolsa+tag (a)']
COST['DM-4 x2 (b)']=dos; COST['DM-4 x2 (a)']=dosa
F=[('DM-4 con bolsa+tag (b)',75),('DM-4 con bolsa+tag (a)',75),('DM-4 x2 (b)',139),('DM-4 x2 (a)',139),
   ('DM-1 foto (b)',199),('DM-1 foto (a)',199),('DM-2 papel picado (b)',179),
   ('DM-3 chico',45),('DM-3 mediano',55),('DM-3 mediano agregado',35),
   ('DM-5 Set Recuerdo (foto)',219),('DM-5 Set Recuerdo (nombre)',199),
   ('DM-6 Set Ofrenda (foto, b)',349),('DM-6 nombre',349)]
for n,p in F:
    c=COST[n]; print(f'| {n} | ${c:.2f} | ${p} | {mg(p,c):.1f}% | {mg(p,c,0,0.0418):.1f}% | {mg(p,c,EMP_SET if "DM-6" in n else EMP_1):.1f}% | ${c/0.55:.0f} |')
# ML kit generico sin personalizar
gen = {'velad mat':10.4+10.4+1.5+12+6.33+0.4,'mo vel 9min':mo(9),'2 cempa':2*sum(v for k,v in cempa('b',False).items() if 'sticker' not in k),'pp generico':5.45,'mo pp 4min':mo(4),'caja':10,'tag':0.41}
cg=total(gen)[2]; print('kit generico costo',cg)
for n,cc in [('DM-6 foto',COST['DM-6 Set Ofrenda (foto, b)']),('generico',cg)]:
    for com in (0.174,0.226):
        for env in (80,):
            print(n,com,env,'min45',round((cc+EMP_SET+env)/(1-com-0.45)), 'margen@299',round(mg(299,cc,EMP_SET+env,com),1),'@349',round(mg(349,cc,EMP_SET+env,com),1),'@499',round(mg(499,cc,EMP_SET+env,com),1))
```

Fuentes de referencia consultadas el 17-oct-2026 (precios de terceros, **verificar**): [Cyberpuerta, opalina Copamex 225 g 100 hojas](https://www.cyberpuerta.mx/Impresion-y-Copiado/Papeles-para-Impresoras/Papel-Opalina/Copamex-Papel-Opalina-225g-m-100-Hojas-de-Tamano-Carta-Blanco.html), [ML, paquetes de opalina](https://listado.mercadolibre.com.mx/paquete-de-100-hojas-de-opalina), [Walmart, papel adhesivo para inyección](https://www.walmart.com.mx/browse/oficina-y-papeleria/papeleria/papel/264672_264673_264677), [Cosmos, proveedores de vasos para veladora](https://www.cosmos.com.mx/producto/vasos-4jc7/vasos-para-veladoras-4szf/). Comisiones de ML: ver fuentes en `costos/margenes-por-canal.md`.
