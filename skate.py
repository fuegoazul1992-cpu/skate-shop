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
    print('--- reporte importacion ---')
    print(f'✔️ Válidos{len(ok)}')
    print(f'❌ No validos{len(bad)}')
    if bad:
        print('Lineas Problematicas')
        for i, s in bad:
            print(f'- Lineas{i}: {s!r}')
    if ok:
        n = len(ok)
        print(f'Promedio: {sum(ok)/n: .4f} | Max:{max(ok)} Min:{min(ok)} n:{n}')
        
if __name__=='__main__':
    ok, bad = leer_notas_seguro
    imprimir_reporte(ok, bad)
    
    
    