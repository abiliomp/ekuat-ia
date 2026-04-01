# Códigos de Moneda (D015 / cMoneOpe)

Campo `cMoneOpe` (D015): código de la moneda de la operación. Sigue el estándar internacional **ISO 4217**. Se requiere la misma moneda para todos los ítems del DE.

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 (campo D015) y sección 15 (Tabla de monedas ISO 4217)

## Moneda por defecto

**PYG** (Guaraní paraguayo) es la moneda por defecto para operaciones domésticas. Cuando la moneda es PYG:
- No se debe informar el campo D017 (condición del tipo de cambio)
- No se debe informar el campo D018 (tipo de cambio de la operación)
- No se debe informar el campo E725 (tipo de cambio por ítem)

## Tabla de monedas utilizadas en SIFEN

| Código ISO 4217 | Moneda | País / Área |
|----------------|--------|------------|
| PYG | Guaraní paraguayo | Paraguay |
| USD | Dólar americano | Estados Unidos |
| EUR | Euro | Zona Euro |
| BRL | Real brasileño | Brasil |
| ARS | Peso argentino | Argentina |
| BOB | Boliviano | Bolivia |
| CLP | Peso chileno | Chile |
| COP | Peso colombiano | Colombia |
| PEN | Sol peruano | Perú |
| UYU | Peso uruguayo | Uruguay |
| GBP | Libra esterlina | Reino Unido |
| JPY | Yen japonés | Japón |
| CNY | Yuan chino (Renminbi) | China |

> La lista completa de códigos de moneda sigue el estándar ISO 4217.
> Referencia oficial: https://www.currency-iso.org/en/home/tables/table-a1.html

## Campos relacionados

| Campo | ID | Descripción |
|-------|----|-------------|
| Moneda de la operación | D015 | Código ISO 4217 de la moneda del DE |
| Descripción de la moneda | D016 | Texto descriptivo de la moneda (referente a D015) |
| Condición del tipo de cambio | D017 | 1=Global, 2=Por ítem. Obligatorio si D015 ≠ PYG |
| Tipo de cambio de la operación | D018 | Obligatorio si D017=1. No informar si D015=PYG |
| Tipo de cambio por tipo de pago | E611 | Obligatorio si E609 ≠ PYG |
| Tipo de cambio por ítem | E725 | Obligatorio si D017=2 y D015 ≠ PYG |

## Reglas de validación asociadas

- Si D015 ≠ PYG: es obligatorio informar D017 (condición del tipo de cambio). Código de error: 1207.
- Si D015 = PYG: no se debe informar D017. Código de error: 1208.
- Si D017 = 1 (global): es obligatorio informar D018. Código de error: 1209.
- Si D017 = 2 (por ítem) o D015 = PYG: no se informa D018. Código de error: 1210.
- La descripción D016 debe coincidir con el código D015. Código de error: 1206.
