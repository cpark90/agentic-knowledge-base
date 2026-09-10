#!/usr/bin/env python3
"""OpenODD 문서(YAML 매핑 참조) → ODD 그래프(-odd.ttl) 생성기 (노트 3.2절, 부록 E.4).

원본은 kb/odd/*.yml, TTL은 생성물. 생성 = 검사:
  - TAXONOMY 확장의 범주 키가 생성된 taxonomy.yml 의 범주 안에 있다 (어휘는 온톨로지에서)
  - MODULES 의 모든 조건 속성이 TAXONOMY 에 선언되어 있고, 식이 OpenODD 식(리터럴·"< n"·"> n"·"[a .. b]"·unknown)이다
  - 범주 리터럴은 선언된 목록 안, 수치 식은 수치 속성에만
  - 모든 속성에 ATTRIBUTES(IRI·라벨)와 CHECKS(방법·등급)가 있다 — 판정 방법 없는 조건은 ODD에 둘 수 없다 (0.4절)
사용: odd2kg.py --taxonomy taxonomy.yml --out project-odd.ttl project-odd.yml
"""
import argparse
import re
import sys
from pathlib import Path

import yaml

CLASS = {"static_element": "agt:StaticElement", "environmental_condition": "agt:EnvironmentalCondition", "dynamic_element": "agt:DynamicElement"}
NUM = re.compile(r'^\s*(<=?|>=?)\s*([-\d.]+)\s*(\w+)?\s*$')
RANGE = re.compile(r'^\s*\[\s*([-\d.]+)\s*\.\.\s*([-\d.]+)\s*\]\s*(\w+)?\s*$')
PREAMBLE = """\
# 생성 파일 — 손으로 고치지 않는다. 원본은 OpenODD 문서 {src} (tools/odd2kg.py).
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
@prefix id: <https://agentic-knowledge-base.dev/id/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
"""


def esc(s) -> str:
    return str(s).replace("\\", "\\\\").replace('"', '\\"')


def classify(expr, decl):
    """(식 종류, 사람이 읽는 값) — OpenODD 식 5종 + unknown."""
    if expr == "unknown":
        return "unknown", "unknown"
    s = str(expr)
    if isinstance(decl, list):  # 범주 속성
        if s not in decl:
            raise ValueError(f"리터럴 {s!r} 이 선언된 목록 {decl} 에 없다")
        return "Equal", s
    m = NUM.match(s)
    if m:
        return ("LowerBound" if m.group(1).startswith(">") else "UpperBound"), s.strip()
    m = RANGE.match(s)
    if m:
        return "Range", s.strip()
    raise ValueError(f"OpenODD 식이 아니다: {s!r} (리터럴 / '< n unit' / '> n unit' / '[a .. b] unit' / unknown)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--taxonomy", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("src")
    a = ap.parse_args()
    tax = yaml.safe_load(Path(a.taxonomy).read_text(encoding="utf-8")) or {}
    doc = yaml.safe_load(Path(a.src).read_text(encoding="utf-8"))
    cats = set((tax.get("TAXONOMY") or {}).keys())
    errors = []
    attrs = {}  # name -> (category, decl)
    for cat, members in (doc.get("TAXONOMY") or {}).items():
        if cat not in cats:
            errors.append(f"TAXONOMY 범주 {cat!r} 가 생성된 택소노미에 없다 — 온톨로지(related/condition)를 먼저 확장하라")
            continue
        for name, decl in (members or {}).items():
            attrs[name] = (cat, decl)
    meta, checks, lits = doc.get("ATTRIBUTES") or {}, doc.get("CHECKS") or {}, doc.get("LITERALS") or {}
    conds = []
    for mod_id, mod in (doc.get("MODULES") or {}).items():
        for sec in ("INCLUDE_AND", "INCLUDE_OR", "EXCLUDE_AND", "EXCLUDE_OR"):
            for name, expr in (mod.get(sec) or {}).items():
                if name not in attrs:
                    errors.append(f"{mod_id}.{sec}: 속성 {name} 이 TAXONOMY 에 선언되지 않았다"); continue
                cat, decl = attrs[name]
                try:
                    kind, text = classify(expr, decl)
                except ValueError as e:
                    errors.append(f"{mod_id}.{sec}.{name}: {e}"); continue
                m, c = meta.get(name), checks.get(name)
                if not m or not m.get("iri") or not m.get("title") or not m.get("title_ko"):
                    errors.append(f"{name}: ATTRIBUTES(iri·title·title_ko) 가 없다"); continue
                if not c or not c.get("method") or not c.get("grade"):
                    errors.append(f"{name}: CHECKS(method·grade) 가 없다 — 판정 방법 없는 조건은 ODD에 둘 수 없다 (0.4절)"); continue
                value = text if kind != "Equal" else f"{text} — {lits[text]}" if text in lits else text
                conds.append((m["iri"], CLASS[cat], m, f"{sec} {kind}: {value}", c))
    if errors:
        print("\n".join("odd2kg: " + e for e in errors), file=sys.stderr); return 1
    root = next(iter(doc["MODULES"]))
    title = doc["MODULES"][root].get("title") or {}
    mode = "restrictive" if doc.get("EXCLUDE_WHEN_UNKNOWN", True) else "permissive"
    ex = [f'"{esc(e["concept"])} — reviewed {e["reviewed"]}, 이유: {esc(e["reason"])}"' for e in doc.get("EXCLUSIONS_REVIEWED") or []]
    out = [PREAMBLE.format(src=a.src), f"id:odd-{root.replace('_', '-')} a agt:ODD ;",
           f'    rdfs:label "{esc(title.get("en", root))}"@en , "{esc(title.get("ko", root))}"@ko ;', f'    agt:mode "{mode}" ;',
           "    agt:hasCondition " + " , ".join(iri for iri, *_ in conds) + (" ;" if ex else " .")]
    if ex:
        out.append("    agt:excludes " + " , ".join(ex) + " .")
    for iri, cls, m, value, c in conds:
        out += ["", f"{iri} a {cls} ;", f'    rdfs:label "{esc(m["title"])}"@en , "{esc(m["title_ko"])}"@ko ;',
                f'    agt:conditionValue "{esc(value)}" ;', f'    agt:checkMethod "{esc(c["method"])}" ;', f'    agt:verificationGrade "{c["grade"]}" .']
    Path(a.out).write_text("\n".join(out) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
