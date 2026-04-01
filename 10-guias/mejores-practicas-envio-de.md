# Guía de Mejores Prácticas para la Gestión del Envío de DE

> **Fuente:** Recomendaciones y mejores prácticas para SIFEN — Guía para el desarrollador, Octubre 2024

## Información general

Esta guía está orientada al usuario desarrollador de servicios web de integración con SIFEN. Es una aplicación práctica de lo especificado en el Manual Técnico del Sistema de Facturación Electrónica Nacional referente a la recepción de documentos electrónicos (DE) por lotes.

**Conocimientos previos requeridos:**
- XML
- SOAP versión 1.2
- HTTP
- Protocolo de seguridad TLS versión 1.2 con autenticación mutua
- Estándar de certificado y firma digital:
  - Firma: XML Digital Signature, formato Enveloped W3C
  - Certificado: Expedido por una PSC habilitada en Paraguay, estándar `http://www.w3.org/2000/09/xmldsig#X509Data`
  - Tamaño de clave criptográfica: RSA 2048 para cifrado por software
  - Función criptográfica asimétrica: RSA
  - Función de message digest: SHA-2
  - Codificación: Base64
  - Transformaciones exigidas: Enveloped, C14N exclusivo

---

## 1. Generación de Documentos Electrónicos

Para mayor información consultar el Manual Técnico en la versión que se esté utilizando. El namespace del DE debe declararse así:

```xml
<rDE xmlns="http://ekuatia.set.gov.py/sifen/xsd"
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xsi:schemaLocation="http://ekuatia.set.gov.py/sifen/xsd siRecepDE_v150.xsd">
```

### Precauciones en la generación del XML

**NO incorporar:**

1. Espacios en blanco al inicio o al final de campos numéricos y alfanuméricos.
2. Comentarios, anotaciones y documentaciones (etiquetas `annotation` y `documentation`).
3. Caracteres de formato de archivo: line-feed, carriage return, tab, espacios entre etiquetas.
4. Prefijos en el namespace de las etiquetas.
5. Etiquetas de campos que no contengan valor (numéricas con ceros, o vacías/blancos para campos alfanuméricos), **excepto** los campos identificados como obligatorios en el MT.
6. Valores negativos o caracteres no numéricos en campos numéricos.
7. El nombre de los campos es **sensible a mayúsculas y minúsculas**. Ejemplo: `gOpeDE` es diferente de `GopeDE`, `gopede` o cualquier otra combinación.

### Prevalidador SIFEN

La DNIT dispone de una herramienta de prevalidación del DE para uso en tiempo de desarrollo:

**Prevalidador:** [https://ekuatia.set.gov.py/prevalidador/](https://ekuatia.set.gov.py/prevalidador/)

---

## 2. Generación de Lotes de Documentos Electrónicos

Los documentos electrónicos se envían al SIFEN en lotes comprimidos para procesarlos de forma asíncrona. El resultado del procesamiento debe consultarse en un momento posterior al envío.

### URLs de los Servicios Web Asíncronos

| Servicio | URL |
|---|---|
| Recepción lote DE (`recibe-lote`) | `https://{ambiente}/de/ws/async/recibe-lote.wsdl` |
| Consulta resultado lote (`consulta-lote`) | `https://{ambiente}/de/ws/consultas/consulta-lote.wsdl` |
| Consulta por CDC (`consulta`) | `https://{ambiente}/de/ws/consultas/consulta.wsdl` |

### Dominios por ambiente

| Ambiente | Dominio |
|---|---|
| Producción | `sifen.set.gov.py` |
| Test (pruebas) | `sifen-test.set.gov.py` |

Para obtener el WSDL de cada servicio, agregar `?wsdl` al final de la URL. Ejemplo:
`https://{ambiente}/de/ws/consultas/consulta-lote.wsdl?wsdl`

Los schemas XSD del SIFEN están publicados en: [http://ekuatia.set.gov.py/sifen/xsd](http://ekuatia.set.gov.py/sifen/xsd)

---

## 3. Recomendaciones para el envío asíncrono

1. **Maximizar el uso del lote:** Enviar la máxima cantidad posible de documentos en un lote (hasta 50 documentos por lote).

2. **Verificar la respuesta de recepción del lote.** Puede devolver dos códigos:
   - **0300 — Lote recibido con éxito:** el lote será procesado. Consultar el estado usando el número de lote retornado.
   - **0301 — Lote no encolado para procesamiento:** el lote NO será procesado. Ver sección "Motivos de rechazo".

3. **Consulta cuando no se recibe respuesta:** Si no se recibe respuesta del SIFEN por corte en la comunicación, se puede consultar el lote usando un CDC que fue enviado en ese lote. Esto permite obtener el estado del lote y su número correspondiente.

4. **Esperar antes de consultar:** El procesamiento de cada DE está definido en aproximadamente 1 segundo, pero en momentos de alta carga puede tardar de 1 a 24 horas. **Se recomienda comenzar a consultar pasados los 10 minutos de la recepción y luego a intervalos regulares no menores a 10 minutos.**

5. **No reenviar sin verificar:** Nunca enviar un mismo CDC sin haber obtenido la respuesta definitiva del SIFEN (Aprobado, Aprobado con Observación o Rechazado). Consultar el resultado del procesamiento del lote con el WS de consulta de lote antes de reenviar.

---

## 4. Motivos de rechazo del lote (código 0301)

La recepción de un lote puede ser rechazada (código **0301 — Lote no encolado para procesamiento**) por los siguientes motivos:

| Motivo | Descripción |
|---|---|
| a. RUC emisores distintos | Se enviaron DE con distintos RUC emisores. Se debe enviar documentos de un solo RUC emisor por lote |
| b. Tipos de DE distintos | Se enviaron DE de distintos tipos. Se debe enviar documentos de un solo tipo por lote (solo FE, solo NCE, etc.) |
| c. Más de 50 DE en el lote | El lote supera el máximo de 50 documentos permitidos |
| d. RUC bloqueado | El RUC está bloqueado por envío duplicado. Ver sección de "Motivos de bloqueo" |
| e. Tamaño superado | El tamaño del archivo comprimido supera el límite. El mensaje de datos de entrada del WS no debe superar **1000 KB** |

---

## 5. Motivos de bloqueo temporal de recepción

Las siguientes operaciones generan un **bloqueo temporal** de recepción de documentos por RUC emisor de **10 a 60 minutos**, según la cantidad de reincidencias. Este esquema puede derivar en penalizaciones en el futuro.

| Motivo | Descripción |
|---|---|
| f. Lotes vacíos o inválidos | Enviar lotes vacíos o con contenido no válido |
| g. CDC repetido en el mismo lote | Enviar el mismo CDC varias veces en un mismo lote |
| h. CDC repetido en procesamiento | Enviar el mismo CDC varias veces en lotes distintos mientras aún se encuentra en procesamiento. Antes de reenviar un DE, verificar con consulta-lote que no esté en procesamiento |
| i. Lote reenviado | Enviar varias veces un mismo lote |

---

## 6. Invocación del WS recibe-lote

Este servicio recibe el lote de DE (hasta 50 DE del mismo tipo) para procesarlos en una cola de espera. Se debe prestar atención a los namespaces especificados para cada servicio web.

### Pasos para construir el Request Body

1. Crear la estructura del lote:
```xml
<rLoteDE>
  …
</rLoteDE>
```

2. Insertar los DE firmados en la estructura:
```xml
<rLoteDE>
  <rDE>...</rDE>
  <rDE>...</rDE>
  …
</rLoteDE>
```

3. Comprimir el contenido de la estructura `rLoteDE`.
4. Convertir el contenido comprimido a Base64.
5. Crear el envelope SOAP con los namespaces especificados:

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
               xmlns:xsd="http://ekuatia.set.gov.py/sifen/xsd">
  <soap:Header/>
  <soap:Body>
    <xsd:rEnvioLote>
      <xsd:dId>20240926</xsd:dId>
      <xsd:xDE>{Aquí va el Base64 del paso 4}</xsd:xDE>
    </xsd:rEnvioLote>
  </soap:Body>
</soap:Envelope>
```

6. Verificar la respuesta de la invocación `rResEnviLoteDe`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope">
  <env:Header/>
  <env:Body>
    <ns2:rResEnviLoteDe xmlns:ns2="http://ekuatia.set.gov.py/sifen/xsd">
      <ns2:dFecProc>2024-10-08T14:51:21-03:00</ns2:dFecProc>
      <ns2:dCodRes>0300</ns2:dCodRes>
      <ns2:dMsgRes>Lote recibido con éxito</ns2:dMsgRes>
      <ns2:dProtConsLote>11158097383597290</ns2:dProtConsLote>
      <ns2:dTpoProces>0</ns2:dTpoProces>
    </ns2:rResEnviLoteDe>
  </env:Body>
</env:Envelope>
```

### Códigos de respuesta de recibe-lote

| Código | Significado | Acción |
|---|---|---|
| 0300 | Lote recibido con éxito | El lote será procesado. Consultar el estado pasados 10 minutos usando el `dProtConsLote` retornado |
| 0301 | Lote no encolado para procesamiento | El lote NO será procesado. Verificar la causa del rechazo |

---

## 7. Invocación del WS consulta-lote

Devuelve el resultado del procesamiento de cada uno de los DE contenidos en un lote. La consulta se realiza usando el campo `dProtConsLote` obtenido en la respuesta de `recibe-lote`.

### Request Body

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
               xmlns:xsd="http://ekuatia.set.gov.py/sifen/xsd">
  <soap:Header/>
  <soap:Body>
    <xsd:rEnviConsLoteDe>
      <xsd:dId>1</xsd:dId>
      <xsd:dProtConsLote>11158097383597290</xsd:dProtConsLote>
    </xsd:rEnviConsLoteDe>
  </soap:Body>
</soap:Envelope>
```

### Códigos de respuesta de consulta-lote

| Código | Significado | Acción |
|---|---|---|
| 0360 | Número del Lote inexistente | El número de lote consultado no existe |
| 0361 | Lote en procesamiento | El lote aún está siendo procesado. Consultar nuevamente a intervalos mínimos de 10 minutos |
| 0362 | Procesamiento de lote concluido | Éxito. Revisar el detalle del procesamiento por CDC en el elemento `gResProcLote` |
| 0364 | Consulta extemporánea de Lote | El plazo de consulta del lote es de hasta 48 horas posteriores al envío. Superado ese tiempo, consultar cada CDC mediante el WS Consulta DE |

### Ejemplo de respuesta con procesamiento concluido (0362)

```xml
<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope">
  <env:Header/>
  <env:Body>
    <ns2:rResEnviConsLoteDe xmlns:ns2="http://ekuatia.set.gov.py/sifen/xsd">
      <ns2:dFecProc>2024-10-08T03:58:16-03:00</ns2:dFecProc>
      <ns2:dCodResLot>0362</ns2:dCodResLot>
      <ns2:dMsgResLot>Procesamiento de lote {11444651783497640} concluido</ns2:dMsgResLot>
      <ns2:gResProcLote>
        <ns2:id>07800252985001001000311822024021016361562161</ns2:id>
        <ns2:dEstRes>Rechazado</ns2:dEstRes>
        <ns2:gResProc>
          <ns2:dCodRes>0160</ns2:dCodRes>
          <ns2:dMsgRes>XML malformado: [El valor del elemento: dDirRec es invalido, El valor del elemento: dDirLocEnt es invalido]</ns2:dMsgRes>
        </ns2:gResProc>
      </ns2:gResProcLote>
    </ns2:rResEnviConsLoteDe>
  </env:Body>
</env:Envelope>
```

---

## 8. Invocación del WS consulta (por CDC)

Devuelve el XML de un DE que está en estado aprobado. La consulta se realiza por el valor del campo `dCDC` (44 caracteres).

### Request Body

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
               xmlns:xsd="http://ekuatia.set.gov.py/sifen/xsd"
               xmlns:si="http://ekuatia.set.gov.py/sifen/xsd">
  <soap:Header/>
  <soap:Body>
    <xsd:rEnviConsDeRequest>
      <xsd:dId>12</xsd:dId>
      <xsd:dCDC>01028052080001001000013622023100111644108186</xsd:dCDC>
    </xsd:rEnviConsDeRequest>
  </soap:Body>
</soap:Envelope>
```

### Códigos de respuesta de consulta por CDC

| Código | Significado | Acción |
|---|---|---|
| 0420 | El DE no existe o no está aprobado | Se debe verificar el resultado de la consulta por lote antes de reenviar el DE |
| 0422 | Existe como DTE, está aprobado | El contenido XML del DE se retorna en el campo `xContenDE` |

### Ejemplo de respuesta exitosa (0422)

```xml
<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope">
  <env:Header/>
  <env:Body>
    <ns2:rEnviConsDeResponse xmlns:ns2="http://ekuatia.set.gov.py/sifen/xsd">
      <ns2:dFecProc>2023-10-02T15:13:52-03:00</ns2:dFecProc>
      <ns2:dCodRes>0422</ns2:dCodRes>
      <ns2:dMsgRes>CDC encontrado</ns2:dMsgRes>
      <ns2:xContenDE>{contenido XML del DE}</ns2:xContenDE>
    </ns2:rEnviConsDeResponse>
  </env:Body>
</env:Envelope>
```

---

## 9. Resumen del flujo recomendado

```
Generar DE(s) → Firmar cada DE → Armar lote (hasta 50 DEs del mismo tipo y RUC)
  ↓
recibe-lote → Guardar dProtConsLote
  ↓ (esperar mínimo 10 minutos)
consulta-lote → Verificar estado (0361 = aún procesando, volver a consultar)
  ↓ (cuando 0362 = procesado)
Revisar gResProcLote → Para cada CDC: Aprobado / Rechazado / Aprobado con observación
  ↓ (si es necesario verificar un CDC específico)
consulta (por CDC) → Obtener el XML del DTE aprobado
```

### Regla fundamental

> **Nunca reenviar un CDC sin haber obtenido su resultado definitivo.** El reenvío de CDC en procesamiento genera bloqueo temporal del RUC emisor.
