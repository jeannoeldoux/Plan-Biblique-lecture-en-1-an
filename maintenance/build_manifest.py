"""Run after editing the release files. Does not modify any reading or user data."""
from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parent.parent
version=json.loads((root/'version.json').read_text(encoding='utf8'))['version']
assert re.search(r"bibleAppRelease='([^']+)'",(root/'app-common.js').read_text(encoding='utf8'))[1]==version,'app-common.js version differs'
assert re.search(r"const RELEASE='([^']+)'",(root/'sw.js').read_text(encoding='utf8'))[1]==version,'sw.js version differs'
files={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.iterdir()) if p.is_file() and p.suffix in {'.html','.js','.css','.svg','.png','.webmanifest'}}
(root/'release-manifest.json').write_text(json.dumps({'version':version,'files':files},indent=2),encoding='utf8')
print('Release manifest:',version,len(files),'files')
