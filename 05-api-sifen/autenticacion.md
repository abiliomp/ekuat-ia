# Autenticación y Certificados Digitales en SIFEN

> **Fuente:** Manual Técnico SIFEN v150, secciones 7.3, 7.4, 7.5 y Nota Técnica NT-016

## Descripción

El SIFEN requiere dos tipos de certificados digitales: uno para la **firma del Documento Electrónico** y otro para la **transmisión (autenticación TLS)**. Ambos deben ser emitidos por Prestadores de Servicios de Certificación (PSC) autorizados por la DINETIC (anteriormente MITIC).

---

## Tipos de Certificados Requeridos

| Tipo | Propósito | Emisor |
|------|-----------|--------|
| Certificado de Firma Digital | Firmar el XML del DE (grupo I, Signature) | PSC autorizado por DINETIC |
| Certificado de Transmisión | Autenticación mutual TLS con el servidor SIFEN | PSC autorizado por DINETIC |

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
| **CA emisora** | PSC autorizado por DINETIC |

---

## Características del Certificado de Transmisión

| Atributo | Requisito |
|----------|-----------|
| **Tipo** | X.509 v3 |
| **Uso** | TLS Client Authentication |
| **Protocolo** | TLS 1.2 (obligatorio) |
| **Autenticación** | Mutua (el servidor SIFEN y el cliente se autentican mutuamente) |
| **CA emisora** | PSC autorizado por la DNIT/DINETIC |

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

## Campos del Grupo I (Inicio del Segmento de Firma)

| ID | Campo | Descripción |
|----|-------|-------------|
| I001 | gIniSeg | Grupo inicio de segmento (dentro del DE, indica inicio de firma) |
| I002 | dsFirma | Datos de la firma (referencia interna) |
| I003 | dCertificado | Número de serie del certificado digital usado |
| I004 | dCNombre | Nombre del titular del certificado (CN) |
| I005 | dFecFirmaDigit | Fecha y hora de la firma digital |

---

## PSC (Prestadores de Servicios de Certificación) Autorizados

Los PSC son las entidades que emiten los certificados digitales aceptados por el SIFEN. La lista oficial de PSC habilitados está publicada por la DINETIC:

- URL: `https://www.dinetic.gov.py`
- Los PSC deben estar acreditados conforme a la Ley N° 4017/2010 "De validez jurídica de la firma electrónica, la firma digital, los mensajes de datos y el expediente electrónico"

---

## Sincronización Horaria (NTP)

El SIFEN valida que la fecha/hora de la firma no difiera en más de ±5 minutos del servidor SIFEN. Es obligatorio sincronizar el reloj del sistema con los servidores NTP oficiales:

| Servidor NTP | Dirección |
|--------------|-----------|
| Primario | `aravo1.set.gov.py` |
| Secundario | `aravo2.set.gov.py` |

---

## Proceso de Habilitación como Facturador Electrónico

1. Obtener certificado digital de un PSC autorizado por DINETIC
2. Registrarse en el Portal e-Kuatia (`https://ekuatia.set.gov.py`)
3. Declarar establecimientos y puntos de expedición en Marangatu
4. Obtener timbrado electrónico en Marangatu
5. Obtener el CSC (Código Secreto del Contribuyente) para generación de QR
6. Realizar pruebas en ambiente de homologación con datos de prueba provisto por DNIT
7. Solicitar habilitación para ambiente de producción a la DNIT

---

## CSC (Código Secreto del Contribuyente)

El CSC es un código alfanumérico de 32 caracteres asignado por la DNIT al contribuyente. Se usa como input en la generación del hash SHA-256 para el código QR del KuDE.

| Atributo | Valor |
|----------|-------|
| **Longitud** | 32 caracteres alfanuméricos |
| **Uso** | Generación del parámetro `kCodCon` en el QR |
| **Confidencialidad** | Solo debe ser conocido por el emisor |
| **Obtención** | Habilitado en el Portal e-Kuatia |
| **ID del CSC** | Identificador numérico de 3 dígitos (`kIdCsc`) |
