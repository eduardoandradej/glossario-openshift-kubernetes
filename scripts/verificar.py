#!/usr/bin/env python3
"""Verificações locais iniciais, sem conectividade ou acesso ao cluster."""
from pathlib import Path
import json, re
root=Path(__file__).resolve().parents[1]
items=json.loads((root/'dados/inventario.json').read_text(encoding='utf8'))
assert all(x.get('term') and x.get('category') for x in items)
assert len(list((root/'categorias').glob('*/README.md'))) >= 18
assert (root/'PROMPT-MESTRE.md').exists()
md=list(root.rglob('*.md'))
errors=[]
for f in md:
    s=f.read_text(encoding='utf8')
    for rel in re.findall(r'\[[^\]]+\]\(([^)#]+)(?:#[^)]*)?\)',s):
        if rel.startswith(('http:', 'https:', 'mailto:')): continue
        if not (f.parent/rel).exists(): errors.append(f'{f.relative_to(root)} => {rel}')
print(f'Inventário: {len(items)} entradas brutas; Markdown: {len(md)} arquivos; links locais quebrados: {len(errors)}')
for e in errors: print('ERRO:',e)
raise SystemExit(bool(errors))
