# Nota de Remisión Electrónica (NRE)

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4, grupo E6 y E10

## Identificación

| Atributo | Valor |
|----------|-------|
| **Código C002** | 7 |
| **Descripción C003** | "Nota de remisión electrónica" |
| **Campo XML principal** | `gCamNRE` |
| **Rango de campos específicos** | E500-E599 |
| **Transporte** | E900-E999 (obligatorio) |

## Descripción

La Nota de Remisión Electrónica es el documento que ampara el traslado de mercaderías. No lleva condición de operación (no es una transacción comercial directa), pero requiere información detallada sobre el transporte.

**Base legal:** Resolución General N° 41/2014, Art. 3 Inc. 7.

## Particularidades

- **Sin operación comercial:** No requiere grupo `gOpeCom` (D010 no se informa, C002=7).
- **Campo dInfoFisc obligatorio:** El campo B006 (dInfoFisc) debe contener el mensaje según Art. 3 Inc. 7 de la RG N° 41/2014.
- **Receptor = Emisor:** Cuando el motivo es por operaciones internas de la empresa (códigos 7, 8, 9), el RUC del receptor debe ser igual al RUC del emisor.
- **Campos de transporte obligatorios:** El grupo E10 (E900-E999) debe ser informado.

## Campos Específicos (E500-E599)

| ID | Campo | Tipo | Longitud | Ocurrencia | Descripción | Observaciones |
|----|-------|------|----------|------------|-------------|---------------|
| E500 | gCamNRE | G | - | 0-1 | Grupo NRE | Obligatorio si C002=7 |
| E501 | iMotEmiNR | N | 1-2 | 1-1 | Motivo de emisión | Ver tabla abajo |
| E502 | dDesMotEmiNR | A | 5-60 | 1-1 | Descripción del motivo | Ref. E501 |
| E503 | iRespEmiNR | N | 1 | 1-1 | Responsable de emisión | Ver tabla abajo |
| E504 | dDesRespEmiNR | A | 20-36 | 1-1 | Descripción responsable | Ref. E503 |
| E505 | dKmR | N | 1-5 | 1-1 | Kilómetros estimados de recorrido | Obligatorio según NT-010 |
| E506 | dFecEm | F | 10 | 0-1 | Fecha futura emisión de la factura | Cuando no se ha emitido FE aún |

## Motivos de Emisión (E501)

| Código | Descripción |
|--------|-------------|
| 1 | Traslado por venta |
| 2 | Traslado por consignación |
| 3 | Exportación |
| 4 | Traslado por compra |
| 5 | Importación |
| 6 | Traslado por devolución |
| 7 | Traslado entre locales de la empresa |
| 8 | Traslado de bienes por transformación |
| 9 | Traslado de bienes por reparación |
| 10 | Traslado por emisor móvil |
| 11 | Exhibición o demostración |
| 12 | Participación en ferias |
| 13 | Traslado de encomienda |
| 14 | Decomiso |
| 99 | Otro (describir expresamente) |

## Responsable de Emisión (E503)

| Código | Descripción |
|--------|-------------|
| 1 | Emisor de la factura |
| 2 | Poseedor de la factura y bienes |
| 3 | Empresa transportista |
| 4 | Despachante de Aduanas |
| 5 | Agente de transporte o intermediario |

## Campos de Transporte (E900-E999)

### Grupo Principal E10

| ID | Campo | Tipo | Longitud | Ocurrencia | Descripción |
|----|-------|------|----------|------------|-------------|
| E903 | iModTrans | N | 1 | 1-1 | Modalidad del transporte (1=Terrestre, 2=Fluvial, 3=Aéreo, 4=Multimodal) |
| E904 | dDesModTrans | A | 6-12 | 1-1 | Descripción modalidad |
| E905 | iRespFlete | N | 1 | 1-1 | Responsable del flete (1=Emisor, 2=Receptor, 3=Tercero) |

### Local de Salida (E920-E939)

| ID | Campo | Descripción |
|----|-------|-------------|
| E920 | gCamSal | Grupo local de salida |
| E921 | dDirSal | Dirección de salida |
| E922 | dNumCasSal | Número de casa salida |
| E923 | cDepSal | Código departamento salida |
| E924 | dDesDepSal | Descripción departamento salida |
| E925 | cDisSal | Código distrito salida |
| E926 | dDesDisSal | Descripción distrito salida |
| E927 | cCiuSal | Código ciudad salida |
| E928 | dDesCiuSal | Descripción ciudad salida |

### Local de Entrega (E940-E959)

| ID | Campo | Descripción |
|----|-------|-------------|
| E940 | gCamEnt | Grupo local de entrega |
| E941 | dDirEnt | Dirección de entrega |
| E942 | dNumCasEnt | Número de casa entrega |
| E943 | cDepEnt | Código departamento entrega |
| E944 | dDesDepEnt | Descripción departamento |
| E945 | cDisEnt | Código distrito entrega |
| E946 | dDesDisEnt | Descripción distrito |
| E947 | cCiuEnt | Código ciudad entrega |
| E948 | dDesCiuEnt | Descripción ciudad |

### Vehículo (E960-E979)

| ID | Campo | Descripción | Observaciones |
|----|-------|-------------|---------------|
| E961 | gVehTras | Grupo vehículo | |
| E962 | dTipIden | Tipo de identificación | 1=Número de chasis, 2=Número matrícula |
| E965 | dNroMatVeh | Número de matrícula | Obligatorio si E967=2 (NT-005) |
| E966 | dMarcVeh | Marca del vehículo | |
| E967 | iTipVeh | Tipo de vehículo | Según Tabla 9 |

### Transportista (E980-E999)

Según NT-010, el grupo `gCamTrans` (E980) es:
- Obligatorio si C002=7
- No informar si C002=4, 5, 6
- Opcional cuando E903=1 y E967=1

| ID | Campo | Descripción | Observaciones |
|----|-------|-------------|---------------|
| E980 | gCamTrans | Grupo transportista | |
| E981 | iNatTrans | Naturaleza del transportista | 1=Contribuyente, 2=No contribuyente |
| E982 | dRucTrans | RUC del transportista | Si E981=1 |
| E989 | dNomTrans | Nombre del transportista | |
| E990 | dNumHabTrans | Número habilitación MOPC | |
| E991 | dNomChofer | Nombre del chofer | |
| E992 | dDomFisc | Domicilio fiscal transportista | Obligatorio por RG N° 41/2014 (NT-010) |
| E993 | dDirChof | Dirección del chofer | Obligatorio por RG N° 41/2014 (NT-010) |
| E994 | dCiudChofer | Ciudad del chofer | |

## Ítems en NRE

En la NRE, los campos `gValorItem` (E720) son opcionales (no informar si C002=7). Los ítems describen las mercaderías trasladadas pero no necesariamente sus precios.

## Campos de Rastreo de Mercadería (E750-E761)

| ID | Campo | Descripción | Observaciones |
|----|-------|-------------|---------------|
| E750 | gCamRasMerc | Grupo rastreo | |
| E751 | dNumLote | Número de lote | Obligados por RG N° 106/2021 – Agroquímicos |
| E756 | dNomImp | Nombre del importador | Obligados por RG N° 16/2019 |
| E757 | dDirImp | Dirección del importador | Obligados por RG N° 16/2019 |
| E758 | dNumFir | Número registro firma importador | Obligados por RG N° 16/2019 |
| E759 | dNumReg | Número registro producto (SENAVE) | Obligados por RG N° 106/2021 |
| E760 | dNumRegEntCom | Número registro entidad comercial (SENAVE) | Obligados por RG N° 106/2021 |
| E761 | dNomPro | Nombre del producto | Obligados por RG N° 106/2021 |

## Eventos Disponibles para NRE

| Evento | Actor | Plazo | Método |
|--------|-------|-------|--------|
| Cancelación | Emisor | 168 horas (7 días) desde aprobación | WS siRecepEvento |
| Actualización datos transporte | Emisor | - | WS siRecepEvento (GET) |
| Notificación recepción | Receptor | 45 días desde emisión | WS/Portal |
| Conformidad | Receptor | 45 días desde emisión | WS/Portal |
| Disconformidad | Receptor | 45 días desde emisión | WS/Portal |
| Desconocimiento | Receptor | 45 días desde emisión | WS/Portal |

### Evento de Actualización de Datos del Transporte (GET)

Permite modificar:
- GET003=1: Cambio del local de entrega
- GET003=2: Cambio del chofer
- GET003=3: Cambio del transportista
- GET003=4: Cambio de vehículo
