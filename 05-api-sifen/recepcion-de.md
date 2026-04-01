# Recepción Sincrónica de DE (siRecepDE)

> **Fuente:** Manual Técnico SIFEN v150, sección 7.6

## Descripción

El WS `siRecepDE` permite enviar un único Documento Electrónico al SIFEN de forma **sincrónica**: el resultado de aprobación o rechazo se devuelve en la misma llamada HTTP. Es ideal para sistemas que requieren confirmación inmediata.

---

## Características

| Atributo | Valor |
|----------|-------|
| **Tipo** | Síncrono |
| **Cantidad de DE por llamada** | 1 |
| **Respuesta** | Inmediata en la misma llamada |
| **Método SOAP** | `rRecepDE` |
| **WS** | `siRecepDE` |

---

## Endpoints

| Ambiente | URL |
|----------|-----|
| Pruebas | `https://sifen-test.set.gov.py/de/ws/sync/recepcion.wsdl` |
| Producción | `https://sifen.set.gov.py/de/ws/sync/recepcion.wsdl` |

---

## Estructura del Request

```xml
<soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope">
  <soapenv:Header/>
  <soapenv:Body>
    <rEnviDE>
      <dId>1</dId>     <!-- Número correlativo del request -->
      <xDE>
        <!-- Contenido completo del DE firmado (XML del rDE) -->
        <rDE xmlns="http://ekuatia.set.gov.py/sifen/xsd" ...>
          <dVerFor>150</dVerFor>
          <DE Id="[CDC_44_DIGITOS]">
            <!-- ... todos los campos del DE ... -->
          </DE>
          <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
            <!-- ... firma digital ... -->
          </Signature>
          <gCamFuFD>
            <dCarQR>[URL_QR]</dCarQR>
          </gCamFuFD>
        </rDE>
      </xDE>
    </rEnviDE>
  </soapenv:Body>
</soapenv:Envelope>
```

### Campos del Request

| Campo | Tipo | Descripción |
|-------|------|-------------|
| dId | N | Identificador correlativo del request (asignado por el emisor) |
| xDE | XML | El DE firmado completo (elemento `<rDE>` con todos sus hijos) |

---

## Estructura de la Response

### DE Aprobado

```xml
<soapenv:Envelope ...>
  <soapenv:Body>
    <rRetEnviDE>
      <dId>1</dId>
      <gResProcDE>
        <dCodRes>0302</dCodRes>
        <dMsgRes>Aprobado</dMsgRes>
        <dFecProc>2024-01-15T10:30:00</dFecProc>
        <Id>[CDC_44_DIGITOS]</Id>
        <gResOK>
          <dProtAut>[PROTOCOLO_DE_AUTORIZACION]</dProtAut>
        </gResOK>
      </gResProcDE>
    </rRetEnviDE>
  </soapenv:Body>
</soapenv:Envelope>
```

### DE Rechazado

```xml
<soapenv:Envelope ...>
  <soapenv:Body>
    <rRetEnviDE>
      <dId>1</dId>
      <gResProcDE>
        <dCodRes>0304</dCodRes>
        <dMsgRes>Rechazado</dMsgRes>
        <dFecProc>2024-01-15T10:30:00</dFecProc>
        <Id>[CDC_44_DIGITOS]</Id>
        <gResNOk>
          <dMotRec>Motivo de rechazo</dMotRec>
          <gDetMotErr>
            <dCodErr>R001</dCodErr>
            <dMsgErr>Descripción detallada del error</dMsgErr>
          </gDetMotErr>
        </gResNOk>
      </gResProcDE>
    </rRetEnviDE>
  </soapenv:Body>
</soapenv:Envelope>
```

### DE Aprobado con Observaciones

```xml
<gResProcDE>
  <dCodRes>0306</dCodRes>
  <dMsgRes>Aprobado con observaciones</dMsgRes>
  <gResOK>
    <dProtAut>[PROTOCOLO]</dProtAut>
  </gResOK>
  <gResObs>
    <dCodObs>O001</dCodObs>
    <dMsgObs>Descripción de la observación</dMsgObs>
  </gResObs>
</gResProcDE>
```

---

## Campos de la Response

| Campo | Descripción |
|-------|-------------|
| dCodRes | Código de respuesta del SIFEN |
| dMsgRes | Mensaje descriptivo de la respuesta |
| dFecProc | Fecha y hora de procesamiento en el SIFEN |
| Id | CDC del DE procesado |
| dProtAut | Número de protocolo de autorización (solo si aprobado) |
| dMotRec | Motivo de rechazo (solo si rechazado) |
| dCodErr | Código de error específico |
| dMsgErr | Mensaje detallado del error |
| dCodObs | Código de observación (si aprobado con observaciones) |
| dMsgObs | Descripción de la observación |

---

## Códigos de Respuesta

| Código | Estado | Descripción |
|--------|--------|-------------|
| 0302 | Aprobado | DE aprobado sin observaciones. Tiene validez fiscal |
| 0304 | Rechazado | DE rechazado. Debe corregirse y enviarse con nuevo CDC |
| 0306 | Aprobado con observaciones | Aprobado pero con advertencias. Tiene validez fiscal |
| 0400 | Error de comunicación | Error técnico en la transmisión |
| 0401 | Error de autenticación | Certificado TLS inválido o vencido |
| 0500 | Error interno SIFEN | Error del servidor SIFEN (reintentar) |

---

## Estados del DE tras la Respuesta

| Código SIFEN | Estado del DE | Acción del Emisor |
|--------------|---------------|-------------------|
| 0302 | Aprobado (DTE) | Enviar KuDE al receptor; conservar 5 años |
| 0306 | Aprobado con obs. | Enviar KuDE; revisar observaciones |
| 0304 | Rechazado | Corregir error; generar nuevo CDC; reenviar |

> **Importante:** Un DE rechazado NO puede reusarse. Debe generarse un nuevo DE con un nuevo CDC (nueva numeración o serie diferente).

---

## Protocolo de Autorización (dProtAut)

El `dProtAut` es el número de protocolo de autorización emitido por el SIFEN al aprobar un DE. Es el equivalente digital del "timbrado" en documentos físicos. Este número:
- Se imprime en el KuDE
- Es único por DE
- Certifica la autenticidad ante la SET

---

## Buenas Prácticas

1. **Validar localmente** el XML contra el XSD y con el prevalidador antes de enviar.
2. **Verificar la firma digital** con una librería local antes de enviar al SIFEN.
3. **Sincronizar el reloj** con los servidores NTP (aravo1.set.gov.py, aravo2.set.gov.py) para que la fecha/hora de firma sea válida.
4. **Guardar la respuesta completa** (incluyendo dProtAut) para auditoría.
5. **Manejo de timeout**: si el WS no responde en el tiempo esperado, consultar con `siConsDE` usando el CDC antes de reenviar, para evitar duplicados.
6. **No reenviar un DE aprobado**: siempre verificar el estado con `siConsDE` ante dudas.
