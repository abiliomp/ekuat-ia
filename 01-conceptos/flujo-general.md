> **Fuente:** Manual Técnico SIFEN v150, secciones 6, 6.1, 6.2, 6.2.1, 6.3–6.6

> **Nota:** Este documento refleja el MT v150 con cambios del historial de versiones marcados.

# Flujo General del Ciclo de Vida de un Documento Electrónico

Descripción del modelo operativo completo: desde la generación del DE hasta la obtención del DTE aprobado y su consulta por el receptor.

---

## 1. Visión General del Modelo Operativo

El SIFEN opera en dos momentos principales:

### Primer momento — Operación comercial con DE
1. El facturador electrónico realiza la operación comercial.
2. Genera el Documento Electrónico (DE) en formato XML.
3. **Firma digitalmente** el DE con su certificado digital.
4. **[MODIFICADO]** Entrega el DE al receptor (como regla general, **antes** de la transmisión al SIFEN):
   - Si el receptor es facturador electrónico: envía el XML firmado.
   - Si el receptor **no** es facturador electrónico: **[MODIFICADO]** envía o disponibiliza el KuDE en formato físico o digital.

### Segundo momento — Transmisión de los DE a la SET
5. El emisor envía el DE firmado digitalmente al SIFEN dentro del plazo establecido.
6. El SIFEN ejecuta las validaciones (de conexión, técnicas y de negocio).
7. Si el DE supera todas las validaciones, se aprueba como **DTE** y se almacena en SIFEN.
8. El receptor verifica la existencia del DTE en el SIFEN.

---

## 2. Pasos Detallados del Flujo

```
[1] GENERACIÓN DEL DE
     │
     ├─► Generar CDC (44 dígitos)
     ├─► Generar Código de Seguridad (9 dígitos aleatorios)
     └─► Estructurar XML según Schema XML 18 (DE_v150.xsd)

[2] FIRMA DIGITAL
     │
     ├─► Firmar DE con certificado X.509 v3 del RUC emisor
     ├─► Firma abarca el grupo A001 (ID = CDC)
     └─► Estándar: XML Enveloped, RSA 2048, SHA-256

[3] ENTREGA AL RECEPTOR
     │  ← La entrega al receptor puede ser previa o simultánea
     │    a la transmisión al SIFEN
     ├─► Si receptor es FE: enviar XML firmado
     └─► Si receptor NO es FE: enviar KuDE (físico o digital)

[4] TRANSMISIÓN AL SIFEN (dentro del plazo establecido)
     │
     ├─► WS siRecepDE (1 DE, síncrono) — Schema XML 2
     └─► WS siRecepLoteDE (hasta 50 DE, asíncrono) — Schema XML 5

[5] VALIDACIÓN POR SIFEN
     │
     ├─► Validaciones de conexión (TLS, certificado)
     ├─► Validaciones técnicas (estructura XML, schema)
     └─► Validaciones de negocio (reglas del capítulo 12)

[6] RESULTADO DE LA VALIDACIÓN
     │
     ├─► APROBADO → DTE almacenado en SIFEN
     │     └─► Protocolo de aprobación: Schema XML 4 (ProtProcesDE_v150.xsd)
     │
     └─► RECHAZADO → DE no ingresa al SIFEN
           ├─► Si los cambios NO alteran el CDC: reutilizar CDC y reenviar
           └─► Si los cambios SÍ alteran el CDC: inutilizar número y emitir nuevo DE

[7] VERIFICACIÓN POR EL RECEPTOR
     │
     ├─► WS siConsDE (por CDC) — Schema XML 9
     ├─► Portal web SIFEN con código QR del KuDE
     └─► Ingreso manual del CDC en el portal
```

---

## 3. Modalidades de Validación

### 3.1 Validación Posterior (Regla General)
- El emisor entrega el DE al receptor y **luego** lo transmite al SIFEN.
- Permite generar el KuDE **antes** de obtener la aprobación.
- Plazo de transmisión: hasta **72 horas** desde la firma digital.
- El receptor se obliga a consultar a posteriori en el SIFEN.

### 3.2 Validación Previa (Opcional — por decisión del emisor)
- **[MODIFICADO]** El emisor transmite el DE al SIFEN **antes** de entregarlo al receptor, o de manera previa a dicha entrega.
- **[MODIFICADO]** El SIFEN realiza las validaciones y se obtiene el protocolo de aprobación del DTE de manera previa o posterior a la entrega del documento al receptor.
- Elimina la incertidumbre para el receptor sobre la validez del documento.

---

## 4. Tabla de Plazos SIFEN

**[MODIFICADO]** Conforme a las bases y condiciones del Modelo SIFEN y el Decreto N° 7.795/2017, se han establecido los siguientes plazos:

| Caso | Plazo | Observación |
|------|-------|-------------|
| **Transmisión normal de los DE** | Hasta **72 horas** (regla general) | **[MODIFICADO]** La transmisión es normal cuando: (1) la diferencia entre fecha/hora de firma y de transmisión no supera 72 h, Y ADEMÁS cumple una de: (a) la diferencia entre la fecha/hora de emisión anterior y la de transmisión al SIFEN no supera 120 horas (5 días), o (b) la diferencia entre la fecha/hora de emisión posterior y la de transmisión al SIFEN no supera 120 horas (5 días). |
| **[MODIFICADO] Transmisión extemporánea de los DE** | Según situación de extemporaneidad | **[MODIFICADO]** Se considera transmisión extemporánea el envío de DE en situación contraria a la Transmisión normal. Se les aplicarán las sanciones que correspondan. |
| **[NUEVO en v150] Rechazo de los DE por transmisión extemporánea** | **720 horas (30 días)** | **[NUEVO en v150]** Se rechaza cuando: la diferencia entre la fecha de transmisión y la fecha de emisión del DE sea **mayor** a 720 horas (30 días), O cuando la diferencia entre la fecha de emisión y la fecha de transmisión sea **mayor** a 120 horas (5 días). |
| **[NUEVO en v150] Trámite administrativo para normalizar DE rechazados por extemporaneidad** | Mayor a **720 horas (30 días)** | **[NUEVO en v150]** Para obtener la aprobación extemporánea de DE rechazados, los facturadores electrónicos deben iniciar un trámite administrativo, sin perjuicio de las sanciones que correspondan. |
| **[MODIFICADO] Evento de cancelación de una FE** | Hasta **48 horas (2 días)** | **[MODIFICADO]** El DTE debe existir en el SIFEN. El cómputo del plazo inicia desde la aprobación del DE por parte de la SET (fecha y hora SIFEN). |
| **[NUEVO en v150] Eventos de cancelación de DTE distintos a FE** | Hasta **168 horas (7 días)** | **[NUEVO en v150]** El DTE (distinto a FE) debe existir en el SIFEN. El cómputo del plazo inicia desde la aprobación del DE por la SET (fecha y hora SIFEN). |
| **Inutilización de la numeración de un DE** | Hasta **360 horas (15 días)** | El plazo comienza a correr a partir del siguiente mes del consumo de la numeración del timbrado. |
| **[NUEVO en v150] Eventos del Receptor: Notificación de Recepción DE/DTE, Conformidad, Disconformidad, Desconocimiento DE/DTE** | Hasta **1080 horas (45 días)** | **[NUEVO en v150]** El plazo se computa desde la fecha de emisión del DE/DTE. |
| **[NUEVO en v150] Corrección — Evento del Receptor: Notificación de Recepción DE/DTE, Conformidad, Disconformidad, Desconocimiento DE/DTE** | Hasta **360 horas (15 días)** | **[NUEVO en v150]** El plazo se computa desde la fecha de registro del primer evento sobre un DTE (Conformidad, Disconformidad o Desconocimiento). |

> **Obs:** El cómputo de los plazos fue establecido en **horas corridas**.

---

## 5. Rechazo y Reenvío del DE

**[MODIFICADO]** En caso de que el DE no supere las validaciones:

- **Si los ajustes NO alteran el CDC**: Se puede reutilizar el mismo CDC del DE rechazado (esto permite que, luego de aprobado, el DTE pueda ser consultado mediante el QR generado en el KuDE entregado al receptor durante la operación comercial). El emisor debe reenviar hasta lograr la aprobación, cuantas veces sea necesario.
- **Si los ajustes SÍ alteran el CDC**: El emisor debe inutilizar el número de comprobante previamente generado y emitir un nuevo DE (con nuevo CDC). Esto implica también el envío del nuevo DE al receptor.

Lo anterior es sin perjuicio del **[MODIFICADO]** incumplimiento de los términos y condiciones en la transmisión de los DE y la consecuente aplicación del régimen sancionatorio por la entrega extemporánea.

---

## 6. Verificación de la Existencia del DTE por el Receptor

**[MODIFICADO]** En el modelo de aprobación posterior, el receptor de los DE, con el objeto de ejercer sus derechos tributarios (como respaldo documental de sus Declaraciones Juradas), se obliga a verificar la existencia y coincidencia de la Representación Gráfica del DTE (KuDE) con el DTE almacenado en el SIFEN.

La verificación puede realizarse:
- Por servicio web de consulta CDC (WS siConsDE).
- Mediante consulta en la página web del SIFEN a partir del código QR del KuDE.
- Por el llenado manual del CDC en el portal.

El receptor debe verificar específicamente:
- **[MODIFICADO]** Que el DE fue transmitido y obtuvo la aprobación como DTE.
- **[MODIFICADO]** Que la información presente en el KuDE coincide plenamente con la información del DTE consultado.

---

## 7. Tiempo de Respuesta del SIFEN

**[MODIFICADO]** Para la SET, el tiempo de respuesta de validación de un DTE está establecido como máximo en **1 (un) minuto**, con el objetivo de llegar, en el futuro, a un tiempo de procesamiento menor a **2 (dos) segundos** por DTE.
