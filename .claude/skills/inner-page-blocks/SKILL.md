---
name: inner-page-blocks
description: "Справочник типов контентных блоков на неглавных (внутренних) страницах сайта BUDGET SOFT — страницы услуг и т.п. Описывает разметку каждого блока: шапка секции (бровь + заголовок + лид), белый прозы-бенд с page-spec-cards (Цена / Сроки / Формат оплаты), сравнительная таблица compare--service, ряды бенто-блоков page-prose-bands__row, блок «Отрасли» (ai-directions) и блок FAQ (page-faq). Используй как справку по классам и структуре, когда нужно понять или воспроизвести блок внутренней страницы. Это только описание разметки — без сценариев генерации."
---

# Типы блоков контента на неглавных страницах

Справочник по контентным блокам внутренних страниц (страницы услуг и подобные,
`<body class="page-body page-inner">`). Только описание разметки: какие классы,
какая структура. Живой пример со всеми блоками —
[uslugi/razrabotka-erp-sistem/index.html](../../../uslugi/razrabotka-erp-sistem/index.html).

## Общие соглашения

- Каждая смысловая секция обёрнута в
  `<section class="revolution" id="..." data-fab-theme="light"><div class="container">…</div></section>`.
  `id` — якорь секции, `data-fab-theme` — тема плавающей кнопки (`light`/`dark`).
- Класс `reveal` — анимация появления при скролле; класс `is-visible` добавляет JS,
  когда блок попадает в вид. В статичной разметке можно писать `reveal` без `is-visible`.
- `page-prose--band--bare` — вариант прозы-бенда **без** карточной подложки (белого фона,
  рамки, hover). Используется как обёртка для шапок-подсекций и полноширинного контента
  (сравнительная таблица, списки). Обычная `page-prose--band` (без `--bare`) — это
  карточка-бенто с белым фоном.
- `page-prose--full` — проза на всю ширину контейнера; `page-prose--service` — контекст
  страницы услуги.

## Шапка секции (бровь + заголовок + лид)

Открывает большинство блоков (Тип 1, 2, 3, FAQ). «Небольшой текст» из ТЗ — это
`.section-lead`. Заголовок — `<h1>` для главного заголовка страницы, иначе `<h2>`.

```html
<div class="section-head reveal">
  <span class="section-rule"></span>
  <span class="eyebrow">Бровь</span>
  <h1 class="section-title">Заголовок <span class="text-gradient">акцент</span></h1>
  <p class="section-lead"><strong>Ключевая мысль.</strong> Небольшой вводный текст.</p>
</div>
```

**Важно:** после `.section-title` — ровно один абзац `<p class="section-lead">`,
никогда не два и больше. Если нужно уместить несколько мыслей, объединяй их в
одном абзаце (первую мысль можно выделить `<strong>`), а не разбивай на
несколько `<p>`.

**Длина лида:** `.section-lead` — короткий, **не более 250 символов** (одно-два
предложения). Это касается и вводного лида страницы услуги (абзац под H1 у
enhanced-slug — он тоже выводится как `.section-lead`), и лидов всех секций
(`{section: …}` → первый абзац после `### заголовка`). Если мысль не помещается
в 250 символов — вынеси подробности в тело блока (bento-карточку, прозу, список),
а лид оставь тезисным. Длинный лид визуально разъезжается и перегружает шапку.

**Перенос строки в `.section-title`:** длинный заголовок секции разбивай на две
сбалансированные строки литеральным `<br>` в MD-заголовке (`### …`), поставив его
в естественном месте (напр. `### Почему разработку в Telegram<br>заказывают у
BUDGET SOFT` → «Почему разработку в Telegram» / «заказывают у BUDGET SOFT»).
Градиент хвоста сохраняется: `_gradient_title` в генераторе подсвечивает последние
два слова (или хвост после «—»), а `<br>` ставь **не внутри** этих двух слов —
иначе `<span class="text-gradient">` захватит `<br>`.

Та же шапка встречается вложенной внутри `page-prose--band--bare` как заголовок
подсекции (тогда заголовок — `<h2>`, а обёртка `.section-head` без `reveal`).
Правило про единственный `.section-lead` действует и там — это касается всех
блоков, которые открываются такой шапкой: Тип 1, Тип 2 и Тип 3.

## Тип блока 1 — прозы-бенд с белой панелью и spec-картами

Шапка секции (см. выше — один `.section-lead`), затем большой блок с белым
фоном: заголовки `page-prose__heading`, абзацы, а внутри — карточки
`page-spec-cards` (визуально 3 в ширину: Цена + Сроки + Формат оплаты).

```html
<div class="page-prose page-prose--service page-prose--full page-prose--band reveal is-visible">
  <h2 class="page-prose__heading">Подзаголовок</h2>
  <p>…</p>
  <p>…</p>

  <h2 class="page-prose__heading">Подзаголовок</h2>
  <p>…</p>

  <div class="page-spec-cards">
    <div class="page-spec-cards__item reveal">
      <p class="page-spec-cards__label"><svg class="page-spec-cards__icon" …></svg><span>Цена</span></p>
      <p class="page-spec-cards__value">От 300 000 руб.</p>
    </div>
    <div class="page-spec-cards__item reveal">
      <p class="page-spec-cards__label"><svg class="page-spec-cards__icon" …></svg><span>Сроки</span></p>
      <p class="page-spec-cards__value">От 2.5 до 6 месяцев</p>
    </div>
    <div class="page-spec-cards__item reveal">
      <p class="page-spec-cards__label"><svg class="page-spec-cards__icon" …></svg><span>Формат оплаты</span></p>
      <p class="page-spec-cards__value">Поэтапный · 30% / 30% / 40%</p>
    </div>
  </div>
</div>
```

`page-spec-cards` — обычно три `page-spec-cards__item` (Цена / Сроки / Формат оплаты),
каждая: `page-spec-cards__label` (иконка + подпись) и `page-spec-cards__value`.

## Тип блока 2 — сравнительная таблица

Шапка секции (см. выше — один `.section-lead`), затем большая сравнительная
таблица `compare compare--service`: строка-шапка `compare__head` и строки
`compare__row`. Колонки — «label» (критерий),
«legacy» (типовое/коробочное) и «ai» (решение под клиента). У ячеек данных `data-label`
дублирует заголовок колонки для мобильной раскладки.

```html
<div class="compare compare--service">
  <div class="compare__head">
    <div class="compare__head-cell compare__head-cell--label">Критерий</div>
    <div class="compare__head-cell compare__head-cell--legacy"><span class="compare__tag compare__tag--legacy">Типовая платформа</span>1С:ERP / коробка</div>
    <div class="compare__head-cell compare__head-cell--ai"><span class="compare__tag compare__tag--ai">Разработка под вас</span>Кастомная ERP на заказ</div>
  </div>
  <div class="compare__row">
    <div class="compare__cell compare__cell--label">Соответствие процессам</div>
    <div class="compare__cell compare__cell--legacy" data-label="1С:ERP / коробка">Процессы под возможности продукта</div>
    <div class="compare__cell compare__cell--ai" data-label="Кастомная ERP на заказ">Полностью под ваши процессы</div>
  </div>
  <!-- ещё строки compare__row -->
</div>
```

## Тип блока 3 — ряды бенто-блоков

Шапка секции (см. выше — один `.section-lead`), затем от 2 до 6 бенто-блоков,
разложенных по рядам `page-prose-bands__row` (по одному, два или три в ширину).
Каждый бенто — карточка
`page-prose--band` (белый фон) с `page-prose__heading` и абзацами. Модификаторы ряда:
`--first` (первый ряд), `--last` (последний) — управляют скруглениями/стыковкой карточек.

```html
<div class="page-prose-bands__row page-prose-bands__row--first">
  <div class="page-prose page-prose--service page-prose--full page-prose--band reveal is-visible">
    <h2 class="page-prose__heading">Заголовок бенто</h2>
    <p>…</p>
    <p>…</p>
  </div>
  <div class="page-prose page-prose--service page-prose--full page-prose--band reveal is-visible">
    <h2 class="page-prose__heading">Заголовок бенто</h2>
    <p>…</p>
    <p>…</p>
  </div>
</div>

<div class="page-prose-bands__row page-prose-bands__row--last">
  <div class="page-prose page-prose--service page-prose--full page-prose--band reveal is-visible">
    <h2 class="page-prose__heading">Заголовок бенто</h2>
    <p>…</p>
  </div>
  <div class="page-prose page-prose--service page-prose--full page-prose--band reveal is-visible">
    <h2 class="page-prose__heading">Заголовок бенто</h2>
    <p>…</p>
  </div>
</div>
```

Типы 1–3 обычно живут внутри общей обёртки `<div class="page-prose-bands">…</div>`,
где чередуются `page-prose--band--bare` (шапки подсекций, таблица) и
`page-prose-bands__row` (ряды бенто).

## Тип блока «Отрасли» (ai-directions)

Блок-плитка отраслей: слева шапка (бровь + двухстрочный заголовок + лид + счётчик),
справа список плиток `ai-direction` с иконкой и подписью.

```html
<section class="ai-directions reveal" aria-labelledby="aiDirectionsTitle">
  <div class="ai-directions__layout">
    <header class="ai-directions__head">
      <p class="ai-directions__eyebrow">Отрасли</p>
      <h3 class="ai-directions__title" id="aiDirectionsTitle">
        <span class="ai-directions__title-main">ERP-решения</span>
        <span class="ai-directions__title-sub">для вашей отрасли</span>
      </h3>
      <p class="ai-directions__lead">Вводный текст блока.</p>
      <p class="ai-directions__meta"><span class="ai-directions__count">18</span> направлений</p>
    </header>
    <ul class="ai-directions__list">
      <li class="ai-direction">
        <span class="ai-direction__icon" aria-hidden="true">
          <img src="../../images/ai-directions/industry.svg" alt="Промышленные предприятия" width="32" height="32" loading="lazy">
        </span>
        <span class="ai-direction__label">Промышленные предприятия</span>
      </li>
      <!-- ещё плитки ai-direction -->
    </ul>
  </div>
</section>
```

## Тип блока FAQ (page-faq)

Своя секция `revolution#faq` с шапкой (бровь «FAQ» + `h2`), затем аккордеон
`page-faq` из элементов `<details class="page-faq__item">`. Общий атрибут
`name="faq-faq"` держит открытым только один пункт. Вопрос — `h3.page-faq__q`
внутри `summary`, ответ — `p.page-faq__a` внутри `page-faq__answer`.

```html
<div class="page-faq reveal">
  <details class="page-faq__item" name="faq-faq">
    <summary class="page-faq__summary">
      <h3 class="page-faq__q">Вопрос?</h3>
      <span class="page-faq__icon" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M4 6l4 4 4-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
    </summary>
    <div class="page-faq__answer">
      <p class="page-faq__a">Ответ.</p>
    </div>
  </details>
  <!-- ещё пункты page-faq__item -->
</div>
```

Вопросы и ответы FAQ обычно дублируются в JSON-LD `FAQPage` в `<head>` страницы.
