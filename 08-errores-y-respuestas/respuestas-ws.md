# Códigos de Respuesta de los Servicios Web

Descripción de los códigos que retorna cada Web Service del SIFEN, según la sección 12.2 y 12.3 del Manual Técnico.

> **Fuente:** Manual Técnico SIFEN v150, secciones 12.2 y 12.3

---

## Estados de respuesta generales

| Estado | Descripción |
|--------|-------------|
| Aprobado (A) | El DE superó todas las validaciones y se convierte en DTE |
| Aprobado con observación (AO) | El DE fue aprobado como DTE pero con observaciones (ej: extemporaneidad) |
| Rechazado (R) | El DE no cumple validaciones y no se convierte en DTE |
| Cancelado (CA) | El DTE fue cancelado por el emisor tras su aprobación |

---

## 12.2.1 — Validaciones del certificado de transmisión (TLS) — Códigos 0000–0099

| ID | Código | Descripción | Estado |
|----|--------|-------------|--------|
| AA01 | 0001 | Certificado de Transmisor Inválido (inexistente, versión incorrecta, sin ClientAuth) | R |
| AA02 | 0002 | Plazo de validez del Certificado digital vencido | R |
| AA03 | 0003 | Cadena de Certificación inválida | R |
| AA04 | 0004 | LCR del Certificado Transmisor inválida o indisponible | R |
| AA05 | 0005 | Certificado del transmisor revocado | R |
| AA06 | 0006 | Certificado Raíz no pertenece al MIC | R |
| AA07 | 0007 | No existe la extensión del RUC del emisor en el certificado | R |

*Nota: Las validaciones AA01 a AA05 son realizadas por el propio protocolo TLS.*

---

## 12.2.3 — Validaciones de forma del área de datos del Request — Códigos 0100–0119

| ID | Código | Descripción | Estado |
|----|--------|-------------|--------|
| AB01 | 0100 | Fallo de schema XML del área de datos | R |
| AB02 | 0101 | Fallo de schema: no existe el campo raíz esperado | R |
| AB03 | 0102 | Fallo de schema: no existe el atributo versión para el campo raíz | R |
| AB05 | 0104 | Existe algún namespace diferente del namespace estándar del DE | R |
| AB06 | 0105 | Existen caracteres de edición en el inicio/final del mensaje o entre campos XML | R |
| AB07 | 0106 | Utilizado prefijo en el namespace | R |
| AB08 | 0107 | Utilizada codificación diferente de UTF-8 | R |

---

## 12.2.4 — Validaciones del certificado de firma — Códigos 0120–0139

| ID | Código | Descripción | Estado |
|----|--------|-------------|--------|
| AC01 | 0120 | Certificado de firma inválido (inexistente, no acepta PSC, KeyUsage incorrecto) | R |
| AC02 | 0121 | Fechas del certificado inválidas | R |
| AC03 | 0122 | No existe la extensión del RUC en el certificado de firma | R |
| AC04 | 0123 | Cadena de certificación inválida | R |
| AC05 | 0124 | Dirección de la LCR no informada (CRLDistributionPoint) | R |
| AC06 | 0125 | Certificado de firma revocado o LCR con error | R |
| AC07 | 0126 | Certificado raíz no corresponde al MIC | R |

---

## 12.2.5 — Validaciones de la firma digital — Códigos 0140–0159

| ID | Código | Descripción | Estado |
|----|--------|-------------|--------|
| AD01 | 0140 | Firma difiere del estándar (falta Reference URI, Transform Algorithm incorrecto) | R |
| AD02 | 0141 | Valor de la firma (SignatureValue) diferente del calculado por el PKI | R |
| AD03 | 0142 | RUC del certificado utilizado para firmar no pertenece al Contribuyente emisor | R |

---

## 12.2.6 — Validaciones genéricas a los mensajes de entrada — Códigos 0160–0179

| ID | Código | Descripción | Estado |
|----|--------|-------------|--------|
| AE01 | 0160 | XML malformado | R |
| AE02 | 0161 | Servidor de procesamiento momentáneamente sin respuesta | R |
| AE03 | 0162 | Servidor de procesamiento paralizado, sin tiempo de regreso | R |
| AE04 | 0163 | Versión del formato del WS no soportada | R |

---

## 12.2.7 — Validaciones genéricas a los mensajes de control de llamada — Códigos 0180–0199

| ID | Código | Descripción | Estado |
|----|--------|-------------|--------|
| AF01 | 0180 | Elemento deHeaderMsg inexistente en el SOAP Header | R |
| AF04 | 0183 | RUC del certificado utilizado en la conexión no pertenece a un contribuyente activo | R |

---

## 12.3.1 — WS siRecepDE (Recepción de DE individual)

**Tipo:** Síncrono | **Tamaño máximo:** 1000 KB

| ID | Código | Descripción | Estado |
|----|--------|-------------|--------|
| BA01 | 0200 | Mensaje de datos de entrada del WS siRecepDE superior a 1000 KB | R |
| BC01 | 0260 | Autorización del DE satisfactoria | N |

**Respuesta del protocolo de procesamiento del DE** (Schema XML 4):

| Campo | Descripción |
|-------|-------------|
| `id` (PP02) | CDC del DE procesado |
| `dFecProc` (PP03) | Fecha y hora del procesamiento |
| `dDigVal` (PP04) | DigestValue del DE (para verificar correspondencia) |
| `dEstRes` (PP050) | Estado: "Aprobado", "Aprobado con observación", "Rechazado" |
| `dProtAut` (PP051) | Número de transacción (solo si aprobado) |
| `dCodRes` (PP052) | Código numérico del resultado |
| `dMsgRes` (PP053) | Mensaje descriptivo del resultado |

---

## 12.3.2 — WS siRecepLoteDE (Recepción de lote de DE)

**Tipo:** Asíncrono | **Tamaño máximo:** 10.000 KB | **Máximo:** 50 DE por lote del mismo tipo

| ID | Código | Descripción | Estado |
|----|--------|-------------|--------|
| BD01 | 0270 | Mensaje de datos de entrada del WS siRecepLoteDE superior a 10.000 KB | R |
| BF01 | 0300 | Lote recibido con éxito | A |
| BF02 | 0301 | Lote no encolado para procesamiento | R |

**Respuesta inicial:** El campo `dProtConsLote` (BRSch05) devuelve el número de lote cuando el código es 0300. Este número se usa para consultar el resultado posterior con siResultLoteDE.

---

## 12.3.3 — WS siResultLoteDE (Consulta resultado de lote)

**Tipo:** Asíncrono | **Tamaño máximo:** 1000 KB

| ID | Código | Descripción | Estado |
|----|--------|-------------|--------|
| BG01 | 0320 | Mensaje de datos de entrada del WS siResultLoteDE superior a 1000 KB | R |
| BH01 | 0340 | RUC del certificado de conexión no autorizado a consultar el lote | R |
| BI01 | 0360 | Lote inexistente | R |
| BI02 | 0361 | Lote en procesamiento | R |
| BI03 | 0362 | Procesamiento de lote concluido | A |
| BI04 | 0363 | Lotes con tipos distintos de DE | R |

**Tabla F — Resultados de procesamiento del WS Consulta Resultado de Lote:**

| Condición | Código | Mensaje |
|-----------|--------|---------|
| No existe número de lote consultado | 0360 | Número del Lote inexistente |
| No se ha culminado el procesamiento | 0361 | Lote en procesamiento |
| Procesamiento concluido con éxito | 0362 | Procesamiento de lote concluido |

Cuando `dCodResLot=0362`, la respuesta incluye el protocolo de respuesta de cada DE del lote.

---

## 12.3.4 — WS siConsDE (Consulta de DE)

**Tipo:** Síncrono | **Tamaño máximo:** 1000 KB

| ID | Código | Descripción | Estado |
|----|--------|-------------|--------|
| BJ01 | 0380 | Mensaje de datos de entrada del WS siConsDE superior a 1000 KB | R |
| BL01 | 0420 | CDC inexistente | — |
| BL02 | 0421 | RUC Certificado sin permiso | — |

**Tabla G — Resultados de procesamiento del WS Consulta DE:**

| Condición | Código | Mensaje |
|-----------|--------|---------|
| No existe DE consultado | 0420 | CDC inexistente |
| RUC sin permiso para consultar el DE | 0421 | RUC Certificado sin permiso |
| Consulta exitosa | 0422 | CDC encontrado |

Cuando el código es 0422, la respuesta incluye el contenedor del DE (Schema XML 11) con el XML del DE, el número de transacción y todos los eventos registrados.

---

## 12.3.5 — WS siConsRUC (Consulta de RUC)

**Tipo:** Síncrono | **Tamaño máximo:** 1000 KB

| ID | Código | Descripción | Estado |
|----|--------|-------------|--------|
| BM01 | 0460 | Mensaje de datos de entrada del WS siConsRUC superior a 1000 KB | R |
| BO01 | 0500 | RUC inexistente | — |
| BO02 | 0501 | RUC no tiene permiso para utilizar el WS | — |
| BO03 | 0502 | Éxito en la consulta | — |

**Respuesta exitosa (0502):** Devuelve el contenedor `xContRUC` (Schema XML 17) con:
- `dRUCCons`: RUC consultado
- `dRazCons`: Razón social del RUC
- `dCodEstCons`: Estado del RUC (ACT/SUS/SAD/BLQ/CAN/CDE)
- `dDesEstCons`: Descripción del estado
- `dRUCFactElec`: S=Es facturador electrónico, N=No es facturador electrónico

---

## 12.3.6 — WS siRecepEvento (Recepción de eventos)

**Tipo:** Síncrono | **Tamaño máximo:** 1000 KB

| ID | Código | Descripción | Estado |
|----|--------|-------------|--------|
| BS01 | 0560 | Mensaje de datos de entrada del WS siRecepEvento superior a 1000 KB | R |
| BU01 | 0600 | Evento registrado correctamente | A |

---

## URLs de los WS

### Producción

| WS | URL |
|----|-----|
| siRecepDE | https://sifen.set.gov.py/de/ws/sync/recibe.wsdl?wsdl |
| siRecepLoteDE | https://sifen.set.gov.py/de/ws/async/recibe-lote.wsdl?wsdl |
| siRecepEvento | https://sifen.set.gov.py/de/ws/eventos/evento.wsdl?wsdl |
| siResultLoteDE | https://sifen.set.gov.py/de/ws/consultas/consulta-lote.wsdl?wsdl |
| siConsRUC | https://sifen.set.gov.py/de/ws/consultas/consulta-ruc.wsdl?wsdl |
| siConsDE | https://sifen.set.gov.py/de/ws/consultas/consulta.wsdl?wsdl |

### Test

| WS | URL |
|----|-----|
| siRecepDE | https://sifen-test.set.gov.py/de/ws/sync/recibe.wsd?wsdl |
| siRecepLoteDE | https://sifen-test.set.gov.py/de/ws/async/recibe-lote.wsdl?wsdl |
| siRecepEvento | https://sifen-test.set.gov.py/de/ws/eventos/evento.wsdl?wsdl |
| siConsDE | https://sifen-test.set.gov.py/de/ws/consultas/consulta.wsdl?wsdl |
| siResultLoteDE | https://sifen-test.set.gov.py/de/ws/consultas/consulta-lote.wsdl?wsdl |
| siConsRUC | https://sifen-test.set.gov.py/de/ws/consultas/consulta-ruc.wsdl?wsdl |
