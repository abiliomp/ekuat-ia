# Códigos de Respuesta de Eventos

Reglas de validación y códigos de respuesta específicos para el procesamiento de eventos en SIFEN. Los eventos modifican o marcan el estado de un DE/DTE a lo largo de su ciclo de vida.

> **Fuente:** Manual Técnico SIFEN v150, sección 11.6

---

## Estados de validación de eventos

| Código | Descripción |
|--------|-------------|
| A | Aprobado |
| AO | Aprobado con Observación |
| R | Rechazado |

---

## 11.6.1 — Validaciones para el evento Cancelación (Códigos 4000–4049)

El emisor puede cancelar cualquier DTE dentro de los plazos establecidos.

| N° Val | ID | Mensaje de Validación | Código | Estado |
|--------|----|-----------------------|--------|--------|
| 1 | GDE005 | La versión no corresponde | 4000 | R |
| 2 | GEC002 | CDC inválido | 4001 | R |
| 3 | GEC002a | CDC no existente en el SIFEN | 4002 | R |
| 4 | GEC002b | CDC ya se encuentra con el mismo evento solicitado (duplicidad) | 4003 | R |
| 5 | GEC002c | CDC ya se ha confirmado por el receptor | 4004 | R |
| 7 | GDE008 | Firmador no autorizado para realizar evento | 4006 | R |
| 8 | GDE008a | Firma Digital inválida por certificado digital revocado | 4007 | R |
| 9 | GDE004 | Fecha de firma digital del evento inválida | 4008 | R |
| 6 | GDE004a | Plazo de solicitud de cancelación de una FE extemporáneo | 4009 | R |
| 7 | GDE004b | Plazo de solicitud de cancelación distinto a una FE es extemporáneo | 4010 | R |

**Plazos para la cancelación:**
- **Factura Electrónica (C002=1):** hasta 48 horas desde la aprobación del DTE.
- **AFE, NCE, NDE, NRE (C002=4,5,6,7):** hasta 168 horas desde la aprobación del DTE.
- El evento requiere el campo `mOtEve` (GEC003): motivo de la cancelación (texto libre, 5-500 caracteres).
- Si el DTE tiene otros DTEs asociados, se debe cancelar desde el último hasta el inicial.

---

## 11.6.2 — Validaciones para el evento Inutilización (Códigos 4050–4099)

El emisor inutiliza rangos de numeración de DE no utilizados.

| N° Val | ID | Mensaje de Validación | Código | Estado |
|--------|----|-----------------------|--------|--------|
| 9 | GEI002 | Número de timbrado inválido para el ambiente de pruebas | 4051 | R |
| 8 | GEI002a | Número de timbrado no corresponde al contribuyente facturador electrónico | 4052 | R |
| 10 | GEI002b | Número de timbrado no corresponde al medio de generación para factura electrónica | 4053 | R |
| 10 | GEI003 | Código de establecimiento inválido para el timbrado informado | 4054 | R |
| 11 | GEI004 | El código del punto de expedición es inválido para el timbrado informado | 4055 | R |
| 12 | GEI007 | Tipo de Documento no corresponde al Número de Timbrado autorizado | 4060 | R |
| 13 | GEI005 | Existe DTE en el rango informado | 4065 | R |
| 14 | GEI005a | Existe número inutilizado en el rango solicitado | 4066 | R |
| 15 | GEI006 | Cantidad de números en el rango es inválida (máximo 1000) | 4067 | R |
| 16 | GEI006a | Número final de rango es inválido (debe ser mayor que el inicio) | 4068 | R |
| 19 | GDE008 | Firmador no autorizado para realizar evento | 4069 | R |
| 20 | GDE008a | Firma Digital inválida por certificado digital revocado | 4070 | R |
| 21 | GDE004 | Fecha de firma digital del evento inválida | 4071 | R |

**Reglas para la inutilización:**
- Plazo: dentro de los primeros 15 días del mes siguiente al hecho, y hasta la fecha límite de validez del timbrado.
- Máximo 1000 números secuenciales por evento.
- El número debe no existir como DE aprobado en SIFEN.
- Requiere el campo `mOtEve` (GEI008): motivo (texto libre, 5-500 caracteres).

---

## 11.6.3 — Validaciones para Notificación – Recepción DE/DTE (Códigos 4100–4113)

El receptor notifica que recibió el documento sin poder manifestarse de forma conclusiva aún.

| N° Val | ID | Mensaje de Validación | Código | Estado |
|--------|----|-----------------------|--------|--------|
| 1 | GEN001 | Incongruencia en el registro de eventos del receptor (hay evento previo de conformidad, disconformidad o desconocimiento) | 4113 | R |
| 2 | GEN002b | CDC del DTE ya cuenta con un evento de esta naturaleza | 4101 | R |
| 3 | GEN002c | CDC del DTE inválido | 4102 | R |
| 4 | GEN003 | Fecha de emisión del DE/DTE ha superado el plazo para registro del evento (45 días) | 4103 | AO |
| 5 | GEN004 | Fecha de Recepción debe ser mayor o igual a la fecha de emisión del DE/DTE | 4104 | R |
| 6 | GEN007 | RUC del Receptor requerido | 4105 | R |
| 7 | GEN007a | RUC del Receptor no se debe informar | 4106 | R |
| 8 | GEN008 | Dígito verificador del RUC del contribuyente receptor requerido | 4107 | R |
| 9 | GEN008a | Dígito verificador del RUC del contribuyente receptor no se debe informar | 4108 | R |
| 10 | GEN009 | Tipo de documento de identidad del receptor requerido | 4109 | R |
| 11 | GEN009a | Tipo de documento de identidad del receptor no se debe informar | 4110 | R |
| 12 | GEN010 | Número de documento de identidad requerido | 4111 | R |
| 13 | GEN010a | Número de documento de identidad no se debe informar | 4112 | R |

**Plazo:** hasta 45 días desde la fecha de emisión del DE/DTE.
**Restricción:** solo se puede registrar un evento de notificación por CDC.

---

## 11.6.4 — Validaciones para el evento Conformidad (Códigos 4150–4156)

El receptor confirma que el DTE es correcto y ha recibido la mercadería o servicio.

| N° Val | ID | Mensaje de Validación | Código | Estado |
|--------|----|-----------------------|--------|--------|
| 14 | GCO001 | Incongruencia en el registro de eventos del receptor (hay un evento previo de desconocimiento) | 4156 | R |
| 15 | GCO002 | CDC del DTE ya cuenta con dos eventos de la misma naturaleza | 4150 | R |
| 16 | GCO002b | CDC del DTE inválido | 4151 | R |
| 17 | GCO002c | CDC del DTE es inexistente o ha superado el plazo para registro del evento | 4152 | R |
| 18 | GCO002e | No se puede registrar la confirmación por CDC del DTE cancelado o ajustado en su totalidad por nota de crédito | 4155 | R |
| 19 | GCO004 | Fecha estimada de Recepción requerida (cuando conformidad parcial) | 4154 | R |

**Tipos de conformidad (GCO003):**
- 1 = Conformidad Total del DTE
- 2 = Conformidad Parcial del DTE (mercadería se entregará en fecha posterior)

**Plazos:**
- Primer evento de conformidad: hasta 45 días desde la fecha de emisión del DTE.
- Evento de corrección (luego de disconformidad): hasta 15 días desde el evento de disconformidad.
- Se permiten hasta 2 eventos de conformidad (parcial y luego total).

---

## 11.6.5 — Validaciones para el evento Disconformidad (Códigos 4200–4205)

El receptor indica que el DTE tiene errores o inconsistencias.

| N° Val | ID | Mensaje de Validación | Código | Estado |
|--------|----|-----------------------|--------|--------|
| 20 | GDI001 | Incongruencia en el registro de eventos del receptor (hay un evento previo de desconocimiento) | 4205 | R |
| 21 | GDI002 | CDC del DTE ya cuenta con un evento de esta naturaleza | 4200 | R |
| 22 | GDI002b | CDC del DTE inválido | 4201 | R |
| 23 | GDI002c | CDC inexistente o ha superado el plazo para registro del evento | 4202 | R |
| 24 | GDI002e | No se puede registrar la disconformidad por CDC del DTE cancelado | 4204 | R |

**Plazos:**
- Primer evento de disconformidad: hasta 45 días desde la fecha de emisión del DTE.
- Evento de corrección (luego de conformidad): hasta 15 días desde el evento de conformidad.
- Se permite solo un evento de disconformidad por CDC.

---

## 11.6.6 — Validaciones para el evento Desconocimiento DE/DTE (Códigos 4250–4262)

El receptor declara que desconoce el documento emitido a su nombre.

| N° Val | ID | Resultado de la Validación | Código | Estado |
|--------|----|-----------------------------|--------|--------|
| 25 | GED002b | CDC del DTE ya cuenta con un evento de esta naturaleza | 4251 | R |
| 26 | GED002c | CDC del DTE inválido | 4252 | R |
| 27 | GED003 | Fecha de emisión del DE/DTE ha superado el plazo para registro del evento | 4253 | AO |
| 28 | GED004 | Fecha de Recepción debe ser mayor a la fecha de emisión del DE/DTE | 4254 | R |
| 29 | GED007 | RUC del Receptor requerido | 4255 | R |
| 30 | GEN007a | RUC del Receptor no se debe informar | 4256 | R |
| 31 | GED008 | Dígito verificador del RUC del contribuyente receptor requerido | 4257 | R |
| 32 | GEN008a | Dígito verificador del RUC del contribuyente receptor no se debe informar | 4258 | R |
| 33 | GED009 | Tipo de documento de identidad del receptor requerido | 4259 | R |
| 34 | GED009a | Tipo de documento de identidad del receptor no se debe informar | 4260 | R |
| 35 | GED010 | Número de documento de identidad requerido | 4261 | R |
| 36 | GED10a | Número de documento de identidad no se debe informar | 4262 | R |

**Plazo:** hasta 45 días desde la fecha de emisión del DE/DTE.
**Característica:** El desconocimiento es un evento informativo; no invalida el DTE sino que lo marca en el SIFEN.

---

## 11.6.7 — Validaciones para el evento por Actualización de Datos del Transporte (Códigos 4300–4323)

| N° Val | ID | Mensaje de Validación | Código | Estado |
|--------|----|-----------------------|--------|--------|
| 1 | GET004 | El Departamento, el Distrito y la Ciudad del local de entrega no están relacionados | 4300 | R |
| 2 | GET004a | Código del departamento del local de entrega requerido para Cambio del local de la entrega | 4301 | R |
| 7 | GET008 | Código de la ciudad del local de la entrega requerido para Cambio del local de la entrega | 4306 | R |
| 10 | GET010 | Dirección del local de la entrega requerida para el motivo Cambio del local de la entrega | 4309 | R |
| 12 | GET013 | Nombre y apellido del chofer requerido para el motivo Cambio del chofer | 4311 | R |
| 14 | GET015 | Naturaleza del transportista requerida para el motivo Cambio del transportista | 4313 | R |
| 15 | GET016 | RUC del transportista no informado | 4314 | R |
| 16 | GET016a | RUC del transportista inexistente | 4315 | R |
| 32 | GET026 | Tipo de vehículo requerido para el motivo Cambio de vehículo | 4319 | R |
| 33 | GET027 | Marca del vehículo requerida para el motivo Cambio de vehículo | 4320 | R |
| 34 | GET028 | Tipo de identificación del vehículo requerido para el motivo Cambio de vehículo | 4321 | R |

**Motivos del evento de transporte (GET003):**
- 1 = Cambio del local de la entrega
- 2 = Cambio del chofer
- 3 = Cambio del transportista
- 4 = Cambio de vehículo

---

## Resumen de plazos por evento

| Evento | Actor | Plazo |
|--------|-------|-------|
| Cancelación (FE) | Emisor | 48 horas desde aprobación |
| Cancelación (AFE, NCE, NDE, NRE) | Emisor | 168 horas desde aprobación |
| Inutilización | Emisor | Hasta el día 15 del mes siguiente al hecho |
| Notificación de recepción | Receptor | 45 días desde la fecha de emisión |
| Conformidad | Receptor | 45 días desde la fecha de emisión (o 15 días desde disconformidad) |
| Disconformidad | Receptor | 45 días desde la fecha de emisión (o 15 días desde conformidad) |
| Desconocimiento | Receptor | 45 días desde la fecha de emisión |
| Corrección de evento del receptor | Receptor | 15 días desde el primer evento |
