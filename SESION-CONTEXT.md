# Contexto de sesiones de trabajo

Este archivo resume el estado del repositorio y las tareas pendientes para retomar el trabajo con IA sin necesidad de re-explorar todo desde cero.

---

## Estado actual (abril 2026)

- **Base:** Manual Técnico SIFEN v150 + NT-001 a NT-026 (hasta junio 2025)
- **70 archivos Markdown** generados desde fuentes oficiales (PDFs, XSD, XML, XLSX)
- **Detección de color correcta:** los PDFs usan resaltado rojo/amarillo/verde para indicar eliminaciones, modificaciones y adiciones. El repositorio refleja esto con `~~tachado~~`, `[MODIFICADO]` y `[NUEVO]`.
- **Herramienta usada para extracción:** PyMuPDF (`fitz`) — NO usar `pdfplumber` que no detecta colores

## Commits

| Hash | Descripción |
|------|-------------|
| `20d43b9` | Commit inicial — base de conocimiento completa |
| `c77c040` | Fix — marcas de color en códigos de referencia y errores |

## Tareas pendientes para próximas sesiones

- [ ] **Revisar consistencia** entre los archivos de `03-estructura-xml/campos-obligatorios.md` y las NTs — las NTs modifican campos que pueden no estar reflejados en el archivo de campos
- [ ] **Aplicar NTs sobre el MT base** — construir una vista "estado actual" de cada campo incorporando todos los cambios de NT-001 a NT-026 acumulados
- [ ] **Agregar más ejemplos** en `06-ejemplos/` — autofactura, nota de crédito, nota de remisión
- [ ] **Agregar KuDE** — documentar la estructura gráfica del KuDE en una carpeta `11-kude/`
- [ ] **Verificar NT-025** — su fecha de publicación (23/04/2024) y fechas de ambiente (28/04/2025) parecen inconsistentes
- [ ] **Actualizar cuando salgan nuevas NTs** — la última procesada es NT-026 (junio 2025)

## Notas técnicas importantes

- Los archivos fuente están en `00-fuentes/` — PDFs oficiales SET/DNIT
- Script de extracción con colores: ver historial de conversación (usa `fitz.get_drawings()` para detectar rectángulos de color)
- Colores identificados: rojo `(1.0,0.0,0.0)` = ELIMINADO, amarillo `(1.0,1.0,0.0)` = MODIFICADO, verde `(0.0,1.0,0.0)` = NUEVO
- Los textos extraídos con colores están en `C:/Users/abili/.claude/colored/` (archivos temporales, no versionados)
