# Eventos del Documento Electrónico (siRecepEvento)

> **Fuente:** Manual Técnico SIFEN v150, secciones 11 y 12, Notas Técnicas NT-010, NT-014, NT-015, NT-019, NT-025

## Descripción

Los eventos son acciones posteriores a la aprobación de un DE que modifican su estado o registran hechos relacionados. Se transmiten al SIFEN mediante el WS `siRecepEvento`. Cada evento tiene su propio schema XSD y requiere firma digital.

---

## Resumen de Todos los Eventos

| Código | Nombre | Actor | Plazo | Schema |
|--------|--------|-------|-------|--------|
| GEC | Cancelación | Emisor | 48h (FE/AFE/NCE/NDE) / 168h (NRE) | Schema XML N° 9 |
| GEI | Inutilización | Emisor | 15 días | Schema XML N° 10 |
| GEN | Notificación de Recepción | Receptor | 45 días | Schema XML N° 11 |
| GCO | Conformidad | Receptor | 45 días | Schema XML N° 12 |
| GDI | Disconformidad | Receptor | 45 días | Schema XML N° 13 |
| GED | Desconocimiento | Receptor | 45 días | Schema XML N° 14 |
| GENFE | Nominación FE | Emisor | Sin plazo definido | Schema XML N° 15 (NT-014) |
| GET | Actualización de Transporte | Emisor | Sin plazo definido | Schema XML N° 16 (NT-010) |

---

## Endpoint del WS siRecepEvento

| Ambiente | URL |
|----------|-----|
| Pruebas | `https://sifen-test.set.gov.py/de/ws/eventos/recepcion-evento.wsdl` |
| Producción | `https://sifen.set.gov.py/de/ws/eventos/recepcion-evento.wsdl` |

**Método SOAP:** `rRecepEvento`

---

## Estructura General del Request de Evento

```xml
<soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope">
  <soapenv:Header/>
  <soapenv:Body>
    <rEnviEvento>
      <dId>1</dId>
      <xDE>
        <rEnviEventoDe
          xmlns="http://ekuatia.set.gov.py/sifen/xsd"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <dVerFor>150</dVerFor>
          <xDE>
            <gGroupEvento>  <!-- Nombre varía según el tipo de evento -->
              <!-- Campos del evento -->
            </gGroupEvento>
            <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
              <!-- Firma digital del evento -->
            </Signature>
          </xDE>
        </rEnviEventoDe>
      </xDE>
    </rEnviEvento>
  </soapenv:Body>
</soapenv:Envelope>
```

---

## Campos Comunes de Todos los Eventos (Grupo GDE)

| ID | Campo | Tipo | Long. | Descripción |
|----|-------|------|-------|-------------|
| GDE001 | Id | A | 44 | CDC del DE al que se aplica el evento |
| GDE002 | dFecFirmaEv | F | 19 | Fecha y hora de firma del evento |
| GDE003 | dIdEv | N | 1-3 | Número correlativo del evento del mismo tipo para ese DE |

---

## Evento GEC: Cancelación

Permite al **emisor** cancelar un DE aprobado dentro del plazo permitido.

### Plazos de Cancelación

| Tipo de DE | Plazo |
|------------|-------|
| FE (C002=1) | 48 horas desde la aprobación |
| AFE (C002=4) | 48 horas desde la aprobación |
| NCE (C002=5) | 48 horas desde la aprobación |
| NDE (C002=6) | 48 horas desde la aprobación |
| NRE (C002=7) | 168 horas (7 días) desde la aprobación |

> **NT-025:** Se elimina la restricción que impedía cancelar un DE si el receptor ya había confirmado su conformidad.

### Campos del Evento GEC

| ID | Campo | Tipo | Long. | Descripción |
|----|-------|------|-------|-------------|
| GEC001 | Id | A | 44 | CDC del DE a cancelar |
| GEC002 | dMotCan | A | 5-500 | Motivo de la cancelación (texto libre) |

### Ejemplo XML del Evento GEC

```xml
<gGroupEvento>
  <gGecDE>
    <Id>[CDC_44_DIGITOS]</Id>
    <dFecFirmaEv>2024-01-15T12:00:00</dFecFirmaEv>
    <dIdEv>1</dIdEv>
    <dMotCan>Error en el monto total de la factura</dMotCan>
  </gGecDE>
</gGroupEvento>
```

---

## Evento GEI: Inutilización

Permite al **emisor** inutilizar un rango de numeración que no fue usado (CDC generados pero no transmitidos al SIFEN).

### Plazo: 15 días calendario desde la generación del CDC

### Campos del Evento GEI

| ID | Campo | Tipo | Long. | Descripción |
|----|-------|------|-------|-------------|
| GEI001 | dCodSeg | N | 9 | Código de seguridad del CDC a inutilizar |
| GEI002 | dInfoInut | A | 5-500 | Motivo de la inutilización |
| GEI003 | dNumIniInut | N | 7 | Número inicial del rango a inutilizar |
| GEI004 | dNumFinInut | N | 7 | Número final del rango a inutilizar |
| GEI005 | dSerieInut | A | 2 | Serie de la numeración a inutilizar (si aplica) |

---

## Evento GEN: Notificación de Recepción

Permite al **receptor** notificar al SIFEN que ha recibido el DE. Es informativo, no modifica el estado fiscal del DE.

### Plazo: 45 días desde la emisión del DE

### Campos del Evento GEN

| ID | Campo | Tipo | Long. | Descripción |
|----|-------|------|-------|-------------|
| GEN001 | Id | A | 44 | CDC del DE recibido |
| GEN002 | dFecFirmaEv | F | 19 | Fecha y hora de la notificación |
| GEN003 | dIdEv | N | 1-3 | Correlativo del evento (NT-019: validación modificada) |

---

## Evento GCO: Conformidad

El **receptor** confirma que el DE es correcto y acepta la operación.

### Plazo: 45 días desde la emisión del DE

### Campos del Evento GCO

| ID | Campo | Tipo | Long. | Descripción |
|----|-------|------|-------|-------------|
| GCO001 | Id | A | 44 | CDC del DE con el que está conforme |
| GCO002 | dFecFirmaEv | F | 19 | Fecha y hora de la conformidad |
| GCO003 | dIdEv | N | 1-3 | Correlativo del evento |

---

## Evento GDI: Disconformidad

El **receptor** indica que tiene observaciones sobre el DE (sin rechazar la operación).

### Plazo: 45 días desde la emisión del DE

### Campos del Evento GDI

| ID | Campo | Tipo | Long. | Descripción |
|----|-------|------|-------|-------------|
| GDI001 | Id | A | 44 | CDC del DE con observaciones |
| GDI002 | dFecFirmaEv | F | 19 | Fecha y hora de la disconformidad |
| GDI003 | dIdEv | N | 1-3 | Correlativo del evento |
| GDI004 | dMotDisconf | A | 5-500 | Motivo de la disconformidad |

---

## Evento GED: Desconocimiento

El **receptor** declara que no reconoce el DE como propio (no realizó la operación).

### Plazo: 45 días desde la emisión del DE

### Campos del Evento GED

| ID | Campo | Tipo | Long. | Descripción |
|----|-------|------|-------|-------------|
| GED001 | Id | A | 44 | CDC del DE desconocido |
| GED002 | dFecFirmaEv | F | 19 | Fecha y hora del desconocimiento |
| GED003 | dIdEv | N | 1-3 | Correlativo del evento (NT-019: validación modificada) |
| GED004 | dMotDescon | A | 5-500 | Motivo del desconocimiento |

---

## Evento GENFE: Nominación de Factura Electrónica (NT-014)

Permite al **emisor** identificar al comprador de una FE emitida como innominada (receptor con `dNumIDRec="0"`). Aplica solo a FE (C002=1).

### Campos del Evento GENFE

| ID | Campo | Tipo | Long. | Descripción |
|----|-------|------|-------|-------------|
| GENFE001 | Id | A | 44 | CDC de la FE a nominar |
| GENFE002 | dFecFirmaEv | F | 19 | Fecha y hora de la nominación |
| GENFE003 | dIdEv | N | 1-3 | Correlativo del evento |
| GENFE004-GENFE027 | Datos del comprador | Varios | Varios | Datos completos del receptor real (nombre, RUC/CI, dirección, etc.) |

> **NT-015:** Las NCE y NDE emitidas contra una FE nominada deben referenciar el CDC correcto de la FE original.

---

## Evento GET: Actualización de Datos de Transporte (NT-010)

Permite al **emisor** de una NRE (C002=7) actualizar los datos de transporte después de la aprobación.

### Tipos de Actualización (GET003)

| Código | Descripción |
|--------|-------------|
| 1 | Cambio del local de entrega |
| 2 | Cambio del chofer |
| 3 | Cambio del transportista |
| 4 | Cambio de vehículo |

### Campos del Evento GET

| ID | Campo | Tipo | Long. | Descripción |
|----|-------|------|-------|-------------|
| GET001 | Id | A | 44 | CDC de la NRE a actualizar |
| GET002 | dFecFirmaEv | F | 19 | Fecha y hora de la actualización |
| GET003 | iTipActTrans | N | 1 | Tipo de actualización (1-4, ver tabla) |
| GET004 | dDesTipActTrans | A | - | Descripción del tipo de actualización |
| GET005+ | Datos nuevos | Varios | Varios | Datos del nuevo local/chofer/transportista/vehículo |

---

## Respuesta del WS siRecepEvento

### Evento Aprobado

```xml
<rRetEnviEvento>
  <dId>1</dId>
  <gResEnviEvento>
    <dCodRes>0700</dCodRes>
    <dMsgRes>Evento registrado</dMsgRes>
    <dFecProc>2024-01-15T12:00:00</dFecProc>
    <Id>[CDC_44_DIGITOS]</Id>
    <dProtAut>[PROTOCOLO_EVENTO]</dProtAut>
  </gResEnviEvento>
</rRetEnviEvento>
```

### Evento Rechazado

```xml
<rRetEnviEvento>
  <dId>1</dId>
  <gResEnviEvento>
    <dCodRes>0704</dCodRes>
    <dMsgRes>Evento rechazado</dMsgRes>
    <gDetMotErr>
      <dCodErr>E001</dCodErr>
      <dMsgErr>Descripción del error</dMsgErr>
    </gDetMotErr>
  </gResEnviEvento>
</rRetEnviEvento>
```

### Códigos de Respuesta de Eventos

| Código | Descripción |
|--------|-------------|
| 0700 | Evento registrado exitosamente |
| 0701 | Evento registrado con observaciones |
| 0704 | Evento rechazado |
| 0705 | DE no encontrado para el evento |
| 0706 | Evento fuera de plazo |
| 0707 | Tipo de evento no aplica al tipo de DE |
| 0708 | El DE ya está cancelado |

---

## Tabla J del Manual Técnico: Resumen de Eventos

| Evento | Emisor puede cancelar | Receptor puede confirmar |
|--------|-----------------------|--------------------------|
| Aprobado | Sí (dentro de plazo) | Sí (GCO, GDI, GED, GEN) |
| Cancelado | No | No |
| Con GCO (conforme) | Sí — NT-025 lo habilitó | No aplica |
| Con GED (desconocido) | El emisor debe gestionar con la SET | — |
