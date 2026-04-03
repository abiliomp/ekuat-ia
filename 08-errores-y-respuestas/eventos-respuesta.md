> **Fuente:** Manual Técnico SIFEN v150, sección 11 (Gestión de Eventos)
> **Nota:** Contenido tachado (~~así~~) indica especificaciones eliminadas en v150. [MODIFICADO] indica cambios. [NUEVO] indica adiciones en v150.

# Gestión de Eventos — Estructura, Tipos y Reglas de Validación

[MODIFICADO] Entiéndase por evento toda ocurrencia o suceso registrado en SIFEN por el cual se asigna una marca o modifica el estado de un DE o DTE.

Los eventos pueden ser de **registro requerido** (solicitados por el emisor o el receptor) o de **registro automático** (generados por SIFEN o por interoperabilidad con otros sistemas de la SET).

Los eventos deben ser estructurados en un archivo XML firmado digitalmente y [MODIFICADO] transmitidos a través del WS siRecepEvento. [MODIFICADO] Los eventos deberán ser enviados en lotes de hasta 15 eventos de cualquier tipo (emisor y/o receptor).

---

## Tabla J — Resumen de los eventos de SIFEN según los actores

| N° | Evento | Actor | Tipo | Plazo | Alcance DE | Criterios principales | Acceso |
|----|--------|-------|------|-------|------------|----------------------|--------|
| 1 | Cancelación del DTE | Emisor | Registro Requerido — [NUEVO] Evento conclusivo | [MODIFICADO] Hasta 48 hs desde la aprobación del DTE cuando es FE. [NUEVO] Hasta 168 hs cuando el documento es NCE, NDE, NRE o AFE (distinto a FE) | Todos los DTE | [MODIFICADO] DTE en SIFEN con situación Aprobado o Aprobado con observación; se requiere justificativa (campo texto libre); [NUEVO] para cancelar un DTE con otros DTE asociados, se debe cancelar el último hasta llegar al inicial | WS |
| 2 | Inutilización del número de DE | Emisor | Registro Requerido — [NUEVO] Evento conclusivo | [MODIFICADO] Dentro de los 15 primeros días del mes siguiente al acaecimiento del hecho; y hasta fecha límite de validez del timbrado | Todos los DE | Número del DE en el rango de inutilización no existe en SIFEN; inutilización por rango de hasta 1.000 números; se requiere justificativa | WS |
| 10 | [MODIFICADO] Notificación de recepción DE o DTE | Receptor | Registro Requerido — [NUEVO] Evento informativo | [MODIFICADO] Hasta 45 días contados desde la fecha de emisión | [MODIFICADO] Todos los DE o DTE | [MODIFICADO] DTE o DE recepcionado | WS/Portal |
| 11 | [MODIFICADO] Conformidad DTE | Receptor | Registro Requerido — [NUEVO] Evento conclusivo | [MODIFICADO] Hasta 45 días contados desde la fecha de emisión | Todos los DTE | DTE en SIFEN | WS/Portal |
| 12 | [MODIFICADO] Disconformidad DTE | Receptor | Registro Requerido — [NUEVO] Evento conclusivo | [MODIFICADO] Hasta 45 días contados desde la fecha de emisión | Todos los DTE | DTE en SIFEN | WS/Portal |
| 13 | [MODIFICADO] Desconocimiento DE o DTE | Receptor | Registro Requerido — [NUEVO] Evento informativo | [MODIFICADO] Hasta 45 días contados desde la fecha de emisión | [MODIFICADO] Todos los DE o DTE | [MODIFICADO] DTE o DE recepcionado | WS/Portal |
| 14 | [MODIFICADO] Devolución y Ajuste de precios | SIFEN | Registro Automático | Plazo límite definido por la SET; [MODIFICADO] plazo de prescripción | FE | Emisión de una NCE o NDE [MODIFICADO] (asociación) para una FE aprobada en SIFEN | Automático |
| 16 | Asociación | SIFEN | Registro Automático | Inmediato a la aprobación en SIFEN | [MODIFICADO] Todos los DE, otros documentos emitidos por otra modalidad de facturación e interoperabilidad con sistemas de la SET | DTE asociado aprobado o aprobado con observaciones en SIFEN, o cuando el SIFEN reciba informaciones de Marangatu o Tesaka | Automático |

### [NUEVO] Tabla K — Correcciones de eventos del Receptor

| N° | Corrección | Actor | Tipo | Plazo | Alcance DE | Criterios | Condición |
|----|-----------|-------|------|-------|------------|-----------|-----------|
| [NUEVO] 1 | [NUEVO] Conformidad – Disconformidad – Desconocimiento DE o DTE | [NUEVO] Receptor | [NUEVO] Registro Requerido | [NUEVO] Hasta 15 días del registro del primer evento | [NUEVO] Todos los DE o DTE | [NUEVO] DTE en SIFEN con situación Aprobado o Aprobado Extemporáneo; se requiere justificativa | [NUEVO] Solo se puede registrar un evento de corrección sobre cada evento; selección de evento del receptor por equivocación |

### Tipología de eventos del receptor [NUEVO]

- **Eventos conclusivos** (conformidad y disconformidad): corresponden a eventos que generan una acción del emisor. Solo se realizan sobre DTE.
- **Eventos informativos** (desconocimiento y notificación de recepción): colocan una marca a un DTE o registran la recepción de un DE. Pueden realizarse sobre DTE y DE. No generan acción del emisor.
- **Eventos automáticos**: generados por SIFEN, se devuelven como parte de la consulta de un DTE.

---

## Estructura de los Eventos — Campos comunes (GDE)

Todos los eventos comparten la estructura raíz del contenedor de eventos:

| Grupo | ID | Campo | Descripción | Longitud | Ocurrencia | Observaciones |
|-------|----|-------|-------------|----------|------------|---------------|
| GDE | GDE000 | gGroupGesEve | Raíz del grupo de eventos | — | 1-1 | |
| GDE | GDE001 | rGesEve | Raíz de Gestión de Eventos | — | 1-15 | Elemento raíz |
| GDE | GDE002 | rEve | Grupos de campos generales del evento | — | 1-1 | Campos incluidos en la firma digital |
| GDE | GDE003 | Id | Identificador del evento | 1-10 (N) | 1-1 | Atributo del campo GDE002 |
| GDE | GDE004 | dFecFirma | Fecha y Hora del firmado | 19 (F) | 1-1 | Formato AAAA-MM-DDThh:mm:ss |
| GDE | GDE005 | dVerFor | Versión del formato | 3 (N) | 1-1 | Control de versiones |
| ~~GDE~~ | ~~GDE006~~ | ~~dTiGDE~~ | ~~Tipo de Evento~~ | ~~1-2 (N)~~ | ~~1-1~~ | ~~Eliminado en v150~~ |
| GDE | GDE007 | gGroupTiEvt | Grupo de campos del tipo de evento | — | 1-1 | Grupo correspondiente al evento según tipo |
| GDE | GDE008 | Signature | Grupo de la Firma Digital | — | 1-1 | [MODIFICADO] Firma Digital del campo rEve (GDE001) |

---

## 11.5.1 – Formato de Eventos del Emisor

### Evento Cancelación (GEC)

| Grupo | ID | Campo | Descripción | Tipo | Longitud | Ocurrencia | Observaciones |
|-------|----|-------|-------------|------|----------|------------|---------------|
| GDE | GEC001 | rGeVeCan | Raíz Gestión de Eventos Cancelación | G | — | — | [MODIFICADO] Nodo padre: GDE007 |
| GDE | GEC002 | Id | Identificador del DTE | A | 44 | 1-1 | Se informa el código de control (CDC) |
| GDE | GEC003 | mOtEve | Motivo del Evento | A | [MODIFICADO] 5-500 | 1-1 | Campo abierto |

### Evento Inutilización (GEI)

| Grupo | ID | Campo | Descripción | Tipo | Longitud | Ocurrencia | Observaciones |
|-------|----|-------|-------------|------|----------|------------|---------------|
| GDE | GEI001 | rGeVeInu | Raíz Gestión de Eventos Inutilización | G | — | — | [MODIFICADO] Nodo padre: GDE007 |
| GDE | GEI002 | dNumTim | Número del Timbrado | N | 8 | 1-1 | |
| GDE | GEI003 | dEst | Establecimiento | A | 3 | 1-1 | Completar con ceros a la izquierda |
| GDE | GEI004 | dPunExp | Punto de expedición | A | 3 | 1-1 | Completar con ceros a la izquierda |
| GDE | GEI005 | dNumIn | Número Inicio del rango | A | 7 | 1-1 | Cantidad máxima para inutilización: rango de hasta 1.000 números. Completar con ceros a la izquierda |
| GDE | GEI006 | dNumFin | Número Final del rango | A | 7 | 1-1 | Completar con ceros a la izquierda |
| GDE | GEI007 | iTiDE | Tipo de Documento Electrónico | N | 1-2 | 1-1 | 1=FE, 2=FEE, 3=FEI, 4=AFE, 5=NCE, 6=NDE, 7=NRE, 8=CRE |
| GDE | GEI008 | mOtEve | Motivo del Evento | A | [MODIFICADO] 5-500 | 1-1 | Campo libre |

---

## 11.5.2 – [NUEVO] Formato de Eventos del Receptor

### [NUEVO] Evento Notificación – Recepción DE/DTE (GEN)

| Grupo | ID | Campo | Descripción | Tipo | Longitud | Ocurrencia | Observaciones |
|-------|----|-------|-------------|------|----------|------------|---------------|
| GER | GEN001 | rGeVeNotRec | Raíz Gestión de Eventos Notificación – Recepción | G | — | — | Nodo padre: GDE007 |
| GER | GEN002 | Id | Identificador del DE/DTE | A | 44 | 1-1 | Se informa el CDC del DE/DTE |
| GER | GEN003 | dFecEmi | Fecha de emisión del DE/DTE | F | 19 | 1-1 | Requerido para conteo del plazo (hasta 45 días desde emisión). Formato AAAA-MM-DDThh:mm:ss |
| GER | GEN004 | dFecRecep | Fecha Recepción DE | F | 19 | 1-1 | Fecha en que el receptor recibió física o electrónicamente el DE. Formato AAAA-MM-DDThh:mm:ss |
| GER | GEN005 | iTipRec | Tipo de Receptor | N | 1 | 1-1 | 1=Contribuyente; 2=No Contribuyente |
| GER | GEN006 | dNomRec | Nombre o Razón Social del Receptor del DE/DTE | A | 4-60 | 1-1 | |
| GER | GEN007 | dRucRec | RUC del Receptor | A | 3-8 | 0-1 | Requerido si GEN005=1; no informar si GEN005=2 |
| GER | GEN008 | dDVRec | Dígito verificador del RUC del contribuyente receptor | N | 1 | 0-1 | Requerido si GEN005=1; no informar si GEN005=2 |
| GER | GEN009 | dTipIDRec | Tipo de documento de identidad del receptor | N | 1 | 0-1 | No informar si GEN005=1. Requerido si GEN005=2. 1=Cédula paraguaya; 2=Pasaporte; 3=Cédula extranjera; 4=Carnet de residencia |
| GER | GEN010 | dNumID | Número de documento de identidad | A | 1-20 | 0-1 | No informar si GEN005=1. Requerido si GEN005=2 |
| [NUEVO] GER | [NUEVO] GEN011 | [NUEVO] dTotalGs | [NUEVO] Total general de la operación en Guaraníes | N | 1-15p(0-8) | 1-1 | |

### [NUEVO] Evento Conformidad (GCO)

| Grupo | ID | Campo | Descripción | Tipo | Longitud | Ocurrencia | Observaciones |
|-------|----|-------|-------------|------|----------|------------|---------------|
| GER | GCO001 | rGeVeConf | Raíz Gestión de Eventos Conformidad | G | — | — | Nodo padre: GDE007 |
| GER | GCO002 | Id | CDC del DTE | A | 44 | 1-1 | Corresponde al CDC de un DTE |
| GER | GCO003 | iTipConf | Tipo de Conformidad | N | 1 | 1-1 | 1=Conformidad Total del DTE; 2=Conformidad Parcial del DTE (mercadería a entregar en fecha posterior a la recepción del DE/DTE) |
| GER | GCO004 | dFecRecep | Fecha Estimada de Recepción | F | 19 | 0-1 | Obligatorio si GCO003=2 (Conformidad Parcial) |

### [NUEVO] Evento Disconformidad (GDI)

| Grupo | ID | Campo | Descripción | Tipo | Longitud | Ocurrencia | Observaciones |
|-------|----|-------|-------------|------|----------|------------|---------------|
| GER | GDI001 | rGeVeDisconf | Raíz Gestión de Eventos Disconformidad | G | — | — | Nodo padre: GDE007 |
| GER | GDI002 | Id | CDC del DTE | N | 44 | 1-1 | Corresponde al CDC de un DTE |
| GER | GDI004 | mOtEve | Motivo del Evento | A | 5-500 | 1-1 | |

### [NUEVO] Evento Desconocimiento DE/DTE (GED)

| Grupo | ID | Campo | Descripción | Tipo | Longitud | Ocurrencia | Observaciones |
|-------|----|-------|-------------|------|----------|------------|---------------|
| GER | GED001 | rGeVeDescon | Raíz Gestión de Eventos Desconocimiento | G | — | — | Nodo padre: GDE007 |
| GER | GED002 | Id | CDC del DE/DTE | A | 44 | 1-1 | Corresponde al CDC de un KuDE o CDC de un DTE |
| GER | GED003 | dFecEmi | Fecha de emisión del DE/DTE | F | 19 | 1-1 | Requerido para conteo del plazo (hasta 45 días desde emisión). Formato AAAA-MM-DDThh:mm:ss |
| GER | GED004 | dFecRecep | Fecha Recepción DE | F | 19 | 1-1 | Formato AAAA-MM-DDThh:mm:ss |
| GER | GED005 | iTipRec | Tipo de Receptor | N | 1 | 1-1 | 1=Contribuyente; 2=No Contribuyente |
| GER | GED006 | dNomRec | Nombre o Razón Social del Receptor | A | 4-60 | 1-1 | |
| GER | GED007 | dRucRec | RUC del Receptor | A | 3-8 | 0-1 | Requerido si GED005=1; no informar si GED005=2 |
| GER | GED008 | dDVRec | Dígito verificador del RUC receptor | N | 1 | 0-1 | Requerido si GED005=1; no informar si GED005=2 |
| GER | GED009 | dTipIDRec | Tipo de documento de identidad del receptor | N | 1 | 0-1 | No informar si GED005=1. Requerido si GED005=2. 1=Cédula paraguaya; 2=Pasaporte; 3=Cédula extranjera; 4=Carnet de residencia |
| GER | GED010 | dNumID | Número de documento de identidad | A | 1-20 | 0-1 | No informar si GED005=1. Requerido si GED005=2 |
| GER | GED011 | mOtEve | Motivo del Evento | A | 5-500 | 1-1 | |

---

## Eventos automáticos por interoperabilidad

### [NUEVO] Evento asociación Retención (GER)

| Grupo | ID | Campo | Descripción | Tipo | Longitud | Ocurrencia |
|-------|----|-------|-------------|------|----------|------------|
| GEA | GER001 | rGeVeRetAce | Raíz Gestión de Eventos de retención | G | — | — |
| GEA | GER002 | Id | CDC del DE/DTE | A | 44 | 1-1 |
| GEA | GER003 | dNumTimRet | Número de timbrado del documento de retención | N | 8 | 1-1 |
| GEA | GER004 | dEstRet | Establecimiento | A | 3 | 1-1 |
| GEA | GER005 | dPunExpRet | Punto de expedición | A | 3 | 1-1 |
| GEA | GER006 | dNumDocRet | Número del documento | A | 7 | 1-1 |
| GEA | GER007 | dCodConRet | Identificador de la retención | A | 40 | 1-1 |
| GEA | GER008 | dFeEmiRet | Fecha de emisión de la retención | F | 19 | 1-1 |

### [NUEVO] Evento asociación de anulación de la Retención (GERA)

| Grupo | ID | Campo | Descripción | Tipo | Longitud | Ocurrencia |
|-------|----|-------|-------------|------|----------|------------|
| GEA | GERA001 | rGeVeRetAnu | Raíz Gestión de Eventos de retención anulación | G | — | — |
| GEA | GERA002 | Id | CDC del DE/DTE | A | 44 | 1-1 |
| GEA | GERA003 | dNumTimRet | Número de timbrado del documento de retención | N | 8 | 1-1 |
| GEA | GERA004 | dEstRet | Establecimiento del documento de retención | A | 3 | 1-1 |
| GEA | GERA005 | dPunExpRet | Punto de expedición del documento de retención | A | 3 | 1-1 |
| GEA | GERA006 | dNumDocRet | Número del documento de la retención | A | 7 | 1-1 |
| GEA | GERA007 | dCodConRet | Identificador de la retención | A | 40 | 1-1 |
| GEA | GERA008 | dFeEmiRet | Fecha de emisión de la retención | F | 19 | 1-1 |
| GEA | GERA009 | dFecAnRet | Fecha de anulación de la retención | F | 19 | 1-1 |

### [NUEVO] Evento anticipo (GEA) — Automático por SIFEN

| Grupo | ID | Campo | Descripción | Tipo | Longitud | Ocurrencia |
|-------|----|-------|-------------|------|----------|------------|
| GEA | GEA001 | rGeVeAnt | Raíz Gestión de Eventos anticipo | G | — | — |
| GEA | GEA002 | Id | CDC del DTE asociado | A | 44 | 1-1 |

### [NUEVO] Evento remisión (GERE) — Automático por SIFEN

| Grupo | ID | Campo | Descripción | Tipo | Longitud | Ocurrencia |
|-------|----|-------|-------------|------|----------|------------|
| GEA | GERE001 | rGeVeRem | Raíz Gestión de Eventos remisión | G | — | — |
| GEA | GERE002 | Id | CDC del DTE asociado | A | 44 | 1-1 |

---

## [NUEVO] Evento por actualización de datos: Datos del transporte (GET)

| Grupo | ID | Campo | Descripción | Tipo | Longitud | Ocurrencia | Observaciones |
|-------|----|-------|-------------|------|----------|------------|---------------|
| GDE | GET001 | rGeVeTr | Raíz Gestión de Eventos por actualización de datos del transporte | G | — | — | Nodo padre: GDE007 |
| GDE | GET002 | Id | CDC del DTE | A | 44 | 1-1 | |
| GDE | GET003 | dMotEv | Motivo del evento | N | 1 | 1-1 | 1=Cambio del local de la entrega; 2=Cambio del chofer; 3=Cambio del transportista; 4=Cambio de vehículo |
| GDE | GET004 | cDepEnt | Código del departamento del local de entrega | N | 1-2 | 0-1 | Obligatorio si GET003=1 |
| GDE | GET005 | dDesDepEnt | Descripción del departamento del local de entrega | A | 6-16 | 0-1 | Referente al campo GET004 |
| GDE | GET006 | cDisEnt | Código del distrito del local de entrega | N | 1-4 | 0-1 | Según Tabla 2.1 - Distritos |
| GDE | GET007 | dDesDisEnt | Descripción de distrito del local de entrega | A | 1-30 | 0-1 | Obligatorio si existe GET006 |
| GDE | GET008 | cCiuEnt | Código de la ciudad del local de entrega | N | 1-5 | 0-1 | Obligatorio si GET003=1 |
| GDE | GET009 | dDesCiuEnt | Descripción de ciudad del local de entrega | A | 1-30 | 0-1 | Referente al campo GET008 |
| GDE | GET010 | dDirEnt | Dirección del local de entrega | A | 1-255 | 0-1 | Obligatorio si GET003=1 |
| GDE | GET011 | dNumCas | Número de casa del local de entrega | N | 1-6 | 0-1 | Obligatorio si GET003=1 |
| GDE | GET012 | dCompDir1 | Complemento de dirección del local de entrega | A | 1-255 | 0-1 | Opcional si GET003=1 |
| GDE | GET013 | dNomChof | Nombre y apellido del chofer | A | 4-60 | 1-1 | Obligatorio si GET003=2 |
| GDE | GET014 | dNumIDChof | Número de documento de identidad del chofer | A | 1-20 | 0-1 | Obligatorio si GET003=2 |
| GDE | GET015 | iNatTrans | Naturaleza del transportista | N | 1 | 0-1 | Obligatorio si GET003=3. 1=Contribuyente; 2=No contribuyente |
| GDE | GET016 | dRucTrans | RUC del transportista | A | 3-8 | 0-1 | Obligatorio si GET015=1; no informar si GET015≠1 |
| GDE | GET017 | dDVTrans | Dígito verificador del RUC del transportista | N | 1 | 0-1 | Obligatorio si GET015=1; no informar si GET015≠1 |
| GDE | GET018 | dNomTrans | Nombre o razón social del transportista | A | 4-60 | 0-1 | Obligatorio si GET003=3 |
| GDE | GET019 | iTipIDTrans | Tipo de documento de identidad del transportista | N | 1 | 0-1 | Obligatorio si GET015=2; no informar si GET015=1. 1=Cédula paraguaya; 2=Pasaporte; 3=Cédula extranjera; 4=Carnet de residencia |
| GDE | GET020 | dDTipIDTrans | Descripción del tipo de documento de identidad del transportista | A | 9-20 | 0-1 | Obligatorio si existe GET019 |
| GDE | GET021 | dNumIDTrans | Número de documento de identidad del transportista | A | 1-20 | 0-1 | Obligatorio si existe GET019 |
| GDE | GET022 | iTipTrans | Tipo de transporte | N | 1 | 0-1 | Obligatorio si GET003=4. 1=Propio; 2=Tercero |
| GDE | GET023 | dDesTipTrans | Descripción del tipo de transporte | A | 6-7 | 0-1 | Obligatorio si existe GET022 |
| GDE | GET024 | iModTrans | Modalidad del transporte | N | 1 | 0-1 | Obligatorio si GET003=4. 1=Terrestre; 2=Fluvial; 3=Aéreo; 4=Multimodal |
| GDE | GET025 | dDesModTrans | Descripción de la modalidad del transporte | A | 5-10 | 1-1 | Referente al campo GET024 |
| GDE | GET026 | dTiVehTras | Tipo de vehículo | A | 4-10 | 0-1 | Obligatorio si GET003=4. Descripción acorde con GET024 |
| GDE | GET027 | dMarVeh | Marca del vehículo | A | 1-10 | 0-1 | Obligatorio si GET003=4 |
| GDE | GET028 | dTipIdenVeh | Tipo de identificación del vehículo | N | 1 | 0-1 | Obligatorio si GET003=4. 1=Número de identificación del vehículo; 2=Número de matrícula del vehículo |
| GDE | GET029 | dNroIDVeh | Número de identificación del vehículo | A | 1-20 | 0-1 | Informar cuando GET028=1 |
| GDE | GET030 | dNroMatVeh | Número de matrícula del vehículo | A | 6 | 0-1 | Informar cuando GET028=2 |

---

## 11.6 — Reglas de Validación de Gestión de Eventos

### 11.6.1 — Validaciones para Cancelación (códigos 4000–4049)

| N° Val | ID | Mensaje de Validación | Código | Observación | E |
|--------|----|-----------------------|--------|-------------|---|
| 1 | [MODIFICADO] GDE005 | La versión no corresponde | 4000 | Versión del formato del evento (GDE005) no corresponde a la versión vigente | R |
| 2 | [MODIFICADO] GEC002 | CDC inválido | 4001 | Debe validar que el CDC (GEC002) cuente con los 44 caracteres ~~según las reglas de estructuración del CDC~~ | R |
| 3 | [MODIFICADO] GEC002a | CDC no existente en el SIFEN | 4002 | El identificador del CDC (GEC002) no se encuentra aprobado como DTE SIFEN | R |
| 4 | [MODIFICADO] GEC002b | CDC ya se encuentra con el mismo evento solicitado | 4003 | El DTE (GEC002) ya se encuentra con un evento que se está requiriendo nuevamente (Duplicidad) | R |
| 5 | [NUEVO] GEC002c | [NUEVO] CDC ya se ha confirmado por el receptor | [NUEVO] 4004 | [NUEVO] Cuando el último evento del receptor sobre un CDC (GEC002) es una confirmación parcial o total, no se permite realizar la cancelación por parte del emisor | R |
| ~~7~~ | ~~GDE008~~ | ~~Firmador no autorizado para realizar evento~~ | ~~4006~~ | ~~El RUC del certificado utilizado para firmar los eventos sobre DE y DTE, no corresponde al emisor/electrónico~~ | ~~R~~ |
| ~~8~~ | ~~GDE008a~~ | ~~Firma Digital inválida por certificado digital revocado~~ | ~~4007~~ | ~~El certificado digital que se utilizó para firmar el evento está revocado en la fecha de firma digital (GDE004)~~ | ~~R~~ |
| ~~9~~ | ~~GDE004~~ | ~~Fecha de firma digital del evento inválida~~ | ~~4008~~ | ~~La fecha y hora de firma digital del evento no puede ser posterior a la Fecha y hora de aprobación en el SIFEN~~ | ~~R~~ |
| 6 | [MODIFICADO] GDE004a | Plazo de solicitud de cancelación de una FE extemporáneo | 4009 | [MODIFICADO] Cuando el tipo de documento es Factura electrónica (GEC002 inicia en 01), la fecha y hora de firma digital del evento (GDE004) de cancelación no puede superar al plazo límite de 48 hs contadas desde la fecha y hora de aprobación en el SIFEN | R |
| 7 | [NUEVO] GDE004b | [NUEVO] Plazo de solicitud de cancelación distinto a una FE es extemporáneo | [NUEVO] 4010 | [NUEVO] Cuando el tipo de documento es Autofactura electrónica o Nota de crédito o Nota de débito o Nota de remisión (GEC002 inicia en 04 o 05 o 06 o 07), la fecha y hora de firma digital del evento (GDE004) de cancelación no puede superar al plazo límite de 168 hs contadas desde la fecha y hora de aprobación en el SIFEN | R |

---

### 11.6.2 — Validaciones para Inutilización (códigos 4050–4099)

| N° Val | ID | Mensaje de Validación | Código | Observación | E |
|--------|----|-----------------------|--------|-------------|---|
| ~~9~~ | ~~GEI002~~ | ~~Número de timbrado inválido para el ambiente de pruebas~~ | ~~4051~~ | ~~Cuando en ambiente de prueba es obligatorio el uso del timbrado de pruebas~~ | ~~R~~ |
| 8 | [MODIFICADO] GEI002a | Número de timbrado no corresponde al contribuyente | 4052 | El número de timbrado no corresponde al RUC del contribuyente facturador electrónico | R |
| 9 | [MODIFICADO] GEI002b | Número de timbrado no corresponde al medio de generación | 4053 | El número del timbrado no corresponde al medio de generación para factura electrónica | R |
| 10 | [MODIFICADO] GEI003 | Código de establecimiento inválido para el timbrado informado | 4054 | El código del establecimiento no corresponde a un timbrado del medio de generación para facturación electrónica | R |
| 11 | [MODIFICADO] GEI004 | El código del punto de expedición es inválido para el timbrado informado | 4055 | El código del punto de expedición no corresponde a un timbrado autorizado para el contribuyente | R |
| 12 | [MODIFICADO] GEI007 | Tipo de Documento no corresponde al Número de Timbrado | 4060 | El tipo de Documento no corresponde a un número de timbrado autorizado | R |
| 13 | [MODIFICADO] GEI005 | Existe DTE en el rango informado | 4065 | Para el rango solicitado existe DTE en SIFEN | R |
| 14 | [MODIFICADO] GEI005a | Existe número inutilizado en el rango solicitado | 4066 | Dentro del rango solicitado para inutilización existen números de DE ya inutilizados en SIFEN | R |
| 15 | [MODIFICADO] GEI006 | Cantidad de números en el rango es inválida | 4067 | La cantidad máxima de números en el rango debe ser menor o igual a 1.000 (GEI006 – GEI005 ≤ 1.000) | R |
| 16 | [MODIFICADO] GEI006a | Número final de rango es inválido | 4068 | El número del final de rango (GEI006) debe ser mayor que el número de inicio del rango (GEI005) | R |
| ~~19~~ | ~~GDE008~~ | ~~Firmador no autorizado para realizar evento~~ | ~~4069~~ | ~~El RUC del certificado utilizado para firmar los eventos no corresponde al emisor/electrónico~~ | ~~R~~ |
| ~~20~~ | ~~GDE008a~~ | ~~Firma Digital inválida por certificado digital revocado~~ | ~~4070~~ | ~~El certificado digital que se utilizó para firmar el evento está revocado en la fecha de firma digital (GDE004)~~ | ~~R~~ |
| ~~21~~ | ~~GDE004~~ | ~~Fecha de firma digital del evento inválida~~ | ~~4071~~ | ~~La fecha de firma digital del evento no puede ser posterior a la Fecha de SIFEN~~ | ~~R~~ |

---

### [NUEVO] 11.6.3 — Validaciones para Notificación – Recepción DE/DTE (códigos 4100–4113)

| N° Val | ID | Mensaje de Validación | Código | Observación | E |
|--------|----|-----------------------|--------|-------------|---|
| 1 | [NUEVO] GEN001 | [NUEVO] Incongruencia en el registro de eventos del receptor (hay un evento previo de conformidad o disconformidad o desconocimiento) | [NUEVO] 4113 | [NUEVO] No se puede realizar una notificación – recepción de DE luego de un evento de desconocimiento. No se puede realizar una notificación – recepción de DTE luego de un evento de Conformidad parcial o total, Disconformidad o Desconocimiento | R |
| 2 | GEN002b | [MODIFICADO] CDC del DTE ya cuenta con un evento de esta naturaleza | 4101 | [MODIFICADO] Sobre el CDC de un DE/DTE se puede realizar hasta un evento de notificación - recepción | R |
| 3 | GEN002c | CDC del DTE inválido | 4102 | La estructura del CDC informado no corresponde (Longitud y/o dígito verificador) | R |
| 4 | GEN003 | Fecha de emisión del DE/DTE ha superado el plazo para registro del evento | 4103 | El plazo del registro del evento ha superado los 45 días contados a partir de la fecha de emisión | AO |
| 5 | GEN004 | Fecha de Recepción debe ser mayor o igual a la fecha de emisión del DE/DTE | 4104 | La fecha de emisión no puede ser mayor que la fecha de recepción del DE/DTE | R |
| 6 | GEN007 | RUC del Receptor requerido | 4105 | Es obligatorio informar RUC del receptor cuando el tipo de receptor es Contribuyente (GEN005=1) | R |
| 7 | GEN007a | RUC del Receptor no se debe informar | 4106 | Cuando el tipo de receptor es No Contribuyente (GEN005=2) no se debe informar el campo RUC del Receptor (GEN007) | R |
| 8 | GEN008 | Dígito verificador del RUC del contribuyente receptor requerido | 4107 | Es obligatorio informar DV del receptor cuando el tipo de receptor es Contribuyente (GEN005=1) | R |
| 9 | GEN008a | [MODIFICADO] Dígito verificador del RUC del contribuyente receptor no se debe informar | 4108 | Cuando el tipo de receptor es No Contribuyente (GEN005=2) no se debe informar el campo Dígito verificador del RUC del contribuyente receptor (GEN008) | R |
| 10 | GEN009 | Tipo de documento de identidad del receptor requerido | 4109 | Es obligatorio informar Tipo de documento de identidad del receptor cuando el tipo de receptor es No contribuyente (GEN005=2) | R |
| 11 | GEN009a | Tipo de documento de identidad del receptor no se debe informar | 4110 | Cuando el Tipo de documento de identidad del receptor es Contribuyente (GEN005=1) no se debe informar el tipo de documento de identidad del receptor | R |
| 12 | GEN010 | Número de documento de identidad requerido | 4111 | Es obligatorio informar Número de documento de identidad cuando el tipo de receptor es No contribuyente (GEN005=2) | R |
| 13 | GEN010a | [MODIFICADO] Número de documento de identidad no se debe informar | 4112 | Cuando el Tipo de documento de identidad del receptor es Contribuyente (GEN005=1) no se debe informar el documento de identidad del receptor (GEN010) | R |

---

### [NUEVO] 11.6.4 — Validaciones para el Evento Conformidad (códigos 4150–4156)

| N° Val | ID | Mensaje de Validación | Código | Observación | E |
|--------|----|-----------------------|--------|-------------|---|
| 14 | [NUEVO] GCO001 | [NUEVO] Incongruencia en el registro de eventos del receptor (hay un evento previo de desconocimiento) | [NUEVO] 4156 | [NUEVO] No se puede realizar una conformidad de DE/DTE luego de un evento de desconocimiento | R |
| 15 | GCO002 | [MODIFICADO] CDC del DTE ya cuenta con dos eventos de la misma naturaleza | 4150 | [MODIFICADO] Sobre el CDC de un DE/DTE se puede realizar hasta dos eventos de conformidad (conformidad parcial luego una conformidad total, en ese orden) | R |
| 16 | GCO002b | CDC del DTE inválido | 4151 | La estructura del CDC informado no corresponde (longitud y/o dígito verificador) | R |
| 17 | GCO002c | [MODIFICADO] CDC del DTE es inexistente o ha superado el plazo para registro del evento | 4152 | [MODIFICADO] Cuando el CDC no se encuentra en la base de datos del SIFEN o el plazo del registro del evento es inválido: Si el primer evento del receptor es conformidad, no se puede realizar después de 45 días desde la fecha de emisión del DTE. Si no es el primer evento y el último realizado no es una disconformidad, la conformidad no puede superar los 45 días desde la emisión. Si el último evento del receptor es una disconformidad, la conformidad (evento correctivo) no puede superar los 15 días desde la fecha de la disconformidad | R |
| 18 | [NUEVO] GCO002e | [NUEVO] No se puede registrar la confirmación por CDC del DTE cancelado o ajustado en su totalidad por nota de crédito | [NUEVO] 4155 | [NUEVO] El CDC del DTE ya ha sido cancelado con anterioridad | R |
| 19 | GCO004 | [MODIFICADO] Fecha estimada de Recepción requerida | 4154 | [MODIFICADO] Cuando el Tipo de Conformidad es parcial (GCO003=2) es obligatorio informar el campo fecha estimada de recepción de la mercadería (GCO004) | R |

---

### [NUEVO] 11.6.5 — Validaciones para el Evento Disconformidad (códigos 4200–4205)

| N° Val | ID | Mensaje de Validación | Código | Observación | E |
|--------|----|-----------------------|--------|-------------|---|
| 20 | [NUEVO] GDI001 | [NUEVO] Incongruencia en el registro de eventos del receptor (hay un evento previo de desconocimiento) | [NUEVO] 4205 | [NUEVO] No se puede realizar una disconformidad de DE/DTE luego de un evento de desconocimiento | R |
| 21 | GDI002 | [MODIFICADO] CDC del DTE ya cuenta con un evento de esta naturaleza | 4200 | [MODIFICADO] Sobre el CDC de un DTE se puede realizar hasta un evento de disconformidad | R |
| 22 | GDI002b | CDC del DTE inválido | 4201 | La estructura del CDC informado no corresponde (longitud y/o dígito verificador) | R |
| 23 | GDI002c | [MODIFICADO] CDC inexistente o ha superado el plazo para registro del evento | 4202 | [MODIFICADO] Cuando el CDC no se encuentra en la base de datos del SIFEN o el plazo del registro del evento es inválido: Si el primer evento del receptor es disconformidad, no se puede realizar después de 45 días desde la fecha de emisión del DTE. Si no es el primer evento y el último no es una conformidad, la disconformidad no puede superar los 45 días desde la emisión. Si el último evento del receptor es una conformidad, la disconformidad (evento correctivo) no puede superar los 15 días desde la fecha de la conformidad | R |
| 24 | [NUEVO] GDI002e | [NUEVO] No se puede registrar la disconformidad por CDC del DTE cancelado | [NUEVO] 4204 | [NUEVO] El CDC del DTE ya ha sido cancelado con anterioridad | R |

---

### [NUEVO] 11.6.6 — Validaciones para el Evento Desconocimiento DE/DTE (códigos 4250–4262)

| N° Val | ID | Mensaje de Validación | Código | Observación | E |
|--------|----|-----------------------|--------|-------------|---|
| 25 | GED002b | [MODIFICADO] CDC del DTE ya cuenta con un evento de esta naturaleza | 4251 | [MODIFICADO] Sobre el CDC de un DTE se puede realizar hasta un evento de desconocimiento | R |
| 26 | GED002c | CDC del DTE inválido | 4252 | La estructura del CDC informado no corresponde (longitud y/o dígito verificador) | R |
| 27 | GED003 | Fecha de emisión del DE/DTE ha superado el plazo para registro del evento | 4253 | El plazo del registro del evento ha superado los 45 días contados a partir de la fecha de emisión | AO |
| 28 | GED004 | Fecha de Recepción debe ser mayor a la fecha de emisión del DE/DTE | 4254 | La fecha de emisión no puede ser mayor que la fecha de recepción del DE/DTE | R |
| 29 | GED007 | RUC del Receptor requerido | 4255 | Es obligatorio informar RUC del receptor cuando el receptor es contribuyente (GED005=1) | R |
| 30 | GEN007a | RUC del Receptor no se debe informar | 4256 | Cuando el tipo de receptor es No Contribuyente (GED005=2) no se debe informar el campo RUC del Receptor (GED007) | R |
| 31 | GED008 | Dígito verificador del RUC del contribuyente receptor requerido | 4257 | Es obligatorio informar DV del receptor cuando el receptor es contribuyente (GED005=1) | R |
| 32 | GEN008a | Dígito verificador del RUC del contribuyente receptor no se debe informar | 4258 | Cuando el tipo de receptor es No Contribuyente (GED005=2) no se debe informar el campo Dígito verificador del RUC del contribuyente receptor (GED008) | R |
| 33 | GED009 | Tipo de documento de identidad del receptor requerido | 4259 | Es obligatorio informar el tipo de documento de identidad del receptor cuando el tipo de receptor es No contribuyente (GED005=2) | R |
| 34 | GED009a | Tipo de documento de identidad del receptor no se debe informar | 4260 | Cuando el Tipo de Receptor es Contribuyente (GED005=1) no es necesario informar el tipo de documento de identidad del receptor (GED009) | R |
| 35 | GED010 | Número de documento de identidad requerido | 4261 | Es obligatorio informar el número de documento de identidad del receptor cuando el tipo de receptor es No contribuyente (GED005=2) | R |
| 36 | GED10a | Número de documento de identidad no se debe informar | 4262 | Cuando el Tipo de Receptor es Contribuyente (GED005=1) no es necesario informar el número de documento de identidad del receptor (GED010a) | R |

---

### [NUEVO] 11.6.7 — Validaciones para el Evento por Actualización de Datos: Datos del Transporte (códigos 4300–4323)

| N° Val | ID | Mensaje de Validación | Código | Observación | E |
|--------|----|-----------------------|--------|-------------|---|
| 1 | GET004 | El Departamento, el Distrito y la Ciudad del local de entrega no están relacionados | 4300 | Debe haber relación entre el departamento (GET004), el distrito (GET006) y la ciudad (GET008) | R |
| 2 | GET004a | Código del departamento del local de la entrega requerido para el motivo Cambio del local de la entrega | 4301 | Cuando GET003=1, es obligatorio informar el código del departamento del local de la entrega (GET004) | R |
| 3 | GET005 | Descripción del departamento del local de la entrega es requerida | 4302 | Cuando se informa GET004, es obligatorio informar la descripción del departamento del local de la entrega (GET005) | R |
| 4 | GET005a | Descripción del departamento del local de la entrega no corresponde al código | 4303 | Descripción del departamento del local de la entrega no coincidente con lo informado en GET004 | R |
| 5 | GET007 | Descripción del distrito del local de la entrega es requerida | 4304 | Cuando se informa GET006, es obligatorio informar la descripción del distrito del local de la entrega (GET007) | R |
| 6 | GET007a | Descripción del distrito del local de la entrega no corresponde al código | 4305 | Descripción del distrito del local de entrega no coincidente con lo informado en GET006 | R |
| 7 | GET008 | Código de la ciudad del local de la entrega requerido para el motivo Cambio del local de la entrega | 4306 | Cuando GET003=1, es obligatorio informar el código de la ciudad del local de la entrega (GET008) | R |
| 8 | GET009 | Descripción de la ciudad del local de la entrega es requerida | 4307 | Cuando se informa GET008, es obligatorio informar la descripción de la ciudad del local de la entrega (GET009) | R |
| 9 | GET009a | Descripción de la ciudad del local de la entrega no corresponde al código | 4308 | Descripción de la ciudad del local de la entrega no coincidente con lo informado en GET008 | R |
| 10 | GET010 | Dirección del local de la entrega requerida para el motivo Cambio del local de la entrega | 4309 | Cuando GET003=1, es obligatorio informar la dirección del local de la entrega (GET010) | R |
| 11 | GET011 | Número de casa del local de la entrega requerido para el motivo Cambio del local de la entrega | 4310 | Cuando GET003=1, es obligatorio informar el número de casa del local de la entrega (GET011) | R |
| 12 | GET013 | Nombre y apellido del chofer requerido para el motivo Cambio del chofer | 4311 | Cuando GET003=2, es obligatorio informar el nombre y apellido del chofer (GET013) | R |
| 13 | GET014 | Número de documento de identidad del chofer requerido para el motivo Cambio del chofer | 4312 | Cuando GET003=2, es obligatorio informar el número de documento de identidad del chofer (GET014) | R |
| 14 | GET015 | Naturaleza del transportista requerida para el motivo Cambio del transportista | 4313 | Cuando GET003=3, es obligatorio informar la naturaleza del transportista (GET015) | R |
| 15 | GET016 | RUC del transportista no informado | 4314 | Se requiere informar el número de RUC si la naturaleza del transportista es igual a contribuyente (GET015=1) | R |
| 16 | GET016a | RUC del transportista inexistente | 4315 | El RUC del transportista informado no existe en la base de datos de Marangatu | R |
| 17 | GET016b | El RUC del transportista se encuentra inactivo | 4316 | El RUC del transportista debe contar con un estado distinto a CANCELADO, CANCELADO DEFINITIVO o SUSPENSIÓN TEMPORAL en Marangatu al momento de la emisión del DE | R |
| 18 | GET016c | RUC del transportista no requerido | 4317 | Si la naturaleza del transportista es distinta a contribuyente (GET015≠1), el RUC del transportista (GET016) no debe ser informado | R |
| 19 | GET017 | Dígito Verificador del RUC del transportista incorrecto | 4318 | El Dígito Verificador ingresado (GET017) no corresponde al módulo 11 del RUC (GET016) | R |
| 20 | GET018 | Nombre o razón social del transportista es requerido para el motivo del evento | 4319 | Cuando GET003=3, es obligatorio informar el nombre o razón social del transportista (GET018) | R |
| 21 | GET019 | Tipo de documento de identidad del transportista no informado | 4320 | Se requiere informar el tipo de documento de identidad si la naturaleza del transportista es igual a NO contribuyente (GET015=2) | R |
| 22 | GET019a | Tipo de documento de identidad del transportista no requerido | 4321 | Si la naturaleza del transportista es igual a contribuyente (GET015=1), el tipo de documento de identidad del transportista (GET019) no debe ser informado | R |
| 23 | GET020 | Descripción del tipo de documento de identidad del transportista no informada | 4322 | Si se informa el código de tipo de documento de identidad del transportista (GET019), es obligatorio indicar la descripción del mismo (GET020) | R |
| 24 | GET020a | Descripción del tipo de documento de identidad del transportista no corresponde al código | 4323 | Descripción del tipo de documento de identidad del transportista (GET020) no coincidente con lo informado en el campo GET019 | R |
| 25 | GET021 | Número de documento de identidad del transportista no informado | 4324 | Si se informa el código de tipo de documento de identidad del transportista (GET019), el número de dicho documento es requerido (GET021) | R |
| 26 | GET022 | Tipo de transporte requerido para el motivo Cambio de vehículo | 4313 | Cuando GET003=4, es obligatorio informar el tipo de transporte (GET022) | R |
| 27 | GET023 | Descripción del tipo de transporte es requerida | 4314 | Cuando se informa GET022, es obligatorio informar la descripción del tipo de transporte (GET023) | R |
| 28 | GET023a | Descripción del tipo de transporte no corresponde al código | 4315 | Descripción del tipo de transporte no coincidente con lo informado en el campo GET022 | R |
| 29 | GET024 | Modalidad del transporte requerido para el motivo Cambio de vehículo | 4316 | Cuando GET003=4, es obligatorio informar la modalidad del transporte (GET024) | R |
| 30 | GET025 | Descripción de la modalidad del transporte es requerida | 4317 | Cuando se informa GET024, es obligatorio informar la descripción de la modalidad del transporte (GET025) | R |
| 31 | GET025a | Descripción de la modalidad del transporte no corresponde al código | 4318 | Descripción de la modalidad del transporte no coincidente con lo informado en el campo GET024 | R |
| 32 | GET026 | Tipo de vehículo requerido para el motivo Cambio de vehículo | 4319 | Cuando GET003=4, es obligatorio informar el tipo de vehículo (GET026) | R |
| 33 | GET027 | Marca del vehículo requerida para el motivo Cambio de vehículo | 4320 | Cuando GET003=4, es obligatorio informar la marca del vehículo (GET027) | R |
| 34 | GET028 | Tipo de identificación del vehículo requerido para el motivo Cambio de vehículo | 4321 | Cuando GET003=4, es obligatorio informar el tipo de identificación del vehículo (GET028) | R |
| 35 | GET029 | Tipo de identificación del vehículo no informado | 4322 | Se requiere el número de identificación del vehículo cuando el tipo de identificación del vehículo es 1 (GET028=1) | R |
| 36 | GET030 | Número de matrícula del vehículo no informado | 4323 | Se requiere número de matrícula del vehículo cuando el tipo de identificación del vehículo es 2 (GET028=2) | R |
