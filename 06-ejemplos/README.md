# Ejemplos de Documentos Electrónicos

> **Fuente:** Manual Técnico SIFEN v150, Schemas XSD v150

## Descripción

Este directorio contiene ejemplos de Documentos Electrónicos en formato XML, junto con explicaciones detalladas de cada campo. Los ejemplos son de **ambiente de prueba** y no tienen valor fiscal.

---

## Índice de Ejemplos

| Directorio | Tipo | Descripción |
|------------|------|-------------|
| `factura-simple/` | FE (C002=1) | Factura Electrónica con 2 ítems, IVA 10%, condición crédito (plazo 28 días) |
| `respuestas-ws/` | Respuestas SOAP reales | Capturas crudas de `sifen-test`, anonimizadas. 09/10/2026, flujo completo: FE aprobada (0260), CDC inexistente (0420), cancelación rechazada (4009 por desfase de reloj, 0100 transitorio) y aceptada (0600), consulta por CDC antes y después de cancelar (0422 con `xContenDE` y `xContEv`). 06/10/2026: rechazos 0160 en ambiente degradado. Ver su `README.md` |

---

## Estructura de Cada Ejemplo

Cada subdirectorio contiene:
- `ejemplo.xml` — El XML completo del DE (de ambiente de prueba)
- `explicacion.md` — Anotación campo por campo del XML

---

## Datos de Prueba Comunes

> **⚠️ Verificado el 03/10/2026:** `factura-simple/ejemplo.xml` proviene del ejemplo del MT v150 y **no valida contra el XSD de producción** (`php 04-schemas-xsd/validacion-local/validar.php 06-ejemplos/factura-simple/ejemplo.xml`): los RUC `00000001` y `00000002` violan el patrón `tRuc` (`[1-9][0-9]*[0-9A-D]?`, sin ceros a la izquierda; ver [xsd-produccion-vs-manual.md](../04-schemas-xsd/xsd-produccion-vs-manual.md) §1.d) y el certificado está reemplazado por texto. Sirve para entender la estructura campo a campo, **no** como plantilla para enviar. Además, estos datos **no** son "provistos por la DNIT": la [Guía de Pruebas](../10-guias/guia-de-pruebas.md) exige el RUC y la razón social **reales** del contribuyente también en pruebas; lo único genérico son el CSC `0001`/`0002` y el literal del nombre del emisor (validación 1263). Reemplazar este ejemplo por una FE real aprobada en `sifen-test` (anonimizada) es un pendiente de la Fase A.

Datos que usa el ejemplo (tomados del MT):

| Campo | Valor |
|-------|-------|
| RUC Emisor | `00000001-9` |
| RUC Receptor | `00000002-7` |
| Timbrado | `12345678` |
| Establecimiento | `001` |
| Punto de Expedición | `001` |
| Tipo de Documento | `1` (FE) |
| Ambiente | Pruebas (QR hacia `https://ekuatia.set.gov.py/consultas-test/qr?`, MT cap. QR) |

---

## Notas Importantes sobre los Ejemplos

1. El campo `<dSisFact>` (A005) es **obligatorio** — el XSD de producción (`DE_v150.xsd`) lo exige entre `dFecFirma` y `gOpeDE` y solo acepta el valor `1`. La NT-010 eliminó únicamente el **valor 2** ("SIFEN solución gratuita"), no el campo. (Corrección de junio 2026: una nota anterior afirmaba erróneamente que el campo había sido eliminado.)
2. El certificado digital en `<X509Certificate>` está redactado con texto indicativo; en un DE real contiene el certificado X.509 en Base64.
3. La firma digital (`<SignatureValue>`) y el digest (`<DigestValue>`) son valores reales del ejemplo de prueba.
4. El QR en `<dCarQR>` apunta al ambiente de prueba (`consultas-test`).
