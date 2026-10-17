# Impresión con colores vivos: Epson L3560 + Imprimir y cortar

Versión 1 · sáb 17-oct-2026 · Responsable: `tecnico-cricut` (chat Mayoreo y eventos)
Para: Noemi y Angélica. Caso: etiquetas de Día de Muertos (veladora en vaso, papel picado con nombre) que salen **opacas** en papel adhesivo mate y glossy.

> Todo lo marcado **verificar** no lo confirmé en una fuente oficial de Cricut, Epson o Canva, o el nombre del botón puede cambiar según la versión y el idioma de la app. Si en tu pantalla dice otra cosa, anota el nombre real aquí.

---

## 1. Lo que se ve en la foto del 17-oct

- **Hoja mate (izquierda):** colores completos, sin rayas ni huecos, pero lavados: el amarillo del papel picado se ve mostaza pálido, el rosa y el naranja se ven pastel y las fotos sepia y en blanco y negro se ven grises, sin negros profundos. El azul marino sí se ve oscuro.
- **Hoja glossy (derecha):** el mismo diseño se ve más saturado que en la mate, aunque también un poco apagado.
- **Diagnóstico rápido:** no faltan colores ni hay rayas, así que **es poco probable que los inyectores estén tapados**. El patrón "todo salió, pero claro y plano" es típico de imprimir con la impresora en **"Papel normal" y calidad estándar**, que pone menos tinta.
- Del corte: en los huecos de las piezas despegadas el sangrado se quedó en el sobrante, lo cual es normal. Se ve una orilla de color un poco más ancha de un lado que del otro. No es urgente, pero revisa que ninguna etiqueta salga con un filo blanco. Si pasa, recalibra (sección 7).

---

## 2. Causas probables, de la más a la menos probable

| # | Causa | Qué tan probable | Cómo saberlo | Solución |
|---|---|---|---|---|
| 1 | **Design Space imprimió con su propio cuadro de diálogo** y la Epson usó su ajuste por omisión (casi siempre "Papel normal", calidad estándar). Sin activar **Usar diálogo del sistema (Use System Dialog)** no puedes elegir tipo de papel ni calidad. | **Muy alta** | Si al imprimir no se abrió la ventana de Epson con "Tipo de papel" y "Calidad", fue esto. | Activar **Usar diálogo del sistema** en cada impresión (sección 3). Cricut recomienda usarlo para elegir la calidad más alta de tu impresora. |
| 2 | **Tipo de papel y calidad incorrectos en el controlador de Epson.** Con "Papel normal" el controlador limita la tinta para no empapar la hoja (dato de guías de modelos parecidos, **verificar** en el manual de la L3560). | **Muy alta** (va de la mano con la 1) | Abre las preferencias de la impresora y revisa qué dice "Tipo de papel". | Mate → papel fotográfico mate; glossy → papel fotográfico brillante; calidad **Alta** (sección 3). |
| 3 | **Papel mate por naturaleza.** El mate dispersa la luz: los colores nunca se ven tan intensos como en glossy ni como en pantalla. | **Alta** (explica la diferencia entre las dos hojas) | Comparas las dos hojas impresas con el mismo ajuste. | No se "arregla" del todo. Mejora con el ajuste correcto y con el **laminado** encima (sección 6). |
| 4 | **Diferencia entre la pantalla y el papel.** La pantalla tiene luz propia y colores RGB más intensos de lo que puede imprimir una impresora de 4 tintas. El naranja intenso y el rosa mexicano se apagan un poco siempre. | **Alta** como parte de la percepción | Compara la hoja con la pantalla con el brillo de la pantalla al 50%. | Aprobar color con la **hoja impresa**, no con la pantalla. Subir un poco la saturación en el diseño si hace falta (sección 5). |
| 5 | **Exportación de Canva.** "PDF para impresión" con perfil **CMYK** apaga los colores vivos. JPG comprime y ensucia los degradados. Un PNG chico se ve borroso (eso afecta la nitidez, no tanto el color). | Media | ¿Exportaste en PDF con CMYK, o en JPG? Revisa los píxeles del archivo. | Exporta en **PNG**, RGB, al tamaño más grande que permita Canva (sección 5). |
| 6 | **Design Space reduce o aplana las imágenes grandes** al subirlas o al mandarlas a imprimir. Hay quejas de usuarios, pero no encontré un dato oficial de resolución máxima. **Verificar.** | Media-baja | Prueba C de la sección 4: la misma imagen impresa desde Canva y desde Design Space con el mismo ajuste. | Si Design Space sale peor, sube PNG a tamaño final (no más grande) y usa el PNG sin agrandarlo dentro de Design Space. |
| 7 | **Tinta nueva: carga inicial incompleta o un inyector tapado.** | Baja (no se ven rayas ni colores faltantes) | **Revisión de inyectores (Nozzle Check)**: el patrón debe salir completo en los 4 colores. | Si falta algo: **Limpieza de cabezales (Head Cleaning)**, esperar y repetir la revisión (sección 3, paso 1). |
| 8 | **Sangrado (Add bleed) de Design Space.** Solo extiende el color de la orilla unos milímetros fuera del corte para que no quede filo blanco. No apaga los colores. | Muy baja | — | Déjalo **activado**. |

---

## 3. Pasos para la próxima impresión (hoy)

### Paso 1. Revisión de inyectores (2 minutos, una sola vez hoy)
1. Pon una hoja de papel bond normal en la bandeja (no gastes adhesivo en esto).
2. **Windows:** Inicio → Configuración → Impresoras → Epson L3560 → **Preferencias de impresión** → pestaña **Mantenimiento (Maintenance)** → **Test de inyectores (Nozzle Check)**. **Mac:** Preferencias del sistema → Impresoras → Epson L3560 → Opciones y recambios → Utilidad → **Test de inyectores**. También se puede hacer desde el panel de la impresora. Nombres exactos: **verificar** en tu equipo.
3. Si el patrón sale completo en negro, cian, magenta y amarillo, sigue al paso 2. Si falta algún renglón: **Limpieza de cabezales (Head Cleaning)** una vez, espera 5 minutos y repite el test. Si después de 2 limpiezas sigue igual, avísame antes de hacer más (gastan tinta).

### Paso 2. En Design Space, al mandar a imprimir
1. Abre el proyecto → **Hacer (Make)** → revisa la pantalla de preparar → **Continuar (Continue)**.
2. Clic en **Enviar a la impresora (Send to Printer)**.
3. En la ventana de impresión de Cricut:
   - **Impresora:** Epson L3560.
   - **Agregar sangrado (Add Bleed):** activado.
   - **Usar diálogo del sistema (Use System Dialog):** **activado**. Esto es lo que te faltaba.
4. Clic en **Imprimir (Print)**. Se abre la ventana de impresión de Windows o Mac. A veces queda **escondida detrás de Design Space**: si no la ves, minimiza Design Space.

### Paso 3. En la ventana de Epson (diálogo del sistema)
1. **Windows:** clic en **Preferencias (Preferences)** o **Propiedades (Properties)**. **Mac:** en el menú desplegable elige **Ajustes de impresión (Print Settings)**.
2. **Tamaño de papel:** Carta (Letter), el mismo que elegiste en Design Space. Si usas el glossy A4, elige A4 en los dos lados.
3. **Tipo de papel (Paper Type):**
   - Adhesivo **mate** → **Epson Matte / Papel mate** (o "Presentation Paper Matte", según cómo aparezca). **Verificar** el nombre exacto en tu lista.
   - Adhesivo **glossy** → **Epson Premium Glossy / Papel fotográfico brillante** (o "Photo Paper Glossy").
   - **Nunca "Papel normal" (Plain Paper)** para etiquetas.
4. **Calidad (Quality):** **Alta (High)**. En Mac puede aparecer como "Fina" o "Superfina" (**verificar**).
5. **Escala / Ajustar a página:** 100%, sin "ajustar a página" ni márgenes estrechos (Cricut lo pide así para que las marcas no se muevan).
6. **Color:** déjalo en **Automático** para esta prueba. No actives escala de grises.
7. **Aceptar** → **Imprimir**.

### Paso 4. Secado y laminado
1. Mate: deja secar **5–10 minutos**. Glossy: **15–30 minutos** (la tinta de colorante tarda más en el brillante y se embarra si la tocas).
2. Lamina **solo las etiquetas**, sin cubrir las marcas negras de las esquinas (la Cricut no las lee a través del laminado).
3. Carga en el tapete y corta como siempre.

### Paso 5. Anota el resultado
Escribe en la orilla de la hoja con lápiz: papel, tipo de papel elegido, calidad. Así sabemos qué ajuste quedó.

---

## 4. Prueba rápida de comparación (15 minutos, usa 1 hoja mate y 1 glossy)

Objetivo: que tú misma veas qué cambia el color, sin gastar una hoja por ajuste.

### Preparar el archivo de prueba (Canva, 5 minutos)
1. Crea un diseño **carta, 21.6 × 27.9 cm**.
2. Arriba pon una **tira de prueba** de 17 × 5 cm con: 4 cuadros de 2 × 2 cm con los colores exactos de tus diseños (naranja, rosa mexicano, morado y azul marino), un trozo de la foto sepia y otro de la foto en blanco y negro, y el nombre "Margarita" en blanco sobre naranja.
3. Duplica la página 2 veces. En la página 2 mueve la tira al **centro** de la hoja; en la página 3, a la **parte de abajo**. Escribe a un lado de cada tira "A", "B" o "C".
4. Descarga: **Compartir → Descargar → PNG**, todas las páginas.

### Imprimir (la misma hoja pasa 3 veces por la impresora)
Imprime desde el visor de imágenes o desde Canva (no desde Design Space), con el diálogo de Epson:

| Pasada | Página | Tipo de papel | Calidad |
|---|---|---|---|
| A | 1 (arriba) | **Papel normal** | Estándar (así salió tu hoja) |
| B | 2 (centro) | **Papel mate** (Epson Matte) | **Alta** |
| C | 3 (abajo) | **Papel fotográfico brillante** (Premium Glossy) | **Alta** |

Entre pasada y pasada, espera 5 minutos y vuelve a meter **la misma hoja** con la misma orientación. Hazlo en el adhesivo mate y repítelo en el glossy.

### Prueba D (opcional): Design Space contra Canva
Sube a Design Space solo la tira de prueba como PNG e imprímela con Imprimir y cortar, **con el mejor ajuste de A–C** y el diálogo del sistema activado. Si se ve igual que la tira impresa desde Canva, Design Space no es el problema. Si se ve peor o borrosa, el problema es la imagen (causa 6): avísame.

### Prueba E (opcional): laminado
Lamina la **mitad derecha** de la mejor tira. Así ves cuánto sube el color con el laminado.

### Cómo leer el resultado
- Si B o C se ven claramente mejor que A, el problema era el ajuste del controlador (causas 1 y 2). Ese ajuste queda fijo para la producción.
- Mate con "Papel mate" frente a mate con "Papel fotográfico brillante": quédate con el que se vea más intenso **sin que la tinta se corra ni tarde en secar**. En papeles adhesivos que no son de Epson a veces el ajuste "equivocado" da mejor resultado; por eso se prueba.
- Si las tres se ven igual de apagadas, revisa el archivo de Canva (sección 5) y el test de inyectores.

Anota el ganador en `diseno/tecnico/ajustes-material.md` (papel, tipo de papel, calidad, fecha).

---

## 5. Exportar desde Canva sin perder color

1. **Formato:** **PNG**. No JPG (comprime) y, para estas etiquetas, no "PDF para impresión" (PDF Print).
2. Si usas PDF para impresión, revisa que el **Perfil de color** quede en **RGB** y no en **CMYK** (la opción CMYK es de Canva Pro). La conversión a CMYK apaga el naranja, el rosa mexicano y el morado. **Verificar** en tu menú de descarga.
3. **Tamaño:** en Canva Pro usa el control de **Tamaño** al máximo. Revisa los píxeles del PNG (clic derecho → Propiedades → Detalles). Para que se vea nítido a 300 ppp, la etiqueta de veladora de ~19 cm de largo necesita unos **2,250 px**; el mínimo aceptable es la mitad (150 ppp, ~1,125 px). La resolución con la que Canva exporta los diseños en cm: **verificar**.
4. **Fondo transparente** solo si la forma no es rectangular (Canva Pro).
5. En Design Space **no agrandes** la imagen después de subirla: ajusta el W/H a la medida final y listo. Achicar no pasa nada; agrandar la vuelve borrosa.
6. **Fotos sepia o en blanco y negro:** en Canva, en la foto → **Editar** → **Ajustar**, sube un poco **Contraste** (+10 a +20) y baja un poco **Sombras** para que los negros salgan más profundos. Haz una sola prueba antes de cambiar todas.
7. **Colores muy intensos de pantalla:** si después de corregir la impresora el rosa o el naranja siguen pálidos, sube la saturación en Canva solo un poco, no a ojo de pantalla, y compara con la hoja impresa.

---

## 6. Qué esperar de cada papel

| Papel | Color | Lectura de marcas en la Cricut | Uso |
|---|---|---|---|
| Adhesivo **mate** | Menos intenso por naturaleza | La lee mejor | Material principal (decisión del 15-oct) |
| Adhesivo **glossy** | Más intenso, negros más profundos | Puede fallar por reflejo: evita luz directa sobre la máquina | Veladoras con foto, si lo prefieres (decisión del 9-oct) |
| Cualquiera + **laminado transparente** | El laminado hace que el color se vea más rico, sobre todo el brillante | No lamines las marcas | Siempre en la veladora |

El mate bien configurado y laminado debería verse bien en la veladora. No hace falta comprar otro papel ni otra impresora para esto.

---

## 7. Si después de corregir el color el corte sale desfasado

1. Design Space → menú → **Calibración (Calibration)** → **Imprimir y cortar (Print Then Cut)**.
2. Sigue los pasos con una hoja de papel bond. Recalibra si cambias de computadora, de impresora o de controlador.

---

## 8. Costo (para `costos-precios`)

Calidad **Alta** y tipo de papel fotográfico gastan **más tinta** por hoja que "Papel normal". Todavía no hay dato medido de tinta por hoja en la L3560. Cuando se rellene un frasco, anota cuántas hojas de etiquetas salieron para calcular el costo real (**estimado** mientras tanto).

---

## Fuentes
- Cricut, cómo hacer Imprimir y cortar (calidad más alta, "Use System Dialog", sin escalar ni márgenes estrechos): [help.cricut.com 38613592650903](https://help.cricut.com/hc/en-us/articles/38613592650903) y [help.cricut.com 360009387274](https://help.cricut.com/hc/en-us/articles/360009387274).
- Cricut, mejores resultados con Imprimir y cortar (el diálogo del sistema puede quedar escondido): [cricut.com/blog](https://cricut.com/blog/gb/?p=206443).
- Nombres de tipo de papel en controladores Epson (modelo L355, de referencia): [manualslib.mx](https://manualslib.mx/manual/7984/Epson-L355.html?page=32). Para la L3560: **verificar** en el manual oficial.
- "Papel normal" limita la tinta en EcoTank (guía de terceros sobre la L3250, no oficial): [ferax.com.br](https://ferax.com.br/blog/impressora/guia-de-impressoras/papel-fotografico-l3250-configuracoes-cores-perfeitas/).

---

## Diagnóstico confirmado (17-oct-2026)
- Noemi imprime desde **Windows** con Design Space, y **nunca se abrió la ventana de Epson** con "Tipo de papel" y "Calidad". Se confirma la causa 1: la impresora usaba sus ajustes por omisión (papel normal, calidad estándar).
- Tiene **Canva Pro**. Su papel glossy es **tamaño carta**.
- Solución: activar "Usar diálogo del sistema" en Design Space y, además, dejar la Epson configurada por omisión en Windows (Configuración → Bluetooth y dispositivos → Impresoras y escáneres → Epson L3560 → Preferencias de impresión). Los nombres exactos de los menús: **verificar** en su equipo.
