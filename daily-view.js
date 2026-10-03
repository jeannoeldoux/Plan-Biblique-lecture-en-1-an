(()=>{
'use strict';
const wrap=document.querySelector('main.wrap'),content=document.getElementById('content');
if(!wrap||!content)return;
const key='bible-app-daily-layout-v1',bar=document.createElement('section');
bar.id='dailyUiBar';bar.className='daily-ui-bar';
bar.innerHTML='<p id="dailyUiProgress" role="status"></p><div class="daily-ui-actions"><button id="dailyResume" type="button">Reprendre ma lecture</button><button id="dailySave" type="button">Sauvegarder</button><button id="dailyLayoutToggle" type="button" aria-controls="dailyTools">Afficher tous les outils</button></div>';
wrap.querySelector('nav[aria-label="Choix du jour"]').before(bar);
const tools=document.createElement('details');tools.id='dailyTools';tools.className='planning';tools.innerHTML='<summary>Outils et réglages</summary><p>Retrouvez ici le calendrier, les recherches, vos archives et toutes les options de suivi.</p>';
content.after(tools);
const entries=[...wrap.children].filter(e=>e!==tools&&(e.tagName==='DETAILS'||e.matches('div.progress')||e.matches('.essential-toggle')||['openStartGuide','myDayStatus'].includes(e.id))).map(e=>{const anchor=document.createComment('Position de '+(e.id||'outil'));e.before(anchor);return {e,anchor}});
let simple=true;try{simple=localStorage.getItem(key)!=='complete'}catch(_){}
function apply(){entries.forEach(({e,anchor})=>simple?tools.append(e):anchor.after(e));tools.hidden=!simple;document.documentElement.dataset.dailyLayout=simple?'simple':'complete';document.getElementById('dailyLayoutToggle').textContent=simple?'Afficher tous les outils':'Revenir à la lecture';document.getElementById('dailyLayoutToggle').setAttribute('aria-expanded',String(!simple))}
document.getElementById('dailyLayoutToggle').onclick=()=>{simple=!simple;try{localStorage.setItem(key,simple?'simple':'complete')}catch(_){}apply()};
document.getElementById('dailyResume').onclick=()=>document.getElementById('resume')?.click();
document.getElementById('dailySave').onclick=()=>window.secureBackup?.startExport();
function progress(){document.getElementById('dailyUiProgress').textContent=typeof completed!=='undefined'?completed.size+' / 365 jours validés':''}
wrap.addEventListener('change',progress);new MutationObserver(progress).observe(content,{childList:true});apply();progress();
})();
