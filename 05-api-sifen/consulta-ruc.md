# Consulta de RUC (siConsRUC / siConsArchivoRUC)

> **Fuente:** Manual Técnico SIFEN v150, sección 7.6, y Nota Técnica NT-011

## Descripción

El SIFEN provee dos Web Services para consultar información de contribuyentes:
1. **siConsRUC**: Consulta en tiempo real los datos de un RUC específico.
2. **siConsArchivoRUC**: Descarga un archivo con el listado de todos los contribuyentes registrados en el sistema (habilitado en NT-011).

---

## Web Service: siConsRUC

### Características

| Atributo | Valor |
|----------|-------|
| **Tipo** | Síncrono |
| **Input** | Número de RUC |
| **Output** | Datos del contribuyente |
| **Método SOAP** | `rConsRUC` |

### Endpoints

| Ambiente | URL |
|----------|-----|
| Pruebas | `https://sifen-test.set.gov.py/de/ws/consultas/consulta-ruc.wsdl` |
| Producción | `https://sifen.set.gov.py/de/ws/consultas/consulta-ruc.wsdl` |

### Estructura del Request

```xml
<soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope">
  <soapenv:Header/>
  <soapenv:Body>
    <rConsRUC>
      <dId>1</dId>
      <dRUCCons>[NUMERO_RUC]</dRUCCons>
    </rConsRUC>
  </soapenv:Body>
</soapenv:Envelope>
```

### Campos del Request siConsRUC

| Campo | Tipo | Descripción |
|-------|------|-------------|
| dId | N | Identificador correlativo del request |
| dRUCCons | A | Número de RUC a consultar (sin dígito verificador) |

### Estructura de la Response siConsRUC

```xml
<rRetConsRUC>
  <dId>1</dId>
  <gConsDatRec>
    <dCodRes>0500</dCodRes>
    <dMsgRes>RUC encontrado</dMsgRes>
    <gDetConsDatRec>
      <dRUCRec>[NUMERO_RUC]</dRUCRec>
      <dDVRec>[DIGITO_VERIFICADOR]</dDVRec>
      <dNomRec>[RAZON_SOCIAL_O_NOMBRE]</dNomRec>
      <dDirRec>[DOMICILIO_FISCAL]</dDirRec>
      <iEsFEV>[1=Facturador_Electronico/0=No]</iEsFEV>
      <iEsAFEV>[1=Autofacturador/0=No]</iEsAFEV>
    </gDetConsDatRec>
  </gConsDatRec>
</rRetConsRUC>
```

### Campos de la Response siConsRUC

| Campo | Descripción |
|-------|-------------|
| dCodRes | Código de respuesta |
| dMsgRes | Mensaje descriptivo |
| dRUCRec | Número de RUC consultado |
| dDVRec | Dígito verificador del RUC |
| dNomRec | Razón social (persona jurídica) o nombre (persona física) |
| dDirRec | Domicilio fiscal registrado |
| iEsFEV | Indica si el RUC está habilitado como Facturador Electrónico Voluntario |
| iEsAFEV | Indica si el RUC está habilitado para emitir Autofacturas Electrónicas |

### Códigos de Respuesta siConsRUC

| Código | Descripción |
|--------|-------------|
| 0500 | RUC encontrado |
| 0501 | RUC no encontrado en el padrón |
| 0502 | RUC inactivo o inhabilitado |
| 0400 | Error de comunicación |
| 0401 | Error de autenticación |

---

## Web Service: siConsArchivoRUC (NT-011)

### Descripción

Habilitado en la Nota Técnica NT-011. Permite descargar un archivo con el listado completo de contribuyentes registrados en el SIFEN. Útil para validar receptores offline o en sistemas que procesan grandes volúmenes.

### Características

| Atributo | Valor |
|----------|-------|
| **Tipo** | Síncrono |
| **Input** | Tipo de archivo / parámetros de filtro |
| **Output** | Archivo ZIP con listado de RUCs |
| **Método SOAP** | `rConsArchivoRUC` |
| **Schemas** | Schema XML N° 20, 21, 22 (NT-011) |

### Endpoints

| Ambiente | URL |
|----------|-----|
| Pruebas | `https://sifen-test.set.gov.py/de/ws/consultas/consulta-archivo-ruc.wsdl` |
| Producción | `https://sifen.set.gov.py/de/ws/consultas/consulta-archivo-ruc.wsdl` |

### Estructura del Request

```xml
<soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope">
  <soapenv:Header/>
  <soapenv:Body>
    <rConsArchivoRUC>
      <dId>1</dId>
      <dTipCons>[TIPO_CONSULTA]</dTipCons>
      <!-- Parámetros adicionales según Schema XML N° 20 -->
    </rConsArchivoRUC>
  </soapenv:Body>
</soapenv:Envelope>
```

### Estructura de la Response

```xml
<rRetConsArchivoRUC>
  <dId>1</dId>
  <gConsArchivoRUC>
    <dCodRes>0600</dCodRes>
    <dMsgRes>Archivo generado</dMsgRes>
    <dArchivo>[BASE64_ZIP_CON_LISTADO_RUC]</dArchivo>
    <dFecGen>[FECHA_GENERACION]</dFecGen>
    <dCantReg>[CANTIDAD_REGISTROS]</dCantReg>
  </gConsArchivoRUC>
</rRetConsArchivoRUC>
```

### Campos de la Response

| Campo | Descripción |
|-------|-------------|
| dCodRes | Código de respuesta |
| dMsgRes | Mensaje descriptivo |
| dArchivo | Archivo ZIP con el listado de RUCs, codificado en Base64 |
| dFecGen | Fecha y hora de generación del archivo |
| dCantReg | Cantidad de registros en el archivo |

---

## Estructura del Archivo de RUCs

El archivo descargado (dentro del ZIP) es un archivo de texto o CSV con el listado de contribuyentes:

| Campo | Descripción |
|-------|-------------|
| RUC | Número de RUC |
| DV | Dígito verificador |
| RAZON_SOCIAL | Nombre o razón social |
| ES_FEV | 1=Es Facturador Electrónico Voluntario, 0=No |
| ES_AFEV | 1=Puede emitir AFE, 0=No |
| ESTADO | Activo/Inactivo |

---

## Casos de Uso

### Validación del Receptor antes de Emitir un DE

Antes de emitir una FE a un receptor con D201=1 (contribuyente), se recomienda verificar que el RUC del receptor esté activo en el padrón:

```
1. Llamar a siConsRUC con el RUC del receptor
2. Si dCodRes=0500 → RUC activo, proceder con la emisión
3. Si dCodRes=0501 → RUC no encontrado → Verificar con el receptor
4. Si dCodRes=0502 → RUC inactivo → No emitir como contribuyente
```

### Sincronización del Padrón Local

Para sistemas con alto volumen de emisión, se recomienda:
1. Descargar el archivo de RUCs con `siConsArchivoRUC` periódicamente (ej: diariamente).
2. Indexar el archivo localmente para validación rápida offline.
3. Usar `siConsRUC` solo para validar RUCs no encontrados en el archivo local.

---

## Consideraciones Importantes

- El dígito verificador del RUC en Paraguay se calcula con el **algoritmo Módulo 11**.
- Un RUC puede tener hasta 8 dígitos + 1 dígito verificador (ej: `80069563-1`).
- Los RUCs de organismos gubernamentales suelen tener el formato `[número]-[DV]`.
- Si el receptor es una persona física, el número de RUC puede coincidir con su cédula de identidad.
