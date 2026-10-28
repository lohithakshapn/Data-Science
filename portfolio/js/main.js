/* ============================================================
   RAHUL.DS — QUANT LAB PORTFOLIO — main.js
   GSAP + ScrollTrigger + Lenis + canvas data-viz
   ============================================================ */
(function () {
  'use strict';

  gsap.registerPlugin(ScrollTrigger);
  var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Lenis smooth scroll ---------- */
  var lenis = null;
  if (!prefersReduced && typeof Lenis !== 'undefined') {
    lenis = new Lenis({ lerp: 0.08, wheelMultiplier: 1.1 });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
    gsap.ticker.lagSmoothing(0);
  }

  function scrollToTarget(target) {
    var el = document.querySelector(target);
    if (!el) return;
    if (lenis) { lenis.scrollTo(el, { offset: -70, duration: 1.4 }); }
    else { el.scrollIntoView({ behavior: 'smooth' }); }
  }

  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var href = a.getAttribute('href');
      if (href.length > 1) {
        e.preventDefault();
        scrollToTarget(href);
        var collapse = document.querySelector('.navbar-collapse.show');
        if (collapse) { bootstrap.Collapse.getOrCreateInstance(collapse).hide(); }
      }
    });
  });

  /* ---------- Custom cursor ---------- */
  var dot = document.getElementById('cursor-dot');
  var ring = document.getElementById('cursor-ring');
  if (window.matchMedia('(hover: hover) and (pointer: fine)').matches && dot && ring) {
    var dotX = gsap.quickTo(dot, 'x', { duration: 0.12, ease: 'power2.out' });
    var dotY = gsap.quickTo(dot, 'y', { duration: 0.12, ease: 'power2.out' });
    var ringX = gsap.quickTo(ring, 'x', { duration: 0.45, ease: 'power3.out' });
    var ringY = gsap.quickTo(ring, 'y', { duration: 0.45, ease: 'power3.out' });
    window.addEventListener('mousemove', function (e) {
      dotX(e.clientX); dotY(e.clientY); ringX(e.clientX); ringY(e.clientY);
    });
    document.querySelectorAll('a, button, [data-hover], input, textarea').forEach(function (el) {
      el.addEventListener('mouseenter', function () { ring.classList.add('is-hover'); });
      el.addEventListener('mouseleave', function () { ring.classList.remove('is-hover'); });
    });
  }

  /* ---------- Hero canvas: particle mesh + live waveform ---------- */
  var canvas = document.getElementById('hero-canvas');
  if (canvas) {
    var ctx = canvas.getContext('2d');
    var W = 0, H = 0, particles = [], wave = [], t = 0;
    var N = window.innerWidth < 768 ? 36 : 70;

    function resize() {
      W = canvas.width = canvas.offsetWidth * window.devicePixelRatio;
      H = canvas.height = canvas.offsetHeight * window.devicePixelRatio;
      ctx.setTransform(window.devicePixelRatio, 0, 0, window.devicePixelRatio, 0, 0);
      W = canvas.offsetWidth; H = canvas.offsetHeight;
    }
    resize();
    window.addEventListener('resize', resize);

    for (var i = 0; i < N; i++) {
      particles.push({
        x: Math.random() * window.innerWidth,
        y: Math.random() * window.innerHeight,
        vx: (Math.random() - 0.5) * 0.35,
        vy: (Math.random() - 0.5) * 0.35,
        r: Math.random() * 1.8 + 0.6
      });
    }

    function drawWave() {
      var base = H * 0.78, amp = 34;
      ctx.beginPath();
      for (var x = 0; x <= W; x += 6) {
        var y = base
          + Math.sin(x * 0.008 + t * 0.9) * amp
          + Math.sin(x * 0.021 + t * 1.7) * amp * 0.35;
        if (x === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.strokeStyle = 'rgba(0, 240, 255, 0.35)';
      ctx.lineWidth = 1.4;
      ctx.shadowColor = 'rgba(0, 240, 255, 0.8)';
      ctx.shadowBlur = 12;
      ctx.stroke();
      ctx.shadowBlur = 0;

      ctx.beginPath();
      for (var x2 = 0; x2 <= W; x2 += 6) {
        var y2 = base + 40
          + Math.sin(x2 * 0.006 + t * 0.6 + 2) * amp * 0.7;
        if (x2 === 0) ctx.moveTo(x2, y2); else ctx.lineTo(x2, y2);
      }
      ctx.strokeStyle = 'rgba(0, 255, 157, 0.16)';
      ctx.lineWidth = 1;
      ctx.stroke();
    }

    function tick() {
      t += 0.012;
      ctx.clearRect(0, 0, W, H);

      for (var i = 0; i < particles.length; i++) {
        var p = particles[i];
        p.x += p.vx; p.y += p.vy;
        if (p.x < 0 || p.x > W) p.vx *= -1;
        if (p.y < 0 || p.y > H) p.vy *= -1;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(0, 240, 255, 0.55)';
        ctx.fill();

        for (var j = i + 1; j < particles.length; j++) {
          var q = particles[j];
          var dx = p.x - q.x, dy = p.y - q.y;
          var d = Math.sqrt(dx * dx + dy * dy);
          if (d < 130) {
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(q.x, q.y);
            ctx.strokeStyle = 'rgba(0, 240, 255,' + (0.14 * (1 - d / 130)) + ')';
            ctx.lineWidth = 0.6;
            ctx.stroke();
          }
        }
      }
      drawWave();
      requestAnimationFrame(tick);
    }
    if (!prefersReduced) tick();
  }

  /* ---------- Preloader + hero intro ---------- */
  var preloader = document.getElementById('preloader');
  var countEl = document.getElementById('preloader-count');
  var fillEl = document.getElementById('preloader-fill');
  var logEl = document.getElementById('preloader-log');
  var logs = ['loading kernels…', 'fitting ARIMA(p,d,q)…', 'calibrating XGBoost…', 'rendering telemetry…', 'signal locked.'];

  gsap.set('.hero-title .line-inner', { yPercent: 110 });
  gsap.set('[data-hero-fade]', { autoAlpha: 0, y: 24 });

  var counter = { v: 0 };
  var loadTl = gsap.timeline();
  loadTl.to(counter, {
    v: 100,
    duration: prefersReduced ? 0.1 : 1.6,
    ease: 'power2.inOut',
    onUpdate: function () {
      var v = Math.round(counter.v);
      countEl.textContent = ('00' + v).slice(-3);
      fillEl.style.width = v + '%';
      logEl.textContent = logs[Math.min(logs.length - 1, Math.floor(v / 25))];
    }
  })
  .to(preloader, {
    yPercent: -100, duration: 0.8, ease: 'power4.inOut',
    onComplete: function () { preloader.style.display = 'none'; }
  }, '+=0.15')
  .to('.hero-title .line-inner', {
    yPercent: 0, duration: 1.15, ease: 'power4.out', stagger: 0.14
  }, '-=0.35')
  .to('[data-hero-fade]', {
    autoAlpha: 1, y: 0, duration: 0.9, ease: 'power3.out', stagger: 0.12
  }, '-=0.7');

  /* ---------- Nav state ---------- */
  var nav = document.getElementById('main-nav');
  window.addEventListener('scroll', function () {
    nav.classList.toggle('scrolled', window.scrollY > 40);
  }, { passive: true });

  var sections = document.querySelectorAll('section[id], header[id]');
  var navLinks = document.querySelectorAll('.quant-nav .nav-link');
  window.addEventListener('scroll', function () {
    var pos = window.scrollY + 140;
    sections.forEach(function (sec) {
      if (pos >= sec.offsetTop && pos < sec.offsetTop + sec.offsetHeight) {
        navLinks.forEach(function (l) {
          l.classList.toggle('active', l.getAttribute('href') === '#' + sec.id);
        });
      }
    });
  }, { passive: true });

  /* ---------- Scroll reveals ---------- */
  gsap.utils.toArray('[data-reveal]').forEach(function (el) {
    gsap.from(el, {
      autoAlpha: 0, y: 44, duration: 0.95, ease: 'power3.out',
      scrollTrigger: { trigger: el, start: 'top 86%' }
    });
  });

  gsap.utils.toArray('[data-reveal-group]').forEach(function (group) {
    gsap.from(group.children, {
      autoAlpha: 0, y: 50, duration: 0.85, ease: 'power3.out', stagger: 0.14,
      scrollTrigger: { trigger: group, start: 'top 84%' }
    });
  });

  /* ---------- Timeline conduit draw ---------- */
  var progress = document.getElementById('timeline-progress');
  if (progress) {
    gsap.to(progress, {
      scaleY: 1, ease: 'none',
      scrollTrigger: {
        trigger: '#timeline',
        start: 'top 75%',
        end: 'bottom 55%',
        scrub: 0.6
      }
    });
  }

  /* ---------- Counters ---------- */
  gsap.utils.toArray('.counter').forEach(function (el) {
    var target = parseInt(el.dataset.target, 10);
    var obj = { v: 0 };
    gsap.to(obj, {
      v: target, duration: 1.6, ease: 'power2.out',
      scrollTrigger: { trigger: el, start: 'top 90%' },
      onUpdate: function () { el.textContent = Math.round(obj.v); }
    });
  });

  /* ---------- Skill bars ---------- */
  gsap.utils.toArray('.skill-fill').forEach(function (fill) {
    var level = parseInt(fill.dataset.level, 10);
    var pct = fill.closest('.skill').querySelector('.skill-pct');
    var obj = { v: 0 };
    gsap.to(fill, {
      width: level + '%', duration: 1.4, ease: 'power3.out',
      scrollTrigger: { trigger: fill, start: 'top 90%' }
    });
    gsap.to(obj, {
      v: level, duration: 1.4, ease: 'power3.out',
      scrollTrigger: { trigger: fill, start: 'top 90%' },
      onUpdate: function () { pct.textContent = Math.round(obj.v) + '%'; }
    });
  });

  /* ---------- Hero parallax ---------- */
  if (!prefersReduced) {
    gsap.to('.hero-content', {
      y: -80, autoAlpha: 0.25, ease: 'none',
      scrollTrigger: { trigger: '#hero', start: 'top top', end: 'bottom top', scrub: true }
    });
  }

  /* ---------- Footer year ---------- */
  var yearEl = document.getElementById('footer-year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------- Contact form: validation + POST /api/contact ---------- */
  var form = document.getElementById('contact-form');
  if (form) {
    var status = document.getElementById('form-status');
    var submitBtn = document.getElementById('cf-submit');

    function setError(id, msg) {
      var input = document.getElementById('cf-' + id);
      var err = document.getElementById('err-' + id);
      err.textContent = msg || '';
      input.classList.toggle('is-invalid', !!msg);
      input.classList.toggle('is-valid', !msg);
    }

    function validate() {
      var ok = true;
      var name = form.name.value.trim();
      var email = form.email.value.trim();
      var subject = form.subject.value.trim();
      var message = form.message.value.trim();

      if (name.length < 2) { setError('name', '// ERROR: NAME REQUIRED (MIN 2 CHARS)'); ok = false; } else setError('name');
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) { setError('email', '// ERROR: VALID EMAIL REQUIRED'); ok = false; } else setError('email');
      if (subject.length < 3) { setError('subject', '// ERROR: SUBJECT REQUIRED (MIN 3 CHARS)'); ok = false; } else setError('subject');
      if (message.length < 10) { setError('message', '// ERROR: MESSAGE TOO SHORT (MIN 10 CHARS)'); ok = false; } else setError('message');
      return ok;
    }

    ['name', 'email', 'subject', 'message'].forEach(function (f) {
      form[f].addEventListener('input', function () {
        form[f].classList.remove('is-invalid');
        document.getElementById('err-' + f).textContent = '';
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      status.textContent = '';
      status.classList.remove('error');
      if (!validate()) {
        gsap.fromTo(form, { x: -8 }, { x: 0, duration: 0.4, ease: 'elastic.out(1, 0.35)' });
        status.textContent = '// TRANSMISSION BLOCKED: FIX FIELDS ABOVE';
        status.classList.add('error');
        return;
      }
      submitBtn.classList.add('is-sending');
      submitBtn.querySelector('.btn-label').textContent = 'TRANSMITTING…';

      fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          access_key: 'YOUR_WEB3FORMS_ACCESS_KEY',
          subject: form.subject.value.trim(),
          name: form.name.value.trim(),
          email: form.email.value.trim(),
          message: form.message.value.trim(),
          botcheck: ''
        })
      })
      .then(async function (res) {
        const data = await res.json().catch(() => ({}));

        if (!res.ok || data.success !== true) {
          console.error('Web3Forms error:', res.status, data);
          throw new Error(
            data.message || 'Submission failed (HTTP ' + res.status + ')'
          );
        }

        status.textContent = '// SIGNAL RECEIVED — MESSAGE SENT SUCCESSFULLY';
        status.classList.remove('error');

        form.reset();
        form.querySelectorAll('.form-control').forEach(function (c) {
          c.classList.remove('is-valid', 'is-invalid');
        });
      })
      .catch(function (err) {
        console.error('Contact form error:', err);
        status.textContent = '// UPLINK FAILED — ' + err.message;
        status.classList.add('error');
      })
      .finally(function () {
        submitBtn.classList.remove('is-sending');
        submitBtn.querySelector('.btn-label').textContent = 'TRANSMIT MESSAGE';
      });
    });
  }
})();
