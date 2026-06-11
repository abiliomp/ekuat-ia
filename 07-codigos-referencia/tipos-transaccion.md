> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 — Campo D011 (iTipTra)
> **Nota:** Contenido tachado (~~así~~) indica especificaciones eliminadas en v150. [MODIFICADO] indica cambios respecto a versión anterior. [NUEVO] indica adiciones en v150.

# Tipos de Transacción (D011 – iTipTra)

El campo `D011` (`iTipTra`) indica el tipo de transacción que documenta el Documento Electrónico. Pertenece al grupo D1 (Campos inherentes a la operación comercial).

**Aplicabilidad:** Obligatorio si C002 = 1 (Factura Electrónica) o C002 = 4 (Autofactura Electrónica). No se informa para otros tipos de documento.

El campo `D012` (`dDesTipTra`) contiene la descripción del tipo de transacción. [MODIFICADO] Su longitud fue ampliada a 5–36 caracteres. Debe ser obligatorio cuando existe D011.

## Tabla de códigos (iTipTra)

| Código | Descripción | Texto exacto del campo D012 (XSD `tdDesTiTran`) | Estado en v150 |
|--------|-------------|--------------------------------------------------|----------------|
| 1 | Venta de mercadería | `Venta de mercadería` | Vigente |
| 2 | Prestación de servicios | `Prestación de servicios` | Vigente |
| 3 | Mixto (venta de mercadería y servicios) | `Mixto (Venta de mercadería y servicios)` | Vigente |
| 4 | Venta de activo fijo | `Venta de activo fijo` | Vigente |
| 5 | Venta de divisas | `Venta de divisas` | Vigente |
| 6 | Compra de divisas | `Compra de divisas` | Vigente |
| 7 | Promoción o entrega de muestras | `Promoción o entrega de muestras` | Vigente |
| 8 | Donación | `Donación` | Vigente |
| 9 | Anticipo | `Anticipo` | Vigente |
| 10 | Compra de productos | `Compra de productos` | Vigente |
| 11 | Compra de servicios | `Compra de servicios` | Vigente |
| 12 | Venta de crédito fiscal | [NUEVO] `Venta de crédito fiscal` | [NUEVO] |
| 13 | Muestras médicas (Art. 3 RG 24/2014) | [NUEVO] `Muestras médicas (Art. 3 RG 24/2014)` | [NUEVO] |

> **⚠️ Literal exacto del código 3 (XSD de producción):** `Mixto (Venta de mercadería y servicios)` — el texto completo con paréntesis y "Venta" en mayúscula, **no** solo "Mixto". `tdDesTiTran` es una enumeración cerrada en `DE_Types_v150.xsd`.

## Reglas relacionadas con D011

| Condición | Regla |
|-----------|-------|
| D011 = 9 (Anticipo) | En facturas asociadas, es obligatorio informar el número de resolución de crédito fiscal |
| [NUEVO] D011 = 12 | Obligatorio informar el número de resolución de crédito fiscal |
| D011 ≠ 12 | No informar el número de resolución de crédito fiscal |
| [NT-024] Umbral de identificación del receptor | El receptor **no puede** ser Innominado (D208 ≠ 5) cuando el total general ≥ **7.000.000 Gs** (desde 01/01/2025; antes: 35.000.000 Gs por NT-021 y 60.000.000 Gs en el MT original con excepción de muestras médicas D011=13) |

## Tipos de operación de venta de vehículos (E771 – iTipOpVN)

Este campo complementario aplica para la sección de automotores nuevos y usados:

| Código | Texto exacto de E772 (XSD `tdDesTipOpVN`) |
|--------|-------------------------------------------|
| 1 | `Venta a representante` |
| 2 | `Venta al Consumidor final` |
| 3 | `Venta a gobierno` |
| 4 | `Venta a flota de vehículos` |

> **⚠️ Literal exacto del código 2:** `Venta al Consumidor final` — con "Consumidor" en mayúscula, según el XSD de producción.

## Tipos de motivo de traslado (E501 – iMotEmi) — Nota de Remisión

Aplica exclusivamente cuando C002 = 7. El tipo numérico del XSD (`tiMotivTras`) acepta 1–14 y 99; la descripción E502 (`tdDMotivTras`) es una unión: enumeración cerrada + texto libre de 5–60 caracteres (para 99=Otro).

| Código | Texto exacto de E502 (XSD `tdDMotivTras`) |
|--------|-------------------------------------------|
| 1 | `Traslado por ventas` |
| 2 | `Traslado por consignación` |
| 3 | `Exportación` |
| 4 | `Traslado por compra` |
| 5 | `Importación` |
| 6 | `Traslado por devolución` |
| 7 | `Traslado entre locales de la empresa` |
| 8 | `Traslado de bienes por transformación` |
| 9 | `Traslado de bienes para reparación` |
| 10 | `Traslado por emisor móvil` |
| 11 | `Exhibición o Demostración` |
| 12 | `Participación en ferias` |
| 13 | `Traslado de encomienda` |
| 14 | [NUEVO] `Decomiso` |
| 99 | [NUEVO] Otro (texto libre: debe consignarse expresamente el motivo en E502) |

> **Corrección (junio 2026):** una versión anterior de esta tabla omitía el código 5 (`Importación`) y 10–11 (`Traslado por emisor móvil`, `Exhibición o Demostración`), e incluía motivos inexistentes ("emisión de documentos que amparan exportaciones", "venta a bordo de nave o aeronave", "transporte de pasajeros"). La lista actual fue verificada contra la enumeración `tdDMotivTras` del XSD de producción. Nótese además: código 1 es "Traslado por venta**s**" (plural) y código 9 es "para reparación" (no "por reparación").
