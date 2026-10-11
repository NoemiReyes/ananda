# Fórmulas de Ananda Velas

| Campo | Valor |
|---|---|
| Responsable técnico | Maestro cerero (agente) · aprueba: Noemi |
| Edita esta carpeta | Chat Producción y costos |
| Versión / fecha | v1 · 11-oct-2026 |
| Meta de calidad | Nivel de vela premium de tienda departamental: aroma fuerte en frío y en caliente, alberca de cera pareja, presentación impecable. **Es una meta interna:** en publicaciones, etiquetas o anuncios nunca se menciona otra marca ni "aroma tipo [marca]". Se describen las notas del aroma ("manzana, canela y vainilla") |

## Archivos

| Archivo | Para qué |
|---|---|
| `README.md` (este) | Diagnóstico, plan para subir el aroma, 10 preguntas para Noemi, lista de compra técnica |
| `punto-de-partida-soya.md` | Fórmula de partida para soya en contenedor (a validar), gramos por contenedor y mecha por diámetro |
| `pruebas-quemado.md` | Cómo probar, qué anotar y cuándo se aprueba |
| `defectos.md` | Síntoma → causa → corrección (soya en contenedor y parafina en figura) |
| `<SKU>.md` (pendiente) | Ficha aprobada por SKU, cuando pase la prueba de quemado |

---

## 1. Diagnóstico: qué sabemos y qué falta (11-oct-2026)

**Lo que sabemos**
- Dos líneas: **parafina en figura** (13 moldes) y **soya en contenedor** (3 contenedores: lata 2.3 × 6 cm, lata 4.6 × 6 cm, frasco 5.8 × 6.7 cm). Viene una **veladora en vaso** para Día de Muertos (vaso aún sin definir).
- 38 aromas en lista. En soya se ofrecen 6 (floral, vainilla, romero, lavanda, champagne, limón italiano).
- El costeo **supone** 8 % de fragancia y gramos de cera **estimados**, no medidos (`costos/plantilla-costeo.csv`).
- En las referencias de compra aparecen "esencias concentradas para veladora" de 30–60 ml y "pabilo pre-encerado 15 cm" genérico (`costos/insumos-referencia.md`). **No sabemos si es lo que usa Noemi.** Si lo es, son las dos primeras sospechosas del aroma débil.
- La soya del catálogo **no lleva colorante** (bien: menos variables para la mecha).

**Lo que falta (todo el cuestionario de fabricación está sin contestar)**
- Qué cera de soya y qué parafina exactas (marca, código, ficha técnica).
- Qué fragancia, de qué proveedor, si es aceite para vela, su hoja de seguridad (punto de inflamación) y certificado IFRA.
- % real de fragancia y cómo se mide (báscula o a ojo).
- Temperaturas de fundido, adición de fragancia y vertido.
- Mecha por producto (serie y número).
- Días de curado.
- Si alguna vez se han quemado velas completas y qué pasa (túnel, humo, aroma en caliente).
- Medidas internas reales de los contenedores y del vaso de veladora.

**Conclusión:** hoy no hay fórmula escrita, así que cada tanda puede salir distinta. Lo primero es **medir y anotar** (Fase 0 de `pruebas-quemado.md`) y contestar las 10 preguntas de abajo. Después se prueba una cosa a la vez.

---

## 2. Las 10 preguntas para Noemi (contestar por nota de voz, ~15 min)

Di el número antes de contestar. Si no sabes, di "no sé" o "más o menos": también sirve.

1. **Ceras:** ¿qué cera de soya y qué parafina usas exactamente? Marca, nombre o código, proveedor y si la soya dice "para contenedor" o "para pilar". Toma foto de la bolsa o etiqueta.
2. **Fragancia y proveedor:** ¿dónde compras las fragancias y cómo se llaman en la etiqueta? ¿Son aceites para vela, "esencia para veladora", esencias para aromatizante o aceites esenciales? ¿Te dieron hoja de seguridad o certificado IFRA? Foto de un frasco.
3. **Cantidad de fragancia:** ¿cuánta pones por tanda o por vela y cómo la mides (báscula en gramos, ml, gotas, a ojo)? ¿Es igual en soya y parafina y en todos los aromas?
4. **Temperaturas:** ¿a cuántos grados derrites, a cuántos agregas la fragancia, cuánto tiempo revuelves y a cuántos viertes? ¿Con qué termómetro? (Por separado para soya y parafina.)
5. **Mechas:** ¿qué mecha usas en cada contenedor y en las figuras? Marca, serie y número, o cómo la pides ("pabilo encerado de 15 cm"). Foto del paquete.
6. **Contenedores:** ¿cuánto mide **por dentro** cada lata y el frasco, hasta dónde los llenas y cuánto pesa una vela terminada de cada uno (pesa 3)? ¿Qué vaso usarás para la veladora (medidas, proveedor, si dice que aguanta calor)?
7. **Curado:** ¿cuántos días dejas reposar la soya y la parafina antes de vender o empacar? ¿Tapadas o destapadas, y dónde?
8. **Quemado:** ¿has prendido alguna de tus velas de soya hasta el final? ¿La cera derretida llega al borde en el primer encendido, hace túnel, humo, flama alta? ¿Cómo huele prendida? ¿Qué aroma huele más y cuál menos?
9. **Enfriado y apariencia:** ¿calientas el contenedor antes de verter? ¿Dónde se enfrían y qué tan frío o caliente está el cuarto? ¿Te salen manchas blancas, partes despegadas del vidrio, hundimientos o gotas de aceite arriba?
10. **Veladora de Día de Muertos:** ¿parafina o soya, vaso alto o corto? ¿Ya hiciste alguna y la quemaste completa? ¿Qué aroma quieres de base (nardo, canela, vainilla, manzana canela)?

> Con estas 10 respuestas se escribe la versión 1 de la fórmula de soya y se arma la compra de prueba. El resto del cuestionario (`procesos/cuestionario-fabricacion.md`) se puede contestar después para los SOP.

---

## 3. Plan para subir la calidad del aroma (en orden de impacto)

El aroma que "llena el cuarto" depende de 5 cosas, en este orden. **Cada cambio se prueba con 2–3 velas antes de pasarlo a producción** (`pruebas-quemado.md`) y se empieza por los best sellers.

| # | Qué cambiar | Por qué es lo primero | Cómo se prueba | Costo / tiempo |
|---|---|---|---|---|
| **1** | **Fragancia: aceite para vela de proveedor confiable**, comprado por kg, con hoja de seguridad (punto de inflamación) y certificado IFRA | Es lo que más mueve el aroma en frío y en caliente. Una "esencia" que no está hecha para vela huele poco prendida, puede sudar y hacer humo. Los aceites esenciales puros casi no se sienten en caliente | Misma cera, misma mecha, mismo %: vela con fragancia actual vs. vela con fragancia nueva. Calificar en frío y en caliente | Por kg baja el costo por gramo ~60 % vs. frascos de 60 ml (`costos/insumos-referencia.md`, estimado). Pedir **muestras** de 2–3 proveedores en los 3 aromas más vendidos. Precio: `costos-precios` |
| **2** | **% exacto, pesado en gramos**, agregado a la temperatura de la ficha y mezclado 2 min | Poco % = poco aroma; demasiado % = suda y no huele más. "A ojo" cambia en cada tanda | Matriz Fase 2 (8 % vs. 10 %, solo si la ficha lo permite) | Báscula de 0.1–1 g (si no hay). Sin costo de tiempo extra |
| **3** | **Mecha bien medida** para cada contenedor | El aroma en caliente sale de la cera **derretida**: si la alberca no llega al borde en 3–4 h, la vela huele a la mitad y hace túnel | Matriz Fase 1 (3 mechas por contenedor) | Mechas de serie: costo por pieza parecido al pabilo actual (**verificar**) |
| **4** | **Curado completo**: soya 1–2 semanas, tapada | La soya libera mucho más aroma en caliente con curado. Vender a los 2 días es la causa más común de "no huele prendida" | Misma tanda: calificar a los 2, 7 y 14 días | Sin costo, pero **requiere inventario adelantado**: avisar a `produccion-inventario` (afecta el plan de Navidad) |
| **5** | **Cera de soya para contenedor de buena carga** (con ficha técnica) | Una cera de pilar o sin especificación aguanta menos fragancia y se despega del vidrio | Solo si 1–4 no alcanzan la meta, o si hoy se usa soya de pilar | Puede subir el costo por kg: consultar a `costos-precios` antes de cambiar todo el catálogo |

**Para figuras de parafina:** se aplica 1, 2 y 4 (la mecha se revisa por figura). En figura el aroma que más se nota es el **en frío**, porque casi siempre se usan de decoración o recuerdo.

**Lo que NO se hace:** subir la fragancia arriba del máximo de la ficha, mezclar aditivos "a ojo" o cambiar varias cosas al mismo tiempo (no se sabe cuál funcionó).

### Orden de trabajo de esta semana
| Día | Qué | Quién |
|---|---|---|
| Lun 12-oct | Contestar las 10 preguntas. Fase 0: prender 1 vela actual de cada contenedor y registrar 4 h. Medir contenedores con el método del agua | Noemi contesta; Angélica mide y registra |
| Lun 12–mar 13 | Pedir muestras de fragancia (3 aromas) y mechas de serie (3 tamaños por contenedor). Pedir la ficha técnica de la cera actual al proveedor | Noemi (compra), precios a `costos-precios` |
| Mar 13–mié 14 | Verter Fase 1 con lo que haya (práctica de Angélica, supervisada) | Angélica con Noemi |
| Mié 14–vie 16 | Prueba de mecha (48 h de curado) | Angélica registra, Noemi revisa |
| Lun 19-oct | Aroma con 7 días de curado; elegir mecha; verter Fase 2 | Ambas |

---

## 4. Lista de compra técnica (para pruebas; precios los pasa `costos-precios`)

| Qué | Para qué | Cantidad de prueba | Pedir al proveedor |
|---|---|---|---|
| Ficha técnica de la **cera de soya actual** | Saber la carga máxima, temperaturas y curado | — | Ficha técnica (TDS) |
| Cera de soya **para contenedor** con ficha (si la actual es de pilar o no tiene ficha). Tipos a cotizar: GW 464 o NatureWax C-3, o la equivalente que tenga el proveedor mexicano | Fase 5 del plan | 2–5 kg | Ficha técnica, disponibilidad continua, precio por caja de 20–25 kg |
| **Aceite de fragancia para vela**, muestras de 2–3 proveedores (Bell Flavors, Century Labs, Novaroma, Petrowax u otros de `costos/insumos-referencia.md`) en vainilla, el aroma más vendido de eventos y uno navideño (manzana canela) | Paso 1 del plan | 100–250 g por aroma | **Hoja de seguridad con punto de inflamación**, certificado IFRA, % máximo recomendado en soya y en parafina |
| **Mechas de serie para soya con base metálica** (ECO, CD, HTP o LX; la que se consiga en México, **verificar disponibilidad**) | Matriz Fase 1 | 3 tamaños por contenedor (tabla en `punto-de-partida-soya.md`), 10–20 pzs de cada uno | Tabla de tamaños por diámetro del fabricante |
| Stickers de mecha y centradores | Mecha recta y centrada | 1 paquete | — |
| Báscula de 0.1 g (si no hay) | Pesar fragancia y colorante exactos | 1 | — |
| Termómetro digital de punta (si no hay) | Temperaturas exactas | 1 | — |
| Apagavelas, regla metálica, vernier | Prueba de quemado | 1 | — |
| Vasos para veladora **aptos para calor** (24 pzs, tarea DM-b) | Veladora Día de Muertos | 24 | Confirmación por escrito de que es apto para veladora; diámetro interior y alto |

---

## 5. Seguridad y normas (aplica a todo)

- **Nunca** exceder la carga máxima de fragancia de la ficha de la cera.
- Agregar la fragancia fuera del fuego y **respetar su punto de inflamación** (hoja de seguridad).
- Solo fragancias con **hoja de seguridad y certificado IFRA**.
- Toda vela lleva advertencias: no dejar encendida sin supervisión; lejos de niños, mascotas y material inflamable (en veladoras de ofrenda: **papel picado y flores secas**); superficie resistente al calor; recortar mecha a ~5 mm; no encender más de 4 h seguidas. Texto completo en `diseno/sistema-etiquetas.md`.
- Normas de referencia, **verificar con el texto oficial antes de citarlas en una etiqueta o venta**:
  - ASTM F2417, especificación de seguridad contra incendio para velas (versión vigente F2417-26): [ASTM](https://store.astm.org/f2417-26.html), [resumen de cambios SGS](https://www.sgs.com/en-gr/news/2026/07/safeguards-09626-astm-updates-candle-fire-safety-standard). **Verificar.**
  - ASTM F2058, etiquetado de seguridad contra incendio para velas (F2058-07, reaprobada 2021): [ASTM](https://store.astm.org/f2058-07r21.html). **Verificar.**
  - NOM-050-SCFI (información comercial de productos en México): **verificar** el texto vigente en el DOF antes de diseñar la etiqueta comercial final.

## 6. Aviso a otros agentes
- `costos-precios`: precios de la lista de compra; si se aprueba 10 % de fragancia o cambia la cera, recalcular.
- `produccion-inventario`: el curado de 1–2 semanas en soya obliga a fabricar con anticipación.
- `documentador-procesos`: cuando una fórmula se apruebe, pasa al SOP-004 (soya) o SOP-003 (parafina). Mientras, el protocolo de `pruebas-quemado.md` puede usarse para capacitar a Angélica.
