"""Static publication checks for this repo (no CUDA/Colab execution)."""
from pathlib import Path
import json, re, sys

ROOT=Path(__file__).resolve().parents[1]
issues=[]
for p in sorted((ROOT/'notebooks').glob('*.ipynb')):
    try: nb=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: issues.append(f'{p}: bad JSON: {e}');continue
    for j,c in enumerate(nb.get('cells',[])):
        if c.get('cell_type')=='code' and (c.get('outputs') or c.get('execution_count') is not None):
            issues.append(f'{p.name}: cell {j}: output/execution count present')
        src=''.join(c.get('source',[]))
        if re.search(r'(hf_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{20,}|AIza[0-9A-Za-z_\-]{30,})',src):
            issues.append(f'{p.name}: cell {j}: possible hardcoded access token')
for doc in [ROOT/'README.md',ROOT/'docs/FIGURE_STATUS.md']:
    text=doc.read_text(encoding='utf-8')
    for target in re.findall(r'!?(?:\[[^\]]*\])\(([^)#]+)(?:#[^)]*)?\)',text):
        if target.startswith(('https://','http://','mailto:')): continue
        if not (doc.parent/target).exists(): issues.append(f'{doc.relative_to(ROOT)}: broken relative link {target}')
print('Notebooks:',len(list((ROOT/'notebooks').glob('*.ipynb'))))
print('Static check:', 'PASS' if not issues else 'FAIL')
for issue in issues:print('-',issue)
if issues:sys.exit(1)
