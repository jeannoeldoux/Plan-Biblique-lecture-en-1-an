(()=>{
'use strict';
const form=document.getElementById('reviewForm');if(!form)return;
const key='bible-independent-review-2026.10.03.31',status=document.getElementById('reviewStatus'),fields=[...form.querySelectorAll('select,textarea')];
function snapshot(){return {format:'bible-review-local',version:1,applicationVersion:'2026.10.03.31',role:form.querySelector('#reviewRole').value,items:fields.filter(f=>f.id!=='reviewRole').map(f=>({id:f.id,value:f.value})),exportedAt:new Date().toISOString()}}
try{const d=JSON.parse(localStorage.getItem(key)||'null');if(d&&Array.isArray(d.items))for(const f of fields){const value=f.id==='reviewRole'?d.role:d.items.find(i=>i.id===f.id)?.value;if(typeof value==='string'&&value.length<=3000&&(f.tagName==='TEXTAREA'||[...f.options].some(o=>o.value===value)))f.value=value}}catch(_){}
function save(){try{localStorage.setItem(key,JSON.stringify(snapshot()));status.textContent='Vos réponses de relecture sont conservées sur cet appareil. Aucun avis n’est envoyé.'}catch(_){status.textContent='Stockage indisponible : exportez vos réponses avant de quitter.'}}
form.addEventListener('input',save);form.addEventListener('change',save);
document.getElementById('exportReview').onclick=()=>{const url=URL.createObjectURL(new Blob([JSON.stringify(snapshot(),null,2)],{type:'application/json'}));const a=document.createElement('a');a.href=url;a.download='relecture-biblique-2026.10.03.31.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);status.textContent='Fichier préparé. Relisez les commentaires avant de le partager : ils sont inclus dans le fichier. Aucun envoi automatique.'};
})();
