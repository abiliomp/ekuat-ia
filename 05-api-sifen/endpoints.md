# Endpoints de los Web Services SIFEN

> **Fuente:** Manual Técnico SIFEN v150, sección 7.10

## Descripción

El SIFEN expone sus servicios a través de Web Services SOAP 1.2. Existen dos ambientes: **pruebas** (preproducción/homologación) y **producción**. Todos los WS requieren TLS 1.2 con autenticación mutua por certificado digital.

---

## Ambiente de Pruebas (Homologación)

Base URL: `https://sifen-test.set.gov.py`

| Web Service | URL Completa | Tipo |
|-------------|--------------|------|
| siRecepDE | `https://sifen-test.set.gov.py/de/ws/sync/recepcion.wsdl` | Síncrono |
| siRecepLoteDE | `https://sifen-test.set.gov.py/de/ws/async/recepcion-lote.wsdl` | Asíncrono |
| siResultLoteDE | `https://sifen-test.set.gov.py/de/ws/async/resultado-lote.wsdl` | Asíncrono |
| siConsDE | `https://sifen-test.set.gov.py/de/ws/consultas/consulta.wsdl` | Síncrono |
| siConsRUC | `https://sifen-test.set.gov.py/de/ws/consultas/consulta-ruc.wsdl` | Síncrono |
| siConsArchivoRUC | `https://sifen-test.set.gov.py/de/ws/consultas/consulta-archivo-ruc.wsdl` | Síncrono (NT-011) |
| siRecepEvento | `https://sifen-test.set.gov.py/de/ws/eventos/recepcion-evento.wsdl` | Síncrono |

---

## Ambiente de Producción

Base URL: `https://sifen.set.gov.py`

| Web Service | URL Completa | Tipo |
|-------------|--------------|------|
| siRecepDE | `https://sifen.set.gov.py/de/ws/sync/recepcion.wsdl` | Síncrono |
| siRecepLoteDE | `https://sifen.set.gov.py/de/ws/async/recepcion-lote.wsdl` | Asíncrono |
| siResultLoteDE | `https://sifen.set.gov.py/de/ws/async/resultado-lote.wsdl` | Asíncrono |
| siConsDE | `https://sifen.set.gov.py/de/ws/consultas/consulta.wsdl` | Síncrono |
| siConsRUC | `https://sifen.set.gov.py/de/ws/consultas/consulta-ruc.wsdl` | Síncrono |
| siConsArchivoRUC | `https://sifen.set.gov.py/de/ws/consultas/consulta-archivo-ruc.wsdl` | Síncrono (NT-011) |
| siRecepEvento | `https://sifen.set.gov.py/de/ws/eventos/recepcion-evento.wsdl` | Síncrono |

---

## Otros Servicios y URLs del Ecosistema e-Kuatia

| Servicio | URL | Propósito |
|----------|-----|-----------|
| Portal e-Kuatia (producción) | `https://ekuatia.set.gov.py` | Portal principal para contribuyentes |
| Portal e-Kuatia (pruebas) | `https://ekuatia-test.set.gov.py` | Ambiente de homologación |
| Prevalidador XML | `https://ekuatia.set.gov.py/prevalidador/` | Validación de XML antes de enviar al SIFEN |
| Consulta pública de DE | `https://ekuatia.set.gov.py/consultas/` | Verificación de autenticidad de DTE |
| Documentación técnica | `https://www.dnit.gov.py/web/e-kuatia/documentacion-tecnica` | Manuales, XSD, Notas Técnicas |
| NTP Server 1 | `aravo1.set.gov.py` | Sincronización de hora |
| NTP Server 2 | `aravo2.set.gov.py` | Sincronización de hora (redundante) |

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

| WS | Método SOAP | Acción |
|----|-------------|--------|
| siRecepDE | `rRecepDE` | Recibe un DE individual y retorna aprobación/rechazo |
| siConsDE | `rConsDE` | Consulta el estado de un DE por su CDC |
| siConsRUC | `rConsRUC` | Consulta datos de un contribuyente por RUC |
| siConsArchivoRUC | `rConsArchivoRUC` | Descarga archivo de contribuyentes registrados (NT-011) |
| siRecepEvento | `rRecepEvento` | Recibe eventos (cancelación, inutilización, eventos del receptor) |

### Web Services Asíncronos

Los WS asíncronos reciben el lote y devuelven un número de lote. El resultado se consulta posteriormente con siResultLoteDE.

| WS | Método SOAP | Acción |
|----|-------------|--------|
| siRecepLoteDE | `rRecepLoteDE` | Envía un lote de DE (hasta 50 DE comprimidos en ZIP+Base64) |
| siResultLoteDE | `rResultLoteDE` | Consulta el resultado de procesamiento de un lote por su número |

---

## Flujo Recomendado para Elección de WS

```
¿Cuántos DE a enviar?
├── 1 DE → siRecepDE (síncrono, respuesta inmediata)
└── 2-50 DE → siRecepLoteDE (asíncrono)
                └── Consultar resultado → siResultLoteDE
                    ├── Estado "En proceso" → Reintentar consulta (esperar)
                    └── Estado "Procesado" → Verificar aprobados/rechazados
```

---

## Consideraciones para Producción vs Pruebas

| Aspecto | Pruebas | Producción |
|---------|---------|------------|
| Timbrado | Timbrado de prueba (provisto por DNIT) | Timbrado real habilitado por la SET |
| Certificado | Certificado de prueba (autofirmado o emitido por CA test) | Certificado emitido por PSC autorizado |
| Efectos tributarios | Ninguno (DE no tienen validez fiscal) | Plena validez fiscal y tributaria |
| RUC del emisor | RUC de prueba provisto por la DNIT | RUC real del contribuyente |
| QR generado | URL de test | URL de producción |
