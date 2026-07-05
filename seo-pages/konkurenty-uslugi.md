# Услуги конкурентов: сводный анализ (06.07.2026)

**Задача:** собрать список услуг, которые предоставляют конкуренты, — только те услуги, для которых на сайте конкурента создана **отдельная страница** (собственный URL).

**Источник списка конкурентов:** таблицы «Анализ конкурентов» в `seo-pages/uslugi/*.md` (razrabotka-crm-sistem, razrabotka-erp-sistem, mobilnaya-razrabotka, telegram-mini-apps). Агрегаторы (profi.ru, kwork, avito, youdo, Яндекс Услуги) и чисто статейные источники (habr, secrets.tbank.ru, cossa, okocrm, sky.pro, bothelp, chatlabs) исключены — это не студии-конкуренты.

**Метод:** по каждому сайту — разбор sitemap.xml, меню и хаба услуг с выборочной проверкой, что страницы реально существуют (параллельные агенты, 05–06.07.2026).

**Покрытие:** 36 компаний в списке → 34 разобраны, **801 услуга с отдельными страницами у 33 компаний**. botcreators.ru — одностраничный лендинг без отдельных страниц услуг. Недоступны: terralink.ru (DNS timeout оба дня), «НеСтудия» (домен не найден — вероятно, сайт закрыт или переименован).

---

## 1. Сводный список услуг (нормализованный)

Услуги сгруппированы по смыслу; в третьей колонке — конкуренты, у которых есть отдельная страница этой услуги. Полные названия и URL — в разделе «Детализация по конкурентам» ниже.

### Корпоративные системы

| Услуга | Конкурентов | Отдельная страница есть у |
|---|---|---|
| Разработка мобильных приложений | 20 | haulmont, tektosoft, surf, pyrobyte, nlabteam, atwinta, sibdev, kozhindev, chillicode, purrweb, wnfx, simbirsoft, appfox, softmg, is-art, koyutech, rarus, smorodina, cetera, novacom |
| Разработка CRM-систем | 14 | bpadevelop, novacom, clientbase, longcatdev, haulmont, tektosoft, surf, fichright, sibdev, kozhindev, purrweb, cetera, 10sec, salesap¹ |
| Разработка ERP-систем | 14 | bpadevelop, novacom, longcatdev, haulmont, tektosoft, surf, pyrobyte, nlabteam, atwinta, fichright, sibdev, kozhindev, purrweb, salesap¹ |
| Разработка корпоративных порталов (вкл. B2B, интранет) | 8 | bpadevelop, novacom, haulmont, surf, sibdev, simbirsoft, cetera, frog-studios |
| Разработка BI-систем | 7 | bpadevelop, surf, nlabteam, atwinta, fichright, sibdev, purrweb |
| Разработка личных кабинетов | 6 | novacom, longcatdev, surf, kozhindev, wnfx, cetera |
| Разработка WMS / автоматизация склада | 6 | bpadevelop, tektosoft, surf, sibdev, purrweb, viant (на 1С) |
| Разработка LMS / платформ онлайн-обучения | 6 | haulmont, surf, nlabteam, sibdev, is-art, purrweb |
| Разработка SaaS-платформ | 6 | bpadevelop, novacom, atwinta, fichright, kozhindev, sibdev |
| Системы документооборота (СЭД/ЭДО) | 4 | haulmont, sibdev, purrweb, viant (1С:ДО) |
| Автоматизация бизнес-процессов / RPA | 4 | tektosoft (АБП + RPA), sibdev, simbirsoft (внедрение RPA + RPA-разработка) |
| Разработка MES-систем | 2 | bpadevelop, sibdev |
| Нишевые корпоративные системы (по 1 конкуренту) | — | BPM, SRM, СУБД (bpadevelop); АИС, helpdesk, PM-системы, конфигураторы, админ-панели (novacom); АСУ (tektosoft); HRM (sibdev); POS (surf); PIM (cetera); системы интеллектуального планирования (haulmont) |

¹ у salesap.ru одна общая страница «Разработка CRM, ERP и нешаблонных корпоративных решений на заказ» + страницы внедрения S2 CRM.

### Веб-разработка

| Услуга | Конкурентов | Отдельная страница есть у |
|---|---|---|
| Разработка сайтов (вкл. корпоративные) | 15 | bpadevelop, longcatdev, surf, pyrobyte, atwinta, fichright, sibdev, purrweb, appfox, softmg, is-art, cetera, 10sec, frog-studios, simbirsoft |
| Разработка веб-приложений / веб-сервисов | 13 | bpadevelop, novacom, haulmont, surf, pyrobyte, nlabteam, atwinta, fichright, sibdev, kozhindev, purrweb, unitech, frog-studios |
| Разработка интернет-магазинов / e-commerce | 10 | bpadevelop, surf, atwinta, fichright, sibdev, purrweb, softmg, is-art, cetera, 10sec |
| Разработка MVP | 7 | bpadevelop, surf, pyrobyte, sibdev, purrweb, metalamp, smorodina |
| Разработка маркетплейсов | 6 | bpadevelop, surf, atwinta, sibdev, purrweb, cetera |
| Разработка для стартапов | 5 | pyrobyte, sibdev, purrweb, appfox, smorodina |
| Лендинги (Landing Page) | 4 | fichright, softmg, is-art, 10sec |
| Высоконагруженные системы (highload) | 4 | bpadevelop, novacom, sibdev, smorodina |
| Микросервисная разработка | 3 | novacom, surf, kozhindev |
| Frontend / Backend-разработка (отдельные страницы) | 3 | surf, nlabteam, simbirsoft |
| Разработка агрегаторов, досок объявлений, соцсетей, поисковых и почтовых сервисов | 1 | bpadevelop |
| Десктопные приложения | 1 | sibdev |

### Мобильная разработка (детализация)

| Услуга | Конкурентов | Отдельная страница есть у |
|---|---|---|
| iOS-разработка | 8 | surf, pyrobyte, atwinta, kozhindev, chillicode, appfox, softmg, smorodina |
| Android-разработка | 7 | pyrobyte, atwinta, kozhindev, chillicode, appfox, softmg, smorodina |
| Кроссплатформенная разработка (Flutter / React Native / KMP) | 6 | surf, pyrobyte, atwinta, purrweb, softmg, smorodina |

### Telegram, боты и мессенджеры

| Услуга | Конкурентов | Отдельная страница есть у |
|---|---|---|
| Разработка чат-ботов / Telegram-ботов | 12 | bpadevelop (5 страниц), novacom, tektosoft, sibdev, purrweb, softmg, wnfx, 10sec, magnetto, simplify-bots, cetera, frog-studios |
| Разработка Telegram Mini Apps | 11 | novacom, purrweb, appfox, 10sec, cetera, metalamp, smorodina, unitech, starlakedigital, simplify-bots, frog-studios |
| VK Mini Apps | 2 | appfox, smorodina |
| Голосовые боты | 2 | purrweb, cetera |
| Боты и приложения для мессенджера MAX | 2 | cetera, magnetto |

### Искусственный интеллект

| Услуга | Конкурентов | Отдельная страница есть у |
|---|---|---|
| ИИ/ML-разработка и внедрение | 14 | novacom, haulmont, surf, nlabteam, kozhindev, purrweb, simbirsoft, softmg, wnfx, koyutech, metalamp, cetera, frog-studios, appfox |
| ИИ-агенты | 2 | softmg, appfox (у wnfx — «ИИ и цифровые сотрудники») |
| Компьютерное зрение | 1 | sibdev |

### Web3, AR/VR, IoT, игры

| Услуга | Конкурентов | Отдельная страница есть у |
|---|---|---|
| AR/VR-разработка | 5 | tektosoft, surf, purrweb, appfox, smorodina |
| Web3 / блокчейн-разработка | 4 | surf, purrweb, appfox, metalamp (у metalamp 20+ страниц: dApps, смарт-контракты, DeFi, DEX, NFT, GameFi, TON/Solana/EVM) |
| IoT / embedded-разработка | 4 | novacom, surf, purrweb, sibdev |
| Приложения для Smart TV | 2 | surf, purrweb |
| Разработка игр (мобильные, ПК, браузерные, промо) | 1 | appfox (10+ страниц) |

### Аутстаффинг, аутсорсинг, команды

| Услуга | Конкурентов | Отдельная страница есть у |
|---|---|---|
| ИТ-аутстаффинг | 11 | haulmont, novacom, surf, atwinta, sibdev, purrweb, simbirsoft, appfox, softmg, wnfx, metalamp |
| ИТ-аутсорсинг разработки | 9 | haulmont, novacom, surf, sibdev, purrweb, simbirsoft, softmg, wnfx, metalamp |
| Выделенная команда / выделенный ИТ-центр | 3 | novacom, sibdev, simbirsoft |
| IT-рекрутинг | 1 | sibdev |

### Дизайн

| Услуга | Конкурентов | Отдельная страница есть у |
|---|---|---|
| UX/UI-дизайн (интерфейсы, приложения, сайты) | 16 | bpadevelop, pyrobyte, nlabteam, atwinta, fichright, surf, sibdev, kozhindev, purrweb, simbirsoft, softmg, appfox, wnfx, smorodina, metalamp, cetera |
| UX-аудит / юзабилити-аудит | 4 | surf, kozhindev, purrweb, simbirsoft |
| Брендинг, айдентика, логотипы | 2 | purrweb, appfox |

### Тестирование (QA)

| Услуга | Конкурентов | Отдельная страница есть у |
|---|---|---|
| Тестирование ПО / QA | 7 | surf, nlabteam, sibdev, purrweb, simbirsoft, softmg, smorodina |
| Нагрузочное тестирование | 2 | surf, purrweb |
| Пентест / информационная безопасность | 2 | purrweb, cetera |

### Поддержка и инфраструктура

| Услуга | Конкурентов | Отдельная страница есть у |
|---|---|---|
| Техподдержка и сопровождение (сайтов, приложений, по SLA) | 14 | bpadevelop, novacom, tektosoft, surf, atwinta, sibdev, purrweb, simbirsoft, appfox, softmg, is-art, koyutech, wnfx, cetera |
| DevOps-услуги | 5 | surf, purrweb, simbirsoft, softmg, sibdev (аутсорсинг DevOps) |
| Администрирование серверов / хостинг | 4 | novacom, softmg, tektosoft, cetera |

### Консалтинг, аудит, аналитика

| Услуга | Конкурентов | Отдельная страница есть у |
|---|---|---|
| Интеграции с внешними системами (1С, CRM, CMS, маркетплейсы, телефония) | 9 | haulmont, novacom, purrweb, sibdev, wnfx (8 страниц интеграций), softmg, cetera, viant, rarus |
| Модернизация legacy / миграции | 5 | novacom (9 страниц миграций), haulmont, simbirsoft, sibdev, is-art (перенос на другую CMS) |
| Разработка ТЗ и спецификаций | 5 | bpadevelop (4 страницы), atwinta, sibdev, purrweb, appfox |
| ИТ-консалтинг | 4 | surf, purrweb, simbirsoft, metalamp (web3) |
| Аудит кода | 4 | novacom, surf, purrweb, softmg |
| Аудит ИТ-инфраструктуры | 3 | surf, purrweb, simbirsoft |
| Бизнес- и системный анализ | 3 | simbirsoft, surf, softmg |
| Предпроектное обследование (Discovery, Sprint Zero, проектная карта) | 3 | simbirsoft, surf, bpadevelop |
| Спасение проектов (Project Rescue) | 2 | novacom, simbirsoft |
| Импортозамещение ПО | 1 | haulmont |

### Экосистема 1С

| Услуга | Конкурентов | Отдельная страница есть у |
|---|---|---|
| Внедрение / доработка / сопровождение 1С | 7 | viant (весь сайт, 35 страниц), rarus (весь каталог), cetera (11 страниц), simbirsoft, tektosoft, softmg (интеграция), wnfx (интеграция) |

### Маркетинг и продвижение

| Услуга | Конкурентов | Отдельная страница есть у |
|---|---|---|
| SEO-продвижение | 8 | bpadevelop, longcatdev, atwinta, fichright, appfox, softmg, is-art, cetera |
| Контекстная / таргетированная реклама | 5 | bpadevelop, atwinta, appfox, is-art, magnetto |
| SMM | 3 | atwinta, appfox, is-art |
| Продвижение в Telegram / Telegram Ads | 1 | magnetto (10+ страниц) |
| ASO-продвижение приложений | 1 | appfox |

### Отраслевые страницы-лендинги («разработка для <отрасли>»)

| Конкурент | Отраслевые страницы услуг |
|---|---|
| surf.ru | 13: банки/финтех (вкл. ДБО), ритейл, фудтех, рестораны, e-commerce, HR, здравоохранение/аптеки, производство, логистика, образование, недвижимость |
| is-art.ru | ~20 отраслевых сайтов: недвижимость, автозапчасти, строительство, юруслуги, автосервис, мебель, одежда, HoReCa, медицина и др. |
| haulmont.ru | 7: банки/финансы, транспорт/логистика, госорганы, производство, энергетика, нефтегаз/химия, образование |
| bpadevelop.ru | 6: EdTech, FoodTech, FinTech, HR-Tech, AdTech, ERP для производства |
| sibdev.pro | 5: FinTech, EdTech, HR-Tech, FoodTech, ПО для банков |
| kozhindev.com | 3: логистика/транспорт, фудтех, образование |
| longcatdev.com | 3: CRM для франшизы, логистики, недвижимости |
| остальные | tektosoft (транспорт/логистика, строительство), pyrobyte (фастфуд/доставка), purrweb (HealthTech, финансы), novacom (финтех, ПО для производства), nlabteam (медицина), wnfx (ритейл, доставка), rarus (розница, госсектор, отрасли 1С) |

---

## 2. Справка: чего нет на нашем сайте из частых услуг конкурентов

У BUDGET SOFT сейчас 16 страниц услуг (`uslugi/*`). Частые услуги конкурентов, под которые у нас **нет отдельной страницы**:

| Услуга конкурентов | Страниц у конкурентов | Наше покрытие |
|---|---|---|
| UX/UI-дизайн | 16 | нет |
| Разработка сайтов | 15 | нет |
| Техподдержка и сопровождение | 14 | нет |
| Веб-приложения / веб-сервисы | 13 | нет |
| Чат-боты / Telegram-боты | 12 | частично (страница Telegram Mini Apps) |
| Корпоративные порталы | 8 | нет |
| Разработка MVP | 7 | упоминается в текстах, страницы нет |
| Тестирование / QA | 7 | нет |
| Личные кабинеты | 6 | нет |
| LMS / онлайн-обучение | 6 | нет |
| WMS / автоматизация склада | 6 | частично (SCM-страница) |
| ИТ-аутсорсинг / выделенная команда | 9 / 3 | частично (только аутстаффинг) |
| Разработка ТЗ / предпроект | 5 | нет |
| Аудит кода / ИТ-аудит | 4 | нет |

Это справочный блок для планирования новых страниц; решение о создании — отдельная задача (новые URL добавляются в `urls.json`).

---

## 3. Детализация по конкурентам

### bpadevelop.ru — услуг с отдельными страницами: 63

*Направление:* разработка CRM и ERP на заказ

> BPA Develop (юрлицо ООО «Гонец», Москва) — заказная разработка ПО, прямой конкурент по CRM/ERP. Каталог большой: 63 отдельные страницы услуг; список приведён ПОЛНОСТЬЮ (порог >40 превышен, но каталог обозрим). Верхнеуровневые направления — первые 5 позиций списка (высоконагруженные системы, сервисы, e-commerce/сайты, дизайн, продвижение), остальное — их подуслуги. Источники: sitemap.xml (устарел, только 50 URL), выпадающее меню «Услуги» на главной и хаб /services/ (содержат больше страниц, чем sitemap). Особенности: 3 страницы услуг лежат в корне вне /services/ (razrabotka-srm-sistem, razrabotka-wms, razrabotka-mes-sistem); сайт имеет региональные поддомены (например omsk.bpadevelop.ru) с теми же страницами — в списке канонический домен bpadevelop.ru. Выборочно проверено 8 страниц (SaaS, SRM, WMS, AdTech, highload, design, develop-services, develop-ecommerce, prodvizhenie) — все живые полноценные лендинги услуг с ценами (типовые пакеты от 350 тыс. до 2,5 млн руб.). Страница /services/promotion/ имеет H1 «Акции», но описывает платную услугу «Проектная карта» (предпроектное обследование + ТЗ, от 10 000 руб.) — включена как консалтинг. Коробочных продуктов на сайте не обнаружено; QA, аутстаффинг, мобильная разработка и интеграция как отдельные страницы услуг отсутствуют (ТЗ для мобильного приложения есть, самой мобильной разработки нет). Документация/политика хостится на docs.ovva.tech — связь с брендом OVVA.

| Услуга | Категория | URL |
|---|---|---|
| Разработка высоконагруженных систем | разработка | https://bpadevelop.ru/services/develop-highload/ |
| Разработка сервисов (цифровые сервисы на заказ) | разработка | https://bpadevelop.ru/services/develop-services/ |
| Разработка E-commerce решений и сайтов | разработка | https://bpadevelop.ru/services/develop-ecommerce/ |
| Дизайн на заказ (ПО, CRM, ERP, сайты) | дизайн | https://bpadevelop.ru/services/design/ |
| Продвижение сайтов | прочее | https://bpadevelop.ru/services/prodvizhenie/ |
| Enterprise разработка | разработка | https://bpadevelop.ru/services/develop-enterprise/ |
| Разработка ПО | разработка | https://bpadevelop.ru/services/develop-soft/ |
| Разработка на заказ | разработка | https://bpadevelop.ru/services/develop-custom/ |
| Разработка под ключ | разработка | https://bpadevelop.ru/services/develop-turnkey/ |
| Разработка порталов | разработка | https://bpadevelop.ru/services/develop-portals/ |
| Разработка CRM | разработка | https://bpadevelop.ru/services/develop-crm/ |
| Разработка ERP | разработка | https://bpadevelop.ru/services/develop-erp/ |
| Разработка BPM | разработка | https://bpadevelop.ru/services/develop-bpm/ |
| Разработка BI | разработка | https://bpadevelop.ru/services/develop-bi/ |
| Разработка интранет-порталов | разработка | https://bpadevelop.ru/services/develop-intranet/ |
| Разработка корпоративных порталов | разработка | https://bpadevelop.ru/services/develop-corp-portals/ |
| Разработка B2B порталов | разработка | https://bpadevelop.ru/services/develop-b2b/ |
| Разработка B2C порталов | разработка | https://bpadevelop.ru/services/develop-b2c/ |
| Разработка СУБД | разработка | https://bpadevelop.ru/services/develop-subd/ |
| Разработка информационных систем | разработка | https://bpadevelop.ru/services/razrabotka-informacionnyh-sistem/ |
| Разработка SaaS | разработка | https://bpadevelop.ru/services/develop-saas/ |
| ERP для производства | отраслевая | https://bpadevelop.ru/services/erp-dlya-proizvodstva/ |
| Разработка MVP | разработка | https://bpadevelop.ru/services/develop-mvp/ |
| Разработка агрегаторов | разработка | https://bpadevelop.ru/services/develop-agregate/ |
| Разработка EdTech | отраслевая | https://bpadevelop.ru/services/develop-edtech/ |
| Разработка FoodTech | отраслевая | https://bpadevelop.ru/services/develop-foodtech/ |
| Разработка FinTech | отраслевая | https://bpadevelop.ru/services/develop-fintech/ |
| Разработка HR-Tech | отраслевая | https://bpadevelop.ru/services/develop-hrtech/ |
| Разработка AdTech платформ | отраслевая | https://bpadevelop.ru/services/razrabotka-adtech-platform/ |
| Разработка поисковых сервисов | разработка | https://bpadevelop.ru/services/razrabotka-poiskovyh-servisov/ |
| Разработка почтовых сервисов | разработка | https://bpadevelop.ru/services/razrabotka-pochtovogo-servisa/ |
| Разработка досок объявлений | разработка | https://bpadevelop.ru/services/razrabotka-doski-obyavleniy/ |
| Разработка сайтов-агрегаторов | разработка | https://bpadevelop.ru/services/razrabotka-saytov-agregatorov/ |
| Разработка социальных сетей | разработка | https://bpadevelop.ru/services/razrabotka-socialnyh-setey/ |
| Разработка SRM-систем | разработка | https://bpadevelop.ru/razrabotka-srm-sistem/ |
| Разработка WMS-систем | разработка | https://bpadevelop.ru/razrabotka-wms/ |
| Разработка MES-систем | разработка | https://bpadevelop.ru/razrabotka-mes-sistem/ |
| Разработка сайтов | разработка | https://bpadevelop.ru/services/develop-website/ |
| Разработка корпоративных сайтов | разработка | https://bpadevelop.ru/services/develop-corp-site/ |
| Разработка интернет-магазинов | разработка | https://bpadevelop.ru/services/develop-market/ |
| Разработка сайта-каталога | разработка | https://bpadevelop.ru/services/razrabotka-sajta-kataloga/ |
| Разработка маркетплейсов | разработка | https://bpadevelop.ru/services/develop-marketplace/ |
| Разработка продающего сайта | разработка | https://bpadevelop.ru/services/razrabotka-prodayuschego-sayta/ |
| Разработка промо-сайта | разработка | https://bpadevelop.ru/services/razrabotka-promo-saita/ |
| Разработка сайта услуг | разработка | https://bpadevelop.ru/services/razrabotka-saita-uslug/ |
| Разработка информационного сайта | разработка | https://bpadevelop.ru/services/razrabotka-informatsionnogo-saita/ |
| UX/UI дизайн | дизайн | https://bpadevelop.ru/services/design-site/ |
| Разработка дизайна ПО | дизайн | https://bpadevelop.ru/services/design-soft/ |
| Разработка дизайна CRM | дизайн | https://bpadevelop.ru/services/design-crm/ |
| Разработка дизайна ERP | дизайн | https://bpadevelop.ru/services/design-erp/ |
| Техническое задание для ИТ-проектов | консалтинг | https://bpadevelop.ru/services/develop-technical-task-for-it-projects/ |
| Техническое задание для мобильного приложения | консалтинг | https://bpadevelop.ru/services/develop-technical-task-for-mobile-app/ |
| Техническое задание для сайта | консалтинг | https://bpadevelop.ru/services/develop-technical-task-for-website/ |
| Техническое задание для CRM | консалтинг | https://bpadevelop.ru/services/tz-na-razrabotku-crm/ |
| Чат-боты для рассылки | разработка | https://bpadevelop.ru/services/chat-bot-rassylki/ |
| Чат-бот для клиентов | разработка | https://bpadevelop.ru/services/chat-bot-dlya-klientov/ |
| Чат-бот для бизнеса | разработка | https://bpadevelop.ru/services/chat-bot-dlya-biznesa/ |
| Чат-бот для сайта | разработка | https://bpadevelop.ru/services/chat-bot-dlya-sajta/ |
| Чат-бот для Telegram | разработка | https://bpadevelop.ru/services/chat-bot-telegram/ |
| Поддержка | поддержка | https://bpadevelop.ru/services/support/ |
| SEO продвижение | прочее | https://bpadevelop.ru/services/seo-prodvizhenie-sajtov/ |
| Контекстная реклама | прочее | https://bpadevelop.ru/services/kontekstnaya-reklama/ |
| Проектная карта (предпроектный аудит, BPMN, прототип, ТЗ) | консалтинг | https://bpadevelop.ru/services/promotion/ |

### novacom.ru — услуг с отдельными страницами: 61

*Направление:* разработка CRM и ERP на заказ

> Сайт доступен, серверный рендеринг, полный sitemap.xml. Источники: sitemap, меню «Услуги», хаб /services, футер. Выборочно проверены живые страницы: /services/saas-development (H1 «Разработка SaaS-платформы на заказ под ключ»), /services/crm-development/business-solutions (H1 «Разработка CRM-системы на заказ под ключ»), /services/iot-audit (H1 «Экспресс-аудит IoT-идеи»), /services/software-development/it-companies-russia — все реальные страницы услуг, не 404. Каталог >40 позиций, список сокращён до 61 верхнеуровневой услуги: НЕ включены ~40 отраслевых под-лендингов вида /services/{crm,erp,portal,personal-cabinet,app,software}-development/dlya-* (для мебельного бизнеса, производства, логистики, медицины, e-commerce, строительства, ресторанов, фитнеса, образования, страховых, банков, торговли, туризма, доставки, пищевого производства, машиностроения, оптовой торговли, интернет-магазинов) и 8 гео-лендингов (/moskva, /spb) тех же услуг. Позиционирование: backend-разработка Java/Kotlin/Python, highload, финтех — прямой конкурент BUDGET SOFT по CRM/ERP на заказ (включая отраслевые CRM/ERP-лендинги, которых у BUDGET SOFT нет). Коробочных продуктов не обнаружено; на сайте есть устаревшая база знаний Cisco (/tech_support) — наследие старого бизнеса компании, не услуга.

| Услуга | Категория | URL |
|---|---|---|
| Заказная разработка ПО | разработка | https://novacom.ru/services/software-development/custom-po |
| Разработка CRM-систем | разработка | https://novacom.ru/services/crm-development/business-solutions |
| Разработка ERP-систем | разработка | https://novacom.ru/services/erp-development/enterprise-solutions |
| Highload-разработка (Java) | разработка | https://novacom.ru/services/java-development/web-mobile-solutions |
| Kotlin-разработка | разработка | https://novacom.ru/services/kotlin-development/backend-mobile |
| Spring-разработка | разработка | https://novacom.ru/services/spring-development |
| Python backend-разработка | разработка | https://novacom.ru/services/python-backend-development |
| Микросервисы на Python | разработка | https://novacom.ru/services/python-microservices |
| ML/DS-разработка на Python | разработка | https://novacom.ru/services/python-ml-development |
| Автоматизация на Python | разработка | https://novacom.ru/services/python-automation |
| AI и машинное обучение | разработка | https://novacom.ru/services/ai-development |
| AI-анализ ТЗ и распознавание спецификаций | разработка | https://novacom.ru/services/ai-spec-recognition/specification-analysis |
| Event-driven & streaming (веб-сервисы и цифровые платформы) | разработка | https://novacom.ru/services/web-services-development/digital-platforms |
| Финтех-разработка и платёжные системы | разработка | https://novacom.ru/services/fintech-development/payment-systems |
| Разработка SaaS-платформ | разработка | https://novacom.ru/services/saas-development |
| Разработка веб- и мобильных приложений | разработка | https://novacom.ru/services/app-development/web-mobile-apps |
| Разработка бизнес-приложений | разработка | https://novacom.ru/services/business-app-development/corporate-solutions |
| Разработка корпоративных порталов (B2B) | разработка | https://novacom.ru/services/portal-development/corporate-b2b |
| Разработка личных кабинетов | разработка | https://novacom.ru/services/personal-cabinet-development/client-portal |
| Разработка информационных систем | разработка | https://novacom.ru/services/information-systems/automation-solutions |
| Разработка АИС | разработка | https://novacom.ru/services/ais-development |
| Разработка админ-панелей и дашбордов | разработка | https://novacom.ru/services/admin-panel-development |
| Разработка конфигураторов | разработка | https://novacom.ru/services/configurator-development |
| Low-code бэкенд | разработка | https://novacom.ru/services/low-code-development |
| IoT и embedded-разработка | разработка | https://novacom.ru/services/iot-embedded-development |
| Telegram Mini Apps | разработка | https://novacom.ru/services/telegram-development/mini-apps |
| Разработка Telegram-ботов | разработка | https://novacom.ru/services/telegram-bot-development |
| Разработка систем управления проектами (PM-системы) | разработка | https://novacom.ru/services/project-management-development |
| Разработка helpdesk-систем | разработка | https://novacom.ru/services/helpdesk-development |
| Realtime-разработка | разработка | https://novacom.ru/services/realtime-development |
| ETL-разработка | разработка | https://novacom.ru/services/etl-development |
| Разработка API Gateway | разработка | https://novacom.ru/services/api-gateway-development |
| Next.js-разработка | разработка | https://novacom.ru/services/nextjs-development |
| NestJS-разработка | разработка | https://novacom.ru/services/nestjs-development |
| Компания по разработке ПО в России (SEO-лендинг заказной разработки) | разработка | https://novacom.ru/services/software-development/it-companies-russia |
| Рефакторинг legacy-кода | разработка | https://novacom.ru/services/legacy-refactoring |
| Миграция монолита на микросервисы | разработка | https://novacom.ru/services/monolith-to-microservices |
| Миграция с Firebase | разработка | https://novacom.ru/services/firebase-migration |
| Миграция с PHP на Node.js | разработка | https://novacom.ru/services/php-to-nodejs |
| Миграция с Битрикс на React | разработка | https://novacom.ru/services/bitrix-to-react |
| Миграция с Angular на React | разработка | https://novacom.ru/services/angular-to-react |
| Миграция с Django на FastAPI | разработка | https://novacom.ru/services/django-to-fastapi |
| Миграция с Oracle на PostgreSQL | разработка | https://novacom.ru/services/oracle-migration |
| Миграция на Python | разработка | https://novacom.ru/services/migration-to-python |
| Интеграция с маркетплейсами | интеграция | https://novacom.ru/services/marketplace-integration |
| Аутстаффинг Senior Java-разработчиков | аутстаффинг | https://novacom.ru/services/it-outstaffing/java-developers |
| Аутстаффинг Python-разработчиков | аутстаффинг | https://novacom.ru/services/it-outstaffing/python-developers |
| Выделенная команда разработки (IT-аутсорсинг) | аутстаффинг | https://novacom.ru/services/it-outsourcing/software-development |
| IT-аутсорсинг (администрирование инфраструктуры) | поддержка | https://novacom.ru/services/it-outsourcing-admin |
| Аутсорсинг системного администрирования | поддержка | https://novacom.ru/services/sysadmin-outsourcing |
| Поддержка проектов (ежемесячное сопровождение) | поддержка | https://novacom.ru/services/project-support/monthly-maintenance |
| Поддержка сайтов | поддержка | https://novacom.ru/services/website-support |
| Техническая поддержка сайтов | поддержка | https://novacom.ru/services/website-technical-support |
| Дежурный SRE (on-call) | поддержка | https://novacom.ru/services/sre-on-call |
| Performance-аудит (аудит производительности) | консалтинг | https://novacom.ru/services/performance-audit/optimization |
| Backend Health-Check | консалтинг | https://novacom.ru/services/backend-health-check |
| Аудит кода | консалтинг | https://novacom.ru/services/code-audit |
| Экспресс-аудит IoT-идеи | консалтинг | https://novacom.ru/services/iot-audit |
| Спасение проектов (Project Rescue) | консалтинг | https://novacom.ru/services/project-rescue |
| Разработка дизайн-систем | дизайн | https://novacom.ru/services/design-system-development |
| ПО для производства | отраслевая | https://novacom.ru/services/manufacturing-software |

### clientbase.ru — услуг с отдельными страницами: 4

*Направление:* разработка CRM (платформа «Клиентская база»)

> clientbase.ru — сайт продукта, а не сервисной компании: это SaaS/коробочная CRM-платформа «Клиентская база» (аренда аккаунта /buy/account_rental/, лицензии /buy/buy_new_licence/, маркетплейс готовых отраслевых конфигураций /marketplace/, модули 1С и DaData, дополнения/опции) — это коробочные продукты, в список услуг не включены. Отдельных страниц заказных услуг мало (4): пара связанных страниц «CRM на заказ» (/config/pers/ — маркетинговая, /config/personal_config/ — детальная с бюджетами и этапами), обучение и помощь в выборе. Проверено выборочно: все 4 URL живые, с собственным контентом. Sitemap.xml содержит 704 URL, но это в основном фичи продукта (/about/features/*), справка (/help/*), новости и тарифы. Отраслевых сервисных лендингов нет — отрасли представлены только готовыми конфигурациями в маркетплейсе и новостными статьями (news/crm_dlya_*), их не включал. /express/ («Экспресс-внедрение» в навигации) фактически ведёт на общий продуктовый лендинг без описания услуги внедрения — не включён; /buy/bid_for_config_support — только форма заявки без описания услуги; /config/projects/* — портфолио внедрённых конфигураций. Техподдержка описана как фича продукта и раздел справки, отдельной коммерческой страницы услуги поддержки нет.

| Услуга | Категория | URL |
|---|---|---|
| Персональная конфигурация CRM (настройка системы под бизнес: создание таблиц, настройка, интеграции, консультации) | внедрение | https://clientbase.ru/config/pers/ |
| CRM на заказ (разработка персональной конфигурации, бюджеты от 25 000 до 500 000+ руб., 11 этапов проекта) | разработка | https://clientbase.ru/config/personal_config/ |
| Школа Клиентской базы (обучение пользователей, администраторов и разработчиков, сертификация) | прочее | https://clientbase.ru/help/cb_school/ |
| Помощь в выборе / сборка CRM под бизнес (подбор и платная настройка функционала, от 1 500 руб.) | консалтинг | https://clientbase.ru/buy/podbor_crm/ |

### longcatdev.com — услуг с отдельными страницами: 10

*Направление:* разработка CRM и ERP

> Компания ООО «Лонг Кэт» (Москва/Саранск), позиционируется как «разработчик CRM №1 в России по количеству работ»; профиль — заказная разработка CRM/ERP/веб-сервисов на Laravel, цены от 700 тыс. руб. за CRM, ставка 1500-2500 руб/час. Сайт на конструкторе (Tilda-подобный), sitemap.xml доступен (~108 URL, большинство — портфолио и блог). Проверено выборочно 10+ страниц — все живые, не редиректы. Коробочные продукты компании (исключены из списка услуг): «HRM для управления персоналом» (/hrm, лицензия 100 тыс. руб.), «CRM Лиды» (/crm_leads, 59 тыс. руб.), «CRM для школ и учебных центров» (/uchebnyj_centr, облако + установка 200 тыс. руб.), CRMBaza.ru (упоминается на странице недвижимости), коробка «Лонг Кэт: Логистика» (200 тыс. руб., упоминается на /logistics наряду с заказной разработкой). Страницы /crm_dlya_malogo_biznesa и /crm_dlya_stroitelnoy_kompanii — SEO-статьи-гайды по выбору CRM с CTA на разработку, не отдельные страницы услуг — не включены. В sitemap есть мусорные/тестовые URL (/testtest, /hrmold, /logistics_old, /logisticstest, /page14780626.html и т.п.). Отдельных страниц аутстаффинга, QA, дизайна, поддержки и мобильной разработки на сайте нет.

| Услуга | Категория | URL |
|---|---|---|
| Разработка корпоративных решений | разработка | https://longcatdev.com/razrabotka-korporativnyh-resheniy |
| Разработка CRM-системы на заказ | разработка | https://longcatdev.com/razrabotka-crm |
| Разработка ERP | разработка | https://longcatdev.com/razrabotka-erp |
| Разработка веб-сервисов на Laravel | разработка | https://longcatdev.com/laravel |
| Разработка личных кабинетов | разработка | https://longcatdev.com/lk |
| Создание сложных сайтов на Laravel | разработка | https://longcatdev.com/sozdanie-sajtov |
| Продвижение сайтов (SEO) | прочее | https://longcatdev.com/prodvizhenie-sajta |
| Разработка CRM для франшизы | отраслевая | https://longcatdev.com/razrabotka-crm-franshizam |
| CRM для логистических компаний (заказная разработка) | отраслевая | https://longcatdev.com/logistics |
| CRM для агентства недвижимости (заказная разработка) | отраслевая | https://longcatdev.com/crm_dlya_agentstva_nedvijimosti |

### www.haulmont.ru — услуг с отдельными страницами: 24

*Направление:* разработка CRM и ERP (топ-1 Яндекса)

> Источник — sitemap.xml (канонический домен www.haulmont.ru) + меню главной; выборочно проверены живьём 8 страниц (CRM, аутсорсинг, интеграция, замена ERP, интеллектуальное планирование, тиражируемое ПО, импортозамещение, custom-development) — все живые отдельные страницы с собственными H1. Страница /custom-development/ («Разработка программного обеспечения на заказ») — одновременно флагманская услуга и хаб, из которого линкуются остальные услуги разработки. Отраслевые страницы (7 шт.) — полноценные лендинги «разработка ПО для отрасли», включены с category «отраслевая»; их H1 не проверялись пословно, названия даны по пунктам меню. ВНИМАНИЕ: URL услуги LMS в sitemap указан как /razrabotka-sistem-upravleniya-obucheniem-lms/ (в выдаче sitemap-парсера), в списке выше он приведён — если 404, проверить вариант written в sitemap: https://www.haulmont.ru/razrabotka-sistem-upravleniya-obucheniem-lms/. Не включены страницы коробочных продуктов компании: Jmix, Amplicode, xDbStream, OpenBPM, OpenIDE, ТЕЗИС (СЭД), Параплан (CRM для детских центров), Printera (управление печатью), а также /tehnologii/ (стек технологий), /projects/ (кейсы), /partners/, /company/, /blog/. Услуг QA/дизайна/техподдержки как отдельных страниц на сайте нет — Haulmont позиционируется через заказную разработку корпоративных систем и собственные платформы.

| Услуга | Категория | URL |
|---|---|---|
| Разработка программного обеспечения на заказ | разработка | https://www.haulmont.ru/custom-development/ |
| Разработка уникального программного обеспечения | разработка | https://www.haulmont.ru/razrabotka-unikalnogo-programmnogo-obespecheniya/ |
| Заказная разработка тиражируемого ПО | разработка | https://www.haulmont.ru/razrabotka-tirazhiruemykh-reshenij/ |
| Разработка ERP-систем на заказ | разработка | https://www.haulmont.ru/razrabotka-erp-sistem-na-zakaz/ |
| Замена ERP-систем без остановки бизнес-процессов | внедрение | https://www.haulmont.ru/zamena-erp-sistem/ |
| Разработка CRM-систем на заказ | разработка | https://www.haulmont.ru/razrabotka-crm-sistem/ |
| Разработка корпоративных порталов | разработка | https://www.haulmont.ru/razrabotka-korporativnyh-portalov/ |
| Разработка веб-приложений | разработка | https://www.haulmont.ru/razrabotka-web-prilozheniy/ |
| Разработка мобильных приложений | разработка | https://www.haulmont.ru/razrabotka-mobilnyh-prilozheniy/ |
| Разработка систем документооборота | разработка | https://www.haulmont.ru/razrabotka-sistem-dokumentooborota/ |
| Разработка систем интеллектуального планирования на заказ | разработка | https://www.haulmont.ru/razrabotka-sistem-intellektualnogo-planirovaniya-na-zakaz/ |
| Разработка систем искусственного интеллекта | разработка | https://www.haulmont.ru/razrabotka-sistem-iskusstvennogo-intellekta/ |
| Разработка систем управления обучением (LMS) | разработка | https://www.haulmont.ru/razrabotka-sistem-upravleniem-obucheniem-lms/ |
| Модернизация устаревшего программного обеспечения | разработка | https://www.haulmont.ru/modernizacziya-ustarevshego-programmnogo-obespecheniya/ |
| Импортозамещение: замена программного обеспечения на российское | внедрение | https://www.haulmont.ru/importozameshchenie/ |
| Услуги по интеграции программного обеспечения | интеграция | https://www.haulmont.ru/integraciya-programmnogo-obespecheniya/ |
| Аутсорсинг и аутстаффинг разработки ПО | аутстаффинг | https://www.haulmont.ru/autsorsing-razrabotki/ |
| Программное обеспечение для банков и финансов | отраслевая | https://www.haulmont.ru/programmnoe-obespechenie-banka/ |
| Программное обеспечение для транспорта и логистики | отраслевая | https://www.haulmont.ru/programmnoe-obespechenie-logistiki/ |
| Программное обеспечение для государственных органов | отраслевая | https://www.haulmont.ru/programmnoe-obespechenie-gosudarstvennyh-organov/ |
| Программное обеспечение для производства | отраслевая | https://www.haulmont.ru/programmnoe-obespechenie-proizvodstva/ |
| Программное обеспечение для энергетики | отраслевая | https://www.haulmont.ru/programmnoe-obespechenie-energetiki/ |
| ПО для нефтегазовой и химической промышленности | отраслевая | https://www.haulmont.ru/po-dlya-neftegazovoj-i-khimicheskoj-promyshlennosti/ |
| Образовательное программное обеспечение (для образования и науки) | отраслевая | https://www.haulmont.ru/obrazovatelnoe-programmnoe-obespechenie/ |

### tektosoft.ru — услуг с отдельными страницами: 16

*Направление:* разработка CRM и ERP

> Источники: sitemap-индекс https://tektosoft.ru/sitemap.xml (page-sitemap.xml + portfolio-sitemap.xml), меню/футер главной, хаб услуг /services/. Выборочно проверены живыми: /services/crm/ (H1 «Разработка CRM-систем на заказ»), /services/automation/, /services/logistics/, /services/ar/, /support/, /services/software-inexpensive/, /wildberries/ — все отдают полноценные страницы. Пункт меню «Недорогое ПО» (/services/software-inexpensive/) отдаёт тот же контент с H1 «Автоматизация бизнес-процессов», что и /services/automation/, и отсутствует в sitemap — похоже на дубликат/редирект, в список не включён отдельно. Пункт меню «Техподдержка» ведёт на /support-tektosoft/, но в sitemap живая страница /support/ — включён именно он. Коробочный продукт компании (не услуга, в список не включён): «Разграничение прав доступа сборщика в ЛК Wildberries» — https://tektosoft.ru/wildberries/ (SaaS-решение, 14 дней бесплатно). Отраслевые страницы logistics и construction содержат описание услуги разработки (цены, этапы, кейсы), поэтому включены с категорией «отраслевая». Портфолио (portfolio-sitemap.xml, /our-portfolio/), «О компании», контакты и политика конфиденциальности исключены по условиям задачи.

| Услуга | Категория | URL |
|---|---|---|
| Разработка CRM-систем на заказ | разработка | https://tektosoft.ru/services/crm/ |
| Разработка ERP-систем | разработка | https://tektosoft.ru/services/erp/ |
| Разработка АСУ (автоматизированных систем управления) | разработка | https://tektosoft.ru/services/asu/ |
| Разработка WMS-систем | разработка | https://tektosoft.ru/services/wms/ |
| Разработка программного обеспечения | разработка | https://tektosoft.ru/services/software/ |
| Разработка мобильных приложений | разработка | https://tektosoft.ru/services/mobile/ |
| Автоматизация бизнес-процессов | разработка | https://tektosoft.ru/services/automation/ |
| Автоматизация 1С | внедрение | https://tektosoft.ru/services/1c/ |
| Чат-боты для бизнеса | разработка | https://tektosoft.ru/services/chat-bot/ |
| Разработка RPA (роботизация процессов) | разработка | https://tektosoft.ru/services/rpa/ |
| Автоматизация Google-таблиц | разработка | https://tektosoft.ru/services/google-table/ |
| Разработка проектов дополненной реальности (AR) | разработка | https://tektosoft.ru/services/ar/ |
| Техническая поддержка (администрирование серверов, мониторинг 24/7) | поддержка | https://tektosoft.ru/support/ |
| Подбор оборудования и аренда серверов | прочее | https://tektosoft.ru/services/servers/ |
| Разработка систем автоматизации транспорта и логистики (CRM, ERP, TMS) | отраслевая | https://tektosoft.ru/services/logistics/ |
| ПО для строительных компаний | отраслевая | https://tektosoft.ru/services/construction/ |

### surf.ru — услуг с отдельными страницами: 72

*Направление:* разработка CRM, мобильная разработка

> Сайт доступен, sitemap.xml отдаётся полностью (300+ URL). Хаб услуг — https://surf.ru/it-razrabotka/ («IT-разработка продукта под ключ»); меню «Услуги» и хаб подтверждают структуру. Выборочно проверено 8 URL: страницы услуг живые (CRM, Flutter, IT-аутстаффинг, тестирование, DevOps, веб-разработка — полноценные лендинги с CTA/ценами/кейсами/FAQ). СПИСОК СОКРАЩЁН: каталог >40 позиций — в sitemap десятки узких SEO-лендингов, не включённых в список: ~40 фудтех-лендингов (приложение для ресторана/кофейни/пиццерии/пекарни/суши-бара/кейтеринга/официантов, CRM/LMS/AI/computer vision для ресторана, интеграция с iiko и агрегаторами, суперапп для ресторанной сети и т.п.), лендинги «приложение как Яндекс.Лавка/Delivery Club/Samokat», дубли-варианты основных услуг (razrabotka-mobilnyh-prilozhenij-pod-kljuch, razrabotka-mobilnyh-prilozhenij-na-zakaz, sozdanie-korporativnogo-portala, audit-programmnogo-koda vs code-audit-for-apps), а также подстраницы web-razrabotka (информационный портал, сложные сайты, сайт для ресторана/доставки). Значительная часть sitemap — блог-статьи с «услуго-подобными» URL: проверка показала, что, например, /razrabotka-prilozhenij-android/ — блог-гайд, а не лендинг услуги (исключён); /razrabotka-erp-sistem/ — лонгрид-лендинг с ценами и CTA (включён). Отдельная Android-страница услуги в меню хаба ссылается на /razrabotka-prilozhenij-dlya-android-cena-i-sroki/ (не проверена). Коробочных продуктов не обнаружено; SurfGen (внутренняя библиотека кодогенерации) фигурирует только в кейсах. Специализация конкурента: мобильная разработка (Flutter — флагман), фудтех, финтех/банкинг, ритейл; enterprise-сегмент.

| Услуга | Категория | URL |
|---|---|---|
| Мобильная разработка | разработка | https://surf.ru/mobilnaya-razrabotka/ |
| Разработка мобильных приложений под ключ | разработка | https://surf.ru/mobilnoe-prilozhenie-pod-kluch/ |
| Flutter-разработка | разработка | https://surf.ru/flutter-razrabotka/ |
| iOS-разработка мобильных приложений | разработка | https://surf.ru/ios-razrabotka-mobilnyh-prilozhenij/ |
| Кроссплатформенная мобильная разработка | разработка | https://surf.ru/krossplatformennaja-mobilnaja-razrabotka/ |
| Разработка на Kotlin Multiplatform | разработка | https://surf.ru/kotlin-multiplatform/ |
| Веб-разработка (веб-приложения и сервисы на заказ) | разработка | https://surf.ru/web-razrabotka/ |
| Разработка сайта под ключ | разработка | https://surf.ru/web-razrabotka/razrabotka-sajta-pod-klyuch/ |
| Разработка корпоративного сайта | разработка | https://surf.ru/web-razrabotka/razrabotka-korporativnogo-sajta/ |
| Разработка B2B-портала | разработка | https://surf.ru/web-razrabotka/b2b-portal-development/ |
| Разработка BI-системы | разработка | https://surf.ru/web-razrabotka/razrabotka-bi-sistemy/ |
| Разработка личного кабинета | разработка | https://surf.ru/web-razrabotka/razrabotka-lichnogo-kabineta/ |
| Backend-разработка | разработка | https://surf.ru/backend/ |
| Frontend-разработка | разработка | https://surf.ru/frontend/ |
| PWA-разработка | разработка | https://surf.ru/pwa/ |
| Разработка CRM-системы на заказ | разработка | https://surf.ru/razrabotka-crm-sistemy/ |
| Разработка ERP-систем | разработка | https://surf.ru/razrabotka-erp-sistem/ |
| Разработка корпоративного портала | разработка | https://surf.ru/razrabotka-korporativnogo-portala/ |
| Разработка маркетплейсов | разработка | https://surf.ru/razrabotka-marketplejsov/ |
| Разработка MVP | разработка | https://surf.ru/razrabotka-mvp/ |
| Разработка API | разработка | https://surf.ru/razrabotka-api/ |
| Разработка микросервисов | разработка | https://surf.ru/razrabotka-mikroservisov/ |
| Разработка LMS | разработка | https://surf.ru/razrabotka-lms/ |
| Разработка WMS | разработка | https://surf.ru/razrabotka-wms/ |
| Разработка POS-систем | разработка | https://surf.ru/razrabotka-pos-sistem/ |
| Комплексная разработка сервисов | разработка | https://surf.ru/services-dev/ |
| AI-ускоренная разработка (AI boosted development) | разработка | https://surf.ru/services/ai-boosted-dev/ |
| Machine Learning / ML-разработка | разработка | https://surf.ru/machine-learning/ |
| Разработка AR-приложений | разработка | https://surf.ru/razrabotka-ar-prilozhenij/ |
| Разработка VR-приложений | разработка | https://surf.ru/razrabotka-vr-prilozhenij/ |
| Разработка IoT-приложений | разработка | https://surf.ru/razrabotka-iot-prilozhenij/ |
| Разработка приложений Smart TV | разработка | https://surf.ru/razrabotka-prilozhenij-smart-tv/ |
| Разработка WebRTC-приложений | разработка | https://surf.ru/razrabotka-prilozhenij-webrtc/ |
| Разработка блокчейн-приложений | разработка | https://surf.ru/razrabotka-blokchejn-prilozhenij/ |
| Разработка ПО для встраиваемых систем | разработка | https://surf.ru/razrabotka-po-dlya-vstraivaemyh-sistem/ |
| Проектирование продукта | консалтинг | https://surf.ru/product-development/ |
| Дизайн UI/UX приложений | дизайн | https://surf.ru/app-design/ |
| UX/UI-дизайн | дизайн | https://surf.ru/ux-ui-dizajn/ |
| Аудит UX/UI-дизайна и AppMetrica | дизайн | https://surf.ru/ui-ux-audit-dizaina/ |
| Аудит кода приложений | консалтинг | https://surf.ru/code-audit-for-apps/ |
| Аудит программного кода | консалтинг | https://surf.ru/audit-programmnogo-koda/ |
| Аудит ИТ-инфраструктуры | консалтинг | https://surf.ru/audit-it-infrastruktury/ |
| QA-аудит (качество приложения и процессов тестирования) | QA | https://surf.ru/qa-audit-ot-kachestva-prilozheniya-do-effektivnosti-processov-testirovaniya/ |
| Тестирование мобильных и веб-приложений | QA | https://surf.ru/testing/ |
| Нагрузочное тестирование | QA | https://surf.ru/uslugi-nagruzochnogo-testirovaniya/ |
| Автотестирование с помощью AI | QA | https://surf.ru/ai-auto-test/ |
| Услуги DevOps | прочее | https://surf.ru/uslugi-devops/ |
| Сопровождение и поддержка в рамках SLA | поддержка | https://surf.ru/soprovozhdenie-v-ramkah-sla/ |
| ИТ-аутстаффинг специалистов | аутстаффинг | https://surf.ru/it-autstaffing/ |
| ИТ-аутсорсинг | аутстаффинг | https://surf.ru/it-outsourcing/ |
| Системные аналитики (предоставление специалистов) | аутстаффинг | https://surf.ru/sistemnye-analitiki/ |
| ИТ-консалтинг | консалтинг | https://surf.ru/it-consulting/ |
| AI-консалтинг | консалтинг | https://surf.ru/ai-consulting/ |
| Бизнес-анализ в мобильной разработке | консалтинг | https://surf.ru/biznes-analiz-v-mobilnoj-razrabotke/ |
| Продуктовая аналитика | консалтинг | https://surf.ru/produktovaya-analitika-sobiraem-i-analiziruem-dannye/ |
| Sprint Zero (быстрый запуск проекта) | консалтинг | https://surf.ru/sprint-zero/ |
| CJM-воркшоп | консалтинг | https://surf.ru/cjm-workshop/ |
| Управление проектами | консалтинг | https://surf.ru/upravlenie-proektami/ |
| Разработка для банков и финтеха | отраслевая | https://surf.ru/banks/ |
| Разработка ДБО для банков | отраслевая | https://surf.ru/dbo-dlya-bankov/ |
| Маскировка банковских приложений (ДБО для сторов) | отраслевая | https://surf.ru/dbo_for_stores/ |
| Разработка для ритейла | отраслевая | https://surf.ru/retail/ |
| Разработка для фудтеха | отраслевая | https://surf.ru/food/ |
| Автоматизация ресторанного бизнеса | отраслевая | https://surf.ru/food-automation/ |
| E-commerce приложения | отраслевая | https://surf.ru/e-commerce-apps/ |
| E-commerce сайты и сервисы | отраслевая | https://surf.ru/e-commerce-services/ |
| HR-приложения (приложения для сотрудников) | отраслевая | https://surf.ru/hr-apps/ |
| Разработка ПО для здравоохранения и аптек | отраслевая | https://surf.ru/healthcare-software-development/ |
| Разработка приложений для производства | отраслевая | https://surf.ru/app-development-for-manufacturing/ |
| Разработка приложений для логистики | отраслевая | https://surf.ru/razrabotka-prilozhenij-dlya-logistiki/ |
| Разработка приложений для образования | отраслевая | https://surf.ru/razrabotka-prilozhenij-dlya-obrazovaniya/ |
| Разработка приложений для недвижимости | отраслевая | https://surf.ru/razrabotka-prilozhenij-dlya-nedvizhimosti/ |

### salesap.ru — услуг с отдельными страницами: 3

*Направление:* заказная разработка CRM/ERP (вендор S2)

> salesap.ru — сайт вендора коробочной CRM/ERP-системы S2 (бывш. SalesapCRM). Услуг с отдельными страницами всего три — ровно пункты меню «Услуги»: заказная разработка CRM/ERP, внедрение «под ключ» и пакетное внедрение за 7 дней; все три проверены как живые страницы. Страница /paketnoe-vnedrenie-crm отсутствует в sitemap.xml, но активно линкуется с сайта. Остальной сайт — страницы коробочного продукта: ~20 функциональных страниц /produkty/* (CRM для продаж, финансов, документооборота, телефонии, ERP для управления предприятием и т.д.) и ~19 отраслевых лендингов продукта /reshenija/* («CRM для юристов», «CRM для клиники» и т.п.) — это лендинги SaaS-продукта, а не заказные услуги, поэтому в список не включены. Отдельных страниц аудита, поддержки, миграции, обучения, аутстаффинга нет (обучение и поддержка входят в состав внедрения, справка — /help). Конкурентное пересечение с BUDGET SOFT — прежде всего страница заказной разработки CRM/ERP.

| Услуга | Категория | URL |
|---|---|---|
| Разработка CRM, ERP и нешаблонных корпоративных решений на заказ | разработка | https://salesap.ru/razrabotka-crm-erp-na-zakaz |
| Внедрение S2 CRM «под ключ» (с гарантией) | внедрение | https://salesap.ru/uslugi-integracii-s2 |
| Пакетное внедрение CRM за 7 дней | внедрение | https://salesap.ru/paketnoe-vnedrenie-crm |

### pyrobyte.ru — услуг с отдельными страницами: 12

*Направление:* разработка ERP

> Список собран из sitemap (https://pyrobyte.ru/page-sitemap.xml), меню «Услуги» на главной и хабовой страницы /services — все три источника полностью совпадают: ровно 12 страниц услуг под /services/. Выборочно проверены /services/erp, /services/krossplatformennaya-razrabotka и /services/foodtech — живые отдельные страницы с собственными H1. Профиль компании: мобильная и веб-разработка с акцентом на MVP/стартапы; по ERP предлагают и заказную разработку (от 3,5 млн руб.), и внедрение 1С:ERP (от 5 млн руб.). Коробочный продукт: MØDUL — «приложение на модулях», конструктор мобильных приложений на отдельном поддомене modul.pyrobyte.ru (в список услуг не включён). Отдельных страниц QA, поддержки, аутстаффинга или интеграций на сайте нет. Кейсы (/cases, case-sitemap) и блог (/pyroblog, post-sitemap) исключены.

| Услуга | Категория | URL |
|---|---|---|
| Разработка и внедрение ERP | разработка | https://pyrobyte.ru/services/erp |
| Разработка MVP под ключ | разработка | https://pyrobyte.ru/services/mvp |
| Разработка для стартапов | разработка | https://pyrobyte.ru/services/startapy |
| Сайты и веб-сервисы | разработка | https://pyrobyte.ru/services/web |
| Корпоративные решения | разработка | https://pyrobyte.ru/services/korporativnye-resheniya-dlya-biznesa |
| Разработка для бизнеса | разработка | https://pyrobyte.ru/services/razrabotka-dlya-biznesa |
| Кроссплатформенная разработка | разработка | https://pyrobyte.ru/services/krossplatformennaya-razrabotka |
| Разработка для Android | разработка | https://pyrobyte.ru/services/android |
| Разработка для iOS | разработка | https://pyrobyte.ru/services/ios |
| Дизайн сайтов | дизайн | https://pyrobyte.ru/services/dizayn-saytov |
| Дизайн мобильных приложений | дизайн | https://pyrobyte.ru/services/dizayn-mobilnyh-prilozheniy |
| Разработка для ресторанов быстрого питания и доставки еды | отраслевая | https://pyrobyte.ru/services/foodtech |

### nlabteam.com — услуг с отдельными страницами: 13

*Направление:* разработка ERP

> Сайт на WordPress; HTML и sitemap_index.xml не отдаются напрямую в WebFetch (пустой контент, вероятно антибот), список собран через текстовый прокси r.jina.ai (страницы /services/ и главная) и подтверждён WebSearch (site:nlabteam.com). Меню «Услуги» содержит 12 пунктов, 13-я страница corporate-apps найдена в плитках хаба услуг и главной. Выборочно проверены как живые: razrabotka-erp-sistem, development, corporate-apps. Конкурент по ERP: у страницы ERP два формата — создание с нуля и внедрение модуля в существующую систему. Аутстаффинга, техподдержки и DevOps как отдельных страниц не обнаружено. Коробочные продукты (не включены): раздел /solutions/ — ИИ чат-боты для бизнеса, LLM-анализ документов on-premise, SpeechXplore (речевая аналитика), SmatCubes (BI для банкинга/прогноз оттока), PyEncrypt (защита Python-кода), а также ИИ-платформа aiplatform.nlabteam.com (/products/ai-platform/).

| Услуга | Категория | URL |
|---|---|---|
| Разработка полного цикла (заказная разработка ПО) | разработка | https://nlabteam.com/services/development/ |
| Разработка ERP-систем | разработка | https://nlabteam.com/services/razrabotka-erp-sistem/ |
| Разработка веб-приложений | разработка | https://nlabteam.com/services/web-development/ |
| Разработка мобильных приложений (iOS/Android) | разработка | https://nlabteam.com/services/mobilnaya-razrabotka-ios-android/ |
| Разработка корпоративных приложений | разработка | https://nlabteam.com/services/corporate-apps/ |
| Машинное обучение (создание ML-моделей) | разработка | https://nlabteam.com/services/machine-learning/ |
| Разработка BI-систем на Yandex DataLens | разработка | https://nlabteam.com/services/data-analytics-bi-datalens/ |
| Разработка платформ онлайн-обучения (LMS на заказ) | разработка | https://nlabteam.com/services/razrabotka-lms-na-zakaz/ |
| Frontend-разработка | разработка | https://nlabteam.com/services/frontend/ |
| Backend-разработка | разработка | https://nlabteam.com/services/backend/ |
| UX/UI дизайн | дизайн | https://nlabteam.com/services/ui-ux-design/ |
| QA и тестирование ПО | QA | https://nlabteam.com/services/qa/ |
| Разработка ПО для медицины | отраслевая | https://nlabteam.com/services/it-resheniya-medicina/ |

### atwinta.ru — услуг с отдельными страницами: 33

*Направление:* разработка ERP

> Atwinta — digital-агентство (Кемерово/Москва) полного цикла: аналитика, дизайн, разработка, продвижение, поддержка, аутстафф. Список сокращён: полный каталог в sitemap >130 URL. Не включены пофакторные лендинги: ~35 страниц типов и отраслей сайтов под /services/razrabotka/razrabotka-saytov/ (лендинг, промо-сайт, корпоративный сайт, сайт-каталог, сайт-визитка, агрегатор, личный кабинет, сложные/адаптивные/информационные/3D-сайты + отрасли: медицина, недвижимость, образование, стоматология, отели, автосалоны, стройка, госучреждения и др.), ~50 страниц «SEO для <товарной ниши>» под /services/prodvizhenie/seo/ (мебель, одежда, автозапчасти и т.п.) и отраслевые страницы мобильной разработки (медицина, e-commerce, доставка еды, такси, библиотека) под /services/razrabotka/razrabotka-mobilnyh-prilozheniy/. Ключевое по ERP-контексту: страница ERP заявляет цену от 5 000 000 ₽ и срок от 6 месяцев; аутстафф — 1700–2400 ₽/час; техподдержка — пакеты от 7900 ₽/мес. Собственные продукты/решения на поддоменах (не включены в услуги): «Платформы для обучения» (education.atwinta.ru), «Фабрика улучшений» (digital-factory.atwinta.ru), «Конструктор планировок» (plan.atwinta.ru). Проверено выборочно: страницы ERP, аутстаффа и техподдержки живые, с уникальным контентом (не 404/редирект). Источники: sitemap-main-pages.xml, меню и футер главной, хаб /services/.

| Услуга | Категория | URL |
|---|---|---|
| Разработка | разработка | https://atwinta.ru/services/razrabotka/ |
| Разработка корпоративного ПО | разработка | https://atwinta.ru/services/razrabotka/razrabotka-korporativnogo-po/ |
| Создание и разработка ERP-систем на заказ | разработка | https://atwinta.ru/services/razrabotka/razrabotka-korporativnogo-po/erp/ |
| Разработка BI-систем | разработка | https://atwinta.ru/services/razrabotka/razrabotka-korporativnogo-po/bi/ |
| Разработка SaaS | разработка | https://atwinta.ru/services/razrabotka/razrabotka-korporativnogo-po/saas/ |
| Разработка веб-сервисов | разработка | https://atwinta.ru/services/razrabotka/razrabotka-veb-servisov/ |
| Разработка облачных сервисов | разработка | https://atwinta.ru/services/razrabotka/razrabotka-veb-servisov/cloud/ |
| Разработка сайтов | разработка | https://atwinta.ru/services/razrabotka/razrabotka-saytov/ |
| Разработка интернет-магазина | разработка | https://atwinta.ru/services/razrabotka/razrabotka-saytov/razrabotka-internet-magazina/ |
| Разработка маркетплейса | разработка | https://atwinta.ru/services/razrabotka/razrabotka-saytov/marketplace/ |
| Разработка мобильных приложений | разработка | https://atwinta.ru/services/razrabotka/razrabotka-mobilnyh-prilozheniy/ |
| Разработка приложений для Android | разработка | https://atwinta.ru/services/razrabotka/razrabotka-mobilnyh-prilozheniy/android/ |
| Разработка приложений для iOS | разработка | https://atwinta.ru/services/razrabotka/razrabotka-mobilnyh-prilozheniy/ios/ |
| Кроссплатформенная разработка приложений | разработка | https://atwinta.ru/services/razrabotka/razrabotka-mobilnyh-prilozheniy/cross-platform/ |
| Разработка приложений на Flutter | разработка | https://atwinta.ru/services/razrabotka/razrabotka-mobilnyh-prilozheniy/flutter/ |
| Разработка технических заданий и прототипов | консалтинг | https://atwinta.ru/services/razrabotka/teh-zadaniya-i-prototipy/ |
| Аналитика | консалтинг | https://atwinta.ru/services/analitika/ |
| Аутстафф | аутстаффинг | https://atwinta.ru/services/autstaff/ |
| Техническая поддержка сайтов, сервисов и мобильных приложений | поддержка | https://atwinta.ru/services/tehnicheskaya-podderzhka/ |
| Дизайн | дизайн | https://atwinta.ru/services/dizayn/ |
| Дизайн сайтов | дизайн | https://atwinta.ru/services/dizayn/dizayn-saytov/ |
| Дизайн интерфейсов | дизайн | https://atwinta.ru/services/dizayn/dizayn-interfeysov/ |
| Дизайн мобильных приложений | дизайн | https://atwinta.ru/services/dizayn/dizayn-mobilnyh-prilozheniy/ |
| Дизайн дашбордов | дизайн | https://atwinta.ru/services/dizayn/dizayn-dashbordov/ |
| Дизайн промышленного оборудования | дизайн | https://atwinta.ru/services/dizayn/dizayn-promyshlennogo-oborudovaniya/ |
| 3D-дизайн | дизайн | https://atwinta.ru/services/dizayn/3d-dizayn/ |
| Продвижение | прочее | https://atwinta.ru/services/prodvizhenie/ |
| SEO-продвижение | прочее | https://atwinta.ru/services/prodvizhenie/seo/ |
| GEO (продвижение в генеративной выдаче) | прочее | https://atwinta.ru/services/prodvizhenie/geo/ |
| SMM | прочее | https://atwinta.ru/services/prodvizhenie/smm/ |
| Таргетированная реклама | прочее | https://atwinta.ru/services/prodvizhenie/targetirovannaya-reklama/ |
| Контекстная реклама | прочее | https://atwinta.ru/services/prodvizhenie/kontekstnaya-reklama/ |
| Комплексное продвижение | прочее | https://atwinta.ru/services/prodvizhenie/kompleksnoe-prodvizhenie/ |

### fichright.ru — услуг с отдельными страницами: 12

*Направление:* разработка ERP

> Fichright — студия разработки сайтов и веб-приложений (Москва). Сайт отдаётся нормально, sitemap.xml полный (21 URL), список услуг собран из sitemap и сверен с меню «Услуги» и хабом /services/. Выборочно проверены /services/erp-system/ (H1 «Разработка ERP-систем» — прямой конкурент по ERP: кастомная разработка и внедрение, отраслевые решения, модели Retainer/T&M/Fixed), /services/web-application/ и /services/site-development/ — все живые полноценные страницы. Услуги сгруппированы в 4 направления: разработка сайтов, веб-приложения, дизайн, продвижение; хабы направлений «Разработка сайтов» и «Веб-приложения» сами являются полноценными продающими страницами услуг и включены в список. UX/UI и «Дизайн» ведут на одну страницу /services/design/; SEO и контекстная реклама — на одну /services/promotion/. Коробочных продуктов у компании нет. Мобильной разработки, аутстаффинга, QA и ИИ-услуг с отдельными страницами не обнаружено.

| Услуга | Категория | URL |
|---|---|---|
| Разработка ERP-систем | разработка | https://fichright.ru/services/erp-system/ |
| Разработка CRM-систем | разработка | https://fichright.ru/services/crm-system/ |
| Разработка BI-систем | разработка | https://fichright.ru/services/bi-system/ |
| Разработка SaaS | разработка | https://fichright.ru/services/saas-development/ |
| Разработка веб-приложений и сервисов | разработка | https://fichright.ru/services/web-application/ |
| Разработка сайтов под ключ | разработка | https://fichright.ru/services/site-development/ |
| Корпоративный сайт | разработка | https://fichright.ru/services/corporate/ |
| Интернет-магазин | разработка | https://fichright.ru/services/online-store/ |
| Landing Page | разработка | https://fichright.ru/services/landing/ |
| Доработка сайтов | поддержка | https://fichright.ru/services/finish-guide-site/ |
| Дизайн (UX/UI) | дизайн | https://fichright.ru/services/design/ |
| Продвижение (SEO и контекстная реклама) | прочее | https://fichright.ru/services/promotion/ |

### viant.ru — услуг с отдельными страницами: 35

*Направление:* разработка ERP (на базе 1С)

> Компания ВИАНТ (viant.ru) — 1С-интегратор: внедрение/сопровождение 1С (в т.ч. 1С:ERP), автоматизация складов (ТСД, штрихкодирование, адресное хранение, WMS-процессы), маркировка «Честный ЗНАК», RFID, учет имущества. Это НЕ заказная разработка ПО в широком смысле — весь стек услуг вокруг платформы 1С; прямой конкурент BUDGET SOFT только по ERP на базе 1С. Список собран из sitemap.xml, меню и хаба /services/; выборочно проверены 6+ страниц — все живые отдельные лендинги услуг. Хабовые страницы направлений не включены в services: /services/ (все услуги), /uslugi_po_1c/ (услуги по 1С), /uslugi-po-erp/ (услуги по 1С ERP), /uslugi_chestni_znak/ (услуги по маркировке), /avtomatizatsiya-skladov/ (проверено: хаб-каталог из 6 под-услуг без собственного контента). Собственные продукты компании (не включены): «АРМ.Логист» (/arm_logist/), «Виант: Контроль имущества» (/catalog/uchet-os-imush/viant-kontrol-imushchestva/), «Виант: Станция агрегации» (/stancziya-agregaczii/), а также 8 готовых «Решений для работы с ТСД» (/resheniyapotsd/ — мобильная упаковка, мобильная печать, массовый сбор заказов для маркетплейсов, KPI склада, фото с ТСД и т.п.). Кроме услуг на сайте большой интернет-магазин оборудования (/catalog/ — ТСД, сканеры, принтеры этикеток, RFID-метки, роботы-уборщики) — это товары, не услуги.

| Услуга | Категория | URL |
|---|---|---|
| Внедрение 1С | внедрение | https://viant.ru/vnedrenie-1c/ |
| Доработка 1С | разработка | https://viant.ru/dorabotka-1c/ |
| Техническая поддержка 1С | поддержка | https://viant.ru/tekhnicheskaya-podderzhka-1c/ |
| Внедрение 1С:Комплексная автоматизация | внедрение | https://viant.ru/vnedrenie-1s-kompleksnaya-avtomatizacziya/ |
| Внедрение 1С:Управление торговлей | внедрение | https://viant.ru/vnedrenie-1c-upravlenie-torgovlej/ |
| Внедрение 1С:ЗУП | внедрение | https://viant.ru/vnedrenie-1s-zup/ |
| Интеграция 1С и CMS Битрикс | интеграция | https://viant.ru/1c-bitrix/ |
| Внедрение 1С:Аналитика | внедрение | https://viant.ru/vnedrenie-1c-analitika/ |
| Внедрение и настройка 1С:Альфа-Авто (автобизнес) | отраслевая | https://viant.ru/vnedrenie-1c-alfa-avto/ |
| Интеграция 1С | интеграция | https://viant.ru/integracziya-1c/ |
| Внедрение и настройка 1С:ERP | внедрение | https://viant.ru/vnedrenie-1s-erp/ |
| Сопровождение 1С:ERP | поддержка | https://viant.ru/soprovozhdenie-1s-erp/ |
| Интеграция 1С:ERP | интеграция | https://viant.ru/integracziya-1s-erp/ |
| Настройка 1С:ERP | внедрение | https://viant.ru/nastrojka-1s-erp/ |
| Переход с 1С:КА на 1С:ERP | внедрение | https://viant.ru/perekhod-s-1s-ka-na-1s-erp/ |
| Переход с 1С:УПП на 1С:ERP | внедрение | https://viant.ru/perekhod-s-1s-upp-na-1s-erp/ |
| Бюджетирование в 1С | внедрение | https://viant.ru/budjetirovanie_v_1C/ |
| Автоматизация склада на базе 1С | внедрение | https://viant.ru/avtomatizacziya-sklada-na-baze-1s/ |
| Внедрение ТСД (терминалов сбора данных) | внедрение | https://viant.ru/vnedrenie-tsd/ |
| Внедрение штрихкодирования в 1С | внедрение | https://viant.ru/vnedrenie-shtrikhkodirovaniya-1c/ |
| Техническая поддержка Клеверенс | поддержка | https://viant.ru/tekhnicheskaya-podderzhka-kleverens/ |
| Адресное хранение на складе в 1С | внедрение | https://viant.ru/adresnoe_hraneni/ |
| Автоматизация отгрузки на складе с помощью ТСД (1С) | внедрение | https://viant.ru/otgruzka-na-sklade-s-pomoschyu-tsd-1c/ |
| Приемка товаров на склад с помощью ТСД (интеграция с 1С) | внедрение | https://viant.ru/priemka-tovara-na-sklade-v-1c-s-pomoschyu-tsd/ |
| Внедрение маркировки Честный ЗНАК в 1С | внедрение | https://viant.ru/vnedrenie_chestni_znak_v_1C/ |
| Внедрение маркировки Честный ЗНАК на производстве (промышленная маркировка) | внедрение | https://viant.ru/chestnii_znak_na_proizvodstve/ |
| Управленческий учет имущества в 1С | внедрение | https://viant.ru/uhchet-imushestva/ |
| Учет специального имущества | внедрение | https://viant.ru/uchet-speczialnogo-imushhestva/ |
| Учет имущества в 1С:БГУ (госучреждения) | отраслевая | https://viant.ru/uchet-imushhestva-v-1s-bgu/ |
| Учет оргтехники в 1С | внедрение | https://viant.ru/uchet-orgtekhniki-1c/ |
| Внедрение 1С:Документооборот | внедрение | https://viant.ru/vnedrenie-1sdokumentooborot/ |
| Бесшовная интеграция 1С:Документооборот | интеграция | https://viant.ru/besshovnaya-integraciya-1sdokumentooborot/ |
| Настройка и доработка 1С:Документооборот | разработка | https://viant.ru/nastrojka-i-dorabotka-1sdokumentooborot/ |
| Внедрение RFID-систем | внедрение | https://viant.ru/vnedrenie-rfid/ |
| Бесшовный Wi-Fi (проектирование и монтаж на складе) | прочее | https://viant.ru/besshovnyj-wifi/ |

### sibdev.pro — услуг с отдельными страницами: 45

*Направление:* разработка ERP

> Sibdev (ООО «ГКМ-СМАРТ», Красноярск) — сайт на WordPress, полностью доступен. Каталог услуг ОГРОМНЫЙ: в service-sitemap.xml более 500 URL отдельных страниц услуг, поэтому список сокращён до ~45 верхнеуровневых направлений (по правилу «каталог >40 позиций»). Полная структура: (1) Разработка ПО — SaaS, стартапы, MVP, highload, плюс отдельные страницы под каждый тип корпоративной системы (CRM, ERP, BI, HRM, LMS, MES, CMS, TMS, MDM, WMS, ГИС, CDP, АРМ, ЭДО, интранет/B2B-порталы) и под крипто/Web3 (криптокошельки, криптообменники, DEX-биржи, NFT-маркетплейсы, DeFi); (2) Сайты — ~60 отраслевых лендингов «сайт для <ниши>» (отели, стоматологии, автосервисы…) и ~20 страниц «сайт на <CMS/фреймворке>» (Bitrix, Tilda, Django, Laravel…); (3) Интернет-магазины — ~14 нишевых страниц (одежда, мебель, автозапчасти…); (4) Мобильные приложения — iOS, Android, кроссплатформ, ~40 отраслевых страниц «приложение для <ниши>» плюс AR/VR, блокчейн; (5) Чат-боты — отдельные страницы под Telegram, WhatsApp, VK, Viber, Instagram; (6) Поддержка/доработка — отдельные страницы под каждую CMS (WordPress, Bitrix, Joomla, Tilda, MODX, Drupal, NetCat, OpenCart, Laravel); (7) Дизайн — интерфейсы, редизайн, прототипы, айдентика, брендбуки, логотипы; (8) Аутсорс/аутстафф — ~25+16 страниц по технологиям (React, Vue, Python, PHP, Java, Go…); (9) IT-рекрутинг — ~110 страниц по ролям и ~70 гео-страниц по городам РФ; (10) Электроника — ~27 страниц (печатные платы, датчики, ПЛИС, АСУ ТП, IoT, обратная разработка, импортозамещение электроники). Ключевая для контекста страница «Разработка ERP-систем» (https://sibdev.pro/erp) проверена: живая, с процессом из 6 этапов и моделями Fixed Price / Time & Materials; выборочно проверены также /outstaffing (ставка от 1800 руб/час) и /maintenance — обе живые. Цены вынесены в скачиваемый xlsx-прайс. Коробочных продуктов не обнаружено; practice.sibdev.pro — учебная практика для студентов, не услуга.

| Услуга | Категория | URL |
|---|---|---|
| Разработка веб-сервисов (SaaS) | разработка | https://sibdev.pro/saas |
| Разработка стартапов | разработка | https://sibdev.pro/startup |
| Разработка MVP | разработка | https://sibdev.pro/mvp |
| Высоконагруженные сервисы | разработка | https://sibdev.pro/highload |
| Разработка веб-приложений | разработка | https://sibdev.pro/web-app |
| Разработка веб-сайтов | разработка | https://sibdev.pro/site |
| Разработка интернет-магазинов | разработка | https://sibdev.pro/online-store |
| E-commerce разработка | разработка | https://sibdev.pro/ecommerce |
| Разработка маркетплейсов | разработка | https://sibdev.pro/marketplace |
| Разработка мобильных приложений | разработка | https://sibdev.pro/mobile |
| Enterprise-разработка (корпоративные системы) | разработка | https://sibdev.pro/enterprise |
| Разработка CRM-систем | разработка | https://sibdev.pro/crm |
| Разработка ERP-систем | разработка | https://sibdev.pro/erp |
| Разработка BI-систем | разработка | https://sibdev.pro/bi |
| Разработка WMS-систем | разработка | https://sibdev.pro/wms |
| Разработка HRM-систем | разработка | https://sibdev.pro/hrm |
| Разработка LMS-систем | разработка | https://sibdev.pro/lms |
| Разработка MES-систем | разработка | https://sibdev.pro/mes |
| Системы автоматизации бизнес-процессов | разработка | https://sibdev.pro/business-automation |
| Разработка систем ЭДО (ECM) | разработка | https://sibdev.pro/ecm |
| Разработка корпоративных порталов | разработка | https://sibdev.pro/corporate-portal |
| Разработка B2B-порталов | разработка | https://sibdev.pro/b2b-portal |
| Разработка чат-ботов | разработка | https://sibdev.pro/chat-bot |
| Разработка десктопных приложений | разработка | https://sibdev.pro/desktop-app |
| Компьютерное зрение | разработка | https://sibdev.pro/computer-vision |
| Электронная разработка (hardware, IoT) | разработка | https://sibdev.pro/electronics |
| Интеграции | интеграция | https://sibdev.pro/integration |
| Перенос сайтов на другую CMS | интеграция | https://sibdev.pro/cms-transfer |
| Сопровождение сайтов и приложений | поддержка | https://sibdev.pro/maintenance |
| Доработка сайтов | поддержка | https://sibdev.pro/upgrade-site |
| Поддержка приложений | поддержка | https://sibdev.pro/maintenance-app |
| Дизайн | дизайн | https://sibdev.pro/design |
| Дизайн интерфейсов (UI/UX) | дизайн | https://sibdev.pro/interface |
| Аутсорсинг разработки | аутстаффинг | https://sibdev.pro/outsourcing |
| Аутстаффинг разработчиков | аутстаффинг | https://sibdev.pro/outstaffing |
| Выделенная команда | аутстаффинг | https://sibdev.pro/dedicated-team |
| Аутсорсинг DevOps-инженеров | аутстаффинг | https://sibdev.pro/outsourcing-devops |
| IT-рекрутинг | прочее | https://sibdev.pro/recruiting |
| Тестирование ПО (аутсорсинг QA) | QA | https://sibdev.pro/outsourcing-qa |
| Разработка спецификаций и ТЗ | консалтинг | https://sibdev.pro/specification |
| Разработка для FinTech | отраслевая | https://sibdev.pro/fintech |
| Разработка для EdTech | отраслевая | https://sibdev.pro/edtech |
| Разработка для HR-Tech | отраслевая | https://sibdev.pro/hrtech |
| Разработка для FoodTech | отраслевая | https://sibdev.pro/foodtech |
| Разработка ПО для банков | отраслевая | https://sibdev.pro/bank-software |

### kozhindev.com — услуг с отдельными страницами: 17

*Направление:* разработка ERP

> Источники: sitemap.xml (77 URL), меню главной страницы и хаб /services. Ключевой конкурентный профиль: заказная разработка веб/мобильных приложений, ERP/CRM, SaaS, ML; выделенные страницы дизайна (дизайн, аудит, исследования) и 3 отраслевых лендинга (логистика, фудтех, образование). Выборочная проверка: razrabotka-erp-sistem (H1 «Разработка ERP систем», 9 лет опыта, сроки от 2 мес.), design-audit (H1 «UX/UI-аудит») и logistics — живые отдельные страницы. Sitemap частично устарел: /services/erp-crm отдаёт 404 (заменён отдельными страницами ERP и CRM, которых в sitemap нет — они найдены через меню и хаб /services). Дополнительно в sitemap ~25 геолендингов тех же услуг по городам (razrabotka-veb-prilozhenij-*, razrabotka-mobilnyh-prilozhenij-*, razrabotka-crm/erp-sistem-<город>, yuzabiliti-audit-sajta-*) — в список не включены как дубли услуг по географии. В разделе ML упомянуты демо «Компьютерное зрение» и «Конструктор языковой модели» — без отдельных страниц; коробочных продуктов не обнаружено. Аутстаффинга, QA как отдельной услуги и техподдержки с отдельными страницами нет.

| Услуга | Категория | URL |
|---|---|---|
| Разработка онлайн-сервисов | разработка | https://kozhindev.com/services/online-services |
| Разработка веб-приложений | разработка | https://kozhindev.com/services/web-services |
| Разработка мобильных приложений | разработка | https://kozhindev.com/services/mobile |
| Разработка iOS-приложений | разработка | https://kozhindev.com/services/razrabotka-dlya-ios |
| Разработка Android-приложений | разработка | https://kozhindev.com/services/razrabotka-dlya-android |
| Разработка ERP-систем | разработка | https://kozhindev.com/services/razrabotka-erp-sistem |
| Разработка CRM-систем | разработка | https://kozhindev.com/services/razrabotka-crm-sistem |
| Разработка SaaS-сервисов | разработка | https://kozhindev.com/services/saas-services |
| Микросервисная разработка | разработка | https://kozhindev.com/services/microservices |
| Разработка личных кабинетов | разработка | https://kozhindev.com/services/personal-area |
| Машинное обучение (ML-разработка) | разработка | https://kozhindev.com/services/ml-development |
| UX/UI дизайн | дизайн | https://kozhindev.com/services/design |
| UX/UI-аудит (юзабилити-аудит) | дизайн | https://kozhindev.com/services/design-audit |
| Дизайн-исследования | дизайн | https://kozhindev.com/services/design-research |
| Разработка приложений для логистики и транспорта | отраслевая | https://kozhindev.com/services/logistics |
| Разработка фудтех-решений | отраслевая | https://kozhindev.com/services/food-tech |
| Разработка ПО для образования | отраслевая | https://kozhindev.com/services/education |

### terralink.ru — недоступен

*Направление:* разработка ERP

> Сайт не отдаётся (DNS timeout) и 05.07, и 06.07.2026 — разобрать невозможно.

### chillicode.agency — услуг с отдельными страницами: 4

*Направление:* разработка ERP, мобильная разработка

> Сайт — компактный сайт агентства мобильной разработки (Москва/СПб, 25 человек, 350+ проектов, 11–13 лет на рынке). Sitemap отсутствует (/sitemap.xml и /sitemap_index.xml — 404, в robots.txt нет директивы Sitemap), поэтому URL собраны из меню главной и поиска site:. Отдельных страниц услуг всего 4 — все по мобильной разработке; каждая проверена: живая, со своим H1, не редирект. Хабовой страницы услуг (/uslugi, /services) нет. Хотя на главной заявлено «создаем сайты, веб-сервисы и мобильные приложения», отдельных страниц веб-разработки нет. ERP, CRM, финтех и отраслевые темы представлены только статьями блога (/blog/razrabotka-erp и т.п.) — по условию не включены; несмотря на позиционирование конкурента «по ERP», страницы услуги ERP у него нет. /flutter — 404. Коробочных продуктов не обнаружено. В футере есть ссылка на смежный домен chillicode.dev (в рамках задачи не разбирался).

| Услуга | Категория | URL |
|---|---|---|
| Разработка мобильных приложений для iOS | разработка | https://chillicode.agency/razrabotka-mobilnyh-prilozheniy-ios |
| Разработка мобильных приложений для Android | разработка | https://chillicode.agency/razrabotka-mobilnyh-prilozheniy-android |
| Разработка приложений на Swift | разработка | https://chillicode.agency/swift |
| Разработка Android-приложений на Kotlin | разработка | https://chillicode.agency/kotlin |

### purrweb.com — услуг с отдельными страницами: 51

*Направление:* мобильная разработка

> Русская версия живёт на purrweb.com/ru/ (домен purrweb.ru отдаёт 301-редирект на purrweb.com/ru/). Полный реестр русских страниц услуг — сайтмап https://www.purrweb.com/sitemap-ru-uslugi.xml: всего ~100 отдельных страниц услуг, поэтому список сокращён до верхнеуровневых услуг/направлений (все из главного меню «Услуги»). За кадром остались подстраницы: технологии/фреймворки (React Native, Flutter, Electron.js, PWA, WebRTC, Webflow, Tilda, игры на React Native), типы сайтов (лендинги, корпоративные, сложные сайты, сайты аукционов), типы веб-порталов (B2B-портал, корпоративный портал, личный кабинет, информационный и интернет-портал, тендерная площадка, встраиваемые системы), дизайн-подуслуги (логотип, брендбук, гайдлайн, фирменный стиль, прототип, проектирование мобильных приложений), ~18 подстраниц healthtech-направления (МИС, ЛИС, CRM для медицины, ИИ в медицине, ВКС/телемедицина, IoMT, автоматизация клиники, медицинский SaaS и др.) и отраслевые лендинги (логистика, туризм, недвижимость, мероприятия, медиа, спорт, образование, POS-системы, интеллектуальное ценообразование). Живость страниц выборочно проверена: mobilnaya-razrabotka (H1 «Разработка мобильных приложений на заказ»), ui-ux-dizajn (H1 «UX/UI дизайн»), healthtech-хаб — все отвечают контентом, с ценами и формами. Коробочных продуктов на сайте не обнаружено; /ru/avangard/ и /ru/purrweb-healthtech-issledovanie/ — промо/исследование, не услуги. Английская версия услуг (sitemap_services.xml) не включалась — по заданию использована русская.

| Услуга | Категория | URL |
|---|---|---|
| Разработка мобильных приложений (iOS и Android) | разработка | https://www.purrweb.com/ru/uslugi/mobilnaya-razrabotka/ |
| Веб-разработка (веб-приложения) | разработка | https://www.purrweb.com/ru/uslugi/veb-razrabotka/ |
| Разработка веб-сервисов | разработка | https://www.purrweb.com/ru/uslugi/razrabotka-web-servisov/ |
| Разработка ПО на заказ | разработка | https://www.purrweb.com/ru/uslugi/razrabotka-po-na-zakaz/ |
| Разработка MVP | разработка | https://www.purrweb.com/ru/uslugi/mvp/ |
| Разработка сайтов | разработка | https://www.purrweb.com/ru/uslugi/razrabotka-sajta/ |
| Разработка маркетплейсов | разработка | https://www.purrweb.com/ru/uslugi/razrabotka-marketplejsov/ |
| Разработка интернет-магазинов (e-commerce) | разработка | https://www.purrweb.com/ru/uslugi/ecommerce/ |
| Кросс-платформенная разработка приложений | разработка | https://www.purrweb.com/ru/uslugi/crossplatform/ |
| Разработка приложений для стартапов | разработка | https://www.purrweb.com/ru/uslugi/razrabotka-dlya-startapov/ |
| AI-разработка (интеграция AI-инструментов) | разработка | https://www.purrweb.com/ru/uslugi/razrabotka-ai/ |
| ML-разработка (машинное обучение) | разработка | https://www.purrweb.com/ru/uslugi/mashinnoe-obuchenie/ |
| Разработка чат-ботов | разработка | https://www.purrweb.com/ru/uslugi/razrabotka-chat-botov/ |
| Разработка голосовых ботов | разработка | https://www.purrweb.com/ru/uslugi/razrabotka-golosovyh-botov/ |
| Разработка Telegram Mini Apps | разработка | https://www.purrweb.com/ru/uslugi/razrabotka-telegram-mini-app/ |
| Разработка ERP-систем | разработка | https://www.purrweb.com/ru/uslugi/razrabotka-erp-sistem/ |
| Разработка CRM-систем | разработка | https://www.purrweb.com/ru/uslugi/razrabotka-crm-sistem/ |
| Автоматизация склада (WMS) | разработка | https://www.purrweb.com/ru/uslugi/avtomatizatsiya-sklada-wms/ |
| Разработка LMS | разработка | https://www.purrweb.com/ru/uslugi/razrabotka-lms/ |
| Разработка BI-систем (Business Intelligence) | разработка | https://www.purrweb.com/ru/uslugi/business-intelligence/ |
| Разработка систем электронного документооборота (ЭДО) | разработка | https://www.purrweb.com/ru/uslugi/razrabotka-sistem-ehlektronnogo-dokumentooborota/ |
| Web3-разработка | разработка | https://www.purrweb.com/ru/uslugi/web3-razrabotka/ |
| Разработка IoT-решений | разработка | https://www.purrweb.com/ru/uslugi/iot/ |
| VR-разработка | разработка | https://www.purrweb.com/ru/uslugi/vr-razrabotka/ |
| AR-разработка | разработка | https://www.purrweb.com/ru/uslugi/ar-razrabotka/ |
| Разработка приложений для Smart TV | разработка | https://www.purrweb.com/ru/uslugi/razrabotka-prilozhenij-dlya-tv/ |
| Доработка сайта | разработка | https://www.purrweb.com/ru/uslugi/dorabotka-sayta/ |
| Интеграция с внешними системами | интеграция | https://www.purrweb.com/ru/uslugi/integratsiya-s-vneshnimi-sistemami/ |
| UI/UX дизайн | дизайн | https://www.purrweb.com/ru/uslugi/ui-ux-dizajn/ |
| Дизайн мобильных приложений | дизайн | https://www.purrweb.com/ru/uslugi/dizajn-mobilnyh-prilozhenij/ |
| Веб-дизайн | дизайн | https://www.purrweb.com/ru/uslugi/veb-dizajn/ |
| Редизайн сайтов | дизайн | https://www.purrweb.com/ru/uslugi/redizajn-saitov/ |
| UX/UI-аудит | дизайн | https://www.purrweb.com/ru/uslugi/ux-audit/ |
| Брендинг | дизайн | https://www.purrweb.com/ru/uslugi/branding/ |
| Графический дизайн | дизайн | https://www.purrweb.com/ru/uslugi/graficheskiy-dizayn/ |
| Моушн-дизайн | дизайн | https://www.purrweb.com/ru/uslugi/motion-design/ |
| Нагрузочное тестирование | QA | https://www.purrweb.com/ru/uslugi/nagruzochnoye-testirovaniye/ |
| Тестирование производительности | QA | https://www.purrweb.com/ru/uslugi/testirovaniye-proizvoditelnosti/ |
| Регрессионное тестирование | QA | https://www.purrweb.com/ru/uslugi/regressionnoe-testirovanie/ |
| Пентест (тестирование на проникновение) | QA | https://www.purrweb.com/ru/uslugi/pentest/ |
| Аутсорсинг разработки | аутстаффинг | https://www.purrweb.com/ru/uslugi/outsourcing/ |
| Аутстаффинг | аутстаффинг | https://www.purrweb.com/ru/uslugi/outstaffing/ |
| Техподдержка мобильных приложений | поддержка | https://www.purrweb.com/ru/uslugi/tehpodderzhka-mobilnyh-prilozhenij/ |
| DevOps-услуги | поддержка | https://www.purrweb.com/ru/uslugi/devops-services/ |
| IT-консалтинг | консалтинг | https://www.purrweb.com/ru/uslugi/it-consulting/ |
| Аудит IT-инфраструктуры | консалтинг | https://www.purrweb.com/ru/uslugi/audit-it-infrastruktury/ |
| Аудит кода (анализ исходного кода) | консалтинг | https://www.purrweb.com/ru/uslugi/audit-koda/ |
| Услуги управления проектами | консалтинг | https://www.purrweb.com/ru/uslugi/uslugi-upravleniya-proektami/ |
| Разработка ТЗ на приложение | консалтинг | https://www.purrweb.com/ru/uslugi/tz-na-razrabotku-prilozheniya/ |
| HealthTech-разработка (медицинское направление) | отраслевая | https://www.purrweb.com/ru/healthtech/ |
| Разработка финансовых приложений | отраслевая | https://www.purrweb.com/ru/uslugi/razrabotka-finansovyh-prilozhenij/ |

### wnfx.ru — услуг с отдельными страницами: 22

*Направление:* мобильная разработка (студия WINFOX)

> Сайт студии мобильной разработки WINFOX (ООО), WordPress, sitemap index доступен. Особенности: (1) отдельной страницы «разработка мобильных приложений» нет — её роль выполняет главная (title «Разработка мобильных приложений на заказ с гарантией...»), включена с url главной. (2) Страницы /integrated/* — краткие карточки интеграций мобильных приложений с платформами (хаб-каталог: https://wnfx.ru/integrated/), контент тонкий, датированы 2020 г., но это отдельные живые URL. (3) /landing-lk/ и /razrabotka-lichnogo-kabineta-dlya-b2b-i-b2c-klientov/ — две отдельные страницы на близкую тему личных кабинетов (вторая, вероятно, SEO-дубль/лендинг). (4) Сервис Stories — продуктизированная услуга по подписке (5000 руб/мес). Не включено: /rate-card/ — прайс почасовых ставок аутстафф-специалистов; раздел /showcase/ (17 стр.) — витрина готовых экранов/функций мобильного приложения, не услуги; в меню внешняя ссылка на собственный продукт Martenn (martenn.com). Кейсы (portfolio-sitemap), блог (post-sitemap) и вакансии исключены. Выборочная проверка ~12 страниц подтвердила, что они живые (не 404/редирект).

| Услуга | Категория | URL |
|---|---|---|
| Разработка мобильных приложений на заказ (iOS и Android) | разработка | https://wnfx.ru/ |
| Проектирование мобильных приложений | консалтинг | https://wnfx.ru/proektirovanie-mobilnyh-prilozhenij/ |
| Дизайн мобильных приложений («Дизайн, который работает») | дизайн | https://wnfx.ru/dizajn-kotoryj-rabotaet/ |
| Техподдержка и сопровождение мобильных приложений | поддержка | https://wnfx.ru/tekhpodderzhka-mobilnykh-prilozheniy/ |
| IT-аутсорсинг и аутстаффинг (разработчики, аналитики, тестировщики) | аутстаффинг | https://wnfx.ru/outstaff/ |
| Разработка личных кабинетов для B2B и B2C клиентов | разработка | https://wnfx.ru/razrabotka-lichnogo-kabineta-dlya-b2b-i-b2c-klientov/ |
| Личный кабинет клиента в B2B | разработка | https://wnfx.ru/landing-lk/ |
| Разработка и внедрение ИИ и цифровых сотрудников (чат-боты с AI) | разработка | https://wnfx.ru/razrabotka-chat-botov-s-ai/ |
| Разработка на Laravel | разработка | https://wnfx.ru/landing-laravel/ |
| Разработка на Vue.js | разработка | https://wnfx.ru/landing-vue/ |
| Разработка на React.js | разработка | https://wnfx.ru/landing-reactjs/ |
| Разработка сервиса Stories (историй) для мобильных приложений | разработка | https://wnfx.ru/stories/ |
| Мобильное приложение для магазина с доставкой (интернет-магазинов) | отраслевая | https://wnfx.ru/mobilnoe-prilozhenie-dlya-internet-magazinov/ |
| Мобильное приложение для розничной торговли | отраслевая | https://wnfx.ru/mobilnoe-prilozhenie-dlya-roznichnoj-torgovli/ |
| Интеграция мобильного приложения с Bitrix24 | интеграция | https://wnfx.ru/integrated/bitrix24/ |
| Интеграция мобильного приложения с 1С-Битрикс | интеграция | https://wnfx.ru/integrated/1s-bitriks/ |
| Интеграция мобильного приложения с 1С | интеграция | https://wnfx.ru/integrated/1s/ |
| Интеграция мобильного приложения с amoCRM | интеграция | https://wnfx.ru/integrated/amocrm/ |
| Интеграция мобильного приложения с OpenCart | интеграция | https://wnfx.ru/integrated/opencart/ |
| Интеграция мобильного приложения с InSales | интеграция | https://wnfx.ru/integrated/insales/ |
| Интеграция мобильного приложения с CS-Cart | интеграция | https://wnfx.ru/integrated/cs-cart/ |
| Интеграция мобильного приложения с UMI.CMS | интеграция | https://wnfx.ru/integrated/umi-cms/ |

### www.simbirsoft.com — услуг с отдельными страницами: 31

*Направление:* мобильная разработка, аутстаффинг

> Источники: sitemap.xml, главное меню и хабовая страница услуг /help/ (28 позиций в трёх разделах: «Разработка», «Доработка продукта», «Консалтинг и аудит»). Дополнительно в sitemap найдены живые страницы услуг вне меню: /help/dedicated-team/ (Выделенный IT-центр), /help/design/ (UX/UI-дизайн, дубль-предшественник /help/design-uslugi/), /help/rpa/ (RPA-разработка, параллельно с /help/vnedrenie_avtomatizacii/). Выборочно проверены на живость (не 404/не редирект): dedicated-team, rpa, design, vnedrenie_avtomatizacii, infrastructure-audit — все живые. /help/it-product-old/ — устаревший дубль страницы «IT-продукт под ключ», в список не включён. Страниц коробочных продуктов и отраслевых лендингов услуг в sitemap не обнаружено. Отдельной страницы «аутстаффинг мобильных разработчиков» нет — мобильная разработка представлена одной страницей /help/razrabotka-mobilnykh-prilozheniy/.

| Услуга | Категория | URL |
|---|---|---|
| Аутстаффинг IT-специалистов | аутстаффинг | https://www.simbirsoft.com/help/outstaffing/ |
| IT-аутсорсинг | аутстаффинг | https://www.simbirsoft.com/help/outsourcing/ |
| Выделенный IT-центр | аутстаффинг | https://www.simbirsoft.com/help/dedicated-team/ |
| IT-продукт под ключ | разработка | https://www.simbirsoft.com/help/it-product/ |
| Разработка мобильных приложений | разработка | https://www.simbirsoft.com/help/razrabotka-mobilnykh-prilozheniy/ |
| Искусственный интеллект (AI/ML, Data) | разработка | https://www.simbirsoft.com/help/data/ |
| Бизнес-анализ и системный анализ | консалтинг | https://www.simbirsoft.com/help/analytics/ |
| Дизайн | дизайн | https://www.simbirsoft.com/help/design-uslugi/ |
| UX/UI-дизайн | дизайн | https://www.simbirsoft.com/help/design/ |
| Frontend-разработка | разработка | https://www.simbirsoft.com/help/frontend/ |
| Backend-разработка | разработка | https://www.simbirsoft.com/help/backend/ |
| Тестирование и обеспечение качества (QA) | QA | https://www.simbirsoft.com/help/quality-of-your-it-systems/ |
| SDET (разработка в тестировании) | QA | https://www.simbirsoft.com/help/sdet/ |
| Внедрение решений 1С | внедрение | https://www.simbirsoft.com/help/business-automation-1c/ |
| Разработка 1С на заказ | разработка | https://www.simbirsoft.com/help/1c-development/ |
| DevOps | прочее | https://www.simbirsoft.com/help/devops/ |
| Техническая поддержка по SLA | поддержка | https://www.simbirsoft.com/help/sla-support/ |
| Jira Service (внедрение и поддержка Jira) | внедрение | https://www.simbirsoft.com/help/jira/ |
| Разработка сайтов и корпоративных порталов | разработка | https://www.simbirsoft.com/help/development-website/ |
| Внедрение Битрикс | внедрение | https://www.simbirsoft.com/help/bitrix24/ |
| IT-архитектура | консалтинг | https://www.simbirsoft.com/help/it-architecture/ |
| Внедрение RPA (роботизация бизнес-процессов) | внедрение | https://www.simbirsoft.com/help/vnedrenie_avtomatizacii/ |
| RPA-разработка | разработка | https://www.simbirsoft.com/help/rpa/ |
| Спасение продукта | разработка | https://www.simbirsoft.com/help/save-a-product/ |
| Модернизация системы | разработка | https://www.simbirsoft.com/help/upgrade-existing-system/ |
| Discovery Phase (предпроектное исследование) | консалтинг | https://www.simbirsoft.com/help/discovery-phase/ |
| QA-консалтинг | консалтинг | https://www.simbirsoft.com/help/qa-consulting/ |
| IT-консалтинг | консалтинг | https://www.simbirsoft.com/help/it-consulting/ |
| UX-аудит | дизайн | https://www.simbirsoft.com/help/ux-audit/ |
| Разработка финансовых методологий | консалтинг | https://www.simbirsoft.com/help/razrabotka-fin-metodologii/ |
| Аудит ИТ-инфраструктуры | консалтинг | https://www.simbirsoft.com/help/infrastructure-audit/ |

### appfox.ru — услуг с отдельными страницами: 49

*Направление:* мобильная разработка, игры

> Сайт полностью доступен, sitemap.xml отдаётся целиком. Каталог услуг очень большой (90+ URL), список сокращён до верхнеуровневых услуг/направлений (49 позиций). Опущены подуровни: (1) 24 технологические страницы «разработка на <стек>» под /uslugi/ — PHP, Laravel, Node.js, React, React Native, Flutter, Unity, Unreal Engine, Python, Java, Kotlin, Swift, Go, C++, C#, Dart, JavaScript, Vue, Nuxt.js, Redux, IoT, Blockchain, нейросети, ASP.NET (хаб: https://appfox.ru/uslugi/); (2) 6 подстраниц iOS-направления под /razrabotka-pod-ios/ (iPhone, iPad, Apple TV, Apple Watch, программы, iOS-игры); (3) 11 подстраниц /podgotovka-tz/ по типам ТЗ (на мобильные/компьютерные/браузерные/крипто/промо-игры, AR, VR, сайты, дизайн, копирайтинг, приложения). У айдентики две дублирующие страницы: /sozdanie-ajdentiki/ (в меню) и /razrabotka-ajdentiki/ (в футере) — включена одна. Коробочных продуктов не обнаружено; есть некоммерческие для нашего списка страницы: онлайн IT-школа (/it-shkola/), калькулятор стоимости (/calculator/), инвестиции. Профиль конкурента: сильный уклон в геймдев (мобильные, ПК, VR/AR, крипто-игры) + мобильная разработка, плюс широкий блок маркетинга (SEO/ASO/SMM/контекст/GEO-AEO). Живость страниц выборочно подтверждена (/razrabotka-mobilnyh-igr/ — H1 «Разработка мобильных игр под ключ», /telegram-mini-apps/ — H1 «Разработка Telegram Mini Apps под ключ»).

| Услуга | Категория | URL |
|---|---|---|
| Разработка мобильных игр | разработка | https://appfox.ru/razrabotka-mobilnyh-igr/ |
| Разработка компьютерных (ПК) игр | разработка | https://appfox.ru/razrabotka-pk-igr/ |
| Разработка браузерных и онлайн-игр | разработка | https://appfox.ru/razrabotka-brauzermix-igr/ |
| Разработка игр на Unreal Engine | разработка | https://appfox.ru/razrabotka-igr-na-unreal-engine/ |
| Разработка крипто-игр на блокчейне (Blockchain/Web3) | разработка | https://appfox.ru/razrabotka-kripto-igr-na-blokchejn/ |
| VR-разработка (виртуальная реальность) | разработка | https://appfox.ru/vr-razrabotka/ |
| Разработка дополненной реальности (AR) | разработка | https://appfox.ru/razrabotka-dopolnennoj-realnosti/ |
| Разработка промо-игр | разработка | https://appfox.ru/promoigry/ |
| Разработка детских игр | разработка | https://appfox.ru/detskie-igry/ |
| Разработка онлайн-казино | отраслевая | https://appfox.ru/kazino/ |
| Озвучка игр | прочее | https://appfox.ru/ozvuchka-igr/ |
| Локализация игр | прочее | https://appfox.ru/lokalizatsiya-igr/ |
| Локализация мобильных приложений | прочее | https://appfox.ru/lokalizatsiya-mobilnykh-prilozheniy/ |
| Портирование игр и приложений | разработка | https://appfox.ru/portirovanie-igr-i-prilozheniy/ |
| Разработка приложений для Android | разработка | https://appfox.ru/razrabotka-pod-android/ |
| Разработка приложений на iOS | разработка | https://appfox.ru/razrabotka-pod-ios/ |
| Приложения для бизнеса | разработка | https://appfox.ru/prilozheniya-dlya-biznesa/ |
| Разработка Telegram Mini Apps | разработка | https://appfox.ru/telegram-mini-apps/ |
| Разработка приложений ВКонтакте (VK Mini Apps) | разработка | https://appfox.ru/razrabotka-prilozhenij-vk/ |
| Разработка сайтов | разработка | https://appfox.ru/razrabotka-sayta/ |
| Разработка порталов | разработка | https://appfox.ru/razrabotka-portalov/ |
| Разработка ПО и софта | разработка | https://appfox.ru/razrabotka-po/ |
| Разработка AI-агентов | разработка | https://appfox.ru/razrabotka-ai-agentov/ |
| AR-маски на заказ | разработка | https://appfox.ru/ar-maski/ |
| Разработка для стартапов | разработка | https://appfox.ru/razrabotka-dlya-startapov/ |
| Разработка интерактивных презентаций | разработка | https://appfox.ru/razrabotka-interaktivnykh-prezentatsiy/ |
| Внедрение геймификации | внедрение | https://appfox.ru/vnedrenie-geymifikatsii/ |
| IT-аутстаффинг | аутстаффинг | https://appfox.ru/it-autstaffing/ |
| Поддержка сайтов | поддержка | https://appfox.ru/podderzhka-sajtov/ |
| Дизайн мобильных приложений | дизайн | https://appfox.ru/dizain-mobilnix-prilojeniy/ |
| Разработка 2D-анимации | дизайн | https://appfox.ru/razrabotka-2d-animacii/ |
| Разработка 3D-анимации | дизайн | https://appfox.ru/razrabotka-3d-animacii/ |
| 3D-моделирование | дизайн | https://appfox.ru/3d-modelirovanie/ |
| Создание мультфильмов | дизайн | https://appfox.ru/sozdanie-multfilmov/ |
| Разработка айдентики | дизайн | https://appfox.ru/sozdanie-ajdentiki/ |
| Разработка логотипа | дизайн | https://appfox.ru/razrabotka-logotipa/ |
| Отрисовка персонажей нейросетью | дизайн | https://appfox.ru/otrisovka-personazha-nejrosetju/ |
| Создание контента нейросетями | прочее | https://appfox.ru/sozdanie-kontenta-neirosetyami/ |
| SEO-продвижение сайтов | прочее | https://appfox.ru/seo-prodvizhenie/ |
| ASO-продвижение приложений | прочее | https://appfox.ru/aso-prodvijenie-prilojeniy/ |
| Продвижение мобильных приложений | прочее | https://appfox.ru/prodvijenie-prilojeniy/ |
| SMM-продвижение | прочее | https://appfox.ru/smm-prodvizhenie/ |
| Таргетированная реклама | прочее | https://appfox.ru/targeting/ |
| Контекстная реклама | прочее | https://appfox.ru/kontekstnaya-reklama/ |
| GEO/AEO-продвижение в нейросетях | прочее | https://appfox.ru/geo-aeo-prodvizhenie-v-neyrosetyakh/ |
| Веб-аналитика | консалтинг | https://appfox.ru/web-analitika/ |
| Подготовка технических заданий | консалтинг | https://appfox.ru/podgotovka-tz/ |
| Разработка токеномики проекта | консалтинг | https://appfox.ru/razrabotka-tokenomiki-proekta/ |
| Менеджмент IT-проектов | консалтинг | https://appfox.ru/menedzhment-proektov/ |

### softmg.ru — услуг с отдельными страницами: 34

*Направление:* мобильная разработка

> Компания — Soft Media Group (ООО «СофтМедиаГрупп»), softmg.ru, «интегратор цифровых решений», 15+ лет, 95 сотрудников, 1000+ проектов. Сайт отдаётся нормально: sitemap.xml (520 URL), меню и хаб /uslugi/ разобраны. Каталог услуг >40 отдельных страниц, поэтому список сокращён до верхнеуровневых услуг и ключевых направлений; опущены многочисленные технолого-специфичные варианты с собственными страницами: разработка сайтов на конкретных фреймворках (Symfony, Laravel, Yii, Zend, CodeIgniter, CakePHP, JavaScript/Vue/React, Java, Spring, PHP), разработка ПО на конкретных языках (Python, Django, Golang, .NET, веб-разработка на Python), интернет-магазины на конкретных CMS (1С-Битрикс, WordPress, OpenCart, Magento, PrestaShop, VirtueMart, Ubercart, osCommerce, Shop Script, UMI.CMS, NetCat), сайты на CMS (Drupal, Joomla, WordPress, 1С-Битрикс, Wix), техподдержка по CMS (Bitrix, WordPress, Joomla, Drupal, NetCat, OpenCart), продвижение по каналам (Яндекс, Google, корпоративные сайты, интернет-магазины), варианты «под ключ»/«недорого»/«с нуля»/«по шаблону». Выборочно проверены живые страницы: /uslugi/ (хаб услуг), /application-development/ (H1 «Разработка приложений»), /audit/ (H1 «Аудит кода») — все реальные, не 404 и не редиректы. Страница /application-development/flutter/ есть в меню и на хабе услуг, но отсутствует в sitemap (видимо, новая). Коробочных продуктов компании не обнаружено; Telegram Mini Apps как отдельной услуги нет. Отраслевых лендингов услуг нет — отрасли представлены только кейсами в /examples/. По мобильной разработке (контекст конкуренции) у компании 6 отдельных страниц: общая, iOS, Android, React Native, Flutter, приложения для смартфонов.

| Услуга | Категория | URL |
|---|---|---|
| Разработка сайтов | разработка | https://softmg.ru/development/ |
| Разработка приложений (мобильная разработка) | разработка | https://softmg.ru/application-development/ |
| Разработка приложений для iOS | разработка | https://softmg.ru/application-development/ios/ |
| Разработка приложений для Android | разработка | https://softmg.ru/application-development/android/ |
| Разработка приложений на React Native | разработка | https://softmg.ru/application-development/react-native/ |
| Разработка приложений на Flutter | разработка | https://softmg.ru/application-development/flutter/ |
| Разработка приложений для смартфонов | разработка | https://softmg.ru/application-development/smartphone/ |
| Разработка ПО | разработка | https://softmg.ru/razrabotka-po/ |
| Разработка программных продуктов | разработка | https://softmg.ru/software-product-development/ |
| Разработка ИИ-решений | разработка | https://softmg.ru/razrabotka-ai/ |
| Разработка ИИ-агентов | разработка | https://softmg.ru/razrabotka-ai/biznes-agenty/ |
| Чат-боты для бизнеса | разработка | https://softmg.ru/razrabotka-ai/chat-boty/ |
| Разработка интернет-магазинов | разработка | https://softmg.ru/development/shop/ |
| Разработка корпоративных сайтов | разработка | https://softmg.ru/development/corporate/ |
| Разработка лендингов | разработка | https://softmg.ru/development/landing-page/ |
| Разработка сайтов-визиток | разработка | https://softmg.ru/development/card/ |
| Разработка сайтов на фреймворках | разработка | https://softmg.ru/development/framework/ |
| Разработка интерактивных сайтов | разработка | https://softmg.ru/development/interactive/ |
| Разработка на Unity | разработка | https://softmg.ru/unity/ |
| Доработка сайтов | разработка | https://softmg.ru/dorabotka-saytov/ |
| Аутстаффинг IT-специалистов | аутстаффинг | https://softmg.ru/it-autstaffing/ |
| Аутсорс IT | аутстаффинг | https://softmg.ru/outsource/ |
| Техподдержка сайтов | поддержка | https://softmg.ru/support/ |
| Администрирование серверов | поддержка | https://softmg.ru/server-administration/ |
| DevOps | прочее | https://softmg.ru/uslugi/devops/ |
| Интеграция с 1С | интеграция | https://softmg.ru/integraciya-1c/ |
| Интеграция аналитики (Google Analytics) | интеграция | https://softmg.ru/ga/ |
| Тестирование ПО | QA | https://softmg.ru/testirovanie/ |
| Автоматизация тестирования | QA | https://softmg.ru/uslugi/automated-testing/ |
| Дизайн | дизайн | https://softmg.ru/development/design/ |
| Системная аналитика | консалтинг | https://softmg.ru/systems-analyst/ |
| Аудит кода | консалтинг | https://softmg.ru/audit/ |
| Продвижение сайтов | прочее | https://softmg.ru/promotion/ |
| Разработка сайта под SEO | прочее | https://softmg.ru/development/seo/ |

### is-art.ru — услуг с отдельными страницами: 42

*Направление:* мобильная разработка и веб-сервисы

> Сайт IS ART (is-art.ru) — веб-студия из Орехово-Зуево (WordPress-сайт). Список собран по sitemap index (https://is-art.ru/sitemap.xml, все pt-page-файлы просмотрены), HTML-карте сайта /karta-sajta/ и меню главной. Выборочно проверены живьём: /apps/, /apps3/, /obsluzhivanie/, /distancionnoe-obuchenie/, /samopisnye-sajty/, /sozdanie-mediczinskih-sajtov/ — все отдают полноценные страницы услуг. Профиль конкурента: в первую очередь разработка и продвижение САЙТОВ; мобильная разработка представлена двумя лендингами — /apps/ (основной, «Разработка мобильных приложений и WEB-сервисов», React Native/Laravel/Node.js) и дублем /apps3/ (в список включён только /apps/). НЕ включены: ~80 гео-лендингов городов (/moskva/, /kazan/ и т.п. — та же услуга разработки сайтов по городам); тарифные страницы продвижения (/prodvizhenie/tarif-start|-optimalnyj|-maksimalnyj/ — тарифы одной услуги SEO); SEO-дубли общей услуги разработки (/professionalnaya-razrabotka-sajtov/, /uslugi-po-razrabotke-sozdaniyu-sajtov/, /internet-agenstvo/, /razrabotka-sajta-v-moskve/, /lending/, /prodvizhenie-2/ и старые корневые дубли страниц типов сайтов); информационные страницы (/razrabotka-sajtov/chto-takoe-sajt/, квизы /quiz/, /site-quiz/, бриф). Коробочных продуктов у компании не обнаружено. CRM/ERP/аутстаффинг/QA как отдельных услуг нет — конкурент пересекается с BUDGET SOFT только по мобильной разработке, интернет-магазинам и веб-сервисам.

| Услуга | Категория | URL |
|---|---|---|
| Разработка сайтов | разработка | https://is-art.ru/razrabotka-sajtov/ |
| Разработка лендинг пейдж | разработка | https://is-art.ru/razrabotka-sajtov/razrabotka-landing-page/ |
| Разработка сайта-визитки | разработка | https://is-art.ru/razrabotka-sajtov/razrabotka-sajta-vizitki/ |
| Разработка корпоративного сайта | разработка | https://is-art.ru/razrabotka-sajtov/razrabotka-korporativnogo-sajta/ |
| Разработка интернет-магазина | разработка | https://is-art.ru/razrabotka-sajtov/razrabotka-internet-magazina/ |
| Создание сайта на 1С-Битрикс | разработка | https://is-art.ru/razrabotka-sajtov/sozdanie-sajta-na-bitrix/ |
| Создание сайта на WordPress | разработка | https://is-art.ru/razrabotka-sajtov/sozdanie-sajta-na-wordpress/ |
| Создание сайта на React JS | разработка | https://is-art.ru/sozdanie-sajta-na-react/ |
| Разработка дорогих сайтов | разработка | https://is-art.ru/razrabotka-sajtov/razrabotka-dorogih-sajtov/ |
| Разработка недорогих сайтов | разработка | https://is-art.ru/razrabotka-sajtov/razrabotka-nedorogih-sajtov/ |
| Разработка самописных сайтов (без CMS) | разработка | https://is-art.ru/samopisnye-sajty/ |
| Разработка мобильных приложений и web-сервисов | разработка | https://is-art.ru/apps/ |
| Редизайн сайта | дизайн | https://is-art.ru/razrabotka-sajtov/redizajn-sajta/ |
| Продвижение сайтов (SEO) | прочее | https://is-art.ru/prodvizhenie/ |
| Реклама (контекстная реклама) | прочее | https://is-art.ru/prodvizhenie/reklama/ |
| SMM-продвижение | прочее | https://is-art.ru/prodvizhenie-smm/ |
| Обслуживание сайтов (техподдержка) | поддержка | https://is-art.ru/obsluzhivanie/ |
| Доработка сайтов | поддержка | https://is-art.ru/dorabotka-sajtov/ |
| Перенос сайта на другую CMS | прочее | https://is-art.ru/perenos-na-cms/ |
| Перенос сайта на 1С-Битрикс | прочее | https://is-art.ru/perenesti-sajt-na-1c-bitrix/ |
| Перенос сайта на WordPress | прочее | https://is-art.ru/perenesti-sajt-na-wordpress/ |
| Разработка систем дистанционного обучения (LMS) | отраслевая | https://is-art.ru/distancionnoe-obuchenie/ |
| Разработка онлайн-школ | отраслевая | https://is-art.ru/razrabotka-onlajn-shkol/ |
| Создание туристических сайтов | отраслевая | https://is-art.ru/sozdanie-turisticheskih-sajtov/ |
| Разработка сайта недвижимости | отраслевая | https://is-art.ru/razrabotka-sajta-nedvizhimosti/ |
| Создание сайта агентства недвижимости | отраслевая | https://is-art.ru/sozdanie-sajta-agentstva-nedvizhimosti/ |
| Разработка сайта магазина автозапчастей | отраслевая | https://is-art.ru/razrabotka-sajta-magazina-avtozapchastej/ |
| Создание сайта строительной компании | отраслевая | https://is-art.ru/sozdanie-sajta-stroitelnoj-kompanii/ |
| Разработка сайта для салона штор | отраслевая | https://is-art.ru/razrabotka-sajta-dlya-salona-shtor/ |
| Сайт для автосалона | отраслевая | https://is-art.ru/sajt-dlya-avtosalona/ |
| Создание сайта по ремонту квартир | отраслевая | https://is-art.ru/sozdanie-sajta-po-remontu-kvartir/ |
| Создание сайта юридических услуг | отраслевая | https://is-art.ru/sozdanie-sajta-yuridicheskih-uslug/ |
| Создание сайта для автосервиса | отраслевая | https://is-art.ru/sozdanie-sajta-dlya-avtoservisa/ |
| Создание сайта для магазина строительных материалов | отраслевая | https://is-art.ru/sozdanie-sajta-dlya-stroitelnyh-materialov/ |
| Создание сайта для рекламного агентства и типографии | отраслевая | https://is-art.ru/sozdanie-sajta-dlya-reklamnogo-agentstva-i-tipografii/ |
| Создание сайта для производства | отраслевая | https://is-art.ru/sozdanie-sajta-dlya-proizvodstva/ |
| Создание сайта для мебельного салона | отраслевая | https://is-art.ru/sozdanie-sajta-dlya-mebelnogo-salona/ |
| Создание сайта для магазина одежды и обуви | отраслевая | https://is-art.ru/sozdanie-sajta-dlya-magazina-odezhdy-i-obuvi/ |
| Создание сайта для магазина люстр и освещения | отраслевая | https://is-art.ru/sozdanie-sajta-dlya-magazina-lyustr-i-osveshheniya/ |
| Создание сайта для кафе и ресторанов | отраслевая | https://is-art.ru/sozdanie-sajta-dlya-kafe-i-restoranov/ |
| Создание сайта для детских товаров | отраслевая | https://is-art.ru/sozdanie-sajta-dlya-detskih-tovarov/ |
| Создание медицинских сайтов | отраслевая | https://is-art.ru/sozdanie-mediczinskih-sajtov/ |

### koyutech.ru — услуг с отдельными страницами: 3

*Направление:* мобильная разработка

> Сайт компании Koyu.Tech (Омск) небольшой, sitemap.xml содержит ~20 URL. Отдельных страниц услуг всего три, все проверены — живые страницы с собственными H1. Флагманская услуга «Разработка CRM-систем под ключ» описана только на главной странице (H1 главной: «Разработка CRM систем и мобильных приложений "под ключ"»), отдельного URL у неё нет, поэтому в список не включена. Страница /ai-integration есть в меню, но отсутствует в sitemap.xml. Раздел /services — каталог собственных бесплатных продуктов компании (TG Push — Telegram-уведомления, SVG Editor, Reverse Geocoding API), это не клиентские услуги. Остальные страницы — портфолио (~10 кейсов), команда, контакты, privacy.

| Услуга | Категория | URL |
|---|---|---|
| Разработка мобильных приложений под ключ (Android и iOS) | разработка | https://koyutech.ru/mobile-apps |
| Внедрение ИИ (искусственный интеллект для бизнеса) | внедрение | https://koyutech.ru/ai-integration |
| Техническая поддержка сайтов | поддержка | https://koyutech.ru/support |

### rarus.ru — услуг с отдельными страницами: 14

*Направление:* мобильная разработка (1С-Рарус)

> Крупный франчайзи 1С, каталог огромный — приведены только верхнеуровневые направления услуг (список сокращён). Добран вручную 06.07.2026.

| Услуга | Категория | URL |
|---|---|---|
| Услуги по 1С для среднего и малого бизнеса | внедрение | https://rarus.ru/1c/ |
| Отраслевая автоматизация на 1С | отраслевая | https://rarus.ru/1c-branches/ |
| Автоматизация крупного бизнеса (1С:КОРП) | внедрение | https://rarus.ru/1c-corp/ |
| Внедрение 1С:ERP для управления производством | внедрение | https://rarus.ru/erp/ |
| Аренда 1С в облаке | прочее | https://rarus.ru/arenda-1c-oblako/ |
| Внедрение CRM для управления продажами | внедрение | https://rarus.ru/crm/ |
| Автоматизация розничной торговли | отраслевая | https://rarus.ru/retail/ |
| 1С:Фреш (облачная 1С) | прочее | https://rarus.ru/1cfresh/ |
| Бухгалтерское сопровождение | прочее | https://rarus.ru/buhgalterskie-uslugi/soprovozhdenie/ |
| Услуги для международных компаний | прочее | https://rarus.ru/1c-corp/for-international-companies/ |
| Учебный центр (обучение 1С) | прочее | https://rarus.ru/1c-edu/ |
| Услуги государственным структурам | отраслевая | https://rarus.ru/government/ |
| Разработка мобильных приложений | разработка | https://rarus.ru/mobile/ |
| Интеграция телефонии (CTI) | интеграция | https://rarus.ru/cti/ |

### 10sec.ru — услуг с отдельными страницами: 7

*Направление:* Telegram Mini Apps

> Небольшая веб-студия. Полный список услуг получен из sitemap.xml и подтверждён по меню сайта и хабовым страницам /services/ и /services/sites/. Страница «Разработка сайтов» (/services/sites/) — одновременно страница услуги (H1 «Разработка сайтов») и хаб трёх подуслуг (корпоративные сайты, интернет-магазины, лендинги). Выборочно проверены живьём: telegram-mini-apps.html (H1 «Разработка Telegram Mini Apps», цены от 50 000 до 150 000+ руб.), crms.html, /services/sites/ — все реальные отдельные страницы, не 404/редиректы. Коробочных продуктов у компании нет. Мобильные приложения, SaaS и высоконагруженные веб-приложения упоминаются только в текстах/блоге — отдельных страниц нет, в список не включены. По направлению Telegram Mini Apps — прямой конкурент с отдельной страницей услуги и указанными ценами.

| Услуга | Категория | URL |
|---|---|---|
| Разработка Telegram Mini Apps | разработка | https://10sec.ru/services/telegram-mini-apps.html |
| Разработка сайтов | разработка | https://10sec.ru/services/sites/ |
| Разработка корпоративных сайтов | разработка | https://10sec.ru/services/sites/razrabotka-korporativnyix-sajtov.html |
| Разработка интернет-магазина | разработка | https://10sec.ru/services/sites/razrabotka-internet-magazina.html |
| Создание Landing Page | разработка | https://10sec.ru/services/sites/sozdanie-landing-page.html |
| Разработка ЦРМ для бизнеса | разработка | https://10sec.ru/services/crms.html |
| Разработка чат-ботов | разработка | https://10sec.ru/services/bots.html |

### НеСтудия — недоступен

*Направление:* Telegram Mini Apps и боты

> Домен в исходном анализе не зафиксирован; поиском (Google/варианты nestudia.ru|.com) сайт не находится — вероятно, закрыт или переименован.

### magnetto.pro — услуг с отдельными страницами: 20

*Направление:* Telegram-боты

> Magnetto.pro (ООО «Магнетто») — не разработчик заказного ПО, а digital-агентство интернет-маркетинга и официальный селлер Telegram Ads. Пересечение с BUDGET SOFT по направлению «Telegram-боты» — только две страницы: «Чат-боты в Telegram» (H1: «Создание чат-бота в Телеграм от 25 000 ₽ (без НДС)»; боты любой сложности, ИИ-боты, интеграция с CRM, геймификация через Telegram Mini Apps) и «Чат-боты и Mini Apps в MAX» (лидогенерация, автоматизация продаж и поддержки, интеграции с CRM и платёжными системами). Остальные услуги — рекламные (Telegram Ads, посевы, контекст, таргет, медийная, мобильная, Авито, маркетплейсы). Отдельной страницы «разработка Telegram Mini Apps» нет — есть только «Продвижение в Mini Apps» (рекламная услуга). Три региональные страницы Telegram Ads (Казахстан, Узбекистан, Беларусь) — гео-лендинги рекламной услуги, найдены только в sitemap, в меню их нет; проставил category «прочее», а не «отраслевая» (это гео, не отрасль). Список собран из sitemap.xml (271 URL, из них 20 /service/), меню и футера главной, хаба /service/; 4 страницы выборочно проверены — живые, не 404/редиректы. Коробочные продукты и обучение (в services не включены): аналитическая платформа Adstat.pro, Magnetto Education, курс «Telegram Ads с нуля до профи», бесплатные уроки, сертификация по Telegram Ads.

| Услуга | Категория | URL |
|---|---|---|
| Чат-боты в Telegram (создание чат-бота от 25 000 ₽) | разработка | https://magnetto.pro/service/telegram-bots/ |
| Чат-боты и Mini Apps для бизнеса в MAX | разработка | https://magnetto.pro/service/max-bots/ |
| Продвижение в Telegram | прочее | https://magnetto.pro/service/prodvizhenie-v-telegram/ |
| Telegram Ads | прочее | https://magnetto.pro/service/telegram-ads/ |
| Telegram Ads по всему миру | прочее | https://magnetto.pro/service/telegram-ads-worldwide/ |
| Посевы в Telegram | прочее | https://magnetto.pro/service/posevy-telegram/ |
| Продвижение в Telegram Mini Apps | прочее | https://magnetto.pro/service/prodvizhenie-v-telegram-mini-apps/ |
| Реклама в MAX | прочее | https://magnetto.pro/service/reklama-v-max/ |
| Продвижение канала в MAX | прочее | https://magnetto.pro/service/prodvizhenie-v-max/ |
| Таргетированная реклама | прочее | https://magnetto.pro/service/target/ |
| Продвижение в VK (ВКонтакте + Одноклассники) | прочее | https://magnetto.pro/service/prodvizhenie-vkontakte/ |
| Контекстная реклама (Яндекс Директ) | прочее | https://magnetto.pro/service/context/ |
| Комплексное продвижение | прочее | https://magnetto.pro/service/business-complex-marketing/ |
| Реклама на маркетплейсах | прочее | https://magnetto.pro/service/promo-on-marketplaces/ |
| Реклама в Авито | прочее | https://magnetto.pro/service/reklama-na-avito/ |
| Медийная реклама | прочее | https://magnetto.pro/service/media/ |
| Мобильная реклама | прочее | https://magnetto.pro/service/mobile/ |
| Реклама в Telegram Ads в Казахстане | прочее | https://magnetto.pro/service/telegram-ads-kazakhstan/ |
| Telegram Ads в Узбекистане | прочее | https://magnetto.pro/service/telegram-ads-uz/ |
| Telegram Ads в Беларуси | прочее | https://magnetto.pro/service/telegram-ads-belarus/ |

### simplify-bots.com — услуг с отдельными страницами: 1

*Направление:* Telegram-боты и Mini Apps

> Сайт — одностраничный SPA-лендинг (без SSR: все маршруты отдают одинаковый HTML-shell, контент рендерится клиентским JS). Sitemap.xml содержит только главную и /privacy-policy; в индексе поиска дополнительно есть /insightify-bot и /offer. Отдельных страниц услуг нет — направления (чат-боты Telegram/WhatsApp, MiniApp, WebApp, автоматизации, CRM-интеграции, хостинг ботов) перечислены только на главной, поэтому включена одна услуга с URL главной страницы. Коробочный продукт компании: Insightify — AI-бот для расшифровки и суммаризации голосовых, видео и аудио (https://simplify-bots.com/insightify-bot) — в список услуг не включён. /offer — публичная оферта, не услуга.

| Услуга | Категория | URL |
|---|---|---|
| Разработка чат-ботов, Web-приложений и Telegram Mini Apps | разработка | https://simplify-bots.com/ |

### cetera.ru — услуг с отдельными страницами: 42

*Направление:* Telegram Mini Apps (Cetera Labs)

> Cetera Labs (cetera.ru) — «AI-first» компания по созданию, поддержке и продвижению сайтов, 250+ сотрудников, ставка 1 800 ₽/час, работа по подписке (Mini Apps от 75 000 ₽/мес, услуги для интернет-магазинов от 195 000 ₽/мес). Каталог отдельных страниц услуг существенно больше 40 позиций, поэтому список сокращён до верхнеуровневых услуг и направлений + подуслуги Telegram/MAX (профильный контекст конкуренции). У каждого направления есть глубокие подстраницы, не включённые в список: например /ecommerce/development/, /ecommerce/types/online-pharmacy-website/, /crm/development/, /pim/implementation/, /corporate-portals/development/, лендинги типов ботов (/messenger/telegram-bot/chat-bot-dlya-otelya-v-telegram/, /messenger/telegram-bot/telegram-bot-dlya-sbora-dannykh-i-statistiki/), /1c/integratsia-1c/integratsiya-internet-magazina-s-1c/. Отраслевые разделы /fields/ и /verticals/, портфолио /portfolio/ и каталог продуктов/технологий /catalog/ (готовые решения, Битрикс и т.п.) в список не включены. Выборочно проверены живые страницы: /messenger/telegram-web-app/mini-apps/ (H1 «Мини-приложения Telegram», цены, FAQ), /services/development/, /ecommerce/ — все отдаются корректно, не 404. Sitemap.xml содержит ~700+ URL, большинство — статьи /about/articles/.

| Услуга | Категория | URL |
|---|---|---|
| Создание и разработка сайтов (полный цикл) | разработка | https://cetera.ru/services/development/ |
| Поддержка и развитие сайтов | поддержка | https://cetera.ru/services/support/ |
| Продвижение сайтов | прочее | https://cetera.ru/services/clients/ |
| Сбор требований, анализ, аудит | консалтинг | https://cetera.ru/services/audit/ |
| Проектирование | дизайн | https://cetera.ru/services/prototype/ |
| Дизайн | дизайн | https://cetera.ru/services/design/ |
| Верстка | разработка | https://cetera.ru/services/coding/ |
| Программирование | разработка | https://cetera.ru/services/programming/ |
| Интеграция данных | интеграция | https://cetera.ru/services/integration/ |
| Публикация (контент-менеджмент) | прочее | https://cetera.ru/services/content-management/ |
| Контроль качества | QA | https://cetera.ru/services/qa/ |
| Внедрение | внедрение | https://cetera.ru/services/implementation/ |
| Информационная безопасность | прочее | https://cetera.ru/services/ib/ |
| Администрирование и хостинг | поддержка | https://cetera.ru/services/hosting/ |
| Корпоративные сайты | разработка | https://cetera.ru/webdevelopment/ |
| Интернет-магазины (создание, поддержка, развитие) | разработка | https://cetera.ru/ecommerce/ |
| Личные кабинеты (B2B-порталы) | разработка | https://cetera.ru/b2b/ |
| CRM (заказная разработка и кастомизация) | разработка | https://cetera.ru/crm/ |
| Корпоративные порталы | разработка | https://cetera.ru/corporate-portals/ |
| AI-решения | разработка | https://cetera.ru/systems/ai/ |
| Телефония и голосовые боты | разработка | https://cetera.ru/systems/call/ |
| Мессенджеры (боты и приложения для Telegram и MAX) | разработка | https://cetera.ru/messenger/ |
| Маркетплейсы | разработка | https://cetera.ru/marketplaces/ |
| PIM-системы | внедрение | https://cetera.ru/pim/ |
| Мобильные приложения и мобильные сайты | разработка | https://cetera.ru/mobile/ |
| Разработка интернет-СМИ | разработка | https://cetera.ru/massmedia/ |
| Телеграм-бот (разработка под ключ) | разработка | https://cetera.ru/messenger/telegram-bot/ |
| Telegram Web App | разработка | https://cetera.ru/messenger/telegram-web-app/ |
| Мини-приложения Telegram (Telegram Mini Apps) | разработка | https://cetera.ru/messenger/telegram-web-app/mini-apps/ |
| Приложение для мессенджера МАКС | разработка | https://cetera.ru/messenger/prilozhenie-max/ |
| МАКС-бот | разработка | https://cetera.ru/messenger/max-bot/ |
| Внедрение 1С | внедрение | https://cetera.ru/1c/implementation/ |
| Интеграция 1С | интеграция | https://cetera.ru/1c/integratsia-1c/ |
| Разработка 1С | разработка | https://cetera.ru/1c/razrabotka-1c/ |
| Доработка 1С | разработка | https://cetera.ru/1c/dorabotka-1c/ |
| Настройка 1С | внедрение | https://cetera.ru/1c/nastroika-1c/ |
| Сопровождение 1С | поддержка | https://cetera.ru/1c/soprovozhdenie-1c/ |
| Техподдержка 1С | поддержка | https://cetera.ru/1c/tehpodderzhka-1c/ |
| Обслуживание 1С | поддержка | https://cetera.ru/1c/obsluzhivanie-1c/ |
| Поддержка 1С | поддержка | https://cetera.ru/1c/support/ |
| 1С:ИТС (сопровождение по договору ИТС) | поддержка | https://cetera.ru/1c/1c-its/ |
| 1С:КП (комплект поддержки) | поддержка | https://cetera.ru/1c/1c-kp/ |

### metalamp.ru — услуг с отдельными страницами: 31

*Направление:* Telegram Mini Apps, Web3

> Сайт полностью доступен, есть чистый sitemap.xml (https://metalamp.ru/sitemap.xml) — список услуг собран по нему, по хабу /services и по меню главной; ~10 страниц выборочно проверены (живые, не 404/редиректы). Позиционирование: web3-решения для стартапов и бигтеха; TOP-10 blockchain-разработчиков по Clutch. Хаб /services содержит 10 верхнеуровневых услуг; остальные — специализированные SEO-лендинги по типам web3-продуктов (DeFi, DEX, NFT, GameFi, кошельки, RWA, TMA и др.) и по экосистемам/технологиям (TON, EVM, Solana, Cardano, LayerZero, Solidity, Haskell, FunC). Полукоробочные white-label продукты (Лаунчпад, NFT-маркетплейс под ключ, хаб «Готовые решения» /white-label) включены в список, т.к. продаются с внедрением/кастомизацией. Не включены: /education — собственная бесплатная школа разработчиков (не услуга клиентам), /agent-program — партнёрская программа, /expertise и /technologies — обзорные страницы, /cases — портфолио, /magazine — блог. По контексту «Telegram Mini Apps, Web3»: прямой конкурент по TMA (/tma и /ton, /func) и по всему спектру Web3; классической заказной разработки (CRM/ERP/сайты) у компании нет — всё сфокусировано на блокчейне, AI и MVP.

| Услуга | Категория | URL |
|---|---|---|
| Разработка dApps (децентрализованных приложений) | разработка | https://metalamp.ru/blockchain |
| Разработка смарт-контрактов | разработка | https://metalamp.ru/smart-contract |
| Разработка токена (токеномика, вестинг, миграция) | разработка | https://metalamp.ru/token-development |
| Дизайн (UX/UI для web3-приложений) | дизайн | https://metalamp.ru/design |
| Корпоративный web3 (криптоинтеграции: биржи, кошельки) | интеграция | https://metalamp.ru/cryptointegration |
| Консалтинг (технический консалтинг по web3) | консалтинг | https://metalamp.ru/consulting |
| AI-разработка | разработка | https://metalamp.ru/ai-development |
| Разработка MVP | разработка | https://metalamp.ru/mvp-development |
| Аутстаффинг | аутстаффинг | https://metalamp.ru/outstaffing |
| Аутсорсинг разработки | аутстаффинг | https://metalamp.ru/outsourcing |
| Разработка Telegram Mini Apps (TMA) | разработка | https://metalamp.ru/tma |
| DeFi: разработка платформ децентрализованных финансов | разработка | https://metalamp.ru/defi |
| Разработка DEX (децентрализованных бирж) | разработка | https://metalamp.ru/dex |
| Разработка криптокошельков (Wallet) | разработка | https://metalamp.ru/wallet |
| NFT-разработка (от концепции до запуска) | разработка | https://metalamp.ru/nft-development |
| NFT-маркетплейс под ключ (готовое решение) | разработка | https://metalamp.ru/nft-marketplace-turnkey |
| Разработка GameFi-приложений | разработка | https://metalamp.ru/gamefi |
| Лаунчпад (готовое white-label решение) | разработка | https://metalamp.ru/launchpad |
| RWA: платформы токенизации реальных активов | разработка | https://metalamp.ru/rwa |
| Разработка Prediction Market (рынков предсказаний) | разработка | https://metalamp.ru/prediction-market |
| ZKP: разработка с zero-knowledge proofs | разработка | https://metalamp.ru/zkp |
| Разработка Bitcoin L2 решений | разработка | https://metalamp.ru/bitcoin-l2 |
| Готовые White Label решения для web3 | прочее | https://metalamp.ru/white-label |
| Разработка на blockchain TON | разработка | https://metalamp.ru/ton |
| Разработка на EVM (Ethereum и EVM-совместимые сети) | разработка | https://metalamp.ru/ethereum |
| Разработка на Solana | разработка | https://metalamp.ru/solana |
| Разработка на Cardano | разработка | https://metalamp.ru/cardano |
| Разработка omnichain-приложений на LayerZero | разработка | https://metalamp.ru/layerzero |
| Разработка смарт-контрактов на Solidity | разработка | https://metalamp.ru/solidity |
| Разработка на Haskell | разработка | https://metalamp.ru/haskell |
| Разработка смарт-контрактов на FunC (TON) | разработка | https://metalamp.ru/func |

### smorodina.mobi — услуг с отдельными страницами: 20

*Направление:* Telegram Mini Apps

> Студия мобильной разработки Smorodina (Москва), узкая специализация: мобильные приложения (iOS/Android, нативная и кроссплатформенная разработка — Kotlin/KMP/Flutter/Dart), Mini Apps (Telegram и VK), высоконагруженные системы, дизайн и тестирование. Источник списка — sitemap.xml (61 URL, из них 20 страниц услуг) + хабовая страница /services (показывает 16 из 20 услуг; страницы iOS, Android, «для стартапа» и KMP-лендинг /kotlin на хабе не выведены, но живы — проверено по H1/Title). Ключевая страница-конкурент по Telegram Mini Apps: /service/telegram_mini_apps_development (Title: «Разработка Telegram Mini Apps | Разработка Tg Mini App под ключ в Москве»), плюс смежные /service/mini_apps и /service/vk_mini_apps_development. Отдельных страниц аутстаффинга, интеграции, поддержки, ИИ/ML нет. Не включены: проектные лендинги-кейсы /promoland, /tosk, /mtsmusic, а также /projects, /blog, /job, /about, /contacts, /policy. Названия услуг приведены по H1/хабу; часть названий на хабе сокращена (напр. «Tg mini apps», «Высоконагруженные системы»). Уровни вложенности URL непоследовательны (/service/ и /services/) — это фактические адреса из sitemap, проверены.

| Услуга | Категория | URL |
|---|---|---|
| Разработка мобильных приложений | разработка | https://smorodina.mobi/service/mobile_application_development |
| Нативная разработка | разработка | https://smorodina.mobi/service/native_development |
| Кроссплатформенная разработка приложений | разработка | https://smorodina.mobi/services/cross-platform_development |
| Разработка приложений для iOS | разработка | https://smorodina.mobi/service/mobile_application_development/ios |
| Разработка мобильных приложений на Android | разработка | https://smorodina.mobi/service/mobile_application_development/android |
| Разработка приложений на Kotlin | разработка | https://smorodina.mobi/services/kotlin_application_development |
| Разработка приложений на Kotlin Multiplatform | разработка | https://smorodina.mobi/kotlin |
| Разработка на Flutter | разработка | https://smorodina.mobi/service/flutter_development |
| Разработка на Dart | разработка | https://smorodina.mobi/service/dart_development |
| Разработка Mini Apps | разработка | https://smorodina.mobi/service/mini_apps |
| Разработка Telegram Mini Apps | разработка | https://smorodina.mobi/service/telegram_mini_apps_development |
| Разработка VK Mini Apps | разработка | https://smorodina.mobi/service/vk_mini_apps_development |
| Разработка высоконагруженных систем | разработка | https://smorodina.mobi/service/development_of_high-loadsystems |
| Мобильные приложения для бизнеса | разработка | https://smorodina.mobi/service/mobile_application_development/dlya-biznesa |
| Разработка приложений для стартапа | разработка | https://smorodina.mobi/service/mobile_application_development/dlya-startapa |
| Разработка MVP продукта | разработка | https://smorodina.mobi/service/mobile_application_development/mvp |
| Разработка VR приложений | разработка | https://smorodina.mobi/service/mobile_application_development/vr |
| Разработка дизайна приложений | дизайн | https://smorodina.mobi/service/razrabotka-dizayna-prilozheniy |
| Тестирование ПО | QA | https://smorodina.mobi/service/testirovaniye-po |
| QA тестирование | QA | https://smorodina.mobi/service/testirovaniye-po/qa |

### unitech.team — услуг с отдельными страницами: 2

*Направление:* Telegram Mini Apps

> Маленький бутик-сайт на Tilda: в sitemap всего 12 URL. Отдельных страниц услуг только две — /web (разработка веб-приложений) и /apps (Telegram Mini Apps под ключ), обе проверены и живые (H1: «Разработка веб-приложений, которые приносят прибыль бизнесу» и «Разработка Telegram Mini Apps под ключ»). Остальные страницы — кейсы (/keis — хаб, /mini-shef, /festique, /hockey-analytics, /hermes, /vtrende, /page105042866.html — дубль кейса «Мини Шеф»), /onas (о нас) и /politica (политика конфиденциальности). На главной перечислены направления (CRM/ERP, мобильные приложения, автоматизация, финтех/e-commerce, AI/ML, 3D, крипто/Web3), но отдельных страниц под них нет — только текст на общих страницах. Коробочных продуктов нет (Мини Шеф и пр. — клиентские кейсы). В sitemap URL указаны с www, но www.unitech.team не резолвится — рабочий домен без www. Поисковый индекс (site:) сайт почти не покрывает, полнота списка подтверждена по sitemap и меню.

| Услуга | Категория | URL |
|---|---|---|
| Разработка веб-приложений | разработка | https://unitech.team/web |
| Разработка Telegram Mini Apps под ключ | разработка | https://unitech.team/apps |

### starlakedigital.pro — услуг с отдельными страницами: 1

*Направление:* Telegram-боты и Mini Apps

> Сайт — одностраничный SPA-лендинг одной услуги (разработка Telegram Mini Apps и веб-приложений), поэтому услуга включена с URL главной страницы. Отдельных страниц услуг не существует: sitemap.xml содержит только главную и 3 кейса-проекта (/projects/nodating, /projects/prostozvonok, /projects/mafia — портфолио, не включены), в поиске проиндексирована только главная. SPA отдаёт один и тот же HTML-шелл на любой URL (включая несуществующие — настоящего 404 нет), клиентский контент через WebFetch не рендерится, поэтому детальный состав блоков лендинга (цены, этапы и т.п.) недоступен. Коробочных продуктов не обнаружено. По данным поисковой выдачи компания также упоминает веб-разработку, дизайн и SEO, но отдельных страниц под эти услуги нет.

| Услуга | Категория | URL |
|---|---|---|
| Разработка Telegram Mini-Apps и Web-приложений | разработка | https://starlakedigital.pro/ |

### botcreators.ru — услуг с отдельными страницами: 0

*Направление:* чат-боты, Mini Apps, ИИ-агенты

> Одностраничный лендинг: заявленные направления (чат-боты, мини-приложения, ИИ-агенты) отдельных страниц услуг НЕ имеют — только кейсы и блог. Добран вручную 06.07.2026.

### frog-studios.com — услуг с отдельными страницами: 7

*Направление:* Telegram Mini Apps

> AI-native студия заказной разработки. Добран вручную 06.07.2026 (основной домен работает, субдомен twa.* не резолвится).

| Услуга | Категория | URL |
|---|---|---|
| ИИ-продукты и автоматизация | разработка | https://frog-studios.com/services/ai-products |
| Разработка веб-сайтов | разработка | https://frog-studios.com/services/websites |
| Разработка веб-сервисов | разработка | https://frog-studios.com/services/web-services |
| Разработка Telegram Mini Apps | разработка | https://frog-studios.com/services/telegram-mini-apps |
| Разработка мобильных приложений | разработка | https://frog-studios.com/services/mobile-apps |
| Разработка корпоративных порталов | разработка | https://frog-studios.com/services/corporate-portals |
| Разработка чат-ботов | разработка | https://frog-studios.com/services/chatbots |
