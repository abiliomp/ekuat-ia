# AGENTS.md — Reglas para agentes de IA que trabajan sobre este repositorio

Este repositorio es la **fuente de verdad** sobre el SIFEN (facturación electrónica de Paraguay) para los agentes que corrigen o amplían la librería PHP [PKuatia](https://github.com/IonysDev/pkuatia) y otras integraciones. Un error aquí se propaga a código que se envía a la DNIT. Leer este archivo antes de citar o modificar cualquier archivo del repo.

## 1. Orden de autoridad

Cuando dos fuentes difieren, **gana la de arriba** y la divergencia se documenta en [04-schemas-xsd/xsd-produccion-vs-manual.md](./04-schemas-xsd/xsd-produccion-vs-manual.md). Nunca se "promedia" ni se elige la versión más cómoda.

| Nivel | Fuente | Dónde está |
|-------|--------|------------|
| 1 | **XSD de producción** publicados en `https://ekuatia.set.gov.py/sifen/xsd/` | Copias en [`00-fuentes/xsd/`](./00-fuentes/xsd/) (md5 en `CHECKSUMS.md5`; última verificación 03/10/2026, sin cambios desde el 11/06/2026) |
| 2 | **Manual Técnico v150, secciones 12.x** (códigos y mensajes de validación) | [`08-errores-y-respuestas/`](./08-errores-y-respuestas/): `respuestas-ws.md`, `estructura-codigos.md`, `errores-validacion.md`, `eventos-respuesta.md` |
| 3 | **Guías oficiales de la DNIT** (mejores prácticas de envío, guía de pruebas) | [`10-guias/`](./10-guias/) |
| 4 | **Notas Técnicas** NT-001 a NT-027 | [`09-notas-tecnicas/`](./09-notas-tecnicas/) |
| 5 | El resto del MT v150 y los demás archivos del repo | `00-fuentes/pdfs/Manual Técnico Versión 150.pdf` y carpetas 01-07 |

Lo **homologado empíricamente** (respuestas reales de `sifen-test` o producción, p. ej. las de PKuatia en junio de 2026 o los sobres de la guía de mejores prácticas) sirve para decidir la forma real de un mensaje cuando el MT es ambiguo, y siempre se cita como tal ("homologado 06/2026").

## 2. Archivos autoritativos por tema

| Tema | Archivo |
|------|---------|
| Literales de enumeraciones (`dDes*`), patrones, longitudes, obligatoriedad | Los XSD en `00-fuentes/xsd/` (`DE_v150.xsd`, `DE_Types_v150.xsd`, `Evento_v150.xsd`, `Evento_Types_v150.xsd`, catálogos). Resumen de trampas: [xsd-produccion-vs-manual.md](./04-schemas-xsd/xsd-produccion-vs-manual.md) |
| Protocolo de los web services (request/response, operaciones, rutas, códigos) | [`05-api-sifen/`](./05-api-sifen/): `endpoints.md`, `recepcion-de.md`, `envio-lote.md`, `consulta-estado.md`, `consulta-ruc.md`, `eventos.md`, `autenticacion.md` (reescritos el 03/10/2026 desde el MT cap. 9, los XSD y lo homologado) |
| Códigos de resultado de los WS (0001-0619) | [`08-errores-y-respuestas/respuestas-ws.md`](./08-errores-y-respuestas/respuestas-ws.md) y [`estructura-codigos.md`](./08-errores-y-respuestas/estructura-codigos.md) |
| Validaciones de negocio del DE (1000-2650) | [`08-errores-y-respuestas/errores-validacion.md`](./08-errores-y-respuestas/errores-validacion.md) |
| Eventos: tablas de campos del MT y validaciones 4000-4478 | [`08-errores-y-respuestas/eventos-respuesta.md`](./08-errores-y-respuestas/eventos-respuesta.md) (MT) + [`05-api-sifen/eventos.md`](./05-api-sifen/eventos.md) (XSD y WS) |
| Tablas de códigos (tipos de documento, impuestos, monedas, países, unidades, geografía…) | [`07-codigos-referencia/`](./07-codigos-referencia/) |
| Campos del DE por grupo, obligatorios y condicionales | [`03-estructura-xml/`](./03-estructura-xml/) y [`02-documentos-electronicos/`](./02-documentos-electronicos/) |
| Cambios al MT por NT | [`09-notas-tecnicas/`](./09-notas-tecnicas/) (una NT por archivo, con la leyenda de colores) |
| Estado de las sesiones y pendientes | [`SESION-CONTEXT.md`](./SESION-CONTEXT.md) |

## 3. Reglas de edición

1. **Nada sin fuente.** Cada afirmación nueva o corregida cita `archivo:línea` del XSD (p. ej. `DE_v150.xsd:973`) o sección y página del PDF del MT (p. ej. "MT §9.4.2 Tabla G, PDF p. 52") o la NT/guía correspondiente. Lo que no se puede verificar se marca literalmente **`[PENDIENTE DE VERIFICACIÓN]`** con una nota de qué falta. **No inventar campos, códigos, rutas ni estructuras**: si un nombre no aparece en un XSD, en un WSDL verificado o en una tabla del MT, no existe.
2. **Los literales se comparan byte a byte.** Un espacio, una tilde o una mayúscula distinta producen rechazo (`0160 XML malformado: El valor del elemento: X es invalido`). Copiar los literales **desde el XSD**, nunca desde el PDF del MT ni de memoria. Ejemplos ya documentados: `Exonerado (Art. 100 - Ley 6380/2019)`, `Gravado parcial (Grav- Exento)`, `IVA - Renta`, `Constancia Electrónica`, `Traslado de bienes para reparación`.
3. **Marcas de color del MT y las NT.** Los PDF oficiales resaltan en **rojo** lo eliminado, **amarillo** lo modificado y **verde** lo nuevo. Al extraer texto hay que detectar esas marcas (PyMuPDF `fitz`, `page.get_drawings()` + `page.get_text(clip=rect)`; nunca `pdfplumber`) y volcarlas como `~~tachado~~`, `[MODIFICADO]` y `[NUEVO]`. Un texto sin marca puede estar igualmente desactualizado respecto del XSD.
4. **Convenciones del repo.** Encabezado `> **Fuente:** …` en cada archivo; tablas Markdown; castellano; marcas `[NUEVO]`, `[MODIFICADO]`, `~~eliminado~~`. Al corregir un archivo, dejar una nota breve de qué se eliminó y por qué, para que un agente que recuerde la versión anterior no la reintroduzca.
5. **Propagar.** Un literal o regla corregida se cambia en todos los archivos de "estado actual" (03, 05, 07, 08) y no solo en la NT que lo introdujo.
6. **Git.** Conventional Commits en castellano (`docs(api): …`, `fix(xsd): …`), un commit por tarea, sin `push` salvo instrucción explícita del propietario.

## 4. Cómo re-descargar y comparar los XSD

```bash
cd 00-fuentes/xsd
for f in siRecepDE_v150.xsd DE_v150.xsd DE_Types_v150.xsd siRecepEvento_v150.xsd Evento_v150.xsd Evento_Types_v150.xsd Paises_v100.xsd Departamentos_v141.xsd Monedas_v150.xsd Unidades_Medida_v141.xsd xmldsig-core-schema.xsd; do
  curl -sS -L -o "/tmp/$f" "https://ekuatia.set.gov.py/sifen/xsd/$f"
done
(cd /tmp && md5sum -c "$OLDPWD/CHECKSUMS.md5")
```

- Si todo es `OK`: anotar la fecha de re-verificación en `xsd-produccion-vs-manual.md` (historial) y en `SESION-CONTEXT.md`.
- Si algo difiere: reemplazar la copia, regenerar `CHECKSUMS.md5`, hacer `git diff` del XSD, documentar cada cambio con fecha en `xsd-produccion-vs-manual.md` y propagar a `07-codigos-referencia/` y a los archivos afectados.
- Comprobar que los 11 archivos estén bien formados (xmllint o PHP `DOMDocument::load`) y que las cadenas de `xs:include` compilen (`DOMDocument::schemaValidate` con un documento mínimo). Los `schemaLocation` apuntan a URLs absolutas; para validar sin red reescribirlos a rutas locales en una copia temporal (`sed 's#https://ekuatia.set.gov.py/sifen/xsd/##g'`).

## 5. Prohibiciones

- **No llamar a los web services del SIFEN** (`sifen.set.gov.py`, `sifen-test.set.gov.py`) desde una sesión de documentación: requieren certificado, y el ambiente de pruebas bloquea temporalmente por saturación. Solo se descargan los XSD estáticos de `ekuatia.set.gov.py/sifen/xsd/`.
- No "corregir" un XSD de `00-fuentes/xsd/` (p. ej. el `dEntCont ` con espacio de `DE_v150.xsd:327`): son copias fieles y son las que se citan por línea. Las copias modificadas para validación local están en [`04-schemas-xsd/validacion-local/`](./04-schemas-xsd/validacion-local/) y se regeneran con `python 04-schemas-xsd/validacion-local/generar.py` cada vez que cambie `00-fuentes/xsd/`; para validar un documento: `php 04-schemas-xsd/validacion-local/validar.php documento.xml`.
- No eliminar información no verificada: se marca `[PENDIENTE DE VERIFICACIÓN]`; eliminar solo lo que se demostró inexistente, dejando la nota correspondiente.

## 6. Pendientes conocidos (03/10/2026)

Ver la sección "Tareas pendientes" de [SESION-CONTEXT.md](./SESION-CONTEXT.md): boletas C002 = 9 y 10, eventos de la DNIT, forma real de `xContEv` con eventos, `dEntCont ` ante el validador del SIFEN, literal de ambiente de prueba (guía vs validación 1263), formato real de `dFecProc`, unidad de `dTpoProces`, endoso (`rGeVeEnd`).
