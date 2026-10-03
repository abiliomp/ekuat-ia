# Consulta de DE por CDC (siConsDE)

> **Fuente:** Manual Técnico SIFEN v150, §9.4 "WS consulta DE" (PDF pp. 51-53: Schemas XML 9, 10, 11 y 12, identificadores DSch0x, DRSch0x, ContDE0x, ContEv0x, Tabla G) y §12.3.4 (PDF pp. 157-158); [Guía de Mejores Prácticas](../10-guias/mejores-practicas-envio-de.md) §8 (sobres reales, octubre 2024); código homologado de PKuatia (`ConsultarDE`, aprobado contra `sifen-test` y usado en producción desde 2023).
>
> **Reescrito el 03/10/2026 (Fase 0).** La versión anterior describía `rConsDE`/`rRetConsDE`/`gConsDe`/`gDetConsDe`, los campos `dEstDE` y `dXmlDE` y los códigos 0418, 0400, 0401 y 0500, además de un "siConsLoteDE" en `resultado-lote.wsdl`. **Nada de eso existe** en el MT ni en los WSDL. No usar.

## Descripción

`siConsDE` devuelve, a partir del CDC (44 caracteres), el **XML completo del DTE aprobado** tal como lo almacena el SIFEN, junto con su protocolo de autorización y el contenedor de eventos registrados. Solo responde con contenido para DE **aprobados**: un DE rechazado o nunca recibido devuelve 0420 ("CDC inexistente" en el MT; "El DE no existe o no está aprobado" en la guía).

**No existe un campo de "estado del DE"** en la respuesta. El estado se infiere así: 0422 = existe como DTE aprobado; 0420 = no está aprobado (rechazado, no recibido o en procesamiento); la cancelación y los demás eventos se ven en `xContEv`.

---

## Características

| Atributo | Valor | Fuente |
|----------|-------|--------|
| **Proceso** | Síncrono | MT §9.4 |
| **Entrada** | CDC de 44 caracteres (`dCDC`) | MT §9.4.1 (DSch03) |
| **Salida** | Código de resultado y, si 0422, el contenedor `xContenDE` con el `rDE` firmado, `dProtAut` y eventos | MT §9.4.3 |
| **Tamaño máximo del mensaje** | 1.000 KB (BJ01, código 0380) | MT §12.3.4.1 |
| **Permiso** | Solo puede consultar el RUC del certificado con permiso sobre el DE; si no, 0421 | MT §9.4.2, Tabla G |
| **Operación SOAP** | `rEnviConsDe`; el elemento del mensaje de request en el WSDL es `rEnviConsDeRequest` y el de la respuesta `rEnviConsDeResponse` (guía §8, verificado 06/2026) | MT §9.4.1; guía §8 |

---

## Endpoints

| Ambiente | URL (agregar `?wsdl`) | Fuente |
|----------|-----|--------|
| Pruebas | `https://sifen-test.set.gov.py/de/ws/consultas/consulta.wsdl` | MT §7.10; guía §2; verificado 06/2026 |
| Producción | `https://sifen.set.gov.py/de/ws/consultas/consulta.wsdl` | MT §7.10; guía §2 |

---

## Request (Schema XML 9 — `rEnviConsDe`)

| ID | Campo | Padre | Tipo | Long. | Ocu. | Descripción |
|----|-------|-------|------|-------|------|-------------|
| DSch01 | `rEnviConsDe` | — | — | — | — | Elemento raíz según el MT. **En el WSDL real el elemento se llama `rEnviConsDeRequest`** (guía §8) |
| DSch02 | `dId` | DSch01 | N | 1-15 | 1-1 | Número secuencial de control |
| DSch03 | `dCDC` | DSch01 | C | 44 | 1-1 | CDC del DE a consultar |

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
               xmlns:xsd="http://ekuatia.set.gov.py/sifen/xsd">
  <soap:Header/>
  <soap:Body>
    <xsd:rEnviConsDeRequest>
      <xsd:dId>12</xsd:dId>
      <xsd:dCDC>01028052080001001000013622023100111644108186</xsd:dCDC>
    </xsd:rEnviConsDeRequest>
  </soap:Body>
</soap:Envelope>
```

(Sobre real de la guía §8.)

---

## Response (Schema XML 10 — `rResEnviConsDe`)

| ID | Campo | Padre | Tipo | Long. | Ocu. | Descripción |
|----|-------|-------|------|-------|------|-------------|
| DRSch01 | `rResEnviConsDe` | — | — | — | — | Elemento raíz según el MT. **En el WSDL real el elemento de respuesta es `rEnviConsDeResponse`** (guía §8) |
| DRSch02 | `dFecProc` | DRSch01 | D | 19 | 1-1 | Fecha y hora del procesamiento; en la práctica con zona horaria (`2023-10-02T15:13:52-03:00`) |
| DRSch03 | `dCodRes` | DRSch01 | N | 4 | 1-1 | 0420, 0421 o 0422 |
| DRSch04 | `dMsgRes` | DRSch01 | C | 1-255 | 1-1 | Mensaje |
| DRSch05 | `xContenDE` | DRSch01 | XML | — | 0-1 | Contenedor del DE. **Existe solamente si `dCodRes` = 0422**. Definido en el Schema XML 11 |

### Contenedor del DE (Schema XML 11 — `rContDe`) y de eventos (Schema XML 12 — `rContEv`)

| ID | Campo | Padre | Tipo | Ocu. | Descripción (MT) |
|----|-------|-------|------|------|-------------|
| ContDE01 | `rContDe` | DRSch01 | — | — | Raíz del contenedor según el MT (ver nota sobre la forma real) |
| ContDE02 | `rDE` | ContDE01 | XML | 1-1 | El DE firmado completo (con `Signature` y `gCamFuFD`) |
| ContDE03 | `dProtAut` | ContDE01 | — | 1-1 | Protocolo de autorización recibido al aprobar el DE (`siRecepDE` o `siResultLoteDE`) |
| ContDE04 | `xContEv` | ContDE01 | XML | 0-n | Contenedor de eventos: "todos los eventos registrados (contenedor montado por la SET) o disponibles (contenedor montado por el emisor) hasta la fecha" |
| ContEv01 | `rContEv` | — | — | — | Raíz de cada evento |
| ContEv02 | `xEvento` | ContEv01 | XML | 1-1 | El XML del evento (capítulo 11; en la práctica el `rGesEve` firmado) |
| ContEv03 | `rResEnviEventoDe` | ContEv01 | XML | — | Respuesta del WS de recepción del evento (Schema XML 14, `rRetEnviEventoDe`) |

> **Forma real observada (producción, PKuatia desde 2023).** `xContenDE` **no** trae el envoltorio `rContDe`: sus hijos directos son `<rDE …>…</rDE>`, `<dProtAut>…</dProtAut>` y `<xContEv>…</xContEv>`, por lo que su contenido tiene varias raíces y no se puede cargar tal cual en un parser XML; hay que recortar el `rDE` **byte a byte** (cualquier re-serialización invalida la firma). `xContEv` llega vacío cuando el DTE no tiene eventos. La forma exacta de `xContEv` **con** eventos (si `rContEv` contiene `xEvento` > `rGesEve` y `rResEnviEventoDe` > `rRetEnviEventoDe`, como asume el parser de PKuatia, y cuántos `rContEv` llegan) está `[PENDIENTE DE VERIFICACIÓN]`: no hay una respuesta real archivada.

```xml
<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope">
  <env:Header/>
  <env:Body>
    <ns2:rEnviConsDeResponse xmlns:ns2="http://ekuatia.set.gov.py/sifen/xsd">
      <ns2:dFecProc>2023-10-02T15:13:52-03:00</ns2:dFecProc>
      <ns2:dCodRes>0422</ns2:dCodRes>
      <ns2:dMsgRes>CDC encontrado</ns2:dMsgRes>
      <ns2:xContenDE>
        <rDE xmlns="http://ekuatia.set.gov.py/sifen/xsd" ...>…</rDE>
        <dProtAut>3409990272</dProtAut>
        <xContEv></xContEv>
      </ns2:xContenDE>
    </ns2:rEnviConsDeResponse>
  </env:Body>
</env:Envelope>
```

(Envoltura y cabecera de la respuesta real de la guía §8; contenido de `xContenDE` según lo observado en producción. Los namespaces exactos de los hijos de `xContenDE` no están documentados: `[PENDIENTE DE VERIFICACIÓN]`.)

Respuesta sin contenido:

```xml
<ns2:rEnviConsDeResponse xmlns:ns2="http://ekuatia.set.gov.py/sifen/xsd">
  <ns2:dFecProc>2026-06-11T10:30:00-04:00</ns2:dFecProc>
  <ns2:dCodRes>0420</ns2:dCodRes>
  <ns2:dMsgRes>CDC inexistente</ns2:dMsgRes>
</ns2:rEnviConsDeResponse>
```

---

## Códigos de respuesta

| Código | Resultado | Fuente | Observación |
|--------|-----------|--------|-------------|
| 0420 | CDC inexistente / "El DE no existe o no está aprobado" | MT §9.4.2 Tabla G y §12.3.4.3 (BL01); guía §8 | También para DE rechazados o aún en procesamiento |
| 0421 | RUC del certificado utilizado en la conexión **sin permiso** para consultar el DE | MT §9.4.2 Tabla G | Ver nota |
| **0422** | **CDC encontrado**: existe como DTE aprobado; `xContenDE` presente | MT §9.4.2 Tabla G; guía §8 (respuesta real); homologación PKuatia | Ver nota |
| 0380 | Mensaje de entrada superior a 1.000 KB | MT §12.3.4.1 (BJ01) | |
| 0001-0183 | Validaciones genéricas (TLS, firma, control de llamada) | MT §12.2 | |

> **Nota 0421/0422.** La tabla 12.3.4.3 del MT (PDF p. 158, sin marcas de color) asigna **BL02 "CDC Encontrado" = 0421** y no lista el caso "sin permiso". La Tabla G del mismo MT (§9.4.2, PDF p. 52) dice **0421 = RUC Certificado sin permiso** y **0422 = CDC encontrado**; la guía de la DNIT de 2024 muestra una respuesta real con `0422` / "CDC encontrado", y PKuatia consulta DE en producción desde 2023 con 0422. **Se adopta 0422 = CDC encontrado y 0421 = sin permiso**; el 0421 de la tabla 12.3.4.3 se trata como error de edición del MT. Detalle en [respuestas-ws.md](../08-errores-y-respuestas/respuestas-ws.md).

---

## Casos de uso

### 1. Verificar un DE antes de reenviarlo (timeout o corte de comunicación)

```
1. Consultar siConsDE con el CDC enviado
2. 0422 → el DE ya está aprobado: NO reenviar; guardar dProtAut y el rDE devuelto
3. 0420 → el DE no está aprobado. Si fue por lote, consultar antes el lote (0361 = aún en proceso: NO reenviar).
         Si el resultado definitivo fue rechazo o el SIFEN nunca lo recibió, corregir y reenviar
4. 0421 → el certificado usado no tiene permiso sobre ese DE
```

### 2. Recuperar el XML firmado de un DTE

El `rDE` dentro de `xContenDE` es el documento firmado original (incluye `Signature` y `gCamFuFD`). Debe extraerse sin alterar bytes para que la firma siga verificando.

### 3. Verificar el estado tras una cancelación

Tras registrar un evento de cancelación (0600), la consulta por CDC sigue devolviendo 0422 con el DTE; el evento debe aparecer dentro de `xContEv` ([eventos.md](./eventos.md)). Forma exacta: `[PENDIENTE DE VERIFICACIÓN]`.

---

## Consulta del resultado de un lote

No existe un "siConsLoteDE" separado: el resultado de un lote se consulta con **siResultLoteDE** (`rEnviConsLoteDe`, ruta `/de/ws/consultas/consulta-lote.wsdl`, 0360-0364). Ver [envio-lote.md](./envio-lote.md).
