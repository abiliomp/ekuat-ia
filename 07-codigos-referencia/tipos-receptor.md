# Tipos de Receptor (D200-D299)

Campos del grupo D3 que identifican al receptor del Documento Electrónico.

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 (campos D200-D299)

---

## Naturaleza del Receptor (D201 / iNatRec)

| Código | Descripción | Observación |
|--------|-------------|-------------|
| 1 | Contribuyente | Requiere RUC (D206) y tipo de contribuyente (D205) |
| 2 | No contribuyente | Requiere tipo y número de documento de identidad (D208, D210) |

---

## Tipo de Operación (D202 / iTiOpe)

Clasifica la operación según los actores involucrados.

| Código | Acrónimo | Descripción |
|--------|----------|-------------|
| 1 | B2B | Business to Business — operación entre empresas |
| 2 | B2C | Business to Consumer — operación entre empresa y consumidor final |
| 3 | B2G | Business to Government — operación entre empresa y entidad gubernamental |
| 4 | B2F | Business to Foreign — servicios prestados a empresa o persona física del exterior |

**Reglas de compatibilidad:**
- Si D201=2 (No contribuyente) y C002 ≠ 4 (no es AFE): el tipo de operación debe ser B2C (D202=2).
- Si D202=4 (B2F): la naturaleza del receptor debe ser No contribuyente (D201=2).
- Si C002=4 (AFE): el tipo de operación debe ser B2C (D202=2).
- Si D202=3 (B2G): es obligatorio informar el grupo E020 (informaciones de compras públicas).

---

## Tipo de Contribuyente Receptor (D205 / iTiContRec)

Obligatorio si D201=1 (Contribuyente). No informar si D201=2.

| Código | Descripción |
|--------|-------------|
| 1 | Persona Física |
| 2 | Persona Jurídica |

---

## Tipo de Documento de Identidad del Receptor (D208 / iTipIDRec)

Obligatorio si D201=2 (No contribuyente) y D202 ≠ 4 (no es B2F). No informar si D201=1 o D202=4.

| Código | Descripción (dDTipIDRec) |
|--------|--------------------------|
| 1 | Cédula paraguaya |
| 2 | Pasaporte |
| 3 | Cédula extranjera |
| 4 | Carnet de residencia |
| 5 | Innominado |
| 6 | Tarjeta Diplomática de exoneración fiscal |
| 9 | Otro (informar descripción en D209) |

**Restricciones del tipo Innominado (D208=5):**
- Solo permitido en operaciones B2C (D202=2).
- Si el tipo de transacción es diferente a Muestras médicas (D011 ≠ 13), el total de la operación debe ser menor a Gs. 60.000.000 para poder usar el tipo Innominado.
- Cuando es innominado, el campo D210 (número de documento) se completa con "0" y D211 (nombre) con "Sin Nombre".

---

## Campos de identificación del receptor

| Campo | ID | Descripción | Obligatorio cuando |
|-------|----|-------------|-------------------|
| Naturaleza del receptor | D201 | Contribuyente o No contribuyente | Siempre |
| Tipo de operación | D202 | B2B, B2C, B2G, B2F | Siempre |
| País del receptor | D203 | Código ISO 3166-1 alpha-3 | Siempre |
| Descripción del país | D204 | Texto del país | Siempre |
| Tipo de contribuyente | D205 | Persona Física / Jurídica | D201=1 |
| RUC del receptor | D206 | RUC sin dígito verificador | D201=1 |
| DV del RUC | D207 | Dígito verificador del RUC | Existe D206 |
| Tipo de documento de identidad | D208 | Código del tipo de documento | D201=2 y D202≠4 |
| Descripción del tipo de documento | D209 | Texto del tipo de documento | Existe D208 |
| Número de documento de identidad | D210 | Número del documento | D201=2 y D202≠4 |
| Nombre o razón social | D211 | Nombre del receptor | Siempre |
| Nombre de fantasía | D212 | Nombre comercial | Opcional |
| Dirección | D213 | Dirección del receptor | C002=7 o D202=4 |
| Teléfono | D214 | Con prefijo de ciudad si D203=PRY | Opcional |
| Celular | D215 | Número de celular | Opcional |
| Correo electrónico | D216 | Email del receptor | Opcional |
| Código del cliente | D217 | Código interno del emisor | Opcional |

---

## Validaciones clave (sección 12.4)

| N° Val | ID | Mensaje | Código |
|--------|----|---------|--------|
| 45 | D201 | Naturaleza del Receptor inválida para el tipo documento | 1315 |
| 46 | D202 | El tipo de operación no compatible con la naturaleza del receptor | 1300 |
| 47 | D202a | El tipo de operación no compatible con el tipo documento electrónico | 1316 |
| 48 | D203 | Código de país del receptor inválido para el tipo de operación | 1320 |
| 52 | D206 | Es obligatorio informar el RUC del receptor contribuyente | 1304 |
| 57 | D206e | RUC del Receptor inválido para la Autofactura | 1317 |
| 59 | D208 | Es obligatorio informar el tipo de documento de identidad del receptor | 1310 |
| 61 | D208b | Tipo de documento innominado incorrecto para el tipo de operación | 1319 |
| 62 | D208c | Tipo de documento innominado incorrecto para el total de la operación | 1321 |
