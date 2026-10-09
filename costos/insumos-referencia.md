# Insumos: precios de referencia (México, oct-2026)

> **Estatus: REFERENCIA / ESTIMADO.** Precios tomados de anuncios en línea consultados el **09-oct-2026** (vía resultados de búsqueda; Mercado Libre bloquea la lectura directa, así que **verifica cada precio abriendo el anuncio**). Los anuncios cambian a diario, las promociones vencen y varios precios no indican si incluyen IVA o envío.
> **Noemi:** llena la columna "Precio real Noemi" con lo que pagas tú (ticket o factura, con envío incluido) y avísale a `costos-precios` para recalcular (`python3 costos/calculo_costos.py`).

## Tabla de insumos

| Insumo | Presentación | Precio | Precio por unidad útil | Fuente (URL) | Fecha consulta | Valor usado en el costeo | Precio real Noemi |
|---|---|---|---|---|---|---|---|
| Parafina (Malasia Plus) | 10 kg | $1,049 | $105/kg = **$0.105/g** | [ML listado parafina](https://listado.mercadolibre.com.mx/cera-de-parafina) | 09-oct-2026 | $0.105/g | |
| Parafina China 58/60 | 5 kg | $449 | $90/kg = $0.090/g | [ML listado parafina](https://listado.mercadolibre.com.mx/cera-de-parafina) | 09-oct-2026 | (escenario optimista ~$0.085/g en 25 kg: **verificar**) | |
| Parafina Malasia | 1 kg | $143 | $143/kg = $0.143/g | [ML Para Velas](https://www.mercadolibre.com.mx/pagina/paravelas) | 09-oct-2026 | escenario pesimista | |
| Cera de soya (Parafinas Tonalá) | 1 kg | $139.20 | $139/kg = **$0.139/g** | [ML Parafinas Tonalá](https://www.mercadolibre.com.mx/pagina/paravelas) (resultado de búsqueda) | 09-oct-2026 | $0.139/g | |
| Cera de soya a granel | caja 25 kg | sin precio 2026 (ref. 2021: USD 10.80/kg + IVA) | **verificar** | [Cosmos, cotización Ceras Universales 2021](https://www.cosmos.com.mx/foros/pregunta/buena-tarde-necesito-la-cotizacion-de-cera-de-soy-129646.html) | 09-oct-2026 | escenario optimista $0.110/g (**verificar**) | |
| Aceite de fragancia para velas (granel) | 1 kg | sin precio publicado; pedir cotización (Bell Flavors, Century Labs, Novaroma, Petrowax) | **verificar** | [Cosmos, fragancias para velas](https://www.cosmos.com.mx/producto/fragancias-para-velas-d1rq/) | 09-oct-2026 | **$0.90/g ESTIMADO** | |
| Esencia concentrada para veladora | 60 ml | $131.50 | ~$2.19/ml | [ML esencias](https://www.mercadolibre.com.mx/pagina/distribucionaromatica) (resultado de búsqueda) | 09-oct-2026 | escenario pesimista | |
| Esencia concentrada para veladora | 30 ml | $90.50 | ~$3.02/ml | ídem | 09-oct-2026 | — | |
| Fragancia liposoluble para velas | 50 g | $148 | $2.96/g | ídem (precio con descuento poco claro: **verificar**) | 09-oct-2026 | — | |
| Pabilo pre-encerado 15 cm | 100 pzs | $168 | **$1.68/pza** | [ML pabilos](https://listado.mercadolibre.com.mx/pabilos-para-velas) | 09-oct-2026 | $1.70/pza (confirmar que trae base metálica) | |
| Porta-pabilo (ficha metálica) | 100 pzs | $55–59 | $0.55–0.59/pza | [ML porta pabilos](https://listado.mercadolibre.com.mx/porta-pabilos-para-velas) | 09-oct-2026 | incluido en $1.70 | |
| Lata aluminio redonda para vela 4 oz | 24 pzs | $338.10 | $14.09/pza | [ML envases metálicos](https://listado.mercadolibre.com.mx/envases-metalicos-latas) | 09-oct-2026 | — | |
| Lata aluminio 6 cm **plateada** (Lume Mini) | — | no encontrada en esa medida | **verificar** | — | 09-oct-2026 | **$12 ESTIMADO** | |
| Lata aluminio 6 cm **dorada** (Lume Soja) | — | no encontrada en esa medida | **verificar** | — | 09-oct-2026 | **$14 ESTIMADO** | |
| Frasco vidrio cilíndrico 250 ml tapa dorada | 12 pzs | $255 | $21.25/pza | [ML frascos (HOPEMOB it-751)](https://listado.mercadolibre.com.mx/frascos-de-vidrio-1-oz) (resultado de búsqueda) | 09-oct-2026 | — | |
| Frasco vidrio ~6.7 cm tapa dorada (Glowing Glass, ~150 ml) | — | no encontrado en esa medida | **verificar** | [Cosmos, vasos para veladoras](https://www.cosmos.com.mx/producto/vasos-4jc7/vasos-para-veladoras-4szf/) | 09-oct-2026 | **$18 ESTIMADO** | |
| Bolsa celofán transparente con adhesivo 8×16 cm | 100 pzs | $90 regular ($44.50 en promo) | $0.45–0.90/pza | [ML bolsas para empaque](https://listado.mercadolibre.com.mx/bolsas-para-empaque) | 09-oct-2026 | $0.90/pza | |
| Bolsa de organza (~10×15 cm) | 100 pzs | sin precio MX encontrado | **verificar** | [Cosmos, bolsas de organza](https://www.cosmos.com.mx/producto/bolsas-de-organza-lsyj/) | 09-oct-2026 | **$2.00 ESTIMADO** | |
| Caja kraft microcorrugado 22×16.5×5.5 cm | 50 pzs | $365 | $7.30/pza | [ML cajas de cartón](https://listado.mercadolibre.com.mx/cajas-de-carton-para-comida) | 09-oct-2026 | $10 (caja + relleno, kits B12/ROM) | |
| Vinil PP adhesivo imprimible blanco brillante, carta | 20 hojas | $169 | $8.45/hoja ≈ $0.56/etiqueta (15 por hoja) | [ML vinil imprimible](https://listado.mercadolibre.com.mx/vinil-imprimible-brillante) | 09-oct-2026 | $0.75/etiqueta con tinta | |
| Vinil PP adhesivo imprimible, carta | 60 hojas | $465 | $7.75/hoja | ídem | 09-oct-2026 | — | |
| Colorante para velas SUNHUI (líquido) | 20 × 10 ml | $154.09 (promo) | ~$7.70/frasco; rinde ~0.5 kg de cera (**verificar dosis**) | [ML Para Velas](https://www.mercadolibre.com.mx/pagina/paravelas) | 09-oct-2026 | $0.015/g de parafina | |
| Colorante para velas SUNHUI | 30 pzs | $248 | ~$8.27/pza | ídem | 09-oct-2026 | — | |
| Base jabón de glicerina (Abreiko Yeko) | 1 kg | precio no visible | **verificar** | [ML tienda Abreiko](https://www.mercadolibre.com.mx/tienda/abreiko) | 09-oct-2026 | **$150/kg ESTIMADO** | |
| Pintura acrílica + barniz (figuras pintadas) | — | no investigado | **verificar** | — | — | $1.50 por figura ESTIMADO | |

## Precio por volumen (cuándo conviene comprar por mayoreo)

| Insumo | Menudeo | Volumen | Ahorro | Recomendación |
|---|---|---|---|---|
| Parafina | 1 kg $143/kg | 5 kg $90/kg · 10 kg $105/kg · 25 kg **verificar** | 27–37% | Con ≥ 3 kg/mes ya conviene el saco de 5–10 kg. Un pedido de 100 osos usa ~19 kg. |
| Fragancia | 60 ml ~$2,190/kg | 1 kg granel ~$900/kg (**estimado**) | ~60% | **Prioridad #1.** Comprar 1 kg por aroma de los 5–6 aromas más vendidos; los otros 30+ aromas solo sobre pedido. |
| Pabilo | 100 pzs $1.68/pza | 500–1,000 pzs **verificar** | — | Comprar por 500 en temporada. |
| Celofán | promo $0.45 / regular $0.90 | millar **verificar** | — | Comprar millar en 2 medidas (figura chica y grande). |
| Latas / frascos | paquete 12–24 | caja 100+ con proveedor de envases **verificar** | potencial 30%+ | Cotizar antes de aceptar pedidos de mayoreo de Glowing Glass / Lume. |

## Lo que Noemi debe capturar (en orden de impacto)
1. Precio real de **fragancia** (presentación, precio, proveedor) y % de carga que usa realmente.
2. **Peso real** de cada vela terminada (pesar 3 piezas por molde) — reemplaza los gramos estimados.
3. Precio real de **frasco Glowing Glass** y **latas** plateada/dorada.
4. **Velas por hora** reales por modelo (incluye desmoldar, pintar, etiquetar y empacar) y cuánto quieres pagarte por hora.
5. Precio real de parafina, soya, organza, base de glicerina, pintura y cajas kraft.
6. Costo real de envío que te cobra Mercado Libre en ventas ≥ $299 (simulador de la publicación).
