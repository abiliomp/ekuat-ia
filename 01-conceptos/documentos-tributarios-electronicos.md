> **Fuente:** Manual Técnico SIFEN v150, sección 5 y campo C002 (sección 10.4)

> **Nota:** Este documento refleja el MT v150 con cambios del historial de versiones marcados.

# Documentos Tributarios Electrónicos (DTE)

Descripción de los tipos de documentos electrónicos previstos por SIFEN y sus códigos de identificación.

---

## 1. Definición

Un **Documento Tributario Electrónico (DTE)** es el Documento Electrónico (DE) que ha sido:
1. Generado y firmado digitalmente por un facturador electrónico autorizado.
2. Transmitido al SIFEN.
3. Validado formalmente por la Administración Tributaria (SET).
4. Aprobado con efectos tributarios.

Adquiere la misma validez jurídica, fuerza probatoria e incidencia tributaria que los comprobantes físicos o convencionales autorizados por la SET (Art. 33, Ley N° 4.868/2013).

---

## 2. Tipos de Documentos Previstos

El campo **C002 (iTiDE)** identifica el tipo de documento electrónico en el XML. Los valores válidos son:

| Código C002 | Tipo | Estado | Descripción |
|-------------|------|--------|-------------|
| 1 | **Factura Electrónica (FE)** | Activo | Comprobante de venta de bienes y/o servicios. |
| 2 | **[MODIFICADO] Factura Electrónica de Exportación (FEE)** | Futuro | ~~Comprobante de exportaciones.~~ Actualmente desactivado — a futuro. |
| 3 | **[MODIFICADO] Factura Electrónica de Importación (FEI)** | Futuro | ~~Comprobante de importaciones.~~ Actualmente desactivado — a futuro. |
| 4 | **[MODIFICADO] Autofactura Electrónica (AFE)** | Activo | Comprobante emitido por el comprador cuando el vendedor no puede emitir factura. |
| 5 | **Nota de Crédito Electrónica (NCE)** | Activo | Documento complementario que reduce el valor de una FE emitida. |
| 6 | **Nota de Débito Electrónica (NDE)** | Activo | Documento complementario que incrementa el valor de una FE emitida. |
| 7 | **[MODIFICADO] Nota de Remisión Electrónica (NRE)** | Activo | Documento que ampara el traslado físico de mercaderías. |
| 8 | **[MODIFICADO] Comprobante de Retención Electrónico** | Futuro | Comprobante de retención de impuestos. A futuro. |

> **[MODIFICADO]** Los tipos 2, 3 y 8 están marcados como **Futuro** en el MT v150. Su implementación está pendiente de definición técnica y normativa.

---

## 3. Documentos Activos en esta Versión

Conforme al capítulo 5 del MT v150, los documentos tributarios electrónicos **activos** en la presente versión son:

### 3.1 Comprobantes de Ventas Electrónicos

#### Factura Electrónica (FE) — C002 = 1
- Respalda la compra y venta de bienes y/o servicios.
- Tipos de transacción aplicables (D011): venta de mercadería, prestación de servicios, mixto, venta de activo fijo, venta/compra de divisas, donación, anticipo, compra de productos/servicios, **[NUEVO en v150]** venta de crédito fiscal, **[NUEVO en v150]** muestras médicas.
- Requiere datos completos del receptor.

#### Autofactura Electrónica (AFE) — C002 = 4 **[NUEVO en v150]**
- Emitida por el **comprador** cuando el vendedor no puede emitir factura (ej.: compras a personas físicas no contribuyentes).
- **[MODIFICADO]** Campos específicos en el grupo E4 (E300–E399).

### 3.2 Documentos Complementarios Electrónicos

#### Nota de Crédito Electrónica (NCE) — C002 = 5
- Reduce el valor de una o más facturas electrónicas ya aprobadas.
- Debe referenciar el DTE original en el grupo H (Documentos Asociados).
- Campos específicos en el grupo E5 (E400–E499).

#### Nota de Débito Electrónica (NDE) — C002 = 6
- Incrementa el valor de una o más facturas electrónicas ya aprobadas.
- Debe referenciar el DTE original en el grupo H (Documentos Asociados).
- Campos específicos en el grupo E5 (E400–E499).

### 3.3 Nota de Remisión Electrónica

#### Nota de Remisión Electrónica (NRE) — C002 = 7
- **[MODIFICADO]** Respalda el traslado físico de mercaderías entre locales del emisor o hacia el receptor comprador.
- No requiere datos de operación comercial (D010 no se informa si C002 = 7).
- **[NUEVO en v150]** Cuando C002 = 7, es **obligatorio** informar el mensaje del Art. 3 Inc. 7 de la Resolución General N° 41/2014 en el campo B006 (dInfoFisc), que debe imprimirse en el KuDE.
- Campos específicos en el grupo E6 (E500–E599).
- Campos de transporte en el grupo E10 (E900–E999).

---

## 4. Documentos Eliminados o No Implementados

### Factura Electrónica de Exportación (FEE) — C002 = 2
~~Comprobante de ventas de exportación.~~
> ⚠️ **ELIMINADO / FUTURO:** Este tipo de documento fue removido de la implementación activa en la versión actual del MT. Los grupos de campos E2 (E100–E199) asociados a este tipo fueron eliminados.

### Factura Electrónica de Importación (FEI) — C002 = 3
~~Comprobante de importaciones.~~
> ⚠️ **ELIMINADO / FUTURO:** Este tipo de documento fue removido de la implementación activa en la versión actual del MT. Los grupos de campos E3 (E200–E299) asociados a este tipo fueron eliminados.

> **Nota del MT v150:** No se respetó el esquema de control de versiones a color en la eliminación de contenido relacionado a ISC, y a los tipos de documentos: Factura electrónica de exportación, Factura electrónica de importación y Comprobante de retenciones electrónico.

---

## 5. Denominación de los KuDE por Tipo de Documento

Cada tipo de documento electrónico tiene una denominación específica para su representación gráfica (KuDE):

| Tipo DE | Denominación KuDE |
|---------|-------------------|
| FE (C002=1) | KuDE de Factura Electrónica |
| ~~FEE (C002=2)~~ | ~~KuDE de Factura de Exportación Electrónica~~ |
| ~~FEI (C002=3)~~ | ~~KuDE de Factura de Importación Electrónica~~ |
| AFE (C002=4) | KuDE de Autofactura Electrónica |
| NDE (C002=6) | KuDE de Nota de Débito Electrónica |
| NCE (C002=5) | KuDE de Nota de Crédito Electrónica |
| NRE (C002=7) | KuDE de Nota de Remisión Electrónica |

---

## 6. Gradualidad e Implementación Futura

Conforme al Decreto N° 7.795/2017 y sus reglamentaciones, la AT puede implementar de manera gradual la utilización de otros DE que, por su naturaleza, requieran un tratamiento similar de operación electrónica. Estos se introducirán en versiones posteriores del MT.
