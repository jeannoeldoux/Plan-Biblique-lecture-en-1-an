"""Reference and data checks for the selected, nonannual study plan."""
from pathlib import Path
import re,json,hashlib,zipfile
def verify(root):
    for v in ['s21','lsg','pdv']:
        file='plan-connexions'+('' if v=='s21' else '-'+v)+'.html'
        text=(root/file).read_text(encoding='utf8')
        data=json.loads(re.search(r'<script type="application/json" id="connectionsData">(.*?)</script>',text,re.S)[1])['sessions']
        counts={(r['book'],r['chapter']):r['verses'] for r in json.loads((root/'maintenance'/('verses-'+v+'.json')).read_text(encoding='utf8'))}
        assert len(data)==24 and len(re.findall(r'<audio\b',text))==1
        for i,d in enumerate(data):
            assert d['id']==i+1 and d['direction']==('AT → NT' if i%2==0 else 'NT → AT')
            assert len(d['questions'])==3 and all(d[k].strip() for k in ['context','reading','limit','kind'])
            chapter_set=set()
            for e in d['chapters']:
                b,ch=re.search(r'/([A-Z0-9]+)\.(\d+)',e['page']).groups();ch=int(ch)
                assert (b,ch) in counts and (b,ch) not in chapter_set
                chapter_set.add((b,ch))
                for k in ['page','src','textPage','audioPage']:
                    if e.get(k):assert e[k].startswith('https://'),(file,k)
            for a in d['anchorLinks']:
                assert (a['book'],a['chapter']) in chapter_set
                assert 1<=a['firstVerse']<=a['lastVerse']<=counts[a['book'],a['chapter']]
                assert a['url'].startswith('https://www.bible.com/fr/bible/')
        joel=[a for a in data[22]['anchorLinks'] if a['book']=='JOL'][0]
        assert (joel['chapter'],joel['firstVerse'],joel['lastVerse'])==((2,28,32) if v=='lsg' else (3,1,5))
    print('PASS Connections: 24 sessions x 3 versions; 12 AT->NT and 12 NT->AT; chapters, verse ranges, Joel mapping, HTTPS sources, single player')
if __name__=='__main__':verify(Path(__file__).resolve().parent.parent)
