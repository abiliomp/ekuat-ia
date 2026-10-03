# XSD para validación local (copias modificadas, NO fieles)

> **Fuente:** generados con [`generar.py`](./generar.py) a partir de las copias fieles de [`00-fuentes/xsd/`](../../00-fuentes/xsd/) (producción, re-verificadas el 03/10/2026). Cambios registrados en [`CAMBIOS.md5`](./CAMBIOS.md5). Creado el 03/10/2026 por decisión del propietario del repo (ver [xsd-produccion-vs-manual.md](../xsd-produccion-vs-manual.md) §14).

## Para qué sirve

Validar un `rDE` o un sobre de eventos `gGroupGesEve` **sin red y antes de enviarlo al SIFEN**, con los mismos esquemas contra los que el SIFEN valida. Las copias fieles de `00-fuentes/xsd/` no sirven directamente para eso por dos motivos:

1. Sus `xs:include` apuntan a URLs absolutas (`https://ekuatia.set.gov.py/sifen/xsd/...`), así que libxml2 necesita red para compilar el esquema.
2. `DE_v150.xsd:327` declara el elemento `dEntCont ` **con un espacio final** (error del XSD oficial). Un nombre así es imposible en XML, y libxml2 rechaza el `dEntCont` correcto con *"This element is not expected. Expected is ( dEntCont  )"*: ninguna factura B2G con el grupo `gCompPub` (E020) puede validarse contra la copia fiel.

## Qué se cambió (y nada más)

| Cambio | Archivos | Detalle |
|--------|----------|---------|
| `schemaLocation` absolutos → relativos | `siRecepDE_v150.xsd`, `DE_v150.xsd`, `siRecepEvento_v150.xsd`, `Evento_v150.xsd` | `https://ekuatia.set.gov.py/sifen/xsd/X.xsd` → `X.xsd` |
| `dEntCont ` → `dEntCont` | `DE_v150.xsd` (línea 327) | Única corrección de contenido. Qué hace el validador del SIFEN con ese grupo sigue `[PENDIENTE DE VERIFICACIÓN]` |
| Sin cambios | `DE_Types_v150.xsd`, `Evento_Types_v150.xsd`, `Paises_v100.xsd`, `Departamentos_v141.xsd`, `Monedas_v150.xsd`, `Unidades_Medida_v141.xsd`, `xmldsig-core-schema.xsd` | md5 idéntico al de origen |

**No usar estas copias como fuente de verdad para literales ni para citar líneas**: para eso están las fieles. Estas son una herramienta de validación.

## Uso

```bash
php 04-schemas-xsd/validacion-local/validar.php documento.xml
```

Elige el XSD por la raíz del documento (`rDE` → `siRecepDE_v150.xsd`; `gGroupGesEve` → `siRecepEvento_v150.xsd`) e imprime cada error con su línea. Código de salida 0 si es válido. Con `--fiel` valida contra las copias de `00-fuentes/xsd/` (necesita red). Desde código PHP:

```php
$doc = new DOMDocument();
$doc->load($rutaXml);
$ok = $doc->schemaValidate(__DIR__ . '/04-schemas-xsd/validacion-local/siRecepDE_v150.xsd');
```

## Mantenimiento

Cada vez que cambie `00-fuentes/xsd/` (ver [AGENTS.md](../../AGENTS.md) §4), volver a ejecutar:

```bash
python 04-schemas-xsd/validacion-local/generar.py
```

El script falla a propósito si `dEntCont ` ya no aparece exactamente una vez en `DE_v150.xsd`: señal de que la DNIT corrigió el XSD y hay que actualizar esta nota y la §14 de xsd-produccion-vs-manual.md.

## Verificación realizada el 03/10/2026

| Documento | Copias fieles (con red) | Esta carpeta |
|-----------|-------------------------|--------------|
| FE B2G con `gCompPub` (`dEntCont`) generada por PKuatia en la evaluación del 02/10/2026 | INVÁLIDO: *Expected is ( dEntCont  )* | VÁLIDO |
| FE básica de la misma evaluación | VÁLIDO | VÁLIDO |

(Resultados reproducidos en esta sesión con PHP 8.3 / libxml2; ver el detalle en la salida del commit.)
