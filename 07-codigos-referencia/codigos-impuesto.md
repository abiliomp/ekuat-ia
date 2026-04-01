# Códigos de Impuesto (D013 / iTImp, E731 / iAfecIVA)

Campos de impuesto en el DE:
- `iTImp` (D013): tipo de impuesto afectado en la operación
- `iAfecIVA` (E731): forma de afectación tributaria del IVA por ítem
- `dTasaIVA` (E734): tasa del IVA aplicada al ítem

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 (campos D013, E731, E734) y sección 15 (TABLA 6, TABLA 7, TABLA 8)

---

## Tipo de Impuesto Afectado (D013 / iTImp)

Indica qué impuesto afecta a la operación documentada. Obligatorio para FE (C002=1) y AFE (C002=4).

| Código | Descripción (dDesTImp) | Observación |
|--------|------------------------|-------------|
| 1 | IVA | Impuesto al Valor Agregado |
| 2 | ISC | Impuesto Selectivo al Consumo |
| 3 | Renta | Impuesto a la Renta |
| 4 | Ninguno | Sin afectación de impuesto |
| 5 | IVA – Renta | Afectado simultáneamente por IVA y Renta |

**Regla:** Si D013 = 2 (ISC) y C002 = 4 o 7: no se informa el grupo E730 (campos de IVA por ítem).

---

## Forma de Afectación Tributaria del IVA (E731 / iAfecIVA)

Indica cómo afecta el IVA a cada ítem de la operación. Se informa en el grupo E730, por cada ítem.

| Código | Descripción (dDesAfecIVA) | Tasa aplicable |
|--------|--------------------------|----------------|
| 1 | Gravado IVA | 5% o 10% |
| 2 | Exonerado (Art. 83 - Ley 125/91) | 0% |
| 3 | Exento | 0% |
| 4 | Gravado parcial (Grav-Exento) | Porción gravada al 5% o 10% |

**Nota sobre TABLA 6 - Códigos de afectación:**

| Código | Descripción |
|--------|-------------|
| 1 | Gravado IVA |
| 2 | Exonerado (Art. 83 - 125) |
| 3 | Exento |
| 4 | Gravado parcial |

---

## Tasa del IVA (E734 / dTasaIVA)

| Valor | Aplica cuando |
|-------|--------------|
| 0 | E731 = 2 (Exonerado) o E731 = 3 (Exento) |
| 5 | E731 = 1 (Gravado) o E731 = 4 (Gravado parcial) — tasa reducida |
| 10 | E731 = 1 (Gravado) o E731 = 4 (Gravado parcial) — tasa general |

**Indicador de IVA (iAfecIVA):** La proporción gravada se informa en el campo E733 (dPropIVA) como porcentaje entero (ejemplo: 100, 50, 30, 0).

---

## Categorías del ISC — TABLA 7

Cuando D013 = 2 (ISC), se aplica una categoría de ISC por ítem.

| Código | Descripción |
|--------|-------------|
| 1 | Sección I - Cigarrillos, Tabacos, Esencias y Otros derivados del Tabaco |
| 2 | Sección II - Bebidas con y sin alcohol |
| 3 | Sección III - Alcoholes y Derivados del alcohol |
| 4 | Sección IV - Combustibles |
| 5 | Sección V - Artículos considerados de lujo |

---

## Tasas del ISC — TABLA 8

Tasas según Decretos N° 4344/04, N° 5158/10, N° 4693/15, N° 4694/15.

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

## Campos de liquidación de IVA en totales (grupo F)

| Campo | ID | Descripción |
|-------|----|-------------|
| Subtotal exentas | F002 | Total ítems exentos de IVA |
| Subtotal al 5% | F004 | Total ítems gravados al 5% |
| Subtotal al 10% | F005 | Total ítems gravados al 10% |
| IVA al 5% | F014 | Monto de IVA calculado al 5% |
| IVA al 10% | F015 | Monto de IVA calculado al 10% |
| Total IVA | F016 | Suma total de IVA de la operación |
