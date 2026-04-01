# Tipos de Transacción (D011 / iTipTra)

Campo `iTipTra` (D011): indica el tipo de transacción que documenta el DE. Es obligatorio solo para Factura Electrónica (C002=1) y Autofactura Electrónica (C002=4). No se informa para otros tipos de documento.

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 (campo D011)

## Tabla de tipos de transacción

| Código | Descripción (dDesTipTra) | Aplica a | Observaciones |
|--------|--------------------------|----------|---------------|
| 1 | Venta de mercadería | FE, AFE | Transacción de venta de bienes tangibles |
| 2 | Prestación de servicios | FE, AFE | Transacción de prestación de servicios |
| 3 | Mixto (Venta de mercadería y servicios) | FE, AFE | Cuando la operación incluye bienes y servicios |
| 4 | Venta de activo fijo | FE | Venta de bienes del activo fijo del emisor |
| 5 | Venta de divisas | FE | Venta de moneda extranjera |
| 6 | Compra de divisas | FE | Compra de moneda extranjera |
| 7 | Promoción o entrega de muestras | FE | Entrega sin contraprestación económica |
| 8 | Donación | FE | Transferencia gratuita de bienes o servicios |
| 9 | Anticipo | FE | Pago o entrega anticipada antes de la operación principal |
| 10 | Compra de productos | FE | Compra de bienes por parte del emisor |
| 11 | Compra de servicios | FE | Compra de servicios por parte del emisor |
| 12 | Venta de crédito fiscal | FE | Enajenación de crédito fiscal (liquidación de crédito) |
| 13 | Muestras médicas (Art. 3 RG 24/2014) | FE | Entrega de muestras médicas según norma específica. Permite el tipo de documento de identidad Innominado (D208=5) independientemente del monto. |

## Tipos de documento que requieren D011

| Tipo DE | C002 | D011 requerido |
|---------|------|----------------|
| Factura Electrónica | 1 | Sí (obligatorio) |
| Factura Electrónica de Exportación | 2 | Sí (obligatorio) |
| Factura Electrónica de Importación | 3 | Sí (obligatorio) |
| Autofactura Electrónica | 4 | Sí (obligatorio) |
| Nota de Crédito Electrónica | 5 | No |
| Nota de Débito Electrónica | 6 | No |
| Nota de Remisión Electrónica | 7 | No |

## Reglas de validación asociadas

- El código D011 solo se informa si C002 = 1 o 4 (validación 24, código 1202).
- La descripción D012 debe coincidir con el código D011 (validación 25, código 1203).
- Cuando D011 = 9 (Anticipo), el campo E719 (CDC del anticipo) es obligatorio en los ítems que apliquen.
- Cuando D011 = 13 (Muestras médicas), el tipo de documento de identidad del receptor puede ser Innominado (D208=5) sin restricción de monto.

## Motivos de emisión de NCE/NDE (E401)

Las Notas de Crédito y Débito tienen su propio campo de motivo de emisión (E401), diferente de D011:

| Código | Descripción |
|--------|-------------|
| 1 | Devolución y Ajuste de precios |
| 2 | Devolución |
| 3 | Descuento |
| 4 | Bonificación |
| 5 | Crédito incobrable |
| 6 | Recupero de costo |
| 7 | Recupero de gasto |
| 8 | Ajuste de precio |
