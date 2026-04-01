# Ejemplos de Documentos Electrónicos

> **Fuente:** Manual Técnico SIFEN v150, Schemas XSD v150

## Descripción

Este directorio contiene ejemplos de Documentos Electrónicos en formato XML, junto con explicaciones detalladas de cada campo. Los ejemplos son de **ambiente de prueba** y no tienen valor fiscal.

---

## Índice de Ejemplos

| Directorio | Tipo | Descripción |
|------------|------|-------------|
| `factura-simple/` | FE (C002=1) | Factura Electrónica con 2 ítems, IVA 10%, condición crédito (plazo 28 días) |

---

## Estructura de Cada Ejemplo

Cada subdirectorio contiene:
- `ejemplo.xml` — El XML completo del DE (de ambiente de prueba)
- `explicacion.md` — Anotación campo por campo del XML

---

## Datos de Prueba Comunes

Los ejemplos usan los siguientes datos del ambiente de prueba provistos por la DNIT:

| Campo | Valor |
|-------|-------|
| RUC Emisor | `00000001-9` |
| RUC Receptor | `00000002-7` |
| Timbrado | `12345678` |
| Establecimiento | `001` |
| Punto de Expedición | `001` |
| Tipo de Documento | `1` (FE) |
| Ambiente | Pruebas (`https://ekuatia-test.set.gov.py`) |

---

## Notas Importantes sobre los Ejemplos

1. El campo `<dSisFact>` presente en el XML de ejemplo fue **eliminado por NT-010** (campo A005). Los XML actuales no deben incluirlo.
2. El certificado digital en `<X509Certificate>` está redactado con texto indicativo; en un DE real contiene el certificado X.509 en Base64.
3. La firma digital (`<SignatureValue>`) y el digest (`<DigestValue>`) son valores reales del ejemplo de prueba.
4. El QR en `<dCarQR>` apunta al ambiente de prueba (`consultas-test`).
