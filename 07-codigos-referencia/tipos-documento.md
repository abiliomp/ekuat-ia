> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 — Campo C002 (iTiDE)
> **Nota:** Contenido tachado (~~así~~) indica especificaciones eliminadas en v150. [MODIFICADO] indica cambios respecto a versión anterior. [NUEVO] indica adiciones en v150.

# Tipos de Documento Electrónico (C002 – iTiDE)

El campo `C002` (`iTiDE`) identifica el tipo de Documento Electrónico incluido en el timbrado. Es un campo numérico de 1-2 dígitos, obligatorio, ubicado dentro del grupo de **Datos del Timbrado** (C001).

El campo `C003` (`dDesTiDE`) contiene la descripción en texto del tipo de documento electrónico, cuyo valor debe corresponder exactamente al código informado en C002.

## Tabla de códigos (iTiDE)

| Código | Descripción | Texto del campo C003 | Estado en v150 | Aceptado por el XSD de producción |
|--------|-------------|----------------------|----------------|-----------------------------------|
| 1 | Factura Electrónica (FE) | `"Factura electrónica"` | [MODIFICADO] Activo | ✅ |
| 2 | Factura Electrónica de Exportación (FEE) | `"Factura electrónica de exportación"` | [MODIFICADO] Futuro | ❌ (enumeración comentada en el XSD) |
| 3 | Factura Electrónica de Importación (FEI) | `"Factura electrónica de importación"` | [MODIFICADO] Futuro | ❌ (enumeración comentada en el XSD) |
| 4 | Autofactura Electrónica (AFE) | `"Autofactura electrónica"` | Activo | ✅ |
| 5 | Nota de Crédito Electrónica (NCE) | `"Nota de crédito electrónica"` | Activo | ✅ |
| 6 | Nota de Débito Electrónica (NDE) | `"Nota de débito electrónica"` | Activo | ✅ |
| 7 | Nota de Remisión Electrónica (NRE) | `"Nota de remisión electrónica"` | [MODIFICADO] Activo | ✅ |
| 8 | Comprobante de Retención Electrónico (CRE) | `"Comprobante de retención electrónico"` | [MODIFICADO] Futuro | ❌ (enumeración comentada en el XSD) |
| 9 | Boleta de Venta Electrónica | `"Boleta de venta electrónica"` | No figura en el MT v150 | ✅ (presente en el XSD de producción) |
| 10 | Boleta Resimple Electrónica | `"Boleta resimple electrónica"` | No figura en el MT v150 | ✅ (presente en el XSD de producción) |

> **⚠️ XSD de producción (verificado en `DE_Types_v150.xsd`, junio 2026):** el tipo numérico `tiTiDE` (C002) tiene el patrón `1|[4-7]|9|10`, es decir **solo acepta 1, 4, 5, 6, 7, 9 y 10**. Los códigos 2 (FEE), 3 (FEI) y 8 (CRE) están comentados en el XSD y serían rechazados por validación de esquema. Los códigos 9 y 10 (boletas, asociadas al régimen RESIMPLE / e-kuatia'i) existen en el XSD aunque el MT v150 y sus NT no los documentan.

## Grupos de campos específicos activados por tipo de documento

| C002 | Grupo XML activo | Estado |
|------|-----------------|--------|
| 1 | E010–E099 — Factura Electrónica (FE) | Activo |
| ~~2~~ | ~~E100–E199 — Factura Electrónica de Exportación (FEE)~~ | ~~Eliminado~~ |
| ~~3~~ | ~~E200–E299 — Factura Electrónica de Importación (FEI)~~ | ~~Eliminado~~ |
| 4 | [NUEVO] E300–E399 — Autofactura Electrónica (AFE) | Activo |
| 5 o 6 | E400–E499 — Nota de Crédito/Débito Electrónica | Activo |
| 7 | [NUEVO] E500–E599 — Nota de Remisión Electrónica (NRE) | Activo |

## Reglas principales por tipo de documento

| Regla | Condición |
|-------|-----------|
| Grupo D010 (operación comercial) **obligatorio** | C002 ≠ 7 |
| Grupo D010 **no se informa** | C002 = 7 |
| Campo D011 (tipo de transacción) **obligatorio** | C002 = 1 o 4 |
| [MODIFICADO] Grupo E600 (condición de operación) **obligatorio** | C002 = 1 o 4 |
| [MODIFICADO] Grupo E600 (condición de operación) **no se informa** | C002 ≠ 1 y C002 ≠ 4 |
| Grupo E700 (ítems) **obligatorio** | C002 ≠ 7 |
| Grupo E730 (IVA) **obligatorio** | D013=1,3,4 o 5 y C002 ≠ 4 o 7 |
| [NUEVO] Campo D213 (dirección receptor) **obligatorio** | C002 = 7 o D202 = 4 |
| [NUEVO] Mensaje en KuDE (B006) **obligatorio** | C002 = 7 (Art. 3 Inc. 7, Res.) |
| [NUEVO] Condición de operación: siempre contado | C002 = 4 → E601 = 1 |
| [NUEVO] Tipo de operación: siempre B2C | C002 = 4 → D202 = 2 |
| [NUEVO] Receptor = emisor en Autofactura | C002 = 4 → D206 = D101 |

## Denominaciones de los KuDE

| C002 | Denominación del KuDE |
|------|-----------------------|
| 1 | KuDE de Factura Electrónica |
| 2 | KuDE de Factura de Exportación Electrónica |
| ~~3~~ | ~~KuDE de Factura de Importación Electrónica~~ |
| 4 | KuDE de Autofactura Electrónica |
| 5 | KuDE de Nota de Crédito Electrónica |
| 6 | KuDE de Nota de Débito Electrónica |
| 7 | KuDE de Nota de Remisión Electrónica |

## Cambios relevantes en v150

- Los grupos ~~E2 (FEE)~~ y ~~E3 (FEI)~~ fueron **eliminados** de la estructura del DE.
- El grupo E4 (AFE, E300–E399) fue incorporado como campo [NUEVO].
- El grupo E6 (NRE, E500–E599) fue incorporado como campo [NUEVO].
- La **Fecha de Fin de Vigencia** del timbrado (C009) fue **eliminada** del encabezado del KuDE.
- El CRE (código 8) sigue siendo futuro y **no es aceptado por el XSD de producción**.
- El XSD de producción acepta además los códigos **9 (Boleta de venta electrónica)** y **10 (Boleta resimple electrónica)**, no documentados en el MT v150. En el XSD de eventos (`Evento_Types_v150.xsd`), el tipo de DTE llega hasta 9 (Boleta de Venta Electrónica).
