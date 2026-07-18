// LogoLoop marquee (ported from reactbits.dev/animations/logo-loop to vanilla JS)
(function () {
  'use strict';

  /* ---------- Конфиг анимации (1:1 с оригиналом) ---------- */
  const ANIMATION_CONFIG = { SMOOTH_TAU: 0.25, MIN_COPIES: 2, COPY_HEADROOM: 2 };

  const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');

  function toCssLength(value) {
    return typeof value === 'number' ? `${value}px` : (value ?? undefined);
  }

  /* ---------- Ядро: один инстанс бесконечной ленты ----------
     Опции повторяют пропсы React-компонента один в один; добавлены только
     linkTarget (на сайте ссылки внутренние, а не target="_blank") и
     pauseOffscreen (глушим rAF, когда лента вне вьюпорта). */
  function initLogoLoop(container, options = {}) {
    const {
      logos = [],
      speed = 120,
      direction = 'left',
      width = '100%',
      logoHeight = 28,
      gap = 32,
      pauseOnHover,
      hoverSpeed,
      fadeOut = false,
      fadeOutColor,
      scaleOnHover = false,
      renderItem,
      ariaLabel = 'Partner logos',
      className,
      style,
      linkTarget = '_blank',
      pauseOffscreen = true
    } = options;

    if (!container || !logos.length) return null;

    const isVertical = direction === 'up' || direction === 'down';

    // Порядок веток тот же, что в useMemo оригинала: явный hoverSpeed важнее
    // pauseOnHover; pauseOnHover === false отключает реакцию на ховер вовсе.
    let effectiveHoverSpeed;
    if (hoverSpeed !== undefined) effectiveHoverSpeed = hoverSpeed;
    else if (pauseOnHover === true) effectiveHoverSpeed = 0;
    else if (pauseOnHover === false) effectiveHoverSpeed = undefined;
    else effectiveHoverSpeed = 0;

    const magnitude = Math.abs(speed);
    const directionMultiplier = isVertical ? (direction === 'up' ? 1 : -1) : (direction === 'left' ? 1 : -1);
    const speedMultiplier = speed < 0 ? -1 : 1;
    const targetVelocity = magnitude * directionMultiplier * speedMultiplier;

    /* ---------- Разметка ---------- */
    const root = document.createElement('div');
    root.className = [
      'logoloop',
      isVertical ? 'logoloop--vertical' : 'logoloop--horizontal',
      fadeOut && 'logoloop--fade',
      scaleOnHover && 'logoloop--scale-hover',
      className
    ].filter(Boolean).join(' ');
    root.setAttribute('role', 'region');
    root.setAttribute('aria-label', ariaLabel);
    root.style.setProperty('--logoloop-gap', `${gap}px`);
    root.style.setProperty('--logoloop-logoHeight', `${logoHeight}px`);
    if (fadeOutColor) root.style.setProperty('--logoloop-fadeColor', fadeOutColor);

    const cssWidth = toCssLength(width);
    if (isVertical) {
      if (cssWidth && cssWidth !== '100%') root.style.width = cssWidth;
    } else {
      root.style.width = cssWidth ?? '100%';
    }
    if (style) Object.assign(root.style, style);

    const track = document.createElement('div');
    track.className = 'logoloop__track';
    root.appendChild(track);

    function createItem(item, key) {
      const li = document.createElement('li');
      li.className = 'logoloop__item';
      li.setAttribute('role', 'listitem');
      li.dataset.key = key;

      // renderItem полностью отвечает за содержимое элемента, включая ссылку.
      if (typeof renderItem === 'function') {
        const rendered = renderItem(item, key);
        if (rendered instanceof Node) li.appendChild(rendered);
        else if (rendered != null) li.insertAdjacentHTML('beforeend', String(rendered));
        return li;
      }

      const isNodeItem = item && typeof item === 'object' && 'node' in item;
      let content;

      if (isNodeItem) {
        // Кастомная нода: Element клонируем, строку вставляем как разметку.
        content = document.createElement('span');
        content.className = 'logoloop__node';
        if (item.node instanceof Node) content.appendChild(item.node.cloneNode(true));
        else if (item.node != null) content.innerHTML = String(item.node);
        if (item.href && !item.ariaLabel) content.setAttribute('aria-hidden', 'true');
      } else {
        content = document.createElement('img');
        content.src = item.src;
        if (item.srcSet) content.srcset = item.srcSet;
        if (item.sizes) content.sizes = item.sizes;
        if (item.width) content.width = item.width;
        if (item.height) content.height = item.height;
        content.alt = item.alt ?? '';
        if (item.title) content.title = item.title;
        content.loading = 'lazy';
        content.decoding = 'async';
        content.draggable = false;
      }

      const itemAriaLabel = isNodeItem ? (item.ariaLabel ?? item.title) : (item.alt ?? item.title);

      if (item.href) {
        const link = document.createElement('a');
        link.className = 'logoloop__link';
        link.href = item.href;
        link.setAttribute('aria-label', itemAriaLabel || 'logo link');
        if (linkTarget && linkTarget !== '_self') {
          link.target = linkTarget;
          link.rel = 'noreferrer noopener';
        }
        link.appendChild(content);
        li.appendChild(link);
      } else {
        li.appendChild(content);
      }
      return li;
    }

    function buildSequence(copyIndex) {
      const list = document.createElement('ul');
      list.className = 'logoloop__list';
      list.setAttribute('role', 'list');
      logos.forEach((item, itemIndex) => {
        list.appendChild(createItem(item, `${copyIndex}-${itemIndex}`));
      });
      return list;
    }

    // Копии-дубли не должны читаться скринридером и не должны ловить Tab:
    // одного aria-hidden мало — ссылки внутри него остаются фокусируемыми.
    // ВАЖНО: inert здесь применять нельзя. По спецификации он отключает и
    // хит-тестинг («как если бы pointer-events: none»), а копии занимают
    // экран бо́льшую часть цикла — чипы стали бы некликабельными и без
    // :hover примерно в половине случаев. tabIndex = -1 убирает их из Tab,
    // не трогая мышь; клик по копии ведёт туда же, куда по оригиналу.
    function deactivateCopy(list) {
      list.setAttribute('aria-hidden', 'true');
      list.querySelectorAll('a[href], button, [tabindex]').forEach((el) => {
        el.tabIndex = -1;
      });
    }

    const seq = buildSequence(0);
    track.appendChild(seq);
    container.appendChild(root);

    /* ---------- Замеры и число копий ---------- */
    let seqWidth = 0;
    let seqHeight = 0;
    let copyCount = ANIMATION_CONFIG.MIN_COPIES;
    let reduced = motionQuery.matches;

    function syncCopies(needed) {
      // При reduce-motion лента не едет — дубли только мусорят DOM и выдачу.
      const target = reduced ? 1 : Math.max(ANIMATION_CONFIG.MIN_COPIES, needed);
      if (target === copyCount && track.children.length === copyCount) return;
      while (track.children.length > target) track.removeChild(track.lastElementChild);
      while (track.children.length < target) {
        const clone = seq.cloneNode(true);
        deactivateCopy(clone);
        track.appendChild(clone);
      }
      copyCount = target;
    }

    function updateDimensions() {
      const containerWidth = root.clientWidth ?? 0;
      const rect = seq.getBoundingClientRect();
      const sequenceWidth = rect?.width ?? 0;
      const sequenceHeight = rect?.height ?? 0;

      if (isVertical) {
        const parentHeight = root.parentElement?.clientHeight ?? 0;
        if (parentHeight > 0) {
          const targetHeight = Math.ceil(parentHeight);
          if (root.style.height !== `${targetHeight}px`) root.style.height = `${targetHeight}px`;
        }
        if (sequenceHeight > 0) {
          seqHeight = Math.ceil(sequenceHeight);
          const viewport = root.clientHeight || parentHeight || sequenceHeight;
          syncCopies(Math.ceil(viewport / sequenceHeight) + ANIMATION_CONFIG.COPY_HEADROOM);
        }
      } else if (sequenceWidth > 0) {
        // Без Math.ceil: браузер раскладывает копии по дробной ширине, а
        // округление модуля вверх на d = ceil(W) - W давало бы микро-рывок на
        // стыке раз в W/speed секунд. Модуль обязан совпадать с шагом копий.
        seqWidth = sequenceWidth;
        syncCopies(Math.ceil(containerWidth / sequenceWidth) + ANIMATION_CONFIG.COPY_HEADROOM);
      }

      applyTransform();
    }

    /* ---------- rAF-цикл ----------
       Почему стык не «прыгает»: трек состоит из N ≥ 2 БАЙТ-В-БАЙТ одинаковых
       копий последовательности, а offset всегда берётся по модулю ширины ОДНОЙ
       копии. В момент, когда offset переходит через seqSize и обнуляется,
       геометрия под вьюпортом идентична: копия k встаёт ровно туда, где
       миллисекунду назад стояла копия k+1. Пиксели не меняются — значит, и
       скачка нет. Число копий ceil(containerWidth / seqWidth) + 2 гарантирует,
       что видимая область всегда перекрыта с запасом в две копии. */
    let rafId = null;
    let lastTimestamp = null;
    let offset = 0;
    let velocity = 0;
    let isHovered = false;

    function transformFor(value) {
      return isVertical ? `translate3d(0, ${-value}px, 0)` : `translate3d(${-value}px, 0, 0)`;
    }

    function applyTransform() {
      const seqSize = isVertical ? seqHeight : seqWidth;
      if (seqSize > 0) {
        offset = ((offset % seqSize) + seqSize) % seqSize;
        track.style.transform = transformFor(reduced ? 0 : offset);
      }
    }

    function animate(timestamp) {
      if (lastTimestamp === null) lastTimestamp = timestamp;
      const deltaTime = Math.max(0, timestamp - lastTimestamp) / 1000;
      lastTimestamp = timestamp;

      const target = isHovered && effectiveHoverSpeed !== undefined ? effectiveHoverSpeed : targetVelocity;

      // Экспоненциальное сглаживание: плавный разгон/торможение вместо рывка.
      const easingFactor = 1 - Math.exp(-deltaTime / ANIMATION_CONFIG.SMOOTH_TAU);
      velocity += (target - velocity) * easingFactor;

      const seqSize = isVertical ? seqHeight : seqWidth;
      if (seqSize > 0) {
        let nextOffset = offset + velocity * deltaTime;
        nextOffset = ((nextOffset % seqSize) + seqSize) % seqSize;
        offset = nextOffset;
        track.style.transform = transformFor(offset);
      }

      rafId = requestAnimationFrame(animate);
    }

    function startLoop() {
      if (rafId !== null || reduced) return;
      lastTimestamp = null; // иначе после паузы прилетит гигантский deltaTime
      rafId = requestAnimationFrame(animate);
    }

    function stopLoop() {
      if (rafId === null) return;
      cancelAnimationFrame(rafId);
      rafId = null;
      lastTimestamp = null;
    }

    // В фоновой вкладке rAF просто перестаёт тикать, а IntersectionObserver
    // не срабатывает — stopLoop не вызывается, lastTimestamp остаётся старым.
    // Первый кадр после возврата принёс бы deltaTime во всю длительность
    // паузы: easingFactor насытился бы до 1, а offset прыгнул бы на случайную
    // фазу. Сбрасываем отметку времени — тогда первый кадр стоит нисколько.
    function handleVisibility() {
      lastTimestamp = null;
    }
    document.addEventListener('visibilitychange', handleVisibility);

    /* ---------- Ховер ---------- */
    function handleMouseEnter() {
      if (effectiveHoverSpeed !== undefined) isHovered = true;
    }
    function handleMouseLeave() {
      if (effectiveHoverSpeed !== undefined) isHovered = false;
    }
    track.addEventListener('mouseenter', handleMouseEnter);
    track.addEventListener('mouseleave', handleMouseLeave);
    // Клавиатура: фокус на ссылке тоже останавливает ленту, иначе по ней не попасть.
    track.addEventListener('focusin', handleMouseEnter);
    track.addEventListener('focusout', handleMouseLeave);

    /* ---------- Наблюдатели размеров ---------- */
    let resizeObserver = null;
    let resizeTimer = null;

    function handleWindowResize() {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(updateDimensions, 120);
    }

    if ('ResizeObserver' in window) {
      resizeObserver = new ResizeObserver(updateDimensions);
      resizeObserver.observe(root);
      resizeObserver.observe(seq);
    } else {
      window.addEventListener('resize', handleWindowResize);
    }

    /* ---------- Ожидание картинок и шрифтов ----------
       Оригинал ждёт только <img>. Здесь элементы могут быть текстовыми
       вордмарками, поэтому дополнительно перезамеряемся после подгрузки
       веб-шрифта — иначе seqWidth посчитается по метрикам фолбэка. */
    function waitForImages() {
      const images = seq.querySelectorAll('img');
      if (images.length === 0) {
        updateDimensions();
        return;
      }
      let remainingImages = images.length;
      const handleImageLoad = () => {
        remainingImages -= 1;
        if (remainingImages === 0) updateDimensions();
      };
      images.forEach((img) => {
        if (img.complete) handleImageLoad();
        else {
          img.addEventListener('load', handleImageLoad, { once: true });
          img.addEventListener('error', handleImageLoad, { once: true });
        }
      });
    }

    waitForImages();
    document.fonts?.ready.then(updateDimensions).catch(() => {});
    window.addEventListener('load', updateDimensions, { once: true });

    /* ---------- Гейт по вьюпорту ---------- */
    let intersectionObserver = null;
    if (pauseOffscreen && 'IntersectionObserver' in window) {
      intersectionObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) startLoop();
          else stopLoop();
        });
      }, { rootMargin: '200px' });
      intersectionObserver.observe(root);
    } else {
      startLoop();
    }

    /* ---------- Реакция на смену prefers-reduced-motion ---------- */
    function handleMotionChange() {
      reduced = motionQuery.matches;
      root.classList.toggle('logoloop--static', reduced);
      if (reduced) {
        stopLoop();
        offset = 0;
        track.style.transform = transformFor(0);
      }
      updateDimensions();
      if (!reduced) startLoop();
    }
    if (motionQuery.addEventListener) motionQuery.addEventListener('change', handleMotionChange);
    else if (motionQuery.addListener) motionQuery.addListener(handleMotionChange);
    if (reduced) root.classList.add('logoloop--static');

    function destroy() {
      stopLoop();
      clearTimeout(resizeTimer);
      resizeObserver?.disconnect();
      intersectionObserver?.disconnect();
      window.removeEventListener('resize', handleWindowResize);
      document.removeEventListener('visibilitychange', handleVisibility);
      if (motionQuery.removeEventListener) motionQuery.removeEventListener('change', handleMotionChange);
      else if (motionQuery.removeListener) motionQuery.removeListener(handleMotionChange);
      track.removeEventListener('mouseenter', handleMouseEnter);
      track.removeEventListener('mouseleave', handleMouseLeave);
      track.removeEventListener('focusin', handleMouseEnter);
      track.removeEventListener('focusout', handleMouseLeave);
      root.remove();
    }

    return { destroy, update: updateDimensions };
  }

  /* ================================================================
     Монтаж на главной: полоса стека между Портфолио и FAQ
     ================================================================ */

  /* Нейтральные геометрические значки-категории. Это НЕ логотипы брендов —
     рисовать неточные торговые знаки нельзя. Когда появятся настоящие SVG/PNG,
     достаточно добавить item.src (картинка) или item.svg (инлайн-разметка):
     renderTechChip уже умеет и то, и другое, модуль переписывать не нужно. */
  const TECH_MARKS = {
    code: '<path d="M9.5 7 4.5 12l5 5"/><path d="m14.5 7 5 5-5 5"/>',
    server: '<rect x="3.25" y="4.25" width="17.5" height="6.5" rx="2"/><rect x="3.25" y="13.25" width="17.5" height="6.5" rx="2"/>',
    device: '<rect x="7.25" y="3.25" width="9.5" height="17.5" rx="2.5"/><path d="M10.5 17.4h3"/>',
    blocks: '<rect x="3.5" y="3.5" width="7" height="7" rx="1.6"/><rect x="13.5" y="3.5" width="7" height="7" rx="1.6"/><rect x="3.5" y="13.5" width="7" height="7" rx="1.6"/><rect x="13.5" y="13.5" width="7" height="7" rx="1.6"/>'
  };

  function markSvg(name) {
    const body = TECH_MARKS[name] || TECH_MARKS.code;
    return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" focusable="false" aria-hidden="true">${body}</svg>`;
  }

  // Порядок подобран так, чтобы значки категорий чередовались и лента
  // не выглядела как четыре слипшихся блока одинаковых иконок.
  const TECH_FALLBACK = [
    { name: 'Laravel', href: '/tehnologii/laravel/', mark: 'server' },
    { name: 'React', href: '/tehnologii/react/', mark: 'code' },
    { name: 'Flutter', href: '/tehnologii/flutter/', mark: 'device' },
    { name: 'Python', href: '/tehnologii/python/', mark: 'server' },
    { name: 'TypeScript', href: '/tehnologii/typescript/', mark: 'code' },
    { name: '1С', href: '/tehnologii/1c/', mark: 'blocks' },
    { name: 'Node.js', href: '/tehnologii/nodejs/', mark: 'server' },
    { name: 'Vue.js', href: '/tehnologii/vue/', mark: 'code' },
    { name: 'Kotlin', href: '/tehnologii/kotlin/', mark: 'device' },
    { name: 'Java', href: '/tehnologii/java/', mark: 'server' },
    { name: 'Next.js', href: '/tehnologii/nextjs/', mark: 'code' },
    { name: '1С-Битрикс', href: '/tehnologii/bitrix/', mark: 'blocks' },
    { name: 'PHP', href: '/tehnologii/php/', mark: 'server' },
    { name: 'Angular', href: '/tehnologii/angular/', mark: 'code' },
    { name: 'Swift', href: '/tehnologii/swift/', mark: 'device' },
    { name: 'Go', href: '/tehnologii/golang/', mark: 'server' },
    { name: 'Django', href: '/tehnologii/django/', mark: 'server' },
    { name: '.NET', href: '/tehnologii/dotnet/', mark: 'server' }
  ];

  /* Источник истины — статический список в HTML: он виден краулерам и
     работает без JS. Забираем элементы оттуда, а разметку-заглушку убираем. */
  function readItemsFromDom(mount) {
    const links = mount.querySelectorAll('.techstack__seed a[href]');
    if (!links.length) return null;
    return Array.from(links).map((a) => ({
      name: (a.textContent || '').trim(),
      href: a.getAttribute('href'),
      mark: a.dataset.mark || 'code',
      src: a.dataset.src || undefined
    }));
  }

  function renderTechChip(item) {
    const chip = document.createElement(item.href ? 'a' : 'span');
    // logoloop__node — чтобы работали базовые правила scaleOnHover из порта.
    chip.className = 'logoloop__link logoloop__node tech-logo';
    if (item.href) {
      chip.href = item.href;
      chip.setAttribute('aria-label', `Технологии: ${item.name}`);
    }

    const mark = document.createElement('span');
    mark.className = 'tech-logo__mark';
    mark.setAttribute('aria-hidden', 'true');
    if (item.src) {
      // Логотипы Simple Icons одноцветные и чёрные. Через <img> их не
      // перекрасить, поэтому кладём файл в mask и заливаем currentColor —
      // так логотип живёт в цвете текста чипа и меняется на ховере вместе с ним.
      mark.classList.add('tech-logo__mark--icon');
      mark.style.setProperty('--tech-icon', `url("${item.src}")`);
    } else {
      mark.innerHTML = item.svg || markSvg(item.mark);
    }

    const label = document.createElement('span');
    label.className = 'tech-logo__name';
    label.textContent = item.name;

    chip.appendChild(mark);
    chip.appendChild(label);
    return chip;
  }

  const techMount = document.querySelector('.techstack__loop');
  // Флаг на элементе — страховка от повторного подключения скрипта: иначе
  // получили бы вторую ленту поверх первой и второй rAF-цикл. Ручку с
  // destroy/update кладём на элемент, чтобы лента поддавалась отладке.
  if (techMount && !techMount.dataset.logoloopReady) {
    techMount.dataset.logoloopReady = '1';
    const techLogos = readItemsFromDom(techMount) || TECH_FALLBACK;
    techMount.innerHTML = '';
    techMount.logoLoop = initLogoLoop(techMount, {
      logos: techLogos,
      speed: 46,
      direction: 'left',
      logoHeight: 55,
      gap: 60,
      pauseOnHover: true,
      fadeOut: true,
      fadeOutColor: '#0a0a14',
      scaleOnHover: true,
      linkTarget: '_self',
      ariaLabel: 'Технологии, с которыми мы работаем',
      renderItem: renderTechChip
    });
  }
})();
