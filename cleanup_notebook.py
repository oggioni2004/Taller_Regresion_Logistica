import json
from pathlib import Path

root = Path(__file__).resolve().parent
nb_path = root / 'Regresion_Logistica_German_Credit_Python.ipynb'

with nb_path.open('r', encoding='utf-8') as f:
    nb = json.load(f)

keep = []
for cell in nb.get('cells', []):
    src = ''.join(cell.get('source', []))
    s = src.lower()
    if any(k in s for k in [
        'taller — regresión logística',
        'taller - regresion logistica',
        'caso: abandono de producto financiero',
        'punto 1',
        'punto 2',
        'punto 3',
        'punto 4',
        'punto 5',
        'punto 6',
        'punto 7',
        'abandono',
        'retención',
        'retencion',
        'probabilidad de abandono',
        'p_abandono',
        'modelo logit',
        'odds ratios',
        'matriz de confusión',
    ]):
        keep.append(cell)

nb['cells'] = keep
with nb_path.open('w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print(f'Notebook limpiado: {len(keep)} celdas restantes.')
print('Primeras celdas:')
for i, cell in enumerate(keep[:6]):
    src = ''.join(cell.get('source', []))
    first = ' '.join(src.strip().splitlines()[:2])
    print(i, first[:120])
