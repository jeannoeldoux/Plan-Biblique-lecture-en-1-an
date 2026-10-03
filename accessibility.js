(()=>{
'use strict';
const main=document.querySelector('main');if(!main)return;if(!main.id)main.id='mainContent';main.setAttribute('tabindex','-1');
const skips=document.createElement('nav');skips.className='skip-links';skips.setAttribute('aria-label','Accès directs');const a=document.createElement('a');a.href=document.getElementById('content')?'#content':'#'+main.id;a.textContent=document.getElementById('content')?'Aller à la lecture du jour':'Aller au contenu';skips.append(a);if(document.getElementById('player')){const b=document.createElement('a');b.href='#player';b.textContent='Aller au lecteur audio';skips.append(b)}document.body.prepend(skips);
skips.addEventListener('click',e=>{const target=e.target.closest('a');if(!target)return;const el=document.querySelector(target.getAttribute('href'));if(el){if(!el.hasAttribute('tabindex'))el.tabIndex=-1;el.focus()}});
const live=document.createElement('p');live.id='accessibleDayStatus';live.className='visually-hidden';live.setAttribute('role','status');live.setAttribute('aria-live','polite');live.setAttribute('aria-atomic','true');document.body.append(live);
function update(){const h=document.querySelector('#content .day h1');if(h){h.tabIndex=-1;live.textContent=h.textContent+' — '+(document.querySelector('#content .theme')?.textContent||'')}document.querySelectorAll('input,select,textarea').forEach(el=>{if(el.type==='hidden'||el.getAttribute('aria-label')||el.getAttribute('aria-labelledby')||el.labels?.length)return;const text=el.title||el.placeholder;if(text)el.setAttribute('aria-label',text)});document.querySelectorAll('dialog').forEach(d=>{if(!d.getAttribute('aria-label')&&!d.getAttribute('aria-labelledby')){const heading=d.querySelector('h1,h2,h3');if(heading){if(!heading.id)heading.id=d.id+'Title';d.setAttribute('aria-labelledby',heading.id)}else d.setAttribute('aria-label','Options de lecture')}});
}
const content=document.getElementById('content');if(content)new MutationObserver(update).observe(content,{childList:true});update();
// Native dialogs keep keyboard focus inside. Restore the opening control when closed.
document.addEventListener('click',e=>{const control=e.target.closest('button,a');if(control)for(const d of document.querySelectorAll('dialog:not([open])'))d._openingControl=control},true);
document.querySelectorAll('dialog').forEach(d=>d.addEventListener('close',()=>{if(d._openingControl?.isConnected)d._openingControl.focus()}));
})();
