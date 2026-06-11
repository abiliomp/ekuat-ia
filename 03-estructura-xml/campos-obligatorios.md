> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 (Schema XML 18: DE_v150.xsd)

> **Nota:** Este documento refleja el MT v150 con cambios del historial de versiones marcados. Los campos marcados con ~~tachado~~ fueron eliminados. Los campos con **[MODIFICADO]** tuvieron cambios en su definición, tipo o longitud. Los campos con **[NUEVO en v150]** fueron agregados en esta versión.

# Campos del Documento Electrónico (DE) — Tabla de Formato Completa

**Schema XML 18: DE_v150.xsd (Documento Electrónico)**

---

## Grupo AA — Campos que identifican el formato electrónico XML (AA001–AA009)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| AA | AA001 | rDE | Documento Electrónico — elemento raíz | Raíz | G | — | 1-1 | |
| AA | AA002 | dVerFor | **[MODIFICADO]** Versión del formato | AA001 | N | 3 | 1-1 | Control de versiones. Este campo debe contener la versión **150** |

---

## Grupo A — Campos firmados del Documento Electrónico (A001–A099)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| A | A001 | DE | Campos firmados del DE | AA001 | G | — | 1-1 | |
| A | A002 | Id | Identificador del DE | A001 | A | 44 | Atributo | CDC (Código de Control). Atributo del Tag `<DE>`. Nota: si el RUC contiene letras, se convierte al valor ASCII para el cálculo del DV y CDC. |
| A | A003 | dDVId | Dígito verificador del identificador del DE | A001 | N | 1 | 1-1 | **[NUEVO en v150]** Según algoritmo módulo 11 |
| A | A004 | dFecFirma | Fecha de la firma | A001 | F | 19 | 1-1 | **[MODIFICADO]** La fecha y hora de la firma digital debe ser anterior a la fecha y hora de transmisión al SIFEN. El certificado debe estar vigente al momento de la firma. Formato: `AAAA-MM-DDThh:mm:ss`. El plazo límite de transmisión al SIFEN para la aprobación normal es de 72 h contadas a partir de la fecha y hora de la firma digital. |
| A | **[NUEVO en v150]** A005 | dSisFact | Sistema de facturación | A001 | N | 1 | 1-1 | **[NUEVO en v150]** 1=Sistema de facturación del contribuyente; ~~2=SIFEN solución gratuita~~ (valor eliminado por NT-010). El XSD de producción solo acepta el valor 1 y el campo es **obligatorio** (va entre `dFecFirma` y `gOpeDE`) |

---

## Grupo B — Campos inherentes a la operación de Documentos Electrónicos (B001–B099)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| B | B001 | gOpeDE | Campos inherentes a la operación de DE | A001 | G | — | 1-1 | |
| B | B002 | iTipEmi | Tipo de emisión | B001 | N | 1 | 1-1 | 1=Normal; 2=Contingencia |
| B | B003 | dDesTipEmi | Descripción del tipo de emisión | B001 | A | 6-12 | 1-1 | Referente al campo B002. 1="Normal"; 2="Contingencia" |
| B | B004 | dCodSeg | Código de seguridad | B001 | N | 9 | 1-1 | Código generado por el emisor de manera aleatoria para asegurar la confidencialidad de la consulta pública del DE |
| B | B005 | dInfoEmi | Información de interés del emisor respecto al DE | B001 | A | 1-3000 | 0-1 | |
| B | B006 | dInfoFisc | Información de interés del Fisco respecto al DE | B001 | A | 1-3000 | 0-1 | Esta información debe ser impresa en el KuDE. **[NUEVO en v150]** Cuando C002=7 (Nota de Remisión) es **obligatorio** informar el mensaje según el Art. 3 Inc. 7 de la Resolución General N° 41/2014 |

---

## Grupo C — Campos de datos del Timbrado (C001–C099)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| C | C001 | gTimb | Datos del timbrado | A001 | G | — | 1-1 | |
| C | C002 | iTiDE | Tipo de Documento Electrónico | C001 | N | 1-2 | 1-1 | **[MODIFICADO]** 1=Factura electrónica; 2=FEE (Futuro); 3=FEI (Futuro); 4=Autofactura electrónica; 5=NCE; 6=NDE; 7=NRE; 8=Comprobante retención (Futuro) |
| C | C003 | dDesTiDE | Descripción del tipo de documento electrónico | C001 | A | 15-40 | 1-1 | Referente al campo C002 |
| C | C004 | dNumTim | Número del timbrado | C001 | N | 8 | 1-1 | Debe coincidir con la estructura de timbrado |
| C | C005 | dEst | Establecimiento | C001 | A | 3 | 1-1 | Completar con 0 (cero) a la izquierda. Debe coincidir con la estructura de timbrado |
| C | C006 | dPunExp | Punto de expedición | C001 | A | 3 | 1-1 | Completar con 0 (cero) a la izquierda. Debe coincidir con la estructura de timbrado |
| C | C007 | dNumDoc | Número del documento | C001 | A | 7 | 1-1 | Debe empezar con 1 para un nuevo timbrado. Completar con 0 a la izquierda hasta 7 cifras. **[NUEVO en v150]** Una vez agotada la numeración (9999999), se reinicia con la utilización de la serie |
| C | **[NUEVO en v150]** C010 | dSerieNum | Serie del número de timbrado | C001 | A | 2 | 0-1 | **[NUEVO en v150]** Campo obligatorio cuando ya se ha consumido la totalidad de la numeración permitida (9999999). Ver sección 10.5 Manejo del timbrado y Numeración |
| C | C008 | dFeIniT | Fecha inicio de vigencia del timbrado | C001 | F | 10 | 1-1 | Formato AAAA-MM-DD |
| C | ~~C009~~ | ~~dFeFinT~~ | ~~Fecha fin de vigencia del timbrado~~ | ~~C001~~ | ~~F~~ | ~~10~~ | ~~1-1~~ | ~~Formato AAAA-MM-DD~~ |

> ⚠️ **ELIMINADO:** El campo C009 (dFeFinT — Fecha fin de vigencia del timbrado) fue eliminado en la versión actual del MT. El timbrado ya no maneja fecha de fin de vigencia.

---

## Grupo D — Campos Generales del Documento Electrónico DE (D001–D299)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| D | D001 | gDatGralOpe | Campos generales del DE | A001 | G | — | 1-1 | |
| D | D002 | dFeEmiDE | Fecha y hora de emisión del DE | D001 | F | 19 | 1-1 | Formato `AAAA-MM-DDThh:mm:ss`. **[MODIFICADO]** Se aceptará como límites técnicos que la fecha de emisión del DE sea atrasada hasta 720 horas (30 días) y adelantada hasta 120 horas (5 días) en relación a la fecha y hora de transmisión al SIFEN |

### D1 — Campos inherentes a la operación comercial (D010–D099)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| D1 | D010 | gOpeCom | Campos inherentes a la operación comercial | D001 | G | — | 0-1 | Obligatorio si C002 ≠ 7; No informar si C002 = 7 |
| D1 | D011 | iTipTra | Tipo de transacción | D010 | N | 1-2 | 0-1 | Obligatorio si C002 = 1 o 4. Valores: 1=Venta de mercadería; 2=Prestación de servicios; 3=Mixto; 4=Venta de activo fijo; 5=Venta de divisas; 6=Compra de divisas; 7=Promoción o entrega de muestras; 8=Donación; 9=Anticipo; 10=Compra de productos; 11=Compra de servicios; **[NUEVO en v150]** 12=Venta de crédito fiscal; **[NUEVO en v150]** 13=Muestras médicas (Art. 3 RG 24/2014) |
| D1 | D012 | dDesTipTra | Descripción del tipo de transacción | D010 | A | **[MODIFICADO]** 5-36 | 0-1 | Obligatorio si existe D011 |
| D1 | D013 | iTImp | **[MODIFICADO]** Tipo de impuesto afectado | D010 | N | 1 | 1-1 | 1=IVA; **[NUEVO en v150]** 2=ISC; **[NUEVO en v150]** 3=Renta; **[NUEVO en v150]** 4=Ninguno; **[NUEVO en v150]** 5=IVA-Renta |
| D1 | D014 | dDesTImp | **[MODIFICADO]** Descripción del tipo de impuesto afectado | D010 | A | **[MODIFICADO]** 3-11 | 1-1 | 1="IVA"; **[NUEVO en v150]** 2="ISC"; **[NUEVO en v150]** 3="Renta"; **[NUEVO en v150]** 4="Ninguno"; **[NUEVO en v150]** 5="IVA - Renta" (literal exacto del XSD: guion simple con espacios) |
| D1 | D015 | cMoneOpe | Moneda de la operación | D010 | A | 3 | 1-1 | Según ISO 4217. Se requiere la misma moneda para todos los ítems |
| D1 | D016 | dDesMoneOpe | Descripción de la moneda de la operación | D010 | A | 3-20 | 1-1 | Referente a D015 |
| D1 | D017 | dCondTiCam | Condición del tipo de cambio | D010 | N | 1 | 0-1 | Obligatorio si D015 ≠ PYG. 1=Global (un solo TC para todo el DE); 2=Por ítem |
| D1 | D018 | dTiCam | Tipo de cambio de la operación | D010 | N | 1-5p(0-4) | 0-1 | Obligatorio si D017=1. **[NUEVO en v150]** No informar si D017=2. **[NUEVO en v150]** No informar si D015=PYG |
| D1 | **[NUEVO en v150]** D019 | iCondAnt | Condición del Anticipo | D010 | N | 1 | 0-1 | **[NUEVO en v150]** 1=Anticipo Global; 2=Anticipo por ítem |
| D1 | **[NUEVO en v150]** D020 | dDesCondAnt | Descripción de la condición del Anticipo | D010 | A | 15-17 | 0-1 | **[NUEVO en v150]** 1="Anticipo Global"; 2="Anticipo por Ítem" |

### D2 — Campos que identifican al emisor del DE (D100–D129) — **[MODIFICADO]**

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| D2 | D100 | gEmis | Grupo de campos que identifican al emisor | D001 | G | — | 1-1 | |
| D2 | D101 | dRucEm | RUC del contribuyente emisor | D100 | A | **[MODIFICADO]** 3-8 | 1-1 | Debe corresponder al RUC del certificado digital utilizado para firmar el DE |
| D2 | D102 | dDVEmi | Dígito verificador del RUC del contribuyente emisor | D100 | N | 1 | 1-1 | **[NUEVO en v150]** Según algoritmo módulo 11 |
| D2 | D103 | iTipCont | Tipo de contribuyente | D100 | N | 1 | 1-1 | 1=Persona Física; 2=Persona Jurídica |
| D2 | D104 | cTipReg | Tipo de régimen | D100 | N | 1-2 | 0-1 | Según Tabla 1 – Tipo de Régimen |
| D2 | D105 | dNomEmi | Nombre o razón social del emisor del DE | D100 | A | **[MODIFICADO]** 4-255 | 1-1 | En ambiente de prueba, debe contener el literal "DE generado en ambiente de prueba - sin valor comercial ni fiscal" |
| D2 | D106 | dNomFanEmi | Nombre de fantasía | D100 | A | **[MODIFICADO]** 4-255 | 0-1 | Debe corresponder a lo declarado en el RUC |
| D2 | D107 | dDirEmi | Dirección del local donde se emite el DE | D100 | A | **[MODIFICADO]** 1-255 | 1-1 | Nombre de la calle principal. Debe corresponder al RUC |
| D2 | D108 | dNumCas | Número de casa | D100 | N | 1-6 | 1-1 | Si no tiene numeración, colocar 0 (cero) |
| D2 | D109 | dCompDir1 | Complemento de dirección 1 | D100 | A | **[MODIFICADO]** 1-255 | 0-1 | Nombre de la calle secundaria |
| D2 | D110 | dCompDir2 | Complemento de dirección 2 | D100 | A | **[MODIFICADO]** 1-255 | 0-1 | N° de departamento/piso/local/edificio/depósito |
| D2 | D111 | cDepEmi | Código del departamento de emisión | D100 | N | 1-2 | 1-1 | Según XSD de Departamentos |
| D2 | D112 | dDesDepEmi | Descripción del departamento de emisión | D100 | A | 6-16 | 1-1 | Referente a D111 |
| D2 | D113 | cDisEmi | Código del distrito de emisión | D100 | N | 1-4 | 0-1 | Según Tabla 2.1 – Distritos |
| D2 | D114 | dDesDisEmi | Descripción del distrito de emisión | D100 | A | 1-30 | 0-1 | Obligatorio si existe D113 |
| D2 | D115 | cCiuEmi | Código de la ciudad de emisión | D100 | N | 1-5 | 1-1 | Según Tabla 2.2 – Ciudades |
| D2 | D116 | dDesCiuEmi | Descripción de la ciudad de emisión | D100 | A | 1-30 | 1-1 | Referente a D115 |
| D2 | D117 | dTelEmi | Teléfono local de emisión de DE | D100 | **[MODIFICADO]** A | **[MODIFICADO]** 6-15 | 1-1 | Debe incluir el prefijo de la ciudad |
| D2 | D118 | dEmailE | Correo electrónico del emisor | D100 | A | 3-80 | 1-1 | Debe corresponder al RUC |
| D2 | D119 | dDenSuc | Denominación comercial de la sucursal | D100 | A | 1-30 | 0-1 | Denominación interna del emisor |

### D2.1 — Campos que describen la actividad económica del emisor (D130–D139) — **[NUEVO en v150]**

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| **[NUEVO en v150]** D2.1 | D130 | gActEco | Grupo de campos que describen la actividad económica del emisor | D100 | G | — | 1-9 | **[NUEVO en v150]** |
| **[NUEVO en v150]** D2.1 | D131 | cActEco | Código de la actividad económica del emisor | D130 | A | 1-8 | 1-1 | **[NUEVO en v150]** Según Tabla 3 – Actividades Económicas. Debe corresponder al RUC |
| **[NUEVO en v150]** D2.1 | D132 | dDesActEco | Descripción de la actividad económica del emisor | D130 | A | 1-300 | 1-1 | **[NUEVO en v150]** Referente al campo D131. Debe corresponder al RUC |

### D2.2 — Campos que identifican al responsable de la generación del DE (D140–D160) — **[NUEVO en v150]**

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| **[NUEVO en v150]** D2.2 | D140 | gRespDE | Grupo de campos que identifican al responsable de la generación del DE | D100 | G | — | 0-1 | **[NUEVO en v150]** |
| **[NUEVO en v150]** D2.2 | D141 | iTipIDRespDE | Tipo de documento de identidad del responsable | D140 | N | 1 | 1-1 | **[NUEVO en v150]** 1=Cédula paraguaya; 2=Pasaporte; 3=Cédula extranjera; 4=Carnet de residencia; 9=Otro |
| **[NUEVO en v150]** D2.2 | D142 | dDTipIDRespDE | Descripción del tipo de documento de identidad del responsable | D140 | A | 9-41 | 1-1 | **[NUEVO en v150]** Si D141=9, informar el tipo de documento |
| **[NUEVO en v150]** D2.2 | D143 | dNumIDRespDE | Número de documento de identidad del responsable | D140 | A | 1-20 | 1-1 | **[NUEVO en v150]** |
| **[NUEVO en v150]** D2.2 | D144 | dNomRespDE | Nombre o razón social del responsable | D140 | A | 4-255 | 1-1 | **[NUEVO en v150]** |
| **[NUEVO en v150]** D2.2 | D145 | dCarRespDE | Cargo del responsable de la generación del DE | D140 | A | 4-100 | 1-1 | **[NUEVO en v150]** |

### D3 — Campos que identifican al receptor del DE (D200–D299)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| D3 | D200 | gDatRec | Grupo de campos que identifican al receptor | D001 | G | — | 1-1 | |
| D3 | D201 | iNatRec | Naturaleza del receptor | D200 | N | 1 | 1-1 | 1=contribuyente; 2=no contribuyente |
| D3 | D202 | iTiOpe | Tipo de operación | D200 | N | 1 | 1-1 | 1=B2B; 2=B2C; **[NUEVO en v150]** 3=B2G; **[NUEVO en v150]** 4=B2F (solo para servicios a empresas o personas físicas del exterior) |
| D3 | D203 | cPaisRec | Código de país del receptor | D200 | A | 3 | 1-1 | Según XSD de Codificación de Países |
| D3 | D204 | dDesPaisRe | Descripción del país receptor | D200 | A | 4-30 | 1-1 | Referente a D203 |
| D3 | D205 | iTiContRec | Tipo de contribuyente receptor | D200 | N | 1 | 0-1 | Obligatorio si D201=1; No informar si D201=2. 1=Persona Física; 2=Persona Jurídica |
| D3 | D206 | dRucRec | RUC del receptor | D200 | A | **[MODIFICADO]** 3-8 | 0-1 | Obligatorio si D201=1; No informar si D201=2 |
| D3 | D207 | dDVRec | Dígito verificador del RUC del receptor | D200 | N | 1 | 0-1 | **[NUEVO en v150]** Obligatorio si existe D206. Según algoritmo módulo 11 |
| D3 | D208 | iTipIDRec | Tipo de documento de identidad del receptor | D200 | N | 1 | 0-1 | **[NT-023]** Obligatorio si D201=2. No informar si D201=1. 1=Cédula paraguaya; 2=Pasaporte; 3=Cédula extranjera; 4=Carnet de residencia; **[NUEVO en v150]** 5=Innominado; **[NUEVO en v150]** 6=Tarjeta Diplomática de exoneración fiscal; 9=Otro |
| D3 | D209 | dDTipIDRec | Descripción del tipo de documento de identidad | D200 | A | **[MODIFICADO]** 9-41 | 0-1 | Obligatorio si existe D208. Si D208=9, informar el tipo de documento |
| D3 | D210 | dNumIDRec | Número de documento de identidad | D200 | A | 1-20 | 0-1 | **[NT-023]** Obligatorio si D201=2. No informar si D201=1. En caso de DE innominado, completar con 0 (cero) |
| D3 | D211 | dNomRec | Nombre o razón social del receptor del DE | D200 | A | **[MODIFICADO]** 4-255 | 1-1 | En caso de DE innominado, completar con "Sin Nombre" |
| D3 | D212 | dNomFanRec | Nombre de fantasía | D200 | A | **[MODIFICADO]** 4-255 | 0-1 | |
| D3 | D213 | dDirRec | Dirección del receptor | D200 | A | **[MODIFICADO]** 1-255 | 0-1 | **[NUEVO en v150]** Campo obligatorio cuando C002=7 o cuando D202=4 |
| D3 | **[NUEVO en v150]** D218 | dNumCasRec | Número de casa del receptor | D200 | N | 1-6 | 0-1 | **[NUEVO en v150]** Campo obligatorio si se informa D213. Cuando D201=1, debe corresponder al RUC |
| D3 | **[NUEVO en v150]** D219 | cDepRec | Código del departamento del receptor | D200 | N | 1-2 | 0-1 | **[NUEVO en v150]** Campo obligatorio si se informa D213 y D202≠4, no se debe informar cuando D202=4 |
| D3 | **[NUEVO en v150]** D220 | dDesDepRec | Descripción del departamento del receptor | D200 | A | 6-16 | 0-1 | **[NUEVO en v150]** Referente a D219 |
| D3 | **[NUEVO en v150]** D221 | cDisRec | Código del distrito del receptor | D200 | N | 1-4 | 0-1 | **[NUEVO en v150]** Según Tabla 2.1 – Distritos |
| D3 | **[NUEVO en v150]** D222 | dDesDisRec | Descripción del distrito del receptor | D200 | A | 1-30 | 0-1 | **[NUEVO en v150]** Obligatorio si existe D221 |
| D3 | **[NUEVO en v150]** D223 | cCiuRec | Código de la ciudad del receptor | D200 | N | 1-5 | 0-1 | **[NUEVO en v150]** Campo obligatorio si se informa D213 y D202≠4 |
| D3 | **[NUEVO en v150]** D224 | dDesCiuRec | Descripción de la ciudad del receptor | D200 | A | 1-30 | 0-1 | **[NUEVO en v150]** Referente a D223 |
| D3 | D214 | dTelRec | Número de teléfono del receptor | D200 | A | **[MODIFICADO]** 6-15 | 0-1 | Debe incluir prefijo de la ciudad si D203=PRY |
| D3 | D215 | dCelRec | Número de celular del receptor | D200 | A | 10-20 | 0-1 | |
| D3 | D216 | dEmailRec | Correo electrónico del receptor | D200 | A | 3-80 | 0-1 | |
| D3 | D217 | dCodCliente | Código del cliente | D200 | A | 3-15 | 0-1 | |

---

## Grupo E — Campos específicos por tipo de Documento Electrónico (E001–E009)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| E | E001 | gDtipDE | Campos específicos por tipo de DE | A001 | G | — | 1-1 | |

### E1 — Campos que componen la Factura Electrónica FE (E010–E099)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| E1 | E010 | gCamFE | Campos que componen la FE | E001 | G | — | 0-1 | Obligatorio si C002=1; No informar si C002≠1 |
| E1 | E011 | iIndPres | Indicador de presencia | E010 | N | 1 | 1-1 | 1=Operación presencial; 2=Operación electrónica; 3=Operación telemarketing; 4=Venta a domicilio; **[NUEVO en v150]** 5=Operación bancaria; **[NUEVO en v150]** 6=Operación cíclica; 9=Otro |
| E1 | E012 | dDesIndPres | Descripción del indicador de presencia | E010 | A | 10-30 | 1-1 | Si E011=9, informar el indicador |
| E1 | **[NUEVO en v150]** E013 | dFecEmNR | Fecha futura del traslado de mercadería | E010 | F | **[MODIFICADO]** 10 | 0-1 | **[NUEVO en v150]** Formato AAAA-MM-DD. Fecha estimada para el traslado de la mercadería y emisión de la NRE cuando corresponda (RG 41/14) |

### E1.1 — Campos de informaciones de Compras Públicas (E020–E029)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| E1.1 | E020 | gCompPub | Campos que describen las informaciones de compras públicas | E010 | G | — | 0-1 | Obligatorio si D202=3 (B2G) |
| E1.1 | E021 | dModCont | Modalidad — Código emitido por la DNCP | E020 | A | 2 | 1-1 | |
| E1.1 | E022 | dEntCont | Entidad — Código emitido por la DNCP | E020 | N | 5 | 1-1 | |
| E1.1 | E023 | dAnoCont | Año — Código emitido por la DNCP | E020 | N | 2 | 1-1 | |
| E1.1 | E024 | dSecCont | Secuencia — emitido por la DNCP | E020 | N | 7 | 1-1 | |
| E1.1 | E025 | dFeCodCont | Fecha de emisión del código de contratación por la DNCP | E020 | F | 10 | 1-1 | Formato AAAA-MM-DD. Esta fecha debe ser anterior a la fecha de emisión de la FE |

### E4 — Campos que componen la Autofactura Electrónica AFE (E300–E399) — **[MODIFICADO]**

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| E4 | E300 | gCamAE | Campos que componen la Autofactura Electrónica | E001 | G | — | 0-1 | Obligatorio si C002=4; No informar si C002≠4 |
| E4 | **[NUEVO en v150]** E301 | iNatVen | Naturaleza del vendedor | E300 | N | 1 | 1-1 | **[NUEVO en v150]** 1=No contribuyente; 2=Extranjero |
| E4 | **[NUEVO en v150]** E302 | dDesNatVen | Descripción de la naturaleza del vendedor | E300 | A | 10-16 | 1-1 | **[NUEVO en v150]** 1="No contribuyente"; 2="Extranjero" |
| E4 | E304 | iTipIDVen | Tipo de documento de identidad del vendedor | E300 | N | 1 | 1-1 | **[MODIFICADO]** 1=Cédula paraguaya; 2=Pasaporte; 3=Cédula extranjera; 4=Carnet de residencia |
| E4 | E305 | dDTipIDVen | Descripción del tipo de documento de identidad del vendedor | E300 | A | 9-20 | 1-1 | **[MODIFICADO]** Referente a E304 |
| E4 | E306 | dNumIDVen | Número de documento de identidad del vendedor | E300 | A | 1-20 | 1-1 | |
| E4 | E307 | dNomVen | Nombre y apellido del vendedor | E300 | A | 4-60 | 1-1 | |
| E4 | E308 | dDirVen | Dirección del vendedor | E300 | A | **[MODIFICADO]** 1-255 | 1-1 | **[NUEVO en v150]** En caso de extranjeros, colocar la dirección donde se realizó la transacción |
| E4 | E309 | dNumCasVen | Número de casa del vendedor | E300 | N | 1-6 | 1-1 | Si no tiene numeración colocar 0 (cero) |
| E4 | E310 | cDepVen | Código del departamento del vendedor | E300 | N | 1-2 | 1-1 | **[NUEVO en v150]** En caso de extranjeros, colocar el departamento donde se realizó la transacción |
| E4 | E311 | dDesDepVen | Descripción del departamento del vendedor | E300 | A | 6-16 | 1-1 | Referente a E310 |
| E4 | E312 | cDisVen | Código del distrito del vendedor | E300 | N | 1-4 | 0-1 | Según Tabla 2.1 - Distritos |
| E4 | E313 | dDesDisVen | Descripción del distrito del vendedor | E300 | A | 1-30 | 0-1 | Obligatorio si existe E312 |
| E4 | E314 | cCiuVen | Código de la ciudad del vendedor | E300 | N | 1-5 | 1-1 | Según Tabla 2.2 - Ciudades |
| E4 | E315 | dDesCiuVen | Descripción de la ciudad del vendedor | E300 | A | 1-30 | 1-1 | Referente a E314 |
| E4 | E316 | dDirProv | **[MODIFICADO]** Lugar de la transacción | E300 | A | **[MODIFICADO]** 1-255 | 1-1 | **[NUEVO en v150]** Nombre de la calle principal (Dirección donde se provee el servicio o producto) |
| E4 | E317 | cDepProv | **[MODIFICADO]** Código del departamento donde se realiza la transacción | E300 | N | 1-2 | 1-1 | Según XSD de Departamentos |
| E4 | E318 | dDesDepProv | **[MODIFICADO]** Descripción del departamento donde se realiza la transacción | E300 | A | 6-16 | 1-1 | Referente a E317 |
| E4 | E319 | cDisProv | **[MODIFICADO]** Código del distrito donde se realiza la transacción | E300 | N | 1-4 | 0-1 | Según Tabla 2.1 - Distritos |
| E4 | E320 | dDesDisProv | **[MODIFICADO]** Descripción del distrito donde se realiza la transacción | E300 | A | 1-30 | 0-1 | Obligatorio si existe E319 |
| E4 | E321 | cCiuProv | **[MODIFICADO]** Código de la ciudad donde se realiza la transacción | E300 | N | 1-5 | 1-1 | Según Tabla 2.2 - Ciudades |
| E4 | E322 | dDesCiuProv | **[MODIFICADO]** Descripción de la ciudad donde se realiza la transacción | E300 | A | 1-30 | 1-1 | Referente a E321 |

### E5 — Campos que componen la Nota de Crédito/Débito Electrónica NCE-NDE (E400–E499)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| E5 | E400 | gCamNCDE | Campos de la Nota de Crédito/Débito Electrónica | E001 | G | — | 0-1 | Obligatorio si C002=5 o 6 (NCE y NDE); No informar si C002≠5 o 6 |
| E5 | E401 | iMotEmi | Motivo de emisión | E400 | N | **[MODIFICADO]** 1-2 | 1-1 | **[MODIFICADO]** 1=Devolución y Ajuste de precios; 2=Devolución; 3=Descuento; 4=Bonificación; 5=Crédito incobrable; 6=Recupero de costo; 7=Recupero de gasto; 8=Ajuste de precio |
| E5 | E402 | dDesMotEmi | Descripción del motivo de emisión | E400 | A | **[MODIFICADO]** 6-30 | 1-1 | **[MODIFICADO]** Referente a E401 |

### E6 — Campos que componen la Nota de Remisión Electrónica (E500–E599)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| E6 | E500 | gCamNRE | Campos que componen la Nota de Remisión Electrónica | E001 | G | — | 0-1 | Obligatorio si C002=7; No informar si C002≠7 |
| E6 | E501 | iMotEmiNR | Motivo de emisión | E500 | N | **[MODIFICADO]** 1-2 | **[MODIFICADO]** 1-1 | 1=Traslado por venta; 2=Traslado por consignación; 3=Exportación; 4=Traslado por compra; 5=Importación; 6=Traslado por devolución; 7=Traslado entre locales de la empresa; 8=Traslado de bienes por transformación; 9=Traslado de bienes por reparación; 10=Traslado por emisor móvil; 11=Exhibición o demostración; 12=Participación en ferias; 13=Traslado de encomienda; **[NUEVO en v150]** 14=Decomiso; **[NUEVO en v150]** 99=Otro (deberá consignarse expresamente el o los motivos). Obs: Cuando el motivo sea por operaciones internas de la empresa, el RUC del receptor debe ser igual al RUC del emisor. |
| E6 | E502 | dDesMotEmiNR | Descripción del motivo de emisión | E500 | A | 5-60 | **[MODIFICADO]** 1-1 | Referente a E501. **[NUEVO en v150]** Si E501=99, describir el motivo |
| E6 | E503 | iRespEmiNR | **[MODIFICADO]** Responsable de la emisión de la NRE | E500 | N | 1 | 1-1 | **[NUEVO en v150]** 1=Emisor de la factura; 2=Poseedor de la factura y bienes; 3=Empresa transportista; 4=Despachante de Aduanas; 5=Agente de transporte o intermediario |
| E6 | **[NUEVO en v150]** E504 | dDesRespEmiNR | Descripción del responsable de la emisión de la NRE | E500 | A | 20-36 | 1-1 | **[NUEVO en v150]** Referente a E503 |
| E6 | E505 | dKmR | Kilómetros estimados de recorrido | E500 | N | 1-5 | 0-1 | |
| E6 | **[NUEVO en v150]** E506 | dFecEm | Fecha futura de emisión de la factura | E500 | F | **[MODIFICADO]** 10 | 0-1 | **[NUEVO en v150]** Formato AAAA-MM-DD. Informar cuando no se ha emitido aún la factura electrónica |

### E7 — Campos que describen la condición de la operación (E600–E699)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| E7 | E600 | gCamCond | Campos que describen la condición de la operación | E001 | G | — | 0-1 | **[MODIFICADO]** Obligatorio si C002=1 o 4; No informar si C002≠1 o 4 |
| E7 | E601 | iCondOpe | Condición de la operación | E600 | N | 1 | 1-1 | 1=Contado; 2=Crédito |
| E7 | E602 | dDCondOpe | Descripción de la condición de operación | E600 | A | 7 | 1-1 | 1="Contado"; 2="Crédito" |

### E7.1 — Campos de la forma de pago al contado o del monto de la entrega inicial (E605–E619) — **[MODIFICADO]**

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| E7.1 | E605 | gPaConEIni | Campos de la forma de pago al contado o del monto de la entrega inicial | E600 | G | **[MODIFICADO]** 0-999 | — | Obligatorio si E601=1; Obligatorio si existe E645 |
| E7.1 | E606 | iTiPago | Tipo de pago | E605 | N | 1-2 | 1-1 | 1=Efectivo; 2=Cheque; 3=Tarjeta de crédito; 4=Tarjeta de débito; 5=Transferencia; 6=Giro; 7=Billetera electrónica; 8=Tarjeta empresarial; 9=Vale; **[MODIFICADO]** 10=Retención; **[MODIFICADO]** 11=Pago por anticipo; 12=Valor fiscal; 13=Valor comercial; 14=Compensación; 15=Permuta; **[NUEVO en v150]** 16=Pago bancario (informar solo si E011=5); **[NUEVO en v150]** 17=Pago Móvil; **[NUEVO en v150]** 18=Donación; **[NUEVO en v150]** 19=Promoción; **[NUEVO en v150]** 20=Consumo Interno; **[NUEVO en v150]** 21=Pago Electrónico; **[NUEVO en v150]** 99=Otro |
| E7.1 | E607 | dDesTiPag | Descripción del tipo de pago | E605 | A | 4-30 | 1-1 | Referente a E606 |
| E7.1 | E608 | dMonTiPag | Monto por tipo de pago | E605 | N | **[MODIFICADO]** 1-15p(0-4) | 1-1 | |
| E7.1 | E609 | cMoneTiPag | Moneda por tipo de pago | E605 | A | 3 | 1-1 | Según ISO 4217 |
| E7.1 | E610 | dDMoneTiPag | Descripción de la moneda por tipo de pago | E605 | A | 3-20 | 1-1 | Referente a E609 |
| E7.1 | E611 | dTiCamTiPag | Tipo de cambio por tipo de pago | E605 | N | 1-5p(0-4) | 0-1 | Obligatorio si E609≠PYG |

### E7.1.1 — Campos del pago con tarjeta de crédito/débito (E620–E629)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| E7.1.1 | E620 | gPagTarCD | Campos del pago con tarjeta de crédito/débito | E605 | G | — | 0-1 | Se activa si E606=3 o 4 |
| E7.1.1 | E621 | iDenTarj | Denominación de la tarjeta | E620 | N | 1-2 | 1-1 | 1=Visa; 2=Mastercard; 3=American Express; 4=Maestro; 5=Panal; **[MODIFICADO]** 6=Cabal; **[MODIFICADO]** 99=Otro |
| E7.1.1 | E622 | dDesDenTarj | Descripción de denominación de la tarjeta | E620 | A | 4-20 | 1-1 | Referente a E621. Si E621=99, informar la descripción |
| E7.1.1 | E623 | dRSProTar | Razón social de la procesadora de tarjeta | E620 | A | 4-60 | **[MODIFICADO]** 0-1 | |
| E7.1.1 | E624 | dRUCProTar | RUC de la procesadora de tarjeta | E620 | A | **[MODIFICADO]** 3-8 | **[MODIFICADO]** 0-1 | |
| E7.1.1 | E625 | dDVProTar | Dígito verificador del RUC de la procesadora | E620 | N | 1 | **[MODIFICADO]** 0-1 | Según algoritmo módulo 11 |
| E7.1.1 | E626 | iForProPa | Forma de procesamiento de pago | E620 | N | 1 | 1-1 | 1=POS; **[MODIFICADO]** 2=Pago Electrónico (ej.: compras por Internet); **[MODIFICADO]** 9=Otro |
| E7.1.1 | E627 | dCodAuOpe | Código de autorización de la operación | E620 | N | 6-10 | **[MODIFICADO]** 0-1 | |
| E7.1.1 | E628 | dNomTit | Nombre del titular de la tarjeta | E620 | A | 4-30 | 0-1 | |
| E7.1.1 | E629 | dNumTarj | Número de la tarjeta | E620 | N | 4 | 0-1 | Cuatro últimos dígitos de la tarjeta |

### E7.1.2 — Campos del pago con cheque (E630–E639)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| E7.1.2 | E630 | gPagCheq | Campos del pago con cheque | E605 | G | — | 0-1 | Se activa si E606=2 |
| E7.1.2 | E631 | dNumCheq | Número de cheque | E630 | A | 8 | 1-1 | Completar con 0 (cero) a la izquierda hasta 8 cifras |
| E7.1.2 | E632 | dBcoEmi | Banco emisor | E630 | A | 4-20 | 1-1 | |

### E7.2 — Campos de la operación a crédito (E640–E649)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| E7.2 | E640 | gPagCred | Campos que describen la operación a crédito | E600 | G | — | 0-1 | Obligatorio si E601=2; No informar si E601≠2 |
| E7.2 | E641 | iCondCred | Condición de la operación a crédito | E640 | N | 1 | 1-1 | 1=Plazo; 2=Cuota |
| E7.2 | E642 | dDCondCred | Descripción de la condición de la operación a crédito | E640 | A | 5-6 | 1-1 | 1="Plazo"; 2="Cuota" |
| E7.2 | E643 | dPlazoCre | Plazo del crédito | E640 | A | 2-15 | 0-1 | Obligatorio si E641=1. Ejemplo: 30 días, 12 meses |
| E7.2 | E644 | dCuotas | Cantidad de cuotas | E640 | N | 1-3 | 0-1 | Obligatorio si E641=2. Ejemplo: 12, 24, 36 |
| E7.2 | E645 | dMonEnt | Monto de la entrega inicial | E640 | N | **[MODIFICADO]** 1-15p(0-4) | 0-1 | |

### E7.2.1 — Campos de las cuotas (E650–E659)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| E7.2.1 | E650 | gCuotas | Campos que describen las cuotas | E640 | G | — | 0-999 | ~~Se activa si E641=2~~ |
| E7.2.1 | **[NUEVO en v150]** E653 | cMoneCuo | Moneda de las cuotas | E650 | A | 3 | 1-1 | **[NUEVO en v150]** Según ISO 4217 |
| E7.2.1 | **[NUEVO en v150]** E654 | dDMoneCuo | Descripción de la moneda de las cuotas | E650 | A | 3-20 | 1-1 | **[NUEVO en v150]** Referente a E653 |
| E7.2.1 | E651 | dMonCuota | Monto de cada cuota | E650 | N | **[MODIFICADO]** 1-15p(0-4) | 1-1 | |
| E7.2.1 | E652 | dVencCuo | Fecha de vencimiento de cada cuota | E650 | F | 10 | 0-1 | Formato AAAA-MM-DD |

### E8 — Campos que describen los ítems de la operación (E700–E899)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| E8 | E700 | gCamItem | Campos que describen los ítems de la operación | E001 | G | — | 1-999 | |
| E8 | E701 | dCodInt | Código interno | E700 | A | 1-20 | 1-1 | Código interno de identificación de la mercadería o servicio. No se pueden tener ítems distintos con el mismo código interno en el catálogo. Puede repetirse en el DE si el producto/servicio es el mismo. |
| E8 | E702 | dParAranc | Partida arancelaria | E700 | N | 4 | 0-1 | |
| E8 | E703 | dNCM | Nomenclatura común del Mercosur (NCM) | E700 | N | 6-8 | 0-1 | |
| E8 | E704 | dDncpG | Código DNCP – Nivel General | E700 | A | 8 | 0-1 | Obligatorio si D202=3. Completar con 0 (cero) a la izquierda para espacios vacíos |
| E8 | E705 | dDncpE | Código DNCP – Nivel Específico | E700 | A | 3-4 | 0-1 | Obligatorio si existe E704 |
| E8 | E706 | dGtin | Código GTIN por producto | E700 | N | 8,12,13,14 | 0-1 | Informar si la mercadería tiene GTIN |
| E8 | E707 | dGtinPq | Código GTIN por paquete | E700 | N | 8,12,13,14 | 0-1 | Informar si el paquete tiene GTIN |
| E8 | E708 | dDesProSer | Descripción del producto y/o servicio | E700 | A | 1-120 | 1-1 | Equivalente a nombre del producto establecido en la RG 24/2019 |
| E8 | E709 | cUniMed | Unidad de medida | E700 | N | 1-5 | 1-1 | Según Tabla 5 – Unidad de Medida. Si D202=3, utilizar datos del WS de la DNCP (atributo "ID") |
| E8 | E710 | dDesUniMed | Descripción de la unidad de medida | E700 | A | 1-10 | 1-1 | Referente a E709. Utilizar el atributo "Código". Ejemplo: UNI |
| E8 | E711 | dCantProSer | Cantidad del producto y/o servicio | E700 | N | **[MODIFICADO]** 1-10p(0-4) | 1-1 | |
| E8 | E712 | cPaisOrig | Código del país de origen del producto | E700 | A | 3 | 0-1 | Según XSD de Codificación de Países |
| E8 | E713 | dDesPaisOrig | Descripción del país de origen del producto | E700 | A | 4-30 | 0-1 | Obligatorio si existe E712 |
| E8 | E714 | dInfItem | Información de interés del emisor con respecto al ítem | E700 | A | 1-500 | 0-1 | |
| E8 | **[NUEVO en v150]** E715 | cRelMerc | Código de datos de relevancia de las mercaderías | E700 | N | 1 | 0-1 | **[NUEVO en v150]** Opcional si C002=7. 1=Tolerancia de quiebra; 2=Tolerancia de merma. Según RG 41/14 |
| E8 | **[NUEVO en v150]** E716 | dDesRelMerc | Descripción del código de datos de relevancia de las mercaderías | E700 | A | 19-21 | 0-1 | **[NUEVO en v150]** 1="Tolerancia de quiebra"; 2="Tolerancia de merma" |
| E8 | **[NUEVO en v150]** E717 | dCanQuiMer | Cantidad de quiebra o merma | E700 | N | 1-10(0-4) | 0-1 | **[NUEVO en v150]** Obligatorio si se informa E715. Según RG 41/14 |
| E8 | **[NUEVO en v150]** E718 | dPorQuiMer | Porcentaje de quiebra o merma | E700 | N | 1-3(0-8) | 0-1 | **[NUEVO en v150]** Obligatorio si se informa E715. Según RG 41/14 |
| E8 | **[NUEVO en v150]** E719 | dCDCAnticipo | CDC del anticipo | E700 | A | 44 | 0-1 | **[NUEVO en v150]** Obligatorio cuando se utilice una factura asociada con tipo de transacción Anticipo (D011 de la factura asociada = 9) |

### E8.1 — Campos del precio, tipo de cambio y valor total por ítem (E720–E729) — **[MODIFICADO]**

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| E8.1 | E720 | gValorItem | Campos que describen los precios, descuentos y valor total por ítem | E700 | G | — | 0-1 | Obligatorio si C002≠7; No informar si C002=7 |
| E8.1 | E721 | dPUniProSer | **[MODIFICADO]** Precio unitario del producto y/o servicio (incluidos impuestos) | E720 | N | **[MODIFICADO]** 1-15p(0-8) | 1-1 | |
| E8.1 | E725 | dTiCamIt | Tipo de cambio por ítem | E720 | N | 1-5p(0-4) | 0-1 | ~~Obligatorio si D015≠PYG~~ Obligatorio si D017=2; No informar si D017=1 |
| E8.1 | **[NUEVO en v150]** E727 | dTotBruOpeItem | Total bruto de la operación por ítem | E720 | N | **[NUEVO en v150]** 1-15p(0-8) | 1-1 | **[NUEVO en v150]** Corresponde a la multiplicación del precio por ítem (E721) y la cantidad por ítem (E711) |

### E8.1.1 — Campos de descuentos, anticipos y valor total por ítem (EA001–EA050) — **[NUEVO en v150]**

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| **[NUEVO en v150]** E8.1.1 | EA001 | gValorRestaItem | Campos que describen los descuentos, anticipos y valor total por ítem | E720 | G | — | 1-1 | **[NUEVO en v150]** |
| E8.1.1 | EA002 | dDescItem | **[MODIFICADO]** Descuento particular sobre el precio unitario por ítem (incluidos impuestos) | EA001 | N | **[MODIFICADO]** 1-15p(0-8) | **[MODIFICADO]** 0-1 | ~~Si no hay descuento por ítem completar con 0 (cero)~~ |
| E8.1.1 | EA003 | dPorcDesIt | **[MODIFICADO]** Porcentaje de descuento particular por ítem | EA001 | N | **[MODIFICADO]** 1-3p(0-8) | 0-1 | Debe existir si EA002 es mayor a **[NUEVO en v150]** 0 (cero). Cálculo: `[EA002 * 100 / E721]` |
| E8.1.1 | **[NUEVO en v150]** EA004 | dDescGloItem | Descuento global sobre el precio unitario por ítem (incluidos impuestos) | EA001 | N | **[NUEVO en v150]** 1-15p(0-8) | 0-1 | **[NUEVO en v150]** Si se cuenta con un descuento global, debe ser aplicado (no prorrateo) a cada uno de los ítems |
| E8.1.1 | **[NUEVO en v150]** EA006 | dAntPreUniIt | Anticipo particular sobre el precio unitario por ítem (incluidos impuestos) | EA001 | N | **[NUEVO en v150]** 1-15p(0-8) | 0-1 | **[NUEVO en v150]** Informar en la misma denominación monetaria de la FE de anticipo asociada (D015 de la FE asociada) |
| E8.1.1 | **[NUEVO en v150]** EA007 | dAntGloPreUniIt | Anticipo global sobre el precio unitario por ítem (incluidos impuestos) | EA001 | N | **[NUEVO en v150]** 1-15p(0-8) | 0-1 | **[NUEVO en v150]** Si se cuenta con anticipo global, debe ser aplicado a cada ítem |
| E8.1.1 | EA008 | dTotOpeItem | Valor total de la operación por ítem | EA001 | N | **[MODIFICADO]** 1-15p(0-8) | 1-1 | **[MODIFICADO]** Cálculo para IVA, Renta, ninguno, IVA-Renta: `(E721 – EA002 – EA004 – EA006 – EA007) * E711`. **[NUEVO en v150]** Para Autofactura (C002=4): `E721*E711` |
| E8.1.1 | EA009 | dTotOpeGs | Valor total de la operación por ítem en guaraníes | EA001 | N | **[MODIFICADO]** 1-15p(0-8) | 0-1 | Obligatorio si existe E725. Corresponde al cálculo aritmético `EA008 * E725` |

### E8.2 — Campos del IVA de la operación por ítem (E730–E739)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| E8.2 | E730 | gCamIVA | Campos que describen el IVA de la operación | E700 | G | — | 0-1 | **[MODIFICADO]** Obligatorio si D013=1, 3, 4 o 5 y C002≠4 o 7; No informar si D013=2 y C002=4 o 7 |
| E8.2 | E731 | iAfecIVA | Forma de afectación tributaria del IVA | E730 | N | 1 | 1-1 | 1=Gravado IVA; 2=Exonerado; 3=Exento; 4=Gravado parcial |
| E8.2 | E732 | dDesAfecIVA | Descripción de la forma de afectación tributaria del IVA | E730 | A | 6-37 | 1-1 | **[MODIFICADO]** Referente a E731. Literales exactos del XSD de producción (enumeración cerrada): 1=`Gravado IVA`; 2=`Exonerado (Art. 100 - Ley 6380/2019)` (NT-010; el MT original decía "Art. 83- Ley 125/91"); 3=`Exento`; 4=`Gravado parcial (Grav- Exento)` (con espacio tras el guion) |
| E8.2 | E733 | dPropIVA | Proporción gravada de IVA | E730 | N | **[MODIFICADO]** 1-3p(0-8) | 1-1 | **[MODIFICADO]** Corresponde al porcentaje (%) gravado. Ejemplo: 100, 50, 30, 0 |
| E8.2 | E734 | dTasaIVA | Tasa del IVA | E730 | N | 1-2 | 1-1 | Porcentaje (%) de la tasa en números enteros: 0 (para E731=2 o 3); 5 (para E731=1 o 4); 10 (para E731=1 o 4) |
| E8.2 | E735 | dBasGravIVA | Base gravada del IVA por ítem | E730 | N | **[MODIFICADO]** 1-15p(0-8) | 1-1 | Si E731=1 o 4: **[MODIFICADO]** `[EA008*(E733/100)]/1,1` si tasa 10%; `[EA008*(E733/100)]/1,05` si tasa 5%. Si E731=2 o 3: igual a 0 |
| E8.2 | E736 | dLiqIVAItem | Liquidación del IVA por ítem | E730 | N | **[MODIFICADO]** 1-15p(0-8) | 1-1 | Cálculo: `E735 * (E734/100)`. Si E731=2 o 3: igual a 0 |

---

## Grupo F — Campos que describen los subtotales y totales de la transacción documentada (F001–F099)

> Reglas de redondeo (Res. 347/2014 SEDECO): aplica a múltiplos de 50 guaraníes. **[MODIFICADO]** Para monedas extranjeras, las reglas de validación aceptarán redondeos de 50 céntimos.

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| F | F001 | gTotSub | Campos de subtotales y totales | A001 | G | — | 0-1 | Obligatorio si C002≠7. **[MODIFICADO]** No informar si C002=7. **[MODIFICADO]** Cuando C002=4, no informar F002, F003, F004, F005, F015, F016, F017, F018, F019, F020, F023, F025 y F026 |
| F | F002 | dSubExe | Subtotal de la operación exenta | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 0-1 | **[MODIFICADO]** Si E731=3: Suma de todas las ocurrencias de EA008 cuando la operación sea exenta |
| F | F003 | dSubExo | Subtotal de la operación exonerada | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 0-1 | **[MODIFICADO]** Si E731=2: Suma de todas las ocurrencias de EA008 cuando exonerada |
| F | F004 | dSub5 | Subtotal de la operación con IVA incluido a la tasa 5% | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 0-1 | **[MODIFICADO]** Si E731=1 o 4: Suma de EA008 cuando tasa del 5% (E734=5). No debe existir si D013≠1 |
| F | F005 | dSub10 | Subtotal de la operación con IVA incluido a la tasa 10% | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 0-1 | **[MODIFICADO]** Si E731=1 o 4: Suma de EA008 cuando tasa del 10% (E734=10). No debe existir si D013≠1 |
| F | **[MODIFICADO]** F008 | dTotOpe | **[MODIFICADO]** Total Bruto de la operación | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 1-1 | **[MODIFICADO]** Cuando D013=1, 3, 4 o 5: suma de F002+F003+F004+F005. **[NUEVO en v150]** Cuando C002=4: suma de todas las ocurrencias de EA008 |
| F | **[MODIFICADO]** F009 | dTotDesc | **[MODIFICADO]** Total descuento particular por ítem | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 1-1 | **[MODIFICADO]** Suma de todos los descuentos particulares por ítem (EA002) |
| F | **[NUEVO en v150]** F033 | dTotDescGlotem | Total descuento global por ítem | F001 | N | **[NUEVO en v150]** 1-15p(0-8) | 1-1 | **[NUEVO en v150]** Sumatoria de todas las ocurrencias de descuentos globales por ítem (EA004) |
| F | **[NUEVO en v150]** F034 | dTotAntItem | Total Anticipo por ítem | F001 | N | **[NUEVO en v150]** 1-15p(0-8) | 1-1 | **[NUEVO en v150]** Sumatoria de todas las ocurrencias de anticipos por ítem (EA006) |
| F | **[NUEVO en v150]** F035 | dTotAnt | Total Anticipo global por ítem | F001 | N | **[NUEVO en v150]** 1-15p(0-8) | 1-1 | **[NUEVO en v150]** Sumatoria de todas las ocurrencias de anticipos global por ítem (EA007) |
| F | **[MODIFICADO]** F010 | dPorcDescTotal | **[MODIFICADO]** Porcentaje de descuento global sobre total de la operación | F001 | N | **[MODIFICADO]** 1-3p(0-8) | 1-1 | **[NUEVO en v150]** Informativo; si no existe %, completar con cero |
| F | **[MODIFICADO]** F011 | dDescTotal | **[MODIFICADO]** Total Descuentos de la operación | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 1-1 | **[NUEVO en v150]** Sumatoria de todos los descuentos (Global por Ítem y particular por ítem) de cada ítem |
| F | **[MODIFICADO]** F012 | dAnticipo | **[MODIFICADO]** Total Anticipos de la operación | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 1-1 | **[NUEVO en v150]** Sumatoria de todos los Anticipos (Global por Ítem y particular por ítem) |
| F | **[MODIFICADO]** F013 | dRedon | **[MODIFICADO]** Redondeo de la operación | F001 | N | 1-3p(0-4) | 1-1 | **[NUEVO en v150]** Se realiza sobre el campo F008. Si no cuenta con redondeo, completar con cero |
| F | **[MODIFICADO]** F025 | dComi | **[MODIFICADO]** Comisión de la operación | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 0-1 | |
| F | **[MODIFICADO]** F014 | dTotGralOpe | Total Neto de la operación | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 1-1 | **[MODIFICADO]** Cálculo aritmético: `F008 - F013 + F025` |
| F | **[MODIFICADO]** F015 | dIVA5 | Liquidación del IVA a la tasa del 5% | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 0-1 | Suma de E736 cuando E734=5. **[NUEVO en v150]** No debe existir si D013≠1 o D013≠5 |
| F | **[MODIFICADO]** F016 | dIVA10 | Liquidación del IVA a la tasa del 10% | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 0-1 | Suma de E736 cuando E734=10. **[NUEVO en v150]** No debe existir si D013≠1 o D013≠5 |
| F | **[NUEVO en v150]** F036 | dLiqTotIVA5 | Liquidación total del IVA por redondeo a la tasa del 5% | F001 | N | **[NUEVO en v150]** 1-15p(0-8) | 0-1 | **[NUEVO en v150]** Cálculo del IVA al 5% sobre el redondeo: `(Valor del redondeo/1,05)`, cuando E734=5 |
| F | **[NUEVO en v150]** F037 | dLiqTotIVA10 | Liquidación total del IVA por redondeo a la tasa del 10% | F001 | N | **[NUEVO en v150]** 1-15p(0-8) | 0-1 | **[NUEVO en v150]** Cálculo del IVA al 10% sobre el redondeo: `(Valor del redondeo/1,1)`, cuando E734=10 |
| F | **[MODIFICADO]** F026 | dIVAComi | **[MODIFICADO]** Liquidación total del IVA de la comisión | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 0-1 | Se aplica la tasa del 10% para comisiones |
| F | **[MODIFICADO]** F017 | dTotIVA | Liquidación total del IVA | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 0-1 | **[MODIFICADO]** Cálculo: `F015 + F016 – F036 – F037 + F026`. **[NUEVO en v150]** No debe existir si D013≠1 o D013≠5 |
| F | **[MODIFICADO]** F018 | dBaseGrav5 | Total base gravada al 5% | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 0-1 | Suma de E735 cuando E734=5. **[NUEVO en v150]** No debe existir si D013≠1 o D013≠5 |
| F | **[MODIFICADO]** F019 | dBaseGrav10 | Total base gravada al 10% | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 0-1 | Suma de E735 cuando E734=10. **[NUEVO en v150]** No debe existir si D013≠1 o D013≠5 |
| F | **[MODIFICADO]** F020 | dTBasGraIVA | Total de la base gravada de IVA | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 0-1 | **[MODIFICADO]** Corresponde al cálculo aritmético F018+F019. **[NUEVO en v150]** No debe existir si D013≠1 o D013≠5 |
| F | **[MODIFICADO]** F023 | dTotalGs | Total general de la operación en Guaraníes | F001 | N | **[MODIFICADO]** 1-15p(0-8) | 0-1 | Si D015≠PYG y D017=1: cálculo aritmético F014 * D018. Si D015≠PYG y D017=2: **[MODIFICADO]** suma de todas las ocurrencias de EA009. **[NUEVO en v150]** No informar si D015=PYG. **[NUEVO en v150]** Cuando C002=4 corresponde a F014 |
| F | ~~F024~~ | ~~dTotCom~~ | ~~Total + comisión~~ | ~~F001~~ | ~~N~~ | ~~1-15p(0-8)~~ | ~~0-1~~ | ⚠️ **ELIMINADO** |

---

## Grupo G — Campos complementarios comerciales de uso general (G001–G049)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| G | **[MODIFICADO]** G001 | gCamGen | Campos de uso general | A001 | G | — | 0-1 | |
| G | G002 | dOrdCompra | Número de orden de compra | G001 | A | 1-15 | 0-1 | |
| G | G003 | dOrdVta | Número de orden de venta | G001 | A | 1-15 | 0-1 | |
| G | G004 | dAsiento | Número de asiento contable | G001 | A | 1-10 | 0-1 | |

---

## Grupo G1 — Campos generales de la carga (G050–G099) **[NUEVO en v150]**

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| G1 | **[NUEVO en v150]** G050 | gCamCarg | Campos generales de la carga | G001 | G | — | 0-1 | Opcional cuando C002=1 o C002=7. No informar para C002≠1 y C002≠7 |
| G1 | **[NUEVO en v150]** G051 | cUniMedTotVol | Unidad de medida del total de volumen de la mercadería | G050 | N | 1-5 | 0-1 | Según Tabla 5 – Unidad de Medida. Si D202=3 utilizar los datos del WS del link de la DNCP. Utilizar el atributo "ID" |
| G1 | **[NUEVO en v150]** G052 | dDesUniMedTotVol | Descripción de la unidad de medida del total de volumen de la mercadería | G050 | A | 1-10 | 0-1 | Referente al campo G051. Utilizar el atributo "Código". Ejemplo: UNI |
| G1 | **[NUEVO en v150]** G053 | dTotVolMerc | Total volumen de la mercadería | G050 | N | 1-20 | 0-1 | Corresponde al volumen total de ítems que se han informado |
| G1 | **[NUEVO en v150]** G054 | cUniMedTotPes | Unidad de medida del peso total de la mercadería | G050 | N | 1-5 | 0-1 | Según Tabla 5 – Unidad de Medida. Si D202=3 utilizar los datos del WS del link de la DNCP. Utilizar el atributo "ID" |
| G1 | **[NUEVO en v150]** G055 | dDesUniMedTotPes | Descripción de la unidad de medida del peso total de la mercadería | G050 | A | 1-10 | 0-1 | Referente al campo G054. Utilizar el atributo "Código". Ejemplo: UNI |
| G1 | **[NUEVO en v150]** G056 | dTotPesMerc | Total peso de la mercadería | G050 | N | 1-20 | 0-1 | Corresponde al peso total de ítems que se han informado |
| G1 | **[NUEVO en v150]** G057 | iCarCarga | Características de la Carga | G050 | N | 1 | 0-1 | 1=Mercaderías con cadena de frío; 2=Carga peligrosa; 3=Otro de características similares (especificar). Obligatorio cuando lo exige la RG 41/14 |
| G1 | **[NUEVO en v150]** G058 | dDesCarCarga | Descripción de las características de la carga | G050 | A | 1-50 | 0-1 | 1="Mercaderías con cadena de frío"; 2="Carga peligrosa". Si G057=3, informar la característica de la carga. Obligatorio cuando lo exige la RG 41/14. Obligatorio para KuDE |

---

## Grupo H — Campos que identifican al documento asociado (H001–H049)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| H | H001 | gCamDEAsoc | Campos que identifican al DE asociado | A001 | G | — | 0-99 | **[MODIFICADO]** Obligatorio si C002=4, 5 o 6. **[NUEVO en v150]** Opcional si C002=1 o 7 |
| H | H002 | iTipDocAso | Tipo de documento asociado | H001 | N | 1 | 1-1 | 1=Electrónico. **[NUEVO en v150]** 2=Impreso; 3=Constancia Electrónica |
| H | H003 | dDesTipDocAso | Descripción del tipo de documento asociado | H001 | A | 7-11 | 1-1 | **[NUEVO en v150]** 1="Electrónico"; 2="Impreso"; 3="Constancia Electrónica" |
| H | H004 | dCdCDERef | CDC del DTE referenciado | H001 | A | 44 | 0-1 | **[NUEVO en v150]** Obligatorio si H002=1. No informar si H002=2 o 3 |
| H | H005 | dNTimDI | Nro. timbrado documento impreso de referencia | H001 | N | 8 | 0-1 | **[MODIFICADO]** Obligatorio si H002=2. **[NUEVO en v150]** No informar si H002=1 o 3 |
| H | H006 | dEstDocAso | Establecimiento | H001 | A | 3 | 0-1 | **[MODIFICADO]** Obligatorio si H002=2. Completar con 0 (cero) a la izquierda. **[NUEVO en v150]** No informar si H002=1 o 3 |
| H | H007 | dPExpDocAso | Punto de expedición | H001 | A | 3 | 0-1 | **[MODIFICADO]** Obligatorio si H002=2. Completar con 0 (cero) a la izquierda. **[NUEVO en v150]** No informar si H002=1 o 3 |
| H | H008 | dNumDocAso | Número del documento | H001 | A | 7 | 0-1 | **[MODIFICADO]** Obligatorio si H002=2. Completar con 0 (cero) a la izquierda hasta alcanzar 7 cifras. **[NUEVO en v150]** No informar si H002=1 o 3 |
| H | H009 | iTipoDocAso | Tipo de documento impreso | H001 | N | 1 | 0-1 | **[NUEVO en v150]** Obligatorio si H002=2. No informar si H002=1 o 3. 1=Factura; 2=Nota de crédito; 3=Nota de débito; 4=Nota de remisión; 5=Comprobante de retención |
| H | H010 | dDTipoDocAso | Descripción del tipo de documento impreso | H001 | A | 7-16 | 0-1 | Obligatorio si existe H009. 1="Factura"; 2="Nota de crédito"; 3="Nota de débito"; 4="Nota de remisión"; 5="Comprobante de retención" |
| H | H011 | dFecEmiDI | Fecha de emisión del documento impreso de referencia | H001 | F | 10 | 0-1 | Obligatorio si existe H005. **[NUEVO en v150]** Formato AAAA-MM-DD. No informar si H005 no existe |
| H | H012 | dNumComRet | Número de comprobante de retención | H001 | A | 15 | 0-1 | **[MODIFICADO]** Si E606=10, es opcional informar número de comprobante de retención (Cambio temporal). No informar si E606≠10 |
| H | H013 | dNumResCF | Número de resolución de crédito fiscal | H001 | A | 15 | 0-1 | Si D011=12 obligatorio informar número de resolución de crédito fiscal. No informar si D011≠12 |
| H | **[NUEVO en v150]** H014 | iTipCons | Tipo de constancia | H001 | N | 1 | 0-1 | **[NUEVO en v150]** Obligatorio cuando H002=3. No informar cuando H002≠3. 1=Constancia de no ser contribuyente; 2=Constancia de microproductores |
| H | **[NUEVO en v150]** H015 | dDesTipCons | Descripción del tipo de constancia | H001 | A | 30-34 | 0-1 | **[NUEVO en v150]** Obligatorio si se informa H014. 1="Constancia de no ser contribuyente"; 2="Constancia de microproductores" |
| H | **[NUEVO en v150]** H016 | dNumCons | Número de constancia | H001 | N | 11 | 0-1 | **[NUEVO en v150]** Obligatorio cuando H002=3 y H014=2. No informar cuando H002≠3 |
| H | **[NUEVO en v150]** H017 | dNumControl | Número de control de la constancia | H001 | A | 8 | 0-1 | **[NUEVO en v150]** Obligatorio cuando H002=3 y H014=2. No informar cuando H002≠3 |

---

## Grupo I — Información de la Firma Digital del DTE (I001–I049)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| I | I001 | Signature | Firma Digital del DTE | AA001 | G | — | 1-1 | Según el estándar XML signature. Debe ser firmado el grupo A (campo A001) que contiene los grupos de información A hasta H |

---

## Grupo J — Campos fuera de la Firma Digital (J001–J049)

| Grupo | ID | Campo | Descripción | Nodo Padre | Tipo | Long. | Ocurr. | Observaciones |
|-------|-----|-------|-------------|-----------|------|-------|--------|---------------|
| J | J001 | gCamFuFD | Campos fuera de la firma digital | AA001 | G | — | 1-1 | |
| J | J002 | dCarQR | Caracteres correspondientes al código QR | J001 | A | 100-600 | 1-1 | Debe ser validado contra la información incluida en el XML del DE, de acuerdo con lo especificado en el capítulo del QR del MT |
