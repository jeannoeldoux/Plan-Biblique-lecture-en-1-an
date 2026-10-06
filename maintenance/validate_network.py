"""Check study structure and references; does not certify proposed comparisons."""
import re,json
from pathlib import Path
def verify(root):
    counts_report={}
    for v in ['s21','lsg','pdv']:
        name='plan-reseau'+('' if v=='s21' else '-'+v)+'.html'
        text=(root/name).read_text(encoding='utf8')
        db=json.loads(re.search(r'<script[^>]*id="connectionsData"[^>]*>(.*?)</script>',text,re.S)[1]);ds=db['sessions']
        counts={(r['book'],r['chapter']):r['verses'] for r in json.loads((root/'maintenance'/('verses-'+v+'.json')).read_text(encoding='utf8'))}
        assert db['planId']=='reseau' and db['edition']=='reseau-200-v1' and len(ds)==200
        assert len({d['module'] for d in ds})==10 and len(re.findall(r'<audio\b',text))==1
        distinct=set()
        for i,d in enumerate(ds):
            assert d['id']==i+1 and d['dossier']==i//4+1 and d['phase']==i%4+1
            assert d['direction']==('AT → NT' if i%2==0 else 'NT → AT')
            assert len(d['questions'])==6 and all(d[k].strip() for k in ['context','reading','limit','kind','chain'])
            chapter_set=set()
            for e in d['chapters']:
                b,ch=re.search(r'/([A-Z0-9]+)\.(\d+)',e['page']).groups();ch=int(ch)
                assert (b,ch) in counts and (b,ch) not in chapter_set
                chapter_set.add((b,ch));distinct.add((b,ch))
                for k in ['page','src','textPage','audioPage']:
                    if e.get(k):assert e[k].startswith('https://')
            assert len(chapter_set)>=4
            for a in d['anchorLinks']:
                assert (a['book'],a['chapter']) in chapter_set
                assert 1<=a['firstVerse']<=a['lastVerse']<=counts[a['book'],a['chapter']]
            if d['phase']!=1:assert 'proposé' in d['kind'] or 'proposée' in d['kind']
        counts_report[v]={'sessions':200,'dossiers':50,'modules':10,'distinctChapters':len(distinct),'outsideReview':'not performed'}
    (root/'controle-reseau.json').write_text(json.dumps(counts_report,ensure_ascii=False,indent=2),encoding='utf8')
    print('PASS Network: 50 dossiers x 4 phases x 3 versions; 10 modules, verse ranges and distinct chapters; no automatic theological certification')
if __name__=='__main__':verify(Path(__file__).resolve().parent.parent)
