> **Fuente:** Manual Técnico SIFEN v150, secciones 1, 4.3 y 16

> **Nota:** Este documento refleja el MT v150 con cambios del historial de versiones marcados.

# Glosario Técnico SIFEN

Términos y definiciones utilizados en el Sistema Integrado de Facturación Electrónica Nacional (SIFEN) del Paraguay.

---

## A

### Administración Tributaria (AT)
Subsecretaría de Estado de Tributación (SET). Organismo que reglamenta, administra y fiscaliza el SIFEN y los Documentos Tributarios Electrónicos.

### Archivo Electrónico de Factura
Archivo electrónico en formato XML con los datos de una factura. **Aún no ha sido firmado digitalmente.** Es la etapa previa al Documento Electrónico (DE).

### Autofactura Electrónica (AFE)
Documento tributario electrónico que constituye el comprobante de venta emitido por el comprador en los casos en que el vendedor no puede emitir factura. **[NUEVO en v150]** Incorporada como tipo de documento activo en la versión actual del MT (código C002 = 4).

---

## B

### B2B
*Business to Business*. Acrónimo para describir las operaciones comerciales entre empresas.

### B2C
*Business to Consumer*. Acrónimo para describir las operaciones entre una empresa y un consumidor final.

### B2G
*Business to Government*. Acrónimo para describir las operaciones entre una empresa y una entidad de gobierno.

### B2F **[NUEVO en v150]**
*Business to Foreign*. Acrónimo del tipo de operación para describir los servicios prestados por una empresa nacional a una empresa o persona física del exterior.

---

## C

### CDC — Código de Control del DTE
Número de **44 dígitos** generado por el sistema del emisor que identifica de manera unívoca a cada DTE, evitando duplicidad en el envío a la SET. Se incluye como atributo `Id` en el tag `<DE>` del XML y se usa como URI en la referencia de la firma digital.

Estructura: `[RUC emisor][DV RUC][Tipo DE][Establecimiento][Punto exp.][Tipo doc.][Número doc.][Código seg.][DV CDC]`

En el KuDE debe ser visible en grupos de cuatro caracteres.

### Certificado Digital
Mensaje de datos emitido por una entidad PSC legalmente habilitada, que confirma la vinculación entre el titular de una firma digital y los datos de creación de la misma. Estándar ITU-T X.509 v3. Tipos válidos:
- **F1**: Certificado de Firma Digital por Software (clave RSA 2048)
- **F2**: Certificado de Firma Digital por Hardware (clave RSA 2048 o RSA 4096)

### Código de Seguridad del Contribuyente (CSC)
Código de 32 dígitos alfanuméricos generado por el SIFEN y entregado al facturador electrónico al momento de su registro. Sirve para garantizar la seguridad y autoría del código QR. Conocimiento exclusivo de la AT y del contribuyente; se permiten hasta dos códigos activos simultáneamente.

### Código QR
Código de respuesta rápida (*Quick Response Code*). Módulo bidimensional para almacenar información, incluido en el KuDE conforme al estándar ISO/IEC 18004. Permite la consulta del DTE en el portal SIFEN mediante escáner o lectura manual del CDC.

---

## D

### DE — Documento Electrónico
Documento emitido y **firmado digitalmente** por un emisor electrónico que **aún no ha sido aprobado** por la AT. No ha ingresado al SIFEN. Registra una operación comercial y constituye el paso previo al DTE. Carecen de validez los DE sin firma digital.

### DNIT — Dirección Nacional de Ingresos Tributarios
También referida como SET. Entidad fiscal administradora del SIFEN.

### Documentos Asociados
DE que complementan a la factura electrónica: nota de crédito electrónica (NCE) y nota de débito electrónica (NDE).

### DTE — Documento Tributario Electrónico
Documento electrónico con **aprobación de uso** por parte de la AT, ingresado al SIFEN. Adquiere validez jurídica, fuerza probatoria e incidencia tributaria equivalente a los comprobantes físicos autorizados por la SET.

---

## E

### Ekuatia'i
**[MODIFICADO en v150]** Solución gratuita de facturación electrónica provista por la SET, orientada a contribuyentes con baja emisión de documentos electrónicos. Opera en tiempo real y se sustenta en los WS del subsistema de aprobación. Contempla el uso de firma digital (SET o contribuyente) para determinados contribuyentes de este segmento.

### Emisor / Facturador Electrónico
Contribuyente autorizado por la AT para emitir y recibir DTE. Genera el archivo electrónico, lo firma digitalmente y lo remite para obtener la autorización de uso.

### ERP
*Enterprise Resource Planning* — Planificación de Recursos Empresariales. Sistema de gestión integrada de los procesos de negocio.

---

## F

### Factura Electrónica (FE)
DTE que respalda la compra y venta de bienes y servicios. Cumple simultáneamente:
1. Es un documento electrónico con formato XML de FE conforme a las definiciones legales.
2. Fue validado conforme a las reglas del SIFEN.
3. Fue aprobado y autorizado para fines fiscales.

Código C002 = 1.

### Firma Digital
Firma electrónica certificada por un PSC acreditado, creada con medios bajo el control exclusivo del titular. Características:
- Se vincula únicamente al titular y a los datos referidos.
- Permite la detección posterior de cualquier modificación.
- Verifica la identidad del titular.
- Impide el desconocimiento de la integridad y autoría del documento.

En SIFEN: XML Digital Signature (Enveloped), RSA 2048, SHA-256.

---

## K

### KuDE — Representación Gráfica del DE
Acrónimo de **Ku** (*Kuatia*, en guaraní: "papel") + **DE** (Documento Electrónico). Expresión simplificada de un DE en formato físico o digital, entregada al receptor no electrónico o consumidor final.

Naturaleza: documento tributario **auxiliar**, no íntegramente el DTE. Contiene sólo algunos campos representativos. Su validez jurídica está **condicionada a la aprobación** del DE por la SET.

**[NUEVO en v150]** El receptor se obliga a consultar y comprobar la existencia del DTE en el SIFEN, tomando en cuenta los campos del KuDE como criterios de consulta.

---

## L

### LCR — Lista de Certificados Revocados
Lista de certificados digitales revocados, consultada por el SIFEN en el momento de la validación de la firma digital.

### Ley Tributaria
Ley N° 125/1991 "Que establece el Nuevo Régimen Tributario" y sus modificaciones.

---

## M

### Marangatu
Sistema de Gestión Tributaria Marangatu. Sistema principal de la SET con el que interopera SIFEN, especialmente en los módulos de RUC y Autorización/Timbrado.

---

## N

### Nota de Crédito Electrónica (NCE)
Documento complementario electrónico que reduce el valor de una factura emitida previamente. Código C002 = 5.

### Nota de Débito Electrónica (NDE)
Documento complementario electrónico que incrementa el valor de una factura emitida previamente. Código C002 = 6.

### Nota de Remisión Electrónica (NRE)
Documento electrónico que ampara el traslado de mercaderías. Código C002 = 7.

---

## O

### Otros Documentos Tributarios Electrónicos
DTE que respaldan operaciones con incidencia tributaria: nota de remisión, autofacturas y comprobantes de retención.

---

## P

### PSC — Prestador de Servicios de Certificación
Entidad prestadora de servicios de certificación de firmas digitales, autorizada por la Dirección General de Firma Digital y Comercio Electrónico del Ministerio de Industria y Comercio (MIC), en su carácter de Administrador de la Autoridad Certificadora Raíz del Paraguay. Referencia: https://www.acraiz.gov.py/html/Certif_1PrestaServ.html

---

## R

### Receptor
Destinatario del documento tributario electrónico. Puede ser nacional o extranjero, persona natural o jurídica.

### Representación Gráfica
Ver **KuDE**.

### RUC — Registro Único del Contribuyente
Número de identificación fiscal único asignado a cada contribuyente en Paraguay.

---

## S

### SET — Subsecretaría de Estado de Tributación
Organismo de la Administración Tributaria del Paraguay que administra y fiscaliza el SIFEN.

### SIFEN — Sistema Integrado de Facturación Electrónica Nacional
Sistema que recepciona, autoriza, almacena y provee los servicios de consulta de los DTE. Estructurado en dos subsistemas:
1. **[MODIFICADO] Subsistema de Aprobación**: orientado a grandes y medianos contribuyentes, con modelo de validación posterior (hasta 72 h) o previa.
2. **[MODIFICADO] Subsistema Solución Gratuita Ekuatia'i**: orientado a contribuyentes con baja emisión, con transacciones en tiempo real.

### Sistema Marangatu
Ver **Marangatu**.

---

## T

### Timbrado
Autorización otorgada por la SET al facturador electrónico para emitir documentos electrónicos con un número específico de 8 dígitos (campo C004).

**[MODIFICADO en v150]**: el timbrado ya no maneja fecha de fin de vigencia. ~~El campo C009 (dFeFinT — Fecha fin de vigencia del timbrado) fue eliminado.~~ Se usa el mecanismo de **series de dos letras mayúsculas** (AA, AB, ... ZZ) para garantizar la unicidad de la numeración al agotarse los 9.999.999 documentos.

---

## X

### XML — eXtensible Markup Language
Lenguaje de marcas extensible utilizado para el intercambio de datos en SIFEN. Todos los DE se estructuran en este formato con codificación UTF-8. La declaración obligatoria es: `<?xml version="1.0" encoding="UTF-8"?>`.

---

## Tabla de Siglas

| Sigla | Significado |
|-------|-------------|
| AFE | Autofactura Electrónica |
| AT | Administración Tributaria |
| B2B | Business to Business |
| B2C | Business to Consumer |
| B2F | Business to Foreign |
| B2G | Business to Government |
| CDC | Código de Control del DTE |
| CSC | Código de Seguridad del Contribuyente |
| DE | Documento Electrónico |
| DNIT | Dirección Nacional de Ingresos Tributarios |
| DTE | Documento Tributario Electrónico |
| ERP | Enterprise Resource Planning |
| FE | Factura Electrónica |
| KuDE | Representación Gráfica del DE (Kuatia DE) |
| LCR | Lista de Certificados Revocados |
| MIC | Ministerio de Industria y Comercio |
| MT | Manual Técnico |
| NCE | Nota de Crédito Electrónica |
| NDE | Nota de Débito Electrónica |
| NRE | Nota de Remisión Electrónica |
| PSC | Prestador de Servicios de Certificación |
| RUC | Registro Único del Contribuyente |
| SET | Subsecretaría de Estado de Tributación |
| SIFEN | Sistema Integrado de Facturación Electrónica Nacional |
| TLS | Transport Layer Security |
| WS | Web Service |
| XSD | XML Schema Definition |
