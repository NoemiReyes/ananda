# Sistema de etiquetas — Ananda Velas

Versión 1 · 9-oct-2026 · Responsable: `diseno-empaque-cricut`
Fuentes: `negocio/catalogo.md` (medidas), `equipo/impresoras.md` (impresora y Cricut), `costos/README.md` (costeo).

> **Antes de imprimir en serie:** las medidas de etiqueta se calcularon con las medidas del catálogo (alto × ancho de la pieza). Mide con regla la tapa, la base y el cuerpo reales de cada contenedor y ajusta si hace falta. Todo lo marcado **verificar** está sin confirmar en fuente oficial.

---

## 1. Identidad visual (aplica a todas las etiquetas)

### Colores
Son una propuesta para empezar. Si el logo "Ananda Candles" ya tiene códigos de color, se usan esos.

| Uso | Nombre | HEX propuesto |
|---|---|---|
| Fondo eventos | Crema | `#F7F2EA` |
| Fondo / bloques | Beige | `#E8DCCB` |
| Acentos, líneas | Topo | `#A39283` |
| Texto principal | Café | `#6B4F3A` |
| Navidad | Rojo | `#A4282B` |
| Navidad | Verde salvia | `#9CAF88` |
| Navidad | Dorado (impreso) | `#C9A44C` |

- **Dorado:** la impresora de tinta no imprime metálico; `#C9A44C` se ve como un mostaza dorado. Si quieres brillo real, se puede aplicar foil con la herramienta Foil Transfer de Cricut (compatible con Maker 3), pero hacer coincidir foil con Imprimir y cortar requiere un segundo paso de registro. **Verificar** con una prueba antes de ofrecerlo.
- Texto siempre en café `#6B4F3A` sobre crema o beige (buen contraste). No pongas texto topo sobre beige: se pierde.

### Tipografías (gratuitas, disponibles en Canva y Google Fonts)
| Rol | Fuente | Uso |
|---|---|---|
| Títulos / nombre del producto | **Cormorant Garamond** (SemiBold) | Serif elegante, combina con lo minimalista |
| Nombres de festejados | **Great Vibes** o **Allura** | Script; solo para nombres, nunca para advertencias |
| Información y advertencias | **Montserrat** (Regular / Medium) | Sans legible en tamaños chicos |

Para usarlas en Cricut Design Space hay que instalarlas en la computadora (Design Space usa las fuentes del sistema).

### Tamaños mínimos de texto
- Nombre en script: mínimo 14 pt.
- Información y advertencias: **mínimo 6 pt** en Montserrat. Debajo de eso la tinta se corre en vinil y no se lee.
- Margen de seguridad: deja 2 mm libres entre el texto y la orilla de corte (la Cricut puede desfasarse un poco al cortar).

---

## 2. Información obligatoria

### Qué lleva cada vela (en la etiqueta frontal, en la de información o entre las dos)
1. **Marca:** Ananda Velas (logo).
2. **Nombre del producto:** p. ej. "Lume Soja · Vela de soya".
3. **Aroma:** p. ej. "Vainilla".
4. **Contenido neto / peso:** "Cont. neto: ___ g". **Pesa la cera de cada producto** (sin contenedor) y anota el dato en `costos/plantilla-costeo.csv` (columna `cera_g`). El catálogo no trae pesos.
5. **Ingredientes / tipo de cera:** "Cera de soya, fragancia, mecha de algodón" o "Parafina, fragancia, colorante, mecha de algodón". **Verificar** el material real de la mecha y si el colorante aplica en cada línea.
6. **Origen:** "Hecho a mano en México".
7. **Contacto / redes:** www.anandavelas.com · @anandavelas (excepto en piezas que se venden por Mercado Libre; ver sección 2.3).
8. **Advertencias de seguridad** (texto de abajo).
9. **Fabricante y domicilio:** la NOM-050-SCFI-2004 (información comercial de productos) pide nombre y domicilio del fabricante, país de origen e instrucciones/advertencias, y la NOM-030-SCFI pide cómo declarar el contenido neto. **Verificar** con `finanzas-fiscal` qué domicilio usar (fiscal o de taller) y si el formato "Cont. neto" cumple. Mientras tanto, deja una línea reservada para el domicilio en la etiqueta de información.

### 2.1 Texto de advertencias (copiar tal cual)

**Versión completa** (etiqueta de información 5 × 3 cm, insertos y tarjetas):
> PRECAUCIÓN: Nunca dejes la vela encendida sin supervisión. Mantenla fuera del alcance de niños y mascotas. Colócala sobre una superficie resistente al calor, lejos de cortinas, papel, adornos y cualquier material inflamable, y lejos de corrientes de aire. Retira etiquetas, listones y celofán antes de encender. Recorta la mecha a 5 mm antes de cada uso. Apágala cuando queden 1 cm de cera.

**Extra para figuras de parafina:**
> Vela decorativa: si la enciendes, ponla sobre un plato, porque la cera escurre.

**Extra para lata y frasco:**
> El recipiente se calienta. No lo muevas encendido.

**Versión corta** (base de lata, círculo 4.5 cm):
> No dejar encendida sin supervisión. Lejos de niños, mascotas y material inflamable. Superficie resistente al calor. Recortar mecha a 5 mm. El recipiente se calienta.

> **Ojo:** el tag de cartulina y el listón **se queman**. Por eso la advertencia dice "retira etiquetas, listones y celofán antes de encender". No la quites del texto.

### 2.2 Bloque de información estándar (etiqueta "INFO")
Plantilla en Montserrat 6 pt, café, alineado a la izquierda:

```
ANANDA VELAS · Lume Soja · Vainilla
Cont. neto: ___ g · Cera de soya, fragancia, mecha de algodón
Hecho a mano en México · anandavelas.com · @anandavelas
[Domicilio del fabricante — verificar]
PRECAUCIÓN: No dejar encendida sin supervisión. Lejos de niños,
mascotas y material inflamable. Usar sobre superficie resistente
al calor. Retirar etiquetas y listón antes de encender. Recortar
mecha a 5 mm. El recipiente se calienta.
```
Son 8 a 9 renglones a 6 pt (unos 2.5 mm por renglón): caben en el área útil de 4.6 × 2.6 cm de la etiqueta de 5 × 3 cm.

### 2.3 Variante Mercado Libre (y TikTok Shop)
Las Políticas de Publicación de Mercado Libre México prohíben enlaces y datos de contacto que lleven a comprar fuera de la plataforma ([fuente](https://www.mercadolibre.com.mx/seguro_publicacion.html)). Esa política habla de las publicaciones. **No encontré una regla oficial sobre lo que va dentro del paquete: verificar con soporte de vendedores.** Mientras se confirma, para lo que se venda por ML o TikTok Shop:
- Sí: marca y logo, nombre, aroma, contenido, ingredientes, "Hecho a mano en México", domicilio del fabricante (es obligatorio) y advertencias.
- No: web, @anandavelas, WhatsApp, QR ni cupones.
- Ten dos archivos de etiqueta INFO: `INFO-directa` y `INFO-marketplace`.

---

## 3. Medidas por producto

Las medidas de las piezas vienen del catálogo; las de las etiquetas son propuesta. **Verificar con el contenedor real.**

| Producto (SKU) | Pieza | Etiqueta frontal / principal | Etiqueta de información | Material |
|---|---|---|---|---|
| **Lume Soja Mini** (EV-LMM), lata plateada 2.3 × 6 cm | Tapa Ø 6 cm | Círculo **Ø 5 cm** en la tapa (deja libre el borde) | Círculo **Ø 4.5 cm** en la base, versión corta | Vinil imprimible para inyección |
| **Lume Soja** (EV-LMS), lata dorada 4.6 × 6 cm | Tapa Ø 6 cm | Círculo **Ø 5 cm** en la tapa | Círculo **Ø 4.5 cm** en la base | Vinil imprimible para inyección |
| **Glowing Glass** (EV-GLO), frasco 5.8 × 6.7 cm, tapa dorada | Cuerpo del frasco | Rectángulo **5 × 3 cm**, esquinas redondeadas a 3 mm, en el frente | Rectángulo **5 × 3 cm** atrás del frasco (INFO completa) | Vinil imprimible para inyección |
| Glowing Glass: tapa | Tapa dorada | Opcional: déjala sin etiqueta para que luzca el dorado | — | — |
| **Figuras de parafina** (EV-OSO, JIR, ELE, DIN, ANG, FLO, BUN, NV-VEN, NAC, PIN, ARB, BOR), en bolsa de celofán | Tag colgante | Tag **5 × 7 cm**, esquinas superiores recortadas en diagonal a 8 mm, perforación de Ø 5 mm centrada a 7 mm del borde superior | Etiqueta INFO **5 × 3 cm** pegada atrás del tag | Tag: cartulina opalina o kraft de 200–250 g. INFO: papel adhesivo mate |
| Cierre de bolsa de celofán u organza | Sello | Círculo **Ø 3.8 cm** con el logo | — | Papel adhesivo mate |
| **Paquete Recuerdos** (EV-PRE), bolsa de organza | Tag | Tag 5 × 7 cm (igual que figuras) | INFO 5 × 3 cm atrás del tag (soya + jabón de glicerina) | Igual que figuras |
| **Borregos de la Abundancia** (NV-B12) y **Rompecabezas** (NV-ROM), cajita kraft | Tapa de la caja | Rectángulo **7 × 4 cm** al frente de la tapa | INFO 5 × 3 cm en la base de la caja | Papel adhesivo mate |
| **Corporativo** | Tarjeta con mensaje | Tarjeta **9 × 5 cm** (tamaño de tarjeta de presentación) | — | Cartulina 200–250 g |

Notas:
- **Tags de figuras:** con Imprimir y cortar se imprime solo una cara. Por eso la información va en una etiqueta INFO adhesiva pegada atrás del tag y no en impresión por las dos caras, que sale chueca.
- **Perforación del tag:** dibuja el círculo de 5 mm y haz Slice/Recortar con el tag antes de aplanar (Flatten). **Verificar** que Design Space corte el hoyo interior en Imprimir y cortar. Si no lo corta, usa una perforadora de 1/8" o 3/16". Para colgar: yute natural o listón satinado de 3 mm en el color del tema.
- **Lume Mini:** mide solo 2.3 cm de alto, así que no lleva etiqueta lateral. Todo va en la tapa (diseño) y en la base (información).
- **Glowing Glass:** antes de pegar, limpia el vidrio con alcohol y deja que seque. Pega la etiqueta con la vela ya fría, nunca recién vaciada.

---

## 4. Plantillas por tema de evento

Regla de oro: **en cada plantilla solo cambian el NOMBRE y la FECHA** (y en corporativo, el logo). Todo lo demás queda fijo para producir rápido. Guarda un archivo maestro por tema y por tamaño (tag 5 × 7, tapa Ø 5, frente 5 × 3).

Estructura común del tag de 5 × 7 cm (de arriba abajo):
1. Perforación (zona libre de 1.4 cm).
2. Ilustración o ícono de línea delgada, 1.5–2 cm.
3. Nombre en script, 18–24 pt.
4. Motivo o frase en Cormorant Garamond, 8–9 pt.
5. Fecha en Montserrat, 7 pt, con espaciado amplio entre letras (p. ej. 12 · 12 · 2026).
6. Logo Ananda chico (0.8 cm) abajo al centro.

En la tapa de Ø 5 cm, la misma estructura sin perforación: ícono arriba, nombre al centro, fecha en arco abajo.

| Tema | Paleta (fondo / acento / texto) | Ícono sugerido | Velas que combinan | Texto ejemplo |
|---|---|---|---|---|
| **Baby shower niño** | Crema `#F7F2EA` / azul claro `#BFD3E6` / café | Osito, nube, huellitas | Oso, Elefante, Jirafa (azul claro) | "Gracias por acompañarnos a esperar a **Mateo** · Baby shower · 15 · 11 · 2026" |
| **Baby shower niña** | Crema / rosa palo `#EBC8C4` / café | Conejito, moño, estrellas | Bunny Happy, Oso (rosa) | "Con amor esperamos a **Valentina** · 22 · 11 · 2026" |
| **Baby shower neutro** | Crema / beige / topo | Luna y estrellas | Oso beige, Lume | "Pronto llegará **Bebé García** · Gracias por venir" |
| **Bautizo** | Blanco / beige / dorado `#C9A44C` | Paloma o cruz de línea fina | Ángeles Divinos, Glowing Glass | "Recuerdo de mi Bautizo · **Santiago** · 06 · 12 · 2026" |
| **Primera comunión** | Crema / dorado / café | Cáliz, espigas | Ángeles, Lume Soja dorada | "Mi Primera Comunión · **Regina** · 13 · 12 · 2026" |
| **Boda** | Crema / verde salvia `#9CAF88` / café | Ramita de eucalipto, iniciales | Glowing Glass, Lume Soja, Flowers On | "**Ana & Luis** · Gracias por ser parte de nuestro amor · 19 · 12 · 2026" |
| **XV años** | Crema / rosa palo / dorado | Corona o mariposa | Flowers On, Glowing Glass | "Mis XV años · **Ximena** · 28 · 11 · 2026" |
| **Cumpleaños** | Beige / topo / café; o el color que pida el cliente | Número de años en Cormorant grande | Cualquiera | "**Emilio** cumple 3 · Gracias por celebrar conmigo" |
| **Safari** | Arena `#E8DCCB` / verde salvia / café | Hojas de palma | Jirafa, Elefante | "Safari de **Leo** · 1er cumpleaños · 08 · 11 · 2026" |
| **Dinosaurios** | Crema / verde salvia / café | Huella de dino | Dino T-Rex | "¡**Diego** cumple 5! · Dino fiesta · 15 · 11 · 2026" |
| **Navidad (regalo)** | Crema / rojo `#A4282B` / verde salvia, detalles dorado | Ramita de pino, estrella | Venado, Pino, Árbol, Borrego, Nacimiento | "Feliz Navidad · Con cariño, **Familia López** · 2026" |
| **Navidad (corporativo)** | Crema / verde salvia / dorado, sin rojo para que el logo resalte | Logo del cliente | Pino, Lume Soja, Glowing Glass | "**[Empresa]** te desea una Feliz Navidad y un próspero 2027" |

Nombres largos: si el nombre pasa de 12 caracteres, baja el script a 16 pt o parte en dos renglones. Nunca bajes de 14 pt.

---

## 5. Flujo de personalización (eventos)

1. **Recibir datos** por WhatsApp o Instagram, con este formulario fijo:
   - Tema · Producto(s) y cantidad · Nombre(s) exacto(s), con acentos · Fecha del evento · Frase (opcional; si no, se usa la de la plantilla) · Color de vela y aroma · Fecha de entrega requerida · Canal (local o envío).
2. **Confirmar capacidad y fecha** con `produccion-inventario` antes de aceptar (CLAUDE.md, regla 4).
3. **Anticipo:** pedidos personalizados de mayoreo pagan **50%** antes de imprimir (`costos/README.md`, regla 4).
4. **Prueba digital:** exporta un PNG del tag o tapa sobre una foto de la vela real (mockup) y envíalo. Incluye este texto: "Revisa nombre, acentos y fecha. Al responder APRUEBO autorizas la impresión; después no se pueden hacer cambios sin costo."
5. **Cambios:** incluye hasta 2 rondas de cambios. Desde la tercera, se cotiza aparte (el precio lo define `costos-precios`).
6. **Aprobación por escrito:** guarda una captura del "APRUEBO" en la carpeta del pedido.
7. **Hoja de prueba:** imprime y corta 1 hoja, pega una etiqueta en una vela real, revisa color y corte, y manda la foto al cliente (en corporativo es obligatorio).
8. **Impresión en serie** con el flujo de la sección 8. Imprime **10% extra** (mínimo 2 etiquetas) para cubrir merma.
9. **Archivar:** guarda el archivo final con el nombre `AAAA-MM-DD_cliente_tema_producto_cantidad` para reimpresiones.

---

## 6. Etiqueta corporativa con logo del cliente

### Formatos
- Tapa de lata Ø 5 cm: logo del cliente al centro (máximo 3 cm de ancho), con la marca Ananda chica en el arco inferior o solo en la base.
- Frente de Glowing Glass 5 × 3 cm: logo a la izquierda (2 cm) y frase de la empresa a la derecha.
- Tag 5 × 7 cm: logo arriba y mensaje corto.
- **Tarjeta con mensaje 9 × 5 cm** (cartulina): logo y mensaje de la empresa de un lado, máximo 40 palabras en Cormorant 9–10 pt. Si el cliente lo pide, el nombre del destinatario va en script.

### Requisitos del archivo del logo (pídelos al cotizar)
| Requisito | Preferido | Aceptable | No aceptable |
|---|---|---|---|
| Formato | Vectorial: **SVG, PDF vectorial, AI o EPS** | **PNG con fondo transparente** | JPG de WhatsApp, captura de pantalla, logo copiado de redes |
| Resolución (si no es vector) | — | **300 ppp al tamaño final**. Para un logo de 3 cm de ancho son al menos 360 px; pide **1000 px o más** | Menos de 300 ppp al tamaño final |
| Color | Códigos HEX/CMYK o Pantone del manual de marca | El logo tal cual | — |
| Versiones | Logo a color y versión en una sola tinta (blanco o negro) | — | — |

- **Color:** la impresión de tinta no reproduce Pantone exactos, sobre todo colores neón o metálicos. El cliente aprueba **la foto de la hoja de prueba impresa**, no la pantalla. Déjalo por escrito en la cotización.
- **Derechos:** al mandar el logo, el cliente confirma que es suyo o que tiene permiso de usarlo. Agrega esta línea en la cotización: "El cliente garantiza que tiene derecho de uso del logotipo enviado."
- **Aprobación:** sigue el mismo flujo de la sección 5. En corporativo, la hoja de prueba física es obligatoria y se cobra el 50% de anticipo.

---

## 7. Planillas de Imprimir y cortar (Cricut Maker 3)

### 7.1 Límites
- Área máxima de Imprimir y cortar en hoja carta: **6.75" × 9.25" = 17.14 × 23.50 cm** (dato de `equipo/impresoras.md`, coincide con guías de terceros). En otras fuentes se menciona que versiones recientes de Design Space amplían el área en algunos modelos. **Verificar** en help.cricut.com y en la pantalla Preparar de Design Space (ahí se ve el límite como línea roja punteada). Las cuentas de abajo usan el área de 17.14 × 23.50 cm.
- **Separación entre etiquetas: 0.6 cm (≈ 1/4")**. Cubre el sangrado (bleed) que agrega Design Space y el margen de error del corte. El ancho exacto del sangrado **está sin verificar**; si ves que las etiquetas se enciman o el corte se sale, sube la separación a 0.8 cm.
- Las esquinas del área quedan cerca de las marcas de registro. Si Design Space marca error, quita la etiqueta de una esquina o reduce 1–2 mm.

### 7.2 Cálculo
Fórmula por cada lado: **piezas = piso[(lado disponible + separación) ÷ (medida de la etiqueta + separación)]**
Ancho disponible + separación = 17.14 + 0.6 = **17.74 cm** · Alto disponible + separación = 23.50 + 0.6 = **24.10 cm**

| Etiqueta | Medida | Columnas | Filas | **Por hoja** |
|---|---|---|---|---|
| Tapa de lata | Ø 5 cm | 17.74 ÷ 5.6 = 3.17 → **3** | 24.10 ÷ 5.6 = 4.30 → **4** | **12** |
| Base de lata (INFO corta) | Ø 4.5 cm | 17.74 ÷ 5.1 = 3.48 → **3** | 24.10 ÷ 5.1 = 4.73 → **4** | **12** |
| Frente Glowing Glass / INFO | 5 × 3 cm (horizontal) | 17.74 ÷ 5.6 = 3.17 → **3** | 24.10 ÷ 3.6 = 6.69 → **6** | **18** |
| Tag de figura | 5 × 7 cm (vertical) | 17.74 ÷ 5.6 = 3.17 → **3** | 24.10 ÷ 7.6 = 3.17 → **3** | **9** |
| Tag de figura (girado) | 7 × 5 cm | 17.74 ÷ 7.6 = 2.33 → 2 | 24.10 ÷ 5.6 = 4.30 → 4 | 8 (peor, no usar) |
| Sello de bolsa | Ø 3.8 cm | 17.74 ÷ 4.4 = 4.03 → **4** | 24.10 ÷ 4.4 = 5.48 → **5** | **20** |
| Tapa de cajita kraft | 7 × 4 cm | 17.74 ÷ 7.6 = 2.33 → **2** | 24.10 ÷ 4.6 = 5.24 → **5** | **10** |
| Tapa de cajita kraft (girada) | 4 × 7 cm | 17.74 ÷ 4.6 = 3.86 → **3** | 24.10 ÷ 7.6 = 3.17 → **3** | 9 |

Comprobación de que la planilla cabe (ejemplo, tag 5 × 7): 3 × 5 + 2 × 0.6 = 16.2 cm ≤ 17.14 ✔ · 3 × 7 + 2 × 0.6 = 22.2 cm ≤ 23.50 ✔.
Comprobación de los círculos de Ø 5: 3 × 5 + 2 × 0.6 = 16.2 ✔ · 4 × 5 + 3 × 0.6 = 21.8 ✔.

Acomodar los círculos en filas desfasadas (tipo panal) **no mejora** el resultado en este tamaño: en las filas desfasadas solo caben 2 círculos. Usa cuadrícula.

### 7.3 Planillas combinadas recomendadas (rinden más en producción)
| Planilla | Contenido | Rinde |
|---|---|---|
| **P-LUME** (vinil) | 6 tapas Ø 5 + 6 bases Ø 4.5, en la misma cuadrícula de 3 × 4 | **6 latas completas por hoja** |
| **P-GLASS** (vinil) | 9 frentes 5 × 3 + 9 INFO 5 × 3, en cuadrícula de 3 × 6 | **9 frascos completos por hoja** |
| **P-TAG** (cartulina) | 9 tags 5 × 7 | 9 figuras |
| **P-INFO** (papel adhesivo mate) | 18 INFO 5 × 3 | Atrás de 18 tags (1 hoja P-INFO por cada 2 de P-TAG) |
| **P-SELLO** (papel adhesivo mate) | 20 sellos Ø 3.8 | 20 bolsas |

Hojas por pedido (con 10% extra de merma), ejemplo de **50 Glowing Glass**: 55 juegos ÷ 9 por hoja = 6.1 → **7 hojas P-GLASS**.
Ejemplo de **100 figuras con tag**: 110 ÷ 9 = 12.2 → **13 hojas P-TAG** + 110 ÷ 18 = 6.1 → **7 hojas P-INFO** + 110 ÷ 20 = 5.5 → **6 hojas P-SELLO**.

### 7.4 Papel recomendado (impresora de inyección Epson EcoTank L3250 o L8050)
| Uso | Papel | Tapete Cricut | Ajuste de material en Design Space (**verificar** nombre exacto en tu versión) |
|---|---|---|---|
| Latas y frascos (humedad, aceite de fragancia) | **Vinil imprimible para inyección**, de preferencia blanco mate | LightGrip (azul) | "Printable Vinyl" / "Vinil imprimible" |
| Sellos, INFO de tags y cajas | **Papel adhesivo mate para inyección** | LightGrip (azul) | "Printable Sticker Paper" / "Papel para stickers imprimible" |
| Tags y tarjetas | **Cartulina opalina o kraft de 200–250 g** | StandardGrip (verde) | "Medium Cardstock" (≈ 200–216 g) o "Heavy Cardstock" (≈ 250–270 g). Haz un corte de prueba |

- **Protección del vinil:** la tinta de inyección se corre con el agua y con el aceite de fragancia. Para latas y frascos, pon **laminado transparente autoadherible mate** sobre la hoja impresa y seca **antes** de cortar, o usa un sellador en spray para papel. **Verificar** que la Maker 3 corte vinil y laminado juntos con el ajuste "Printable Vinyl" y más presión: haz una prueba.
- **Lectura de marcas:** los papeles brillantes o laminados pueden reflejar luz y hacer que la Cricut no lea las marcas de registro. Prefiere acabados mate y evita luz directa sobre la máquina. Un truco que circula en comunidades de usuarios (no es oficial) es poner cinta mate sobre las marcas.
- **Kraft:** la tinta blanca no existe en inyección. En cartulina kraft el texto debe ser café oscuro o negro, y los colores claros se pierden.
- Ajusta la impresora con su controlador: tipo de papel "Mate" o "Papel fotográfico mate", calidad **Alta**.

### 7.5 Flujo paso a paso
1. **Una sola vez:** calibra Imprimir y cortar en Design Space (Menú → Calibración → Imprimir y cortar) con la impresora instalada.
2. **Diseñar** en Canva a tamaño real (p. ej. lienzo de 5 × 7 cm). Exporta en **PNG, fondo transparente si la forma no es rectangular, calidad máxima** (Canva Pro) o en PDF para impresión.
3. **Subir** a Design Space → Cargar → elige "Imagen compleja" → elimina el fondo sobrante → guárdala como **"Imagen para imprimir y cortar"**.
4. **Ajustar medida exacta** en el panel (W/H) a la medida de la tabla.
5. **Armar la planilla:** duplica y acomoda en cuadrícula con 0.6 cm de separación. Si necesitas que no se muevan de lugar, selecciona todo y usa **Aplanar (Flatten)**: así Design Space respeta tu acomodo en vez de reorganizar las piezas. **Verificar** en tu versión; la alternativa es Adjuntar (Attach).
6. Clic en **Hacer (Make)** y revisa que todo quede dentro de la línea roja punteada.
7. **Enviar a la impresora:** activa **Agregar sangrado (Add bleed)** y activa **"Usar diálogo del sistema"** para elegir en la impresora papel mate y calidad alta.
8. **Secar 5 minutos.** En vinil, aplica aquí el laminado.
9. **Cargar en el tapete** alineando la esquina superior izquierda con la cuadrícula del tapete.
10. **Elegir material** (tabla 7.4) y presión ("Más" si el corte no atraviesa).
11. **Cortar.** La máquina lee las marcas y corta.
12. **Revisar la primera hoja** de cada tanda: corte centrado, color y texto legible. Si el corte sale desfasado, recalibra (paso 1).
13. **Despegar** volteando el tapete y doblando el tapete, no el papel, para que no se enrolle. Guarda las etiquetas en sobre o carpeta por pedido.

### 7.6 Costo por etiqueta (para `costos-precios`)
Todavía no hay precios reales de papel ni de tinta en el repo. **Noemi debe capturarlos.** Fórmula:

```
Costo por hoja   = precio del paquete ÷ hojas del paquete
                   + tinta por hoja (estimado)
                   + laminado por hoja (solo vinil)
Costo por etiqueta = Costo por hoja ÷ etiquetas por hoja × 1.10   (10% de merma)
Costo etiqueta por producto = suma de las etiquetas que lleva (p. ej. lata = tapa + base)
```

| Producto | Etiquetas que lleva | Hoja(s) | Fórmula del costo de etiqueta |
|---|---|---|---|
| Lume Mini / Lume | Tapa + base | P-LUME (6 juegos) | Hoja vinil ÷ 6 × 1.10 |
| Glowing Glass | Frente + INFO | P-GLASS (9 juegos) | Hoja vinil ÷ 9 × 1.10 |
| Figura | Tag + INFO + sello | P-TAG ÷ 9 + P-INFO ÷ 18 + P-SELLO ÷ 20 | (Cartulina ÷ 9 + Adhesivo ÷ 18 + Adhesivo ÷ 20) × 1.10 |
| Cajita kraft (NV-B12, NV-ROM) | Tapa 7 × 4 + INFO | 10 por hoja + 18 por hoja | (Adhesivo ÷ 10 + Adhesivo ÷ 18) × 1.10 |

Ejemplo **ilustrativo, no es un precio real**: si una hoja de vinil con tinta y laminado costara $15, cada juego de Glowing Glass costaría 15 ÷ 9 × 1.10 = **$1.83**. El resultado va en la columna `etiqueta` de `costos/plantilla-costeo.csv` (la edita el chat de Producción y costos).

Además del papel, hay que contar el desgaste de la navaja y de los tapetes. Es un costo chico, pero se puede sumar como un porcentaje **estimado** cuando Noemi sepa cada cuántas hojas los reemplaza.
