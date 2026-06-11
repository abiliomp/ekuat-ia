# Contexto de sesiones de trabajo

Este archivo resume el estado del repositorio y las tareas pendientes para retomar el trabajo con IA sin necesidad de re-explorar todo desde cero.

---

## Estado actual (junio 2026)

- **Base:** Manual Técnico SIFEN v150 + NT-001 a **NT-027** (hasta marzo 2026)
- **Archivos Markdown** generados desde fuentes oficiales (PDFs, XSD, XML, XLSX)
- **XSD de producción descargados** (11/06/2026) en `00-fuentes/xsd/`: `siRecepDE_v150.xsd`, `DE_v150.xsd`, `DE_Types_v150.xsd`, `siRecepEvento_v150.xsd`, `Evento_v150.xsd`, `Evento_Types_v150.xsd`, `Paises_v100.xsd`, `Departamentos_v141.xsd`, `Monedas_v150.xsd`, `Unidades_Medida_v141.xsd`
- **Divergencias MT vs XSD documentadas** en `04-schemas-xsd/xsd-produccion-vs-manual.md` — es el documento de referencia cuando un literal del MT no coincide con producción (caso típico: `dDesAfecIVA` código 2 = "Exonerado (Art. 100 - Ley 6380/2019)")
- **Detección de color correcta:** los PDFs usan resaltado rojo/amarillo/verde para indicar eliminaciones, modificaciones y adiciones. El repositorio refleja esto con `~~tachado~~`, `[MODIFICADO]` y `[NUEVO]`.
- **Herramienta usada para extracción:** PyMuPDF (`fitz`) — NO usar `pdfplumber` que no detecta colores. Las marcas de color pueden ser rectángulos diminutos (en NT-027 cubrían un solo dígito): conviene listar los rects de color con `page.get_drawings()` y extraer el texto bajo cada rect con `page.get_text(clip=rect)`.

## Trabajo realizado en la sesión de junio 2026

1. **NT-027 procesada** (`09-notas-tecnicas/NT-027.md`): el código de "Tarjeta Diplomática de exoneración fiscal" en el evento de Nominación de FE (GENFE010/GENFE011) pasa de 5 a 6, alineándose con D208. Propagado a `eventos.md`, `NT-014.md`, índices y READMEs.
2. **XSD de producción comparados contra la documentación**; correcciones aplicadas en:
   - `07-codigos-referencia/codigos-impuesto.md` — literales exactos de E732 (`dDesAfecIVA`), D014 (`IVA - Renta`), categorías ISC
   - `07-codigos-referencia/tipos-documento.md` — C002: el XSD solo acepta `1|4-7|9|10`; códigos 9/10 = boletas (RESIMPLE), no documentados en el MT
   - `07-codigos-referencia/tipos-transaccion.md` — literal "Mixto (Venta de mercadería y servicios)", "Venta al Consumidor final", tabla de motivos de traslado corregida (faltaba Importación=5; había motivos inexistentes)
   - `07-codigos-referencia/tipos-receptor.md`, `03-estructura-xml/campos-obligatorios.md`, `campos-condicionales.md`, `reglas-de-validacion.md`, `08-errores-y-respuestas/errores-validacion.md` — condiciones D208/D210 post NT-023 y umbral innominado 7M (NT-024)
   - `07-codigos-referencia/codigos-unidad-medida.md` — agregados códigos 111-140 (NT-023), literal `kg/m2`
   - `07-codigos-referencia/codigos-moneda.md` / `codigos-pais.md` — son listas cerradas del XSD (200 monedas / 250 países), no "todo ISO"
   - `02-documentos-electronicos/nota-remision-electronica.md` — literales exactos de motivos de traslado
   - `04-schemas-xsd/README.md` — en producción no hay XSD por evento; URLs directas de descarga

## Commits

| Hash | Descripción |
|------|-------------|
| `20d43b9` | Commit inicial — base de conocimiento completa |
| `c77c040` | Fix — marcas de color en códigos de referencia y errores |
| `8b189dd` | Archivo de contexto de sesión |
| (pendiente) | NT-027 + alineación con XSD de producción |

## Tareas pendientes para próximas sesiones

- [ ] **Documentar las boletas (C002=9 y 10)** — "Boleta de venta electrónica" y "Boleta resimple electrónica" existen en el XSD de producción pero no hay NT ni sección del MT que las describa; buscar documentación oficial del régimen RESIMPLE / e-kuatia'i
- [ ] **Documentar los eventos no cubiertos por el MT** que aparecen en `Evento_v150.xsd`: endoso, retención aceptada/anulada, CCFF, eventos de la SET (bloqueo, impugnación, detención) — ver sección 10 de `xsd-produccion-vs-manual.md`
- [ ] **Agregar más ejemplos** en `06-ejemplos/` — autofactura, nota de crédito, nota de remisión
- [ ] **Agregar KuDE** — documentar la estructura gráfica del KuDE en una carpeta `11-kude/`
- [ ] **Verificar NT-025** — su fecha de publicación (23/04/2024) y fechas de ambiente (28/04/2025) parecen inconsistentes
- [ ] **Re-descargar los XSD periódicamente** y refrescar `xsd-produccion-vs-manual.md` — la DNIT cambia los XSD sin reeditar el MT
- [ ] **Actualizar cuando salgan nuevas NTs** — la última procesada es NT-027 (marzo 2026)

## Notas técnicas importantes

- Los archivos fuente están en `00-fuentes/` — PDFs oficiales SET/DNIT y XSD de producción
- Colores identificados en los PDFs de NT: rojo `(1.0,0.0,0.0)` = ELIMINADO, amarillo `(1.0,1.0,0.0)` = MODIFICADO, verde `(0.0,1.0,0.0)` = NUEVO
- Al comparar enumeraciones del XSD: cuidado con los tipos `xs:union` (enumeración + texto libre) y con las enumeraciones **comentadas** dentro del XSD (p. ej. FEE/FEI/CRE en `tdDesTiDE`); los comentarios `<!--...-->` de códigos suelen estar desplazados una línea respecto al valor que describen
