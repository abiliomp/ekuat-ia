# Schemas XSD del Sistema SIFEN

> **Fuente:** Manual Técnico SIFEN v150, sección 7.2 y Notas Técnicas NT-010, NT-011
>
> **⚠️ Importante:** este archivo describe la numeración *documental* del MT. Los archivos XSD **realmente publicados en producción** (y sus divergencias con el MT) están documentados en [xsd-produccion-vs-manual.md](./xsd-produccion-vs-manual.md), con copias locales en [`00-fuentes/xsd/`](../00-fuentes/xsd/). Ante cualquier diferencia, **el XSD de producción es la fuente de verdad**.
>
> **Validación local sin red:** usar las copias de [`validacion-local/`](./validacion-local/) (`php validacion-local/validar.php documento.xml`): son los mismos XSD con `schemaLocation` relativos y el único fix de `dEntCont ` → `dEntCont` (ver [xsd-produccion-vs-manual.md](./xsd-produccion-vs-manual.md) §14). Para citar líneas o literales, usar siempre las copias fieles de `00-fuentes/xsd/`.

## Descripción

Los Schemas XSD definen la estructura y validación del XML de los Documentos Electrónicos y sus mensajes de intercambio con el SIFEN. A partir de la versión 150 del Manual Técnico y sus Notas Técnicas, el sistema cuenta con 22 schemas numerados como "Schema XML N°".

---

## Listado de Schemas XML según el MT v150

Numeración **documental** del propio MT (índice de "Schemas XML", PDF p. 6, y capítulos 7, 9 y 10-11). Solo los marcados con ✅ existen como archivos descargables en producción; los demás describen mensajes de los WS cuya estructura solo está en el WSDL o en las tablas del MT.

| N° (MT) | Archivo según el MT | Qué define | Publicado en producción |
|---------|---------------------|------------|-------------------------|
| 1 | `xmldsig-core-schema-v150.xsd` | Firma digital (W3C XML DSig; NT-016 amplía algoritmos) | ✅ `xmldsig-core-schema.xsd` |
| 2 | `siRecepDE_v150.xsd` | Request de siRecepDE (`rEnviDe`); el archivo publicado solo declara `rDE` | ✅ |
| 3 | `resRecepDE_v150.xsd` | Respuesta de siRecepDE (`rRetEnviDe`) | ❌ |
| 4 | `ProtProcesDE_v150.xsd` | Protocolo de procesamiento (`rProtDe`) | ❌ |
| 5 | `SiRecepLoteDE_v150.xsd` | Request de siRecepLoteDE (`rEnvioLote`) | ❌ |
| 5A | `ProtProcesLoteDE_v150.xsd` | Contenedor del lote (`rLoteDE` > `rDE` 1-50) | ❌ |
| 6 | `resRecepLoteDE_v150.xsd` | Respuesta de siRecepLoteDE (`rResEnviLoteDe`) | ❌ |
| 7 | `SiResultLoteDE_v150.xsd` | Request de siResultLoteDE (`rEnviConsLoteDe`) | ❌ |
| 8 | `resResultLoteDE_v150.xsd` | Respuesta de siResultLoteDE (`rResEnviConsLoteDe`) | ❌ |
| 9 | `siConsDE_v150.xsd` | Request de siConsDE (`rEnviConsDe`) | ❌ |
| 10 | `resConsDE_v150.xsd` | Respuesta de siConsDE (`rResEnviConsDe`) | ❌ |
| 11 | `ContenedorDE_v150.xsd` | Contenedor del DE consultado (`rContDe`) | ❌ |
| 12 | `ContenedorEvento_v150.xsd` | Contenedor de evento (`rContEv`) | ❌ |
| 13 | `siRecepEvento_v150.xsd` | Request de siRecepEvento (`rEnviEventoDe`); el archivo publicado solo declara `gGroupGesEve` | ✅ |
| 14 | `resRecepEvento_v150.xsd` | Respuesta de siRecepEvento (`rRetEnviEventoDe`) | ❌ |
| 15 | `siConsRUC_v150.xsd` | Request de siConsRUC (`rEnviConsRUC`) | ❌ |
| 16 | `resConsRUC_v150.xsd` | Respuesta de siConsRUC (`rResEnviConsRUC`) | ❌ |
| 17 | `ContenedorRUC_v150.xsd` | Contenedor del RUC (`rContRUC` / `xContRUC`) | ❌ |
| 18 | `DE_v150.xsd` | Documento Electrónico (`rDE`, grupos A-J) | ✅ (+ `DE_Types_v150.xsd` y catálogos) |
| 19 | `Evento_v150.xsd` | **Todos** los eventos (emisor, receptor, automáticos, DNIT) en un solo archivo | ✅ (+ `Evento_Types_v150.xsd`) |
| 20-22 (NT-011) | `WS_ConsultaArchivoRuc.xsd`, `siConsultaArchivoRuc.xsd` | Consulta masiva de RUC (`rEnviConsArchivoRUCRequest` / `Response`) | ❌ |

> **Nota (verificado junio 2026, re-verificado 03/10/2026):** en producción **no existen archivos separados por evento**; todos los eventos están definidos como `complexType` dentro de `Evento_v150.xsd` (incluido vía `siRecepEvento_v150.xsd`). La numeración "Schema XML N° 9-16 por evento" que figuraba en versiones anteriores de este repositorio no es la del MT. Ver [xsd-produccion-vs-manual.md](./xsd-produccion-vs-manual.md).

---

## Paquete de Distribución

| Atributo | Valor |
|----------|-------|
| **Archivo ZIP** | `PS_FE_150.zip` |
| **URL base del namespace** | `http://ekuatia.set.gov.py/sifen/xsd` |
| **Fuente oficial** | `https://www.dnit.gov.py/web/e-kuatia/documentacion-tecnica` |
| **Versión del formato** | 150 (campo `<dVerFor>AA002</dVerFor>`) |

### URLs directas de los XSD vigentes en producción

| XSD | URL |
|-----|-----|
| Recepción DE (wrapper) | `https://ekuatia.set.gov.py/sifen/xsd/siRecepDE_v150.xsd` |
| Estructura del DE | `https://ekuatia.set.gov.py/sifen/xsd/DE_v150.xsd` |
| Tipos y enumeraciones del DE | `https://ekuatia.set.gov.py/sifen/xsd/DE_Types_v150.xsd` |
| Recepción de eventos (wrapper) | `https://ekuatia.set.gov.py/sifen/xsd/siRecepEvento_v150.xsd` |
| Estructura de eventos | `https://ekuatia.set.gov.py/sifen/xsd/Evento_v150.xsd` |
| Tipos de eventos | `https://ekuatia.set.gov.py/sifen/xsd/Evento_Types_v150.xsd` |
| Países | `https://ekuatia.set.gov.py/sifen/xsd/Paises_v100.xsd` |
| Departamentos | `https://ekuatia.set.gov.py/sifen/xsd/Departamentos_v141.xsd` |
| Monedas | `https://ekuatia.set.gov.py/sifen/xsd/Monedas_v150.xsd` |
| Unidades de medida | `https://ekuatia.set.gov.py/sifen/xsd/Unidades_Medida_v141.xsd` |
| Firma digital (W3C XMLDSig) | `https://ekuatia.set.gov.py/sifen/xsd/xmldsig-core-schema.xsd` |

Copias locales (descargadas el 11/06/2026) en [`00-fuentes/xsd/`](../00-fuentes/xsd/).

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
│   └── gCamDEAsoc   (H)     — Documentos asociados
├── Signature        (I001)  — Firma digital XML DSig (ds:Signature, hijo de rDE; no existe ningún grupo "gIniSeg")
└── gCamFuFD         (J)     — Campos fuera de la firma
    └── dCarQR                — URL del código QR
```

---

## Schema de Eventos: `siRecepEvento_v150.xsd` + `Evento_v150.xsd` (Schema XML 19)

Todos los eventos comparten un único XSD. El elemento global es `gGroupGesEve`; la estructura (XSD `Evento_v150.xsd:480-565`; MT §11.5 GDE000-GDE008) es:

```xml
<rEnviEventoDe xmlns="http://ekuatia.set.gov.py/sifen/xsd">   <!-- raíz del request del WS (GSch01), definida en el WSDL -->
  <dId>1</dId>                                                 <!-- GSch02 -->
  <dEvReg>                                                     <!-- GSch03 -->
    <gGroupGesEve xmlns="http://ekuatia.set.gov.py/sifen/xsd"> <!-- GDE000 -->
      <rGesEve>                                                <!-- GDE001, 1 a 15 -->
        <rEve Id="1">                                          <!-- GDE002; @Id = GDE003 -->
          <dFecFirma>2026-06-11T10:30:00</dFecFirma>           <!-- GDE004 -->
          <dVerFor>150</dVerFor>                               <!-- GDE005 -->
          <gGroupTiEvt>                                        <!-- GDE007: xs:choice -->
            <rGeVeCan>…</rGeVeCan>                             <!-- uno de los 9 eventos enviables -->
          </gGroupTiEvt>
        </rEve>
        <Signature xmlns="http://www.w3.org/2000/09/xmldsig#"/> <!-- GDE008: firma del rEve, Reference URI="#1" -->
      </rGesEve>
    </gGroupGesEve>
  </dEvReg>
</rEnviEventoDe>
```

### Eventos enviables (`xs:choice` de `tgGroupEvt`) y prefijos de identificadores del MT

| Elemento XSD | Tipo XSD | Prefijo MT | Evento |
|--------------|----------|------------|--------|
| `rGeVeCan` | `trGeVeCan` | GEC | Cancelación |
| `rGeVeInu` | `trGeVeInu` | GEI | Inutilización |
| `rGeVeNotRec` | `trGeVeNotRec` | GEN | Notificación de recepción |
| `rGeVeConf` | `trGeVeConf` | GCO | Conformidad |
| `rGeVeDisconf` | `trGeVeDisconf` | GDI | Disconformidad |
| `rGeVeDescon` | `trGeVeDescon` | GED | Desconocimiento |
| `rGeVeEnd` | `trGeVeEnd` | — | Endoso (sin documentación en el MT v150) |
| `rGeVeTr` | `trGeVeTr` | GET | Actualización de datos de transporte (NT-010) |
| `rGEveNom` | `trGEveNom` | GENFE | Nominación de FE (NT-014, NT-027) |

Detalle de campos, respuesta y códigos en [05-api-sifen/eventos.md](../05-api-sifen/eventos.md).

---

## Schemas de Web Services (WSDL)

Los Web Services del SIFEN usan SOAP 1.2. Los schemas de los mensajes de los WS (request y response) **no** se publican como XSD: están embebidos en cada WSDL (`<URL>?wsdl`) y descritos en las tablas del MT cap. 9. Operaciones reales (MT cap. 9; WSDL verificados 06/2026):

| WS | Operación / raíz del request | Schema request (MT) | Raíz de la respuesta | Schema response (MT) |
|----|------------------------------|---------------------|----------------------|----------------------|
| siRecepDE | `rEnviDe` | 2 | `rRetEnviDe` > `rProtDe` | 3 y 4 |
| siRecepLoteDE | `rEnvioLote` (ZIP con `rLoteDE`) | 5 y 5A | `rResEnviLoteDe` | 6 |
| siResultLoteDE | `rEnviConsLoteDe` | 7 | `rResEnviConsLoteDe` | 8 |
| siConsDE | `rEnviConsDe` (mensaje WSDL `rEnviConsDeRequest`) | 9 | `rResEnviConsDe` (`rEnviConsDeResponse`) > `xContenDE` | 10, 11 y 12 |
| siRecepEvento | `rEnviEventoDe` | 13 (+ 19) | `rRetEnviEventoDe` | 14 |
| siConsRUC | `rEnviConsRUC` | 15 | `rResEnviConsRUC` > `xContRUC` | 16 y 17 |
| siConsArchivoRUC (NT-011) | `rEnviConsArchivoRUCRequest` | 20 y 21 | `rEnviConsArchivoRUCResponse` | 22 |

> No existe un WS "siConsLoteDE": la consulta del lote es siResultLoteDE. Las operaciones `rRecepDE`, `rRecepLoteDE`, `rResultLoteDE`, `rConsDE`, `rConsLoteDE`, `rRecepEvento`, `rConsRUC` y `rConsArchivoRUC` que figuraban aquí **no existen** (corregido el 03/10/2026).

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
| NT-010 | Evento GET (actualización de transporte) incorporado a `Evento_v150.xsd` (`trGeVeTr`); elimina el **valor 2** del campo A005 `dSisFact` (el campo sigue siendo obligatorio, solo acepta 1) |
| NT-011 | Nuevos schemas XML N° 20, 21, 22 para siConsArchivoRUC (no publicados en producción) |
| NT-014 | Evento GENFE (nominación de FE) incorporado a `Evento_v150.xsd` (`trGEveNom`) |
| NT-016 | Cambios en el schema de firma digital: algoritmos adicionales, métodos C14N |
| NT-018 | Nuevo grupo D1.1 (obligaciones afectadas) en Schema XML N° 1 |
| NT-023 | Modificaciones en E711 (precisión decimal), E791 (ocurrencias), H018 |
| NT-027 | Evento GENFE: código de Tarjeta Diplomática pasa de 5 a 6 en GENFE010/GENFE011 |
