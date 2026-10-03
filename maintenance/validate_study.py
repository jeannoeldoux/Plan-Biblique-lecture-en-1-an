"""Check references in the original study aids; does not certify interpretation."""
import json,re
def verify(root):
    source=(root/'book-guides.js').read_text(encoding='utf8').strip()
    db=json.loads(source.removeprefix('window.bibleStudyData=').removesuffix(';'))
    assert len(db['books'])==66
    variants={v:{(r['book'],r['chapter']):r['verses'] for r in json.loads((root/'maintenance'/('verses-'+v+'.json')).read_text(encoding='utf8'))} for v in ['s21','lsg','pdv']}
    for v,counts in variants.items():
        for span in [q['span'] for q in db['questions']]+[r[k] for r in db['links'] for k in ['ot','nt']]:
            b,ch,a,z=span
            assert b in db['books'] and 1<=a<=z<=counts[b,ch],(v,span)
        name='plan-continuite'+('' if v=='s21' else '-'+v)+'.html'
        text=(root/name).read_text(encoding='utf8')
        data=json.loads(re.search(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>',text,re.S)[1])
        assert len(data)==365
        membership={}
        for i,day in enumerate(data):
            for c in day['cards']:
                for e in c['entries']:
                    b,ch=re.search(r'/([A-Z0-9]+)\.(\d+)',e['page']).groups();ch=int(ch)
                    assert (b,ch) not in membership,(name,'repeated chapter',b,ch)
                    assert e.get('firstVerse',1)==1 and e.get('lastVerse',counts[b,ch])==counts[b,ch],(name,'partial chapter')
                    membership[b,ch]=i
        assert len(membership)==1189 and set(membership)==set(counts)
        for b,spans in db['protected'].items():
            for a,z in spans:
                assert len({membership[b,ch] for ch in range(a,z+1)})==1,(name,'protected group split',b,a,z)
    print('PASS study aids:',len(db['books']),'books,',len(db['questions']),'targeted question sets,',len(db['links']),'documented links; valid ranges and protected groups in all three versions')
if __name__=='__main__':
    from pathlib import Path
    verify(Path(__file__).resolve().parent.parent)
