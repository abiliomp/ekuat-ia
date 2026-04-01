# Códigos de País (D203 / cPaisRec, E712 / cPaisOrig)

Campos que utilizan códigos de país:
- `cPaisRec` (D203): código del país del receptor
- `cPaisOrig` (E712): código del país de origen del producto

Todos siguen el estándar internacional **ISO 3166-1 alpha-3** (código de tres letras).

> **Fuente:** Manual Técnico SIFEN v150, sección 15 (TABLA 4) y sección 10.4 (campos D203, E712)

## Estándar utilizado

El sistema SIFEN utiliza el estándar **ISO 3166-1 alpha-3**. La lista completa se encuentra en:
- Referencia: https://es.wikipedia.org/wiki/ISO_3166-1#Códigos_ISO_3166-1
- El Schema XSD de codificación de países está disponible en: http://ekuatia.set.gov.py/portal/ekuatia/documentaciontecnica

## Países principales referenciados en SIFEN

| Código Alpha-3 | País | Región |
|---------------|------|--------|
| PRY | Paraguay | América del Sur |
| ARG | Argentina | América del Sur |
| BRA | Brasil | América del Sur |
| BOL | Bolivia | América del Sur |
| CHL | Chile | América del Sur |
| COL | Colombia | América del Sur |
| PER | Perú | América del Sur |
| URY | Uruguay | América del Sur |
| VEN | Venezuela | América del Sur |
| ECU | Ecuador | América del Sur |
| MEX | México | América del Norte |
| USA | Estados Unidos | América del Norte |
| CAN | Canadá | América del Norte |
| GBR | Reino Unido | Europa |
| DEU | Alemania | Europa |
| ESP | España | Europa |
| FRA | Francia | Europa |
| ITA | Italia | Europa |
| PRT | Portugal | Europa |
| CHN | China | Asia |
| JPN | Japón | Asia |
| KOR | Corea del Sur | Asia |

## Reglas de validación (campo D203)

- Si el tipo de operación es **B2F** (D202=4): el país del receptor debe ser **diferente a PRY** (D203 ≠ PRY). Error 1320.
- Si el tipo de operación es **distinto a B2F** (D202 ≠ 4): el país del receptor debe ser **PRY** (D203 = PRY). Error 1320.
- La descripción D204 debe coincidir con el código D203. Error 1301.

## Uso en la Autofactura Electrónica

En la AFE, cuando el vendedor es extranjero (E301=2), se utilizan los campos de dirección del vendedor donde la ciudad, departamento y distrito corresponden a donde se realizó la transacción.

## Nota sobre operaciones internacionales (B2F)

El tipo de operación **B2F** (Business to Foreign) se utiliza exclusivamente para servicios prestados por una empresa nacional a una empresa o persona física del exterior. En este caso:
- D203 debe ser ≠ PRY
- No se informa el tipo de documento de identidad del receptor (D208)
- No se informa la dirección del receptor (D213)
