#!/usr/bin/env python3
"""ODD 택소노미 뷰 — related/condition 온톨로지에서 taxonomy.yml을 생성한다 (노트 부록 E.4).

OpenODD의 택소노미(속성 범주)는 이 체계에서 온톨로지의 조건 클래스다. 손으로 쓰지 않는다.
사용: taxonomy.py --out taxonomy.yml <condition 모듈 TTL...>
"""
import argparse
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, OWL
from rdflib.namespace import SKOS

AGT = Namespace("https://agentic-knowledge-base.dev/agt/")
KEYS = {AGT.StaticElement: "static", AGT.EnvironmentalCondition: "environmental", AGT.DynamicElement: "dynamic"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("files", nargs="+")
    args = ap.parse_args()
    g = Graph()
    for f in args.files:
        g.parse(f, format="turtle")
    out = ["# 생성 파일 — 손으로 고치지 않는다. 원본은 kb/ontology/related/condition (tools/taxonomy.py)",
           "# OpenODD 속성 범주 = agt:Condition 의 하위 클래스. ODD 문서의 attributes.*.category 가 여기의 key 여야 한다.",
           "categories:"]
    for cls in g.subjects(RDFS.subClassOf, AGT.Condition):
        if (cls, RDF.type, OWL.Class) not in g:
            continue
        ko = next((str(o) for o in g.objects(cls, RDFS.label) if o.language == "ko"), "")
        en = next((str(o) for o in g.objects(cls, RDFS.label) if o.language == "en"), "")
        dfn = next((str(o) for o in g.objects(cls, SKOS.definition)), "")
        key = KEYS.get(cls, str(cls).split("/")[-1].lower())
        out += [f"  - key: {key}", f"    class: agt:{str(cls).split('/')[-1]}", f'    title: "{en}"', f'    title_ko: "{ko}"',
                f'    definition: "{dfn.replace(chr(34), chr(39))}"']
    out += ["value_forms: [equal, range, lower_bound, upper_bound, in, any, unknown]  # OpenODD 식 (부록 E.4)"]
    Path(args.out).write_text("\n".join(out) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
