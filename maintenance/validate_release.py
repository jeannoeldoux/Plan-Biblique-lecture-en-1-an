"""Offline structural/editorial checks for the 24 reading variants and release assets."""
from pathlib import Path
import re,json,hashlib,unicodedata
root=Path(__file__).resolve().parent.parent
def normalize(s):return ''.join(c for c in unicodedata.normalize('NFD',s.casefold()) if unicodedata.category(c)!='Mn').strip()
catalogs={v:json.loads((root/'maintenance'/('verses-'+v+'.json')).read_text(encoding='utf8')) for v in ['s21','lsg','pdv']}
counts={v:{(x['book'],int(x['chapter'])):int(x['verses']) for x in rows} for v,rows in catalogs.items()}
titlemap={}
for p in root.glob('plan-*.html'):
 s=p.read_text(encoding='utf8');d=json.loads(re.search(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>',s,re.S)[1])
 for day in d:
  for card in day['cards']:
   for e in card['entries']:
    book=e.get('book') or re.search(r'/([A-Z0-9]+)\.\d+',e['page'])[1]
    titlemap[normalize(re.sub(r'\s+\d+$','',e['title']))]=book
titlemap['psaume']='PSA'
def passages(ref,version):
 covered=set()
 for raw in ref.split(';'):
  raw=normalize(raw)
  if not raw:continue
  bookname=next((n for n in sorted(titlemap,key=len,reverse=True) if raw.startswith(n+' ')),None)
  assert bookname,('unrecognized book',ref)
  book=titlemap[bookname];number=raw[len(bookname):].strip()
  m=re.fullmatch(r'(\d+)(?:[–-](\d+))?(?:[.:](\d+)(?:[–-](\d+))?)?',number)
  assert m,('unrecognized passage',ref,number)
  a,b,first,last=m.groups();a=int(a);b=int(b or a)
  assert a<=b,(ref,'reversed chapters')
  for chapter in range(a,b+1):
   total=counts[version].get((book,chapter))
   assert total,(version,ref,'invalid chapter')
   lo=int(first or 1);hi=int(last or first or total)
   assert 1<=lo<=hi<=total,(version,ref,'invalid verses',total)
   covered.update((book,chapter,v) for v in range(lo,hi+1))
 return covered
report={}
for p in sorted(root.glob('plan-*.html')):
 version='lsg' if p.stem.endswith('-lsg') else 'pdv' if p.stem.endswith('-pdv') else 's21'
 plan=p.stem[5:].removesuffix('-'+version);s=p.read_text(encoding='utf8')
 d=json.loads(re.search(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>',s,re.S)[1]);assert len(d)==365,p
 coverage=set();repeats=0;partial=0;pauses=0;entries=0
 for day in d:
  assert isinstance(day.get('theme'),str) and day['theme'].strip(),p
  if not any(c['entries'] for c in day['cards']):pauses+=1
  for i,c in enumerate(day['cards']):
   if not c['entries']:continue
   actual=passages(c['ref'],version)
   # Complementary thematic/family cards are not the full-Bible spine.
   if plan not in ['semaines','famille'] or c['kind']!='mirror':
    repeats+=len(coverage&actual);coverage.update(actual)
   for e in c['entries']:
    entries+=1;book=e.get('book') or re.search(r'/([A-Z0-9]+)\.\d+',e['page'])[1]
    chapter=int(e.get('chapter') or re.search(r'/[A-Z0-9]+\.(\d+)',e['page'])[1])
    assert (book,chapter) in counts[version],(p,e['title'])
    if e.get('firstVerse',1)>1 or e.get('lastVerse',counts[version][book,chapter])<counts[version][book,chapter]:partial+=1
    for field in ['src','page','textPage','audioPage']:
     if e.get(field):assert e[field].startswith('https://'),(p,field)
 expected={(book,ch,v) for (book,ch),n in counts[version].items() for v in range(1,n+1)}
 missing=expected-coverage;assert not missing,(p,'missing numbered verses',len(missing),sorted(missing)[:5])
 if plan in ['genres','salut','chronologique','parallele','rattrapage','famille']:assert repeats==0,(p,'unintended repeat',repeats)
 if plan=='rattrapage':assert pauses==52,(p,pauses)
 report[p.name]={'days':365,'numbered_verses':len(coverage),'books':len({x[0] for x in coverage}),'partial_entries':partial,'repeated_verses':repeats,'pause_days':pauses,'audio_entries':entries}
manifest=json.loads((root/'release-manifest.json').read_text(encoding='utf8'))
assert manifest['version']==json.loads((root/'version.json').read_text())['version']
for name,digest in manifest['files'].items():assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,('release hash',name)
for p in root.glob('*.html'):
 for link in re.findall(r'(?:src|href)="(\./[^"]+)"',p.read_text(encoding='utf8')):
  local=link.split('?')[0].split('#')[0]
  assert (root/local).exists(),('missing local link',p.name,local)
assert len(report)==24,len(report)
(root/'controle-editorial.json').write_text(json.dumps({'version':manifest['version'],'scope':'Structural checks of written references; not independent theological certification.','plans':report},ensure_ascii=False,indent=2),encoding='utf8')
print('PASS:',len(report),'variants, 8760 days, written references, full numbered-verse coverage, HTTPS links and release hashes')
