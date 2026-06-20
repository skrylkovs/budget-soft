# План доработок для запуска сайта BUDGET SOFT

## Контекст

Сайт BUDGET SOFT (prototype-main) — статический сайт из 27 страниц на русском, бо́льшая часть генерируется скриптом `_generate_pages.py` (подстраницы через `render_page`, главная — через `update_index_html`). Сейчас он живёт на `skrylkovs.github.io/budget-soft/` и не готов к публичному запуску и продвижению под Яндекс: есть фейковые контакты, нет своего домена, отсутствует базовый технический SEO (robots, sitemap, description на подстраницах, canonical, Open Graph, schema.org).

**Цель:** довести сайт до состояния, когда его можно публиковать на собственном домене `budget-soft.ru` и сдавать в Яндекс.Вебмастер без грубых дефектов.

**Решения пользователя:**

- Блог — скрыть до запуска (статьи отдельной задачей позже).
- Домен — я готовлю репозиторий (CNAME + абсолютные URL под `budget-soft.ru`); покупку домена и DNS-записи пользователь делает сам.

## Что уже хорошо (не трогаем)

Часть исходного аудита неактуальна — это уже закрыто:

- Не SPA: отдаётся готовый HTML (вопрос SSR снят).
- `<html lang="ru">`, контент полностью русский (нет смешения RU/EN).
- Ровно один `<h1>` на каждой из 27 страниц.
- `title` и `description` на главной — уникальные и развёрнутые.
- `loading="lazy"` на 576 из 630 `<img>`.
- Блог уже только в футере с бейджем «скоро» (не в главном меню).

## 🔴 Блокеры запуска

### 1. Контакты: убрать телефон, прописать реальные мессенджеры

**Решение пользователя:** телефон на сайте не нужен — убрать полностью. Вместо него — Telegram `@skrylkovs` и WhatsApp `+66634340262` на всех страницах (футер + contact-modal) и на странице контактов.

Все правки — в генераторе `_generate_pages.py`, затем перегон (плейсхолдер сейчас на всех 27 страницах, 136 вхождений; источник — генератор).

**Убрать телефон-плейсхолдер** `+7 (495) 000-00-00` / `tel:+74950000000` целиком из:
- футера, `<li>` с телефоном (строка ~1090);
- contact-modal, плитка «Телефон» (строки ~1162–1173) — удалить плитку;
- страницы контактов, футер (строка ~1361) и блок `page-contacts` (строка ~1512) — удалить `<li>` с телефоном.

**Прописать мессенджеры:**
- Telegram: `https://t.me/` → `https://t.me/skrylkovs` (contact-modal, строка 1145; страница контактов, строка 1514).
- WhatsApp: `https://wa.me/74950000000` → `https://wa.me/66634340262` (contact-modal, строка 1154). При необходимости добавить WhatsApp-ссылку и в `page-contacts`.

> Ввод от пользователя больше не требуется — телефон исключён.

### 2. Свой домен budget-soft.ru (подготовка репозитория)

Email на сайте уже `info@budget-soft.ru`, домен подразумевается.

- Создать файл `CNAME` в корне со значением `budget-soft.ru`.
- Использовать `https://budget-soft.ru` как базовый абсолютный URL в canonical / OG / sitemap (см. ниже).
- Покупку домена, DNS-записи (ALIAS/CNAME на GitHub Pages), включение HTTPS и 301 — делает пользователь.

## 🟠 Технический SEO (один проход через генератор)

Всё ниже удобно закрыть правкой `_generate_pages.py` с последующим перегоном `python3 _generate_pages.py`, плюс правка `update_index_html()` для главной.

### 3. robots.txt

Создать в корне:

```
User-agent: *
Allow: /
Sitemap: https://budget-soft.ru/sitemap.xml
```

### 4. sitemap.xml

Сгенерировать по 27 URL из `urls.json` с базой `https://budget-soft.ru`. Добавить функцию `write_sitemap()` в генератор и вызвать из `main()` — чтобы не вести вручную. Блог исключить из sitemap (решение: скрыт до запуска) → **26 URL**.

### 5. meta description на подстраницах (массовый дефект)

Сейчас `description` есть только на главной, остальные 26 страниц — без неё.

- Добавить параметр `description: str` в сигнатуру `render_page` (`_generate_pages.py:1219`).
- Вставить `<meta name="description" content="{description}">` в `<head>`-шаблон (после `<title>`).
- Передать уникальную `description` в каждом из 4 вызовов `render_page` и в цикле по uslugi (page-объекты в `_uslugi_data.py` — добавить туда поле `description`).

### 6. rel="canonical" (нет нигде, 0/27)

В тот же `<head>`-шаблон добавить `<link rel="canonical" href="https://budget-soft.ru/{path}/">` и аналогично в `update_index_html()` для главной.

### 7. Open Graph / Twitter Card (нет нигде)

Добавить в `<head>`-шаблон `og:type/title/description/url/image` (+ `twitter:card`). `og:image` — заранее подготовленная картинка-превью (кандидаты: `aurora-team.png`, `hero-section.png`). Минимум — главная, портфолио, страницы услуг.

### 8. schema.org JSON-LD (нет нигде)

- `Organization` на главной (name, url `https://budget-soft.ru`, email `info@budget-soft.ru`; телефон не указываем — его на сайте нет; при желании `contactPoint`/`sameAs` с Telegram/WhatsApp).
- `BreadcrumbList` / `Service` на страницах `uslugi/*` — опционально, через генератор.

## 🟡 Контент и индексация

### 9. Блог — скрыть до запуска

- Исключить `/blog/` из sitemap (п.4).
- Карточки-заглушки внутри `blog/index.html` не должны вести на несуществующие `/blog/<slug>/`.
- Футерную ссылку с бейджем «скоро» можно оставить (честно помечена), но из индексации убрать.

### 10. Яндекс.Вебмастер (после привязки домена — делает пользователь)

Добавить сайт, загрузить sitemap, задать регион (Россия), подтвердить организацию, проверить обход.

## Порядок выполнения

1. Телефон — заменить плейсхолдер в генераторе (нужен реальный номер).
2. `CNAME` + базовый URL `https://budget-soft.ru` зафиксировать в генераторе.
3. Генератор за один проход: `description` (+ поле в `_uslugi_data.py`), canonical, OG, JSON-LD в `render_page` и `update_index_html`; функции `write_robots()` и `write_sitemap()`.
4. Перегнать: `python3 _generate_pages.py`.
5. Блог — исключить из sitemap, проверить отсутствие битых ссылок.
6. (Пользователь) DNS, HTTPS, 301, Яндекс.Вебмастер.

## Файлы, которые будут изменены

- `_generate_pages.py` — `render_page` (head: description/canonical/OG/JSON-LD), `update_index_html`, новые `write_robots`/`write_sitemap`, вызовы из `main`.
- `_uslugi_data.py` — поле `description` для страниц услуг.
- `CNAME`, `robots.txt`, `sitemap.xml` — новые файлы в корне.
- Перегенерированные: `index.html` + все `*/index.html` (27 страниц).
- Реестр `urls.json` — без изменения существующих адресов (правило проекта).

## Проверка

- `python3 _generate_pages.py` отрабатывает без ошибок.
- `grep -L 'name="description"' */index.html index.html` — пусто (description у всех).
- `grep -L 'rel="canonical"' */index.html index.html` — пусто.
- В корне есть `CNAME`, `robots.txt`, `sitemap.xml`; sitemap содержит 26 URL (без блога), все с `https://budget-soft.ru`.
- `grep -rn '000-00-00\|+74950000000' .` — пусто (плейсхолдер вычищен).
- Локальный просмотр (`python3 -m http.server`) — главная, портфолио, услуга: в `<head>` видны description, canonical, og:*, ld+json; превью ссылки в Telegram отображается.
- Валидация JSON-LD через Schema Markup Validator / Яндекс.Вебмастер после деплоя.

---

## Чеклист выполнения

### Входные данные от пользователя
- [ ] Реальный номер телефона РФ получен
- [ ] Выбрана картинка `og:image` (`aurora-team.png` / `hero-section.png` / другая)
- [ ] Подтверждён базовый домен `https://budget-soft.ru`

### 🔴 Блокеры
- [ ] Телефон заменён в `_generate_pages.py` (6 мест: 1090, 1154, 1165, 1171, 1361, 1512)
- [ ] `wa.me/74950000000` заменён на реальный номер
- [ ] Создан `CNAME` со значением `budget-soft.ru`

### 🟠 Технический SEO (через генератор)
- [ ] `write_robots()` добавлена и вызвана из `main()` → создан `robots.txt`
- [ ] `write_sitemap()` добавлена и вызвана из `main()` → создан `sitemap.xml` (26 URL, без блога)
- [ ] Параметр `description` добавлен в `render_page`, `<meta name="description">` в `<head>`
- [ ] Поле `description` добавлено для всех страниц услуг в `_uslugi_data.py`
- [ ] `description` передан во все 4 вызова `render_page` и в `update_index_html()`
- [ ] `<link rel="canonical">` добавлен в `<head>`-шаблон и в `update_index_html()`
- [ ] Open Graph / Twitter Card добавлены в `<head>`-шаблон (главная, портфолио, услуги)
- [ ] JSON-LD `Organization` добавлен на главную
- [ ] (Опц.) JSON-LD `Service` / `BreadcrumbList` на страницах услуг

### 🟡 Контент и индексация
- [ ] `/blog/` исключён из sitemap
- [ ] Битые ссылки на `/blog/<slug>/` в `blog/index.html` устранены

### Перегон и проверка
- [ ] `python3 _generate_pages.py` отработал без ошибок
- [ ] `grep -L 'name="description"' */index.html index.html` — пусто
- [ ] `grep -L 'rel="canonical"' */index.html index.html` — пусто
- [ ] `grep -rn '000-00-00\|+74950000000' .` — пусто
- [ ] В корне присутствуют `CNAME`, `robots.txt`, `sitemap.xml`
- [ ] Локальный просмотр: в `<head>` видны description, canonical, og:*, ld+json
- [ ] JSON-LD прошёл валидацию (Schema Markup Validator)

### Пользователь (после деплоя)
- [ ] Куплен домен, настроены DNS (ALIAS/CNAME на GitHub Pages)
- [ ] Включён HTTPS, настроен 301-редирект
- [ ] Сайт добавлен в Яндекс.Вебмастер, загружен sitemap, задан регион (Россия)
