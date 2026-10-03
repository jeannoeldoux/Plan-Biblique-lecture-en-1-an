(()=>{const root=document.documentElement,key='bible-app-theme-v1',toggle=document.getElementById('darkMode');if(!toggle)root.classList.add('app-guide');
let saved;try{saved=localStorage.getItem(key)}catch(_){}
let dark=saved==='dark';if(!saved){let old;try{old=JSON.parse(localStorage.getItem('bible-plan-comfort-v1')||'{}').dark}catch(_){}dark=typeof old==='boolean'?old:matchMedia('(prefers-color-scheme:dark)').matches}
const button=document.createElement('button');button.id='appThemeButton';button.type='button';document.body.prepend(button);
function refresh(){const active=root.dataset.theme==='dark';button.textContent=active?'Passer en mode clair':'Passer en mode sombre';button.setAttribute('aria-pressed',String(active));if(toggle)toggle.checked=active;try{localStorage.setItem(key,active?'dark':'light')}catch(_){}}
root.dataset.theme=dark?'dark':'light';refresh();new MutationObserver(refresh).observe(root,{attributes:true,attributeFilter:['data-theme']});
button.onclick=()=>{if(toggle){toggle.checked=root.dataset.theme!=='dark';toggle.dispatchEvent(new Event('change',{bubbles:true}))}else root.dataset.theme=root.dataset.theme==='dark'?'light':'dark'};
window.addEventListener('storage',e=>{if(e.key===key&&['dark','light'].includes(e.newValue))root.dataset.theme=e.newValue});
})();