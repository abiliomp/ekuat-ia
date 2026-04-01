# Envío de Lote de Documentos Electrónicos (siRecepLoteDE / siResultLoteDE)

> **Fuente:** Manual Técnico SIFEN v150, secciones 7.6 y 7.8, Guía de Mejores Prácticas

## Descripción

El envío en lote es el mecanismo **asíncrono** para transmitir múltiples Documentos Electrónicos al SIFEN en una sola llamada. El resultado no se entrega inmediatamente, sino que debe consultarse posteriormente con el WS `siResultLoteDE`.

---

## Características del Lote

| Atributo | Valor |
|----------|-------|
| **Máximo de DE por lote** | 50 |
| **Tipo de documento** | Todos los DE del lote deben ser del mismo tipo (C002) |
| **Compresión** | Los DE se comprimen en un archivo ZIP |
| **Codificación** | El ZIP se codifica en Base64 para incluir en el mensaje SOAP |
| **WS de envío** | `siRecepLoteDE` (método `rRecepLoteDE`) |
| **WS de consulta** | `siResultLoteDE` (método `rResultLoteDE`) |

---

## Flujo del Proceso Asíncrono

```
1. Generador prepara hasta 50 DE firmados
2. Generador comprime DE en archivo ZIP
3. Generador codifica ZIP en Base64
4. Generador llama a siRecepLoteDE
   └── SIFEN responde con dNumLote (número de lote)
5. Generador espera (recomendado: 1-5 minutos para lotes pequeños)
6. Generador llama a siResultLoteDE con dNumLote
   └── SIFEN responde con estado:
       ├── "En proceso" → Reintentar consulta más tarde
       └── "Procesado" → Verificar lista de aprobados y rechazados
```

---

## Web Service: siRecepLoteDE

### Endpoint

| Ambiente | URL |
|----------|-----|
| Pruebas | `https://sifen-test.set.gov.py/de/ws/async/recepcion-lote.wsdl` |
| Producción | `https://sifen.set.gov.py/de/ws/async/recepcion-lote.wsdl` |

### Método: rRecepLoteDE

**Request (envío del lote):**

```xml
<soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope"
                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <soapenv:Header/>
  <soapenv:Body>
    <rEnvioLote>
      <dId>1</dId>                    <!-- Número correlativo del request -->
      <xDELote>                        <!-- Contenido del lote -->
        <dCantRegDTE>2</dCantRegDTE>   <!-- Cantidad de DE en el lote -->
        <dIdLote>[BASE64_ZIP]</dIdLote> <!-- ZIP de DE firmados, codificado en Base64 -->
      </xDELote>
    </rEnvioLote>
  </soapenv:Body>
</soapenv:Envelope>
```

**Response (confirmación de recepción del lote):**

```xml
<soapenv:Envelope ...>
  <soapenv:Body>
    <rRetEnvioLote>
      <dId>1</dId>
      <gResProcDE>
        <dCodRes>0300</dCodRes>          <!-- Código de respuesta -->
        <dMsgRes>Lote recibido</dMsgRes> <!-- Mensaje de respuesta -->
        <dNumLote>98765</dNumLote>       <!-- Número de lote asignado por SIFEN -->
      </gResProcDE>
    </rRetEnvioLote>
  </soapenv:Body>
</soapenv:Envelope>
```

### Campos del Request siRecepLoteDE

| Campo | Tipo | Descripción |
|-------|------|-------------|
| dId | N | Identificador del request (correlativo interno del emisor) |
| dCantRegDTE | N | Cantidad de DE incluidos en el lote (1-50) |
| dIdLote | B | Contenido del ZIP con los DE firmados, codificado en Base64 |

### Estructura del ZIP

El archivo ZIP debe contener los DE firmados como archivos XML individuales:
- Un archivo XML por DE
- El nombre del archivo puede ser el CDC del DE: `[CDC_44_DIGITOS].xml`
- Los XML deben incluir la declaración XML y el namespace completo

---

## Web Service: siResultLoteDE

### Endpoint

| Ambiente | URL |
|----------|-----|
| Pruebas | `https://sifen-test.set.gov.py/de/ws/async/resultado-lote.wsdl` |
| Producción | `https://sifen.set.gov.py/de/ws/async/resultado-lote.wsdl` |

### Método: rResultLoteDE

**Request (consulta del resultado):**

```xml
<soapenv:Envelope ...>
  <soapenv:Header/>
  <soapenv:Body>
    <rConsLoteDE>
      <dId>1</dId>
      <dNumLote>98765</dNumLote>  <!-- Número de lote recibido en la respuesta de siRecepLoteDE -->
    </rConsLoteDE>
  </soapenv:Body>
</soapenv:Envelope>
```

**Response (resultado del procesamiento):**

```xml
<soapenv:Envelope ...>
  <soapenv:Body>
    <rRetConsLoteDE>
      <dId>1</dId>
      <gResLoteDe>
        <dCodRes>0304</dCodRes>          <!-- 0304 = Lote procesado -->
        <dMsgRes>Lote procesado</dMsgRes>
        <dNumLote>98765</dNumLote>
        <dCantRegInf>2</dCantRegInf>     <!-- Cantidad de DE en el lote -->
        <dFecProc>2024-01-15T10:30:00</dFecProc>
        <gDetalle>
          <!-- Detalle por cada DE del lote -->
          <gResProc>
            <dId>1</dId>
            <dCDC>[CDC_44_DIGITOS]</dCDC>
            <dCodRes>0302</dCodRes>       <!-- 0302 = Aprobado -->
            <dMsgRes>Aprobado</dMsgRes>
          </gResProc>
          <gResProc>
            <dId>2</dId>
            <dCDC>[CDC_44_DIGITOS_2]</dCDC>
            <dCodRes>0304</dCodRes>       <!-- Código de rechazo -->
            <dMsgRes>Rechazado: [motivo]</dMsgRes>
            <gDetMotErr>
              <dMsgErr>[Descripción del error]</dMsgErr>
            </gDetMotErr>
          </gResProc>
        </gDetalle>
      </gResLoteDe>
    </rRetConsLoteDE>
  </soapenv:Body>
</soapenv:Envelope>
```

### Códigos de Respuesta del Lote

| Código | Descripción |
|--------|-------------|
| 0300 | Lote recibido (pendiente de procesamiento) |
| 0301 | Lote en proceso |
| 0302 | Lote procesado exitosamente |
| 0303 | Lote con errores parciales (algunos DE aprobados, otros rechazados) |
| 0304 | Lote rechazado completamente |
| 0305 | Número de lote no encontrado |

### Códigos de Resultado por DE dentro del Lote

| Código | Descripción |
|--------|-------------|
| 0302 | DE aprobado |
| 0304 | DE rechazado (ver dMsgErr para detalle) |
| 0306 | DE aprobado con observaciones |

---

## Razones de Rechazo de un Lote

| Motivo | Descripción |
|--------|-------------|
| Lote vacío | El ZIP no contiene DE |
| Exceso de DE | Más de 50 DE en el lote |
| Tipos mixtos | DE de distintos tipos (C002) en el mismo lote |
| ZIP inválido | El Base64 no corresponde a un ZIP válido |
| XML malformado | Uno o más DE no son XML válidos |
| Certificado inválido | Certificado TLS o de firma no válido |

---

## Razones de Bloqueo del Facturador (según Guía de Mejores Prácticas)

| Motivo | Descripción |
|--------|-------------|
| Saturación del WS | Envío excesivo de lotes en un corto período |
| Lotes con muchos errores | Alto porcentaje de DE rechazados consecutivos |
| Certificado vencido | El certificado de transmisión está expirado |
| IP bloqueada | Múltiples intentos fallidos de autenticación |

---

## Buenas Prácticas para el Envío en Lote

1. **Agrupar DE del mismo tipo** para evitar rechazos por tipos mixtos.
2. **Verificar el XML localmente** con el prevalidador antes de incluirlo en el lote.
3. **Mantener el correlativo `dId`** para rastrear qué DE corresponde a qué resultado.
4. **Guardar el `dNumLote`** recibido para poder consultar el resultado.
5. **Implementar retry con backoff exponencial** para la consulta de resultados: esperar 1 minuto en el primer intento, luego aumentar progresivamente.
6. **No reenviar un DE aprobado**: si el SIFEN devuelve que un DE ya fue aprobado, no volver a enviarlo.
7. **Manejo de rechazados**: corregir el error indicado en `dMsgErr` antes de reenviar el DE corregido con un nuevo CDC.

---

## Límites y Consideraciones de Rendimiento

| Parámetro | Valor |
|-----------|-------|
| Máximo DE por lote | 50 |
| Tiempo estimado de procesamiento (lote pequeño) | 1-5 minutos |
| Tiempo estimado de procesamiento (lote grande) | 5-15 minutos |
| Timeout recomendado para consulta de resultado | 30 minutos máximo |
