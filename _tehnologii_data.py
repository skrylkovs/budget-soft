"""Данные и парсинг docs/texts-tehnologii.md — стековые лендинги /tehnologii/.

Раздел собирается отдельным конвейером от страниц услуг (см. трек B в
docs/plan-novye-stranicy-uslug-i-stekovye-lendingi.md): свой источник, свой
парсер и свои типы блоков. Общая MD-разметка (заголовки, таблицы, списки,
{section: …}) делегируется md_body_to_html из _uslugi_data; спец-маркеры
раздела ({verdict-cards}, {eco-map}, {price-models}) рендерятся здесь.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from _uslugi_data import inline_md, md_body_to_html

ROOT = Path(__file__).parent
TEXTS_TEHNOLOGII_MD = ROOT / "docs" / "texts-tehnologii.md"

# Порядок = номер секции `## N.` в MD. Поля:
#   slug        — каталог /tehnologii/<slug>/;
#   menu_label  — короткое имя в меню/футере/хабе;
#   menu_desc   — подпись пункта в панели меню «Технологии»;
#   service_type, low_price — Schema.org Service/Offer (low_price = нижняя
#     цена матрицы «Что строим», не самый дешёвый доп);
#   hub_what / hub_term / hub_price — строка стека в карте хаба /tehnologii/;
#   intro_image / intro_alt — картинка интро-панели первого экрана
#     (файл кладётся руками; до замены лежит плейсхолдер).
TECH_META: list[dict] = [
    {
        "slug": "laravel",
        "menu_label": "Laravel",
        "menu_desc": "Веб-приложения и SaaS",
        "service_type": "Разработка веб-приложений и сайтов на Laravel",
        "low_price": "150000",
        "hub_what": "Сайты, магазины, личные кабинеты, SaaS",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 150 000 ₽",
        "intro_image": "images/tech/laravel-hero.png",
        "intro_alt": "Разработка на Laravel в BUDGET SOFT",
    },
    {
        "slug": "python",
        "menu_label": "Python",
        "menu_desc": "Бэкенд, ИИ и аналитика",
        "service_type": "Разработка на Python",
        "low_price": "150000",
        "hub_what": "Веб-сервисы, ИИ, аналитика, автоматизация",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 150 000 ₽",
        "intro_image": "images/tech/python-hero.png",
        "intro_alt": "Разработка на Python в BUDGET SOFT",
    },
    {
        "slug": "react",
        "menu_label": "React",
        "menu_desc": "SPA, кабинеты, дашборды",
        "service_type": "Разработка сайтов и веб-приложений на React",
        "low_price": "150000",
        "hub_what": "Сайты, SPA, кабинеты, дашборды",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 150 000 ₽",
        "intro_image": "images/tech/react-hero.png",
        "intro_alt": "Разработка на React в BUDGET SOFT",
    },
    {
        "slug": "nodejs",
        "menu_label": "Node.js",
        "menu_desc": "API и real-time сервисы",
        "service_type": "Разработка веб-приложений и API на Node.js",
        "low_price": "250000",
        "hub_what": "Веб-приложения, API и real-time сервисы",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 250 000 ₽",
        "intro_image": "images/tech/nodejs-hero.png",
        "intro_alt": "Разработка на Node.js в BUDGET SOFT",
    },
    {
        "slug": "vue",
        "menu_label": "Vue.js",
        "menu_desc": "SPA, кабинеты и витрины",
        "service_type": "Разработка интерфейсов и веб-приложений на Vue.js",
        "low_price": "45000",
        "hub_what": "SPA, сайты, кабинеты, дашборды, витрины",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 45 000 ₽",
        "intro_image": "images/tech/vue-hero.png",
        "intro_alt": "Разработка на Vue.js в BUDGET SOFT",
    },
    {
        "slug": "flutter",
        "menu_label": "Flutter",
        "menu_desc": "Мобильные iOS и Android",
        "service_type": "Разработка мобильных приложений на Flutter",
        "low_price": "220000",
        "hub_what": "Мобильное приложение iOS + Android",
        "hub_term": "MVP 6–10 недель",
        "hub_price": "от 220 000 ₽",
        "intro_image": "images/tech/flutter-hero.png",
        "intro_alt": "Разработка на Flutter в BUDGET SOFT",
    },
    {
        "slug": "react-native",
        "menu_label": "React Native",
        "menu_desc": "Мобильные iOS и Android",
        "service_type": "Разработка мобильных приложений на React Native",
        "low_price": "220000",
        "hub_what": "Мобильные приложения iOS + Android",
        "hub_term": "MVP 8–12 недель",
        "hub_price": "от 220 000 ₽",
        "intro_image": "images/tech/react-native-hero.png",
        "intro_alt": "Разработка на React Native в BUDGET SOFT",
    },
    {
        "slug": "kotlin",
        "menu_label": "Kotlin",
        "menu_desc": "Мобильные и бэкенд",
        "service_type": "Разработка мобильных приложений на Kotlin",
        "low_price": "220000",
        "hub_what": "Мобильные приложения, бэкенд",
        "hub_term": "MVP 8–12 недель",
        "hub_price": "от 220 000 ₽",
        "intro_image": "images/tech/kotlin-hero.png",
        "intro_alt": "Разработка на Kotlin в BUDGET SOFT",
    },
    {
        "slug": "swift",
        "menu_label": "Swift",
        "menu_desc": "Нативные iOS-приложения",
        "service_type": "Разработка iOS-приложений на Swift",
        "low_price": "300000",
        "hub_what": "iOS-приложения для iPhone и iPad",
        "hub_term": "MVP 6–8 недель",
        "hub_price": "от 300 000 ₽",
        "intro_image": "images/tech/swift-hero.png",
        "intro_alt": "Разработка на Swift в BUDGET SOFT",
    },
    {
        "slug": "angular",
        "menu_label": "Angular",
        "menu_desc": "Корпоративные SPA",
        "service_type": "Разработка на Angular",
        "low_price": "150000",
        "hub_what": "SPA, кабинеты, порталы, дашборды",
        "hub_term": "MVP за 4–8 недель",
        "hub_price": "от 150 000 ₽",
        "intro_image": "images/tech/angular-hero.png",
        "intro_alt": "Разработка на Angular в BUDGET SOFT",
    },
    {
        "slug": "typescript",
        "menu_label": "TypeScript",
        "menu_desc": "SPA, SaaS и API",
        "service_type": "Разработка на TypeScript",
        "low_price": "150000",
        "hub_what": "Сайты, SPA, кабинеты, SaaS и API",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 150 000 ₽",
        "intro_image": "images/tech/typescript-hero.png",
        "intro_alt": "Разработка на TypeScript в BUDGET SOFT",
    },
    {
        "slug": "golang",
        "menu_label": "Go",
        "menu_desc": "Микросервисы и highload",
        "service_type": "Разработка бэкенда и highload-сервисов на Go",
        "low_price": "250000",
        "hub_what": "Бэкенд, API, микросервисы, highload",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 250 000 ₽",
        "intro_image": "images/tech/golang-hero.png",
        "intro_alt": "Разработка на Go в BUDGET SOFT",
    },
    {
        "slug": "java",
        "menu_label": "Java",
        "menu_desc": "Highload и enterprise",
        "service_type": "Разработка на Java",
        "low_price": "250000",
        "hub_what": "Highload-бэкенды, микросервисы, API",
        "hub_term": "MVP 6–10 недель",
        "hub_price": "от 250 000 ₽",
        "intro_image": "images/tech/java-hero.png",
        "intro_alt": "Разработка на Java в BUDGET SOFT",
    },
    {
        "slug": "dotnet",
        "menu_label": ".NET",
        "menu_desc": "Корпоративные системы",
        "service_type": "Разработка корпоративных систем на .NET",
        "low_price": "160000",
        "hub_what": "Корпоративные системы, веб-приложения и API",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 160 000 ₽",
        "intro_image": "images/tech/dotnet-hero.png",
        "intro_alt": "Разработка на .NET в BUDGET SOFT",
    },
    {
        "slug": "php",
        "menu_label": "PHP",
        "menu_desc": "Сайты, магазины, CRM",
        "service_type": "Разработка на PHP",
        "low_price": "150000",
        "hub_what": "Сайты, магазины, кабинеты, SaaS и API",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 150 000 ₽",
        "intro_image": "images/tech/php-hero.png",
        "intro_alt": "Разработка на PHP в BUDGET SOFT",
    },
    {
        "slug": "symfony",
        "menu_label": "Symfony",
        "menu_desc": "Порталы, CRM/ERP, SaaS",
        "service_type": "Разработка на Symfony",
        "low_price": "150000",
        "hub_what": "Порталы, CRM/ERP, магазины, SaaS и API",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 150 000 ₽",
        "intro_image": "images/tech/symfony-hero.png",
        "intro_alt": "Разработка на Symfony в BUDGET SOFT",
    },
    {
        "slug": "yii",
        "menu_label": "Yii",
        "menu_desc": "Порталы, CRM/ERP и API",
        "service_type": "Разработка веб-приложений и сайтов на Yii",
        "low_price": "150000",
        "hub_what": "Порталы, CRM/ERP, магазины с 1С, API",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 150 000 ₽",
        "intro_image": "images/tech/yii-hero.png",
        "intro_alt": "Разработка на Yii в BUDGET SOFT",
    },
    {
        "slug": "wordpress",
        "menu_label": "WordPress",
        "menu_desc": "Сайты и магазины",
        "service_type": "Разработка сайтов на WordPress",
        "low_price": "45000",
        "hub_what": "Сайты, магазины, порталы",
        "hub_term": "от 1 недели",
        "hub_price": "от 45 000 ₽",
        "intro_image": "images/tech/wordpress-hero.png",
        "intro_alt": "Разработка на WordPress в BUDGET SOFT",
    },
    {
        "slug": "bitrix",
        "menu_label": "1С-Битрикс",
        "menu_desc": "Сайты и порталы с 1С",
        "service_type": "Разработка сайтов на 1С-Битрикс",
        "low_price": "150000",
        "hub_what": "Сайты, магазины, порталы",
        "hub_term": "от 3 недель",
        "hub_price": "от 150 000 ₽",
        "intro_image": "images/tech/bitrix-hero.png",
        "intro_alt": "Разработка на 1С-Битрикс в BUDGET SOFT",
    },
    {
        "slug": "drupal",
        "menu_label": "Drupal",
        "menu_desc": "Порталы и контент-сайты",
        "service_type": "Разработка сайтов и порталов на Drupal",
        "low_price": "150000",
        "hub_what": "Порталы, сайты, магазины",
        "hub_term": "MVP 4–6 недель",
        "hub_price": "от 150 000 ₽",
        "intro_image": "images/tech/drupal-hero.png",
        "intro_alt": "Разработка на Drupal в BUDGET SOFT",
    },
    {
        "slug": "django",
        "menu_label": "Django",
        "menu_desc": "Сайты, API и SaaS",
        "service_type": "Разработка на Django",
        "low_price": "150000",
        "hub_what": "Сайты, веб-приложения, API, CRM и SaaS",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 150 000 ₽",
        "intro_image": "images/tech/django-hero.png",
        "intro_alt": "Разработка на Django в BUDGET SOFT",
    },
    {
        "slug": "fastapi",
        "menu_label": "FastAPI",
        "menu_desc": "REST/GraphQL API",
        "service_type": "Разработка бэкенда на FastAPI",
        "low_price": "180000",
        "hub_what": "REST/GraphQL API, микросервисы, бэкенд",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 180 000 ₽",
        "intro_image": "images/tech/fastapi-hero.png",
        "intro_alt": "Разработка на FastAPI в BUDGET SOFT",
    },
    {
        "slug": "nextjs",
        "menu_label": "Next.js",
        "menu_desc": "SEO-сайты с SSR",
        "service_type": "Разработка сайтов и веб-приложений на Next.js",
        "low_price": "150000",
        "hub_what": "Сайты, магазины, кабинеты, SaaS и веб-приложения",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 150 000 ₽",
        "intro_image": "images/tech/nextjs-hero.png",
        "intro_alt": "Разработка на Next.js в BUDGET SOFT",
    },
    {
        "slug": "nestjs",
        "menu_label": "NestJS",
        "menu_desc": "API и микросервисы",
        "service_type": "Разработка backend на NestJS",
        "low_price": "160000",
        "hub_what": "API, SaaS, микросервисы",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 160 000 ₽",
        "intro_image": "images/tech/nestjs-hero.png",
        "intro_alt": "Разработка на NestJS в BUDGET SOFT",
    },
    {
        "slug": "nuxt",
        "menu_label": "Nuxt",
        "menu_desc": "SEO-сайты и PWA",
        "service_type": "Разработка сайтов и веб-приложений на Nuxt",
        "low_price": "45000",
        "hub_what": "Сайты, магазины, кабинеты, SaaS и PWA",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 45 000 ₽",
        "intro_image": "images/tech/nuxt-hero.png",
        "intro_alt": "Разработка на Nuxt в BUDGET SOFT",
    },
    {
        "slug": "spring",
        "menu_label": "Spring",
        "menu_desc": "Микросервисы и enterprise",
        "service_type": "Разработка бэкенда на Spring",
        "low_price": "160000",
        "hub_what": "Бэкенд, микросервисы, корпоративные системы",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 160 000 ₽",
        "intro_image": "images/tech/spring-hero.png",
        "intro_alt": "Разработка на Spring в BUDGET SOFT",
    },
    {
        "slug": "rust",
        "menu_label": "Rust",
        "menu_desc": "Highload и блокчейн",
        "service_type": "Разработка на Rust",
        "low_price": "150000",
        "hub_what": "Высоконагруженный backend, блокчейн, IoT",
        "hub_term": "MVP 6–10 недель",
        "hub_price": "от 150 000 ₽",
        "intro_image": "images/tech/rust-hero.png",
        "intro_alt": "Разработка на Rust в BUDGET SOFT",
    },
    {
        "slug": "ruby",
        "menu_label": "Ruby on Rails",
        "menu_desc": "MVP и SaaS",
        "service_type": "Разработка веб-приложений на Ruby on Rails",
        "low_price": "160000",
        "hub_what": "MVP, SaaS, маркетплейсы и веб-приложения",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 160 000 ₽",
        "intro_image": "images/tech/ruby-hero.png",
        "intro_alt": "Разработка на Ruby on Rails в BUDGET SOFT",
    },
    {
        "slug": "cpp",
        "menu_label": "C++",
        "menu_desc": "Десктоп и встроенное ПО",
        "service_type": "Разработка ПО на C++",
        "low_price": "400000",
        "hub_what": "Highload, десктоп и встроенное ПО",
        "hub_term": "MVP 8–12 недель",
        "hub_price": "от 400 000 ₽",
        "intro_image": "images/tech/cpp-hero.png",
        "intro_alt": "Разработка на C++ в BUDGET SOFT",
    },
    {
        "slug": "solidity",
        "menu_label": "Solidity",
        "menu_desc": "Смарт-контракты и NFT",
        "service_type": "Разработка смарт-контрактов на Solidity",
        "low_price": "150000",
        "hub_what": "Смарт-контракты, DeFi, NFT, DApps",
        "hub_term": "MVP 4–8 недель",
        "hub_price": "от 150 000 ₽",
        "intro_image": "images/tech/solidity-hero.png",
        "intro_alt": "Разработка на Solidity в BUDGET SOFT",
    },
    {
        "slug": "1c",
        "menu_label": "1С",
        "menu_desc": "Доработка и интеграции",
        "service_type": "Разработка на 1С",
        "low_price": "150000",
        "hub_what": "Доработка 1С, ERP и учёт, интеграции",
        "hub_term": "от 2 недель",
        "hub_price": "от 150 000 ₽",
        "intro_image": "images/tech/1c-hero.png",
        "intro_alt": "Разработка на 1С в BUDGET SOFT",
    },
]


@dataclass
class TechPage:
    slug: str
    menu_label: str
    menu_desc: str
    service_type: str
    low_price: str
    hub_what: str
    hub_term: str
    hub_price: str
    meta_title: str  # Title целиком, включая бренд — генератор не дописывает
    h1: str
    description: str  # явное поле **Description:** секции
    facts: list[tuple[str, str]]  # факты интро-панели: (крупная цифра, подпись)
    intro_image: str
    intro_alt: str
    cta: tuple[str, str, str]  # заголовок, кнопка, подпись финального CTA
    lead: str
    body_html: str
    faq: list[tuple[str, str]]  # вопрос/ответ в MD-разметке (ссылки в ответах)


def md_plain(text: str) -> str:
    """Текст без MD-разметки (для JSON-LD FAQPage: совпадает с видимым 1:1)."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def render_verdict_cards(items: list[tuple[str, str, str]]) -> str:
    """Пары «подходит / не подходит» (.tech-verdict): каждый пункт маркера
    {verdict-cards} — строка ``- yes|no :: Заголовок :: Текст``."""
    yes_icon = (
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
        '<path d="M5 12.5l4.5 4.5L19 7.5" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg>'
    )
    no_icon = (
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
        '<path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round"/></svg>'
    )
    cards = []
    for kind, title, text in items:
        icon = yes_icon if kind == "yes" else no_icon
        cards.append(
            f'<div class="tech-verdict__card tech-verdict__card--{kind} reveal">'
            f'<p class="tech-verdict__title"><span class="tech-verdict__mark" aria-hidden="true">{icon}</span>'
            f"{inline_md(title)}</p>"
            f'<p class="tech-verdict__text">{inline_md(text)}</p></div>'
        )
    return f'<div class="tech-verdict">{"".join(cards)}</div>'


def render_eco_map(items: list[tuple[str, str]]) -> str:
    """Карта экосистемы (.tech-eco): пункты маркера {eco-map} вида
    ``- **Инструмент** — выгода бизнесу``."""
    cells = "".join(
        f'<li class="tech-eco__item reveal">'
        f'<p class="tech-eco__name">{inline_md(name)}</p>'
        f'<p class="tech-eco__desc">{inline_md(desc)}</p></li>'
        for name, desc in items
    )
    return f'<ul class="tech-eco" role="list">{cells}</ul>'


# Иконки карточек {rescue-cards} по slug услуги (стиль SERVICE_ICONS:
# контур, viewBox 24×24, stroke 1.6, currentColor). Нет slug — фолбэк-скобки.
RESCUE_ICONS: dict[str, str] = {
    "audit-koda": '<circle cx="11" cy="11" r="6.5" stroke="currentColor" stroke-width="1.6"></circle><path d="M15.8 15.8L21 21" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path><path d="M8.5 10l1.8 1.8 3.2-3.2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>',
    "spasenie-proektov": '<circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.6"></circle><circle cx="12" cy="12" r="3.6" stroke="currentColor" stroke-width="1.6"></circle><path d="M12 3v5.4M12 15.6V21M3 12h5.4M15.6 12H21" stroke="currentColor" stroke-width="1.6"></path>',
    "modernizaciya-legacy": '<path d="M4 11a8 8 0 0113.7-4.7L20 8.5M20 13a8 8 0 01-13.7 4.7L4 15.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path><path d="M20 4v4.5h-4.5M4 20v-4.5h4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>',
    "tehpodderzhka-i-soprovozhdenie": '<path d="M4 13v-2a8 8 0 0116 0v2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path><rect x="2.5" y="13" width="4.5" height="6" rx="2" stroke="currentColor" stroke-width="1.6"></rect><rect x="17" y="13" width="4.5" height="6" rx="2" stroke="currentColor" stroke-width="1.6"></rect><path d="M19 19a5 5 0 01-5 3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path>',
}
_RESCUE_FALLBACK_ICON = '<path d="M8 6l-5.5 6L8 18M16 6l5.5 6L16 18" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>'

_RESCUE_ITEM_RE = re.compile(r"^\*\*\[(?P<title>[^\]]+)\]\((?P<url>/[^)]+)\)\*\*\s*—\s*(?P<desc>.+)$")


def render_rescue_cards(items: list[tuple[str, str, str]]) -> str:
    """Кликабельные карточки услуг блока «чужой код» (.tech-rescue): каждый
    пункт маркера {rescue-cards} — `- **[Название](/uslugi/…/)** — описание`.
    Вся карточка — ссылка; иконка подбирается по slug услуги."""
    arrow = (
        '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
        '<path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg>'
    )
    cards = []
    for title, url, desc in items:
        slug = url.rstrip("/").rsplit("/", 1)[-1]
        icon = RESCUE_ICONS.get(slug, _RESCUE_FALLBACK_ICON)
        cards.append(
            f'<a class="tech-rescue__card reveal" href="{url}">'
            f'<span class="tech-rescue__icon" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none">{icon}</svg></span>'
            f'<span class="tech-rescue__body">'
            f'<span class="tech-rescue__title">{inline_md(title)}<span class="tech-rescue__arrow">{arrow}</span></span>'
            f'<span class="tech-rescue__desc">{inline_md(desc)}</span></span></a>'
        )
    return f'<div class="tech-rescue">{"".join(cards)}</div>'


def render_staff_panel(stats: list[tuple[str, str]], formats: list[tuple[str, str]]) -> str:
    """Панель аутстаффинга (.tech-staff): сверху три ключевых условия крупными
    цифрами, ниже — две кликабельные карточки форматов работы."""
    stat_html = "".join(
        f'<div class="tech-staff__stat">'
        f'<p class="tech-staff__value">{inline_md(value)}</p>'
        f'<p class="tech-staff__label">{inline_md(label)}</p></div>'
        for value, label in stats
    )
    arrow = (
        '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
        '<path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg>'
    )
    fmt_html = ""
    for link_md, desc in formats:
        m = re.match(r"^\[(?P<name>[^\]]+)\]\((?P<url>/[^)]+)\)$", link_md.strip())
        if not m:
            raise ValueError(f"{{staff-panel}}: format ожидает '[Название](/путь/)', получено: {link_md!r}")
        fmt_html += (
            f'<a class="tech-staff__format reveal" href="{m.group("url")}">'
            f'<span class="tech-staff__format-name">{inline_md(m.group("name"))}<span class="tech-staff__format-arrow">{arrow}</span></span>'
            f'<span class="tech-staff__format-desc">{inline_md(desc)}</span></a>'
        )
    return (
        f'<div class="tech-staff reveal">'
        f'<div class="tech-staff__stats">{stat_html}</div>'
        f'<div class="tech-staff__formats">{fmt_html}</div></div>'
    )


def render_steps(items: list[tuple[str, str]]) -> str:
    """Таймлайн старта (.tech-steps): нумерованные карточки «01 → 02 → 03» из
    списка после маркера {steps} (`1. **Заголовок** — текст`)."""
    cards = []
    for i, (title, text) in enumerate(items, start=1):
        text = text[:1].upper() + text[1:] if text else text
        cards.append(
            f'<li class="tech-steps__item reveal">'
            f'<span class="tech-steps__num" aria-hidden="true">{i:02d}</span>'
            f'<p class="tech-steps__title">{inline_md(title)}</p>'
            f'<p class="tech-steps__text">{inline_md(text)}</p></li>'
        )
    return f'<ol class="tech-steps" role="list">{"".join(cards)}</ol>'


def render_price_models(rows: list[list[str]]) -> str:
    """Две равноправные модели цены (.tech-price-models). Колонки таблицы
    после маркера {price-models}: «Модель | Условия | Кому подходит | Подробнее»."""
    cards = []
    for row in rows:
        name, value, desc, link = (c.strip() for c in row[:4])
        cards.append(
            f'<div class="tech-price-model reveal">'
            f'<p class="tech-price-model__name">{inline_md(name)}</p>'
            f'<p class="tech-price-model__value">{inline_md(value)}</p>'
            f'<p class="tech-price-model__desc">{inline_md(desc)}</p>'
            f'<p class="tech-price-model__link">{inline_md(link)} →</p></div>'
        )
    return f'<div class="tech-price-models">{"".join(cards)}</div>'


def tech_body_to_html(body: str) -> str:
    """Тело секции стека → HTML: спец-маркеры раздела рендерятся здесь,
    остальные фрагменты — md_body_to_html (порядок блоков сохраняется)."""
    lines = body.split("\n")
    parts: list[str] = []
    md_buf: list[str] = []

    def flush() -> None:
        chunk = "\n".join(md_buf).strip()
        md_buf.clear()
        if chunk:
            parts.append(md_body_to_html(chunk))

    i = 0
    while i < len(lines):
        stripped = lines[i].strip()

        if stripped == "{verdict-cards}":
            flush()
            i += 1
            items: list[tuple[str, str, str]] = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                pieces = [p.strip() for p in lines[i].strip()[2:].split("::", 2)]
                if len(pieces) != 3 or pieces[0] not in ("yes", "no"):
                    raise ValueError(f"{{verdict-cards}}: ожидался формат 'yes|no :: Заголовок :: Текст', получено: {lines[i]!r}")
                items.append((pieces[0], pieces[1], pieces[2]))
                i += 1
            parts.append(render_verdict_cards(items))
            continue

        if stripped == "{eco-map}":
            flush()
            i += 1
            eco: list[tuple[str, str]] = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                m = re.match(r"^\*\*(?P<name>.+?)\*\*\s*—\s*(?P<desc>.+)$", lines[i].strip()[2:])
                if not m:
                    raise ValueError(f"{{eco-map}}: ожидался пункт '- **Инструмент** — выгода', получено: {lines[i]!r}")
                eco.append((m.group("name"), m.group("desc")))
                i += 1
            parts.append(render_eco_map(eco))
            continue

        if stripped == "{price-models}":
            flush()
            i += 1
            if not (i + 1 < len(lines) and lines[i].strip().startswith("|")):
                raise ValueError("{price-models}: после маркера ожидалась MD-таблица")
            i += 2  # заголовок таблицы (документация) + разделитель |---|
            rows: list[list[str]] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            parts.append(render_price_models(rows))
            continue

        if stripped == "{rescue-cards}":
            flush()
            i += 1
            rescue: list[tuple[str, str, str]] = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                m = _RESCUE_ITEM_RE.match(lines[i].strip()[2:])
                if not m:
                    raise ValueError(f"{{rescue-cards}}: ожидался пункт '- **[Название](/путь/)** — описание', получено: {lines[i]!r}")
                rescue.append((m.group("title"), m.group("url"), m.group("desc")))
                i += 1
            parts.append(render_rescue_cards(rescue))
            continue

        if stripped == "{staff-panel}":
            flush()
            i += 1
            stats: list[tuple[str, str]] = []
            formats: list[tuple[str, str]] = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                pieces = [p.strip() for p in lines[i].strip()[2:].split("::", 2)]
                if len(pieces) != 3 or pieces[0] not in ("stat", "format"):
                    raise ValueError(f"{{staff-panel}}: ожидалось 'stat|format :: … :: …', получено: {lines[i]!r}")
                (stats if pieces[0] == "stat" else formats).append((pieces[1], pieces[2]))
                i += 1
            if not stats or not formats:
                raise ValueError("{staff-panel}: нужны и stat-, и format-строки")
            parts.append(render_staff_panel(stats, formats))
            continue

        if stripped == "{steps}":
            flush()
            i += 1
            steps: list[tuple[str, str]] = []
            while i < len(lines) and re.match(r"^\d+\.\s+", lines[i].strip()):
                item = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                m = re.match(r"^\*\*(?P<title>.+?)\*\*\s*—\s*(?P<text>.+)$", item)
                if not m:
                    raise ValueError(f"{{steps}}: ожидался пункт '1. **Заголовок** — текст', получено: {lines[i]!r}")
                steps.append((m.group("title"), m.group("text")))
                i += 1
            parts.append(render_steps(steps))
            continue

        md_buf.append(lines[i])
        i += 1

    flush()
    return "\n".join(parts)


def _parse_faq(faq_raw: str) -> list[tuple[str, str]]:
    """FAQ секции стека: вопрос — `**жирная строка**`, ответ — абзац ниже."""
    items = re.findall(r"\*\*(.+?)\*\*\n(.+?)(?=\n\s*\n\*\*|\s*\Z)", faq_raw.strip(), re.S)
    return [(q.strip(), re.sub(r"\s+", " ", a).strip()) for q, a in items]


def _meta_field(chunk: str, name: str, slug: str) -> str:
    m = re.search(rf"\*\*{name}:\*\*\s*(.+)", chunk)
    if not m:
        raise ValueError(f"Секция {slug}: нет обязательного поля **{name}:**")
    return m.group(1).strip()


def parse_texts_tehnologii(path: Path = TEXTS_TEHNOLOGII_MD) -> list[TechPage]:
    raw = path.read_text(encoding="utf-8")
    sections = re.split(r"\n## \d+\.\s+", raw)
    pages: list[TechPage] = []

    for idx, chunk in enumerate(sections[1:], start=1):
        if idx > len(TECH_META):
            break
        meta = TECH_META[idx - 1]
        slug = meta["slug"]

        title = _meta_field(chunk, "Title", slug)
        description = _meta_field(chunk, "Description", slug)
        h1 = _meta_field(chunk, "H1", slug)
        facts_raw = _meta_field(chunk, "Facts", slug)
        cta_raw = _meta_field(chunk, "CTA", slug)

        facts: list[tuple[str, str]] = []
        for item in facts_raw.split("·"):
            if not item.strip():
                continue
            if "::" not in item:
                raise ValueError(f"Секция {slug}: факт должен быть 'цифра :: подпись', получено: {item!r}")
            num, label = (p.strip() for p in item.split("::", 1))
            facts.append((num, label))

        cta_parts = [p.strip() for p in cta_raw.split("::", 2)]
        if len(cta_parts) != 3:
            raise ValueError(f"Секция {slug}: CTA должен быть 'заголовок :: кнопка :: подпись'")

        cta_m = re.search(r"\*\*CTA:\*\*\s*.+", chunk)
        body = chunk[cta_m.end():].strip()

        faq_split = re.split(r"\n### FAQ\s*\n", body, maxsplit=1)
        if len(faq_split) != 2:
            raise ValueError(f"Секция {slug}: нет подсекции '### FAQ'")
        body, faq_raw = faq_split[0].strip(), faq_split[1]
        faq = _parse_faq(faq_raw)
        if not faq:
            raise ValueError(f"Секция {slug}: FAQ пуст")

        # Лид (подзаголовок H1, → .section-lead) — первый абзац тела до блоков.
        lead = ""
        lead_m = re.match(r"^(?!\{|#|\||[-*]\s|\d+\.\s)(.+?)(?:\n\s*\n|\Z)", body, re.S)
        if lead_m:
            lead = inline_md(re.sub(r"\s+", " ", lead_m.group(1)))
            body = body[lead_m.end():].strip()

        pages.append(
            TechPage(
                slug=slug,
                menu_label=meta["menu_label"],
                menu_desc=meta["menu_desc"],
                service_type=meta["service_type"],
                low_price=meta["low_price"],
                hub_what=meta["hub_what"],
                hub_term=meta["hub_term"],
                hub_price=meta["hub_price"],
                meta_title=title,
                h1=h1,
                description=description,
                facts=facts,
                intro_image=meta["intro_image"],
                intro_alt=meta["intro_alt"],
                cta=(cta_parts[0], cta_parts[1], cta_parts[2]),
                lead=lead,
                body_html=tech_body_to_html(body),
                faq=faq,
            )
        )

    if len(pages) != len(TECH_META):
        raise ValueError(f"Ожидалось {len(TECH_META)} стеков, получено {len(pages)}")
    return pages
