# Endpoints de los Web Services SIFEN

> **Fuente:** Manual Técnico SIFEN v150, §7.10 "Resumen de las direcciones electrónicas de los servicios web" y §7.11 "Servidor NTP" (PDF p. 42); §9.1-9.6 para los nombres de las operaciones (PDF pp. 46-56); [Guía de Mejores Prácticas](../10-guias/mejores-practicas-envio-de.md) §2; NT-011 para la consulta masiva de RUC. Rutas verificadas empíricamente vía mTLS con certificado real contra `sifen-test` el 11/06/2026 (PKuatia) y, para `consulta-ruc`, también contra producción.
>
> **⚠️ Rutas inexistentes.** Las rutas `recepcion.wsdl`, `recepcion-lote.wsdl`, `recepcion-evento.wsdl` y `resultado-lote.wsdl` que figuraban en versiones anteriores de este repositorio **no aparecen en el MT v150 ni en ninguna NT 001-027** (búsqueda en todos los PDF el 03/10/2026) y **no existen** en `sifen-test.set.gov.py` (HTTP 200 con cuerpo vacío). El MT §7.10 publica exactamente las rutas de las tablas siguientes (`recibe.wsdl`, `recibe-lote.wsdl`, `evento.wsdl`, `consulta-lote.wsdl`, `consulta.wsdl`, `consulta-ruc.wsdl`); en la fila de pruebas de `recibe.wsdl` el PDF tiene el error tipográfico `recibe.wsd`.
>
> **siConsArchivoRUC** (NT-011): la ruta `/de/ws/consultas/consulta-archivo-ruc.wsdl` no está publicada en ningún documento oficial; devolvió cuerpo vacío en pruebas y error de carga en producción (06/2026). `[PENDIENTE DE VERIFICACIÓN]`.
>
> **Corregido el 03/10/2026 (Fase 0):** nombres de las operaciones SOAP (antes figuraban `rRecepDE`, `rConsDE`, `rConsRUC`, `rRecepEvento`, `rRecepLoteDE`, `rResultLoteDE`, inexistentes) y condiciones del ambiente de pruebas.

## Descripción

El SIFEN expone sus servicios a través de Web Services SOAP 1.2. Existen dos ambientes: **pruebas** (preproducción/homologación) y **producción**. Todos los WS requieren TLS 1.2 con autenticación mutua por certificado digital.

---

## Ambiente de Pruebas (Homologación)

Base URL: `https://sifen-test.set.gov.py`

Agregar `?wsdl` a cada URL para obtener el WSDL (MT §7.10; guía §2).

| Web Service | URL (MT §7.10; verificada 06/2026) | Operación SOAP | Tipo |
|-------------|--------------|----------------|------|
| siRecepDE | `https://sifen-test.set.gov.py/de/ws/sync/recibe.wsdl` | `rEnviDe` | Síncrono |
| siRecepLoteDE | `https://sifen-test.set.gov.py/de/ws/async/recibe-lote.wsdl` | `rEnvioLote` | Asíncrono |
| siResultLoteDE | `https://sifen-test.set.gov.py/de/ws/consultas/consulta-lote.wsdl` | `rEnviConsLoteDe` | Síncrono (consulta del lote asíncrono) |
| siConsDE | `https://sifen-test.set.gov.py/de/ws/consultas/consulta.wsdl` | `rEnviConsDe` (mensaje `rEnviConsDeRequest`) | Síncrono |
| siConsRUC | `https://sifen-test.set.gov.py/de/ws/consultas/consulta-ruc.wsdl` | `rEnviConsRUC` | Síncrono |
| siRecepEvento | `https://sifen-test.set.gov.py/de/ws/eventos/evento.wsdl` | `rEnviEventoDe` | Síncrono |
| siConsArchivoRUC (NT-011) | `https://sifen-test.set.gov.py/de/ws/consultas/consulta-archivo-ruc.wsdl` `[PENDIENTE DE VERIFICACIÓN]` | `rEnviConsArchivoRUCRequest` | Síncrono — devuelve vacío en test |

---

## Ambiente de Producción

Base URL: `https://sifen.set.gov.py`

> Las seis rutas de producción están publicadas en el MT §7.10 (PDF p. 42). Solo `consulta-ruc.wsdl` fue verificada contra producción (06/2026); las demás se usan en producción por PKuatia desde 2023.

| Web Service | URL (MT §7.10) | Operación SOAP | Tipo |
|-------------|--------------|----------------|------|
| siRecepDE | `https://sifen.set.gov.py/de/ws/sync/recibe.wsdl` | `rEnviDe` | Síncrono |
| siRecepLoteDE | `https://sifen.set.gov.py/de/ws/async/recibe-lote.wsdl` | `rEnvioLote` | Asíncrono |
| siResultLoteDE | `https://sifen.set.gov.py/de/ws/consultas/consulta-lote.wsdl` | `rEnviConsLoteDe` | Síncrono (consulta del lote asíncrono) |
| siConsDE | `https://sifen.set.gov.py/de/ws/consultas/consulta.wsdl` | `rEnviConsDe` (mensaje `rEnviConsDeRequest`) | Síncrono |
| siConsRUC | `https://sifen.set.gov.py/de/ws/consultas/consulta-ruc.wsdl` | `rEnviConsRUC` | Síncrono (verificado en producción) |
| siRecepEvento | `https://sifen.set.gov.py/de/ws/eventos/evento.wsdl` | `rEnviEventoDe` | Síncrono |
| siConsArchivoRUC (NT-011) | `https://sifen.set.gov.py/de/ws/consultas/consulta-archivo-ruc.wsdl` `[PENDIENTE DE VERIFICACIÓN]` | `rEnviConsArchivoRUCRequest` | Síncrono — error de carga del WSDL en producción (06/2026) |

---

## Datos verificados de los WSDL reales (sifen-test, 06/2026)

| WS | Operación SOAP real | Detalle de tipos relevante |
|----|---------------------|----------------------------|
| siRecepDE | `rEnviDe(rEnvioDe)` | `rEnviDe { dId; xDE }` con `xDE` = **anyXML** (el rDE va embebido como XML) |
| siRecepLoteDE | `rEnvioLote(rEnvioLote)` | `rEnvioLote { dId; xDE }` con `xDE` = **base64Binary** (la capa SOAP de PHP codifica automáticamente: pasar el ZIP binario crudo) |
| siResultLoteDE | `rEnviConsLoteDe(rEnviConsLoteDe)` | — |
| siConsDE | `rEnviConsDe(rEnviConsDeRequest)` | — |

**Comportamiento operativo observado:** el ambiente de pruebas limita la tasa de solicitudes;
descargas repetidas de WSDL en poco tiempo producen respuestas vacías, errores intermitentes
y finalmente ausencia total de respuesta (bloqueo temporal). Usar caché de WSDL
(`Config::$wsdlCacheEnabled` en PKuatia) y espaciar los reintentos.

---

## Otros Servicios y URLs del Ecosistema e-Kuatia

| Servicio | URL | Propósito |
|----------|-----|-----------|
| Portal e-Kuatia (producción) | `https://ekuatia.set.gov.py` | Portal principal para contribuyentes |
| Consulta pública de DTE (producción) | `https://ekuatia.set.gov.py/consultas/` | Verificación de autenticidad de DTE (MT cap. QR, PDF p. 204) |
| Consulta pública de DTE (pruebas) | `https://ekuatia.set.gov.py/consultas-test/` | Ídem para el ambiente de pruebas (MT cap. QR) |
| URL base del QR (producción) | `https://ekuatia.set.gov.py/consultas/qr?` | Destino del código QR del KuDE (MT cap. QR, PDF p. 206) |
| URL base del QR (pruebas) | `https://ekuatia.set.gov.py/consultas-test/qr?` | Ídem para pruebas |
| Prevalidador XML | `https://ekuatia.set.gov.py/prevalidador/` | Validación de XML antes de enviar al SIFEN (guía de mejores prácticas §1) |
| Documentación técnica | `https://www.dnit.gov.py/web/e-kuatia/documentacion-tecnica` | Manuales, XSD, Notas Técnicas |
| NTP Server 1 | `aravo1.set.gov.py` | Sincronización de hora (MT §7.11) |
| NTP Server 2 | `aravo2.set.gov.py` | Sincronización de hora (MT §7.11) |

> El MT §7.11 advierte que el acceso a los servicios de 7.10 y 7.11 "dependerá de la política de seguridad establecida por la SET", que puede restringirlos por contribuyente o dirección IP. La URL `https://ekuatia-test.set.gov.py` que figuraba aquí no aparece en el MT ni en las guías: eliminada.

---

## Características Técnicas de los WS

| Atributo | Valor |
|----------|-------|
| **Protocolo** | SOAP 1.2 |
| **Style/Encoding** | Document/Literal |
| **Transporte** | HTTPS con TLS 1.2 |
| **Autenticación** | Certificado digital (mutual TLS) |
| **Formato de mensaje** | XML con namespace `http://ekuatia.set.gov.py/sifen/xsd` |
| **Codificación** | UTF-8 |

---

## Resumen por Tipo de WS

### Web Services Síncronos

Los WS síncronos devuelven la respuesta de validación inmediatamente en la misma llamada HTTP.

| WS | Operación SOAP (raíz del request, MT cap. 9) | Respuesta (raíz) | Acción |
|----|-------------|------------------|--------|
| siRecepDE | `rEnviDe` | `rRetEnviDe` > `rProtDe` | Recibe un DE y devuelve el protocolo de procesamiento (0260 = aprobado) — [recepcion-de.md](./recepcion-de.md) |
| siConsDE | `rEnviConsDe` (mensaje WSDL `rEnviConsDeRequest`) | `rResEnviConsDe` (`rEnviConsDeResponse`) | Devuelve el DTE aprobado por CDC (0422) — [consulta-estado.md](./consulta-estado.md) |
| siConsRUC | `rEnviConsRUC` | `rResEnviConsRUC` | Datos y estado de un RUC (0502) — [consulta-ruc.md](./consulta-ruc.md) |
| siConsArchivoRUC | `rEnviConsArchivoRUCRequest` (NT-011) | `rEnviConsArchivoRUCResponse` | Archivo diario de RUC (0520); no homologado |
| siRecepEvento | `rEnviEventoDe` | `rRetEnviEventoDe` > `gResProcEVe` | Registra hasta 15 eventos firmados (0600) — [eventos.md](./eventos.md) |

### Web Services Asíncronos

Los WS asíncronos reciben el lote y devuelven un número de lote. El resultado se consulta posteriormente con siResultLoteDE.

| WS | Operación SOAP (raíz del request, MT cap. 9) | Respuesta (raíz) | Acción |
|----|-------------|------------------|--------|
| siRecepLoteDE | `rEnvioLote` | `rResEnviLoteDe` | Encola un lote de hasta 50 DE del mismo tipo (ZIP con `rLoteDE` en Base64); devuelve `dProtConsLote` (0300) — [envio-lote.md](./envio-lote.md) |
| siResultLoteDE | `rEnviConsLoteDe` | `rResEnviConsLoteDe` > `gResProcLote` | Resultado por CDC de un lote (0362); consultar desde los 10 minutos — [envio-lote.md](./envio-lote.md) |

---

## Flujo Recomendado para Elección de WS

```
¿Cuántos DE a enviar?
├── 1 DE → siRecepDE (síncrono, respuesta inmediata)
└── 2-50 DE → siRecepLoteDE (asíncrono)
                └── Consultar resultado → siResultLoteDE
                    ├── 0361 "Lote en procesamiento" → volver a consultar (intervalos ≥ 10 min)
                    └── 0362 "Procesamiento de lote concluido" → recorrer gResProcLote (dEstRes por CDC)
```

---

## Consideraciones para Producción vs Pruebas

Según la [Guía de Pruebas](../10-guias/guia-de-pruebas.md) (DNIT, 02/2026) §2 y el MT cap. QR:

| Aspecto | Pruebas | Producción |
|---------|---------|------------|
| Timbrado | Timbrado y datos (vigencia, establecimiento, punto) obtenidos en el SGTM de Marangatu, también para pruebas | Timbrado real del SGTM |
| Certificado | **Certificado cualificado real** de un PSC habilitado, con el RUC del contribuyente (el certificado autogenerado solo sirve para el escenario "certificado NO válido") | Certificado cualificado de PSC habilitado |
| RUC del emisor | **RUC y DV reales** del contribuyente, tal como figuran en Marangatu | RUC real |
| Nombre del emisor (D105) | Literal obligatorio de ambiente de prueba (validación 1263; ver la divergencia con la guía en [guia-de-pruebas.md](../10-guias/guia-de-pruebas.md)) | Razón social real; el literal de prueba está prohibido |
| CSC | Genérico: `0001` → `ABCD0000000000000000000000000000`, `0002` → `EFGH0000000000000000000000000000` | CSC propio, obtenido en el portal |
| Efectos tributarios | Ninguno (sin valor jurídico) | Plena validez fiscal |
| URL del QR | `https://ekuatia.set.gov.py/consultas-test/qr?` | `https://ekuatia.set.gov.py/consultas/qr?` |
