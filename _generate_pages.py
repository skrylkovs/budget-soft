#!/usr/bin/env python3
"""Generate inner pages in stoimost-style layout. Run: python3 _generate_pages.py"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).parent

SERVICE_PRICING = {
    "razrabotka-erp-sistem": {
        "price": "От 1 500 000 руб. (расчитывается индивидуально под масштаб бизнеса)",
        "terms": "От 2.5 до 6 месяцев",
        "payment_steps": [
            "30% — Предоплата, аналитика и ТЗ",
            "30% — Разработка основного функционала",
            "40% — Финальное тестирование, деплой и передача прав",
        ],
    },
    "razrabotka-crm-sistem": {
        "price": "От 800 000 руб. (зависит от количества интеграций и архитектуры)",
        "terms": "От 1.5 до 3 месяцев",
        "payment_steps": [
            "30% — Предоплата, проектирование воронки и User Flow",
            "30% — Интеграция, кастомизация и настройка ИИ-скриптов",
            "40% — Тестирование на реальных лидах, обучение и запуск",
        ],
    },
    "kiberbezopasnost": {
        "price": "От 600 000 руб. (включая аудит и выстраивание контура DevSecOps)",
        "terms": "От 1 до 2.5 месяцев",
        "payment_steps": [
            "30% — Предоплата, комплексный аудит инфраструктуры и выявление уязвимостей",
            "30% — Развертывание систем защиты, DLP и антифрод-модулей",
            "40% — Стресс-тесты (пентесты), симуляция атак и финальный деплой",
        ],
    },
    "iskusstvennyj-intellekt": {
        "price": "От 900 000 руб. (зависит от сложности LLM-моделей и объема данных для обучения)",
        "terms": "От 1 до 3 месяцев",
        "payment_steps": [
            "30% — Предоплата, сбор датасетов и проектирование логики агентов",
            "30% — Обучение моделей, интеграция API и настройка промпт-инжиниринга",
            "40% — Калибровка точности ответов, пилотный запуск и сдача",
        ],
    },
    "mobilnaya-razrabotka": {
        "price": "От 1 100 000 руб. (в зависимости от выбора стека: Native или Cross-platform)",
        "terms": "От 2 до 4 месяцев",
        "payment_steps": [
            "30% — Предоплата, создание интерактивных прототипов и UI/UX дизайна",
            "30% — Верстка интерфейсов, бэкенд-разработка и базовая сборка",
            "40% — Публикация в App Store / Google Play, отладка и передача исходников",
        ],
    },
    "importozameshchenie": {
        "price": "От 1 300 000 руб. (определяется сложностью архитектуры замещаемого ПО)",
        "terms": "От 2 до 5 месяцев",
        "payment_steps": [
            "30% — Предоплата, маппинг данных и проектирование суверенной архитектуры",
            "30% — Разработка независимых модулей и перенос баз данных (бекапы)",
            "40% — Финальное переключение систем, нагрузочные тесты и сдача проекта",
        ],
    },
}

SERVICES = [
    (
        "razrabotka-erp-sistem",
        "ERP-системы",
        "Кастомные ERP-системы: Единый цифровой мозг и интеллектуальный центр управления предприятием",
        """<p>Классический подход к управлению предприятием изживает себя: бесконечные таблицы Excel, разрозненный софт в разных отделах и постоянная ручная сверка данных приводят к критическим ошибкам и потере прибыли. M-SOFT IT предлагает принципиально новое решение — проектирование и разработку кастомных ERP-систем полного цикла, которые объединяют все бизнес-процессы компании в единую, бесшовно функционирующую экосистему. Мы создаем комплексные цифровые платформы для управления ресурсами, финансовыми потоками, цепочками поставок, закупками, производственными мощностями и персоналом.</p>
<p>Благодаря нашему фирменному AI-Native подходу, внедряемая ERP-система перестает быть просто пассивным хранилищем бухгалтерских и складских записей. Она превращается в активного интеллектуального ассистента топ-менеджмента. Система непрерывно анализирует исторические данные и рыночные тренды, позволяя с высокой точностью прогнозировать кассовые разрывы, автоматически оптимизировать объемы запасов на складах под сезонный спрос и самостоятельно формировать сложные консолидированные отчеты для инвесторов или регуляторов. Вы получаете абсолютную прозрачность каждого процесса и тотальный контроль над компанией в режиме реального времени, построенный на базе самых передовых Enterprise-технологий.</p>""",
    ),
    (
        "razrabotka-crm-sistem",
        "CRM-системы",
        "Умные CRM-системы: Интеллектуальная автоматизация продаж и бесшовное ИИ-сопровождение клиентов",
        """<p>Современный бизнес больше не может позволить себе тратить ресурсы на CRM-системы, которые работают как простые цифровые записные книжки. Эффективное решение должно не просто фиксировать контакты, а активно и автономно помогать вашей команде продавать. Команда M-SOFT IT специализируется на проектировании высоконагруженных кастомных CRM-решений, а также на глубокой кастомизации и бесшовной интеграции ведущих международных и локальных платформ, таких как Salesforce, Creatio и SAP. Мы адаптируем интерфейсы и логику системы строго под уникальный цикл продаж вашей индустрии.</p>
<p>Главное конкурентное преимущество наших CRM-систем — усиление классического функционала встроенными автономными ИИ-агентами. ИИ полностью берет на себя рутину: он детально помнит историю взаимодействий с каждым контрагентом, мгновенно распознает скрытый контекст и эмоциональный окрас в переписке или телефонных разговорах, автоматически квалифицирует лиды и самостоятельно подсказывает менеджеру идеальный момент для совершения звонка или отправки персонализированного коммерческого предложения. Исключая человеческий фактор, забытые заявки и ошибки менеджеров на всех этапах воронки, наши умные CRM-системы обеспечивают кратный и прогнозируемый рост конверсии и лояльности клиентов.</p>""",
    ),
    (
        "kiberbezopasnost",
        "Кибербезопасность",
        "Cybersecurity & DevSecOps: Комплексная защита данных, транзакций и критической ИТ-инфраструктуры",
        """<p>В эпоху тотальной цифровизации и стремительного развития ИИ безопасность корпоративных данных становится главным условием выживания и стабильности любого масштабируемого бизнеса. Направление информационной безопасности в M-SOFT IT охватывает полный цикл защиты enterprise-предприятий от современных цифровых угроз. Мы начинаем с проведения глубокого технологического аудита ваших текущих систем, выявляя скрытые уязвимости, после чего внедряем строгие международные протоколы DevSecOps непосредственно в конвейер разработки программного обеспечения. Это означает, что безопасность закладывается в ваш софт еще на этапе написания первых строк кода.</p>
<p>Мы проектируем отказоустойчивую архитектуру с максимальной защитой от внешних атак и внутренних утечек (DLP). Наши специалисты настраивают интеллектуальные системы контроля и разграничения доступа, включая современные биометрические решения и интеграцию со сложными системами СКУД на объектах. Для финтех-проектов, маркетплейсов и e-commerce платформ мы разворачиваем кастомные автоматизированные антифрод-системы на базе машинного обучения, которые выявляют подозрительную активность пользователей за миллисекунды. С M-SOFT IT ваши коммерческие тайны, финансовые транзакции и персональные данные миллионов клиентов находятся под непрерывным автоматизированным контролем 24/7/365.</p>""",
    ),
    (
        "iskusstvennyj-intellekt",
        "Внедрение ИИ",
        "AI Agent Workflows: Проектирование и интеграция автономных ИИ-агентов в бизнес-архитектуру",
        """<p>Мы не занимаемся поверхностным подключением готовых публичных нейросетей — мы полностью перестраиваем операционную архитектуру ваших бизнес-процессов с помощью прикладного искусственного интеллекта. M-SOFT IT разрабатывает, обучает и внедряет кастомные связки многоагентных ИИ-систем (AI Agents), которые способны автономно выполнять роли реальных квалифицированных сотрудников: от операторов клиентской поддержки первой и второй линии до менеджеров по закупкам, финансовых аудиторов, контент-мейкеров и системных аналитиков.</p>
<p>Наш технологический стек в сфере AI включает в себя интеллектуальное распознавание и извлечение данных из любых документов (OCR), создание предиктивных математических моделей в рамках Data Science & Machine Learning для прогнозирования спроса и рисков, а также внедрение систем компьютерного зрения (Computer Vision) для автоматического контроля качества на производстве или в логистике. Кроме того, мы создаем продвинутых Telegram-ботов нового поколения со встроенными платежными шлюзами и полноценным ИИ-сопровождением пользователя. Передав рутинные, аналитические и текстовые операции автономным агентам, вы сможете сократить операционные расходы компании на порядок, одновременно повысив скорость выполнения задач в десятки раз.</p>""",
    ),
    (
        "mobilnaya-razrabotka",
        "Мобильная разработка",
        "Мобильная разработка Enterprise-уровня: Высокопроизводительные приложения для iOS и Android",
        """<p>Мобильное приложение сегодня — это ключевой инструмент взаимодействия с клиентом и критически важный узел управления внутренними бизнес-процессами компании. Мы создаем безопасные, легко масштабируемые мобильные продукты с интуитивно понятным, современным UX/UI дизайном и глубокой встроенной ИИ-аналитикой поведения пользователей. M-SOFT IT предлагает клиентам как классическую нативную разработку (Swift для iOS, Kotlin для Android) для проектов с максимальными требованиями к производительности, так и кроссплатформенные решения на базе Flutter и React Native, позволяющие запустить продукт на обеих операционных системах в кратчайшие сроки с единой кодовой базой.</p>
<p>Мы обладаем глубокой экспертизой в разработке масштабных m-Commerce проектов с бесшовной интеграцией платежных хабов, биометрии и динамических систем лояльности. Наша команда регулярно создает специализированные Enterprise-приложения для автоматизации работы выездных сотрудников, оптимизации логистических цепочек (TMS-системы, умный GPS-трекинг флота), высокотехнологичной медицины (телемедицинские платформы, интеграция с электронными медицинскими картами EHR), а также комплексные интерфейсы для мониторинга и удаленного управления IoT-устройствами и промышленным оборудованием.</p>""",
    ),
]

SCREENS: dict[str, tuple[str, str]] = {
    "stoimost": ("cases/saas.png", "Скриншот SaaS-платформы"),
    "razrabotka-erp-sistem": ("cases/digital-twin.png", "Скриншот цифрового двойника производства"),
    "razrabotka-crm-sistem": ("cases/ecommerce.png", "Скриншот e-commerce платформы"),
    "kiberbezopasnost": ("cases/biometrics.png", "Скриншот системы биометрической аутентификации"),
    "iskusstvennyj-intellekt": ("cases/saas.png", "Скриншот SaaS-платформы сбора данных"),
    "mobilnaya-razrabotka": ("cases/wallet.png", "Скриншот мобильного криптокошелька"),
    "importozameshchenie": ("cases/digital-twin.png", "Скриншот цифрового двойника производства"),
}

WORKFLOW_STEPS = [
    (
        "Экспертная консультация",
        "Мы не просто принимаем заказ, а погружаемся в ваш бизнес. Проводим интервью, выявляем скрытые потребности и анализируем конкурентную среду.",
        "Чёткое понимание целей проекта и первичный концепт решения.",
    ),
    (
        "Стратегическое планирование и оценка",
        "Подбор оптимального технологического стека, формирование команды и расчёт бюджета. Мы выбираем модель сотрудничества (Fixed Price или Time & Material).",
        "Детальное коммерческое предложение с графиком платежей и таймлайном проекта.",
    ),
    (
        "Проектирование и UI/UX дизайн",
        "Создание логической структуры (User Flow) и интерактивных прототипов. Мы визуализируем продукт до того, как будет написана первая строчка кода.",
        "Согласованный визуальный стиль и кликабельный прототип будущего ПО.",
    ),
    (
        "Техническая архитектура и ТЗ",
        "Глубокая проработка технической документации. Мы описываем логику работы базы данных, интеграции с внешними сервисами и требования к безопасности.",
        "Полное Техническое Задание (Blueprint), исключающее двусмысленность при разработке.",
    ),
    (
        "Итеративная разработка (Agile Development)",
        "Создание продукта короткими циклами (спринтами). Вы видите прогресс каждые две недели на демонстрациях и можете вносить корректировки в процессе.",
        "Работающий функционал, готовый к тестированию.",
    ),
    (
        "Контроль качества (Quality Assurance)",
        "Многоуровневое тестирование: функциональное, нагрузочное и проверка на уязвимости. Мы гарантируем стабильность работы при любых сценариях.",
        "Продукт без багов, полностью соответствующий ТЗ.",
    ),
    (
        "Релиз, внедрение и поддержка",
        "Развёртывание системы на серверах, обучение ваших сотрудников и первичный сбор обратной связи. После запуска мы продолжаем мониторинг 24/7.",
        "Успешно работающее решение и уверенность в его технической стабильности.",
    ),
]

SPEED_ROWS = [
    ("Discovery & Оценка", "2–4 дня"),
    ("Прототипирование (UI/UX)", "5–7 дней"),
    ("Запуск MVP (Первая версия)", "от 21 дня"),
    ("Полноценный релиз", "от 2 месяцев"),
]

USLUGI_CATALOG = [
    (
        "1. Корпоративные и управленческие системы (Enterprise Solutions)",
        [
            "<strong>ERP-системы (Enterprise Resource Planning):</strong> Комплексное управление ресурсами, финансами и производством.",
            "<strong>CRM-системы:</strong> Кастомные решения и внедрение платформ (Salesforce, Creatio, SAP).",
            "<strong>SCM (Supply Chain Management):</strong> Автоматизация цепочек поставок, складского учёта и инвентаризации.",
            "<strong>HRM & Talent Management:</strong> ПО для подбора, оценки, обучения и управления персоналом.",
            "<strong>DMS & ECM (Document Management):</strong> Системы документооборота с ИИ-распознаванием (OCR) и классификацией.",
            "<strong>Asset & Equipment Management:</strong> Мониторинг состояния активов и промышленного оборудования.",
            "<strong>Risk & Compliance:</strong> Контроль соответствия регуляторным нормам, аудит безопасности и управление рисками.",
            "<strong>Voucher & Loyalty Management:</strong> Системы управления программами лояльности и внутренними ваучерами.",
        ],
    ),
    (
        "2. Веб-разработка (Web Development & Engineering)",
        [
            "<strong>Корпоративные сайты и порталы:</strong> Высоконагруженные представительства бизнеса и инфо-порталы.",
            "<strong>SaaS-платформы (Software as a Service):</strong> Облачное ПО с многопользовательской архитектурой и подписками.",
            "<strong>B2B/B2C Личные кабинеты:</strong> Защищённые порталы для самообслуживания клиентов, дилеров и партнёров.",
            "<strong>PWA (Progressive Web Apps):</strong> Веб-приложения, работающие как нативные мобильные (с оффлайн-режимом).",
            "<strong>CMS Development:</strong> Кастомные системы управления контентом (Headless CMS, Strapi, WordPress).",
            "<strong>API Architecture:</strong> Проектирование и разработка REST/GraphQL API для сложных интеграций.",
            "<strong>Streaming & Media:</strong> Сервисы для трансляции видео и аудио контента в реальном времени.",
        ],
    ),
    (
        "3. Мобильная разработка (Mobile App Development)",
        [
            "<strong>Нативная разработка (iOS & Android):</strong> Высокопроизводительные приложения на Swift и Kotlin.",
            "<strong>Кроссплатформенная разработка:</strong> Создание приложений на Flutter и React Native с единой кодовой базой.",
            "<strong>m-Commerce:</strong> Мобильные магазины с интеграцией Apple/Google Pay и систем лояльности.",
            "<strong>Enterprise Mobile Apps:</strong> Мобильные инструменты для сотрудников (склад, логистика, выездные специалисты).",
            "<strong>IoT Mobile Interfaces:</strong> Пульты управления для умных устройств и промышленного оборудования.",
            "<strong>Location-based Services:</strong> Приложения с GPS-трекингом, навигацией и геофенсингом.",
        ],
    ),
    (
        "4. Финтех и Электронная коммерция (Fintech & E-commerce)",
        [
            "<strong>Интернет-магазины и Маркетплейсы:</strong> Торговые площадки с автоматизацией биллинга и вендорскими кабинетами.",
            "<strong>Blockchain & DeFi:</strong> Смарт-контракты, dApps, криптокошельки и частные блокчейн-сети.",
            "<strong>Платёжные шлюзы:</strong> Разработка и интеграция защищённых систем эквайринга и транзакций.",
            "<strong>Investment & Trading Platforms:</strong> Торговые терминалы, личные кабинеты инвесторов и ИИ-скоринг.",
            "<strong>Insurance Management (InsurTech):</strong> Автоматизация полисов и прогнозирование страховых претензий.",
        ],
    ),
    (
        "5. Индустриальные и вертикальные решения (Verticals)",
        [
            "<strong>Healthcare (MedTech):</strong> Системы управления клиниками (HIS), EHR/EMR, телемедицина.",
            "<strong>Logistics & Transportation:</strong> Управление перевозками (TMS), трекинг флота и оптимизация маршрутов.",
            "<strong>Construction & Real Estate:</strong> ПО для моделирования (CAD), тендерные площадки и системы недвижимости (MLS).",
            "<strong>Energy & Utilities:</strong> Управление коммунальными сетями, солнечной/ветряной энергетикой и отходами.",
            "<strong>Agriculture (AgroTech):</strong> Агро-аналитика, ПО для дронов и мониторинга полей.",
            "<strong>Manufacturing (Industry 4.0):</strong> Системы MES, SCADA и автоматизация производственных линий.",
        ],
    ),
    (
        "6. Данные, ИИ и Визуальные технологии (Data & Visual)",
        [
            "<strong>BI & Big Data:</strong> Сбор, хранение и глубокая аналитика больших массивов данных.",
            "<strong>Data Science & Machine Learning:</strong> Прогнозные модели и системы автоматического принятия решений.",
            "<strong>Computer Vision:</strong> Распознавание лиц, объектов и интеллектуальный контроль качества.",
            "<strong>AR/VR:</strong> Иммерсивные решения для обучения, маркетинга и промышленности.",
            "<strong>GIS:</strong> Геоинформационные системы, картография и 3D-маппинг.",
        ],
    ),
    (
        "7. Инфраструктура, Безопасность и Инновации",
        [
            "<strong>AI Agent Workflows:</strong> Разработка автономных ИИ-агентов для полной автоматизации бизнес-процессов.",
            "<strong>Cloud Development & Migration:</strong> Проектирование и перенос инфраструктуры в облака (AWS, Azure, GCP).",
            "<strong>Cybersecurity & DevSecOps:</strong> Защита данных, аудит безопасности и интеграция защиты в цикл разработки.",
            "<strong>Legacy Modernization:</strong> Рефакторинг и «спасение» устаревших ИТ-систем.",
            "<strong>IoT & Edge Computing:</strong> Управление сетями умных устройств и датчиков.",
            "<strong>QA Automation:</strong> Автоматизированное тестирование для обеспечения качества 24/7.",
        ],
    ),
    (
        "8. Интеграция с оборудованием и IoT",
        [
            "<strong>Торговое и POS-оборудование:</strong> Интеграция с фискальными регистраторами, сканерами штрих-кодов, терминалами эквайринга и весами.",
            "<strong>Системы контроля и управления доступом (СКУД):</strong> ПО для работы с биометрией, считывателями карт и контроллерами турникетов.",
            "<strong>Промышленное оборудование:</strong> Разработка ПО для взаимодействия с датчиками, станками (ЧПУ) и программируемыми логическими контроллерами (ПЛК).",
            "<strong>Медицинское и лабораторное оборудование:</strong> Съём и обработка данных с диагностических аппаратов.",
        ],
    ),
    (
        "9. Работа с данными и системные утилиты",
        [
            "<strong>Парсеры и системы сбора данных:</strong> Автоматический мониторинг цен, сбор информации из государственных реестров или соцсетей.",
            "<strong>Инструменты миграции данных:</strong> Разработка ПО для переноса информации между несовместимыми базами данных.",
            "<strong>RPA (Роботизация процессов):</strong> Программные роботы, имитирующие действия пользователя в интерфейсах старых программ, где нет API.",
        ],
    ),
    (
        "10. Прикладная автоматизация и экосистемы (Частные случаи)",
        [
            "<strong>Решения на базе 1С:</strong> Создание внешних обработок и сложных отчётов. Синхронизация 1С с интернет-магазинами, CRM и складскими системами.",
            "<strong>Расширения для офисного ПО: Excel / Google Sheets:</strong> Сложные макросы (VBA), надстройки VSTO, скрипты автоматизации отчётности и финансового анализа.",
            "<strong>Браузерные расширения:</strong> Кастомные плагины для автоматизации работы в веб-интерфейсах, парсинга данных или модификации сторонних сервисов под нужды компании.",
        ],
    ),
]


def rel_prefix(depth: int) -> str:
    return "../" * depth if depth else "./"


def page_href(prefix: str, slug: str) -> str:
    if not slug:
        return prefix
    return f"{prefix}{slug}/"


def render_workflow() -> str:
    items = []
    for idx, (title, process, result) in enumerate(WORKFLOW_STEPS, start=1):
        items.append(
            f"""<li>
  <strong>{idx}. {title}</strong>
  <p><span class="page-workflow__label">Что происходит</span> {process}</p>
  <p class="page-workflow__result"><span class="page-workflow__label">Результат</span> {result}</p>
</li>"""
        )
    return f'<ol class="page-workflow reveal">{"".join(items)}</ol>'


def render_service_pricing_table(pricing: dict) -> str:
    steps = "".join(f"<li>{step}</li>" for step in pricing["payment_steps"])
    payment_cell = f"""<strong>Поэтапный (30% / 30% / 40%):</strong>
<ul class="page-service-table__list">
{steps}
</ul>"""
    return f"""<div class="page-service-table reveal">
  <table class="page-service-table__table">
    <thead>
      <tr>
        <th scope="col">Параметр</th>
        <th scope="col">Условия и детали</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Цена</th>
        <td>{pricing["price"]}</td>
      </tr>
      <tr>
        <th scope="row">Сроки</th>
        <td>{pricing["terms"]}</td>
      </tr>
      <tr>
        <th scope="row">Формат оплаты</th>
        <td>{payment_cell}</td>
      </tr>
    </tbody>
  </table>
</div>"""


def render_speed_table() -> str:
    rows = "".join(
        f"""<div class="compare__row">
  <div class="compare__cell compare__cell--label">{stage}</div>
  <div class="compare__cell compare__cell--ai">{term}</div>
</div>"""
        for stage, term in SPEED_ROWS
    )
    return f"""<div class="compare reveal page-speed-table">
  <div class="compare__head">
    <div class="compare__head-cell compare__head-cell--label">Этап</div>
    <div class="compare__head-cell compare__head-cell--ai">Срок</div>
  </div>
  {rows}
</div>"""


def render_stoimost_compare() -> str:
    return """<div class="compare reveal">
  <div class="compare__head">
    <div class="compare__head-cell compare__head-cell--label">Параметр</div>
    <div class="compare__head-cell compare__head-cell--legacy">
      <span class="compare__tag compare__tag--legacy">MVP и чёткое ТЗ</span>
      Fixed Price
    </div>
    <div class="compare__head-cell compare__head-cell--ai">
      <span class="compare__tag compare__tag--ai">Крупные проекты</span>
      Time &amp; Material
    </div>
  </div>
  <div class="compare__row">
    <div class="compare__cell compare__cell--label">Модель оплаты</div>
    <div class="compare__cell compare__cell--legacy">Фиксированная стоимость и чёткие рамки проекта</div>
    <div class="compare__cell compare__cell--ai">Оплата по факту выполнения задач</div>
  </div>
  <div class="compare__row">
    <div class="compare__cell compare__cell--label">Когда выбирать</div>
    <div class="compare__cell compare__cell--legacy">MVP и продукты с детально прописанным ТЗ</div>
    <div class="compare__cell compare__cell--ai">Динамичные проекты с гибкими изменениями в процессе</div>
  </div>
  <div class="compare__row">
    <div class="compare__cell compare__cell--label">Прозрачность бюджета</div>
    <div class="compare__cell compare__cell--legacy">Сумма и сроки фиксируются до старта работ</div>
    <div class="compare__cell compare__cell--ai">Бюджет масштабируется вместе с приоритетами</div>
  </div>
  <div class="compare__row">
    <div class="compare__cell compare__cell--label">Контроль результата</div>
    <div class="compare__cell compare__cell--legacy">Приёмка по согласованному scope и KPI</div>
    <div class="compare__cell compare__cell--ai">Итерации каждые 2 недели с демо и отчётами</div>
  </div>
</div>"""


def render_uslugi_catalog() -> str:
    sections = []
    for heading, items in USLUGI_CATALOG:
        lis = "".join(f"<li>{item}</li>" for item in items)
        sections.append(f"<section><h3>{heading}</h3><ul>{lis}</ul></section>")
    return f'<div class="page-services-catalog reveal">{"".join(sections)}</div>'


def render_screen_card(prefix: str, image: str, alt: str) -> str:
    return f"""<div class="page-screen-card bento-showcase__card bento-showcase__card--lg reveal">
  <figure class="page-screen-card__shot">
    <img src="{prefix}{image}" alt="{alt}" loading="lazy">
  </figure>
</div>"""


def render_submenu(prefix: str) -> str:
    items = [
        ("uslugi/razrabotka-erp-sistem", "ERP-системы", '<path d="M4 21V7l8-4 8 4v14M4 21h16M9 21V12h6v9M9 8h.01M12 8h.01M15 8h.01" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>'),
        ("uslugi/razrabotka-crm-sistem", "CRM-системы", '<path d="M3 3v18h18M7 14l4-4 4 4 5-5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>'),
        ("uslugi/kiberbezopasnost", "Кибербезопасность", '<path d="M12 2l8 4v6c0 5-3.5 9-8 10-4.5-1-8-5-8-10V6l8-4z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"></path>'),
        ("uslugi/iskusstvennyj-intellekt", "Внедрение ИИ", '<path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2M12 8a4 4 0 100 8 4 4 0 000-8z" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path>'),
        ("uslugi/mobilnaya-razrabotka", "Мобильная разработка", '<rect x="7" y="2" width="10" height="20" rx="2" stroke="currentColor" stroke-width="1.6"></rect><path d="M11 18h2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path>'),
        ("uslugi", "Все услуги", '<path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path>'),
    ]
    links = []
    for slug, label, icon_path in items:
        links.append(
            f"""<a class="submenu__link" href="{page_href(prefix, slug)}" role="menuitem">
  <span class="submenu__icon">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">{icon_path}</svg>
  </span>
  <span>{label}</span>
</a>"""
        )
    return f'<div class="submenu" role="menu">{"".join(links)}</div>'


def render_clients_strip(prefix: str) -> str:
    return f"""    <section class="clients-strip" data-fab-theme="light">
      <div class="container">
        <div class="clients-strip__card">
          <div class="directions reveal" role="list">
            <a class="direction" href="{page_href(prefix, 'uslugi/razrabotka-erp-sistem')}" role="listitem">
              <span class="direction__icon">
                <svg width="60" height="60" viewBox="0 0 60 60" fill="none" aria-hidden="true">
                  <rect x="10" y="10" width="30" height="30" rx="2" stroke="currentColor" stroke-width="1.6"/>
                  <rect x="22" y="22" width="30" height="30" rx="2" fill="#fff" stroke="currentColor" stroke-width="1.6"/>
                </svg>
              </span>
              <span class="direction__label">ERP-системы</span>
            </a>
            <a class="direction" href="{page_href(prefix, 'uslugi/razrabotka-crm-sistem')}" role="listitem">
              <span class="direction__icon">
                <svg width="60" height="60" viewBox="0 0 60 60" fill="none" aria-hidden="true">
                  <circle cx="30" cy="30" r="22" stroke="currentColor" stroke-width="1.6"/>
                  <text x="30" y="34" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="currentColor">CRM</text>
                </svg>
              </span>
              <span class="direction__label">CRM-системы</span>
            </a>
            <a class="direction" href="{page_href(prefix, 'uslugi/kiberbezopasnost')}" role="listitem">
              <span class="direction__icon">
                <svg width="60" height="60" viewBox="0 0 60 60" fill="none" aria-hidden="true">
                  <path d="M30 8 L48 14 L48 28 C48 40 40 48 30 52 C20 48 12 40 12 28 L12 14 Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>
                  <circle cx="30" cy="27" r="3" stroke="currentColor" stroke-width="1.6"/>
                  <path d="M30 30 L30 38" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
                </svg>
              </span>
              <span class="direction__label">Кибербезопасность</span>
            </a>
            <a class="direction" href="{page_href(prefix, 'uslugi/iskusstvennyj-intellekt')}" role="listitem">
              <span class="direction__icon">
                <svg width="60" height="60" viewBox="0 0 60 60" fill="none" aria-hidden="true">
                  <path d="M28 12 C22 10 16 13 15 19 C10 21 10 27 14 30 C11 34 14 40 19 40 C20 45 27 46 28 41 L28 12 Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>
                  <path d="M28 20 L28 33" stroke="currentColor" stroke-width="1.6"/>
                  <path d="M32 16 L40 16" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
                  <circle cx="44" cy="16" r="2.5" stroke="currentColor" stroke-width="1.6"/>
                  <path d="M32 26 L38 26 L38 32" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
                  <circle cx="42" cy="32" r="2.5" stroke="currentColor" stroke-width="1.6"/>
                  <path d="M38 32 L39.5 32" stroke="currentColor" stroke-width="1.6"/>
                  <path d="M32 38 L40 38 L40 44" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
                  <circle cx="44" cy="44" r="2.5" stroke="currentColor" stroke-width="1.6"/>
                  <path d="M40 44 L41.5 44" stroke="currentColor" stroke-width="1.6"/>
                </svg>
              </span>
              <span class="direction__label">Внедрение ИИ</span>
            </a>
            <a class="direction" href="{page_href(prefix, 'uslugi/mobilnaya-razrabotka')}" role="listitem">
              <span class="direction__icon">
                <svg width="60" height="60" viewBox="0 0 60 60" fill="none" aria-hidden="true">
                  <rect x="18" y="8" width="24" height="44" rx="3" stroke="currentColor" stroke-width="1.6"/>
                  <rect x="22" y="20" width="4" height="4" stroke="currentColor" stroke-width="1.4"/>
                  <rect x="28" y="20" width="4" height="4" stroke="currentColor" stroke-width="1.4"/>
                  <rect x="34" y="20" width="4" height="4" stroke="currentColor" stroke-width="1.4"/>
                  <rect x="22" y="26" width="4" height="4" stroke="currentColor" stroke-width="1.4"/>
                  <rect x="28" y="26" width="4" height="4" stroke="currentColor" stroke-width="1.4"/>
                  <rect x="34" y="26" width="4" height="4" stroke="currentColor" stroke-width="1.4"/>
                  <rect x="22" y="32" width="4" height="4" stroke="currentColor" stroke-width="1.4"/>
                  <rect x="28" y="32" width="4" height="4" stroke="currentColor" stroke-width="1.4"/>
                  <rect x="34" y="32" width="4" height="4" stroke="currentColor" stroke-width="1.4"/>
                </svg>
              </span>
              <span class="direction__label">Мобильные приложения</span>
            </a>
            <a class="direction" href="{page_href(prefix, 'importozameshchenie')}" role="listitem">
              <span class="direction__icon">
                <svg width="60" height="60" viewBox="0 0 60 60" fill="none" aria-hidden="true">
                  <circle cx="28" cy="32" r="18" stroke="currentColor" stroke-width="1.6"/>
                  <ellipse cx="28" cy="32" rx="8" ry="18" stroke="currentColor" stroke-width="1.6"/>
                  <path d="M10 32 L46 32" stroke="currentColor" stroke-width="1.6"/>
                  <path d="M40 14 C44 10 49 10 51 14" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" fill="none"/>
                  <path d="M51 14 L48 11 M51 14 L48 17" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </span>
              <span class="direction__label">Импортозамещение</span>
            </a>
          </div>
          <div class="clients-strip__divider" aria-hidden="true" hidden></div>
          <p class="clients-strip__caption" hidden>Нам доверяют</p>
          <div class="clients-strip__logos" hidden>
            <div class="clients-strip__logo"><img src="{prefix}logos/pzu.svg" alt="PZU logo" loading="lazy"></div>
            <div class="clients-strip__logo"><img src="{prefix}logos/truststamp.svg" alt="TrustStamp logo" loading="lazy"></div>
            <div class="clients-strip__logo"><img src="{prefix}logos/crescent.svg" alt="Crescent logo" loading="lazy"></div>
            <div class="clients-strip__logo"><img src="{prefix}logos/alephzero.svg" alt="Aleph Zero logo" loading="lazy"></div>
            <div class="clients-strip__logo"><img src="{prefix}logos/qenta.webp" alt="Qenta logo" loading="lazy"></div>
          </div>
        </div>
      </div>
    </section>"""


def render_header(prefix: str, active: str) -> str:
    def nav_link(slug: str, label: str) -> str:
        cls = "nav__link is-active" if active == slug else "nav__link"
        return f'<li class="nav__item"><a class="{cls}" href="{page_href(prefix, slug)}">{label}</a></li>'

    services_active = active == "uslugi" or active.startswith("uslugi/") or active in {s[0] for s in SERVICES}
    services_cls = "nav__link is-active" if services_active else "nav__link"

    return f"""  <header class="header" id="siteHeader">
    <div class="container header__inner">
      <a href="{prefix}" class="logo" aria-label="BUDGET SOFT — на главную">
        <img src="{prefix}logos/budget-soft.svg" alt="BUDGET SOFT" class="logo__img">
      </a>
      <nav class="nav" aria-label="Основная навигация">
        <ul class="nav__list">
          <li class="nav__item nav__item--has-submenu">
            <button class="{services_cls}" aria-haspopup="true" aria-expanded="false">
              Услуги
              <svg class="nav__chevron" width="10" height="6" viewBox="0 0 10 6" fill="none" aria-hidden="true">
                <path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>
              </svg>
            </button>
            {render_submenu(prefix)}
          </li>
          {nav_link("portfolio", "Портфолио")}
          {nav_link("etapy", "Этапы реализации")}
          {nav_link("sroki", "Сроки")}
          {nav_link("garantii", "Гарантии")}
        </ul>
      </nav>
      <div class="header__actions">
        <button type="button" class="btn btn--primary btn--sm js-open-contact">ОБСУДИТЬ ПРОЕКТ</button>
        <button class="burger" id="burgerBtn" aria-label="Открыть меню" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
    <div class="mobile-menu" id="mobileMenu">
      <a href="{page_href(prefix, 'uslugi')}" class="mobile-menu__link">Услуги</a>
      <a href="{page_href(prefix, 'portfolio')}" class="mobile-menu__link">Портфолио</a>
      <a href="{page_href(prefix, 'etapy')}" class="mobile-menu__link">Этапы реализации</a>
      <a href="{page_href(prefix, 'sroki')}" class="mobile-menu__link">Сроки</a>
      <a href="{page_href(prefix, 'garantii')}" class="mobile-menu__link">Гарантии</a>
      <button type="button" class="btn btn--primary mobile-menu__cta js-open-contact">Обсудить проект</button>
    </div>
  </header>"""


def render_hero(prefix: str, second_btn: tuple[str, str] | None = None) -> str:
    second = ""
    if second_btn:
        href, label = second_btn
        second = f"""
            <a href="{href}" class="btn btn--outline btn--lg">{label}</a>"""
    return f"""    <section class="hero" data-fab-theme="dark">
      <div class="hero__bg" aria-hidden="true">
        <video class="hero__video" autoplay muted loop playsinline>
          <source src="{prefix}hero-background.webm" type="video/webm">
        </video>
        <div class="hero__overlay"></div>
      </div>
      <div class="container hero__inner">
        <div class="hero__content reveal">
          <h1 class="hero__title">
            Разрабатываем ПО любой сложности для <span class="text-gradient">автоматизации бизнеса</span>
          </h1>
          <div class="hero__actions">
            <button type="button" class="btn btn--primary btn--lg js-open-contact">
              Обсудить проект
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>
            </button>{second}
          </div>
        </div>
      </div>
    </section>"""


def render_revolution(
    *,
    eyebrow: str,
    title_html: str,
    lead: str,
    content: str,
    section_id: str = "",
    accent: str = "",
) -> str:
    id_attr = f' id="{section_id}"' if section_id else ""
    accent_html = f'\n          <p class="section-accent">{accent}</p>' if accent else ""
    return f"""    <section class="revolution"{id_attr} data-fab-theme="light">
      <div class="container">
        <div class="section-head reveal">
          <span class="section-rule"></span>
          <span class="eyebrow">{eyebrow}</span>
          <h2 class="section-title">{title_html}</h2>
          <p class="section-lead">{lead}</p>{accent_html}
        </div>
        {content}
      </div>
    </section>"""


def render_cta(prefix: str) -> str:
    return f"""    <section class="cta cta--simple" id="cta" data-fab-theme="light">
      <div class="container">
        <div class="cta__card cta__inner cta__inner--centered">
          <div class="cta__text">
            <h2 class="section-title section-title--light">Следующий прорыв на рынке может быть <span class="text-gradient">вашим</span>. Давайте воплотим это в жизнь.</h2>
            <a href="{page_href(prefix, 'kontakty')}" class="btn btn--primary btn--lg cta__submit">Связаться с нами</a>
          </div>
        </div>
      </div>
    </section>"""


def render_footer(prefix: str) -> str:
    footer_service_links = "".join(
        f"<li><a href=\"{page_href(prefix, f'uslugi/{slug}')}\">{label}</a></li>"
        for slug, label, _, _ in SERVICES
    )
    return f"""  <footer class="footer" data-fab-theme="dark">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__col footer__col--brand">
          <a href="{prefix}" class="logo logo--footer">
            <img src="{prefix}logos/budget-soft.svg" alt="BUDGET SOFT" class="logo__img">
          </a>
          <p class="footer__tagline">Разработка ПО для бизнеса. Импортозамещение и автоматизация.</p>
          <ul class="footer__contacts">
            <li><a href="tel:+74950000000">+7 (495) 000-00-00</a></li>
            <li><a href="mailto:info@budget-soft.ru">info@budget-soft.ru</a></li>
            <li><span>Москва</span></li>
          </ul>
        </div>
        <div class="footer__col">
          <h4 class="footer__title">Услуги</h4>
          <ul class="footer__links">
            {footer_service_links}
            <li><a href="{page_href(prefix, 'uslugi')}" class="footer__links-all">Все услуги →</a></li>
          </ul>
        </div>
        <div class="footer__col">
          <h4 class="footer__title">Компания</h4>
          <ul class="footer__links">
            <li><a href="{page_href(prefix, 'importozameshchenie')}">Импортозамещение</a></li>
            <li><a href="{page_href(prefix, 'portfolio')}">Портфолио</a></li>
            <li><a href="{page_href(prefix, 'stoimost')}">Стоимость</a></li>
            <li><a href="{page_href(prefix, 'o-nas')}">О нас</a></li>
            <li><a href="{page_href(prefix, 'kontakty')}">Контакты</a></li>
          </ul>
        </div>
        <div class="footer__col">
          <h4 class="footer__title">Ресурсы</h4>
          <ul class="footer__links">
            <li><a href="{page_href(prefix, 'etapy')}">Этапы реализации</a></li>
            <li><a href="{page_href(prefix, 'sroki')}">Сроки</a></li>
            <li><a href="{page_href(prefix, 'garantii')}">Гарантии</a></li>
            <li><a href="{page_href(prefix, 'blog')}" class="footer__links-soon">Блог <span class="badge-soon">скоро</span></a></li>
          </ul>
        </div>
      </div>
      <div class="footer__bottom">
        <div class="footer__copy">© 2026 BUDGET SOFT</div>
        <div class="footer__legal"><a href="{page_href(prefix, 'privacy')}">Политика конфиденциальности</a></div>
      </div>
    </div>
  </footer>"""


def render_contact_modal() -> str:
    return """  <div class="contact-modal" id="contactModal" hidden>
    <div class="contact-modal__backdrop" data-close-contact></div>
    <div class="contact-modal__panel" role="dialog" aria-modal="true" aria-labelledby="contactModalTitle">
      <button class="contact-modal__close" type="button" aria-label="Закрыть" data-close-contact>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"></path></svg>
      </button>
      <h2 class="contact-modal__title" id="contactModalTitle">Обсудить проект</h2>
      <p class="contact-modal__lead">Свяжитесь с нами любым удобным способом — ответим в ближайшее время.</p>
      <ul class="contact-modal__list">
        <li><strong>Телефон:</strong> <a href="tel:+74950000000">+7 (495) 000-00-00</a></li>
        <li><strong>Email:</strong> <a href="mailto:info@budget-soft.ru">info@budget-soft.ru</a></li>
        <li><strong>Telegram:</strong> <a href="https://t.me/" target="_blank" rel="noopener">Написать в Telegram</a></li>
        <li><strong>Офис:</strong> Москва</li>
      </ul>
    </div>
  </div>"""


def render_tail(prefix: str) -> str:
    return f"""{render_contact_modal()}

  <div class="cookie" id="cookie" role="dialog" aria-label="Согласие на использование cookie" hidden>
    <p class="cookie__text">Мы используем cookie, чтобы сайт работал лучше.</p>
    <div class="cookie__actions">
      <button class="btn btn--outline btn--sm" id="cookieDecline" type="button">Отклонить</button>
      <button class="btn btn--primary btn--sm" id="cookieAccept" type="button">Принять</button>
    </div>
  </div>

  <a class="messenger-fab" href="https://t.me/" target="_blank" rel="noopener" aria-label="Написать в Telegram">
    <svg width="26" height="26" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M21.5 4.5L2 12l6 2 2 6 4-4 6 5 1.5-16.5z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"></path></svg>
  </a>

  <script src="{prefix}script.js"></script>"""


def render_page(
    *,
    depth: int,
    title: str,
    active: str,
    eyebrow: str,
    title_html: str,
    lead: str,
    content: str,
    section_id: str = "",
    accent: str = "",
    second_btn: tuple[str, str] | None = None,
) -> str:
    p = rel_prefix(depth)
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{p}styles.css">
  <link rel="stylesheet" href="{p}page.css">
</head>
<body class="page-body page-inner">
{render_header(p, active)}
  <main>
{render_hero(p, second_btn)}
{render_clients_strip(p)}
{render_revolution(eyebrow=eyebrow, title_html=title_html, lead=lead, content=content, section_id=section_id, accent=accent)}
{render_cta(p)}
  </main>
{render_footer(p)}
{render_tail(p)}
</body>
</html>"""


def content_etapy() -> str:
    return render_workflow()


def content_sroki() -> str:
    bullets = """<ul class="page-list reveal">
<li><strong>Мгновенный старт (On-Demand Scaling):</strong> Благодаря обширному ресурсному пулу и отлаженным HR-процессам, мы формируем и выводим команду на проект в течение 2–3 рабочих дней. Вам не нужно ждать, пока освободятся специалисты.</li>
<li><strong>AI-Native Engineering:</strong> Мы используем ИИ-агентов для автоматизации рутинного кодинга, генерации тестов и создания документации. Это позволяет нашим инженерам фокусироваться на архитектуре и логике, ускоряя производство кода в 2–3 раза.</li>
<li><strong>Слаженная экосистема разработки:</strong> Использование готовых внутренних библиотек и микросервисных шаблонов позволяет нам не писать базовые функции с нуля, а собирать фундамент проекта за считанные часы.</li>
<li><strong>Параллельные спринты:</strong> Наши процессы выстроены так, что проектирование, дизайн и разработка бэкенда идут одновременно. Мы сокращаем «мёртвые зоны» ожидания между этапами до минимума.</li>
</ul>
<h3 class="page-subsection__title reveal">Наши стандарты скорости</h3>
"""
    return bullets + render_speed_table() + """
<blockquote class="timeline__benefit reveal">«Пока конкуренты пишут ТЗ, вы уже тестируете первую версию продукта на реальных пользователях».</blockquote>"""


def content_garantii() -> str:
    return """<div class="page-prose reveal">
<h3>1. Юридическая и Интеллектуальная защита</h3>
<ul class="page-list page-list--cards">
<li><strong>Полная передача прав (IP Ownership):</strong> Согласно договору, 100% прав на исходный код, документацию и интеллектуальную собственность переходят к вам сразу после завершения работ.</li>
<li><strong>Строгий NDA (Конфиденциальность):</strong> Мы подписываем соглашение о неразглашении на этапе первых переговоров. Ваша бизнес-логика и данные защищены юридически.</li>
</ul>
<h3>2. Технологические гарантии (Quality Assurance)</h3>
<ul class="page-list page-list--cards">
<li><strong>Гарантийный период:</strong> После релиза мы предоставляем период бесплатной технической поддержки для устранения любых выявленных скрытых дефектов.</li>
<li><strong>SLA (Service Level Agreement):</strong> Мы фиксируем параметры доступности и скорости реакции в соглашении об уровне сервиса. Вы всегда знаете, когда задача будет выполнена.</li>
</ul>
<h3>3. Безопасность данных и инфраструктуры</h3>
<ul class="page-list page-list--cards">
<li><strong>Соответствие стандартам:</strong> Разработка ведётся с учётом международных стандартов безопасности (ISO, GDPR, HIPAA — в зависимости от ниши).</li>
<li><strong>Безопасный цикл разработки (DevSecOps):</strong> Мы интегрируем проверку уязвимостей на каждом этапе написания кода, минимизируя риски взлома.</li>
</ul>
<h3>4. Гарантия прозрачности (Operational Transparency)</h3>
<ul class="page-list page-list--cards">
<li><strong>Регулярная отчётность:</strong> Вы получаете доступ к системе управления проектами (Jira/ClickUp) и видите прогресс в режиме реального времени.</li>
<li><strong>Демо-сессии:</strong> Каждые две недели мы демонстрируем работающий функционал, чтобы вы могли убедиться в соответствии продукта вашим ожиданиям.</li>
</ul>
</div>"""


def content_stoimost(prefix: str) -> str:
    return render_stoimost_compare() + render_screen_card(prefix, *SCREENS["stoimost"]) + """
<div class="page-outro reveal">
  <p>Свяжитесь с нами, и наш эксперт рассчитает точный бюджет проекта под ваши задачи уже в рамках первичного планирования.</p>
  <button type="button" class="btn btn--primary btn--lg js-open-contact">Получить расчёт</button>
</div>"""


def content_prose(
    body: str,
    prefix: str,
    screen_key: str | None = None,
    pricing_key: str | None = None,
) -> str:
    body = body.replace("{home}", prefix.rstrip("/") or ".")
    screen = ""
    if screen_key and screen_key in SCREENS:
        screen = render_screen_card(prefix, *SCREENS[screen_key])
    pricing = ""
    if pricing_key and pricing_key in SERVICE_PRICING:
        pricing = render_service_pricing_table(SERVICE_PRICING[pricing_key])
    return f'<div class="page-prose reveal">{body}</div>{pricing}{screen}'


def write_page(path: Path, html: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print(f"  {path.relative_to(ROOT)}")


def main() -> None:
    print("Generating pages…")

    pages_depth1 = [
        {
            "slug": "etapy",
            "title": "Этапы реализации — BUDGET SOFT",
            "active": "etapy",
            "eyebrow": "Workflow",
            "title_html": 'Этапы реализации <span class="text-gradient">вашего проекта</span>',
            "lead": "Мы не просто принимаем заказ — выстраиваем прозрачный процесс от первой консультации до релиза и поддержки.",
            "content_fn": lambda p: content_etapy(),
        },
        {
            "slug": "sroki",
            "title": "Сроки — BUDGET SOFT",
            "active": "sroki",
            "eyebrow": "Time-to-Market",
            "title_html": 'От идеи до запуска — за <span class="text-gradient">недели, а не месяцы</span>',
            "lead": "Мы пересмотрели классический подход к разработке, чтобы ваш бизнес получал технологическое преимущество в кратчайшие сроки.",
            "accent": "За счёт чего мы работаем быстрее рынка?",
            "content_fn": lambda p: content_sroki(),
            "section_id": "speed",
        },
        {
            "slug": "garantii",
            "title": "Гарантии — BUDGET SOFT",
            "active": "garantii",
            "eyebrow": "Risk Mitigation",
            "title_html": 'Гарантии и <span class="text-gradient">безопасность</span>',
            "lead": "Мы берём на себя полную ответственность за результат и обеспечиваем многоуровневую защиту ваших интересов.",
            "content_fn": lambda p: content_garantii(),
        },
        {
            "slug": "stoimost",
            "title": "Стоимость — BUDGET SOFT",
            "active": "stoimost",
            "eyebrow": "Стоимость",
            "title_html": 'Новая математика <span class="text-gradient">вашей разработки</span>',
            "lead": "Благодаря полной автоматизации рутинного написания кода и автоматическому контролю качества QA 24/7, мы радикально сократили внутренние издержки. В BUDGET SOFT вы платите исключительно за готовый результат, архитектуру и интеллект, а не за оплату сотен человеко-часов legacy-команд.",
            "accent": "Снижение издержек в 10 раз — без компромиссов по качеству.",
            "content_fn": content_stoimost,
            "section_id": "pricing",
            "second_btn": ("#pricing", "Рассчитать стоимость"),
        },
        {
            "slug": "importozameshchenie",
            "title": "Импортозамещение — BUDGET SOFT",
            "active": "importozameshchenie",
            "eyebrow": "Legacy Modernization",
            "title_html": 'Legacy Modernization: <span class="text-gradient">независимое ПО</span>',
            "lead": "Безопасный и бесшовный переход на кастомное независимое ПО без потери данных и простоя.",
            "content_fn": lambda p: content_prose(
                """<h3>Legacy Modernization: Безопасный и бесшовный переход на кастомное независимое ПО</h3>
<p>Массовый уход зарубежных ИТ-вендоров, отзыв лицензий и постоянные риски внезапных блокировок софта ставят под угрозу непрерывность работы крупных предприятий. M-SOFT IT предлагает комплексную услугу глубокой модернизации, рефакторинга и пересборки устаревших или ставших небезопасными зарубежных ИТ-систем (Legacy Modernization). Мы помогаем бизнесу полностью избавиться от вендорозависимости и перейти на суверенную, контролируемую ИТ-архитектуру без потери накопленных данных и падения эффективности.</p>
<p>Мы разрабатываем с нуля независимые облачные SaaS-платформы, проектируем кастомные CRM и ERP-решения, полностью принадлежащие вашей компании, а также создаем отказоустойчивые интеграции со всеми конфигурациями систем 1С (автоматическая синхронизация со сложными складами, CRM-модулями и внешними маркетплейсами). Весь процесс миграции данных в защищенные контуры и новые базы данных осуществляется нашими инженерами в фоновом режиме по строгим регламентам. Мы гарантируем, что переход на новое независимое ПО пройдет абсолютно незаметно для ваших сотрудников и не вызовет ни одной секунды простоя в ключевых бизнес-процессах организации.</p>""",
                p,
                "importozameshchenie",
                "importozameshchenie",
            ),
            "second_btn": ("#content", "Подробнее"),
        },
        {
            "slug": "o-nas",
            "title": "О нас — BUDGET SOFT",
            "active": "o-nas",
            "eyebrow": "О компании",
            "title_html": 'Мы отменили разработку <span class="text-gradient">«прошлого века»</span>',
            "lead": "В 2025–2026 годах мы полностью реформировали классический подход к созданию программного обеспечения.",
            "content_fn": lambda p: content_prose(
                """<p>Традиционные громоздкие ИТ-команды из множества менеджеров, фронтенд-, бэкенд-разработчиков и тестировщиков — это медленно, неэффективно и неоправданно дорого.</p>
<p>Эпоха раздутых штатов закончилась. Наступила эра ИИ-дирижеров.</p>
<p>Специалисты BUDGET SOFT — это проджект-менеджеры с глубочайшей технической экспертизой, которые используют продвинутые ИИ-агенты как мультипликатор силы. Один человек у нас управляет целым пулом ИИ-разработчиков и заменяет стандартный ИТ-отдел.</p>
<p>Мы стерли границы доступности технологий: то, что раньше могли позволить себе только транснациональные корпорации с миллионными бюджетами, сегодня мы быстро и доступно внедряем для малого и среднего бизнеса.</p>""",
                p,
            ),
        },
        {
            "slug": "kontakty",
            "title": "Контакты — BUDGET SOFT",
            "active": "kontakty",
            "eyebrow": "Контакты",
            "title_html": 'Начните цифровую революцию <span class="text-gradient">вашего бизнеса</span>',
            "lead": "Готовы перевести компанию на AI-Native технологии и сократить расходы на разработку? Наши эксперты на связи.",
            "content_fn": lambda p: content_prose(
                """<p>Оставьте заявку прямо сейчас, и мы подготовим первичный концепт решения и расчёт бюджета для вашего проекта.</p>
<ul class="page-contacts">
<li><strong>Телефон:</strong> <a href="tel:+74950000000">+7 (495) 000-00-00</a></li>
<li><strong>Email:</strong> <a href="mailto:info@budget-soft.ru">info@budget-soft.ru</a></li>
<li><strong>Telegram:</strong> <a href="https://t.me/" target="_blank" rel="noopener">Написать в Telegram</a></li>
<li><strong>Офис:</strong> Москва</li>
</ul>
<p><button type="button" class="btn btn--primary btn--lg js-open-contact">Обсудить проект</button></p>""",
                p,
            ),
        },
        {
            "slug": "portfolio",
            "title": "Портфолио — BUDGET SOFT",
            "active": "portfolio",
            "eyebrow": "Портфолио",
            "title_html": 'Наши <span class="text-gradient">проекты</span>',
            "lead": "Мы реализуем проекты для компаний из финтеха, логистики, ритейла и промышленности.",
            "content_fn": lambda p: content_prose(
                """<p>Подборка кейсов с главной страницы — отправная точка для знакомства с нашим опытом.</p>
<p><a class="page-inline-link" href="{home}#cases">Смотреть кейсы на главной →</a></p>""",
                p,
            ),
        },
        {
            "slug": "privacy",
            "title": "Политика конфиденциальности — BUDGET SOFT",
            "active": "privacy",
            "eyebrow": "Документы",
            "title_html": 'Политика <span class="text-gradient">конфиденциальности</span>',
            "lead": "Настоящая политика описывает порядок обработки персональных данных посетителей сайта BUDGET SOFT.",
            "content_fn": lambda p: content_prose(
                """<p>Мы собираем только те данные, которые вы добровольно передаёте при обращении к нам (имя, email, телефон, описание проекта). Данные используются исключительно для связи с вами и подготовки коммерческого предложения.</p>
<p>Мы не передаём персональные данные третьим лицам без вашего согласия, за исключением случаев, предусмотренных законодательством РФ.</p>
<p>По вопросам обработки данных: <a href="mailto:info@budget-soft.ru">info@budget-soft.ru</a>.</p>""",
                p,
            ),
        },
        {
            "slug": "blog",
            "title": "Блог — BUDGET SOFT",
            "active": "blog",
            "eyebrow": "Блог",
            "title_html": 'Материалы об <span class="text-gradient">AI-Native разработке</span>',
            "lead": "Раздел в разработке — скоро здесь появятся кейсы и технологические тренды.",
            "content_fn": lambda p: content_prose('<p class="page-soon">Раздел в разработке. Скоро здесь появятся материалы об AI-Native разработке, кейсах и технологических трендах.</p>', p),
        },
    ]

    for cfg in pages_depth1:
        slug = cfg["slug"]
        prefix = rel_prefix(1)
        html = render_page(
            depth=1,
            title=cfg["title"],
            active=cfg["active"],
            eyebrow=cfg["eyebrow"],
            title_html=cfg["title_html"],
            lead=cfg["lead"],
            content=cfg["content_fn"](prefix),
            section_id=cfg.get("section_id", slug),
            accent=cfg.get("accent", ""),
            second_btn=cfg.get("second_btn"),
        )
        write_page(ROOT / slug / "index.html", html)

    uslugi_prefix = rel_prefix(1)
    uslugi_html = render_page(
        depth=1,
        title="Услуги — BUDGET SOFT",
        active="uslugi",
        eyebrow="Услуги",
        title_html='Направления и <span class="text-gradient">услуги</span>',
        lead="Мы разрабатываем программное обеспечение на заказ для каждой функции предприятия.",
        content=render_uslugi_catalog(),
        section_id="services",
    )
    write_page(ROOT / "uslugi" / "index.html", uslugi_html)

    for slug, label, heading, body in SERVICES:
        prefix = rel_prefix(2)
        content = content_prose(f"<h3>{heading}</h3>{body}", prefix, slug, slug)
        html = render_page(
            depth=2,
            title=f"{label} — BUDGET SOFT",
            active=f"uslugi/{slug}",
            eyebrow=label,
            title_html=heading.split(":")[0] if ":" in heading else heading,
            lead=heading.split(":", 1)[1].strip() if ":" in heading else "",
            content=content,
            section_id=slug,
            second_btn=(page_href(rel_prefix(2), "stoimost"), "Рассчитать стоимость"),
        )
        write_page(ROOT / "uslugi" / slug / "index.html", html)

    stoimost_css = ROOT / "stoimost" / "stoimost.css"
    if stoimost_css.exists():
        stoimost_css.unlink()
        print(f"  deleted {stoimost_css.relative_to(ROOT)}")

    print("Done.")


if __name__ == "__main__":
    main()
