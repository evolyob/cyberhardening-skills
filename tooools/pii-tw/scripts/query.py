#!/usr/bin/env python3
"""Taiwan Personal Data Protection Act (PDPA) and Privacy Engineering Query Engine."""

import argparse
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_json_data(filename: str) -> dict:
    target = DATA_DIR / filename
    if not target.exists():
        return {}
    with open(target, "r", encoding="utf-8-sig") as f:
        return json.load(f)


def extract_digits(raw: str) -> str:
    cleaned = re.sub(r"[^\d]", "", raw)
    return cleaned if cleaned else raw.strip()


def query_by_article(matrix: dict, article_num: str) -> list:
    digits = extract_digits(article_num)
    target_tag = f"Art-{int(digits):02d}" if digits.isdigit() else digits
    items = matrix.get("articles", [])
    results = []
    for it in items:
        art_id = it.get("article_id", "")
        ref = it.get("legal_reference", "")
        if "Sec-" in art_id and "第12條" not in digits:
            continue
        if target_tag in art_id or f"第{digits}條" in ref or f"第{article_num}條" in ref:
            results.append(it)
    return results


def query_by_measure(matrix: dict, measure_num: str) -> list:
    digits = extract_digits(measure_num)
    target_tag = f"Sec-{int(digits):02d}" if digits.isdigit() else digits
    items = matrix.get("articles", [])
    results = []
    for it in items:
        art_id = it.get("article_id", "")
        ref = it.get("legal_reference", "")
        if target_tag in art_id or f"第{digits}款" in ref or f"第{measure_num}款" in ref:
            results.append(it)
    return results


def query_by_domain(matrix: dict, index_data: dict, keyword: str) -> list:
    kw = keyword.strip().lower()
    results = []
    for art in matrix.get("articles", []):
        domain = art.get("domain", "").lower()
        topic = art.get("topic", "").lower()
        if kw in domain or kw in topic:
            results.append({"type": "article", "data": art})
    for ch in index_data.get("chapters", []):
        cd_dom = ch.get("domain", "").lower()
        slug = ch.get("slug", "").lower()
        if kw in cd_dom or kw in slug:
            results.append({"type": "chapter", "data": ch})
    return results


def query_by_category(categories_data: dict, keyword: str) -> dict:
    kw = keyword.strip().lower()
    matched_cats = []
    matched_purposes = []
    for cat in categories_data.get("categories", []):
        text = f"{cat.get('code', '')} {cat.get('name', '')} {cat.get('class', '')} {cat.get('description', '')} {' '.join(cat.get('examples', []))}".lower()
        if kw in text:
            matched_cats.append(cat)
    for pur in categories_data.get("purposes", []):
        text = f"{pur.get('code', '')} {pur.get('name', '')} {pur.get('class', '')} {pur.get('description', '')} {' '.join(pur.get('examples', []))}".lower()
        if kw in text:
            matched_purposes.append(pur)
    return {"categories": matched_cats, "purposes": matched_purposes}


def cross_check(matrix: dict, glossary: dict, index_data: dict, keyword: str) -> dict:
    kw = keyword.strip().lower()
    res = {"articles": [], "measures": [], "glossary": [], "chapters": []}
    for item in matrix.get("articles", []):
        text = f"{item.get('article_id', '')} {item.get('title', '')} {item.get('legal_reference', '')} {item.get('legal_requirement', '')} {item.get('engineering_control', '')} {item.get('domain', '')}".lower()
        if kw in text:
            if "Sec-" in item.get("article_id", ""):
                res["measures"].append(item)
            else:
                res["articles"].append(item)
    for term in glossary.get("terms", []):
        text = f"{term.get('term_zh', '')} {term.get('term_en', '')} {term.get('legal_definition', '')} {term.get('engineering_definition', '')} {term.get('practical_guidance', '')}".lower()
        if kw in text:
            res["glossary"].append(term)
    for ch in index_data.get("chapters", []):
        text = f"{ch.get('title', '')} {ch.get('domain', '')} {ch.get('slug', '')}".lower()
        if kw in text:
            res["chapters"].append(ch)
    return res


def format_markdown_chapters(index_data: dict) -> str:
    lines = ["# 台灣個資法 (PDPA) 與 Privacy Engineering 核心章節指南 (Chapters 01~08)\n"]
    for ch in index_data.get("chapters", []):
        lines.append(f"- **Ch{ch.get('id')}**: {ch.get('title')} (`{ch.get('file')}`)")
        lines.append(f"  - 領域: {ch.get('domain')}")
        lines.append(f"  - 法源: {', '.join(ch.get('legal_basis', []))}")
    return "\n".join(lines)


def format_markdown_list(index_data: dict, matrix: dict) -> str:
    lines = ["# 台灣個資法 (PDPA) 與 Privacy Engineering 合規架構總覽\n", "## 1. 核心章節指南 (Chapters 01~08)"]
    for ch in index_data.get("chapters", []):
        lines.append(f"- **Ch{ch.get('id')}**: {ch.get('title')} (`{ch.get('file')}`)")
        lines.append(f"  - 領域: {ch.get('domain')}")
        lines.append(f"  - 法源: {', '.join(ch.get('legal_basis', []))}")
    lines.append("\n## 2. 施行細則第 12 條 11 款安全維護事項")
    for it in matrix.get("articles", []):
        if "Sec-" in it.get("article_id", ""):
            lines.append(f"- **{it.get('article_id')}**: {it.get('title')} (領域: {it.get('domain')})")
    return "\n".join(lines)


def format_markdown_items(items: list, header_title: str) -> str:
    if not items:
        return f"未找到對應的{header_title}。"
    lines = []
    for it in items:
        lines.append(f"## {it.get('legal_reference', it.get('title', ''))}")
        lines.append(f"- **項目名稱**: {it.get('title', '')}")
        lines.append(f"- **Privacy Engineering 領域**: {it.get('domain', '')} ({it.get('topic', '')})")
        lines.append(f"- **法定要求**: {it.get('legal_requirement', '')}")
        lines.append(f"- **工程控制項**: {it.get('engineering_control', '')}")
        if it.get("audit_checks"):
            lines.append("- **查核重點**:")
            for check in it.get("audit_checks", []):
                lines.append(f"  - {check}")
        if it.get("gap_remediation"):
            lines.append(f"- **缺口處置措施**: {it.get('gap_remediation')}")
        lines.append("")
    return "\n".join(lines).strip()


def format_markdown_category(res: dict, keyword: str) -> str:
    lines = [f"# 個資類別與特定目的檢索: `{keyword}`\n"]
    if res["categories"]:
        lines.append(f"### 個人資料類別代號 ({len(res['categories'])} 筆)")
        for c in res["categories"]:
            spec_badge = " [特種個資 (Art 6)]" if c.get("is_special") else ""
            lines.append(f"- **{c.get('code', '')} {c.get('name', '')}** ({c.get('class', '')}){spec_badge}")
            lines.append(f"  - 說明: {c.get('description', '')}")
            if c.get("examples"):
                lines.append(f"  - 範例: {', '.join(c.get('examples', []))}")
    if res["purposes"]:
        lines.append(f"\n### 特定目的代號 ({len(res['purposes'])} 筆)")
        for p in res["purposes"]:
            lines.append(f"- **{p.get('code', '')} {p.get('name', '')}** ({p.get('class', '')})")
            lines.append(f"  - 說明: {p.get('description', '')}")
            if p.get("examples"):
                lines.append(f"  - 範例: {', '.join(p.get('examples', []))}")
    if not any(res.values()):
        lines.append("未檢索到相關個資類別或特定目的。")
    return "\n".join(lines).strip()


def format_markdown_check(res: dict, keyword: str) -> str:
    lines = [f"# 交叉檢索結果: `{keyword}`\n"]
    if res["articles"]:
        lines.append(f"### 個資法母法條文 ({len(res['articles'])} 筆)")
        for a in res["articles"]:
            lines.append(f"- **{a.get('title', '')}** (`{a.get('article_id', '')}`): {a.get('engineering_control', '')[:100]}...")
    if res["measures"]:
        lines.append(f"\n### 細則第 12 條安全維護措施 ({len(res['measures'])} 筆)")
        for m in res["measures"]:
            lines.append(f"- **{m.get('title', '')}**: {m.get('engineering_control', '')[:100]}...")
    if res["glossary"]:
        lines.append(f"\n### 術語詞典 ({len(res['glossary'])} 筆)")
        for g in res["glossary"]:
            lines.append(f"- **{g.get('term_zh', '')}** ({g.get('term_en', '')}): {g.get('legal_definition', '')[:80]}...")
    if res["chapters"]:
        lines.append(f"\n### 指南章節 ({len(res['chapters'])} 筆)")
        for c in res["chapters"]:
            lines.append(f"- **Ch{c.get('id')} {c.get('title', '')}**: `{c.get('file', '')}`")
    if not any(res.values()):
        lines.append("未檢索到相關合規項目。")
    return "\n".join(lines).strip()


def main():
    parser = argparse.ArgumentParser(description="Taiwan PDPA & Privacy Engineering Compliance Query Engine")
    parser.add_argument("--article", type=str, help="依個資法條號查詢技術控制項與合規查核點")
    parser.add_argument("--measure", type=str, help="依施行細則第12條款次查詢安全維護措施指引")
    parser.add_argument("--domain", type=str, help="依隱私工程領域或章節關鍵字查詢對應法令與技術規範")
    parser.add_argument("--category", type=str, help="依個資類別代號 (如 C001) 或特定目的代號 (如 001) 查詢詳細定義")
    parser.add_argument("--check", type=str, help="法規、技術控制、術語與章節跨庫交叉檢索")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown", help="輸出格式")
    parser.add_argument("--list", action="store_true", help="列出完整章節與安全維護款次總覽")
    parser.add_argument("--list-chapters", action="store_true", help="列出核心合規指南八大章節清單")

    args = parser.parse_args()

    index_data = load_json_data("index.json")
    matrix_data = load_json_data("compliance_matrix.json")
    glossary_data = load_json_data("glossary.json")
    categories_data = load_json_data("data_categories.json")

    if args.list_chapters:
        if args.format == "json":
            print(json.dumps(index_data.get("chapters", []), ensure_ascii=False, indent=2))
            return
        print(format_markdown_chapters(index_data))
        return

    if args.list:
        if args.format == "json":
            print(json.dumps({"index": index_data, "matrix": matrix_data}, ensure_ascii=False, indent=2))
            return
        print(format_markdown_list(index_data, matrix_data))
        return

    if args.category:
        res = query_by_category(categories_data, args.category)
        if args.format == "json":
            print(json.dumps(res, ensure_ascii=False, indent=2))
            return
        print(format_markdown_category(res, args.category))
        return

    if args.article:
        res = query_by_article(matrix_data, args.article)
        if args.format == "json":
            print(json.dumps(res, ensure_ascii=False, indent=2))
            return
        print(format_markdown_items(res, f"個資法第 {args.article} 條"))
        return

    if args.measure:
        res = query_by_measure(matrix_data, args.measure)
        if args.format == "json":
            print(json.dumps(res, ensure_ascii=False, indent=2))
            return
        print(format_markdown_items(res, f"細則第 12 條第 {args.measure} 款"))
        return

    if args.domain:
        res = query_by_domain(matrix_data, index_data, args.domain)
        if args.format == "json":
            print(json.dumps(res, ensure_ascii=False, indent=2))
            return
        lines = [f"## Privacy Engineering 檢索: `{args.domain}`\n"]
        for r in res:
            t, d = r["type"], r["data"]
            if t == "article":
                lines.append(f"- **{d.get('title', '')}**: {d.get('engineering_control', '')}")
            else:
                lines.append(f"- **Ch{d.get('id', '')} {d.get('title', '')}**: `{d.get('file', '')}`")
        print("\n".join(lines) if len(lines) > 1 else "未找到對應項目。")
        return

    if args.check:
        res = cross_check(matrix_data, glossary_data, index_data, args.check)
        if args.format == "json":
            print(json.dumps(res, ensure_ascii=False, indent=2))
            return
        print(format_markdown_check(res, args.check))
        return

    parser.print_help()


if __name__ == "__main__":
    main()
