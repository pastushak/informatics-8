(function(){
  const store={get(k){try{return JSON.parse(localStorage.getItem(k))}catch(e){return null}},set(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}};
  const $=id=>document.getElementById(id);
  // theme
  const th=store.get('inf8-theme'); if(th) document.documentElement.dataset.theme=th;
  const tb=document.querySelector('.theme');
  if(tb) tb.addEventListener('click',()=>{const cur=document.documentElement.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');const nx=cur==='dark'?'light':'dark';document.documentElement.dataset.theme=nx;store.set('inf8-theme',nx);});
  const D=window.LESSON; if(!D) return;
  const SK='inf8-L'+D.n;            // per-lesson state
  const PK='inf8-progress';         // course progress
  const st=store.get(SK)||{sec:{},chk:{}};
  function save(){store.set(SK,st);}
  function prog(patch){const p=store.get(PK)||{};p[D.n]=Object.assign(p[D.n]||{},patch);store.set(PK,p);}
  function markSec(k){st.sec[k]=1;save();markPlan();}
  function markPlan(){document.querySelectorAll('.plan a').forEach(a=>a.classList.toggle('done',!!st.sec[a.dataset.k]));}
  // quizzes
  document.querySelectorAll('[data-quiz]').forEach(root=>{
    const id=root.dataset.quiz, items=D.q[id], score=$(id+'s'), sec=root.closest('section').id;
    const isFinal=root.hasAttribute('data-final');
    let answered=0,right=0;
    items.forEach((it0,i)=>{
      // shuffle options (3+ options) so the correct answer is not always in the same place
      let it=it0;
      if(it0[1].length>2){
        const idx=it0[1].map((_,k)=>k);
        for(let k=idx.length-1;k>0;k--){const r=Math.floor(Math.random()*(k+1));[idx[k],idx[r]]=[idx[r],idx[k]];}
        it=[it0[0],idx.map(k=>it0[1][k]),idx.indexOf(it0[2]),it0[3]];
      }
      const box=document.createElement('div');box.className='ex-item';
      const p=document.createElement('p');p.textContent=(i+1)+'. '+it[0];box.appendChild(p);
      const opts=document.createElement('div');opts.className='opts';
      const fb=document.createElement('p');fb.className='fb';
      it[1].forEach((o,j)=>{
        const b=document.createElement('button');b.type='button';b.textContent=o;
        b.addEventListener('click',()=>{
          if(box.dataset.done)return;box.dataset.done=1;answered++;
          const ok=j===it[2];if(ok)right++;
          b.classList.add(ok?'right':'wrong');if(!ok)opts.children[it[2]].classList.add('right');
          fb.className='fb '+(ok?'ok':'no');fb.textContent=(ok?'Правильно. ':'Не зовсім. ')+(it[3]||'');
          if(answered===items.length){
            score.textContent='Результат: '+right+' з '+items.length+(right===items.length?' — чудово!':right>=items.length*0.7?' — добре, перегляньте помилки.':' — перечитайте теорію і спробуйте ще раз.');
            markSec(sec);
            if(isFinal){prog({q:right,of:items.length});const r=document.createElement('button');r.type='button';r.className='theme';r.textContent='Пройти ще раз';r.onclick=()=>location.reload();score.appendChild(document.createTextNode(' '));score.appendChild(r);}
          }
        });
        opts.appendChild(b);
      });
      box.appendChild(opts);box.appendChild(fb);root.appendChild(box);
    });
  });
  // checklist
  const boxes=[...document.querySelectorAll('#check input')], bar=$('bar'), ban=$('donebanner');
  function upd(){
    const n=boxes.filter(b=>b.checked).length; if(bar) bar.style.width=(boxes.length?n/boxes.length*100:0)+'%';
    const all=boxes.length&&n===boxes.length;
    if(ban) ban.classList.toggle('on',!!all);
    prog({chk:n,chkOf:boxes.length,done:all?1:0});
    boxes.forEach(b=>{if(b.dataset.sec){ if(b.checked) st.sec[b.dataset.sec]=1; }});save();markPlan();
  }
  boxes.forEach(b=>{b.checked=!!st.chk[b.id];b.addEventListener('change',()=>{st.chk[b.id]=b.checked;save();upd();});});
  // copy buttons
  document.querySelectorAll('pre.code').forEach(pre=>{const b=document.createElement('button');b.className='cp';b.type='button';b.textContent='Копіювати';
    b.onclick=()=>{const t=pre.innerText.replace(/Копіювати$|Скопійовано$/,'').trimEnd();(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(()=>{b.textContent='Скопійовано';setTimeout(()=>b.textContent='Копіювати',1500)}).catch(()=>{});};pre.appendChild(b);});
  // nav highlight
  const navLinks=[...document.querySelectorAll('nav.bar a')];
  if('IntersectionObserver' in window){
    const io=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){
      const id=e.target.id;navLinks.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+id));
      const act=navLinks.find(a=>a.classList.contains('on'));if(act){const ol=act.closest('ol');ol.scrollLeft=act.offsetLeft-ol.clientWidth/2+act.offsetWidth/2;}
      const sec=e.target; if(sec.dataset.read) markSec(sec.id);
    }})},{rootMargin:'-40% 0px -55% 0px'});
    document.querySelectorAll('section').forEach(s=>io.observe(s));
  }
  prog({seen:1});
  upd();markPlan();
})();
