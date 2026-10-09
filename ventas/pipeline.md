# Pipeline de ventas B2B — mayoreo, eventos y corporativo

Responsable: `ventas-eventos-mayoreo`. Actualizar el mismo día de cada contacto. Una fila por oportunidad.

## Tabla de oportunidades

| Fecha | Prospecto | Tipo | Contacto | Canal | Etapa | Producto / cantidad | Monto estimado | Próximo paso | Fecha seguimiento | Notas |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

Guía de llenado:
- **Tipo:** Corporativo navideño · Evento (bautizo, comunión, boda, XV, baby shower, cumpleaños) · Aliado/referidor · Tienda/reventa.
- **Canal:** WhatsApp · Correo · LinkedIn · Instagram · Visita · Referido.
- **Monto estimado:** cantidad × precio de catálogo del nivel de volumen (sin envío).
- **Notas:** referido por (aliado, para comisión 10%), folio de cotización, requisitos de factura, fecha de evento.

## Etapas

| # | Etapa | Qué significa | Para avanzar |
|---|---|---|---|
| 1 | Prospecto | Identificado, sin contacto | Enviar primer mensaje |
| 2 | Contactado | Primer mensaje enviado (seguimientos día 3 y 7) | Respuesta del prospecto |
| 3 | Interesado | Respondió y pidió info, precio o muestra | Conocer cantidad, producto y fecha |
| 4 | Cotización enviada | Cotización con folio enviada (vigencia 7 días) | Fecha validada con producción |
| 5 | Negociación | Ajustes de cantidad, producto, fecha o diseño | Aceptación de la cotización |
| 6 | Diseño en aprobación | Logo recibido, prueba digital enviada | Aprobación por escrito |
| 7 | Cerrado – anticipo recibido | 50% pagado + diseño aprobado | Pasar orden a `produccion-inventario` |
| 8 | En producción | Fabricación, curado, etiquetado | Pedido terminado y revisado |
| 9 | Entregado y liquidado | Entregado y saldo 50% cobrado | Pagar comisión si fue referido; pedir reseña/recompra |
| 0 | Perdido | No compró (anotar motivo) o sin respuesta tras día 7 | Retomar en temporada siguiente |

Regla: una venta cuenta como **cerrada** solo en la etapa 7 (anticipo recibido).

## Reporte semanal (cada lunes)

| Semana | Prospectos nuevos | Contactados | Cotizaciones enviadas | Cerradas (anticipo) | Monto cerrado | Monto en cotizaciones abiertas | Tasa de cierre |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Meta del tablero (`negocio/plan-90-dias.md`): 20 cotizaciones enviadas / 5 cerradas por semana. Meta del canal mayoreo + corporativo: $15k oct · $45k nov · $70k dic · $90k ene.

## 30 tipos de negocio a prospectar

### Corporativo navideño (regalo a colaboradores y clientes)
1. Despachos contables
2. Despachos de abogados y notarías
3. Inmobiliarias y agentes de bienes raíces (regalo a clientes que compraron/rentaron)
4. Consultorios médicos y clínicas
5. Consultorios dentales y de ortodoncia
6. Clínicas veterinarias
7. Escuelas y colegios privados (regalo a maestros y personal)
8. Guarderías y estancias infantiles
9. Gimnasios y estudios de yoga, pilates o barre
10. Agencias de marketing y publicidad
11. Agencias de seguros y asesores financieros
12. Concesionarias de autos
13. Hoteles y hostales boutique (amenidad o regalo a huéspedes)
14. Restaurantes y cafeterías (regalo a clientes frecuentes)
15. Spas, salones de belleza y barberías
16. Empresas de tecnología y startups (RH)
17. Constructoras y despachos de arquitectura
18. Bancos y cajas de ahorro locales (sucursales)
19. Laboratorios clínicos y farmacias independientes
20. Cámaras empresariales y asociaciones (canastas o regalo a socios)

### Eventos (aliados y referidores)
21. Planeadoras y wedding planners
22. Salones y jardines de eventos
23. Mesas de dulces y postres
24. Fotógrafos y videógrafos de eventos
25. Tiendas de fiesta y artículos para recuerdos
26. Parroquias y catequesis (primera comunión)
27. Grupos de mamás (Facebook, WhatsApp, escuelas)
28. Florerías y decoradoras de eventos
29. Tiendas de vestidos de XV, novia y ropa de bautizo
30. Pastelerías y reposterías de eventos

> Capacidad: no confirmar fecha de ningún pedido sin validar con `produccion-inventario`. Mientras no exista el cuadro de moldes en `negocio/catalogo.md`, el tope por pedido y por semana está **a confirmar con producción**.
