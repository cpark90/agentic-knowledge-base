#!/usr/bin/env python3
"""ODD 택소노미 뷰 — related/condition 온톨로지에서 OpenODD 택소노미 YAML(taxonomy.yml)을 생성한다 (부록 E.4).

OpenODD YAML 매핑 참조: 최상위 `TAXONOMY:` 아래 개념 레코드. 이 체계에서 범주(정적 요소·환경 조건·동적 요소)는
온톨로지의 agt:Condition 하위 클래스이고, 속성은 프로젝트의 ODD 문서가 같은 범주 키 아래에 확장한다.
손으로 쓰지 않는다. 사용: taxonomy.py --out taxonomy.yml <condition 모듈 TTL...>
"""
import argparse
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, OWL
from rdflib.namespace import SKOS

AGT = Namespace("https://agentic-knowledge-base.dev/agt/")
KEYS = {AGT.StaticElement: "static_element", AGT.EnvironmentalCondition: "environmental_condition", AGT.DynamicElement: "dynamic_element"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("files", nargs="+")
    args = ap.parse_args()
    g = Graph()
    for f in args.files:
        g.parse(f, format="turtle")
    out = ["# 생성 파일 — 손으로 고치지 않는다. 원본은 kb/ontology/related/condition (tools/taxonomy.py).",
           "# ASAM OpenODD YAML 매핑: TAXONOMY 아래 개념 레코드. 범주 3 = agt:Condition 의 하위 클래스. 속성은 ODD 문서의 TAXONOMY 확장이 같은 키 아래에 둔다.",
           "TAXONOMY:"]
    for cls in sorted(g.subjects(RDFS.subClassOf, AGT.Condition), key=lambda c: list(KEYS).index(c) if c in KEYS else 99):
        if (cls, RDF.type, OWL.Class) not in g:
            continue
        ko = next((str(o) for o in g.objects(cls, RDFS.label) if o.language == "ko"), "")
        en = next((str(o) for o in g.objects(cls, RDFS.label) if o.language == "en"), "")
        dfn = next((str(o) for o in g.objects(cls, SKOS.definition)), "").replace("\n", " ")
        key = KEYS.get(cls, str(cls).split("/")[-1].lower())
        out.append(f"  {key}: {{}}    # agt:{str(cls).split('/')[-1]} — {en} · {ko}: {dfn}")
    Path(args.out).write_text("\n".join(out) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
