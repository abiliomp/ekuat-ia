> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 — Campos E601 (iCondOpe), E606 (iTiPago), E641 (iCondCred) y grupos E7, E7.1, E7.2
> **Nota:** Contenido tachado (~~así~~) indica especificaciones eliminadas en v150. [MODIFICADO] indica cambios. [NUEVO] indica adiciones en v150.

# Condición de Operación y Formas de Pago

## Campo E601 – iCondOpe (Condición de la operación)

[MODIFICADO] Obligatorio si C002 = 1 (Factura Electrónica) o C002 = 4 (Autofactura Electrónica). No se informa para otros tipos de documento.

El campo `E602` (`dDCondOpe`) contiene la descripción de la condición; longitud 7 caracteres, obligatorio.

| Código | Descripción | Texto del campo E602 | Notas |
|--------|-------------|----------------------|-------|
| 1 | Contado | `"Contado"` | [NUEVO] Autofactura siempre contado (C002=4 → E601=1) |
| 2 | Crédito | `"Crédito"` | |

---

## Campo E606 – iTiPago (Tipo de pago)

Pertenece al grupo E7.1 ([MODIFICADO] Campos que describen la forma de pago al contado o del monto de la entrega inicial, E605–E619).

**Aplicabilidad:** Obligatorio cuando E601=1 (contado) o cuando E601=2 con monto de entrega inicial (E645).

El campo `E607` (`dDesTiPag`) contiene la descripción del tipo de pago (4–30 caracteres). [MODIFICADO] Si E606=99, es obligatorio informar el tipo de pago en texto libre.

| Código | Descripción | Estado en v150 |
|--------|-------------|----------------|
| 1 | Efectivo | Vigente |
| 2 | Cheque | Vigente |
| 3 | Tarjeta de crédito | Vigente |
| 4 | Tarjeta de débito | Vigente |
| 5 | Transferencia | Vigente |
| 6 | Giro | Vigente |
| 7 | Billetera electrónica | Vigente |
| 8 | Tarjeta empresarial | Vigente |
| 9 | Vale | Vigente |
| 10 | Retención | [MODIFICADO] |
| 11 | Pago por anticipo | [MODIFICADO] |
| 12 | Valor fiscal | Vigente |
| 13 | Valor comercial | Vigente |
| 14 | Compensación | Vigente |
| 15 | Permuta | Vigente |
| 16 | Pago bancario | [NUEVO] Informar solo si E011=5 (Operación bancaria) |
| 17 | Pago Móvil | [NUEVO] |
| 18 | Donación | [NUEVO] |
| 19 | Promoción | [NUEVO] |
| 20 | Consumo Interno | [NUEVO] |
| 21 | Pago Electrónico | [NUEVO] |
| 99 | Otro | [NUEVO] Obligatorio informar texto en E607 |

**Regla especial:** Si E606=16 (Pago bancario), el indicador de presencia (E011) debe ser igual a 5 (Operación bancaria). Esta validación aplica solo a Factura Electrónica.

---

## Campo E609 – cMoneTiPag (Moneda por tipo de pago)

Código ISO 4217 de la moneda para cada forma de pago. Obligatorio si E609 ≠ PYG, informar el tipo de cambio E611.

---

## Campo E641 – iCondCred (Condición de la operación a crédito)

Pertenece al grupo E7.2 (Campos que describen la operación a crédito, E640–E649). Obligatorio si E601=2 (crédito).

El campo `E642` (`dDCondCred`) contiene la descripción de la condición de crédito.

| Código | Descripción | Campos obligatorios |
|--------|-------------|---------------------|
| 1 | Plazo | E643 (dPlazo — plazo del crédito) |
| 2 | Cuota | E644 (dCuotas — cantidad de cuotas) |

---

## Cuotas (E650–E659)

Cuando E641=2, el grupo E650 describe cada cuota individualmente.

[NUEVO] El campo `cMoneCuo` (E653) contiene el código de moneda de las cuotas (ISO 4217).
[NUEVO] El campo `dDMoneCuo` (E654) contiene la descripción de la moneda de las cuotas.

---

## Resumen de grupos de condición de operación

| Grupo | Campos | Descripción |
|-------|--------|-------------|
| E600 | E601–E602 | Condición de la operación (contado/crédito) |
| E605 | E605–E619 | [MODIFICADO] Forma de pago al contado o monto de entrega inicial |
| E620 | E620–E629 | [MODIFICADO] Pago con tarjeta de crédito/débito |
| E630 | E630–E639 | Pago con cheque |
| E640 | E640–E649 | Operación a crédito |
| E650 | E650–E659 | Cuotas |
