(function () {
  'use strict';

  /* ---------- Sticky header shadow on scroll ---------- */
  const header = document.getElementById('siteHeader');
  const onScroll = () => {
    if (window.scrollY > 12) header.classList.add('is-scrolled');
    else header.classList.remove('is-scrolled');
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- Mobile burger menu ---------- */
  const burger = document.getElementById('burgerBtn');
  const mobileMenu = document.getElementById('mobileMenu');
  if (burger && mobileMenu) {
    burger.addEventListener('click', () => {
      const isOpen = burger.classList.toggle('is-open');
      mobileMenu.classList.toggle('is-open', isOpen);
      burger.setAttribute('aria-expanded', String(isOpen));
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    mobileMenu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        burger.classList.remove('is-open');
        mobileMenu.classList.remove('is-open');
        burger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }

  /* ---------- Dropdown a11y: toggle on click for keyboard users ---------- */
  document.querySelectorAll('.nav__item--has-submenu > .nav__link').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const expanded = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!expanded));
    });
  });

  /* ---------- Scroll reveal via IntersectionObserver ---------- */
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add('is-visible'));
  }

  /* ---------- CountUp for stats numbers ---------- */
  const counters = document.querySelectorAll('[data-count]');
  if ('IntersectionObserver' in window && counters.length) {
    const animate = (el) => {
      const target = parseInt(el.getAttribute('data-count'), 10) || 0;
      const duration = 1400;
      const start = performance.now();
      const tick = (now) => {
        const p = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - p, 3); // easeOutCubic
        el.textContent = Math.round(target * eased);
        if (p < 1) requestAnimationFrame(tick);
      };
      el.textContent = '0';
      requestAnimationFrame(tick);
    };
    const co = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            animate(entry.target);
            co.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.25 }
    );
    counters.forEach((el) => co.observe(el));
  }

  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Блок 1. Announcement Bar ---------- */
  (function announceBar() {
    const bar = document.getElementById('announce');
    if (!bar) return;
    if (localStorage.getItem('announceDismissed') === '1') return;

    document.body.classList.add('has-announce');
    bar.classList.add('is-shown');

    const slides = Array.from(bar.querySelectorAll('.announce__slide'));
    const dots = Array.from(bar.querySelectorAll('.announce__dot'));
    let idx = 0;
    let timer = null;

    const show = (n) => {
      idx = (n + slides.length) % slides.length;
      slides.forEach((s, i) => s.classList.toggle('is-active', i === idx));
      dots.forEach((d, i) => d.classList.toggle('is-active', i === idx));
    };
    const next = () => show(idx + 1);
    const start = () => { if (!prefersReduced && slides.length > 1) timer = setInterval(next, 5000); };
    const stop = () => { if (timer) { clearInterval(timer); timer = null; } };

    dots.forEach((d, i) => d.addEventListener('click', () => { stop(); show(i); start(); }));

    const dismiss = () => {
      stop();
      bar.classList.remove('is-shown');
      document.body.classList.remove('has-announce');
      localStorage.setItem('announceDismissed', '1');
    };
    const closeBtn = document.getElementById('announceClose');
    if (closeBtn) closeBtn.addEventListener('click', dismiss);

    show(0);
    start();
  })();

  /* ---------- Блок 6. Timeline storytelling ---------- */
  (function timelineStory() {
    const steps = Array.from(document.querySelectorAll('.timeline__step'));
    const fill = document.getElementById('timelineFill');
    if (!steps.length) return;

    const setActive = (activeIdx) => {
      steps.forEach((s, i) => s.classList.toggle('is-active', i <= activeIdx));
      if (fill) fill.style.height = ((activeIdx + 1) / steps.length * 100) + '%';
    };

    if (window.gsap && window.ScrollTrigger) {
      gsap.registerPlugin(ScrollTrigger);
      steps.forEach((step, i) => {
        ScrollTrigger.create({
          trigger: step,
          start: 'top center',
          end: 'bottom center',
          onToggle: (self) => { if (self.isActive) setActive(i); },
        });
      });
    } else if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) setActive(steps.indexOf(e.target));
        });
      }, { threshold: 0.6 });
      steps.forEach((s) => io.observe(s));
    } else {
      setActive(steps.length - 1);
    }
  })();

  /* ---------- Блок 7. Bento mouse-follow glow ---------- */
  document.querySelectorAll('.bento__tile').forEach((tile) => {
    tile.addEventListener('mousemove', (e) => {
      const r = tile.getBoundingClientRect();
      tile.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      tile.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });

  /* ---------- Блок 9b. Cases carousel (Swiper) ---------- */
  if (window.Swiper && document.getElementById('caseSwiper')) {
    const progress = document.getElementById('caseProgress');
    new Swiper('#caseSwiper', {
      slidesPerView: 1.1,
      spaceBetween: 20,
      grabCursor: true,
      navigation: { prevEl: '#casePrev', nextEl: '#caseNext' },
      breakpoints: {
        640: { slidesPerView: 2, spaceBetween: 20 },
        1024: { slidesPerView: 3, spaceBetween: 24 },
      },
      on: {
        progress(sw, p) { if (progress) progress.style.width = Math.max(8, p * 100) + '%'; },
        init(sw) { if (progress) progress.style.width = Math.max(8, (1 / sw.slides.length) * 100) + '%'; },
      },
    });
  }

  /* ---------- Блок 11b. Testimonials (Swiper coverflow) ---------- */
  if (window.Swiper && document.getElementById('testimonialsSwiper')) {
    new Swiper('#testimonialsSwiper', {
      effect: 'coverflow',
      grabCursor: true,
      centeredSlides: true,
      slidesPerView: 1.15,
      loop: false,
      coverflowEffect: { rotate: 0, stretch: 0, depth: 120, modifier: 2, slideShadows: false },
      pagination: { el: '#testimonialsPagination', clickable: true },
      breakpoints: { 768: { slidesPerView: 1.8 }, 1100: { slidesPerView: 2.4 } },
    });
  }

  /* ---------- Блок 12. CTA spotlight + form ---------- */
  (function ctaSection() {
    const cta = document.getElementById('cta');
    if (cta && !cta.classList.contains('cta--simple') && !prefersReduced) {
      cta.addEventListener('mousemove', (e) => {
        const r = cta.getBoundingClientRect();
        cta.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        cta.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    }
    const form = document.getElementById('ctaForm');
    const success = document.getElementById('ctaSuccess');
    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        if (!form.checkValidity()) { form.reportValidity(); return; }
        form.querySelectorAll('input, textarea, button').forEach((el) => { el.disabled = true; });
        if (success) success.hidden = false;
      });
    }
  })();

  /* ---------- Messenger FAB: theme by background under button ---------- */
  (function messengerFabTheme() {
    const fab = document.querySelector('.messenger-fab');
    if (!fab) return;

    const skipRoot = (el) =>
      el.closest('.messenger-fab, .cookie, .announce, #siteHeader');

    const update = () => {
      const rect = fab.getBoundingClientRect();
      const x = rect.left + rect.width / 2;
      const y = rect.top + rect.height / 2;
      fab.style.pointerEvents = 'none';
      const stack = document.elementsFromPoint(x, y);
      fab.style.pointerEvents = '';

      let theme = 'dark';
      for (const el of stack) {
        if (skipRoot(el)) continue;
        const host = el.closest('[data-fab-theme]');
        if (host) {
          theme = host.dataset.fabTheme === 'light' ? 'light' : 'dark';
          break;
        }
      }

      fab.classList.toggle('is-on-light', theme === 'light');
      fab.classList.toggle('is-on-dark', theme === 'dark');
    };

    let ticking = false;
    const schedule = () => {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(() => {
        update();
        ticking = false;
      });
    };

    window.addEventListener('scroll', schedule, { passive: true });
    window.addEventListener('resize', schedule);
    schedule();
  })();

  /* ---------- Блок 14a. Cookie consent ---------- */
  (function cookieConsent() {
    const cookie = document.getElementById('cookie');
    if (!cookie) return;
    if (localStorage.getItem('cookieChoice')) return;
    cookie.hidden = false;
    const decide = (choice) => () => {
      localStorage.setItem('cookieChoice', choice);
      cookie.hidden = true;
    };
    const accept = document.getElementById('cookieAccept');
    const decline = document.getElementById('cookieDecline');
    if (accept) accept.addEventListener('click', decide('accepted'));
    if (decline) decline.addEventListener('click', decide('declined'));
  })();
})();
