> **Fuente:** Manual Técnico SIFEN v150, sección 15 — TABLA 5 (Codificación de Unidades de Medida)
> **Nota:** Contenido tachado (~~así~~) indica especificaciones eliminadas en v150. [MODIFICADO] indica cambios. [NUEVO] indica adiciones en v150.

# Códigos de Unidad de Medida (E709 – cUniMed)

El campo `cUniMed` (E709) contiene el código numérico de la unidad de medida del ítem. El campo `dDesUniMed` (E710) contiene la representación textual (abreviatura) de la unidad.

La validación 131 verifica que la descripción de la unidad de medida (E710) corresponda al código informado en E709.

> Cuando el tipo de operación es B2G (D202=3), se deben utilizar los datos provistos por el WS de la DNCP para la unidad de medida (campos E704, E705).

## TABLA 5 – Codificación de Unidades de Medida

| Código | Representación | Descripción |
|--------|---------------|-------------|
| 77 | UNI | Unidad |
| 79 | kg/m2 | Kilogramos por metro cuadrado (literal exacto del XSD: `kg/m2`, sin superíndice) |
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
| 869 | ha | Hectáreas |
| 885 | GL | Unidad Medida Global |
| 891 | pm | Por Milaje |
| 2329 | UI | Unidad Internacional |
| 2366 | CPM | Costo por Mil |

## Unidades agregadas por NT-023 (códigos 111–140)

Incorporadas a `Unidades_Medida_v141.xsd` (vigentes en producción desde 27/09/2024):

| Código | Representación | Descripción |
|--------|---------------|-------------|
| 111 | 4A | Bovinas |
| 112 | Ci | Curie |
| 113 | DOC | Docena |
| 114 | GLL | Galones (US) (3,7843 LT) |
| 115 | GRO | Gruesas |
| 116 | E4 | Kilogramo Bruto |
| 117 | KT | Kits |
| 118 | M5 | Microcurie |
| 119 | MCU | Milicurie |
| 120 | MIL | Millar |
| 121 | PAR | Par |
| 122 | FOT | Pies |
| 123 | FTK | Pies Cuadradas |
| 124 | PCE | Piezas |
| 125 | KLT | Quilate |
| 126 | RM | Resmas |
| 127 | RO | Rollos |
| 128 | kWh | 1000 Kilowatt Hora |
| 129 | U(JGO) | Mazos |
| 130 | DR | Tambores |
| 131 | BX | Caja |
| 132 | SET | Juego |
| 133 | PK | Paquete |
| 134 | BG | Bolsa |
| 135 | DPC | Docena Par |
| 136 | JR | Pote |
| 137 | BL | Fardos |
| 138 | AB | Bulto |
| 139 | BK | Cesta |
| 140 | BW | Peso Base |

## Notas del XSD de producción

- `tcUniMed` (E709) y `tdDesUniMed` (E710) son **enumeraciones cerradas** en `Unidades_Medida_v141.xsd` (64 códigos y 64 representaciones). La representación E710 debe coincidir **carácter por carácter** con el literal del XSD (sensible a mayúsculas: `kg`, `Hs`, `Mi`, `ración`, `U(JGO)`, etc.).
- Copia local del XSD: [`00-fuentes/xsd/Unidades_Medida_v141.xsd`](../00-fuentes/xsd/Unidades_Medida_v141.xsd).
