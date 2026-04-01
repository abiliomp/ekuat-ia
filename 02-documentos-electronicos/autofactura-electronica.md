# Autofactura Electrónica (AFE)

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4, grupo E4

## Identificación

| Atributo | Valor |
|----------|-------|
| **Código C002** | 4 |
| **Descripción C003** | "Autofactura electrónica" |
| **Campo XML principal** | `gCamAE` |
| **Rango de campos** | E300-E399 |
| **Moneda obligatoria** | PYG (Guaraní) — NT-012 |

## Descripción

La Autofactura Electrónica es emitida por el comprador/adquiriente cuando realiza operaciones con personas que no son contribuyentes del IVA o con extranjeros, quienes no están en condiciones de emitir una factura. El comprador actúa como emisor del documento.

**Base legal:** Ley N° 125/1991 y sus modificaciones.

## Características Particulares

- La **moneda** debe ser obligatoriamente PYG (D015=PYG). Conforme al Dictamen DEINT N° 344/2022 (NT-012).
- El **receptor** (adquiriente) es quien emite el documento.
- El **vendedor** es un no contribuyente o extranjero.
- Requiere el grupo `gCamCond` (E600) para condición de operación.
- Cancelación: hasta 168 horas (7 días) desde la aprobación.

## Campos del Vendedor (E300-E322)

| ID | Campo | Tipo | Longitud | Ocurrencia | Descripción | Observaciones |
|----|-------|------|----------|------------|-------------|---------------|
| E300 | gCamAE | G | - | 0-1 | Grupo Autofactura | Obligatorio si C002=4 |
| E301 | iNatVen | N | 1 | 1-1 | Naturaleza del vendedor | 1=No contribuyente, 2=Extranjero |
| E302 | dDesNatVen | A | 10-16 | 1-1 | Descripción naturaleza | Ref. E301 |
| E304 | iTipIDVen | N | 1 | 1-1 | Tipo doc. identidad vendedor | 1=Cédula PY, 2=Pasaporte, 3=Cédula Ext., 4=Carnet residencia |
| E305 | dDTipIDVen | A | 9-20 | 1-1 | Descripción tipo doc. identidad | Ref. E304 |
| E306 | dNumIDVen | A | 1-20 | 1-1 | Número doc. identidad vendedor | |
| E307 | dNomVen | A | 4-60 | 1-1 | Nombre y apellido del vendedor | |
| E308 | dDirVen | A | 1-255 | 1-1 | Dirección del vendedor | Calle principal; para extranjeros: dirección de la transacción |
| E309 | dNumCasVen | N | 1-6 | 1-1 | Número de casa vendedor | 0 si no tiene numeración |
| E310 | cDepVen | N | 1-2 | 1-1 | Código departamento vendedor | Según XSD Departamentos |
| E311 | dDesDepVen | A | 6-16 | 1-1 | Descripción departamento | Ref. E310 |
| E312 | cDisVen | N | 1-4 | 0-1 | Código distrito vendedor | |
| E313 | dDesDisVen | A | 1-30 | 0-1 | Descripción distrito | Obligatorio si E312 existe |
| E314 | cCiuVen | N | 1-5 | 1-1 | Código ciudad vendedor | |
| E315 | dDesCiuVen | A | 1-30 | 1-1 | Descripción ciudad | Ref. E314 |

## Campos del Lugar de la Transacción (E316-E322)

| ID | Campo | Tipo | Longitud | Ocurrencia | Descripción |
|----|-------|------|----------|------------|-------------|
| E316 | dDirProv | A | 1-255 | 1-1 | Lugar de la transacción (calle principal) |
| E317 | cDepProv | N | 1-2 | 1-1 | Código departamento de la transacción |
| E318 | dDesDepProv | A | 6-16 | 1-1 | Descripción departamento |
| E319 | cDisProv | N | 1-4 | 0-1 | Código distrito |
| E320 | dDesDisProv | A | 1-30 | 0-1 | Descripción distrito |
| E321 | cCiuProv | N | 1-5 | 1-1 | Código ciudad de la transacción |
| E322 | dDesCiuProv | A | 1-30 | 1-1 | Descripción ciudad |

## Condición de Operación

La AFE incluye el grupo `gCamCond` (E600) igual que la FE. Ver campos E601-E659.

## Tipos de Transacción (D011)

Obligatorio para AFE. Mismos valores que para FE (códigos 1-13).

## Totales para AFE

El campo F023 (dTotalGs) en AFE corresponde directamente a F014 (total general de la operación), según NT-008.

## Eventos Disponibles para AFE

| Evento | Actor | Plazo | Método |
|--------|-------|-------|--------|
| Cancelación | Emisor | 168 horas (7 días) desde aprobación | WS siRecepEvento |
| Notificación recepción | Receptor | 45 días desde emisión | WS/Portal |
| Conformidad | Receptor | 45 días desde emisión | WS/Portal |
| Disconformidad | Receptor | 45 días desde emisión | WS/Portal |
| Desconocimiento | Receptor | 45 días desde emisión | WS/Portal |

## Ejemplo Parcial de Estructura XML para AFE

```xml
<gDtipDE>
  <gCamAE>
    <iNatVen>1</iNatVen>
    <dDesNatVen>No contribuyente</dDesNatVen>
    <iTipIDVen>1</iTipIDVen>
    <dDTipIDVen>Cédula paraguaya</dDTipIDVen>
    <dNumIDVen>1234567</dNumIDVen>
    <dNomVen>Juan Pérez López</dNomVen>
    <dDirVen>Calle Principal 123</dDirVen>
    <dNumCasVen>123</dNumCasVen>
    <cDepVen>1</cDepVen>
    <dDesDepVen>CAPITAL</dDesDepVen>
    <cCiuVen>1</cCiuVen>
    <dDesCiuVen>ASUNCION (DISTRITO)</dDesCiuVen>
    <dDirProv>Av. Mariscal López 500</dDirProv>
    <cDepProv>1</cDepProv>
    <dDesDepProv>CAPITAL</dDesDepProv>
    <cCiuProv>1</cCiuProv>
    <dDesCiuProv>ASUNCION (DISTRITO)</dDesCiuProv>
  </gCamAE>
  <gCamCond>
    <iCondOpe>1</iCondOpe>
    <dDCondOpe>Contado</dDCondOpe>
    <!-- Formas de pago... -->
  </gCamCond>
  <gCamItem>...</gCamItem>
</gDtipDE>
```
