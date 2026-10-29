#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PVE 搜打撤研究站点生成器。

把 docs/research/*.md 渲染为 docs/research/*.html（引用主题 CSS，带返回导航），
并重新生成 docs/pveextraction_index.html 索引页。

用法：python tools/build.py

约定：
- 源 md 放在 docs/research/，生成同名 .html（不手改，改源后重跑本脚本）。
- 页面只引用 tokens.css/base.css 的令牌，不写死色值与字号。
"""
from __future__ import annotations

import markdown
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
RESEARCH = DOCS / "research"

SITE_TITLE = "PVE 搜打撤研究"

# 分组 → 页面清单。src 为 md 文件名；title/summary 用于索引卡片与页头。
# wide=True 的页面用 .page-wide（宽表），其余用 .page。
GROUPS = [
    {
        "name": "玩法框架",
        "pages": [
            {
                "src": "GameFramework.md",
                "title": "游戏框架讨论",
                "summary": "基于维多利亚 + 科幻侦探二次元 IP 的搜打撤玩法定位：PVE/PVP、TPS 手感、通胀控制、侦探题材融合等关键决策。",
            },
            {
                "src": "TPS分析.md",
                "title": "TPS 分析",
                "summary": "TPS 与 FPS 的本质区别、视角（腰射/肩射/FPP）与表现，供搜打撤射击玩法参考。",
            },
        ],
    },
    {
        "name": "题材研究",
        "pages": [
            {
                "src": "维多利亚时期_影视小说游戏_研究文档.md",
                "title": "维多利亚时期：影视 / 小说 / 游戏",
                "summary": "维多利亚时期（Victorian Era）的定义、时间线与相关影视、小说、游戏作品盘点。",
                "wide": True,
            },
            {
                "src": "维多利亚时期_枪械技术_研究文档.md",
                "title": "维多利亚时期枪械技术",
                "summary": "枪械技术发展考据：从击发前装到自动武器的 63 年演进，用于世界观与武器设定。",
                "wide": True,
            },
        ],
    },
    {
        "name": "竞品研究",
        "pages": [
            {
                "src": "超自然行动组_研究文档.md",
                "title": "《超自然行动组》研究",
                "summary": "中式微恐搜打撤竞品拆解：上线节奏、赛季制、段位设计、联动与官方数据，来源均为官网一手信息。",
                "wide": True,
            },
            {
                "src": "超自然行动组_道具属性表.md",
                "title": "《超自然行动组》道具属性总表",
                "summary": "竞品武器/战术道具/回收物属性整理，全部为官方一手信息。",
                "wide": True,
            },
        ],
    },
]


def convert_md(src: Path) -> str:
    """md → 正文 html（剥掉首个 # 标题，交给页头 h1 呈现）。"""
    text = src.read_text(encoding="utf-8")
    lines = text.split("\n")
    # 去掉开头的 # 标题行及其后空行
    if lines and lines[0].lstrip().startswith("# "):
        lines = lines[1:]
    while lines and lines[0].strip() == "":
        lines = lines[1:]

    # 连续引用行之间加硬换行，让多行「数据来源」等说明分行显示
    for i in range(len(lines) - 1):
        if lines[i].lstrip().startswith(">") and lines[i + 1].lstrip().startswith(">"):
            lines[i] = lines[i].rstrip() + "  "

    body = "\n".join(lines)

    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
    return md.convert(body)


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · {site_title}</title>
<link rel="stylesheet" href="../assets/theme/tokens.css">
<link rel="stylesheet" href="../assets/theme/base.css">
</head>
<body>

<section class="band">
  <div class="page">
    <header class="hero">
      <span class="tag">{group}</span>
      <h1>{title}</h1>
      <p class="lead">{summary}</p>
    </header>
  </div>
</section>

<section class="band band-alt band-tight">
  <div class="{page_cls}">
{body}
  </div>
</section>

<section class="band band-tight">
  <div class="page">
    <div class="links">
      <a href="../pveextraction_index.html">← 返回索引</a>
    </div>
  </div>
</section>

</body>
</html>
"""


def build_page(page: dict, group: str) -> None:
    src = RESEARCH / page["src"]
    body = convert_md(src)
    # 缩进正文以保持模板排版（每行前置 4 空格）
    body_indented = "\n".join(("    " + l if l else "") for l in body.split("\n"))
    html = PAGE_TEMPLATE.format(
        title=page["title"],
        site_title=SITE_TITLE,
        group=group,
        summary=page["summary"],
        page_cls="page-wide" if page.get("wide") else "page",
        body=body_indented,
    )
    out = RESEARCH / (page["src"][: -len(".md")] + ".html")
    out.write_text(html, encoding="utf-8")
    print(f"  ✓ {out.relative_to(ROOT)}")


def build_index() -> None:
    cards = []
    for group in GROUPS:
        cards.append(
            f'    <h2 class="group">{group["name"]}</h2>\n'
            '    <div class="grid">'
        )
        for page in group["pages"]:
            href = "research/" + page["src"][: -len(".md")] + ".html"
            cards.append(
                f'\n      <a class="card" href="{href}">\n'
                f"        <strong>{page['title']}</strong>\n"
                f"        <span>{page['summary']}</span>\n"
                "      </a>"
            )
        cards.append("\n    </div>\n")

    html = INDEX_HEAD + "\n".join(cards) + INDEX_TAIL
    (DOCS / "pveextraction_index.html").write_text(html, encoding="utf-8")
    print("  ✓ docs/pveextraction_index.html")


INDEX_HEAD = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PVE 搜打撤研究</title>
<link rel="stylesheet" href="assets/theme/tokens.css">
<link rel="stylesheet" href="assets/theme/base.css">
<style>
  .group { margin-top: var(--space-6); }
</style>
</head>
<body>

<section class="band">
  <div class="page">
    <header class="hero">
      <span class="tag">game project · 游戏项目</span>
      <h1>PVE 搜打撤研究</h1>
      <p class="lead">维多利亚风格 + 科幻元素的侦探题材二次元 IP，带「搜打撤」玩法方向的研究笔记：题材考据、射击手感、竞品拆解。</p>
    </header>
  </div>
</section>

<section class="band band-alt band-tight">
  <div class="page">
    <h2>选题速览</h2>
    <div class="stats">
      <div class="stat"><span>玩法方向</span><strong>PVE 搜打撤</strong></div>
      <div class="stat"><span>射击手感</span><strong>TPS · 单发为主</strong></div>
      <div class="stat"><span>题材</span><strong>维多利亚 + 科幻侦探</strong></div>
      <div class="stat"><span>对标竞品</span><strong>超自然行动组</strong></div>
    </div>
  </div>
</section>

<section class="band band-tight">
  <div class="page">
"""

INDEX_TAIL = """
  </div>
</section>

</body>
</html>
"""


def main() -> None:
    print("生成研究页面：")
    for group in GROUPS:
        for page in group["pages"]:
            build_page(page, group["name"])
    print("生成索引页：")
    build_index()
    print("完成。")


if __name__ == "__main__":
    main()
