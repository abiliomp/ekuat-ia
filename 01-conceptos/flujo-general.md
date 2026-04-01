# Flujo General del Ciclo de Vida de un Documento Electrónico

> **Fuente:** Manual Técnico SIFEN v150, secciones 5, 6 y 8

## Resumen del Ciclo Completo

El ciclo de vida de un Documento Electrónico (DE) abarca desde su generación hasta su consulta y posibles eventos posteriores.

---

## Fase 1: Generación del Documento Electrónico

1. El sistema de facturación del emisor genera el archivo XML del DE conforme a los Schemas XSD definidos en el Manual Técnico.
2. Se genera el **CDC** (Código de Control, 44 dígitos) que identifica unívocamente al documento.
3. Se genera el **código de seguridad** (dCodSeg, 9 dígitos aleatorios) para proteger la consulta pública.
4. Se genera el **código QR** (campo J002/dCarQR) utilizando el CSC otorgado por la SET.

### Estructura del CDC

El CDC se forma con los siguientes componentes:
- RUC del emisor (8 dígitos)
- Tipo de documento C002 (2 dígitos)
- Establecimiento C005 (3 dígitos)
- Punto de expedición C006 (3 dígitos)
- Número de timbrado C004 (8 dígitos)
- Fecha de emisión D002 (8 dígitos: AAAAMMDD)
- Tipo de emisor A005 (1 dígito)
- Código de seguridad B004 (9 dígitos)
- Dígito verificador (módulo 11, 1 dígito)

**Representación gráfica del CDC (grupos de 4):**
```
0144 4444 0170 0100 1001 4528 2201 7012 5158 7326 0988
```

---

## Fase 2: Firma Digital

1. El emisor firma digitalmente el DE utilizando su certificado digital emitido por un PSC habilitado.
2. La firma aplica al grupo de campos A001 (DE firmado) identificado por el atributo `Id` del CDC.
3. Se utiliza el estándar XML Digital Signature (Enveloped).
4. Algoritmos: RSA-SHA256, canonización C14N.
5. La fecha y hora de firma (campo A004/dFecFirma) debe ser **anterior** a la fecha de transmisión al SIFEN.

---

## Fase 3: Entrega al Receptor

1. El emisor genera el **KuDE** (representación gráfica) del DE.
2. El KuDE se entrega al receptor en formato físico o digital.
3. El KuDE contiene el CDC impreso en grupos de 4 caracteres y el código QR.
4. La entrega puede realizarse antes o después de la transmisión al SIFEN.

> **Importante:** Cuando el DE se modifica de forma que altera el CDC, el emisor debe inutilizar el número previo y emitir uno nuevo, enviando el nuevo comprobante al receptor.

---

## Fase 4: Transmisión al SIFEN

### Plazo de transmisión
| Condición | Plazo |
|-----------|-------|
| Transmisión normal | Hasta **72 horas** desde la fecha/hora de firma digital |
| Fecha de emisión (D002) adelantada | Hasta 120 horas (5 días) antes de la transmisión |
| Fecha de emisión (D002) atrasada | Hasta 720 horas (30 días) antes de la transmisión |

### Métodos de transmisión

#### Transmisión individual (síncrona)
- WS: `siRecepDE`
- Proceso: El SIFEN responde en la misma conexión.
- Resultado: Aprobado, Aprobado con observación, o Rechazado.

#### Transmisión por lotes (asíncrona)
- WS: `siRecepLoteDE`
- Capacidad: hasta 50 DE del mismo tipo por lote.
- Proceso: SIFEN devuelve un número de lote; el resultado se consulta posteriormente con `siResultLoteDE`.
- Formato del lote: archivo XML comprimido en Base64 (ZIP).

---

## Fase 5: Validación por el SIFEN

El SIFEN ejecuta las siguientes validaciones en orden:

1. **Validaciones de conexión/autenticación:** TLS 1.2, certificado digital del emisor.
2. **Validaciones técnicas del XML:** Conformidad con el Schema XSD, namespace, encoding.
3. **Validaciones de firma digital:** Integridad, LCR, cadena de confianza.
4. **Validaciones de negocio:** Reglas del Manual Técnico (timbrado vigente, CDC correcto, campos obligatorios, cálculos de IVA, etc.).

---

## Fase 6: Aprobación como DTE

Según el resultado de la validación:

| Estado | Descripción |
|--------|-------------|
| **Aprobado** | El DE cumple todas las validaciones. Se convierte en DTE. |
| **Aprobado con observación** | El DE fue aprobado pero tiene observaciones (puede incluir transmisión extemporánea). |
| **Rechazado** | El DE no cumple las validaciones. Se devuelve el código de error. |

Cuando es aprobado:
- El DTE queda registrado en la base de datos del SIFEN.
- Se genera el número de transacción (dProtAut, 10 dígitos).
- El DTE puede ser consultado por el emisor o receptor.

---

## Fase 7: Verificación por el Receptor

El receptor verifica la existencia del DTE:
- **Por WS:** `siConsDE` usando el CDC.
- **Por portal:** `https://ekuatia.set.gov.py/consultas/` ingresando el CDC.
- **Por QR:** Leyendo el código QR del KuDE.

El receptor debe confirmar:
1. Que el DE fue transmitido y aprobado como DTE.
2. Que la información del KuDE coincide con el DTE en el SIFEN.

---

## Fase 8: Eventos Post-Aprobación

### Eventos del Emisor
| Evento | Plazo | WS |
|--------|-------|----|
| Cancelación de FE | Hasta **48 horas** desde la aprobación | siRecepEvento |
| Cancelación de NCE/NDE/NRE/AFE | Hasta **168 horas** (7 días) desde la aprobación | siRecepEvento |
| Inutilización de número | Hasta el día 15 del mes siguiente al hecho | siRecepEvento |

### Eventos del Receptor
| Evento | Plazo | WS |
|--------|-------|----|
| Notificación de recepción | Hasta **45 días** desde la fecha de emisión | siRecepEvento / Portal |
| Conformidad | Hasta **45 días** desde la fecha de emisión | siRecepEvento / Portal |
| Disconformidad | Hasta **45 días** desde la fecha de emisión | siRecepEvento / Portal |
| Desconocimiento | Hasta **45 días** desde la fecha de emisión | siRecepEvento / Portal |

### Eventos Automáticos del SIFEN
- Vinculación de NCE/NDE a una FE (automático al aprobar la NCE/NDE).
- Vinculación de NRE a una FE (automático al aprobar la NRE).
- Asociaciones por interoperabilidad con Marangatu y Tesaka.

---

## Diagrama de Flujo Resumido

```
[Emisor genera XML] → [Firma digital] → [Genera KuDE] → [Entrega KuDE al receptor]
         ↓
[Transmite DE al SIFEN (máx. 72h desde firma)]
         ↓
[SIFEN valida: técnicas + firma + negocio]
         ↓
    [¿Válido?]
      /     \
   Sí        No
   ↓          ↓
[Aprobado]  [Rechazado → emisor corrige]
[DTE en BD]
   ↓
[Receptor consulta DTE en SIFEN]
   ↓
[Eventos opcionales: conformidad, cancelación, etc.]
```

---

## Plazos de Conservación

- DTE aprobados: conservar por **5 años**.
- FE con NCE/NDE asociadas: conservar por **5 años**.
- DTE cancelados: conservar por **5 años**.

## Herramienta de Prevalidación

La DNIT disponibiliza un prevalidador en tiempo de desarrollo:
`https://ekuatia.set.gov.py/prevalidador/`
