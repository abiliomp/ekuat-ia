> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 — Campo D015 (cMoneOpe); `00-fuentes/xsd/Monedas_v150.xsd` (`cMondT`, 200 códigos) y `DE_Types_v150.xsd:884-895` (`tdDMoneTiPag`), verificado el 03/10/2026
> **Nota:** Contenido tachado (~~así~~) indica especificaciones eliminadas en v150. [MODIFICADO] indica cambios. [NUEVO] indica adiciones en v150.

# Códigos de Moneda (D015 – cMoneOpe)

El campo `cMoneOpe` (D015) contiene el código de la moneda de la operación. Sigue el estándar internacional **ISO 4217** (tres letras mayúsculas). Es un campo alfanumérico de longitud 3, obligatorio.

**Regla:** Se requiere la misma moneda para todos los ítems del DE.

El campo `D016` (`dDesMoneOpe`) contiene la descripción de la moneda; su valor debe corresponder al código informado en D015 (validación 1206).

> **⚠️ Longitud de la descripción (verificado 03/10/2026).** D016 `dDesMoneOpe` (`DE_v150.xsd:209`), E651 `dDMoneCuo` (`:311`) y E609 `dDMoneTiPag` (`:1276`) son de tipo `tdDMoneTiPag` (`DE_Types_v150.xsd:884-895`): **texto libre de 3 a 20 caracteres**, no una enumeración. El `CodeName` de `Monedas_v150.xsd` es solo documentación y en **15 monedas supera los 20 caracteres**: ANG (29), BMD (46), FKP (22), KYD (21), MXV (27), SBD (22), TMT (22), TTD (26), UYI (38), XCD (21), XBA (48), XBB (50), XBC (57), XTS (48), XXX (65). Para ellas la descripción debe truncarse o adaptarse a ≤ 20 caracteres; qué literal acepta la validación 1206 en esos casos está `[PENDIENTE DE VERIFICACIÓN]`. Ver [xsd-produccion-vs-manual.md](../04-schemas-xsd/xsd-produccion-vs-manual.md) §16.

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

> **Precisión (XSD de producción):** SIFEN no valida contra "todo ISO 4217" sino contra la **lista cerrada de 200 códigos** del tipo `cMondT` en `Monedas_v150.xsd` (copia en [`00-fuentes/xsd/Monedas_v150.xsd`](../00-fuentes/xsd/Monedas_v150.xsd)). La lista incluye incluso códigos ISO retirados (ZMK, ZWD, YUM). Un código ISO válido que no esté en esa enumeración será rechazado por el esquema.

## Campos de moneda en otros grupos del DE

| Campo | ID | Descripción | Notas |
|-------|----|-------------|-------|
| `cMoneTiPag` | E609 | Moneda por tipo de pago | Mismo estándar ISO 4217. Obligatorio si E609 ≠ PYG informar E611 (tipo de cambio por pago) |
| [NUEVO] `cMoneCuo` | E653 | Moneda de las cuotas | [NUEVO] Aplica para operaciones a crédito por cuotas |

## Observación sobre decimales

[MODIFICADO] Para monedas extranjeras o cualquier cálculo que contenga decimales, las reglas de validación aceptarán redondeos de 50 céntimos (por encima o por debajo).
