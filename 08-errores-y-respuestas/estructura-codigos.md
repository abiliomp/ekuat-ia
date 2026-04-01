# Estructura de los Códigos de Validación

El SIFEN realiza validaciones en múltiples niveles: desde la conexión TLS hasta el contenido de cada campo del DE. Cada validación produce un resultado identificado por un código numérico de 4 dígitos.

> **Fuente:** Manual Técnico SIFEN v150, sección 12.1

---

## Estados de validación

| Código | Descripción | Significado |
|--------|-------------|-------------|
| A | Aprobado | El DE ha superado todas las validaciones y se convierte en DTE |
| AO | Aprobado con Observación | El DE fue aprobado como DTE pero presenta observaciones (ej: extemporaneidad) |
| R | Rechazado | El DE no cumple con las validaciones y no se convierte en DTE |

---

## Estructura de los códigos de validación

Los códigos de incumplimiento están compuestos de **4 dígitos numéricos**. El campo "ID" en las tablas de reglas identifica el código con dos letras que corresponden al tipo de validación (secuencia AA, AB, AC...).

---

## 12.1.1 — Códigos de respuesta de los Servicios Web

Rangos asignados a cada WS y tipo de validación:

| ID | Código inicio | Código fin | Tipo de validación |
|----|--------------|------------|-------------------|
| AA01 | 0000 | 0099 | Certificado de Transmisión (Protocolo TLS) |
| AB01 | 0100 | 0119 | Forma del área de datos de los mensajes de entrada de los WS |
| AC01 | 0120 | 0139 | Certificado digital del contribuyente para firmar |
| AD01 | 0140 | 0159 | Firma digital |
| AE01 | 0160 | 0179 | Validaciones genéricas sobre los mensajes de entrada de los WS |
| AF01 | 0180 | 0199 | Validaciones genéricas sobre los mensajes de control de llamada de los WS |
| BA01 | 0200 | 0219 | Mensaje de entrada del WS siRecepDE |
| BB01 | 0220 | 0239 | Información de control de la llamada al WS siRecepDE |
| BC01 | 0260 | 0259 | Área de datos del WS siRecepDE |
| BD01 | 0270 | 0279 | Mensaje de entrada del WS siRecepLoteDE |
| BE01 | 0280 | 0299 | Información de control de la llamada al WS siRecepLoteDE |
| BF01 | 0300 | 0319 | Área de datos del WS siRecepLoteDE |
| BG01 | 0320 | 0339 | Mensaje de entrada del WS siResultLoteDE |
| BH01 | 0340 | 0359 | Información de control de la llamada al WS siResultLoteDE |
| BI01 | 0360 | 0379 | Área de datos del WS siResultLoteDE |
| BJ01 | 0380 | 0399 | Mensaje de entrada del WS siConsDE |
| BK01 | 0400 | 0419 | Información de control de la llamada al WS siConsDE |
| BL01 | 0420 | 0439 | Área de datos del WS siConsDE |
| BM01 | 0460 | 0479 | Mensaje de entrada del WS siConsRUC |
| BN01 | 0480 | 0499 | Información de control de la llamada al WS siConsRUC |
| BO01 | 0500 | 0559 | Área de datos del WS siConsRUC |
| BS01 | 0560 | 0579 | Mensaje de entrada del WS siRecepEvento |
| BT01 | 0580 | 0599 | Información de control de la llamada al WS siRecepEvento |
| BU01 | 0600 | 0619 | Área de datos del WS siRecepEvento |

---

## 12.1.2 — Códigos de respuesta de las validaciones de los DE

Rangos asignados a cada grupo de campos del DE:

| ID inicio | ID fin | Código inicio | Código fin | Grupo de campos |
|-----------|--------|--------------|------------|----------------|
| A002 | A004b | 1000 | 1049 | Campos firmados del DE (A001-A099) |
| B002 | B003 | 1050 | 1099 | Campos inherentes a la operación de DE (B001-B099) |
| C003 | C009 | 1100 | 1149 | Campos de datos del Timbrado (C001-C099) |
| D002 | D002e | 1150 | 1199 | Campos generales del DE (D001-D299) |
| D010 | D020 | 1200 | 1249 | Campos inherentes a la operación comercial (D010-D099) |
| D101 | D116 | 1250 | 1299 | Campos que identifican al emisor (D100-D129) |
| D130 | D132 | 1261 | 1262 | Actividad económica del emisor (D130-D139) |
| D201 | D224 | 1300 | 1349 | Datos del receptor (D200-D299) |
| E010 | E012 | 1350 | 1399 | Campos de la Factura Electrónica (E010-E099) |
| E020 | E025 | 1400 | 1449 | Campos de Compras Públicas (E020-E029) |
| E300 | E322 | 2550 | 2561 | Campos de la Autofactura Electrónica (E300-E399) |
| E400 | E402 | 1450 | 1499 | Campos NCE/NDE (E400-E499) |
| E500 | E506 | 2600 | 2650 | Campos de la Nota de Remisión (E500-E599) |
| E600 | E602 | 1500 | 1549 | Condición de la operación (E600-E699) |
| E605 | E611a | 1550 | 1599 | Forma de pago al contado (E605-E619) |
| E620 | E624 | 1600 | 1649 | Pago con tarjeta (E620-E629) |
| E630 | E630a | 1650 | 1699 | Pago con cheque (E630-E639) |
| E640 | E644a | 1700 | 1749 | Operación a crédito (E640-E649) |
| E650 | E650a | 1750 | 1799 | Cuotas (E650-E659) |
| E704 | E717 | 1800 | 1849 | Ítems de la operación (E700-E899) |
| E720 | E727 | 1850 | 1899 | Precio y valor total por ítem (E720-E729) |
| EA003 | EA050 | 1852 | 1862 | Descuentos, anticipos y valor total por ítem (EA001-EA050) |
| E730 | E736a | 1900 | 1999 | IVA por ítem (E730-E739) |
| E740 | E745 | 2000 | 2049 | ISC por ítem (E740-E749) |
| E822 | E824 | 2050 | 2099 | Datos adicionales de uso comercial (E820-E829) |
| E900 | E912a | 2100 | 2149 | Transporte de mercaderías (E900-E999) |
| E920 | E930 | 2150 | 2199 | Local de salida de mercaderías (E920-E939) |
| E940 | E950 | 2200 | 2249 | Local de entrega de mercaderías (E940-E959) |
| E960 | E966a | 2250 | 2299 | Vehículo de traslado (E960-E979) |
| E980 | E989a | 2300 | 2349 | Transportista (E980-E999) |
| F001 | F023b | 2350 | 2399 | Subtotales y totales (F001-F099) |
| G050 | G050 | 2390 | 2399 | Campos de la carga (G050-G099) |
| H001 | H017a | 2400 | 2449 | Documento asociado (H001-H049) |
| I002 | I002 | 2450 | 2459 | Firma Digital del DTE (I001-I049) |
| J002 | J003 | 2500 | 2599 | Campos fuera de la Firma Digital (J001-J049) |

---

## 12.1.3 — Códigos de respuesta de las validaciones de eventos

| ID inicio | ID fin | Código inicio | Código fin | Tipo de validación |
|-----------|--------|--------------|------------|-------------------|
| GEC002 | GEC002c | 4000 | 4049 | Evento de cancelación |
| GEI002 | GEI006a | 4050 | 4099 | Evento de inutilización |
| GEN001 | GEN010a | 4100 | 4113 | Evento de notificación – recepción DE/DTE |
| GCO001 | GCO004 | 4150 | 4156 | Evento de conformidad |
| GDI001 | GDI002e | 4200 | 4205 | Evento de disconformidad |
| GED002b | GED10a | 4250 | 4262 | Evento de desconocimiento |
| GET004 | GET030 | 4300 | 4323 | Evento por actualización de datos del transporte |

---

## Estructura del Response de los WS

Los WS devuelven una respuesta con la siguiente estructura (campos clave):

| Campo | Descripción |
|-------|-------------|
| `dEstRes` | Estado del resultado: "Aprobado", "Aprobado con observación" o "Rechazado" |
| `dProtAut` | Número de transacción (solo para resultados aprobados) |
| `dCodRes` | Código numérico de 4 dígitos del resultado |
| `dMsgRes` | Mensaje descriptivo del resultado |

Para producción, la respuesta se limita a **5 mensajes máximos** por DE.

---

## Diferencia entre validaciones WS y validaciones DE

| Tipo | Descripción | Rango de códigos |
|------|-------------|-----------------|
| **Validaciones WS** | Verifican la estructura, certificados, firma y mensajes de los Web Services | 0000–0619 |
| **Validaciones DE** | Verifican el contenido y los campos del Documento Electrónico | 1000–2599 |
| **Validaciones de eventos** | Verifican la estructura y datos de los eventos (cancelación, inutilización, etc.) | 4000–4323 |
