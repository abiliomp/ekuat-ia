# Actores del Sistema SIFEN

> **Fuente:** Manual Técnico SIFEN v150, secciones 1-6 y 16

## Visión General

El SIFEN involucra a múltiples actores que interactúan entre sí para la generación, transmisión, validación y consulta de Documentos Electrónicos.

---

## 1. SET / DNIT (Administración Tributaria)

**Nombre completo:** Subsecretaría de Estado de Tributación (SET) / Dirección Nacional de Ingresos Tributarios (DNIT)

**Rol:** Autoridad tributaria central del sistema.

**Responsabilidades:**
- Administrar y operar el SIFEN.
- Aprobar o rechazar los Documentos Electrónicos transmitidos.
- Emitir y administrar los timbrados de los facturadores electrónicos.
- Publicar y mantener los Schemas XSD y el Manual Técnico.
- Otorgar el Código Secreto del Contribuyente (CSC) para la generación del QR.
- Disponibilizar los Web Services para la transmisión de DE y consultas.
- Mantener el portal e-Kuatia para consultas públicas.
- Registrar eventos automáticos (asociaciones, anulaciones).
- Impugnar DTE cuando se compruebe falta de veracidad (evento futuro).

**URLs relevantes:**
- Portal público: `https://ekuatia.set.gov.py/consultas/`
- Portal test: `https://ekuatia.set.gov.py/consultas-test/`
- Prevalidador: `https://ekuatia.set.gov.py/prevalidador/`
- Documentación técnica: `https://www.dnit.gov.py/web/e-kuatia/documentacion-tecnica`

---

## 2. Facturador Electrónico (Emisor)

**Definición:** Contribuyente autorizado por la Administración Tributaria para emitir y recibir DTE. Adquiere simultáneamente la naturaleza de emisor y receptor.

**Tipos de facturadores:**
- **Subsistema de Aprobación:** Contribuyentes grandes y medianos que desarrollan su propio sistema de facturación.
- **Solución Gratuita Ekuatia'i:** Pequeños contribuyentes que utilizan la solución provista por la SET.

**Responsabilidades:**
- Generar los Documentos Electrónicos (DE) conforme al formato XML definido.
- Firmar digitalmente cada DE con su certificado digital.
- Transmitir los DE al SIFEN dentro del plazo de 72 horas desde la firma.
- Generar el CDC único para cada DE.
- Generar y entregar el KuDE al receptor.
- Registrar eventos (cancelaciones, inutilizaciones).
- Conservar los DTE por 5 años.
- Verificar el estado de los DTE transmitidos.

**Obligaciones técnicas:**
- Poseer conexión a Internet de banda ancha.
- Desarrollar software cliente compatible con los WS del SIFEN.
- Obtener certificado digital de un PSC habilitado.
- Sincronizar el horario con los servidores NTP de la SET.

---

## 3. Receptor

**Definición:** Persona física o jurídica a quien se emite un Documento Electrónico.

**Tipos:**
- **Receptor contribuyente** (D201=1): Tiene RUC. Puede ser facturador electrónico o no.
- **Receptor no contribuyente** (D201=2): Persona física o jurídica sin RUC (consumidor final).

**Derechos y obligaciones:**
- Verificar la existencia del DTE en el SIFEN (obligación para ejercer derechos tributarios).
- Puede verificar mediante: consulta por CDC, lectura del QR, o portal e-Kuatia.
- Registrar eventos de receptor: Notificación de recepción, Conformidad, Disconformidad, Desconocimiento.
- Plazo máximo para registrar eventos: 45 días desde la fecha de emisión.

**Verificación obligatoria:**
El receptor debe confirmar:
1. Que el DE fue transmitido y obtuvo aprobación como DTE.
2. Que la información del KuDE coincide con el DTE consultado en SIFEN.

---

## 4. Proveedores de Servicios de Certificación (PSC)

**Definición:** Entidades habilitadas por el Ministerio de Industria y Comercio (MIC) para emitir certificados digitales en Paraguay.

**Base legal:** Ley N° 4017 de Firma Digital.

**Funciones:**
- Emitir certificados digitales Tipo F1 (por software) y Tipo F2 (por hardware).
- Emitir certificados para persona física y persona jurídica.
- Mantener la Lista de Certificados Revocados (LCR).
- Operar como parte de la cadena de confianza del SIFEN.

**Requisitos del certificado para SIFEN:**
- Persona jurídica: El RUC del contribuyente debe estar en el campo Subject/SerialNumber (OID: 2.5.4.5).
- Persona física: El RUC debe estar en SubjectAlternativeName/SerialNumber (OID: 2.5.4.5).
- Formato del RUC: `RUCXXXXXXXXX-X` (sin espacios, con guion antes del DV).
- Para autenticación TLS: Debe incluir la extensión Extended Key Usage con permiso `clientAuth`.

**Directorio de PSC:** `https://www.acraiz.gov.py/html/Certif_1PrestaServ.html`

---

## 5. Proveedores de Certificación (Terceros/Integradores)

**Definición:** Empresas que brindan servicios de integración y certificación para facturadores electrónicos que optan por tercerizar su sistema de FE.

**Rol en el modelo:**
- Actúan como intermediarios tecnológicos entre el emisor y el SIFEN.
- Pueden operar el sistema de FE en nombre del contribuyente emisor.
- La responsabilidad tributaria siempre recae en el facturador electrónico (emisor).

---

## 6. Interacción entre Actores

```
Facturador Electrónico (Emisor)
        |
        | 1. Genera DE (XML)
        | 2. Firma digitalmente (PSC)
        | 3. Entrega KuDE al receptor
        | 4. Transmite DE al SIFEN (WS)
        v
      SIFEN (SET/DNIT)
        |
        | 5. Valida DE
        | 6. Aprueba → DTE
        | 7. Registra en base de datos
        |
        v
     Receptor
        |
        | 8. Recibe KuDE
        | 9. Verifica DTE en SIFEN
        | 10. Registra eventos (opcional)
```

## 7. Tipos de Operación por Actor

| Código D202 | Tipo | Descripción |
|-------------|------|-------------|
| 1 | B2B | Empresa a Empresa |
| 2 | B2C | Empresa a Consumidor Final |
| 3 | B2G | Empresa a Gobierno |
| 4 | B2F | Empresa a Extranjero |
