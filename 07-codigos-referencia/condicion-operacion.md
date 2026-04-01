# Condición de Operación y Formas de Pago

Campos que describen cómo se realiza el pago de la operación documentada.

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 (campos E601, E641, E606, grupos E7, E7.1, E7.2)

---

## Condición de la Operación (E601 / iCondOpe)

Indica si la operación es al contado o a crédito. Obligatorio para FE (C002=1) y AFE (C002=4).

| Código | Descripción (dDCondOpe) |
|--------|------------------------|
| 1 | Contado |
| 2 | Crédito |

**Regla:** Si E601=1 (Contado), es obligatorio informar el grupo E605 (forma de pago).

---

## Condición de la Operación a Crédito (E641 / iCondCred)

Se informa solo cuando E601=2 (Crédito). Describe la modalidad del crédito.

| Código | Descripción (dDCondCred) |
|--------|--------------------------|
| 1 | Plazo |
| 2 | Cuota |

- Si E641=1 (Plazo): informar el campo E643 (dPlazoCre), ej: "30 días", "12 meses".
- Si E641=2 (Cuota): informar el campo E644 (dCuotas) con la cantidad de cuotas, ej: 12, 24, 36.

---

## Tipos de Pago (E606 / iTiPago)

Se informan dentro del grupo E605 (forma de pago al contado o entrega inicial). Puede haber múltiples tipos de pago (hasta 999 ocurrencias).

| Código | Descripción (dDesTiPag) | Observación |
|--------|------------------------|-------------|
| 1 | Efectivo | |
| 2 | Cheque | Activa grupo E630 (datos del cheque) |
| 3 | Tarjeta de crédito | Activa grupo E620 (datos de tarjeta) |
| 4 | Tarjeta de débito | Activa grupo E620 (datos de tarjeta) |
| 5 | Transferencia | |
| 6 | Giro | |
| 7 | Billetera electrónica | |
| 8 | Tarjeta empresarial | |
| 9 | Vale | |
| 10 | Retención | |
| 11 | Pago por anticipo | |
| 12 | Valor fiscal | |
| 13 | Valor comercial | |
| 14 | Compensación | |
| 15 | Permuta | |
| 16 | Pago bancario | Solo informar si E011=5 (Operación bancaria) |
| 17 | Pago Móvil | |
| 18 | Donación | |
| 19 | Promoción | |
| 20 | Consumo Interno | |
| 21 | Pago Electrónico | |
| 99 | Otro | Informar descripción en dDesTiPag |

---

## Datos de Pago con Tarjeta (E621 / iDenTarj)

Se informa cuando E606 = 3 (Tarjeta de crédito) o E606 = 4 (Tarjeta de débito). Grupo E620.

| Código | Descripción (dDesDenTarj) |
|--------|--------------------------|
| 1 | Visa |
| 2 | Mastercard |
| 3 | American Express |
| 4 | Maestro |
| 5 | Panal |
| 6 | Cabal |
| 99 | Otro |

**Campos adicionales del grupo E620:**
- E623: Razón social de la procesadora
- E624: RUC de la procesadora
- E626: Forma de procesamiento (1=POS, 2=Pago Electrónico, 9=Otro)
- E627: Código de autorización de la operación
- E628: Nombre del titular de la tarjeta
- E629: Cuatro últimos dígitos de la tarjeta

---

## Datos de Pago con Cheque (Grupo E630)

Se informa cuando E606 = 2 (Cheque).

| Campo | ID | Descripción |
|-------|----|-------------|
| Número de cheque | E631 | 8 dígitos, completar con ceros a la izquierda |
| Banco emisor | E632 | Nombre del banco |

---

## Cuotas (Grupo E650)

Se informa cuando E641=2 (Cuota). Hasta 999 ocurrencias.

| Campo | ID | Descripción |
|-------|----|-------------|
| Monto de cada cuota | E651 | Monto de la cuota |
| Fecha de vencimiento | E652 | Formato AAAA-MM-DD |
| Moneda de las cuotas | E653 | Código ISO 4217 |
| Descripción de la moneda | E654 | Referente a E653 |

---

## Resumen de grupos E7 (condición de operación)

| Grupo | Rango | Descripción | Activo cuando |
|-------|-------|-------------|---------------|
| E7 | E600-E699 | Condición de la operación | C002=1 o 4 |
| E7.1 | E605-E619 | Forma de pago al contado o entrega inicial | E601=1 o existe E645 |
| E7.1.1 | E620-E629 | Pago con tarjeta de crédito/débito | E606=3 o 4 |
| E7.1.2 | E630-E639 | Pago con cheque | E606=2 |
| E7.2 | E640-E649 | Operación a crédito | E601=2 |
| E7.2.1 | E650-E659 | Cuotas del crédito | E641=2 |
