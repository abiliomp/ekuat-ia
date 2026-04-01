# Tipos de Documento Electrónico (C002 / iTiDE)

Campo `iTiDE` (C002): identifica el tipo de Documento Electrónico. Es parte del grupo de datos del timbrado y forma parte del CDC (Código de Control).

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 (campo C002)

## Tabla de tipos de documento

| Código | Abreviatura | Nombre completo | Descripción |
|--------|------------|-----------------|-------------|
| 1 | FE | Factura Electrónica | Documento que respalda la compra y venta de bienes y servicios en el mercado interno. Operaciones B2B, B2C y B2G. |
| 2 | FEE | Factura Electrónica de Exportación | Factura para operaciones de comercio exterior (exportaciones). Futuro en v150. |
| 3 | FEI | Factura Electrónica de Importación | Factura para operaciones de importación. Futuro en v150. |
| 4 | AFE | Autofactura Electrónica | Emitida por el comprador cuando el vendedor es un no contribuyente o extranjero. El RUC del receptor debe coincidir con el RUC del emisor. |
| 5 | NCE | Nota de Crédito Electrónica | Documento para devoluciones, descuentos, bonificaciones y ajustes de precio vinculados a una FE. |
| 6 | NDE | Nota de Débito Electrónica | Documento para recupero de costos, gastos y ajustes de precio vinculados a una FE. |
| 7 | NRE | Nota de Remisión Electrónica | Documento que ampara el traslado de mercaderías. No tiene campos de operación comercial (D010). |
| 8 | CRE | Comprobante de Retención Electrónico | Futuro en v150. |
| 11 | FCE | Factura de Contingencia Electrónica | Utilizada cuando el sistema de facturación normal no está disponible (modo contingencia). |

## Observaciones por tipo

### FE (1) — Factura Electrónica
- Requiere grupo D010 (operación comercial)
- Requiere campo D011 (tipo de transacción)
- Requiere campo D013 (tipo de impuesto)
- Requiere grupo E010 (campos específicos de FE)
- Requiere grupo E600 (condición de la operación)

### AFE (4) — Autofactura Electrónica
- Naturaleza del receptor debe ser Contribuyente (D201=1)
- El tipo de operación debe ser B2C (D202=2)
- El RUC del receptor debe ser igual al RUC del emisor
- Vendedor puede ser no contribuyente o extranjero (campo E301)

### NCE (5) y NDE (6) — Notas de Crédito/Débito
- Deben estar vinculadas a una FE existente en SIFEN (campo H001 y siguientes)
- Tienen plazo de cancelación de 168 horas desde la aprobación
- Generan evento automático de ajuste en la FE asociada

### NRE (7) — Nota de Remisión
- No debe incluir el grupo D010 (operación comercial)
- El campo B006 (información de interés del fisco) es obligatorio con el mensaje del Art. 3 Inc. 7 de la RG 41/2014
- La dirección del receptor (D213) es obligatoria

## Relación con el CDC

El tipo de documento es el cuarto componente del CDC (posiciones 11-12 de los 44 caracteres).

## Descripciones textuales (campo C003 / dDesTiDE)

| Código | Descripción textual (dDesTiDE) |
|--------|-------------------------------|
| 1 | "Factura electrónica" |
| 2 | "Factura electrónica de exportación" |
| 3 | "Factura electrónica de importación" |
| 4 | "Autofactura electrónica" |
| 5 | "Nota de crédito electrónica" |
| 6 | "Nota de débito electrónica" |
| 7 | "Nota de remisión electrónica" |
| 8 | "Comprobante de retención electrónico" |
