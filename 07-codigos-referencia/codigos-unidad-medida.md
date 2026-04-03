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
| 79 | kg/m² | Kilogramos por metro cuadrado |
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
