# ekuat-ia — Repositorio de Conocimiento SIFEN para IA

Base de conocimiento técnica del **SIFEN** (Sistema Integrado de Facturación Electrónica Nacional de Paraguay), estructurada para consumo por modelos de lenguaje (LLMs).

> Versión del Manual Técnico: **v150** | Notas Técnicas: **NT-001 al NT-027** (hasta marzo 2026) | XSD de producción re-verificados el **03/10/2026**
>
> **Agentes de IA:** leer primero [AGENTS.md](./AGENTS.md) (orden de autoridad, archivos autoritativos por tema, reglas de cita y prohibiciones).

## Estructura

| Carpeta | Contenido |
|---|---|
| [00-fuentes](./00-fuentes/) | Documentos fuente originales (PDFs, XSD, XML) |
| [01-conceptos](./01-conceptos/) | Conceptos fundamentales, glosario y flujos |
| [02-documentos-electronicos](./02-documentos-electronicos/) | Descripción por tipo de documento electrónico |
| [03-estructura-xml](./03-estructura-xml/) | Anatomía del XML, campos y reglas de validación |
| [04-schemas-xsd](./04-schemas-xsd/) | Esquemas XSD con documentación explicativa y [divergencias MT vs XSD de producción](./04-schemas-xsd/xsd-produccion-vs-manual.md) |
| [05-api-sifen](./05-api-sifen/) | Web services, endpoints y autenticación |
| [06-ejemplos](./06-ejemplos/) | Ejemplos XML anotados por caso de uso |
| [07-codigos-referencia](./07-codigos-referencia/) | Tablas de códigos y enumeraciones oficiales |
| [08-errores-y-respuestas](./08-errores-y-respuestas/) | Códigos de error y respuestas del sistema |
| [09-notas-tecnicas](./09-notas-tecnicas/) | Notas Técnicas NT-001 al NT-027 (cambios al MT) |
| [10-guias](./10-guias/) | Guía de pruebas y mejores prácticas |

## Fuente oficial

Documentación producida por la **Dirección Nacional de Ingresos Tributarios (DNIT)** de Paraguay.

### Fuente de verdad y orden de autoridad

Cuando dos fuentes difieren gana la de arriba y la divergencia se documenta en [04-schemas-xsd/xsd-produccion-vs-manual.md](./04-schemas-xsd/xsd-produccion-vs-manual.md); nunca se "promedia":

1. **XSD de producción** publicados en `https://ekuatia.set.gov.py/sifen/xsd/` (copias en [00-fuentes/xsd/](./00-fuentes/xsd/), md5 en `CHECKSUMS.md5`; re-verificados sin cambios el 03/10/2026). Son los esquemas contra los que el SIFEN valida realmente; los literales se comparan byte a byte.
2. **Manual Técnico v150, secciones 12.x** (códigos y validaciones), tal como están volcadas en [08-errores-y-respuestas/](./08-errores-y-respuestas/).
3. **Guías oficiales de la DNIT** en [10-guias/](./10-guias/).
4. **Notas Técnicas** NT-001 a NT-027 en [09-notas-tecnicas/](./09-notas-tecnicas/).
5. El resto del MT v150 y los demás archivos del repositorio.

> **⚠️ El Manual Técnico v150 (PDF) está desactualizado** en varios puntos respecto de los XSD (literales de `dDesAfecIVA`, tipos de documento C002, `Constancia Electrónica`, `dDomFisc`/`dDirChof` obligatorios, etc.) y tiene inconsistencias internas (0421/0422 en la consulta por CDC). Todo está registrado en [xsd-produccion-vs-manual.md](./04-schemas-xsd/xsd-produccion-vs-manual.md).

> **⚠️ Aviso sobre 05-api-sifen (03/10/2026):** los archivos de [05-api-sifen/](./05-api-sifen/) fueron **reescritos** desde el MT cap. 9, los XSD y lo homologado contra `sifen-test`. Las versiones anteriores describían estructuras y códigos inexistentes (`gResProcDE`, `gDetMotErr`, 0302/0304/0306, `xDELote`, `dNumLote`, `gConsDe`, `dEstDE`, 0418, `gConsDatRec`, 0700-0708, `recepcion-evento.wsdl`, etc.). Si un agente o un clon antiguo todavía los recuerda, **no son válidos**. Lo que no pudo confirmarse contra una respuesta real está marcado `[PENDIENTE DE VERIFICACIÓN]`.

### 🎯 Objetivo

Este repositorio está diseñado para ser utilizado como contexto en sistemas RAG (Retrieval-Augmented Generation) o como base de conocimiento directa para modelos de IA que asistan en integraciones con el SIFEN. La idea es reducir errores y ambigüedades al integrar con SIFEN, permitiendo que tanto desarrolladores como asistentes de IA trabajen con información consistente, validada y lista para usar.

## 🤖 Uso con asistentes de IA (Cursor, Copilot, Claude)

Este repositorio está optimizado para ser utilizado como referencia por asistentes de programación basados en IA.

Para obtener mejores resultados, se recomienda integrarlo directamente en el entorno de desarrollo.

---

### 📦 Opción 1: Clonar dentro de tu proyecto (recomendado)

La forma más efectiva es incluir este repositorio dentro de tu proyecto:

```bash
git clone https://github.com/abiliomp/ekuat-ia docs/sifen-ai
```

O como submódulo:

```bash
git submodule add https://github.com/abiliomp/ekuat-ia docs/sifen-ai
```

Esto permite que herramientas como Cursor indexen automáticamente la documentación y la utilicen como contexto durante la generación de código.

---

### 🧠 Opción 2: Configurar reglas en Cursor

Si utilizas Cursor, puedes guiar el comportamiento de la IA creando el archivo:

```
.cursor/rules/sifen.md
```

Con el siguiente contenido:

```md
When working with SIFEN (Paraguay electronic invoicing):

- Use the documentation in /docs/sifen-ai as the primary source of truth
- Prefer existing XML and JSON examples over generating new structures
- Follow SIFEN specifications strictly (avoid inventing fields)
- Use guides and examples from this repository for end-to-end flows
```

---

### 💬 Opción 3: Prompt inicial (alternativa simple)

También puedes indicar manualmente a la IA:

```
Use the SIFEN documentation located in /docs/sifen-ai as the main reference.
```




