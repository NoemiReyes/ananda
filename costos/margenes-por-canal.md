# Márgenes por canal — Ananda Velas

> **Costos v2 (27-nov-2026): ESTIMADOS con precios parcialmente reales.** Cera, aroma, pabilo, colorante, papel adhesivo y opalina con precio real de Noemi (17-oct); gramos por vela, % de aroma, velas por hora, envases y empaques siguen estimados. Comisiones de ML/TikTok tomadas de fuentes de terceros: **verificar** en el simulador de costos de Mercado Libre y en TikTok Seller Center antes de publicar. Se regenera con `python3 costos/calculo_costos.py`.

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

EV-PRE se evalúa a $115; con la promo de octubre ($95) el margen directo sería 46% y en ML Clásica 3%.

Costo unitario: cera + fragancia (8% del peso, $1.667/g) + colorante + mecha + contenedor/base/pintura + etiqueta + empaque + mano de obra ($80/h) + merma 5%. Detalle en `costos/plantilla-costeo.csv`.

## Hallazgos (v2, 27-nov-2026)

> Los costos v2 usan los **precios reales** que Noemi dio el 17-oct (parafina $80/kg, soya $150/kg, aroma $50/30 ml, pabilo $25/3 m, colorante, papel adhesivo y opalina). **Siguen estimados** los gramos por vela, el % de aroma, las velas por hora, latas/frascos y empaques. Las alertas de las secciones 5 y 6 se generan solas con estos costos; las recomendaciones de texto de la v1 (9-oct) quedaron en el historial de git y **ya no aplican** porque el aroma real ($1.67/g) cuesta casi el doble de lo estimado ($0.90/g).
>
> Comisiones y envíos siguen siendo los del 9-oct (fuentes de terceros): **verificar** en el simulador de Mercado Libre y en TikTok Seller Center antes de publicar.

## 1. Costo unitario (v2) y margen en venta directa

| SKU | Producto | Cera g (supuesto) | Velas/h | Costo unitario | Menudeo | Margen directo |
|---|---|---|---|---|---|---|
| EV-OSO | Oso de Ternura | 188 g (10x9.5 cm, fondo 5.5, llenado 40%) | 10.00 | $55.94 | $87.00 | ⚠️ 35.7% |
| EV-JIR | Jirafa Africana | 39 g (9x4 cm, fondo 3, llenado 40%) | 12.00 | $19.23 | $45.00 | 57.3% |
| EV-ELE | Elefante Safari | 108 g (7x9.5 cm, fondo 4.5, llenado 40%) | 12.00 | $35.36 | $57.00 | ⚠️ 38.0% |
| EV-DIN | Dino T-Rex | 94 g (9.3x8 cm, fondo 4, llenado 35%) | 12.00 | $32.26 | $57.00 | ⚠️ 43.4% |
| EV-ANG | Ángeles Divinos | 60 g (6x7 cm, fondo 3.5, llenado 45%) | 12.00 | $23.93 | $57.00 | 58.0% |
| EV-FLO | Flowers On | 95 g (peonía Ø8 x 3.5 cm, llenado 60%) | 10.00 | $33.39 | $77.00 | 56.6% |
| EV-BUN | Bunny Happy | 126 g (10x7 cm, fondo 5, llenado 40%) | 10.00 | $41.28 | $87.00 | 52.5% |
| EV-GLO | Glowing Glass | 126 g (frasco Ø int 6.1, llenado a 4.8 cm) | 15.00 | $64.86 | $74.00 | ⚠️ 12.4% |
| EV-LMM | Lume Soja Mini | 43 g (lata Ø int 5.8, llenado a 1.8 cm) | 15.00 | $33.56 | $52.00 | ⚠️ 35.5% |
| EV-LMS | Lume Soja | 95 g (lata Ø int 5.8, llenado a 4.0 cm) | 15.00 | $51.33 | $88.00 | ⚠️ 41.7% |
| EV-PRE | Paquete Recuerdos | 43 g (vela = Lume Mini (43 g) + 2 jabones 25 g) | 8.00 | $51.06 | $115.00 | 55.6% |
| NV-VEN | Venado | 103 g (9.5x7.5 cm, fondo 4, llenado 40%) | 10.00 | $36.33 | $78.00 | 53.4% |
| NV-NAC | Nacimiento | 38 g (6.2x4.5 cm, fondo 3, llenado 50%) | 12.00 | $18.75 | $65.00 | 71.2% |
| NV-PIN | Pino | 98 g (cono 10 x Ø7.2, llenado 80%) | 10.00 | $35.14 | $87.00 | 59.6% |
| NV-ARB | Árbol Navideño | 50 g (cono 10 x Ø5, llenado 85%) | 12.00 | $22.39 | $85.00 | 73.7% |
| NV-BOR | Borrego | 46 g (6.5x4.5 cm, fondo 3.5, llenado 50%) | 8.00 | $25.74 | $57.00 | 54.8% |
| NV-B12 | Borregos de la Abundancia 12 pzs | 552 g (12 borregos x 46 g) | 0.58 | $323.63 | $385.00 | ⚠️ 15.9% |
| NV-ROM | Rompecabezas Navideño | 361 g (4 piezas, Ø6.5 x 22 cm, llenado 55%) | 2.00 | $148.18 | $375.00 | 60.5% |

## 2. Pieza suelta por canal (precio menudeo)

| SKU | Canal | Precio | Comisión % | Cargo fijo | Envío | Neto | Margen $ | Margen % | Precio mín. 45% |
|---|---|---|---|---|---|---|---|---|---|
| EV-OSO | ML Clásica | $87.00 | 17.4% | $25.00 | $0.00 | $46.86 | $-9.08 | ⚠️ -10.4% | $248.00 |
| EV-OSO | ML Premium | $87.00 | 22.6% | $25.00 | $0.00 | $42.32 | $-13.62 | ⚠️ -15.7% | $288.00 |
| EV-OSO | TikTok Shop | $87.00 | 8.0% | $0.00 | $0.00 | $80.04 | $24.10 | ⚠️ 27.7% | $120.00 |
| EV-OSO | Tienda propia | $87.00 | 4.2% | $3.48 | $0.00 | $79.89 | $23.95 | ⚠️ 27.5% | $117.00 |
| EV-JIR | ML Clásica | $45.00 | 17.4% | $25.00 | $0.00 | $12.17 | $-7.06 | ⚠️ -15.7% | $131.00 |
| EV-JIR | ML Premium | $45.00 | 22.6% | $25.00 | $0.00 | $9.82 | $-9.41 | ⚠️ -20.9% | $174.00 |
| EV-JIR | TikTok Shop | $45.00 | 8.0% | $0.00 | $0.00 | $41.40 | $22.17 | 49.3% | $41.00 |
| EV-JIR | Tienda propia | $45.00 | 4.2% | $3.48 | $0.00 | $39.64 | $20.41 | 45.4% | $45.00 |
| EV-ELE | ML Clásica | $57.00 | 17.4% | $25.00 | $0.00 | $22.08 | $-13.28 | ⚠️ -23.3% | $193.00 |
| EV-ELE | ML Premium | $57.00 | 22.6% | $25.00 | $0.00 | $19.11 | $-16.26 | ⚠️ -28.5% | $224.00 |
| EV-ELE | TikTok Shop | $57.00 | 8.0% | $0.00 | $0.00 | $52.44 | $17.08 | ⚠️ 30.0% | $76.00 |
| EV-ELE | Tienda propia | $57.00 | 4.2% | $3.48 | $0.00 | $51.14 | $15.78 | ⚠️ 27.7% | $77.00 |
| EV-DIN | ML Clásica | $57.00 | 17.4% | $25.00 | $0.00 | $22.08 | $-10.17 | ⚠️ -17.8% | $185.00 |
| EV-DIN | ML Premium | $57.00 | 22.6% | $25.00 | $0.00 | $19.11 | $-13.15 | ⚠️ -23.1% | $214.00 |
| EV-DIN | TikTok Shop | $57.00 | 8.0% | $0.00 | $0.00 | $52.44 | $20.18 | ⚠️ 35.4% | $69.00 |
| EV-DIN | Tienda propia | $57.00 | 4.2% | $3.48 | $0.00 | $51.14 | $18.88 | ⚠️ 33.1% | $71.00 |
| EV-ANG | ML Clásica | $57.00 | 17.4% | $25.00 | $0.00 | $22.08 | $-1.85 | ⚠️ -3.2% | $144.00 |
| EV-ANG | ML Premium | $57.00 | 22.6% | $25.00 | $0.00 | $19.11 | $-4.82 | ⚠️ -8.5% | $189.00 |
| EV-ANG | TikTok Shop | $57.00 | 8.0% | $0.00 | $0.00 | $52.44 | $28.51 | 50.0% | $51.00 |
| EV-ANG | Tienda propia | $57.00 | 4.2% | $3.48 | $0.00 | $51.14 | $27.21 | 47.7% | $54.00 |
| EV-FLO | ML Clásica | $77.00 | 17.4% | $25.00 | $0.00 | $38.60 | $5.22 | ⚠️ 6.8% | $188.00 |
| EV-FLO | ML Premium | $77.00 | 22.6% | $25.00 | $0.00 | $34.58 | $1.20 | ⚠️ 1.6% | $218.00 |
| EV-FLO | TikTok Shop | $77.00 | 8.0% | $0.00 | $0.00 | $70.84 | $37.45 | 48.6% | $72.00 |
| EV-FLO | Tienda propia | $77.00 | 4.2% | $3.48 | $0.00 | $70.30 | $36.92 | 47.9% | $73.00 |
| EV-BUN | ML Clásica | $87.00 | 17.4% | $25.00 | $0.00 | $46.86 | $5.58 | ⚠️ 6.4% | $209.00 |
| EV-BUN | ML Premium | $87.00 | 22.6% | $25.00 | $0.00 | $42.32 | $1.04 | ⚠️ 1.2% | $242.00 |
| EV-BUN | TikTok Shop | $87.00 | 8.0% | $0.00 | $0.00 | $80.04 | $38.76 | ⚠️ 44.5% | $88.00 |
| EV-BUN | Tienda propia | $87.00 | 4.2% | $3.48 | $0.00 | $79.89 | $38.61 | ⚠️ 44.4% | $89.00 |
| EV-GLO | ML Clásica | $74.00 | 17.4% | $25.00 | $0.00 | $36.12 | $-28.73 | ⚠️ -38.8% | $271.00 |
| EV-GLO | ML Premium | $74.00 | 22.6% | $25.00 | $0.00 | $32.26 | $-32.60 | ⚠️ -44.1% | $448.00 |
| EV-GLO | TikTok Shop | $74.00 | 8.0% | $0.00 | $0.00 | $68.08 | $3.22 | ⚠️ 4.4% | $138.00 |
| EV-GLO | Tienda propia | $74.00 | 4.2% | $3.48 | $0.00 | $67.43 | $2.57 | ⚠️ 3.5% | $135.00 |
| EV-LMM | ML Clásica | $52.00 | 17.4% | $25.00 | $0.00 | $17.95 | $-15.61 | ⚠️ -30.0% | $188.00 |
| EV-LMM | ML Premium | $52.00 | 22.6% | $25.00 | $0.00 | $15.24 | $-18.32 | ⚠️ -35.2% | $218.00 |
| EV-LMM | TikTok Shop | $52.00 | 8.0% | $0.00 | $0.00 | $47.84 | $14.28 | ⚠️ 27.5% | $72.00 |
| EV-LMM | Tienda propia | $52.00 | 4.2% | $3.48 | $0.00 | $46.35 | $12.79 | ⚠️ 24.6% | $73.00 |
| EV-LMS | ML Clásica | $88.00 | 17.4% | $25.00 | $0.00 | $47.69 | $-3.64 | ⚠️ -4.1% | $235.00 |
| EV-LMS | ML Premium | $88.00 | 22.6% | $25.00 | $0.00 | $43.09 | $-8.24 | ⚠️ -9.4% | $273.00 |
| EV-LMS | TikTok Shop | $88.00 | 8.0% | $0.00 | $0.00 | $80.96 | $29.63 | ⚠️ 33.7% | $110.00 |
| EV-LMS | Tienda propia | $88.00 | 4.2% | $3.48 | $0.00 | $80.85 | $29.51 | ⚠️ 33.5% | $108.00 |
| EV-PRE | ML Clásica | $115.00 | 17.4% | $30.00 | $0.00 | $64.99 | $13.93 | ⚠️ 12.1% | $235.00 |
| EV-PRE | ML Premium | $115.00 | 22.6% | $30.00 | $0.00 | $58.99 | $7.93 | ⚠️ 6.9% | $272.00 |
| EV-PRE | TikTok Shop | $115.00 | 8.0% | $0.00 | $0.00 | $105.80 | $54.74 | 47.6% | $109.00 |
| EV-PRE | Tienda propia | $115.00 | 4.2% | $3.48 | $0.00 | $106.72 | $55.66 | 48.4% | $108.00 |
| NV-VEN | ML Clásica | $78.00 | 17.4% | $25.00 | $0.00 | $39.43 | $3.10 | ⚠️ 4.0% | $196.00 |
| NV-VEN | ML Premium | $78.00 | 22.6% | $25.00 | $0.00 | $35.36 | $-0.97 | ⚠️ -1.2% | $227.00 |
| NV-VEN | TikTok Shop | $78.00 | 8.0% | $0.00 | $0.00 | $71.76 | $35.43 | 45.4% | $78.00 |
| NV-VEN | Tienda propia | $78.00 | 4.2% | $3.48 | $0.00 | $71.26 | $34.94 | ⚠️ 44.8% | $79.00 |
| NV-NAC | ML Clásica | $65.00 | 17.4% | $25.00 | $0.00 | $28.69 | $9.94 | ⚠️ 15.3% | $130.00 |
| NV-NAC | ML Premium | $65.00 | 22.6% | $25.00 | $0.00 | $25.30 | $6.55 | ⚠️ 10.1% | $173.00 |
| NV-NAC | TikTok Shop | $65.00 | 8.0% | $0.00 | $0.00 | $59.80 | $41.05 | 63.2% | $40.00 |
| NV-NAC | Tienda propia | $65.00 | 4.2% | $3.48 | $0.00 | $58.81 | $40.06 | 61.6% | $44.00 |
| NV-PIN | ML Clásica | $87.00 | 17.4% | $25.00 | $0.00 | $46.86 | $11.73 | ⚠️ 13.5% | $192.00 |
| NV-PIN | ML Premium | $87.00 | 22.6% | $25.00 | $0.00 | $42.32 | $7.19 | ⚠️ 8.3% | $223.00 |
| NV-PIN | TikTok Shop | $87.00 | 8.0% | $0.00 | $0.00 | $80.04 | $44.90 | 51.6% | $75.00 |
| NV-PIN | Tienda propia | $87.00 | 4.2% | $3.48 | $0.00 | $79.89 | $44.75 | 51.4% | $76.00 |
| NV-ARB | ML Clásica | $85.00 | 17.4% | $25.00 | $0.00 | $45.21 | $22.82 | ⚠️ 26.8% | $140.00 |
| NV-ARB | ML Premium | $85.00 | 22.6% | $25.00 | $0.00 | $40.77 | $18.38 | ⚠️ 21.6% | $184.00 |
| NV-ARB | TikTok Shop | $85.00 | 8.0% | $0.00 | $0.00 | $78.20 | $55.81 | 65.7% | $48.00 |
| NV-ARB | Tienda propia | $85.00 | 4.2% | $3.48 | $0.00 | $77.97 | $55.58 | 65.4% | $51.00 |
| NV-BOR | ML Clásica | $57.00 | 17.4% | $25.00 | $0.00 | $22.08 | $-3.66 | ⚠️ -6.4% | $149.00 |
| NV-BOR | ML Premium | $57.00 | 22.6% | $25.00 | $0.00 | $19.11 | $-6.63 | ⚠️ -11.6% | $194.00 |
| NV-BOR | TikTok Shop | $57.00 | 8.0% | $0.00 | $0.00 | $52.44 | $26.70 | 46.8% | $55.00 |
| NV-BOR | Tienda propia | $57.00 | 4.2% | $3.48 | $0.00 | $51.14 | $25.40 | ⚠️ 44.6% | $58.00 |
| NV-B12 | ML Clásica | $385.00 | 17.4% | $0.00 | $80.00 | $238.01 | $-85.62 | ⚠️ -22.2% | $1,074.00 |
| NV-B12 | ML Premium | $385.00 | 22.6% | $0.00 | $80.00 | $217.91 | $-105.72 | ⚠️ -27.5% | $1,247.00 |
| NV-B12 | TikTok Shop | $385.00 | 8.0% | $0.00 | $80.00 | $274.20 | $-49.43 | ⚠️ -12.8% | $859.00 |
| NV-B12 | Tienda propia | $385.00 | 4.2% | $3.48 | $120.00 | $245.44 | $-78.19 | ⚠️ -20.3% | $880.00 |
| NV-ROM | ML Clásica | $375.00 | 17.4% | $0.00 | $80.00 | $229.75 | $81.57 | ⚠️ 21.8% | $607.00 |
| NV-ROM | ML Premium | $375.00 | 22.6% | $0.00 | $80.00 | $210.18 | $62.00 | ⚠️ 16.5% | $705.00 |
| NV-ROM | TikTok Shop | $375.00 | 8.0% | $0.00 | $80.00 | $265.00 | $116.82 | ⚠️ 31.2% | $486.00 |
| NV-ROM | Tienda propia | $375.00 | 4.2% | $3.48 | $120.00 | $235.86 | $87.68 | ⚠️ 23.4% | $299.00 |

## 3. Kits para marketplace (ticket ≥ $299, sin cargo fijo de ML)

Kit = N piezas del mismo modelo a precio menudeo × N, en caja kraft (+$10 de caja; se quita el celofán individual: se conserva por simplicidad, sobreestima costo ~$1/pza). Al pasar de $299 el vendedor paga envío (supuesto $80 ML/TikTok, $120 tienda).

| Kit | Precio kit | Costo kit | Canal | Comisión % | Envío | Neto | Margen $ | Margen % | Precio mín. kit 45% (por pieza) |
|---|---|---|---|---|---|---|---|---|---|
| EV-OSO x4 | $348.00 | $233.75 | ML Clásica | 17.4% | $80.00 | $207.45 | $-26.30 | ⚠️ -7.6% | $835.00 ($208.75) |
| EV-OSO x4 | $348.00 | $233.75 | ML Premium | 22.6% | $80.00 | $189.28 | $-44.47 | ⚠️ -12.8% | $969.00 ($242.25) |
| EV-OSO x4 | $348.00 | $233.75 | TikTok Shop | 8.0% | $80.00 | $240.16 | $6.41 | ⚠️ 1.8% | $668.00 ($167.00) |
| EV-JIR x8 | $360.00 | $163.83 | ML Clásica | 17.4% | $80.00 | $217.36 | $53.53 | ⚠️ 14.9% | $649.00 ($81.12) |
| EV-JIR x8 | $360.00 | $163.83 | ML Premium | 22.6% | $80.00 | $198.57 | $34.74 | ⚠️ 9.6% | $754.00 ($94.25) |
| EV-JIR x8 | $360.00 | $163.83 | TikTok Shop | 8.0% | $80.00 | $251.20 | $87.37 | ⚠️ 24.3% | $519.00 ($64.88) |
| EV-ELE x6 | $342.00 | $222.19 | ML Clásica | 17.4% | $80.00 | $202.49 | $-19.69 | ⚠️ -5.8% | $804.00 ($134.00) |
| EV-ELE x6 | $342.00 | $222.19 | ML Premium | 22.6% | $80.00 | $184.64 | $-37.55 | ⚠️ -11.0% | $934.00 ($155.67) |
| EV-ELE x6 | $342.00 | $222.19 | TikTok Shop | 8.0% | $80.00 | $234.64 | $12.45 | ⚠️ 3.6% | $643.00 ($107.17) |
| EV-DIN x6 | $342.00 | $203.54 | ML Clásica | 17.4% | $80.00 | $202.49 | $-1.04 | ⚠️ -0.3% | $755.00 ($125.83) |
| EV-DIN x6 | $342.00 | $203.54 | ML Premium | 22.6% | $80.00 | $184.64 | $-18.90 | ⚠️ -5.5% | $876.00 ($146.00) |
| EV-DIN x6 | $342.00 | $203.54 | TikTok Shop | 8.0% | $80.00 | $234.64 | $31.10 | ⚠️ 9.1% | $604.00 ($100.67) |
| EV-ANG x6 | $342.00 | $153.58 | ML Clásica | 17.4% | $80.00 | $202.49 | $48.91 | ⚠️ 14.3% | $622.00 ($103.67) |
| EV-ANG x6 | $342.00 | $153.58 | ML Premium | 22.6% | $80.00 | $184.64 | $31.06 | ⚠️ 9.1% | $722.00 ($120.33) |
| EV-ANG x6 | $342.00 | $153.58 | TikTok Shop | 8.0% | $80.00 | $234.64 | $81.06 | ⚠️ 23.7% | $497.00 ($82.83) |
| EV-FLO x4 | $308.00 | $143.54 | ML Clásica | 17.4% | $80.00 | $174.41 | $30.87 | ⚠️ 10.0% | $595.00 ($148.75) |
| EV-FLO x4 | $308.00 | $143.54 | ML Premium | 22.6% | $80.00 | $158.33 | $14.79 | ⚠️ 4.8% | $691.00 ($172.75) |
| EV-FLO x4 | $308.00 | $143.54 | TikTok Shop | 8.0% | $80.00 | $203.36 | $59.82 | ⚠️ 19.4% | $476.00 ($119.00) |
| EV-BUN x4 | $348.00 | $175.13 | ML Clásica | 17.4% | $80.00 | $207.45 | $32.32 | ⚠️ 9.3% | $679.00 ($169.75) |
| EV-BUN x4 | $348.00 | $175.13 | ML Premium | 22.6% | $80.00 | $189.28 | $14.16 | ⚠️ 4.1% | $788.00 ($197.00) |
| EV-BUN x4 | $348.00 | $175.13 | TikTok Shop | 8.0% | $80.00 | $240.16 | $65.03 | ⚠️ 18.7% | $543.00 ($135.75) |
| EV-GLO x6 | $444.00 | $399.15 | ML Clásica | 17.4% | $80.00 | $286.74 | $-112.41 | ⚠️ -25.3% | $1,275.00 ($212.50) |
| EV-GLO x6 | $444.00 | $399.15 | ML Premium | 22.6% | $80.00 | $263.57 | $-135.58 | ⚠️ -30.5% | $1,480.00 ($246.67) |
| EV-GLO x6 | $444.00 | $399.15 | TikTok Shop | 8.0% | $80.00 | $328.48 | $-70.67 | ⚠️ -15.9% | $1,020.00 ($170.00) |
| EV-LMM x6 | $312.00 | $211.36 | ML Clásica | 17.4% | $80.00 | $177.71 | $-33.65 | ⚠️ -10.8% | $775.00 ($129.17) |
| EV-LMM x6 | $312.00 | $211.36 | ML Premium | 22.6% | $80.00 | $161.43 | $-49.93 | ⚠️ -16.0% | $900.00 ($150.00) |
| EV-LMM x6 | $312.00 | $211.36 | TikTok Shop | 8.0% | $80.00 | $207.04 | $-4.32 | ⚠️ -1.4% | $620.00 ($103.33) |
| EV-LMS x4 | $352.00 | $215.32 | ML Clásica | 17.4% | $80.00 | $210.75 | $-4.57 | ⚠️ -1.3% | $786.00 ($196.50) |
| EV-LMS x4 | $352.00 | $215.32 | ML Premium | 22.6% | $80.00 | $192.38 | $-22.95 | ⚠️ -6.5% | $913.00 ($228.25) |
| EV-LMS x4 | $352.00 | $215.32 | TikTok Shop | 8.0% | $80.00 | $243.84 | $28.52 | ⚠️ 8.1% | $629.00 ($157.25) |
| EV-PRE x4 | $460.00 | $214.24 | ML Clásica | 17.4% | $80.00 | $299.96 | $85.72 | ⚠️ 18.6% | $783.00 ($195.75) |
| EV-PRE x4 | $460.00 | $214.24 | ML Premium | 22.6% | $80.00 | $275.95 | $61.71 | ⚠️ 13.4% | $909.00 ($227.25) |
| EV-PRE x4 | $460.00 | $214.24 | TikTok Shop | 8.0% | $80.00 | $343.20 | $128.96 | ⚠️ 28.0% | $627.00 ($156.75) |
| NV-VEN x4 | $312.00 | $155.30 | ML Clásica | 17.4% | $80.00 | $177.71 | $22.41 | ⚠️ 7.2% | $626.00 ($156.50) |
| NV-VEN x4 | $312.00 | $155.30 | ML Premium | 22.6% | $80.00 | $161.43 | $6.12 | ⚠️ 2.0% | $727.00 ($181.75) |
| NV-VEN x4 | $312.00 | $155.30 | TikTok Shop | 8.0% | $80.00 | $207.04 | $51.74 | ⚠️ 16.6% | $501.00 ($125.25) |
| NV-NAC x6 | $390.00 | $122.49 | ML Clásica | 17.4% | $80.00 | $242.14 | $119.65 | ⚠️ 30.7% | $539.00 ($89.83) |
| NV-NAC x6 | $390.00 | $122.49 | ML Premium | 22.6% | $80.00 | $221.78 | $99.30 | ⚠️ 25.5% | $626.00 ($104.33) |
| NV-NAC x6 | $390.00 | $122.49 | TikTok Shop | 8.0% | $80.00 | $278.80 | $156.31 | ⚠️ 40.1% | $299.00 ($49.83) |
| NV-PIN x4 | $348.00 | $150.54 | ML Clásica | 17.4% | $80.00 | $207.45 | $56.91 | ⚠️ 16.4% | $614.00 ($153.50) |
| NV-PIN x4 | $348.00 | $150.54 | ML Premium | 22.6% | $80.00 | $189.28 | $38.74 | ⚠️ 11.1% | $712.00 ($178.00) |
| NV-PIN x4 | $348.00 | $150.54 | TikTok Shop | 8.0% | $80.00 | $240.16 | $89.62 | ⚠️ 25.8% | $491.00 ($122.75) |
| NV-ARB x4 | $340.00 | $99.56 | ML Clásica | 17.4% | $80.00 | $200.84 | $101.28 | ⚠️ 29.8% | $478.00 ($119.50) |
| NV-ARB x4 | $340.00 | $99.56 | ML Premium | 22.6% | $80.00 | $183.09 | $83.54 | ⚠️ 24.6% | $555.00 ($138.75) |
| NV-ARB x4 | $340.00 | $99.56 | TikTok Shop | 8.0% | $80.00 | $232.80 | $133.24 | ⚠️ 39.2% | $299.00 ($74.75) |
| NV-BOR x6 | $342.00 | $164.44 | ML Clásica | 17.4% | $80.00 | $202.49 | $38.05 | ⚠️ 11.1% | $651.00 ($108.50) |
| NV-BOR x6 | $342.00 | $164.44 | ML Premium | 22.6% | $80.00 | $184.64 | $20.20 | ⚠️ 5.9% | $755.00 ($125.83) |
| NV-BOR x6 | $342.00 | $164.44 | TikTok Shop | 8.0% | $80.00 | $234.64 | $70.20 | ⚠️ 20.5% | $521.00 ($86.83) |

## 4. Mayoreo directo (WhatsApp/Instagram, 0% comisión, envío por cuenta del cliente)

| SKU | Costo unitario | 11–50 | Margen | 51–99 | Margen | 100–150 | Margen |
|---|---|---|---|---|---|---|---|
| EV-OSO | $55.94 | $78.00 | ⚠️ 28.3% | $75.00 | ⚠️ 25.4% | $71.00 | ⚠️ 21.2% |
| EV-JIR | $19.23 | $40.00 | 51.9% | $38.00 | 49.4% | $36.00 | 46.6% |
| EV-ELE | $35.36 | $51.00 | ⚠️ 30.7% | $49.50 | ⚠️ 28.6% | $46.00 | ⚠️ 23.1% |
| EV-DIN | $32.26 | $51.00 | 36.8% | $49.50 | ⚠️ 34.8% | $46.00 | ⚠️ 29.9% |
| EV-ANG | $23.93 | $51.00 | 53.1% | $49.50 | 51.7% | $46.00 | 48.0% |
| EV-FLO | $33.39 | $69.50 | 52.0% | $67.00 | 50.2% | $63.00 | 47.0% |
| EV-BUN | $41.28 | $78.00 | 47.1% | $75.50 | 45.3% | $71.00 | 41.9% |
| EV-GLO | $64.86 | $66.50 | ⚠️ 2.5% | $64.00 | ⚠️ -1.3% | $60.00 | ⚠️ -8.1% |
| EV-LMM | $33.56 | $46.50 | ⚠️ 27.8% | $45.00 | ⚠️ 25.4% | $42.00 | ⚠️ 20.1% |
| EV-LMS | $51.33 | $79.00 | 35.0% | $76.50 | ⚠️ 32.9% | $72.00 | ⚠️ 28.7% |
| EV-PRE | $51.06 | $86.00 | 40.6% | $83.00 | 38.5% | $78.00 | ⚠️ 34.5% |
| NV-VEN | $36.33 | $70.00 | 48.1% | $67.00 | 45.8% | $62.00 | 41.4% |
| NV-NAC | $18.75 | $58.00 | 67.7% | $55.00 | 65.9% | $50.00 | 62.5% |
| NV-PIN | $35.14 | $78.00 | 55.0% | $75.00 | 53.2% | $69.00 | 49.1% |
| NV-ARB | $22.39 | $76.00 | 70.5% | $73.00 | 69.3% | $68.00 | 67.1% |
| NV-BOR | $25.74 | $51.00 | 49.5% | $49.00 | 47.5% | $45.00 | 42.8% |

## 5. Alertas ⚠️ y precio mínimo recomendado

Fórmula (README): `Precio = (costo + envío + cargo fijo + margen$) ÷ (1 − %comisión)` con margen$ = 45% del precio (menudeo) o 35% (mayoreo) ⇒ `Precio mínimo = (costo + envío + cargo fijo) ÷ (1 − %comisión − margen%)`.

### Menudeo pieza suelta con margen < 45%

| SKU | Canal | Precio actual | Margen | Precio mínimo para 45% |
|---|---|---|---|---|
| EV-OSO | ML Clásica | $87.00 | ⚠️ -10.4% | $248.00 |
| EV-OSO | ML Premium | $87.00 | ⚠️ -15.7% | $288.00 |
| EV-OSO | TikTok Shop | $87.00 | ⚠️ 27.7% | $120.00 |
| EV-OSO | Tienda propia | $87.00 | ⚠️ 27.5% | $117.00 |
| EV-JIR | ML Clásica | $45.00 | ⚠️ -15.7% | $131.00 |
| EV-JIR | ML Premium | $45.00 | ⚠️ -20.9% | $174.00 |
| EV-ELE | ML Clásica | $57.00 | ⚠️ -23.3% | $193.00 |
| EV-ELE | ML Premium | $57.00 | ⚠️ -28.5% | $224.00 |
| EV-ELE | TikTok Shop | $57.00 | ⚠️ 30.0% | $76.00 |
| EV-ELE | Tienda propia | $57.00 | ⚠️ 27.7% | $77.00 |
| EV-DIN | ML Clásica | $57.00 | ⚠️ -17.8% | $185.00 |
| EV-DIN | ML Premium | $57.00 | ⚠️ -23.1% | $214.00 |
| EV-DIN | TikTok Shop | $57.00 | ⚠️ 35.4% | $69.00 |
| EV-DIN | Tienda propia | $57.00 | ⚠️ 33.1% | $71.00 |
| EV-ANG | ML Clásica | $57.00 | ⚠️ -3.2% | $144.00 |
| EV-ANG | ML Premium | $57.00 | ⚠️ -8.5% | $189.00 |
| EV-FLO | ML Clásica | $77.00 | ⚠️ 6.8% | $188.00 |
| EV-FLO | ML Premium | $77.00 | ⚠️ 1.6% | $218.00 |
| EV-BUN | ML Clásica | $87.00 | ⚠️ 6.4% | $209.00 |
| EV-BUN | ML Premium | $87.00 | ⚠️ 1.2% | $242.00 |
| EV-BUN | TikTok Shop | $87.00 | ⚠️ 44.5% | $88.00 |
| EV-BUN | Tienda propia | $87.00 | ⚠️ 44.4% | $89.00 |
| EV-GLO | ML Clásica | $74.00 | ⚠️ -38.8% | $271.00 |
| EV-GLO | ML Premium | $74.00 | ⚠️ -44.1% | $448.00 |
| EV-GLO | TikTok Shop | $74.00 | ⚠️ 4.4% | $138.00 |
| EV-GLO | Tienda propia | $74.00 | ⚠️ 3.5% | $135.00 |
| EV-LMM | ML Clásica | $52.00 | ⚠️ -30.0% | $188.00 |
| EV-LMM | ML Premium | $52.00 | ⚠️ -35.2% | $218.00 |
| EV-LMM | TikTok Shop | $52.00 | ⚠️ 27.5% | $72.00 |
| EV-LMM | Tienda propia | $52.00 | ⚠️ 24.6% | $73.00 |
| EV-LMS | ML Clásica | $88.00 | ⚠️ -4.1% | $235.00 |
| EV-LMS | ML Premium | $88.00 | ⚠️ -9.4% | $273.00 |
| EV-LMS | TikTok Shop | $88.00 | ⚠️ 33.7% | $110.00 |
| EV-LMS | Tienda propia | $88.00 | ⚠️ 33.5% | $108.00 |
| EV-PRE | ML Clásica | $115.00 | ⚠️ 12.1% | $235.00 |
| EV-PRE | ML Premium | $115.00 | ⚠️ 6.9% | $272.00 |
| NV-VEN | ML Clásica | $78.00 | ⚠️ 4.0% | $196.00 |
| NV-VEN | ML Premium | $78.00 | ⚠️ -1.2% | $227.00 |
| NV-VEN | Tienda propia | $78.00 | ⚠️ 44.8% | $79.00 |
| NV-NAC | ML Clásica | $65.00 | ⚠️ 15.3% | $130.00 |
| NV-NAC | ML Premium | $65.00 | ⚠️ 10.1% | $173.00 |
| NV-PIN | ML Clásica | $87.00 | ⚠️ 13.5% | $192.00 |
| NV-PIN | ML Premium | $87.00 | ⚠️ 8.3% | $223.00 |
| NV-ARB | ML Clásica | $85.00 | ⚠️ 26.8% | $140.00 |
| NV-ARB | ML Premium | $85.00 | ⚠️ 21.6% | $184.00 |
| NV-BOR | ML Clásica | $57.00 | ⚠️ -6.4% | $149.00 |
| NV-BOR | ML Premium | $57.00 | ⚠️ -11.6% | $194.00 |
| NV-BOR | Tienda propia | $57.00 | ⚠️ 44.6% | $58.00 |
| NV-B12 | ML Clásica | $385.00 | ⚠️ -22.2% | $1,074.00 |
| NV-B12 | ML Premium | $385.00 | ⚠️ -27.5% | $1,247.00 |
| NV-B12 | TikTok Shop | $385.00 | ⚠️ -12.8% | $859.00 |
| NV-B12 | Tienda propia | $385.00 | ⚠️ -20.3% | $880.00 |
| NV-ROM | ML Clásica | $375.00 | ⚠️ 21.8% | $607.00 |
| NV-ROM | ML Premium | $375.00 | ⚠️ 16.5% | $705.00 |
| NV-ROM | TikTok Shop | $375.00 | ⚠️ 31.2% | $486.00 |
| NV-ROM | Tienda propia | $375.00 | ⚠️ 23.4% | $299.00 |

### Mayoreo con margen < 35%

| SKU | Nivel | Precio actual | Margen | Precio mínimo para 35% |
|---|---|---|---|---|
| EV-OSO | 11–50 | $78.00 | ⚠️ 28.3% | $87.00 |
| EV-OSO | 51–99 | $75.00 | ⚠️ 25.4% | $87.00 |
| EV-OSO | 100–150 | $71.00 | ⚠️ 21.2% | $87.00 |
| EV-ELE | 11–50 | $51.00 | ⚠️ 30.7% | $55.00 |
| EV-ELE | 51–99 | $49.50 | ⚠️ 28.6% | $55.00 |
| EV-ELE | 100–150 | $46.00 | ⚠️ 23.1% | $55.00 |
| EV-DIN | 51–99 | $49.50 | ⚠️ 34.8% | $50.00 |
| EV-DIN | 100–150 | $46.00 | ⚠️ 29.9% | $50.00 |
| EV-GLO | 11–50 | $66.50 | ⚠️ 2.5% | $100.00 |
| EV-GLO | 51–99 | $64.00 | ⚠️ -1.3% | $100.00 |
| EV-GLO | 100–150 | $60.00 | ⚠️ -8.1% | $100.00 |
| EV-LMM | 11–50 | $46.50 | ⚠️ 27.8% | $52.00 |
| EV-LMM | 51–99 | $45.00 | ⚠️ 25.4% | $52.00 |
| EV-LMM | 100–150 | $42.00 | ⚠️ 20.1% | $52.00 |
| EV-LMS | 51–99 | $76.50 | ⚠️ 32.9% | $79.00 |
| EV-LMS | 100–150 | $72.00 | ⚠️ 28.7% | $79.00 |
| EV-PRE | 100–150 | $78.00 | ⚠️ 34.5% | $79.00 |

## 6. Sensibilidad del costo unitario (qué tanto cambia si los insumos reales son distintos)

- **Base**: supuestos de arriba (aroma real $1.667/g al 8%, velas/h estimadas).
- **Aroma 6%**: la dosis que Noemi usa en cempasúchil (~5.7%); baja costo pero puede oler poco (ver `produccion/formulas/`).
- **Aroma granel**: $0.90/g comprando 1 kg (ESTIMADO, pedir cotización), al 8%.
- **Mitad de velas/h**: si cada pieza tarda el doble de lo estimado (referencia real: cempasúchil 3 velas/h).
- **Figuras 50/50**: figuras con 50% parafina + 50% soya ($0.115/g), si esa es la fórmula que usa Noemi.

| SKU | Base | Aroma 6% | Aroma granel | Mitad velas/h | Figuras 50/50 | Margen directo base / mitad velas/h |
|---|---|---|---|---|---|---|
| EV-OSO | $55.94 | $49.36 | $43.83 | $64.34 | $62.85 | 36% / 26% |
| EV-JIR | $19.23 | $17.86 | $16.72 | $26.23 | $20.66 | 57% / 42% |
| EV-ELE | $35.36 | $31.58 | $28.41 | $42.36 | $39.33 | 38% / 26% |
| EV-DIN | $32.26 | $28.97 | $26.20 | $39.26 | $35.71 | 43% / 31% |
| EV-ANG | $23.93 | $21.83 | $20.07 | $30.93 | $26.14 | 58% / 46% |
| EV-FLO | $33.39 | $30.06 | $27.27 | $41.79 | $36.88 | 57% / 46% |
| EV-BUN | $41.28 | $36.87 | $33.17 | $49.68 | $45.91 | 53% / 43% |
| EV-GLO | $64.86 | $60.45 | $56.74 | $70.46 | $64.86 | 12% / 5% |
| EV-LMM | $33.56 | $32.05 | $30.79 | $39.16 | $33.56 | 35% / 25% |
| EV-LMS | $51.33 | $48.01 | $45.21 | $56.93 | $51.33 | 42% / 35% |
| EV-PRE | $51.06 | $49.55 | $47.08 | $61.56 | $51.06 | 56% / 46% |
| NV-VEN | $36.33 | $32.72 | $29.69 | $44.73 | $40.11 | 53% / 43% |
| NV-NAC | $18.75 | $17.42 | $16.30 | $25.75 | $20.14 | 71% / 60% |
| NV-PIN | $35.14 | $31.71 | $28.82 | $43.54 | $38.74 | 60% / 50% |
| NV-ARB | $22.39 | $20.64 | $19.17 | $29.39 | $24.23 | 74% / 65% |
| NV-BOR | $25.74 | $24.13 | $22.78 | $36.24 | $27.43 | 55% / 36% |
| NV-B12 | $323.63 | $304.31 | $288.08 | $468.53 | $343.92 | 16% / -22% |
| NV-ROM | $148.18 | $135.54 | $124.93 | $190.18 | $161.44 | 60% / 49% |

