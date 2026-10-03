# Consulta de RUC (siConsRUC) y consulta masiva de RUC (NT-011)

> **Fuente:** Manual Técnico SIFEN v150, §9.6 "WS consulta RUC" (PDF pp. 54-56: Schemas XML 15, 16 y 17, identificadores RSch0x, RRSch0x, ContRUC0x, Tabla H) y §12.3.5 (PDF p. 158); Nota Técnica [NT-011](../09-notas-tecnicas/NT-011.md) (20/10/2022) para la consulta masiva; código homologado de PKuatia (`ConsultarRUC`, verificado contra `sifen-test` **y producción** en junio de 2026).
>
> **Reescrito el 03/10/2026 (Fase 0).** La versión anterior describía `rConsRUC`/`rRetConsRUC`/`gConsDatRec`/`gDetConsDatRec`, los campos `dRUCRec`, `dDVRec`, `dNomRec`, `dDirRec`, `iEsFEV`, `iEsAFEV`, un "0500 = RUC encontrado" y un formato de archivo CSV para la consulta masiva. **Nada de eso existe** en el MT ni en la NT-011. No usar.

---

## WS siConsRUC — consulta en línea de un RUC

### Características

| Atributo | Valor | Fuente |
|----------|-------|--------|
| **Proceso** | Síncrono | MT §9.6 |
| **Entrada** | RUC **sin** dígito verificador (`dRUCCons`) | MT §9.6.1 (RSch03) |
| **Salida** | Razón social, estado del RUC y si es facturador electrónico | MT §9.6.3 (Schema XML 17) |
| **Tamaño máximo del mensaje** | 1.000 KB (BM01, código 0460) | MT §12.3.5.1 |
| **Acceso** | Solo con certificado digital; el RUC debe tener permiso para usar el WS (si no, 0501) | MT §9.6.2 |
| **Operación SOAP** | `rEnviConsRUC` | MT §9.6.1 (RSch01) |

### Endpoints

| Ambiente | URL (agregar `?wsdl`) | Fuente |
|----------|-----|--------|
| Pruebas | `https://sifen-test.set.gov.py/de/ws/consultas/consulta-ruc.wsdl` | MT §7.10; verificado 06/2026 |
| Producción | `https://sifen.set.gov.py/de/ws/consultas/consulta-ruc.wsdl` | MT §7.10; verificado en producción 06/2026 |

### Request (Schema XML 15 — `rEnviConsRUC`)

| ID | Campo | Padre | Tipo | Long. | Ocu. | Descripción |
|----|-------|-------|------|-------|------|-------------|
| RSch01 | `rEnviConsRUC` | — | — | — | — | Elemento raíz |
| RSch02 | `dId` | RSch01 | N | 1-15 | 1-1 | Número secuencial de control |
| RSch03 | `dRUCCons` | RSch01 | A | 5-8 | 1-1 | RUC consultado, **sin** DV. (El tipo `tRuc` del XSD del DE admite 3-8 caracteres sin ceros a la izquierda; el MT fija 5-8 para este WS) |

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
               xmlns:xsd="http://ekuatia.set.gov.py/sifen/xsd">
  <soap:Header/>
  <soap:Body>
    <xsd:rEnviConsRUC>
      <xsd:dId>1</xsd:dId>
      <xsd:dRUCCons>80069563</xsd:dRUCCons>
    </xsd:rEnviConsRUC>
  </soap:Body>
</soap:Envelope>
```

### Response (Schema XML 16 — `rResEnviConsRUC`; Schema XML 17 — contenedor)

| ID | Campo | Padre | Tipo | Long. | Ocu. | Descripción |
|----|-------|-------|------|-------|------|-------------|
| RRSch01 | `rResEnviConsRUC` | — | — | — | — | Elemento raíz |
| RRSch02 | `dCodRes` | RRSch01 | N | 4 | 1-1 | 0500, 0501 o 0502 |
| RRSch03 | `dMsgRes` | RRSch01 | A | 1-255 | 1-1 | Mensaje |
| RRSch04 | `xContRUC` | RRSch01 | XML | — | 0-1 | Contenedor del RUC. **Existe solamente si `dCodRes` = 0502** |
| ContRUC01 | `rContRUC` | RRSch01 | — | — | — | Raíz del contenedor según el MT. **En la respuesta real los campos ContRUC02-06 son hijos directos de `xContRUC`, sin envoltorio `rContRUC`** (homologado en producción, PKuatia) |
| ContRUC02 | `dRUCCons` | ContRUC01 | A | 5-8 | 1-1 | RUC consultado |
| ContRUC03 | `dRazCons` | ContRUC01 | A | [MODIFICADO] 1-250 | 1-1 | Razón social o nombre |
| ContRUC04 | `dCodEstCons` | ContRUC01 | A | 3 | 1-1 | Código de estado del RUC: `ACT` Activo, `SUS` Suspensión temporal, `SAD` Suspensión administrativa, `BLQ` Bloqueado, `CAN` Cancelado, `CDE` Cancelado definitivo |
| ContRUC05 | `dDesEstCons` | ContRUC01 | A | [MODIFICADO] 6-25 | 1-1 | Descripción del estado (misma tabla) |
| ContRUC06 | `dRUCFactElec` | ContRUC01 | A | 1 | 1-1 | `S` = es facturador electrónico; `N` = no lo es |

```xml
<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope">
  <env:Header/>
  <env:Body>
    <ns2:rResEnviConsRUC xmlns:ns2="http://ekuatia.set.gov.py/sifen/xsd">
      <ns2:dCodRes>0502</ns2:dCodRes>
      <ns2:dMsgRes>RUC encontrado</ns2:dMsgRes>
      <ns2:xContRUC>
        <ns2:dRUCCons>80069563</ns2:dRUCCons>
        <ns2:dRazCons>[RAZON_SOCIAL]</ns2:dRazCons>
        <ns2:dCodEstCons>ACT</ns2:dCodEstCons>
        <ns2:dDesEstCons>Activo</ns2:dDesEstCons>
        <ns2:dRUCFactElec>S</ns2:dRUCFactElec>
      </ns2:xContRUC>
    </ns2:rResEnviConsRUC>
  </env:Body>
</env:Envelope>
```

(Estructura según MT §9.6.3 con la forma real de `xContRUC`; los literales de `dMsgRes` y `dDesEstCons` exactos que devuelve el servidor no están archivados: `[PENDIENTE DE VERIFICACIÓN]`.)

### Códigos de respuesta (MT §9.6.2 Tabla H y §12.3.5.3)

| Código | ID | Resultado | Acción |
|--------|----|-----------|--------|
| 0500 | BO01 | RUC inexistente / "RUC no existe" | No es un RUC válido en el SIFEN |
| 0501 | BO02 | RUC (del certificado) sin permiso para utilizar el WS | Gestionar la habilitación ante la DNIT |
| **0502** | BO03 | Éxito en la consulta / "RUC encontrado" | Leer `xContRUC` |
| 0460 | BM01 | Mensaje de entrada superior a 1.000 KB | — |
| 0001-0183 | AA-AF | Validaciones genéricas | Ver [respuestas-ws.md](../08-errores-y-respuestas/respuestas-ws.md) |

### Uso recomendado: validar al receptor antes de emitir

```
1. Consultar siConsRUC con el RUC del receptor (sin DV)
2. 0502 y dCodEstCons = ACT → emitir con D201=1 (contribuyente)
3. 0502 con otro estado (SUS, SAD, BLQ, CAN, CDE) → el RUC existe pero no está activo; evaluar según el caso
4. 0500 → el RUC no existe: tratar al receptor como no contribuyente (D201=2) o verificar el dato
```

El DV del RUC se calcula con el módulo 11 (validaciones 1253 del MT para el emisor y 1309 para el receptor). El patrón del XSD para el RUC es `[1-9][0-9]*[0-9A-D]?`, 3-8 caracteres, sin ceros a la izquierda ([xsd-produccion-vs-manual.md](../04-schemas-xsd/xsd-produccion-vs-manual.md) §1.d).

---

## WS de consulta masiva de RUC (NT-011) — siConsArchivoRUC

> Documentado únicamente a partir de la [NT-011](../09-notas-tecnicas/NT-011.md). **No homologado**: en junio de 2026 el WSDL de `/de/ws/consultas/consulta-archivo-ruc.wsdl` devolvió cuerpo vacío en `sifen-test` y error de carga en producción. La ruta misma está `[PENDIENTE DE VERIFICACIÓN]` (la NT-011 no la publica).

### Características

| Atributo | Valor | Fuente |
|----------|-------|--------|
| **Proceso** | Síncrono | NT-011 §1 |
| **Función** | Devuelve un archivo con razón social, estado del RUC y condición de facturador electrónico de todos los contribuyentes (excepto cancelados) | NT-011 §1 |
| **Operación / raíz del request** | `rEnviConsArchivoRUCRequest` | NT-011 (ESch01) |
| **Límite** | Una descarga por día (0522 si se supera) | NT-011 Tabla L |
| **Firma** | El request lleva `Signature`; el RUC del certificado debe coincidir con `dRucFactElec` (0523) | NT-011 (ESch06, Tabla L) |

### Request (Schemas XML 20 y 21 de la NT-011)

| ID | Campo | Padre | Tipo | Long. | Ocu. | Descripción |
|----|-------|-------|------|-------|------|-------------|
| ESch01 | `rEnviConsArchivoRUCRequest` | — | — | — | — | Elemento raíz |
| ESch02 | `rConsultaArchivo` | ESch01 | G | — | 1-1 | Contenedor de parámetros |
| ESch03 | `ConsultaDTE` | ESch02 | G | — | 1-1 | Raíz de la consulta |
| ESch04 | `Id` | ESch03 | N | 1-15 | 1-1 | Número secuencial de control |
| ESch05 | `dRucFactElec` | ESch03 | A | 5-8 | 1-1 | RUC del facturador electrónico, sin DV |
| ESch06 | `Signature` | ESch02 | G | — | 1-1 | Firma digital (XML DSig) del contenido |

### Response (Schema XML 22)

| ID | Campo | Padre | Tipo | Long. | Ocu. | Descripción |
|----|-------|-------|------|-------|------|-------------|
| FSch01 | `rEnviConsArchivoRUCResponse` | — | G | — | 1-1 | Elemento raíz |
| FSch02 | `dFecProc` | FSch01 | D | — | 1-1 | Fecha y hora del procesamiento (`AAAA-MM-DDTHH:MI:SS`) |
| FSch03 | `dFecArchivo` | FSch01 | D | — | 0-1 | Fecha del archivo (`AAAA-MM-DD`) |
| FSch04 | `dCodRes` | FSch01 | A | 1-4 | 1-1 | 0520-0523 |
| FSch05 | `dMsgRes` | FSch01 | A | 1-255 | 1-1 | Mensaje |
| FSch06 | `rConsDte` | FSch01 | B | — | 0-1 | Archivo de RUC comprimido, en Base64 |

### Códigos (NT-011 Tabla L / §12.3.7.1)

| Código | ID | Resultado |
|--------|----|-----------|
| 0520 | BO04 | Archivo encontrado (se devuelve en `rConsDte`) |
| 0521 | BO05 | No se encontró el archivo generado en el día |
| 0522 | BO06 | Se superó el límite de descargas del día (una diaria) |
| 0523 | BO07 | El RUC del certificado usado para firmar no coincide con el RUC de consulta |

### Formato del archivo

La NT-011 solo dice que el archivo contiene "la razón social, estado de facturador electrónico y estado del RUC de todos los contribuyentes activos". **El formato interno (campos, separador, codificación) no está documentado**: `[PENDIENTE DE VERIFICACIÓN]`.
