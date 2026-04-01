# Nota de Débito Electrónica (NDE)

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4, grupo E5

## Identificación

| Atributo | Valor |
|----------|-------|
| **Código C002** | 6 |
| **Descripción C003** | "Nota de débito electrónica" |
| **Campo XML principal** | `gCamNCDE` (mismo grupo que NCE) |
| **Rango de campos** | E400-E499 |

## Descripción

La Nota de Débito Electrónica es el documento emitido para ajustar, aumentar o corregir el valor de una Factura Electrónica previamente aprobada por el SIFEN. Se emite cuando corresponde realizar un cargo adicional al cliente (ajuste de precio al alza, recupero de costos/gastos, etc.).

## Requisito Principal

La NDE debe estar vinculada a una FE ya existente y aprobada en el SIFEN. Se referencia mediante el grupo H (campos H001-H049, documentos asociados).

## Campos Específicos (E400-E499)

La NDE utiliza el mismo grupo `gCamNCDE` que la NCE:

| ID | Campo | Tipo | Longitud | Ocurrencia | Descripción | Observaciones |
|----|-------|------|----------|------------|-------------|---------------|
| E400 | gCamNCDE | G | - | 0-1 | Grupo NCE/NDE | Obligatorio si C002=5 o 6 |
| E401 | iMotEmi | N | 1-2 | 1-1 | Motivo de emisión | Ver tabla abajo |
| E402 | dDesMotEmi | A | 6-30 | 1-1 | Descripción del motivo | Ref. E401 |

## Motivos de Emisión (E401)

| Código | Descripción |
|--------|-------------|
| 1 | Devolución y Ajuste de precios |
| 2 | Devolución |
| 3 | Descuento |
| 4 | Bonificación |
| 5 | Crédito incobrable |
| 6 | Recupero de costo |
| 7 | Recupero de gasto |
| 8 | Ajuste de precio |

## Diferencia con NCE

| Aspecto | NCE (C002=5) | NDE (C002=6) |
|---------|--------------|--------------|
| Efecto sobre FE | Disminuye el valor | Aumenta el valor |
| Uso típico | Devoluciones, descuentos | Cargos adicionales, correcciones al alza |
| Grupo XML | `gCamNCDE` | `gCamNCDE` (mismo) |
| Motivos | Mismos códigos 1-8 | Mismos códigos 1-8 |

## Documento Asociado (H001-H049)

Igual que para NCE, la NDE debe referenciar la FE original:

| ID | Campo | Tipo | Longitud | Descripción |
|----|-------|------|----------|-------------|
| H001 | gDocAso | G | - | Grupo documentos asociados |
| H002 | iTipDocAso | N | 1 | Tipo: 1=Electrónico, 2=Impreso |
| H004 | dCDCAnteDE | A | 44 | CDC del DTE anterior (si H002=1) |

## Efectos en el SIFEN

Al aprobar una NDE:
1. El SIFEN genera automáticamente el evento de "Devolución y Ajuste de precios" sobre la FE referenciada.
2. El estado de la FE queda registrado con el ajuste correspondiente.

## Plazos y Eventos

| Evento | Actor | Plazo | Método |
|--------|-------|-------|--------|
| Cancelación | Emisor | 168 horas (7 días) desde aprobación | WS siRecepEvento |
| Notificación recepción | Receptor | 45 días desde emisión | WS/Portal |
| Conformidad | Receptor | 45 días desde emisión | WS/Portal |
| Disconformidad | Receptor | 45 días desde emisión | WS/Portal |
| Desconocimiento | Receptor | 45 días desde emisión | WS/Portal |

## Ejemplo Parcial XML para NDE

```xml
<gDtipDE>
  <gCamNCDE>
    <iMotEmi>8</iMotEmi>
    <dDesMotEmi>Ajuste de precio</dDesMotEmi>
  </gCamNCDE>
  <!-- Ítems con ajuste adicional -->
  <gCamItem>
    <dCodInt>SERV001</dCodInt>
    <dDesProSer>Cargo adicional por servicio</dDesProSer>
    <cUniMed>77</cUniMed>
    <dDesUniMed>UNI</dDesUniMed>
    <dCantProSer>1</dCantProSer>
    <gValorItem>
      <dPUniProSer>50000</dPUniProSer>
      <dTotBruOpeItem>50000</dTotBruOpeItem>
      <gValorRestaItem>
        <dDescItem>0</dDescItem>
        <dTotOpeItem>50000</dTotOpeItem>
      </gValorRestaItem>
    </gValorItem>
    <gCamIVA>
      <iAfecIVA>1</iAfecIVA>
      <dDesAfecIVA>Gravado IVA</dDesAfecIVA>
      <dPropIVA>100</dPropIVA>
      <dTasaIVA>10</dTasaIVA>
      <dBasGravIVA>45455</dBasGravIVA>
      <dLiqIVAItem>4545</dLiqIVAItem>
    </gCamIVA>
  </gCamItem>
</gDtipDE>
<!-- Documento asociado: FE referenciada -->
<gDocAso>
  <iTipDocAso>1</iTipDocAso>
  <dCDCAnteDE>[CDC-DE-LA-FE-REFERENCIADA]</dCDCAnteDE>
</gDocAso>
```
