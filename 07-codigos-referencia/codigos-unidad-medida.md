# Códigos de Unidad de Medida (E709 / cUniMed)

Campo `cUniMed` (E709): código de la unidad de medida del ítem. El campo `dDesUniMed` (E710) contiene la descripción textual (representación) de la unidad.

Cuando el tipo de operación es B2G (D202=3), se deben utilizar los datos del WS de la DNCP para la unidad de medida.

> **Fuente:** Manual Técnico SIFEN v150, sección 15 (TABLA 5 – Codificación de Unidades de Medida)

## TABLA 5 – Unidades de Medida

| Código (cUniMed) | Representación (dDesUniMed) | Descripción |
|-----------------|----------------------------|-------------|
| 77 | UNI | Unidad |
| 83 | kg | Kilogramos |
| 86 | g | Gramos |
| 87 | m | Metros |
| 88 | ML | Mililitros |
| 89 | LT | Litros |
| 90 | MG | Miligramos |
| 91 | CM | Centímetros |
| 92 | CM2 | Centímetros cuadrados |
| 93 | CM3 | Centímetros cúbicos |
| 94 | PUL | Pulgadas |
| 95 | MM | Milímetros |
| 96 | MM2 | Milímetros cuadrados |
| 97 | AA | Año |
| 98 | ME | Mes |
| 99 | TN | Tonelada |
| 100 | Hs | Hora |
| 101 | Mi | Minuto |
| 102 | Di | Día |
| 103 | Ya | Yardas |
| 104 | DET | Determinación |
| 108 | MT | Metros |
| 109 | M2 | Metros cuadrados |
| 110 | M3 | Metros cúbicos |
| 569 | ración | Ración |
| 625 | Km | Kilómetros |
| 660 | ml | Metro lineal |
| 666 | Se | Segundo |
| 79 | kg/m² | Kilogramos por metro cuadrado |
| 869 | ha | Hectáreas |
| 885 | GL | Unidad Medida Global |
| 891 | pm | Por Milaje |
| 2329 | UI | Unidad Internacional |
| 2366 | CPM | Costo por Mil |

## Uso en el DE

Los campos de unidad de medida se encuentran en el grupo E8 (ítems de la operación):

| Campo | ID | Descripción |
|-------|----|-------------|
| Código de unidad de medida | E709 / cUniMed | Código numérico de la TABLA 5 |
| Descripción de unidad de medida | E710 / dDesUniMed | Representación textual (ej: "UNI", "kg", "LT") |

## Observaciones

- El campo E709 (cUniMed) usa el atributo "ID" del XSD de unidades.
- El campo E710 (dDesUniMed) usa el atributo "Código" del XSD de unidades.
- Cuando D202=3 (B2G - compras públicas): utilizar los datos del WS del link de la DNCP.
