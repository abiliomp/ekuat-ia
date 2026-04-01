# Documentos Tributarios Electrónicos (DTE)

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4, campo C002

## Definiciones Fundamentales

- **DE (Documento Electrónico):** Documento emitido y firmado digitalmente por el emisor, que aún no ha sido aprobado por la Administración Tributaria y no ha ingresado al SIFEN.
- **DTE (Documento Tributario Electrónico):** Documento electrónico con aprobación de uso por parte de la Administración Tributaria, ingresado al SIFEN.

---

## Tipos de Documentos Electrónicos (Campo C002)

| Código | Sigla | Nombre | Estado |
|--------|-------|--------|--------|
| 1 | FE | Factura Electrónica | Vigente |
| 2 | FEE | Factura Electrónica de Exportación | Futuro |
| 3 | LCE | Liquidación de Crédito Electrónica | Futuro |
| 4 | AFE | Autofactura Electrónica | Vigente |
| 5 | NCE | Nota de Crédito Electrónica | Vigente |
| 6 | NDE | Nota de Débito Electrónica | Vigente |
| 7 | NRE | Nota de Remisión Electrónica | Vigente |
| 8 | CRE | Comprobante de Retención Electrónico | Futuro |
| 11 | FCE | Factura de Contingencia Electrónica | Contingencia |

---

## Descripción de Cada Tipo

### 1. Factura Electrónica (FE) — Código 1

**Descripción:** Documento que respalda la compra y venta de bienes y servicios entre contribuyentes o hacia consumidores finales.

**Campo XML:** `gCamFE` (E010-E099)
**Indicador de presencia:** E011 (presencial, electrónica, telemarketing, domicilio, bancaria, cíclica)
**Condición de operación:** Contado (E601=1) o Crédito (E601=2)
**Compras públicas:** E020-E029 cuando D202=3 (B2G)

**Tipos de transacción (D011) permitidos:**
- 1 = Venta de mercadería
- 2 = Prestación de servicios
- 3 = Mixto
- 4 = Venta de activo fijo
- 5 = Venta de divisas
- 6 = Compra de divisas
- 7 = Promoción o entrega de muestras
- 8 = Donación
- 9 = Anticipo
- 10 = Compra de productos
- 11 = Compra de servicios
- 12 = Venta de crédito fiscal
- 13 = Muestras médicas (Art. 3 RG 24/2014)

**Eventos disponibles:**
- Cancelación (hasta 48 hs desde aprobación)
- Vinculación automática de NCE/NDE
- Vinculación automática de NRE
- Nominación (NT-014)

---

### 2. Factura Electrónica de Exportación (FEE) — Código 2

**Estado:** Futuro (en desarrollo)
**Campo XML:** `gCamFEE` (E100-E199)

**Observación:** Hasta tanto se defina el documento FEE con timbrado propio, las operaciones de exportación se registran en la Factura Electrónica (C002=1) usando el campo B006 (dInfoFisc) para informar los datos requeridos por el Art. 20 numeral 15 del Decreto N° 10797/2013 (NT-007).

---

### 3. Liquidación de Crédito Electrónica (LCE) — Código 3

**Estado:** Futuro
**Campo XML:** Grupo específico por definir

---

### 4. Autofactura Electrónica (AFE) — Código 4

**Descripción:** Documento emitido por el comprador/adquiriente cuando realiza operaciones con no contribuyentes o extranjeros que no emiten facturas.

**Campo XML:** `gCamAE` (E300-E399)
**Moneda:** Obligatoriamente PYG (D015=PYG, según NT-012)
**Vendedor:** No contribuyente (E301=1) o Extranjero (E301=2)

**Datos del vendedor requeridos:**
- Tipo de documento de identidad (E304)
- Número de documento (E306)
- Nombre y apellido (E307)
- Dirección (E308)
- Ciudad/Departamento (E309-E315)
- Lugar de la transacción (E316-E322)

**Condición de operación:** Contado (E601=1) o Crédito (E601=2)

**Eventos disponibles:**
- Cancelación (hasta 168 hs desde aprobación)

---

### 5. Nota de Crédito Electrónica (NCE) — Código 5

**Descripción:** Documento emitido para ajustar, disminuir o anular el valor de una Factura Electrónica previamente aprobada.

**Campo XML:** `gCamNCDE` (E400-E499)
**Requisito:** Debe estar vinculada a una FE aprobada en el SIFEN (campo H001-H049, documento asociado).

**Motivos de emisión (E401):**
- 1 = Devolución y Ajuste de precios
- 2 = Devolución
- 3 = Descuento
- 4 = Bonificación
- 5 = Crédito incobrable
- 6 = Recupero de costo
- 7 = Recupero de gasto
- 8 = Ajuste de precio

**Efecto en SIFEN:**
- Genera automáticamente un evento de "Devolución y Ajuste de precios" sobre la FE referenciada.
- El receptor de la FE asociada no tendrá derecho al crédito del IVA en forma total o parcial.

**Eventos disponibles:**
- Cancelación (hasta 168 hs desde aprobación)

---

### 6. Nota de Débito Electrónica (NDE) — Código 6

**Descripción:** Documento emitido para ajustar, aumentar o corregir el valor de una Factura Electrónica previamente aprobada.

**Campo XML:** `gCamNCDE` (E400-E499) — mismo grupo que NCE
**Requisito:** Debe estar vinculada a una FE aprobada en el SIFEN.

**Motivos de emisión (E401):** Mismos que NCE (códigos 1-8).

**Efecto en SIFEN:**
- Genera automáticamente un evento de "Devolución y Ajuste de precios" sobre la FE referenciada.

**Eventos disponibles:**
- Cancelación (hasta 168 hs desde aprobación)

---

### 7. Nota de Remisión Electrónica (NRE) — Código 7

**Descripción:** Documento que ampara el traslado de mercaderías. No tiene condición de operación (no lleva IVA).

**Campo XML:** `gCamNRE` (E500-E599)
**Particularidad:** No requiere grupo gOpeCom (D010). El campo dInfoFisc (B006) es obligatorio según Art. 3 Inc. 7 de la RG N° 41/2014.

**Motivos de emisión (E501):**
- 1 = Traslado por venta
- 2 = Traslado por consignación
- 3 = Exportación
- 4 = Traslado por compra
- 5 = Importación
- 6 = Traslado por devolución
- 7 = Traslado entre locales de la empresa
- 8 = Traslado de bienes por transformación
- 9 = Traslado de bienes por reparación
- 10 = Traslado por emisor móvil
- 11 = Exhibición o demostración
- 12 = Participación en ferias
- 13 = Traslado de encomienda
- 14 = Decomiso
- 99 = Otro

**Responsable de la emisión (E503):**
- 1 = Emisor de la factura
- 2 = Poseedor de la factura y bienes
- 3 = Empresa transportista
- 4 = Despachante de Aduanas
- 5 = Agente de transporte o intermediario

**Campos de transporte requeridos:**
- Grupo E900-E999 (transporte): local de salida, local de entrega, vehículo, transportista.

**Eventos disponibles:**
- Cancelación (hasta 168 hs desde aprobación)
- Vinculación automática a FE
- Actualización de datos del transporte (GET)

---

### 8. Comprobante de Retención Electrónico (CRE) — Código 8

**Estado:** Futuro

---

### 11. Factura de Contingencia Electrónica (FCE) — Código 11

**Descripción:** Documento emitido en modo contingencia cuando no hay conectividad con el SIFEN.
**Estado:** Contingencia (pendiente de implementación completa)

---

## Campos Comunes a Todos los Tipos

Independientemente del tipo de documento, todos los DE incluyen:

| Grupo | Campos | Descripción |
|-------|--------|-------------|
| AA | AA001-AA002 | Identificación del formato XML |
| A | A001-A005 | Campos firmados (CDC, fecha firma, sistema) |
| B | B001-B006 | Operación DE (tipo emisión, código seguridad, info) |
| C | C001-C010 | Datos del timbrado |
| D | D001-D299 | Datos generales, emisor y receptor |
| F | F001-F099 | Subtotales y totales |
| G | G001-G099 | Campos complementarios comerciales |
| H | H001-H049 | Documento asociado |
| I | I001-I049 | Firma digital del DTE |
| J | J001-J049 | Campos fuera de la firma (QR, info adicional) |
