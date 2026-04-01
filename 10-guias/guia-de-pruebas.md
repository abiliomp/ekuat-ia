# Guía de Pruebas para el Sistema e-kuatia (SIFEN)

> **Fuente:** Guía de Pruebas para el Sistema e-kuatia — DNIT, Febrero/2026

## Información general

Esta guía tiene como propósito orientar sobre las condiciones, plazos y tareas para la realización del proceso de pruebas en el ambiente dispuesto por la DNIT mediante el SIFEN. Está dirigida a contribuyentes designados por la DNIT como facturadores electrónicos y a quienes se adhieran voluntariamente al Sistema Integrado de Facturación Electrónica Nacional.

**Documentación técnica de referencia:**
- Manual Técnico Versión 150
- Notas Técnicas (ajustes al Manual Técnico)
- Recomendaciones - servicio asíncrono
- Listado Checksum MD5 de las versiones del Manual Técnico
- Estructura xml_DE / Estructura_DE xsd

Portal oficial: [https://www.dnit.gov.py/web/e-kuatia/documentacion-tecnica](https://www.dnit.gov.py/web/e-kuatia/documentacion-tecnica)

---

## 1. Ambientes disponibles

### Ambiente de Pruebas (Test)

La DNIT dispone en este ambiente los servicios web y funcionalidades básicas del SIFEN, junto con datos de prueba (RUC, Timbrado y CSC Genérico). Permite probar:

- Ingreso con autenticación mutua
- Validación de Documentos Electrónicos generados
- Vigencia y revocación de certificados electrónicos
- Firma electrónica
- Registro de eventos
- Consulta de DTE con sus eventos

Los documentos emitidos en este ambiente **no tienen valor jurídico**.

### Ambiente de Producción

La DNIT dispone en este ambiente los servicios completos del SIFEN para facturadores electrónicos habilitados. Los DTE aprobados en este ambiente **tienen valor jurídico** para efectos tributarios.

---

## 2. Set de datos de pruebas

### Timbrado

El número de timbrado y su conjunto de datos (Inicio de Vigencia, Establecimiento, Punto de Expedición) deben ser incluidos en todos los Documentos Electrónicos. Se obtienen a través del SGTM (Sistema de Gestión de Timbrado de Marangatu).

Para la habilitación como Facturador Electrónico consultar la Guía disponible en: [https://www.dnit.gov.py/web/e-kuatia/guias](https://www.dnit.gov.py/web/e-kuatia/guias)

### Datos del emisor

| Campo | Valor |
|---|---|
| RUC | Datos reales del contribuyente según registro en SISTEMA MARANGATU |
| DV | Dígito verificador real |
| Nombre/Razón social | El campo debe tener la descripción: "DOCUMENTO ELECTRÓNICO SIN VALOR COMERCIAL NI FISCAL - GENERADO EN AMBIENTE DE PRUEBA" |

> Los datos del emisor deben corresponder a la información real de cada contribuyente como se encuentra registrado ante la DNIT.

### Datos del receptor e ítem de mercadería

| Campo | Valor |
|---|---|
| RUC | Datos reales para informaciones de clientes (RUC, Dirección, etc.) |
| Ítem de mercadería | El primer ítem debe tener la descripción: "DOCUMENTO ELECTRÓNICO SIN VALOR COMERCIAL NI FISCAL - GENERADO EN AMBIENTE DE PRUEBA" |

### Código de Seguridad del Contribuyente (CSC)

Para generación del Hash del QR en ambiente de pruebas:

| ID CSC | CSC (código secreto) |
|---|---|
| 0001 | ABCD0000000000000000000000000000 |
| 0002 | EFGH0000000000000000000000000000 |

> Todos los demás datos deben estar conforme al Manual Técnico y sus notas técnicas vigentes.

### Certificado Electrónico

Para probar el acceso con certificado no autorizado se debe contar con un certificado **no válido** (NO registrado o que NO reúne las condiciones tecnológicas exigidas por el SIFEN). Se pueden autogenerar certificados con herramientas gratuitas disponibles en internet.

---

## 3. Servicios Web y Funcionalidades del SIFEN

Los servicios web del SIFEN deben probarse de forma secuencial, siguiendo la cadena completa de valor:

1. Ingreso, comunicación y autenticación mutua
2. Transmisión de DE (sincrónica y asincrónica), ejecución de validaciones y obtención del resultado
3. Recepción, registro y asociación de eventos a los DE/DTE
4. Consulta de DTE y sus eventos (por CDC o por Código QR)
5. Generación de la representación gráfica (KuDE)

---

## 4. Secuencia de pruebas mínimas

### 4.1. Ingreso, Comunicación y Autenticación Mutua

El software cliente del facturador electrónico debe autenticarse ante el SIFEN usando un certificado cualificado de firma electrónica emitido por un Prestador de Servicios de Certificación (PSC) habilitado por el MIC.

El certificado debe contener el RUC del contribuyente y la extensión Extended Key Usage con el permiso `clientAuth`.

Lista de PSC habilitados: [https://www.acraiz.gov.py/html/Certif_1PrestaServ.html](https://www.acraiz.gov.py/html/Certif_1PrestaServ.html)

| Escenario de Prueba | Servicios a probar | Cantidad mínima | Observaciones |
|---|---|---|---|
| Comunicación y autenticación con certificado VÁLIDO | WS Sincrónico, WS Asincrónico, WS Consulta, Resultado Lote, WS Consulta DE, WS Recepción evento, WS Consulta RUC | 1 por cada Servicio Web | Certificado cualificado con RUC del contribuyente. Identificar mensajes del resultado conforme MT vigente |
| Comunicación y autenticación con certificado NO VÁLIDO | WS Sincrónico, WS Asincrónico, WS Consulta, Resultado Lote, WS Consulta DE, WS Recepción evento, WS Consulta RUC | 1 (recomendable) | Certificado cualificado NO válido. Identificar mensajes del resultado |

### 4.2. Transmisión de Documentos Electrónicos y Validaciones

#### WS Sincrónico — DE que deben ser APROBADOS

| Tipo de DE | Cantidad mínima | Observaciones |
|---|---|---|
| Factura Electrónica (con mínimo 2 ítems) | 5 | Generación y transmisión con datos CORRECTOS. Enviar 1 DE por tipo por cada conexión |
| Nota de Crédito Electrónica | 5 | — |
| Nota de Débito Electrónica | 5 | — |
| Autofactura Electrónica | 5 | — |
| Nota de Remisión Electrónica | 5 | — |

#### WS Sincrónico — DE que deben ser RECHAZADOS

| Tipo de DE | Cantidad mínima | Observaciones |
|---|---|---|
| Factura Electrónica | 5 | Generación y transmisión con datos INCORRECTOS (distintos errores). Enviar 1 DE por tipo por cada conexión |
| Nota de Crédito Electrónica | 5 | — |
| Nota de Débito Electrónica | 5 | — |
| Autofactura Electrónica | 5 | — |
| Nota de Remisión Electrónica | 5 | — |

#### WS Asincrónico — DE que deben ser APROBADOS

| Tipo de DE | Cantidad mínima | Observaciones |
|---|---|---|
| Factura Electrónica (mínimo 2 ítems) | 5 (en 1 Lote) | Datos CORRECTOS. Se recomienda enviar entre 30 y 50 DE por lote |
| Nota de Crédito Electrónica | 5 (en 1 Lote) | — |
| Nota de Débito Electrónica | 5 (en 1 Lote) | — |
| Autofactura Electrónica | 5 (en 1 Lote) | — |
| Nota de Remisión Electrónica | 5 (en 1 Lote) | — |

#### WS Asincrónico — DE que deben ser RECHAZADOS

| Tipo de DE | Cantidad mínima | Observaciones |
|---|---|---|
| Factura Electrónica | 5 (en 1 Lote) | Datos INCORRECTOS. Se recomienda enviar entre 3 y 5 DE por lote |
| Nota de Crédito Electrónica | 5 (en 1 Lote) | — |
| Nota de Débito Electrónica | 5 (en 1 Lote) | — |
| Autofactura Electrónica | 5 (en 1 Lote) | — |
| Nota de Remisión Electrónica | 5 (en 1 Lote) | — |

> Pueden incorporarse otros tipos de DE/DTE según el Art. 3 del Decreto N° 872/2023.

### 4.3. Recepción, Registro y Asociación de Eventos

#### Rol: EMISOR

| Escenario de Prueba | Evento | Cantidad mínima | Observaciones |
|---|---|---|---|
| Emisión, envío y aprobación del evento de Cancelación | Cancelación | 5 (cualquier DE) | WS Sincrónico de Eventos |
| Emisión, envío y aprobación del evento de Inutilización | Inutilización | 2 (FE) + 1 (NCE) + 1 (NDE) + 1 (AFE) | Verificar mensajes del resultado |

#### Rol: RECEPTOR

| Escenario de Prueba | Evento | Cantidad mínima | Observaciones |
|---|---|---|---|
| Emisión, envío y aprobación del evento de Conformidad | Conformidad | 3 | WS Sincrónico de Eventos. La cantidad se realiza sobre CDC |
| Emisión, envío y aprobación del evento de Disconformidad | Disconformidad | 3 | — |
| Emisión, envío y aprobación del evento de Desconocimiento | Desconocimiento DE/DTE | 3 | — |
| Emisión, envío y aprobación del evento de Notificación de Recepción | Notificación de Recepción DE/DTE | 3 | — |
| Emisión, envío y aprobación de ajuste a un evento previo | Ajuste del Evento | 3 | — |

### 4.4. Consulta de DTE y sus Eventos

| Tipo de DE | Cantidad mínima | Observaciones |
|---|---|---|
| Factura Electrónica | 3 | Acceder, autenticarse y consultar los DTE |
| Nota de Crédito Electrónica | 3 | — |
| Nota de Débito Electrónica | 3 | — |
| Autofactura Electrónica | 3 | — |
| Nota de Remisión Electrónica | 3 | — |

### 4.5. Generación de Representación Gráfica (KuDE) y Validación QR

#### Generación de KuDE en formato PDF

| Tipo de DE | Cantidad mínima |
|---|---|
| Factura Electrónica | 1 |
| Nota de Crédito Electrónica | 1 |
| Nota de Débito Electrónica | 1 |
| Autofactura Electrónica | 1 |
| Nota de Remisión Electrónica | 1 |

#### Consulta del DTE con uso de Código QR

| Tipo de DE | Cantidad mínima |
|---|---|
| Factura Electrónica | 2 |
| Nota de Crédito Electrónica | 2 |
| Nota de Débito Electrónica | 2 |
| Autofactura Electrónica | 2 |
| Nota de Remisión Electrónica | 2 |

---

## 5. Canales de Comunicación

Para consultas o problemas relacionados con el ambiente de pruebas:

- Portal de contacto DNIT: [https://www.dnit.gov.py/web/e-kuatia/contactenos](https://www.dnit.gov.py/web/e-kuatia/contactenos)
- Envío de consultas o archivos para verificación: [https://servicios.set.gov.py/eset-publico/EnvioMailSetIService.do](https://servicios.set.gov.py/eset-publico/EnvioMailSetIService.do)

---

## Anexo: Glosario Técnico

| Término | Significado |
|---|---|
| CDC (Código de Control del DTE) | Número de 44 dígitos generado dentro del sistema del emisor que identifica de manera inequívoca a un DTE, evitando duplicidad |
| Certificado Cualificado de Firma Electrónica | Certificado expedido por un prestador cualificado de servicios de confianza conforme al Art. 43 de la Ley N° 6822/2021 |
| CSC (Código de Seguridad del Contribuyente) | Código secreto brindado por la DNIT al facturador electrónico, utilizado para la generación del QR |
| DE (Documento Electrónico) | Documento emitido y firmado electrónicamente que aún no ha sido aprobado por la Administración Tributaria |
| DNIT | Dirección Nacional de Ingresos Tributarios |
| DTE (Documento Tributario Electrónico) | Documento electrónico con aprobación de uso por parte de la Administración Tributaria, ingresado al SIFEN |
| Evento | Toda ocurrencia registrada en el SIFEN por el Emisor, Receptor, o la DNIT que modifica o afecta el estado de un DE o DTE |
| Facturador Electrónico | Contribuyente autorizado por la Administración Tributaria para emitir y recibir DTE |
| KuDE | Expresión de los DE en formato físico o digital (representación impresa/PDF del DE). Incluye código QR |
| PCSC (Prestadores Cualificados de Servicios de Confianza) | Entidad prestadora de servicios de certificación de firmas electrónicas autorizada por la Dirección General de Firma Digital y Comercio Electrónico del MIC |
| RUC | Registro Único del Contribuyente |
| SIFEN | Sistema Integrado de Facturación Electrónica Nacional |
| Sistema Marangatu | Sistema de Gestión Tributaria Marangatu |
| Validación | Conjunto de reglas técnicas y de negocio aplicadas por el SIFEN al archivo electrónico de los DE y eventos |
