# Inventario — producto terminado e insumos

**Responsable del conteo:** Noemi (o ayudante con su revisión) · **Conteo completo:** cada lunes antes de las 10 am · **Última actualización:** ____

Las cantidades en blanco están **por capturar**. No llenar con estimados sin marcarlos como **estimado**.

---

## 1. Cómo se usa

### Definiciones
- **Existencia:** piezas terminadas, curadas y listas para vender (no cuentan las que están curando ni las que tienen defecto).
- **Apartado:** piezas ya comprometidas con un pedido pagado o con anticipo (ML, TikTok, tienda, WhatsApp, mayoreo).
- **Disponible = Existencia − Apartado.** Es lo único que se puede ofrecer o publicar como stock.
- **Mínimo:** piezas que siempre deben estar listas para despachar sin fabricar (cubren los envíos de 24–48 h de Mercado Libre y TikTok). Si **Disponible < Mínimo**, entra al plan de producción de la semana.
- **En curado:** piezas fabricadas que aún no se pueden vender. Se anotan aparte para saber qué estará listo y cuándo.

### Reglas diarias
1. Al confirmar un pedido: sumar en **Apartado** (no restar de Existencia todavía).
2. Al enviar o entregar: restar de **Existencia** y de **Apartado**.
3. Al terminar el curado y empacar: sumar a **Existencia**.
4. El stock publicado en Mercado Libre y TikTok debe ser **≤ Disponible**. Si se vende en un canal, ajustar los demás el mismo día para no sobrevender.
5. Vela con defecto (burbuja, mecha chueca, base dispareja, pintura manchada): no entra a Existencia; se anota en la columna "Merma" y se refunde.

### Conteo semanal (lunes)
1. Contar físicamente cada SKU / color / aroma (no copiar la cifra anterior).
2. Comparar contra la cifra del archivo. Diferencia mayor a 2 piezas → anotar causa en la sección 4.
3. Contar insumos en la unidad indicada (kg, ml, piezas, hojas).
4. Calcular **punto de reorden** y marcar "PEDIR" donde Existencia ≤ Punto de reorden.
5. Hacer los pedidos a proveedores ese mismo lunes.
6. Pasar los faltantes de producto terminado a `produccion/plan-semanal.md`.

---

## 2. Producto terminado

Agregar una fila por cada combinación de color/aroma que se fabrique. Ejemplos de fila: "EV-OSO · beige · vainilla".

### 2.1 Línea Eventos — parafina (figura)

| SKU | Producto | Color | Aroma | Existencia | Apartado | Disponible | Mínimo | En curado (listo el) | Merma semana |
|---|---|---|---|---|---|---|---|---|---|
| EV-OSO | Oso de Ternura | | | | | | | | |
| EV-JIR | Jirafa Africana | | | | | | | | |
| EV-ELE | Elefante Safari | | | | | | | | |
| EV-DIN | Dino T-Rex | | | | | | | | |
| EV-ANG | Ángeles Divinos | | | | | | | | |
| EV-FLO | Flowers On (peonía) | | | | | | | | |
| EV-BUN | Bunny Happy | | | | | | | | |

### 2.2 Línea Eventos — soya (contenedor) y paquetes

| SKU | Producto | Aroma | Existencia | Apartado | Disponible | Mínimo | En curado (listo el) | Merma semana |
|---|---|---|---|---|---|---|---|---|
| EV-GLO | Glowing Glass | | | | | | | |
| EV-LMM | Lume Soja Mini | | | | | | | |
| EV-LMS | Lume Soja | | | | | | | |
| EV-PRE | Paquete Recuerdos | | | | | | | |

### 2.3 Línea Navidad — parafina

| SKU | Producto | Aroma | Existencia | Apartado | Disponible | Mínimo | En curado (listo el) | Merma semana |
|---|---|---|---|---|---|---|---|---|
| NV-VEN | Venado | | | | | | | |
| NV-NAC | Nacimiento | | | | | | | |
| NV-PIN | Pino | | | | | | | |
| NV-ARB | Árbol Navideño | | | | | | | |
| NV-BOR | Borrego (suelto) | | | | | | | |
| NV-B12 | Borregos de la Abundancia (12 pzs, armado) | | | | | | | |
| NV-ROM | Rompecabezas Navideño (juego armado) | | | | | | | |

> NV-B12 usa 12 NV-BOR. Al armar una caja: restar 12 de NV-BOR y sumar 1 a NV-B12. Igual con NV-ROM (4 piezas por juego).

**Cómo fijar el Mínimo:** Mínimo = ventas promedio por día de ese SKU × días que tardas en fabricarlo y curarlo. Al inicio (sin historial), proponer 5–10 piezas para los SKUs publicados en ML/TikTok y 0 para los que solo se hacen bajo pedido; ajustar cada mes con ventas reales.

---

## 3. Insumos

### Fórmulas

```
Consumo diario       = consumo semanal ÷ días de producción por semana
Stock de seguridad   = consumo diario × días de colchón (sugerido: 5 días en temporada normal, 7–10 en nov–dic)
Punto de reorden     = consumo diario × días de entrega del proveedor + stock de seguridad
Cantidad a pedir     = (consumo diario × días que debe cubrir el pedido) + stock de seguridad − existencia
                       redondeado hacia arriba a la presentación del proveedor (caja, galón, paquete)
```

Si **Existencia ≤ Punto de reorden → PEDIR**.

- **Consumo semanal:** al principio, calcúlalo con el plan de producción (velas planeadas × gramos o piezas por vela, de `costos/plantilla-costeo.csv`). Después de 3–4 semanas, usa el promedio real de los conteos.
- **Días de entrega:** del cuestionario (sección 9). En nov–dic suma 2–3 días porque las paqueterías se saturan (**verificar** con cada proveedor).

### Tabla de insumos

| Insumo | Unidad | Existencia | Consumo semanal | Consumo diario | Días de entrega proveedor | Stock de seguridad | Punto de reorden | ¿PEDIR? | Cantidad a pedir | Proveedor |
|---|---|---|---|---|---|---|---|---|---|---|
| Parafina | kg | | | | | | | | | |
| Cera de soya | kg | | | | | | | | | |
| Fragancia — vainilla | ml | | | | | | | | | |
| Fragancia — floral | ml | | | | | | | | | |
| Fragancia — lavanda | ml | | | | | | | | | |
| Fragancia — romero | ml | | | | | | | | | |
| Fragancia — canela | ml | | | | | | | | | |
| Fragancia — champagne | ml | | | | | | | | | |
| Fragancia — limón italiano | ml | | | | | | | | | |
| Fragancia — manzana canela | ml | | | | | | | | | |
| Fragancia — pino navideño | ml | | | | | | | | | |
| Colorante — (color) | g / ml | | | | | | | | | |
| Pintura para pintado a mano — (color) | ml | | | | | | | | | |
| Mecha — figura (medida: ____) | pzs | | | | | | | | | |
| Mecha — contenedor (medida: ____) | pzs | | | | | | | | | |
| Bases metálicas / centradores de mecha | pzs | | | | | | | | | |
| Frasco Glowing Glass + tapa dorada | pzs | | | | | | | | | |
| Lata plata (Lume Mini) | pzs | | | | | | | | | |
| Lata dorada (Lume Soja) | pzs | | | | | | | | | |
| Glicerina para jabones | kg | | | | | | | | | |
| Bolsa de celofán | pzs | | | | | | | | | |
| Bolsa de organza | pzs | | | | | | | | | |
| Listón / moño rojo | m | | | | | | | | | |
| Cajita kraft Borregos 12 | pzs | | | | | | | | | |
| Cajita kraft Rompecabezas | pzs | | | | | | | | | |
| Oraciones impresas (Borregos) | juegos | | | | | | | | | |
| Papel adhesivo / vinil para etiquetas | hojas | | | | | | | | | |
| Cartulina para tags | hojas | | | | | | | | | |
| Tinta impresora | botellas | | | | | | | | | |
| Etiquetas térmicas 4×6 (guías) | rollos | | | | | | | | | |
| Cajas de envío | pzs | | | | | | | | | |
| Relleno / papel de protección | kg o rollos | | | | | | | | | |
| Cinta de empaque | rollos | | | | | | | | | |

> Agregar una fila por cada fragancia, colorante y pintura que se use. Las fragancias se cargan normalmente al 6–10% del peso de la cera (`costos/README.md`); usa el % real de Noemi para calcular el consumo.

### Ejemplo hipotético de cálculo (números inventados)
Parafina: consumo semanal 12 kg, se produce 6 días → consumo diario 2 kg. Proveedor tarda 4 días. Colchón 5 días → stock de seguridad 10 kg. **Punto de reorden = 2 × 4 + 10 = 18 kg.** Si hay 15 kg → PEDIR. Para cubrir 14 días: 2 × 14 + 10 − 15 = 23 kg → se piden 25 kg (caja completa).

---

## 4. Registro de diferencias y merma

| Fecha | SKU / insumo | Diferencia (piezas o unidades) | Causa (defecto, error de registro, regalo, muestra, otro) | Acción |
|---|---|---|---|---|
| | | | | |

---

## 5. Control de calidad antes de sumar a Existencia

Una vela solo entra a Existencia si cumple todo:
- [ ] Sin burbujas, grietas ni hundimientos visibles.
- [ ] Mecha centrada y recta, recortada a la medida estándar (anotar la medida cuando Noemi la defina).
- [ ] Base pareja: la vela no se tambalea sobre una mesa plana.
- [ ] Pintura limpia: sin manchas fuera de la línea, sin partes despintadas, seca al tacto.
- [ ] Aroma correcto y etiqueta del aroma correcto.
- [ ] Etiqueta con advertencias de uso (no dejar encendida sin supervisión; lejos de niños, mascotas y material inflamable).
- [ ] Empaque cerrado y limpio (celofán sin huellas, frasco/lata sin cera escurrida).
