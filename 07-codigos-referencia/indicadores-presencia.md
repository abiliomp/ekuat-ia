> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 — Campo E011 (iIndPres)
> **Nota:** Contenido tachado (~~así~~) indica especificaciones eliminadas en v150. [MODIFICADO] indica cambios. [NUEVO] indica adiciones en v150.

# Indicador de Presencia (E011 – iIndPres)

El campo `iIndPres` (E011) indica la modalidad de la operación según el tipo de contacto entre el emisor y el receptor. Pertenece al grupo E1 (Campos que componen la Factura Electrónica FE).

**Aplicabilidad:** Obligatorio cuando C002=1 (Factura Electrónica). No aplica para otros tipos de documento electrónico.

El campo `E012` (`dDesIndPres`) contiene la descripción del indicador de presencia (10–30 caracteres). Debe corresponder exactamente al código informado en E011.

## Tabla de códigos (iIndPres)

| Código | Descripción | Estado en v150 | Tipos de documento aplicables |
|--------|-------------|----------------|-------------------------------|
| 1 | Operación presencial | Vigente | FE (C002=1) |
| 2 | Operación electrónica | Vigente | FE (C002=1) |
| 3 | Operación telemarketing | Vigente | FE (C002=1) |
| 4 | Venta a domicilio | Vigente | FE (C002=1) |
| 5 | Operación bancaria | [NUEVO] | FE (C002=1) |
| 6 | Operación cíclica | [NUEVO] | FE (C002=1) |
| 9 | Otro | Vigente | FE (C002=1) — obligatorio informar descripción en E012 |

## Reglas relacionadas con E011

| Condición | Regla |
|-----------|-------|
| E011 = 9 (Otro) | Obligatorio informar la descripción en E012 |
| [NUEVO] E606 = 16 (Pago bancario) | El indicador de presencia debe ser E011=5 (Operación bancaria). Aplica solo para FE. |
| E011 = 5 (Operación bancaria) | Permite el tipo de pago E606=16 (Pago bancario) |

## Descripción de los valores

- **1 — Operación presencial:** El receptor está físicamente presente en el momento de la transacción.
- **2 — Operación electrónica:** La transacción se realiza por medios electrónicos (e-commerce, plataformas digitales).
- **3 — Operación telemarketing:** La transacción se gestiona telefónicamente.
- **4 — Venta a domicilio:** El bien o servicio se entrega en el domicilio del receptor.
- **5 — Operación bancaria:** [NUEVO] La transacción se gestiona a través de un canal bancario. Requiere E606=16.
- **6 — Operación cíclica:** [NUEVO] Operaciones recurrentes o periódicas (ejemplo: suscripciones, servicios continuos).
- **9 — Otro:** Cualquier otra modalidad no clasificada. Requiere descripción libre en E012.
