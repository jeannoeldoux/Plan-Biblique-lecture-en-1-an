(()=>{
const CURRENT=window.bibleAppRelease||'2026.10.06.41';let available=null,busy=false;
const panel=document.createElement('section');panel.className='app-update';panel.setAttribute('aria-label','Mises à jour de l’application');
const check=document.createElement('button'),apply=document.createElement('button'),status=document.createElement('p');
check.id='checkAppUpdate';check.type='button';check.textContent='Vérifier les mises à jour';apply.id='applyAppUpdate';apply.type='button';apply.textContent='Mettre à jour maintenant';apply.hidden=true;status.id='appUpdateStatus';status.setAttribute('role','status');status.setAttribute('aria-live','polite');status.textContent='Version '+CURRENT;
panel.append(check,apply,status);document.body.append(panel);
async function announceUpdate(){if(busy||location.protocol==='file:'||!navigator.onLine)return;try{const r=await fetch('./version.json?check='+Date.now(),{cache:'no-store'});if(!r.ok)return;const d=await r.json();if(typeof d.version==='string'&&/^\d{4}\.\d{2}\.\d{2}\.\d+$/.test(d.version)&&d.version.localeCompare(CURRENT,undefined,{numeric:true})>0){available=d.version;apply.hidden=false;status.textContent='Nouvelle version disponible : '+available+'. Votre suivi sera conservé.'}}catch(_){}}
setTimeout(announceUpdate,1200);document.addEventListener('visibilitychange',()=>{if(!document.hidden&&Date.now()-(window._lastBibleUpdateCheck||0)>900000){window._lastBibleUpdateCheck=Date.now();announceUpdate()}});
function lock(value){busy=value;check.disabled=apply.disabled=value}
check.onclick=async()=>{
if(busy)return;
if(location.protocol==='file:'){status.textContent='La vérification sera disponible lorsque cette application sera publiée sur GitHub Pages. Vous consultez actuellement les fichiers locaux.';return}
lock(true);apply.hidden=true;available=null;status.textContent='Recherche d’une nouvelle version…';
try{const r=await fetch('./version.json?check='+Date.now(),{cache:'no-store'});if(!r.ok)throw Error();const data=await r.json();if(typeof data.version!=='string'||!data.version.trim())throw Error();if(data.version===CURRENT){status.textContent='Votre application est à jour — version '+CURRENT+'.'}else{available=data.version;apply.hidden=false;status.textContent='Une nouvelle version est disponible : '+available+'. Vos notes et votre suivi seront conservés.'}}
catch(_){status.textContent='Vérification impossible. Vérifiez votre connexion Internet et réessayez.'}finally{lock(false)}
};
apply.onclick=async()=>{
if(busy||!available)return;lock(true);status.textContent='Téléchargement de la mise à jour…';
try{
if(!('serviceWorker' in navigator))throw Error();
const reg=await navigator.serviceWorker.register('./sw.js',{updateViaCache:'none'});await reg.update();
const pending=reg.installing||reg.waiting;
if(pending&&pending.state!=='activated')await new Promise((resolve,reject)=>{const timeout=setTimeout(()=>reject(Error()),45000);function changed(){if(pending.state==='activated'){clearTimeout(timeout);resolve()}else if(pending.state==='redundant'){clearTimeout(timeout);reject(Error())}}pending.addEventListener('statechange',changed);changed()});
const worker=reg.active;if(!worker)throw Error();
await new Promise((resolve,reject)=>{const channel=new MessageChannel(),timeout=setTimeout(()=>reject(Error()),45000);channel.port1.onmessage=e=>{clearTimeout(timeout);channel.port1.close();e.data&&e.data.ok&&e.data.version===available?resolve():reject(Error())};worker.postMessage({type:'REFRESH_APP'},[channel.port2])});
status.textContent='Mise à jour téléchargée. Ouverture de la nouvelle version…';location.reload();
}catch(_){status.textContent='La mise à jour n’a pas pu être terminée. Votre suivi est conservé ; réessayez avec une connexion Internet.';lock(false)}
};
})();