"""Verify that compact search records still describe the reading pages."""
from pathlib import Path
import json,re

def verify(root):
    source=(root/'search-index.js').read_text(encoding='utf8')
    data=json.loads(source.removeprefix('window.bibleSearchData=').strip().removesuffix(';'))
    actual={}
    for pi,vi,n,ti,ri in data['rows']:
        plan,label=data['plans'][pi];version=data['versions'][vi]
        key=(plan,version,n)
        assert key not in actual,'duplicate search record'
        actual[key]=(data['themes'][ti],data['references'][ri])
    expected={}
    for path in root.glob('plan-*.html'):
        name=path.stem.removeprefix('plan-');version='s21'
        if name.endswith(('-lsg','-pdv')):name,version=name.rsplit('-',1)
        study=name in ('connexions','reseau');identifier='connectionsData' if study else 'plan'
        match=re.search(r'<script[^>]*id="'+identifier+r'"[^>]*>(.*?)</script>',path.read_text(encoding='utf8'),re.S)
        contents=json.loads(match[1]);items=contents['sessions'] if study else contents
        for i,item in enumerate(items,1):
            if study:
                theme=' — '.join([item['title']]+([item['module']] if item.get('module') else [])+[item['kind']])
                refs=' ; '.join(c['title'] for c in item['chapters'])
            else:theme=item['theme'];refs=' ; '.join(c['ref'] for c in item['cards'])
            expected[(name,version,i)]=(theme,refs)
    assert actual==expected,'rebuild search-index.js before release'
    verse_source=(root/'daily-verse.js').read_text(encoding='utf8')
    verses=json.loads(re.search(r'const verses=(\[.*?\]);\n',verse_source,re.S)[1])
    assert len(verses)>=40 and len({(v['book'],v['chapter'],v['verse']) for v in verses})==len(verses)
    for version in ('s21','lsg','pdv'):
        counts=json.loads((root/'maintenance'/('verses-'+version+'.json')).read_text(encoding='utf8'))
        limits={(v['book'],v['chapter']):v['verses'] for v in counts}
        for v in verses:assert 1<=v['verse']<=limits[(v['book'],v['chapter'])]
    print('PASS compact search:',len(actual),'records match all reading pages;',len(verses),'daily verse references valid in three editions')

if __name__=='__main__':verify(Path(__file__).resolve().parent.parent)
