# Indicador de Presencia (E011 / iIndPres)

Campo `iIndPres` (E011): indica la modalidad de la operación según el tipo de contacto entre emisor y receptor. Es un campo del grupo E1 (Factura Electrónica) y es obligatorio cuando C002=1 (FE).

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 (campo E011)

---

## Tabla de indicadores de presencia

| Código | Descripción (dDesIndPres) | Descripción detallada | Aplica a |
|--------|--------------------------|----------------------|----------|
| 1 | Operación presencial | El emisor y el receptor se encuentran físicamente en el mismo lugar al momento de la operación | FE |
| 2 | Operación electrónica | La transacción se realiza por medios electrónicos (comercio electrónico, tienda online) | FE |
| 3 | Operación telemarketing | La transacción se origina a través de contacto telefónico o telemático | FE |
| 4 | Venta a domicilio | El emisor entrega el bien o servicio en el domicilio del receptor | FE |
| 5 | Operación bancaria | La transacción se realiza a través de entidades bancarias o financieras. Si E011=5, se habilita el tipo de pago "Pago bancario" (E606=16) | FE |
| 6 | Operación cíclica | Operación recurrente o periódica entre las partes | FE |
| 9 | Otro | Cualquier otra modalidad no contemplada. Requiere descripción en el campo E012 | FE |

---

## Tipos de documento que utilizan iIndPres

El campo E011 pertenece al grupo E010 (campos específicos de la Factura Electrónica).

| Tipo DE | C002 | E011 requerido |
|---------|------|---------------|
| Factura Electrónica | 1 | Sí (obligatorio dentro del grupo E010) |
| Factura Electrónica de Exportación | 2 | No aplicable (otros grupos específicos) |
| Factura Electrónica de Importación | 3 | No aplicable |
| Autofactura Electrónica | 4 | No (usa grupo E300) |
| Nota de Crédito Electrónica | 5 | No (usa grupo E400) |
| Nota de Débito Electrónica | 6 | No (usa grupo E400) |
| Nota de Remisión Electrónica | 7 | No (usa grupo E500) |

---

## Campo fecha futura de traslado (E013)

Dentro del mismo grupo E010, el campo `dFecEmNR` (E013) permite indicar una fecha futura estimada para el traslado de mercadería y emisión de la NRE:
- Formato: AAAA-MM-DD
- Es opcional
- Aplica según la Resolución General 41/14

---

## Interacción con el tipo de pago

Cuando E011=5 (Operación bancaria), se habilita el código de tipo de pago E606=16 (Pago bancario). Este es el único caso donde dicho tipo de pago está disponible.

---

## Descripción textual (dDesIndPres)

La descripción en el campo E012 debe coincidir exactamente con el valor de E011:

| E011 | E012 (texto) |
|------|-------------|
| 1 | "Operación presencial" |
| 2 | "Operación electrónica" |
| 3 | "Operación telemarketing" |
| 4 | "Venta a domicilio" |
| 5 | "Operación bancaria" |
| 6 | "Operación cíclica" |
| 9 | Describir el tipo de operación |
