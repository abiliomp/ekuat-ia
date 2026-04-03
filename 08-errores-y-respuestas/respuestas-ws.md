> **Fuente:** Manual Técnico SIFEN v150, secciones 12.2 y 12.3
> **Nota:** Contenido tachado (~~así~~) indica especificaciones eliminadas en v150. [MODIFICADO] indica cambios. [NUEVO] indica adiciones en v150.

# Códigos de Respuesta de los Servicios Web

El SIFEN valida cada mensaje entrante en múltiples niveles. Los códigos de respuesta devueltos por los Web Services son identificadores de 4 dígitos asignados según el tipo de validación y el WS que la emite.

---

## 12.2.1 – Validación del certificado de transmisión (Protocolo TLS)

Las validaciones AA01 a AA05 son realizadas por el propio protocolo TLS.

| ID | Resultado de Validación | Código | Observaciones | E |
|----|------------------------|--------|---------------|---|
| AA01 | Certificado de Transmisor Inválido | 0001 | Certificado de Transmisor inexistente en el mensaje; versión incorrecta; no se aceptan certificados de la AC; ExtendKeyUsage no define "ClientAuth" | R |
| AA02 | Plazo de validez del Certificado digital vencido o inválido | 0002 | | R |
| AA03 | Cadena de Certificación inválida | 0003 | Certificado del emisor no corresponde a un PSC habilitado en el país; certificado del PSC revocado; certificado no firmado por el PSC emisor | R |
| AA04 | LCR del Certificado Transmisor inválida o inaccesible | 0004 | No existe la dirección de la LCR (CRLDistributionPoint); LCR indisponible; LCR inválida | R |
| AA05 | Certificado del transmisor revocado | 0005 | | R |
| AA06 | Certificado Raíz no pertenece al MIC | 0006 | | R |
| AA07 | No existe la extensión del RUC del emisor en el certificado | 0007 | Si el certificado es de persona jurídica, el RUC debe estar en el campo SerialNumber. Si es de persona física, en el campo SubjectAlternativeName | R |

---

## 12.2.2 – Validación de la estructura XML de los WS

La primera validación sobre el mensaje es la correspondencia entre el XML enviado y su Schema XSD correspondiente. El emisor debe generar los mensajes XML en el formato correspondiente a la versión vigente, [MODIFICADO] informando ésta en el campo de versión dentro del grupo `rDE`.

El emisor debe validar los archivos XML contra el Schema XSD correspondiente antes de transmitirlos al SIFEN.

---

## 12.2.3 – Validación de forma del área de datos del Request

~~El grupo AB (AB01-AB20, códigos 0100-0119) ha sido eliminado en v150.~~

| ID | Resultado de Validación | Código | E |
|----|------------------------|--------|---|
| ~~AB01~~ | ~~Fallo de schema XML del área de datos~~ | ~~0100~~ | ~~R~~ |
| ~~AB02~~ | ~~Fallo de schema: no existe el campo raíz esperado para el mensaje~~ | ~~0101~~ | ~~R~~ |
| ~~AB03~~ | ~~Fallo de schema: no existe el atributo versión para el campo raíz esperado para el mensaje~~ | ~~0102~~ | ~~R~~ |
| ~~AB05~~ | ~~Existe algún namespace diferente del namespace estándar del DE~~ | ~~0104~~ | ~~R~~ |
| ~~AB06~~ | ~~Existe(n) carácter(es) de edición en el inicio o en el final del mensaje, o entre los campos XML~~ | ~~0105~~ | ~~R~~ |
| ~~AB07~~ | ~~Utilizado prefijo en el namespace~~ | ~~0106~~ | ~~R~~ |
| ~~AB08~~ | ~~Utilizada codificación diferente de UTF-8~~ | ~~0107~~ | ~~R~~ |

---

## 12.2.4 – Validación del certificado de firma

| ID | Resultado de Validación | Código | Observaciones | E |
|----|------------------------|--------|---------------|---|
| AC01 | Certificado inválido | 0120 | No existe certificado de firma en el mensaje; no se aceptan certificados del PSC; KeyUsage no define firma digital y no repudio | R |
| AC02 | Alguna o todas las fechas del certificado (inicio o final de validez) inválidas | 0121 | | R |
| AC03 | No existe la extensión del RUC en el certificado | 0122 | De Persona Física: en el OID correspondiente al SubjectAlternativeName. De Persona Jurídica: en el OID correspondiente al SerialNumber | R |
| ~~AC04~~ | ~~Cadena de certificación inválida~~ | ~~0123~~ | ~~Certificado del PSC no habilitado por el MIC; certificado del PSC revocado; certificado no está firmado por el PSC~~ | ~~R~~ |
| ~~AC05~~ | ~~Problema en la LCR del certificado de firma~~ | ~~0124~~ | ~~Dirección de la LCR no informada (CRLDistributionPoint); error en el acceso a la LCR; LCR inexistente~~ | ~~R~~ |
| ~~AC06~~ | ~~Certificado de firma revocado~~ | ~~0125~~ | | ~~R~~ |
| ~~AC07~~ | ~~Certificado raíz no corresponde al MIC~~ | ~~0126~~ | | ~~R~~ |

**Nota:** En v150, las validaciones AC04–AC07 (cadena de certificación, LCR, revocación y raíz del certificado de firma) fueron eliminadas como validaciones independientes. Sus controles fueron absorbidos por la validación AD02.

---

## 12.2.5 – Validación de la firma digital

| ID | Resultado de Validación | Código | Observaciones | E |
|----|------------------------|--------|---------------|---|
| AD01 | Firma difiere del estándar | 0140 | No fue firmado el documento completo (falta Reference URI en la firma); Transform Algorithm previsto en la firma ("C14N" y Enveloped) no informado | R |
| AD02 | [MODIFICADO] Valor de la firma (SignatureValue) diferente del calculado por el PKI | [MODIFICADO] 0141 | [MODIFICADO] Ahora incluye también: certificado del PSC no habilitado por el MIC; certificado del PSC revocado; certificado no está firmado por el PSC; dirección de la LCR no informada (CRLDistributionPoint); error en el acceso a la LCR; LCR inexistente; certificado de firma revocado; certificado raíz no corresponde al MIC | R |
| AD03 | RUC del certificado utilizado para firmar no pertenece al Contribuyente emisor | 0142 | | R |

---

## 12.2.6 – Validaciones genéricas a los mensajes de entrada de los WS

Aplicadas a los mensajes de entrada de cualquiera de los Web Services dispuestos por la SET.

| ID | Resultado de Validación | Código | E |
|----|------------------------|--------|---|
| AE01 | XML malformado | 0160 | R |
| AE02 | Servidor de procesamiento momentáneamente sin respuesta | 0161 | R |
| AE03 | Servidor de procesamiento paralizado, sin tiempo de regreso | 0162 | R |
| AE04 | Versión del formato del WS no soportada | 0163 | R |

---

## 12.2.7 – Validaciones genéricas a los mensajes de control de llamada de los WS

| ID | Resultado de Validación | Código | E |
|----|------------------------|--------|---|
| AF01 | Elemento de HeaderMsg inexistente en el SOAP Header | 0180 | R |
| AF04 | RUC del certificado utilizado en la conexión no pertenece a un contribuyente activo en la base de datos de RUC | 0183 | R |

---

## 12.3 – Validaciones por Web Service

### 12.3.1 – WS siRecepDE (Recepción de Documento Electrónico)

**12.3.1.1 – Mensaje de entrada**

Tamaño máximo permitido: **1.000 KB**. Si la conexión se interrumpe sin generar el código 0200, corresponde verificar la configuración de red (firewall).

| ID | Resultado de Validación | Código | E |
|----|------------------------|--------|---|
| BA01 | Mensaje de datos de entrada del WS siRecepDE superior a 1.000 KB | 0200 | R |

**12.3.1.2 – Información de control de la llamada al WS**

Sin validaciones específicas en v100/v150. Códigos reservados: 0220 a 0239 (BB01 a BB20).

**12.3.1.3 – Área de datos del WS**

| ID | Resultado de Validación | Código | E |
|----|------------------------|--------|---|
| BC01 | Autorización del DE satisfactoria | 0260 | A |

---

### 12.3.2 – WS siRecepLoteDE (Recepción de Lote de DE)

**12.3.2.1 – Mensaje de entrada**

Tamaño máximo permitido: **10.000 KB**. Si la conexión se interrumpe sin generar el código 0270, corresponde verificar la configuración de red.

| ID | Resultado de Validación | Código | E |
|----|------------------------|--------|---|
| BD01 | Mensaje de datos de entrada del WS siRecepLoteDE superior a 10.000 KB | 0270 | R |

**12.3.2.2 – Información de control de la llamada al WS**

Sin validaciones específicas en v100/v150. Códigos reservados: 0280 a 0299 (BE01 a BE20).

**12.3.2.3 – Área de datos del WS**

| ID | Resultado de Validación | Código | E |
|----|------------------------|--------|---|
| BF01 | Lote recibido con éxito | 0300 | A |
| BF02 | Lote no encolado para procesamiento | 0301 | R |

---

### 12.3.3 – WS siResultLoteDE (Consulta de Resultado de Lote de DE)

**12.3.3.1 – Mensaje de entrada**

Tamaño máximo permitido: **1.000 KB**.

| ID | Resultado de Validación | Código | E |
|----|------------------------|--------|---|
| BG01 | Mensaje de datos de entrada del WS siResultLoteDE superior a 1.000 KB | 0320 | R |

**12.3.3.2 – Información de control de la llamada al WS**

| ID | Resultado de Validación | Código | Observaciones | E |
|----|------------------------|--------|---------------|---|
| BH01 | RUC del certificado de conexión no autorizado a consultar el lote | 0340 | El resultado del procesamiento del lote solo puede ser consultado por el RUC que realizó la transmisión del mismo | R |

**12.3.3.3 – Área de datos del WS**

| ID | Resultado de Validación | Código | E |
|----|------------------------|--------|---|
| BI01 | Lote inexistente | 0360 | R |
| BI02 | Lote en procesamiento | 0361 | R |
| BI03 | Procesamiento de lote concluido | 0362 | A |
| B104 | Lotes con tipos distintos de DE | 0363 | R |

---

### 12.3.4 – WS siConsDE (Consulta de Documento Electrónico)

**12.3.4.1 – Mensaje de entrada**

Tamaño máximo permitido: **1.000 KB**.

| ID | Resultado de Validación | Código | E |
|----|------------------------|--------|---|
| BJ01 | Mensaje de datos de entrada del WS siConsDE superior a 1.000 KB | 0380 | R |

**12.3.4.2 – Información de control de la llamada al WS**

Sin validaciones específicas. Códigos reservados: 0400 a 0419 (BK00 a BK19).

**12.3.4.3 – Área de datos del WS**

| ID | Resultado de Validación | Código | E |
|----|------------------------|--------|---|
| BL01 | CDC inexistente | 0420 | R |
| BL02 | CDC encontrado | 0421 | A |

---

### 12.3.5 – WS siConsRUC (Consulta de RUC)

**12.3.5.1 – Mensaje de entrada**

Tamaño máximo permitido: **1.000 KB**.

| ID | Resultado de Validación | Código | E |
|----|------------------------|--------|---|
| BM01 | Mensaje de datos de entrada del WS siConsRUC superior a 1.000 KB | 0460 | R |

**12.3.5.2 – Información de control de la llamada al WS**

Sin validaciones específicas. Códigos reservados: 0480 a 0499 (BN01 a BN20).

**12.3.5.3 – Área de datos del WS**

| ID | Resultado de Validación | Código | E |
|----|------------------------|--------|---|
| BO01 | RUC inexistente | 0500 | R |
| BO02 | RUC no tiene permiso para utilizar el WS | 0501 | R |
| BO03 | Éxito en la consulta | 0502 | A |

---

### 12.3.6 – WS siRecepEvento (Recepción de Evento)

**12.3.6.1 – Mensaje de entrada**

Tamaño máximo permitido: **1.000 KB**.

| ID | Resultado de Validación | Código | E |
|----|------------------------|--------|---|
| BS01 | Mensaje de datos de entrada del WS siRecepEvento superior a 1.000 KB | 0560 | R |

**12.3.6.2 – Información de control de la llamada al WS**

Sin validaciones específicas. Códigos reservados: 0580 a 0599 (BT01 a BT20).

**12.3.6.3 – Área de datos del WS**

| ID | Resultado de Validación | Código | E |
|----|------------------------|--------|---|
| BU01 | Evento registrado correctamente | 0600 | A |

---

## Resumen de rangos de códigos por WS

| Grupo | Código Inicio | Código Fin | WS / Tipo de Validación | Estado |
|-------|--------------|-----------|--------------------------|--------|
| AA | 0000 | 0099 | Certificado de Transmisión (Protocolo TLS) | Vigente |
| ~~AB~~ | ~~0100~~ | ~~0119~~ | ~~Forma del área de datos de los mensajes de entrada~~ | ~~Eliminado~~ |
| AC | 0120 | 0139 | Certificado digital utilizado por el contribuyente para firmar | Vigente |
| AD | 0140 | 0159 | Firma digital | Vigente |
| AE | 0160 | 0179 | Validaciones genéricas — mensajes de entrada de los WS | Vigente |
| AF | 0180 | 0199 | Validaciones genéricas — mensajes de control de llamada de los WS | Vigente |
| BA-BB | 0200 | 0239 | siRecepDE — Mensaje de entrada e información de control | Vigente |
| BC | 0260 | 0259 | siRecepDE — Área de datos | Vigente |
| BD-BE | 0270 | 0299 | siRecepLoteDE — Mensaje de entrada e información de control | Vigente |
| BF | 0300 | 0319 | siRecepLoteDE — Área de datos | Vigente |
| BG-BH | 0320 | 0359 | siResultLoteDE — Mensaje de entrada e información de control | Vigente |
| BI | 0360 | 0379 | siResultLoteDE — Área de datos | Vigente |
| BJ-BK | 0380 | 0419 | siConsDE — Mensaje de entrada e información de control | Vigente |
| BL | 0420 | 0439 | siConsDE — Área de datos | Vigente |
| BM-BN | 0460 | 0499 | siConsRUC — Mensaje de entrada e información de control | Vigente |
| BO | 0500 | 0559 | siConsRUC — Área de datos | Vigente |
| BS-BT | 0560 | 0599 | siRecepEvento — Mensaje de entrada e información de control | Vigente |
| BU | 0600 | 0619 | siRecepEvento — Área de datos | Vigente |
