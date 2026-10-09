# Márgenes por canal — Ananda Velas

> **TODO ES ESTIMADO.** Costos calculados con precios de referencia de internet (oct-2026) y supuestos de gramaje y productividad, NO con compras reales de Noemi. Comisiones de ML/TikTok tomadas de fuentes de terceros: **verificar** en el simulador de costos de Mercado Libre y en TikTok Seller Center antes de publicar. Se regenera con `python3 costos/calculo_costos.py`.

## Supuestos

| Concepto | Supuesto | Estatus |
|---|---|---|
| ML Clásica | 15% (Hogar; rango 8–16%) + IVA sobre comisión = 17.4% efectivo. Cargo fijo: $25 (<$99), $30 ($99–148), $37 ($149–298), $0 desde $299 | verificar (Tiendanube 19-mar-2026, calcforlife) |
| ML Premium | 19.5% (rango 12.5–20.5%) + IVA = 22.6% efectivo. Mismo cargo fijo | verificar |
| TikTok Shop | 6% comisión (incluye impuestos) + 2% procesamiento = 8%. Vendedores nuevos: 0% comisión 60 días (no considerado) | verificar (Tiendanube 10-abr-2026; otra fuente dice 10% Hogar) |
| Tienda propia | Pasarela 3.6% + $3 + IVA = 4.18% + $3.48 por venta. Plan mensual NO incluido (es costo fijo) | verificar |
| Mayoreo | 0% comisión, transferencia; envío lo paga cliente o entrega local | — |
| Envío | Tickets < $299: lo paga el comprador ($0 para el vendedor). Tickets ≥ $299: envío gratis absorbido por vendedor: ML $80 (parte del vendedor, paquete < 1 kg), TikTok $80, tienda propia $120 (guía de paquetería) | verificar (ML dio envío gratis desde $99 para Meli+ en abr-2026: confirmar si cobra al vendedor en tickets < $299) |
| Impuestos | Margen ANTES de ISR/IVA. Retenciones de plataforma (ISR 2.5% con RFC, mayor sin RFC) son pagos a cuenta, no costo. Si Noemi debe trasladar IVA, el neto real baja ~13.8%: revisar con `finanzas-fiscal` | verificar |
| Margen | margen $ = precio − comisión − cargo fijo − envío − costo unitario; margen % = margen $ ÷ precio. Mínimos: 45% menudeo, 35% mayoreo | regla README |

Fuentes de comisiones (terceros, no oficiales; consultadas 09-oct-2026): [Tiendanube ML México (act. 19-mar-2026)](https://www.tiendanube.com/mx/blog/comision-mercado-libre-mexico/), [calcforlife calculadora ML](https://calcforlife.com/es/calculadora-mercado-libre-comisiones/), [Tiendanube TikTok Shop (act. 10-abr-2026)](https://www.tiendanube.com/blog/tiktok-shop), [ecomcalctools TikTok LATAM 2026](https://ecomcalctools.com/es/blog/tiktok-shop-fees-latam-2026/). La ayuda oficial de ML no se pudo consultar (bloqueo 403): **verificar en el simulador de la publicación**.

EV-PRE se evalúa a $115; con la promo de octubre ($95) el margen directo baja a ~50% y en ML Clásica a ~6%.

Costo unitario: cera + fragancia (8% del peso) + colorante + mecha + contenedor/base/pintura + etiqueta + empaque + mano de obra ($80/h) + merma 5%. Detalle en `costos/plantilla-costeo.csv`.

## Hallazgos y recomendaciones (resumen)

> Basado en costos ESTIMADOS. Repetir en cuanto Noemi capture precios reales de compra, gramos reales (pesar 3 piezas de cada molde) y velas/hora.

1. **Mercado Libre, pieza suelta: no es viable a precio de catálogo.** Cargo fijo de $25–37 + 17.4% de comisión deja margen negativo o < 30% en todas las piezas. Para 45% la pieza suelta tendría que costar entre ~$130 (Nacimiento, Jirafa) y ~$250 (Glowing Glass): ver columna "Precio mín. 45%" de la sección 2. **No publicar piezas sueltas a precio de catálogo en ML.**
2. **Kits en ML (≥ $299) tampoco llegan a 45% al precio de catálogo × N**, porque al pasar de $299 el vendedor absorbe envío (supuesto $80) además de la comisión. Para 45% el kit necesita ~2.6 × (costo del kit + envío). Los que mejor salen son los de mayor margen unitario: **Nacimiento x6, Árbol x4, Pino x4, Paquete Recuerdos x4** (30–40% en TikTok, 20–30% en ML). Propuesta para el agente `mercadolibre`: armar kits navideños mixtos y publicarlos al precio mínimo de la sección 3, o tomar ML como canal de visibilidad con margen menor **solo con aprobación de Dirección** (regla README = 45%). Verificar el costo real de envío del vendedor en el simulador de ML: es la variable que más mueve el resultado.
3. **TikTok Shop y tienda propia (cliente paga envío) funcionan** para la mayoría de piezas. Ajustes mínimos de menudeo sugeridos para llegar a 45%: **Oso $87 → $108**, **Elefante $57 → $72**, **Dino $57 → $66**, **Lume Soja $88 → $96**, **Lume Mini $52 → $69**, **Glowing Glass $74 → $119** (o cambiar frasco). Si se ofrece envío gratis, el ticket mínimo sube mucho (sección 2, ver Rompecabezas).
4. **EV-GLO Glowing Glass es el producto más débil** (margen directo 25%; mayoreo 7–16%). El frasco con tapa dorada (~$18 estimado) + 126 g de soya + fragancia ya suman ~$50. Opciones: (a) cotizar frasco ≤ $10 por caja de 100+, (b) llenar menos (≈100 g), (c) subir mayoreo a **≥ $86** y menudeo a ≥ $102 (venta directa).
5. **NV-B12 Borregos de la Abundancia ($385) pierde dinero en todos los canales de marketplace** y deja solo ~18% en venta directa: 12 borregos pintados cuestan ~$314 (mano de obra ~$138 + 12 × fragancia/pintura/mecha). Opciones: (a) subir a **≥ $572** en venta directa; (b) **versión de 6 borregos a ≥ $296** directo (≈ $299); (c) borregos más chicos o sin pintar a mano por pieza (pintar más rápido: con 12/h el costo baja a ~$266 y el mínimo directo a $484). **Rechazado al precio actual.**
6. **NV-ROM Rompecabezas ($375)** deja 64% en venta directa, pero con envío gratis cae a 25–35%. Venderlo con envío pagado por el cliente, o subir a **≥ $456 en TikTok / $507 en tienda propia** si se incluye envío; en ML Clásica ≥ $570.
7. **Mayoreo bajo 35%:** Oso (51–99 y 100–150 → **$78**), Elefante (51–99 y 100–150 → **$51**), Dino (100–150 → **$47**), Lume Mini (todos los niveles → **$48**), Glowing Glass (todos → **$86**). El resto del mayoreo pasa (Navidad y Jirafa/Ángel/Flowers/Bunny con 45–70%).
8. **La fragancia es el insumo que más pesa** (8% del peso a ~$0.90/g): comprar fragancia en frascos de 30–60 ml la sube a ~$2.19/g y hunde los márgenes (escenario pesimista, sección 6). Prioridad de compra: fragancia a granel (1 kg o más) con proveedor de velas, y parafina en presentación de 10–25 kg.
9. **Impuestos no incluidos.** Si Noemi factura con IVA trasladado, todos los márgenes bajan ~13.8 puntos sobre el precio. Revisar con `finanzas-fiscal` antes de fijar precios finales.

## 1. Costo unitario estimado y margen en venta directa

| SKU | Producto | Cera g (supuesto) | Velas/h | Costo unitario | Menudeo | Margen directo |
|---|---|---|---|---|---|---|
| EV-OSO | Oso de Ternura | 188 g (10x9.5 cm, fondo 5.5, llenado 40%) | 10.00 | $50.34 | $87.00 | ⚠️ 42.1% |
| EV-JIR | Jirafa Africana | 39 g (9x4 cm, fondo 3, llenado 40%) | 12.00 | $18.90 | $45.00 | 58.0% |
| EV-ELE | Elefante Safari | 108 g (7x9.5 cm, fondo 4.5, llenado 40%) | 12.00 | $32.82 | $57.00 | ⚠️ 42.4% |
| EV-DIN | Dino T-Rex | 94 g (9.3x8 cm, fondo 4, llenado 35%) | 12.00 | $29.99 | $57.00 | 47.4% |
| EV-ANG | Ángeles Divinos | 60 g (6x7 cm, fondo 3.5, llenado 45%) | 12.00 | $23.14 | $57.00 | 59.4% |
| EV-FLO | Flowers On | 95 g (peonía Ø8 x 3.5 cm, llenado 60%) | 10.00 | $31.59 | $77.00 | 59.0% |
| EV-BUN | Bunny Happy | 126 g (10x7 cm, fondo 5, llenado 40%) | 10.00 | $37.84 | $87.00 | 56.5% |
| EV-GLO | Glowing Glass | 126 g (frasco Ø int 6.1, llenado a 4.8 cm) | 15.00 | $55.80 | $74.00 | ⚠️ 24.6% |
| EV-LMM | Lume Soja Mini | 43 g (lata Ø int 5.8, llenado a 1.8 cm) | 15.00 | $31.10 | $52.00 | ⚠️ 40.2% |
| EV-LMS | Lume Soja | 95 g (lata Ø int 5.8, llenado a 4.0 cm) | 15.00 | $44.73 | $88.00 | 49.2% |
| EV-PRE | Paquete Recuerdos | 43 g (vela = Lume Mini (43 g) + 2 jabones 25 g) | 8.00 | $47.39 | $115.00 | 58.8% |
| NV-VEN | Venado | 103 g (9.5x7.5 cm, fondo 4, llenado 40%) | 10.00 | $33.73 | $78.00 | 56.8% |
| NV-NAC | Nacimiento | 38 g (6.2x4.5 cm, fondo 3, llenado 50%) | 12.00 | $18.70 | $65.00 | 71.2% |
| NV-PIN | Pino | 98 g (cono 10 x Ø7.2, llenado 80%) | 10.00 | $32.67 | $87.00 | 62.4% |
| NV-ARB | Árbol Navideño | 50 g (cono 10 x Ø5, llenado 85%) | 12.00 | $21.59 | $85.00 | 74.6% |
| NV-BOR | Borrego | 46 g (6.5x4.5 cm, fondo 3.5, llenado 50%) | 8.00 | $25.39 | $57.00 | 55.5% |
| NV-B12 | Borregos de la Abundancia 12 pzs | 552 g (12 borregos x 46 g) | 0.58 | $314.09 | $385.00 | ⚠️ 18.4% |
| NV-ROM | Rompecabezas Navideño | 361 g (4 piezas, Ø6.5 x 22 cm, llenado 55%) | 2.00 | $134.15 | $375.00 | 64.2% |

## 2. Pieza suelta por canal (precio menudeo)

| SKU | Canal | Precio | Comisión % | Cargo fijo | Envío | Neto | Margen $ | Margen % | Precio mín. 45% |
|---|---|---|---|---|---|---|---|---|---|
| EV-OSO | ML Clásica | $87.00 | 17.4% | $25.00 | $0.00 | $46.86 | $-3.48 | ⚠️ -4.0% | $233.00 |
| EV-OSO | ML Premium | $87.00 | 22.6% | $25.00 | $0.00 | $42.32 | $-8.02 | ⚠️ -9.2% | $270.00 |
| EV-OSO | TikTok Shop | $87.00 | 8.0% | $0.00 | $0.00 | $80.04 | $29.70 | ⚠️ 34.1% | $108.00 |
| EV-OSO | Tienda propia | $87.00 | 4.2% | $3.48 | $0.00 | $79.89 | $29.54 | ⚠️ 34.0% | $106.00 |
| EV-JIR | ML Clásica | $45.00 | 17.4% | $25.00 | $0.00 | $12.17 | $-6.73 | ⚠️ -15.0% | $131.00 |
| EV-JIR | ML Premium | $45.00 | 22.6% | $25.00 | $0.00 | $9.82 | $-9.08 | ⚠️ -20.2% | $173.00 |
| EV-JIR | TikTok Shop | $45.00 | 8.0% | $0.00 | $0.00 | $41.40 | $22.50 | 50.0% | $41.00 |
| EV-JIR | Tienda propia | $45.00 | 4.2% | $3.48 | $0.00 | $39.64 | $20.74 | 46.1% | $45.00 |
| EV-ELE | ML Clásica | $57.00 | 17.4% | $25.00 | $0.00 | $22.08 | $-10.73 | ⚠️ -18.8% | $186.00 |
| EV-ELE | ML Premium | $57.00 | 22.6% | $25.00 | $0.00 | $19.11 | $-13.71 | ⚠️ -24.1% | $216.00 |
| EV-ELE | TikTok Shop | $57.00 | 8.0% | $0.00 | $0.00 | $52.44 | $19.62 | ⚠️ 34.4% | $70.00 |
| EV-ELE | Tienda propia | $57.00 | 4.2% | $3.48 | $0.00 | $51.14 | $18.32 | ⚠️ 32.1% | $72.00 |
| EV-DIN | ML Clásica | $57.00 | 17.4% | $25.00 | $0.00 | $22.08 | $-7.91 | ⚠️ -13.9% | $179.00 |
| EV-DIN | ML Premium | $57.00 | 22.6% | $25.00 | $0.00 | $19.11 | $-10.89 | ⚠️ -19.1% | $207.00 |
| EV-DIN | TikTok Shop | $57.00 | 8.0% | $0.00 | $0.00 | $52.44 | $22.45 | ⚠️ 39.4% | $64.00 |
| EV-DIN | Tienda propia | $57.00 | 4.2% | $3.48 | $0.00 | $51.14 | $21.15 | ⚠️ 37.1% | $66.00 |
| EV-ANG | ML Clásica | $57.00 | 17.4% | $25.00 | $0.00 | $22.08 | $-1.06 | ⚠️ -1.9% | $142.00 |
| EV-ANG | ML Premium | $57.00 | 22.6% | $25.00 | $0.00 | $19.11 | $-4.03 | ⚠️ -7.1% | $186.00 |
| EV-ANG | TikTok Shop | $57.00 | 8.0% | $0.00 | $0.00 | $52.44 | $29.30 | 51.4% | $50.00 |
| EV-ANG | Tienda propia | $57.00 | 4.2% | $3.48 | $0.00 | $51.14 | $28.00 | 49.1% | $53.00 |
| EV-FLO | ML Clásica | $77.00 | 17.4% | $25.00 | $0.00 | $38.60 | $7.01 | ⚠️ 9.1% | $183.00 |
| EV-FLO | ML Premium | $77.00 | 22.6% | $25.00 | $0.00 | $34.58 | $2.99 | ⚠️ 3.9% | $212.00 |
| EV-FLO | TikTok Shop | $77.00 | 8.0% | $0.00 | $0.00 | $70.84 | $39.25 | 51.0% | $68.00 |
| EV-FLO | Tienda propia | $77.00 | 4.2% | $3.48 | $0.00 | $70.30 | $38.71 | 50.3% | $70.00 |
| EV-BUN | ML Clásica | $87.00 | 17.4% | $25.00 | $0.00 | $46.86 | $9.02 | ⚠️ 10.4% | $200.00 |
| EV-BUN | ML Premium | $87.00 | 22.6% | $25.00 | $0.00 | $42.32 | $4.48 | ⚠️ 5.1% | $232.00 |
| EV-BUN | TikTok Shop | $87.00 | 8.0% | $0.00 | $0.00 | $80.04 | $42.20 | 48.5% | $81.00 |
| EV-BUN | Tienda propia | $87.00 | 4.2% | $3.48 | $0.00 | $79.89 | $42.04 | 48.3% | $82.00 |
| EV-GLO | ML Clásica | $74.00 | 17.4% | $25.00 | $0.00 | $36.12 | $-19.68 | ⚠️ -26.6% | $247.00 |
| EV-GLO | ML Premium | $74.00 | 22.6% | $25.00 | $0.00 | $32.26 | $-23.54 | ⚠️ -31.8% | $287.00 |
| EV-GLO | TikTok Shop | $74.00 | 8.0% | $0.00 | $0.00 | $68.08 | $12.28 | ⚠️ 16.6% | $119.00 |
| EV-GLO | Tienda propia | $74.00 | 4.2% | $3.48 | $0.00 | $67.43 | $11.63 | ⚠️ 15.7% | $117.00 |
| EV-LMM | ML Clásica | $52.00 | 17.4% | $25.00 | $0.00 | $17.95 | $-13.14 | ⚠️ -25.3% | $182.00 |
| EV-LMM | ML Premium | $52.00 | 22.6% | $25.00 | $0.00 | $15.24 | $-15.86 | ⚠️ -30.5% | $211.00 |
| EV-LMM | TikTok Shop | $52.00 | 8.0% | $0.00 | $0.00 | $47.84 | $16.74 | ⚠️ 32.2% | $67.00 |
| EV-LMM | Tienda propia | $52.00 | 4.2% | $3.48 | $0.00 | $46.35 | $15.25 | ⚠️ 29.3% | $69.00 |
| EV-LMS | ML Clásica | $88.00 | 17.4% | $25.00 | $0.00 | $47.69 | $2.96 | ⚠️ 3.4% | $218.00 |
| EV-LMS | ML Premium | $88.00 | 22.6% | $25.00 | $0.00 | $43.09 | $-1.63 | ⚠️ -1.9% | $253.00 |
| EV-LMS | TikTok Shop | $88.00 | 8.0% | $0.00 | $0.00 | $80.96 | $36.23 | ⚠️ 41.2% | $96.00 |
| EV-LMS | Tienda propia | $88.00 | 4.2% | $3.48 | $0.00 | $80.85 | $36.12 | ⚠️ 41.0% | $95.00 |
| EV-PRE | ML Clásica | $115.00 | 17.4% | $30.00 | $0.00 | $64.99 | $17.60 | ⚠️ 15.3% | $225.00 |
| EV-PRE | ML Premium | $115.00 | 22.6% | $30.00 | $0.00 | $58.99 | $11.60 | ⚠️ 10.1% | $261.00 |
| EV-PRE | TikTok Shop | $115.00 | 8.0% | $0.00 | $0.00 | $105.80 | $58.41 | 50.8% | $101.00 |
| EV-PRE | Tienda propia | $115.00 | 4.2% | $3.48 | $0.00 | $106.72 | $59.33 | 51.6% | $101.00 |
| NV-VEN | ML Clásica | $78.00 | 17.4% | $25.00 | $0.00 | $39.43 | $5.70 | ⚠️ 7.3% | $189.00 |
| NV-VEN | ML Premium | $78.00 | 22.6% | $25.00 | $0.00 | $35.36 | $1.62 | ⚠️ 2.1% | $219.00 |
| NV-VEN | TikTok Shop | $78.00 | 8.0% | $0.00 | $0.00 | $71.76 | $38.03 | 48.8% | $72.00 |
| NV-VEN | Tienda propia | $78.00 | 4.2% | $3.48 | $0.00 | $71.26 | $37.53 | 48.1% | $74.00 |
| NV-NAC | ML Clásica | $65.00 | 17.4% | $25.00 | $0.00 | $28.69 | $9.99 | ⚠️ 15.4% | $130.00 |
| NV-NAC | ML Premium | $65.00 | 22.6% | $25.00 | $0.00 | $25.30 | $6.59 | ⚠️ 10.1% | $173.00 |
| NV-NAC | TikTok Shop | $65.00 | 8.0% | $0.00 | $0.00 | $59.80 | $41.10 | 63.2% | $40.00 |
| NV-NAC | Tienda propia | $65.00 | 4.2% | $3.48 | $0.00 | $58.81 | $40.10 | 61.7% | $44.00 |
| NV-PIN | ML Clásica | $87.00 | 17.4% | $25.00 | $0.00 | $46.86 | $14.19 | ⚠️ 16.3% | $186.00 |
| NV-PIN | ML Premium | $87.00 | 22.6% | $25.00 | $0.00 | $42.32 | $9.65 | ⚠️ 11.1% | $216.00 |
| NV-PIN | TikTok Shop | $87.00 | 8.0% | $0.00 | $0.00 | $80.04 | $47.37 | 54.4% | $70.00 |
| NV-PIN | Tienda propia | $87.00 | 4.2% | $3.48 | $0.00 | $79.89 | $47.22 | 54.3% | $72.00 |
| NV-ARB | ML Clásica | $85.00 | 17.4% | $25.00 | $0.00 | $45.21 | $23.62 | ⚠️ 27.8% | $138.00 |
| NV-ARB | ML Premium | $85.00 | 22.6% | $25.00 | $0.00 | $40.77 | $19.18 | ⚠️ 22.6% | $181.00 |
| NV-ARB | TikTok Shop | $85.00 | 8.0% | $0.00 | $0.00 | $78.20 | $56.61 | 66.6% | $46.00 |
| NV-ARB | Tienda propia | $85.00 | 4.2% | $3.48 | $0.00 | $77.97 | $56.38 | 66.3% | $50.00 |
| NV-BOR | ML Clásica | $57.00 | 17.4% | $25.00 | $0.00 | $22.08 | $-3.31 | ⚠️ -5.8% | $148.00 |
| NV-BOR | ML Premium | $57.00 | 22.6% | $25.00 | $0.00 | $19.11 | $-6.28 | ⚠️ -11.0% | $193.00 |
| NV-BOR | TikTok Shop | $57.00 | 8.0% | $0.00 | $0.00 | $52.44 | $27.05 | 47.5% | $55.00 |
| NV-BOR | Tienda propia | $57.00 | 4.2% | $3.48 | $0.00 | $51.14 | $25.75 | 45.2% | $57.00 |
| NV-B12 | ML Clásica | $385.00 | 17.4% | $0.00 | $80.00 | $238.01 | $-76.08 | ⚠️ -19.8% | $1,049.00 |
| NV-B12 | ML Premium | $385.00 | 22.6% | $0.00 | $80.00 | $217.91 | $-96.18 | ⚠️ -25.0% | $1,218.00 |
| NV-B12 | TikTok Shop | $385.00 | 8.0% | $0.00 | $80.00 | $274.20 | $-39.89 | ⚠️ -10.4% | $839.00 |
| NV-B12 | Tienda propia | $385.00 | 4.2% | $3.48 | $120.00 | $245.44 | $-68.65 | ⚠️ -17.8% | $861.00 |
| NV-ROM | ML Clásica | $375.00 | 17.4% | $0.00 | $80.00 | $229.75 | $95.60 | ⚠️ 25.5% | $570.00 |
| NV-ROM | ML Premium | $375.00 | 22.6% | $0.00 | $80.00 | $210.18 | $76.02 | ⚠️ 20.3% | $662.00 |
| NV-ROM | TikTok Shop | $375.00 | 8.0% | $0.00 | $80.00 | $265.00 | $130.85 | ⚠️ 34.9% | $286.00 |
| NV-ROM | Tienda propia | $375.00 | 4.2% | $3.48 | $120.00 | $235.86 | $101.71 | ⚠️ 27.1% | $271.00 |

## 3. Kits para marketplace (ticket ≥ $299, sin cargo fijo de ML)

Kit = N piezas del mismo modelo a precio menudeo × N, en caja kraft (+$10 de caja; se quita el celofán individual: se conserva por simplicidad, sobreestima costo ~$1/pza). Al pasar de $299 el vendedor paga envío (supuesto $80 ML/TikTok, $120 tienda).

| Kit | Precio kit | Costo kit | Canal | Comisión % | Envío | Neto | Margen $ | Margen % | Precio mín. kit 45% (por pieza) |
|---|---|---|---|---|---|---|---|---|---|
| EV-OSO x4 | $348.00 | $211.37 | ML Clásica | 17.4% | $80.00 | $207.45 | $-3.93 | ⚠️ -1.1% | $775.00 ($193.75) |
| EV-OSO x4 | $348.00 | $211.37 | ML Premium | 22.6% | $80.00 | $189.28 | $-22.09 | ⚠️ -6.3% | $900.00 ($225.00) |
| EV-OSO x4 | $348.00 | $211.37 | TikTok Shop | 8.0% | $80.00 | $240.16 | $28.79 | ⚠️ 8.3% | $620.00 ($155.00) |
| EV-JIR x8 | $360.00 | $161.24 | ML Clásica | 17.4% | $80.00 | $217.36 | $56.12 | ⚠️ 15.6% | $642.00 ($80.25) |
| EV-JIR x8 | $360.00 | $161.24 | ML Premium | 22.6% | $80.00 | $198.57 | $37.33 | ⚠️ 10.4% | $746.00 ($93.25) |
| EV-JIR x8 | $360.00 | $161.24 | TikTok Shop | 8.0% | $80.00 | $251.20 | $89.96 | ⚠️ 25.0% | $514.00 ($64.25) |
| EV-ELE x6 | $342.00 | $206.89 | ML Clásica | 17.4% | $80.00 | $202.49 | $-4.40 | ⚠️ -1.3% | $764.00 ($127.33) |
| EV-ELE x6 | $342.00 | $206.89 | ML Premium | 22.6% | $80.00 | $184.64 | $-22.25 | ⚠️ -6.5% | $887.00 ($147.83) |
| EV-ELE x6 | $342.00 | $206.89 | TikTok Shop | 8.0% | $80.00 | $234.64 | $27.75 | ⚠️ 8.1% | $611.00 ($101.83) |
| EV-DIN x6 | $342.00 | $189.96 | ML Clásica | 17.4% | $80.00 | $202.49 | $12.53 | ⚠️ 3.7% | $718.00 ($119.67) |
| EV-DIN x6 | $342.00 | $189.96 | ML Premium | 22.6% | $80.00 | $184.64 | $-5.32 | ⚠️ -1.6% | $834.00 ($139.00) |
| EV-DIN x6 | $342.00 | $189.96 | TikTok Shop | 8.0% | $80.00 | $234.64 | $44.68 | ⚠️ 13.1% | $575.00 ($95.83) |
| EV-ANG x6 | $342.00 | $148.83 | ML Clásica | 17.4% | $80.00 | $202.49 | $53.66 | ⚠️ 15.7% | $609.00 ($101.50) |
| EV-ANG x6 | $342.00 | $148.83 | ML Premium | 22.6% | $80.00 | $184.64 | $35.81 | ⚠️ 10.5% | $707.00 ($117.83) |
| EV-ANG x6 | $342.00 | $148.83 | TikTok Shop | 8.0% | $80.00 | $234.64 | $85.81 | ⚠️ 25.1% | $487.00 ($81.17) |
| EV-FLO x4 | $308.00 | $136.38 | ML Clásica | 17.4% | $80.00 | $174.41 | $38.03 | ⚠️ 12.3% | $576.00 ($144.00) |
| EV-FLO x4 | $308.00 | $136.38 | ML Premium | 22.6% | $80.00 | $158.33 | $21.95 | ⚠️ 7.1% | $669.00 ($167.25) |
| EV-FLO x4 | $308.00 | $136.38 | TikTok Shop | 8.0% | $80.00 | $203.36 | $66.98 | ⚠️ 21.7% | $299.00 ($74.75) |
| EV-BUN x4 | $348.00 | $161.38 | ML Clásica | 17.4% | $80.00 | $207.45 | $46.07 | ⚠️ 13.2% | $642.00 ($160.50) |
| EV-BUN x4 | $348.00 | $161.38 | ML Premium | 22.6% | $80.00 | $189.28 | $27.91 | ⚠️ 8.0% | $746.00 ($186.50) |
| EV-BUN x4 | $348.00 | $161.38 | TikTok Shop | 8.0% | $80.00 | $240.16 | $78.78 | ⚠️ 22.6% | $514.00 ($128.50) |
| EV-GLO x6 | $444.00 | $344.81 | ML Clásica | 17.4% | $80.00 | $286.74 | $-58.07 | ⚠️ -13.1% | $1,130.00 ($188.33) |
| EV-GLO x6 | $444.00 | $344.81 | ML Premium | 22.6% | $80.00 | $263.57 | $-81.24 | ⚠️ -18.3% | $1,312.00 ($218.67) |
| EV-GLO x6 | $444.00 | $344.81 | TikTok Shop | 8.0% | $80.00 | $328.48 | $-16.33 | ⚠️ -3.7% | $904.00 ($150.67) |
| EV-LMM x6 | $312.00 | $196.57 | ML Clásica | 17.4% | $80.00 | $177.71 | $-18.86 | ⚠️ -6.0% | $736.00 ($122.67) |
| EV-LMM x6 | $312.00 | $196.57 | ML Premium | 22.6% | $80.00 | $161.43 | $-35.15 | ⚠️ -11.3% | $855.00 ($142.50) |
| EV-LMM x6 | $312.00 | $196.57 | TikTok Shop | 8.0% | $80.00 | $207.04 | $10.47 | ⚠️ 3.4% | $589.00 ($98.17) |
| EV-LMS x4 | $352.00 | $188.91 | ML Clásica | 17.4% | $80.00 | $210.75 | $21.84 | ⚠️ 6.2% | $716.00 ($179.00) |
| EV-LMS x4 | $352.00 | $188.91 | ML Premium | 22.6% | $80.00 | $192.38 | $3.47 | ⚠️ 1.0% | $831.00 ($207.75) |
| EV-LMS x4 | $352.00 | $188.91 | TikTok Shop | 8.0% | $80.00 | $243.84 | $54.93 | ⚠️ 15.6% | $573.00 ($143.25) |
| EV-PRE x4 | $460.00 | $199.55 | ML Clásica | 17.4% | $80.00 | $299.96 | $100.41 | ⚠️ 21.8% | $744.00 ($186.00) |
| EV-PRE x4 | $460.00 | $199.55 | ML Premium | 22.6% | $80.00 | $275.95 | $76.40 | ⚠️ 16.6% | $864.00 ($216.00) |
| EV-PRE x4 | $460.00 | $199.55 | TikTok Shop | 8.0% | $80.00 | $343.20 | $143.65 | ⚠️ 31.2% | $595.00 ($148.75) |
| NV-VEN x4 | $312.00 | $144.93 | ML Clásica | 17.4% | $80.00 | $177.71 | $32.78 | ⚠️ 10.5% | $599.00 ($149.75) |
| NV-VEN x4 | $312.00 | $144.93 | ML Premium | 22.6% | $80.00 | $161.43 | $16.50 | ⚠️ 5.3% | $695.00 ($173.75) |
| NV-VEN x4 | $312.00 | $144.93 | TikTok Shop | 8.0% | $80.00 | $207.04 | $62.11 | ⚠️ 19.9% | $479.00 ($119.75) |
| NV-NAC x6 | $390.00 | $122.22 | ML Clásica | 17.4% | $80.00 | $242.14 | $119.92 | ⚠️ 30.7% | $538.00 ($89.67) |
| NV-NAC x6 | $390.00 | $122.22 | ML Premium | 22.6% | $80.00 | $221.78 | $99.56 | ⚠️ 25.5% | $625.00 ($104.17) |
| NV-NAC x6 | $390.00 | $122.22 | TikTok Shop | 8.0% | $80.00 | $278.80 | $156.58 | ⚠️ 40.1% | $299.00 ($49.83) |
| NV-PIN x4 | $348.00 | $140.69 | ML Clásica | 17.4% | $80.00 | $207.45 | $66.76 | ⚠️ 19.2% | $587.00 ($146.75) |
| NV-PIN x4 | $348.00 | $140.69 | ML Premium | 22.6% | $80.00 | $189.28 | $48.60 | ⚠️ 14.0% | $682.00 ($170.50) |
| NV-PIN x4 | $348.00 | $140.69 | TikTok Shop | 8.0% | $80.00 | $240.16 | $99.47 | ⚠️ 28.6% | $470.00 ($117.50) |
| NV-ARB x4 | $340.00 | $96.38 | ML Clásica | 17.4% | $80.00 | $200.84 | $104.46 | ⚠️ 30.7% | $470.00 ($117.50) |
| NV-ARB x4 | $340.00 | $96.38 | ML Premium | 22.6% | $80.00 | $183.09 | $86.71 | ⚠️ 25.5% | $545.00 ($136.25) |
| NV-ARB x4 | $340.00 | $96.38 | TikTok Shop | 8.0% | $80.00 | $232.80 | $136.42 | ⚠️ 40.1% | $299.00 ($74.75) |
| NV-BOR x6 | $342.00 | $162.35 | ML Clásica | 17.4% | $80.00 | $202.49 | $40.15 | ⚠️ 11.7% | $645.00 ($107.50) |
| NV-BOR x6 | $342.00 | $162.35 | ML Premium | 22.6% | $80.00 | $184.64 | $22.29 | ⚠️ 6.5% | $749.00 ($124.83) |
| NV-BOR x6 | $342.00 | $162.35 | TikTok Shop | 8.0% | $80.00 | $234.64 | $72.29 | ⚠️ 21.1% | $516.00 ($86.00) |

## 4. Mayoreo directo (WhatsApp/Instagram, 0% comisión, envío por cuenta del cliente)

| SKU | Costo unitario | 11–50 | Margen | 51–99 | Margen | 100–150 | Margen |
|---|---|---|---|---|---|---|---|
| EV-OSO | $50.34 | $78.00 | 35.5% | $75.00 | ⚠️ 32.9% | $71.00 | ⚠️ 29.1% |
| EV-JIR | $18.90 | $40.00 | 52.7% | $38.00 | 50.3% | $36.00 | 47.5% |
| EV-ELE | $32.82 | $51.00 | 35.7% | $49.50 | ⚠️ 33.7% | $46.00 | ⚠️ 28.7% |
| EV-DIN | $29.99 | $51.00 | 41.2% | $49.50 | 39.4% | $46.00 | ⚠️ 34.8% |
| EV-ANG | $23.14 | $51.00 | 54.6% | $49.50 | 53.3% | $46.00 | 49.7% |
| EV-FLO | $31.59 | $69.50 | 54.5% | $67.00 | 52.8% | $63.00 | 49.9% |
| EV-BUN | $37.84 | $78.00 | 51.5% | $75.50 | 49.9% | $71.00 | 46.7% |
| EV-GLO | $55.80 | $66.50 | ⚠️ 16.1% | $64.00 | ⚠️ 12.8% | $60.00 | ⚠️ 7.0% |
| EV-LMM | $31.10 | $46.50 | ⚠️ 33.1% | $45.00 | ⚠️ 30.9% | $42.00 | ⚠️ 26.0% |
| EV-LMS | $44.73 | $79.00 | 43.4% | $76.50 | 41.5% | $72.00 | 37.9% |
| EV-PRE | $47.39 | $86.00 | 44.9% | $83.00 | 42.9% | $78.00 | 39.2% |
| NV-VEN | $33.73 | $70.00 | 51.8% | $67.00 | 49.7% | $62.00 | 45.6% |
| NV-NAC | $18.70 | $58.00 | 67.8% | $55.00 | 66.0% | $50.00 | 62.6% |
| NV-PIN | $32.67 | $78.00 | 58.1% | $75.00 | 56.4% | $69.00 | 52.6% |
| NV-ARB | $21.59 | $76.00 | 71.6% | $73.00 | 70.4% | $68.00 | 68.2% |
| NV-BOR | $25.39 | $51.00 | 50.2% | $49.00 | 48.2% | $45.00 | 43.6% |

## 5. Alertas ⚠️ y precio mínimo recomendado

Fórmula (README): `Precio = (costo + envío + cargo fijo + margen$) ÷ (1 − %comisión)` con margen$ = 45% del precio (menudeo) o 35% (mayoreo) ⇒ `Precio mínimo = (costo + envío + cargo fijo) ÷ (1 − %comisión − margen%)`.

### Menudeo pieza suelta con margen < 45%

| SKU | Canal | Precio actual | Margen | Precio mínimo para 45% |
|---|---|---|---|---|
| EV-OSO | ML Clásica | $87.00 | ⚠️ -4.0% | $233.00 |
| EV-OSO | ML Premium | $87.00 | ⚠️ -9.2% | $270.00 |
| EV-OSO | TikTok Shop | $87.00 | ⚠️ 34.1% | $108.00 |
| EV-OSO | Tienda propia | $87.00 | ⚠️ 34.0% | $106.00 |
| EV-JIR | ML Clásica | $45.00 | ⚠️ -15.0% | $131.00 |
| EV-JIR | ML Premium | $45.00 | ⚠️ -20.2% | $173.00 |
| EV-ELE | ML Clásica | $57.00 | ⚠️ -18.8% | $186.00 |
| EV-ELE | ML Premium | $57.00 | ⚠️ -24.1% | $216.00 |
| EV-ELE | TikTok Shop | $57.00 | ⚠️ 34.4% | $70.00 |
| EV-ELE | Tienda propia | $57.00 | ⚠️ 32.1% | $72.00 |
| EV-DIN | ML Clásica | $57.00 | ⚠️ -13.9% | $179.00 |
| EV-DIN | ML Premium | $57.00 | ⚠️ -19.1% | $207.00 |
| EV-DIN | TikTok Shop | $57.00 | ⚠️ 39.4% | $64.00 |
| EV-DIN | Tienda propia | $57.00 | ⚠️ 37.1% | $66.00 |
| EV-ANG | ML Clásica | $57.00 | ⚠️ -1.9% | $142.00 |
| EV-ANG | ML Premium | $57.00 | ⚠️ -7.1% | $186.00 |
| EV-FLO | ML Clásica | $77.00 | ⚠️ 9.1% | $183.00 |
| EV-FLO | ML Premium | $77.00 | ⚠️ 3.9% | $212.00 |
| EV-BUN | ML Clásica | $87.00 | ⚠️ 10.4% | $200.00 |
| EV-BUN | ML Premium | $87.00 | ⚠️ 5.1% | $232.00 |
| EV-GLO | ML Clásica | $74.00 | ⚠️ -26.6% | $247.00 |
| EV-GLO | ML Premium | $74.00 | ⚠️ -31.8% | $287.00 |
| EV-GLO | TikTok Shop | $74.00 | ⚠️ 16.6% | $119.00 |
| EV-GLO | Tienda propia | $74.00 | ⚠️ 15.7% | $117.00 |
| EV-LMM | ML Clásica | $52.00 | ⚠️ -25.3% | $182.00 |
| EV-LMM | ML Premium | $52.00 | ⚠️ -30.5% | $211.00 |
| EV-LMM | TikTok Shop | $52.00 | ⚠️ 32.2% | $67.00 |
| EV-LMM | Tienda propia | $52.00 | ⚠️ 29.3% | $69.00 |
| EV-LMS | ML Clásica | $88.00 | ⚠️ 3.4% | $218.00 |
| EV-LMS | ML Premium | $88.00 | ⚠️ -1.9% | $253.00 |
| EV-LMS | TikTok Shop | $88.00 | ⚠️ 41.2% | $96.00 |
| EV-LMS | Tienda propia | $88.00 | ⚠️ 41.0% | $95.00 |
| EV-PRE | ML Clásica | $115.00 | ⚠️ 15.3% | $225.00 |
| EV-PRE | ML Premium | $115.00 | ⚠️ 10.1% | $261.00 |
| NV-VEN | ML Clásica | $78.00 | ⚠️ 7.3% | $189.00 |
| NV-VEN | ML Premium | $78.00 | ⚠️ 2.1% | $219.00 |
| NV-NAC | ML Clásica | $65.00 | ⚠️ 15.4% | $130.00 |
| NV-NAC | ML Premium | $65.00 | ⚠️ 10.1% | $173.00 |
| NV-PIN | ML Clásica | $87.00 | ⚠️ 16.3% | $186.00 |
| NV-PIN | ML Premium | $87.00 | ⚠️ 11.1% | $216.00 |
| NV-ARB | ML Clásica | $85.00 | ⚠️ 27.8% | $138.00 |
| NV-ARB | ML Premium | $85.00 | ⚠️ 22.6% | $181.00 |
| NV-BOR | ML Clásica | $57.00 | ⚠️ -5.8% | $148.00 |
| NV-BOR | ML Premium | $57.00 | ⚠️ -11.0% | $193.00 |
| NV-B12 | ML Clásica | $385.00 | ⚠️ -19.8% | $1,049.00 |
| NV-B12 | ML Premium | $385.00 | ⚠️ -25.0% | $1,218.00 |
| NV-B12 | TikTok Shop | $385.00 | ⚠️ -10.4% | $839.00 |
| NV-B12 | Tienda propia | $385.00 | ⚠️ -17.8% | $861.00 |
| NV-ROM | ML Clásica | $375.00 | ⚠️ 25.5% | $570.00 |
| NV-ROM | ML Premium | $375.00 | ⚠️ 20.3% | $662.00 |
| NV-ROM | TikTok Shop | $375.00 | ⚠️ 34.9% | $286.00 |
| NV-ROM | Tienda propia | $375.00 | ⚠️ 27.1% | $271.00 |

### Mayoreo con margen < 35%

| SKU | Nivel | Precio actual | Margen | Precio mínimo para 35% |
|---|---|---|---|---|
| EV-OSO | 51–99 | $75.00 | ⚠️ 32.9% | $78.00 |
| EV-OSO | 100–150 | $71.00 | ⚠️ 29.1% | $78.00 |
| EV-ELE | 51–99 | $49.50 | ⚠️ 33.7% | $51.00 |
| EV-ELE | 100–150 | $46.00 | ⚠️ 28.7% | $51.00 |
| EV-DIN | 100–150 | $46.00 | ⚠️ 34.8% | $47.00 |
| EV-GLO | 11–50 | $66.50 | ⚠️ 16.1% | $86.00 |
| EV-GLO | 51–99 | $64.00 | ⚠️ 12.8% | $86.00 |
| EV-GLO | 100–150 | $60.00 | ⚠️ 7.0% | $86.00 |
| EV-LMM | 11–50 | $46.50 | ⚠️ 33.1% | $48.00 |
| EV-LMM | 51–99 | $45.00 | ⚠️ 30.9% | $48.00 |
| EV-LMM | 100–150 | $42.00 | ⚠️ 26.0% | $48.00 |

## 6. Sensibilidad del costo unitario (qué tanto cambia si los insumos reales son distintos)

- **Base**: supuestos de arriba.
- **Optimista (compra por volumen)**: parafina 25 kg ~$85/kg, soya 25 kg ~$110/kg (verificar), fragancia $550/kg al 6%, latas/frascos −30%.
- **Pesimista (compra al menudeo)**: parafina 1 kg $143/kg, fragancia en frasco chico ~$2,190/kg (60 ml $131.50) al 8%.

| SKU | Base | Optimista | Pesimista | Margen directo base / opt / pes |
|---|---|---|---|---|
| EV-OSO | $50.34 | $38.70 | $78.22 | 42% / 56% / 10% |
| EV-JIR | $18.90 | $16.49 | $24.69 | 58% / 63% / 45% |
| EV-ELE | $32.82 | $26.12 | $48.83 | 42% / 54% / 14% |
| EV-DIN | $29.99 | $24.17 | $43.93 | 47% / 58% / 23% |
| EV-ANG | $23.14 | $19.42 | $32.03 | 59% / 66% / 44% |
| EV-FLO | $31.59 | $25.71 | $45.68 | 59% / 67% / 41% |
| EV-BUN | $37.84 | $30.04 | $56.52 | 57% / 65% / 35% |
| EV-GLO | $55.80 | $41.11 | $69.46 | 25% / 44% / 6% |
| EV-LMM | $31.10 | $24.24 | $35.76 | 40% / 53% / 31% |
| EV-LMS | $44.73 | $33.51 | $55.02 | 49% / 62% / 37% |
| EV-PRE | $47.39 | $39.98 | $54.08 | 59% / 65% / 53% |
| NV-VEN | $33.73 | $27.35 | $49.00 | 57% / 65% / 37% |
| NV-NAC | $18.70 | $16.35 | $24.34 | 71% / 75% / 63% |
| NV-PIN | $32.67 | $26.60 | $47.20 | 62% / 69% / 46% |
| NV-ARB | $21.59 | $18.50 | $29.01 | 75% / 78% / 66% |
| NV-BOR | $25.39 | $22.54 | $32.21 | 55% / 60% / 43% |
| NV-B12 | $314.09 | $279.89 | $395.93 | 18% / 27% / -3% |
| NV-ROM | $134.15 | $111.79 | $187.67 | 64% / 70% / 50% |

