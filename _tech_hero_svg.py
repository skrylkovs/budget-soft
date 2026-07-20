"""Генератор интро-картинок стековых лендингов /tehnologii/ (31 стек).

Рисует композицию исходного плейсхолдера laravel-hero.png — тёмная сетка,
водяной знак </>, окно код-редактора, статус-строки и три тега, — но
содержимое своё для каждого стека: имя файла, подсвеченный сниппет на языке
стека и теги. Формат SVG: вектор чёток на любом экране и весит ~5 КБ против
52 КБ у PNG.

Запуск: python _tech_hero_svg.py  → пишет images/tech/<slug>-hero.svg.
Подключение: поле intro_image в TECH_META (_tehnologii_data.py) указывает на
.svg, дальше обычный python _generate_pages.py.

Палитра синхронизирована с тёмной системой .tech-* в page.css: фон #101018,
неон-циан #22d3ee, фиолетовый #8b7bff.

Числа в статус-строках (tests: N passed, p99, вес бандла) — декоративная
часть мокапа, как и в исходном плейсхолдере: это стилизованный экран IDE,
а не заявление о конкретном проекте. Версии стеков в тегах сверены с
текстами самих страниц либо являются объективным фактом о платформе
(LTS-релизы), выдуманных версий здесь нет.
"""
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "images" / "tech"

# --- палитра ---------------------------------------------------------------
BG        = "#0E1018"
CARD_HEAD = "#242a3c"
CARD_BODY = "#1c2131"
DOT_V     = "#8b7bff"
DOT_C     = "#22d3ee"
DOT_G     = "#4a5169"
FILENAME  = "#8b93a8"
CYAN      = "#22d3ee"
VIOLET    = "#a78bfa"
STRING    = "#86e1fc"
PLAIN     = "#c9d1e4"
SKELETON  = "#3a4055"
MUTED     = "#6b7488"

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "Inter, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif"

# --- геометрия (viewBox 640×480) -------------------------------------------
# Картинка тянется object-fit: cover в колонку .tech-intro__media, а пропорции
# этой колонки гуляют очень широко:
#   десктоп  ~560×326 (1.72:1)
#   планшет   734×240 (3.06:1)  — полоса во всю ширину, min-height 240px
#   телефон   326×240 (1.36:1)
# Одного «правильного» аспекта тут не существует: при любом формате часть кадра
# срезается — где-то по высоте, где-то по бокам. Поэтому раскладка строится не
# по краям картинки, а по ПЕРЕСЕЧЕНИЮ видимых зон всех трёх случаев.
#
# Перебор по H показал: высота пересечения всегда ≈209px (её задаёт планшет —
# самый широкий контейнер), а ширина растёт вместе с H и при H >= 480 занимает
# весь кадр. Отсюда 640×480: по горизонтали безопасен весь кадр, по вертикали
# видно y ∈ [136, 344] (жёсткий случай — планшет). Контент держим в [142, 338].
#
# Исходный плейсхолдер был вертикальным (640×720) — из-за этого ряд тегов внизу
# не было видно НИКОГДА, ни на одном разрешении.
# Меняешь раскладку — пересчитай зону (скрипт перебора описан выше).
SAFE_TOP, SAFE_BOTTOM = 142, 338

CARD_X, CARD_Y, CARD_W, CARD_H = 40, 142, 560, 148
CODE_X = CARD_X + 28
HEAD_H = 32
TAG_Y, TAG_H, TAG_GAP = 302, 32, 12


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def tspans(parts):
    return "".join(
        f'<tspan fill="{c}" xml:space="preserve">{esc(t)}</tspan>' for t, c in parts
    )


def text_w(s: str, size: int = 14) -> float:
    """Оценка ширины строки пропорциональным шрифтом (для плашек тегов).
    Точных метрик без рендера нет, поэтому таблица приближённых ширин."""
    total = 0.0
    for ch in s:
        if ch == " ":
            total += 0.28
        elif ch in "·.,:;":
            total += 0.30
        elif ch in "iljtfrI|!()":
            total += 0.32
        elif ch.isdigit():
            total += 0.58
        elif ch.isupper():
            total += 0.66
        else:
            total += 0.55
    return total * size


def tag_width(label: str) -> int:
    return int(text_w(label) + 26)


# --- спецификации стеков ---------------------------------------------------
# file   — имя файла в шапке окна редактора
# code   — две строки, каждая = список (кусок текста, цвет) для подсветки
# status — («✓ …» циан, «➜ …» приглушённый)
# tags   — три тега: акцентный циан / белый / приглушённый
S = {}

S["laravel"] = dict(
    file="routes/web.php",
    code=[[("Route", VIOLET), ("::", PLAIN), ("get", CYAN), ("(", PLAIN), ("'/orders'", STRING), (", fn() =>", PLAIN)],
          [("    Order", VIOLET), ("::", PLAIN), ("paginate", CYAN), ("());", PLAIN)]],
    status=("pest: 148 passed", "deploy: production ready"),
    tags=["Laravel 11+", "PHP 8+", "SaaS · Магазины · API"])

S["python"] = dict(
    file="main.py",
    code=[[("@app", VIOLET), (".", PLAIN), ("get", CYAN), ("(", PLAIN), ('"/api/report"', STRING), (")", PLAIN)],
          [("async def ", VIOLET), ("report", CYAN), ("() -> ", PLAIN), ("Report", VIOLET), (":", PLAIN)]],
    status=("pytest: 173 passed", "deploy: docker · gunicorn"),
    tags=["Python 3.11+", "FastAPI · Django", "ИИ · Аналитика"])

S["react"] = dict(
    file="Dashboard.tsx",
    code=[[("export function ", VIOLET), ("Dashboard", CYAN), ("() {", PLAIN)],
          [("  return ", VIOLET), ("<Orders ", CYAN), ("live", STRING), (" />;", CYAN)]],
    status=("vitest: 186 passed", "build: 92 kB gzip"),
    tags=["React 19", "TypeScript 5", "SPA · Кабинеты"])

S["nodejs"] = dict(
    file="server.js",
    code=[[("app", PLAIN), (".", PLAIN), ("get", CYAN), ("(", PLAIN), ('"/api/feed"', STRING), (", ", PLAIN), ("async", VIOLET), (" (req, res)", PLAIN)],
          [("  => res.", PLAIN), ("json", CYAN), ("(feed));", PLAIN)]],
    status=("jest: 192 passed", "runtime: pm2 · docker"),
    tags=["Node.js LTS", "Express · Fastify", "API · Real-time"])

S["vue"] = dict(
    file="OrdersView.vue",
    code=[[("const ", VIOLET), ("orders", PLAIN), (" = ", PLAIN), ("ref", CYAN), ("([]);", PLAIN)],
          [("watch", CYAN), ("(query, ", PLAIN), ("load", CYAN), (");", PLAIN)]],
    status=("vitest: 164 passed", "build: 78 kB gzip"),
    tags=["Vue 3", "Composition API", "SPA · Кабинеты"])

S["flutter"] = dict(
    file="main.dart",
    code=[[("Widget ", VIOLET), ("build", CYAN), ("(", PLAIN), ("BuildContext", VIOLET), (" ctx) {", PLAIN)],
          [("  return ", VIOLET), ("OrdersView", CYAN), ("();", PLAIN)]],
    status=("flutter test: 128 passed", "build: iOS · Android"),
    tags=["Flutter 3+", "Dart 3", "iOS + Android"])

S["react-native"] = dict(
    file="App.tsx",
    code=[[("export default function ", VIOLET), ("App", CYAN), ("()", PLAIN)],
          [("  return ", VIOLET), ("<OrdersScreen />;", CYAN)]],
    status=("detox: 96 passed", "release: App Store · Google Play"),
    tags=["React Native", "Expo", "iOS + Android"])

S["kotlin"] = dict(
    file="OrderService.kt",
    code=[[("suspend fun ", VIOLET), ("load", CYAN), ("(): ", PLAIN), ("List", VIOLET), ("<Order> =", PLAIN)],
          [("    repo.", PLAIN), ("fetch", CYAN), ("().", PLAIN), ("await", CYAN), ("()", PLAIN)]],
    status=("junit: 154 passed", "target: android · jvm"),
    tags=["Kotlin", "Coroutines · Compose", "Мобайл · Бэкенд"])

S["swift"] = dict(
    file="OrdersView.swift",
    code=[[("struct ", VIOLET), ("OrdersView", CYAN), (": ", PLAIN), ("View", VIOLET), (" {", PLAIN)],
          [("  var body: ", PLAIN), ("some View", VIOLET), (" { … }", PLAIN)]],
    status=("xctest: 118 passed", "release: App Store ready"),
    tags=["Swift 5+", "SwiftUI", "iPhone · iPad"])

S["angular"] = dict(
    file="orders.component.ts",
    code=[[("@Component", VIOLET), ("({ standalone: ", PLAIN), ("true", CYAN), (" })", PLAIN)],
          [("export class ", VIOLET), ("OrdersCmp", CYAN), (" {}", PLAIN)]],
    status=("karma: 176 passed", "build: aot · ivy"),
    tags=["Angular 17+", "TypeScript 5+", "Корпоративные SPA"])

S["typescript"] = dict(
    file="api.ts",
    code=[[("export type ", VIOLET), ("Order", CYAN), (" = {", PLAIN)],
          [("  id: ", PLAIN), ("string", VIOLET), ("; total: ", PLAIN), ("number", VIOLET), (";", PLAIN)]],
    status=("tsc: 0 errors", "strict: true"),
    tags=["TypeScript 5+", "Strict mode", "SPA · SaaS · API"])

S["golang"] = dict(
    file="main.go",
    code=[[("func ", VIOLET), ("orders", CYAN), ("(c ", PLAIN), ("*gin", VIOLET), (".Context) {", PLAIN)],
          [("  c.", PLAIN), ("JSON", CYAN), ("(200, list)", PLAIN)]],
    status=("go test: 208 passed", "p99: 12 ms · 8k rps"),
    tags=["Go 1.22+", "Горутины", "Микросервисы"])

S["java"] = dict(
    file="OrderService.java",
    code=[[("@RestController", VIOLET)],
          [("public ", VIOLET), ("List", VIOLET), ("<Order> ", PLAIN), ("all", CYAN), ("() {", PLAIN)]],
    status=("junit: 246 passed", "jvm: g1gc · 8k rps"),
    tags=["Java 17+ LTS", "Spring Boot", "Highload · Enterprise"])

S["dotnet"] = dict(
    file="Program.cs",
    code=[[("app", PLAIN), (".", PLAIN), ("MapGet", CYAN), ("(", PLAIN), ('"/api/orders"', STRING), (",", PLAIN)],
          [("    () => ", PLAIN), ("Results", VIOLET), (".", PLAIN), ("Ok", CYAN), ("(orders));", PLAIN)]],
    status=("dotnet test: 214 passed", "deploy: linux · postgresql"),
    tags=[".NET 8 LTS", "C# 12", "ERP · CRM · API"])

S["php"] = dict(
    file="OrderController.php",
    code=[[("public function ", VIOLET), ("index", CYAN), ("()", PLAIN)],
          [("    return ", VIOLET), ("Order", VIOLET), ("::", PLAIN), ("all", CYAN), ("();", PLAIN)]],
    status=("phpunit: 186 passed", "php-fpm: opcache on"),
    tags=["PHP 8+", "Laravel · Symfony", "Сайты · CRM · API"])

S["symfony"] = dict(
    file="OrderController.php",
    code=[[("#[Route(", VIOLET), ("'/orders'", STRING), (")]", VIOLET)],
          [("public function ", VIOLET), ("list", CYAN), ("()", PLAIN)]],
    status=("phpunit: 204 passed", "cache: warm · prod"),
    tags=["Symfony 7", "PHP 8.2+", "Порталы · CRM/ERP"])

S["yii"] = dict(
    file="OrderController.php",
    code=[[("public function ", VIOLET), ("actionIndex", CYAN), ("()", PLAIN)],
          [("  return ", VIOLET), ("Order", VIOLET), ("::", PLAIN), ("find", CYAN), ("()->all();", PLAIN)]],
    status=("codeception: 142 passed", "1С: обмен настроен"),
    tags=["Yii 2.0", "PHP 8+", "Порталы · CRM · 1С"])

S["wordpress"] = dict(
    file="functions.php",
    code=[[("add_action", CYAN), ("(", PLAIN), ("'init'", STRING), (", ", PLAIN), ("'setup'", STRING), (");", PLAIN)],
          [("register_post_type", CYAN), ("(", PLAIN), ("'case'", STRING), (");", PLAIN)]],
    status=("lighthouse: 96 / 100", "woo: заказы · оплата"),
    tags=["WordPress 6+", "PHP 8+", "Сайты · Магазины"])

S["bitrix"] = dict(
    file="init.php",
    code=[[("AddEventHandler", CYAN), ("(", PLAIN), ("'sale'", STRING), (",", PLAIN)],
          [("  ", PLAIN), ("'OnOrderAdd'", STRING), (", ", PLAIN), ("'syncTo1C'", STRING), (");", PLAIN)]],
    status=("phpunit: 118 passed", "1С: обмен заказами"),
    tags=["1С-Битрикс", "D7 · Composer", "Сайты · Порталы"])

S["drupal"] = dict(
    file="orders.module",
    code=[[("function ", VIOLET), ("orders_view", CYAN), ("(&$build)", PLAIN)],
          [("  $build[", PLAIN), ("'#cache'", STRING), ("] = $tags;", PLAIN)]],
    status=("phpunit: 132 passed", "cache: bigpipe · cdn"),
    tags=["Drupal 10", "PHP 8+", "Порталы · Контент"])

S["django"] = dict(
    file="views.py",
    code=[[("class ", VIOLET), ("OrderViewSet", CYAN), ("(", PLAIN), ("ModelViewSet", VIOLET), ("):", PLAIN)],
          [("  queryset = ", PLAIN), ("Order", VIOLET), (".objects.", PLAIN), ("all", CYAN), ("()", PLAIN)]],
    status=("pytest: 218 passed", "migrations: 0 pending"),
    tags=["Django 5+", "Python 3.12+", "Сайты · API · SaaS"])

S["fastapi"] = dict(
    file="routers/orders.py",
    code=[[("@router", VIOLET), (".", PLAIN), ("get", CYAN), ("(", PLAIN), ('"/orders"', STRING), (")", PLAIN)],
          [("async def ", VIOLET), ("list_orders", CYAN), ("():", PLAIN)]],
    status=("pytest: 196 passed", "p99: 18 ms · async"),
    tags=["FastAPI", "Python 3.11+", "REST · GraphQL"])

S["nextjs"] = dict(
    file="app/page.tsx",
    code=[[("export default async function ", VIOLET), ("Page", CYAN)],
          [("  const orders = ", PLAIN), ("await ", VIOLET), ("getOrders", CYAN), ("()", PLAIN)]],
    status=("lighthouse: 98 / 100", "render: ssr · isr"),
    tags=["Next.js", "App Router", "SEO · SSR"])

S["nestjs"] = dict(
    file="orders.controller.ts",
    code=[[("@Controller", VIOLET), ("(", PLAIN), ("'orders'", STRING), (")", PLAIN)],
          [("export class ", VIOLET), ("OrdersController", CYAN), (" {}", PLAIN)]],
    status=("jest: 224 passed", "swagger: /api/docs"),
    tags=["NestJS 10+", "TypeScript", "API · Микросервисы"])

S["nuxt"] = dict(
    file="pages/orders.vue",
    code=[[("const { data } = ", PLAIN), ("await ", VIOLET), ("useFetch", CYAN), ("(", PLAIN)],
          [("  ", PLAIN), ('"/api/orders"', STRING), (");", PLAIN)]],
    status=("lighthouse: 97 / 100", "render: ssr · pwa"),
    tags=["Nuxt 3+", "Vue 3", "SEO · PWA"])

S["spring"] = dict(
    file="OrderController.java",
    code=[[("@GetMapping", VIOLET), ("(", PLAIN), ('"/orders"', STRING), (")", PLAIN)],
          [("public ", VIOLET), ("List", VIOLET), ("<Order> ", PLAIN), ("all", CYAN), ("()", PLAIN)]],
    status=("junit: 238 passed", "actuator: health UP"),
    tags=["Spring Boot", "Java 17+", "Микросервисы"])

S["rust"] = dict(
    file="main.rs",
    code=[[("async fn ", VIOLET), ("orders", CYAN), ("() -> ", PLAIN), ("Json", VIOLET), ("<Orders>", PLAIN)],
          [("  Json(store.", PLAIN), ("all", CYAN), ("().", PLAIN), ("await", CYAN), (")", PLAIN)]],
    status=("cargo test: 164 passed", "p99: 4 ms · без GC"),
    tags=["Rust", "Tokio · Axum", "Highload · Блокчейн"])

S["ruby"] = dict(
    file="orders_controller.rb",
    code=[[("class ", VIOLET), ("OrdersController", CYAN)],
          [("  render ", VIOLET), ("json", CYAN), (": ", PLAIN), ("Order", VIOLET), (".all", PLAIN)]],
    status=("rspec: 178 passed", "deploy: kamal · docker"),
    tags=["Ruby 3.3+", "Rails 7+", "MVP · SaaS"])

S["cpp"] = dict(
    file="main.cpp",
    code=[[("auto ", VIOLET), ("process", CYAN), ("(", PLAIN), ("std", VIOLET), ("::span<Frame> in)", PLAIN)],
          [("  return ", VIOLET), ("transform", CYAN), ("(in, kernel);", PLAIN)]],
    status=("ctest: 142 passed", "latency: 0.8 ms"),
    tags=["C++17", "Qt · Boost · STL", "Десктоп · Embedded"])

S["solidity"] = dict(
    file="Vault.sol",
    code=[[("contract ", VIOLET), ("Vault", CYAN), (" is ", PLAIN), ("ERC20", VIOLET), (" {", PLAIN)],
          [("  function ", VIOLET), ("stake", CYAN), ("() ", PLAIN), ("external", VIOLET), (" {}", PLAIN)]],
    status=("forge test: 88 passed", "audit: slither clean"),
    tags=["Solidity 0.8+", "EVM · Hardhat", "DeFi · NFT · DApps"])

S["1c"] = dict(
    file="ОбменССайтом.epf",
    code=[[("Процедура ", VIOLET), ("ОбменЗаказами", CYAN), ("()", PLAIN)],
          [("  Заказ.", PLAIN), ("Записать", CYAN), ("();", PLAIN)]],
    status=("тесты: 74 passed", "обмен: сайт · ЭДО"),
    tags=["1С:Предприятие 8", "Обмен с сайтом", "ERP · Учёт · ЭДО"])


def build(slug: str) -> str:
    spec = S[slug]

    grid = "".join(
        f'<line x1="{x}" y1="0" x2="{x}" y2="480" stroke="#ffffff" '
        f'stroke-opacity="0.028"/>' for x in range(60, 640, 60)
    ) + "".join(
        f'<line x1="0" y1="{y}" x2="640" y2="{y}" stroke="#ffffff" '
        f'stroke-opacity="0.028"/>' for y in range(60, 480, 60)
    )

    bars = "".join(
        f'<rect x="{CODE_X}" y="{y}" width="{w}" height="4" rx="2" '
        f'fill="{SKELETON}" fill-opacity="{o}"/>'
        for y, w, o in [(234, 300, 0.85), (244, 380, 0.6)]
    )

    widths = [tag_width(t) for t in spec["tags"]]
    total = sum(widths) + TAG_GAP * (len(widths) - 1)
    if total > CARD_W:
        raise ValueError(f"{slug}: теги не влезают ({total:.0f} > {CARD_W}): {spec['tags']}")

    tags, x = "", CARD_X
    for i, (label, w) in enumerate(zip(spec["tags"], widths)):
        stroke, s_op, color, weight = [
            (CYAN, 0.5, "#ffffff", 700),
            ("#ffffff", 0.16, "#ffffff", 700),
            ("#ffffff", 0.10, FILENAME, 600),
        ][i]
        tags += (
            f'<rect x="{x}" y="{TAG_Y}" width="{w}" height="{TAG_H}" rx="8" '
            f'fill="none" stroke="{stroke}" stroke-opacity="{s_op}"/>'
            f'<text x="{x + w / 2}" y="{TAG_Y + 23}" text-anchor="middle" '
            f'font-family="{SANS}" font-size="14" font-weight="{weight}" '
            f'fill="{color}">{esc(label)}</text>'
        )
        x += w + TAG_GAP

    ok, deploy = spec["status"]
    c_r = CARD_X + CARD_W
    head_y = CARD_Y + HEAD_H          # низ шапки окна
    dot_y = CARD_Y + HEAD_H / 2

    if CARD_Y < SAFE_TOP or TAG_Y + TAG_H > SAFE_BOTTOM:
        raise ValueError(
            f"{slug}: содержимое вне безопасной зоны [{SAFE_TOP}, {SAFE_BOTTOM}] — "
            f"на мобайле обрежется"
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="480" viewBox="0 0 640 480" preserveAspectRatio="xMidYMid slice" role="img">
  <rect width="640" height="480" fill="{BG}"/>
  {grid}
  <text x="320" y="120" text-anchor="middle" font-family="{MONO}" font-size="150" font-weight="700" fill="#ffffff" fill-opacity="0.03">&lt;/&gt;</text>

  <rect x="{CARD_X}" y="{CARD_Y}" width="{CARD_W}" height="{CARD_H}" rx="10" fill="{CARD_BODY}" stroke="#ffffff" stroke-opacity="0.07"/>
  <path d="M{CARD_X} {CARD_Y + 10} a10 10 0 0 1 10 -10 h{CARD_W - 20} a10 10 0 0 1 10 10 v{HEAD_H - 10} h-{CARD_W} z" fill="{CARD_HEAD}"/>
  <line x1="{CARD_X}" y1="{head_y}" x2="{c_r}" y2="{head_y}" stroke="#ffffff" stroke-opacity="0.07"/>
  <circle cx="{CARD_X + 22}" cy="{dot_y}" r="4" fill="none" stroke="{DOT_V}" stroke-width="1.5"/>
  <circle cx="{CARD_X + 39}" cy="{dot_y}" r="4" fill="none" stroke="{DOT_C}" stroke-width="1.5"/>
  <circle cx="{CARD_X + 56}" cy="{dot_y}" r="4" fill="none" stroke="{DOT_G}" stroke-width="1.5"/>
  <text x="{c_r - 20}" y="{dot_y + 4.5}" text-anchor="end" font-family="{MONO}" font-size="13" fill="{FILENAME}">{esc(spec["file"])}</text>

  <text x="{CODE_X}" y="198" font-family="{MONO}" font-size="17">{tspans(spec["code"][0])}</text>
  <text x="{CODE_X}" y="221" font-family="{MONO}" font-size="17">{tspans(spec["code"][1])}</text>
  {bars}

  <text x="{CODE_X}" y="267" font-family="{MONO}" font-size="14" fill="{CYAN}">✓ {esc(ok)}</text>
  <text x="{CODE_X}" y="284" font-family="{MONO}" font-size="14" fill="{MUTED}">➜ {esc(deploy)}</text>

  {tags}
</svg>
'''


def main() -> None:
    from _tehnologii_data import TECH_META

    slugs = [m["slug"] for m in TECH_META]
    missing = [s for s in slugs if s not in S]
    if missing:
        raise ValueError(f"Нет спецификации мокапа для: {missing}")

    for slug in slugs:
        path = OUT / f"{slug}-hero.svg"
        path.write_text(build(slug), encoding="utf-8")
    print(f"Готово: {len(slugs)} SVG в {OUT}")


if __name__ == "__main__":
    main()
