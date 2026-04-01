# Campos Obligatorios del Documento Electrónico

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 (Schema XML 18: DE_v150.xsd)

## Grupo AA: Identificación del Formato XML

| ID | Campo | Tipo | Long. | Ocu. | Descripción | Observaciones |
|----|-------|------|-------|------|-------------|---------------|
| AA001 | rDE | G | - | 1-1 | Raíz del DE | Elemento raíz del XML |
| AA002 | dVerFor | N | 3 | 1-1 | Versión del formato | Debe contener: 150 |

## Grupo A: Campos Firmados del DE

| ID | Campo | Tipo | Long. | Ocu. | Descripción | Observaciones |
|----|-------|------|-------|------|-------------|---------------|
| A001 | DE | G | - | 1-1 | Campos firmados | Elemento `<DE Id="CDC">` |
| A002 | Id | A | 44 | - | Identificador del DE (CDC) | Atributo del tag `<DE>`. Ver CDC. |
| A003 | dDVId | N | 1 | 1-1 | Dígito verificador del CDC | Algoritmo módulo 11 |
| A004 | dFecFirma | F | 19 | 1-1 | Fecha y hora de firma digital | Formato: AAAA-MM-DDThh:mm:ss. Debe ser anterior a la transmisión. |
| ~~A005~~ | ~~dSisFact~~ | ~~N~~ | ~~1~~ | ~~1-1~~ | ~~Sistema de facturación~~ | **Eliminado por NT-010** |

## Grupo B: Campos de la Operación DE

| ID | Campo | Tipo | Long. | Ocu. | Descripción | Observaciones |
|----|-------|------|-------|------|-------------|---------------|
| B001 | gOpeDE | G | - | 1-1 | Grupo operación DE | |
| B002 | iTipEmi | N | 1 | 1-1 | Tipo de emisión | 1=Normal, 2=Contingencia |
| B003 | dDesTipEmi | A | 6-12 | 1-1 | Descripción tipo emisión | "Normal" o "Contingencia" |
| B004 | dCodSeg | N | 9 | 1-1 | Código de seguridad | Aleatorio, no secuencial, 000000001-999999999 |
| B005 | dInfoEmi | A | 1-3000 | 0-1 | Información del emisor | Se imprime en KuDE |
| B006 | dInfoFisc | A | 1-3000 | 0-1 | Información del Fisco | Obligatorio si C002=7 (NRE). Para FEE, informar datos según Decreto 10797/2013 (NT-007) |

## Grupo C: Datos del Timbrado

| ID | Campo | Tipo | Long. | Ocu. | Descripción | Observaciones |
|----|-------|------|-------|------|-------------|---------------|
| C001 | gTimb | G | - | 1-1 | Grupo timbrado | |
| C002 | iTiDE | N | 1-2 | 1-1 | Tipo de Documento Electrónico | 1=FE, 2=FEE, 3=LCE, 4=AFE, 5=NCE, 6=NDE, 7=NRE, 8=CRE |
| C003 | dDesTiDE | A | 15-40 | 1-1 | Descripción del tipo de DE | Ref. C002 |
| C004 | dNumTim | N | 8 | 1-1 | Número del timbrado | 8 dígitos, vigente a la fecha de emisión |
| C005 | dEst | A | 3 | 1-1 | Establecimiento | Completar con 0 a la izquierda |
| C006 | dPunExp | A | 3 | 1-1 | Punto de expedición | Completar con 0 a la izquierda |
| C007 | dNumDoc | A | 7 | 1-1 | Número del documento | Comienza en 1, completar con 0. Reinicia con serie (C010) |
| C008 | dFeIniT | F | 10 | 1-1 | Fecha inicio de vigencia timbrado | Formato AAAA-MM-DD |
| C009 | dFeFinT | F | 10 | 1-1 | Fecha fin de vigencia timbrado | Formato AAAA-MM-DD |
| C010 | dSerieNum | A | 2 | 0-1 | Serie del número de timbrado | Obligatorio una vez agotada numeración 0000001-9999999. Orden: AA, AB, ..., ZZ |

## Grupo D: Campos Generales del DE

| ID | Campo | Tipo | Long. | Ocu. | Descripción | Observaciones |
|----|-------|------|-------|------|-------------|---------------|
| D001 | gDatGralOpe | G | - | 1-1 | Grupo datos generales | |
| D002 | dFeEmiDE | F | 19 | 1-1 | Fecha y hora de emisión | Formato AAAA-MM-DDThh:mm:ss. Rango: -720h a +120h respecto a transmisión |

## Grupo D1: Operación Comercial

| ID | Campo | Tipo | Long. | Ocu. | Descripción | Observaciones |
|----|-------|------|-------|------|-------------|---------------|
| D010 | gOpeCom | G | - | 0-1 | Grupo operación comercial | Obligatorio si C002≠7; No informar si C002=7 |
| D011 | iTipTra | N | 1-2 | 0-1 | Tipo de transacción | Obligatorio si C002=1 o 4. No informar si C002≠1 o 4 (NT-006) |
| D012 | dDesTipTra | A | 5-39 | 0-1 | Descripción tipo de transacción | Obligatorio si existe D011 (longitud 5-39 según NT-010) |
| D013 | iTImp | N | 1 | 1-1 | Tipo de impuesto | 1=IVA, 2=ISC, 3=Renta, 4=Ninguno, 5=IVA-Renta |
| D014 | dDesTImp | A | 3-11 | 1-1 | Descripción tipo impuesto | Ref. D013 |
| D015 | cMoneOpe | A | 3 | 1-1 | Moneda de la operación | ISO 4217. La misma moneda en todos los ítems. PYG obligatorio si C002=4 (NT-012) |
| D016 | dDesMoneOpe | A | 3-20 | 1-1 | Descripción de la moneda | Ref. D015 |
| D017 | dCondTiCam | N | 1 | 0-1 | Condición tipo de cambio | Obligatorio si D015≠PYG. 1=Global, 2=Por ítem |
| D018 | dTiCam | N | 1-5p(0-4) | 0-1 | Tipo de cambio | Obligatorio si D017=1; No informar si D017=2 o D015=PYG |
| D019 | iCondAnt | N | 1 | 0-1 | Condición del Anticipo | 1=Anticipo Global, 2=Anticipo por ítem |
| D020 | dDesCondAnt | A | 15-17 | 0-1 | Descripción condición anticipo | Ref. D019 |

## Grupo D1.1: Obligaciones Afectadas (NT-018)

| ID | Campo | Tipo | Long. | Ocu. | Descripción | Observaciones |
|----|-------|------|-------|------|-------------|---------------|
| D030 | gOblAfe | G | - | 0-11 | Grupo obligaciones afectadas | Para imputación automática RG90 |
| D031 | cOblAfe | N | 3 | 1-1 | Código de la obligación | Según Tabla 12. No repetir códigos (NT-022) |
| D032 | dDesOblAfe | A | 21-65 | 1-1 | Descripción de la obligación | Ref. D031 |

## Grupo D2: Datos del Emisor

| ID | Campo | Tipo | Long. | Ocu. | Descripción | Observaciones |
|----|-------|------|-------|------|-------------|---------------|
| D100 | gEmis | G | - | 1-1 | Grupo emisor | |
| D101 | dRucEm | A | 3-8 | 1-1 | RUC del emisor | Debe coincidir con el certificado digital |
| D102 | dDVEmi | N | 1 | 1-1 | DV del RUC del emisor | Módulo 11 |
| D103 | iTipCont | N | 1 | 1-1 | Tipo de contribuyente | 1=Persona Física, 2=Persona Jurídica |
| D104 | cTipReg | N | 1-2 | 0-1 | Tipo de régimen | Según Tabla 1 |
| D105 | dNomEmi | A | 4-255 | 1-1 | Nombre o razón social del emisor | En pruebas: obligatorio incluir "DE generado en ambiente de prueba..." |
| D106 | dNomFanEmi | A | 4-255 | 0-1 | Nombre de fantasía | Conforme al RUC |
| D107 | dDirEmi | A | 1-255 | 1-1 | Dirección del local de emisión | Calle principal. Conforme al RUC |
| D108 | dNumCas | N | 1-6 | 1-1 | Número de casa | 0 si no tiene numeración |
| D109 | dCompDir1 | A | 1-255 | 0-1 | Complemento dirección 1 | Calle secundaria |
| D110 | dCompDir2 | A | 1-255 | 0-1 | Complemento dirección 2 | Dpto/piso/local/edificio |
| D111 | cDepEmi | N | 1-2 | 1-1 | Código departamento | Conforme al RUC |
| D112 | dDesDepEmi | A | 6-16 | 1-1 | Descripción departamento | Ref. D111 |
| D113 | cDisEmi | N | 1-4 | 0-1 | Código distrito | |
| D114 | dDesDisEmi | A | 1-30 | 0-1 | Descripción distrito | Obligatorio si D113 existe |
| D115 | cCiuEmi | N | 1-5 | 1-1 | Código ciudad | Conforme al RUC |
| D116 | dDesCiuEmi | A | 1-30 | 1-1 | Descripción ciudad | Ref. D115 |
| D117 | dTelEmi | A | 6-15 | 1-1 | Teléfono | Con prefijo de ciudad |
| D118 | dEmailE | A | 3-80 | 1-1 | Correo electrónico | Conforme al RUC |
| D119 | dDenSuc | A | 1-30 | 0-1 | Denominación comercial sucursal | |

## Grupo D2.1: Actividad Económica del Emisor

| ID | Campo | Tipo | Long. | Ocu. | Descripción | Observaciones |
|----|-------|------|-------|------|-------------|---------------|
| D130 | gActEco | G | - | 1-9 | Grupo actividad económica | |
| D131 | cActEco | A | 1-8 | 1-1 | Código de actividad económica | Según Tabla 3. Conforme al RUC |
| D132 | dDesActEco | A | 1-300 | 1-1 | Descripción de la actividad | Conforme al RUC |

## Grupo D3: Datos del Receptor

| ID | Campo | Tipo | Long. | Ocu. | Descripción | Observaciones |
|----|-------|------|-------|------|-------------|---------------|
| D200 | gDatRec | G | - | 1-1 | Grupo receptor | |
| D201 | iNatRec | N | 1 | 1-1 | Naturaleza del receptor | 1=Contribuyente, 2=No contribuyente |
| D202 | iTiOpe | N | 1 | 1-1 | Tipo de operación | 1=B2B, 2=B2C, 3=B2G, 4=B2F. Si RUC es OEE, debe ser B2G (NT-020) |
| D203 | cPaisRec | A | 3 | 1-1 | Código país del receptor | ISO 3166 Alfa-3 |
| D204 | dDesPaisRe | A | 4-50 | 1-1 | Descripción país receptor | Longitud 4-50 según NT-005 |
| D205 | iTiContRec | N | 1 | 0-1 | Tipo contribuyente receptor | Obligatorio si D201=1; 1=Persona Física, 2=Persona Jurídica |
| D206 | dRucRec | A | 3-8 | 0-1 | RUC del receptor | Obligatorio si D201=1 |
| D207 | dDVRec | N | 1 | 0-1 | DV del RUC receptor | Obligatorio si D206 existe |
| D208 | iTipIDRec | N | 1 | 0-1 | Tipo doc. identidad receptor | Obligatorio si D201=2 y D202≠4. Actualizado NT-002, NT-023 |
| D209 | dDTipIDRec | A | 9-41 | 0-1 | Descripción tipo doc. identidad | Obligatorio si D208 existe |
| D210 | dNumIDRec | A | 1-20 | 0-1 | Número doc. identidad | Obligatorio si D201=2 y D202≠4. Para innominado: "0" |
| D211 | dNomRec | A | 4-255 | 1-1 | Nombre/razón social receptor | Para innominado: "Sin Nombre" |
| D212 | dNomFanRec | A | 4-255 | 0-1 | Nombre de fantasía receptor | |
| D213 | dDirRec | A | 1-255 | 0-1 | Dirección del receptor | Obligatorio si C002=7 o D202=4 |
| D214 | dTelRec | A | 6-15 | 0-1 | Teléfono receptor | Con prefijo si D203=PRY |
| D215 | dCelRec | A | 10-20 | 0-1 | Celular receptor | |
| D216 | dEmailRec | A | 3-80 | 0-1 | Correo electrónico receptor | |
| D217 | dCodCliente | A | 3-15 | 0-1 | Código del cliente | |
| D218 | dNumCasRec | N | 1-6 | 0-1 | Número de casa receptor | Obligatorio si D213 existe |
| D219 | cDepRec | N | 1-2 | 0-1 | Código departamento receptor | Obligatorio si D213 y D202≠4 (NT-003) |
| D220 | dDesDepRec | A | 6-16 | 0-1 | Descripción departamento | Ref. D219 |
| D221 | cDisRec | N | 1-4 | 0-1 | Código distrito receptor | |
| D222 | dDesDisRec | A | 1-30 | 0-1 | Descripción distrito | Obligatorio si D221 existe. Mensaje corregido NT-017 |
| D223 | cCiuRec | N | 1-5 | 0-1 | Código ciudad receptor | Obligatorio si D213 y D202≠4 (NT-003) |
| D224 | dDesCiuRec | A | 1-30 | 0-1 | Descripción ciudad receptor | Ref. D223. Mensaje corregido NT-017 |

## Grupo E8: Ítems de la Operación

| ID | Campo | Tipo | Long. | Ocu. | Descripción | Observaciones |
|----|-------|------|-------|------|-------------|---------------|
| E700 | gCamItem | G | - | 1-999 | Grupo ítems | |
| E701 | dCodInt | A | 1-50 | 1-1 | Código interno | No repetir ítems distintos con mismo código. Ampliado en NT-009 |
| E702 | dParAranc | N | 4 | 0-1 | Partida arancelaria | |
| E703 | dNCM | N | 6-8 | 0-1 | Nomenclatura Mercosur | |
| E704 | dDncpG | A | 8 | 0-1 | Código DNCP Nivel General | Opcional si D202=3 (NT-026) |
| E705 | dDncpE | A | 3-4 | 0-1 | Código DNCP Nivel Específico | Opcional si D202=3 (NT-026) |
| E706 | dGtin | N | 8,12,13,14 | 0-1 | Código GTIN por producto | |
| E707 | dGtinPq | N | 8,12,13,14 | 0-1 | Código GTIN por paquete | |
| E708 | dDesProSer | A | 1-2000 | 1-1 | Descripción producto/servicio | Longitud ampliada en NT-009 |
| E709 | cUniMed | N | 1-5 | 1-1 | Unidad de medida | Según Tabla 5 |
| E710 | dDesUniMed | A | 1-10 | 1-1 | Descripción unidad de medida | |
| E711 | dCantProSer | N | 1-10p(0-8) | 1-1 | Cantidad del producto/servicio | Longitud decimales ampliada en NT-023 |
| E712 | cPaisOrig | A | 3 | 0-1 | Código país de origen | ISO 3166 |
| E719 | dCDCAnticipo | A | 44 | 0-1 | CDC del anticipo | Obligatorio cuando factura usa tipo D011=9 |
| E720 | gValorItem | G | - | 0-1 | Grupo precios por ítem | Obligatorio si C002≠7; No informar si C002=7 |
| E721 | dPUniProSer | N | 1-15p(0-4) | 1-1 | Precio unitario | |
| E731 | iAfecIVA | N | 1 | 1-1 | Afectación IVA | 1=Gravado, 2=Exonerado, 3=Exento, 4=Gravado Parcial |
| E732 | dDesAfecIVA | A | 6-15 | 1-1 | Descripción afectación | Ref. E731 |
| E733 | dPropIVA | N | 1-3 | 1-1 | Proporción gravada del IVA (%) | Si E731=4, porcentaje gravado |
| E734 | dTasaIVA | N | 1-3 | 1-1 | Tasa de IVA aplicable | 5 o 10 |
| E735 | dBasGravIVA | N | 1-15p(0-8) | 1-1 | Base gravada del IVA por ítem | Fórmula actualizada en NT-013 |
| E736 | dLiqIVAItem | N | 1-15p(0-8) | 1-1 | Liquidación IVA por ítem | |
| E737 | dBasExe | N | 1-15p(0-8) | 1-1 | Base exenta por ítem | Campo añadido en NT-013. Si E731=4 |

## Grupo F: Subtotales y Totales

| ID | Campo | Tipo | Long. | Ocu. | Descripción | Observaciones |
|----|-------|------|-------|------|-------------|---------------|
| F001 | gTotSub | G | - | 1-1 | Grupo totales | |
| F002 | dSubExe | N | 1-15p(0-8) | 0-1 | Subtotal exento | Actualizado NT-013 |
| F003 | dSubExo | N | 1-15p(0-8) | 0-1 | Subtotal exonerado | |
| F004 | dSub5 | N | 1-15p(0-8) | 0-1 | Subtotal IVA 5% | Actualizado NT-013 |
| F005 | dSub10 | N | 1-15p(0-8) | 0-1 | Subtotal IVA 10% | Actualizado NT-013 |
| F006 | dTotOpe | N | 1-15p(0-8) | 1-1 | Total de la operación bruta | |
| F007 | dTotDesc | N | 1-15p(0-8) | 1-1 | Total descuento particular por ítem | |
| F008 | dTotOpe | N | 1-15p(0-8) | 1-1 | Subtotal neto | |
| F009 | dTotDesc | N | 1-15p(0-8) | 1-1 | Total descuento particular por ítem | Sumatoria EA002*E711 (NT-001) |
| F010 | dPorcDescTotal | N | 1-3p(0-8) | 0-1 | Porcentaje descuento global total | |
| F011 | dDescTotal | N | 1-15p(0-8) | 1-1 | Total descuentos de la operación | F009+F033 (NT-001) |
| F012 | dAnticipo | N | 1-15p(0-8) | 1-1 | Total anticipos | F034+F035 (NT-001) |
| F013 | dRedon | N | 1-15p(0-8) | 0-1 | Redondeo | |
| F014 | dTotGralOpe | N | 1-15p(0-8) | 1-1 | Total neto de la operación | Fórmula: F008-F013+F025 (NT-001) |
| F015 | dIVA5 | N | 1-15p(0-8) | 0-1 | Total IVA 5% | |
| F016 | dIVA10 | N | 1-15p(0-8) | 0-1 | Total IVA 10% | |
| F017 | dTotIVA | N | 1-15p(0-8) | 0-1 | Total IVA | |
| F023 | dTotalGs | N | 1-15p(0-8) | 0-1 | Total general en Guaraníes | Si D015≠PYG y D017=1: F014*D018. Si D017=2: suma EA009. En AFE: igual a F014. No informar si D015=PYG (NT-008) |
| F033 | dTotDescGlotem | N | 1-15p(0-8) | 1-1 | Total descuento global por ítem | Suma EA004*E711 (NT-001) |
| F034 | dTotAntItem | N | 1-15p(0-8) | 1-1 | Total anticipo por ítem | Suma EA006*E711 (NT-001) |
| F035 | dTotAnt | N | 1-15p(0-8) | 1-1 | Total anticipo global por ítem | Suma EA007*E711 (NT-001) |

## Grupo H: Documento Asociado

| ID | Campo | Tipo | Long. | Ocu. | Descripción | Observaciones |
|----|-------|------|-------|------|-------------|---------------|
| H001 | gDocAso | G | - | 0-9 | Grupo documento asociado | |
| H002 | iTipDocAso | N | 1 | 1-1 | Tipo de documento asociado | 1=Electrónico, 2=Impreso, 3=Constancia electrónica |
| H004 | dCDCAnteDE | A | 44 | 0-1 | CDC del DTE anterior | Si H002=1. NT-015: debe coincidir con CDC del evento de Nominación |
| H006 | dNumDocAso | A | 1-13 | 0-1 | Número del documento impreso | Si H002=2 |
| H018 | dRucFus | A | 3-8 | 0-1 | RUC fusionado | Obligatorio si CDC referenciado es de RUC fusionado (NT-023) |

## Grupo J: Campos Fuera de la Firma Digital

| ID | Campo | Tipo | Long. | Ocu. | Descripción | Observaciones |
|----|-------|------|-------|------|-------------|---------------|
| J001 | gCamFuFD | G | - | 1-1 | Grupo campos fuera firma | |
| J002 | dCarQR | A | 1-1000 | 1-1 | URL del código QR | Ver sección 13.8 |
| J002b | dURLBase | A | 1-500 | 1-1 | URL de consulta CDC | |
| J003 | dInfAdic | A | 1-5000 | 0-1 | Información adicional del emisor | **NO enviar al SIFEN**. Solo para KuDE. |
