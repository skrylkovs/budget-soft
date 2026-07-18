# Он-пейдж оптимизация: Разработка helpdesk / service desk систем

## Scope
`uslugi/razrabotka-helpdesk-sistem/`; ядро/контент-док/секция MD §64 (17.07.2026). Дата: 17.07.2026.

## Preflight и блокеры
Локально HTTP 200; production 404; section-lead ≤ 250 (max 113); вёрстка общая с проверенными. www-зеркало не в Вебмастере. **Спрос по «разработка service desk» ≈0 (19); «service desk система» 452 — выбор готового ПО** (Okdesk, ITSM365, Naumen). Страница нишевая — для полноты каталога и long-tail.

## Карта покрытия (после; до — заглушка)
service desk/helpdesk/разработка (P0, Title/H1/лид) — покрыт; приём/маршрутизация заявок (P1, блок+FAQ-3) — покрыт; SLA/приоритеты/эскалации (P1, блок+FAQ-4) — покрыт; база знаний/самообслуживание (P1, блок) — покрыт; каналы почта/портал/мессенджеры/телефония (P1, блок+FAQ-3) — покрыт; отчётность/интеграции (P1, блок) — покрыт; on-premise/импортозамещение (P1, FAQ-5) — покрыт; стоимость (P0, price-cards/FAQ-1) — покрыт ⚠️[≈ согласовать]; услуга поддержки по SLA — передан tehpodderzhka; обзоры Okdesk/ITSM365/курсы ITIL — исключён.

## Внесённые правки
Title/H1/Description (§64, SEO_DESCRIPTIONS); структура О решении → Что умеет (4 бенто) → Стоимость (3) → Процесс → Почему мы (4 бенто) + FAQ; «О решении» erp-map 5 сигналов; FAQ 5 + FAQPage; JSON-LD Service+AggregateOffer lowPrice 350000. Отстройка от коробок (свои SLA/процессы, все каналы в одной очереди, on-premise/импортозамещение).

## Перелинковка
исходящие: tehpodderzhka-i-soprovozhdenie (услуга поддержки по SLA), avtomatizaciya-biznesa, integracii-s-sistemami.

## Фактология
Профиль заказных корп-систем и услуга поддержки по SLA — факты сайта. ⚠️ `[≈ согласовать]`: от 350 000 ₽ (контур), от 800 000 ₽ (платформа).

## Анти-переспам
Обзоры готового service desk и курсы ITIL не таргетированы; Title/Description уникальны; FAQ = FAQPage 1:1 (5=5); JSON-LD валиден.

## Верификация сборки
`python _generate_pages.py` (sitemap 87 URL); page-soon отсутствует, 3 price-cards (1 featured) + 3 spec-карточки, signals, FAQ 5/5 = FAQPage 5, lowPrice 350000, serviceType «Разработка helpdesk / service desk системы», section-lead ≤ 250 (max 113). urls.json title синхронизирован.

## Индексация / контроль
Деплой/переобход — после согласования цен и деплоя (www-зеркало). База нулевая; спрос узкий — Мониторинг за длинный период; разграничить с tehpodderzhka (service desk = система, tehpodderzhka = наша услуга поддержки).
