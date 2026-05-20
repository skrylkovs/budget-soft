# M-SOFT IT — прототип главной (blocks 2, 3, 4, 5, 13)

Статичный прототип на чистых HTML/CSS/JS, без сборки и зависимостей.

Реализованы блоки из `site-structure-main-mvp.md`:

- **Блок 2** — Header / Navigation (sticky, dropdown «Услуги», мобильное меню)
- **Блок 3** — Hero с иконками направлений и 2 CTA-кнопками
- **Блок 4** — «Почему мы?» — вступление + 3 карточки + финальная фраза
- **Блок 5** — «Революция 2026» — таблица сравнения Legacy vs AI-Native
- **Блок 13** — Footer (4 колонки + соцсети + копирайт)

Все тексты взяты 1:1 из `site-structure-main-mvp.md`.

## Запуск

Любой статический сервер подойдёт. Например:

```bash
cd prototype-main
python3 -m http.server 8080
```

Открыть: http://localhost:8080

## Структура

```
prototype-main/
├── index.html   — разметка всех 5 блоков
├── styles.css   — стили (Inter, dark-тема + светлая секция «Почему мы»)
├── script.js    — sticky-хедер, mobile-меню, dropdown a11y, scroll-reveal
└── README.md
```

## Палитра

- Primary: `#e10600` (красный)
- Фон тёмный: `#0a0a12` / `#0f0f1c`
- Фон светлый (блок «Почему мы»): `#f6f6f9`
- Шрифт: Inter (Google Fonts)
