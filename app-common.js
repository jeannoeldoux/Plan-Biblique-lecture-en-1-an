(()=>{
'use strict';
// Shared release configuration, independent of the user's follow-up namespaces.
window.bibleAppRelease='2026.10.06.38';
window.bibleAppWorkerReady=()=>{if(!('serviceWorker'in navigator)||!['http:','https:'].includes(location.protocol))return Promise.reject(Error('unsupported'));if(!window._bibleWorkerRegistration)window._bibleWorkerRegistration=navigator.serviceWorker.register('./sw.js',{updateViaCache:'none'}).then(()=>navigator.serviceWorker.ready);return window._bibleWorkerRegistration};
})();
