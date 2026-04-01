# Consulta de Estado de DE (siConsDE)

> **Fuente:** Manual Técnico SIFEN v150, sección 7.6

## Descripción

El WS `siConsDE` permite consultar el estado actual de un Documento Electrónico en el SIFEN usando su CDC (Código de Control de 44 dígitos). Es un servicio síncrono que devuelve el estado y los datos del DE almacenados en el SIFEN.

---

## Características

| Atributo | Valor |
|----------|-------|
| **Tipo** | Síncrono |
| **Input** | CDC del DE (44 dígitos) |
| **Output** | Estado del DE + datos almacenados |
| **Método SOAP** | `rConsDE` |
| **WS** | `siConsDE` |

---

## Endpoints

| Ambiente | URL |
|----------|-----|
| Pruebas | `https://sifen-test.set.gov.py/de/ws/consultas/consulta.wsdl` |
| Producción | `https://sifen.set.gov.py/de/ws/consultas/consulta.wsdl` |

---

## Estructura del Request

```xml
<soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope">
  <soapenv:Header/>
  <soapenv:Body>
    <rConsDE>
      <dId>1</dId>
      <dCDC>[CDC_44_DIGITOS]</dCDC>
    </rConsDE>
  </soapenv:Body>
</soapenv:Envelope>
```

### Campos del Request

| Campo | Tipo | Descripción |
|-------|------|-------------|
| dId | N | Identificador correlativo del request |
| dCDC | A | CDC del DE a consultar (44 dígitos exactos) |

---

## Estructura de la Response

### DE Encontrado y Aprobado

```xml
<soapenv:Envelope ...>
  <soapenv:Body>
    <rRetConsDE>
      <dId>1</dId>
      <gConsDe>
        <dCodRes>0422</dCodRes>
        <dMsgRes>CDC encontrado</dMsgRes>
        <gDetConsDe>
          <dCDC>[CDC_44_DIGITOS]</dCDC>
          <dEstDE>Aprobado</dEstDE>
          <dProtAut>[PROTOCOLO_AUTORIZACION]</dProtAut>
          <dFecProc>2024-01-15T10:30:00</dFecProc>
          <dXmlDE>
            <!-- XML completo del DE almacenado en el SIFEN (codificado) -->
          </dXmlDE>
        </gDetConsDe>
      </gConsDe>
    </rRetConsDE>
  </soapenv:Body>
</soapenv:Envelope>
```

### DE No Encontrado

```xml
<rRetConsDE>
  <dId>1</dId>
  <gConsDe>
    <dCodRes>0418</dCodRes>
    <dMsgRes>CDC no encontrado en el SIFEN</dMsgRes>
  </gConsDe>
</rRetConsDE>
```

---

## Campos de la Response

| Campo | Descripción |
|-------|-------------|
| dCodRes | Código de respuesta |
| dMsgRes | Mensaje descriptivo |
| dCDC | CDC del DE consultado |
| dEstDE | Estado actual del DE en el SIFEN |
| dProtAut | Protocolo de autorización (si aprobado) |
| dFecProc | Fecha y hora de procesamiento en el SIFEN |
| dXmlDE | XML completo del DE almacenado (cuando aplica) |

---

## Estados Posibles del DE (dEstDE)

| Estado | Descripción |
|--------|-------------|
| Aprobado | DE aprobado por el SIFEN. Tiene plena validez fiscal |
| Aprobado con observaciones | Aprobado con advertencias. Tiene validez fiscal |
| Rechazado | DE rechazado. No tiene validez fiscal |
| Cancelado | DE cancelado por el emisor mediante evento de cancelación |
| Inutilizado | CDC inutilizado (numeración no usada) |
| En proceso | DE en cola de procesamiento (lote asíncrono aún no procesado) |

---

## Códigos de Respuesta

| Código | Descripción |
|--------|-------------|
| 0422 | CDC encontrado — devuelve el estado del DE |
| 0418 | CDC no encontrado en el SIFEN |
| 0400 | Error de comunicación |
| 0401 | Error de autenticación (certificado TLS) |
| 0500 | Error interno del servidor SIFEN |

---

## Casos de Uso Frecuentes

### 1. Verificar si un DE fue aprobado antes de reenviar

Cuando el `siRecepDE` no devuelve respuesta (timeout), consultar con `siConsDE` antes de reenviar para evitar duplicados:

```
1. Llamar a siConsDE con el CDC del DE enviado
2. Si dCodRes=0422 y dEstDE="Aprobado" → No reenviar, guardar dProtAut
3. Si dCodRes=0418 → El SIFEN no lo recibió → Se puede reenviar con el mismo CDC
4. Si dCodRes=0422 y dEstDE="Rechazado" → Generar nuevo DE con nuevo CDC
```

### 2. Obtener el XML de un DE archivado

El campo `dXmlDE` de la respuesta contiene el XML del DE almacenado en el SIFEN, lo que permite recuperar DTE archivados.

### 3. Verificar el estado tras cancelación

Después de enviar un evento de cancelación, usar `siConsDE` para confirmar que el estado del DE cambió a "Cancelado".

---

## Consulta de Lote (siConsLoteDE)

El WS `siConsLoteDE` es similar a `siConsDE` pero para consultar el estado de un lote entero por su número de lote (`dNumLote`).

### Endpoint

| Ambiente | URL |
|----------|-----|
| Pruebas | `https://sifen-test.set.gov.py/de/ws/async/resultado-lote.wsdl` |
| Producción | `https://sifen.set.gov.py/de/ws/async/resultado-lote.wsdl` |

### Request

```xml
<rConsLoteDE>
  <dId>1</dId>
  <dNumLote>98765</dNumLote>
</rConsLoteDE>
```

Ver detalles de `siResultLoteDE` en `/05-api-sifen/envio-lote.md`.
