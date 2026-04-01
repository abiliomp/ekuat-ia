# Estructura General del XML de un Documento Electrónico

> **Fuente:** Manual Técnico SIFEN v150, secciones 7.2 y 10.4

## Declaración XML

Todo DE comienza con la siguiente declaración:

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

- Versión: 1.0
- Codificación: **UTF-8** (obligatorio)
- Cada archivo XML debe poseer **solo una** declaración.

## Namespace (Espacio de Nombres)

El namespace se declara en el elemento raíz `<rDE>`:

```xml
<rDE
  xmlns="http://ekuatia.set.gov.py/sifen/xsd"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://ekuatia.set.gov.py/sifen/xsd siRecepDE_v150.xsd">
```

### Namespace para Eventos

```xml
<rEnviEventoDe
  xmlns="http://ekuatia.set.gov.py/sifen/xsd"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
```

### Reglas de Namespace

- Solo se puede utilizar el namespace definido en el Manual Técnico.
- **No** se pueden utilizar prefijos de namespace.
- La firma digital usa su propio namespace declarado en `<Signature>`:
  ```xml
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
  ```

### Namespace en envío de lotes

En el envío de lotes, **cada DE** debe contener la declaración de su namespace individual.

## Elemento Raíz

El elemento raíz del DE es `<rDE>` (campo AA001). La versión del formato se informa en el campo `<dVerFor>` (AA002):

```xml
<rDE xmlns="http://ekuatia.set.gov.py/sifen/xsd" ...>
  <dVerFor>150</dVerFor>
  <DE Id="[CDC-44-DIGITOS]">
    ...
  </DE>
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    ...
  </Signature>
  <gCamFuFD>
    <dCarQR>[URL_QR]</dCarQR>
  </gCamFuFD>
</rDE>
```

## Grupos de Campos

La estructura interna del elemento `<DE>` se organiza en grupos:

| Grupo | Rango IDs | Descripción |
|-------|-----------|-------------|
| **AA** | AA001-AA009 | Campos que identifican el formato electrónico XML |
| **A** | A001-A099 | Campos firmados del Documento Electrónico |
| **B** | B001-B099 | Campos inherentes a la operación de DE |
| **C** | C001-C099 | Campos de datos del Timbrado |
| **D** | D001-D299 | Campos Generales del DE |
| **D1** | D010-D099 | Campos inherentes a la operación comercial |
| **D1.1** | D030-D040 | Campos que identifican las obligaciones afectadas (NT-018) |
| **D2** | D100-D129 | Campos que identifican al emisor |
| **D2.1** | D130-D139 | Campos de actividad económica del emisor |
| **D2.2** | D140-D160 | Campos del responsable de la generación del DE |
| **D3** | D200-D299 | Campos que identifican al receptor |
| **E** | E001-E009 | Campos específicos por tipo de DE |
| **E1** | E010-E099 | Campos de la Factura Electrónica FE |
| **E1.1** | E020-E029 | Campos de Compras Públicas |
| **E2** | E100-E199 | Campos de la FE de Exportación (futuro) |
| **E3** | E200-E299 | Campos de la FE de Importación (futuro) |
| **E4** | E300-E399 | Campos de la Autofactura Electrónica AFE |
| **E5** | E400-E499 | Campos de la NCE y NDE |
| **E6** | E500-E599 | Campos de la Nota de Remisión Electrónica |
| **E7** | E600-E699 | Campos de condición de la operación |
| **E7.1** | E605-E619 | Forma de pago contado / entrega inicial |
| **E7.1.1** | E620-E629 | Pago con tarjeta crédito/débito |
| **E7.1.2** | E630-E639 | Pago con cheque |
| **E7.2** | E640-E649 | Operación a crédito |
| **E7.2.1** | E650-E659 | Campos de cuotas |
| **E8** | E700-E899 | Campos que describen los ítems |
| **E8.1** | E720-E729 | Precio, tipo de cambio y valor total por ítem |
| **E8.1.1** | EA001-EA050 | Descuentos, anticipos y valor total por ítem |
| **E8.2** | E730-E739 | IVA de la operación por ítem |
| **E8.3** | - | ISC por ítem (futuro) |
| **E8.4** | E750-E761 | Grupo de rastreo de la mercadería |
| **E8.5** | E770-E789 | Sector de automotores |
| **E9** | E790-E899 | Campos complementarios comerciales específicos |
| **E9.2** | E791-E799 | Sector Energía Eléctrica |
| **E9.3** | E800-E809 | Sector de Seguros |
| **E9.3.1** | EA790-EA799 | Póliza de seguros |
| **E9.4** | E810-E819 | Sector de Supermercados |
| **E9.5** | E820-E829 | Datos adicionales de uso comercial |
| **E10** | E900-E999 | Campos de transporte de mercaderías |
| **E10.1** | E920-E939 | Local de salida |
| **E10.2** | E940-E959 | Local de entrega |
| **E10.3** | E960-E979 | Vehículo de traslado |
| **E10.4** | E980-E999 | Transportista |
| **F** | F001-F099 | Subtotales y totales de la transacción |
| **G** | G001-G049 | Campos complementarios comerciales generales |
| **G1** | G050-G099 | Campos generales de la carga |
| **H** | H001-H049 | Campos del documento asociado |
| **I** | I001-I049 | Información de la Firma Digital del DTE |
| **J** | J001-J049 | Campos fuera de la Firma Digital |

## Convenciones de Tablas (Tabla A del MT)

| Columna | Descripción |
|---------|-------------|
| **Grupo** | Conjunto de campos |
| **ID** | Identificación del campo para referencia (ej: D011, E701) |
| **Campo** | Nombre del campo XML. Prefijos: c=código tabla, i=código observaciones, d=campo común, g=grupo, r=raíz |
| **Descripción** | Descripción y significado del campo |
| **Nodo Padre** | ID del campo padre en el árbol XML |
| **Tipo Dato** | Tipo de datos (A, N, F, G, XML, B, CG, CE) |
| **Longitud** | Tamaño del campo (ver Tabla C) |
| **Ocurrencia** | m-n (mínimo-máximo de veces) |
| **Observaciones** | Validaciones, tablas de valores, reglas |
| **Versión** | Versión en que fue introducido o modificado |

## Tipos de Datos (Tabla B)

| Tipo | Descripción |
|------|-------------|
| XML | Documento XML |
| G | Grupo de elementos |
| CG | Choice Group (excluye otro CG del mismo padre) |
| CE | Choice Element (excluye otro CE del mismo padre) |
| A | Alfanumérico |
| N | Numérico |
| F | Fecha: AAAA-MM-DDThh:mm:ss o AAAA-MM-DD |
| B | Binario en Base64 |

## Formatos de Longitud (Tabla C)

| Formato | Descripción |
|---------|-------------|
| `X` | Tamaño exacto del campo (ej: 2) |
| `x-y` | Tamaño mínimo x, máximo y (ej: 0-10) |
| `Xpn` | Exacto X con n cifras decimales exactas (ej: 22p4) |
| `xp(n-m)` | Exacto X con decimales entre n y m (ej: 22p(0-7)) |
| `(x-y)p(n-m)` | Variable con decimales variables (ej: 1-11p(0-6)) |

## Mejores Prácticas de Generación (Sección 7.2.4)

**NO incorporar:**
- Espacios en blanco al inicio o final de campos.
- Comentarios, anotaciones, etiquetas `annotation` y `documentation`.
- Caracteres de formato: line-feed, carriage return, tab, espacios entre etiquetas.
- Prefijos en el namespace de las etiquetas.
- Etiquetas de campos sin valor (excepto campos obligatorios).
- Valores negativos.

**Sensibilidad a mayúsculas/minúsculas:** Los nombres de campos son case-sensitive.
- Correcto: `gOpeDE`
- Incorrecto: `GopeDE`, `gopede`

**Separador decimal:** Usar punto (`.`) como separador decimal.
- Correcto: `1105.13`
- Incorrecto: `1.105,13`

## Schema XML Principal

El Schema XML del DE (versión 150):
- **Archivo:** `DE_v150.xsd` (Schema XML 18)
- **URL base:** `http://ekuatia.set.gov.py/sifen/xsd`
- **Paquete comprimido:** `PS_FE_150.zip`
