# XSD de Producción vs Manual Técnico v150 — Divergencias Confirmadas

> **Fuente de verdad:** XSD publicados en `https://ekuatia.set.gov.py/sifen/xsd/` (descargados y verificados el **11/06/2026**, copias en [`00-fuentes/xsd/`](../00-fuentes/xsd/)).
>
> **Regla de oro:** cuando el Manual Técnico (MT v150 + NTs) y el XSD de producción difieren, **gana el XSD**: es el esquema contra el que SIFEN valida efectivamente cada documento recibido. Las enumeraciones de cadenas son **exactas, carácter por carácter** — un espacio o una tilde de diferencia produce el rechazo *"El valor X del elemento: Y es invalido"*.

## Archivos XSD realmente publicados en producción

A diferencia del listado de 22 "Schema XML N°" del MT, los archivos publicados son pocos y encadenados por `xs:include`:

```
siRecepDE_v150.xsd          (wrapper de 395 bytes, define <rDE>)
└── DE_v150.xsd             (estructura completa del DE)
    ├── DE_Types_v150.xsd   (tipos y enumeraciones: tdDesAfecIVA, tiTiDE, etc.)
    ├── Paises_v100.xsd     (paisType: 250 códigos de país)
    ├── Departamentos_v141.xsd (tDepartamentos/tDesDepartamento: 20 departamentos)
    ├── Monedas_v150.xsd    (cMondT: 200 códigos ISO 4217)
    └── Unidades_Medida_v141.xsd (tcUniMed/tdDesUniMed — incluye los códigos 111-140 de NT-023)

siRecepEvento_v150.xsd      (wrapper, define <gGroupGesEve>)
└── Evento_v150.xsd         (estructura de TODOS los eventos en un solo archivo)
    └── Evento_Types_v150.xsd
        ├── Paises_v100.xsd
        ├── Departamentos_v141.xsd
        └── DE_Types_v150.xsd
```

> **No existen** archivos separados por evento (`GEC_v150.xsd`, `GENFE_v150.xsd`, etc.) en el servidor: esa numeración es solo documental (del MT). Todos los eventos viven en `Evento_v150.xsd` como `complexType` (`trGeVeCan`, `trGeVeInu`, `trGeVeNotRec`, `trGeVeConf`, `trGeVeDisconf`, `trGeVeDescon`, `trGEveNom`, `trGeVeTr`, etc.).

---

## Divergencias y precisiones confirmadas (verificación junio 2026)

### 1. E732 `dDesAfecIVA` — enumeración cerrada (la causa de rechazo más común)

| E731 | Literal EXACTO exigido por el XSD | Nota |
|------|-----------------------------------|------|
| 1 | `Gravado IVA` | |
| 2 | `Exonerado (Art. 100 - Ley 6380/2019)` | El MT v150 original decía "Exonerado (Art. 83- Ley 125/91)"; fue actualizado por **NT-010** (Tabla 6). El XSD solo acepta el literal nuevo. |
| 3 | `Exento` | |
| 4 | `Gravado parcial (Grav- Exento)` | **Espacio después del guion** — error tipográfico del XSD oficial que debe reproducirse tal cual. |

### 1.b A005 `dSisFact` — campo obligatorio (confusión frecuente)

- El XSD de producción define `dSisFact` como **elemento obligatorio** del `<DE>`, ubicado **entre `dFecFirma` y `gOpeDE`**, con **único valor aceptado `1`** (`xs:positiveInteger`, `maxInclusive=1`).
- La **NT-010** eliminó solamente el **valor 2** ("SIFEN solución gratuita") — **no el campo**. Omitir `dSisFact` produce el error de esquema *"Element 'gOpeDE': This element is not expected. Expected is ( dSisFact )"*.

### 1.c E737 `dBasExe` — hijo obligatorio de `gCamIVA`

- En el XSD de producción, la secuencia de `gCamIVA` (E730) es: `iAfecIVA`, `dDesAfecIVA`, `dPropIVA`, `dTasaIVA`, `dBasGravIVA`, `dLiqIVAItem`, **`dBasExe`** — y `dBasExe` (agregado por NT-013) **no tiene `minOccurs="0"`**: debe informarse siempre (con `0` cuando no hay base exenta).
- Omitirlo produce *"Element 'gCamIVA': Missing child element(s). Expected is ( dBasExe )"*.

### 1.d RUC — sin ceros a la izquierda

- Patrón de `tRuc` (emisor y receptor): `[1-9][0-9]*[0-9A-D]?` con longitud 3–8 — **no admite ceros a la izquierda** y admite que el último carácter sea una letra A–D.
- Los RUC de prueba `00000001`/`00000002` que aparecen en los ejemplos del MT **no pasan** el XSD vigente.

### 2. C002 `iTiDE` — tipos de documento aceptados

- Patrón del XSD (`tiTiDE`): **`1|[4-7]|9|10`**.
- Los códigos **2 (FEE), 3 (FEI) y 8 (CRE)** están **comentados** en el XSD: serían rechazados por el esquema aunque el MT los liste como "futuros".
- Existen códigos **9 = `Boleta de venta electrónica`** y **10 = `Boleta resimple electrónica`** (régimen RESIMPLE / e-kuatia'i), **no documentados** en el MT v150 ni en las NT 001–027.

### 3. D014 `dDesTImp` — tipo de impuesto

- Literales exactos: `IVA`, `ISC`, `Renta`, `Ninguno`, `IVA - Renta` (código 5 con **guion simple ASCII rodeado de espacios**, no guion largo).
- El XSD incluye el comentario *"Cambio temporal, solo se aceptará IVA"* junto a `tiTImp` (D013): en la práctica, usar D013=1.

### 4. D012 `dDesTipTra` — tipo de transacción

- Código 3: el literal exacto es **`Mixto (Venta de mercadería y servicios)`** (no solo "Mixto").
- El resto coincide con la tabla del MT (1–13), incluyendo `Venta de crédito fiscal` (12) y `Muestras médicas (Art. 3 RG 24/2014)` (13).

### 5. E502 `dDesMotEmiNR` — motivos de traslado (NRE)

Enumeración + texto libre (5–60 caracteres, para 99=Otro). Literales con diferencias sutiles respecto a redacciones habituales:

- Código 1: `Traslado por ventas` (**plural**)
- Código 9: `Traslado de bienes para reparación` (**"para"**, no "por")
- Código 11: `Exhibición o Demostración` (**D mayúscula**)
- Código 5 es `Importación` — algunas tablas derivadas del MT lo omiten.

### 6. E772 `dDesTipOpVN` — venta de vehículos

- Código 2: `Venta al Consumidor final` (**C mayúscula**).

### 7. `dDesCatISC` — categorías ISC

- Código 1 **sin espacios**: `SECCION I-(Cigarrillos,Tabacos,Esencias y Otros derivados del Tabaco)`.
- Códigos 2–5 **con espacios**: `SECCION II - (Bebidas con y sin alcohol)`, etc.

### 8. Tipos con unión (enumeración + texto libre)

Estos campos de descripción aceptan los literales enumerados **o** texto libre (necesario cuando el código es 9/99="Otro"):

| Campo | Tipo XSD | Texto libre permitido |
|-------|----------|-----------------------|
| E012 `dDesIndPres` | `tdDesIndPres` | 10–30 caracteres |
| D209 `dDTipIDRec` | `tdDtipDocRec` | 9–41 caracteres |
| D141a desc. responsable | `tdDTipIDRespDE` | 9–41 caracteres |
| E607 `dDesTiPag` | `tdDesTiPag` | 4–30 caracteres |
| Denominación de tarjeta (grupo E7.1.1) | `tdDesDenTarj` | 4–20 caracteres |
| E502 motivo traslado | `tdDMotivTras` | 5–60 caracteres |
| E504 responsable NR | `tdDesRespEmiNR` | 20–36 caracteres |
| Tipo de combustible (sector automotores) | `tdDesTipCom` | 3–20 caracteres |

### 9. Patrones numéricos útiles del XSD

| Tipo | Patrón | Significado |
|------|--------|-------------|
| `tiTiDE` (C002) | `1\|[4-7]\|9\|10` | Tipos de DE aceptados |
| `tiIndPres` (E011) | `[1-6]\|9` | Indicador de presencia |
| `tiTipDocRec` (D208) | `[1-6]\|9` | Doc. identidad receptor |
| `tiTipIDRespDE` | `[1-4]\|9` | Doc. identidad responsable |
| `tiMotEmi` (E401) | `[1-8]` | Motivos NCE/NDE |
| `tCDC` | `[0-9]{2}([0-9]{7}[0-9A-D])[0-9]{34}` | CDC: 44 caracteres; la posición del DV del RUC admite A–D |
| `tRuc` | `[1-9][0-9]*[0-9A-D]?` (3–8) | El RUC puede terminar en letra A–D |
| `tdNumDoc` | `[0-9]{7}` exactos | Número de documento: 7 dígitos con ceros a la izquierda |
| `tVerFor` (eventos) | `141\|150` | Versiones de formato aceptadas en eventos |

### 10. XSD de eventos — contenido no documentado en el MT

`Evento_v150.xsd` / `Evento_Types_v150.xsd` incluyen, además de los eventos documentados (cancelación, inutilización, notificación, conformidad, disconformidad, desconocimiento, nominación, transporte):

- **Eventos del emisor** adicionales: retención aceptada/anulada (`trGeVeRetAce`, `trGeVeRetAnu`), CCFF (`trGeVeCCFF`), anticipo/remisión (`rGeVeAnt`, `rGeVeRem`), **endoso** (`trGeVeEnd`, tipos 1=En Venta, 2=En Administración).
- **Eventos de la SET/DNIT** (`tgGroupEvtSet`): bloqueo por omisión/inconsistencias (`trGeVeOA`), procesos de control (`trGeVePC`), **impugnación** (`trGeVeImp`) y detención/multas (`trGeVeDet`), cada uno con su enumeración de motivos.
- `tdTiGDE` (tipo de evento): 1=Cancelación, 2=Inutilización, 3=Endoso, 10=Acuse del DE, 11=Conformidad, 12=Disconformidad, 13=Desconocimiento.
- `tiTiOpeEv` (tipo de operación en nominación): patrón `[1-2]|[4]` (B2B, B2C, B2F — el B2G no aplica).
- `tiTiDEEv` (tipo de DTE en eventos): 1–9, donde 9=Boleta de Venta Electrónica.
- **NT-027:** el campo `iTipIDRec` del evento de nominación usa el tipo compartido `tiTipDocRec` (`[1-6]|9`), coherente con el cambio de código 5→6 para la Tarjeta Diplomática.

### 11. Listas cerradas de códigos auxiliares

- **Monedas** (`Monedas_v150.xsd`): 200 códigos ISO 4217 — lista cerrada, no "cualquier código ISO".
- **Países** (`Paises_v100.xsd`): 250 códigos ISO 3166-1 alpha-3 (incluye el código especial `NN`).
- **Unidades de medida** (`Unidades_Medida_v141.xsd`): incluye las 30 unidades nuevas de NT-023 (códigos 111–140).
- **Departamentos** (`Departamentos_v141.xsd`): 20 códigos/descripciones (incluye `CHACO` y `NUEVA ASUNCION`).

---

## Recomendación práctica

1. **Validar localmente** el XML contra los XSD de `00-fuentes/xsd/` antes de enviar a SIFEN (por ejemplo con `xmllint --schema siRecepDE_v150.xsd`).
2. Para cualquier campo `dDes*` que acompañe a un código, copiar el literal **desde el XSD**, nunca desde el PDF del MT.
3. Re-descargar los XSD periódicamente: la SET/DNIT incorpora cambios al XSD que no siempre se reflejan en una reedición del MT (caso `dDesAfecIVA`, actualizado por NT-010 pero nunca en el PDF base) e incluso elementos sin NT alguna (caso boletas, códigos 9 y 10 de C002).
