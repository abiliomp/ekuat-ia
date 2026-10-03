# Recepción Sincrónica de DE (siRecepDE)

> **Fuente:** Manual Técnico SIFEN v150, §9.1 "WS recepción DE" (PDF pp. 46-47: Schemas XML 2, 3 y 4, identificadores ASch0x, ARSch0x y PP0x), §7.10 (PDF p. 42, direcciones) y §12.3.1 (PDF p. 155, códigos BA01/BC01); `00-fuentes/xsd/siRecepDE_v150.xsd` (define el elemento `rDE`); respuesta real confirmada con el código homologado de PKuatia contra `sifen-test` (FE aprobada, junio 2026).
>
> **Reescrito el 03/10/2026 (Fase 0).** La versión anterior de este archivo describía una respuesta `gResProcDE` / `gResOK` / `gResNOk` / `gDetMotErr` / `gResObs` con códigos 0302, 0304, 0306, 0400, 0401 y 0500 que **no existen** en el MT v150 ni en ningún XSD ni WSDL del SIFEN. No usar esos nombres ni códigos.

## Descripción

El WS `siRecepDE` recibe **un único** Documento Electrónico firmado y devuelve en la misma llamada HTTP el protocolo de procesamiento con el resultado (aprobado, aprobado con observación o rechazado). Es el servicio a usar cuando se necesita confirmación inmediata; para volumen, usar el lote ([envio-lote.md](./envio-lote.md)).

---

## Características

| Atributo | Valor | Fuente |
|----------|-------|--------|
| **Proceso** | Síncrono | MT §9.1 |
| **DE por llamada** | 1 | MT §9.1 (ASch03, ocurrencia 1-1) |
| **Tamaño máximo del mensaje** | 1.000 KB; si se supera, código **0200** (BA01) | MT §12.3.1.1 |
| **Operación SOAP** | `rEnviDe` (nombre del elemento raíz del request y de la operación del WSDL, verificado contra el WSDL de `sifen-test` en 06/2026) | MT §9.1.1 (ASch01); WSDL |
| **Protocolo** | SOAP 1.2 (`http://www.w3.org/2003/05/soap-envelope`), TLS 1.2 con certificado de cliente | MT §9.1 ejemplo (PDF p. 36); [autenticacion.md](./autenticacion.md) |
| **Namespace** | `http://ekuatia.set.gov.py/sifen/xsd` (request, response y `rDE`) | MT §9.1; XSD |

---

## Endpoints

| Ambiente | URL (agregar `?wsdl` para obtener el WSDL) | Fuente |
|----------|-----|--------|
| Pruebas | `https://sifen-test.set.gov.py/de/ws/sync/recibe.wsdl` | MT §7.10 (allí figura con el error tipográfico `recibe.wsd`); verificado en 06/2026 |
| Producción | `https://sifen.set.gov.py/de/ws/sync/recibe.wsdl` | MT §7.10 |

Ver [endpoints.md](./endpoints.md) para el detalle de rutas verificadas y las que **no** existen.

---

## Estructura del Request (Schema XML 2 — `siRecepDE_v150.xsd`)

| ID | Campo | Padre | Tipo | Long. | Ocu. | Descripción |
|----|-------|-------|------|-------|------|-------------|
| ASch01 | `rEnviDe` | — | — | — | — | Elemento raíz |
| ASch02 | `dId` | ASch01 | N | 1-15 | 1-1 | Número secuencial autoincremental que identifica el mensaje; lo genera y controla el contribuyente |
| ASch03 | `xDE` | ASch01 | XML | — | 1-1 | El `rDE` firmado completo, embebido como XML (no como texto escapado ni Base64) |

> El XSD publicado `siRecepDE_v150.xsd` solo declara el elemento `rDE` (incluye `DE_v150.xsd`); la envoltura `rEnviDe`/`xDE` está definida en el WSDL, no en un XSD descargable. En el WSDL verificado en 06/2026 `xDE` es de tipo *anyXML*.

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Header/>
  <soap:Body>
    <rEnviDe xmlns="http://ekuatia.set.gov.py/sifen/xsd">
      <dId>10000011111111</dId>
      <xDE>
        <rDE xmlns="http://ekuatia.set.gov.py/sifen/xsd"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://ekuatia.set.gov.py/sifen/xsd siRecepDE_v150.xsd">
          <dVerFor>150</dVerFor>
          <DE Id="[CDC_44]">
            <!-- grupos A a H -->
          </DE>
          <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
            <!-- firma enveloped sobre el elemento DE (Reference URI="#[CDC_44]") -->
          </Signature>
          <gCamFuFD>
            <dCarQR>[URL_QR]</dCarQR>
          </gCamFuFD>
        </rDE>
      </xDE>
    </rEnviDe>
  </soap:Body>
</soap:Envelope>
```

(Ejemplo del MT §9.1, PDF p. 36, normalizado: el PDF escribe `<soap:body>` en minúscula y marca en amarillo `soap:Body`.)

---

## Estructura de la Response (Schemas XML 3 y 4 — `rRetEnviDe` / `rProtDe`)

| ID | Campo | Padre | Tipo | Long. | Ocu. | Descripción (MT §9.1.3) |
|----|-------|-------|------|-------|------|-------------|
| ARSch01 | `rRetEnviDe` | — | — | — | — | Elemento raíz de la respuesta |
| ARSch02 | `rProtDe` | ARSch01 | XML | — | 1-1 | Protocolo de procesamiento del DE (el MT lo llama `xProtDe` en la tabla ARSch02 y `rProtDe` en el Schema XML 4 y en el ejemplo; **la respuesta real usa `rProtDe`**) |
| PP02 | `id` | PP01 | A | 44 | 1-1 | CDC del DE procesado (el ejemplo del MT en la p. 36 escribe `dId`; la respuesta real y el código homologado usan `id`) |
| PP03 | `dFecProc` | PP01 | D | 19 | 1-1 | Fecha y hora del procesamiento. El MT indica `AAAA-MM-DDThh:mm:ss`; en las respuestas reales del lote y de la consulta (guía de mejores prácticas) viene con zona horaria (`2024-10-08T14:51:21-03:00`). Formato exacto en `siRecepDE`: `[PENDIENTE DE VERIFICACIÓN]` |
| PP04 | `dDigVal` | PP01 | — | 28 | 1-1 | `DigestValue` del DE procesado (Base64), para cotejar con el enviado |
| PP050 | `dEstRes` | ver nota | A | 8-30 | 1-1 | [MODIFICADO] Estado del resultado: `Aprobado`, `Aprobado con observación`, `Rechazado` |
| PP051 | `dProtAut` | ver nota | N | 10 | 0-1 | [MODIFICADO] Número de transacción (protocolo de autorización). Solo cuando el DE fue aprobado |
| PP05 | `gResProc` | PP01 | G | — | 1-100 | [MODIFICADO] Grupo resultado de procesamiento. "Para producción se limitará a 5 mensajes máximos sin modificación de esta especificación" |
| PP052 | `dCodRes` | PP05 | N | 4 | 1-1 | Código de resultado (ver abajo) |
| PP053 | `dMsgRes` | PP05 | A | 1-255 | 1-1 | Mensaje del resultado |

> **Nota sobre la ubicación de `dEstRes` y `dProtAut`.** La tabla del MT (PP050/PP051, "Nodo Padre" = PP05) y su ejemplo de la p. 36 los ubican **dentro** de `gResProc`. En la respuesta real del SIFEN son **hermanos** de `gResProc`, hijos directos de `rProtDe`: así lo parsea el código homologado de PKuatia (`RProtDe::FromSimpleXMLElement`) y así aparece la estructura análoga `gResProcLote` en la respuesta real de la consulta de lote publicada en la guía de mejores prácticas (`id`, `dEstRes`, `gResProc{dCodRes, dMsgRes}`). Se documenta la forma real:

```xml
<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope">
  <env:Header/>
  <env:Body>
    <ns2:rRetEnviDe xmlns:ns2="http://ekuatia.set.gov.py/sifen/xsd">
      <ns2:rProtDe>
        <ns2:id>[CDC_44]</ns2:id>
        <ns2:dFecProc>2026-06-11T10:30:00-04:00</ns2:dFecProc>
        <ns2:dDigVal>[DigestValue_Base64_28]</ns2:dDigVal>
        <ns2:dEstRes>Aprobado</ns2:dEstRes>
        <ns2:dProtAut>[NUMERO_10_DIGITOS]</ns2:dProtAut>
        <ns2:gResProc>
          <ns2:dCodRes>0260</ns2:dCodRes>
          <ns2:dMsgRes>Autorización del DE satisfactoria</ns2:dMsgRes>
        </ns2:gResProc>
      </ns2:rProtDe>
    </ns2:rRetEnviDe>
  </env:Body>
</env:Envelope>
```

Rechazo (ejemplo del MT, PDF p. 36, con la ubicación real de `dEstRes`):

```xml
<ns2:rProtDe>
  <ns2:id>[CDC_44]</ns2:id>
  <ns2:dFecProc>2019-06-03T12:00:00</ns2:dFecProc>
  <ns2:dDigVal>0000000000000000000000000000</ns2:dDigVal>
  <ns2:dEstRes>Rechazado</ns2:dEstRes>
  <ns2:gResProc>
    <ns2:dCodRes>0160</ns2:dCodRes>
    <ns2:dMsgRes>XML malformado</ns2:dMsgRes>
  </ns2:gResProc>
</ns2:rProtDe>
```

En un rechazo **solo se informa el primer motivo** (MT §9.3.2, mismo criterio que en el lote); en una aprobación con observaciones pueden venir hasta 100 mensajes (5 en producción). No hay `dProtAut` cuando `dEstRes` = `Rechazado`.

---

## Códigos de respuesta

Todos los códigos son de 4 dígitos y se devuelven en `gResProc/dCodRes`. La fuente completa es [08-errores-y-respuestas/respuestas-ws.md](../08-errores-y-respuestas/respuestas-ws.md) (WS) y [errores-validacion.md](../08-errores-y-respuestas/errores-validacion.md) (reglas de negocio del DE).

| Código | ID | Resultado | `dEstRes` | Fuente |
|--------|----|-----------|-----------|--------|
| **0260** | BC01 | Autorización del DE satisfactoria | `Aprobado` (o `Aprobado con observación` si además hay mensajes AO) | MT §12.3.1.3 |
| 0200 | BA01 | Mensaje de entrada superior a 1.000 KB | `Rechazado` | MT §12.3.1.1 |
| 0001-0007 | AA | Certificado de transmisión (TLS) | `Rechazado` | MT §12.2.1 |
| 0120-0122 | AC | Certificado de firma | `Rechazado` | MT §12.2.4 |
| 0140-0142 | AD | Firma digital (0141 incluye cadena, LCR y revocación; 0142 RUC del certificado ≠ emisor) | `Rechazado` | MT §12.2.5 |
| 0160-0163 | AE | Genéricos: XML malformado (0160, también cuando falla el XSD: *"El valor del elemento: X es invalido"*), servidor sin respuesta, versión no soportada | `Rechazado` | MT §12.2.6 |
| 0180, 0183 | AF | Control de llamada (HeaderMsg, RUC del certificado no activo) | `Rechazado` | MT §12.2.7 |
| 1000-2650 | A002…J003 | Validaciones de negocio del DE; `E` = R (rechazo) o AO (aprobado con observación, p. ej. 1005 transmisión extemporánea) | según columna E | MT §12.4 |

> El código 0100 ("Fallo de schema", grupo AB) fue **eliminado** en v150 (ver respuestas-ws.md); en junio de 2026 se observó un 0100 transitorio en `sifen-test` con el ambiente degradado. Tratarlo como error del servidor y reintentar más tarde, no como error del documento.

---

## Estados del DE tras la respuesta

| `dEstRes` | Significado | Acción del emisor |
|-----------|-------------|-------------------|
| `Aprobado` | El DE pasa a ser DTE. Tiene validez fiscal | Guardar `dProtAut`, `dFecProc` y la respuesta completa; entregar el KuDE al receptor |
| `Aprobado con observación` | DTE con observaciones (p. ej. extemporaneidad, código 1005) | Igual que aprobado; revisar los `gResProc` adicionales |
| `Rechazado` | No es DTE. El SIFEN no lo almacena (una consulta posterior por CDC devuelve 0420) | Corregir y reenviar. El MT no obliga a cambiar el CDC: las validaciones 1001 (CDC duplicado) y 1002 (DE duplicado) solo se disparan contra documentos **ya autorizados**, y la guía de mejores prácticas (§8) prevé reenviar el DE tras verificar que no está aprobado |

> **Nunca reenviar un CDC sin tener su resultado definitivo.** Ante un timeout, consultar primero con `siConsDE` ([consulta-estado.md](./consulta-estado.md)): 0422 = ya está aprobado (no reenviar); 0420 = no está aprobado. El reenvío de un CDC en procesamiento produce bloqueos temporales del RUC (guía de mejores prácticas, §5).

---

## Protocolo de autorización (`dProtAut`)

Número de transacción de 10 dígitos (PP051) que el SIFEN asigna al aprobar un DE. Es único por DTE, se imprime en el KuDE y vuelve en la consulta por CDC dentro de `xContenDE` (ContDE03). Guardarlo junto con el XML firmado y `dFecProc`.

---

## Buenas prácticas

1. **Validar localmente** el `rDE` antes de enviar con `php 04-schemas-xsd/validacion-local/validar.php documento.xml` (mismos XSD de producción, sin red; ver [validacion-local/](../04-schemas-xsd/validacion-local/)): es exactamente lo que valida el SIFEN y un literal distinto produce 0160.
2. **Verificar la firma** con una biblioteca local antes de enviar.
3. **Sincronizar el reloj** con `aravo1.set.gov.py` / `aravo2.set.gov.py` (MT §7.11): la fecha de firma posterior a la hora del SIFEN produce 1004.
4. **Guardar la respuesta completa** (`rProtDe`) para auditoría.
5. **Timeout**: consultar con `siConsDE` antes de reenviar.
6. **Ambiente de pruebas**: el nombre del emisor (D105) debe ser el literal exigido por la validación 1263 (ver [guia-de-pruebas.md](../10-guias/guia-de-pruebas.md) para la divergencia con la guía).
