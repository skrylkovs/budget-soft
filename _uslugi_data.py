"""Данные и парсинг docs/texts-usligi.md для генератора страниц."""
from __future__ import annotations

import html
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).parent
TEXTS_USLUGI_MD = ROOT / "docs" / "texts-usligi.md"

# Slug и короткая подпись в меню для 15 посадочных (порядок = номер в MD)
SERVICE_META: list[tuple[str, str]] = [
    ("razrabotka-erp-sistem", "ERP-системы"),
    ("razrabotka-crm-sistem", "CRM-системы"),
    ("iskusstvennyj-intellekt", "Внедрение ИИ"),
    ("mobilnaya-razrabotka", "Мобильная разработка"),
    ("telegram-mini-apps", "Telegram Mini Apps"),
    ("scm-upravlenie-postavkami", "SCM и WMS"),
    ("bi-big-data", "BI и Big Data"),
    ("razrabotka-saas", "SaaS-платформы"),
    ("razrabotka-internet-magazinov", "Интернет-магазины"),
    ("razrabotka-marketplejsov", "Маркетплейсы"),
    ("avtomatizaciya-biznesa", "Автоматизация бизнеса"),
    ("digital-health", "Digital Health / МИС"),
    ("fintech", "FinTech"),
    ("blockchain-web3", "Блокчейн и Web3"),
    ("it-autstaffing", "IT-аутстаффинг"),
]

# Быстрые ссылки в полосе направлений (6 шт.)
DIRECTION_STRIP_SLUGS = (
    "razrabotka-erp-sistem",
    "razrabotka-crm-sistem",
    "iskusstvennyj-intellekt",
    "mobilnaya-razrabotka",
    "telegram-mini-apps",
    "digital-health",
)

SERVICE_ICONS: dict[str, str] = {
    "razrabotka-erp-sistem": '<path d="M4 21V7l8-4 8 4v14M4 21h16M9 21V12h6v9M9 8h.01M12 8h.01M15 8h.01" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>',
    "razrabotka-crm-sistem": '<path d="M3 3v18h18M7 14l4-4 4 4 5-5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>',
    "iskusstvennyj-intellekt": '<path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2M12 8a4 4 0 100 8 4 4 0 000-8z" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path>',
    "mobilnaya-razrabotka": '<rect x="7" y="2" width="10" height="20" rx="2" stroke="currentColor" stroke-width="1.6"></rect><path d="M11 18h2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path>',
    "telegram-mini-apps": '<path d="M21.5 4.5L2 12l6 2 2 6 4-4 6 5 1.5-16.5z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"></path>',
    "scm-upravlenie-postavkami": '<path d="M3 7h18M3 12h12M3 17h8M16 17l3 3 3-3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>',
    "bi-big-data": '<path d="M4 19V5M4 19h16M8 15v-4M12 19V9M16 13V7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path>',
    "razrabotka-saas": '<path d="M4 7h16v10H4zM8 7V5h8v2" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"></path><path d="M12 12h.01" stroke="currentColor" stroke-width="2" stroke-linecap="round"></path>',
    "razrabotka-internet-magazinov": '<path d="M6 6h15l-1.5 9h-12zM6 6l-2-2H2M9 20a1 1 0 100-2 1 1 0 000 2zm8 0a1 1 0 100-2 1 1 0 000 2z" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>',
    "razrabotka-marketplejsov": '<rect x="3" y="3" width="7" height="7" rx="1" stroke="currentColor" stroke-width="1.6"/><rect x="14" y="3" width="7" height="7" rx="1" stroke="currentColor" stroke-width="1.6"/><rect x="3" y="14" width="7" height="7" rx="1" stroke="currentColor" stroke-width="1.6"/><rect x="14" y="14" width="7" height="7" rx="1" stroke="currentColor" stroke-width="1.6"/>',
    "avtomatizaciya-biznesa": '<circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="1.6"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path>',
    "digital-health": '<path d="M12 21s-7-4.5-7-10a4 4 0 017-2 4 4 0 017 2c0 5.5-7 10-7 10z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M12 11v4M10 13h4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path>',
    "fintech": '<path d="M12 3v18M8 7h8M7 11h10M6 15h12" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path>',
    "blockchain-web3": '<path d="M6 8h12v8H6zM9 8V5h6v3M9 16v3h6v-3" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"></path>',
    "it-autstaffing": '<circle cx="9" cy="8" r="3" stroke="currentColor" stroke-width="1.6"/><path d="M3 20c0-3.3 2.7-6 6-6M16 11h5M16 15h5M16 19h5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path>',
}

DIRECTION_ICONS: dict[str, str] = {
    "razrabotka-erp-sistem": """<rect x="10" y="10" width="30" height="30" rx="2" stroke="currentColor" stroke-width="1.6"/>
                  <rect x="22" y="22" width="30" height="30" rx="2" fill="#fff" stroke="currentColor" stroke-width="1.6"/>""",
    "razrabotka-crm-sistem": """<circle cx="30" cy="30" r="22" stroke="currentColor" stroke-width="1.6"/>
                  <text x="30" y="34" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="currentColor">CRM</text>""",
    "iskusstvennyj-intellekt": """<path d="M28 12 C22 10 16 13 15 19 C10 21 10 27 14 30 C11 34 14 40 19 40 C20 45 27 46 28 41 L28 12 Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>
                  <path d="M28 20 L28 33" stroke="currentColor" stroke-width="1.6"/>
                  <path d="M32 16 L40 16" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
                  <circle cx="44" cy="16" r="2.5" stroke="currentColor" stroke-width="1.6"/>""",
    "mobilnaya-razrabotka": """<rect x="18" y="8" width="24" height="44" rx="3" stroke="currentColor" stroke-width="1.6"/>
                  <rect x="22" y="20" width="4" height="4" stroke="currentColor" stroke-width="1.4"/>
                  <rect x="28" y="20" width="4" height="4" stroke="currentColor" stroke-width="1.4"/>
                  <rect x="34" y="20" width="4" height="4" stroke="currentColor" stroke-width="1.4"/>""",
    "telegram-mini-apps": """<path d="M10 29.5L46 15.5L39.5 44.5L27.5 35.5L21 42L22.5 32.5L10 29.5Z" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
                  <path d="M22.5 32.5L31 24" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>""",
    "digital-health": """<path d="M30 14 L30 38 M22 22 L38 22 M22 30 L38 30" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
                  <circle cx="30" cy="30" r="18" stroke="currentColor" stroke-width="1.6"/>""",
}


@dataclass
class ServicePage:
    slug: str
    menu_label: str
    meta_title: str
    h1: str
    lead: str
    body_html: str
    description: str


def inline_md(text: str) -> str:
    text = html.escape(text.strip())
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    return text


def md_body_to_html(body: str) -> str:
    lines = body.strip().split("\n")
    parts: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped or stripped == "---":
            i += 1
            continue

        if stripped.startswith("### "):
            parts.append(
                f'<h4 class="page-prose__heading">{inline_md(stripped[4:])}</h4>'
            )
            i += 1
            continue

        if stripped.startswith("#### "):
            parts.append(
                f'<h4 class="page-prose__heading">{inline_md(stripped[5:])}</h4>'
            )
            i += 1
            continue

        if stripped.startswith("```"):
            code_lines: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(html.escape(lines[i]))
                i += 1
            if i < len(lines):
                i += 1
            parts.append(
                f'<pre class="page-prose__diagram"><code>{"<br>".join(code_lines)}</code></pre>'
            )
            continue

        if stripped.startswith("|") and i + 1 < len(lines) and re.match(
            r"^\|[-\s|:]+\|$", lines[i + 1].strip()
        ):
            header_cells = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows: list[list[str]] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(
                    [c.strip() for c in lines[i].strip().strip("|").split("|")]
                )
                i += 1
            thead = "".join(f"<th>{inline_md(c)}</th>" for c in header_cells)
            tbody_rows = []
            for row in rows:
                cells = "".join(
                    (
                        f"<th scope=\"row\">{inline_md(c)}</th>"
                        if j == 0
                        else f"<td>{inline_md(c)}</td>"
                    )
                    for j, c in enumerate(row)
                )
                tbody_rows.append(f"<tr>{cells}</tr>")
            parts.append(
                f'<div class="page-service-table"><table class="page-service-table__table">'
                f"<thead><tr>{thead}</tr></thead>"
                f"<tbody>{''.join(tbody_rows)}</tbody></table></div>"
            )
            continue

        if stripped.startswith("> "):
            quote_lines: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("> "):
                quote_lines.append(lines[i].strip()[2:])
                i += 1
            parts.append(
                f'<blockquote class="page-prose__quote"><p>{inline_md(" ".join(quote_lines))}</p></blockquote>'
            )
            continue

        if re.match(r"^[*\-]\s+", stripped):
            items: list[str] = []
            while i < len(lines) and re.match(
                r"^[*\-]\s+", lines[i].strip()
            ):
                item_text = re.sub(r"^[*\-]\s+", "", lines[i].strip())
                items.append(f"<li>{inline_md(item_text)}</li>")
                i += 1
            parts.append(f'<ul class="page-prose__list">{"".join(items)}</ul>')
            continue

        if re.match(r"^\d+\.\s+", stripped):
            items = []
            while i < len(lines) and re.match(
                r"^\d+\.\s+", lines[i].strip()
            ):
                item_text = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                items.append(f"<li>{inline_md(item_text)}</li>")
                i += 1
            parts.append(
                f'<ol class="page-prose__list page-prose__list--num">{"".join(items)}</ol>'
            )
            continue

        para_lines = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if (
                not nxt
                or nxt.startswith("#")
                or nxt.startswith("```")
                or nxt.startswith("|")
                or nxt.startswith(">")
                or re.match(r"^[*\-]\s+", nxt)
                or re.match(r"^\d+\.\s+", nxt)
            ):
                break
            para_lines.append(nxt)
            i += 1
        parts.append(f"<p>{inline_md(' '.join(para_lines))}</p>")

    return "\n".join(parts)


def parse_texts_uslugi(path: Path = TEXTS_USLUGI_MD) -> list[ServicePage]:
    raw = path.read_text(encoding="utf-8")
    sections = re.split(r"\n## \d+\.\s+", raw)
    pages: list[ServicePage] = []

    for idx, chunk in enumerate(sections[1:], start=1):
        if idx > len(SERVICE_META):
            break
        slug, menu_label = SERVICE_META[idx - 1]

        title_m = re.search(r"\*\*Title:\*\*\s*(.+)", chunk)
        h1_m = re.search(r"\*\*H1:\*\*\s*(.+)", chunk)
        if not title_m or not h1_m:
            raise ValueError(f"Секция {idx}: нет Title или H1")

        body_start = chunk.find("\n\n", h1_m.end())
        body = chunk[body_start:].strip()
        body = re.split(r"\n### 💡", body, maxsplit=1)[0].strip()
        body = re.sub(r"^---\s*$", "", body, flags=re.MULTILINE).strip()

        body_html = md_body_to_html(body)
        lead_m = re.search(r"<p>(.+?)</p>", body_html)
        lead = re.sub(r"<[^>]+>", "", lead_m.group(1)) if lead_m else ""

        pages.append(
            ServicePage(
                slug=slug,
                menu_label=menu_label,
                meta_title=title_m.group(1).strip(),
                h1=h1_m.group(1).strip(),
                lead=lead[:280] + ("…" if len(lead) > 280 else ""),
                body_html=body_html,
            )
        )

    if len(pages) != len(SERVICE_META):
        raise ValueError(f"Ожидалось {len(SERVICE_META)} услуг, получено {len(pages)}")
    return pages


def services_as_tuples() -> list[tuple[str, str, str, str]]:
    """Формат для совместимости: slug, label, heading, body."""
    return [
        (p.slug, p.menu_label, p.h1, p.body_html)
        for p in parse_texts_uslugi()
    ]
