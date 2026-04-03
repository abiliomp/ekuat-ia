> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 — Campo D011 (iTipTra)
> **Nota:** Contenido tachado (~~así~~) indica especificaciones eliminadas en v150. [MODIFICADO] indica cambios respecto a versión anterior. [NUEVO] indica adiciones en v150.

# Tipos de Transacción (D011 – iTipTra)

El campo `D011` (`iTipTra`) indica el tipo de transacción que documenta el Documento Electrónico. Pertenece al grupo D1 (Campos inherentes a la operación comercial).

**Aplicabilidad:** Obligatorio si C002 = 1 (Factura Electrónica) o C002 = 4 (Autofactura Electrónica). No se informa para otros tipos de documento.

El campo `D012` (`dDesTipTra`) contiene la descripción del tipo de transacción. [MODIFICADO] Su longitud fue ampliada a 5–36 caracteres. Debe ser obligatorio cuando existe D011.

## Tabla de códigos (iTipTra)

| Código | Descripción | Texto del campo D012 | Estado en v150 |
|--------|-------------|----------------------|----------------|
| 1 | Venta de mercadería | `"Venta de mercadería"` | Vigente |
| 2 | Prestación de servicios | `"Prestación de servicios"` | Vigente |
| 3 | Mixto (venta de mercadería y servicios) | `"Mixto"` | Vigente |
| 4 | Venta de activo fijo | `"Venta de activo fijo"` | Vigente |
| 5 | Venta de divisas | `"Venta de divisas"` | Vigente |
| 6 | Compra de divisas | `"Compra de divisas"` | Vigente |
| 7 | Promoción o entrega de muestras | `"Promoción o entrega de muestras"` | Vigente |
| 8 | Donación | `"Donación"` | Vigente |
| 9 | Anticipo | `"Anticipo"` | Vigente |
| 10 | Compra de productos | `"Compra de productos"` | Vigente |
| 11 | Compra de servicios | `"Compra de servicios"` | Vigente |
| 12 | Venta de crédito fiscal | [NUEVO] `"Venta de crédito fiscal"` | [NUEVO] |
| 13 | Muestras médicas (Art. 3 RG 24/2014) | [NUEVO] `"Muestras médicas (Art. 3 RG 24/2014)"` | [NUEVO] |

## Reglas relacionadas con D011

| Condición | Regla |
|-----------|-------|
| D011 = 9 (Anticipo) | En facturas asociadas, es obligatorio informar el número de resolución de crédito fiscal |
| [NUEVO] D011 = 12 | Obligatorio informar el número de resolución de crédito fiscal |
| D011 ≠ 12 | No informar el número de resolución de crédito fiscal |
| [NUEVO] D011 ≠ 13 (Muestras médicas) | El receptor **no puede** ser Innominado (D208 ≠ 5) cuando el total ≥ 60.000.000 Gs |

## Tipos de operación de venta de vehículos (E771 – iTipOpVN)

Este campo complementario aplica para la sección de automotores nuevos y usados:

| Código | Descripción |
|--------|-------------|
| 1 | Venta a representante |
| 2 | Venta al consumidor final |
| 3 | Venta a gobierno |
| 4 | Venta a flota de vehículos |

## Tipos de motivo de traslado (E501 – iMotEmi) — Nota de Remisión

Aplica exclusivamente cuando C002 = 7:

| Código | Descripción |
|--------|-------------|
| 1 | Traslado por venta |
| 2 | Traslado por consignación |
| 3 | Exportación |
| 4 | Traslado por compra |
| 5 | Traslado por devolución |
| 6 | Traslado entre locales de la empresa |
| 7 | Traslado de bienes por transformación |
| 8 | Traslado de bienes por reparación |
| 9 | Traslado por emisión de documentos que amparan exportaciones |
| 10 | Traslado por venta a bordo de nave o aeronave |
| 11 | Traslado por transporte de pasajeros |
| 12 | Participación en ferias |
| 13 | Traslado de encomienda |
| 14 | [NUEVO] Decomiso |
| 99 | [NUEVO] Otro (debe consignarse expresamente el motivo) |
