"""Copy best (and optionally last) PADC checkpoint files to a release staging dir.

Example:
  python scripts/collect_checkpoints.py --run-root /content/drive/MyDrive/PADC_reproduction_CIFAR_fresh_20261022_v1 --out /content/PADC_release_weights

No PyTorch dependency, no unpickling or deserializing. Makes SHA256SUMS.txt.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import shutil
from pathlib import Path

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as fp:
        for block in iter(lambda: fp.read(8 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run-root', required=True, type=Path,
                   help='MyDrive/<RUN_FOLDER> from the PADC Colab notebook')
    p.add_argument('--out', required=True, type=Path)
    p.add_argument('--include-last', action='store_true',
                   help='Include optimizer resume checkpoints as well as best')
    args = p.parse_args()
    dstroot = args.out.resolve()
    dstroot.mkdir(parents=True, exist_ok=True)
    rows=[];missing=[]
    suffixes=['best']+(['last'] if args.include_last else [])
    for channel in ('awgn','repo_fading'):
        source_dir=args.run_root/'paper'/channel/'checkpoints'
        for kind in ('jscc_v','oracle'):
            for dataset in ('cifar10','imagenet128'):
                for suffix in suffixes:
                    filename=f'{kind}_{channel}_{dataset}_{suffix}.pt'
                    src=source_dir/filename
                    if not src.is_file():
                        missing.append(str(src))
                        continue
                    dst=dstroot/channel/filename
                    dst.parent.mkdir(exist_ok=True,parents=True)
                    if not dst.exists() or src.stat().st_size!=dst.stat().st_size:
                        shutil.copy2(src,dst)
                    rows.append({'channel':channel,'model':kind,'dataset':dataset,
                                 'selection':suffix,'path':str(dst.relative_to(dstroot)),
                                 'sha256':sha256(dst),'size_bytes':dst.stat().st_size})
                    print('READY',dst, f'{dst.stat().st_size/2**20:.1f} MiB')
    (dstroot/'weight_manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
    (dstroot/'SHA256SUMS.txt').write_text(''.join(f'{r["sha256"]}  {r["path"]}\n' for r in rows))
    if missing:
        print('\nMissing (not created, model checkpoints not attached to starter kit):')
        for name in missing:print('-',name)
    print('\nComplete files:',len(rows),'; missing:',len(missing))
    if missing:
        raise SystemExit('INCOMPLETE: verify your original Colab checkpoint paths before publishing.')

if __name__=='__main__': main()
