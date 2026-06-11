# Reglas de Validación del Documento Electrónico

> **Fuente:** Manual Técnico SIFEN v150, secciones 12.3 y 12.4, y Notas Técnicas NT-001 a NT-026

## Descripción

Las reglas de validación son condiciones que el SIFEN verifica antes de aprobar un Documento Electrónico. Las reglas están identificadas con códigos alfanuméricos (ej: D011a, EA004a, NT-013) referenciados en el Manual Técnico.

---

## Reglas del Grupo A (Datos del DE)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| A002a | CDC (A002) | Los 44 dígitos del CDC deben conformar la estructura definida (RUC 8d + dígito verificador + año 4d + timbrado 8d + establecimiento 3d + punto expedición 3d + número 7d + tipo DE 1d + código seguridad 9d + verificador Módulo 11 1d) |
| A002b | CDC (A002) | El dígito verificador del CDC debe calcularse con Módulo 11 sobre los primeros 43 dígitos |

---

## Reglas del Grupo B (Inherentes a la Operación)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| B002a | dFecFirma (B002) | La fecha de firma no puede ser futura (mayor a la fecha/hora actual del servidor SIFEN) |
| B002b | dFecFirma (B002) | La diferencia entre dFecFirma y la hora actual del servidor no puede superar el rango tolerado (±5 minutos según sincronización NTP) |
| B006a | dInfoFisc (B006) | Si C002=7 (NRE): obligatorio. Debe contener el mensaje del Art. 3 Inc. 7 de la RG N° 41/2014 |

---

## Reglas del Grupo C (Timbrado)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| C002a | iTiDE (C002) | Valor debe pertenecer al conjunto {1, 2, 3, 4, 5, 6, 7, 8} (tipos habilitados) |
| C004a | dNumTim (C004) | El timbrado debe estar vigente y habilitado para el RUC del emisor en la SET |
| C007a | dEst (C007) | El establecimiento debe corresponder al RUC del emisor en el timbrado |
| C008a | dPunExp (C008) | El punto de expedición debe corresponder al establecimiento declarado |
| C010a | dSerieNum (C010) | Si informado: formato AA-ZZ (dos letras mayúsculas), secuencia progresiva |
| C010b | dSerieNum (C010) | No puede retroceder a una serie anterior ya agotada |

---

## Reglas del Grupo D1 (Operación Comercial)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| D011a | iTipTra (D011) | Agregado por NT-006. Si D011=1 (B2B), el receptor debe ser contribuyente (D201=1). Si D011=2 (B2C), receptor puede ser no contribuyente |
| D011b | iTipTra (D011) | Si C002=1 o C002=4: obligatorio. Si C002≠1 y C002≠4: no informar |
| D015a | dMonTiChange (D015) | Si C002=4 (AFE): debe ser PYG (NT-012, validación D022) |
| D019a | iCondAnt (D019) | Si D019=1: un solo tipo de anticipo para todo el DE. Si D019=2: anticipos por ítem |

---

## Reglas del Grupo D1.1 (Obligaciones Afectadas, NT-018)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| D031a | cOblAfe (D031) | NT-022: No puede repetirse el mismo código de obligación dentro de un mismo DE |
| D031b | cOblAfe (D031) | El código de obligación debe pertenecer a la Tabla 12 del MT |
| D032a | dDesOblAfe (D032) | Descripción debe corresponder al código D031 según Tabla 12 |

---

## Reglas del Grupo D2 (Emisor)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| D101a | — | Eliminada por NT-004. (Anteriormente validaba longitud del RUC del emisor) |
| D108a | dNomEmi (D108) | Nombre del emisor debe coincidir con el registrado en la SET para el RUC informado |

---

## Reglas del Grupo D3 (Receptor)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| D202a | iTiOpe (D202) | Si el RUC del receptor (D206) corresponde a un OEE (Organismo del Estado): D202 debe ser 3 (B2G). NT-020 |
| D202b | iTiOpe (D202) | Valores válidos: 1=B2B, 2=B2C, 3=B2G, 4=exportación |
| D204a | iTipIDRec (D204) | NT-005: Longitud ampliada. Código debe pertenecer a la Tabla correspondiente |
| D207a | dDVRec (D207) | Si D206 está informado: el dígito verificador debe ser correcto (Módulo 11) |
| D208a | iTipIDRec (D208) | Si D201=2 y D202≠4: obligatorio. Si D201=1: no informar |
| D208b | iTipIDRec (D208) | NT-023: Se elimina la condición "No informar si D202=4" (puede informarse en exportaciones) |
| D208c | iTipIDRec (D208) | NT-024 (vigente desde 01/01/2025): Si monto total ≥ 7.000.000 PYG (F023 o F014), no puede ser Innominado (D208≠5). Historial: 60M (MT original, salvo D011=13) → 35M (NT-021) → 7M (NT-024) |
| D208d | iTipIDRec (D208) | NT-024: A partir del 01/01/2025, límite actualizado a 7.000.000 PYG |
| D213a | dDirRec (D213) | Si C002=7 o D202=4: obligatorio |
| D219a | cDepRec (D219) | NT-003: Si D213 informado y D202≠4: obligatorio |
| D222a | dDesCiuRec (D222) | NT-017: Mensaje actualizado para la descripción de ciudad del receptor |
| D223a | cCiuRec (D223) | NT-003: Si D213 informado y D202≠4: obligatorio |
| D224a | dDesDepRec (D224) | NT-017: Mensaje actualizado para la descripción de departamento del receptor |

---

## Reglas del Grupo E8 (Ítems)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| E701a | dDesProSer (E701) | NT-009: Longitud 1-1000 (ampliada). No puede estar vacío |
| E708a | dInfoItem (E708) | NT-009: Longitud 1-2000 (ampliada) |
| E711a | dUniMed (E711) | NT-023: Precisión decimal actualizada |
| EA004a | dDescItem (EA004) | NT-001: Monto del descuento por ítem. Fórmula: dDescItem = EA008 * E732 / 100 (si descuento es porcentaje) |
| EA008a | dTotBruOpeItem (EA008) | NT-001: Total bruto del ítem = E721 * E711 (precio * cantidad) |

---

## Reglas del Grupo E8.2 (IVA por Ítem)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| E731a | iAfecIVA (E731) | Valor debe pertenecer a {1=Gravado IVA, 2=Exonerado, 3=Exento, 4=Gravado parcial}. Literales exactos de E732 según XSD de producción: `Gravado IVA`, `Exonerado (Art. 100 - Ley 6380/2019)`, `Exento`, `Gravado parcial (Grav- Exento)` |
| E733a | dPropIVA (E733) | Si E731=4: valor debe ser mayor a 0 y menor a 100 (no puede ser 100%) |
| E735a | dBasGravIVA (E735) | NT-013: Si E731=1 o E731=4: fórmula = [100 * EA008 * E733] / [10000 + (E734 * E733)] |
| E735b | dBasGravIVA (E735) | Si E731=2 o E731=3: debe ser igual a 0 |
| E737a | dBasExe (E737) | NT-013: Si E731=4: fórmula = [100 * EA008 * (100 - E733)] / [10000 + (E734 * E733)] |
| E737b | dBasExe (E737) | Si E731=1, 2 o 3: debe ser igual a 0 |

---

## Reglas del Grupo E8.1.1 (Descuentos y Anticipos)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| EA004a | dDescItem (EA004) | NT-001: Si descuento es porcentaje, el monto se calcula como EA008 * E732 / 100 |
| EA009a | dTotOpeItem (EA009) | NT-001: Total neto = EA008 - EA004 - EA006 + EA005 + EA007 (bruto - descuento - anticipo + incremento) |

---

## Reglas del Grupo E6 (Condición de Operación)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| E601a | iCondOpe (E601) | Si C002=1 o C002=4: obligatorio. Valores: 1=contado, 2=crédito |
| E611a | dTiCamTiPag (E611) | Si E609≠PYG: obligatorio (tipo de cambio para la forma de pago) |
| E641a | iForPag (E641) | Si E601=2 (crédito): forma de pago del crédito: 1=plazo, 2=cuotas |
| E643a | dPlazoCre (E643) | Si E641=1: obligatorio (plazo en días) |
| E644a | dCuotas (E644) | Si E641=2: obligatorio (número de cuotas) |

---

## Reglas del Grupo F (Totales)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| F002a | dTotGravIVA10 (F002) | NT-013: Suma de EA009 de todos los ítems con E731=1 |
| F004a | dTotGravIVA5 (F004) | NT-013: Suma de EA009 de todos los ítems con E731=2 |
| F005a | dTotExe (F005) | NT-013: Suma de EA009 de todos los ítems con E731=3 |
| F009a | dTotDesc (F009) | NT-001: Suma de EA004 de todos los ítems |
| F011a | dTotDescGlotem (F011) | NT-001: Monto descuento global sobre el total del DE |
| F012a | dAnticipItem (F012) | NT-001: Suma de EA006 de todos los ítems |
| F014a | dTotOpe (F014) | NT-001: Total de la operación = suma de EA009 de todos los ítems |
| F023a | dTotalGs (F023) | Si D015=PYG: no informar. Si D015≠PYG y D017=1: F014 * D018. Si D015≠PYG y D017=2: suma de EA009 |
| F033a | dIVA10 (F033) | NT-001: IVA al 10% = F002 * 10 / 110 |
| F034a | dIVA5 (F034) | NT-001: IVA al 5% = F004 * 5 / 105 |
| F035a | dExe (F035) | NT-001: Exento = F005 |

---

## Reglas del Grupo H (Documento Asociado)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| H004a | dCDC (H004) | Si H002=1 (CDC de DE asociado): el CDC debe existir y haber sido aprobado por SIFEN |
| H004b | dCDC (H004) | NT-015: Si C002=5 o C002=6 (NCE/NDE): el CDC referenciado debe coincidir con el CDC del evento de nominación de FE (cuando aplica) |
| H018a | dRucFus (H018) | NT-023: Campo para indicar RUC de empresa fusionada/absorbida |

---

## Reglas de Eventos

### Cancelación (GEC)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| GEC001a | — | Solo puede cancelarse un DE aprobado (estado=Aprobado) |
| GEC002a | — | El DE debe estar dentro del plazo: 48h para FE/AFE/NCE/NDE, 168h para NRE |
| GEC002b | — | NT-025: Se elimina la restricción que impedía cancelar si el receptor ya confirmó conformidad |
| GEC003a | — | Solo el emisor puede solicitar la cancelación |

### Inutilización (GEI)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| GEI001a | — | Solo puede inutilizarse un DE no enviado al SIFEN (CDC generado pero no transmitido) |
| GEI002a | — | Plazo: 15 días calendario desde la generación del CDC |
| GEI003a | — | El rango de numeración debe ser continuo y no puede contener números ya aprobados |

### Receptor (GEN, GCO, GDI, GED)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| GEN003a | — | NT-019: Modificación de validación de notificación de recepción |
| GED003a | — | NT-019: Modificación de validación de desconocimiento del receptor |
| Receptor001 | — | Los eventos del receptor (conformidad, disconformidad, desconocimiento, notificación) tienen un plazo de 45 días desde la emisión del DE |
| Receptor002 | — | El receptor solo puede emitir un evento por tipo (no puede enviar conformidad si ya envió disconformidad) |

### Nominación de FE (GENFE, NT-014)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| GENFE001 | — | La nominación de FE permite asociar un comprador después de emitida la FE |
| GENFE002 | — | Solo aplica a FE (C002=1) con receptor innominado (D210="0") |
| GENFE003 | — | NT-015: Las NCE/NDE emitidas contra una FE nominada deben referenciar el CDC correcto |

### Actualización de Transporte (GET, NT-010)

| Código | Campo(s) | Regla |
|--------|----------|-------|
| GET003a | — | Tipo de actualización válido: 1=local entrega, 2=chofer, 3=transportista, 4=vehículo |
| GET003b | — | Solo aplica a NRE (C002=7) |

---

## Reglas de Validación de Firma Digital

| Regla | Descripción |
|-------|-------------|
| FIRMA-001 | El certificado digital del emisor debe estar vigente (no expirado) al momento de la firma |
| FIRMA-002 | El certificado debe haber sido emitido por una CA autorizada por la SET/DNIT |
| FIRMA-003 | El método de canonicalización debe ser Exclusive XML Canonicalization (C14N) |
| FIRMA-004 | Algoritmo mínimo: RSA-SHA256. NT-016 habilita además RSA-SHA384 y RSA-SHA512 |
| FIRMA-005 | NT-016: La clave RSA debe ser de 2048 a 4096 bits |
| FIRMA-006 | NT-016: Se elimina XPath como método de transformación |
| FIRMA-007 | NT-016: Se habilitan métodos de canonicalización adicionales (Inclusive C14N with/without comments, Exclusive with/without comments) |

---

## Reglas de Conexión y Transmisión

| Regla | Descripción |
|-------|-------------|
| TRANS-001 | Protocolo: TLS 1.2 con autenticación mutua |
| TRANS-002 | Certificado de transmisión (persona jurídica o física habilitada por la SET) requerido |
| TRANS-003 | Para lotes: máximo 50 DE por lote, mismo tipo de documento (C002) |
| TRANS-004 | Los lotes se comprimen en ZIP y se codifican en Base64 antes de enviar |
| TRANS-005 | Sincronización horaria: diferencia máxima de ±5 minutos con servidores NTP aravo1.set.gov.py y aravo2.set.gov.py |

---

## Tabla de Notas Técnicas que Modifican Validaciones

| NT | Validación(es) Modificadas |
|----|---------------------------|
| NT-001 | EA004a, EA009a, F009a, F011a, F012a, F014a, F033a, F034a, F035a |
| NT-002 | D208, D210 (innominado) |
| NT-003 | D219a, D223a (dept/ciudad receptor) |
| NT-004 | Elimina D101a |
| NT-005 | D204a (longitud), E965 nota |
| NT-006 | Agrega D011a |
| NT-007 | B006a (exportación) |
| NT-008 | EA797, F023a (AFE) |
| NT-009 | E701a, E708a (longitud) |
| NT-010 | Elimina el valor 2 de A005 (dSisFact, el campo sigue obligatorio), modifica E505, E980, E992, E993 |
| NT-011 | Agrega WS siConsArchivoRUC |
| NT-012 | D015a (AFE en PYG) |
| NT-013 | E735a, E737a, F002a, F004a, F005a |
| NT-014 | Evento GENFE (nominación FE) |
| NT-015 | H004b (CDC nominación) |
| NT-016 | FIRMA-004 a FIRMA-007 |
| NT-017 | D222a, D224a (mensajes) |
| NT-018 | D031a, D032a (obligaciones) |
| NT-019 | GEN003a, GED003a |
| NT-020 | D202a (OEE → B2G), agrega E827 |
| NT-021 | D208c (límite 35M PYG innominado) |
| NT-022 | D031a (no duplicar obligaciones) |
| NT-023 | D208b, E711a, E791, H018a |
| NT-024 | D208d (límite 7M PYG desde 01/01/2025) |
| NT-025 | GEC002b (cancelación post-conformidad) |
| NT-026 | E704, E705, E020 opcionales B2G |
| NT-027 | Solo formato del evento de nominación FE: GENFE010/GENFE011 (Tarjeta Diplomática pasa de código 5 a 6). No afecta la generación de DE |
