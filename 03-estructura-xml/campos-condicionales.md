# Campos Condicionales del Documento Electrónico

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4

## Descripción

Los campos condicionales son aquellos cuya obligatoriedad o ausencia depende del valor de otro campo. Este documento resume las principales reglas de condicionalidad.

---

## Condiciones por Tipo de Documento (C002)

| Campo | Condición | Regla |
|-------|-----------|-------|
| gOpeCom (D010) | C002=7 (NRE) | NO informar el grupo gOpeCom |
| gOpeCom (D010) | C002≠7 | Obligatorio |
| iTipTra (D011) | C002=1 o C002=4 (FE o AFE) | Obligatorio |
| iTipTra (D011) | C002≠1 y C002≠4 | No informar (NT-006) |
| gCamFE (E010) | C002=1 (FE) | Obligatorio |
| gCamFE (E010) | C002≠1 | No informar |
| gCamAE (E300) | C002=4 (AFE) | Obligatorio |
| gCamAE (E300) | C002≠4 | No informar |
| gCamNCDE (E400) | C002=5 o C002=6 (NCE/NDE) | Obligatorio |
| gCamNCDE (E400) | C002≠5 y C002≠6 | No informar |
| gCamNRE (E500) | C002=7 (NRE) | Obligatorio |
| gCamNRE (E500) | C002≠7 | No informar |
| gCamCond (E600) | C002=1 o C002=4 (FE o AFE) | Obligatorio |
| gCamCond (E600) | C002≠1 y C002≠4 | No informar |
| gValorItem (E720) | C002≠7 | Obligatorio |
| gValorItem (E720) | C002=7 (NRE) | No informar |
| dInfoFisc (B006) | C002=7 (NRE) | Obligatorio (mensaje Art. 3 Inc. 7 RG 41/2014) |
| dDirRec (D213) | C002=7 o D202=4 | Obligatorio |
| iTiDE (C002) = 4 | D015 | Debe ser PYG (NT-012) |

---

## Condiciones por Naturaleza del Receptor (D201)

| Campo | Condición | Regla |
|-------|-----------|-------|
| iTiContRec (D205) | D201=1 (contribuyente) | Obligatorio |
| iTiContRec (D205) | D201=2 (no contribuyente) | No informar |
| dRucRec (D206) | D201=1 | Obligatorio |
| dRucRec (D206) | D201=2 | No informar |
| dDVRec (D207) | D206 existe | Obligatorio |
| iTipIDRec (D208) | D201=2 y D202≠4 | Obligatorio |
| iTipIDRec (D208) | D201=1 | No informar |
| dNumIDRec (D210) | D201=2 y D202≠4 | Obligatorio. "0" si innominado |
| dNumIDRec (D210) | D201=1 | No informar |

---

## Condiciones por Tipo de Operación (D202)

| Campo | Condición | Regla |
|-------|-----------|-------|
| iTiOpe (D202) | D206 = RUC de OEE | Debe ser B2G (D202=3) (NT-020) |
| dDirRec (D213) | D202=4 | Obligatorio |
| cDepRec (D219) | D213 informado y D202≠4 | Obligatorio (NT-003) |
| cCiuRec (D223) | D213 informado y D202≠4 | Obligatorio (NT-003) |
| cDepRec (D219) | D202=4 | No informar |
| cCiuRec (D223) | D202=4 | No informar |
| gCompPub (E020) | D202=3 (B2G) | Opcional (NT-026 lo hizo opcional) |
| dDncpG (E704) | D202=3 | Opcional (NT-026) |
| dDncpE (E705) | E704 informado | Obligatorio si E704 informado |

---

## Condiciones por Tipo de Cambio (D015/D017)

| Campo | Condición | Regla |
|-------|-----------|-------|
| dCondTiCam (D017) | D015≠PYG | Obligatorio |
| dCondTiCam (D017) | D015=PYG | No informar |
| dTiCam (D018) | D017=1 (global) | Obligatorio |
| dTiCam (D018) | D017=2 o D015=PYG | No informar |
| dTotalGs (F023) | D015=PYG | No informar |
| dTotalGs (F023) | D015≠PYG y D017=1 | F014*D018 |
| dTotalGs (F023) | D015≠PYG y D017=2 | Suma de EA009 |
| dTiCamTiPag (E611) | E609≠PYG | Obligatorio |

---

## Condiciones de Pago (E601)

| Campo | Condición | Regla |
|-------|-----------|-------|
| gPaConEIni (E605) | E601=1 (contado) | Obligatorio |
| gPaConEIni (E605) | E645 (entrega inicial) existe | Obligatorio |
| gPagCred (E640) | E601=2 (crédito) | Obligatorio |
| gPagCred (E640) | E601≠2 | No informar |
| dPlazoCre (E643) | E641=1 (plazo) | Obligatorio |
| dCuotas (E644) | E641=2 (cuota) | Obligatorio |
| gCuotas (E650) | E641=2 | Se activa |
| gPagTarCD (E620) | E606=3 o E606=4 | Se activa (tarjeta crédito/débito) |
| gPagCheq (E630) | E606=2 | Se activa (cheque) |

---

## Condiciones del IVA (E731-E737)

| Campo | Condición | Regla |
|-------|-----------|-------|
| dPropIVA (E733) | E731=4 (gravado parcial) | Porcentaje gravado (no 100%) |
| dBasGravIVA (E735) | E731=1 o E731=4 | Calculado: [100*EA008*E733]/[10000+(E734*E733)] (NT-013) |
| dBasGravIVA (E735) | E731=2 o E731=3 | Igual a 0 |
| dBasExe (E737) | E731=4 | Calculado: [100*EA008*(100-E733)]/[10000+(E734*E733)] (NT-013) |
| dBasExe (E737) | E731=1, 2 o 3 | Igual a 0 |

---

## Condiciones del Anticipo (D019)

| Campo | Condición | Regla |
|-------|-----------|-------|
| iCondAnt (D019) | 1=Anticipo Global | Un solo tipo de anticipo para todo el DE |
| iCondAnt (D019) | 2=Anticipo por ítem | Distribución de anticipos por ítem |
| dCDCAnticipo (E719) | D011=9 (anticipo) en FE asociada | Obligatorio |

---

## Condiciones por Tipo de Documento Innominado (D208=5)

| Campo | Condición | Regla |
|-------|-----------|-------|
| iTipIDRec (D208) | Operaciones ≥ 35.000.000 PYG o equivalente | No puede ser Innominado (D208≠5), salvo D011=13 (NT-021) |
| iTipIDRec (D208) | Operaciones ≥ 7.000.000 PYG o equivalente | Actualizado en NT-024 a partir del 01/01/2025 |

---

## Condiciones del Responsable de Generación (D140-D160)

| Campo | Condición | Regla |
|-------|-----------|-------|
| gRespDE (D140) | - | Opcional en todos los DE |
| Todos los campos D141-D145 | D140 existe | Obligatorios |

---

## Condiciones de la Numeración con Serie (C010)

| Campo | Condición | Regla |
|-------|-----------|-------|
| dSerieNum (C010) | Numeración 0000001-9999999 no agotada | No informar (ocurrencia 0-1) |
| dSerieNum (C010) | Numeración agotada | Obligatorio. Orden: AA, AB, ..., ZZ |

---

## Condiciones del Grupo de Transporte (E900)

| Campo | Condición | Regla |
|-------|-----------|-------|
| gCamTrans (E980) | C002=7 (NRE) | Obligatorio |
| gCamTrans (E980) | C002=4, 5, 6 | No informar |
| gCamTrans (E980) | E903=1 y E967=1 | Opcional |
| dNroMatVeh (E965) | E967=2 (identificado por matrícula) | Obligatorio (NT-005) |
| dKmR (E505) en NRE | NT-010 | Obligatorio (anteriormente opcional) |

---

## Condiciones para Datos de Agroquímicos (E750-E761)

| Campo | Condición | Regla |
|-------|-----------|-------|
| dNumLote (E751) | Agroquímicos | Obligatorio por RG N° 106/2021 |
| dNomImp (E756) | Agroquímicos | Obligatorio por RG N° 16/2019 |
| dDirImp (E757) | Agroquímicos | Obligatorio por RG N° 16/2019 |
| dNumFir (E758) | Agroquímicos | Obligatorio por RG N° 16/2019 |
| dNumReg (E759) | Agroquímicos | Obligatorio por RG N° 106/2021 |
| dNumRegEntCom (E760) | Agroquímicos | Obligatorio por RG N° 106/2021 |
| dNomPro (E761) | Agroquímicos | Obligatorio por RG N° 106/2021 |
