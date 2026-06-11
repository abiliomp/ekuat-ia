# Nota de Crédito Electrónica (NCE)

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4, grupo E5

## Identificación

| Atributo | Valor |
|----------|-------|
| **Código C002** | 5 |
| **Descripción C003** | "Nota de crédito electrónica" |
| **Campo XML principal** | `gCamNCDE` |
| **Rango de campos** | E400-E499 |

## Descripción

La Nota de Crédito Electrónica es el documento emitido para ajustar, disminuir o anular el valor de una Factura Electrónica previamente aprobada por el SIFEN. Se emite cuando existe una devolución de mercadería, descuento, bonificación u otro ajuste que reduce el valor original de la factura.

## Requisito Principal

La NCE debe estar vinculada a una FE ya existente y aprobada en el SIFEN. Se referencia mediante el grupo H (campos H001-H049, documentos asociados).

**Condición:** La FE referenciada debe estar en situación "Aprobado" o "Aprobado con observación" en el SIFEN.

## Campos Específicos (E400-E499)

| ID | Campo | Tipo | Longitud | Ocurrencia | Descripción | Observaciones |
|----|-------|------|----------|------------|-------------|---------------|
| E400 | gCamNCDE | G | - | 0-1 | Grupo NCE/NDE | Obligatorio si C002=5 o 6 |
| E401 | iMotEmi | N | 1-2 | 1-1 | Motivo de emisión | Ver tabla abajo |
| E402 | dDesMotEmi | A | 6-30 | 1-1 | Descripción motivo | Ref. E401 |

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

## Documento Asociado (H001-H049)

La NCE debe referenciar la FE a la que aplica:

| ID | Campo | Tipo | Longitud | Descripción |
|----|-------|------|----------|-------------|
| H001 | gDocAso | G | - | Grupo documentos asociados |
| H002 | iTipDocAso | N | 1 | Tipo: 1=Electrónico, 2=Impreso, 3=Constancia Electrónica (literal exacto del XSD para H003: `Constancia Electrónica`) |
| H004 | dCDCAnteDE | A | 44 | CDC del DTE anterior (si H002=1) |
| H006 | dNumDocAso | A | 1-13 | Número del documento impreso (si H002=2) |

## Efectos en el SIFEN

Al aprobar una NCE:
1. El SIFEN genera automáticamente el evento de "Devolución y Ajuste de precios" sobre la FE referenciada.
2. El receptor de la FE asociada **no tendrá derecho** al crédito del IVA en forma total o parcial.
3. En caso de devolución/ajuste total de una FE, **no es posible retractarse**. Para corregir, el emisor debe generar una nueva FE idéntica.

## Particularidades

- **Sin condición de operación:** La NCE no lleva grupo `gCamCond` (E600).
- **Ítems:** Se deben detallar los ítems devueltos o ajustados con sus respectivos valores e IVA.
- **Coexistencia:** Durante las etapas de Plan Piloto y Voluntariedad, la NCE puede vincularse a una factura pre-impresa. El sistema genera el evento automático de AJUSTE pero no valida los montos.

## Plazos y Eventos

| Evento | Actor | Plazo | Método |
|--------|-------|-------|--------|
| Cancelación | Emisor | 168 horas (7 días) desde aprobación | WS siRecepEvento |
| Notificación recepción | Receptor | 45 días desde emisión | WS/Portal |
| Conformidad | Receptor | 45 días desde emisión | WS/Portal |
| Disconformidad | Receptor | 45 días desde emisión | WS/Portal |
| Desconocimiento | Receptor | 45 días desde emisión | WS/Portal |

## Conservación

Las FE con NCE asociadas deben conservarse obligatoriamente por **5 años**.

## Ejemplo Parcial XML para NCE

```xml
<gDtipDE>
  <gCamNCDE>
    <iMotEmi>2</iMotEmi>
    <dDesMotEmi>Devolución</dDesMotEmi>
  </gCamNCDE>
  <!-- Ítems devueltos -->
  <gCamItem>
    <dCodInt>PROD001</dCodInt>
    <dDesProSer>Producto devuelto</dDesProSer>
    <cUniMed>77</cUniMed>
    <dDesUniMed>UNI</dDesUniMed>
    <dCantProSer>1</dCantProSer>
    <gValorItem>
      <dPUniProSer>100000</dPUniProSer>
      <dTotBruOpeItem>100000</dTotBruOpeItem>
      <gValorRestaItem>
        <dDescItem>0</dDescItem>
        <dTotOpeItem>100000</dTotOpeItem>
      </gValorRestaItem>
    </gValorItem>
    <gCamIVA>
      <iAfecIVA>1</iAfecIVA>
      <dDesAfecIVA>Gravado IVA</dDesAfecIVA>
      <dPropIVA>100</dPropIVA>
      <dTasaIVA>10</dTasaIVA>
      <dBasGravIVA>90909</dBasGravIVA>
      <dLiqIVAItem>9091</dLiqIVAItem>
    </gCamIVA>
  </gCamItem>
</gDtipDE>
<!-- Documento asociado: FE referenciada -->
<gDocAso>
  <iTipDocAso>1</iTipDocAso>
  <dCDCAnteDE>[CDC-DE-LA-FE-REFERENCIADA]</dCDCAnteDE>
</gDocAso>
```
