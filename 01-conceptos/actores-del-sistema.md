> **Fuente:** Manual Técnico SIFEN v150, secciones 4.1, 6.3, 6.4, 6.6 y 7.5

> **Nota:** Este documento refleja el MT v150 con cambios del historial de versiones marcados.

# Actores del Sistema SIFEN

Descripción de los actores que intervienen en el Sistema Integrado de Facturación Electrónica Nacional.

---

## 1. SET / DNIT — Administración Tributaria

### Rol
La Subsecretaría de Estado de Tributación (SET) es el actor central del SIFEN. Actúa como Administración Tributaria (AT) y es responsable de la operación, reglamentación y fiscalización del sistema.

### Responsabilidades
- Reglamentar los requisitos técnicos, condiciones y procedimientos del SIFEN mediante el Manual Técnico y las Resoluciones correspondientes.
- Recepcionar los Documentos Electrónicos (DE) enviados por los facturadores electrónicos.
- Ejecutar las validaciones (de conexión, técnicas y de negocio) sobre cada DE.
- Otorgar la aprobación de uso del DTE cuando el DE supera todas las validaciones.
- Almacenar los DTE aprobados y proveer los servicios de consulta pública y por Web Service.
- Gestionar el Registro Único del Contribuyente (RUC) a través de Marangatu.
- Otorgar el timbrado electrónico a los facturadores autorizados.
- Emitir y distribuir el Código de Seguridad del Contribuyente (CSC) para la generación del código QR.
- Proveer la solución gratuita **Ekuatia'i** para contribuyentes de bajo volumen.
- **[MODIFICADO]** Establecer un tiempo máximo de respuesta de validación de 1 (un) minuto, con objetivo de reducirlo en el futuro a menos de 2 (dos) segundos por DTE.

### Subsistemas que opera
1. **[MODIFICADO] Subsistema de Aprobación (Validación)**: orientado en especial a grandes y medianos contribuyentes. Opera con modelo de validación posterior (hasta 72 h) o previa (en tiempo real antes de la entrega al receptor).
2. **[MODIFICADO] Subsistema Solución Gratuita Ekuatia'i**: orientado a contribuyentes con baja emisión de documentos. Transacciones en tiempo real. Contempla firma digital por la SET o por el contribuyente, según el segmento.

### Marco legal de la SET
- Ley N° 125/1991 — Nuevo Régimen Tributario
- Decreto N° 7.795/2017 — Crea el SIFEN
- **[MODIFICADO]** Resolución General Reglamentaria N° 05/2018 — Reglamenta el SIFEN
- **[MODIFICADO]** Resolución General Reglamentaria Futura — Para la etapa de voluntariedad

---

## 2. Facturador Electrónico (Emisor)

### Rol
Contribuyente de IVA autorizado por la AT para emitir y recibir Documentos Tributarios Electrónicos. Puede adherirse voluntariamente o ser seleccionado de manera obligatoria por la SET.

### Responsabilidades
- Adaptar sus sistemas de facturación conforme a los requisitos técnicos del MT.
- Generar el Documento Electrónico (DE) en formato XML según los esquemas XSD del SIFEN.
- Firmar digitalmente cada DE con el certificado digital correspondiente a su RUC **antes** de entregarlo al receptor.
- **[MODIFICADO]** Entregar el DE al receptor como regla general de manera previa a la transmisión al SIFEN, enviando el XML o el KuDE según corresponda.
  - Si el receptor no es facturador electrónico, debe enviar o disponibilizar el KuDE (en formato físico o digital).
- Transmitir los DE firmados al SIFEN dentro de los plazos establecidos (regla general: hasta 72 horas desde la firma digital).
- Reutilizar el CDC del DE rechazado cuando los ajustes necesarios no alteren su construcción.
- Inutilizar el número de comprobante cuando los cambios alteren el CDC.
- Gestionar y registrar los eventos sobre los DTE (cancelación, inutilización, etc.) dentro de los plazos correspondientes.
- Mantener la relación directa con la SET, sin intermediación obligatoria.

### Medios de entrega del DE al receptor
- **[MODIFICADO]** Archivo adjunto transmitido por correo electrónico o aplicaciones.
- Descarga por el receptor en página web expuesta por el emisor.
- **[MODIFICADO]** Archivo adjunto transmitido por aplicativo de mensajería electrónica de datos.

### Certificado digital requerido
El emisor debe poseer un certificado digital emitido por un PSC habilitado por el MIC, estándar X.509 v3, tipo F1 o F2:
- Para **firma de mensajes de datos**: **[MODIFICADO]** el certificado debe contener el RUC del contribuyente emisor y la clave para función de firma digital.
- Para **establecimiento de conexiones y autenticaciones mutuas**: **[MODIFICADO]** el certificado debe contener el RUC del contribuyente emisor, con la extensión Extended Key Usage con el permiso `clientAuth`.

---

## 3. Receptor

### Rol
Destinatario del Documento Tributario Electrónico. Puede ser:
- Un facturador electrónico (recibe el DE en XML).
- Un contribuyente de IVA o renta que no es facturador electrónico (recibe el KuDE).
- Un consumidor final (recibe el KuDE).

### Responsabilidades
- **[MODIFICADO]** En el modelo de aprobación posterior: verificar a posteriori, en los servicios de consulta del SIFEN, que el DTE (luego de aprobado el DE) se encuentre conforme a la operación comercial realizada. En específico debe verificar:
  - **[MODIFICADO]** Que el DE fue transmitido y obtuvo la aprobación como DTE.
  - **[MODIFICADO]** Que la información presente en el KuDE coincide plenamente con la información del DTE consultado.
- **[NUEVO en v150]** Consultar y/o comprobar la existencia del DTE en el SIFEN, utilizando campos del KuDE como criterios de consulta (CDC, código QR).
- Registrar eventos de receptor (Notificación de Recepción, Conformidad, Disconformidad, Desconocimiento) dentro de los plazos establecidos.

### Medios de verificación disponibles
- Servicio web de consulta CDC (WS siConsDE).
- Página web del portal SIFEN mediante código QR del KuDE.
- Ingreso manual del CDC en el portal.

---

## 4. Proveedores de Servicios de Certificación (PSC)

### Rol
Entidades autorizadas por el Ministerio de Industria y Comercio (MIC) para emitir certificados digitales válidos en Paraguay.

### Responsabilidades
- Emitir certificados digitales X.509 v3 (tipo F1 por software o F2 por hardware) a personas físicas y jurídicas.
- Mantener y publicar la Lista de Certificados Revocados (LCR).
- Responder a consultas de validación de certificados en tiempo real.

### Interoperabilidad con SIFEN
El SIFEN consulta automáticamente la LCR de los PSC al momento de validar cada DE. No es necesario que el contribuyente adjunte la LCR al firmar el documento.

Referencia: https://www.acraiz.gov.py/html/Certif_1PrestaServ.html

---

## 5. Proveedores Tecnológicos (Opcionales)

### Rol
Prestadores de servicios tecnológicos que pueden asistir a los contribuyentes facturadores electrónicos en la implementación y operación de sus sistemas.

### Característica clave
- **La relación con la SET siempre es directa con el contribuyente**, independientemente del uso de proveedores tecnológicos.
- El modelo operativo de SIFEN entiende la interacción SET–facturador como directa, sin necesidad de intermediación obligatoria.
- A discreción y decisión del contribuyente, este puede acudir a estos servicios.

---

## Diagrama de relaciones

```
                  ┌──────────────────┐
                  │   SET / DNIT     │
                  │ (AT - SIFEN)     │
                  └────────┬─────────┘
                           │ WS SIFEN
                           │ (HTTPS/TLS 1.2)
          ┌────────────────┼────────────────┐
          │                │                │
   ┌──────┴──────┐  ┌──────┴──────┐  ┌─────┴──────┐
   │  Facturador │  │  Marangatu  │  │    PSC     │
   │ Electrónico │  │  (RUC/Timb) │  │ (Certif.)  │
   │  (Emisor)   │  └─────────────┘  └────────────┘
   └──────┬──────┘
          │ DE (XML) o KuDE
          ▼
   ┌─────────────┐
   │  Receptor   │
   └─────────────┘
```
