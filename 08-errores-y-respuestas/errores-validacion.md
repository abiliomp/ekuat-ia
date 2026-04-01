# Errores de Validación del DE

Códigos de validación del formato del Documento Electrónico (sección 12.4 del MT). Las validaciones verifican que los campos del XML cumplan con las normas establecidas.

**Estados:** A=Aprobado, AO=Aprobado con Observación, R=Rechazado

> **Fuente:** Manual Técnico SIFEN v150, sección 12.4

---

## A. Campos firmados del Documento Electrónico (A001-A099) — Códigos 1000–1049

| N° Val | ID | Mensaje de Validación | Código | Estado |
|--------|----|-----------------------|--------|--------|
| 1 | A002 | CDC no correspondiente con las informaciones del XML | 1000 | R |
| 2 | A002a | CDC duplicado | 1001 | R |
| 3 | A002b | Documento electrónico duplicado | 1002 | R |
| 4 | A003 | DV del CDC inválido | 1003 | R |
| 5 | A004a | La fecha y hora de la firma digital es adelantada | 1004 | R |
| 6 | A004b | Transmisión extemporánea del DE | 1005 | AO |

**Observaciones:**
- A002: El CDC debe ser compatible con C002, D101, D102, C005, C006, C007, D103, D002, B002, B004, A003.
- A002b: Duplicidad verificada por coincidencia de Tipo de documento, Timbrado, Número de documento, Tipo de emisión, Establecimiento, Punto de Expedición y Serie.
- A004b: La transmisión extemporánea genera Aprobado con Observación (AO). La SET puede aplicar sanción.

---

## B. Campos inherentes a la operación de DE (B001-B099) — Códigos 1050–1099

| N° Val | ID | Mensaje de Validación | Código | Estado |
|--------|----|-----------------------|--------|--------|
| 7 | B002 | Tipo de emisión inválido en esta etapa | 1050 | R |
| 8 | B003 | Descripción del tipo de emisión no corresponde al código | 1051 | R |

**Observación:** El tipo de emisión en contingencia (B002=2) no está permitido en la etapa actual.

---

## C. Campos de datos del Timbrado (C001-C099) — Códigos 1100–1149

| N° Val | ID | Mensaje de Validación | Código | Estado |
|--------|----|-----------------------|--------|--------|
| 9 | C003 | Descripción del tipo de documento electrónico no corresponde al código | 1100 | R |
| 10 | C004 | Número de timbrado inválido | 1101 | R |
| 11 | C004a | Número de timbrado no corresponde al medio de generación para facturación electrónica | 1102 | R |
| 12 | C004b | El número de timbrado no se encuentra vigente a la fecha de emisión del comprobante | 1103 | R |
| 13 | C004c | El número de timbrado informado no se encuentra en estado ACTIVO | 1104 | R |
| 14 | C005 | Código de establecimiento incorrecto | 1105 | R |
| 15 | C006 | Código de punto de expedición incorrecto | 1106 | R |
| 17 | C008 | Fecha de inicio de vigencia del timbrado incorrecta | 1107 | R |
| 18 | C009 | Fecha fin de vigencia del timbrado incorrecta | 1108 | R |
| 16 | C007 | Número de documento ha sido inutilizado anteriormente | 1109 | R |
| 18 | C010 | Serie informada incorrecta | 1110 | R |

---

## D. Datos generales del DE (D001-D299) — Códigos 1150–1349

### D. Fecha y datos generales (D002)

| N° Val | ID | Mensaje de Validación | Código | Estado |
|--------|----|-----------------------|--------|--------|
| 19 | D002 | La fecha y hora de emisión del DE informada es inválida por retraso | 1150 | R |
| 20 | D002f | La fecha y hora de emisión del DE informada es inválida por envío adelantado | 1151 | R |
| 21 | D002a | Fecha y hora de emisión del DE es anterior a la fecha de lanzamiento del sistema | 1156 | R |

**Límites técnicos:**
- Fecha de emisión atrasada: máximo 720 horas (30 días) antes de la transmisión.
- Fecha de emisión adelantada: máximo 120 horas (5 días) antes de la transmisión.
- Fecha mínima: 22 de noviembre de 2018.

### D1. Operación comercial (D010-D099)

| N° Val | ID | Mensaje de Validación | Código | Estado |
|--------|----|-----------------------|--------|--------|
| 22 | D010 | Grupo de informaciones inherentes a la operación comercial es obligatorio | 1200 | R |
| 23 | D010a | Grupo de informaciones inherentes a la operación comercial no es permitido para NRE | 1201 | R |
| 24 | D011 | Tipo de transacción no informado para el documento electrónico seleccionado | 1202 | R |
| 25 | D012 | Descripción del tipo de transacción no corresponde al código | 1203 | R |
| 28 | D013 | Tipo de impuesto afectado no informado | 1204 | R |
| 26 | D014 | La descripción del tipo de impuesto afectado no corresponde al código | 1205 | R |
| 27 | D016 | Descripción de la moneda de la operación no corresponde al código | 1206 | R |
| 28 | D017 | Condición del tipo de cambio no informada | 1207 | R |
| 29 | D017a | Condición del tipo de cambio no requerida | 1208 | R |
| 30 | D018 | Tipo de cambio de la operación no informado | 1209 | R |
| 31 | D018a | Tipo de cambio de la operación no requerido | 1210 | R |
| 32 | D020 | Descripción de la condición del anticipo no corresponde al código | 1211 | R |

### D2. Emisor (D100-D129)

| N° Val | ID | Mensaje de Validación | Código | Estado |
|--------|----|-----------------------|--------|--------|
| 33 | D101 | RUC del emisor inexistente | 1250 | R |
| 34 | D101a | RUC del Emisor inhabilitado para facturación electrónica | 1251 | R |
| 35 | D101b | El RUC del emisor se encuentra inactivo | 1252 | R |
| 36 | D101c | RUC del emisor no está habilitado para utilizar este tipo de servicio | 1264 | R |
| 37 | D102 | Dígito Verificador del RUC del emisor incorrecto | 1253 | R |
| 38 | D105 | Nombre o razón social del emisor del DE inválido | 1263 | R |
| 39 | D111 | El Departamento, el Distrito y la Ciudad de emisión no están relacionados | 1255 | R |
| 40 | D112 | Descripción del departamento de emisión no corresponde al código | 1254 | R |
| 43 | D115 | La ciudad de emisión no corresponde al departamento seleccionado | 1258 | R |
| 42 | D116 | Descripción de la ciudad de emisión no corresponde al código | 1260 | R |

### D2.1. Actividad económica del emisor

| N° Val | ID | Mensaje de Validación | Código | Estado |
|--------|----|-----------------------|--------|--------|
| 43 | D131 | Código de actividad económica incorrecto | 1261 | R |
| 44 | D132 | Descripción de la actividad económica no corresponde al código | 1262 | R |

### D3. Receptor (D200-D299)

| N° Val | ID | Mensaje de Validación | Código | Estado |
|--------|----|-----------------------|--------|--------|
| 45 | D201 | Naturaleza del Receptor inválida para el tipo documento electrónico | 1315 | R |
| 46 | D202 | El tipo de operación no compatible con la naturaleza del receptor | 1300 | R |
| 47 | D202a | El tipo de operación no compatible con el tipo documento electrónico | 1316 | R |
| 48 | D203 | Código de país del receptor inválido para el tipo de operación | 1320 | R |
| 49 | D204 | Descripción del país receptor no corresponde al código | 1301 | R |
| 50 | D205 | Es obligatorio informar el tipo de contribuyente receptor contribuyente | 1302 | R |
| 51 | D205a | Tipo de contribuyente receptor inválido | 1303 | R |
| 52 | D206 | Es obligatorio informar el RUC del receptor contribuyente | 1304 | R |
| 53 | D206a | RUC del receptor no requerido | 1305 | R |
| 54 | D206b | RUC del receptor inexistente en la base de datos de Marangatu | 1306 | R |
| 57 | D206e | RUC del Receptor inválido para el tipo de documento electrónico (AFE) | 1317 | R |
| 58 | D207 | Dígito Verificador del RUC del receptor incorrecto | 1309 | R |
| 59 | D208 | Es obligatorio informar el tipo de documento de identidad del receptor | 1310 | R |
| 60 | D208a | Tipo de documento de identidad del receptor inválido | 1311 | R |
| 61 | D208b | Tipo de documento de identidad del receptor incorrecto para el tipo de operación | 1319 | R |
| 62 | D208c | Tipo de documento de identidad del receptor incorrecto para el total general de la operación | 1321 | R |

---

## E. Ítems de la Operación (E700-E899) — Códigos 1800–1999

### E8. Ítems (E704-E717)

| N° Val | ID | Mensaje de Validación | Código | Estado |
|--------|----|-----------------------|--------|--------|
| - | E704 | Código DNCP – Nivel General requerido para B2G | 1800+ | R |

### E8.2. IVA por ítem (E730-E739)

| N° Val | ID | Mensaje de Validación | Código | Estado |
|--------|----|-----------------------|--------|--------|
| - | E730 | Campos de IVA obligatorios según D013 | 1900+ | R |

---

## H. Campos que identifican al documento asociado (H001-H049) — Códigos 2400–2449

Validaciones sobre los documentos asociados (NCE/NDE vinculadas a FE). Rango de códigos 2400 a 2449.

---

## Notas sobre la guía de reglas de validación

- **N° VAL**: cantidad de reglas de validación.
- **ID**: identificación del campo del DE que origina la validación.
- **Código**: número de 4 dígitos de la respuesta.
- **E**: estado de la validación (A/AO/R).
- Solo se reporta el **primer error** detectado en caso de rechazo.
- En caso de aprobación con observaciones (AO), se pueden reportar hasta 100 mensajes.
