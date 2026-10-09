# TikTok Shop México: textos para dar de alta los kits

Estado de la cuenta: **en verificación** (9-oct-2026). Estos textos quedan listos para copiar y pegar cuando se apruebe.
Base: `negocio/catalogo.md` y `mercadolibre/publicaciones-navidad-eventos.md` (mismos kits y mismo precio que en ML para no generar conflicto entre canales).

---

## 0. Reglas generales de alta (aplican a todos los kits)

| Campo | Qué poner | Estado |
|---|---|---|
| Título | Entre ~25 y 100 caracteres, con palabra clave al inicio (vela + figura + ocasión). Sin emojis, sin MAYÚSCULAS completas, sin "envío gratis", "el mejor", "100% original" | Límite exacto **verificar** en Seller Center (referencias globales hablan de 25–255 caracteres; no confirmado para MX) |
| Categoría | Hogar › Decoración del hogar › Velas y portavelas (o la más parecida que sugiera el sistema) | **verificar** nombre exacto del árbol de categorías MX |
| Marca | Ananda Velas (si pide registro de marca y no la tienes registrada, elegir "Sin marca / genérico") | **verificar** |
| Fotos | Mínimo 5 por kit. **Principal: 1:1, fondo blanco liso**, producto centrado ocupando ~80% del cuadro, sin texto ni logos encima. Recomendado 1200 × 1200 px | Mínimo de resolución y número máximo de fotos **verificar** (referencia: 600 × 600 mín., hasta 9 fotos) |
| Orden de fotos | 1) fondo blanco · 2) todo lo que incluye el kit · 3) vela en la mano (escala) · 4) ambientación navideña · 5) empaque/cajita kraft · 6) foto con medidas · 7) vela encendida **sobre plato resistente al calor** | — |
| Video del producto | 15–30 s: encender, acercar al aroma, mostrar tamaño en la mano, empaque | Duración/formato **verificar** |
| Peso y medidas del paquete | Pesar cada kit **ya empacado** (caja + burbuja) y medir la caja. TikTok cobra el envío con eso | **Pendiente: pesar** (no hay datos en el repo) |
| Tiempo de preparación (handling) | Kits en stock: el mínimo que permita la plataforma. Kit personalizado: el máximo permitido o "pre-venta / hecho bajo pedido" si existe | Opciones y límites **verificar** |
| Stock | Solo lo que ya está fabricado y empacado. El inventario es **compartido con Mercado Libre**: descontar en ambos canales | — |
| Garantía/devoluciones | Política de TikTok Shop MX por defecto + "llega en buen estado o te lo reponemos" | Política oficial **verificar** |

### Advertencia de seguridad (pegar al final de TODAS las descripciones)
```
CUIDADOS Y SEGURIDAD
- Nunca dejes la vela encendida sin supervisión.
- Colócala sobre una superficie plana y resistente al calor.
- Mantenla lejos de niños, mascotas, cortinas, adornos, papel y cualquier material inflamable.
- No la enciendas cerca de ramas de pino, esferas, listones u otra decoración navideña.
- Apágala antes de dormir o salir de casa. No la muevas mientras esté encendida o el material siga líquido.
- Velas de parafina: no las expongas al sol ni a calor; se pueden deformar.
- Velas de soya en lata: recorta la mecha a 5 mm antes de cada uso; la lata se calienta, no la toques encendida.
- Pieza artesanal: puede tener pequeñas variaciones de color y acabado.
```

### Nota de empaque y envío (aplica a todos)
- Caja rígida + plástico burbuja + relleno para que no se mueva. Figuras pintadas: cada pieza en su bolsa de celofán antes de la burbuja.
- **Calor:** la parafina se deforma. No dejar paquetes al sol en el lugar de recolección; en la caja, etiqueta "FRÁGIL / NO EXPONER AL CALOR" (hecha en la Cricut).
- Paquetería: según referencias de terceros TikTok asigna la paquetería (J&T, iMile) y la cobertura inicial era CDMX, Edomex, Guadalajara y Monterrey; algunas cuentas pueden enviar con paquetería propia. **Verificar** en Seller Center la cobertura desde la ciudad de Noemi y quién paga el envío.
- Tarjeta dentro de la caja: agradecimiento + "cuidados y seguridad" + invitación a seguir @anandavelas (sin pedir que compren fuera de TikTok; **verificar** política sobre material impreso con redes).

---

## 1. Precios sugeridos y costo máximo permitido

**Todos los precios son sugeridos y deben validarse con la fórmula de `costos/README.md` antes de publicar** (lo valida el agente `costos-precios`).

Supuestos (todos por **verificar**):
- Comisión TikTok Shop MX: fuentes de terceros dicen 6% general o 10% en Hogar, más ~2% de procesamiento de pago; algunas mencionan 0% los primeros 60–90 días para vendedores nuevos. **No confirmado en Seller Center.** Para no quedarnos cortos se usa **12% total**.
- Envío pagado por el vendedor: **$90 estimado** (mismo supuesto que ML; no confirmado).
- Retenciones ISR/IVA: no incluidas; dependen de que el RFC esté registrado en la plataforma (ver `finanzas-fiscal`).
- Costo unitario real: **no capturado todavía** en `costos/plantilla-costeo.csv`.

Como no hay costos reales, la tabla dice **cuánto puede costar como máximo cada kit** (materiales + empaque + mano de obra + merma) para que el margen sea ≥45%:

```
Costo máximo del kit = Precio × (1 − 0.12 comisión − 0.45 margen) − $90 envío = 0.43 × Precio − 90
```

| # | Kit | Precio catálogo equivalente | Precio TikTok sugerido | Costo máx. del kit | Costo máx. por pieza |
|---|---|---|---|---|---|
| 1 | Borregos de la Abundancia 12 pzs | $385 | **$529** | $137 | $11.4 por borrego (con cajita) |
| 2 | Rompecabezas navideño apilable | $375 | **$529** | $137 | $137 (1 pieza de 4 partes) |
| 3 | Set 3 velas navideñas (Pino, Árbol, Venado) | $250 | **$399** | $81 | $27 |
| 4 | Nacimiento kit 3 piezas | $195 | **$339** | $55 | $18.6 |
| 5 | Kit 2 árboles navideños | $172 | **$319** | $47 | $23.6 |
| 6 | 10 recuerdos Lume mini personalizados | $520 | **$649** | $189 | $18.9 |
| 7 | Kit 2 velas soya lata dorada | $176 | **$329** | $51 | $25.7 |
| 8 | Kit 2 Oso de Ternura | $174 | **$329** | $51 | $25.7 |

> Si el costo real de un kit sale **arriba** del costo máximo, NO se publica a ese precio: subir precio o cambiar el kit. Si TikTok confirma comisión 0% en el periodo de arranque, el margen sube, pero **no bajar precios** por eso: el periodo se termina y el precio se queda.
> Kits 3, 4, 5, 7 y 8 tienen costo máximo muy ajustado. Prioridad de alta: **1, 2, 6** (dejan más) y luego el resto.

---

## 2. Fichas por kit

### Kit 1. Borregos de la Abundancia 12 piezas  (SKU base NV-B12)
**Título:** `Velas Borregos de la Abundancia 12 Piezas Pintadas a Mano Tradición Año Nuevo`
**Descripción corta:**
```
12 borreguitos de vela pintados a mano, uno para cada mes del año. Tradición mexicana para recibir el Año Nuevo con abundancia.
- 12 velas de 6.5 cm de alto x 4.5 cm de ancho
- Cajita kraft lista para regalar + oración de abundancia para cada mes
- Aroma a elegir: manzana canela o pino navideño
- Hechas a mano en México por Ananda Velas
Ideal para regalo de Navidad, intercambio, Año Nuevo, mamá, abuelita o compañeros de trabajo.
```
**Variaciones:** Aroma: Manzana canela / Pino navideño
**Atributos:** Material: parafina · Cantidad: 12 · Medidas c/u: 6.5 × 4.5 cm · Aromática: sí · Hecho a mano: sí · Ocasión: Navidad, Año Nuevo
**Precio sugerido:** $529 (validar con `costos/README.md`; comisión TikTok **verificar**)
**Empaque:** cajita kraft dentro de caja rígida con burbuja; los borregos pintados no deben rozarse entre sí (separadores o papel china).
**Nota:** es el producto estrella para lives y videos (antes/después de pintar, tradición de Año Nuevo). No usar frases como "te traerá dinero" o "garantiza abundancia": es una tradición, no una promesa.

### Kit 2. Rompecabezas Navideño apilable  (NV-ROM)
**Título:** `Vela Navideña Apilable Santa y Muñeco de Nieve 22 cm Pintada a Mano`
**Descripción corta:**
```
Cuatro figuras apilables que forman una torre navideña de 22 cm: base de pino, regalo, Santa Claus y muñeco de nieve.
- Pintada a mano pieza por pieza
- Cajita kraft lista para regalar
- Aroma a elegir: manzana canela o pino navideño
- Medidas: 22 cm de alto x 6.5 cm de ancho
- Hecha a mano en México por Ananda Velas
Centro de mesa, repisa o regalo especial de Navidad.
```
**Variaciones:** Aroma: Manzana canela / Pino navideño
**Atributos:** Material: parafina · Piezas: 4 apilables · Alto: 22 cm · Ancho: 6.5 cm · Hecho a mano: sí
**Precio sugerido:** $529 (validar)
**Empaque:** cada parte envuelta por separado; es la pieza más frágil. Probar envío de prueba antes de abrir stock.

### Kit 3. Set 3 velas navideñas
**Título:** `Set 3 Velas Navideñas Pino Árbol y Venado Aromáticas Decoración`
**Descripción corta:**
```
Incluye:
- 1 Pino (10 x 7.2 cm) verde con punta nevada
- 1 Árbol navideño de hojas (10 x 5 cm) verde con punta nevada
- 1 Venado con moño rojo (9.5 x 7.5 cm)
Aroma a elegir: manzana canela o pino navideño. Cada vela con bolsa de celofán y etiqueta. Hechas a mano en México.
Decora tu mesa navideña o regálalo en el intercambio.
```
**Variaciones:** Aroma: Manzana canela / Pino navideño
**Atributos:** Material: parafina · Cantidad: 3 · Hecho a mano: sí · Ocasión: Navidad
**Precio sugerido:** $399 (validar; costo máximo $81 el set)

### Kit 4. Nacimiento 3 piezas  (NV-NAC × 3)
**Título:** `Velas Nacimiento Sagrada Familia Aromáticas Kit 3 Piezas`
**Descripción corta:**
```
Figura de la Sagrada Familia en vela artesanal.
- 3 velas de 6.2 cm de alto x 4.5 cm de ancho
- Aroma a elegir: manzana canela o pino navideño
- Cada una con bolsa de celofán y etiqueta
- Hechas a mano en México por Ananda Velas
Para posadas, recuerdos de Navidad, Día de Reyes, Candelaria y regalos para la familia.
```
**Variaciones:** Aroma: Manzana canela / Pino navideño
**Atributos:** Material: parafina · Cantidad: 3 · Medidas: 6.2 × 4.5 cm · Ocasión: Navidad, posada
**Precio sugerido:** $339 (validar; costo máximo $55 el kit, muy ajustado)
**Nota:** para posadas de 20–100 piezas, atender por mensajes de TikTok y pasar a `ventas-eventos-mayoreo`. No pedir WhatsApp en la ficha (**verificar** política de datos de contacto).

### Kit 5. Kit 2 árboles navideños  (NV-PIN + NV-ARB)
**Título:** `Kit 2 Velas Árbol de Navidad Pino Aromáticas Hechas a Mano`
**Descripción corta:**
```
Incluye 1 Pino (10 x 7.2 cm) y 1 Árbol de hojas (10 x 5 cm), verdes con punta nevada.
Aroma a elegir: manzana canela o pino navideño. Con bolsa de celofán y etiqueta. Hechas a mano en México por Ananda Velas.
```
**Variaciones:** Aroma: Manzana canela / Pino navideño
**Atributos:** Material: parafina · Cantidad: 2 · Alto: 10 cm
**Precio sugerido:** $319 (validar; costo máximo $47, el más ajustado de todos. Si no cuadra, subir a $349 o no publicar)

### Kit 6. 10 recuerdos Lume mini personalizados  (EV-LMM × 10)
**Título:** `10 Velas Recuerdo Personalizadas Cera de Soya Baby Shower Bautizo Boda`
**Descripción corta:**
```
Recuerdos para baby shower, bautizo, primera comunión, boda, XV años o cumpleaños.
- 10 velas de cera de soya en lata de aluminio con tapa (6 x 2.3 cm)
- Etiqueta personalizada con nombre, fecha y diseño de tu evento
- Aroma a elegir: floral, vainilla, romero, lavanda, champagne o limón italiano
Cómo personalizar: después de comprar, mándanos por mensaje de TikTok el nombre, la fecha y los colores o tema. Te enviamos el diseño para aprobar antes de producir.
Tiempo de elaboración: 5 días hábiles después de aprobar el diseño, más el envío.
¿Necesitas más de 50? Escríbenos por mensaje para precio especial.
```
**Variaciones:** Aroma: Floral / Vainilla / Romero / Lavanda / Champagne / Limón italiano
**Atributos:** Material: cera de soya · Contenedor: lata de aluminio · Cantidad: 10 · Personalizable: sí
**Precio sugerido:** $649 (validar)
**Pendientes a verificar:** si TikTok Shop MX permite productos personalizados / hechos bajo pedido y con qué tiempo máximo de preparación. Si no lo permite, **no publicar** este kit en TikTok y dejarlo en ML, tienda propia y mayoreo. Stock en TikTok = solo lo que se pueda producir en 5 días hábiles sin afectar Navidad (confirmar con `produccion-inventario`).

### Kit 7. Kit 2 velas soya lata dorada  (EV-LMS × 2)
**Título:** `Kit 2 Velas Aromáticas Cera de Soya Lata Dorada para Regalo`
**Descripción corta:**
```
- 2 velas en lata de aluminio dorado con tapa (6 x 4.6 cm)
- Cera de soya
- Aroma a elegir: floral, vainilla, romero, lavanda, champagne o limón italiano
- Con etiqueta Ananda Velas. Hechas a mano en México
Regalo para Navidad, intercambio, cumpleaños, maestras o para consentirte.
```
**Variaciones:** Aroma: Floral / Vainilla / Romero / Lavanda / Champagne / Limón italiano
**Atributos:** Material: cera de soya · Contenedor: lata · Cantidad: 2 · Alto: 4.6 cm · Diámetro: 6 cm
**Precio sugerido:** $329 (validar; costo máximo $51)
**Nota:** no afirmar "no tóxica", "ecológica" ni "combustión 100% limpia" sin respaldo (riesgo de promesa engañosa). Decir solo "cera de soya".

### Kit 8. Kit 2 Oso de Ternura  (EV-OSO × 2)
**Título:** `Kit 2 Velas Decorativas Oso de Ternura Aromáticas Regalo`
**Descripción corta:**
```
- 2 velas en forma de osito (10 x 9.5 cm)
- Color a elegir: beige, rosa, azul claro o amarillo
- Aroma: vainilla (otro aroma de la lista: floral, romero, lavanda o canela, avísanos por mensaje después de comprar)
- Con bolsa de celofán y etiqueta. Hechas a mano en México
Decoración de cuarto, regalo de baby shower o cumpleaños.
```
**Variaciones:** Color: Beige / Rosa / Azul claro / Amarillo
**Atributos:** Material: parafina · Cantidad: 2 · Medidas: 10 × 9.5 cm
**Precio sugerido:** $329 (validar; costo máximo $51)
**Nota:** es decorativa; aunque es para baby shower, en fotos no colocarla al alcance de bebés ni encendida cerca de ellos.

---

## 3. Pendientes antes de publicar
- [ ] Costos reales de cada kit en `costos/plantilla-costeo.csv` y validación de `costos-precios`.
- [ ] Comisión real, tarifa de procesamiento y promoción de vendedor nuevo en Seller Center (**verificar**).
- [ ] Quién paga el envío y cuánto, por peso real del paquete (**verificar**).
- [ ] Límite de caracteres del título y especificaciones de foto/video en MX (**verificar**).
- [ ] Si se permiten productos personalizados/bajo pedido (kit 6) (**verificar**).
- [ ] Pesar y medir cada kit empacado.
- [ ] Stock inicial por kit confirmado con `produccion-inventario` (inventario compartido con ML).
