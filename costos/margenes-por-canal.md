# Márgenes por canal — Ananda Velas

> **Costos v3 (27-nov-2026): precios de cera, aroma, pabilo, jabón y porta pabilo REALES; fórmula real en figuras; peso real en Borrego, Venado, Pino y Árbol.** El resto de gramos, las velas por hora, envases y empaques siguen estimados. Comisiones de ML/TikTok tomadas de fuentes de terceros: **verificar** en el simulador de costos de Mercado Libre y en TikTok Seller Center antes de publicar. Se regenera con `python3 costos/calculo_costos.py`.

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

EV-PRE se evalúa a $115; con la promo de octubre ($95) el margen directo sería 50% y en ML Clásica 6%.

Costo unitario: cera + fragancia (8% del peso, $1.667/g) + colorante + mecha + contenedor/base/pintura + etiqueta + empaque + mano de obra ($80/h) + merma 5%. Detalle en `costos/plantilla-costeo.csv`.

## Hallazgos (v3, 27-nov-2026)

> **v3:** figuras de parafina con la fórmula real de Noemi (80% Malasia $106/kg + 15% soya de fusión $111/kg + 5% cera ámbar $120/kg) = **$107.45/kg de mezcla**; aroma 8%; colorante 1 g por vela (tope, $1.25). Pesos reales (1 pieza, confirmados por Noemi): Borrego 72 g, Venado 66 g, Árbol NV-ARB 114 g, Árbol delgado NV-ARB2 58 g y Piña NV-PIN2 45 g (los dos últimos son SKUs provisionales con precio **propuesto**). Pino NV-PIN sigue estimado: **pesar**. Soya de contenedor a $111/kg (confirmar que es la misma). Base de jabón $105/kg y porta pabilo $1 (pizarrón del proveedor, 27-nov).
>
> **Siguen estimados:** gramos de las figuras no pesadas, velas por hora, precio del aroma por kg (hoy frasco de 30 ml a $50), precio del colorante por gramo, latas/frascos y empaques. Las recomendaciones de texto de la v1 (9-oct) ya no aplican; las alertas de las secciones 5 y 6 se generan solas.
>
> Comisiones y envíos siguen siendo los del 9-oct (fuentes de terceros): **verificar** en el simulador de Mercado Libre y en TikTok Seller Center antes de publicar.

## 1. Costo unitario (v3) y margen en venta directa

| SKU | Producto | Cera g (supuesto) | Velas/h | Costo unitario | Menudeo | Margen directo |
|---|---|---|---|---|---|---|
| EV-OSO | Oso de Ternura | 188 g (10x9.5 cm, fondo 5.5, llenado 40%) | 10.00 | $60.34 | $87.00 | ⚠️ 30.6% |
| EV-JIR | Jirafa Africana | 39 g (9x4 cm, fondo 3, llenado 40%) | 12.00 | $21.18 | $45.00 | 52.9% |
| EV-ELE | Elefante Safari | 108 g (7x9.5 cm, fondo 4.5, llenado 40%) | 12.00 | $38.45 | $57.00 | ⚠️ 32.5% |
| EV-DIN | Dino T-Rex | 94 g (9.3x8 cm, fondo 4, llenado 35%) | 12.00 | $35.11 | $57.00 | ⚠️ 38.4% |
| EV-ANG | Ángeles Divinos | 60 g (6x7 cm, fondo 3.5, llenado 45%) | 12.00 | $26.23 | $57.00 | 54.0% |
| EV-FLO | Flowers On | 95 g (peonía Ø8 x 3.5 cm, llenado 60%) | 10.00 | $36.26 | $77.00 | 52.9% |
| EV-BUN | Bunny Happy | 126 g (10x7 cm, fondo 5, llenado 40%) | 10.00 | $44.67 | $87.00 | 48.7% |
| EV-GLO | Glowing Glass | 126 g (frasco Ø int 6.1, llenado a 4.8 cm) | 15.00 | $60.15 | $74.00 | ⚠️ 18.7% |
| EV-LMM | Lume Soja Mini | 43 g (lata Ø int 5.8, llenado a 1.8 cm) | 15.00 | $32.25 | $52.00 | ⚠️ 38.0% |
| EV-LMS | Lume Soja | 95 g (lata Ø int 5.8, llenado a 4.0 cm) | 15.00 | $47.89 | $88.00 | 45.6% |
| EV-PRE | Paquete Recuerdos | 43 g (vela = Lume Mini (43 g) + 2 jabones 25 g) | 8.00 | $47.39 | $115.00 | 58.8% |
| NV-VEN | Venado | 61.1 g (REAL 66 g terminado ÷ 1.08) | 10.00 | $28.74 | $78.00 | 63.2% |
| NV-NAC | Nacimiento | 38 g (6.2x4.5 cm, fondo 3, llenado 50%) | 12.00 | $20.68 | $65.00 | 68.2% |
| NV-PIN | Pino | 98 g (ESTIMADO cono 10 x Ø7.2, llenado 80% (PESAR)) | 10.00 | $38.06 | $87.00 | 56.3% |
| NV-ARB | Árbol Navideño | 105.6 g (REAL 114 g terminado (árbol grande de hojas) ÷ 1.08) | 12.00 | $38.58 | $85.00 | 54.6% |
| NV-ARB2 | Árbol Navideño versión delgada (58 g) | 53.7 g (REAL 58 g terminado ÷ 1.08) | 12.00 | $25.46 | $69.00 | 63.1% |
| NV-BOR | Borrego | 66.7 g (REAL 72 g terminado ÷ 1.08) | 8.00 | $33.04 | $57.00 | ⚠️ 42.0% |
| NV-B12 | Borregos de la Abundancia 12 pzs | 800.4 g (12 borregos x 72 g REAL ÷ 1.08) | 0.58 | $411.26 | $385.00 | ⚠️ -6.8% |
| NV-ROM | Rompecabezas Navideño | 361 g (4 piezas, Ø6.5 x 22 cm, llenado 55%) | 2.00 | $159.36 | $375.00 | 57.5% |
| NV-PIN2 | Piña de pino café | 41.7 g (REAL 45 g terminado ÷ 1.08) | 12.00 | $21.60 | $55.00 | 60.7% |


## 2. Pieza suelta por canal (precio menudeo)

| SKU | Canal | Precio | Comisión % | Cargo fijo | Envío | Neto | Margen $ | Margen % | Precio mín. 45% |
|---|---|---|---|---|---|---|---|---|---|
| EV-OSO | ML Clásica | $87.00 | 17.4% | $25.00 | $0.00 | $46.86 | $-13.48 | ⚠️ -15.5% | $259.00 |
| EV-OSO | ML Premium | $87.00 | 22.6% | $25.00 | $0.00 | $42.32 | $-18.02 | ⚠️ -20.7% | $434.00 |
| EV-OSO | TikTok Shop | $87.00 | 8.0% | $0.00 | $0.00 | $80.04 | $19.70 | ⚠️ 22.6% | $129.00 |
| EV-OSO | Tienda propia | $87.00 | 4.2% | $3.48 | $0.00 | $79.89 | $19.55 | ⚠️ 22.5% | $126.00 |
| EV-JIR | ML Clásica | $45.00 | 17.4% | $25.00 | $0.00 | $12.17 | $-9.01 | ⚠️ -20.0% | $137.00 |
| EV-JIR | ML Premium | $45.00 | 22.6% | $25.00 | $0.00 | $9.82 | $-11.36 | ⚠️ -25.2% | $180.00 |
| EV-JIR | TikTok Shop | $45.00 | 8.0% | $0.00 | $0.00 | $41.40 | $20.22 | ⚠️ 44.9% | $46.00 |
| EV-JIR | Tienda propia | $45.00 | 4.2% | $3.48 | $0.00 | $39.64 | $18.46 | ⚠️ 41.0% | $49.00 |
| EV-ELE | ML Clásica | $57.00 | 17.4% | $25.00 | $0.00 | $22.08 | $-16.37 | ⚠️ -28.7% | $201.00 |
| EV-ELE | ML Premium | $57.00 | 22.6% | $25.00 | $0.00 | $19.11 | $-19.35 | ⚠️ -33.9% | $234.00 |
| EV-ELE | TikTok Shop | $57.00 | 8.0% | $0.00 | $0.00 | $52.44 | $13.99 | ⚠️ 24.5% | $82.00 |
| EV-ELE | Tienda propia | $57.00 | 4.2% | $3.48 | $0.00 | $51.14 | $12.69 | ⚠️ 22.3% | $83.00 |
| EV-DIN | ML Clásica | $57.00 | 17.4% | $25.00 | $0.00 | $22.08 | $-13.03 | ⚠️ -22.9% | $192.00 |
| EV-DIN | ML Premium | $57.00 | 22.6% | $25.00 | $0.00 | $19.11 | $-16.01 | ⚠️ -28.1% | $223.00 |
| EV-DIN | TikTok Shop | $57.00 | 8.0% | $0.00 | $0.00 | $52.44 | $17.33 | ⚠️ 30.4% | $75.00 |
| EV-DIN | Tienda propia | $57.00 | 4.2% | $3.48 | $0.00 | $51.14 | $16.03 | ⚠️ 28.1% | $76.00 |
| EV-ANG | ML Clásica | $57.00 | 17.4% | $25.00 | $0.00 | $22.08 | $-4.15 | ⚠️ -7.3% | $169.00 |
| EV-ANG | ML Premium | $57.00 | 22.6% | $25.00 | $0.00 | $19.11 | $-7.12 | ⚠️ -12.5% | $196.00 |
| EV-ANG | TikTok Shop | $57.00 | 8.0% | $0.00 | $0.00 | $52.44 | $26.21 | 46.0% | $56.00 |
| EV-ANG | Tienda propia | $57.00 | 4.2% | $3.48 | $0.00 | $51.14 | $24.91 | ⚠️ 43.7% | $59.00 |
| EV-FLO | ML Clásica | $77.00 | 17.4% | $25.00 | $0.00 | $38.60 | $2.34 | ⚠️ 3.0% | $195.00 |
| EV-FLO | ML Premium | $77.00 | 22.6% | $25.00 | $0.00 | $34.58 | $-1.68 | ⚠️ -2.2% | $227.00 |
| EV-FLO | TikTok Shop | $77.00 | 8.0% | $0.00 | $0.00 | $70.84 | $34.58 | ⚠️ 44.9% | $78.00 |
| EV-FLO | Tienda propia | $77.00 | 4.2% | $3.48 | $0.00 | $70.30 | $34.05 | ⚠️ 44.2% | $79.00 |
| EV-BUN | ML Clásica | $87.00 | 17.4% | $25.00 | $0.00 | $46.86 | $2.20 | ⚠️ 2.5% | $218.00 |
| EV-BUN | ML Premium | $87.00 | 22.6% | $25.00 | $0.00 | $42.32 | $-2.35 | ⚠️ -2.7% | $253.00 |
| EV-BUN | TikTok Shop | $87.00 | 8.0% | $0.00 | $0.00 | $80.04 | $35.37 | ⚠️ 40.7% | $96.00 |
| EV-BUN | Tienda propia | $87.00 | 4.2% | $3.48 | $0.00 | $79.89 | $35.22 | ⚠️ 40.5% | $95.00 |
| EV-GLO | ML Clásica | $74.00 | 17.4% | $25.00 | $0.00 | $36.12 | $-24.03 | ⚠️ -32.5% | $259.00 |
| EV-GLO | ML Premium | $74.00 | 22.6% | $25.00 | $0.00 | $32.26 | $-27.89 | ⚠️ -37.7% | $433.00 |
| EV-GLO | TikTok Shop | $74.00 | 8.0% | $0.00 | $0.00 | $68.08 | $7.93 | ⚠️ 10.7% | $128.00 |
| EV-GLO | Tienda propia | $74.00 | 4.2% | $3.48 | $0.00 | $67.43 | $7.28 | ⚠️ 9.8% | $126.00 |
| EV-LMM | ML Clásica | $52.00 | 17.4% | $25.00 | $0.00 | $17.95 | $-14.30 | ⚠️ -27.5% | $185.00 |
| EV-LMM | ML Premium | $52.00 | 22.6% | $25.00 | $0.00 | $15.24 | $-17.01 | ⚠️ -32.7% | $214.00 |
| EV-LMM | TikTok Shop | $52.00 | 8.0% | $0.00 | $0.00 | $47.84 | $15.59 | ⚠️ 30.0% | $69.00 |
| EV-LMM | Tienda propia | $52.00 | 4.2% | $3.48 | $0.00 | $46.35 | $14.10 | ⚠️ 27.1% | $71.00 |
| EV-LMS | ML Clásica | $88.00 | 17.4% | $25.00 | $0.00 | $47.69 | $-0.20 | ⚠️ -0.2% | $226.00 |
| EV-LMS | ML Premium | $88.00 | 22.6% | $25.00 | $0.00 | $43.09 | $-4.80 | ⚠️ -5.5% | $263.00 |
| EV-LMS | TikTok Shop | $88.00 | 8.0% | $0.00 | $0.00 | $80.96 | $33.07 | ⚠️ 37.6% | $102.00 |
| EV-LMS | Tienda propia | $88.00 | 4.2% | $3.48 | $0.00 | $80.85 | $32.95 | ⚠️ 37.4% | $102.00 |
| EV-PRE | ML Clásica | $115.00 | 17.4% | $30.00 | $0.00 | $64.99 | $17.60 | ⚠️ 15.3% | $225.00 |
| EV-PRE | ML Premium | $115.00 | 22.6% | $30.00 | $0.00 | $58.99 | $11.60 | ⚠️ 10.1% | $261.00 |
| EV-PRE | TikTok Shop | $115.00 | 8.0% | $0.00 | $0.00 | $105.80 | $58.41 | 50.8% | $101.00 |
| EV-PRE | Tienda propia | $115.00 | 4.2% | $3.48 | $0.00 | $106.72 | $59.33 | 51.6% | $101.00 |
| NV-VEN | ML Clásica | $78.00 | 17.4% | $25.00 | $0.00 | $39.43 | $10.69 | ⚠️ 13.7% | $175.00 |
| NV-VEN | ML Premium | $78.00 | 22.6% | $25.00 | $0.00 | $35.36 | $6.62 | ⚠️ 8.5% | $204.00 |
| NV-VEN | TikTok Shop | $78.00 | 8.0% | $0.00 | $0.00 | $71.76 | $43.02 | 55.2% | $62.00 |
| NV-VEN | Tienda propia | $78.00 | 4.2% | $3.48 | $0.00 | $71.26 | $42.52 | 54.5% | $64.00 |
| NV-NAC | ML Clásica | $65.00 | 17.4% | $25.00 | $0.00 | $28.69 | $8.01 | ⚠️ 12.3% | $135.00 |
| NV-NAC | ML Premium | $65.00 | 22.6% | $25.00 | $0.00 | $25.30 | $4.61 | ⚠️ 7.1% | $179.00 |
| NV-NAC | TikTok Shop | $65.00 | 8.0% | $0.00 | $0.00 | $59.80 | $39.12 | 60.2% | $45.00 |
| NV-NAC | Tienda propia | $65.00 | 4.2% | $3.48 | $0.00 | $58.81 | $38.12 | 58.6% | $48.00 |
| NV-PIN | ML Clásica | $87.00 | 17.4% | $25.00 | $0.00 | $46.86 | $8.80 | ⚠️ 10.1% | $200.00 |
| NV-PIN | ML Premium | $87.00 | 22.6% | $25.00 | $0.00 | $42.32 | $4.26 | ⚠️ 4.9% | $232.00 |
| NV-PIN | TikTok Shop | $87.00 | 8.0% | $0.00 | $0.00 | $80.04 | $41.98 | 48.3% | $81.00 |
| NV-PIN | Tienda propia | $87.00 | 4.2% | $3.48 | $0.00 | $79.89 | $41.83 | 48.1% | $82.00 |
| NV-ARB | ML Clásica | $85.00 | 17.4% | $25.00 | $0.00 | $45.21 | $6.63 | ⚠️ 7.8% | $202.00 |
| NV-ARB | ML Premium | $85.00 | 22.6% | $25.00 | $0.00 | $40.77 | $2.19 | ⚠️ 2.6% | $234.00 |
| NV-ARB | TikTok Shop | $85.00 | 8.0% | $0.00 | $0.00 | $78.20 | $39.62 | 46.6% | $83.00 |
| NV-ARB | Tienda propia | $85.00 | 4.2% | $3.48 | $0.00 | $77.97 | $39.39 | 46.3% | $83.00 |
| NV-ARB2 | ML Clásica | $69.00 | 17.4% | $25.00 | $0.00 | $31.99 | $6.53 | ⚠️ 9.5% | $148.00 |
| NV-ARB2 | ML Premium | $69.00 | 22.6% | $25.00 | $0.00 | $28.39 | $2.93 | ⚠️ 4.3% | $193.00 |
| NV-ARB2 | TikTok Shop | $69.00 | 8.0% | $0.00 | $0.00 | $63.48 | $38.02 | 55.1% | $55.00 |
| NV-ARB2 | Tienda propia | $69.00 | 4.2% | $3.48 | $0.00 | $62.64 | $37.18 | 53.9% | $57.00 |
| NV-BOR | ML Clásica | $57.00 | 17.4% | $25.00 | $0.00 | $22.08 | $-10.96 | ⚠️ -19.2% | $187.00 |
| NV-BOR | ML Premium | $57.00 | 22.6% | $25.00 | $0.00 | $19.11 | $-13.94 | ⚠️ -24.4% | $217.00 |
| NV-BOR | TikTok Shop | $57.00 | 8.0% | $0.00 | $0.00 | $52.44 | $19.40 | ⚠️ 34.0% | $71.00 |
| NV-BOR | Tienda propia | $57.00 | 4.2% | $3.48 | $0.00 | $51.14 | $18.10 | ⚠️ 31.8% | $72.00 |
| NV-B12 | ML Clásica | $385.00 | 17.4% | $0.00 | $80.00 | $238.01 | $-173.25 | ⚠️ -45.0% | $1,307.00 |
| NV-B12 | ML Premium | $385.00 | 22.6% | $0.00 | $80.00 | $217.91 | $-193.34 | ⚠️ -50.2% | $1,518.00 |
| NV-B12 | TikTok Shop | $385.00 | 8.0% | $0.00 | $80.00 | $274.20 | $-137.06 | ⚠️ -35.6% | $1,046.00 |
| NV-B12 | Tienda propia | $385.00 | 4.2% | $3.48 | $120.00 | $245.44 | $-165.81 | ⚠️ -43.1% | $1,053.00 |
| NV-ROM | ML Clásica | $375.00 | 17.4% | $0.00 | $80.00 | $229.75 | $70.39 | ⚠️ 18.8% | $637.00 |
| NV-ROM | ML Premium | $375.00 | 22.6% | $0.00 | $80.00 | $210.18 | $50.81 | ⚠️ 13.6% | $740.00 |
| NV-ROM | TikTok Shop | $375.00 | 8.0% | $0.00 | $80.00 | $265.00 | $105.64 | ⚠️ 28.2% | $510.00 |
| NV-ROM | Tienda propia | $375.00 | 4.2% | $3.48 | $120.00 | $235.86 | $76.50 | ⚠️ 20.4% | $557.00 |
| NV-PIN2 | ML Clásica | $55.00 | 17.4% | $25.00 | $0.00 | $20.43 | $-1.17 | ⚠️ -2.1% | $138.00 |
| NV-PIN2 | ML Premium | $55.00 | 22.6% | $25.00 | $0.00 | $17.56 | $-4.04 | ⚠️ -7.4% | $181.00 |
| NV-PIN2 | TikTok Shop | $55.00 | 8.0% | $0.00 | $0.00 | $50.60 | $29.00 | 52.7% | $46.00 |
| NV-PIN2 | Tienda propia | $55.00 | 4.2% | $3.48 | $0.00 | $49.22 | $27.62 | 50.2% | $50.00 |

## 3. Kits para marketplace (ticket ≥ $299, sin cargo fijo de ML)

Kit = N piezas del mismo modelo a precio menudeo × N, en caja kraft (+$10 de caja; se quita el celofán individual: se conserva por simplicidad, sobreestima costo ~$1/pza). Al pasar de $299 el vendedor paga envío (supuesto $80 ML/TikTok, $120 tienda).

| Kit | Precio kit | Costo kit | Canal | Comisión % | Envío | Neto | Margen $ | Margen % | Precio mín. kit 45% (por pieza) |
|---|---|---|---|---|---|---|---|---|---|
| EV-OSO x4 | $348.00 | $251.36 | ML Clásica | 17.4% | $80.00 | $207.45 | $-43.91 | ⚠️ -12.6% | $882.00 ($220.50) |
| EV-OSO x4 | $348.00 | $251.36 | ML Premium | 22.6% | $80.00 | $189.28 | $-62.08 | ⚠️ -17.8% | $1,024.00 ($256.00) |
| EV-OSO x4 | $348.00 | $251.36 | TikTok Shop | 8.0% | $80.00 | $240.16 | $-11.20 | ⚠️ -3.2% | $706.00 ($176.50) |
| EV-JIR x8 | $360.00 | $179.46 | ML Clásica | 17.4% | $80.00 | $217.36 | $37.90 | ⚠️ 10.5% | $691.00 ($86.38) |
| EV-JIR x8 | $360.00 | $179.46 | ML Premium | 22.6% | $80.00 | $198.57 | $19.11 | ⚠️ 5.3% | $802.00 ($100.25) |
| EV-JIR x8 | $360.00 | $179.46 | TikTok Shop | 8.0% | $80.00 | $251.20 | $71.74 | ⚠️ 19.9% | $553.00 ($69.12) |
| EV-ELE x6 | $342.00 | $240.71 | ML Clásica | 17.4% | $80.00 | $202.49 | $-38.22 | ⚠️ -11.2% | $853.00 ($142.17) |
| EV-ELE x6 | $342.00 | $240.71 | ML Premium | 22.6% | $80.00 | $184.64 | $-56.07 | ⚠️ -16.4% | $991.00 ($165.17) |
| EV-ELE x6 | $342.00 | $240.71 | TikTok Shop | 8.0% | $80.00 | $234.64 | $-6.07 | ⚠️ -1.8% | $683.00 ($113.83) |
| EV-DIN x6 | $342.00 | $220.68 | ML Clásica | 17.4% | $80.00 | $202.49 | $-18.19 | ⚠️ -5.3% | $800.00 ($133.33) |
| EV-DIN x6 | $342.00 | $220.68 | ML Premium | 22.6% | $80.00 | $184.64 | $-36.04 | ⚠️ -10.5% | $929.00 ($154.83) |
| EV-DIN x6 | $342.00 | $220.68 | TikTok Shop | 8.0% | $80.00 | $234.64 | $13.96 | ⚠️ 4.1% | $640.00 ($106.67) |
| EV-ANG x6 | $342.00 | $167.38 | ML Clásica | 17.4% | $80.00 | $202.49 | $35.12 | ⚠️ 10.3% | $658.00 ($109.67) |
| EV-ANG x6 | $342.00 | $167.38 | ML Premium | 22.6% | $80.00 | $184.64 | $17.26 | ⚠️ 5.0% | $764.00 ($127.33) |
| EV-ANG x6 | $342.00 | $167.38 | TikTok Shop | 8.0% | $80.00 | $234.64 | $67.26 | ⚠️ 19.7% | $527.00 ($87.83) |
| EV-FLO x4 | $308.00 | $155.04 | ML Clásica | 17.4% | $80.00 | $174.41 | $19.37 | ⚠️ 6.3% | $626.00 ($156.50) |
| EV-FLO x4 | $308.00 | $155.04 | ML Premium | 22.6% | $80.00 | $158.33 | $3.29 | ⚠️ 1.1% | $726.00 ($181.50) |
| EV-FLO x4 | $308.00 | $155.04 | TikTok Shop | 8.0% | $80.00 | $203.36 | $48.32 | ⚠️ 15.7% | $501.00 ($125.25) |
| EV-BUN x4 | $348.00 | $188.66 | ML Clásica | 17.4% | $80.00 | $207.45 | $18.79 | ⚠️ 5.4% | $715.00 ($178.75) |
| EV-BUN x4 | $348.00 | $188.66 | ML Premium | 22.6% | $80.00 | $189.28 | $0.62 | ⚠️ 0.2% | $830.00 ($207.50) |
| EV-BUN x4 | $348.00 | $188.66 | TikTok Shop | 8.0% | $80.00 | $240.16 | $51.50 | ⚠️ 14.8% | $572.00 ($143.00) |
| EV-GLO x6 | $444.00 | $370.90 | ML Clásica | 17.4% | $80.00 | $286.74 | $-84.16 | ⚠️ -19.0% | $1,200.00 ($200.00) |
| EV-GLO x6 | $444.00 | $370.90 | ML Premium | 22.6% | $80.00 | $263.57 | $-107.33 | ⚠️ -24.2% | $1,393.00 ($232.17) |
| EV-GLO x6 | $444.00 | $370.90 | TikTok Shop | 8.0% | $80.00 | $328.48 | $-42.42 | ⚠️ -9.6% | $960.00 ($160.00) |
| EV-LMM x6 | $312.00 | $203.50 | ML Clásica | 17.4% | $80.00 | $177.71 | $-25.79 | ⚠️ -8.3% | $754.00 ($125.67) |
| EV-LMM x6 | $312.00 | $203.50 | ML Premium | 22.6% | $80.00 | $161.43 | $-42.08 | ⚠️ -13.5% | $876.00 ($146.00) |
| EV-LMM x6 | $312.00 | $203.50 | TikTok Shop | 8.0% | $80.00 | $207.04 | $3.54 | ⚠️ 1.1% | $604.00 ($100.67) |
| EV-LMS x4 | $352.00 | $201.57 | ML Clásica | 17.4% | $80.00 | $210.75 | $9.18 | ⚠️ 2.6% | $749.00 ($187.25) |
| EV-LMS x4 | $352.00 | $201.57 | ML Premium | 22.6% | $80.00 | $192.38 | $-9.19 | ⚠️ -2.6% | $870.00 ($217.50) |
| EV-LMS x4 | $352.00 | $201.57 | TikTok Shop | 8.0% | $80.00 | $243.84 | $42.27 | ⚠️ 12.0% | $600.00 ($150.00) |
| EV-PRE x4 | $460.00 | $199.55 | ML Clásica | 17.4% | $80.00 | $299.96 | $100.41 | ⚠️ 21.8% | $744.00 ($186.00) |
| EV-PRE x4 | $460.00 | $199.55 | ML Premium | 22.6% | $80.00 | $275.95 | $76.40 | ⚠️ 16.6% | $864.00 ($216.00) |
| EV-PRE x4 | $460.00 | $199.55 | TikTok Shop | 8.0% | $80.00 | $343.20 | $143.65 | ⚠️ 31.2% | $595.00 ($148.75) |
| NV-VEN x4 | $312.00 | $124.95 | ML Clásica | 17.4% | $80.00 | $177.71 | $52.76 | ⚠️ 16.9% | $546.00 ($136.50) |
| NV-VEN x4 | $312.00 | $124.95 | ML Premium | 22.6% | $80.00 | $161.43 | $36.47 | ⚠️ 11.7% | $633.00 ($158.25) |
| NV-VEN x4 | $312.00 | $124.95 | TikTok Shop | 8.0% | $80.00 | $207.04 | $82.09 | ⚠️ 26.3% | $299.00 ($74.75) |
| NV-NAC x6 | $390.00 | $134.11 | ML Clásica | 17.4% | $80.00 | $242.14 | $108.03 | ⚠️ 27.7% | $570.00 ($95.00) |
| NV-NAC x6 | $390.00 | $134.11 | ML Premium | 22.6% | $80.00 | $221.78 | $87.67 | ⚠️ 22.5% | $662.00 ($110.33) |
| NV-NAC x6 | $390.00 | $134.11 | TikTok Shop | 8.0% | $80.00 | $278.80 | $144.69 | ⚠️ 37.1% | $299.00 ($49.83) |
| NV-PIN x4 | $348.00 | $162.24 | ML Clásica | 17.4% | $80.00 | $207.45 | $45.21 | ⚠️ 13.0% | $645.00 ($161.25) |
| NV-PIN x4 | $348.00 | $162.24 | ML Premium | 22.6% | $80.00 | $189.28 | $27.05 | ⚠️ 7.8% | $749.00 ($187.25) |
| NV-PIN x4 | $348.00 | $162.24 | TikTok Shop | 8.0% | $80.00 | $240.16 | $77.92 | ⚠️ 22.4% | $516.00 ($129.00) |
| NV-ARB x4 | $340.00 | $164.32 | ML Clásica | 17.4% | $80.00 | $200.84 | $36.52 | ⚠️ 10.7% | $650.00 ($162.50) |
| NV-ARB x4 | $340.00 | $164.32 | ML Premium | 22.6% | $80.00 | $183.09 | $18.77 | ⚠️ 5.5% | $755.00 ($188.75) |
| NV-ARB x4 | $340.00 | $164.32 | TikTok Shop | 8.0% | $80.00 | $232.80 | $68.48 | ⚠️ 20.1% | $520.00 ($130.00) |
| NV-ARB2 x6 | $414.00 | $162.75 | ML Clásica | 17.4% | $80.00 | $261.96 | $99.21 | ⚠️ 24.0% | $646.00 ($107.67) |
| NV-ARB2 x6 | $414.00 | $162.75 | ML Premium | 22.6% | $80.00 | $240.35 | $77.60 | ⚠️ 18.7% | $750.00 ($125.00) |
| NV-ARB2 x6 | $414.00 | $162.75 | TikTok Shop | 8.0% | $80.00 | $300.88 | $138.13 | ⚠️ 33.4% | $517.00 ($86.17) |
| NV-BOR x6 | $342.00 | $208.25 | ML Clásica | 17.4% | $80.00 | $202.49 | $-5.76 | ⚠️ -1.7% | $767.00 ($127.83) |
| NV-BOR x6 | $342.00 | $208.25 | ML Premium | 22.6% | $80.00 | $184.64 | $-23.61 | ⚠️ -6.9% | $891.00 ($148.50) |
| NV-BOR x6 | $342.00 | $208.25 | TikTok Shop | 8.0% | $80.00 | $234.64 | $26.39 | ⚠️ 7.7% | $614.00 ($102.33) |
| NV-PIN2 x6 | $330.00 | $139.62 | ML Clásica | 17.4% | $80.00 | $192.58 | $52.96 | ⚠️ 16.0% | $585.00 ($97.50) |
| NV-PIN2 x6 | $330.00 | $139.62 | ML Premium | 22.6% | $80.00 | $175.35 | $35.74 | ⚠️ 10.8% | $679.00 ($113.17) |
| NV-PIN2 x6 | $330.00 | $139.62 | TikTok Shop | 8.0% | $80.00 | $223.60 | $83.98 | ⚠️ 25.4% | $299.00 ($49.83) |

## 4. Mayoreo directo (WhatsApp/Instagram, 0% comisión, envío por cuenta del cliente)

| SKU | Costo unitario | 11–50 | Margen | 51–99 | Margen | 100–150 | Margen |
|---|---|---|---|---|---|---|---|
| EV-OSO | $60.34 | $78.00 | ⚠️ 22.6% | $75.00 | ⚠️ 19.5% | $71.00 | ⚠️ 15.0% |
| EV-JIR | $21.18 | $40.00 | 47.0% | $38.00 | 44.3% | $36.00 | 41.2% |
| EV-ELE | $38.45 | $51.00 | ⚠️ 24.6% | $49.50 | ⚠️ 22.3% | $46.00 | ⚠️ 16.4% |
| EV-DIN | $35.11 | $51.00 | ⚠️ 31.1% | $49.50 | ⚠️ 29.1% | $46.00 | ⚠️ 23.7% |
| EV-ANG | $26.23 | $51.00 | 48.6% | $49.50 | 47.0% | $46.00 | 43.0% |
| EV-FLO | $36.26 | $69.50 | 47.8% | $67.00 | 45.9% | $63.00 | 42.4% |
| EV-BUN | $44.67 | $78.00 | 42.7% | $75.50 | 40.8% | $71.00 | 37.1% |
| EV-GLO | $60.15 | $66.50 | ⚠️ 9.5% | $64.00 | ⚠️ 6.0% | $60.00 | ⚠️ -0.3% |
| EV-LMM | $32.25 | $46.50 | ⚠️ 30.6% | $45.00 | ⚠️ 28.3% | $42.00 | ⚠️ 23.2% |
| EV-LMS | $47.89 | $79.00 | 39.4% | $76.50 | 37.4% | $72.00 | ⚠️ 33.5% |
| EV-PRE | $47.39 | $86.00 | 44.9% | $83.00 | 42.9% | $78.00 | 39.2% |
| NV-VEN | $28.74 | $70.00 | 58.9% | $67.00 | 57.1% | $62.00 | 53.6% |
| NV-NAC | $20.68 | $58.00 | 64.3% | $55.00 | 62.4% | $50.00 | 58.6% |
| NV-PIN | $38.06 | $78.00 | 51.2% | $75.00 | 49.3% | $69.00 | 44.8% |
| NV-ARB | $38.58 | $76.00 | 49.2% | $73.00 | 47.1% | $68.00 | 43.3% |
| NV-ARB2 | $25.46 | $62.00 | 58.9% | $59.00 | 56.8% | $55.00 | 53.7% |
| NV-BOR | $33.04 | $51.00 | 35.2% | $49.00 | ⚠️ 32.6% | $45.00 | ⚠️ 26.6% |
| NV-PIN2 | $21.60 | $49.00 | 55.9% | $47.00 | 54.0% | $44.00 | 50.9% |

## 5. Alertas ⚠️ y precio mínimo recomendado

Fórmula (README): `Precio = (costo + envío + cargo fijo + margen$) ÷ (1 − %comisión)` con margen$ = 45% del precio (menudeo) o 35% (mayoreo) ⇒ `Precio mínimo = (costo + envío + cargo fijo) ÷ (1 − %comisión − margen%)`.

### Menudeo pieza suelta con margen < 45%

| SKU | Canal | Precio actual | Margen | Precio mínimo para 45% |
|---|---|---|---|---|
| EV-OSO | ML Clásica | $87.00 | ⚠️ -15.5% | $259.00 |
| EV-OSO | ML Premium | $87.00 | ⚠️ -20.7% | $434.00 |
| EV-OSO | TikTok Shop | $87.00 | ⚠️ 22.6% | $129.00 |
| EV-OSO | Tienda propia | $87.00 | ⚠️ 22.5% | $126.00 |
| EV-JIR | ML Clásica | $45.00 | ⚠️ -20.0% | $137.00 |
| EV-JIR | ML Premium | $45.00 | ⚠️ -25.2% | $180.00 |
| EV-JIR | TikTok Shop | $45.00 | ⚠️ 44.9% | $46.00 |
| EV-JIR | Tienda propia | $45.00 | ⚠️ 41.0% | $49.00 |
| EV-ELE | ML Clásica | $57.00 | ⚠️ -28.7% | $201.00 |
| EV-ELE | ML Premium | $57.00 | ⚠️ -33.9% | $234.00 |
| EV-ELE | TikTok Shop | $57.00 | ⚠️ 24.5% | $82.00 |
| EV-ELE | Tienda propia | $57.00 | ⚠️ 22.3% | $83.00 |
| EV-DIN | ML Clásica | $57.00 | ⚠️ -22.9% | $192.00 |
| EV-DIN | ML Premium | $57.00 | ⚠️ -28.1% | $223.00 |
| EV-DIN | TikTok Shop | $57.00 | ⚠️ 30.4% | $75.00 |
| EV-DIN | Tienda propia | $57.00 | ⚠️ 28.1% | $76.00 |
| EV-ANG | ML Clásica | $57.00 | ⚠️ -7.3% | $169.00 |
| EV-ANG | ML Premium | $57.00 | ⚠️ -12.5% | $196.00 |
| EV-ANG | Tienda propia | $57.00 | ⚠️ 43.7% | $59.00 |
| EV-FLO | ML Clásica | $77.00 | ⚠️ 3.0% | $195.00 |
| EV-FLO | ML Premium | $77.00 | ⚠️ -2.2% | $227.00 |
| EV-FLO | TikTok Shop | $77.00 | ⚠️ 44.9% | $78.00 |
| EV-FLO | Tienda propia | $77.00 | ⚠️ 44.2% | $79.00 |
| EV-BUN | ML Clásica | $87.00 | ⚠️ 2.5% | $218.00 |
| EV-BUN | ML Premium | $87.00 | ⚠️ -2.7% | $253.00 |
| EV-BUN | TikTok Shop | $87.00 | ⚠️ 40.7% | $96.00 |
| EV-BUN | Tienda propia | $87.00 | ⚠️ 40.5% | $95.00 |
| EV-GLO | ML Clásica | $74.00 | ⚠️ -32.5% | $259.00 |
| EV-GLO | ML Premium | $74.00 | ⚠️ -37.7% | $433.00 |
| EV-GLO | TikTok Shop | $74.00 | ⚠️ 10.7% | $128.00 |
| EV-GLO | Tienda propia | $74.00 | ⚠️ 9.8% | $126.00 |
| EV-LMM | ML Clásica | $52.00 | ⚠️ -27.5% | $185.00 |
| EV-LMM | ML Premium | $52.00 | ⚠️ -32.7% | $214.00 |
| EV-LMM | TikTok Shop | $52.00 | ⚠️ 30.0% | $69.00 |
| EV-LMM | Tienda propia | $52.00 | ⚠️ 27.1% | $71.00 |
| EV-LMS | ML Clásica | $88.00 | ⚠️ -0.2% | $226.00 |
| EV-LMS | ML Premium | $88.00 | ⚠️ -5.5% | $263.00 |
| EV-LMS | TikTok Shop | $88.00 | ⚠️ 37.6% | $102.00 |
| EV-LMS | Tienda propia | $88.00 | ⚠️ 37.4% | $102.00 |
| EV-PRE | ML Clásica | $115.00 | ⚠️ 15.3% | $225.00 |
| EV-PRE | ML Premium | $115.00 | ⚠️ 10.1% | $261.00 |
| NV-VEN | ML Clásica | $78.00 | ⚠️ 13.7% | $175.00 |
| NV-VEN | ML Premium | $78.00 | ⚠️ 8.5% | $204.00 |
| NV-NAC | ML Clásica | $65.00 | ⚠️ 12.3% | $135.00 |
| NV-NAC | ML Premium | $65.00 | ⚠️ 7.1% | $179.00 |
| NV-PIN | ML Clásica | $87.00 | ⚠️ 10.1% | $200.00 |
| NV-PIN | ML Premium | $87.00 | ⚠️ 4.9% | $232.00 |
| NV-ARB | ML Clásica | $85.00 | ⚠️ 7.8% | $202.00 |
| NV-ARB | ML Premium | $85.00 | ⚠️ 2.6% | $234.00 |
| NV-ARB2 | ML Clásica | $69.00 | ⚠️ 9.5% | $148.00 |
| NV-ARB2 | ML Premium | $69.00 | ⚠️ 4.3% | $193.00 |
| NV-BOR | ML Clásica | $57.00 | ⚠️ -19.2% | $187.00 |
| NV-BOR | ML Premium | $57.00 | ⚠️ -24.4% | $217.00 |
| NV-BOR | TikTok Shop | $57.00 | ⚠️ 34.0% | $71.00 |
| NV-BOR | Tienda propia | $57.00 | ⚠️ 31.8% | $72.00 |
| NV-B12 | ML Clásica | $385.00 | ⚠️ -45.0% | $1,307.00 |
| NV-B12 | ML Premium | $385.00 | ⚠️ -50.2% | $1,518.00 |
| NV-B12 | TikTok Shop | $385.00 | ⚠️ -35.6% | $1,046.00 |
| NV-B12 | Tienda propia | $385.00 | ⚠️ -43.1% | $1,053.00 |
| NV-ROM | ML Clásica | $375.00 | ⚠️ 18.8% | $637.00 |
| NV-ROM | ML Premium | $375.00 | ⚠️ 13.6% | $740.00 |
| NV-ROM | TikTok Shop | $375.00 | ⚠️ 28.2% | $510.00 |
| NV-ROM | Tienda propia | $375.00 | ⚠️ 20.4% | $557.00 |
| NV-PIN2 | ML Clásica | $55.00 | ⚠️ -2.1% | $138.00 |
| NV-PIN2 | ML Premium | $55.00 | ⚠️ -7.4% | $181.00 |

### Mayoreo con margen < 35%

| SKU | Nivel | Precio actual | Margen | Precio mínimo para 35% |
|---|---|---|---|---|
| EV-OSO | 11–50 | $78.00 | ⚠️ 22.6% | $93.00 |
| EV-OSO | 51–99 | $75.00 | ⚠️ 19.5% | $93.00 |
| EV-OSO | 100–150 | $71.00 | ⚠️ 15.0% | $93.00 |
| EV-ELE | 11–50 | $51.00 | ⚠️ 24.6% | $60.00 |
| EV-ELE | 51–99 | $49.50 | ⚠️ 22.3% | $60.00 |
| EV-ELE | 100–150 | $46.00 | ⚠️ 16.4% | $60.00 |
| EV-DIN | 11–50 | $51.00 | ⚠️ 31.1% | $55.00 |
| EV-DIN | 51–99 | $49.50 | ⚠️ 29.1% | $55.00 |
| EV-DIN | 100–150 | $46.00 | ⚠️ 23.7% | $55.00 |
| EV-GLO | 11–50 | $66.50 | ⚠️ 9.5% | $93.00 |
| EV-GLO | 51–99 | $64.00 | ⚠️ 6.0% | $93.00 |
| EV-GLO | 100–150 | $60.00 | ⚠️ -0.3% | $93.00 |
| EV-LMM | 11–50 | $46.50 | ⚠️ 30.6% | $50.00 |
| EV-LMM | 51–99 | $45.00 | ⚠️ 28.3% | $50.00 |
| EV-LMM | 100–150 | $42.00 | ⚠️ 23.2% | $50.00 |
| EV-LMS | 100–150 | $72.00 | ⚠️ 33.5% | $74.00 |
| NV-BOR | 51–99 | $49.00 | ⚠️ 32.6% | $51.00 |
| NV-BOR | 100–150 | $45.00 | ⚠️ 26.6% | $51.00 |

## 6. Sensibilidad del costo unitario (qué tanto cambia si los insumos reales son distintos)

- **Base**: supuestos de arriba (aroma real $1.667/g al 8%, velas/h estimadas).
- **Aroma 6%**: la dosis que Noemi usa en cempasúchil (~5.7%); baja costo pero puede oler poco (ver `produccion/formulas/`).
- **Aroma granel**: $0.90/g comprando 1 kg (ESTIMADO, pedir cotización), al 8%.
- **Mitad de velas/h**: si cada pieza tarda el doble de lo estimado (referencia real: cempasúchil 3 velas/h).
- **Malasia $97**: precio por volumen que aparece en el pizarrón ("-97").

| SKU | Base | Aroma 6% | Aroma granel | Mitad velas/h | Malasia $97 | Margen directo base / mitad velas/h |
|---|---|---|---|---|---|---|
| EV-OSO | $60.34 | $53.76 | $48.23 | $68.74 | $58.92 | 31% / 21% |
| EV-JIR | $21.18 | $19.82 | $18.67 | $28.18 | $20.89 | 53% / 37% |
| EV-ELE | $38.45 | $34.67 | $31.50 | $45.45 | $37.64 | 33% / 20% |
| EV-DIN | $35.11 | $31.82 | $29.06 | $42.11 | $34.40 | 38% / 26% |
| EV-ANG | $26.23 | $24.13 | $22.37 | $33.23 | $25.78 | 54% / 42% |
| EV-FLO | $36.26 | $32.93 | $30.14 | $44.66 | $35.54 | 53% / 42% |
| EV-BUN | $44.67 | $40.26 | $36.55 | $53.07 | $43.71 | 49% / 39% |
| EV-GLO | $60.15 | $55.74 | $52.04 | $65.75 | $60.15 | 19% / 11% |
| EV-LMM | $32.25 | $30.75 | $29.48 | $37.85 | $32.25 | 38% / 27% |
| EV-LMS | $47.89 | $44.57 | $41.77 | $53.49 | $47.89 | 46% / 39% |
| EV-PRE | $47.39 | $45.88 | $43.41 | $57.89 | $47.39 | 59% / 50% |
| NV-VEN | $28.74 | $26.60 | $24.80 | $37.14 | $28.28 | 63% / 52% |
| NV-NAC | $20.68 | $19.35 | $18.24 | $27.68 | $20.40 | 68% / 57% |
| NV-PIN | $38.06 | $34.63 | $31.75 | $46.46 | $37.32 | 56% / 47% |
| NV-ARB | $38.58 | $34.88 | $31.78 | $45.58 | $37.78 | 55% / 46% |
| NV-ARB2 | $25.46 | $23.58 | $22.00 | $32.46 | $25.05 | 63% / 53% |
| NV-BOR | $33.04 | $30.71 | $28.75 | $43.54 | $32.54 | 42% / 24% |
| NV-B12 | $411.26 | $383.24 | $359.71 | $556.16 | $405.21 | -7% / -44% |
| NV-ROM | $159.36 | $146.73 | $136.11 | $201.36 | $156.63 | 58% / 46% |
| NV-PIN2 | $21.60 | $20.14 | $18.92 | $28.60 | $21.29 | 61% / 48% |

