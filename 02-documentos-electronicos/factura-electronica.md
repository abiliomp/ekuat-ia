# Factura Electrónica (FE)

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4, grupos E1 y E1.1

## Identificación

| Atributo | Valor |
|----------|-------|
| **Código C002** | 1 |
| **Descripción C003** | "Factura electrónica" |
| **Campo XML principal** | `gCamFE` |
| **Rango de campos** | E010-E099 |
| **Tipo de impuesto** | IVA (D013=1), Renta (D013=3), IVA-Renta (D013=5), Ninguno (D013=4) |

## Descripción

La Factura Electrónica es el DTE que respalda la compra y venta de bienes y servicios. Puede emitirse en operaciones B2B (empresa a empresa), B2C (empresa a consumidor), B2G (empresa a gobierno) y B2F (empresa a extranjero).

## Campos Específicos del Grupo E1 (E010-E099)

| ID | Campo | Tipo | Longitud | Ocurrencia | Descripción | Observaciones |
|----|-------|------|----------|------------|-------------|---------------|
| E010 | gCamFE | G | - | 0-1 | Campos de la FE | Obligatorio si C002=1 |
| E011 | iIndPres | N | 1 | 1-1 | Indicador de presencia | Ver tabla abajo |
| E012 | dDesIndPres | A | 10-30 | 1-1 | Descripción del indicador | Referente a E011 |
| E013 | dFecEmNR | F | 10 | 0-1 | Fecha futura traslado mercadería | Para NRE futura (RG 41/14) |

### Valores de Indicador de Presencia (E011)

| Código | Descripción |
|--------|-------------|
| 1 | Operación presencial |
| 2 | Operación electrónica |
| 3 | Operación telemarketing |
| 4 | Venta a domicilio |
| 5 | Operación bancaria |
| 6 | Operación cíclica |
| 9 | Otro |

## Campos de Compras Públicas (E1.1: E020-E029)

Obligatorio cuando D202=3 (operación B2G). Opcional a partir de NT-026.

| ID | Campo | Tipo | Longitud | Ocurrencia | Descripción |
|----|-------|------|----------|------------|-------------|
| E020 | gCompPub | G | - | 0-1 | Grupo compras públicas |
| E021 | dModCont | A | 2 | 1-1 | Modalidad - Código DNCP |
| E022 | dEntCont | N | 5 | 1-1 | Entidad - Código DNCP |
| E023 | dAnoCont | N | 2 | 1-1 | Año - Código DNCP |
| E024 | dSecCont | N | 7 | 1-1 | Secuencia - Código DNCP |
| E025 | dFeCodCont | F | 10 | 1-1 | Fecha de emisión del código de contratación |

## Condición de Operación (E7: E600-E699)

La FE requiere el grupo `gCamCond` (E600) para describir la condición de pago.

| ID | Campo | Tipo | Longitud | Descripción | Observaciones |
|----|-------|------|----------|-------------|---------------|
| E600 | gCamCond | G | - | Grupo condición | Obligatorio si C002=1 |
| E601 | iCondOpe | N | 1 | Condición de operación | 1=Contado, 2=Crédito |
| E602 | dDCondOpe | A | 7 | Descripción | "Contado" o "Crédito" |

### Pago al Contado (E605-E619, E620-E639)

Campos para describir las formas de pago cuando E601=1:

| ID | Campo | Descripción |
|----|-------|-------------|
| E605 | gPaConEIni | Grupo forma de pago contado (0-999 ocurrencias) |
| E606 | iTiPago | Tipo de pago (Efectivo, Cheque, Tarjeta, etc.) |
| E607 | dDesTiPag | Descripción tipo de pago |
| E608 | dMonTiPag | Monto por tipo de pago |
| E609 | cMoneTiPag | Moneda (ISO 4217) |

**Tipos de pago (E606):**
1=Efectivo, 2=Cheque, 3=Tarjeta de crédito, 4=Tarjeta de débito, 5=Transferencia, 6=Giro, 7=Billetera electrónica, 8=Tarjeta empresarial, 9=Vale, 10=Retención, 11=Pago por anticipo, 12=Valor fiscal, 13=Valor comercial, 14=Compensación, 15=Permuta, 16=Pago bancario (solo si E011=5), 17=Pago Móvil, 18=Donación, 19=Promoción, 20=Consumo Interno, 21=Pago Electrónico, 99=Otro

### Pago a Crédito (E640-E659)

| ID | Campo | Descripción | Observaciones |
|----|-------|-------------|---------------|
| E640 | gPagCred | Grupo crédito | Obligatorio si E601=2 |
| E641 | iCondCred | Condición de crédito | 1=Plazo, 2=Cuota |
| E643 | dPlazoCre | Plazo del crédito | Obligatorio si E641=1 |
| E644 | dCuotas | Cantidad de cuotas | Obligatorio si E641=2 |
| E645 | dMonEnt | Monto entrega inicial | Opcional |
| E650 | gCuotas | Detalle de cuotas | Si E641=2 |
| E651 | dMonCuota | Monto de cada cuota | |
| E652 | dVencCuo | Fecha vencimiento cuota | Formato AAAA-MM-DD |

## Tipos de Transacción (D011) — Solo para FE y AFE

| Código | Descripción |
|--------|-------------|
| 1 | Venta de mercadería |
| 2 | Prestación de servicios |
| 3 | Mixto (Venta de mercadería y servicios) |
| 4 | Venta de activo fijo |
| 5 | Venta de divisas |
| 6 | Compra de divisas |
| 7 | Promoción o entrega de muestras |
| 8 | Donación |
| 9 | Anticipo |
| 10 | Compra de productos |
| 11 | Compra de servicios |
| 12 | Venta de crédito fiscal |
| 13 | Muestras médicas (Art. 3 RG 24/2014) |

## Eventos Disponibles para FE

| Evento | Actor | Plazo | Método |
|--------|-------|-------|--------|
| Cancelación | Emisor | 48 horas desde aprobación | WS siRecepEvento |
| Nominación (NT-014) | Emisor | - | WS siRecepEvento |
| Notificación recepción | Receptor | 45 días desde emisión | WS/Portal |
| Conformidad | Receptor | 45 días desde emisión | WS/Portal |
| Disconformidad | Receptor | 45 días desde emisión | WS/Portal |
| Desconocimiento | Receptor | 45 días desde emisión | WS/Portal |
| Vinculación NCE/NDE | SIFEN (automático) | Inmediato a aprobación NCE/NDE | Automático |
| Vinculación NRE | SIFEN (automático) | Inmediato a aprobación NRE | Automático |

## Ejemplo de Estructura XML Mínima para FE

```xml
<rDE xmlns="http://ekuatia.set.gov.py/sifen/xsd">
  <dVerFor>150</dVerFor>
  <DE Id="[CDC-44-DIGITOS]">
    <!-- A: Campos firmados -->
    <dDVId>[digito_verificador]</dDVId>
    <dFecFirma>2024-01-15T10:30:00</dFecFirma>
    <!-- B: Operación -->
    <gOpeDE>
      <iTipEmi>1</iTipEmi>
      <dDesTipEmi>Normal</dDesTipEmi>
      <dCodSeg>123456789</dCodSeg>
    </gOpeDE>
    <!-- C: Timbrado -->
    <gTimb>
      <iTiDE>1</iTiDE>
      <dDesTiDE>Factura electrónica</dDesTiDE>
      <dNumTim>12345678</dNumTim>
      <dEst>001</dEst>
      <dPunExp>001</dPunExp>
      <dNumDoc>0000001</dNumDoc>
      <dFeIniT>2024-01-01</dFeIniT>
    </gTimb>
    <!-- D: Datos generales -->
    <gDatGralOpe>
      <dFeEmiDE>2024-01-15T10:30:00</dFeEmiDE>
      <gOpeCom>
        <iTipTra>1</iTipTra>
        <dDesTipTra>Venta de mercadería</dDesTipTra>
        <iTImp>1</iTImp>
        <dDesTImp>IVA</dDesTImp>
        <cMoneOpe>PYG</cMoneOpe>
        <dDesMoneOpe>Guarani</dDesMoneOpe>
      </gOpeCom>
      <gEmis>...</gEmis>
      <gDatRec>...</gDatRec>
    </gDatGralOpe>
    <!-- E: Específico FE -->
    <gDtipDE>
      <gCamFE>
        <iIndPres>1</iIndPres>
        <dDesIndPres>Operación presencial</dDesIndPres>
      </gCamFE>
      <gCamCond>
        <iCondOpe>1</iCondOpe>
        <dDCondOpe>Contado</dDCondOpe>
        <!-- Formas de pago -->
      </gCamCond>
      <gCamItem>...</gCamItem>
    </gDtipDE>
    <!-- F: Totales -->
    <gTotSub>...</gTotSub>
  </DE>
  <Signature>...</Signature>
  <gCamFuFD>
    <dCarQR>[URL_QR]</dCarQR>
  </gCamFuFD>
</rDE>
```
