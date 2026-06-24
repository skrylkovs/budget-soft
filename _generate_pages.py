#!/usr/bin/env python3
"""Generate inner pages in stoimost-style layout. Run: python3 _generate_pages.py"""
from __future__ import annotations

import html
import json
import random
import re
from pathlib import Path

from _uslugi_data import (
    DIRECTION_ICONS,
    DIRECTION_STRIP_SLUGS,
    SERVICE_ICONS,
    parse_texts_uslugi,
    services_as_tuples,
)

ROOT = Path(__file__).parent

# Базовый абсолютный URL сайта (для canonical / Open Graph / sitemap).
SITE_URL = "https://budget-soft.ru"
OG_IMAGE = f"{SITE_URL}/aurora-team.png"
CONTACT_TELEGRAM = "https://t.me/skrylkovs"
CONTACT_WHATSAPP = "https://wa.me/66634340262"

# Yandex.Metrika (счётчик 110021925). Единый сниппет на все страницы сайта.
YANDEX_METRIKA_ID = "110021925"
YANDEX_METRIKA = """  <!-- Yandex.Metrika counter -->
  <script type="text/javascript">
    (function(m,e,t,r,i,k,a){
        m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
        m[i].l=1*new Date();
        for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
        k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)
    })(window, document,'script','https://mc.yandex.ru/metrika/tag.js?id=110021925', 'ym');

    ym(110021925, 'init', {ssr:true, webvisor:true, clickmap:true, ecommerce:"dataLayer", referrer: document.referrer, url: location.href, accurateTrackBounce:true, trackLinks:true});
  </script>
  <noscript><div><img src="https://mc.yandex.ru/watch/110021925" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
  <!-- /Yandex.Metrika counter -->
"""


def inject_metrika(html_doc: str) -> str:
    """Вставляет счётчик Яндекс.Метрики перед </head>. Идемпотентно."""
    if "mc.yandex.ru/metrika" in html_doc:
        return html_doc
    return html_doc.replace("</head>", YANDEX_METRIKA + "</head>", 1)

STATS_CASES_PARTIAL = (ROOT / "partials" / "stats-cases.html").read_text(encoding="utf-8")
# Разбиваем партиал на секцию stats и секцию cases: cases-блок нужен отдельно,
# чтобы синхронизировать его на index.html (там stats и cases — в разных местах).
_CASES_MARKER = '    <section class="cases"'
_STATS_PART, _CASES_PART_BODY = STATS_CASES_PARTIAL.split(_CASES_MARKER, 1)
CASES_PARTIAL = _CASES_MARKER + _CASES_PART_BODY

BTN_ARROW_SM = (
    '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="2" '
    'stroke-linecap="round" stroke-linejoin="round"></path></svg>'
)

_OFFICE_ADDRESSES = (
    "Москва, Пресненская наб., 12, БЦ «Меркурий», оф. 1804",
    "Москва, ул. Лесная, 43, стр. 1, оф. 712",
    "Москва, Ленинградский пр-т, 37, корп. 3, эт. 9",
    "Москва, ул. Бауманская, 11, стр. 8, оф. 402",
    "Москва, наб. Тараса Шевченко, 23А, башня «Запад», оф. 1507",
    "Москва, ул. Ордынка, 40, БЦ «Палаты Черкасских», оф. 305",
)
OFFICE_ADDRESS = random.choice(_OFFICE_ADDRESSES)

SERVICE_PRICING = {
    "razrabotka-erp-sistem": {
        "price": "От 300 000 руб. (расчитывается индивидуально под масштаб бизнеса)",
        "terms": "От 2.5 до 6 месяцев",
        "payment_steps": [
            "30% — Предоплата, аналитика и ТЗ",
            "30% — Разработка основного функционала",
            "40% — Финальное тестирование, деплой и передача прав",
        ],
    },
    "razrabotka-crm-sistem": {
        "price": "От 160 000 руб. (зависит от количества интеграций и архитектуры)",
        "terms": "От 1.5 до 3 месяцев",
        "payment_steps": [
            "30% — Предоплата, проектирование воронки и User Flow",
            "30% — Интеграция, кастомизация и настройка AI-скриптов",
            "40% — Тестирование на реальных лидах, обучение и запуск",
        ],
    },
    "iskusstvennyj-intellekt": {
        "price": "От 180 000 руб. (зависит от сложности LLM-моделей и объема данных для обучения)",
        "terms": "От 1 до 3 месяцев",
        "payment_steps": [
            "30% — Предоплата, сбор датасетов и проектирование логики агентов",
            "30% — Обучение моделей, интеграция API и настройка промпт-инжиниринга",
            "40% — Калибровка точности ответов, пилотный запуск и сдача",
        ],
    },
    "mobilnaya-razrabotka": {
        "price": "От 220 000 руб. (в зависимости от выбора стека: Native или Cross-platform)",
        "terms": "От 2 до 4 месяцев",
        "payment_steps": [
            "30% — Предоплата, создание интерактивных прототипов и UI/UX дизайна",
            "30% — Верстка интерфейсов, бэкенд-разработка и базовая сборка",
            "40% — Публикация в App Store / Google Play, отладка и передача исходников",
        ],
    },
}

_DEFAULT_SERVICE_PRICING = {
    "price": "Рассчитывается индивидуально под масштаб и сложность проекта",
    "terms": "От 1.5 до 6 месяцев",
    "payment_steps": [
        "30% — Предоплата, аналитика и проектирование",
        "30% — Разработка и интеграции",
        "40% — Тестирование, внедрение и передача прав",
    ],
}

SERVICE_PAGES = parse_texts_uslugi()
SERVICE_BY_SLUG = {p.slug: p for p in SERVICE_PAGES}
SERVICES = services_as_tuples()

for _slug in SERVICE_BY_SLUG:
    SERVICE_PRICING.setdefault(
        _slug,
        {
            **_DEFAULT_SERVICE_PRICING,
            "payment_steps": list(_DEFAULT_SERVICE_PRICING["payment_steps"]),
        },
    )
SERVICE_PRICING["it-autstaffing"] = {
    "price": "Оплата по Time & Materials (фактически отработанные часы)",
    "terms": "Вывод специалиста от 3 рабочих дней",
    "payment_steps": [
        "Ежемесячный отчёт по часам и задачам",
        "Прямое управление специалистом на стороне заказчика",
        "Юридическое оформление и налоги — на BUDGET SOFT",
    ],
}

# Сортировка по востребованности внедрения AI (2025–2026): финтех/IT → ритейл/промышленность → медицина → прочие услуги
AI_BUSINESS_DIRECTIONS = [
    ("it", "ИТ-компании и Digital-агентства"),
    ("insurance", "Страховые компании и брокеры"),
    ("mfo", "МФО и ломбарды"),
    ("ecommerce", "Интернет-магазины (e-Commerce)"),
    ("wholesale", "Оптовая торговля и дистрибуция"),
    ("industry", "Промышленные предприятия"),
    ("logistics", "Грузоперевозки и экспедирование"),
    ("medical", "Медцентры и клиники общего профиля"),
    ("dentistry", "Стоматология"),
    ("auto", "Автодилеры и автосервисы"),
    ("edtech", "Онлайн-образование (EdTech)"),
    ("legal", "Юридические и консалтинговые компании"),
    ("equipment", "Аренда спецтехники и оборудования"),
    ("realty", "Агентства недвижимости"),
    ("developer", "Застройщики (девелоперы)"),
    ("travel", "Турагентства и Event-индустрия"),
    ("beauty", "Салоны красоты и бьюти-индустрия"),
    ("construction", "Ремонтно-строительные компании"),
]

# Заголовок и lead блока «Отрасли» (title_main, title_sub, lead)
AI_DIRECTIONS_COPY: dict[str, tuple[str, str, str]] = {
    "uslugi": (
        "Разработка и AI",
        "для каждой сферы бизнеса",
        "От финтеха и e-commerce до промышленности и девелопмента — собираем стек под отраслевую специфику, а не под абстрактный «коробочный» продукт.",
    ),
    "razrabotka-erp-sistem": (
        "ERP-решения",
        "для вашей отрасли",
        "Внедряем единые контуры управления — производство, опт, логистика, девелопмент — с отраслевыми регламентами, KPI и интеграциями под вашу модель бизнеса.",
    ),
    "razrabotka-crm-sistem": (
        "CRM",
        "под цикл продаж отрасли",
        "Автоматизируем воронку и сопровождение клиентов в финтехе, B2B-услугах, ритейле и производстве — с AI-подсказками и сквозной аналитикой.",
    ),
    "iskusstvennyj-intellekt": (
        "Внедрение AI",
        "во все сферы бизнеса",
        "Внедряем агентов и автоматизацию с учётом отраслевой специфики — от медицины и ритейла до промышленности и девелопмента.",
    ),
    "mobilnaya-razrabotka": (
        "Мобильные продукты",
        "для вашей аудитории",
        "Создаём приложения для ритейла, финтеха, логистики, медицины и полевых команд — с UX и интеграциями под отраслевые сценарии.",
    ),
}

AI_DIRECTIONS_DEFAULT = (
    "Отрасли",
    "для вашего проекта",
    "Внедряем решения с учётом отраслевой специфики — от финтеха и ритейла до промышленности и медицины.",
)

SCREENS: dict[str, tuple[str, str]] = {
    "razrabotka-erp-sistem": ("cases/digital-twin.png", "Скриншот цифрового двойника производства"),
    "razrabotka-crm-sistem": ("cases/ecommerce.png", "Скриншот e-commerce платформы"),
    "iskusstvennyj-intellekt": ("cases/saas.png", "Скриншот SaaS-платформы сбора данных"),
    "mobilnaya-razrabotka": ("cases/wallet.png", "Скриншот мобильного криптокошелька"),
    "fintech": ("cases/biometrics.png", "Скриншот финтех-приложения"),
    "razrabotka-internet-magazinov": ("cases/ecommerce.png", "Скриншот интернет-магазина"),
    "blockchain-web3": ("cases/wallet.png", "Скриншот Web3-приложения"),
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
        "Техническая архитектура и техническое задание",
        "Глубокая проработка технической документации. Мы описываем логику работы базы данных, интеграции с внешними сервисами и требования к безопасности.",
        "Полное Техническое Задание (Blueprint), исключающее двусмысленность при разработке.",
    ),
    (
        "Итеративная разработка (Agile Development)",
        "Создаём продукт короткими спринтами по две недели. На каждом цикле вы получаете демо работающего функционала, доступ к трекеру задач и прозрачные метрики скорости команды. AI-агенты ускоряют рутинный кодинг и тесты, а инженеры фокусируются на архитектуре и бизнес-логике. Приоритеты можно менять между спринтами без остановки разработки.",
        "Рабочие сборки после каждого спринта, согласованный backlog и функционал, готовый к полноценному QA.",
    ),
    (
        "Контроль качества (Quality Assurance)",
        "Проводим функциональное, регрессионное и нагрузочное тестирование по сценариям из ТЗ. Встраиваем автотесты в CI/CD — критичные дефекты выявляются до выкладки на прод, а не после обращений пользователей.",
        "Протокол тестирования с зафиксированными кейсами и стабильная сборка, готовая к релизу и внедрению у заказчика.",
    ),
    (
        "Релиз, внедрение и поддержка",
        "Развёртывание системы на серверах, обучение ваших сотрудников и первичный сбор обратной связи. После запуска мы продолжаем мониторинг 24/7.",
        "Успешно работающее решение и уверенность в его технической стабильности.",
    ),
]

WORKFLOW_ACCENT_POOL = (
    "#6f4cff",
    "#5b8def",
    "#8b5cf6",
    "#6366f1",
    "#7c3aed",
    "#0ea5e9",
    "#10b981",
    "#ec4899",
    "#f59e0b",
    "#14b8a6",
    "#ef4444",
    "#a855f7",
    "#3b82f6",
    "#22c55e",
    "#06b6d4",
    "#e11d48",
    "#84cc16",
    "#d946ef",
)
_workflow_accents = list(WORKFLOW_ACCENT_POOL)
random.shuffle(_workflow_accents)
WORKFLOW_ACCENTS = _workflow_accents[: len(WORKFLOW_STEPS)]

WORKFLOW_ICONS = [
    '<path d="M7 9h10M7 13h6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><path d="M5 4h14a2 2 0 012 2v11a2 2 0 01-2 2H9l-4 3v-3H5a2 2 0 01-2-2V6a2 2 0 012-2z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>',
    '<path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2" stroke="currentColor" stroke-width="1.6"/><path d="M9 5a2 2 0 014 0M12 11v4M10 13h4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>',
    '<rect x="4" y="4" width="16" height="16" rx="2" stroke="currentColor" stroke-width="1.6"/><path d="M8 12h8M12 8v8" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>',
    '<path d="M12 3l8 4v6c0 4.5-3.5 8-8 8s-8-3.5-8-8V7l8-4z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M9 12h6M12 9v6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>',
    '<path d="M8 8l-2 2 2 2M16 8l2 2-2 2M14 6l-4 12" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
    '<path d="M12 3l8 4v6c0 4.5-3.5 8-8 8s-8-3.5-8-8V7l8-4z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M9 12l2 2 4-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
    '<path d="M12 3c2 3 5 5 5 9a5 5 0 01-10 0c0-4 3-6 5-9z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M9 18h6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>',
]

SPEED_ROWS = [
    ("Discovery & Оценка", "2–4 дня"),
    ("Прототипирование (UI/UX)", "5–7 дней"),
    ("Запуск MVP (Первая версия)", "от 21 дня"),
    ("Полноценный релиз", "от 2 месяцев"),
]

TTM_METRICS = [
    ("2–3", "дня", "вывод команды на проект"),
    ("×2–3", "", "ускорение разработки кода"),
    ("21+", "день", "запуск MVP"),
]

TTM_PILLARS = [
    (
        "01",
        "Мгновенный старт",
        "On-Demand Scaling",
        "Благодаря ресурсному пулу и отлаженным HR-процессам формируем и выводим команду на проект за 2–3 рабочих дня — без ожидания «освободившихся» специалистов.",
    ),
    (
        "02",
        "AI-Native Engineering",
        "",
        "AI-агенты автоматизируют рутинный код, тесты и документацию — инженеры фокусируются на архитектуре и логике. Производство кода быстрее в 2–3 раза.",
    ),
    (
        "03",
        "Экосистема разработки",
        "",
        "Внутренние библиотеки и микросервисные шаблоны: базовый фундамент собирается за часы, а не пишется с нуля на каждом проекте.",
    ),
    (
        "04",
        "Параллельные спринты",
        "",
        "Проектирование, дизайн и бэкенд идут одновременно — «мёртвые зоны» между этапами сведены к минимуму.",
    ),
]

RISK_PAYMENT_SCHEME = "30% · 30% · 40%"

RISK_METRICS = [
    ("30", "%", "старт и проектирование"),
    ("30", "%", "разработка и демо"),
    ("40", "%", "приёмка и сдача"),
]

RISK_PILLAR_ICONS = {
    "legal": '<path d="M8 4h8v2H8V4zm0 14h8v2H8v-2zm-2-8h12v2H6v-2z" fill="currentColor"/>',
    "qa": '<path d="M12 3l8 4v6c0 5-3.5 9-8 10-4.5-1-8-5-8-10V7l8-4zm-1 10.2l5.4-5.4-1.4-1.4L11 12.4 8.4 9.8 7 11.2l4 4z" fill="currentColor"/>',
    "security": '<path d="M12 2l8 4v6c0 5-3.5 9-8 10-4.5-1-8-5-8-10V6l8-4zm0 3.2L7 8.1v3.9c0 3.6 2.2 6.8 5 7.8 2.8-1 5-4.2 5-7.8V8.1l-5-2.9z" fill="currentColor"/>',
    "transparency": '<path d="M12 4.5C7.86 4.5 4.5 7.86 4.5 12S7.86 19.5 12 19.5 19.5 16.14 19.5 12 16.14 4.5 12 4.5zm0 2.8c2.76 0 5 2.24 5 5s-2.24 5-5 5-5-2.24-5-5 2.24-5 5-5zm0 2.2a2.8 2.8 0 100 5.6 2.8 2.8 0 000-5.6z" fill="currentColor"/>',
}

RISK_PILLARS = [
    (
        "01",
        "Юридическая и интеллектуальная защита",
        "Legal & IP",
        "legal",
        "Согласно договору, 100% прав на исходный код, документацию и интеллектуальную собственность переходят к вам сразу после завершения работ. NDA подписываем на этапе первых переговоров — бизнес-логика и данные защищены юридически.",
    ),
    (
        "02",
        "Технологические гарантии",
        "Quality Assurance",
        "qa",
        "После релиза — период бесплатной технической поддержки для устранения скрытых дефектов. Параметры доступности и скорости реакции фиксируем в SLA: вы всегда знаете, когда задача будет выполнена.",
    ),
    (
        "03",
        "Безопасность данных и инфраструктуры",
        "Security",
        "security",
        "Разработка с учётом международных стандартов (ISO, GDPR, HIPAA — по нише). DevSecOps встроен в цикл: проверка уязвимостей на каждом этапе написания кода.",
    ),
    (
        "04",
        "Гарантия прозрачности",
        "Operational Transparency",
        "transparency",
        "Доступ к Jira или ClickUp — прогресс в режиме реального времени. Каждые две недели — демо работающего функционала, чтобы убедиться в соответствии продукта ожиданиям.",
    ),
]

RISK_COMMITMENTS = [
    ("IP Ownership", "100% прав на исходный код и документацию"),
    ("NDA", "Конфиденциальность с этапа переговоров"),
    ("Гарантийный период", "Бесплатное устранение скрытых дефектов после релиза"),
    ("SLA", "Фиксированные сроки реакции и доступности"),
    ("Стандарты", "ISO · GDPR · HIPAA — по нише проекта"),
    ("DevSecOps", "Проверка уязвимостей на каждом этапе разработки"),
    ("Отчётность", "Jira / ClickUp — прогресс в реальном времени"),
    ("Демо-сессии", "Работающий функционал каждые 2 недели"),
]

USLUGI_CATALOG = [
    (
        "1. Корпоративные и управленческие системы (Enterprise Solutions)",
        [
            "<strong>ERP-системы (Enterprise Resource Planning):</strong> Комплексное управление ресурсами, финансами и производством.",
            "<strong>CRM-системы:</strong> Кастомные решения и внедрение платформ (Salesforce, Creatio, SAP).",
            "<strong>SCM (Supply Chain Management):</strong> Автоматизация цепочек поставок, складского учёта и инвентаризации.",
            "<strong>HRM & Talent Management:</strong> ПО для подбора, оценки, обучения и управления персоналом.",
            "<strong>DMS & ECM (Document Management):</strong> Системы документооборота с AI-распознаванием (OCR) и классификацией.",
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
            "<strong>Investment & Trading Platforms:</strong> Торговые терминалы, личные кабинеты инвесторов и AI-скоринг.",
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
        "6. Данные, AI и Визуальные технологии (Data & Visual)",
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
            "<strong>AI Agent Workflows:</strong> Разработка автономных AI-агентов для полной автоматизации бизнес-процессов.",
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


def render_workflow_card(idx: int, title: str, process: str, result: str) -> str:
    icon = WORKFLOW_ICONS[idx - 1]
    accent = WORKFLOW_ACCENTS[idx - 1]
    return f"""<article class="page-workflow__card page-workflow__card--{idx}" style="--wf-accent: {accent}">
  <span class="page-workflow__glow" aria-hidden="true"></span>
  <span class="page-workflow__step">{idx:02d}</span>
  <header class="page-workflow__head">
    <span class="page-workflow__icon" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none">{icon}</svg></span>
    <h3 class="page-workflow__title">{title}</h3>
  </header>
  <div class="page-workflow__body">
    <div class="page-workflow__process">
      <span class="page-workflow__label">Что происходит</span>
      <p>{process}</p>
    </div>
    <div class="page-workflow__result">
      <span class="page-workflow__label">Результат</span>
      <p>{result}</p>
    </div>
  </div>
</article>"""


def render_workflow() -> str:
    cards = [
        render_workflow_card(idx, title, process, result)
        for idx, (title, process, result) in enumerate(WORKFLOW_STEPS, start=1)
    ]
    rows = [
        ("page-workflow__row--30", cards[0:3]),
        ("page-workflow__row--wide", cards[3:5]),
        ("page-workflow__row--half", cards[5:7]),
    ]
    row_html = "".join(
        f'<li class="page-workflow__row {row_cls}">{"".join(row_cards)}</li>'
        for row_cls, row_cards in rows
    )
    return f'<ol class="page-workflow page-workflow--layout reveal">{row_html}</ol>'


def render_service_pricing_table(pricing: dict, *, sidebar: bool = False) -> str:
    if sidebar:
        steps = "".join(
            f'<li class="page-spec__step"><span class="page-spec__step-num">{i:02d}</span>'
            f"<span>{step}</span></li>"
            for i, step in enumerate(pricing["payment_steps"], start=1)
        )
        return f"""<div class="page-spec">
  <div class="page-spec__head">
    <span class="page-spec__label">Коммерческие условия</span>
    <h3 class="page-spec__title">Условия проекта</h3>
  </div>
  <dl class="page-spec__metrics">
    <div class="page-spec__metric">
      <dt>Цена</dt>
      <dd>{pricing["price"]}</dd>
    </div>
    <div class="page-spec__metric">
      <dt>Сроки</dt>
      <dd>{pricing["terms"]}</dd>
    </div>
  </dl>
  <div class="page-spec__payment">
    <p class="page-spec__payment-label">Формат оплаты</p>
    <p class="page-spec__payment-format">Поэтапный · 30 / 30 / 40</p>
    <ol class="page-spec__steps">{steps}</ol>
  </div>
</div>"""

    steps = "".join(f"<li>{step}</li>" for step in pricing["payment_steps"])
    payment_cell = f"""<strong>Поэтапный (30% / 30% / 40%):</strong>
<ul class="page-service-table__list">
{steps}
</ul>"""
    return f"""<div class="page-service-table">
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


def render_ttm_content() -> str:
    metrics = "".join(
        f"""<div class="ttm-metric">
  <p class="ttm-metric__value">{val}{f'<span class="ttm-metric__unit">{unit}</span>' if unit else ""}</p>
  <p class="ttm-metric__label">{label}</p>
</div>"""
        for val, unit, label in TTM_METRICS
    )
    pillars = "".join(
        f"""<article class="ttm-pillar">
  <span class="ttm-pillar__index" aria-hidden="true">{index}</span>
  <h3 class="ttm-pillar__title">{title}{f'<span class="ttm-pillar__tag">{tag}</span>' if tag else ""}</h3>
  <p class="ttm-pillar__text">{text}</p>
</article>"""
        for index, title, tag, text in TTM_PILLARS
    )
    stages = "".join(
        f"""<div class="ttm-stage{" ttm-stage--highlight" if "MVP" in stage else ""}">
  <span class="ttm-stage__name">{stage}</span>
  <span class="ttm-stage__term">{term}</span>
</div>"""
        for stage, term in SPEED_ROWS
    )
    return f"""<div class="ttm">
  <div class="ttm-metrics reveal" aria-label="Ключевые показатели скорости">
{metrics}
  </div>
  <p class="ttm-kicker reveal">За счёт чего мы работаем быстрее рынка?</p>
  <div class="ttm-pillars reveal">
{pillars}
  </div>
  <div class="ttm-standards reveal" aria-labelledby="ttmStandardsTitle">
    <h3 class="ttm-standards__title" id="ttmStandardsTitle">Наши стандарты скорости</h3>
    <div class="ttm-standards__list">
{stages}
    </div>
  </div>
  <figure class="ttm-quote reveal">
    <blockquote>«Пока конкуренты пишут ТЗ, вы уже тестируете первую версию продукта на реальных пользователях».</blockquote>
  </figure>
</div>"""


def _risk_icon(icon_key: str) -> str:
    path = RISK_PILLAR_ICONS.get(icon_key, RISK_PILLAR_ICONS["legal"])
    return (
        f'<span class="risk-layer__icon" aria-hidden="true">'
        f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none">{path}</svg>'
        f"</span>"
    )


def render_risk_content() -> str:
    metrics = "".join(
        f"""<div class="risk-metric">
  <p class="risk-metric__value{" risk-metric__value--compact" if "·" in val else ""}">{val}{f'<span class="risk-metric__unit">{unit}</span>' if unit else ""}</p>
  <p class="risk-metric__label">{label}</p>
</div>"""
        for val, unit, label in RISK_METRICS
    )
    layers = "".join(
        f"""<article class="risk-layer">
  <span class="risk-layer__num" aria-hidden="true">{index}</span>
  <div class="risk-layer__body">
    <div class="risk-layer__head">
      {_risk_icon(icon_key)}
      <h3 class="risk-layer__title">{title}<span class="risk-layer__dot" aria-hidden="true">·</span><span class="risk-layer__tag">{tag}</span></h3>
    </div>
    <p class="risk-layer__text">{text}</p>
  </div>
</article>"""
        for index, title, tag, icon_key, text in RISK_PILLARS
    )
    commitments = "".join(
        f"""<div class="risk-contract__item">
  <span class="risk-contract__num" aria-hidden="true">{num:02d}</span>
  <div class="risk-contract__copy">
    <p class="risk-contract__name">{name}</p>
    <p class="risk-contract__detail">{detail}</p>
  </div>
</div>"""
        for num, (name, detail) in enumerate(RISK_COMMITMENTS, start=1)
    )
    return f"""<div class="risk">
  <div class="risk-hero reveal">
    <p class="risk-hero__lead risk-hero__lead--accent">Ваше спокойствие и уверенность в результате</p>
    <p class="risk-hero__lead">Мы выстраиваем сотрудничество так, чтобы вы контролировали бюджет и видели прогресс на каждом этапе — за счёт схемы оплаты <strong>{RISK_PAYMENT_SCHEME}</strong>.</p>
    <div class="risk-metrics" aria-label="Схема оплаты {RISK_PAYMENT_SCHEME}">
{metrics}
    </div>
  </div>
  <section class="risk-layers reveal" aria-labelledby="riskLayersTitle">
    <header class="risk-layers__head">
      <p class="risk-layers__eyebrow" id="riskLayersTitle">Четыре уровня защиты ваших интересов</p>
      <p class="risk-layers__sub">Юридическая, технологическая и операционная безопасность — в одной модели сотрудничества.</p>
    </header>
    <div class="risk-layers__stack">
{layers}
    </div>
  </section>
  <section class="risk-contract reveal" aria-labelledby="riskContractTitle">
    <div class="risk-contract__panel">
      <header class="risk-contract__head">
        <p class="risk-contract__eyebrow" id="riskContractTitle">Договор</p>
        <h3 class="risk-contract__title">Что фиксируем в договоре</h3>
      </header>
      <div class="risk-contract__grid">
{commitments}
      </div>
    </div>
  </section>
  <figure class="risk-quote reveal">
    <blockquote>«Ответственность за результат — не формулировка в презентации, а условия, по которым мы работаем с первого дня».</blockquote>
  </figure>
</div>"""


def render_stoimost_compare() -> str:
    return """<div class="compare reveal">
  <div class="compare__head">
    <div class="compare__head-cell compare__head-cell--label">Параметр</div>
    <div class="compare__head-cell compare__head-cell--ai">
      <span class="compare__tag compare__tag--ai">MVP и чёткое ТЗ</span>
      Fixed Price
    </div>
    <div class="compare__head-cell compare__head-cell--ai">
      <span class="compare__tag compare__tag--ai">Крупные проекты</span>
      Time &amp; Material
    </div>
  </div>
  <div class="compare__row">
    <div class="compare__cell compare__cell--label">Модель оплаты</div>
    <div class="compare__cell compare__cell--ai">Фиксированная стоимость и чёткие рамки проекта</div>
    <div class="compare__cell compare__cell--ai">Оплата по факту выполнения задач</div>
  </div>
  <div class="compare__row">
    <div class="compare__cell compare__cell--label">Когда выбирать</div>
    <div class="compare__cell compare__cell--ai">MVP и продукты с детально прописанным ТЗ</div>
    <div class="compare__cell compare__cell--ai">Динамичные проекты с гибкими изменениями в процессе</div>
  </div>
  <div class="compare__row">
    <div class="compare__cell compare__cell--label">Прозрачность бюджета</div>
    <div class="compare__cell compare__cell--ai">Сумма и сроки фиксируются до старта работ</div>
    <div class="compare__cell compare__cell--ai">Бюджет масштабируется вместе с приоритетами</div>
  </div>
  <div class="compare__row">
    <div class="compare__cell compare__cell--label">Контроль результата</div>
    <div class="compare__cell compare__cell--ai">Приёмка по согласованному scope и KPI</div>
    <div class="compare__cell compare__cell--ai">Итерации каждые 2 недели с демо и отчётами</div>
  </div>
</div>"""


def render_ai_directions_block(
    prefix: str,
    *,
    copy_key: str,
) -> str:
    title_main, title_sub, lead = AI_DIRECTIONS_COPY.get(copy_key, AI_DIRECTIONS_DEFAULT)
    items = []
    for slug, label in AI_BUSINESS_DIRECTIONS:
        items.append(
            f"""<li class="ai-direction">
  <span class="ai-direction__icon" aria-hidden="true">
    <img src="{prefix}images/ai-directions/{slug}.svg" alt="" width="32" height="32" loading="lazy">
  </span>
  <span class="ai-direction__label">{label}</span>
</li>"""
        )
    count = len(AI_BUSINESS_DIRECTIONS)
    return f"""<section class="ai-directions reveal" aria-labelledby="aiDirectionsTitle">
  <div class="ai-directions__layout">
    <header class="ai-directions__head">
      <p class="ai-directions__eyebrow">Отрасли</p>
      <h3 class="ai-directions__title" id="aiDirectionsTitle">
        <span class="ai-directions__title-main">{title_main}</span>
        <span class="ai-directions__title-sub">{title_sub}</span>
      </h3>
      <p class="ai-directions__lead">{lead}</p>
      <p class="ai-directions__meta"><span class="ai-directions__count">{count}</span> направлений</p>
    </header>
    <ul class="ai-directions__list">
      {"".join(items)}
    </ul>
  </div>
</section>"""


FEATURED_SERVICE_SLUGS = tuple(p.slug for p in SERVICE_PAGES)


def _parse_catalog_heading(heading: str) -> tuple[str, str, str]:
    match = re.match(r"(\d+)\.\s*(.+?)(?:\s*\(([^)]+)\))?\s*$", heading)
    if not match:
        return "00", heading, ""
    return f"{int(match.group(1)):02d}", match.group(2).strip(), (match.group(3) or "").strip()


def _parse_catalog_item(item_html: str) -> tuple[str, str]:
    match = re.match(r"<strong>(.*?)</strong>\s*:?\s*(.*)", item_html, re.DOTALL)
    if not match:
        return item_html, ""
    return match.group(1).strip().rstrip(":"), match.group(2).strip()


def render_uslugi_sidebar(prefix: str) -> str:
    by_slug = {slug: label for slug, label, *_ in SERVICES}
    links = []
    for slug in FEATURED_SERVICE_SLUGS:
        label = by_slug.get(slug)
        if not label:
            continue
        links.append(
            f'<a class="svc-aside__link" href="{page_href(prefix, f"uslugi/{slug}")}">'
            f'<span>{label}</span><span class="svc-aside__arrow" aria-hidden="true">→</span></a>'
        )
    return f"""<aside class="page-layout__sidebar" aria-label="Ключевые направления">
  <div class="page-spec svc-aside">
    <div class="page-spec__head">
      <span class="page-spec__label">Направления</span>
      <h3 class="page-spec__title">Ключевые услуги</h3>
    </div>
    <nav class="svc-aside__nav">{"".join(links)}</nav>
    <div class="svc-aside__actions">
      <button type="button" class="btn btn--primary btn--lg svc-aside__cta js-open-contact">Обсудить проект</button>
      <a class="btn btn--outline btn--sm svc-aside__cta-secondary" href="{page_href(prefix, "stoimost")}">Рассчитать стоимость</a>
    </div>
  </div>
</aside>"""


def render_uslugi_catalog(prefix: str) -> str:
    groups = []
    for heading, items in USLUGI_CATALOG:
        num, title_ru, title_en = _parse_catalog_heading(heading)
        rows = []
        for item in items:
            name, desc = _parse_catalog_item(item)
            rows.append(
                f'<li class="svc-item">'
                f'<span class="svc-item__name">{name}</span>'
                f'<span class="svc-item__desc">{desc}</span></li>'
            )
        en_html = f'<p class="svc-group__en">{title_en}</p>' if title_en else ""
        groups.append(
            f"""<article class="svc-group">
  <header class="svc-group__head">
    <span class="svc-group__num" aria-hidden="true">{num}</span>
    <div class="svc-group__titles">
      <h3 class="svc-group__title">{title_ru}</h3>
      {en_html}
    </div>
  </header>
  <ul class="svc-list">{"".join(rows)}</ul>
</article>"""
        )

    return f"""<div class="page-layout page-layout--with-sidebar reveal">
  <div class="page-layout__main">
    <div class="page-prose page-prose--service svc-catalog-panel">
      <div class="svc-catalog">
        <div class="svc-catalog__grid">
          {"".join(groups)}
        </div>
      </div>
    </div>
  </div>
  {render_uslugi_sidebar(prefix)}
</div>"""


def render_screen_card(
    prefix: str, image: str, alt: str, *, shot_modifier: str = ""
) -> str:
    src = image if image.startswith(("http://", "https://")) else f"{prefix}{image}"
    shot_class = "page-screen-card__shot"
    if shot_modifier:
        shot_class += f" page-screen-card__shot--{shot_modifier}"
    return f"""<div class="page-screen-card bento-showcase__card bento-showcase__card--lg reveal">
  <figure class="{shot_class}">
    <img src="{src}" alt="{alt}" loading="lazy">
  </figure>
</div>"""


def render_submenu(prefix: str) -> str:
    items: list[tuple[str, str, str]] = [
        (f"uslugi/{slug}", label, SERVICE_ICONS.get(slug, SERVICE_ICONS["avtomatizaciya-biznesa"]))
        for slug, label, *_ in SERVICES
    ]
    items.append(
        (
            "uslugi",
            "Все услуги",
            '<path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path>',
        )
    )
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
    return f'<div class="submenu submenu--services" role="menu">{"".join(links)}</div>'


def render_direction_link(prefix: str, slug: str, label: str) -> str:
    icon = DIRECTION_ICONS.get(
        slug,
        '<circle cx="30" cy="30" r="20" stroke="currentColor" stroke-width="1.6"/>',
    )
    return f"""            <a class="direction" href="{page_href(prefix, f'uslugi/{slug}')}" role="listitem">
              <span class="direction__icon">
                <svg width="60" height="60" viewBox="0 0 60 60" fill="none" aria-hidden="true">
                  {icon}
                </svg>
              </span>
              <span class="direction__label">{label}</span>
            </a>"""


def render_clients_strip(prefix: str) -> str:
    by_slug = {slug: label for slug, label, *_ in SERVICES}
    direction_links = "\n".join(
        render_direction_link(prefix, slug, by_slug[slug])
        for slug in DIRECTION_STRIP_SLUGS
        if slug in by_slug
    )
    return f"""    <section class="clients-strip" data-fab-theme="light">
      <div class="container">
        <div class="clients-strip__card">
          <div class="directions reveal" role="list">
{direction_links}
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
    home_href = page_href(prefix, "")
    portfolio_href = "#portfolio" if home_href in ("", "./") else f"{home_href}#portfolio"

    def nav_link(slug: str, label: str) -> str:
        cls = "nav__link is-active" if active == slug else "nav__link"
        if slug == "portfolio":
            return f'<li class="nav__item"><a class="{cls}" href="{portfolio_href}">{label}</a></li>'
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
        <button type="button" class="btn btn--primary btn--sm js-open-contact">ОБСУДИТЬ ПРОЕКТ {BTN_ARROW_SM}</button>
        <button class="burger" id="burgerBtn" aria-label="Открыть меню" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
    <div class="mobile-menu" id="mobileMenu">
      <a href="{page_href(prefix, 'uslugi')}" class="mobile-menu__link">Услуги</a>
      <a href="{portfolio_href}" class="mobile-menu__link">Портфолио</a>
      <a href="{page_href(prefix, 'etapy')}" class="mobile-menu__link">Этапы реализации</a>
      <a href="{page_href(prefix, 'sroki')}" class="mobile-menu__link">Сроки</a>
      <a href="{page_href(prefix, 'garantii')}" class="mobile-menu__link">Гарантии</a>
      <button type="button" class="btn btn--primary mobile-menu__cta js-open-contact">Обсудить проект</button>
    </div>
  </header>"""


def render_hero(
    prefix: str,
    second_btn: tuple[str, str] | None = None,
    *,
    hero_h1: str | None = None,
) -> str:
    second = ""
    if second_btn:
        href, label = second_btn
        second = f"""
            <a href="{href}" class="btn btn--outline btn--lg">{label}</a>"""
    # Единый hero-заголовок на всех страницах (hero_h1 намеренно игнорируется
    # для заголовка — текст должен быть одинаковым по всему сайту).
    title_html = (
        'Разрабатываем ПО любой сложности для '
        '<span class="text-gradient">автоматизации бизнеса</span>'
    )
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
            {title_html}
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


def render_stats_cases(prefix: str) -> str:
    return STATS_CASES_PARTIAL.replace("{{ROOT}}", prefix)


def render_cases(prefix: str) -> str:
    """Только секция cases (портфолио) — для синхронизации блока на index.html."""
    return CASES_PARTIAL.replace("{{ROOT}}", prefix)


def render_portfolio_assets(prefix: str) -> tuple[str, str]:
    head = '  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">\n'
    tail = f"""  <script type="importmap">
  {{ "imports": {{ "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js" }} }}
  </script>
  <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
  <script src="{prefix}script.js"></script>
  <script type="module" src="{prefix}case3d.js"></script>
"""
    return head, tail


def render_cta(prefix: str) -> str:
    return f"""    <section class="cta cta--simple" id="cta" data-fab-theme="light">
      <div class="container">
        <div class="cta__card cta__inner cta__inner--centered">
          <div class="cta__bg" aria-hidden="true"></div>
          <div class="cta__text reveal">
            <h2 class="section-title section-title--light">Следующий успех на рынке может стать <span class="text-gradient">вашим</span>.</h2>
            <button type="button" class="btn btn--primary btn--lg cta__submit js-open-contact">Связаться с нами {BTN_ARROW_SM}</button>
            <h2 class="section-title section-title--light">Давайте сделаем это.</h2>
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
      <div class="footer__main">
        <div class="footer__col footer__col--brand">
          <a href="{prefix}" class="logo logo--footer">
            <img src="{prefix}logos/budget-soft.svg" alt="BUDGET SOFT" class="logo__img">
          </a>
          <p class="footer__tagline">Заказная разработка ПО, AI и автоматизация бизнес-процессов.</p>
          <ul class="footer__contacts">
            <li><a href="{CONTACT_TELEGRAM}" target="_blank" rel="noopener">Telegram: @skrylkovs</a></li>
            <li><a href="{CONTACT_WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a></li>
            <li><a href="mailto:info@budget-soft.ru">info@budget-soft.ru</a></li>
            <li><span>{OFFICE_ADDRESS}</span></li>
          </ul>
        </div>
        <div class="footer__nav">
          <div class="footer__col">
            <h4 class="footer__title">Компания</h4>
            <ul class="footer__links">
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
      </div>
      <section class="footer__services" aria-labelledby="footerServicesTitle">
        <h4 class="footer__title" id="footerServicesTitle">Услуги</h4>
        <ul class="footer__links footer__links--services">
          {footer_service_links}
          <li class="footer__links-all-item"><a href="{page_href(prefix, 'uslugi')}" class="footer__links-all">Все услуги →</a></li>
        </ul>
      </section>
      <div class="footer__bottom">
        <div class="footer__copy">© 2026 BUDGET SOFT</div>
        <div class="footer__legal"><a href="{page_href(prefix, 'privacy')}">Политика конфиденциальности</a></div>
      </div>
    </div>
  </footer>"""


def render_contact_modal() -> str:
    return f"""  <div class="contact-modal" id="contactModal" hidden>
    <div class="contact-modal__backdrop" data-close-contact></div>
    <div class="contact-modal__panel" role="dialog" aria-modal="true" aria-labelledby="contactModalTitle">
      <button class="contact-modal__close" type="button" aria-label="Закрыть" data-close-contact>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"></path></svg>
      </button>
      <div class="contact-modal__inner">
        <header class="contact-modal__header">
          <h2 class="contact-modal__title" id="contactModalTitle">Обсудить <span class="contact-modal__accent">проект</span></h2>
          <p class="contact-modal__lead">Расскажите о задаче — подберём формат и сроки. Обычно отвечаем в течение рабочего дня.</p>
        </header>
        <div class="contact-modal__grid">
          <div class="contact-modal__row contact-modal__row--messengers">
            <a class="contact-modal__tile contact-modal__tile--telegram" href="{CONTACT_TELEGRAM}" target="_blank" rel="noopener">
              <span class="contact-modal__tile-icon" aria-hidden="true">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M21.5 4.5L2 12l6 2 2 6 4-4 6 5 1.5-16.5z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
              </span>
              <span class="contact-modal__tile-text">
                <strong>Telegram</strong>
                <span>@skrylkovs</span>
              </span>
            </a>
            <a class="contact-modal__tile contact-modal__tile--whatsapp" href="{CONTACT_WHATSAPP}" target="_blank" rel="noopener">
              <span class="contact-modal__tile-icon" aria-hidden="true">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M12 2a10 10 0 00-9.2 14L2 22l6.1-1.6A10 10 0 1012 2z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M8.2 9.8c.3 1.1 1.4 2.6 3.1 3.4 1 .5 1.9.7 2.2.8" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
              </span>
              <span class="contact-modal__tile-text">
                <strong>WhatsApp</strong>
                <span>Написать</span>
              </span>
            </a>
          </div>
          <div class="contact-modal__row contact-modal__row--contacts">
            <a class="contact-modal__tile" href="mailto:info@budget-soft.ru">
              <span class="contact-modal__tile-icon" aria-hidden="true">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><rect x="3" y="5" width="18" height="14" rx="2" stroke="currentColor" stroke-width="1.6"/><path d="M3 7l9 6 9-6" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
              </span>
              <span class="contact-modal__tile-text">
                <strong>Email</strong>
                <span>info@budget-soft.ru</span>
              </span>
            </a>
          </div>
          <div class="contact-modal__tile contact-modal__tile--muted">
            <span class="contact-modal__tile-icon" aria-hidden="true">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M12 2C8.1 2 5 5.1 5 9c0 5.2 7 13 7 13s7-7.8 7-13c0-3.9-3.1-7-7-7z" stroke="currentColor" stroke-width="1.6"/><circle cx="12" cy="9" r="2.5" stroke="currentColor" stroke-width="1.6"/></svg>
            </span>
            <span class="contact-modal__tile-text">
              <strong>Офис</strong>
              <span>{OFFICE_ADDRESS}</span>
            </span>
          </div>
        </div>
      </div>
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

  <button type="button" class="messenger-fab js-open-contact" aria-label="Обсудить проект">
    <svg width="26" height="26" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M21.5 4.5L2 12l6 2 2 6 4-4 6 5 1.5-16.5z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"></path></svg>
  </button>"""


def render_scripts(prefix: str) -> str:
    return f'  <script src="{prefix}script.js"></script>'


def canonical_url(path: str) -> str:
    """Абсолютный canonical-URL по «красивому» пути (без хвостовых слешей на входе)."""
    path = path.strip("/")
    return f"{SITE_URL}/{path}/" if path else f"{SITE_URL}/"


def seo_head(*, title: str, description: str, canonical_path: str, jsonld: str = "") -> str:
    """Блок <head>: description, canonical, Open Graph, Twitter Card и (опц.) JSON-LD."""
    url = canonical_url(canonical_path)
    desc = html.escape(description or "", quote=True)
    t = html.escape(title or "", quote=True)
    lines = [
        f'  <meta name="description" content="{desc}">',
        f'  <link rel="canonical" href="{url}">',
        '  <meta property="og:type" content="website">',
        '  <meta property="og:site_name" content="BUDGET SOFT">',
        '  <meta property="og:locale" content="ru_RU">',
        f'  <meta property="og:title" content="{t}">',
        f'  <meta property="og:description" content="{desc}">',
        f'  <meta property="og:url" content="{url}">',
        f'  <meta property="og:image" content="{OG_IMAGE}">',
        '  <meta name="twitter:card" content="summary_large_image">',
        f'  <meta name="twitter:title" content="{t}">',
        f'  <meta name="twitter:description" content="{desc}">',
        f'  <meta name="twitter:image" content="{OG_IMAGE}">',
    ]
    if jsonld:
        lines.append(f'  <script type="application/ld+json">{jsonld}</script>')
    return "\n".join(lines) + "\n"


def breadcrumb_jsonld(menu_label: str, slug: str) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Главная", "item": f"{SITE_URL}/"},
            {"@type": "ListItem", "position": 2, "name": "Услуги", "item": f"{SITE_URL}/uslugi/"},
            {"@type": "ListItem", "position": 3, "name": menu_label, "item": canonical_url(f"uslugi/{slug}")},
        ],
    }
    return json.dumps(data, ensure_ascii=False)


def render_page(
    *,
    depth: int,
    title: str,
    active: str,
    eyebrow: str,
    title_html: str,
    lead: str,
    content: str,
    description: str = "",
    canonical_path: str = "",
    jsonld: str = "",
    section_id: str = "",
    accent: str = "",
    second_btn: tuple[str, str] | None = None,
    include_stats_cases: bool = True,
    hero_h1: str | None = None,
) -> str:
    p = rel_prefix(depth)
    portfolio_head, portfolio_tail = render_portfolio_assets(p) if include_stats_cases else ("", "")
    stats_cases = render_stats_cases(p) if include_stats_cases else ""
    seo = seo_head(title=title, description=description, canonical_path=canonical_path, jsonld=jsonld)
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
{seo}  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{p}styles.css">
  <link rel="stylesheet" href="{p}page.css">
{portfolio_head}</head>
<body class="page-body page-inner">
{render_header(p, active)}
  <main>
{render_hero(p, second_btn, hero_h1=hero_h1)}
{render_clients_strip(p)}
{render_revolution(eyebrow=eyebrow, title_html=title_html, lead=lead, content=content, section_id=section_id, accent=accent)}
{stats_cases}{render_cta(p)}
  </main>
{render_footer(p)}
{render_tail(p)}
{portfolio_tail if include_stats_cases else render_scripts(p)}</body>
</html>"""


def content_etapy() -> str:
    return render_workflow()


def content_sroki() -> str:
    return render_ttm_content()


def content_garantii() -> str:
    return render_risk_content()


def content_stoimost(prefix: str) -> str:
    return render_stoimost_compare() + """
<div class="page-outro reveal">
  <p>Свяжитесь с нами, и наш эксперт рассчитает точный бюджет проекта под ваши задачи уже в рамках первичного планирования.</p>
  <button type="button" class="btn btn--primary btn--lg js-open-contact">Получить расчёт</button>
</div>"""


def content_prose(
    body: str,
    prefix: str,
    screen_key: str | None = None,
    pricing_key: str | None = None,
    middle: str = "",
) -> str:
    body = body.replace("{home}", prefix.rstrip("/") or ".")
    screen = ""
    if screen_key and screen_key in SCREENS:
        screen = render_screen_card(prefix, *SCREENS[screen_key])
    if pricing_key and pricing_key in SERVICE_PRICING:
        pricing = render_service_pricing_table(
            SERVICE_PRICING[pricing_key], sidebar=True
        )
        return f"""<div class="page-layout page-layout--with-sidebar reveal">
  <div class="page-layout__main">
    <div class="page-prose page-prose--service">{body}</div>
  </div>
  <aside class="page-layout__sidebar" aria-label="Условия и стоимость">
    {pricing}
  </aside>
</div>{middle}{screen}"""
    return f'<div class="page-prose reveal">{body}</div>{middle}{screen}'


def write_page(path: Path, html: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    html = inject_metrika(html)
    path.write_text(html, encoding="utf-8")
    print(f"  {path.relative_to(ROOT)}")


def update_index_html() -> None:
    """Синхронизирует меню услуг, полосу направлений и футер на главной."""
    path = ROOT / "index.html"
    html = path.read_text(encoding="utf-8")
    prefix = ""

    submenu_new = render_submenu(prefix).replace(
        'class="submenu submenu--services"', 'class="submenu submenu--services"', 1
    )
    # index uses <div class="submenu" without submenu--services in old file
    submenu_new = submenu_new.replace('submenu submenu--services', 'submenu submenu--services', 1)

    html = re.sub(
        r'<div class="submenu" role="menu">.*?</div>\s*</li>\s*<li class="nav__item"><a class="nav__link" href="#portfolio">',
        submenu_new + '\n          </li>\n          <li class="nav__item"><a class="nav__link" href="#portfolio">',
        html,
        count=1,
        flags=re.DOTALL,
    )

    strip_inner = "\n".join(
        render_direction_link(prefix, slug, SERVICE_BY_SLUG[slug].menu_label)
        for slug in DIRECTION_STRIP_SLUGS
        if slug in SERVICE_BY_SLUG
    )
    html = re.sub(
        r'<div class="directions reveal[^"]*" role="list">.*?</div>\s*<!-- TODO: временно скрыто',
        f'<div class="directions reveal is-visible" role="list">\n{strip_inner}\n          </div>\n\n          <!-- TODO: временно скрыто',
        html,
        count=1,
        flags=re.DOTALL,
    )

    footer_links = "".join(
        f'          <li><a href="uslugi/{p.slug}/">{p.menu_label}</a></li>\n'
        for p in SERVICE_PAGES
    )
    footer_block = f"""      <div class="footer__main">
        <div class="footer__col footer__col--brand">
          <a href="./" class="logo logo--footer">
            <img src="logos/budget-soft.svg" alt="BUDGET SOFT" class="logo__img">
          </a>
          <p class="footer__tagline">Заказная разработка ПО, AI и автоматизация бизнес-процессов.</p>
          <ul class="footer__contacts">
            <li>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M21.5 4.5L2 12l6 2 2 6 4-4 6 5 1.5-16.5z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"></path></svg>
              <a href="{CONTACT_TELEGRAM}" target="_blank" rel="noopener">Telegram: @skrylkovs</a>
            </li>
            <li>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 2a10 10 0 00-9.2 14L2 22l6.1-1.6A10 10 0 1012 2z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"></path></svg>
              <a href="{CONTACT_WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a>
            </li>
            <li>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2" stroke="currentColor" stroke-width="1.6"></rect><path d="M2 6l10 7L22 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path></svg>
              <a href="mailto:info@budget-soft.ru">info@budget-soft.ru</a>
            </li>
            <li>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 22s8-7.58 8-13a8 8 0 10-16 0c0 5.42 8 13 8 13z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"></path><circle cx="12" cy="9" r="3" stroke="currentColor" stroke-width="1.6"></circle></svg>
              <span>Москва, ул. Бауманская, 11, стр. 8, оф. 402</span>
            </li>
          </ul>
        </div>
        <div class="footer__nav">
          <div class="footer__col">
            <h4 class="footer__title">Компания</h4>
            <ul class="footer__links">
              <li><a href="portfolio/">Портфолио</a></li>
              <li><a href="stoimost/">Стоимость</a></li>
              <li><a href="o-nas/">О нас</a></li>
              <li><a href="kontakty/">Контакты</a></li>
            </ul>
          </div>
          <div class="footer__col">
            <h4 class="footer__title">Ресурсы</h4>
            <ul class="footer__links">
              <li><a href="etapy/">Этапы реализации</a></li>
              <li><a href="sroki/">Сроки</a></li>
              <li><a href="garantii/">Гарантии</a></li>
              <li><a href="blog/" class="footer__links-soon">Блог <span class="badge-soon">скоро</span></a></li>
            </ul>
          </div>
        </div>
      </div>
      <section class="footer__services" aria-labelledby="footerServicesTitle">
        <h4 class="footer__title" id="footerServicesTitle">Услуги</h4>
        <ul class="footer__links footer__links--services">
{footer_links}          <li class="footer__links-all-item"><a href="uslugi/" class="footer__links-all">Все услуги →</a></li>
        </ul>
      </section>"""
    html = re.sub(
        r'<div class="footer__grid">.*?</div>\s*<div class="footer__bottom">',
        footer_block + '\n\n      <div class="footer__bottom">',
        html,
        count=1,
        flags=re.DOTALL,
    )

    html = html.replace(
        '<p class="footer__tagline">Разработка ПО для бизнеса. Импортозамещение и автоматизация.</p>',
        '<p class="footer__tagline">Заказная разработка ПО, AI и автоматизация бизнес-процессов.</p>',
    )
    html = html.replace(
        '<li><a href="importozameshchenie/">Импортозамещение</a></li>',
        '',
    )

    html = fix_home_contacts(html)
    html = inject_home_seo(html)
    html = inject_metrika(html)

    path.write_text(html, encoding="utf-8")
    print(f"  {path.relative_to(ROOT)} (menu sync)")


def fix_home_contacts(html_doc: str) -> str:
    """Убирает телефон-плейсхолдер и прописывает Telegram/WhatsApp в собственной
    разметке index.html (футер, соц-блок, contact-modal). Идемпотентно."""
    # Футер: <li> с телефоном → Telegram + WhatsApp
    html_doc = html_doc.replace(
        """            <li>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.13.96.37 1.9.72 2.8a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.9.35 1.84.59 2.8.72A2 2 0 0122 16.92z" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path></svg>
              <a href="tel:+74950000000">+7 (495) 000-00-00</a>
            </li>""",
        f"""            <li>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M21.5 4.5L2 12l6 2 2 6 4-4 6 5 1.5-16.5z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"></path></svg>
              <a href="{CONTACT_TELEGRAM}" target="_blank" rel="noopener">Telegram: @skrylkovs</a>
            </li>
            <li>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 2a10 10 0 00-9.2 14L2 22l6.1-1.6A10 10 0 1012 2z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"></path></svg>
              <a href="{CONTACT_WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a>
            </li>""",
    )
    # Соц-блок в подвале
    html_doc = html_doc.replace(
        '<a href="https://t.me/" target="_blank" rel="noopener" class="footer__social-link" aria-label="Telegram">',
        f'<a href="{CONTACT_TELEGRAM}" target="_blank" rel="noopener" class="footer__social-link" aria-label="Telegram">',
    )
    html_doc = html_doc.replace(
        '<a href="https://wa.me/74950000000" target="_blank" rel="noopener" class="footer__social-link" aria-label="WhatsApp">',
        f'<a href="{CONTACT_WHATSAPP}" target="_blank" rel="noopener" class="footer__social-link" aria-label="WhatsApp">',
    )
    # Contact-modal: ссылки мессенджеров и подписи
    html_doc = html_doc.replace(
        '<a class="contact-modal__tile contact-modal__tile--telegram" href="https://t.me/" target="_blank" rel="noopener">',
        f'<a class="contact-modal__tile contact-modal__tile--telegram" href="{CONTACT_TELEGRAM}" target="_blank" rel="noopener">',
    )
    html_doc = html_doc.replace(
        '<a class="contact-modal__tile contact-modal__tile--whatsapp" href="https://wa.me/74950000000" target="_blank" rel="noopener">',
        f'<a class="contact-modal__tile contact-modal__tile--whatsapp" href="{CONTACT_WHATSAPP}" target="_blank" rel="noopener">',
    )
    html_doc = html_doc.replace(
        """                <strong>Telegram</strong>
                <span>Написать в мессенджер</span>""",
        """                <strong>Telegram</strong>
                <span>@skrylkovs</span>""",
    )
    html_doc = html_doc.replace(
        """                <strong>WhatsApp</strong>
                <span>Написать в мессенджер</span>""",
        """                <strong>WhatsApp</strong>
                <span>Написать</span>""",
    )
    # Contact-modal: убрать плитку «Телефон» целиком
    html_doc = html_doc.replace(
        """            <a class="contact-modal__tile" href="tel:+74950000000">
              <span class="contact-modal__tile-icon" aria-hidden="true">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M5 4h4l2 5-2 1a13 13 0 006 6l1-2 5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
              </span>
              <span class="contact-modal__tile-text">
                <strong>Телефон</strong>
                <span>+7 (495) 000-00-00</span>
              </span>
            </a>
            <a class="contact-modal__tile" href="mailto:info@budget-soft.ru">""",
        """            <a class="contact-modal__tile" href="mailto:info@budget-soft.ru">""",
    )
    return html_doc


def inject_home_seo(html_doc: str) -> str:
    """Добавляет canonical, Open Graph, Twitter Card и JSON-LD Organization в <head> главной.

    description на главной уже есть в index.html — берём её текст для OG/Twitter.
    Идемпотентно: повторный прогон ничего не дублирует.
    """
    if 'rel="canonical"' in html_doc:
        return html_doc

    m_title = re.search(r"<title>(.*?)</title>", html_doc, flags=re.DOTALL)
    m_desc = re.search(r'<meta name="description" content="(.*?)">', html_doc, flags=re.DOTALL)
    title = m_title.group(1).strip() if m_title else "BUDGET SOFT"
    desc = m_desc.group(1).strip() if m_desc else ""
    url = f"{SITE_URL}/"

    org = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": "BUDGET SOFT",
            "url": url,
            "email": "info@budget-soft.ru",
            "logo": f"{SITE_URL}/logos/budget-soft.svg",
            "image": OG_IMAGE,
            "description": desc,
            "sameAs": [CONTACT_TELEGRAM, CONTACT_WHATSAPP],
        },
        ensure_ascii=False,
    )

    block = (
        f'  <link rel="canonical" href="{url}">\n'
        '  <meta property="og:type" content="website">\n'
        '  <meta property="og:site_name" content="BUDGET SOFT">\n'
        '  <meta property="og:locale" content="ru_RU">\n'
        f'  <meta property="og:title" content="{html.escape(title, quote=True)}">\n'
        f'  <meta property="og:description" content="{html.escape(desc, quote=True)}">\n'
        f'  <meta property="og:url" content="{url}">\n'
        f'  <meta property="og:image" content="{OG_IMAGE}">\n'
        '  <meta name="twitter:card" content="summary_large_image">\n'
        f'  <meta name="twitter:title" content="{html.escape(title, quote=True)}">\n'
        f'  <meta name="twitter:description" content="{html.escape(desc, quote=True)}">\n'
        f'  <meta name="twitter:image" content="{OG_IMAGE}">\n'
        f'  <script type="application/ld+json">{org}</script>\n'
    )
    return html_doc.replace("</head>", block + "</head>", 1)


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
            "content_fn": lambda p: content_sroki(),
            "section_id": "speed",
        },
        {
            "slug": "garantii",
            "title": "Гарантии — BUDGET SOFT",
            "active": "garantii",
            "eyebrow": "Risk Mitigation",
            "title_html": 'Гарантии и <span class="text-gradient">безопасность</span>',
            "lead": f"Ориентируемся на ваше спокойствие и уверенность в результате — с поэтапной оплатой {RISK_PAYMENT_SCHEME} и прозрачным процессом на каждом этапе.",
            "content_fn": lambda p: content_garantii(),
            "section_id": "garantii",
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
                """<h4 class="page-prose__heading">Почему импортозамещение нельзя откладывать</h4>
<p>Уход зарубежных вендоров, отзыв лицензий и риск внезапной блокировки софта бьют по непрерывности операций — особенно у компаний с длинными цепочками поставок и жёсткими SLA перед клиентами. Дедлайны регуляторики для субъектов КИИ делают вопрос не теоретическим, а календарным.</p>
<p>Мы оцениваем текущий ландшафт: что критично заменить в первую очередь, какие данные и интеграции затронуты, где допустим поэтапный переход, а где нужен «мост» между старой и новой системой.</p>
<h4 class="page-prose__heading">Legacy Modernization и суверенная архитектура</h4>
<p>Проводим рефакторинг и пересборку устаревших систем: сохраняем бизнес-логику и данные, убираем технический долг и зависимость от недоступных компонентов. Цель — ИТ-контур, которым вы владеете: исходники, инфраструктура, регламенты обновлений и ключи шифрования под вашим контролем.</p>
<p>Разрабатываем SaaS, кастомные CRM и ERP, модули для складов и маркетплейсов, интеграции с 1С и отечественным стеком — без «чёрного ящика», который снова окажется за рубежом.</p>
<h4 class="page-prose__heading">Миграция без простоя для бизнеса</h4>
<p>Перенос данных и переключение пользователей идут по согласованному регламенту: параллельная работа контуров, контрольные сверки, откат при отклонениях. Сотрудники не остаются без инструментов в пиковые периоды — критичные процессы закрыты до отключения legacy.</p>
<p>После cutover — гиперопека, мониторинг и донастройка под реальную нагрузку. Фиксируем юридически и технически передачу прав на ПО и документацию, чтобы импортозамещение было завершённым проектом, а не бесконечной «миграцией в процессе».</p>""",
                p,
                pricing_key="importozameshchenie",
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
<p>Эпоха раздутых штатов закончилась. Наступила эра AI-дирижеров.</p>
<p>Специалисты BUDGET SOFT — это проджект-менеджеры с глубочайшей технической экспертизой, которые используют продвинутые AI-агенты как мультипликатор силы. Один человек у нас управляет целым пулом AI-разработчиков и заменяет стандартный ИТ-отдел.</p>
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
                f"""<p>Оставьте заявку прямо сейчас, и мы подготовим первичный концепт решения и расчёт бюджета для вашего проекта.</p>
<ul class="page-contacts">
<li><strong>Telegram:</strong> <a href="{CONTACT_TELEGRAM}" target="_blank" rel="noopener">@skrylkovs</a></li>
<li><strong>WhatsApp:</strong> <a href="{CONTACT_WHATSAPP}" target="_blank" rel="noopener">Написать</a></li>
<li><strong>Email:</strong> <a href="mailto:info@budget-soft.ru">info@budget-soft.ru</a></li>
<li><strong>Офис:</strong> {OFFICE_ADDRESS}</li>
</ul>
<p><button type="button" class="btn btn--primary btn--lg js-open-contact">Обсудить проект</button></p>""",
                p,
            ),
        },
        {
            "slug": "portfolio",
            "title": "Портфолио — BUDGET SOFT",
            "active": "portfolio",
            "section_id": "portfolio-page",
            "eyebrow": "Портфолио",
            "title_html": 'Наши <span class="text-gradient">проекты</span>',
            "lead": "Мы реализуем проекты для компаний из финтеха, логистики, ритейла и промышленности.",
            "content_fn": lambda p: content_prose(
                """<p>Подборка кейсов с главной страницы — отправная точка для знакомства с нашим опытом.</p>
<p><a class="page-inline-link" href="{home}#portfolio">Смотреть кейсы на главной →</a></p>""",
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

    page_descriptions = {
        "etapy": "Как мы ведём проект: от консультации и ТЗ до разработки, тестирования и поддержки. Прозрачные этапы реализации и поэтапная оплата в BUDGET SOFT.",
        "sroki": "Запускаем продукты за недели, а не месяцы: AI-Native подход сокращает time-to-market без потери качества. Реальные сроки разработки ПО в BUDGET SOFT.",
        "garantii": "Гарантии результата и безопасность данных: поэтапная оплата 30·30·40, прозрачный процесс и передача прав на код. Как BUDGET SOFT снижает риски проекта.",
        "stoimost": "Новая математика разработки: вы платите за результат и архитектуру, а не за человеко-часы. Снижение издержек до 10 раз. Рассчитайте стоимость в BUDGET SOFT.",
        "importozameshchenie": "Импортозамещение ПО без простоя: миграция с зарубежных систем на собственное независимое ПО, рефакторинг legacy и передача прав. BUDGET SOFT.",
        "o-nas": "BUDGET SOFT — команда AI-дирижёров: проджект-менеджеры с технической экспертизой управляют пулом AI-агентов и заменяют классический ИТ-отдел.",
        "kontakty": "Связаться с BUDGET SOFT: Telegram, WhatsApp, email. Оставьте заявку — подготовим первичный концепт решения и расчёт бюджета вашего проекта.",
        "portfolio": "Портфолио BUDGET SOFT: проекты для финтеха, логистики, ритейла и промышленности. Кейсы заказной разработки ПО, AI и автоматизации бизнеса.",
        "privacy": "Политика конфиденциальности BUDGET SOFT: как мы обрабатываем и защищаем персональные данные посетителей сайта в соответствии с законодательством РФ.",
        "blog": "Блог BUDGET SOFT об AI-Native разработке, кейсах и технологических трендах. Раздел скоро откроется.",
    }

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
            description=page_descriptions[slug],
            canonical_path=slug,
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
        lead="Заказная разработка для каждой функции бизнеса — от корпоративных систем до AI, мобильных продуктов и инфраструктуры.",
        content=render_uslugi_catalog(uslugi_prefix)
        + render_ai_directions_block(uslugi_prefix, copy_key="uslugi"),
        description="Услуги BUDGET SOFT: заказная разработка ERP, CRM, мобильных и SaaS-приложений, внедрение ИИ, BI и Big Data, FinTech и автоматизация бизнес-процессов.",
        canonical_path="uslugi",
        section_id="services",
        second_btn=(page_href(uslugi_prefix, "stoimost"), "Рассчитать стоимость"),
    )
    write_page(ROOT / "uslugi" / "index.html", uslugi_html)

    for page in SERVICE_PAGES:
        prefix = rel_prefix(2)
        middle = render_ai_directions_block(prefix, copy_key=page.slug)
        content = content_prose(page.body_html, prefix, pricing_key=page.slug, middle=middle)
        html = render_page(
            depth=2,
            title=f"{page.meta_title} — BUDGET SOFT",
            active=f"uslugi/{page.slug}",
            eyebrow=page.menu_label,
            title_html=page.h1,
            lead=page.lead,
            content=content,
            description=page.description,
            canonical_path=f"uslugi/{page.slug}",
            jsonld=breadcrumb_jsonld(page.menu_label, page.slug),
            section_id=page.slug,
            second_btn=(page_href(rel_prefix(2), "stoimost"), "Рассчитать стоимость"),
            hero_h1=page.h1,
        )
        write_page(ROOT / "uslugi" / page.slug / "index.html", html)

    update_index_html()

    write_cname()
    write_robots()
    write_sitemap()

    stoimost_css = ROOT / "stoimost" / "stoimost.css"
    if stoimost_css.exists():
        stoimost_css.unlink()
        print(f"  deleted {stoimost_css.relative_to(ROOT)}")

    print("Done.")


def write_cname() -> None:
    (ROOT / "CNAME").write_text("budget-soft.ru\n", encoding="utf-8")
    print("  CNAME")


def write_robots() -> None:
    content = "User-agent: *\nAllow: /\n\n" f"Sitemap: {SITE_URL}/sitemap.xml\n"
    (ROOT / "robots.txt").write_text(content, encoding="utf-8")
    print("  robots.txt")


def write_sitemap() -> None:
    """Генерирует sitemap.xml по urls.json. Блог исключён (скрыт до запуска)."""
    data = json.loads((ROOT / "urls.json").read_text(encoding="utf-8"))
    urls = [p["url"] for p in data["pages"] if p["url"] != "/blog/"]
    items = "\n".join(f"  <url>\n    <loc>{SITE_URL}{u}</loc>\n  </url>" for u in urls)
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{items}\n"
        "</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")
    print(f"  sitemap.xml ({len(urls)} url)")


if __name__ == "__main__":
    main()
