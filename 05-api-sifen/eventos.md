# Eventos del Documento Electrónico (siRecepEvento)

> **Fuente:** `00-fuentes/xsd/siRecepEvento_v150.xsd` + `Evento_v150.xsd` + `Evento_Types_v150.xsd` (XSD de producción, re-verificados el 03/10/2026; **autoridad para nombres, tipos y ocurrencias de los campos**); Manual Técnico SIFEN v150 §9.5 "WS recepción evento" (PDF pp. 53-54: Schemas XML 13 y 14, GSch0x/GRSch0x), §11.5 "Estructura de los eventos" (PDF pp. 121-130, GDE/GEC/GEI/GEN/GCO/GDI/GED) y §12.3.6 (PDF p. 159); Notas Técnicas NT-010 (transporte), NT-014/NT-015/NT-027 (nominación), NT-019, NT-025; evento de cancelación homologado contra `sifen-test` (0600, junio 2026, PKuatia).
>
> **Reescrito el 03/10/2026 (Fase 0).** La versión anterior describía la ruta `recepcion-evento.wsdl`, la operación `rRecepEvento`, un sobre `rEnviEvento`/`xDE`/`gGroupEvento`, los campos `dFecFirmaEv`, `dIdEv`, `dMotCan`, `dCodSeg`, `dInfoInut`, `dNumIniInut`, `dSerieInut`, `dMotDisconf`, `dMotDescon`, `iTipActTrans`, una respuesta `rRetEnviEvento`/`gResEnviEvento`/`gDetMotErr` y los códigos 0700-0708, además de "un XSD por evento" (Schema XML N° 9-16). **Nada de eso existe** en el XSD ni en el MT. No usar.

## Descripción

Un evento es una ocurrencia registrada en el SIFEN que marca o modifica el estado de un DE o DTE (MT §11). Los eventos de **registro requerido** los envía el emisor o el receptor por el WS `siRecepEvento`, firmados digitalmente, en sobres de **hasta 15 eventos**. Los eventos de **registro automático** (asociación, retenciones, anticipo, remisión, eventos de la DNIT) los genera el SIFEN y solo se ven al consultar el DTE ([consulta-estado.md](./consulta-estado.md)).

Las reglas de negocio y los códigos de validación 4000-4478 están en [08-errores-y-respuestas/eventos-respuesta.md](../08-errores-y-respuestas/eventos-respuesta.md); aquí se documenta el protocolo del WS y la estructura exacta según el XSD.

---

## Eventos enviables por el WS (XSD `tgGroupEvt`, `Evento_v150.xsd:363-380`)

Solo los nueve elementos del `xs:choice` de `tgGroupEvt` son alcanzables desde `gGroupGesEve` y, por lo tanto, enviables. Los tipos `tgGroupEvtRecep`, `tgGroupEvtEmi` y `tgGroupEvtSet` del mismo XSD **no** están referenciados desde la raíz (ver [xsd-produccion-vs-manual.md](../04-schemas-xsd/xsd-produccion-vs-manual.md)).

| Elemento XSD | Tipo XSD (línea) | Evento | Actor | IDs del MT | Plazo (MT Tabla J) | Fuente del plazo |
|--------------|------------------|--------|-------|------------|--------------------|------------------|
| `rGeVeCan` | `trGeVeCan` (:17) | Cancelación | Emisor | GEC001-003 | 48 h desde la aprobación si es FE; 168 h si es AFE, NCE, NDE o NRE | MT Tabla J (v150); validaciones 4009/4010 |
| `rGeVeInu` | `trGeVeInu` (:29) | Inutilización de numeración | Emisor | GEI001-008 | Dentro de los primeros 15 días del mes siguiente al hecho y hasta el fin de vigencia del timbrado; rangos de hasta 1.000 números | MT Tabla J |
| `rGeVeNotRec` | `trGeVeNotRec` (:47) | Notificación de recepción DE/DTE | Receptor | GEN001-011 | 45 días desde la emisión | MT Tabla J; 4103 |
| `rGeVeConf` | `trGeVeConf` (:67) | Conformidad (total o parcial) | Receptor | GCO001-004 | 45 días desde la emisión | MT Tabla J |
| `rGeVeDisconf` | `trGeVeDisconf` (:80) | Disconformidad | Receptor | GDI001-004 | 45 días desde la emisión | MT Tabla J |
| `rGeVeDescon` | `trGeVeDescon` (:92) | Desconocimiento DE/DTE | Receptor | GED001-011 | 45 días desde la emisión | MT Tabla J; 4253 |
| `rGeVeEnd` | `trGeVeEnd` (:231) | Endoso | Emisor | — | El MT v150 lo lista como "3 = Endoso (futuro)" (GDE006); sin reglas publicadas. Si el SIFEN lo acepta hoy: `[PENDIENTE DE VERIFICACIÓN]` | — |
| `rGeVeTr` | `trGeVeTr` (:264) | Actualización de datos de transporte (NRE) | Emisor | GET001-030 (NT-010) | No definido | NT-010 |
| `rGEveNom` | `trGEveNom` (:382) | Nominación de FE innominada | Emisor | GENFE001-027 (NT-014) | No definido | NT-014, NT-015, NT-027 |

> Nótese la mayúscula irregular de `rGEveNom` / `trGEveNom`: es el nombre exacto del XSD.

---

## Endpoint y operación

| Ambiente | URL (agregar `?wsdl`) | Fuente |
|----------|-----|--------|
| Pruebas | `https://sifen-test.set.gov.py/de/ws/eventos/evento.wsdl` | MT §7.10; verificado 06/2026 |
| Producción | `https://sifen.set.gov.py/de/ws/eventos/evento.wsdl` | MT §7.10 |

| Atributo | Valor | Fuente |
|----------|-------|--------|
| **Operación SOAP / raíz del request** | `rEnviEventoDe` | MT §9.5.1 (GSch01); homologado |
| **Proceso** | Síncrono | MT §9.5 |
| **Eventos por mensaje** | 1 a 15 (`rGesEve` `maxOccurs="15"`) | `Evento_v150.xsd:563`; MT GDE001 |
| **Tamaño máximo del mensaje** | 1.000 KB (BS01, código 0560) | MT §12.3.6.1 |
| **Versión del formato** | `dVerFor` = `150` (el XSD también admite `141`) | `Evento_Types_v150.xsd:36-45` (`tVerFor`) |

> La ruta `/de/ws/eventos/recepcion-evento.wsdl` que figuraba en versiones anteriores de este repositorio **no existe** y no aparece en el MT ni en las NT.

---

## Estructura del request (Schema XML 13 + `siRecepEvento_v150.xsd`)

| ID | Campo | Padre | Tipo | Long. | Ocu. | Descripción | Fuente |
|----|-------|-------|------|-------|------|-------------|--------|
| GSch01 | `rEnviEventoDe` | — | — | — | — | Elemento raíz del request | MT §9.5.1 |
| GSch02 | `dId` | GSch01 | N | 1-15 | 1-1 | Número secuencial de control | MT §9.5.1 |
| GSch03 | `dEvReg` | GSch01 | XML | — | 1-1 | Evento(s) a registrar: contiene el `gGroupGesEve` | MT §9.5.1 |
| GDE000 | `gGroupGesEve` | GSch03 | G | — | 1-1 | Raíz del grupo de eventos (único elemento global de `siRecepEvento_v150.xsd`) | XSD `:9`; MT §11.5 |
| GDE001 | `rGesEve` | GDE000 | G | — | **1-15** | Un contenedor por evento: `rEve` + `ds:Signature` | `Evento_v150.xsd:546-557, 563` |
| GDE002 | `rEve` | GDE001 | G | — | 1-1 | Campos del evento, **todos dentro de la firma** | `Evento_v150.xsd:480-488` |
| GDE003 | `@Id` | GDE002 | N | 1-10 | 1-1 | **Atributo** `Id` de `rEve` (`tdIdEve`: entero 1 a 9999999999). Lo asigna el emisor; vuelve en la respuesta como `id`. Es el destino de `Reference URI="#Id"` de la firma | `Evento_v150.xsd:487`; `Evento_Types_v150.xsd:167-178` |
| GDE004 | `dFecFirma` | GDE002 | F | 19 | 1-1 | Fecha y hora de la firma, `AAAA-MM-DDThh:mm:ss` (`fecHhmmss`) | `Evento_v150.xsd:482` |
| GDE005 | `dVerFor` | GDE002 | N | 3 | 1-1 | `150` | `Evento_v150.xsd:483` |
| ~~GDE006~~ | ~~`dTiGDE`~~ | — | — | — | — | ~~Tipo de evento (1, 2, 3, 10-13)~~ **No existe en `trEve`**: el tipo `tdTiGDE` quedó huérfano en el XSD; el evento se identifica por el hijo elegido en `gGroupTiEvt` | `Evento_v150.xsd:480-488` |
| GDE007 | `gGroupTiEvt` | GDE002 | G | — | 1-1 | `xs:choice`: **exactamente uno** de los nueve elementos de la tabla anterior | `Evento_v150.xsd:484, 363-380` |
| GDE008 | `ds:Signature` | GDE001 | G | — | 1-1 | Firma XML DSig enveloped del `rEve` (hermano de `rEve`, dentro de `rGesEve`) | `Evento_v150.xsd:549-555`; MT GDE008 [MODIFICADO] |

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Header/>
  <soap:Body>
    <rEnviEventoDe xmlns="http://ekuatia.set.gov.py/sifen/xsd">
      <dId>1</dId>
      <dEvReg>
        <gGroupGesEve xmlns="http://ekuatia.set.gov.py/sifen/xsd"
                      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                      xsi:schemaLocation="http://ekuatia.set.gov.py/sifen/xsd siRecepEvento_v150.xsd">
          <rGesEve>
            <rEve Id="1">
              <dFecFirma>2026-06-11T10:30:00</dFecFirma>
              <dVerFor>150</dVerFor>
              <gGroupTiEvt>
                <rGeVeCan>
                  <Id>[CDC_44]</Id>
                  <mOtEve>Error en el monto total de la factura</mOtEve>
                </rGeVeCan>
              </gGroupTiEvt>
            </rEve>
            <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
              <SignedInfo>
                <!-- Reference URI="#1" (el @Id del rEve), transforms enveloped + exc-c14n, sha256 -->
              </SignedInfo>
              <SignatureValue>…</SignatureValue>
              <KeyInfo><X509Data><X509Certificate>…</X509Certificate></X509Data></KeyInfo>
            </Signature>
          </rGesEve>
          <!-- hasta 15 rGesEve, cada uno con su propio @Id y su propia firma -->
        </gGroupGesEve>
      </dEvReg>
    </rEnviEventoDe>
  </soap:Body>
</soap:Envelope>
```

(Estructura del MT §7 ejemplo de namespaces, PDF p. 32, completada con el XSD. En el MT el `xsi:schemaLocation` aparece sobre `rGesEve`; el XSD permite declararlo en cualquier nivel. Homologado con `@Id` = 1 y un evento por sobre; la semántica de `@Id` cuando hay varios eventos (correlativo vs. libre) no está documentada: `[PENDIENTE DE VERIFICACIÓN]`.)

---

## Campos de cada evento (según `Evento_v150.xsd`)

Tipos de dato citados de `Evento_Types_v150.xsd` (`tId` = CDC 44; `tmotEve` = texto 5-500; `fecHhmmss` = `AAAA-MM-DDThh:mm:ss`; `tiTipEve` = 1 Contribuyente / 2 No contribuyente; `tRuc` = 3-8 sin ceros a la izquierda; `tDVer` = 1 dígito; `tdNumDocId` = 1-20). Las columnas "ID MT" remiten a las tablas completas de [eventos-respuesta.md](../08-errores-y-respuestas/eventos-respuesta.md).

### Cancelación — `rGeVeCan` (`trGeVeCan`, XSD :17-27)

| Campo | Tipo | Ocu. | ID MT | Descripción |
|-------|------|------|-------|-------------|
| `Id` | `tId` | 1-1 | GEC002 | CDC del DTE a cancelar |
| `mOtEve` | `tmotEve` | 1-1 | GEC003 | Motivo (5-500 caracteres) |

Homologado: respuesta 0600 con `dEstRes` = `Aprobado`. **NT-025:** se puede cancelar aunque el receptor haya registrado conformidad (la validación 4004 fue eliminada).

### Inutilización — `rGeVeInu` (`trGeVeInu`, XSD :29-45)

| Campo | Tipo | Ocu. | ID MT | Descripción |
|-------|------|------|-------|-------------|
| `dNumTim` | `tdNumTim` | 1-1 | GEI002 | Timbrado (8 dígitos) |
| `dEst` | `tdEst` | 1-1 | GEI003 | Establecimiento (3, con ceros a la izquierda) |
| `dPunExp` | `tdPunExp` | 1-1 | GEI004 | Punto de expedición (3) |
| `dNumIn` | `tdNumDE` | 1-1 | GEI005 | Número inicial del rango (7 dígitos, patrón `0+[1-9][0-9]*\|[1-9]+[0-9]+`) |
| `dNumFin` | `tdNumDE` | 1-1 | GEI006 | Número final (rango ≤ 1.000; validaciones 4067/4068) |
| `iTiDE` | `tiTiDEEv` | 1-1 | GEI007 | Tipo de DE: 1-9 (9 = Boleta de venta electrónica; el MT lista 1-8) |
| `mOtEve` | `tmotEve` | 1-1 | GEI008 | Motivo |
| `dSerieNum` | `tserieNum` | 0-1 | — | Serie (2 letras); **no figura en el MT**, sí en el XSD |

### Notificación de recepción — `rGeVeNotRec` (`trGeVeNotRec`, XSD :47-65)

| Campo | Tipo | Ocu. | ID MT | Descripción |
|-------|------|------|-------|-------------|
| `Id` | `tId` | 1-1 | GEN002 | CDC |
| `dFecEmi` | `fecHhmmss` | 1-1 | GEN003 | Fecha y hora de emisión del DE (para el plazo de 45 días) |
| `dFecRecep` | `fecHhmmss` | 1-1 | GEN004 | Fecha y hora de recepción (≥ emisión, validación 4104) |
| `iTipRec` | `tiTipEve` | 1-1 | GEN005 | 1 Contribuyente / 2 No contribuyente |
| `dNomRec` | `tdNomRec` | 1-1 | GEN006 | Nombre o razón social del receptor |
| `dRucRec`, `dDVRec` | `tRuc`, `tDVer` | 0-1 | GEN007-008 | Solo si `iTipRec` = 1 (4105-4108) |
| `dTipIDRec` | `tiTipDocRec` (`[1-6]\|9`) | 0-1 | GEN009 | Solo si `iTipRec` = 2; códigos de D208 (NT-027: 6 = Tarjeta Diplomática) |
| `dNumID` | `tdNumDocId` | 0-1 | GEN010 | Solo si `iTipRec` = 2 |
| `dTotalGs` | `tMontoBase` | 1-1 | GEN011 [NUEVO] | Total de la operación en guaraníes |

### Conformidad — `rGeVeConf` (`trGeVeConf`, XSD :67-78)

| Campo | Tipo | Ocu. | ID MT | Descripción |
|-------|------|------|-------|-------------|
| `Id` | `tId` | 1-1 | GCO002 | CDC |
| `iTipConf` | `tiTipEve` | 1-1 | GCO003 | 1 Total / 2 Parcial |
| `dFecRecep` | **`fecHhmmss`** (fecha **y hora**) | 0-1 | GCO004 | Fecha estimada de recepción; obligatoria si parcial (4154). El MT la describe como fecha; el XSD exige `dateTime` |

Homologación (06/2026): el pipeline fue aceptado por `sifen-test`, que respondió **0143** porque la firma era del emisor y no del receptor. Ese código no está en el MT v150 (AD = 0140-0142): texto oficial `[PENDIENTE DE VERIFICACIÓN]`.

### Disconformidad — `rGeVeDisconf` (`trGeVeDisconf`, XSD :80-90)

| Campo | Tipo | Ocu. | ID MT | Descripción |
|-------|------|------|-------|-------------|
| `Id` | `tId` | 1-1 | GDI002 | CDC |
| `mOtEve` | `tmotEve` | 1-1 | GDI004 | Motivo |

### Desconocimiento — `rGeVeDescon` (`trGeVeDescon`, XSD :92-110)

Misma secuencia que la notificación de recepción (`Id`, `dFecEmi`, `dFecRecep`, `iTipRec`, `dNomRec`, `dRucRec`, `dDVRec`, `dTipIDRec`, `dNumID`) más `mOtEve` (GED011) y **sin** `dTotalGs`. Diferencia importante: aquí `dTipIDRec` es de tipo **`tiTipDoc` (`[1-4]`)**, no `tiTipDocRec`: el desconocimiento no admite 5 (innominado), 6 (Tarjeta Diplomática) ni 9 (otro), a diferencia de la notificación (`Evento_v150.xsd:106` vs `:61`).

### Endoso — `rGeVeEnd` (`trGeVeEnd`, XSD :231-262)

`Id`, `iTipRec`, `dNomRec`, `dRucRec`?, `dDVRec`?, `dTipIDRec`? (`tiTipDoc`), `dNumIDRec`?, `dRucEmi`, `dDVEmi`, `dNomEmi`, `dTipEnd` (`tdTipEnd`: 1 = En Venta, 2 = En Administración), `iTipFac`, `dNomFac`, `dRucFac`, `dDVFac`, `dNumCon`?, `dNumRegPubCon`?, `dTotalGs`, `dPorDes`, `dMonDesMonExt`?, `dTipCamDesMonExt`?, `dMonDesGs`, `dTotOpeEndGs`. Sin tabla ni validaciones en el MT v150 ni en las NT 001-027. Uso real: `[PENDIENTE DE VERIFICACIÓN]`.

### Actualización de datos de transporte — `rGeVeTr` (`trGeVeTr`, XSD :264-301; NT-010)

| Campo | Tipo | Ocu. | ID MT | Descripción |
|-------|------|------|-------|-------------|
| `Id` | `tId` | 1-1 | GET002 | CDC de la NRE |
| `dMotEv` | `tdMotEv` | 1-1 | GET003 | 1 Cambio del local de entrega; 2 Cambio del chofer; 3 Cambio del transportista; 4 Cambio de vehículo |
| `cDepEnt`, `dDesDepEnt`, `cDisEnt`, `dDesDisEnt`, `cCiuEnt`, `dDesCiuEnt`, `dDirEnt`, `dNumCas`, `dCompDir1` | varios | 0-1 | GET004-012 | Local de entrega (obligatorios según 4300-4310 si `dMotEv` = 1). Las descripciones son las de **departamento/distrito/ciudad** (tablas geográficas), no de país |
| `dNomChof`, `dNumIDChof` | `tdNomRec`, `tdNumDocId` | 0-1 | GET013-014 | Chofer (si `dMotEv` = 2) |
| `iNatTrans`, `dRucTrans`, `dDVTrans`, `dNomTrans`, `iTipIDTrans` (`tiTipDoc`), `dDTipIDTrans`, `dNumIDTrans` | varios | 0-1 | GET015-021 | Transportista (si `dMotEv` = 3) |
| `iTipTrans`, `dDesTipTrans`, `iModTrans`, `dDesModTrans`, `dTiVehTras`, `dMarVeh`, `dTipIdenVeh`, `dNroIDVeh`, `dNroMatVeh` | varios | 0-1 | GET022-030 | Vehículo (si `dMotEv` = 4). `dNroMatVeh` es `tdNroMatVeh`: **longitud exacta 6** (`Evento_Types_v150.xsd:524-533`) |

> El XSD contiene además un `complexType` `trGeDeVTr` (:192-229) con los mismos nombres de campo pero tipos incoherentes (fechas donde van textos); **no está referenciado** desde ningún elemento y debe ignorarse. El elemento enviable es `rGeVeTr` de tipo `trGeVeTr`.

### Nominación de FE — `rGEveNom` (`trGEveNom`, XSD :382-430; NT-014, NT-015, NT-027)

| Campo | Tipo | Ocu. | Descripción |
|-------|------|------|-------------|
| `Id` | `tId` | 1-1 | CDC de la FE innominada (D208 = 5, `dNumIDRec` = 0) |
| `mOtEve` | `tmotEve` | 1-1 | Motivo |
| `iNatRec` | `tiTipEve` | 1-1 | 1 Contribuyente / 2 No contribuyente |
| `iTiOpe` | `tiTiOpeEv` (`[1-2]\|[4]`) | 1-1 | 1 B2B, 2 B2C, 4 B2F. **El 3 (B2G) no es válido** (`Evento_Types_v150.xsd:57-66`) |
| `cPaisRec`, `dDesPaisRe` | `paisType`, `tDesPais` | 1-1 | País del receptor |
| `iTiContRec` | `tiTipCont` | 0-1 | Tipo de contribuyente |
| `dRucRec`, `dDVRec` | `tRuc`, `tDVer` | 0-1 | Si contribuyente |
| `iTipIDRec` | `tiTipDocRec` (`[1-6]\|9`) | 0-1 | Si no contribuyente. **NT-027:** 6 = Tarjeta Diplomática de exoneración fiscal (antes 5) |
| `dDTipIDRec` | `tdDtipDocRec` | 0-1 | Literal de D209 o texto libre de 9-41 caracteres cuando `iTipIDRec` = 9 |
| `dNumIDRec` | `tdNumDocId` | 0-1 | Número de documento |
| `dNomRec` | `tdNomRec` | 1-1 | Nombre o razón social |
| `dNomFanRec`, `dDirRec`, `dNumCasRec`, `cDepRec`, `dDesDepRec`, `cDisRec`, `dDesDisRec`, `cCiuRec`, `dDesCiuRec`, `dTelRec`, `dCelRec`, `dEmailRec` | varios | 0-1 | Datos del receptor (como D2 del DE) |
| `dCodCliente` | texto 3-15 | 0-1 | Código interno del cliente |

**NT-015:** las NCE/NDE emitidas contra una FE nominada deben referenciar el CDC de la FE original (validación H004i).

---

## Respuesta del WS (Schema XML 14 — `rRetEnviEventoDe`)

| ID | Campo | Padre | Tipo | Long. | Ocu. | Descripción |
|----|-------|-------|------|-------|------|-------------|
| GRSch01 | `rRetEnviEventoDe` | — | — | — | — | Elemento raíz |
| GRSch02 | `dFecProc` | GRSch01 | D | 19 | 1-1 | Fecha y hora del procesamiento del último evento. El MT la marca [MODIFICADO] con el formato `AAAA-MM-DD-hh:mm:ss-ss:ss` (sic). Formato real: `[PENDIENTE DE VERIFICACIÓN]` (PKuatia la parsea como ISO 8601 con zona) |
| GRSch03 | `gResProcEVe` | GRSch01 | G | — | **1-15** | [MODIFICADO] Un grupo por evento enviado |
| GRSch030 | `dEstRes` | GRSch03 | A | 8-30 | 1-1 | `Aprobado`, `Aprobado con observación`, `Rechazado` |
| GRSch031 | `dProtAut` | GRSch03 | N | 10 | 0-1 | Número de transacción; solo si `dCodRes` = 0600 |
| GRSch032 | `id` | GRSch03 | N | 10 | 1-1 | El `@Id` del `rEve` correspondiente, "autogenerado por el emisor" |
| GRSch033 | `gResProc` | GRSch03 | G | — | 1-100 | Mensajes (5 máximo en producción) |
| GRSch034 | `dCodRes` | GRSch033 | N | 4 | 1-1 | Código |
| GRSch035 | `dMsgRes` | GRSch033 | A | 1-255 | 1-1 | Mensaje |

```xml
<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope">
  <env:Header/>
  <env:Body>
    <ns2:rRetEnviEventoDe xmlns:ns2="http://ekuatia.set.gov.py/sifen/xsd">
      <ns2:dFecProc>2026-06-11T10:30:05-04:00</ns2:dFecProc>
      <ns2:gResProcEVe>
        <ns2:dEstRes>Aprobado</ns2:dEstRes>
        <ns2:dProtAut>[NUMERO_10_DIGITOS]</ns2:dProtAut>
        <ns2:id>1</ns2:id>
        <ns2:gResProc>
          <ns2:dCodRes>0600</ns2:dCodRes>
          <ns2:dMsgRes>Evento registrado correctamente</ns2:dMsgRes>
        </ns2:gResProc>
      </ns2:gResProcEVe>
    </ns2:rRetEnviEventoDe>
  </env:Body>
</env:Envelope>
```

(Estructura según MT §9.5.3; orden de los hijos y literal de `dMsgRes` según el MT, no confirmados contra una respuesta real archivada: `[PENDIENTE DE VERIFICACIÓN]`.)

### Códigos de respuesta

| Código | ID | Resultado | Fuente |
|--------|----|-----------|--------|
| **0600** | BU01 | Evento registrado correctamente (`dEstRes` = `Aprobado`) | MT §12.3.6.3; homologado (cancelación, 06/2026) |
| 0560 | BS01 | Mensaje de entrada superior a 1.000 KB | MT §12.3.6.1 |
| 0001-0183 | AA-AF | Validaciones genéricas (certificados, firma, XML malformado, control de llamada) | MT §12.2 |
| 0143 | — | Observado en `sifen-test` (06/2026) al enviar un evento de receptor firmado con el certificado del emisor; **no está en el MT v150** (el grupo AD termina en 0142). Texto oficial: `[PENDIENTE DE VERIFICACIÓN]` | homologación |
| 4000-4049 | GEC/GDE | Validaciones de cancelación | [eventos-respuesta.md](../08-errores-y-respuestas/eventos-respuesta.md) §11.6.1 |
| 4050-4099 | GEI | Inutilización | §11.6.2 |
| 4100-4113 | GEN | Notificación de recepción | §11.6.3 |
| 4150-4156 | GCO | Conformidad | §11.6.4 |
| 4200-4205 | GDI | Disconformidad | §11.6.5 |
| 4250-4262 | GED | Desconocimiento | §11.6.6 |
| 4300-4323 | GET | Actualización de transporte (NT-010) | §11.6.7 |
| 4451-4478 | GENFE | Nominación (NT-014/015/027) | [NT-014.md](../09-notas-tecnicas/NT-014.md) |

Como en el DE, un rechazo informa solo el primer motivo y una aprobación con observación puede traer varios `gResProc`.

---

## Eventos no enviables (solo aparecen al consultar un DTE)

Definidos en `Evento_v150.xsd` pero fuera de `tgGroupEvt`; el SIFEN los genera y los devuelve en `xContEv` ([consulta-estado.md](./consulta-estado.md)). Forma real de esa devolución: `[PENDIENTE DE VERIFICACIÓN]`.

| Elemento | Tipo (línea) | Origen | Observación |
|----------|--------------|--------|-------------|
| `rGeVeRetAce`, `rGeVeRetAnu` | `trGeVeRetAce` (:112), `trGeVeRetAnu` (:131) | Interoperabilidad (Tesaka): retención aceptada / anulada | Exigen `dRuc` y `dMonRet`, que el MT no lista; todas las fechas son `fecHhmmss` |
| `rGeVeCCFF`, `rGeDevCCFFCue`, `rGeDevCCFFDev` | `trGeVeCCFF` (:151), `trGeDevCCFF` (:175) | Créditos fiscales | — |
| `rGeVeAnt`, `rGeVeRem` | `rGeEvenAntRem` (:164) | Anticipo / remisión (asociación automática) | Solo `Id` |
| `rGeVeOA`, `rGeVePC`, `rGeVeImp`, `rGeVeDet` | `trGeVeOA` (:303), `trGeVePC` (:318), `trGeVeImp` (:333), `trGeVeDet` (:348) | DNIT: bloqueo por omisión/inconsistencias, proceso de control, impugnación, detención/multas | Fechas `formatFecha` (solo fecha); motivos en `Evento_Types_v150.xsd:555-693` |

---

## Resumen de plazos y actores (MT Tabla J, v150)

| Evento | Actor | Plazo | Condición principal |
|--------|-------|-------|---------------------|
| Cancelación | Emisor | 48 h (FE) / 168 h (AFE, NCE, NDE, NRE) desde la aprobación | DTE aprobado o aprobado con observación; con DTE asociados, cancelar del último al inicial. NT-025: también si ya hay conformidad |
| Inutilización | Emisor | Hasta el día 15 del mes siguiente; vigencia del timbrado | Los números no existen en el SIFEN; rango ≤ 1.000 |
| Notificación de recepción | Receptor | 45 días desde la emisión | DE o DTE; informativo |
| Conformidad / Disconformidad | Receptor | 45 días desde la emisión | Solo DTE; conclusivos |
| Desconocimiento | Receptor | 45 días desde la emisión | DE o DTE; informativo |
| Corrección de un evento del receptor (Tabla K) | Receptor | 15 días desde el primer evento | Un solo evento de corrección por evento |
