#!/usr/bin/env python3
"""Cálculo reproducible de costos unitarios y márgenes por canal — Ananda Velas.

TODO ES ESTIMADO hasta que Noemi capture costos reales (ver costos/insumos-referencia.md).
Para recalcular: cambia los supuestos de las secciones 1-4 y ejecuta
    python3 costos/calculo_costos.py
Genera: costos/plantilla-costeo.csv y costos/margenes-por-canal.md
"""
import csv
import math
import os

AQUI = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# 1. PRECIOS DE INSUMOS (MXN, estimados; fuente en insumos-referencia.md)
# ---------------------------------------------------------------------------
INS = {
    "parafina_g": 105 / 1000,     # Parafina Malasia 10 kg $1,049 (ML) -> $105/kg
    "soya_g": 139.20 / 1000,      # Cera de soya 1 kg $139.20 (ML Parafinas Tonalá)
    "fragancia_g": 900 / 1000,    # ESTIMADO $900/kg a granel (verificar; en frasco 60 ml sale ~$2,190/kg)
    "colorante_g_cera": 0.015,    # 20 frascos 10 ml $154 -> ~$7.7 por frasco, rinde ~0.5 kg cera
    "mecha": 1.70,                # 100 pabilos pre-encerados $168 (ML)
    "lata_plateada": 12.00,       # ESTIMADO (ref. 24 latas 4 oz $338 = $14.09)
    "lata_dorada": 14.00,         # ESTIMADO (ref. idem)
    "frasco_tapa_dorada": 18.00,  # ESTIMADO (ref. 12 frascos 250 ml tapa dorada $255 = $21.25; GLO es más chico)
    "celofan": 0.90,              # 100 bolsas $90 precio regular ($44.50 en promo)
    "organza": 2.00,              # ESTIMADO, sin precio MX verificado
    "etiqueta": 0.75,             # hoja vinil carta $8.45 / ~15 etiquetas + tinta
    "liston_cierre": 0.50,        # rafia/listón para cerrar celofán (estimado)
    "caja_kraft_kit": 10.00,      # ESTIMADO (ref. 50 cajas kraft 22x16.5x5.5 $365 = $7.30) + relleno
    "jabon_base_g": 150 / 1000,   # ESTIMADO $150/kg base glicerina (verificar)
    "pintura_figura": 1.50,       # acrílico + barniz por figura pintada (estimado)
    "tarjeta_oracion": 0.50,      # tarjetita impresa (B12: 12 pzs)
}

FRAG_PCT = 0.08     # fragancia = 8% del peso de cera
MERMA = 0.05        # merma 5% sobre (materiales + mano de obra)
MO_HORA = 80.0      # $/hora que se paga Noemi

# ---------------------------------------------------------------------------
# 2. PRODUCTOS: gramos de cera estimados + extras + velas/hora
#    gramos = alto x ancho x fondo(supuesto) x factor_llenado x densidad 0.9 g/cm3
# ---------------------------------------------------------------------------
DENS = 0.9

def caja(alto, ancho, fondo, llenado):
    return round(alto * ancho * fondo * llenado * DENS)

def cilindro(alto_llenado, diam_int, llenado=1.0):
    return round(math.pi * (diam_int / 2) ** 2 * alto_llenado * llenado * DENS)

def cono(alto, diam, llenado):
    return round(math.pi * (diam / 2) ** 2 * alto / 3 * llenado * DENS)

# (sku, nombre, cera, gramos, supuesto_gramos, extras{insumo:cant}, velas_por_hora, precios[men,11-50,51-99,100-150])
P = [
    ("EV-OSO", "Oso de Ternura", "parafina", caja(10, 9.5, 5.5, .40), "10x9.5 cm, fondo 5.5, llenado 40%",
        {"celofan": 1, "etiqueta": 1, "liston_cierre": 1}, 10, [87, 78, 75, 71]),
    ("EV-JIR", "Jirafa Africana", "parafina", caja(9, 4, 3, .40), "9x4 cm, fondo 3, llenado 40%",
        {"celofan": 1, "etiqueta": 1, "liston_cierre": 1}, 12, [45, 40, 38, 36]),
    ("EV-ELE", "Elefante Safari", "parafina", caja(7, 9.5, 4.5, .40), "7x9.5 cm, fondo 4.5, llenado 40%",
        {"celofan": 1, "etiqueta": 1, "liston_cierre": 1}, 12, [57, 51, 49.5, 46]),
    ("EV-DIN", "Dino T-Rex", "parafina", caja(9.3, 8, 4, .35), "9.3x8 cm, fondo 4, llenado 35%",
        {"celofan": 1, "etiqueta": 1, "liston_cierre": 1}, 12, [57, 51, 49.5, 46]),
    ("EV-ANG", "Ángeles Divinos", "parafina", caja(6, 7, 3.5, .45), "6x7 cm, fondo 3.5, llenado 45%",
        {"celofan": 1, "etiqueta": 1, "liston_cierre": 1}, 12, [57, 51, 49.5, 46]),
    ("EV-FLO", "Flowers On", "parafina", cilindro(3.5, 8, .60), "peonía Ø8 x 3.5 cm, llenado 60%",
        {"celofan": 1, "etiqueta": 1, "liston_cierre": 1}, 10, [77, 69.5, 67, 63]),
    ("EV-BUN", "Bunny Happy", "parafina", caja(10, 7, 5, .40), "10x7 cm, fondo 5, llenado 40%",
        {"celofan": 1, "etiqueta": 1, "liston_cierre": 1}, 10, [87, 78, 75.5, 71]),
    ("EV-GLO", "Glowing Glass", "soya", cilindro(4.8, 6.1), "frasco Ø int 6.1, llenado a 4.8 cm",
        {"frasco_tapa_dorada": 1, "etiqueta": 2}, 15, [74, 66.5, 64, 60]),
    ("EV-LMM", "Lume Soja Mini", "soya", cilindro(1.8, 5.8), "lata Ø int 5.8, llenado a 1.8 cm",
        {"lata_plateada": 1, "etiqueta": 2}, 15, [52, 46.5, 45, 42]),
    ("EV-LMS", "Lume Soja", "soya", cilindro(4.0, 5.8), "lata Ø int 5.8, llenado a 4.0 cm",
        {"lata_dorada": 1, "etiqueta": 2}, 15, [88, 79, 76.5, 72]),
    ("EV-PRE", "Paquete Recuerdos", "soya", cilindro(1.8, 5.8), "vela = Lume Mini (43 g) + 2 jabones 25 g",
        {"lata_plateada": 1, "etiqueta": 2, "organza": 1, "jabon_base_g": 50, "fragancia_g": 1.5}, 8, [115, 86, 83, 78]),
    ("NV-VEN", "Venado", "parafina", caja(9.5, 7.5, 4, .40), "9.5x7.5 cm, fondo 4, llenado 40%",
        {"celofan": 1, "etiqueta": 1, "liston_cierre": 2}, 10, [78, 70, 67, 62]),
    ("NV-NAC", "Nacimiento", "parafina", caja(6.2, 4.5, 3, .50), "6.2x4.5 cm, fondo 3, llenado 50%",
        {"celofan": 1, "etiqueta": 1, "liston_cierre": 1}, 12, [65, 58, 55, 50]),
    ("NV-PIN", "Pino", "parafina", cono(10, 7.2, .80), "cono 10 x Ø7.2, llenado 80%",
        {"celofan": 1, "etiqueta": 1, "liston_cierre": 1, "pintura_figura": .3}, 10, [87, 78, 75, 69]),
    ("NV-ARB", "Árbol Navideño", "parafina", cono(10, 5, .85), "cono 10 x Ø5, llenado 85%",
        {"celofan": 1, "etiqueta": 1, "liston_cierre": 1, "pintura_figura": .3}, 12, [85, 76, 73, 68]),
    ("NV-BOR", "Borrego", "parafina", caja(6.5, 4.5, 3.5, .50), "6.5x4.5 cm, fondo 3.5, llenado 50%",
        {"celofan": 1, "etiqueta": 1, "liston_cierre": 1, "pintura_figura": 1}, 8, [57, 51, 49, 45]),
    ("NV-B12", "Borregos de la Abundancia 12 pzs", "parafina", 12 * caja(6.5, 4.5, 3.5, .50), "12 borregos x 46 g",
        {"caja_kraft_kit": 1, "etiqueta": 1, "tarjeta_oracion": 12, "pintura_figura": 12, "mecha_extra": 11}, 8 / 12 / 1.15, [385]),
    ("NV-ROM", "Rompecabezas Navideño", "parafina", cilindro(22, 6.5, .55), "4 piezas, Ø6.5 x 22 cm, llenado 55%",
        {"caja_kraft_kit": 1, "etiqueta": 1, "pintura_figura": 4, "mecha_extra": 0}, 2, [375]),
]
# Notas velas/hora: incluye colado, desmolde, acabado, etiquetado y empaque (por lote).
# NV-B12: 12 borregos a 8/h + 15% de tiempo de armado de caja = 0.57 kits/h.
# NV-ROM: 2 juegos/h (4 piezas pintadas por juego).

# ---------------------------------------------------------------------------
# 3. CANALES (verificar en fuente oficial)
# ---------------------------------------------------------------------------
IVA = 1.16
CANALES = {
    # nombre: (% comisión efectiva, cargo fijo por venta, envío que paga vendedor si ticket >= umbral)
    "ML Clásica": (0.15 * IVA, None, 80.0),   # 15% Hogar (rango 8-16%) + IVA; cargo fijo por tramo
    "ML Premium": (0.195 * IVA, None, 80.0),  # 19.5% (rango 12.5-20.5%) + IVA
    "TikTok Shop": (0.08, 0.0, 80.0),         # 6% comisión (incluye impuestos) + 2% procesamiento (verificar)
    "Tienda propia": (0.036 * IVA, 3.0 * IVA, 120.0),  # pasarela 3.6% + $3 + IVA; guía paquetería ~$120
}
UMBRAL_ENVIO = 299  # >= $299: envío gratis lo absorbe el vendedor (ML obligatorio; en otros canales es política propia)

def cargo_fijo_ml(precio):
    if precio >= 299:
        return 0.0
    if precio < 99:
        return 25.0
    if precio < 149:
        return 30.0
    return 37.0

def costos_canal(canal, precio):
    pct, fijo, envio_vend = CANALES[canal]
    if fijo is None:
        fijo = cargo_fijo_ml(precio)
    envio = envio_vend if precio >= UMBRAL_ENVIO else 0.0
    return pct, fijo, envio

def neto(canal, precio):
    pct, fijo, envio = costos_canal(canal, precio)
    return precio - precio * pct - fijo - envio, pct, fijo, envio

def precio_minimo(canal, costo, margen_obj, forzar_envio=False):
    """Precio mínimo = (costo + envío + cargo fijo) / (1 - %comisión - margen%).
    Se evalúa cada tramo (cargo fijo ML / umbral de envío) y se devuelve el menor precio que cae en su propio tramo.
    forzar_envio=True: el vendedor ofrece envío gratis aunque el ticket sea < $299 (no aplica a ML)."""
    pct, fijo_c, envio_vend = CANALES[canal]
    tramos = [(0, 99, 25.0), (99, 149, 30.0), (149, 299, 37.0), (299, 10**9, 0.0)]
    candidatos = []
    for lo, hi, fijo_ml in tramos:
        fijo = fijo_ml if fijo_c is None else fijo_c
        envio = envio_vend if (lo >= 299 or (forzar_envio and fijo_c is not None)) else 0.0
        p = (costo + envio + fijo) / (1 - pct - margen_obj)
        if p < lo:
            p = lo  # el tramo exige un precio mayor; verificar margen
            if (p - p * pct - fijo - envio - costo) / p < margen_obj:
                continue
        if lo <= p < hi:
            candidatos.append(p)
    return math.ceil(min(candidatos))

# ---------------------------------------------------------------------------
# 4. CÁLCULO DE COSTO UNITARIO
# ---------------------------------------------------------------------------
def costear(prod):
    sku, nom, cera, g, sup, ext, vph, precios = prod
    costo_cera = g * INS[cera + "_g"]
    frag_g = g * FRAG_PCT
    costo_frag = frag_g * INS["fragancia_g"]
    colorante = g * INS["colorante_g_cera"] if cera == "parafina" else 0.0
    n_mechas = 1 + ext.get("mecha_extra", 0)
    if sku == "NV-ROM":
        n_mechas = 1  # solo la pieza superior lleva pabilo (verificar)
    mecha = n_mechas * INS["mecha"]
    contenedor = sum(INS[k] * ext.get(k, 0) for k in ("lata_plateada", "lata_dorada", "frasco_tapa_dorada", "jabon_base_g"))
    contenedor += ext.get("fragancia_g", 0) * INS["fragancia_g"]  # fragancia del jabón
    contenedor += INS["pintura_figura"] * ext.get("pintura_figura", 0)
    etiqueta = INS["etiqueta"] * ext.get("etiqueta", 0) + INS["tarjeta_oracion"] * ext.get("tarjeta_oracion", 0)
    empaque = sum(INS[k] * ext.get(k, 0) for k in ("celofan", "organza", "caja_kraft_kit", "liston_cierre"))
    mo = MO_HORA / vph
    sub = costo_cera + costo_frag + colorante + mecha + contenedor + etiqueta + empaque + mo
    merma = sub * MERMA
    total = sub + merma
    r = dict(sku=sku, producto=nom, cera_g=g, costo_cera=costo_cera, fragancia_g=frag_g, costo_fragancia=costo_frag,
             colorante=colorante, mecha=mecha, contenedor_o_base=contenedor, etiqueta=etiqueta, empaque=empaque,
             mano_obra=mo, merma_5pct=merma, costo_unitario=total, precio_menudeo=precios[0],
             margen_menudeo_pct=(precios[0] - total) / precios[0] * 100, supuesto=sup, vph=vph, precios=precios)
    return r

R = [costear(p) for p in P]

RECOMENDACIONES = """## Hallazgos y recomendaciones (resumen)

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
"""

# ---------------------------------------------------------------------------
# 5. SALIDAS
# ---------------------------------------------------------------------------
CAMPOS = ["sku", "producto", "cera_g", "costo_cera", "fragancia_g", "costo_fragancia", "colorante", "mecha",
          "contenedor_o_base", "etiqueta", "empaque", "mano_obra", "merma_5pct", "costo_unitario",
          "precio_menudeo", "margen_menudeo_pct", "estatus"]

def fmt(v):
    if isinstance(v, float):
        return f"{v:.2f}"
    return v

with open(os.path.join(AQUI, "plantilla-costeo.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(CAMPOS)
    for r in R:
        w.writerow([fmt(r[c]) if c != "estatus" else "ESTIMADO" for c in CAMPOS[:-1]] + ["ESTIMADO"])

def m(x):
    return f"${x:,.2f}"

def flag(pct, minimo):
    return f"⚠️ {pct:.1f}%" if pct < minimo else f"{pct:.1f}%"

out = []
A = out.append
A("# Márgenes por canal — Ananda Velas\n")
A("> **TODO ES ESTIMADO.** Costos calculados con precios de referencia de internet (oct-2026) y supuestos de gramaje y "
  "productividad, NO con compras reales de Noemi. Comisiones de ML/TikTok tomadas de fuentes de terceros: **verificar** "
  "en el simulador de costos de Mercado Libre y en TikTok Seller Center antes de publicar. "
  "Se regenera con `python3 costos/calculo_costos.py`.\n")
A("## Supuestos\n")
A("| Concepto | Supuesto | Estatus |\n|---|---|---|")
A("| ML Clásica | 15% (Hogar; rango 8–16%) + IVA sobre comisión = 17.4% efectivo. Cargo fijo: $25 (<$99), $30 ($99–148), $37 ($149–298), $0 desde $299 | verificar (Tiendanube 19-mar-2026, calcforlife) |")
A("| ML Premium | 19.5% (rango 12.5–20.5%) + IVA = 22.6% efectivo. Mismo cargo fijo | verificar |")
A("| TikTok Shop | 6% comisión (incluye impuestos) + 2% procesamiento = 8%. Vendedores nuevos: 0% comisión 60 días (no considerado) | verificar (Tiendanube 10-abr-2026; otra fuente dice 10% Hogar) |")
A("| Tienda propia | Pasarela 3.6% + $3 + IVA = 4.18% + $3.48 por venta. Plan mensual NO incluido (es costo fijo) | verificar |")
A("| Mayoreo | 0% comisión, transferencia; envío lo paga cliente o entrega local | — |")
A("| Envío | Tickets < $299: lo paga el comprador ($0 para el vendedor). Tickets ≥ $299: envío gratis absorbido por vendedor: ML $80 (parte del vendedor, paquete < 1 kg), TikTok $80, tienda propia $120 (guía de paquetería) | verificar (ML dio envío gratis desde $99 para Meli+ en abr-2026: confirmar si cobra al vendedor en tickets < $299) |")
A("| Impuestos | Margen ANTES de ISR/IVA. Retenciones de plataforma (ISR 2.5% con RFC, mayor sin RFC) son pagos a cuenta, no costo. Si Noemi debe trasladar IVA, el neto real baja ~13.8%: revisar con `finanzas-fiscal` | verificar |")
A("| Margen | margen $ = precio − comisión − cargo fijo − envío − costo unitario; margen % = margen $ ÷ precio. Mínimos: 45% menudeo, 35% mayoreo | regla README |")
A("")
A("Fuentes de comisiones (terceros, no oficiales; consultadas 09-oct-2026): [Tiendanube ML México (act. 19-mar-2026)](https://www.tiendanube.com/mx/blog/comision-mercado-libre-mexico/), [calcforlife calculadora ML](https://calcforlife.com/es/calculadora-mercado-libre-comisiones/), [Tiendanube TikTok Shop (act. 10-abr-2026)](https://www.tiendanube.com/blog/tiktok-shop), [ecomcalctools TikTok LATAM 2026](https://ecomcalctools.com/es/blog/tiktok-shop-fees-latam-2026/). La ayuda oficial de ML no se pudo consultar (bloqueo 403): **verificar en el simulador de la publicación**.\n")
A("EV-PRE se evalúa a $115; con la promo de octubre ($95) el margen directo baja a ~50% y en ML Clásica a ~6%.\n")
A(f"Costo unitario: cera + fragancia (8% del peso) + colorante + mecha + contenedor/base/pintura + etiqueta + empaque + mano de obra (${MO_HORA:.0f}/h) + merma 5%. Detalle en `costos/plantilla-costeo.csv`.\n")

OUT_SPLIT = len(out)
A("## 1. Costo unitario estimado y margen en venta directa\n")
A("| SKU | Producto | Cera g (supuesto) | Velas/h | Costo unitario | Menudeo | Margen directo |\n|---|---|---|---|---|---|---|")
for r in R:
    A(f"| {r['sku']} | {r['producto']} | {r['cera_g']} g ({r['supuesto']}) | {r['vph']:.2f} | {m(r['costo_unitario'])} | {m(r['precio_menudeo'])} | {flag(r['margen_menudeo_pct'], 45)} |")
A("")

A("## 2. Pieza suelta por canal (precio menudeo)\n")
A("| SKU | Canal | Precio | Comisión % | Cargo fijo | Envío | Neto | Margen $ | Margen % | Precio mín. 45% |\n|---|---|---|---|---|---|---|---|---|---|")
flags_menudeo = []
for r in R:
    p = r["precio_menudeo"]
    for c in CANALES:
        n, pct, fijo, env = neto(c, p)
        mg = n - r["costo_unitario"]
        mp = mg / p * 100
        if mp < 45:
            flags_menudeo.append((r["sku"], c, p, mp, precio_minimo(c, r["costo_unitario"], 0.45)))
        A(f"| {r['sku']} | {c} | {m(p)} | {pct*100:.1f}% | {m(fijo)} | {m(env)} | {m(n)} | {m(mg)} | {flag(mp, 45)} | {m(precio_minimo(c, r['costo_unitario'], 0.45))} |")
A("")

A("## 3. Kits para marketplace (ticket ≥ $299, sin cargo fijo de ML)\n")
A("Kit = N piezas del mismo modelo a precio menudeo × N, en caja kraft (+$10 de caja; se quita el celofán individual: "
  "se conserva por simplicidad, sobreestima costo ~$1/pza). Al pasar de $299 el vendedor paga envío (supuesto $80 ML/TikTok, $120 tienda).\n")
A("| Kit | Precio kit | Costo kit | Canal | Comisión % | Envío | Neto | Margen $ | Margen % | Precio mín. kit 45% (por pieza) |\n|---|---|---|---|---|---|---|---|---|---|")
kits = []
for r in R:
    if r["sku"] in ("NV-B12", "NV-ROM") or r["precio_menudeo"] >= 299:
        continue
    n = next(k for k in (4, 6, 8, 12) if k * r["precio_menudeo"] >= 299)
    pk = n * r["precio_menudeo"]
    ck = n * r["costo_unitario"] + INS["caja_kraft_kit"]
    kits.append((r, n, pk, ck))
    for c in ("ML Clásica", "ML Premium", "TikTok Shop"):
        nn, pct, fijo, env = neto(c, pk)
        mg = nn - ck
        pmk = max(precio_minimo(c, ck, 0.45), 299)
        A(f"| {r['sku']} x{n} | {m(pk)} | {m(ck)} | {c} | {pct*100:.1f}% | {m(env)} | {m(nn)} | {m(mg)} | {flag(mg/pk*100, 45)} | {m(pmk)} ({m(pmk/n)}) |")
A("")

A("## 4. Mayoreo directo (WhatsApp/Instagram, 0% comisión, envío por cuenta del cliente)\n")
A("| SKU | Costo unitario | 11–50 | Margen | 51–99 | Margen | 100–150 | Margen |\n|---|---|---|---|---|---|---|---|")
flags_may = []
for r in R:
    if len(r["precios"]) < 4:
        continue
    celdas = []
    for nivel, p in zip(("11–50", "51–99", "100–150"), r["precios"][1:]):
        mp = (p - r["costo_unitario"]) / p * 100
        if mp < 35:
            flags_may.append((r["sku"], nivel, p, mp, math.ceil(r["costo_unitario"] / 0.65)))
        celdas += [m(p), flag(mp, 35)]
    A(f"| {r['sku']} | {m(r['costo_unitario'])} | " + " | ".join(celdas) + " |")
A("")

A("## 5. Alertas ⚠️ y precio mínimo recomendado\n")
A("Fórmula (README): `Precio = (costo + envío + cargo fijo + margen$) ÷ (1 − %comisión)` con margen$ = 45% del precio "
  "(menudeo) o 35% (mayoreo) ⇒ `Precio mínimo = (costo + envío + cargo fijo) ÷ (1 − %comisión − margen%)`.\n")
A("### Menudeo pieza suelta con margen < 45%\n")
A("| SKU | Canal | Precio actual | Margen | Precio mínimo para 45% |\n|---|---|---|---|---|")
for sku, c, p, mp, pm in flags_menudeo:
    A(f"| {sku} | {c} | {m(p)} | ⚠️ {mp:.1f}% | {m(pm)} |")
A("")
A("### Mayoreo con margen < 35%\n")
if flags_may:
    A("| SKU | Nivel | Precio actual | Margen | Precio mínimo para 35% |\n|---|---|---|---|---|")
    for sku, nv, p, mp, pm in flags_may:
        A(f"| {sku} | {nv} | {m(p)} | ⚠️ {mp:.1f}% | {m(pm)} |")
else:
    A("Ningún nivel de mayoreo queda bajo 35% con los costos estimados.")
A("")

# --- Sensibilidad ---
A("## 6. Sensibilidad del costo unitario (qué tanto cambia si los insumos reales son distintos)\n")
A("- **Base**: supuestos de arriba.\n- **Optimista (compra por volumen)**: parafina 25 kg ~$85/kg, soya 25 kg ~$110/kg (verificar), fragancia $550/kg al 6%, latas/frascos −30%.\n"
  "- **Pesimista (compra al menudeo)**: parafina 1 kg $143/kg, fragancia en frasco chico ~$2,190/kg (60 ml $131.50) al 8%.\n")
A("| SKU | Base | Optimista | Pesimista | Margen directo base / opt / pes |\n|---|---|---|---|---|")
base_ins = dict(INS)
def escenario(cambios, frag_pct):
    global FRAG_PCT
    INS.update(base_ins); INS.update(cambios); viejo = FRAG_PCT; FRAG_PCT = frag_pct
    res = {p[0]: costear(p)["costo_unitario"] for p in P}
    FRAG_PCT = viejo; INS.update(base_ins)
    return res
opt = escenario({"parafina_g": .085, "soya_g": .110, "fragancia_g": .55, "lata_plateada": 12*.7, "lata_dorada": 14*.7, "frasco_tapa_dorada": 18*.7}, 0.06)
pes = escenario({"parafina_g": .143, "fragancia_g": 2.19}, 0.08)
for r in R:
    pr = r["precio_menudeo"]; s_ = r["sku"]
    A(f"| {s_} | {m(r['costo_unitario'])} | {m(opt[s_])} | {m(pes[s_])} | {(pr-r['costo_unitario'])/pr*100:.0f}% / {(pr-opt[s_])/pr*100:.0f}% / {(pr-pes[s_])/pr*100:.0f}% |")
A("")

recomendaciones = RECOMENDACIONES
with open(os.path.join(AQUI, "margenes-por-canal.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(out[:OUT_SPLIT]) + "\n" + recomendaciones + "\n" + "\n".join(out[OUT_SPLIT:]) + "\n")

# Resumen en consola
for r in R:
    print(f"{r['sku']:7s} {r['cera_g']:4d} g  costo {r['costo_unitario']:7.2f}  menudeo {r['precio_menudeo']:6.1f}  margen {r['margen_menudeo_pct']:5.1f}%")
print("flags menudeo:", len(flags_menudeo), " flags mayoreo:", len(flags_may))
for x in flags_may:
    print("  MAY", x)
