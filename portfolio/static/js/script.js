'use strict';

/* ── Custom cursor ────────────────────────────── */
const cursor   = document.getElementById('cursor');
const follower = document.getElementById('cursorFollower');
let mx=0,my=0,fx=0,fy=0;
document.addEventListener('mousemove', e => {
  mx=e.clientX; my=e.clientY;
  if(cursor){ cursor.style.left=mx+'px'; cursor.style.top=my+'px'; }
});
(function tick(){
  fx+=(mx-fx)*.12; fy+=(my-fy)*.12;
  if(follower){ follower.style.left=fx+'px'; follower.style.top=fy+'px'; }
  requestAnimationFrame(tick);
})();
document.querySelectorAll('a,button,.btn,.mtype,.faq-q').forEach(el=>{
  el.addEventListener('mouseenter',()=>{
    if(cursor){cursor.style.transform='translate(-50%,-50%) scale(2.4)'}
    if(follower){follower.style.transform='translate(-50%,-50%) scale(1.3)'}
  });
  el.addEventListener('mouseleave',()=>{
    if(cursor){cursor.style.transform='translate(-50%,-50%) scale(1)'}
    if(follower){follower.style.transform='translate(-50%,-50%) scale(1)'}
  });
});

/* ── Read progress bar ────────────────────────── */
const progress = document.getElementById('readProgress');
window.addEventListener('scroll', ()=>{
  if(!progress) return;
  const h = document.documentElement;
  const pct = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100;
  progress.style.width = pct + '%';
}, {passive:true});

/* ── Nav scroll ───────────────────────────────── */
const nav = document.getElementById('nav');
const handleNav = () => nav && nav.classList.toggle('scrolled', window.scrollY > 40);
window.addEventListener('scroll', handleNav, {passive:true});
handleNav();

/* ── Mobile menu ──────────────────────────────── */
const toggle   = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');
if(toggle && navLinks){
  toggle.addEventListener('click', ()=>{
    const open = navLinks.classList.toggle('open');
    const [a,b,c] = toggle.querySelectorAll('span');
    if(open){
      a.style.cssText='transform:rotate(45deg) translate(5px,5px)';
      b.style.opacity='0';
      c.style.cssText='transform:rotate(-45deg) translate(5px,-5px)';
    } else {
      [a,b,c].forEach(s=>s.style.cssText='');
    }
  });
  navLinks.querySelectorAll('a').forEach(a=>
    a.addEventListener('click', ()=>{
      navLinks.classList.remove('open');
      toggle.querySelectorAll('span').forEach(s=>s.style.cssText='');
    })
  );
  // Fermer si clic hors menu
  document.addEventListener('click', e=>{
    if(!nav.contains(e.target)) navLinks.classList.remove('open');
  });
}

/* ── Scroll reveal ────────────────────────────── */
const revObs = new IntersectionObserver(entries=>{
  entries.forEach(e=>{
    if(!e.isIntersecting) return;
    const delay = parseInt(e.target.dataset.delay||0);
    setTimeout(()=>e.target.classList.add('visible'), delay);
    revObs.unobserve(e.target);
  });
}, {threshold:0.1});
document.querySelectorAll('.reveal').forEach(el=>revObs.observe(el));

/* ── Skill bars & lang bars ───────────────────── */
const barObs = new IntersectionObserver(entries=>{
  entries.forEach(e=>{
    if(!e.isIntersecting) return;
    e.target.querySelectorAll('.stag-fill,.sbar-fill,.lang-fill').forEach((b,i)=>{
      setTimeout(()=>{ b.style.width = b.dataset.w||'0%'; }, i*80);
    });
    barObs.unobserve(e.target);
  });
}, {threshold:0.2});
document.querySelectorAll('.stags,.skills-bars,.lang-list').forEach(el=>barObs.observe(el));

/* ── Flash auto-dismiss ───────────────────────── */
document.querySelectorAll('.flash').forEach(el=>{
  setTimeout(()=>{
    el.style.transition='opacity .5s';
    el.style.opacity='0';
    setTimeout(()=>el.remove(), 520);
  }, 5000);
});

/* ── Active nav link ──────────────────────────── */
const sections   = document.querySelectorAll('section[id]');
const navLinkEls = document.querySelectorAll('.nav-link');
window.addEventListener('scroll', ()=>{
  let cur='';
  sections.forEach(s=>{
    if(window.scrollY >= s.offsetTop - 150) cur=s.id;
  });
  navLinkEls.forEach(a=>{
    const href = a.getAttribute('href')||'';
    a.classList.toggle('active', href.endsWith('#'+cur));
  });
}, {passive:true});

/* ── Smooth scroll ────────────────────────────── */
document.querySelectorAll('a[href*="#"]').forEach(a=>{
  a.addEventListener('click', e=>{
    const hash = a.getAttribute('href').split('#')[1];
    const target = hash && document.getElementById(hash);
    if(target){ e.preventDefault(); target.scrollIntoView({behavior:'smooth'}); }
  });
});

/* ── Counter animation ────────────────────────── */
function animCount(el){
  const target = parseInt(el.dataset.target || el.textContent);
  if(isNaN(target)) return;
  let current = 0;
  const step = Math.ceil(target / 40);
  const t = setInterval(()=>{
    current = Math.min(current + step, target);
    el.textContent = current + (el.dataset.suffix || '');
    if(current >= target) clearInterval(t);
  }, 40);
}
const countObs = new IntersectionObserver(entries=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      e.target.querySelectorAll('[data-target]').forEach(animCount);
      countObs.unobserve(e.target);
    }
  });
}, {threshold:0.5});
document.querySelectorAll('.about-vstat-list,.hero-photo-wrap').forEach(el=>countObs.observe(el));

/* ── Back to top visibility ───────────────────── */
const btt = document.getElementById('backToTop');
if(btt){
  window.addEventListener('scroll', ()=>{
    btt.style.opacity = window.scrollY > 400 ? '1' : '0';
    btt.style.pointerEvents = window.scrollY > 400 ? 'auto' : 'none';
  }, {passive:true});
  btt.style.opacity='0';
}
