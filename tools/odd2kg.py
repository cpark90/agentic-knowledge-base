#!/usr/bin/env python3
"""OpenODD 문서(YAML) → ODD 그래프(-odd.ttl) 생성기 (노트 3.2절, 부록 E.4).

원본은 kb/odd/*.yml 이고 TTL은 생성물이다. 검사:
  - attributes.*.category 가 택소노미(taxonomy.yml)의 key 안에 있다
  - include_and 의 모든 속성이 attributes 에 선언되어 있고 checks 에 판정 방법·등급이 있다
    (0.4절 "모든 조건은 객관적 판정 방법을 갖는다")
사용: odd2kg.py --taxonomy taxonomy.yml --out project-odd.ttl project-odd.yml
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kb_yaml  # noqa: E402

CLASS = {"static": "agt:StaticElement", "environmental": "agt:EnvironmentalCondition", "dynamic": "agt:DynamicElement"}
PREAMBLE = """\
# 생성 파일 — 손으로 고치지 않는다. 원본은 OpenODD 문서 {src} (tools/odd2kg.py).
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
@prefix id: <https://agentic-knowledge-base.dev/id/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
"""


def esc(s) -> str:
    return str(s).replace("\\", "\\\\").replace('"', '\\"')


def value_text(expr) -> str:
    """OpenODD 식 → 사람이 읽는 조건 값 (agt:conditionValue)."""
    if not isinstance(expr, dict):
        return str(expr)
    parts = []
    if "equal" in expr: parts.append(str(expr["equal"]))
    if "range" in expr: parts.append(f"[{expr['range'][0]} .. {expr['range'][1]}]")
    if "lower_bound" in expr: parts.append(f"≥ {expr['lower_bound']}")
    if "upper_bound" in expr: parts.append(f"≤ {expr['upper_bound']}")
    if "in" in expr: parts.append("{" + ", ".join(map(str, expr["in"])) + "}")
    if expr.get("any"): parts.append("any")
    if expr.get("unknown"): parts.append("unknown")
    if "unit" in expr: parts[-1] += f" {expr['unit']}"
    if "note" in expr: parts.append(f"— {expr['note']}")
    return " ".join(parts)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--taxonomy", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("src")
    args = ap.parse_args()
    tax = kb_yaml.load(Path(args.taxonomy).read_text(encoding="utf-8"))
    keys = {c["key"] for c in tax["categories"]}
    doc = kb_yaml.load(Path(args.src).read_text(encoding="utf-8"))
    attrs = doc.get("attributes", {})
    errors = []
    for a, meta in attrs.items():
        if meta.get("category") not in keys:
            errors.append(f"{a}: category {meta.get('category')!r} 가 택소노미에 없다 — 온톨로지(related/condition)를 먼저 확장하라")
    conds = []
    for mod in doc["modules"]:
        checks = mod.get("checks", {})
        for entry in mod.get("include_and", []):
            (attr, expr), = entry.items()
            if attr not in attrs:
                errors.append(f"{mod['id']}: 속성 {attr} 가 attributes 에 선언되지 않았다"); continue
            chk = checks.get(attr)
            if not chk or not chk.get("method") or not chk.get("grade"):
                errors.append(f"{mod['id']}: {attr} 에 checks(method·grade)가 없다 — 판정 방법 없는 조건은 ODD에 둘 수 없다 (0.4절)"); continue
            conds.append((attr, attrs[attr], expr, chk))
    if errors:
        print("\n".join("odd2kg: " + e for e in errors), file=sys.stderr); return 1
    mode = "restrictive" if doc.get("exclude_when_unknown", True) else "permissive"
    out = [PREAMBLE.format(src=args.src), f"{doc['id']} a agt:ODD ;",
           f'    rdfs:label "{esc(doc["title"])}"@en , "{esc(doc["title_ko"])}"@ko ;', f'    agt:mode "{mode}" ;',
           "    agt:hasCondition " + " , ".join(a for a, *_ in conds) + " ;"]
    ex = [f'"{esc(e["concept"])} — reviewed {e["reviewed"]}, 이유: {esc(e["reason"])}"' for m in doc["modules"] for e in m.get("exclusions_reviewed", [])]
    out[-1] = out[-1][:-2] + (" ;\n    agt:excludes " + " , ".join(ex) + " ." if ex else " .")
    for attr, meta, expr, chk in conds:
        out += ["", f"{attr} a {CLASS[meta['category']]} ;", f'    rdfs:label "{esc(meta["title"])}"@en , "{esc(meta["title_ko"])}"@ko ;',
                f'    agt:conditionValue "{esc(value_text(expr))}" ;', f'    agt:checkMethod "{esc(chk["method"])}" ;',
                f'    agt:verificationGrade "{chk["grade"]}" .']
    Path(args.out).write_text("\n".join(out) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
