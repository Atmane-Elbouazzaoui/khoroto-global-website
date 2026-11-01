#!/usr/bin/env python3
"""Check the site, then prepare the generated /docs Pages source; never pushes."""
from pathlib import Path
import argparse
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
args = argparse.ArgumentParser()
args.add_argument('--preview', action='store_true', help='Omit CNAME while custom-domain setup is pending')
options = args.parse_args()
for command in [[sys.executable,'scripts/build_site.py'], [sys.executable,'scripts/check_site.py'], ['node','--test','scripts/invitation.test.mjs']]:
    subprocess.run(command, cwd=ROOT, check=True)
source, target = ROOT/'dist', ROOT/'docs'
files = [p.relative_to(source) for p in source.rglob('*') if p.is_file()]
if options.preview:
    files.remove(Path('CNAME'))
target.mkdir(exist_ok=True)
unexpected = [p.relative_to(target) for p in target.rglob('*') if p.is_file() and p.relative_to(target) not in files and p.relative_to(target) != Path('CNAME')]
if unexpected:
    raise SystemExit('Refusing to overwrite/remove unexpected Pages files: '+str(unexpected))
for path in files:
    (target/path).parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(source/path,target/path)
if options.preview and (target/'CNAME').exists():
    (target/'CNAME').unlink()
print(f'Prepared {len(files)} public files in docs/; custom domain '+('pending' if options.preview else 'included'))
