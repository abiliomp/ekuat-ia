# Schemas XSD del Sistema SIFEN

> **Fuente:** Manual Técnico SIFEN v150, sección 7.2 y Notas Técnicas NT-010, NT-011

## Descripción

Los Schemas XSD definen la estructura y validación del XML de los Documentos Electrónicos y sus mensajes de intercambio con el SIFEN. A partir de la versión 150 del Manual Técnico y sus Notas Técnicas, el sistema cuenta con 22 schemas numerados como "Schema XML N°".

---

## Listado Completo de Schemas XSD

| N° | Nombre | Archivo | Propósito |
|----|--------|---------|-----------|
| 1 | Schema XML DE | `DE_v150.xsd` | Estructura del Documento Electrónico (raíz `<rDE>`) |
| 2 | Schema XML siRecepDE | `siRecepDE_v150.xsd` | Recepción sincrónica de un DE individual |
| 3 | Schema XML siRecepLoteDE | `siRecepLoteDE_v150.xsd` | Recepción asíncrona de lote de DE |
| 4 | Schema XML siResultLoteDE | `siResultLoteDE_v150.xsd` | Resultado de procesamiento de lote de DE |
| 5 | Schema XML siConsDE | `siConsDE_v150.xsd` | Consulta de estado de un DE por CDC |
| 6 | Schema XML siConsLoteDE | `siConsLoteDE_v150.xsd` | Consulta de estado de un lote (número de lote) |
| 7 | Schema XML siRecepEvento | `siRecepEvento_v150.xsd` | Recepción de eventos (cancelación, inutilización, etc.) |
| 8 | Schema XML siConsRUC | `siConsRUC_v150.xsd` | Consulta de contribuyente por RUC |
| 9 | Schema XML DE Evento Cancelación | `GEC_v150.xsd` | Estructura del evento de cancelación de DE |
| 10 | Schema XML DE Evento Inutilización | `GEI_v150.xsd` | Estructura del evento de inutilización de numeración |
| 11 | Schema XML DE Evento Notif. Recepción | `GEN_v150.xsd` | Estructura del evento de notificación de recepción |
| 12 | Schema XML DE Evento Conformidad | `GCO_v150.xsd` | Estructura del evento de conformidad del receptor |
| 13 | Schema XML DE Evento Disconformidad | `GDI_v150.xsd` | Estructura del evento de disconformidad del receptor |
| 14 | Schema XML DE Evento Desconocimiento | `GED_v150.xsd` | Estructura del evento de desconocimiento del receptor |
| 15 | Schema XML DE Evento Nominación FE | `GENFE_v150.xsd` | Estructura del evento de nominación de Factura Electrónica (NT-014) |
| 16 | Schema XML DE Evento Act. Transporte | `GET_v150.xsd` | Estructura del evento de actualización de datos de transporte (NT-010) |
| 17 | Schema XML KuDE | `KuDE_v150.xsd` | Estructura del KuDE (representación gráfica, si aplica XSD) |
| 18 | Schema XML DE (principal) | `DE_v150.xsd` | Schema principal del Documento Electrónico (referenciado en namespace) |
| 19 | Schema XML Firma Digital | Basado en `xmldsig-core-schema.xsd` | Firma XML DSig enveloped |
| 20 | Schema XML siConsArchivoRUC request | `siConsArchivoRUC_req_v150.xsd` | Consulta de archivo de RUC (request) — NT-011 |
| 21 | Schema XML siConsArchivoRUC response | `siConsArchivoRUC_res_v150.xsd` | Consulta de archivo de RUC (response) — NT-011 |
| 22 | Schema XML siConsArchivoRUC aux | `siConsArchivoRUC_aux_v150.xsd` | Tipos auxiliares para siConsArchivoRUC — NT-011 |

---

## Paquete de Distribución

| Atributo | Valor |
|----------|-------|
| **Archivo ZIP** | `PS_FE_150.zip` |
| **URL base del namespace** | `http://ekuatia.set.gov.py/sifen/xsd` |
| **Fuente oficial** | `https://www.dnit.gov.py/web/e-kuatia/documentacion-tecnica` |
| **Versión del formato** | 150 (campo `<dVerFor>AA002</dVerFor>`) |

---

## Schema Principal: DE_v150.xsd

El Schema XML N° 1 (o N° 18) define la estructura del `<rDE>`. Se referencia en el `xsi:schemaLocation` del documento:

```xml
<rDE
  xmlns="http://ekuatia.set.gov.py/sifen/xsd"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://ekuatia.set.gov.py/sifen/xsd siRecepDE_v150.xsd">
```

### Estructura del rDE

```
rDE
├── dVerFor          (AA002) — Versión del formato: "150"
├── DE Id="[CDC]"    (A001)  — Documento Electrónico firmado
│   ├── gOpeDE       (B)     — Operación del DE
│   ├── gTimb        (C)     — Datos del Timbrado
│   ├── gDatGralOpe  (D)     — Datos Generales
│   │   ├── gOpeCom  (D1)    — Operación comercial (excepto NRE)
│   │   ├── gEmis    (D2)    — Datos del emisor
│   │   └── gDatRec  (D3)    — Datos del receptor
│   ├── gDtipDE      (E)     — Campos específicos por tipo
│   ├── gTotSub      (F)     — Subtotales y totales
│   ├── gCamGen      (G)     — Campos complementarios generales
│   ├── gCamDEAsoc   (H)     — Documentos asociados
│   └── gIniSeg      (I)     — Inicio de segmento de firma
├── Signature         (xmldsig) — Firma Digital XML
└── gCamFuFD         (J)     — Campos fuera de la firma
    └── dCarQR                — URL del código QR
```

---

## Schema de Eventos: GEC, GEI, GEN, GCO, GDI, GED, GENFE, GET

Cada evento tiene su propio schema. La estructura general de un evento es:

```xml
<rEnviEventoDe
  xmlns="http://ekuatia.set.gov.py/sifen/xsd"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dVerFor>150</dVerFor>
  <xDE>
    <gGroupEvent>
      <!-- Campos específicos del evento -->
    </gGroupEvent>
    <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
      <!-- Firma del evento -->
    </Signature>
  </xDE>
</rEnviEventoDe>
```

### Identificadores de Grupos de Eventos

| Prefijo | Evento | Schema |
|---------|--------|--------|
| `GDE` | Datos generales del evento | Común a todos |
| `GEC` | Evento de Cancelación | Schema XML N° 9 |
| `GEI` | Evento de Inutilización | Schema XML N° 10 |
| `GEN` | Evento de Notificación de Recepción | Schema XML N° 11 |
| `GCO` | Evento de Conformidad | Schema XML N° 12 |
| `GDI` | Evento de Disconformidad | Schema XML N° 13 |
| `GED` | Evento de Desconocimiento | Schema XML N° 14 |
| `GENFE` | Evento de Nominación FE (NT-014) | Schema XML N° 15 |
| `GET` | Evento de Actualización Transporte (NT-010) | Schema XML N° 16 |

---

## Schemas de Web Services (WSDL)

Los Web Services del SIFEN usan SOAP 1.2 con style Document/Literal. Los schemas de los WS se distribuyen junto con los XSD de los DE.

| WS | Método | Schema Request | Schema Response |
|----|--------|----------------|-----------------|
| siRecepDE | rRecepDE | Schema XML N° 2 | Respuesta SIFEN |
| siRecepLoteDE | rRecepLoteDE | Schema XML N° 3 | Respuesta SIFEN |
| siResultLoteDE | rResultLoteDE | Schema XML N° 4 | Respuesta SIFEN |
| siConsDE | rConsDE | Schema XML N° 5 | Respuesta SIFEN |
| siConsLoteDE | rConsLoteDE | Schema XML N° 6 | Respuesta SIFEN |
| siRecepEvento | rRecepEvento | Schema XML N° 7 | Respuesta SIFEN |
| siConsRUC | rConsRUC | Schema XML N° 8 | Respuesta SIFEN |
| siConsArchivoRUC | rConsArchivoRUC | Schema XML N° 20 | Schema XML N° 21 |

---

## Tipos de Datos XSD Usados

| Tipo XSD | Tipo MT | Descripción |
|----------|---------|-------------|
| `xs:string` | A | Alfanumérico |
| `xs:decimal` | N | Numérico con decimales |
| `xs:integer` | N | Numérico entero |
| `xs:dateTime` | F | Fecha y hora: `YYYY-MM-DDThh:mm:ss` |
| `xs:date` | F | Solo fecha: `YYYY-MM-DD` |
| `xs:base64Binary` | B | Binario en Base64 |
| `xs:complexType` | G | Grupo de elementos |

---

## Notas Técnicas que Afectan los Schemas

| NT | Cambio en Schemas |
|----|-------------------|
| NT-010 | Nuevos schemas para eventos GET (actualización transporte); elimina campo A005 del DE |
| NT-011 | Nuevos schemas XML N° 20, 21, 22 para siConsArchivoRUC |
| NT-014 | Nuevo schema para evento GENFE (nominación FE) |
| NT-016 | Cambios en el schema de firma digital: algoritmos adicionales, métodos C14N |
| NT-018 | Nuevo grupo D1.1 (obligaciones afectadas) en Schema XML N° 1 |
| NT-023 | Modificaciones en E711 (precisión decimal), E791 (ocurrencias), H018 |
