#!/usr/bin/env python
"""Filtro `clean` de Git para notebooks: quita la metadata que hace ruido.

Lee un .ipynb en stdin y lo escribe normalizado en stdout. Git lo aplica al
pasar del directorio de trabajo al índice, así que el notebook local conserva
lo que Jupyter o VS Code le hayan puesto, pero el commit solo registra los
cambios que importan.

**Las salidas de las celdas se conservan a propósito**: los alumnos necesitan
ver los resultados esperados sin ejecutar el notebook.

Lo que se elimina:

- `metadata.language_info.version`: cambia con el intérprete de cada máquina
  (3.11.9 aquí, 3.12.3 en otra) y no aporta nada al material del curso.
- `metadata.kernelspec`: se fija a un valor canónico, porque Jupyter lo
  escribe como "Python 3" y el kernel de ipykernel como "Python 3 (ipykernel)".
- Metadata de herramientas por celda (`vscode`, `execution`, `ExecuteTime`,
  y estados de plegado en falso), que cambia con solo abrir el archivo.
- `metadata.widgets`: estado serializado de widgets, a veces de miles de líneas.

Instalación (una sola vez por clon, porque `.git/config` no se clona):

    git config filter.nbclean.clean "python tools/nb_clean.py"
    git add --renormalize .

Sin esa configuración, Git ignora el filtro y todo sigue funcionando: el
notebook se commitea tal cual. Por eso `filter.nbclean.required` se deja sin
activar, para que un clon nuevo no falle.
"""

import json
import sys

KERNELSPEC = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3",
}

# Metadata de nivel notebook que no describe el contenido.
NOTEBOOK_NOISE = ("widgets", "vscode", "colab", "toc")

# Metadata por celda que escriben los editores al abrir o ejecutar.
CELL_NOISE = ("vscode", "execution", "ExecuteTime", "collapsed", "scrolled")

# Dentro de `cell.metadata.jupyter`: solo son ruido cuando están en falso.
JUPYTER_FLAGS = ("outputs_hidden", "source_hidden")


def clean_cell(cell):
    meta = cell.get("metadata")
    if not isinstance(meta, dict):
        return
    for key in CELL_NOISE:
        meta.pop(key, None)
    jupyter = meta.get("jupyter")
    if isinstance(jupyter, dict):
        for flag in JUPYTER_FLAGS:
            if jupyter.get(flag) is False:
                jupyter.pop(flag)
        if not jupyter:
            meta.pop("jupyter")


def clean_notebook(nb):
    meta = nb.get("metadata")
    if isinstance(meta, dict):
        for key in NOTEBOOK_NOISE:
            meta.pop(key, None)
        meta["kernelspec"] = dict(KERNELSPEC)
        language_info = meta.get("language_info")
        if isinstance(language_info, dict):
            language_info.pop("version", None)
    for cell in nb.get("cells", []):
        if isinstance(cell, dict):
            clean_cell(cell)
    return nb


def main():
    raw = sys.stdin.buffer.read()
    try:
        nb = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        # Ante un archivo que no es JSON válido, pasarlo intacto: un filtro de
        # Git nunca debe ser la razón por la que se pierde trabajo.
        sys.stdout.buffer.write(raw)
        return

    clean_notebook(nb)

    # Mismo formato que usa nbformat al guardar (indent=1, claves ordenadas),
    # para que el diff contra lo que escribe Jupyter sea mínimo.
    text = json.dumps(nb, indent=1, sort_keys=True, ensure_ascii=False,
                      separators=(",", ": "))
    sys.stdout.buffer.write((text + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
