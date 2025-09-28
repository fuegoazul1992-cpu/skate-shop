from __future__ import annotations
from pathlib import Path
from typing import Iterable

BASE = Path('.')
TXT = BASE / 'notas.txt'

def normaliza_num(s: str) -> float | None:
    s = s.strip().replace(' ', '')
    if not s:
        return None
    if ',' in s and '.' in s:
        s = s.replace('.', '')
        s = s.replace(',', '.')
    else:
        s = s.replace(',', '.')
        try:
            return float(s)
        except ValueError:
            return None
        
def leer_notas_seguro(ruta: Path = TXT):
    ok: list[float] = []
    bad: list[tuple[int, str]] = []
    with ruta.open('r', encoding='utf-8') as f:
        for i, linea in enumerate(f, 1):
            s = linea.strip()
            if not s or s.startswith('#'):
                continue
            v = normaliza_num(s)
            if v is None:
                bad.append((i, s))
            else:
                ok.append(v)
                return ok, bad
            
def imprimir_reporte(ok: list[float],bad: list[tuple[int, str]]) -> None:
    print('--- Reporte Importacion ---')
    print(f'Validos{len(ok)}')
    print(f'no validos{len(bad)}')
    if bad:
        print(' Lineas problematicas')
        for i, s in bad:
            print(f' - linea{i}: {s!r}')
    if ok:
        n =len(ok)
        