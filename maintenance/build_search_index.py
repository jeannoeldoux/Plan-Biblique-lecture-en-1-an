"""Rebuild the compact search index from the 36 plan pages; run before build_manifest.py."""
from pathlib import Path
import re,json
root=Path(__file__).resolve().parent.parent
PAIRS=[('classique', 's21'), ('genres', 's21'), ('salut', 's21'), ('semaines', 's21'), ('classique', 'lsg'), ('genres', 'lsg'), ('salut', 'lsg'), ('semaines', 'lsg'), ('classique', 'pdv'), ('genres', 'pdv'), ('salut', 'pdv'), ('semaines', 'pdv'), ('chronologique', 's21'), ('parallele', 's21'), ('rattrapage', 's21'), ('chronologique', 'lsg'), ('parallele', 'lsg'), ('rattrapage', 'lsg'), ('chronologique', 'pdv'), ('parallele', 'pdv'), ('rattrapage', 'pdv'), ('famille', 's21'), ('famille', 'lsg'), ('famille', 'pdv'), ('continuite', 's21'), ('continuite', 'lsg'), ('continuite', 'pdv'), ('israel-nations', 'lsg'), ('israel-nations', 'pdv'), ('israel-nations', 's21'), ('connexions', 's21'), ('connexions', 'lsg'), ('connexions', 'pdv'), ('reseau', 's21'), ('reseau', 'lsg'), ('reseau', 'pdv')]
LABELS={'classique': 'Avec thèmes', 'genres': 'Par genres', 'salut': 'Histoire du salut', 'semaines': 'Semaines thématiques', 'chronologique': 'Lecture chronologique', 'parallele': 'Ancien et Nouveau Testament en parallèle', 'rattrapage': 'Lecture avec jour de rattrapage', 'famille': 'En famille ou petit groupe', 'continuite': 'Lecture avec continuité', 'israel-nations': 'Israël et les nations : un seul peuple en Christ', 'connexions': 'Connexions bibliques : AT ↔ NT', 'reseau': 'La Bible en réseau — connexions AT ↔ NT'}
records=[]
for slug,version in PAIRS:
 name='plan-'+slug+('' if version=='s21' else '-'+version)+'.html'
 html=(root/name).read_text(encoding='utf8')
 study=slug in ('connexions','reseau')
 identifier='connectionsData' if study else 'plan'
 m=re.search(r'<script[^>]*id="'+identifier+r'"[^>]*>(.*?)</script>',html,re.S)
 assert m,name
 data=json.loads(m[1]);items=data['sessions'] if study else data
 for i,d in enumerate(items,1):
  if study:
   theme=' — '.join([d['title']]+([d['module']] if d.get('module') else [])+[d['kind']])
   refs=' ; '.join(c['title'] for c in d['chapters'])
  else:
   theme=d['theme'];refs=' ; '.join(c['ref'] for c in d['cards'])
  records.append(dict(plan=slug,label=LABELS[slug],version=version,jour=i,theme=theme,references=refs,url=name+('#seance-' if study else '#jour-')+str(i)))
plans=list(LABELS);versions=['s21','lsg','pdv'];themes=list(dict.fromkeys(d['theme'] for d in records));refs=list(dict.fromkeys(d['references'] for d in records));ti={t:i for i,t in enumerate(themes)};ri={t:i for i,t in enumerate(refs)}
packed=dict(plans=[[p,LABELS[p]] for p in plans],versions=versions,themes=themes,references=refs,rows=[[plans.index(d['plan']),versions.index(d['version']),d['jour'],ti[d['theme']],ri[d['references']]] for d in records])
(root/'search-index.js').write_text('window.bibleSearchData='+json.dumps(packed,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf8')
print('Compact search index:',len(records),'records')
