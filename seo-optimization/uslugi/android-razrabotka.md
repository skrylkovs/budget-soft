# Он-пейдж оптимизация: Разработка Android-приложений

## Scope

- **Страница:** `uslugi/android-razrabotka/` (https://www.budget-soft.ru/uslugi/android-razrabotka/)
- **Ядро:** `seo-core/uslugi/android-razrabotka.md` (17.07.2026, Вордстат добран)
- **Контент-документ:** `seo-pages/uslugi/android-razrabotka.md` (17.07.2026)
- **Версия до правок:** заглушка «в разработке»
- **Источник контента:** `docs/texts-usligi.md` §53 + `_generate_pages.py` (slug `android-razrabotka`)
- **Дата внедрения:** 17.07.2026

## Preflight и блокеры

- **Индексируемость:** локально HTTP 200 (sitemap 87 URL), self-canonical; production 404.
- **Мобильная версия:** section-lead ≤ 250 (max 211); вёрстка общая с проверенными на 320 px страницами.
- **Блокеры наблюдаемости:** www-зеркало не в Вебмастере; не в проде.
- **Каннибализация:** риск с `mobilnaya-razrabotka` (общая) и `ios-razrabotka` (пара) — разведён перелинковкой и разными интентами (натив Android vs натив iOS vs общая).

## Карта покрытия (после; до — заглушка)

| Интент | Приоритет | Зона | Статус |
|---|---|---|---|
| Разработка Android-приложений / для android | P0 | Title, H1, лид, блок «Что входит» | покрыт |
| Создание android приложения | P1 | тело, FAQ | покрыт |
| Приложение для android заказать | P1 | Title, CTA | покрыт |
| Разработка на Kotlin | P1 | блок «Натив на Kotlin», FAQ-2 | покрыт |
| Публикация Google Play / RuStore | P0 | блок «Публикация», FAQ-4, карточка «Знаем RuStore» | покрыт |
| Стоимость android приложения | P0 | {price-cards}, FAQ-1 | покрыт ⚠️ [≈ согласовать] |
| Kotlin vs Java / Flutter (инфо) | P1 | FAQ-2, FAQ-3 | покрыт |
| Общая мобильная / кросс / iOS | передан | ссылки | передан |
| android studio / с нуля / курсы | исключён | — | не таргетируется |

## Внесённые правки

| # | Зона | Стало | Обоснование | Источник |
|---|---|---|---|---|
| 1 | Title | «Разработка Android-приложений на заказ — от 250 000 ₽: нативные приложения на Kotlin с публикацией в Google Play и RuStore» | P0 + Kotlin + RuStore (Android-специфика РФ) + цена | §53 |
| 2 | H1 | «Разработка Android-приложений на заказ» | P0-макро | §53 |
| 3 | Description | Kotlin + RuStore/AppGallery + от 250 000 ₽ + исходники у вас | ценовой и отстроечный интент | SEO_DESCRIPTIONS |
| 4 | Структура | О решении → Что входит (4 бенто) → Натив vs кросс (compare) → Стоимость (3) → Процесс → Почему мы (4 бенто) + FAQ | контент-документ (конкуренты+ядро) | §53; SERVICE_BAND_ROWS |
| 5 | «О решении» | erp-map: когда нужен натив Android + 5 сигналов + spec-карточки | паттерн болей + массовость Android | SECTION_BODY_RENDERERS |
| 6 | Compare | «Кроссплатформа vs Натив Kotlin» | Kotlin vs Flutter (FAQ chillicode) | §53 {compare} |
| 7 | FAQ 7 + FAQPage | цена, Kotlin vs Java, Kotlin vs Flutter, Google Play/RuStore, сроки, фрагментация, iOS | вопросные интенты топа | SERVICE_FAQ |
| 8 | JSON-LD | Service+Offer lowPrice 250000 + FAQPage | SEO-цикл | SEO_ENHANCED_SLUGS |
| 9 | Карточка «Почему мы» | «Знаем RuStore и альтсторы» | Android-специфика РФ (факт сайта), отстройка | SERVICE_BAND_ROWS |

## Перелинковка

| Направление | Куда | Обоснование |
|---|---|---|
| исходящая | /uslugi/mobilnaya-razrabotka/ | родитель (общая мобильная) |
| исходящая | /uslugi/krossplatformennaya-razrabotka/ | «натив vs кросс», Kotlin vs Flutter |
| исходящая | /uslugi/ios-razrabotka/ | парная платформа |
| исходящая | /etapy/, /tehpodderzhka-i-soprovozhdenie/ | процесс и сопровождение |
| входящая (TODO) | mobilnaya-razrabotka → сюда | «нативная Android» — отдельной задачей |

## Фактология

- Мобильная от 220 000 ₽, натив Kotlin, MVP за 60 дней, публикация в сторах, «знаем RuStore и альтсторы» — **факты сайта** (mobilnaya-razrabotka).
- ⚠️ `[≈ согласовать]`: вилка Android от 250 000 ₽, с интеграциями от 550 000 ₽ (price-cards, FAQ-1, lowPrice, urls.json title).

## Анти-переспам-проверка

- «android studio»/«с нуля»/курсы не таргетированы (образовательный интент).
- Title/Description уникальны; лемма распределена.
- Видимый FAQ = FAQPage 1:1 (7=7); JSON-LD валиден.

## Верификация сборки

- `python _generate_pages.py`: выполнен 17.07.2026 (sitemap 87 URL).
- Программная проверка: 3 price-cards (1 featured), 1 compare-таблица, spec-карточки в signals, FAQ 7/7, lowPrice 250000, section-lead ≤ 250 (max 211), RuStore-карточка, перелинковка на 3 URL. Структура совпадает с эталонными.
- `urls.json`: title синхронизирован.
- Живой рендер 320 px — общая вёрстка с проверенными страницами.

## Индексация

| Действие | Статус | Примечание |
|---|---|---|
| Деплой | ожидает пользователя | вилка Android ⚠️ согласовать |
| Переобход | отложен | после деплоя + www-зеркала |

## Базовая линия и план контроля

- **Базовая линия:** нулевая.
- **Контроль:** после деплоя — Мониторинг по «разработка android приложений», «создание android приложения», «разработка на kotlin»; **следить за каннибализацией** с mobilnaya-razrabotka и ios-razrabotka.
- **Семья страниц:** mobilnaya-razrabotka (родитель) / ios-razrabotka / android-razrabotka / krossplatformennaya-razrabotka — согласовать разграничение интентов при финальной вычитке.
