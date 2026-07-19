#!/usr/bin/env python3
"""Отправка URL сайта в IndexNow (Яндекс + Bing/Seznam через общий эндпоинт).

Зачем: Яндекс перечитывает sitemap неделями (в июле 2026 файл висел в очереди
на переобход с 07.07 по 19.07), а ручной «Переобход страниц» в Вебмастере
ограничен 150 адресами в сутки. IndexNow уведомляет о новых и изменённых
страницах сразу.

Порядок запуска:
  1. Ключевой файл 24998a1f02ad5271e85b130b3a22a445.txt должен быть ЗАДЕПЛОЕН
     и отдавать 200 по https://www.budget-soft.ru/<key>.txt — до этого
     эндпоинт ответит 403 и все URL будут отброшены.
  2. python _indexnow_ping.py            — отправить все URL из sitemap.xml
     python _indexnow_ping.py /uslugi/pentest/ /tehnologii/react/
                                          — отправить только указанные пути

Ответ 200/202 — принято. 403 — ключевой файл не найден или не совпадает.
422 — URL не соответствуют домену ключа.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HOST = "www.budget-soft.ru"
KEY = "24998a1f02ad5271e85b130b3a22a445"
ENDPOINT = "https://api.indexnow.org/indexnow"


def urls_from_sitemap() -> list[str]:
    xml = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    return re.findall(r"<loc>(.*?)</loc>", xml)


def main() -> int:
    if len(sys.argv) > 1:
        urls = [f"https://{HOST}{p if p.startswith('/') else '/' + p}" for p in sys.argv[1:]]
    else:
        urls = urls_from_sitemap()

    if not urls:
        print("Нет URL для отправки")
        return 1

    payload = json.dumps(
        {"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls},
        ensure_ascii=False,
    ).encode("utf-8")

    req = urllib.request.Request(
        ENDPOINT,
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"HTTP {resp.status} — отправлено URL: {len(urls)}")
            body = resp.read().decode("utf-8", "replace").strip()
            if body:
                print(body)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace").strip()
        print(f"HTTP {e.code} — {e.reason}")
        if e.code == 403:
            print(f"Ключевой файл не подтверждён. Проверь: https://{HOST}/{KEY}.txt")
        if body:
            print(body)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
