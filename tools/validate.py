#!/usr/bin/env python3
"""검사 게이트 (노트 6.7절) — 온톨로지 위생(2.5절) + SHACL(4.4절) + ODD 참조(3.3절).

검사 항목
  syntax      모든 TTL이 파싱된다
  labels      온톨로지가 정의한 모든 agt: 용어에 rdfs:label 한/영 + skos:definition (2.5절)
  boundary    한 agt: 용어는 정확히 한 모듈 파일에서만 정의된다 (2.3절 경계 규칙)
  vocab       데이터 그래프의 술어는 온톨로지 정의 또는 표준 어휘 안에 있다 (4.4절 일관성,
              Part XIII "어휘 우회" 리스크)
  odd-ref     agt:refersTo 의 대상은 ODD 그래프에 존재한다 — "ODD에 없는 속성을 참조하는
              스코프나 가정은 존재할 수 없다" (0.4절)
  shacl       (--shapes) OWL-RL 추론 후 pySHACL 적합성 (--reason 시 추론 적용)

실패는 비영(non-zero) 종료 — bazel test 가 곧 게이트다.
"""

from __future__ import annotations

import argparse
import sys

from rdflib import RDF, RDFS, Graph, URIRef
from rdflib.namespace import SKOS

try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준

AGT = kb_lib.AGT


def check_labels(per_file: dict[str, Graph]) -> list[str]:
    errors = []
    for path, g in per_file.items():
        for term in kb_lib.defined_terms(g):
            langs = {
                lbl.language
                for lbl in g.objects(term, RDFS.label)
                if getattr(lbl, "language", None)
            }
            missing = {"ko", "en"} - langs
            if missing:
                errors.append(
                    f"[labels] {path}: {g.qname(term)} 에 rdfs:label 누락 (언어: {sorted(missing)})"
                )
            if (term, SKOS.definition, None) not in g:
                errors.append(f"[labels] {path}: {g.qname(term)} 에 skos:definition 없음")
    return errors


def check_boundary(per_file: dict[str, Graph]) -> list[str]:
    owner: dict[URIRef, str] = {}
    errors = []
    for path, g in per_file.items():
        for term in kb_lib.defined_terms(g):
            if term in owner and owner[term] != path:
                errors.append(
                    f"[boundary] {g.qname(term)} 가 두 모듈에서 정의됨: {owner[term]}, {path}"
                )
            owner.setdefault(term, path)
    return errors


def check_vocab(data_files: dict[str, Graph], ontology: Graph) -> list[str]:
    defined = kb_lib.defined_terms(ontology)
    errors = []
    for path, g in data_files.items():
        preds = {p for p in g.predicates() if isinstance(p, URIRef)}
        for p in sorted(preds):
            iri = str(p)
            if kb_lib.is_well_known(iri):
                continue
            if p in defined:
                continue
            if iri.startswith(str(AGT)):
                errors.append(f"[vocab] {path}: 온톨로지에 정의되지 않은 agt: 술어 {iri}")
            else:
                errors.append(f"[vocab] {path}: 미등록 어휘의 술어 {iri} (0.3절 네임스페이스 참조)")
    return errors


def check_odd_refs(merged: Graph, odd: Graph) -> list[str]:
    errors = []
    odd_subjects = {s for s in odd.subjects() if isinstance(s, URIRef)}
    for s, o in merged.subject_objects(AGT.refersTo):
        if o not in odd_subjects:
            errors.append(
                f"[odd-ref] {merged.qname(s)} 가 ODD에 없는 속성을 참조: {o} (0.4절 — ODD를 먼저 확장하라)"
            )
    return errors


def check_dangling(merged: Graph) -> list[str]:
    """저장소 안을 가리키는 링크의 대상이 실재하는가 (참조 무결성, 8.2절).

    인용·구성체 부분·가정·출처처럼 id: 개체를 가리키는 술어의 목적어는 그래프에
    주어로 나타나야 한다. 나타나지 않으면 끊어진 링크이고, 끊어진 링크는 실제
    구조를 오도하므로 없는 것보다 해롭다 (8.6절).
    """
    checked = (
        kb_lib.AGT.cites,
        kb_lib.AGT.hasDirectPart,
        kb_lib.AGT.assumes,
        kb_lib.AGT.satisfies,
        kb_lib.AGT.refines,
    )
    subjects = set(merged.subjects())
    errors = []
    for pred in checked:
        for s, o in merged.subject_objects(pred):
            if isinstance(o, URIRef) and str(o).startswith(str(kb_lib.ID)) and o not in subjects:
                errors.append(f"[dangling] {merged.qname(s)} 의 {merged.qname(pred)} 대상이 없다: {o}")
    return errors


def check_verify(merged: Graph, query_dir: str) -> list[str]:
    """안티패턴 계층 (노트 2.5절) — '이런 트리플이 존재하면 실패'를 SPARQL로 명세.

    tools/verify-queries/*.rq 하나가 안티패턴 하나다. 결과 행이 나오면 그 행 수만큼
    위반이며, 질의 첫 주석 줄이 실패 메시지의 근거가 된다. shape로 쓰기 어색한
    제약(연쇄·부정·집계)이 여기로 온다.
    """
    from pathlib import Path
    errors = []
    for rq in sorted(Path(query_dir).glob("*.rq")):
        text = rq.read_text(encoding="utf-8")
        title = text.splitlines()[0].lstrip("# ").strip() if text.startswith("#") else rq.stem
        try:
            rows = list(merged.query(text))
        except Exception as e:
            errors.append(f"[verify] {rq.name}: 질의 자체가 실패 — {e}")
            continue
        for row in rows[:20]:
            vals = " ".join(str(v) for v in row)
            errors.append(f"[verify] {rq.stem}: {vals}  ({title})")
        if len(rows) > 20:
            errors.append(f"[verify] {rq.stem}: … 외 {len(rows)-20}건")
    return errors


def check_shacl(merged: Graph, shapes: Graph, reason: bool) -> list[str]:
    from pyshacl import validate as shacl_validate

    conforms, _, text = shacl_validate(
        merged,
        shacl_graph=shapes,
        ont_graph=None,
        inference="rdfs" if not reason else "both",
        abort_on_first=False,
        allow_infos=True,
        allow_warnings=False,
    )
    return [] if conforms else [f"[shacl] {text}"]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ontology", nargs="*", default=[], help="T-Box 모듈 파일들 (*-ontology, *-rules)")
    ap.add_argument("--shapes", nargs="*", default=[], help="SHACL shape 파일들 (*-shapes)")
    ap.add_argument("--odd", nargs="*", default=[], help="ODD 파일들 (*-odd)")
    ap.add_argument("--data", nargs="*", default=[], help="A-Box 파일들 (*-kg, *-space)")
    ap.add_argument("--reason", action="store_true", help="SHACL 전에 OWL-RL 추론 적용")
    ap.add_argument("--verify-queries", default="", help="안티패턴 SPARQL 디렉토리 (2.5절 verify 계층)")
    args = ap.parse_args()

    errors: list[str] = []

    try:
        onto_merged, onto_files = kb_lib.load_merged(args.ontology)
        odd_merged, odd_files = kb_lib.load_merged(args.odd)
        data_merged, data_files = kb_lib.load_merged(args.data)
        shapes_merged, _ = kb_lib.load_merged(args.shapes)
    except Exception as e:  # 파싱 실패 = syntax 게이트 실패
        print(f"FAIL [syntax] {e}")
        return 1

    errors += check_labels(onto_files)
    errors += check_boundary(onto_files)
    errors += check_vocab({**odd_files, **data_files}, onto_merged)

    merged = onto_merged + odd_merged + data_merged
    if args.odd:
        errors += check_odd_refs(merged, odd_merged)
    if data_files:
        errors += check_dangling(merged)
    if args.shapes:
        errors += check_shacl(merged, shapes_merged, args.reason)
    if args.verify_queries:
        errors += check_verify(merged, args.verify_queries)

    if errors:
        for e in errors:
            print(f"FAIL {e}")
        print(f"\nFAIL — {len(errors)}건")
        return 1

    n_files = len(onto_files) + len(odd_files) + len(data_files)
    print(f"PASS — 파일 {n_files}개, 트리플 {len(merged)}개")
    return 0


if __name__ == "__main__":
    sys.exit(main())
