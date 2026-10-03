#!/usr/bin/env python3
"""Genera la carpeta de XSD para validación local a partir de las copias fieles de 00-fuentes/xsd/.

Cambios aplicados (y ningún otro):
  1. Los `schemaLocation` absolutos `https://ekuatia.set.gov.py/sifen/xsd/<archivo>` pasan a ser
     relativos (`<archivo>`), para validar sin red.
  2. En DE_v150.xsd se corrige el nombre de elemento `dEntCont ` (con espacio final, error del XSD
     oficial, ver xsd-produccion-vs-manual.md §14) por `dEntCont`.

Uso:  python generar.py        (desde cualquier directorio)
Vuelve a ejecutarse cada vez que cambie 00-fuentes/xsd/ (ver AGENTS.md §4). Escribe CAMBIOS.md5 con
los md5 de origen y destino para poder auditar qué se modificó.
"""
import hashlib
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ORIGEN = os.path.normpath(os.path.join(AQUI, "..", "..", "00-fuentes", "xsd"))
ARCHIVOS = [
    "siRecepDE_v150.xsd", "DE_v150.xsd", "DE_Types_v150.xsd",
    "siRecepEvento_v150.xsd", "Evento_v150.xsd", "Evento_Types_v150.xsd",
    "Paises_v100.xsd", "Departamentos_v141.xsd", "Monedas_v150.xsd",
    "Unidades_Medida_v141.xsd", "xmldsig-core-schema.xsd",
]
URL_BASE = "https://ekuatia.set.gov.py/sifen/xsd/"


def md5(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def main() -> int:
    filas = []
    for nombre in ARCHIVOS:
        ruta_in = os.path.join(ORIGEN, nombre)
        with open(ruta_in, "rb") as f:
            original = f.read()
        texto = original.decode("utf-8")
        cambios = []

        n = texto.count(URL_BASE)
        if n:
            texto = texto.replace(URL_BASE, "")
            cambios.append(f"{n} schemaLocation absolutos -> relativos")

        if nombre == "DE_v150.xsd":
            malo = 'name="dEntCont "'
            c = texto.count(malo)
            if c != 1:
                print(f"ERROR: se esperaba exactamente 1 ocurrencia de {malo!r} en DE_v150.xsd y hay {c}. "
                      f"¿Cambió el XSD oficial? Revisar xsd-produccion-vs-manual.md §14.", file=sys.stderr)
                return 1
            texto = texto.replace(malo, 'name="dEntCont"')
            cambios.append("dEntCont con espacio final -> dEntCont")

        salida = texto.encode("utf-8")
        with open(os.path.join(AQUI, nombre), "wb") as f:
            f.write(salida)
        filas.append((nombre, md5(original), md5(salida), "; ".join(cambios) or "sin cambios (copia idéntica)"))

    with io.open(os.path.join(AQUI, "CAMBIOS.md5"), "w", encoding="utf-8", newline="\n") as f:
        f.write("# Generado por generar.py. Columnas: archivo | md5 origen (00-fuentes/xsd) | md5 local | cambios\n")
        for nombre, m_in, m_out, cambios in filas:
            f.write(f"{nombre} | {m_in} | {m_out} | {cambios}\n")

    for nombre, m_in, m_out, cambios in filas:
        marca = "=" if m_in == m_out else "~"
        print(f"{marca} {nombre:28s} {cambios}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
