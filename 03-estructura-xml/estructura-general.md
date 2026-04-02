> **Fuente:** Manual Técnico SIFEN v150, secciones 7.2, 7.2.1, 7.2.2, 7.2.3, 7.2.4 y 10.4

> **Nota:** Este documento refleja el MT v150 con cambios del historial de versiones marcados.

# Estructura General del XML de un Documento Electrónico

---

## 1. Estándar del Formato XML

El formato de documentos y protocolos de servicios utiliza el lenguaje XML. Cada archivo XML sigue un estándar denominado "Schema XML" (archivo `.xsd`) que establece qué elementos contendrá el documento, su organización, atributos y tipos.

### 1.1 Estándar de Codificación

**[MODIFICADO]** La especificación de los documentos XML es el estándar **v150**, con codificación de caracteres **UTF-8**. Todos los documentos deben iniciar con la declaración:

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

Cada archivo XML debe poseer **solo una declaración**. Para envíos de lotes, la estructura completa del archivo debe contener solo una declaración.

Referencia: http://www.w3.org/TR/REC-xml

---

## 2. Namespace

El "Espacio de Nombres" XML se declara mediante el atributo `xmlns` en el elemento raíz. El namespace de SIFEN es:

```
http://ekuatia.set.gov.py/sifen/xsd
```

### Ejemplo de namespace para un DE:

```xml
<rDE
    xmlns="http://ekuatia.set.gov.py/sifen/xsd"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://ekuatia.set.gov.py/sifen/xsd siRecepDE_v150.xsd">
```

### Namespace para Eventos:

```xml
<rEnviEventoDe
    xmlns="http://ekuatia.set.gov.py/sifen/xsd"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
```

### Restricciones de namespace:
- **[MODIFICADO]** No se pueden utilizar namespaces distintos a los definidos en el MT.
- **[MODIFICADO]** No se pueden utilizar **prefijos de namespace**.
- Cada documento XML tiene su namespace individual en su elemento raíz.

### Particularidad de la firma digital
La declaración del namespace de la firma digital debe realizarse en la etiqueta `<Signature>`:

```xml
<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
```

### Particularidad del envío de lote
**[MODIFICADO]** En el caso de envío de lote, cada DE debe contener la declaración de su namespace individual.

---

## 3. Grupos de Campos del Documento Electrónico

El Schema XML 18 (`DE_v150.xsd`) define la estructura completa del DE. Los campos están organizados en los siguientes grupos:

| Grupo | Rango de IDs | Descripción |
|-------|-------------|-------------|
| **AA** | AA001–AA009 | Campos que identifican el formato electrónico XML |
| **A** | A001–A099 | Campos firmados del Documento Electrónico |
| **B** | B001–B099 | Campos inherentes a la operación de Documentos Electrónicos |
| **C** | C001–C099 | Campos de datos del Timbrado |
| **D** | D001–D299 | Campos Generales del Documento Electrónico |
| **D1** | D010–D099 | Campos inherentes a la operación comercial |
| **D2** | **[MODIFICADO]** D100–D129 | Campos que identifican al emisor del DE |
| **[NUEVO en v150] D2.1** | D130–D139 | Campos que describen la actividad económica del emisor |
| **D3** | D200–D299 | Campos que identifican al receptor del DE |
| **E** | E001–E009 | Campos específicos por tipo de Documento Electrónico |
| **E1** | E010–E099 | Campos de la Factura Electrónica (FE) |
| **E1.1** | E020–E029 | Campos de informaciones de Compras Públicas |
| ~~**E2**~~ | ~~E100–E199~~ | ~~Campos de la Factura Electrónica de Exportación FEE~~ |
| ~~**E3**~~ | ~~E200–E299~~ | ~~Campos de la Factura Electrónica de Importación FEI~~ |
| **E4** | **[MODIFICADO]** E300–E399 | Campos de la Autofactura Electrónica (AFE) |
| **E5** | E400–E499 | Campos de la Nota de Crédito/Débito Electrónica (NCE-NDE) |
| **E6** | E500–E599 | Campos de la Nota de Remisión Electrónica (NRE) |
| **E7** | E600–E699 | Campos que describen la condición de la operación |
| **E7.1** | **[MODIFICADO]** E605–E619 | Campos de la forma de pago al contado o del monto de entrega inicial |
| **E7.1.1** | E620–E629 | Campos del pago con tarjeta de crédito/débito |
| **E7.1.2** | E630–E639 | Campos del pago con cheque |
| **E7.2** | E640–E649 | Campos de la operación a crédito |
| **E7.2.1** | E650–E659 | Campos de las cuotas |
| **E8** | E700–E899 | Campos que describen los ítems de la operación |
| **E8.1** | **[MODIFICADO]** E720–E729 | Campos del precio, tipo de cambio y valor total por ítem |
| **[NUEVO en v150] E8.1.1** | EA001–EA050 | Campos de descuentos, anticipos y valor total por ítem |
| **E8.2** | E730–E739 | Campos del IVA de la operación por ítem |
| **E8.3** | **[MODIFICADO]** E740–E749 | Campos del ISC de la operación por ítem (futuro) |
| **E8.4** | **[MODIFICADO]** E750–E760 | Grupo de rastreo de la mercadería |
| **E8.5** | **[MODIFICADO]** E770–E789 | Sector de automotores nuevos y usados |
| **E9** | **[MODIFICADO]** E790–E899 | Campos complementarios comerciales de uso específico |
| **E9.2** | **[MODIFICADO]** E791–E799 | Sector Energía Eléctrica |
| **E9.3** | **[MODIFICADO]** E800–E809 | Sector de Seguros |
| **[NUEVO en v150] E9.3.1** | EA790–EA799 | Póliza de seguros |
| **E9.4** | **[MODIFICADO]** E810–E819 | Sector de Supermercados |
| **E9.5** | **[MODIFICADO]** E820–E829 | Datos adicionales de uso comercial |
| **E10** | E900–E999 | Campos del transporte de las mercaderías |
| **E10.1** | E920–E939 | Campos del local de salida de las mercaderías |
| **E10.2** | E940–E959 | Campos del local de entrega de las mercaderías |
| **E10.3** | E960–E979 | Campos del vehículo de traslado |
| **E10.4** | E980–E999 | Campos del transportista |
| **F** | F001–F099 | Campos de subtotales y totales de la transacción |
| **G** | **[MODIFICADO]** G001–G049 | Campos complementarios comerciales de uso general |
| **[NUEVO en v150] G1** | G050–G099 | Campos generales de la carga |
| **H** | H001–H049 | Campos que identifican al documento asociado |
| **I** | I001–I049 | Información de la Firma Digital del DTE |
| **J** | J001–J049 | Campos fuera de la Firma Digital |

> ⚠️ **ELIMINADO:** Los grupos E2 (Factura de Exportación) y E3 (Factura de Importación) fueron removidos de la implementación activa.

---

## 4. Convenciones de Tablas de Formato

### Tabla A — Convenciones Utilizadas en las Tablas de Definición de los Formatos XML

| Título | Descripción |
|--------|-------------|
| **Grupo** | Conjunto de campos |
| **ID** | Identificación del campo para fines de referencia |
| **Campo** | Nombre del campo. La primera letra indica: `c`=código de tabla cap. 16; `i`=código en columna Observaciones; `d`=campo común; `g`=grupo; `r`=raíz XML |
| **Descripción** | Descripción del campo y su significado |
| **Nodo Padre** | ID del campo de grupo que contiene este campo (campo padre) |
| **Tipo de Dato** | Tipo de dato (ver Tabla B) |
| **Longitud** | Tamaño del campo (ver Tabla C) |
| **Ocurrencia** | En formato m-n: m=mínimo, n=máximo de veces que el campo debe/puede aparecer |
| **Observaciones** | Observaciones importantes: listas de valores posibles, validaciones, condiciones de obligatoriedad |
| **Versión** | Versión en que fue introducido o modificado por última vez |

### Tabla B — Tipos de Datos

| Tipo | Descripción |
|------|-------------|
| **XML** | Documento XML descripto en un schema |
| **G** | Grupo de elementos y/o grupos de elementos |
| **CG** | "Choice Group" — elemento que excluye la ocurrencia de otro Choice Group con el mismo padre |
| **CE** | "Choice Element" — elemento que excluye la ocurrencia de otro Choice Element con el mismo padre. Ej.: "CEA" = Choice Element alfanumérico |
| **A** | Alfanumérico |
| **N** | Numérico (ver formatos en Tabla C) |
| **F** | Fecha: `AAAA-MM-DDThh:mm:ss` o `AAAA-MM-DD` |
| **B** | Binario en Base64 (para envío de lote) |

### Tabla C — Tamaños de Campos

| Notación | Descripción | Ejemplo |
|----------|-------------|---------|
| **X** | Tamaño exacto | `2` |
| **x-y** | Tamaño mínimo x, máximo y | `0-10` |
| **Xpn** | Tamaño exacto x, con n cifras decimales exactas | `22p4` |
| **xp(n-m)** | Tamaño exacto x, con decimales entre n y m | `22p(0-7)` |
| **(x-y)p(n-m)** | Tamaño mínimo x, máximo y, con decimales entre n y m | `1-11p(0-6)` |
| **Valores separados por comas** | Tamaño exacto de una de las opciones listadas | `1, 3, 5, 8` |

> **Nota:** El punto (`.`) se utiliza como separador de decimales en todos los campos numéricos del XML.
>
> En campos con tamaño exacto, los espacios no utilizados deben rellenarse con ceros no significativos (a la izquierda del campo).

---

## 5. Buenas Prácticas en la Generación del Archivo XML

Al momento de generar los DE, **NO** incorporar:

- Espacios en blanco al inicio o al final de campos numéricos y alfanuméricos.
- Comentarios, anotaciones y documentaciones (etiquetas `annotation` y `documentation`).
- Caracteres de formato: line-feed, carriage return, tab, espacios entre etiquetas.
- Prefijos en el namespace de las etiquetas.
- Etiquetas de campos que no contengan valor (ceros en numéricos, vacíos en alfanuméricos). **Excepción:** campos identificados como obligatorios.
- **[NUEVO en v150]** No utilizar valores negativos.
- Nombres de campos distintos a los especificados en el MT (son sensibles a mayúsculas/minúsculas). Ejemplo: `gOpeDE` es diferente a `GopeDE`, `gopede`, etc.

---

## 6. Esquema de la Estructura XML del DE

```
<rDE>                           ← Grupo AA (elemento raíz)
  <dVerFor>150</dVerFor>        ← AA002 (versión del formato)
  <DE Id="[CDC 44 dígitos]">   ← Grupo A (campos firmados)
    <gOpeDE>...</gOpeDE>        ← Grupo B (operación DE)
    <gTimb>...</gTimb>          ← Grupo C (timbrado)
    <gDatGralOpe>               ← Grupo D (datos generales)
      <gOpeCom>...</gOpeCom>    ← Grupo D1 (operación comercial)
      <gEmis>...</gEmis>        ← Grupo D2 (emisor)
      <gDatRec>...</gDatRec>    ← Grupo D3 (receptor)
    </gDatGralOpe>
    <gDtipDE>...</gDtipDE>      ← Grupo E (específico por tipo DE)
    <gTotSub>...</gTotSub>      ← Grupo F (subtotales y totales)
    <gCamGen>...</gCamGen>      ← Grupo G (complementarios generales)
    <gCamDEAsoc>...</gCamDEAsoc> ← Grupo H (documento asociado)
  </DE>
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    ...                         ← Firma digital (Schema XML 1)
  </Signature>
</rDE>
```
