#!/usr/bin/env python3
"""Cálculo reproducible de costos unitarios y márgenes por canal — Ananda Velas.

v3 (27-nov-2026, tarde). Cambios vs v2:
- Figuras de parafina con la FÓRMULA REAL de Noemi: 80% parafina Malasia + 15% soya de fusión + 5% cera ámbar
  (corrección de Noemi 27-nov: el 5% NO es estearina),
  aroma 8% del peso de cera, colorante 0.5-1 g por vela (se usa 1 g como tope: confirmar).
- PESOS REALES (1 pieza en báscula, 27-nov): Borrego 72 g, Venado 66 g (display tapado: verificar),
  árbol hojas grandes 114 g (-> NV-PIN, mapeo por confirmar), árbol delgado 58 g (-> NV-ARB, mapeo por confirmar),
  piña de pino café 45 g (producto sin SKU). Cera = peso terminado ÷ 1.08 (el peso incluye 8% de aroma).
- Precios del pizarrón del proveedor (27-nov): Malasia $106/kg (escenario $97), soya A F/B F $111/kg,
  base de jabón $105/kg, porta pabilo $1, pabilo $25. Cera ámbar $120/kg.
Siguen ESTIMADOS: gramos de las figuras no pesadas, velas por hora, precio del colorante por gramo, latas/frascos,
empaques, pintura y tinta. El aroma sigue a $50 por 30 ml (precio real del 17-oct).

Para recalcular: cambia los valores de las secciones 1-2 (y su estatus en ESTATUS) y ejecuta
    python3 costos/calculo_costos.py
Genera: costos/plantilla-costeo.csv y costos/margenes-por-canal.md
"""
import csv
import math
import os

AQUI = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# 1. PRECIOS DE INSUMOS (MXN por unidad útil)
#    ESTATUS: "REAL" = precio que pagó Noemi · "ESTIMADO" = referencia de internet o supuesto
# ---------------------------------------------------------------------------
INS = {
    "malasia_g": 106 / 1000,       # REAL pizarrón proveedor 27-nov: Malasia $106/kg (aparece "-97": escenario volumen $97/kg)
    "soya_fusion_g": 111 / 1000,   # REAL pizarrón 27-nov: soya A F y B F $111/kg (las dos igual)
    "ambar_g": 120 / 1000,         # REAL pizarrón 27-nov: cera ámbar $120/kg (5% de la mezcla de figuras)
    "soya_g": 111 / 1000,          # soya de contenedor: se usa la misma $111/kg del pizarrón (CONFIRMAR que es la misma soya)
    "parafina_china_g": 66 / 1000, # REAL pizarrón 27-nov: "parafina $67-65/kg" (no se usa en figuras; referencia)
    "fragancia_g": 50 / 30,        # REAL $50 por 30 ml = $1.667/ml; densidad 1 g/ml supuesta (verificar pesando 10 ml)
    "colorante_vela": 1.25,        # dosis REAL 0.5-1 g por vela (tope 1 g, confirmar); precio por gramo NO visible en pizarrón
                                   # ("color para velas $1..." cortado) -> se usa el tope real del 17-oct: 1/4 de sobre de $5 = $1.25/vela
    "pabilo_cm": 25 / 300,         # REAL rollo 3 m $25 -> $0.083/cm
    "base_mecha": 1.00,            # REAL pizarrón 27-nov: porta pabilo $1 c/u — solo contenedores
    "lata_plateada": 12.00,        # ESTIMADO (ref. 24 latas 4 oz $338 = $14.09)
    "lata_dorada": 14.00,          # ESTIMADO
    "frasco_tapa_dorada": 18.00,   # ESTIMADO (ref. 12 frascos 250 ml tapa dorada $255 = $21.25; GLO es más chico)
    "celofan": 0.90,               # ESTIMADO 100 bolsas $90 precio regular ML
    "organza": 2.00,               # ESTIMADO, sin precio MX verificado
    "liston_cierre": 0.50,         # ESTIMADO rafia/listón para cerrar celofán
    "tag_opalina": 3.00 / 12 + 0.30,   # opalina $3/hoja REAL ÷ 12 tags por hoja (ESTIMADO) + tinta $0.30 (ESTIMADO) = $0.55
    "etiqueta_adh": 6.00 / 12 + 0.30,  # papel adhesivo $6/hoja REAL ÷ 12 etiquetas por hoja (ESTIMADO) + tinta $0.30 (ESTIMADO) = $0.80
    "tarjeta_oracion": 3.00 / 8 + 0.30,  # opalina $3/hoja REAL ÷ 8 tarjetas (ESTIMADO) + tinta (ESTIMADO) = $0.68
    "caja_kraft_kit": 10.00,       # ESTIMADO (ref. 50 cajas kraft 22x16.5x5.5 $365 = $7.30) + relleno
    "jabon_base_g": 105 / 1000,    # REAL pizarrón 27-nov: jabón $105/kg (base de glicerina)
    "pintura_figura": 1.50,        # ESTIMADO acrílico + barniz por figura pintada completa
}
ESTATUS = {
    "malasia_g": "REAL", "soya_fusion_g": "REAL", "ambar_g": "REAL", "soya_g": "REAL (confirmar tipo)",
    "fragancia_g": "REAL", "colorante_vela": "MIXTO (dosis real, precio tope)",
    "pabilo_cm": "REAL", "base_mecha": "REAL", "lata_plateada": "ESTIMADO", "lata_dorada": "ESTIMADO",
    "frasco_tapa_dorada": "ESTIMADO", "celofan": "ESTIMADO", "organza": "ESTIMADO", "liston_cierre": "ESTIMADO",
    "tag_opalina": "MIXTO", "etiqueta_adh": "MIXTO", "tarjeta_oracion": "MIXTO", "caja_kraft_kit": "ESTIMADO",
    "jabon_base_g": "REAL", "pintura_figura": "ESTIMADO",
}

FRAG_PCT = 0.08     # REAL en figuras (Noemi, 27-nov): aroma = 8% del peso de cera. En soya/contenedor: supuesto 8%
FORMULA_FIG = {"malasia_g": 0.80, "soya_fusion_g": 0.15, "ambar_g": 0.05}   # REAL (Noemi, 27-nov), % de la mezcla de cera
FACTOR_AROMA = 1 + FRAG_PCT   # peso terminado = cera × 1.08 -> cera = peso ÷ 1.08 (pabilo despreciable)

def precio_mezcla_fig():
    return sum(INS[k] * f for k, f in FORMULA_FIG.items())

def cera_de_peso(peso_g):
    return round(peso_g / FACTOR_AROMA, 1)
MERMA = 0.05        # merma 5% sobre (materiales + mano de obra)
MO_HORA = 80.0      # SUPUESTO $80/h (el mismo que Noemi aceptó en Día de Muertos; confirmar)

# ---------------------------------------------------------------------------
# 2. PRODUCTOS: gramos de cera ESTIMADOS (nadie ha pesado las piezas) + extras + velas/hora ESTIMADAS
#    gramos = alto x ancho x fondo(supuesto) x factor_llenado x densidad 0.9 g/cm3
#    pabilo: figura = alto + 2 cm; contenedor = alto + 1 cm + base metálica
# ---------------------------------------------------------------------------
DENS = 0.9

def caja(alto, ancho, fondo, llenado):
    return round(alto * ancho * fondo * llenado * DENS)

def cilindro(alto_llenado, diam_int, llenado=1.0):
    return round(math.pi * (diam_int / 2) ** 2 * alto_llenado * llenado * DENS)

def cono(alto, diam, llenado):
    return round(math.pi * (diam / 2) ** 2 * alto / 3 * llenado * DENS)

FIG = {"celofan": 1, "tag_opalina": 1, "liston_cierre": 1}

# (sku, nombre, cera, gramos, supuesto_gramos, extras{insumo:cant}, velas_por_hora, precios[men,11-50,51-99,100-150])
P = [
    ("EV-OSO", "Oso de Ternura", "figura", caja(10, 9.5, 5.5, .40), "10x9.5 cm, fondo 5.5, llenado 40%",
        {**FIG, "pabilo_cm": 12}, 10, [87, 78, 75, 71]),
    ("EV-JIR", "Jirafa Africana", "figura", caja(9, 4, 3, .40), "9x4 cm, fondo 3, llenado 40%",
        {**FIG, "pabilo_cm": 11}, 12, [45, 40, 38, 36]),
    ("EV-ELE", "Elefante Safari", "figura", caja(7, 9.5, 4.5, .40), "7x9.5 cm, fondo 4.5, llenado 40%",
        {**FIG, "pabilo_cm": 9}, 12, [57, 51, 49.5, 46]),
    ("EV-DIN", "Dino T-Rex", "figura", caja(9.3, 8, 4, .35), "9.3x8 cm, fondo 4, llenado 35%",
        {**FIG, "pabilo_cm": 11.3}, 12, [57, 51, 49.5, 46]),
    ("EV-ANG", "Ángeles Divinos", "figura", caja(6, 7, 3.5, .45), "6x7 cm, fondo 3.5, llenado 45%",
        {**FIG, "pabilo_cm": 8}, 12, [57, 51, 49.5, 46]),
    ("EV-FLO", "Flowers On", "figura", cilindro(3.5, 8, .60), "peonía Ø8 x 3.5 cm, llenado 60%",
        {**FIG, "pabilo_cm": 5.5}, 10, [77, 69.5, 67, 63]),
    ("EV-BUN", "Bunny Happy", "figura", caja(10, 7, 5, .40), "10x7 cm, fondo 5, llenado 40%",
        {**FIG, "pabilo_cm": 12}, 10, [87, 78, 75.5, 71]),
    ("EV-GLO", "Glowing Glass", "soya", cilindro(4.8, 6.1), "frasco Ø int 6.1, llenado a 4.8 cm",
        {"frasco_tapa_dorada": 1, "etiqueta_adh": 2, "pabilo_cm": 6.8, "base_mecha": 1}, 15, [74, 66.5, 64, 60]),
    ("EV-LMM", "Lume Soja Mini", "soya", cilindro(1.8, 5.8), "lata Ø int 5.8, llenado a 1.8 cm",
        {"lata_plateada": 1, "etiqueta_adh": 2, "pabilo_cm": 3.3, "base_mecha": 1}, 15, [52, 46.5, 45, 42]),
    ("EV-LMS", "Lume Soja", "soya", cilindro(4.0, 5.8), "lata Ø int 5.8, llenado a 4.0 cm",
        {"lata_dorada": 1, "etiqueta_adh": 2, "pabilo_cm": 5.6, "base_mecha": 1}, 15, [88, 79, 76.5, 72]),
    ("EV-PRE", "Paquete Recuerdos", "soya", cilindro(1.8, 5.8), "vela = Lume Mini (43 g) + 2 jabones 25 g",
        {"lata_plateada": 1, "etiqueta_adh": 2, "pabilo_cm": 3.3, "base_mecha": 1, "organza": 1,
         "jabon_base_g": 50, "fragancia_g": 1.5}, 8, [115, 86, 83, 78]),
    ("NV-VEN", "Venado", "figura", cera_de_peso(66), "REAL 66 g terminado (display tapado: VERIFICAR) ÷ 1.08",
        {**FIG, "liston_cierre": 2, "pabilo_cm": 11.5}, 10, [78, 70, 67, 62]),
    ("NV-NAC", "Nacimiento", "figura", caja(6.2, 4.5, 3, .50), "6.2x4.5 cm, fondo 3, llenado 50%",
        {**FIG, "pabilo_cm": 8.2}, 12, [65, 58, 55, 50]),
    ("NV-PIN", "Pino", "figura", cera_de_peso(114), "REAL 114 g terminado (árbol hojas grandes; MAPEO POR CONFIRMAR) ÷ 1.08",
        {**FIG, "pabilo_cm": 12, "pintura_figura": .3}, 10, [87, 78, 75, 69]),
    ("NV-ARB", "Árbol Navideño", "figura", cera_de_peso(58), "REAL 58 g terminado (árbol delgado hojitas; MAPEO POR CONFIRMAR) ÷ 1.08",
        {**FIG, "pabilo_cm": 12, "pintura_figura": .3}, 12, [85, 76, 73, 68]),
    ("NV-BOR", "Borrego", "figura", cera_de_peso(72), "REAL 72 g terminado ÷ 1.08",
        {**FIG, "pabilo_cm": 8.5, "pintura_figura": 1}, 8, [57, 51, 49, 45]),
    ("NV-B12", "Borregos de la Abundancia 12 pzs", "figura", round(12 * cera_de_peso(72), 1), "12 borregos x 72 g REAL ÷ 1.08",
        {"caja_kraft_kit": 1, "etiqueta_adh": 1, "tag_opalina": 1, "tarjeta_oracion": 12, "pintura_figura": 12,
         "pabilo_cm": 12 * 8.5, "piezas": 12}, 8 / 12 / 1.15, [385]),
    ("NV-ROM", "Rompecabezas Navideño", "figura", cilindro(22, 6.5, .55), "4 piezas, Ø6.5 x 22 cm, llenado 55%",
        {"caja_kraft_kit": 1, "etiqueta_adh": 1, "tag_opalina": 1, "pintura_figura": 4,
         "pabilo_cm": 4 * (22 / 4 + 2), "piezas": 4}, 2, [375]),
]
REALES = {"NV-VEN", "NV-PIN", "NV-ARB", "NV-BOR", "NV-B12"}   # SKUs con peso pesado en báscula (27-nov)

# Producto sin SKU (no está en catálogo): se costea, sin precio de venta
SIN_SKU = [("SIN-SKU-PINA", "Producto sin SKU (piña de pino café)", "figura", cera_de_peso(45),
            "REAL 45 g terminado ÷ 1.08", {**FIG, "pabilo_cm": 8}, 12, [0])]   # pabilo 8 cm y 12 velas/h ESTIMADOS

# Notas velas/hora (ESTIMADAS): incluye colado, desmolde, acabado, etiquetado y empaque (por lote).
# Dato real de referencia: cempasúchil (106 g) = 3 velas/h por persona (Noemi, 17-oct) — ver escenario en sección 6.
# NV-B12: 12 borregos a 8/h + 15% de tiempo de armado de caja = 0.58 kits/h.
# NV-ROM: 2 juegos/h (4 piezas pintadas por juego). Pabilo: 1 por pieza (verificar si solo la de arriba lleva).

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
def costear(prod, vph_factor=1.0):
    sku, nom, cera, g, sup, ext, vph, precios = prod
    vph = vph * vph_factor
    precio_g = precio_mezcla_fig() if cera == "figura" else INS[cera + "_g"]
    costo_cera = g * precio_g
    frag_g = g * FRAG_PCT
    costo_frag = frag_g * INS["fragancia_g"]
    colorante = INS["colorante_vela"] * ext.get("piezas", 1) if cera == "figura" else 0.0
    pabilo = ext.get("pabilo_cm", 0) * INS["pabilo_cm"]
    mecha = pabilo + ext.get("base_mecha", 0) * INS["base_mecha"]
    envase = sum(INS[k] * ext.get(k, 0) for k in ("lata_plateada", "lata_dorada", "frasco_tapa_dorada"))
    jabon = INS["jabon_base_g"] * ext.get("jabon_base_g", 0) + ext.get("fragancia_g", 0) * INS["fragancia_g"]
    pintura = INS["pintura_figura"] * ext.get("pintura_figura", 0)
    contenedor = envase + jabon + pintura
    etiqueta = sum(INS[k] * ext.get(k, 0) for k in ("tag_opalina", "etiqueta_adh", "tarjeta_oracion"))
    empaque = sum(INS[k] * ext.get(k, 0) for k in ("celofan", "organza", "caja_kraft_kit", "liston_cierre"))
    mo = MO_HORA / vph
    materiales = costo_cera + costo_frag + colorante + mecha + contenedor + etiqueta + empaque
    sub = materiales + mo
    merma = sub * MERMA
    total = sub + merma
    # parte de los materiales cuyo PRECIO ya es real (los gramos siguen siendo estimados)
    precio_real = costo_cera + costo_frag + pabilo + ext.get("fragancia_g", 0) * INS["fragancia_g"] + jabon \
        + ext.get("base_mecha", 0) * INS["base_mecha"]
    r = dict(sku=sku, producto=nom, cera_g=g, costo_cera=costo_cera, fragancia_g=frag_g, costo_fragancia=costo_frag,
             colorante=colorante, mecha=mecha, contenedor_o_base=contenedor, etiqueta=etiqueta, empaque=empaque,
             mano_obra=mo, merma_5pct=merma, costo_unitario=total, precio_menudeo=precios[0],
             margen_menudeo_pct=(precios[0] - total) / precios[0] * 100 if precios[0] else 0.0, supuesto=sup, vph=vph, velas_hora=vph, precios=precios,
             materiales=materiales, pct_materiales_precio_real=precio_real / materiales * 100)
    pend = ([] if sku in REALES or sku.startswith("SIN-SKU") else ["gramos"]) + ([] if cera == "figura" else ["%aroma"]) \
        + ["velas/h", "precio aroma por kg"] + (["colorante $/g"] if cera == "figura" else [])
    if sku in ("NV-PIN", "NV-ARB"):
        pend.append("mapeo Pino/Árbol")
    if sku == "NV-VEN":
        pend.append("re-pesar (display tapado)")
    if envase:
        pend.append("envase")
    if ext.get("organza") or ext.get("caja_kraft_kit") or ext.get("celofan"):
        pend.append("empaque")
    if pintura:
        pend.append("pintura")
    base = "GRAMOS REALES" if (sku in REALES or sku.startswith("SIN-SKU")) else "ESTIMADO"
    r["estatus"] = base + " (falta: " + ", ".join(pend) + ")"
    return r

R = [costear(p) for p in P]
R_SIN = [costear(p) for p in SIN_SKU]

RECOMENDACIONES = f"""## Hallazgos (v3, 27-nov-2026)

> **v3:** figuras de parafina con la fórmula real de Noemi (80% Malasia ${INS['malasia_g']*1000:.0f}/kg + 15% soya de fusión ${INS['soya_fusion_g']*1000:.0f}/kg + 5% cera ámbar ${INS['ambar_g']*1000:.0f}/kg) = **${precio_mezcla_fig()*1000:.2f}/kg de mezcla**; aroma 8%; colorante 1 g por vela (tope, $1.25). Pesos reales (1 pieza): Borrego 72 g, Venado 66 g (verificar), Pino 114 g y Árbol 58 g (**mapeo por confirmar**). Soya de contenedor a $111/kg (confirmar que es la misma). Base de jabón $105/kg y porta pabilo $1 (pizarrón del proveedor, 27-nov).
>
> **Siguen estimados:** gramos de las figuras no pesadas, velas por hora, precio del aroma por kg (hoy frasco de 30 ml a $50), precio del colorante por gramo, latas/frascos y empaques. Las recomendaciones de texto de la v1 (9-oct) ya no aplican; las alertas de las secciones 5 y 6 se generan solas.
>
> Comisiones y envíos siguen siendo los del 9-oct (fuentes de terceros): **verificar** en el simulador de Mercado Libre y en TikTok Seller Center antes de publicar.
"""

# ---------------------------------------------------------------------------
# 5. SALIDAS
# ---------------------------------------------------------------------------
CAMPOS = ["sku", "producto", "cera_g", "costo_cera", "fragancia_g", "costo_fragancia", "colorante", "mecha",
          "contenedor_o_base", "etiqueta", "empaque", "mano_obra", "merma_5pct", "costo_unitario",
          "precio_menudeo", "margen_menudeo_pct", "velas_hora", "pct_materiales_precio_real", "estatus"]

def fmt(v):
    if isinstance(v, float):
        return f"{v:.2f}"
    return v

with open(os.path.join(AQUI, "plantilla-costeo.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(CAMPOS)
    for r in R:
        w.writerow([fmt(r[c]) for c in CAMPOS])
    for r in R_SIN:   # sin precio de venta
        w.writerow([fmt(r[c]) if c not in ("precio_menudeo", "margen_menudeo_pct") else "" for c in CAMPOS])

def m(x):
    return f"${x:,.2f}"

def flag(pct, minimo):
    return f"⚠️ {pct:.1f}%" if pct < minimo else f"{pct:.1f}%"

out = []
A = out.append
A("# Márgenes por canal — Ananda Velas\n")
A("> **Costos v3 (27-nov-2026): precios de cera, aroma, pabilo, jabón y porta pabilo REALES; fórmula real en figuras; "
  "peso real en Borrego, Venado, Pino y Árbol.** El resto de gramos, las velas por hora, envases y empaques siguen estimados. Comisiones de ML/TikTok tomadas de fuentes de terceros: **verificar** "
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
_pre = next(r for r in R if r["sku"] == "EV-PRE")
A(f"EV-PRE se evalúa a $115; con la promo de octubre ($95) el margen directo sería {(95 - _pre['costo_unitario']) / 95 * 100:.0f}% "
  f"y en ML Clásica {(neto('ML Clásica', 95)[0] - _pre['costo_unitario']) / 95 * 100:.0f}%.\n")
A(f"Costo unitario: cera + fragancia ({FRAG_PCT*100:.0f}% del peso, ${INS['fragancia_g']:.3f}/g) + colorante + mecha + contenedor/base/pintura + etiqueta + empaque + mano de obra (${MO_HORA:.0f}/h) + merma 5%. Detalle en `costos/plantilla-costeo.csv`.\n")

OUT_SPLIT = len(out)
A("## 1. Costo unitario (v3) y margen en venta directa\n")
A("| SKU | Producto | Cera g (supuesto) | Velas/h | Costo unitario | Menudeo | Margen directo |\n|---|---|---|---|---|---|---|")
for r in R:
    A(f"| {r['sku']} | {r['producto']} | {r['cera_g']} g ({r['supuesto']}) | {r['vph']:.2f} | {m(r['costo_unitario'])} | {m(r['precio_menudeo'])} | {flag(r['margen_menudeo_pct'], 45)} |")
A("")

for r in R_SIN:
    A(f"| — | {r['producto']} | {r['cera_g']} g ({r['supuesto']}) | {r['vph']:.2f} | {m(r['costo_unitario'])} | sin precio | — |")
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
A("- **Base**: supuestos de arriba (aroma real $1.667/g al 8%, velas/h estimadas).\n"
  "- **Aroma 6%**: la dosis que Noemi usa en cempasúchil (~5.7%); baja costo pero puede oler poco (ver `produccion/formulas/`).\n"
  "- **Aroma granel**: $0.90/g comprando 1 kg (ESTIMADO, pedir cotización), al 8%.\n"
  "- **Mitad de velas/h**: si cada pieza tarda el doble de lo estimado (referencia real: cempasúchil 3 velas/h).\n"
  "- **Malasia $97**: precio por volumen que aparece en el pizarrón (\"-97\").\n"
  "- **Mapeo invertido**: si el árbol de 114 g es NV-ARB y el de 58 g es NV-PIN.\n")
A("| SKU | Base | Aroma 6% | Aroma granel | Mitad velas/h | Malasia $97 | Mapeo invertido | Margen directo base / mitad velas/h |\n|---|---|---|---|---|---|---|---|")
base_ins = dict(INS)
def escenario(cambios, frag_pct, vph_factor=1.0):
    global FRAG_PCT
    INS.update(base_ins); INS.update(cambios); viejo = FRAG_PCT; FRAG_PCT = frag_pct
    res = {p[0]: costear(p, vph_factor)["costo_unitario"] for p in P}
    FRAG_PCT = viejo; INS.update(base_ins)
    return res
e6 = escenario({}, 0.06)
egr = escenario({"fragancia_g": .90}, 0.08)
emo = escenario({}, 0.08, 0.5)
e97 = escenario({"malasia_g": .097}, 0.08)
_g = {p[0]: p[3] for p in P}
def _swap(p):
    if p[0] in ("NV-PIN", "NV-ARB"):
        otro = "NV-ARB" if p[0] == "NV-PIN" else "NV-PIN"
        p = (p[0], p[1], p[2], _g[otro]) + tuple(p[4:])
    return p
einv = {p[0]: costear(_swap(p))["costo_unitario"] for p in P}
ESCEN = dict(aroma6=e6, granel=egr, mitad_vph=emo, malasia97=e97, invertido=einv)
for r in R:
    pr = r["precio_menudeo"]; s_ = r["sku"]
    A(f"| {s_} | {m(r['costo_unitario'])} | {m(e6[s_])} | {m(egr[s_])} | {m(emo[s_])} | {m(e97[s_])} | {m(einv[s_])} | {(pr-r['costo_unitario'])/pr*100:.0f}% / {(pr-emo[s_])/pr*100:.0f}% |")
A("")

recomendaciones = RECOMENDACIONES
with open(os.path.join(AQUI, "margenes-por-canal.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(out[:OUT_SPLIT]) + "\n" + recomendaciones + "\n" + "\n".join(out[OUT_SPLIT:]) + "\n")

# Resumen en consola
print(f"mezcla figuras: ${precio_mezcla_fig()*1000:.2f}/kg")
for r in R_SIN:
    print(r["producto"], r["cera_g"], "g  costo", round(r["costo_unitario"], 2))
for r in R:
    print(f"{r['sku']:7s} {r['cera_g']:6.1f} g  costo {r['costo_unitario']:7.2f}  menudeo {r['precio_menudeo']:6.1f}  margen {r['margen_menudeo_pct']:5.1f}%  mitad_vph {ESCEN['mitad_vph'][r['sku']]:7.2f}  granel {ESCEN['granel'][r['sku']]:7.2f}")
print("flags menudeo:", len(flags_menudeo), " flags mayoreo:", len(flags_may))
for x in flags_may:
    print("  MAY", x)
