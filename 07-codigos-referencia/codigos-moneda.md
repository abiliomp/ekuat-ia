> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 — Campo D015 (cMoneOpe)
> **Nota:** Contenido tachado (~~así~~) indica especificaciones eliminadas en v150. [MODIFICADO] indica cambios. [NUEVO] indica adiciones en v150.

# Códigos de Moneda (D015 – cMoneOpe)

El campo `cMoneOpe` (D015) contiene el código de la moneda de la operación. Sigue el estándar internacional **ISO 4217** (tres letras mayúsculas). Es un campo alfanumérico de longitud 3, obligatorio.

**Regla:** Se requiere la misma moneda para todos los ítems del DE.

El campo `D016` (`dDesMoneOpe`) contiene la descripción de la moneda; su valor debe corresponder exactamente al código informado en D015.

## Reglas de tipo de cambio

| Condición | Regla |
|-----------|-------|
| D015 ≠ PYG | Obligatorio informar la condición del tipo de cambio (D017) |
| D015 = PYG | No se informa D017 ni D018 |
| D017 = 1 (Global) | Obligatorio informar D018 (tipo de cambio global) |
| [NUEVO] D017 = 2 (Por ítem) | No se informa D018 |
| [NUEVO] D015 = PYG | No se informa D018 |

## Monedas utilizadas en SIFEN (ISO 4217)

SIFEN acepta cualquier código de moneda válido conforme al estándar ISO 4217. A continuación se listan las monedas de mayor uso en Paraguay:

| Código ISO 4217 | Moneda | País / Región |
|----------------|--------|---------------|
| PYG | Guaraní paraguayo | Paraguay |
| USD | Dólar estadounidense | Estados Unidos |
| EUR | Euro | Unión Europea |
| BRL | Real brasileño | Brasil |
| ARS | Peso argentino | Argentina |
| UYU | Peso uruguayo | Uruguay |
| BOB | Boliviano | Bolivia |
| CLP | Peso chileno | Chile |
| COP | Peso colombiano | Colombia |
| PEN | Sol peruano | Perú |
| GBP | Libra esterlina | Reino Unido |
| JPY | Yen japonés | Japón |
| CNY | Yuan renminbi | China |
| CAD | Dólar canadiense | Canadá |
| CHF | Franco suizo | Suiza |
| MXN | Peso mexicano | México |

> La lista completa está definida por el estándar ISO 4217. SIFEN valida que el código informado sea válido según dicho estándar.

## Campos de moneda en otros grupos del DE

| Campo | ID | Descripción | Notas |
|-------|----|-------------|-------|
| `cMoneTiPag` | E609 | Moneda por tipo de pago | Mismo estándar ISO 4217. Obligatorio si E609 ≠ PYG informar E611 (tipo de cambio por pago) |
| [NUEVO] `cMoneCuo` | E653 | Moneda de las cuotas | [NUEVO] Aplica para operaciones a crédito por cuotas |

## Observación sobre decimales

[MODIFICADO] Para monedas extranjeras o cualquier cálculo que contenga decimales, las reglas de validación aceptarán redondeos de 50 céntimos (por encima o por debajo).
