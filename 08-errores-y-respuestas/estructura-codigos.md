> **Fuente:** Manual Técnico SIFEN v150, sección 12.1
> **Nota:** Contenido tachado (~~así~~) indica especificaciones eliminadas en v150. [MODIFICADO] indica cambios. [NUEVO] indica adiciones en v150.

# Estructura de los Códigos de Validación

El SIFEN realiza validaciones en múltiples niveles: desde la conexión TLS hasta el contenido de cada campo del Documento Electrónico. Cada validación produce un resultado identificado por un código numérico de **4 dígitos**.

## Estados de validación

| Código | Descripción |
|--------|-------------|
| A | **APROBADO** — El DE superó satisfactoriamente todas las validaciones y se convierte en DTE |
| AO | **APROBADO CON OBSERVACIONES** — El DE es aprobado (se convierte en DTE) pero posee observaciones (Ejemplo: extemporaneidad) |
| R | **RECHAZADO** — El DE no cumple las validaciones; se menciona el primer error identificado |

## Guía de columnas en las tablas de validación

| Columna | Descripción |
|---------|-------------|
| N° Val | Número secuencial de la regla de validación |
| ID | Identificación del campo del DE al que aplica |
| Mensaje de Validación | Texto de respuesta de la verificación |
| Código | Número de 4 dígitos correspondiente a la validación |
| Observación | Descripción de las reglas aplicadas |
| E | Estado resultante: A, AO o R |

---

## 12.1.1 – Códigos de respuesta de las validaciones de los Servicios Web

| ID Inicio | Código Inicio | ID Fin | Código Fin | Tipo de Regla | Estado v150 |
|-----------|---------------|--------|------------|---------------|-------------|
| AA01 | 0000 | AA100 | 0099 | Certificado de Transmisión (Protocolo TLS) | Vigente |
| ~~AB01~~ | ~~0100~~ | ~~AB20~~ | ~~0119~~ | ~~Forma del área de datos de los mensajes de entrada de los WS~~ | ~~Eliminado~~ |
| AC01 | 0120 | AC20 | 0139 | Certificado digital utilizado por el contribuyente para firmar | Vigente |
| AD01 | 0140 | AD20 | 0159 | Firma digital | Vigente |
| AE01 | 0160 | AE20 | 0179 | Validaciones genéricas sobre los mensajes de entrada de los WS | Vigente |
| AF01 | 0180 | AR20 | 0199 | Validaciones genéricas sobre los mensajes de control de llamada de los WS | Vigente |
| BA01 | 0200 | BA20 | 0219 | Mensaje de entrada del WS siRecepDE | Vigente |
| BB01 | 0220 | BB20 | 0239 | Información de control de la llamada al WS siRecepDE | Vigente |
| BC01 | 0260 | BC20 | 0259 | Área de datos del WS siRecepDE | Vigente |
| BD01 | 0270 | BD20 | 0279 | Mensaje de entrada del WS siRecepLoteDE | Vigente |
| BE01 | 0280 | BE20 | 0299 | Información de control de la llamada al WS siRecepLoteDE | Vigente |
| BF01 | 0300 | BF20 | 0319 | Área de datos del WS siRecepLoteDE | Vigente |
| BG01 | 0320 | BG20 | 0339 | Mensaje de entrada del WS siResultLoteDE | Vigente |
| BH01 | 0340 | BH20 | 0359 | Información de control de la llamada al WS siResultLoteDE | Vigente |
| BI01 | 0360 | BI20 | 0379 | Área de datos del WS siResultLoteDE | Vigente |
| BJ01 | 0380 | BJ20 | 0399 | Mensaje de entrada del WS siConsDE | Vigente |
| BK01 | 0400 | BK20 | 0419 | Información de control de la llamada al WS siConsDE | Vigente |
| BL01 | 0420 | BL20 | 0439 | Área de datos del WS siConsDE | Vigente |
| BM01 | 0460 | BM20 | 0479 | Mensaje de entrada del WS siConsRUC | Vigente |
| BN01 | 0480 | BN20 | 0499 | Información de control de la llamada al WS siConsRUC | Vigente |
| BO01 | 0500 | BO20 | 0559 | Área de datos del WS siConsRUC | Vigente |
| BS01 | 0560 | BS20 | 0579 | Mensaje de entrada del WS siRecepEvento | Vigente |
| BT01 | 0580 | BT20 | 0599 | Información de control de la llamada al WS siRecepEvento | Vigente |
| BU01 | 0600 | BU20 | 0619 | Área de datos del WS siRecepEvento | Vigente |

---

## 12.1.2 – Códigos de respuesta de las validaciones de los DE

| ID Inicio | Código Inicio | ID Fin | Código Fin | Tipo de Regla — Grupo de campos | Estado v150 |
|-----------|---------------|--------|------------|----------------------------------|-------------|
| A002 | 1000 | A004b | 1049 | Campos firmados del DE (A001–A099) | Vigente |
| B002 | 1050 | B003 | 1099 | Campos inherentes a la operación comercial (B001–B099) | Vigente |
| C003 | 1100 | C009 | 1149 | Campos de datos del Timbrado (C001–C099) | Vigente |
| D002 | 1150 | D002e | 1199 | Campos generales del DE (D001–D299) | Vigente |
| D010 | 1200 | [MODIFICADO] D020 | 1249 | Campos inherentes a la operación comercial (D010–D099) | [MODIFICADO] |
| D101 | 1250 | [MODIFICADO] D116 | 1299 | Campos que identifican al emisor del DE ([MODIFICADO] D100–D129) | [MODIFICADO] |
| [NUEVO] D130 | [NUEVO] 1261 | [NUEVO] D132 | [NUEVO] 1262 | [NUEVO] Campos que describen la actividad económica del emisor (D130–D139) | [NUEVO] |
| [MODIFICADO] D201 | 1300 | [MODIFICADO] D224 | 1349 | Datos que identifican al receptor del DE (D200–D299) | [MODIFICADO] |
| E010 | 1350 | E012 | 1399 | Campos que componen la Factura Electrónica FE (E010–E099) | Vigente |
| E020 | 1400 | E025 | 1449 | Campos de informaciones de Compras Públicas (E020–E029) | Vigente |
| [NUEVO] E300 | [NUEVO] 2550 | [NUEVO] E322 | [NUEVO] 2561 | [NUEVO] Campos que componen la Autofactura Electrónica AFE (E300–E399) | [NUEVO] |
| E400 | 1450 | E402 | 1499 | Campos que componen la Nota Crédito/Débito Electrónica NCE–NDE (E400–E499) | Vigente |
| [NUEVO] E500 | [NUEVO] 2600 | [NUEVO] E506 | [NUEVO] 2650 | [NUEVO] Campos que componen la Nota de Remisión Electrónica (E500–E599) | [NUEVO] |
| E600 | 1500 | E602 | 1549 | Campos que describen la condición de la operación (E600–E699) | Vigente |
| E605 | 1550 | E611a | 1599 | [MODIFICADO] Campos que describen la forma de pago al contado o del monto de la entrega inicial (E605–E619) | [MODIFICADO] |
| E620 | 1600 | E624 | 1649 | Campos que describen el pago con tarjeta de crédito/débito (E620–E629) | [MODIFICADO] |
| E630 | 1650 | E630a | 1699 | Campos que describen el pago en cheque (E630–E639) | Vigente |
| E640 | 1700 | E644a | 1749 | Campos que describen la operación a crédito (E640–E649) | Vigente |
| E650 | 1750 | E650a | 1799 | Campos que describen las cuotas (E650–E659) | Vigente |
| E704 | 1800 | [MODIFICADO] E717 | 1849 | Campos que describen los ítems de la operación (E700–E899) | [MODIFICADO] |
| E720 | 1850 | [MODIFICADO] E727 | 1899 | [MODIFICADO] Campos que describen el precio, tipo de cambio y valor total por ítem (E720–E729) | [MODIFICADO] |
| [NUEVO] EA003 | [NUEVO] 1852 | [NUEVO] EA050 | [NUEVO] 1862 | [NUEVO] Campos que describen los descuentos, anticipos y valor total por ítem (EA001–EA050) | [NUEVO] |
| E730 | 1900 | E736a | 1999 | Campos que describen el IVA de la operación (E730–E739) | Vigente |
| ~~E740~~ | ~~2000~~ | ~~E745~~ | ~~2049~~ | ~~Campos que describen el ISC de la operación (E740–E749)~~ | ~~Eliminado~~ |
| [MODIFICADO] E822 | 2050 | [MODIFICADO] E824 | 2099 | Campos de datos adicionales de uso comercial ([MODIFICADO] E820–E829) | [MODIFICADO] |
| E900 | 2100 | E912a | 2149 | Campos que describen el transporte de las mercaderías (E900–E999) | Vigente |
| E920 | 2150 | E930 | 2199 | Campos que identifican el local de salida de las mercaderías (E920–E939) | Vigente |
| E940 | 2200 | E950 | 2249 | Campos que identifican el local de entrega de las mercaderías (E940–E959) | Vigente |
| E960 | 2250 | [MODIFICADO] E966a | 2299 | Campos que identifican el vehículo de traslado (E960–E979) | [MODIFICADO] |
| E980 | 2300 | E989a | 2349 | Campos que identifican al transportista (E980–E999) | Vigente |
| F001 | 2350 | [MODIFICADO] F023b | 2399 | Campos que describen los subtotales y totales (F001–F099) | [MODIFICADO] |
| [NUEVO] G050 | [NUEVO] 2390 | [NUEVO] G050 | [NUEVO] 2399 | [NUEVO] Campos generales de la carga (G050–G099) | [NUEVO] |
| H001 | 2400 | [MODIFICADO] H017a | 2449 | Campos que identifican el documento asociado (H001–H049) | [MODIFICADO] |
| I002 | 2450 | I002 | 2459 | Información de la Firma Digital del DTE (I001–I049) | Vigente |
| J002 | 2500 | J003 | 2599 | Campos fuera de la Firma Digital (J001–J049) | Vigente |

---

## 12.1.3 – Códigos de respuesta de las validaciones de los eventos

| ID Inicio | Código Inicio | ID Fin | Código Fin | Tipo de Regla | Estado v150 |
|-----------|---------------|--------|------------|---------------|-------------|
| [MODIFICADO] GEC002 / GDE004 | 4000 | [NUEVO] GEC002c / [MODIFICADO] GDE008a | 4049 | Registro del evento cancelación de factura | [MODIFICADO] |
| [MODIFICADO] GEI002 | 4050 | [MODIFICADO] GEI006a | 4099 | Registro del evento Inutilización | [MODIFICADO] |
| [NUEVO] GEN001 | [NUEVO] 4100 | [NUEVO] GEN010a | [NUEVO] 4113 | [NUEVO] Registro del evento de Notificación – Recepción DE/DTE | [NUEVO] |
| [NUEVO] GCO001 | [NUEVO] 4150 | [NUEVO] GCO004 | [NUEVO] 4156 | [NUEVO] Registro del evento de Conformidad | [NUEVO] |
| [NUEVO] GDI001 | [NUEVO] 4200 | [NUEVO] GDI002e | [NUEVO] 4205 | [NUEVO] Registro del evento de Disconformidad | [NUEVO] |
| [NUEVO] GED002b | [NUEVO] 4250 | [NUEVO] GED10a | [NUEVO] 4262 | [NUEVO] Registro del evento de Desconocimiento | [NUEVO] |
| [NUEVO] GET004 | [NUEVO] 4300 | [NUEVO] GET030 | [NUEVO] 4323 | [NUEVO] Reglas de validación para el evento por actualización de datos: datos del transporte | [NUEVO] |
