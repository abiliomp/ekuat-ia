# Envío de Lote de DE (siRecepLoteDE) y Consulta de Resultado de Lote (siResultLoteDE)

> **Fuente:** Manual Técnico SIFEN v150, §9.2 "WS recepción lote DE" (PDF pp. 48-49: Schemas XML 5, 5A y 6, identificadores BSch0x, LSch0x, BRSch0x), §9.3 "WS consulta resultado de lote" (PDF pp. 49-51: Schemas XML 7 y 8, CSch0x, CRSch0x, Tabla F), §12.3.2 y §12.3.3 (PDF pp. 156-157); [Guía de Mejores Prácticas para la Gestión del Envío de DE](../10-guias/mejores-practicas-envio-de.md) (DNIT, octubre 2024: sobres SOAP reales, 0364, motivos de rechazo y bloqueo); envío homologado contra `sifen-test` en junio de 2026 (lote de 2 FE aprobado).
>
> **Reescrito el 03/10/2026 (Fase 0).** La versión anterior describía un request `xDELote`/`dCantRegDTE`/`dIdLote`, una respuesta con `dNumLote`, un ZIP "con un XML por DE", los WS `resultado-lote.wsdl`/`rResultLoteDE` y los códigos 0302-0305. **Nada de eso existe** en el MT ni en los WSDL. No usar.

## Descripción

El envío en lote es el mecanismo **asíncrono**: `siRecepLoteDE` encola hasta 50 DE del mismo tipo y devuelve un número de lote (`dProtConsLote`); el resultado por DE se obtiene después con `siResultLoteDE`. La DNIT recomienda este mecanismo para la operación habitual y el sincrónico para casos puntuales (guía, §3).

---

## Características del lote

| Atributo | Valor | Fuente |
|----------|-------|--------|
| **Máximo de DE por lote** | 50 | MT §9.2.1 (LSch02, ocurrencia 1-50) |
| **Mínimo** | 1 (un lote vacío provoca bloqueo temporal del RUC) | guía §5.f |
| **Tipo de documento** | Todos los DE del lote del **mismo tipo** (C002); si no, rechazo 0301 (y 0363 en la consulta) | MT §9.2.2; §12.3.3.3; guía §4.b |
| **RUC emisor** | Un solo RUC emisor por lote | guía §4.a |
| **Numeración** | No se exige que los DE sean secuenciales | MT §9.2.2 |
| **Contenedor** | Un único XML `<rLoteDE>` con los `<rDE>` firmados, comprimido en ZIP y codificado en Base64 | MT §9.2.1 (BSch03, LSch01-02); guía §6 |
| **Tamaño máximo del mensaje** | El MT fija **10.000 KB** (BD01, código 0270); la guía de 2024 dice que el mensaje "no debe superar **1000 KB**" (§4.e). Prevalece el límite menor hasta que la DNIT aclare: `[PENDIENTE DE VERIFICACIÓN]` | MT §12.3.2.1; guía §4.e |
| **Operaciones SOAP** | `rEnvioLote` (envío) y `rEnviConsLoteDe` (consulta); nombres de los elementos raíz del MT, coincidentes con los WSDL verificados en 06/2026 | MT §9.2.1, §9.3.1 |

---

## Flujo asíncrono

```
1. Firmar cada DE (rDE completo, con Signature y gCamFuFD)
2. Armar <rLoteDE> con 1..50 <rDE> del mismo tipo y mismo RUC emisor
3. Comprimir el XML del rLoteDE en un ZIP y codificarlo en Base64
4. Llamar a siRecepLoteDE (rEnvioLote)
   ├── 0300 → guardar dProtConsLote
   └── 0301 → el lote NO se procesará: corregir la causa (guía §4)
5. Esperar: comenzar a consultar a los 10 minutos y luego a intervalos ≥ 10 minutos (guía §3.4)
6. Llamar a siResultLoteDE (rEnviConsLoteDe) con dProtConsLote
   ├── 0361 → sigue en procesamiento: volver a consultar
   ├── 0362 → concluido: recorrer gResProcLote (un ítem por CDC)
   ├── 0360 → número de lote inexistente
   └── 0364 → consulta extemporánea (> 48 h): consultar cada CDC con siConsDE
```

---

## WS siRecepLoteDE — envío del lote

### Endpoint

| Ambiente | URL (agregar `?wsdl`) | Fuente |
|----------|-----|--------|
| Pruebas | `https://sifen-test.set.gov.py/de/ws/async/recibe-lote.wsdl` | MT §7.10; guía §2; verificado 06/2026 |
| Producción | `https://sifen.set.gov.py/de/ws/async/recibe-lote.wsdl` | MT §7.10; guía §2 |

### Request (Schema XML 5 — `rEnvioLote`)

| ID | Campo | Padre | Tipo | Long. | Ocu. | Descripción |
|----|-------|-------|------|-------|------|-------------|
| BSch01 | `rEnvioLote` | — | — | — | — | Elemento raíz |
| BSch02 | `dId` | BSch01 | N | 1-15 | 1-1 | Número secuencial de control del mensaje, responsabilidad del contribuyente |
| BSch03 | `xDE` | BSch01 | B | — | 1-1 | Archivo de lote comprimido, en Base64 (`base64Binary` en el WSDL). Contiene el `rLoteDE` del Schema XML 5A |

#### Contenido del ZIP (Schema XML 5A — `rLoteDE`)

| ID | Campo | Padre | Tipo | Ocu. | Descripción |
|----|-------|-------|------|------|-------------|
| LSch01 | `rLoteDE` | — | — | — | Elemento raíz del lote |
| LSch02 | `rDE` | LSch01 | XML | 1-50 | Cada DE firmado completo, "según las definiciones del capítulo Formato de los DE" |

- El ZIP contiene **un solo archivo XML** cuyo elemento raíz es `rLoteDE` y cuyos hijos son los `rDE` firmados (guía §6, pasos 1-4). **No** es "un XML por DE".
- Ni el MT ni la guía fijan el nombre del archivo dentro del ZIP. El nombre `rLoteDE.xml` fue aceptado por `sifen-test` en junio de 2026 (PKuatia). Si otros nombres son aceptados: `[PENDIENTE DE VERIFICACIÓN]`.
- `rLoteDE` no está definido en ningún XSD publicado (el Schema XML 5A `ProtProcesLoteDE_v150.xsd` del MT no se publica en `ekuatia.set.gov.py/sifen/xsd/`). Cada `rDE` conserva su propio `xmlns`; en el envío homologado el elemento `rLoteDE` se envió **sin** namespace.
- La capa SOAP debe transmitir `xDE` como `base64Binary`: si la biblioteca SOAP codifica automáticamente (p. ej. `SoapClient` de PHP), hay que pasarle el ZIP binario y **no** codificarlo antes (un doble Base64 impide descomprimir el lote).

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
               xmlns:xsd="http://ekuatia.set.gov.py/sifen/xsd">
  <soap:Header/>
  <soap:Body>
    <xsd:rEnvioLote>
      <xsd:dId>20240926</xsd:dId>
      <xsd:xDE>[Base64 del ZIP que contiene rLoteDE.xml]</xsd:xDE>
    </xsd:rEnvioLote>
  </soap:Body>
</soap:Envelope>
```

(Sobre real de la guía §6, paso 5.)

### Response (Schema XML 6 — `rResEnviLoteDe`)

| ID | Campo | Padre | Tipo | Long. | Ocu. | Descripción |
|----|-------|-------|------|-------|------|-------------|
| BRSch01 | `rResEnviLoteDe` | — | — | — | — | Elemento raíz |
| BRSch02 | `dFecProc` | BRSch01 | D | 19 | 1-1 | Fecha y hora de recepción. El MT indica `AAAA-MM-DDThh:mm:ss`; la respuesta real trae zona horaria: `2024-10-08T14:51:21-03:00` (guía §6) |
| BRSch03 | `dCodRes` | BRSch01 | N | 4 | 1-1 | 0300 o 0301 |
| BRSch04 | `dMsgRes` | BRSch01 | A | 1-255 | 1-1 | Mensaje |
| BRSch05 | `dProtConsLote` | BRSch01 | N | 1-15 (MT) | 0-1 | Número de lote; solo si `dCodRes` = 0300. **La respuesta real tiene 17 dígitos** (`11158097383597290`, guía §6): tratarlo como cadena, no como entero de 32/64 bits sin verificar |
| BRSch06 | `dTpoProces` | BRSch01 | N | 1-5 | 1-1 | Tiempo medio de procesamiento de un DE en los últimos 5 minutos. La tabla BRSch06 dice **segundos**; el §8.2.2 del MT (PDF p. 44) dice **milisegundos**. Unidad real: `[PENDIENTE DE VERIFICACIÓN]` (en la respuesta real de la guía vale `0`) |

```xml
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

(Respuesta real de la guía §6, paso 6.)

### Códigos de respuesta de siRecepLoteDE

| Código | ID | Resultado | Acción | Fuente |
|--------|----|-----------|--------|--------|
| **0300** | BF01 | Lote recibido con éxito | Guardar `dProtConsLote`; consultar a partir de los 10 minutos | MT §12.3.2.3; guía §6 |
| **0301** | BF02 | Lote no encolado para procesamiento | El lote **no** se procesará. Causas en la tabla siguiente | MT §12.3.2.3; guía §4 |
| 0270 | BD01 | Mensaje de entrada superior a 10.000 KB | Reducir el lote | MT §12.3.2.1 |
| 0001-0183 | AA-AF | Validaciones genéricas (TLS, firma, XML malformado, control de llamada) | Ver [respuestas-ws.md](../08-errores-y-respuestas/respuestas-ws.md) | MT §12.2 |

#### Motivos de rechazo del lote (0301) — guía §4

| Motivo | Descripción |
|--------|-------------|
| a. RUC emisores distintos | Un solo RUC emisor por lote |
| b. Tipos de DE distintos | Un solo tipo de DE por lote (solo FE, solo NCE, etc.) |
| c. Más de 50 DE | Máximo 50 |
| d. RUC bloqueado | Bloqueo temporal por envío duplicado (tabla siguiente) |
| e. Tamaño superado | El mensaje de datos de entrada no debe superar 1000 KB (guía) |

#### Motivos de bloqueo temporal del RUC emisor (10 a 60 minutos según reincidencia) — guía §5

| Motivo | Descripción |
|--------|-------------|
| f. Lotes vacíos o inválidos | ZIP vacío o contenido no válido |
| g. CDC repetido en el mismo lote | El mismo CDC dos veces en un lote |
| h. CDC repetido en procesamiento | El mismo CDC en lotes distintos mientras el primero sigue en procesamiento |
| i. Lote reenviado | Enviar varias veces el mismo lote |

---

## WS siResultLoteDE — consulta del resultado

### Endpoint

| Ambiente | URL (agregar `?wsdl`) | Fuente |
|----------|-----|--------|
| Pruebas | `https://sifen-test.set.gov.py/de/ws/consultas/consulta-lote.wsdl` | MT §7.10; guía §2; verificado 06/2026 |
| Producción | `https://sifen.set.gov.py/de/ws/consultas/consulta-lote.wsdl` | MT §7.10; guía §2 |

> La ruta `/de/ws/async/resultado-lote.wsdl` que figuraba en versiones anteriores de este repositorio **no existe** (devuelve vacío) y no aparece en el MT ni en las NT.

### Request (Schema XML 7 — `rEnviConsLoteDe`)

| ID | Campo | Padre | Tipo | Long. | Ocu. | Descripción |
|----|-------|-------|------|-------|------|-------------|
| CSch01 | `rEnviConsLoteDe` | — | — | — | — | Elemento raíz |
| CSch02 | `dId` | CSch01 | N | 1-15 | 1-1 | Número secuencial de control |
| CSch03 | `dProtConsLote` | CSch01 | N | 1-15 (MT; 17 dígitos en la práctica) | 1-1 | Número de lote devuelto por `siRecepLoteDE` |

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

### Response (Schema XML 8 — `rResEnviConsLoteDe`)

| ID | Campo | Padre | Tipo | Long. | Ocu. | Descripción |
|----|-------|-------|------|-------|------|-------------|
| CRSch01 | `rResEnviConsLoteDe` | — | — | — | — | Elemento raíz |
| CRSch02 | `dFecProc` | CRSch01 | D | 19 | 1-1 | Fecha y hora del procesamiento del lote; vacío si el lote no fue procesado. Con zona horaria en la práctica |
| CRSch03 | `dCodResLot` | CRSch01 | N | 4 | 1-1 | Código de resultado **del lote** (0360-0364). Nótese el sufijo `Lot` |
| CRSch04 | `dMsgResLot` | CRSch01 | A | 1-255 | 1-1 | Mensaje del lote |
| CRSch05 | `gResProcLote` | CRSch01 | G | — | 0-50 | [MODIFICADO] Un grupo por DE del lote; presente cuando `dCodResLot` = 0362 |
| CRSch050 | `id` | CRSch05 | A | 44 | 1-1 | CDC del DE |
| CRSch051 | `dEstRes` | CRSch05 | A | 8-30 | 1-1 | `Aprobado`, `Aprobado con observación`, `Rechazado` |
| CRSch052 | `dProtAut` | CRSch05 | N | 10 | 0-1 | Protocolo de autorización, solo si el DE fue aprobado |
| CRSch053 | `gResProc` | CRSch05 | G | — | 1-100 | Mensajes del DE: si es rechazo, solo el primero; si es aprobación con observaciones, hasta 100 (5 en producción) |
| CRSch054 | `dCodRes` | CRSch053 | N | 4 | 1-1 | Código de resultado **del DE** (0260, 1000-2650, 0160…) |
| CRSch055 | `dMsgRes` | CRSch053 | A | 1-255 | 1-1 | Mensaje del DE |

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

(Respuesta real de la guía §7. Un DE aprobado trae además `<ns2:dProtAut>` entre `dEstRes` y `gResProc`, con `dCodRes` 0260.)

### Códigos de respuesta de siResultLoteDE (`dCodResLot`)

| Código | ID | Resultado | Acción | Fuente |
|--------|----|-----------|--------|--------|
| 0360 | BI01 | Número de lote inexistente | Verificar `dProtConsLote` | MT §12.3.3.3, Tabla F |
| 0361 | BI02 | Lote en procesamiento | Volver a consultar a intervalos ≥ 10 minutos | MT §12.3.3.3; guía §7 |
| **0362** | BI03 | Procesamiento de lote concluido | Recorrer `gResProcLote` | MT §12.3.3.3 |
| 0363 | BI04 | Lotes con tipos distintos de DE | Reenviar separando por tipo | MT §12.3.3.3 (el PDF escribe "B104") |
| 0364 | — | Consulta extemporánea de lote (> 48 h desde el envío) | Consultar cada CDC con `siConsDE` | guía §7 (no está en el MT v150) |
| 0320 | BG01 | Mensaje de entrada superior a 1.000 KB | — | MT §12.3.3.1 |
| 0340 | BH01 | RUC del certificado no autorizado a consultar el lote (solo el RUC que transmitió puede consultar) | — | MT §12.3.3.2 |

Los códigos **por DE** dentro de `gResProcLote/gResProc/dCodRes` son los mismos que en el envío sincrónico: 0260 aprobado y 1000-2650 / 0160 para los rechazos ([recepcion-de.md](./recepcion-de.md), [errores-validacion.md](../08-errores-y-respuestas/errores-validacion.md)).

---

## Tiempos y buenas prácticas (guía de mejores prácticas, §3)

| Parámetro | Valor | Fuente |
|-----------|-------|--------|
| Procesamiento por DE | ≈ 1 segundo en condiciones normales; **de 1 a 24 horas** en momentos de alta carga | guía §3.4 |
| Primera consulta | A los **10 minutos** de la recepción | guía §3.4, §6 |
| Intervalo entre consultas | **No menor a 10 minutos** | guía §3.4, §7 |
| Ventana de consulta del lote | 48 horas; después, 0364 y consulta por CDC | guía §7 |
| Tamaño sugerido del lote | Entre 30 y 50 DE en pruebas de aprobados; 3 a 5 en pruebas de rechazados | [guia-de-pruebas.md](../10-guias/guia-de-pruebas.md) §4.2 |

1. **Un tipo de DE y un RUC emisor por lote**.
2. **Validar cada `rDE` contra el XSD** antes de armar el lote: el XSD rechaza con 0160 y un lote con muchos rechazos no bloquea, pero un lote inválido o vacío sí.
3. **Guardar `dProtConsLote` como cadena** junto con la lista de CDC enviados.
4. **No consultar antes de los 10 minutos** ni más seguido que cada 10 minutos: el ambiente limita la tasa de solicitudes y bloquea temporalmente.
5. **Si no llega respuesta al enviar**, no reenviar: consultar el lote (si se tiene el número) o el CDC con `siConsDE` (guía §3.3 indica que "se puede consultar el lote usando un CDC que fue enviado en ese lote"; la forma concreta de esa consulta por CDC del lote no está documentada: `[PENDIENTE DE VERIFICACIÓN]`).
6. **Nunca reenviar un CDC** sin su resultado definitivo (Aprobado, Aprobado con observación o Rechazado).
