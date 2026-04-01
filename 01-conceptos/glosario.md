# Glosario Técnico SIFEN

> **Fuente:** Manual Técnico SIFEN v150, sección 16

## Términos y Definiciones

| Término | Significado |
|---------|-------------|
| **Administración Tributaria (AT)** | Subsecretaría de Estado de Tributación (SET), actualmente denominada Dirección Nacional de Ingresos Tributarios (DNIT). |
| **Archivo Electrónico de Factura** | Archivo electrónico (XML) con los datos de una factura. No ha sido aún firmado digitalmente. |
| **B2B** | Business to Business. Acrónimo para describir las operaciones entre empresas. Código D202=1. |
| **B2C** | Business to Consumer. Acrónimo para describir operaciones entre una empresa y un consumidor final. Código D202=2. |
| **B2G** | Business to Government. Acrónimo para operaciones entre una empresa y una entidad de gobierno. Código D202=3. |
| **B2F** | Business to Foreign. Tipo de operación para servicios prestados por una empresa nacional a una empresa o persona física del exterior. Código D202=4. |
| **CDC** | Código de Control. Número de 44 dígitos generado dentro del sistema del emisor, que permite identificar de manera inequívoca a un DTE, evitando duplicidad en el envío de documentos a la SET. Ver campo A002. |
| **Certificado Digital** | Mensaje de datos u otro registro emitido por una entidad legalmente habilitada que confirma la vinculación entre el titular de una firma digital y los datos de creación de la misma. |
| **Código QR** | Quick Response Code. Módulo para almacenar información en una matriz de puntos o código de barras bidimensional. Se genera conforme a ISO/IEC 18004. |
| **CSC** | Código Secreto del Contribuyente. Código de 32 dígitos alfanuméricos generado por el SIFEN y entregado al facturador electrónico. Se utiliza para la generación segura del QR. |
| **DE** | Documento Electrónico. Documento emitido y firmado digitalmente por un emisor electrónico que aún no ha sido aprobado por la Administración Tributaria. No ha ingresado al SIFEN. |
| **DNCP** | Dirección Nacional de Contrataciones Públicas. |
| **DNIT** | Dirección Nacional de Ingresos Tributarios (antes SET). |
| **DTE** | Documento Tributario Electrónico. Documento electrónico con aprobación de uso por parte de la Administración Tributaria, ingresado al SIFEN. |
| **Documentos Asociados** | DE que pueden complementar a la factura electrónica: nota de crédito y nota de débito. |
| **Emisor** | Contribuyente que genera el archivo electrónico, lo firma electrónicamente y lo remite para solicitar la autorización de uso. |
| **ERP** | Enterprise Resource Planning. Gestión integrada de los procesos de negocio básicos, mediada por software y tecnología. |
| **Factura Electrónica** | DTE que respalda la compra y venta de bienes y servicios. Documento electrónico en formato XML aprobado y autorizado para fines fiscales. |
| **Facturador Electrónico** | Contribuyente autorizado por la Administración Tributaria para emitir y recibir DTE. Adquiere la naturaleza de emisor y receptor. |
| **Firma Digital** | Firma electrónica certificada por un prestador acreditado, creada usando medios bajo exclusivo control del titular. Permite verificar identidad, integridad y autoría del documento. |
| **KuDE** | Representación gráfica de un Documento Electrónico. Palabra compuesta: "Ku" de "Kuatia" (papel en guaraní) + "DE" de Documento Electrónico. |
| **LCR** | Lista de Certificados Revocados. Utilizada en el proceso de validación de la firma digital. |
| **Módulo 11** | Algoritmo utilizado para calcular el dígito verificador del CDC y del RUC. |
| **MIC** | Ministerio de Industria y Comercio. Administrador de la Autoridad Certificadora Raíz del Paraguay. |
| **NDE** | Nota de Débito Electrónica. Tipo de documento electrónico C002=6. |
| **NCE** | Nota de Crédito Electrónica. Tipo de documento electrónico C002=5. |
| **NRE** | Nota de Remisión Electrónica. Tipo de documento electrónico C002=7. |
| **PSC** | Prestador de Servicios de Certificación. Entidad habilitada por el MIC para emitir certificados digitales. |
| **RUC** | Registro Único de Contribuyentes. Número de identificación tributaria en Paraguay. |
| **Schema XML (XSD)** | Archivo con extensión `.xsd` que describe la estructura y restricciones de los documentos XML. |
| **SENAVE** | Servicio Nacional de Calidad y Sanidad Vegetal y de Semillas. |
| **SET** | Subsecretaría de Estado de Tributación. Ver DNIT. |
| **SGTM** | Sistema de Gestión de Timbrado Marangatu. |
| **SIFEN** | Sistema Integrado de Facturación Electrónica Nacional. Sistema creado por Decreto 7.795/2017 para la facturación electrónica en Paraguay. |
| **SOAP** | Simple Object Access Protocol versión 1.2. Estándar de intercambio de datos utilizado en los Web Services del SIFEN. |
| **TLS** | Transport Layer Security versión 1.2. Protocolo de seguridad para la comunicación entre contribuyentes y SET. |
| **Timbrado** | Autorización o habilitación otorgada por la SET para emitir documentos tributarios. Identificado por un número de 8 dígitos (campo C004). |
| **WS** | Web Service. Servicio web disponibilizado por el SIFEN para el intercambio de documentos y datos. |
| **XML** | Extensible Markup Language. Lenguaje de marcas utilizado para la estructura de los Documentos Electrónicos. |
| **XSD** | XML Schema Definition. Archivo que define la estructura y restricciones de los documentos XML. |

## Acrónimos de Tipos de Documentos

| Acrónimo | Descripción | Código C002 |
|----------|-------------|-------------|
| FE | Factura Electrónica | 1 |
| FEE | Factura Electrónica de Exportación | 2 |
| LCE | Liquidación de Crédito Electrónica | 3 |
| AFE | Autofactura Electrónica | 4 |
| NCE | Nota de Crédito Electrónica | 5 |
| NDE | Nota de Débito Electrónica | 6 |
| NRE | Nota de Remisión Electrónica | 7 |
| CRE | Comprobante de Retención Electrónico | 8 (futuro) |
| FCE | Factura de Contingencia Electrónica | 11 |

## Prefijos de Nombres de Campos XML

| Prefijo | Significado |
|---------|-------------|
| `c` | Código integrante de una tabla del Capítulo 16 |
| `i` | Código integrante de una tabla en la columna "Observaciones" |
| `d` | Nombre de un campo común (dato) |
| `g` | Nombre de un grupo |
| `r` | Raíz del XML |

## Tipos de Datos XML

| Tipo | Descripción |
|------|-------------|
| XML | Documento XML |
| G | Grupo de elementos |
| CG | Choice Group (excluye otro CG del mismo padre) |
| CE | Choice Element (excluye otro CE del mismo padre) |
| A | Alfanumérico |
| N | Numérico |
| F | Fecha (AAAA-MM-DDThh:mm:ss o AAAA-MM-DD) |
| B | Binario en Base64 |
