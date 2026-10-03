# Autenticación y Certificados Digitales en SIFEN

> **Fuente:** Manual Técnico SIFEN v150, §7 "Estándares de comunicación" (PDF pp. 40-42: certificados, firma, §7.11 NTP), sección I "Información de la firma digital" (campo I001) y cap. QR (PDF pp. 204-208, parámetros `IdCSC` y `cHashQR`); Nota Técnica [NT-016](../09-notas-tecnicas/NT-016.md) (algoritmos, Ley 6822/2021); [Guía de Pruebas](../10-guias/guia-de-pruebas.md) §2 y §4.1; `00-fuentes/xsd/DE_v150.xsd:1939-1960` (posición de `Signature` en `rDE`).
>
> **Corregido el 03/10/2026 (Fase 0):** se eliminaron la tabla de "campos I001-I005" (`gIniSeg`, `dsFirma`, `dCertificado`, `dCNombre`, `dFecFirmaDigit`), la tolerancia de "±5 minutos", el organismo "DINETIC" y los parámetros `kCodCon`/`kIdCsc`, que no existen en el MT, en los XSD ni en las NT.

## Descripción

El SIFEN requiere dos tipos de certificados digitales: uno para la **firma del Documento Electrónico** y otro para la **transmisión (autenticación mutua TLS)**. Ambos deben ser certificados cualificados emitidos por Prestadores (Cualificados) de Servicios de Certificación/Confianza (PSC/PCSC) habilitados, según la lista de la Autoridad Certificadora Raíz del Paraguay administrada por el MIC (MT §7, PDF p. 42; guía de pruebas §4.1: `https://www.acraiz.gov.py/html/Certif_1PrestaServ.html`). La denominación actual del organismo rector de la firma digital tras la Ley 6822/2021: `[PENDIENTE DE VERIFICACIÓN]`.

---

## Tipos de Certificados Requeridos

| Tipo | Propósito | Emisor |
|------|-----------|--------|
| Certificado de Firma Digital | Firmar el XML del DE (campo I001 `Signature`) y de los eventos | PSC/PCSC habilitado (lista de la AC Raíz, MIC) |
| Certificado de Transmisión | Autenticación mutua TLS con el servidor SIFEN; debe contener el RUC y `ExtendedKeyUsage` con `clientAuth` (validación AA01) | PSC/PCSC habilitado |

> En la práctica, puede usarse el mismo certificado para ambas funciones si cumple con los requisitos técnicos.

---

## Características del Certificado de Firma Digital

| Atributo | Requisito |
|----------|-----------|
| **Tipo** | X.509 v3 |
| **Tamaño de clave RSA** | 2048 a 4096 bits (NT-016) |
| **Algoritmo de firma del certificado** | SHA-256, SHA-384 o SHA-512 con RSA |
| **Titular** | Puede ser persona jurídica (empresa) o persona física (representante autorizado) |
| **RUC** | El RUC del titular debe coincidir con el RUC del emisor del DE |
| **Vigencia** | El certificado debe estar vigente al momento de la firma |
| **CA emisora** | PSC/PCSC habilitado (AC Raíz del Paraguay) |

---

## Características del Certificado de Transmisión

| Atributo | Requisito |
|----------|-----------|
| **Tipo** | X.509 v3 |
| **Uso** | TLS Client Authentication |
| **Protocolo** | TLS 1.2 (obligatorio) |
| **Autenticación** | Mutua (el servidor SIFEN y el cliente se autentican mutuamente) |
| **CA emisora** | PSC/PCSC habilitado (AC Raíz del Paraguay) |

---

## Firma Digital XML (XML DSig Enveloped)

La firma digital del DE sigue el estándar XML DSig Enveloped según W3C.

### Estructura de la Firma

```xml
<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
  <SignedInfo>
    <CanonicalizationMethod Algorithm="..." />
    <SignatureMethod Algorithm="..." />
    <Reference URI="#[CDC]">
      <Transforms>
        <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" />
        <Transform Algorithm="[C14N Method]" />
      </Transforms>
      <DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
      <DigestValue>[BASE64]</DigestValue>
    </Reference>
  </SignedInfo>
  <SignatureValue>[BASE64]</SignatureValue>
  <KeyInfo>
    <X509Data>
      <X509Certificate>[BASE64 del certificado]</X509Certificate>
    </X509Data>
  </KeyInfo>
</Signature>
```

### Algoritmos de Firma Soportados (NT-016)

| Algoritmo | URI |
|-----------|-----|
| RSA-SHA256 (mínimo obligatorio) | `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256` |
| RSA-SHA384 (habilitado en NT-016) | `http://www.w3.org/2001/04/xmldsig-more#rsa-sha384` |
| RSA-SHA512 (habilitado en NT-016) | `http://www.w3.org/2001/04/xmldsig-more#rsa-sha512` |

### Métodos de Canonicalización Soportados (NT-016)

| Método | URI |
|--------|-----|
| Exclusive XML Canonicalization (sin comentarios) — **Recomendado** | `http://www.w3.org/2001/10/xml-exc-c14n#` |
| Exclusive XML Canonicalization (con comentarios) | `http://www.w3.org/2001/10/xml-exc-c14n#WithComments` |
| Inclusive XML Canonicalization (sin comentarios) | `http://www.w3.org/TR/2001/REC-xml-c14n-20010315` |
| Inclusive XML Canonicalization (con comentarios) | `http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments` |

> **Nota:** NT-016 elimina XPath como método de transformación. Solo se permiten los métodos listados arriba.

### Algoritmo de Resumen (Digest)

| Algoritmo | URI |
|-----------|-----|
| SHA-256 | `http://www.w3.org/2001/04/xmlenc#sha256` |

---

## Elemento `<Reference>` del DE

- La referencia `URI` apunta al atributo `Id` del elemento `<DE>`:
  - `URI="#[CDC_44_DIGITOS]"`
- La transformación `enveloped-signature` se aplica siempre.
- La segunda transformación es el método de canonicalización elegido.

---

## Ubicación de la Firma en el XML

La firma se ubica **dentro del elemento `<rDE>`**, después del `<DE>` y antes del `<gCamFuFD>`:

```xml
<rDE xmlns="...">
  <dVerFor>150</dVerFor>
  <DE Id="[CDC]">
    <!-- Contenido del DE -->
  </DE>
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <!-- Firma digital -->
  </Signature>
  <gCamFuFD>
    <dCarQR>[URL QR]</dCarQR>
  </gCamFuFD>
</rDE>
```

> Los campos `<gCamFuFD>` y `<dCarQR>` están **fuera de la firma** (grupo J). Son añadidos después de la firma digital.

---

## Grupo I del MT (Información de la Firma Digital, I001-I049)

El MT define **un solo campo** en este grupo (sección I del formato del DE):

| ID | Campo | Padre | Ocu. | Descripción |
|----|-------|-------|------|-------------|
| I001 | `Signature` | AA001 (`rDE`) | 1-1 | "Según el estándar XML signature. Debe ser firmado el grupo A (campo A001) que contiene los grupos de información del A hasta H" |

La validación 2450 (I002) exige que el certificado esté vigente y no revocado al momento de la firma (fecha A004 `dFecFirma`). En el XSD, `Signature` es el elemento `ds:Signature` importado de `xmldsig-core-schema.xsd`, hijo de `rDE` entre `DE` y `gCamFuFD` (`DE_v150.xsd:1939-1960`); **no existe** ningún grupo `gIniSeg` ni campos `dsFirma`, `dCertificado`, `dCNombre` o `dFecFirmaDigit`.

---

## PSC / PCSC habilitados

Los PSC (Prestadores de Servicios de Certificación; tras la Ley 6822/2021, PCSC = Prestadores Cualificados de Servicios de Confianza, NT-016) emiten los certificados aceptados por el SIFEN. La lista oficial está publicada por la Autoridad Certificadora Raíz del Paraguay:

- URL: `https://www.acraiz.gov.py/html/Certif_1PrestaServ.html` (MT §7, PDF p. 42; guía de pruebas §4.1)
- Marco legal citado por los documentos oficiales: Ley N° 4017/2010 (firma digital) y Ley N° 6822/2021 (servicios de confianza; "certificado cualificado de firma electrónica", Art. 43, según el glosario de la guía de pruebas)

---

## Sincronización Horaria (NTP)

El SIFEN rechaza con **1004** (A004a) una firma cuya fecha y hora sea **posterior** a la del SIFEN, y aprueba con observación (**1005**, A004b) la transmisión extemporánea respecto de la fecha de firma ([errores-validacion.md](../08-errores-y-respuestas/errores-validacion.md)). El MT **no publica una tolerancia en minutos**; la cifra "±5 minutos" que figuraba aquí no tiene fuente: `[PENDIENTE DE VERIFICACIÓN]`. Servidores NTP oficiales (MT §7.11, PDF p. 42):

| Servidor NTP | Dirección |
|--------------|-----------|
| Primario | `aravo1.set.gov.py` |
| Secundario | `aravo2.set.gov.py` |

> El acceso a los NTP y a los WS "dependerá de la política de seguridad establecida por la SET" (MT §7.11). En servidores configurados en UTC, generar `dFecFirma`/`dFeEmiDE` en hora de Asunción.

---

## Proceso de Habilitación como Facturador Electrónico

1. Obtener un certificado cualificado de un PSC/PCSC habilitado (lista de la AC Raíz)
2. Registrarse en el Portal e-Kuatia (`https://ekuatia.set.gov.py`)
3. Declarar establecimientos y puntos de expedición en Marangatu
4. Obtener timbrado electrónico en Marangatu
5. Obtener el CSC (Código Secreto del Contribuyente) para generación de QR
6. Realizar pruebas en ambiente de homologación con datos de prueba provisto por DNIT
7. Solicitar habilitación para ambiente de producción a la DNIT

---

## CSC (Código Secreto del Contribuyente)

El CSC es el código secreto que la DNIT entrega al facturador electrónico. Se **concatena al final** de los parámetros del QR antes de calcular el hash SHA-256 que viaja en el parámetro `cHashQR`; el CSC mismo **nunca** se incluye en la URL (MT cap. QR, PDF pp. 205-207; [06-ejemplos/factura-simple/explicacion.md](../06-ejemplos/factura-simple/explicacion.md)).

| Atributo | Valor | Fuente |
|----------|-------|--------|
| **Longitud** | 32 caracteres alfanuméricos (los genéricos de prueba son `ABCD` + 28 ceros y `EFGH` + 28 ceros) | Guía de pruebas §2; MT ejemplo `IdCSC=0001ABCD0000000000000000000000000000` |
| **Identificador** | Parámetro `IdCSC` del QR, **4 dígitos** (`0001`, `0002`); si el contribuyente tiene más de un CSC activo debe indicar el que usó | MT cap. QR (tabla de parámetros: `IdCSC`, longitud 4) |
| **Uso** | Insumo del hash `cHashQR` = SHA-256(parámetros del QR + CSC) | MT cap. QR |
| **Confidencialidad** | Solo el emisor debe conocerlo | MT cap. QR |
| **Obtención** | Portal e-Kuatia / DNIT (producción); CSC genéricos publicados en la guía para pruebas | Guía de pruebas §2 |
