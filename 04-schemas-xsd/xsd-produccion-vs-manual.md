# XSD de Producción vs Manual Técnico v150 — Divergencias Confirmadas

> **Fuente de verdad:** XSD publicados en `https://ekuatia.set.gov.py/sifen/xsd/` (descargados el **11/06/2026**, copias en [`00-fuentes/xsd/`](../00-fuentes/xsd/)).
>
> **Última re-verificación: 03/10/2026.** Los 11 archivos se volvieron a descargar y resultaron **byte a byte idénticos** a las copias locales (md5 en [`00-fuentes/xsd/CHECKSUMS.md5`](../00-fuentes/xsd/CHECKSUMS.md5)); los 11 están bien formados y las dos cadenas de `xs:include` (`siRecepDE_v150.xsd` y `siRecepEvento_v150.xsd`) compilan con libxml2. Ver el [historial de verificaciones](#historial-de-verificaciones) al final.
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

- **Endoso** (`rGeVeEnd` / `trGeVeEnd`, `Evento_v150.xsd:231-262`; `tdTipEnd` 1=En Venta, 2=En Administración): es el único de estos eventos adicionales que está en `tgGroupEvt` y por lo tanto es **enviable**; el MT v150 lo lista como "futuro" (ver §17 y [05-api-sifen/eventos.md](../05-api-sifen/eventos.md)).
- **Eventos automáticos del emisor** (`tgGroupEvtEmi`, tipo huérfano): retención aceptada/anulada (`trGeVeRetAce`, `trGeVeRetAnu`), CCFF (`trGeVeCCFF`, `trGeDevCCFF`), anticipo/remisión (`rGeVeAnt`, `rGeVeRem`). No enviables; el SIFEN los devuelve al consultar un DTE.
- **Eventos de la SET/DNIT** (`tgGroupEvtSet`): bloqueo por omisión/inconsistencias (`trGeVeOA`), procesos de control (`trGeVePC`), **impugnación** (`trGeVeImp`) y detención/multas (`trGeVeDet`), cada uno con su enumeración de motivos.
- `tdTiGDE` (tipo de evento, `Evento_Types_v150.xsd:134-157`): 1=Cancelación, 2=Inutilización, 3=Endoso, 10=Acuse del DE, 11=Conformidad, 12=Disconformidad, 13=Desconocimiento. **Tipo huérfano**: ningún elemento lo usa (el campo GDE006 `dTiGDE` del MT no existe en `trEve`); el evento se identifica por el hijo elegido en `gGroupTiEvt` (ver §17).
- `tiTiOpeEv` (tipo de operación en nominación): patrón `[1-2]|[4]` (B2B, B2C, B2F — el B2G no aplica).
- `tiTiDEEv` (tipo de DTE en eventos): 1–9, donde 9=Boleta de Venta Electrónica.
- **NT-027:** el campo `iTipIDRec` del evento de nominación usa el tipo compartido `tiTipDocRec` (`[1-6]|9`), coherente con el cambio de código 5→6 para la Tarjeta Diplomática.

### 11. Listas cerradas de códigos auxiliares

- **Monedas** (`Monedas_v150.xsd`): 200 códigos ISO 4217 — lista cerrada, no "cualquier código ISO".
- **Países** (`Paises_v100.xsd`): 250 códigos ISO 3166-1 alpha-3 (incluye el código especial `NN`).
- **Unidades de medida** (`Unidades_Medida_v141.xsd`): incluye las 30 unidades nuevas de NT-023 (códigos 111–140).
- **Departamentos** (`Departamentos_v141.xsd`): 20 códigos/descripciones (incluye `CHACO` y `NUEVA ASUNCION`).

### 12. H003 `dDesTipDocAso` — `Constancia Electrónica` con E mayúscula

- `DE_Types_v150.xsd:1831-1842` (`tdDesTipDocAso`): literales exactos `Electrónico`, `Impreso`, **`Constancia Electrónica`**. El comentario del código 3 de `tiTipDocAso` (`:1825`) lo escribe igual.
- El MT (H003) y la mayoría de las implementaciones lo escriben "Constancia electrónica" (e minúscula) → rechazo 0160 (*"El valor del elemento: dDesTipDocAso es invalido"*). Afecta a **toda Autofactura** (H002 = 3 es obligatorio en AFE, validación 2416) y a toda FE que referencie una constancia. Propagado a [tipos-documento.md](../07-codigos-referencia/tipos-documento.md).

### 13. E992 `dDomFisc` y E993 `dDirChof` — obligatorios en `gCamTrans` (NRE)

- `DE_v150.xsd:973` (`dDomFisc`, `minOccurs="1"`, `noEmptyString` 1-150) y `:986` (`dDirChof`, `tdDirec`, `minOccurs="1"`) dentro de `tgCamTrans` (`:951-995`). La NT-010 ya los marcó `[MODIFICADO]` 1-1 "obligatorio por RG N° 41/2014"; el MT base los mostraba condicionales y varias implementaciones los tratan como opcionales.
- En `tgCamTrans` también son obligatorios (sin `minOccurs="0"`) `iNatTrans` (`:959`), `dNomTrans` (`:960`), `dNumIDChof` (`:971`) y `dNomChof` (`:972`). Omitir `dDomFisc` produce *"Element 'gCamTrans': Missing child element(s). Expected is ( dDomFisc )"* y luego lo mismo con `dDirChof`. Propagado a [nota-remision-electronica.md](../02-documentos-electronicos/nota-remision-electronica.md).

### 14. E022 `dEntCont ` — nombre de elemento con espacio final (error del XSD oficial)

- `DE_v150.xsd:327`: `<xs:element name="dEntCont " type="tdEntCont" />` dentro de `tgCompPub` (`:321-334`, grupo E020 de compras públicas). Un nombre con espacio es imposible en un documento XML; libxml2 compila el esquema igual, pero rechaza el `dEntCont` correcto: *"Element 'dEntCont': This element is not expected. Expected is ( dEntCont  )"*.
- Consecuencia: las FE B2G con `gCompPub` **no se pueden validar localmente** contra el XSD tal cual. Para validar, usar una copia del XSD con el nombre corregido **fuera** de `00-fuentes/xsd/` (las copias de esta carpeta son fieles al original). Qué hace el validador del SIFEN con ese grupo: `[PENDIENTE DE VERIFICACIÓN]`.

### 15. `Unidades_Medida_v141.xsd` — códigos 111-140 (NT-023) documentados como "Descripción - ABREV"

- En `tcUniMed` (E709, `:12-341`) los códigos 111-140 llevan la documentación con sufijo de abreviatura: `Bovinas - 4A` (`:186`), `Curie - Ci` (`:191`), `Docena - DOC`, `Galones (US) (3,7843 LT) - GLL`, … `Peso Base - BW` (`:331`); los códigos 1-110 llevan solo la descripción.
- La enumeración de E710 `tdDesUniMed` (`:343-666`) contiene las **abreviaturas** como valores (`4A` `:517`, `Ci` `:522`, …, `BW` `:662`) con la descripción larga en `xs:documentation`: el literal que debe ir en `dDesUniMed` es la abreviatura (`4A`, `Ci`, `DOC`, `GLL`, …).
- Versiones anteriores del XSD (p. ej. la empaquetada en PKuatia hasta v0.1.5, md5 `25a38e63…`) no llevaban el sufijo; un parser que corte la cadena de documentación en el último " - " produce descripciones inválidas (`vinas`, `rrie`, `llar`). Comparar siempre contra la copia actual (md5 `381ec7c4…`, `CHECKSUMS.md5`). Propagado a [codigos-unidad-medida.md](../07-codigos-referencia/codigos-unidad-medida.md).

### 16. `Monedas_v150.xsd` — 15 `CodeName` de más de 20 caracteres frente a `tdDMoneTiPag` (3-20)

`tdDMoneTiPag` (`DE_Types_v150.xsd:884-895`: `noEmptyString`, 3-20 caracteres) es el tipo de D016 `dDesMoneOpe` (`DE_v150.xsd:209`), E651 `dDMoneCuo` (`:311`) y E609 `dDMoneTiPag` (`:1276`). El `CodeName` de `Monedas_v150.xsd` es `xs:documentation`, no enumeración, así que la descripción es texto libre de 3-20; estas 15 monedas no caben:

| Código (línea) | `CodeName` del XSD | Long. |
|----------------|--------------------|-------|
| ANG (`:48`) | Netherlands Antillian Guilder | 29 |
| BMD (`:139`) | Bermudian Dollar (customarily: Bermuda Dollar) | 46 |
| FKP (`:391`) | Falkland Islands Pound | 22 |
| KYD (`:608`) | Cayman Islands Dollar | 21 |
| MXV (`:797`) | Mexican Unidad de Inversion | 27 |
| SBD (`:965`) | Solomon Islands Dollar | 22 |
| TMT (`:1126`) | Turkmenistan New Manat | 22 |
| TTD (`:1147`) | Trinidad and Tobago Dollar | 26 |
| UYI (`:1203`) | Uruguay Peso en Unidades Indexadas(UI) | 38 |
| XCD (`:1287`) | East Carribean Dollar | 21 |
| XBA (`:1336`) | Bond Markets Unit European Composite Unit(EURCO) | 48 |
| XBB (`:1343`) | Bond Markets Unit European Monetary Unit(E.M.U.-6) | 50 |
| XBC (`:1350`) | Bond Markets Unit European Unit of Account 17 (E.U.A.-17) | 57 |
| XTS (`:1357`) | Codes specifically reserved for testing purposes | 48 |
| XXX (`:1364`) | The codes assigned for transactions where no currency is involved | 65 |

La descripción debe truncarse o adaptarse a ≤ 20 caracteres; qué literal acepta la validación 1206 ("Descripción de la moneda no corresponde al código") para estas monedas: `[PENDIENTE DE VERIFICACIÓN]`. Propagado a [codigos-moneda.md](../07-codigos-referencia/codigos-moneda.md).

### 17. `Evento_v150.xsd` — solo `tgGroupEvt` es alcanzable: 9 eventos enviables

- Cadena de inclusión desde la raíz: `gGroupGesEve` (`siRecepEvento_v150.xsd:9`) → `tgGroupGesEve` (`Evento_v150.xsd:561-565`, `rGesEve` 1-15) → `trGesEve` (`:546-557`: `rEve` + `ds:Signature`) → `trEve` (`:480-488`: `dFecFirma`, `dVerFor`, `gGroupTiEvt`, atributo `Id`) → **`tgGroupEvt`** (`:363-380`, `xs:choice`): `rGeVeCan`, `rGeVeInu`, `rGeVeNotRec`, `rGeVeConf`, `rGeVeDisconf`, `rGeVeDescon`, `rGeVeEnd`, `rGeVeTr`, `rGEveNom`.
- **Tipos huérfanos** (definidos pero no referenciados desde ningún elemento global): `tgGroupEvtRecep` (`:432-444`), `tgGroupEvtEmi` (`:446-462`), `tgGroupEvtSet` (`:464-476`), `trEveRecep`/`trEveEmi`/`trEveSet` (`:492-518`) y `trGesEveRecep`/`trGesEveEmi`/`trGesEveSet` (`:522-542`); presumiblemente son los contenedores de los eventos que el SIFEN devuelve en `xContEv` al consultar un DTE (`[PENDIENTE DE VERIFICACIÓN]`). También huérfanos: `trGeDeVTr` (`:192-229`, duplicado del evento de transporte con tipos incoherentes: fechas donde van textos) y `tdTiGDE` (`Evento_Types_v150.xsd:134-157`).
- `rGEveNom` figura tanto en `tgGroupEvt` como en `tgGroupEvtEmi`. Detalle en [05-api-sifen/eventos.md](../05-api-sifen/eventos.md).

### 18. `trGeVeRetAce` / `trGeVeRetAnu` exigen `dRuc` y `dMonRet`

- `Evento_v150.xsd:112-129` (`trGeVeRetAce`) y `:131-149` (`trGeVeRetAnu`): `dRuc` (`:120` / `:139`, `tRuc`) y `dMonRet` (`:127` / `:147`, `tMontoBase`) sin `minOccurs="0"`. Las tablas del MT (GER001-008 y GERA001-009 en [eventos-respuesta.md](../08-errores-y-respuestas/eventos-respuesta.md)) no los listan. Solo relevante para deserializar eventos devueltos por el SIFEN.

### 19. Fechas de los eventos: `fecHhmmss` (fecha y hora), salvo los eventos de la DNIT

- `rGeVeConf.dFecRecep` es `fecHhmmss` (`Evento_v150.xsd:76`; `DE_Types_v150.xsd:345-354`: `xs:dateTime`, `AAAA-MM-DDThh:mm:ss`). El MT la llama "fecha estimada de recepción" (GCO004, F 19): enviar solo la fecha produce rechazo de esquema.
- Todas las fechas de los eventos automáticos GEA también son `fecHhmmss`: `dFeEmiRet` (`:126`, `:145`), `dFecAnRet` (`:146`), `dFeAceTraCCFF` (`:160`), `dFeEmiSol`/`dFeEmiInf`/`dFeEmiRes` (`:186-188`).
- Los eventos de la DNIT usan `formatFecha` (`Evento_Types_v150.xsd:535-543`, `xs:date` `AAAA-MM-DD`): `dFechaOA` (`:311`), `dFechaPC` (`:326`), `dFechaImp` (`:341`), `dFechaDet` (`:356`).

### 20. `dTipIDRec`: `tiTipDoc` (`[1-4]`) en desconocimiento y endoso, `tiTipDocRec` (`[1-6]|9`) en notificación y nominación

| Evento | Campo | Tipo | Patrón | Línea |
|--------|-------|------|--------|-------|
| `rGeVeNotRec` | `dTipIDRec` | `tiTipDocRec` | `[1-6]\|9` | `Evento_v150.xsd:61` |
| `rGEveNom` | `iTipIDRec` | `tiTipDocRec` | `[1-6]\|9` | `:398` |
| `rGeVeDescon` | `dTipIDRec` | **`tiTipDoc`** | **`[1-4]`** | `:106` |
| `rGeVeEnd` | `dTipIDRec` | **`tiTipDoc`** | **`[1-4]`** | `:243` |

`tiTipDoc` (`DE_Types_v150.xsd:645-655`, "tipo de documento de identidad del vendedor") y `tiTipDocRec` (`:658-668`). El MT (GED009) describe para el desconocimiento la misma lista que para la notificación; por el XSD, el desconocimiento **no admite** 5 (innominado), 6 (Tarjeta Diplomática) ni 9 (otro).

### 21. `tdNroMatVeh` — longitud exacta 6 en el evento de transporte frente a máximo 7 en el DE

- `Evento_Types_v150.xsd:524-533` (`tdNroMatVeh`): `xs:length value="6"` (su `xs:documentation` dice por error "Marca del vehículo"); lo usa `rGeVeTr.dNroMatVeh` (`Evento_v150.xsd:299`; MT GET030 "A 6").
- En el DE, E965 `dNroMatVeh` (`DE_v150.xsd:1174-1184`) es `noEmptyString` con `maxLength 7`. Una matrícula de 7 caracteres aceptada en la NRE no puede informarse en el evento de actualización de transporte.

### 22. Confirmaciones (ya documentadas en secciones anteriores, verificadas el 03/10/2026)

- `tiTiOpeEv` `[1-2]|[4]` (`Evento_Types_v150.xsd:57-66`): §10; B2G (3) no es válido en la nominación.
- `tdDMotivTras` (`DE_Types_v150.xsd:1933-1965`): código 9 = `Traslado de bienes para reparación` (`:1953`), código 11 = `Exhibición o Demostración` (`:1955`): §5.
- `tdDtipDocRec` (`DE_Types_v150.xsd:699-725`): unión de la enumeración (6 literales, incluida `Tarjeta Diplomática de exoneración fiscal`) con texto libre de 9-41 caracteres: §8.

---

## Divergencias entre documentos oficiales (MT, guías de la DNIT, NT)

Casos en que dos fuentes oficiales se contradicen entre sí (no contra el XSD). Se registra la resolución adoptada y la fuente de cada versión.

### D1. Código de "CDC encontrado" en siConsDE: 0421 vs 0422 (resuelto el 03/10/2026)

| Fuente | Dice | Observación |
|--------|------|-------------|
| MT v150 §12.3.4.3 (PDF p. 158) | BL02 "CDC Encontrado" = **0421** | Sin marcas de color; no lista el caso "sin permiso" |
| MT v150 §9.4.2 Tabla G (PDF p. 52) | 0420 CDC inexistente; **0421 RUC Certificado sin permiso**; **0422 CDC encontrado** | Schema XML 10: `xContenDE` existe solo si `dCodRes` = 0422 |
| Guía de Mejores Prácticas (DNIT, 10/2024) §8 | **0422** "Existe como DTE, está aprobado"; respuesta real con `<dCodRes>0422</dCodRes>` | Documento posterior y con evidencia real |
| PKuatia (producción desde 2023; homologación 06/2026) | 0422 = encontrado, 0421 = sin permiso | Código operativo |

**Resolución:** 0422 = CDC encontrado; 0421 = RUC del certificado sin permiso; 0420 = inexistente/no aprobado. El 0421 de la tabla 12.3.4.3 se considera error de edición. Aplicado en [respuestas-ws.md](../08-errores-y-respuestas/respuestas-ws.md), [estructura-codigos.md](../08-errores-y-respuestas/estructura-codigos.md) y [05-api-sifen/consulta-estado.md](../05-api-sifen/consulta-estado.md).

### D2. Literal del nombre del emisor en el ambiente de pruebas (anotado el 03/10/2026)

| Fuente | Literal exigido | Dónde |
|--------|-----------------|-------|
| MT v150, campo D105 `dNomEmi` (PDF p. 69) y validación **1263** (PDF p. 165) | `DE generado en ambiente de prueba - sin valor comercial ni fiscal` | Solo en `dNomEmi`; prohibido en producción |
| Guía de Pruebas (DNIT, 02/2026), §2 "Set de datos" (PDF p. 4) | `DOCUMENTO ELECTRÓNICO SIN VALOR COMERCIAL NI FISCAL - GENERADO EN AMBIENTE DE PRUEBA` | En el nombre/razón social del emisor **y** en la descripción del primer ítem |
| Homologación PKuatia (`sifen-test`, 06/2026) | El literal del MT en `dNomEmi` fue **aprobado**; el ítem no llevaba ningún literal | — |

**Resolución provisional:** usar el literal de la validación 1263 del MT en `dNomEmi` (es el que el validador acepta hoy). El literal de la guía y la exigencia sobre el primer ítem quedan `[PENDIENTE DE VERIFICACIÓN]` hasta que la DNIT aclare o se pruebe en `sifen-test`. Anotado en [guia-de-pruebas.md](../10-guias/guia-de-pruebas.md) y [errores-validacion.md](../08-errores-y-respuestas/errores-validacion.md).

---

## Recomendación práctica

1. **Validar localmente** el XML contra los XSD de `00-fuentes/xsd/` antes de enviar a SIFEN (por ejemplo con `xmllint --schema siRecepDE_v150.xsd`).
2. Para cualquier campo `dDes*` que acompañe a un código, copiar el literal **desde el XSD**, nunca desde el PDF del MT.
3. Re-descargar los XSD periódicamente: la SET/DNIT incorpora cambios al XSD que no siempre se reflejan en una reedición del MT (caso `dDesAfecIVA`, actualizado por NT-010 pero nunca en el PDF base) e incluso elementos sin NT alguna (caso boletas, códigos 9 y 10 de C002).

---

## Historial de verificaciones

| Fecha | Resultado | Método |
|-------|-----------|--------|
| 11/06/2026 | Descarga inicial de los 11 XSD; divergencias con el MT documentadas en este archivo | Descarga directa desde `ekuatia.set.gov.py/sifen/xsd/` |
| 03/10/2026 | **Sin cambios**: md5 idéntico en los 11 archivos; bien formados; `schemaValidate` de libxml2 resuelve la cadena completa de `xs:include` | `curl` + `md5sum -c CHECKSUMS.md5` + PHP `DOMDocument::load`/`schemaValidate` |

### Cómo repetir la verificación

```bash
cd 00-fuentes/xsd
for f in siRecepDE_v150.xsd DE_v150.xsd DE_Types_v150.xsd siRecepEvento_v150.xsd Evento_v150.xsd Evento_Types_v150.xsd Paises_v100.xsd Departamentos_v141.xsd Monedas_v150.xsd Unidades_Medida_v141.xsd xmldsig-core-schema.xsd; do
  curl -sS -L -o "/tmp/$f" "https://ekuatia.set.gov.py/sifen/xsd/$f"
done
(cd /tmp && md5sum -c "$OLDPWD/CHECKSUMS.md5")
```

Si algún archivo difiere: reemplazar la copia local, regenerar `CHECKSUMS.md5`, hacer `diff` contra la versión anterior (git) y registrar cada cambio en este archivo con la fecha, propagando a `07-codigos-referencia/` lo que corresponda. Los `schemaLocation` de los `xs:include` apuntan a URLs absolutas de producción; para validar sin red hay que reescribirlos a rutas locales (`sed 's#https://ekuatia.set.gov.py/sifen/xsd/##g'`).

> **Prohibido** desde una sesión de documentación: llamar a los web services (`sifen.set.gov.py`, `sifen-test.set.gov.py`). Solo se descargan los XSD estáticos.
