> **Fuente:** Manual Técnico SIFEN v150, sección 12.4
> **Nota:** Contenido tachado (~~así~~) indica validaciones eliminadas en v150 — **NO deben tratarse como reglas vigentes**. [MODIFICADO] indica cambios. [NUEVO] indica adiciones en v150.

# Errores de Validación del DE (Sección 12.4)

**Estados:** A=Aprobado, AO=Aprobado con Observación, R=Rechazado

La tabla sigue el formato: `| N° | ID | Mensaje | Código | Tipo | Observación |`

---

## A. Campos firmados del Documento Electrónico (A001–A099) — Códigos 1000–1049

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 1 | A002 | CDC no correspondiente con las informaciones del XML | 1000 | R | El CDC no es compatible con C002, D101, D102, C005, C006, C007, D103, D002, B002, B004, A003 |
| 2 | A002a | CDC duplicado | 1001 | R | Ya fue autorizado otro documento con coincidencia simultánea de contenido de los campos del CDC |
| 3 | A002b | Documento electrónico duplicado | 1002 | R | Coincidencia en: Tipo doc (C002), Nº Timbrado (C004), Nº doc (C007), Tipo emisión (B002), Establecimiento (C005), Punto expedición (C006). [NUEVO] 7) Serie (C010) Si se informa |
| 4 | A003 | DV del CDC inválido | 1003 | R | Valor incorrecto del dígito verificador según algoritmo módulo 11 |
| 5 | A004a | La fecha y hora de la firma digital es adelantada | 1004 | R | La fecha y hora de la firma digital no debe ser posterior a la fecha y hora de SIFEN |
| 6 | A004b | Transmisión extemporánea del DE | 1005 | AO | Transmisión excede el tiempo de validación posterior parametrizado para el contribuyente (referencia: fecha de la Firma Digital A004). Aprobado con observaciones (Extemporaneidad) |

---

## B. Campos inherentes a la operación comercial de los DE (B001–B099) — Códigos 1050–1099

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 7 | B002 | Tipo de emisión inválido en esta etapa | 1050 | R | El tipo de emisión en contingencia (B002=2) no está permitido en esta etapa |
| 8 | B003 | Descripción del tipo de emisión no corresponde al código | [MODIFICADO] 1051 | R | Descripción del tipo de emisión no coincidente con lo informado en B002 |

---

## C. Campos de datos del Timbrado (C001–C099) — Códigos 1100–1149

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 9 | C003 | Descripción del tipo de documento electrónico no corresponde al código | 1100 | R | |
| 10 | C004 | Número de timbrado inválido | 1101 | R | [NUEVO] Número de timbrado no corresponde al RUC ni al Tipo de Documento electrónico del contribuyente emisor |
| 11 | C004a | Número de timbrado no corresponde al medio de generación para facturación electrónica | 1102 | R | Medio de generación incorrecto en el sistema de Timbrado de Marangatu |
| 12 | C004b | El número de timbrado no se encuentra vigente a la fecha de emisión del comprobante | 1103 | R | Número de timbrado no vigente: D002 debe estar dentro del rango de fechas de vigencia del timbrado (C008–C009) |
| 13 | C004c | El número de timbrado informado no se encuentra en estado ACTIVO | 1104 | R | |
| 14 | C005 | Código de establecimiento incorrecto | 1105 | R | El código de establecimiento no corresponde al timbrado autorizado |
| 15 | C006 | Código de punto de expedición incorrecto | 1106 | R | El código de punto de expedición no corresponde al timbrado autorizado |
| 16 | [NUEVO] C007 | Número de documento ha sido inutilizado anteriormente | [NUEVO] 1109 | R | [NUEVO] El número de documento que pertenece al Nº de Timbrado, establecimiento y punto de expedición se encuentra inutilizado |
| 17 | C008 | Fecha de inicio de vigencia del timbrado incorrecta | 1107 | R | Fecha de inicio de vigencia no corresponde al timbrado autorizado |
| ~~18~~ | ~~C009~~ | ~~Fecha fin de vigencia del timbrado incorrecta~~ | ~~1108~~ | ~~R~~ | ~~Eliminada en v150~~ |
| 18 | [NUEVO] C010 | Serie informada incorrecta | [NUEVO] 1110 | R | [NUEVO] Se debe respetar la secuencialidad de la serie (AA, AB, AC…AZ…ZA…ZZ). Primera serie debe ser AA. No se permiten: primera serie ≠ AA; serie no vecina a la mayor enviada al SIFEN; serie anterior/posterior con fecha inconsistente |

---

## D. Datos generales del Documento Electrónico (D001–D299) — Códigos 1150–1199

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 19 | [MODIFICADO] D002 | La fecha y hora de emisión del DE informada es inválida por retraso | [MODIFICADO] 1150 | R | [MODIFICADO] Cuando la fecha de emisión es anterior a la de transmisión al SIFEN, la diferencia no debe ser mayor a 720 horas (30 días) |
| 20 | [MODIFICADO] D002f | La fecha y hora de emisión del DE informada es inválida por envío adelantado | [MODIFICADO] 1151 | R | [MODIFICADO] Cuando la fecha de emisión del DE es posterior a la de transmisión al SIFEN, la diferencia no debe ser mayor a 120 horas (5 días) |
| 21 | [NUEVO] D002a | Fecha y hora de emisión del DE es anterior a la fecha de lanzamiento del sistema | [NUEVO] 1156 | R | [NUEVO] La fecha y hora de emisión del DE debe ser posterior al 22 de noviembre del 2018 |

### D1. Campos inherentes a la operación comercial (D010–D099) — Códigos 1200–1249

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 22 | D010 | Grupo de informaciones inherentes a la operación comercial es obligatorio informar para el tipo de documento | 1200 | R | Obligatorio para todos los tipos de DE excepto Nota de Remisión Electrónica (C002=7) |
| 23 | D010a | Grupo de informaciones inherentes a la operación comercial no es permitido para el tipo de documento | 1201 | R | No permitido para Nota de Remisión Electrónica (C002=7) |
| 24 | D011 | Tipo de transacción no informado para el documento electrónico seleccionado | 1202 | R | Obligatorio si C002=1, 2, 3 o 4 |
| 25 | D012 | Descripción del tipo de transacción no corresponde al código | 1203 | R | |
| ~~28~~ | ~~D013~~ | ~~Tipo de impuesto afectado no informado~~ | ~~1204~~ | ~~R~~ | ~~Eliminada en v150~~ |
| 26 | [MODIFICADO] D014 | La descripción del tipo de impuesto afectado no corresponde al código | [MODIFICADO] 1205 | R | [MODIFICADO] |
| 27 | D016 | Descripción de la moneda de la operación no corresponde al código | 1206 | R | |
| 28 | D017 | Condición del tipo de cambio no informada | 1207 | R | Obligatorio si D015≠PYG |
| 29 | D017a | Condición del tipo de cambio no requerida | 1208 | R | Si D015=PYG, D017 no debe informarse |
| 30 | D018 | Tipo de cambio de la operación no informado | 1209 | R | Obligatorio si D017=1 (global) |
| 31 | D018a | Tipo de cambio de la operación no requerido | 1210 | R | [NUEVO] Si D017=2 o D015=PYG, D018 no debe informarse |
| 32 | [NUEVO] D020 | Descripción de la condición del anticipo no corresponde al código | [NUEVO] 1211 | R | [NUEVO] |

### D2. Datos que identifican al emisor del DE ([MODIFICADO] D100–D129) — Códigos 1250–1299

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 33 | D101 | RUC del emisor inexistente | 1250 | R | El RUC informado no existe en la base de datos |
| 34 | D101a | RUC del Emisor inhabilitado para facturación electrónica | 1251 | R | RUC no habilitado en Marangatu |
| 35 | D101b | El RUC del emisor se encuentra inactivo | 1252 | R | El RUC debe tener estado distinto a CANCELADO, CANCELADO DEFINITIVO o SUSPENSIÓN TEMPORAL al momento de emisión |
| 36 | [NUEVO] D101c | RUC del emisor no está habilitado para utilizar este tipo de servicio | [NUEVO] 1264 | R | [NUEVO] RUC no habilitado para el servicio síncrono |
| 37 | D102 | Dígito Verificador del RUC del emisor incorrecto | 1253 | R | DV no corresponde al módulo 11 del RUC |
| 38 | [NUEVO] D105 | Nombre o razón social del emisor del DE inválido | [NUEVO] 1263 | R | [NUEVO] Ambiente de pruebas: debe usarse `"DE generado en ambiente de prueba - sin valor comercial ni fiscal"`. No usar ese texto en producción. |
| 39 | [MODIFICADO] D111 | El Departamento, el Distrito y la Ciudad de emisión no están relacionados | 1255 | R | [MODIFICADO] |
| 40 | D112 | Descripción del departamento de emisión no corresponde al código | 1254 | R | |
| ~~44~~ | ~~D114~~ | ~~Es obligatorio indicar la descripción del código de distrito de emisión~~ | ~~1256~~ | ~~R~~ | ~~Eliminada en v150~~ |
| 41 | D114a | Descripción del distrito de emisión no corresponde al código | 1257 | R | |
| ~~43~~ | ~~D115~~ | ~~La ciudad de emisión no corresponde al departamento seleccionado~~ | ~~1258~~ | ~~R~~ | ~~Eliminada en v150~~ |
| ~~44~~ | ~~D115a~~ | ~~La ciudad de emisión no corresponde al distrito seleccionado~~ | ~~1259~~ | ~~R~~ | ~~Eliminada en v150~~ |
| 42 | D116 | Descripción de la ciudad de emisión no corresponde al código | 1260 | R | |

### D2.1 Campos de actividad económica del emisor (D130–D139) — [NUEVO] Códigos 1261–1262

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 43 | [MODIFICADO] D131 | Código de actividad económica incorrecto | 1261 | R | La actividad económica seleccionada no corresponde a lo declarado en el RUC |
| 44 | [MODIFICADO] D132 | Descripción de la actividad económica no corresponde al código | 1262 | R | |

### D3. Datos que identifican al receptor del DE (D200–D299) — Códigos 1300–1349

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 45 | [NUEVO] D201 | Naturaleza del Receptor inválida para el tipo documento electrónico | [NUEVO] 1315 | R | [NUEVO] Si C002=4 (Autofactura), D201 debe ser Contribuyente (D201=1) |
| 46 | D202 | El tipo de operación no compatible con la naturaleza del receptor | 1300 | R | [MODIFICADO] Si C002≠4 y D201=2, D202 debe ser B2C. [NUEVO] Si D202=4 (B2F), D201 debe ser 2 |
| 47 | [NUEVO] D202a | El tipo de operación no compatible con el tipo documento electrónico | [NUEVO] 1316 | R | [NUEVO] Si C002=4, D202 debe ser B2C (D202=2) |
| 48 | [NUEVO] D203 | Código de país del receptor inválido para el tipo de operación informado | [NUEVO] 1320 | R | [NUEVO] Si D202=4: D203≠PRY. Si D202≠4: D203=PRY |
| 49 | D204 | Descripción del país receptor no corresponde al código | 1301 | R | |
| 50 | D205 | Es obligatorio informar el tipo de contribuyente receptor | 1302 | R | Obligatorio si D201=1 |
| 51 | D205a | [MODIFICADO] Tipo de contribuyente receptor inválido | 1303 | R | Si D201=2, D205 no debe informarse |
| 52 | D206 | Es obligatorio informar el RUC del receptor contribuyente | 1304 | R | Obligatorio si D201=1 |
| 53 | D206a | RUC del receptor no requerido | 1305 | R | Si D201=2, D206 no debe informarse |
| 54 | D206b | RUC del receptor inexistente en la base de datos de Marangatu | 1306 | R | |
| 55 | D206c | El RUC se encuentra inactivo para el tipo de contribuyente receptor | 1307 | R | Si D205=2 (persona jurídica), debe tener estado distinto a CANCELADO/CANCELADO DEFINITIVO/SUSPENSIÓN TEMPORAL |
| 56 | D206d | El RUC del receptor se encuentra inactivo para el tipo de operación | 1308 | R | Si D202=1 o 3 (B2B o B2G), RUC debe estar activo |
| 57 | [NUEVO] D206e | RUC del Receptor inválido para el tipo de documento electrónico | [NUEVO] 1317 | R | [NUEVO] Si C002=4, D206 debe ser igual a D101 (receptor = emisor) |
| 58 | D207 | Dígito Verificador del RUC del receptor incorrecto | 1309 | R | |
| 59 | D208 | Es obligatorio informar el tipo de documento de identidad del receptor | 1310 | R | [NUEVO] Si D201=2 y D202≠4, D208 es obligatorio |
| 60 | D208a | Tipo de documento de identidad del receptor [MODIFICADO] inválido | 1311 | R | Si D201=1, D208 no debe informarse |
| 61 | [NUEVO] D208b | Tipo de documento de identidad del receptor incorrecto para el tipo de operación | [NUEVO] 1319 | R | [NUEVO] D208=5 (innominado) no puede ser cuando D202≠2 |
| 62 | [NUEVO] D208c | Tipo de documento de identidad del receptor incorrecto para el total general de la operación en guaraníes | [NUEVO] 1321 | R | [NUEVO] Si D011≠13, D208≠5 cuando F023≥60.000.000 o F014≥60.000.000 |
| 63 | [NUEVO] D208d | El tipo de documento de identidad del receptor no es requerido | [NUEVO] 1322 | R | [NUEVO] Si D201=1 o D202=4, D208 no debe informarse |
| ~~60~~ | ~~D209~~ | ~~Descripción del tipo de documento de identidad del receptor no informada~~ | ~~1312~~ | ~~R~~ | ~~Eliminada en v150~~ |
| 64 | D209a | Descripción del tipo de documento de identidad del receptor no corresponde al código | 1313 | R | |
| 65 | D210 | Es obligatorio informar el número de documento de identidad del receptor | 1314 | R | [NUEVO] Si D201=2 y D202≠4, D210 es obligatorio |
| 66 | [NUEVO] D210a | El número de documento de identidad del receptor no es requerido | [NUEVO] 1323 | R | [NUEVO] Si D201=1 o D202=4, D210 no debe informarse |
| 67 | [NUEVO] D213 | Dirección del receptor no informado para el tipo de documento electrónico | [NUEVO] 1318 | R | [NUEVO] Si C002=7 o D202=4, D213 es obligatorio |
| 68 | [NUEVO] D218 | Es obligatorio informar el número de casa del receptor | [NUEVO] 1330 | R | [NUEVO] Si se informa D213, D218 es obligatorio |
| 69 | [NUEVO] D219 | Es obligatorio informar el departamento del receptor | [NUEVO] 1324 | R | [NUEVO] Si se informa D213 y D202≠4 |
| 70 | [NUEVO] D220 | Descripción del departamento de emisión no corresponde al código | [NUEVO] 1325 | R | [NUEVO] |
| 71 | [NUEVO] D222 | Descripción del distrito de emisión no corresponde al código | [NUEVO] 1326 | R | [NUEVO] |
| 72 | [NUEVO] D223 | Es obligatorio informar la ciudad del receptor | [NUEVO] 1327 | R | [NUEVO] Si se informa D213 y D202≠4 |
| 73 | [NUEVO] D223a | El Departamento, el Distrito y la Ciudad del receptor no están relacionados | [NUEVO] 1328 | R | [NUEVO] |
| 74 | [NUEVO] D224 | Descripción de la ciudad de emisión no corresponde al código | [NUEVO] 1329 | R | [NUEVO] |

---

## E. Campos específicos por tipo de Documento Electrónico

### E1. Campos de la FE (E010–E099) — Códigos 1350–1399

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 75 | E010 | Grupo de campos que componen la FE es obligatorio para tipo de documento electrónico seleccionado | 1350 | R | Si C002=1 |
| 76 | E010a | Grupo de campos que componen la FE no requerido | 1351 | R | Si C002≠1 |
| 77 | E012 | Descripción del indicador de presencia no corresponde al código | 1352 | R | |

### E1.1. Compras Públicas (E020–E029) — Códigos 1400–1449

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 78 | E020 | Grupo de informaciones de Compras Públicas es obligatorio | 1400 | R | Obligatorio si D202=3 (B2G) |
| 79 | [MODIFICADO] E020a | Grupo de informaciones de Compras Públicas no requerido para el tipo de operación | 1401 | R | Solo permitido si D202=3 |
| 80 | E025 | Fecha de emisión del código de contratación inválida | 1402 | R | E025 no puede ser superior a la fecha de emisión (D202) de la FE |

### E4. Campos de la AFE (E300–E399) — [NUEVO] Códigos 2550–2561

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 81 | [NUEVO] E300 | Para el tipo de documento electrónico seleccionado, es obligatorio informar el grupo de campos que componen la AFE | [NUEVO] 2550 | R | [NUEVO] Si C002=4 |
| 82 | [NUEVO] E300a | Para el tipo de documento electrónico seleccionado, no se debe informar el grupo de campos que componen la AFE | [NUEVO] 2551 | R | [NUEVO] Si C002≠4 |
| 83 | [NUEVO] E304 | El vendedor no debe ser contribuyente | [NUEVO] 2562 | R | [NUEVO] Si E304=1 o 2 (cédula o pasaporte), el vendedor no debe ser contribuyente activo |
| 84 | [NUEVO] E310 | El Departamento, el Distrito y la Ciudad del vendedor no están relacionados | [NUEVO] 2553 | R | [NUEVO] |
| 85 | [NUEVO] E311 | Descripción del departamento del vendedor no corresponde al código | [NUEVO] 2552 | R | [NUEVO] |
| 86 | [NUEVO] E313b | Descripción del código del distrito del vendedor no corresponde al código | [NUEVO] 2561 | R | [NUEVO] |
| 87 | [NUEVO] E315 | Descripción de la ciudad del vendedor no corresponde al código | [NUEVO] 2555 | R | [NUEVO] |
| 88 | [NUEVO] E317 | El Departamento, el Distrito y la Ciudad donde se realiza la transacción no están relacionados | [NUEVO] 2557 | R | [NUEVO] |
| 89 | [NUEVO] E318 | Descripción del departamento no corresponde al código donde se realiza la transacción | [NUEVO] 2556 | R | [NUEVO] |
| 90 | [NUEVO] E320 | Descripción del distrito donde se realiza la transacción no corresponde al código | [NUEVO] 2558 | R | [NUEVO] |
| 91 | [NUEVO] E322 | Descripción de la ciudad no corresponde al código donde se realiza la transacción | [NUEVO] 2559 | R | [NUEVO] |

### E5. Campos de la NCE/NDE (E400–E499) — Códigos 1450–1499

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 92 | E400 | Para el tipo de documento electrónico seleccionado es obligatorio informar el grupo de campos que componen la NCE–NDE | 1450 | R | Si C002=5 o 6 |
| 93 | E400a | Para el tipo de documento electrónico seleccionado no se requiere informar el grupo de campos que componen la NCE–NDE | 1451 | R | Si C002≠5 o 6 |
| 94 | E402 | Descripción del motivo de emisión no corresponde al código | 1452 | R | |

### E6. Campos de la NRE (E500–E599) — [NUEVO] Códigos 2600–2650

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 95 | [NUEVO] E500 | Para el tipo de documento electrónico seleccionado, es obligatorio informar el grupo de campos que componen la NRE | [NUEVO] 2600 | R | [NUEVO] Si C002=7 |
| 96 | [NUEVO] E500a | Para el tipo de documento electrónico seleccionado, no se debe informar el grupo de campos que componen la NRE | [NUEVO] 2601 | R | [NUEVO] Si C002≠7 |
| 97 | [NUEVO] E501 | RUC del receptor no coincidente con el RUC del emisor | [NUEVO] 2606 | R | [NUEVO] Si E501=7 (traslado entre locales), D101=D206 |
| 98 | [NUEVO] E502 | Descripción del motivo de emisión no corresponde al código | [NUEVO] 2602 | R | [NUEVO] |
| 99 | [NUEVO] E504 | Descripción del responsable de la emisión de la NRE, no corresponde al código | [NUEVO] 2603 | R | [NUEVO] |
| 100 | [NUEVO] E506 | Fecha futura de emisión de la factura excede el límite permitido | [NUEVO] 2604 | R | [NUEVO] El mes de la fecha estimada no puede ser posterior al mes de emisión de la NRE |
| 101 | [NUEVO] E506a | Fecha futura de emisión de la factura no informada para el tipo de documento electrónico | [NUEVO] 2605 | R | [NUEVO] Si E501=1 (traslado por venta) y no se informan documentos asociados (H001), E506 es obligatorio |

---

## E7. Condición de la operación (E600–E699) — Códigos 1500–1549

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 102 | E600 | Para el tipo de documento electrónico seleccionado es obligatorio informar la condición de la operación | 1500 | R | [MODIFICADO] Si C002=1 o C002=4 |
| 103 | E600a | Para el tipo de documento electrónico seleccionado no se requiere informar la condición de la operación | 1501 | R | [MODIFICADO] Si C002≠1 y C002≠4 |
| 104 | [NUEVO] E601 | Condición de la operación inválida para el tipo de documento electrónico | [NUEVO] 1503 | R | [NUEVO] Si C002=4 (Autofactura), E601 debe ser 1 (contado) |
| 105 | E602 | Descripción de la condición de la operación no corresponde al código | 1502 | R | |
| 106 | E605 | El grupo de campos que describen la forma de pago al contado o del monto de la entrega inicial es obligatorio | 1550 | R | Si E601=1 (contado) |
| 107 | E605a | El grupo de campos que describen la forma de pago al contado o del monto de la entrega inicial (crédito con cuota inicial) es obligatorio | 1551 | R | Si E601=2 y existe E645 |
| 108 | E605b | El grupo de campos que describen la forma de pago al contado o del monto de la entrega inicial no requerida | 1552 | R | Si E601=2 y NO existe E645 |
| 109 | E606 | Tipo de pago inválido | 1553 | R | [MODIFICADO] Si E606=16 (Pago bancario), E011 debe ser 5 (Operación bancaria). Solo aplica a FE. |
| 110 | E607 | Descripción del tipo de pago no corresponde al código | 1554 | R | |
| 111 | E610 | Descripción de la moneda no corresponde al código | 1555 | R | |
| 112 | E611 | Tipo de cambio no informado para la moneda por tipo de pago seleccionada | 1556 | R | Si E609≠PYG, E611 es obligatorio |
| 113 | E611a | Tipo de cambio informado es inválido para la moneda por tipo de pago seleccionada | 1557 | R | Si E609=PYG, E611 no debe existir |

### E7.1.1. Pago con tarjeta (E620–E629) — Códigos 1600–1649

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 114 | E620 | Grupo de campos que describen el pago o entrega inicial con tarjeta de crédito/débito es obligatorio | 1600 | R | Si E606=3 o 4 |
| 115 | E620a | Grupo de los campos que describen el pago de la operación con tarjeta de crédito/débito no requerido | 1601 | R | [MODIFICADO] Si E606≠3 o 4 |
| 116 | E622 | Descripción de la denominación de la tarjeta no corresponde al código | 1602 | R | |
| 117 | E623 | RUC de la procesadora de tarjeta inexistente | 1603 | R | |
| 118 | E624 | Digito verificador del RUC de la procesadora de tarjeta es inexistente | 1604 | R | |

### E7.1.2. Pago en cheque (E630–E639) — Códigos 1650–1699

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 119 | E630 | Grupo de los campos que describen el pago o entrega inicial de la operación en cheque es obligatorio | 1650 | R | Si E606=2 |
| 120 | E630a | Grupo de los campos que describen el pago o entrega inicial de la operación en cheque no requerido | 1651 | R | Si E606≠2 |

### E7.2. Operación a crédito (E640–E649) — Códigos 1700–1749

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 121 | E640 | Grupo de los campos que describen la forma de pago a crédito es obligatorio | 1700 | R | Si E601=2 |
| 122 | E640a | Grupo de los campos que describen la forma de pago a crédito no requerido | 1701 | R | Si E601≠2 |
| 123 | E642 | Descripción de la condición de la operación a crédito no corresponde al código | 1702 | R | |
| 124 | E643 | Plazo del crédito es obligatorio | 1703 | R | Si E641=1 |
| 125 | E643a | Plazo del crédito no requerido | 1704 | R | Si E641≠1 |
| 126 | E644 | Cantidad de cuotas es obligatorio | 1705 | R | Si E641=2 |
| 127 | E644a | Cantidad de cuotas no requerida | 1706 | R | Si E641≠2 |

### E7.2.1. Cuotas (E650–E659) — Códigos 1750–1799

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| ~~117~~ | ~~E650~~ | ~~Grupo de los campos que describen las cuotas es obligatorio~~ | ~~1750~~ | ~~R~~ | ~~Eliminada en v150~~ |
| 128 | E650a | Grupo de los campos que describen las cuotas no requerido | 1751 | R | Si E641≠2 |

---

## E8. Campos que describen los ítems de la operación (E700–E899) — Códigos 1800–1849

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 129 | E704 | Código de DNCP - Nivel General es obligatorio para el tipo de operación B2G | 1800 | R | Si D202=3 |
| 130 | E705 | Código de DNCP – Nivel Específico es obligatorio | 1801 | R | Si existe E704 |
| 131 | E710 | Descripción de la unidad de medida no corresponde al código | 1802 | R | |
| 132 | E713 | Descripción del país de origen del producto no corresponde al código | 1804 | R | |
| ~~132~~ | ~~E715~~ | ~~Código de datos de relevancia de las mercaderías no informado para el tipo de documento electrónico~~ | ~~1805~~ | ~~R~~ | ~~Eliminada en v150~~ |
| 133 | [NUEVO] E715 | Código de datos de relevancia de las mercaderías no requerido para el tipo de documento electrónico | [NUEVO] 1807 | R | [NUEVO] No informar E715 cuando C002≠7 |
| 134 | [NUEVO] E716 | Descripción del código de datos de relevancia de las mercaderías no corresponde al código | [NUEVO] 1806 | R | [NUEVO] |
| 135 | [NUEVO] E717 | Se debe informar la cantidad o el porcentaje de quiebra o merma | [NUEVO] 1808 | R | [NUEVO] Si se informa E715, obligatorio uno de: E717 o E718 |

### E8.1. Precio, tipo de cambio y valor total por ítem (E720–E729) — Códigos 1850–1899

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 136 | E720 | Grupo de los campos que describen los precios, descuentos y valor total por ítem es obligatorio | 1850 | R | Obligatorio para todos los tipos de DE excepto NRE (C002=7) |
| 137 | E720a | Grupo de los campos que describen los precios, descuentos y valor total por ítem no requerido | 1851 | R | Si C002=7 |
| 138 | E725 | Tipo de cambio por ítem no informado | 1854 | R | Si D017=2 |
| 139 | E725a | Tipo de cambio por ítem no requerido | 1855 | R | Si D017=1 |
| 140 | E725b | La moneda de la operación seleccionada no requiere tipo de cambio por ítem | 1856 | R | Si D015=PYG |
| 141 | [NUEVO] E727 | Error en el cálculo del valor total bruto de la operación por ítem | [NUEVO] 1859 | R | [NUEVO] E727 debe ser E721 * E711 |

### E8.1.1. Descuentos, anticipos y valor total por ítem (EA001–EA050) — [NUEVO] Códigos 1852–1862

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 142 | EA003 | [MODIFICADO] Porcentaje de descuento particular por ítem no informado | 1852 | R | [MODIFICADO] Si EA002 > 0, es obligatorio el porcentaje respectivo |
| 143 | [NUEVO] EA003a | Error en el cálculo del porcentaje de descuento particular por ítem | [NUEVO] 1861 | R | [NUEVO] EA003 = [EA002 * 100 / E721]. Variación permitida: 0.8 |
| 144 | [NUEVO] EA004 | El descuento global sobre el precio unitario por ítem no coincidente con lo informado | [NUEVO] 1862 | R | [NUEVO] EA004 = [EA004 * 100 / E721]. Variación permitida: 0.8 |
| 145 | EA008 | Error en el cálculo del valor total de la operación por ítem | 1853 | R | [MODIFICADO] EA008 = (E721 - EA002 – EA004 – EA006 – EA007) * E711 |
| 146 | EA009 | [MODIFICADO] Valor total de la operación por ítem en guaraníes no informado | 1857 | R | Si existe E725 (tipo de cambio por ítem), EA009 es obligatorio |
| 147 | EA009a | [MODIFICADO] Error en el cálculo del valor total de la operación por ítem en guaraníes | 1858 | R | [MODIFICADO] EA009 = EA008 * E725 |

### E8.2. IVA de la operación (E730–E739) — Códigos 1900–1999

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 148 | E730 | Grupo de los campos que describen el IVA de la operación es obligatorio | 1900 | R | [NUEVO] Si D013=1, 3, 4 o 5 y C002≠3,4,7 |
| 149 | E730a | Grupo de los campos que describen el IVA de la operación no requerido para el tipo de documento electrónico seleccionado | 1901 | R | Si C002=3, 4 o 7 |
| 150 | E730b | Grupo de los campos que describen el IVA de la operación no requerido para el tipo de impuesto al consumo afectado seleccionado | 1902 | R | Si D013=2 (ISC) |
| 151 | E732 | Descripción de la forma de afectación tributaria del IVA no corresponde al código | 1903 | R | |
| 152 | E733 | Proporción gravada del IVA incorrecta para forma de afectación Gravado IVA | 1904 | R | Si E731=1, E733 debe ser 100 |
| 153 | E733a | Proporción gravada del IVA incorrecta para forma de afectación Exonerado o Exento | 1905 | R | Si E731=2 o 3, E733 debe ser 0 |
| 154 | E733b | Proporción gravada del IVA incorrecta para forma de afectación Gravado Parcial | 1906 | R | Si E731=4, E733 debe ser >0 y <100 |
| 155 | E734 | Tasa del IVA es incorrecta para forma de afectación Exonerado o Exento | 1907 | R | Si E731=2 o 3, E734 debe ser 0 |
| 156 | E734a | Tasa del IVA es incorrecta para la forma de afectación Gravado IVA o Gravado parcial | 1908 | R | Si E731=1 o 4, E734 debe ser 5 o 10 |
| 157 | E735 | Error en el cálculo de la base gravada del IVA por ítem para forma de afectación Exonerado o Exento | 1909 | R | Si E731=2 o 3, E735 debe ser 0 |
| 158 | E735a | Error en el cálculo de la base gravada del IVA por ítem para tasa del 5% | 1910 | R | [MODIFICADO] E735 = [EA008 * (E733/100)] / 1,05 |
| 159 | E735b | Error en el cálculo de la base gravada del IVA por ítem para tasa del 10% | 1911 | R | [MODIFICADO] E735 = [EA008 * (E733/100)] / 1,1 |
| 160 | E736 | Error en el cálculo de la liquidación del IVA por ítem para forma de afectación Exonerado o Exento | 1912 | R | Si E731=2 o 3, E736 debe ser 0 |
| 161 | E736a | Error en el cálculo de la liquidación del IVA por ítem para forma de afectación Gravado IVA o Gravado Parcial | 1913 | R | E736 = E735 * (E734/100) |

### E9.5. Datos adicionales de uso comercial ([MODIFICADO] E820–E829) — Códigos 2050–2099

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 162 | [MODIFICADO] E822 | Fecha de inicio de ciclo es obligatorio | 2050 | R | Si se informa E811, E822 (E812) es obligatorio |
| 163 | [MODIFICADO] E822a | Fecha de inicio de ciclo no requerida | 2051 | R | Si NO existe E811, no informar E822 |
| 164 | [MODIFICADO] E823 | Fecha de fin de ciclo es obligatoria | 2052 | R | Si se informa E822 (E812), E823 (E813) es obligatorio |
| 165 | [MODIFICADO] E823a | Fecha de fin de ciclo no requerida | 2053 | R | Si NO existe E822, no informar E823 |
| 166 | [MODIFICADO] E823b | Fecha de fin de ciclo inválida | 2054 | R | E813 debe ser ≥ E812 |
| 167 | [MODIFICADO] E824 | Fecha de vencimiento del pago es retrasada | 2055 | R | La fecha de vencimiento del pago no debe ser anterior a D002 |

---

## E10. Campos de transporte de mercaderías (E900–E999) — Códigos 2100–2349

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 168 | E900 | Grupo de los campos que describen el transporte de las mercaderías es obligatorio | 2100 | R | Si C002=7 |
| 169 | E900a | Grupo de los campos que describen el transporte de las mercaderías no es permitido para el tipo de DE seleccionado | 2101 | R | No permitido si C002=4, 5, 6 o 8 |
| 170 | E901 | Tipo de transporte no informado | 2102 | R | Obligatorio si C002=7 |
| 171 | E902 | Descripción del tipo de transporte no corresponde al código | 2103 | R | |
| 172 | E904 | Descripción de la modalidad de transporte no corresponde al código | 2104 | R | |
| 173 | [MODIFICADO] E909 | Fecha estimada de inicio de traslado no informada | [MODIFICADO] 2107 | R | [MODIFICADO] Obligatorio si C002=7 |
| 174 | E909a | Fecha estimada de inicio de traslado es antigua | 2108 | R | Si se informa E909, debe ser posterior a la fecha de producción del SIFEN |
| 175 | [MODIFICADO] E910 | Fecha estimada de fin de traslado no informada | [MODIFICADO] 2109 | R | [MODIFICADO] Obligatorio si C002=7 |
| 176 | [MODIFICADO] E910a | Fecha estimada de fin de traslado es inválida | 2110 | R | E910 debe ser ≥ E909 |
| ~~186~~ | ~~E912~~ | ~~Descripción del país de destino no informada~~ | ~~2112~~ | ~~R~~ | ~~Eliminada en v150~~ |
| 177 | E912a | Descripción del país de destino no corresponde al código | 2113 | R | |
| 178 | E920 | Grupo de los campos que identifican el local de salida de las mercaderías es obligatorio | 2150 | R | Si C002=2 o 7 |
| 179 | E920a | Grupo de los campos que identifican el local de salida de las mercaderías no es permitido para el tipo de documento electrónico seleccionado | 2151 | R | No permitido si C002=3, 4, 5, 6 o 8 |
| 180 | [NUEVO] E925 | El Departamento, el Distrito y Ciudad del local de Salida no están relacionados | [NUEVO] 2153 | R | [NUEVO] |
| 181 | E926 | Descripción del departamento del local de salida no corresponde al código | 2152 | R | |
| ~~193~~ | ~~E928~~ | ~~Descripción del código de distrito del local de salida no informada~~ | ~~2154~~ | ~~R~~ | ~~Eliminada en v150~~ |
| 182 | E928a | Descripción del distrito del local de salida no corresponde al código | 2155 | R | |
| ~~159~~ | ~~E929~~ | ~~La ciudad del local de salida no corresponde al departamento seleccionado~~ | ~~2156~~ | ~~R~~ | ~~Eliminada en v150~~ |
| ~~160~~ | ~~E929a~~ | ~~La ciudad del local de salida no corresponde al distrito seleccionado~~ | ~~2157~~ | ~~R~~ | ~~Eliminada en v150~~ |
| 183 | E930 | Descripción de la ciudad del local de salida no corresponde al código | 2158 | R | |
| 184 | E940 | Grupo de los campos que identifican el local de entrega de las mercaderías es obligatorio | 2200 | R | Si C002=7 |
| 185 | E940a | Grupo de los campos que identifican el local de entrega de las mercaderías no es permitido para el tipo de documento electrónico seleccionado | 2201 | R | No permitido si C002=4, 5, 6 o 8 |
| 186 | [MODIFICADO] E945 | El Departamento, el Distrito y la Ciudad del local de entrega no están relacionados | 2203 | R | [MODIFICADO] |
| 187 | E946 | Descripción del departamento del local de entrega no corresponde al código | 2202 | R | |
| ~~201~~ | ~~E948~~ | ~~Descripción del código del distrito del local de la entrega no informada~~ | ~~2204~~ | ~~R~~ | ~~Eliminada en v150~~ |
| 188 | E948a | Descripción del distrito del local de entrega no corresponde al código | 2205 | R | |
| ~~168~~ | ~~E949~~ | ~~La ciudad del local de entrega no corresponde al departamento seleccionado~~ | ~~2206~~ | ~~R~~ | ~~Eliminada en v150~~ |
| ~~169~~ | ~~E949a~~ | ~~La ciudad del local de entrega no corresponde al distrito seleccionado~~ | ~~2207~~ | ~~R~~ | ~~Eliminada en v150~~ |
| 189 | E950 | Descripción de la ciudad del local de entrega no corresponde al código | 2208 | R | |
| 190 | E960 | Grupo de los campos que identifican el vehículo de traslado de las mercaderías es obligatorio | 2250 | R | Si C002=7 |
| 191 | E960a | Grupo de los campos que identifican el vehículo de traslado de las mercaderías no es permitido para el tipo de documento electrónico seleccionado | 2251 | R | No permitido si C002=4, 5, 6 o 8 |
| 192 | [NUEVO] E963 | Tipo de identificación del vehículo no informado | [NUEVO] 2255 | R | [NUEVO] Si E967=1, número de identificación del vehículo es requerido |
| 193 | [NUEVO] E965 | Número de matrícula del vehículo no informado | [NUEVO] 2254 | R | [NUEVO] Si E967=2, número de matrícula es requerido |
| 194 | [MODIFICADO] E966 | Número de vuelo no informado | 2252 | R | Si E903=3 (Aéreo) |
| 195 | [MODIFICADO] E966a | Número de vuelo no requerido | 2253 | R | Si E903≠3 |
| 196 | E980 | Grupo de los campos que identifican al transportista es obligatorio | 2300 | R | Si C002=7 |
| 197 | E980a | Grupo de los campos que identifican al transportista no es permitido para el tipo de documento electrónico seleccionado | 2301 | R | No permitido si C002=4, 5, 6 o 8 |
| 198 | E983 | RUC del transportista no informado | 2302 | R | Si E981=1 |
| 199 | E983a | RUC del transportista inexistente | 2303 | R | |
| 200 | E983b | El RUC del transportista se encuentra inactivo | 2304 | R | Estado distinto a CANCELADO/CANCELADO DEFINITIVO/SUSPENSIÓN TEMPORAL |
| 201 | E983c | RUC del transportista no requerido | 2305 | R | Si E981≠1 |
| 202 | E984 | Dígito Verificador del RUC del transportista incorrecto | 2306 | R | |
| 203 | E985 | Tipo de documento de identidad del transportista no informado | 2307 | R | Si E981=2 |
| 204 | E985a | Tipo de documento de identidad del transportista no requerido | 2308 | R | Si E981=1 |
| 205 | E986 | Descripción del tipo de documento de identidad del transportista no informada | 2309 | R | Si se informa E985, E986 es obligatorio |
| 206 | E986a | Descripción del tipo de documento de identidad del transportista no corresponde al código | 2310 | R | |
| 207 | E987 | Número de documento de identidad del transportista no informado | 2311 | R | Si se informa E985, E987 es requerido |
| 208 | E989 | Descripción de la nacionalidad del transportista no informada | 2312 | R | Si se informa E988, E989 es obligatorio |
| 209 | E989a | Descripción de la nacionalidad del transportista no corresponde al código | 2313 | R | |

---

## F. Subtotales y totales de la transacción (F001–F099) — Códigos 2350–2399

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 210 | F001 | Grupo de los campos que describen los subtotales y totales de la transacción documentada es obligatorio para el tipo de documento electrónico seleccionado | 2350 | R | Si C002≠7 |
| 211 | F001a | Grupo de los campos que describen los subtotales y totales de la transacción documentada no es permitido para el tipo de documento electrónico seleccionado | 2351 | R | Si C002=7 |
| 212 | F002 | Subtotal de operaciones exentas de IVA no informado | 2352 | R | Si E731=3, F002 debe existir |
| 213 | F002a | Cálculo del subtotal de la operación exenta incorrecto | 2353 | R | [MODIFICADO] = Suma de EA008 cuando E731=3 |
| 214 | F003 | Subtotal de operaciones exoneradas de IVA no informado | 2354 | R | Si E731=2, F003 debe existir |
| 215 | F003a | Cálculo del subtotal de la operación exonerada incorrecto | 2355 | R | [MODIFICADO] = Suma de EA008 cuando E731=2 |
| 216 | F004 | Subtotal de operaciones gravadas al 5% de IVA no informado | 2356 | R | Si E731=1 o 4 y E734=5 |
| 217 | F004a | Cálculo del subtotal de la operación gravada al 5% incorrecto | 2357 | R | [MODIFICADO] = Suma de EA008 cuando E734=5 |
| 218 | F005 | Subtotal de operaciones gravadas al 10% de IVA no informado | 2358 | R | Si E731=1 o 4 y E734=10 |
| 219 | F005a | Cálculo del subtotal de la operación gravada al 10% incorrecto | 2359 | R | [MODIFICADO] = Suma de EA008 cuando E734=10 |
| 220 | [MODIFICADO] F008 | Cálculo del total de la operación incorrecto | 2362 | R | [NUEVO] Si D013=1,3,4 o 5: = F002+F003+F004+F005. Si C002=4: = suma de EA008 |
| 221 | [MODIFICADO] F009 | Cálculo del total descuento por ítem incorrecto | 2363 | R | [MODIFICADO] = Suma de EA002 * E711 |
| 222 | [MODIFICADO] F011 | Cálculo del descuento sobre el total de la operación incorrecto | 2364 | R | [MODIFICADO] = Sumatoria de EA002 y EA004 de cada ítem |
| 223 | [MODIFICADO] F014 | Cálculo del total general de la operación incorrecto | 2365 | R | [MODIFICADO] Si C002=1,5 o 6: = F008–F011–F012–F013 |
| 224 | [MODIFICADO] F015 | Si se informan operaciones gravadas al 5%, es obligatorio reportar la liquidación del IVA de dichas operaciones | 2366 | R | [MODIFICADO] Si existe E736 y E734=5, F015 debe existir |
| 225 | [MODIFICADO] F015a | Cálculo de la liquidación del IVA a la tasa del 5% incorrecto | 2367 | R | = Suma de E736 cuando E734=5 |
| 226 | [MODIFICADO] F016 | Si se informan operaciones gravadas al 10%, es obligatorio reportar la liquidación del IVA de dichas operaciones | 2368 | R | [MODIFICADO] Si existe E736 y E734=10, F016 debe existir |
| 227 | [MODIFICADO] F016a | Cálculo de la liquidación del IVA a la tasa del 10% incorrecto | 2369 | R | = Suma de E736 cuando E734=10 |
| 228 | [MODIFICADO] F017 | Es obligatorio informar la liquidación total del IVA | 2370 | R | [MODIFICADO] Si existe F015 y/o F016 |
| 229 | [MODIFICADO] F017a | Cálculo de la liquidación total del IVA incorrecto | 2371 | R | [MODIFICADO] = F015 + F016 |
| 230 | [MODIFICADO] F018 | Si se informan operaciones gravadas al 5%, es obligatorio reportar el total de la base gravada de dichas operaciones | 2372 | R | [MODIFICADO] Si existe E735 y E734=5, F018 debe existir |
| 231 | [MODIFICADO] F018a | Cálculo total base gravada al 5% incorrecto | 2373 | R | = Suma de E735 cuando E734=5 |
| 232 | [MODIFICADO] F019 | Si se informan operaciones gravadas al 10%, es obligatorio reportar el total de la base gravada de dichas operaciones | 2374 | R | [MODIFICADO] Si existe E735 y E734=10, F019 debe existir |
| 233 | [MODIFICADO] F019a | Cálculo total base gravada al 10% incorrecto | 2375 | R | = Suma de E735 cuando E734=10 |
| 234 | [MODIFICADO] F020 | Es obligatorio informar el total de la base gravada de IVA | 2376 | R | [MODIFICADO] Si existe F018 y/o F019 |
| 235 | [MODIFICADO] F020a | Cálculo del total de la base gravada del IVA incorrecto | 2377 | R | [MODIFICADO] = F018 + F019 |
| 236 | [MODIFICADO] F023 | Si se informan operaciones con moneda extranjera, es obligatorio reportar el total general de la operación en guaraníes | 2382 | R | [MODIFICADO] Si D015≠PYG |
| 237 | [MODIFICADO] F023a | Cálculo del total general de la operación en guaraníes incorrecto para la condición del tipo de cambio global | 2385 | R | Si D015≠PYG y D017=1: [MODIFICADO] = F014 * D018 |
| 238 | [MODIFICADO] F023b | Cálculo del total general de la operación en guaraníes incorrecto para la condición del tipo de cambio por ítem | 2386 | R | Si D015≠PYG y D017=2: [MODIFICADO] = suma de EA009 |

---

## G1. Campos generales de la carga (G050–G099) — [NUEVO] Códigos 2390–2399

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 239 | [NUEVO] G050 | Grupo generales de la carga no es permitido para el tipo de documento electrónico seleccionado | [NUEVO] 2390 | R | [NUEVO] No permitido si C002≠1 y C002≠7 |

---

## H. Campos que identifican al documento asociado (H001–H049) — Códigos 2400–2449

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 240 | H001 | Documento asociado es obligatorio para el tipo de documento electrónico seleccionado | 2400 | R | [MODIFICADO] Obligatorio si C002=4, 5, 6 o 8 |
| 241 | [NUEVO] H001a | No informar el grupo de documento asociado | [NUEVO] 2414 | R | [NUEVO] Reglas de tipos de documentos asociados permitidos por tipo de DE |
| 242 | [NUEVO] H001b | Cantidad incorrecta de documento(s) asociado(s) | [NUEVO] 2415 | R | [NUEVO] Si C002=4, 5 o 6, solo se permite un grupo de documento asociado |
| 243 | [NUEVO] H002 | Tipo de documento asociado obligatorio para el tipo de documento electrónico | [NUEVO] 2416 | R | [NUEVO] Si C002=4 (Autofactura), el tipo de doc asociado debe ser constancia electrónica (H002=3) |
| 244 | [NUEVO] H002a | Tipo de documento asociado no requerido para el tipo de documento electrónico | [NUEVO] 2434 | R | [NUEVO] Si C002=1,5,6 o 7, H002 no puede ser constancia electrónica (H002≠3) |
| ~~247~~ | ~~H002c~~ | ~~CDC no requerido para el tipo de documento asociado~~ | ~~2419~~ | ~~R~~ | ~~Eliminada en v150~~ |
| ~~250~~ | ~~H002~~ | ~~CDC no informado~~ | ~~2416~~ | ~~R~~ | ~~Eliminada en v150~~ |
| 245 | H003 | Descripción del tipo de documento asociado no corresponde al código | 2401 | R | |
| 246 | H004 | Número de CDC del DTE referenciado no informado | 2402 | R | Si H002=1 (electrónico) |
| 247 | H004a | Número de CDC del DTE referenciado inexistente | 2403 | R | [MODIFICADO] |
| 248 | H004b | El CDC informado corresponde a un DTE cancelado | 2404 | R | |
| 249 | [NUEVO] H004c | Número de CDC no requerido para el tipo de documento asociado | [NUEVO] 2418 | R | [NUEVO] Si H002=2 o H002=3, no informar H004 |
| 250 | [NUEVO] H004d | Sumatoria de los documentos asociados supera el monto total del documento electrónico referenciado | [NUEVO] 2417 | R | [NUEVO] Suma de F014 de NCEs no puede superar F014 de la FE asociada |
| 251 | [NUEVO] H004e | Tipo de transacción de la FE asociada, es incorrecto | [NUEVO] 2437 | R | [NUEVO] Si C002=1 y documento asociado es otra FE (H004 inicia con 01), la FE asociada debe tener tipo de transacción Anticipo (D011=9) |
| 252 | [NUEVO] H004f | Moneda de la operación informada no coincidente con la moneda del documento asociado | [NUEVO] 2438 | R | [NUEVO] |
| 253 | H005 | Número de timbrado del documento impreso de referencia no informado | 2405 | R | Si H002=2 |
| 254 | [NUEVO] H005a | Número de timbrado no requerido para el tipo de documento asociado | [NUEVO] 2419 | R | [NUEVO] Si H002=1 o H002=3 |
| 255 | [NUEVO] H005b | Número de timbrado no corresponde al tipo de documento asociado | [NUEVO] 2440 | R | [NUEVO] Si H002=2, no informar timbrado electrónico |
| 256 | H006 | Código de establecimiento del documento impreso de referencia no informado | 2406 | R | Si H002=2 |
| 257 | [NUEVO] H006a | Código de establecimiento no requerido para el tipo de documento asociado | [NUEVO] 2420 | R | [NUEVO] Si H002=1 o H002=3 |
| 258 | H007 | Código de punto de expedición del documento impreso de referencia no informado | 2407 | R | Si H002=2 |
| 259 | [NUEVO] H007a | Código de punto de expedición no requerido para el tipo de documento asociado | [NUEVO] 2421 | R | [NUEVO] Si H002=1 o H002=3 |
| 260 | H008 | Número del documento impreso no informado | 2408 | R | Si H002=2 |
| 261 | [NUEVO] H008a | Número del documento no requerido para el tipo de documento asociado | [NUEVO] 2422 | R | [NUEVO] Si H002=1 o H002=3 |
| 262 | H009 | Tipo de documento impreso no informado | 2409 | R | Si H002=2 |
| 263 | [NUEVO] H009a | Tipo de documento impreso no requerido para el tipo de documento asociado | [NUEVO] 2423 | R | [NUEVO] Si H002=1 o H002=3 |
| 264 | H010 | Descripción del tipo de documento impreso no corresponde al código | 2410 | R | |
| 265 | [NUEVO] H010a | Descripción del tipo de documento impreso no informada | [NUEVO] 2424 | R | [NUEVO] Si se informa H009, H010 es obligatorio |
| 266 | [NUEVO] H010b | Descripción del tipo de documento impreso no requerida | [NUEVO] 2435 | R | [NUEVO] Si no se informa H009, no informar H010 |
| 267 | H011 | Fecha de emisión del documento impreso de referencia no informada | 2411 | R | Si H002=2 |
| 268 | [NUEVO] H011a | Fecha de emisión del documento impreso de referencia no requerida para el tipo de documento asociado | [NUEVO] 2425 | R | [NUEVO] Si H002=1 o H002=3 |
| ~~236~~ | ~~H012~~ | ~~Número de comprobante de retención no informado~~ | ~~2412~~ | ~~R~~ | ~~Eliminada en v150~~ |
| 269 | [NUEVO] H012a | Forma de pago incorrecto para el Número de comprobante de retención | [NUEVO] 2436 | R | [NUEVO] Si se informa H012, E606 debe ser 10 (Retención) |
| 270 | H013 | Número de resolución de crédito fiscal no informado | 2413 | R | Si D011=12 |
| 271 | [NUEVO] H014 | Tipo de constancia no informado | [NUEVO] 2426 | R | [NUEVO] Si H002=3 |
| 272 | [NUEVO] H014a | Tipo de constancia no requerido para el tipo de documento asociado | [NUEVO] 2427 | R | [NUEVO] Si H002=1 o H002=2 |
| 273 | [NUEVO] H015a | Descripción del tipo de constancia no corresponde al código | [NUEVO] 2429 | R | [NUEVO] |
| 274 | [NUEVO] H016 | Número de constancia no informado | [NUEVO] 2430 | R | [NUEVO] Si H002=3 y H014=2 |
| 275 | [NUEVO] H016a | Número de constancia no requerido para el tipo de documento asociado | [NUEVO] 2431 | R | [NUEVO] Si H002=1 o H002=2 |
| 276 | [NUEVO] H017 | Número de control de la constancia no informado | [NUEVO] 2432 | R | [NUEVO] Si H002=3 y H014=2 |
| 277 | [NUEVO] H017a | Número de control de la constancia no requerido para el tipo de documento asociado | [NUEVO] 2433 | R | [NUEVO] Si H002=1 o H002=2 |

---

## I. Información de la Firma Digital del DTE (I001–I049) — Código 2450

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 278 | I002 | Certificado digital no vigente al momento de firma del DE | 2450 | R | El certificado digital (I002) debe estar vigente (no revocado) al momento de la firma digital (A004) |

---

## J. Campos fuera de la Firma Digital (J001–J049) — Códigos 2500–2599

| N° | ID | Mensaje | Código | Tipo | Observación |
|----|-----|---------|--------|------|-------------|
| 279 | J002 | Cadena de caracteres correspondiente al código QR no es coincidente con el archivo XML | 2500 | R | |
| 280 | J002a | El hash del código QR incluido en la cadena de caracteres es inválido | 2501 | R | Hash del QR no corresponde al calculado con la cadena informada y el CSC en la base de datos de SIFEN |
| 281 | [MODIFICADO] J002b | URL de consulta de código QR es inválida | 2502 | R | [MODIFICADO] La URL del código QR informada en la cadena de caracteres (J002) no es correcta |
| 282 | J003 | Información adicional de interés para el emisor fue incluida en el DE | 2503 | R | El campo J003 fue incluido en el XML del DE — no debe enviarse al SIFEN |
