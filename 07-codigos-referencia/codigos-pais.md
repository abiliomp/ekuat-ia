> **Fuente:** Manual Técnico SIFEN v150, sección 15 — TABLA 4 (Codificación de Países)
> **Nota:** Contenido tachado (~~así~~) indica especificaciones eliminadas en v150. [MODIFICADO] indica cambios. [NUEVO] indica adiciones en v150.

# Códigos de País (D203 / cPaisRec — E712 / cPaisOrig)

SIFEN utiliza el estándar internacional **ISO 3166-1 alpha-3** (tres letras mayúsculas) para identificar países.

**Referencia oficial:** https://es.wikipedia.org/wiki/ISO_3166-1#Códigos_ISO_3166-1
**Archivo XSD:** `https://ekuatia.set.gov.py/sifen/xsd/Paises_v100.xsd` (copia en [`00-fuentes/xsd/Paises_v100.xsd`](../00-fuentes/xsd/Paises_v100.xsd)).

> **Precisión (XSD de producción):** la validación es contra la **lista cerrada de 250 códigos** del tipo `paisType` en `Paises_v100.xsd` (incluye el código especial `NN`), no contra "todo ISO 3166-1".

## Campos que utilizan códigos de país

| Campo | ID | Descripción | Observaciones |
|-------|----|-------------|---------------|
| `cPaisRec` | D203 | Código del país del receptor | Validado contra XSD de codificación de países |
| `dDesPaisRec` | D204 | Descripción del país receptor | Debe corresponder al código D203 |
| `cPaisOrig` | E712 | Código del país de origen del producto | Aplica para ítems en el grupo E700 |
| `dDesPaisOrig` | E713 | Descripción del país de origen | Debe corresponder al código E712 |

## Reglas de aplicación

| Condición | Regla |
|-----------|-------|
| [NUEVO] D202 = 4 (B2F — operaciones al exterior) | El país del receptor **debe ser diferente a PRY** (D203 ≠ PRY) |
| [NUEVO] D202 ≠ 4 | El país del receptor **debe ser Paraguay** (D203 = PRY) |
| [NUEVO] D202 = 4 | La naturaleza del receptor debe ser No Contribuyente (D201 = 2) |

## Principales códigos ISO 3166-1 alpha-3

| Código | País |
|--------|------|
| PRY | Paraguay |
| ARG | Argentina |
| BRA | Brasil |
| URY | Uruguay |
| BOL | Bolivia |
| CHL | Chile |
| COL | Colombia |
| PER | Perú |
| VEN | Venezuela |
| ECU | Ecuador |
| MEX | México |
| USA | Estados Unidos |
| ESP | España |
| DEU | Alemania |
| FRA | Francia |
| GBR | Reino Unido |
| ITA | Italia |
| CHN | China |
| JPN | Japón |
| CAN | Canadá |
| KOR | Corea del Sur |
| IND | India |
| RUS | Rusia |
| AUS | Australia |
| NLD | Países Bajos |
| PRT | Portugal |
| CHE | Suiza |
| BEL | Bélgica |
| SWE | Suecia |
| NOR | Noruega |
| DNK | Dinamarca |
| FIN | Finlandia |
| AUT | Austria |
| POL | Polonia |
| CZE | República Checa |
| HUN | Hungría |
| ROU | Rumanía |
| BGR | Bulgaria |
| HRV | Croacia |
| GRC | Grecia |
| TUR | Turquía |
| ISR | Israel |
| SAU | Arabia Saudita |
| ARE | Emiratos Árabes Unidos |
| ZAF | Sudáfrica |
| EGY | Egipto |
| NGA | Nigeria |
| KEN | Kenia |
| MAR | Marruecos |
| THA | Tailandia |
| VNM | Vietnam |
| IDN | Indonesia |
| MYS | Malasia |
| SGP | Singapur |
| PHL | Filipinas |
| PAK | Pakistán |
| BGD | Bangladesh |

> La lista completa de códigos ISO 3166-1 alpha-3 se define en el estándar internacional y en el archivo XSD provisto por la SET. Esta tabla incluye los países de mayor relevancia para operaciones con Paraguay.
