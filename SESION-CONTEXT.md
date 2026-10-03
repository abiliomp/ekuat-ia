# Contexto de sesiones de trabajo

Este archivo resume el estado del repositorio y las tareas pendientes para retomar el trabajo con IA sin necesidad de re-explorar todo desde cero.

---

## Estado actual (octubre 2026)

- **Base:** Manual Técnico SIFEN v150 + NT-001 a **NT-027** (hasta marzo 2026)
- **Archivos Markdown** generados desde fuentes oficiales (PDFs, XSD, XML, XLSX)
- **XSD de producción descargados** (11/06/2026; **re-verificados sin cambios el 03/10/2026**, md5 en `00-fuentes/xsd/CHECKSUMS.md5`) en `00-fuentes/xsd/`: `siRecepDE_v150.xsd`, `DE_v150.xsd`, `DE_Types_v150.xsd`, `siRecepEvento_v150.xsd`, `Evento_v150.xsd`, `Evento_Types_v150.xsd`, `Paises_v100.xsd`, `Departamentos_v141.xsd`, `Monedas_v150.xsd`, `Unidades_Medida_v141.xsd`
- **`AGENTS.md`** en la raíz: orden de autoridad, archivos autoritativos por tema, reglas de cita (`archivo:línea` del XSD o sección/página del MT), marca `[PENDIENTE DE VERIFICACIÓN]`, procedimiento de re-descarga de XSD y prohibición de llamar a los WS. Leerlo primero.
- **Validación local sin red:** `04-schemas-xsd/validacion-local/` (`generar.py`, `validar.php`, `CAMBIOS.md5`): copias de los XSD con `schemaLocation` relativos y el fix `dEntCont ` → `dEntCont`. Regenerar cuando cambie `00-fuentes/xsd/`.
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

## Trabajo realizado en la sesión del 03/10/2026 (Fase 0 — saneamiento como fuente de verdad)

Motivación: la evaluación integral de PKuatia del 02/10/2026 (`pkuatia/docs/evaluacion-2026-10-02/EVALUACION-SIFEN-2026-10-02.md`, sección 14) detectó que varios archivos de este repo describían estructuras inexistentes. Se corrigió **antes** de tocar código.

1. **T1 — XSD re-verificados (03/10/2026):** los 11 archivos de `00-fuentes/xsd/` son byte a byte idénticos a producción (`CHECKSUMS.md5`, `md5sum -c`); bien formados; cadenas de `xs:include` compilables con libxml2. Historial y procedimiento en `xsd-produccion-vs-manual.md`.
2. **T2 — `05-api-sifen/` reescrito** desde el MT cap. 9 (PDF pp. 46-56, con páginas y IDs ASch/PP/BRSch/CRSch/DRSch/ContDE/GSch/GRSch/RRSch/ContRUC), los XSD y lo homologado por PKuatia (06/2026): `recepcion-de.md`, `envio-lote.md`, `consulta-estado.md`, `consulta-ruc.md`, `eventos.md`, `endpoints.md`, `autenticacion.md`. También `04-schemas-xsd/README.md` (numeración real de Schemas XML del MT, operaciones SOAP reales, estructura única de eventos) y `03-estructura-xml/reglas-de-validacion.md` (sin "±5 minutos"). Verificado con las marcas de color del PDF: en las tablas de los WS solo hay amarillo (`dEstRes`, `dProtAut`, `gResProcLote`, `gResProcEVe`, formato de `dFecProc` de eventos); ningún rojo.
3. **T3 — 0421/0422 resuelto:** 0422 = CDC encontrado, 0421 = RUC sin permiso (MT §9.4.2 Tabla G, guía 2024, homologación); el 0421 de la tabla 12.3.4.3 es error de edición. Sección "Divergencias entre documentos oficiales" (D1) en `xsd-produccion-vs-manual.md`.
4. **T4 — divergencias XSD vs MT ampliadas** (secciones 12-21 de `xsd-produccion-vs-manual.md`): `Constancia Electrónica`, `dDomFisc`/`dDirChof` obligatorios, `dEntCont ` con espacio, unidades 111-140 con sufijo " - ABREV", 15 monedas con `CodeName` > 20, eventos alcanzables vs huérfanos, `dRuc`/`dMonRet` en retenciones, fechas `fecHhmmss`, `tiTipDoc` vs `tiTipDocRec`, `tdNroMatVeh` = 6. Propagado a `07-codigos-referencia/` (tipos-documento, unidades, monedas) y a `nota-remision-electronica.md`.
5. **T5 — literal de ambiente de prueba:** divergencia guía (02/2026) vs validación 1263 anotada en `guia-de-pruebas.md`, `errores-validacion.md` y `xsd-produccion-vs-manual.md` (D2); se recomienda el literal del MT (aprobado en `sifen-test`).
6. **T6 — `AGENTS.md`, README (orden de autoridad y aviso sobre 05-api-sifen) y este archivo.**

Fuentes de las estructuras de los WS: MT cap. 9 (texto extraído con PyMuPDF a `mt150.txt`; páginas PDF: §7.10 p. 42, §9.1 p. 46, §9.2 p. 48, §9.3 p. 49, §9.4 p. 51, §9.5 p. 53, §9.6 p. 54, §11.5 p. 121, §12.3.x pp. 155-159), código homologado de PKuatia (`src/Core/Responses/*`, `src/Core/Fields/Response/*`, `src/Sifen.php`) y la guía de mejores prácticas (sobres reales).

## Commits

| Hash | Descripción |
|------|-------------|
| `20d43b9` | Commit inicial — base de conocimiento completa |
| `c77c040` | Fix — marcas de color en códigos de referencia y errores |
| `8b189dd` | Archivo de contexto de sesión |
| `8f7ac56` | NT-027 + alineación con XSD de producción |
| `c726909` | Endpoints verificados (06/2026) |
| `ec6865d` | Fase 0 T1 — re-verificación de XSD (03/10/2026) + `CHECKSUMS.md5` |
| `f980569` | Fase 0 T2 — reescritura de `05-api-sifen/` |
| `db04b63` | Fase 0 T3 — resolución 0421/0422 |
| (ver `git log`) | Fase 0 T4, T5 y T6 |

## Tareas pendientes para próximas sesiones

### Pendientes de verificación surgidos en la Fase 0 (03/10/2026)

Marcados `[PENDIENTE DE VERIFICACIÓN]` en los archivos; requieren una respuesta real del SIFEN o una aclaración de la DNIT:

- [ ] **Forma real de `xContEv` con eventos** en la respuesta de siConsDE (si trae `rContEv` > `xEvento` > `rGesEve` y `rResEnviEventoDe` > `rRetEnviEventoDe`; cuántos `rContEv`; namespaces de los hijos de `xContenDE`). Hoy solo se conoce `xContEv` vacío. **Decisión 03/10/2026:** se captura en la prueba de inicio de la Fase A (ver abajo).
- [ ] **Formato exacto de `dFecProc`** en `rProtDe` y en `rRetEnviEventoDe` (el MT dice `AAAA-MM-DDThh:mm:ss` y, para eventos, `AAAA-MM-DD-hh:mm:ss-ss:ss`; las respuestas reales del lote y la consulta traen zona horaria `-03:00`/`-04:00`).
- [ ] **Orden real de los hijos de `gResProcEVe`** y literal de `dMsgRes` para 0600.
- [ ] **`dEntCont ` con espacio** (`DE_v150.xsd:327`): qué hace el validador del SIFEN con una FE B2G que lleva `gCompPub`. **Decisión 03/10/2026:** mientras tanto se valida con `04-schemas-xsd/validacion-local/` (copias con el fix y `schemaLocation` relativos, generadas por `generar.py`).
- [ ] **Literal de ambiente de prueba**: guía (02/2026) vs validación 1263; y si el primer ítem debe llevar el literal. **Decisión 03/10/2026:** la regla es el literal del MT en `dNomEmi`; probar el de la guía en `sifen-test` durante la Fase A.
- [ ] **Unidad de `dTpoProces`** (segundos según BRSch06, milisegundos según §8.2.2).
- [ ] **Nombre del archivo dentro del ZIP del lote** (solo se probó `rLoteDE.xml`) y tamaño máximo del lote (10.000 KB en el MT vs 1000 KB en la guía).
- [ ] **Código 0143** observado en `sifen-test` para un evento de receptor firmado por el emisor (no está en el MT).
- [ ] **Endoso (`rGeVeEnd`)**: enviable según el XSD, "futuro" según el MT; sin validaciones publicadas.
- [ ] **Descripción de las 15 monedas con `CodeName` > 20 caracteres** (`tdDMoneTiPag` admite 3-20): qué literal acepta la validación 1206.
- [ ] **Organismo rector de la firma digital** tras la Ley 6822/2021 (el MT dice MIC; "DINETIC" no tiene fuente).
- [ ] **Tolerancia de reloj**: el MT no publica minutos (solo 1004/1005).
- [ ] **Semántica de `rEve@Id`** con varios eventos por sobre (homologado solo con Id = 1).

### Prueba a ejecutar al inicio de la Fase A de PKuatia (decisión 03/10/2026)

Antes de tocar las clases de respuesta de PKuatia, una sesión **con red y certificado** ejecuta contra `sifen-test` el flujo FE → cancelación → consulta y archiva las respuestas SOAP **crudas** (`SoapClient::__getLastResponse()`, sin parsear) anonimizadas en `06-ejemplos/respuestas-ws/` de este repo. Capturar exactamente:

| Llamada | Qué guardar | Pendientes que cierra |
|---------|-------------|-----------------------|
| `EnviarDE` (FE aprobada) | `rRetEnviDe` completo | Formato real de `dFecProc` en `rProtDe`; orden de `id`/`dFecProc`/`dDigVal`/`dEstRes`/`dProtAut`/`gResProc`; literal de `dMsgRes` para 0260 |
| `CancelarDE` del mismo CDC | `rRetEnviEventoDe` completo | Formato real de `dFecProc` de eventos; orden de los hijos de `gResProcEVe`; literal de `dMsgRes` para 0600 |
| `ConsultarDE` del CDC cancelado | `rEnviConsDeResponse` completo, con `xContenDE` **byte a byte** | Forma de `xContEv` con eventos (`rContEv` > `xEvento`/`rResEnviEventoDe`?, cuántos `rContEv`), namespaces de los hijos de `xContenDE`, si `dProtAut` sigue presente tras la cancelación |
| (opcional) `ConsultarDE` de un CDC rechazado y de uno inexistente | Respuestas 0420 | Literal de `dMsgRes` para 0420 |

Con los archivos capturados: actualizar `05-api-sifen/recepcion-de.md`, `eventos.md` y `consulta-estado.md` quitando las marcas `[PENDIENTE DE VERIFICACIÓN]` correspondientes y citando el fixture.

### Pendientes anteriores


- [ ] **Documentar las boletas (C002=9 y 10)** — "Boleta de venta electrónica" y "Boleta resimple electrónica" existen en el XSD de producción pero no hay NT ni sección del MT que las describa; buscar documentación oficial del régimen RESIMPLE / e-kuatia'i
- [ ] **Documentar los eventos no cubiertos por el MT** que aparecen en `Evento_v150.xsd`: endoso, retención aceptada/anulada, CCFF, eventos de la SET (bloqueo, impugnación, detención) — ver sección 10 de `xsd-produccion-vs-manual.md`
- [ ] **Agregar más ejemplos** en `06-ejemplos/` — autofactura, nota de crédito, nota de remisión
- [ ] **Agregar KuDE** — documentar la estructura gráfica del KuDE en una carpeta `11-kude/`
- [ ] **Verificar NT-025** — su fecha de publicación (23/04/2024) y fechas de ambiente (28/04/2025) parecen inconsistentes
- [ ] **Re-descargar los XSD periódicamente** (`md5sum -c 00-fuentes/xsd/CHECKSUMS.md5`, procedimiento en `AGENTS.md` §4) y refrescar `xsd-produccion-vs-manual.md` — la DNIT cambia los XSD sin reeditar el MT. Última verificación: 03/10/2026, sin cambios
- [ ] **Actualizar cuando salgan nuevas NTs** — la última procesada es NT-027 (marzo 2026)

## Notas técnicas importantes

- **Marcas de color en el MT v150 (no solo en las NT):** amarillo sobre `dEstRes`, `dProtAut`, `gResProcLote`, `gResProcEVe` y el formato de `dFecProc` de eventos (pp. 47, 51, 54); la tabla 12.3.4.3 (p. 158) no tiene marcas. Script de detección: `page.get_drawings()` filtrando `fill` ≈ (1,1,0) / (1,0,0) / (0,1,0) y `page.get_text(clip=rect)`.
- **Herramienta Bash de la sesión:** los comandos muy largos (heredocs > ~4 KB) fallan con "unexpected EOF"; escribir los scripts a un archivo y ejecutarlos.

- Los archivos fuente están en `00-fuentes/` — PDFs oficiales SET/DNIT y XSD de producción
- Colores identificados en los PDFs de NT: rojo `(1.0,0.0,0.0)` = ELIMINADO, amarillo `(1.0,1.0,0.0)` = MODIFICADO, verde `(0.0,1.0,0.0)` = NUEVO
- Al comparar enumeraciones del XSD: cuidado con los tipos `xs:union` (enumeración + texto libre) y con las enumeraciones **comentadas** dentro del XSD (p. ej. FEE/FEI/CRE en `tdDesTiDE`); los comentarios `<!--...-->` de códigos suelen estar desplazados una línea respecto al valor que describen
