#!/usr/bin/env python3
"""Retrieve relevant 350-layout-compositions cases by catalog text."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen


DEFAULT_URL = "https://raw.githubusercontent.com/nevertoday/350-layout-compositions/main/v2/catalog.json"
DEFAULT_CATEGORIES = {
    "01-composition-logic",
    "02-visual-principles",
    "03-editorial-advertising",
    "04-type-grid-cjk",
}

LAW_HINTS = {
    "三分法": "thirds placement and focal hierarchy",
    "黄金": "proportional scale and guided movement",
    "螺旋": "progressive reading path toward a focal point",
    "对角线": "directional energy and diagonal vector",
    "负空间": "intentional empty field and isolation",
    "居中": "center axis and authority",
    "对称": "mirrored balance and stability",
    "偏心": "asymmetric balance through mass and whitespace",
    "非对称": "asymmetric balance through mass and whitespace",
    "引导线": "leading lines toward a target",
    "网格": "shared columns, baselines, and alignment",
    "比例": "scale relationships between type, image, and margins",
    "留白": "whitespace as framing, pacing, or emphasis",
    "填满": "edge-to-edge density and impact",
}


def load_catalog(path: str | None) -> list[dict]:
    if path:
        data = Path(path).read_text(encoding="utf-8")
    else:
        request = Request(DEFAULT_URL, headers={"User-Agent": "qiaomu-flat-layout-advisor"})
        with urlopen(request, timeout=20) as response:
            data = response.read().decode("utf-8")
    catalog = json.loads(data)
    if not isinstance(catalog, list):
        raise ValueError("catalog must be a JSON array")
    return catalog


def tokens(query: str) -> list[str]:
    raw = re.findall(r"[\u4e00-\u9fff]+|[A-Za-z0-9]+", query.lower())
    parts: list[str] = []
    for item in raw:
        parts.append(item)
        if len(item) > 2 and all("\u4e00" <= ch <= "\u9fff" for ch in item):
            parts.extend(item[i : i + 2] for i in range(len(item) - 1))
    return list(dict.fromkeys(parts))


def score(item: dict, query_tokens: list[str]) -> tuple[int, int]:
    haystack = " ".join(
        str(item.get(key, "")).lower()
        for key in ("name", "category", "subcategory", "category_slug", "subcategory_slug")
    )
    matched = sum(1 for token in query_tokens if token in haystack)
    category_bonus = 2 if item.get("category_slug") in DEFAULT_CATEGORIES else 0
    return matched + category_bonus, matched


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    parser.add_argument("--catalog")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--all-categories", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    try:
        catalog = load_catalog(args.catalog)
    except Exception as exc:  # pragma: no cover - network and user path errors
        print(f"catalog load failed: {exc}", file=sys.stderr)
        return 2

    query_tokens = tokens(args.query)
    ranked = []
    for item in catalog:
        if not args.all_categories and item.get("category_slug") not in DEFAULT_CATEGORIES:
            continue
        primary, matched = score(item, query_tokens)
        if matched:
            name = str(item.get("name", ""))
            hint = next((value for key, value in LAW_HINTS.items() if key in name), None)
            row = dict(item)
            row["match_score"] = primary
            row["matched_terms"] = matched
            if hint:
                row["law_hint"] = hint
            ranked.append(row)

    ranked.sort(key=lambda item: (-item["match_score"], -item["matched_terms"], item.get("id", "")))
    result = ranked[: max(0, args.limit)]
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for item in result:
            print(f"{item.get('id')} · {item.get('name')} · {item.get('category')} / {item.get('subcategory')}")
            print(f"  score={item.get('match_score')} image={item.get('image')}")
            if item.get("law_hint"):
                print(f"  law_hint={item['law_hint']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
