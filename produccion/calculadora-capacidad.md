# Calculadora de capacidad de producción

**Objetivo:** saber cuántas velas por día y por mes puede fabricar Ananda Velas, qué paso nos frena (cuello de botella) y qué comprar o contratar para acercarnos a la meta.

**Datos de entrada:** `produccion/cuestionario-capacidad.md` (los contesta Noemi). Mientras no estén, la capacidad real es **desconocida** y ningún canal debe prometer volúmenes grandes (regla 4 de `CLAUDE.md`).

---

## 1. ¿De dónde sale la meta de 2,600 velas/mes?

Viene de `negocio/plan-90-dias.md` (sección 1):

| Meta | Ticket promedio por pedido | Pedidos/mes | Velas/mes |
|---|---|---|---|
| $50,000 | $350 | 143 | ~650 |
| $100,000 | $400 | 250 | ~1,300 |
| $200,000 | $450 | 445 | ~2,600 |

- 2,600 velas ÷ 445 pedidos ≈ **5.8 velas por pedido** (kits y mayoreo).
- $200,000 ÷ 2,600 velas ≈ **$77 de ingreso promedio por vela**.
- Por día: 2,600 ÷ 26 días hábiles ≈ **100 velas/día**; si solo produces 5 días a la semana (≈22 días), son ≈ **118 velas/día**.

> Si la mezcla real vende más mayoreo (precios más bajos por pieza), el ingreso por vela baja y se necesitan **más** de 2,600 velas para llegar a $200k. Recalcular con los pedidos reales cada mes.

---

## 2. Las cuatro restricciones

Cada vela pasa por cuatro "embudos". La capacidad real es la del **más angosto**.

| # | Restricción | Qué la limita |
|---|---|---|
| A | **Moldes** (o lugares en la mesa, en soya) | Cuántos moldes tienes y cuántas veces al día los puedes reusar (ciclos), según el enfriado |
| B | **Derretido** | Kg por tanda y tandas por día |
| C | **Mano de obra** | Minutos de trabajo por vela (vertido + desmolde + pintado + etiqueta + empaque) contra horas disponibles |
| D | **Curado y espacio** | No baja las velas/día, pero define cuántos días de anticipación necesitas y cuántas velas deben caber guardadas |

---

## 3. Fórmulas paso a paso

### Paso A — Capacidad por moldes (por figura)

```
Velas por colada        = moldes × cavidades por molde
Ciclo de molde (h)      = enfriado hasta desmoldar (h) + desmolde y re-preparación (h)
Ciclos por día          = PISO( horas de vertido disponibles ÷ ciclo de molde ) + 1 si la última colada se deja enfriar de noche
Capacidad moldes/día    = velas por colada × ciclos por día
```

- "PISO" = redondear hacia abajo (no hay medio ciclo).
- Soya en contenedor: en lugar de moldes usa "contenedores que caben en la mesa de enfriado" y "tandas por día".

### Paso B — Capacidad de derretido

```
Velas por tanda de cera = (kg por tanda × 1,000) ÷ gramos por vela
Tandas por día          = PISO( horas de derretido disponibles ÷ (derretir + temperar en h) ) × número de ollas
Capacidad derretido/día = velas por tanda × tandas por día
```

Normalmente no es el cuello de botella, pero revísalo: cambiar de aroma o de cera (parafina ↔ soya) obliga a otra tanda.

### Paso C — Capacidad de mano de obra

```
Minutos por vela        = vertido + desmolde/rebaba + pintado + moño/detalle + etiqueta + empaque
                          (vertido por molde ÷ velas por molde; Cricut por hoja ÷ etiquetas por hoja)
Minutos disponibles/día = horas de producción de Noemi × 60 + horas de ayudantes × 60
Capacidad mano de obra  = minutos disponibles ÷ minutos por vela        (si solo hicieras esa figura)
```

Para una **mezcla** de figuras en el mismo día:

```
Minutos necesarios = Σ (velas de cada figura × minutos por vela de esa figura)
La mezcla cabe si:  minutos necesarios ≤ minutos disponibles
                    y  velas de cada figura ≤ su capacidad de moldes (Paso A)
```

> Cuenta solo las horas de **producción**. Las horas de mensajes, fotos, lives y envíos no son horas de producción.

### Paso D — Curado y espacio

```
Velas en curado al mismo tiempo = velas por día × días de curado
Anticipación mínima de un pedido = días de fabricación + días de curado + días de empaque y envío
```

Si el espacio de curado no alcanza para "velas por día × días de curado", el espacio se vuelve el cuello de botella.

### Paso E — Capacidad real y mensual

```
Capacidad real/día (por figura) = MÍNIMO( A, B, C )
Velas buenas/día                = capacidad real × (1 − % de merma)
Velas/mes                       = velas buenas/día × días de producción al mes
Brecha                          = 2,600 − velas/mes
```

El **cuello de botella** es la restricción que dio el número más bajo. Mejorar cualquier otra no aumenta la producción.

---

## 4. EJEMPLO HIPOTÉTICO (números inventados, NO son datos de Ananda)

> Solo sirve para ver cómo se usan las fórmulas. Reemplazar con las respuestas del cuestionario.

**Supuestos inventados:**

| Dato | Borrego | Árbol hojas | Glowing Glass (soya) |
|---|---|---|---|
| Moldes / lugares | 6 moldes × 1 cavidad | 4 moldes × 1 cavidad | 24 frascos por tanda |
| Enfriado hasta desmoldar | 2 h | 3 h | 3 h (hasta poder mover) |
| Desmolde y re-preparación | 15 min | 15 min | — |
| Gramos por vela | 80 g | 120 g | 150 g |
| Minutos por vela (vertido 1 + desmolde 1 + pintado + etiqueta/empaque 2) | 1+1+5+2 = **9 min** | 1+1+3+2 = **7 min** | prep. 1 + vertido 0.5 + etiqueta/tapa 1.5 = **3 min** |
| Merma | 5% | 5% | 5% |

Otros supuestos: Noemi produce **6 h/día** (360 min), **24 días al mes**; ventana de vertido 8 h; 1 olla de 5 kg que tarda 1 h en derretir y temperar.

**Paso A — moldes**
- Borrego: ciclo = 2 + 0.25 = 2.25 h → PISO(8 ÷ 2.25) = 3, + 1 nocturno = **4 ciclos** → 6 × 4 = **24 borregos/día**.
- Árbol: ciclo = 3.25 h → PISO(8 ÷ 3.25) = 2, + 1 nocturno = **3 ciclos** → 4 × 3 = **12 árboles/día**.
- Glowing Glass: ciclo 3 h → 2 tandas en el día = **48 frascos/día**.

**Paso B — derretido:** 8 tandas × 5 kg = 40 kg/día. Borrego: 5,000 ÷ 80 = 62 por tanda. No limita.

**Paso C — mano de obra (si hiciera solo una figura):**
- Borrego: 360 ÷ 9 = 40/día · Árbol: 360 ÷ 7 = 51/día · Glowing Glass: 360 ÷ 3 = 120/día.

**Capacidad real por figura (MÍNIMO):** Borrego 24 (manda el **molde**) · Árbol 12 (manda el **molde**) · Glowing Glass 48 (manda la **mesa/tandas**).

**Mezcla de un día típico:**

| Figura | Velas | Min/vela | Minutos | ¿Cabe en moldes? |
|---|---|---|---|---|
| Borrego | 20 | 9 | 180 | 20 ≤ 24 sí |
| Árbol | 10 | 7 | 70 | 10 ≤ 12 sí |
| Glowing Glass | 30 | 3 | 90 | 30 ≤ 48 sí |
| **Total** | **60** | — | **340 de 360** | |

- Velas buenas/día = 60 × 0.95 = **57**. Velas/mes = 57 × 24 = **1,368**.
- **Brecha contra 2,600 = 1,232 velas/mes** (≈ 51 velas/día más). Con la mezcla del día, el cuello de botella es la **mano de obra** (340 de 360 min usados); moldes de borrego y árbol están cerca del tope.
- Curado (supuesto soya 7 días): 30 frascos/día × 7 = 210 frascos curando al mismo tiempo → hay que tener ese espacio.

**¿Qué haría falta para 2,600 con esta mezcla?** 2,600 ÷ 24 días ÷ 0.95 ≈ **114 velas/día** (1.9 veces la mezcla).
- Borrego 38/día → moldes necesarios = 38 ÷ (1 × 4 ciclos) = 9.5 → **10 moldes (comprar 4)**.
- Árbol 19/día → 19 ÷ 3 = 6.3 → **7 moldes (comprar 3)**.
- Glowing Glass 57/día → 3 tandas de 24 en la mesa (o una mesa más grande).
- Mano de obra: 340 min × 1.9 ≈ 646 min/día = 10.8 h → Noemi 6 h + **≈ 5 h/día de ayudante** (≈ 30 h/semana).

---

## 5. Si no alcanza la meta: qué hacer (en este orden)

1. **Identifica el cuello de botella** con la tabla de la sección 6. Solo invierte en esa restricción.
2. **Si el cuello es el molde → compra moldes duplicados** de los best sellers (borrego, árbol, pino, venado según `plan-90-dias.md`):
   ```
   Moldes necesarios = velas/día objetivo de esa figura ÷ (cavidades por molde × ciclos por día)
   Moldes a comprar  = moldes necesarios (redondeado hacia arriba) − moldes que ya tienes
   ```
   Verifica antes que haya mano de obra para pintarlas: más moldes sin manos solo acumula velas sin terminar.
3. **Si el cuello es el enfriado → más ciclos:** colada nocturna, área fresca o ventilador (no meter la cera caliente al refrigerador sin probar: puede agrietar; probar primero con 2 piezas).
4. **Si el cuello es la mano de obra → ayudante.** Delegar en este orden (de lo más fácil a lo más difícil):
   1. Empaque y armado de cajitas / bolsas de celofán y organza.
   2. Etiquetado y despegado de etiquetas de Cricut.
   3. Desmolde y limpieza de rebaba.
   4. Pintado sencillo: puntas blancas de pino/árbol, base verde del rompecabezas, moño del venado.
   5. Pintado fino (caras, ojos, borrego, Santa) — solo después de entrenar y aprobar muestras.
   ```
   Horas de ayudante/semana = (velas/semana objetivo × minutos por vela promedio − minutos de Noemi/semana) ÷ 60
   ```
5. **Producción por lotes:** un aroma y una figura por tanda; pintar todas las piezas de un mismo paso juntas (todas las puntas blancas, luego todos los ojos). Reduce minutos por vela.
6. **Prioriza SKUs por margen por minuto** (no por precio):
   ```
   Margen por minuto = (precio neto después de comisión y envío − costo unitario) ÷ minutos de mano de obra por vela
   ```
   El precio neto y el costo salen de `costos/README.md` y `costos/plantilla-costeo.csv` (si un costo no está capturado, el resultado es **estimado**). En temporada alta, empuja en ventas los SKUs con más margen por minuto y menos pintado (por ejemplo, soya en contenedor) y limita los que consumen más pintado (Rompecabezas, Borregos 12 pzs) con cupo semanal.
7. **Si aun así no alcanza:** la meta se ajusta a la capacidad, no al revés. Avisar a Dirección (`negocio/plan-90-dias.md`) y poner cupo por canal y fecha de corte de pedidos.

---

## 6. Tabla para llenar (una fila por figura)

Días de producción al mes: ____ · Minutos de producción disponibles por día (Noemi + ayuda): ____ · % merma: ____

| Figura | Moldes × cavidades | Ciclo de molde (h) | Ciclos/día | A. Cap. moldes/día | Gramos/vela | B. Cap. derretido/día | Min/vela | C. Cap. mano de obra/día | Real/día = MÍN(A,B,C) | Cuello de botella | Días curado | Velas/mes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oso | | | | | | | | | | | | |
| Jirafa | | | | | | | | | | | | |
| Elefante | | | | | | | | | | | | |
| Dino | | | | | | | | | | | | |
| Ángel | | | | | | | | | | | | |
| Peonía | | | | | | | | | | | | |
| Conejo | | | | | | | | | | | | |
| Venado | | | | | | | | | | | | |
| Nacimiento | | | | | | | | | | | | |
| Pino | | | | | | | | | | | | |
| Árbol hojas | | | | | | | | | | | | |
| Borrego | | | | | | | | | | | | |
| Rompecabezas (juego) | | | | | | | | | | | | |
| Glowing Glass | | | | | | | | | | | | |
| Lume Soja Mini | | | | | | | | | | | | |
| Lume Soja | | | | | | | | | | | | |
| Paquete Recuerdos | | | | | | | | | | | | |

### Mezcla planeada de la semana

| Figura | Velas/día planeadas | Min/vela | Minutos/día | ¿≤ cap. moldes? |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| **Total** | | — | **≤ minutos disponibles** | |

### Resultado

| Concepto | Valor |
|---|---|
| Velas buenas por día (mezcla) | |
| Velas por mes | |
| Meta | 2,600 |
| Brecha (meta − velas/mes) | |
| Cuello de botella principal | |
| Acción: moldes a comprar (figura y cantidad) | |
| Acción: horas de ayudante por semana | |
| Anticipación mínima para pedidos de mayoreo (días) | |

> Actualizar esta tabla cada vez que se compren moldes, entre una ayudante o cambien los tiempos. El resultado se copia a la tabla de moldes de `negocio/catalogo.md`.
