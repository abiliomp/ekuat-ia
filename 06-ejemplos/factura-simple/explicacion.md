# Explicación: Factura Electrónica Simple

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4
> **Archivo:** `ejemplo.xml` en este mismo directorio

## Descripción del Ejemplo

Este ejemplo representa una **Factura Electrónica (FE, C002=1)** de ambiente de prueba con las siguientes características:
- 2 ítems de servicios
- IVA al 10%
- Condición de pago: crédito a plazo de 28 días
- Moneda: PYG (Guaraní)
- Total: 2.200.000 PYG (IVA incluido: 200.000 PYG)

> **Nota:** Este XML es de ambiente de prueba y no tiene valor fiscal. El campo `<dSisFact>` presente en el original fue eliminado por NT-010 y no debe incluirse en nuevos DE.

---

## Análisis Campo por Campo

### 1. Declaración XML y Namespace

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rDE xmlns="http://ekuatia.set.gov.py/sifen/xsd"
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xsi:schemaLocation="https://ekuatia.set.gov.py/sifen/xsd siRecepDE_v150.xsd">
```

| Elemento | Explicación |
|----------|-------------|
| `version="1.0" encoding="UTF-8"` | Obligatorio. Todo DE usa UTF-8 |
| `xmlns` | Namespace del SIFEN. Único permitido |
| `xsi:schemaLocation` | Referencia al XSD de validación (versión 150) |

---

### 2. Versión del Formato (AA002)

```xml
<dVerFor>150</dVerFor>
```

Indica que este DE sigue el formato versión 150 del Manual Técnico.

---

### 3. Elemento DE: El CDC (A001/A002)

```xml
<DE Id="01000000019001001100005022020050710000000231">
```

El CDC tiene 44 dígitos. Desglose:

| Posición | Valor | Significado |
|----------|-------|-------------|
| 1-8 | `01000000` | RUC del emisor sin DV (00000001 con ceros) |
| 9 | `1` | Dígito verificador del RUC |
| 10-11 | `90` | Código que identifica el timbrado (parte del CDC) |
| 12-19 | `01001100` | Timbrado: 12345678 (transformado) |
| 20-22 | `001` | Establecimiento: 001 |
| 23-25 | `001` | Punto de expedición: 001 |
| 26-32 | `1000050` | Número del documento: 1000050 |
| 33 | `2` | Tipo de DE: 1=FE, pero en CDC se codifica diferente |
| 34-42 | `202005071` | Fecha en formato AAAAMMDD: 20200507 |
| 43 | `1` | Código de seguridad parcial |
| 44 | `1` | Dígito verificador del CDC (Módulo 11) |

> El CDC se calcula siguiendo el algoritmo especificado en el MT sección 10.3.

---

### 4. Campos del DE (dDVId, dFecFirma)

```xml
<dDVId>1</dDVId>
<dFecFirma>2020-05-01T14:01:50</dFecFirma>
```

| Campo | ID | Valor | Descripción |
|-------|----|-------|-------------|
| dDVId | A003 | `1` | Dígito verificador del CDC |
| dFecFirma | B002 | `2020-05-01T14:01:50` | Fecha y hora de firma digital. Debe ser cercana a la hora actual del servidor SIFEN (±5 min). **Nota:** La fecha de firma (01/05) es anterior a la fecha de emisión del DE (07/05); esto puede ser intencional en el ejemplo de prueba. |

---

### 5. Grupo gOpeDE (Operación del DE, Grupo B)

```xml
<gOpeDE>
    <iTipEmi>1</iTipEmi>
    <dDesTipEmi>Normal</dDesTipEmi>
    <dCodSeg>000000023</dCodSeg>
    <dInfoEmi>1</dInfoEmi>
    <dInfoFisc>Información de interés del Fisco respecto al DE</dInfoFisc>
</gOpeDE>
```

| Campo | ID | Valor | Descripción |
|-------|----|-------|-------------|
| iTipEmi | B001 | `1` | Tipo de emisión: 1=Normal (online). 2=Contingencia offline |
| dDesTipEmi | B002 | `Normal` | Descripción del tipo de emisión |
| dCodSeg | B004 | `000000023` | Código de seguridad (9 dígitos, parte del CDC). Corresponde a la porción 34-42 del CDC |
| dInfoEmi | B005 | `1` | Información del emisor (código de referencia interna) |
| dInfoFisc | B006 | texto | Información para el fisco. Opcional en FE normal; obligatorio en NRE (con mensaje de RG 41/2014) |

---

### 6. Grupo gTimb (Timbrado, Grupo C)

```xml
<gTimb>
    <iTiDE>1</iTiDE>
    <dDesTiDE>Factura electrónica</dDesTiDE>
    <dNumTim>12345678</dNumTim>
    <dEst>001</dEst>
    <dPunExp>001</dPunExp>
    <dNumDoc>1000050</dNumDoc>
    <dSerieNum>AB</dSerieNum>
    <dFeIniT>2019-08-13</dFeIniT>
</gTimb>
```

| Campo | ID | Valor | Descripción |
|-------|----|-------|-------------|
| iTiDE | C002 | `1` | Tipo de DE: 1=Factura Electrónica |
| dDesTiDE | C003 | `Factura electrónica` | Descripción del tipo |
| dNumTim | C004 | `12345678` | Número de timbrado (8 dígitos, emitido por la SET) |
| dEst | C007 | `001` | Establecimiento (3 dígitos) |
| dPunExp | C008 | `001` | Punto de expedición (3 dígitos) |
| dNumDoc | C009 | `1000050` | Número del documento (7 dígitos, de 0000001 a 9999999) |
| dSerieNum | C010 | `AB` | Serie cuando la numeración se agota. Secuencia: AA, AB, ..., ZZ |
| dFeIniT | C005 | `2019-08-13` | Fecha de inicio de vigencia del timbrado |

---

### 7. Grupo gDatGralOpe (Datos Generales, Grupo D)

```xml
<dFeEmiDE>2020-05-07T15:03:57</dFeEmiDE>
```

| Campo | ID | Valor | Descripción |
|-------|----|-------|-------------|
| dFeEmiDE | D002 | `2020-05-07T15:03:57` | Fecha y hora de emisión del DE |

---

### 8. Grupo gOpeCom (Operación Comercial, D1)

```xml
<gOpeCom>
    <iTipTra>1</iTipTra>
    <dDesTipTra>Venta de mercadería</dDesTipTra>
    <iTImp>1</iTImp>
    <dDesTImp>IVA</dDesTImp>
    <cMoneOpe>PYG</cMoneOpe>
    <dDesMoneOpe>Guarani</dDesMoneOpe>
</gOpeCom>
```

| Campo | ID | Valor | Descripción |
|-------|----|-------|-------------|
| iTipTra | D011 | `1` | Tipo de transacción: 1=Venta de mercadería |
| iTImp | D013 | `1` | Tipo de impuesto: 1=IVA |
| cMoneOpe | D015 | `PYG` | Moneda de la operación: PYG=Guaraní (ISO 4217) |

---

### 9. Grupo gEmis (Emisor, D2)

```xml
<gEmis>
    <dRucEm>00000001</dRucEm>
    <dDVEmi>9</dDVEmi>
    <iTipCont>2</iTipCont>
    <cTipReg>3</cTipReg>
    <dNomEmi>DE generado en ambiente de prueba - sin valor comercial ni fiscal</dNomEmi>
    ...
    <gActEco>
        <cActEco>46510</cActEco>
        <dDesActEco>COMERCIO AL POR MAYOR DE EQUIPOS INFORMÁTICOS Y SOFTWARE</dDesActEco>
    </gActEco>
</gEmis>
```

| Campo | ID | Valor | Descripción |
|-------|----|-------|-------------|
| dRucEm | D101 | `00000001` | RUC del emisor (sin dígito verificador) |
| dDVEmi | D102 | `9` | Dígito verificador del RUC del emisor |
| iTipCont | D103 | `2` | Tipo de contribuyente: 1=Física, 2=Jurídica |
| cTipReg | D104 | `3` | Tipo de régimen: 3=Régimen General |
| cActEco | D131 | `46510` | Código de actividad económica (Tabla 3 del MT) |

---

### 10. Grupo gDatRec (Receptor, D3)

```xml
<gDatRec>
    <iNatRec>1</iNatRec>
    <iTiOpe>1</iTiOpe>
    <cPaisRec>PRY</cPaisRec>
    <iTiContRec>2</iTiContRec>
    <dRucRec>00000002</dRucRec>
    <dDVRec>7</dDVRec>
    <dNomRec>RECEPTOR DEL DOCUMENTO</dNomRec>
    ...
</gDatRec>
```

| Campo | ID | Valor | Descripción |
|-------|----|-------|-------------|
| iNatRec | D201 | `1` | Naturaleza: 1=Contribuyente, 2=No contribuyente |
| iTiOpe | D202 | `1` | Tipo de operación: 1=B2B |
| cPaisRec | D203 | `PRY` | País del receptor: PRY=Paraguay (ISO 3166) |
| iTiContRec | D205 | `2` | Tipo de contribuyente receptor: 2=Persona jurídica |
| dRucRec | D206 | `00000002` | RUC del receptor |
| dDVRec | D207 | `7` | Dígito verificador del RUC receptor |

---

### 11. Grupo gCamFE (Campos FE, E1)

```xml
<gCamFE>
    <iIndPres>1</iIndPres>
    <dDesIndPres>Operación presencial</dDesIndPres>
</gCamFE>
```

| Campo | ID | Valor | Descripción |
|-------|----|-------|-------------|
| iIndPres | E010 | `1` | Indicador de presencialidad: 1=Presencial, 2=Por internet, 3=Exportación, 4=TV/Radio, 5=Vía comisionista, 6=Mensajería, 7=Otro |

---

### 12. Grupo gCamCond (Condición de la Operación, E6)

```xml
<gCamCond>
    <iCondOpe>2</iCondOpe>
    <dDCondOpe>Crédito</dDCondOpe>
    <gPagCred>
        <iCondCred>1</iCondCred>
        <dDCondCred>Plazo</dDCondCred>
        <dPlazoCre>28</dPlazoCre>
    </gPagCred>
</gCamCond>
```

| Campo | ID | Valor | Descripción |
|-------|----|-------|-------------|
| iCondOpe | E601 | `2` | Condición: 1=Contado, 2=Crédito |
| iCondCred | E641 | `1` | Tipo de crédito: 1=Plazo, 2=Cuotas |
| dPlazoCre | E643 | `28` | Plazo en días (obligatorio si E641=1) |

---

### 13. Grupos gCamItem (Ítems, E8)

El ejemplo tiene 2 ítems:

**Ítem 1: CUENTAS ACTIVAS**

| Campo | ID | Valor | Descripción |
|-------|----|-------|-------------|
| dCodInt | E701 | `CAC/CTAC` | Código interno del producto/servicio |
| dDesProSer | E702 | `CUENTAS ACTIVAS` | Descripción del producto o servicio |
| cUniMed | E708 | `77` | Unidad de medida: 77=UNI (unidad) |
| dCantProSer | E711 | `1` | Cantidad: 1 unidad |
| dPUniProSer | E721 | `1.100.000` | Precio unitario en PYG |
| dTotBruOpeItem | EA008 | `1.100.000` | Total bruto = precio × cantidad |
| dTotOpeItem | EA009 | `1.100.000` | Total neto = bruto - descuentos |
| iAfecIVA | E731 | `1` | Afectación IVA: 1=Gravado IVA (tasa normal) |
| dTasaIVA | E734 | `10` | Tasa de IVA: 10% |
| dBasGravIVA | E735 | `1.000.000` | Base gravada = 1.100.000 × 100/110 = 1.000.000 |
| dLiqIVAItem | E736 | `100.000` | IVA del ítem = 1.000.000 × 10/100 = 100.000 |

**Ítem 2: TARJETA URGENTE**

Mismo estructura que el Ítem 1. Precio: 1.100.000 PYG, IVA 10%.

---

### 14. Grupo gTotSub (Subtotales y Totales, Grupo F)

```xml
<gTotSub>
    <dSub10>2200000</dSub10>
    <dTotOpe>2200000</dTotOpe>
    <dTotGralOpe>2200000</dTotGralOpe>
    <dIVA10>200000</dIVA10>
    <dTotIVA>200000</dTotIVA>
    <dBaseGrav10>2000000</dBaseGrav10>
    <dTBasGraIVA>2000000</dTBasGraIVA>
</gTotSub>
```

| Campo | ID | Valor | Descripción |
|-------|----|-------|-------------|
| dSub10 | F003 | `2.200.000` | Subtotal de ítems gravados al 10% (incluye IVA) |
| dTotOpe | F014 | `2.200.000` | Total de la operación (suma de todos los ítems) |
| dTotGralOpe | F018 | `2.200.000` | Total general (mismo que F014 en PYG) |
| dIVA10 | F033 | `200.000` | IVA al 10% = 2.000.000 × 10/100 |
| dTotIVA | F036 | `200.000` | Total de IVA de todos los ítems |
| dBaseGrav10 | F023 | `2.000.000` | Base gravada al 10% = 2.200.000 × 100/110 |
| dTBasGraIVA | F037 | `2.000.000` | Total base gravada IVA |

**Verificación de cálculos:**
- 2 ítems × 1.100.000 = 2.200.000 (total con IVA)
- Base gravada 10%: 2.200.000 × 100/110 = 2.000.000
- IVA 10%: 2.000.000 × 10/100 = 200.000
- Total = Base + IVA = 2.000.000 + 200.000 = 2.200.000 ✓

---

### 15. Firma Digital (Signature)

```xml
<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <SignedInfo>
        <CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
        <SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
        <Reference URI="#01000000019001001100005022020050710000000231">
            ...
            <DigestValue>4koJaqXWpOnd3IquMS1s7vbnBaIpYs1d5XjSW+n3uI4=</DigestValue>
        </Reference>
    </SignedInfo>
    <SignatureValue>[Base64 de la firma RSA]</SignatureValue>
    <KeyInfo>
        <X509Data>
            <X509Certificate>[Certificado X.509 en Base64]</X509Certificate>
        </X509Data>
    </KeyInfo>
</Signature>
```

| Elemento | Valor | Descripción |
|----------|-------|-------------|
| CanonicalizationMethod | Exclusive C14N | Método de canonicalización del XML antes de firmar |
| SignatureMethod | rsa-sha256 | Algoritmo de firma: RSA con SHA-256 |
| Reference URI | `#[CDC]` | Apunta al elemento `<DE Id="...">` por su CDC |
| DigestValue | Base64 | Hash SHA-256 del contenido canonicalizado del DE |
| SignatureValue | Base64 | Firma RSA del DigestValue, cifrada con la clave privada del certificado |

---

### 16. Grupo gCamFuFD (Campos Fuera de la Firma, Grupo J)

```xml
<gCamFuFD>
    <dCarQR>https://ekuatia.set.gov.py/consultas-test/qr?nVersion=150&amp;
            Id=01000000019001001100005022020050710000000231&amp;
            dFeEmiDE=323032302d...&amp;
            dRucRec=00000002&amp;
            dTotGralOpe=2200000&amp;
            dTotIVA=200000&amp;
            cItems=2&amp;
            DigestValue=346b6f...&amp;
            IdCSC=0001&amp;
            cHashQR=67b07c78...</dCarQR>
</gCamFuFD>
```

El QR contiene los siguientes parámetros:

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| nVersion | `150` | Versión del formato |
| Id | CDC | Código de Control del DE |
| dFeEmiDE | Hex | Fecha de emisión en hexadecimal |
| dRucRec | `00000002` | RUC del receptor |
| dTotGralOpe | `2200000` | Total general de la operación |
| dTotIVA | `200000` | Total de IVA |
| cItems | `2` | Cantidad de ítems |
| DigestValue | Hex | DigestValue de la firma en hexadecimal |
| IdCSC | `0001` | ID del CSC (Código Secreto del Contribuyente) |
| cHashQR | SHA-256 | Hash de todos los parámetros concatenados + CSC |

**Proceso de generación del QR:**
1. Concatenar los parámetros del URL en el orden indicado
2. Agregar el CSC al final de la cadena
3. Calcular SHA-256 de la cadena completa → `cHashQR`
4. El URL del QR se genera con todos los parámetros + `cHashQR` (sin el CSC)
5. El QR se imprime en el KuDE apuntando a ese URL
