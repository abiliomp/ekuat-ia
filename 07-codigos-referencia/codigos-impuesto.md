> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 (campos D013, E731) y sección 15 (TABLA 6, TABLA 7, TABLA 8)
> **Nota:** Contenido tachado (~~así~~) indica especificaciones eliminadas en v150. [MODIFICADO] indica cambios. [NUEVO] indica adiciones en v150.

# Códigos de Impuesto

## Campo D013 – iTImp (Tipo de impuesto afectado)

El campo `iTImp` (D013) es [MODIFICADO] "Tipo de impuesto afectado", obligatorio para la Factura Electrónica y la Autofactura Electrónica (cuando aplique). Pertenece al grupo D1.

El campo `D014` (`dDesTImp`) contiene la descripción del tipo de impuesto; su valor debe corresponder al código de D013. [MODIFICADO] Su longitud fue ajustada a 3–11 caracteres.

| Código | Texto exacto del campo D014 (XSD `tdDesTImp`) | Estado en v150 |
|--------|-----------------------------------------------|----------------|
| 1 | `IVA` | Vigente |
| 2 | `ISC` | [NUEVO] |
| 3 | `Renta` | [NUEVO] |
| 4 | `Ninguno` | [NUEVO] |
| 5 | `IVA - Renta` | [NUEVO] |

> **⚠️ Literal exacto (XSD de producción):** el valor del código 5 es `IVA - Renta` con **guion simple ASCII rodeado de espacios** (no guion largo "–"). `tdDesTImp` es una enumeración cerrada en `DE_Types_v150.xsd`: cualquier diferencia de carácter produce rechazo.
>
> **Nota del XSD:** el tipo numérico `tiTImp` (D013) acepta 1–5, pero el XSD de producción incluye el comentario *"Cambio temporal, solo se aceptará IVA"* — en la práctica usar D013=1 salvo confirmación oficial en contrario.

> **Nota importante:** La validación ~~28~~ (D013 obligatorio para C002=1 o 4) fue **eliminada** en v150. La descripción sigue siendo validada mediante la regla 26 (D014).

---

## Campo E731 – iAfecIVA (Forma de afectación tributaria del IVA por ítem)

El campo `iAfecIVA` (E731) pertenece al grupo E8.2 (Campos que describen el IVA de la operación por ítem, E730-E739).

**Aplicabilidad:** [MODIFICADO] Obligatorio si D013=1, 3, 4 o 5 y C002 ≠ 4 o 7. No informar si D013=2 y C002=4 o 7.

El campo `E732` (`dDesAfecIVA`) contiene la descripción de la afectación; debe corresponder al código E731.

### TABLA 6 – Códigos de afectación tributaria del IVA

| Código | Texto exacto del campo E732 (XSD `tdDesAfecIVA`) | Tasa válida (E734) |
|--------|--------------------------------------------------|-------------------|
| 1 | `Gravado IVA` | 5% o 10% |
| 2 | `Exonerado (Art. 100 - Ley 6380/2019)` | 0% |
| 3 | `Exento` | 0% |
| 4 | `Gravado parcial (Grav- Exento)` | 5% o 10% |

> **⚠️ Literales exactos verificados contra el XSD de producción** (`DE_Types_v150.xsd` en `ekuatia.set.gov.py`, junio 2026). `tdDesAfecIVA` es una **enumeración cerrada**: el valor debe coincidir carácter por carácter o SIFEN rechaza con *"El valor ... del elemento: dDesAfecIVA es invalido"*. En particular:
> - Código 2: el Manual Técnico v150 original decía "Exonerado (Art. 83- Ley 125/91)", pero la **NT-010 (Tabla 6)** lo cambió a `Exonerado (Art. 100 - Ley 6380/2019)` (la Ley 6380/2019, Art. 100, reemplazó al Art. 83 de la Ley 125/91 como base legal de las exoneraciones). El XSD de producción solo acepta el literal nuevo.
> - Código 4: nótese el **espacio después del guion** en `(Grav- Exento)` — así lo exige el XSD, aunque parezca un error tipográfico.

**Reglas de cálculo de base gravada (E735):**
- Si E731 = 1 o 4: `[EA008 * (E733/100)] / 1,10` si tasa es 10%; `[EA008 * (E733/100)] / 1,05` si tasa es 5%
- Si E731 = 2 o 3: E735 = 0; E736 = 0

---

## TABLA 7 – Categorías del ISC

El campo `iTipISC` (código del grupo E8.3) — actualmente futuro — utilizará estas categorías:

| Código | Descripción | Texto exacto (XSD `tdDesCatISC`) |
|--------|-------------|----------------------------------|
| 1 | Sección I — Cigarrillos, Tabacos, Esencias y Otros derivados del Tabaco | `SECCION I-(Cigarrillos,Tabacos,Esencias y Otros derivados del Tabaco)` |
| 2 | Sección II — Bebidas con y sin alcohol | `SECCION II - (Bebidas con y sin alcohol)` |
| 3 | Sección III — Alcoholes y Derivados del alcohol | `SECCION III - (Alcoholes y Derivados del alcohol)` |
| 4 | Sección IV — Combustibles | `SECCION IV - (Combustibles)` |
| 5 | Sección V — Artículos considerados de lujo | `SECCION V - (Artículos considerados de lujo)` |

> **⚠️ Literales exactos del XSD de producción:** nótese que el código 1 **no lleva espacios** alrededor del guion ni después de las comas (`SECCION I-(Cigarrillos,Tabacos,...)`), mientras que los códigos 2–5 sí llevan espacios alrededor del guion. Son inconsistencias tipográficas del propio XSD oficial que deben reproducirse tal cual.

---

## TABLA 8 – Tasas del ISC

Tasas del ISC según Decretos N° 4344/04, N° 5158/10, N° 4693/15, N° 4694/15:

| Código | Porcentaje |
|--------|-----------|
| 1 | 1% |
| 2 | 5% |
| 3 | 9% |
| 4 | 10% |
| 5 | 11% |
| 6 | 13% |
| 7 | 16% |
| 8 | 18% |
| 9 | 20% |
| 10 | 24% |
| 11 | 34% |
| 12 | 38% |

---

## TABLA 9 – Tipos de Vehículos

~~TABLA 9 – TIPOS DE VEHÍCULOS~~

~~Se incluirá un link de descarga con la codificación a fin de agilizar su implementación.~~

> Esta tabla fue **eliminada** del Manual Técnico en v150.

---

## Resumen de campos de IVA por ítem (E730-E739)

| ID | Campo | Descripción | Longitud | Observaciones |
|----|-------|-------------|----------|---------------|
| E730 | gCamIVA | Grupo IVA por ítem | G | [MODIFICADO] Obligatorio según D013 y C002 |
| E731 | iAfecIVA | Forma de afectación tributaria | N 1 | Ver TABLA 6 |
| E732 | dDesAfecIVA | Descripción de afectación | A | [MODIFICADO] Referente a E731 |
| E733 | dPropIVA | Proporción gravada del IVA (%) | N [MODIFICADO] 1-3p(0-8) | Ejemplo: 100, 50, 30, 0 |
| E734 | dTasaIVA | Tasa del IVA (% entero) | N 1-2 | 0 si E731=2 o 3; 5 o 10 si E731=1 o 4 |
| E735 | dBasGravIVA | Base gravada del IVA | N [MODIFICADO] 1-15p(0-8) | |
| E736 | dLiqIVAItem | Liquidación del IVA por ítem | N [MODIFICADO] 1-15p(0-8) | E735 * (E734/100) |
