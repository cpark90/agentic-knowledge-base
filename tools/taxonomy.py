#!/usr/bin/env python3
"""ODD 택소노미 뷰 — related/condition 온톨로지에서 OpenODD 택소노미 YAML(taxonomy.yml)을 생성한다 (부록 E.4).

OpenODD YAML 매핑 참조: 최상위 `TAXONOMY:` 아래 개념 레코드. 이 체계에서 범주(정적 요소·환경 조건·동적 요소)는
온톨로지의 agt:Condition 하위 클래스이고, 속성은 프로젝트의 ODD 문서가 같은 범주 키 아래에 확장한다.
손으로 쓰지 않는다. 사용: taxonomy.py --out taxonomy.yml <condition 모듈 TTL...>
출력·종료: 읽을 수 없거나 파싱되지 않는 입력은 `FAIL [taxonomy] <경로>: …` + EXIT_CONFIG (판정 규칙은 없다 — 생성기).
"""
import argparse
import sys
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, OWL
from rdflib.namespace import SKOS

try:  # 종료 코드 규약의 단일 정의처는 kb_lib — 없으면 같은 값의 폴백
    from tools import kb_lib
except ImportError:
    try:
        import kb_lib
    except ImportError:
        kb_lib = None
EXIT_CONFIG = getattr(kb_lib, "EXIT_CONFIG", 2)

AGT = Namespace("https://agentic-knowledge-base.dev/agt/")
KEYS = {AGT.StaticElement: "static_element", AGT.EnvironmentalCondition: "environmental_condition", AGT.DynamicElement: "dynamic_element"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("files", nargs="+")
    args = ap.parse_args()
    g = Graph()
    for f in args.files:
        try:
            g.parse(f, format="turtle")
        except Exception as e:  # rdflib 파서·OSError — 판정 불가 입력
            print(f"FAIL [taxonomy] {f}: 읽거나 파싱할 수 없다 — {e}", file=sys.stderr)
            return EXIT_CONFIG
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
