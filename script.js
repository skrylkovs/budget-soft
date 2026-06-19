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

    mobileMenu.querySelectorAll('a, button.js-open-contact').forEach((link) => {
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
    if (!bar || bar.hidden) return;
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
          start: 'top 78%',
          end: 'bottom 55%',
          onToggle: (self) => { if (self.isActive) setActive(i); },
        });
      });
    } else if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) setActive(steps.indexOf(e.target));
        });
      }, { threshold: 0.15, rootMargin: '0px 0px -28% 0px' });
      steps.forEach((s) => io.observe(s));
    } else {
      setActive(steps.length - 1);
    }
  })();

  /* ---------- Bento + workflow cards: mouse-follow glow ---------- */
  document.querySelectorAll('.bento__tile, .page-workflow__card').forEach((tile) => {
    tile.addEventListener('mousemove', (e) => {
      const r = tile.getBoundingClientRect();
      tile.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      tile.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });

  /* ---------- Этапы: одинаковая высота «Что происходит» и «Результат» в ряду ---------- */
  (function equalizeWorkflowBlocks() {
    const grid = document.querySelector('.page-workflow--layout');
    if (!grid) return;

    const rowGroups = () =>
      [...grid.querySelectorAll('.page-workflow__row')].map((row) =>
        [...row.querySelectorAll('.page-workflow__card')]
      );
    let resizeTimer;

    function equalizeGroup(nodes) {
      nodes.forEach((node) => node.style.removeProperty('min-height'));
      if (!nodes.length) return;
      const max = Math.max(...nodes.map((node) => node.getBoundingClientRect().height));
      nodes.forEach((node) => {
        node.style.minHeight = `${Math.ceil(max)}px`;
      });
    }

    function syncLeadCards() {
      const lead1 = grid.querySelector('.page-workflow__card--1');
      const lead4 = grid.querySelector('.page-workflow__card--4');
      if (!lead1 || !lead4) return;

      lead1.style.removeProperty('min-height');
      lead4.style.removeProperty('min-height');

      if (window.innerWidth <= 1100) return;

      const height = Math.max(lead1.offsetHeight, lead4.offsetHeight);
      const px = `${Math.ceil(height)}px`;
      lead1.style.minHeight = px;
      lead4.style.minHeight = px;
    }

    function run() {
      const cards = [...grid.querySelectorAll('.page-workflow__card')];
      const processes = cards.map((card) => card.querySelector('.page-workflow__process')).filter(Boolean);
      const results = cards.map((card) => card.querySelector('.page-workflow__result')).filter(Boolean);

      processes.forEach((node) => node.style.removeProperty('min-height'));
      results.forEach((node) => node.style.removeProperty('min-height'));

      if (window.innerWidth <= 640) {
        syncLeadCards();
        return;
      }

      const groups = rowGroups().filter((group) => group.length);

      groups.forEach((group) => {
        equalizeGroup(group.map((card) => card.querySelector('.page-workflow__result')).filter(Boolean));
      });

      syncLeadCards();
    }

    run();
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(run, 120);
    });
    if (document.fonts?.ready) document.fonts.ready.then(run);
    window.addEventListener('load', run);
  })();

  /* ---------- Блок 9b. Cases carousel (Swiper) ---------- */
  if (window.Swiper && document.getElementById('caseSwiper')) {
    const progress = document.getElementById('caseProgress');
    new Swiper('#caseSwiper', {
      slidesPerView: 1,
      spaceBetween: 25,
      grabCursor: true,
      navigation: { prevEl: '#casePrev', nextEl: '#caseNext' },
      breakpoints: {
        640: { slidesPerView: 2, spaceBetween: 25 },
        1024: { slidesPerView: 3, spaceBetween: 30 },
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

  /* ---------- Contact modal ---------- */
  (function contactModal() {
    const modal = document.getElementById('contactModal');
    if (!modal) return;

    const cookie = document.getElementById('cookie');
    const fab = document.querySelector('.messenger-fab');

    const open = () => {
      modal.hidden = false;
      document.body.style.overflow = 'hidden';
      if (cookie) cookie.hidden = true;
      if (fab) fab.style.visibility = 'hidden';
      requestAnimationFrame(() => modal.classList.add('is-open'));
      const closeBtn = modal.querySelector('.contact-modal__close');
      if (closeBtn) closeBtn.focus();
    };

    const close = () => {
      modal.classList.remove('is-open');
      window.setTimeout(() => {
        modal.hidden = true;
        document.body.style.overflow = '';
        if (cookie && !localStorage.getItem('cookieChoice')) cookie.hidden = false;
        if (fab) fab.style.visibility = '';
      }, 320);
    };

    document.querySelectorAll('.js-open-contact').forEach((el) => {
      el.addEventListener('click', (e) => {
        e.preventDefault();
        open();
      });
    });

    modal.querySelectorAll('[data-close-contact]').forEach((el) => {
      el.addEventListener('click', close);
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !modal.hidden) close();
    });
  })();

  /* ---------- Портфолио в меню: скролл к блоку кейсов на главной ---------- */
  (function portfolioMenuScroll() {
    const HASH = '#portfolio';
    const STORAGE_KEY = 'budgetSoftScrollPortfolio';
    const menuLinks = document.querySelectorAll(
      'header .nav__link[href*="portfolio"], header .mobile-menu__link[href*="portfolio"]'
    );
    if (!menuLinks.length) return;

    const portfolioSection = () => document.querySelector('.cases#portfolio, #portfolio.cases');
    const isHomePage = () => !!portfolioSection();

    const scrollToPortfolio = (behavior = 'auto') => {
      const target = portfolioSection();
      if (!target) return false;
      target.scrollIntoView({ behavior, block: 'start' });
      return true;
    };

    const isPortfolioAligned = () => {
      const target = portfolioSection();
      if (!target) return true;
      const headerEl = document.getElementById('siteHeader');
      const offset = (headerEl?.offsetHeight ?? 0) + 16;
      return Math.abs(target.getBoundingClientRect().top - offset) <= 6;
    };

    const clearPortfolioScrollFlag = () => {
      try {
        sessionStorage.removeItem(STORAGE_KEY);
      } catch (_) {
        /* ignore */
      }
    };

    const shouldAlignPortfolio = () => {
      if (!isHomePage()) return false;
      if (location.hash === HASH) return true;
      try {
        return sessionStorage.getItem(STORAGE_KEY) === '1';
      } catch (_) {
        return false;
      }
    };

    const closeMobileMenu = () => {
      if (!burger || !mobileMenu) return;
      burger.classList.remove('is-open');
      mobileMenu.classList.remove('is-open');
      burger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    };

    const homeHashUrl = (link) => {
      const href = link.getAttribute('href') || '';
      if (href === HASH || href.endsWith(HASH)) return href;
      const base = href.replace(/#portfolio.*$/, '').replace(/\/?portfolio\/?$/, '');
      if (!base || base === '.') return HASH;
      return `${base.endsWith('/') ? base : `${base}/`}#portfolio`;
    };

    menuLinks.forEach((link) => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        if (isHomePage()) {
          scrollToPortfolio('smooth');
          closeMobileMenu();
          history.replaceState(null, '', HASH);
        } else {
          try {
            sessionStorage.setItem(STORAGE_KEY, '1');
          } catch (_) {
            /* ignore */
          }
          window.location.href = homeHashUrl(link);
        }
      });
    });

    const alignPortfolio = () => {
      if (!shouldAlignPortfolio()) return;
      scrollToPortfolio('auto');
      if (isPortfolioAligned()) {
        clearPortfolioScrollFlag();
        if (location.hash !== HASH) history.replaceState(null, '', HASH);
      }
    };

    const schedulePortfolioAlign = () => {
      if (!shouldAlignPortfolio()) return;

      alignPortfolio();
      requestAnimationFrame(alignPortfolio);
      window.addEventListener('load', alignPortfolio, { once: true });

      [80, 200, 450, 900, 1500].forEach((ms) => {
        window.setTimeout(() => {
          if (!shouldAlignPortfolio()) return;
          alignPortfolio();
          if (isPortfolioAligned()) clearPortfolioScrollFlag();
        }, ms);
      });
    };

    if ('scrollRestoration' in history) {
      history.scrollRestoration = 'manual';
    }

    schedulePortfolioAlign();
    window.addEventListener('hashchange', schedulePortfolioAlign);
  })();

  /* ---------- Сроки в меню: скролл к блоку Time-to-Market ---------- */
  (function timelineMenuScroll() {
    const HASH = '#timeline';
    const STORAGE_KEY = 'budgetSoftScrollTimeline';
    const menuLinks = document.querySelectorAll(
      'header .nav__link[href*="#timeline"], header .nav__link[href*="#speed"], header .mobile-menu__link[href*="#timeline"], header .mobile-menu__link[href*="#speed"]'
    );
    if (!menuLinks.length) return;

    const timelineSection = () => document.querySelector('#timeline, #speed');
    const hasTimelineBlock = () => !!timelineSection();

    const timelineScrollOffset = () => {
      const headerEl = document.getElementById('siteHeader');
      return (headerEl?.offsetHeight ?? 0) + 40;
    };

    const scrollToTimeline = (behavior = 'auto') => {
      const target = timelineSection();
      if (!target) return false;
      const top = target.getBoundingClientRect().top + window.scrollY - timelineScrollOffset();
      window.scrollTo({ top: Math.max(0, top), behavior });
      return true;
    };

    const isTimelineAligned = () => {
      const target = timelineSection();
      if (!target) return true;
      const offset = timelineScrollOffset();
      return Math.abs(target.getBoundingClientRect().top - offset) <= 6;
    };

    const clearTimelineScrollFlag = () => {
      try {
        sessionStorage.removeItem(STORAGE_KEY);
      } catch (_) {
        /* ignore */
      }
    };

    const shouldAlignTimeline = () => {
      if (!hasTimelineBlock()) return false;
      const hash = location.hash;
      if (hash === HASH || hash === '#speed') return true;
      try {
        return sessionStorage.getItem(STORAGE_KEY) === '1';
      } catch (_) {
        return false;
      }
    };

    const closeMobileMenu = () => {
      if (!burger || !mobileMenu) return;
      burger.classList.remove('is-open');
      mobileMenu.classList.remove('is-open');
      burger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    };

    const homeHashUrl = (link) => {
      const href = link.getAttribute('href') || '';
      if (href === HASH || href === '#speed' || href.endsWith(HASH) || href.endsWith('#speed')) return href;
      const base = href.replace(/#(timeline|speed).*$/, '').replace(/\/?sroki\/?$/, '');
      if (!base || base === '.') return HASH;
      return `${base.endsWith('/') ? base : `${base}/`}${HASH}`;
    };

    const targetHash = (link) => {
      const href = link.getAttribute('href') || '';
      if (href.endsWith('#speed')) return '#speed';
      return HASH;
    };

    menuLinks.forEach((link) => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        if (hasTimelineBlock()) {
          scrollToTimeline('smooth');
          closeMobileMenu();
          history.replaceState(null, '', targetHash(link));
        } else {
          try {
            sessionStorage.setItem(STORAGE_KEY, '1');
          } catch (_) {
            /* ignore */
          }
          window.location.href = homeHashUrl(link);
        }
      });
    });

    const alignTimeline = () => {
      if (!shouldAlignTimeline()) return;
      scrollToTimeline('auto');
      if (isTimelineAligned()) {
        clearTimelineScrollFlag();
        const hash = location.hash === '#speed' ? '#speed' : HASH;
        if (location.hash !== hash) history.replaceState(null, '', hash);
      }
    };

    const scheduleTimelineAlign = () => {
      if (!shouldAlignTimeline()) return;

      alignTimeline();
      requestAnimationFrame(alignTimeline);
      window.addEventListener('load', alignTimeline, { once: true });

      [80, 200, 450, 900, 1500].forEach((ms) => {
        window.setTimeout(() => {
          if (!shouldAlignTimeline()) return;
          alignTimeline();
          if (isTimelineAligned()) clearTimelineScrollFlag();
        }, ms);
      });
    };

    scheduleTimelineAlign();
    window.addEventListener('hashchange', scheduleTimelineAlign);
  })();

  /* ---------- Border glow follows the cursor (team role cards) ---------- */
  (function borderGlow() {
    const cards = document.querySelectorAll('.role-card');
    if (!cards.length) return;
    cards.forEach((card) => {
      card.addEventListener('pointermove', (e) => {
        const r = card.getBoundingClientRect();
        card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        card.style.setProperty('--my', (e.clientY - r.top) + 'px');
        card.classList.add('is-glow');
      });
      card.addEventListener('pointerleave', () => card.classList.remove('is-glow'));
    });
  })();

  /* ---------- Карусель команды: стрелки на мобиле ---------- */
  (function teamCarousel() {
    const track = document.getElementById('teamRoles');
    if (!track) return;
    const prev = document.querySelector('.team__arrow--prev');
    const next = document.querySelector('.team__arrow--next');
    if (!prev || !next) return;

    const update = () => {
      const overflow = track.scrollWidth - track.clientWidth;
      const scrollable = overflow > 1;
      prev.hidden = !scrollable;
      next.hidden = !scrollable;
      if (!scrollable) return;
      prev.disabled = track.scrollLeft <= 1;
      next.disabled = track.scrollLeft >= overflow - 1;
    };

    const page = (dir) => {
      track.scrollBy({ left: dir * track.clientWidth, behavior: 'smooth' });
    };

    prev.addEventListener('click', () => page(-1));
    next.addEventListener('click', () => page(1));
    track.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
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
