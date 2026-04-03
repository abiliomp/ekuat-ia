> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 — Campos D201–D224 (Grupo D3)
> **Nota:** Contenido tachado (~~así~~) indica especificaciones eliminadas en v150. [MODIFICADO] indica cambios. [NUEVO] indica adiciones en v150.

# Tipos de Receptor (D200–D299)

El grupo D3 identifica al receptor del Documento Electrónico. Los campos D201 a D224 conforman la información del receptor.

---

## Campo D201 – iNatRec (Naturaleza del receptor)

| Código | Descripción | Notas |
|--------|-------------|-------|
| 1 | Contribuyente | D205, D206 son obligatorios |
| 2 | No contribuyente | D208, D210 son obligatorios (salvo D202=4) |

**Regla nueva:** [NUEVO] Si C002=4 (Autofactura), la naturaleza del receptor debe ser Contribuyente (D201=1).

---

## Campo D202 – iTiOpe (Tipo de operación)

| Código | Descripción | Estado en v150 |
|--------|-------------|----------------|
| 1 | B2B (Business to Business) | Vigente |
| 2 | B2C (Business to Consumer) | Vigente |
| 3 | B2G (Business to Government) | [NUEVO] |
| 4 | B2F (Business to Foreign — servicios al exterior) | [NUEVO] Solo para servicios a empresas o personas físicas del exterior |

**Reglas de compatibilidad:**

| Condición | Regla |
|-----------|-------|
| D201=2 (No contribuyente) y C002 ≠ 4 | [MODIFICADO] El tipo de operación debe ser B2C (D202=2) |
| [NUEVO] D202=4 (B2F) | La naturaleza del receptor debe ser No Contribuyente (D201=2) |
| [NUEVO] C002=4 (Autofactura) | El tipo de operación debe ser B2C (D202=2) |
| D202=3 (B2G) | El grupo de Compras Públicas (E020) es obligatorio |
| [NUEVO] D202=4 (B2F) | D203 ≠ PRY (país del receptor debe ser diferente a Paraguay) |
| D202 ≠ 4 | D203 = PRY (país del receptor debe ser Paraguay) |

---

## Campo D203 – cPaisRec (Código de país del receptor)

Código ISO 3166-1 alpha-3. Obligatorio. Ver archivo [codigos-pais.md](codigos-pais.md).

- El campo `D204` (`dDesPaisRec`) contiene la descripción del país (4–30 caracteres).

---

## Campo D205 – iTiContRec (Tipo de contribuyente receptor)

Obligatorio si D201=1. No informar si D201=2.

| Código | Descripción |
|--------|-------------|
| 1 | Persona Física |
| 2 | Persona Jurídica |

---

## Campo D206 – dRucRec (RUC del receptor)

Obligatorio si D201=1 (contribuyente). No informar si D201=2.
[MODIFICADO] Longitud ajustada a 3–8 caracteres.

- `D207` (`dDVRec`): Dígito verificador del RUC del receptor. [NUEVO] Obligatorio si existe D206. Calculado mediante algoritmo módulo 11.
- **Validaciones nuevas:**
  - [NUEVO] Si C002=4 (Autofactura), el RUC del receptor debe ser igual al RUC del emisor (D206 = D101).
  - Si D201=2 (no contribuyente), D206 no debe informarse.
  - Si D205=2 (persona jurídica), el RUC debe tener estado distinto a CANCELADO, CANCELADO DEFINITIVO o SUSPENSIÓN TEMPORAL.
  - Si D202=1 o 3 (B2B o B2G), el RUC del receptor debe tener estado activo.

---

## Campo D208 – iTipIDRec (Tipo de documento de identidad del receptor)

[NUEVO] Obligatorio si D201=2 y D202≠4. No informar si D201=1 o D202=4.

El campo `D209a` (`dDesDocIDRec`) [MODIFICADO] contiene la descripción del tipo de documento (9–41 caracteres).

| Código | Descripción | Estado en v150 |
|--------|-------------|----------------|
| 1 | Cédula paraguaya | Vigente |
| 2 | Pasaporte | Vigente |
| 3 | Cédula extranjera | Vigente |
| 4 | Carnet de residencia | Vigente |
| 5 | Innominado | [NUEVO] Solo permitido si D202=2 (B2C) |
| 6 | Tarjeta Diplomática de exoneración fiscal | [NUEVO] |
| 9 | Otro | [NUEVO] Informar descripción en D209a |

**Restricciones del tipo Innominado (D208=5):**
- [NUEVO] No puede ser innominado cuando D202 ≠ 2 (B2C).
- [NUEVO] No puede ser innominado cuando F023 ≥ 60.000.000 Gs o F014 ≥ 60.000.000 Gs, salvo que D011=13 (Muestras médicas).

~~Validación 60 (D209 — descripción obligatoria si existe D208)~~ fue **eliminada** en v150. La validación 64 (D209a — descripción no coincidente) sigue vigente.

---

## Campo D210 – dNumIDRec (Número de documento de identidad del receptor)

[NUEVO] Obligatorio si D201=2 y D202≠4. No informar si D201=1 o D202=4.

- En caso de DE innominado, el campo queda en blanco o con valor indicativo.
- [NUEVO] Validación D210a: Si D201=1 o D202=4, el número de documento **no debe informarse**.

---

## Campos nuevos de dirección del receptor (D213–D224)

[NUEVO] El campo `D213` (dirección del receptor, 1–255 caracteres) es **obligatorio cuando C002=7** (Nota de Remisión) **o cuando D202=4** (B2F).

| Campo | ID | Descripción | Estado |
|-------|----|-------------|--------|
| Dirección | D213 | Dirección del receptor | [NUEVO] Obligatorio para C002=7 o D202=4 |
| Número de casa | D218 | Número de casa del receptor | [NUEVO] Obligatorio si existe D213 |
| Departamento | D219 | Código del departamento del receptor | [NUEVO] Obligatorio si D213 y D202≠4 |
| Desc. departamento | D220 | Descripción del departamento | [NUEVO] Debe corresponder a D219 |
| Distrito | D221 | Código del distrito del receptor | [NUEVO] |
| Desc. distrito | D222 | Descripción del distrito | [NUEVO] Debe corresponder a D221 |
| Ciudad | D223 | Código de la ciudad del receptor | [NUEVO] Obligatorio si D213 y D202≠4 |
| Desc. ciudad | D224 | Descripción de la ciudad | [NUEVO] Debe corresponder a D223 |

**Validación D223a:** [NUEVO] Debe haber relación entre el departamento (D219), el distrito (D221) y la ciudad (D223).

---

## Campos del responsable del DE (D2.2) — [NUEVO]

| Campo | ID | Descripción |
|-------|----|-------------|
| Tipo de documento de identidad del responsable | D141 (`iTipIDRespDE`) | [NUEVO] |
