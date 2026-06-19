# ТЗ: умный калькулятор стоимости разработки ПО

## 1. Название продукта

**AI Software Cost Estimator**

Рабочее название для сайта:

> **Калькулятор стоимости разработки ПО**

Маркетинговый заголовок:

> **Оцените стоимость разработки вашего проекта за 3 минуты**

Альтернативный вариант:

> **AI-калькулятор разработки: часы, сроки, команда и бюджет**

---

# 2. Главная идея

Пользователь заполняет умную анкету о будущем проекте. Система анализирует ответы, определяет тип продукта, сложность, количество модулей, интеграций, ролей пользователей, технические риски и на выходе формирует предварительную оценку:

```text
Backend: 180–240 часов
Frontend: 160–220 часов
QA: 60–90 часов
DevOps: 20–40 часов
Project Management: 40–60 часов

Итого: 460–650 часов
Срок: 2.5–4 месяца
Команда: 2 backend, 1 frontend, 1 QA, 1 PM part-time
Ориентировочная стоимость: от €18,000 до €32,000
```

Важно: калькулятор не должен выглядеть как игрушка. Он должен создавать ощущение, что компания реально понимает разработку, риски, архитектуру и бизнес-процессы.

---

# 3. Бизнес-цель

Основная цель — **лидогенерация для веб-студии / software agency**.

Калькулятор должен:

1. Привлекать потенциальных клиентов из SEO и рекламы.
2. Помогать клиенту понять порядок бюджета.
3. Собирать заявки от более теплых лидов.
4. Отсеивать клиентов с нереалистичными ожиданиями.
5. Показывать экспертность компании.
6. Давать менеджеру/аналитику стартовую информацию до первого звонка.
7. Генерировать PDF-отчет, который клиент может сохранить или переслать.

---

# 4. Ключевая ценность для клиента

Клиент получает не просто цену, а понятную структуру:

* что именно нужно разработать;
* какие модули входят в проект;
* где основные риски;
* сколько часов уйдет на backend, frontend, QA, DevOps;
* какая команда нужна;
* сколько это может стоить;
* какие функции лучше оставить на MVP;
* какие функции могут сильно увеличить бюджет.

---

# 5. Ключевая ценность для компании

Компания получает:

* email / телефон / Telegram клиента;
* описание проекта;
* бюджетный диапазон клиента;
* понимание серьезности лида;
* автоматическую предварительную декомпозицию;
* возможность сразу предложить консультацию;
* SEO-страницу под запросы вроде:

  * “сколько стоит разработка сайта”;
  * “калькулятор стоимости разработки приложения”;
  * “оценка разработки CRM”;
  * “стоимость разработки SaaS”;
  * “сколько часов нужно на разработку MVP”.

---

# 6. Тип продукта

Web-приложение, встроенное в сайт компании.

Формат:

```text
/estimate
/calculator
/software-cost-calculator
```

Для русской аудитории:

```text
/kalkulyator-stoimosti-razrabotki
/ocenka-proekta
```

---

# 7. Основные роли пользователей

## 7.1. Посетитель / потенциальный клиент

Может:

* пройти анкету;
* получить предварительную оценку;
* оставить контакты;
* скачать PDF;
* отправить результат себе на email;
* запросить консультацию.

## 7.2. Менеджер компании

Может:

* видеть заявки;
* смотреть ответы клиента;
* видеть расчет;
* менять статус лида;
* добавлять комментарии;
* отправлять уточняющее письмо.

## 7.3. Администратор

Может:

* менять ставки специалистов;
* менять коэффициенты сложности;
* редактировать вопросы анкеты;
* редактировать шаблон PDF;
* управлять типами проектов;
* смотреть статистику конверсий.

---

# 8. Общий пользовательский сценарий

## Сценарий 1: быстрый расчет

1. Пользователь заходит на страницу калькулятора.
2. Видит обещание:

```text
Ответьте на 15–25 вопросов и получите предварительную оценку часов, сроков и бюджета.
```

3. Выбирает тип проекта.
4. Отвечает на вопросы.
5. Система задает 2–5 уточняющих AI-вопросов, если данных недостаточно.
6. Пользователь вводит email.
7. Получает результат на экране.
8. Может скачать PDF.
9. Менеджеру создается лид.

---

## Сценарий 2: клиент вставляет текстовое ТЗ

1. Пользователь выбирает режим:

```text
У меня уже есть описание проекта
```

2. Вставляет текст.
3. AI анализирует ТЗ.
4. Система автоматически определяет:

   * тип проекта;
   * модули;
   * роли пользователей;
   * интеграции;
   * риски;
   * примерный объем работ.
5. Пользователь дополняет ответы через короткую анкету.
6. Получает оценку.

---

## Сценарий 3: клиент хочет только MVP

1. Пользователь выбирает:

```text
Мне нужна MVP-версия
```

2. Система отдельно показывает:

```text
MVP: 280–420 часов
Full version: 700–1100 часов
```

3. В отчете выделяются:

   * обязательные функции;
   * функции второй очереди;
   * дорогие функции;
   * необязательные функции.

---

# 9. Структура анкеты

## 9.1. Блок 1 — тип проекта

Вопрос:

> Что вы хотите разработать?

Варианты:

* корпоративный сайт;
* интернет-магазин;
* маркетплейс;
* CRM;
* ERP;
* WMS / складская система;
* SaaS-сервис;
* мобильное приложение;
* личный кабинет;
* веб-приложение;
* AI-сервис;
* Telegram-бот;
* интеграция с существующей системой;
* другое.

Каждый тип проекта должен иметь свою базовую модель оценки.

Пример:

```text
Корпоративный сайт: 80–180 часов
CRM: 300–900 часов
Marketplace: 700–1800 часов
SaaS: 500–1600 часов
WMS: 800–2500 часов
AI-сервис: 400–1500 часов
```

---

## 9.2. Блок 2 — стадия проекта

Вопрос:

> На какой стадии находится проект?

Варианты:

* только идея;
* есть описание;
* есть дизайн;
* есть прототип;
* есть старая система;
* нужно доработать существующий проект;
* нужно переписать старый проект;
* есть готовое ТЗ.

Влияние на оценку:

```text
Только идея: +15–25% на аналитику
Есть дизайн: -5–10% на discovery
Есть старая система: +10–40% на анализ legacy-кода
Нужно переписать: +20–60% к рискам
```

---

## 9.3. Блок 3 — платформы

Вопрос:

> Где должен работать продукт?

Варианты:

* только web;
* web + mobile responsive;
* iOS;
* Android;
* iOS + Android;
* desktop;
* Telegram;
* API only;
* internal admin panel.

Пример логики:

```text
Web only: базовая оценка
Web + responsive: +10–20% frontend
iOS + Android native: +300–800 часов
Telegram bot: +40–160 часов
Admin panel: +80–300 часов
API only: акцент на backend
```

---

## 9.4. Блок 4 — пользователи и роли

Вопрос:

> Какие роли пользователей будут в системе?

Варианты:

* гость;
* зарегистрированный пользователь;
* администратор;
* менеджер;
* владелец бизнеса;
* поставщик;
* покупатель;
* курьер;
* оператор склада;
* модератор;
* бухгалтер;
* custom role.

Оценка:

```text
1 роль: базово
2–3 роли: +20–60 часов
4–6 ролей: +60–160 часов
7+ ролей: +150–400 часов
Сложные права доступа: +80–250 часов
```

---

## 9.5. Блок 5 — авторизация

Вопрос:

> Какая авторизация нужна?

Варианты:

* email + password;
* phone + SMS;
* Google login;
* Apple login;
* Facebook login;
* Telegram login;
* SSO;
* 2FA;
* magic link;
* корпоративные роли и permissions.

Пример оценки:

```text
Email/password: 16–32 часа
Password reset: 8–16 часов
Google login: 8–20 часов
Apple login: 12–24 часа
Phone/SMS: 20–50 часов
2FA: 24–60 часов
SSO: 40–120 часов
RBAC permissions: 40–160 часов
```

---

## 9.6. Блок 6 — основные модули

Вопрос:

> Какие разделы нужны в системе?

Варианты:

* dashboard;
* профили пользователей;
* каталог;
* карточка товара/объекта;
* поиск;
* фильтры;
* корзина;
* заказы;
* оплаты;
* подписки;
* уведомления;
* чат;
* отчеты;
* импорт/экспорт;
* календарь;
* документы;
* файлы;
* комментарии;
* задачи;
* роли и доступы;
* админ-панель;
* аналитика;
* API;
* интеграции.

Для каждого модуля нужно иметь базовый диапазон.

Пример:

```text
Dashboard: 24–80 часов
User profile: 20–60 часов
Catalog: 60–180 часов
Advanced filters: 30–100 часов
Orders: 80–240 часов
Payments: 40–120 часов
Reports: 50–200 часов
Notifications: 30–120 часов
Chat: 80–250 часов
File upload: 20–80 часов
Admin panel: 80–300 часов
```

---

# 10. Отдельный блок для AI-функций

Это важно, потому что сейчас многие клиенты хотят “AI”, но не понимают сложность.

Вопрос:

> Нужны ли AI-функции?

Варианты:

* нет;
* AI-чат;
* генерация текстов;
* генерация изображений;
* анализ документов;
* поиск по базе знаний;
* RAG;
* AI-агент;
* автоматическая классификация заявок;
* распознавание изображений;
* голосовой ввод;
* транскрибация;
* перевод;
* рекомендации;
* другое.

Оценка:

```text
AI chat простой: 40–100 часов
AI chat с историей: 80–180 часов
RAG по документам: 120–350 часов
AI agent workflow: 200–700 часов
Document parsing: 80–250 часов
Transcription: 40–120 часов
Image recognition: 80–300 часов
AI moderation: 60–180 часов
```

Дополнительные вопросы:

* Какие данные должен использовать AI?
* Нужно ли хранить историю?
* Нужна ли модерация ответов?
* Нужна ли проверка качества AI-ответов?
* Есть ли конфиденциальные данные?
* Нужно ли подключение OpenAI / Claude / локальной модели?
* Нужна ли защита от prompt injection?
* Нужна ли ручная проверка результата человеком?

AI-функции должны получать отдельный риск-множитель:

```text
AI risk coefficient: 1.2–1.8
```

---

# 11. Интеграции

Вопрос:

> С какими сервисами нужна интеграция?

Варианты:

* Stripe;
* PayPal;
* YooKassa;
* CloudPayments;
* Telegram;
* WhatsApp;
* email;
* SMS;
* Google Maps;
* Google Calendar;
* Google Sheets;
* CRM;
* ERP;
* 1C;
* SAP;
* Shopify;
* WooCommerce;
* Amazon;
* eBay;
* OpenAI;
* Claude;
* платежный шлюз;
* delivery API;
* custom API.

Оценка:

```text
Простая API-интеграция: 16–40 часов
Средняя интеграция: 40–100 часов
Сложная интеграция: 100–300 часов
Плохая документация API: +20–50%
Нет документации API: +50–100%
Webhook processing: 20–80 часов
Retry/queue logic: 20–80 часов
Sync jobs: 30–120 часов
```

---

# 12. Блок по дизайну

Вопрос:

> Нужен ли дизайн?

Варианты:

* дизайн уже есть;
* нужен простой дизайн;
* нужен уникальный дизайн;
* нужна дизайн-система;
* нужен UX-прототип;
* нужно улучшить текущий интерфейс;
* достаточно готового UI kit.

Оценка:

```text
Готовый UI kit: 20–60 часов
Простой дизайн: 60–160 часов
Уникальный дизайн: 160–400 часов
Дизайн-система: 200–600 часов
UX-прототип: 40–160 часов
Редизайн существующего продукта: 100–400 часов
```

---

# 13. Блок по админке

Вопрос:

> Нужна ли административная панель?

Варианты:

* нет;
* простая;
* средняя;
* сложная;
* с ролями;
* с отчетами;
* с логами;
* с импортом/экспортом;
* с управлением контентом;
* с управлением пользователями.

Оценка:

```text
Простая админка: 60–120 часов
Средняя админка: 120–300 часов
Сложная админка: 300–800 часов
```

---

# 14. Блок по нагрузке

Вопрос:

> Какую нагрузку ожидаете?

Варианты:

* до 100 пользователей;
* до 1 000 пользователей;
* до 10 000 пользователей;
* до 100 000 пользователей;
* 100 000+ пользователей;
* не знаю.

Влияние:

```text
До 1 000: базовая архитектура
10 000+: +10–25% backend/devops
100 000+: +30–80% backend/devops
High-load: отдельная архитектурная оценка
```

Дополнительные вопросы:

* Будут ли пики нагрузки?
* Нужны ли очереди?
* Нужен ли кеш?
* Нужна ли горизонтальная масштабируемость?
* Нужен ли real-time?
* Нужен ли CDN?

---

# 15. Блок безопасности

Вопрос:

> Есть ли повышенные требования к безопасности?

Варианты:

* стандартные;
* персональные данные;
* платежные данные;
* медицинские данные;
* финансовые данные;
* корпоративные данные;
* аудит действий;
* шифрование;
* 2FA;
* role-based access;
* compliance;
* penetration test.

Оценка:

```text
Basic security: включено
Audit logs: 30–120 часов
2FA: 24–60 часов
Encryption: 40–160 часов
Advanced permissions: 80–250 часов
Security review: 40–120 часов
Compliance preparation: 100–400 часов
```

---

# 16. Блок отчетов и аналитики

Вопрос:

> Нужны ли отчеты?

Варианты:

* нет;
* простые таблицы;
* графики;
* экспорт CSV;
* экспорт Excel;
* PDF-отчеты;
* scheduled reports;
* BI dashboard;
* custom report builder.

Оценка:

```text
Простой отчет: 12–30 часов
Сложный отчет: 30–100 часов
PDF report: 30–120 часов
Excel export: 20–80 часов
Scheduled reports: 40–140 часов
Custom report builder: 200–700 часов
```

---

# 17. Блок legacy / доработки

Если пользователь выбирает “доработать существующий проект”, нужно спросить:

* На чем написан проект?
* Есть ли доступ к коду?
* Есть ли документация?
* Есть ли тесты?
* Есть ли staging-сервер?
* Есть ли DevOps?
* Кто писал проект?
* Сколько лет проекту?
* Нужно исправлять баги или добавлять новые функции?

Оценка:

```text
Code review: 20–80 часов
Legacy analysis: 40–200 часов
Refactoring risk: +20–80%
No tests: +15–40%
No documentation: +10–30%
Old framework: +20–60%
```

---

# 18. Логика расчета

Расчет должен быть не одной формулой, а комбинацией:

## 18.1. Base estimate

Каждый тип проекта имеет базовый диапазон.

Пример:

```json
{
  "crm": {
    "min_hours": 300,
    "max_hours": 900
  },
  "marketplace": {
    "min_hours": 700,
    "max_hours": 1800
  },
  "saas": {
    "min_hours": 500,
    "max_hours": 1600
  }
}
```

---

## 18.2. Module estimate

Каждый выбранный модуль добавляет часы.

Пример:

```json
{
  "payments": {
    "backend_min": 24,
    "backend_max": 80,
    "frontend_min": 16,
    "frontend_max": 40,
    "qa_min": 8,
    "qa_max": 24
  }
}
```

---

## 18.3. Complexity multiplier

Общий коэффициент сложности:

```text
Simple: 1.0
Medium: 1.25
Complex: 1.5
Very complex: 2.0
```

---

## 18.4. Risk multiplier

Риск-множитель:

```text
Clear requirements: 1.0
Some unknowns: 1.15
Many unknowns: 1.3
Legacy / integrations / AI: 1.4–1.8
```

---

## 18.5. Confidence level

Нужно показывать уровень уверенности:

```text
High confidence: ±20%
Medium confidence: ±35%
Low confidence: ±50%
```

Пример:

```text
Оценка: 480–720 часов
Уверенность: средняя
Причина: нет готового дизайна, есть внешние интеграции, не описаны роли пользователей.
```

---

# 19. Формула расчета

Упрощенно:

```text
Total hours =
Base project hours
+ Sum(module hours)
+ Sum(integration hours)
+ Design hours
+ QA hours
+ DevOps hours
+ PM hours
```

Затем:

```text
Total adjusted hours =
Total hours × complexity coefficient × risk coefficient
```

После этого добавляется буфер:

```text
Buffer:
Low risk: +10%
Medium risk: +20%
High risk: +30–50%
```

---

# 20. Распределение по ролям

Система должна показывать часы по ролям:

```text
Business Analysis
UX/UI Design
Backend
Frontend
Mobile
QA
DevOps
Project Management
Architecture
```

Пример:

```text
Business Analysis: 40–70h
UX/UI Design: 80–140h
Backend: 180–260h
Frontend: 160–230h
QA: 70–110h
DevOps: 20–50h
PM: 45–80h
```

---

# 21. Расчет стоимости

Администратор задает ставки:

```text
Backend: €35/h
Frontend: €35/h
QA: €25/h
Designer: €30/h
PM: €35/h
DevOps: €45/h
Architect: €50/h
```

Можно сделать 3 режима:

```text
Economy
Standard
Premium
```

Пример:

```text
Economy: €25/h average
Standard: €35/h average
Premium: €50/h average
```

На выходе:

```text
MVP estimate:
420–620 часов

Стоимость:
€14,700 – €21,700 при ставке €35/h
```

Важно: лучше показывать не точную цену, а диапазон.

---

# 22. Результат для пользователя

После прохождения анкеты пользователь видит экран:

## 22.1. Summary

```text
Ваш проект похож на: SaaS / CRM-система

Предварительная оценка:
520–780 часов

Ориентировочный срок:
3–5 месяцев

Рекомендуемая команда:
1 Backend developer
1 Frontend developer
1 QA engineer
1 PM part-time
1 UX/UI designer на этапе старта
```

---

## 22.2. Breakdown

```text
Discovery & Analysis: 40–80h
UX/UI Design: 80–140h
Backend: 180–280h
Frontend: 160–260h
QA: 60–120h
DevOps: 20–50h
PM: 50–90h
```

---

## 22.3. MVP vs Full version

```text
MVP:
320–480 часов
€11,200 – €16,800

Full version:
700–1100 часов
€24,500 – €38,500
```

---

## 22.4. Main cost drivers

Система должна объяснять, что увеличивает стоимость:

```text
Основные факторы стоимости:
1. Наличие нескольких ролей пользователей.
2. Интеграция с платежной системой.
3. Необходимость админ-панели.
4. AI-функции.
5. PDF-отчеты и экспорт данных.
```

---

## 22.5. Risks

```text
Риски:
- Не описаны бизнес-процессы.
- Неизвестна сложность интеграции с внешним API.
- Нет готового дизайна.
- AI-функциональность требует отдельного этапа проверки качества.
```

---

## 22.6. Recommendation

```text
Рекомендация:
Начать с MVP: авторизация, роли пользователей, основной dashboard, базовый CRUD, платежи и админ-панель.

AI-функции и расширенную аналитику лучше вынести во вторую фазу.
```

---

# 23. PDF-отчет

PDF должен включать:

1. Логотип компании.
2. Название проекта клиента.
3. Краткое описание.
4. Тип проекта.
5. Предварительную оценку часов.
6. Оценку стоимости.
7. Распределение по ролям.
8. MVP / Full version.
9. Основные модули.
10. Риски.
11. Рекомендации.
12. Следующий шаг:

```text
Запишитесь на бесплатную консультацию, чтобы получить точную оценку.
```

---

# 24. Lead capture

Контакты лучше не просить сразу. Иначе будет хуже конверсия.

Правильный сценарий:

1. Сначала пользователь проходит 60–80% анкеты.
2. Потом видит:

```text
Оценка почти готова.
Куда отправить PDF-отчет?
```

Поля:

* имя;
* email;
* Telegram / WhatsApp;
* компания;
* сайт компании;
* желаемый бюджет;
* когда хотите начать.

Важно: можно показать краткий результат сразу, а PDF отправлять после email.

Например:

```text
Предварительно: 400–700 часов.
Оставьте email, чтобы получить подробный PDF-отчет.
```

---

# 25. Админ-панель

## 25.1. Раздел Leads

Таблица:

| Поле         | Описание                           |
| ------------ | ---------------------------------- |
| Name         | Имя клиента                        |
| Email        | Email                              |
| Project type | Тип проекта                        |
| Budget       | Бюджет                             |
| Hours        | Оценка часов                       |
| Status       | New / Contacted / Qualified / Lost |
| Created at   | Дата                               |

---

## 25.2. Карточка лида

Внутри:

* ответы анкеты;
* AI summary;
* расчет часов;
* PDF;
* заметки менеджера;
* история статусов;
* кнопка “Send email”;
* кнопка “Book call”.

---

## 25.3. Настройки ставок

Админ может менять:

```text
Backend hourly rate
Frontend hourly rate
QA hourly rate
Designer hourly rate
DevOps hourly rate
PM hourly rate
Architect hourly rate
```

---

## 25.4. Настройки коэффициентов

Админ может менять:

```text
AI complexity multiplier
Legacy multiplier
Integration risk multiplier
High-load multiplier
Security multiplier
Unclear requirements multiplier
```

---

## 25.5. Настройки вопросов

Желательно, чтобы вопросы можно было редактировать без кода.

Минимально:

* включить/выключить вопрос;
* изменить текст вопроса;
* изменить варианты ответов;
* изменить порядок;
* указать, к какому модулю относится ответ.

---

# 26. AI-логика

AI не должен просто “фантазировать цену”. Лучше использовать гибридную модель:

## 26.1. Rule-based core

Основной расчет идет по правилам:

* тип проекта;
* модули;
* интеграции;
* роли;
* сложность;
* ставки;
* коэффициенты.

## 26.2. AI layer

AI используется для:

* анализа текстового описания проекта;
* определения недостающих данных;
* генерации уточняющих вопросов;
* объяснения оценки простым языком;
* генерации PDF summary;
* рекомендации MVP;
* выделения рисков;
* классификации проекта.

---

# 27. Пример AI-промпта

```text
You are a senior software architect and business analyst.

Analyze the user's project description and questionnaire answers.

Return structured JSON with:
- project_type
- suggested_modules
- user_roles
- integrations
- ai_features
- complexity_level
- risk_level
- missing_information
- mvp_recommendation
- estimation_notes

Do not calculate final price directly.
Do not invent exact numbers.
Use only structured factors.
```

Почему так: финальная цена должна считаться системой, а не только AI. Иначе будет нестабильно.

---

# 28. JSON-структура результата AI

```json
{
  "project_type": "crm",
  "complexity_level": "medium",
  "risk_level": "medium",
  "modules": [
    "authentication",
    "dashboard",
    "user_management",
    "orders",
    "reports",
    "notifications",
    "admin_panel"
  ],
  "integrations": [
    {
      "name": "Stripe",
      "complexity": "medium"
    }
  ],
  "ai_features": [
    {
      "name": "AI assistant",
      "complexity": "medium"
    }
  ],
  "missing_information": [
    "No detailed user roles",
    "No information about payment flow",
    "No design status"
  ],
  "mvp_recommendation": [
    "Authentication",
    "Main dashboard",
    "User management",
    "Core order flow",
    "Basic admin panel"
  ],
  "estimation_notes": [
    "Payment integration increases QA scope",
    "AI assistant should be validated in a separate discovery phase"
  ]
}
```

---

# 29. Технический стек

Для Budget Soft логично сделать так:

## Frontend

```text
React / Next.js
TypeScript
Tailwind CSS
```

## Backend

```text
Laravel 11/12
PHP 8.3+
MySQL / PostgreSQL
Redis
Queue jobs
```

## AI

```text
OpenAI API / Claude API
Structured JSON output
Prompt templates
```

## PDF

```text
wkhtmltopdf / Puppeteer / Browsershot
```

## Email

```text
SMTP / Mailgun / SendGrid
```

## Admin

```text
Laravel Nova / Filament / custom admin panel
```

Для быстрого MVP я бы выбрал:

```text
Laravel + Filament + React/Next.js
```

или даже:

```text
Laravel + Inertia + React + Filament
```

---

# 30. База данных

## Таблица `estimation_sessions`

```text
id
uuid
status
project_type
project_description
complexity_level
risk_level
confidence_level
total_hours_min
total_hours_max
total_price_min
total_price_max
currency
created_at
updated_at
```

---

## Таблица `estimation_answers`

```text
id
session_id
question_key
question_text
answer_value
answer_label
created_at
```

---

## Таблица `estimation_modules`

```text
id
session_id
module_key
module_name
backend_hours_min
backend_hours_max
frontend_hours_min
frontend_hours_max
qa_hours_min
qa_hours_max
devops_hours_min
devops_hours_max
created_at
```

---

## Таблица `estimation_leads`

```text
id
session_id
name
email
phone
telegram
company
website
budget_range
start_timeframe
message
status
created_at
updated_at
```

---

## Таблица `estimation_settings`

```text
id
key
value
type
created_at
updated_at
```

---

## Таблица `estimation_rate_cards`

```text
id
role
hourly_rate
currency
is_active
created_at
updated_at
```

---

# 31. API endpoints

## Public API

```text
POST /api/estimation/session/start
POST /api/estimation/session/{uuid}/answer
POST /api/estimation/session/{uuid}/analyze
GET  /api/estimation/session/{uuid}/result
POST /api/estimation/session/{uuid}/lead
GET  /api/estimation/session/{uuid}/pdf
```

---

## Admin API

```text
GET    /api/admin/estimations
GET    /api/admin/estimations/{id}
PATCH  /api/admin/estimations/{id}/status
GET    /api/admin/settings
PATCH  /api/admin/settings
GET    /api/admin/rate-cards
PATCH  /api/admin/rate-cards
```

---

# 32. MVP-версия

Для первой версии не нужно делать всё.

## MVP должен включать:

1. Лендинг калькулятора.
2. Анкету на 15–20 вопросов.
3. Базовый rule-based расчет.
4. AI summary.
5. Сбор контактов.
6. Результат на экране.
7. Отправку результата на email.
8. Простую админку лидов.
9. Настройку hourly rate.
10. PDF-отчет.

---

# 33. Что не делать в MVP

Не нужно сразу делать:

* сложный drag-and-drop конструктор вопросов;
* личный кабинет клиента;
* оплату;
* интеграцию с CRM;
* сложную аналитику;
* мультиязычность;
* полностью AI-generated estimate без правил;
* слишком длинную анкету на 50+ вопросов.

---

# 34. Оптимальный MVP-flow

```text
Step 1: Project type
Step 2: Project stage
Step 3: Platforms
Step 4: User roles
Step 5: Key features
Step 6: Integrations
Step 7: Design status
Step 8: AI features
Step 9: Timeline and budget
Step 10: Contact details
Step 11: Result
```

---

# 35. Пример вопросов для MVP

## Question 1

```text
Что вы хотите разработать?
```

Варианты:

```text
Website
Online store
Marketplace
CRM
SaaS
Mobile app
AI tool
Internal business system
Other
```

---

## Question 2

```text
На какой стадии проект?
```

Варианты:

```text
Only idea
Short description
Detailed specification
Design ready
Existing product
Need to rebuild old system
```

---

## Question 3

```text
Какие платформы нужны?
```

Варианты:

```text
Web
Mobile responsive
iOS
Android
Admin panel
API
Telegram bot
```

---

## Question 4

```text
Какие функции нужны?
```

Варианты:

```text
Authentication
User profiles
Dashboard
Catalog
Search
Filters
Orders
Payments
Subscriptions
Notifications
Chat
Reports
File upload
Admin panel
Analytics
```

---

## Question 5

```text
Нужны ли интеграции?
```

Варианты:

```text
Payment provider
CRM
ERP
Email
SMS
Telegram
Google services
AI API
External API
Not sure
```

---

## Question 6

```text
Нужны ли AI-функции?
```

Варианты:

```text
No
AI chat
Document analysis
Knowledge base search
Text generation
Image generation
Workflow automation
Not sure
```

---

## Question 7

```text
Есть ли готовый дизайн?
```

Варианты:

```text
No
Wireframes only
Figma ready
Need UI/UX design
Need redesign
```

---

## Question 8

```text
Когда хотите запустить проект?
```

Варианты:

```text
ASAP
1–2 months
3–6 months
6+ months
Just researching
```

---

## Question 9

```text
Какой бюджет рассматриваете?
```

Варианты:

```text
< €5,000
€5,000–€10,000
€10,000–€25,000
€25,000–€50,000
€50,000+
Not sure
```

---

# 36. Важная UX-деталь

Не нужно показывать пользователю сразу “слишком дорого”.

Лучше писать так:

```text
Ваш проект можно запустить в формате MVP от 320–480 часов.
Полная версия может потребовать 700–1100 часов.
```

Это психологически лучше, чем просто:

```text
Ваш проект стоит €40,000.
```

---

# 37. Защита от плохих оценок

Калькулятор обязан показывать дисклеймер:

```text
Это предварительная автоматическая оценка. Точная стоимость зависит от деталей бизнес-логики, дизайна, интеграций и технических ограничений. Финальная оценка формируется после короткого discovery-звонка.
```

---

# 38. Ключевая фишка

Самая сильная фишка — не просто “цена”, а **разбивка на MVP и Full Version**.

Пример:

```text
Recommended MVP:
- Authorization
- User dashboard
- Core business flow
- Admin panel
- Basic reports

Move to Phase 2:
- AI assistant
- Advanced analytics
- Mobile app
- Complex integrations
```

Это делает компанию похожей не на исполнителя “за деньги”, а на партнера, который помогает оптимизировать бюджет.

---

# 39. Вторая сильная фишка

**AI-generated project brief**

После анкеты клиент получает:

```text
Based on your answers, your project can be described as:

A B2B SaaS platform with user accounts, subscription payments, admin panel, reporting module and AI-powered document analysis. The MVP should focus on authentication, dashboard, document upload, AI summary and admin moderation.
```

Это можно использовать как начало нормального ТЗ.

---

# 40. Третья сильная фишка

**Lead scoring**

Система должна автоматически оценивать качество лида.

Пример:

```text
Lead score: 82/100
```

Факторы:

```text
+30 оставил email
+20 бюджет €10k+
+15 есть готовое ТЗ
+10 хочет начать в течение месяца
+10 корпоративный email
-20 бюджет меньше минимального
-15 “just researching”
```

В админке менеджер сразу видит, кому стоит писать первым.

---

# 41. Email клиенту

После расчета клиент получает письмо:

```text
Subject: Your software development estimate is ready

Hi {{name}},

Based on your answers, your project is estimated at:

MVP: {{mvp_hours_min}}–{{mvp_hours_max}} hours
Full version: {{full_hours_min}}–{{full_hours_max}} hours

The main cost drivers are:
- {{driver_1}}
- {{driver_2}}
- {{driver_3}}

We recommend starting with MVP and validating the core business logic first.

You can download your PDF estimate here:
{{pdf_link}}

Best regards,
Budget Soft team
```

---

# 42. Email менеджеру

```text
Subject: New estimate request: {{project_type}}, {{hours}}h, {{budget}}

New lead submitted a project estimation request.

Name: {{name}}
Email: {{email}}
Company: {{company}}
Project type: {{project_type}}
Estimated hours: {{hours_min}}–{{hours_max}}
Budget: {{budget_range}}
Start timeframe: {{start_timeframe}}
Lead score: {{lead_score}}

Project summary:
{{ai_summary}}

Main risks:
{{risks}}

Admin link:
{{admin_url}}
```

---

# 43. SEO-структура страницы

Страница должна содержать SEO-блоки:

## H1

```text
Калькулятор стоимости разработки ПО
```

## H2

```text
Как рассчитывается стоимость разработки?
Сколько часов нужно на разработку MVP?
Что влияет на цену?
Почему точная оценка невозможна без discovery?
Сколько стоит разработка CRM?
Сколько стоит разработка SaaS?
Сколько стоит разработка мобильного приложения?
```

---

# 44. SEO FAQ

Добавить FAQ:

```text
Сколько стоит разработка CRM?
Сколько стоит разработка MVP?
Почему разработка приложения стоит дорого?
Можно ли точно оценить проект без ТЗ?
Сколько часов занимает разработка интернет-магазина?
Что входит в стоимость разработки?
Как снизить бюджет разработки?
Что дороже: web-приложение или мобильное приложение?
```

---

# 45. Метрики

Нужно отслеживать:

```text
Visitors
Started questionnaire
Completed questionnaire
Left email
Downloaded PDF
Booked call
Average estimated budget
Average project type
Drop-off by step
Most selected features
Lead score distribution
```

---

# 46. Возможные риски продукта

## Риск 1: калькулятор дает слишком низкую оценку

Решение:

* использовать диапазоны;
* добавлять risk buffer;
* показывать disclaimer;
* не обещать фиксированную цену.

## Риск 2: пользователь пугается высокой цены

Решение:

* показывать MVP отдельно;
* объяснять, что можно запускать поэтапно;
* предлагать бесплатную консультацию.

## Риск 3: AI придумывает неадекватные часы

Решение:

* не доверять AI финальный расчет;
* AI только классифицирует и объясняет;
* расчет делает rule-based engine.

## Риск 4: анкета слишком длинная

Решение:

* 10–15 обязательных вопросов;
* остальные динамически;
* прогресс-бар;
* возможность вставить описание проекта.

---

# 47. Оценка разработки самого калькулятора

## MVP

```text
Frontend questionnaire: 40–70h
Backend estimation engine: 50–90h
AI integration: 30–60h
PDF generation: 20–40h
Email sending: 10–20h
Admin leads panel: 30–60h
Settings/rates: 20–40h
QA: 30–50h
DevOps: 10–25h

Итого: 240–455 часов
```

## Хорошая версия

```text
Dynamic questionnaire: 80–160h
Advanced estimation engine: 100–200h
AI project analysis: 60–140h
PDF customization: 40–90h
Admin settings: 80–160h
Lead scoring: 30–70h
Analytics: 40–100h
CRM integration: 30–100h
QA: 80–160h

Итого: 540–1180 часов
```

---

# 48. Лучший вариант для запуска

Я бы делал так:

## Версия 1

* 15 вопросов;
* 8 типов проектов;
* 20–30 типовых модулей;
* расчет по правилам;
* AI summary;
* PDF;
* заявки в админке.

## Версия 2

* текстовое ТЗ → AI-анализ;
* динамические вопросы;
* lead scoring;
* CRM integration;
* мультиязычность.

## Версия 3

* полноценный конструктор оценки;
* история оценок;
* личный кабинет клиента;
* сравнение MVP / Full / Enterprise;
* автоматическая генерация коммерческого предложения.

---

# 49. Главное продуктовое решение

Калькулятор должен продавать не “дешевую разработку”, а **экспертную оценку**.

Плохой вариант:

```text
Ответьте на вопросы и узнайте цену.
```

Хороший вариант:

```text
Получите предварительную техническую оценку: часы, сроки, команда, риски и MVP-рекомендации.
```

---

# 50. Короткое резюме ТЗ

Нужно разработать web-калькулятор, который:

1. Собирает данные о проекте через анкету.
2. Анализирует ответы с помощью правил и AI.
3. Раскладывает проект на модули.
4. Считает часы по ролям.
5. Показывает диапазон стоимости.
6. Делит оценку на MVP и Full version.
7. Генерирует PDF-отчет.
8. Собирает лиды.
9. Передает менеджеру структурированную заявку.
10. Позволяет администратору менять ставки, коэффициенты и вопросы.

Главная фишка: **не просто калькулятор цены, а AI-помощник, который превращает идею клиента в предварительное техническое описание проекта и реалистичную оценку разработки.**
