# Tipos de Documento Electrónico (C002 / iTiDE)

Campo `iTiDE` (C002): identifica el tipo de Documento Electrónico. Es parte del grupo de datos del timbrado y forma parte del CDC (Código de Control).

> **Fuente:** Manual Técnico SIFEN v150, sección 10.4 (campo C002)
> **Nota:** Contenido tachado (~~así~~) indica especificaciones eliminadas en v150. [MODIFICADO] indica cambios. [NUEVO] indica adiciones.

## Definición del campo

| Atributo    | Valor |
|-------------|-------|
| ID          | C002  |
| Nombre XML  | iTiDE |
| Tipo        | N (numérico) |
| Longitud    | 1–2  |
| Ocurrencia  | 1-1 (obligatorio) |
| Nodo padre  | C001  |

El campo complementario `dDesTiDE` (C003) contiene la descripción textual del tipo, y debe coincidir exactamente con el código informado en C002.

---

## Tabla de Tipos de Documento

| Código | Abreviatura | Nombre completo | Descripción / uso principal | Observación |
|--------|-------------|-----------------|----------------------------|-------------|
| [MODIFICADO] 1 | FE | Factura Electrónica | Respalda compraventa de bienes y servicios. Aplica para operaciones B2B, B2C, B2G y [NUEVO] B2F. Admite condición contado y crédito. | Grupo E010 obligatorio. [MODIFICADO] iTipTra es obligatorio. |
| [MODIFICADO] 2 | FEE | Factura Electrónica de Exportación | Para exportaciones de bienes y servicios al exterior. | [MODIFICADO] **(Futuro)** — no implementar como disponible en producción. Campos E100–E199. |
| [MODIFICADO] 3 | FEI | Factura Electrónica de Importación | Para importaciones de bienes y servicios. | [MODIFICADO] **(Futuro)** — no implementar como disponible en producción. Campos E200–E299. |
| 4 | AFE | Autofactura Electrónica | Emitida por el comprador en nombre del vendedor no contribuyente. Siempre condición contado. RUC receptor = RUC emisor. | [MODIFICADO] Campos E300–E399 completamente redefinidos en v150. |
| 5 | NCE | Nota de Crédito Electrónica | Reduce el valor de una FE aprobada (devoluciones, descuentos, bonificaciones). | Documento asociado obligatorio (H001). |
| 6 | NDE | Nota de Débito Electrónica | Aumenta el valor de una FE aprobada (intereses, diferencias de precio). | Documento asociado obligatorio (H001). |
| [MODIFICADO] 7 | NRE | Nota de Remisión Electrónica | Ampara el traslado físico de mercaderías. No lleva grupo de operación comercial (D010). | [MODIFICADO] En v150 cuenta con campos propios E500–E599 y grupo de transporte E900 obligatorio. |
| [MODIFICADO] 8 | CRE | Comprobante de Retención Electrónico | Respalda retenciones practicadas por agentes de retención. | [MODIFICADO] **(Futuro)** — no implementar como disponible en producción. |

### Tipos eliminados en v150

Los tipos FEE (2), FEI (3) y CRE (8) existían en versiones anteriores del MT con definición propia, pero en v150 están marcados explícitamente como **(Futuro)**. Deben considerarse **no operativos** en producción actual.

---

## Impacto del C002 en la estructura del DE

| C002 | Grupo obligatorio | Grupo prohibido / no aplica |
|------|-------------------|------------------------------|
| 1 (FE)  | E010 (gCamFE), D010 (operación comercial) | E300, E400, E500 |
| 4 (AFE) | E300 (gCamAFE), E600 (condición operación), H001 (doc. asociado) | E010, E400, E500 |
| 5 (NCE) | E400 (gCamNCDE), H001 (doc. asociado) | E010, E300, E500, E600 |
| 6 (NDE) | E400 (gCamNCDE), H001 (doc. asociado) | E010, E300, E500, E600 |
| 7 (NRE) | E500 (gCamNRE), E900 (transporte) | E010, E300, E400, E600, D010 |

---

## Denominación en el KuDE

Según la sección 13.3, cada tipo de DE tiene su denominación en la representación gráfica:

- **C002=1:** "KuDE de Factura Electrónica"
- **C002=4:** "KuDE de Autofactura Electrónica"
- **C002=5:** "KuDE de Nota de Crédito Electrónica"
- **C002=6:** "KuDE de Nota de Débito Electrónica"
- **C002=7:** "KuDE de Nota de Remisión Electrónica"
