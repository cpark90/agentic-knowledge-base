#!/usr/bin/env python3
"""검사 게이트 (노트 6.7절) — 온톨로지 품질 검사(2.5절) + SHACL(4.4절) + ODD 참조(3.3절).

검사 항목
  syntax      모든 TTL이 파싱된다
  labels      온톨로지가 정의한 모든 agt: 용어에 rdfs:label 한/영 + skos:definition (2.5절)
  boundary    한 agt: 용어는 정확히 한 모듈 파일에서만 정의된다 (2.3절 경계 규칙)
  vocab       데이터 그래프의 술어는 온톨로지 정의 또는 표준 어휘 안에 있다 (4.4절 일관성,
              Part XIII "어휘 우회" 리스크). --standard-vocab <원문...> 을 주면 그 원문
              (PROV-O·SKOS, MODULE.bazel http_file 해시 고정)의 네임스페이스에 속한 용어가
              실제로 거기 정의돼 있는지까지 본다 — 접두사만 맞는 오타를 잡는다
  odd-ref     agt:refersTo 의 대상은 ODD 그래프에 존재한다 — "ODD에 없는 속성을 참조하는
              스코프나 가정은 존재할 수 없다" (0.4절)
  dangling    저장소 안을 가리키는 링크의 대상이 실재한다. agt:usesConcept 의 대상은
              온톨로지가 정의한 용어여야 한다 (dependency-graph-design §5 참조 무결성)
  shacl       (--shapes) OWL-RL 추론 후 pySHACL 적합성 (--reason 시 추론 적용)

경고(비영 종료 아님, `warn [검사명]` 접두사)
  usesConcept-deprecated  agt:usesConcept 의 대상이 폐기된 용어(owl:deprecated true 또는
              라벨의 "(deprecated)"/"(폐기)")다 — 용어 일관성 (dependency-graph-design §5)

실패는 비영(non-zero) 종료 — bazel test 가 곧 게이트다.
"""

from __future__ import annotations

import argparse
import sys

from rdflib import OWL, RDF, RDFS, XSD, Graph, URIRef
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


def _namespace(iri: URIRef) -> str:
    s = str(iri)
    return s[: max(s.rfind("#"), s.rfind("/")) + 1]


def load_standard_vocab(paths: list[str]) -> tuple[set[URIRef], set[str]]:
    """등록 표준 어휘 원문(PROV-O·SKOS — MODULE.bazel 의 http_file 이 해시 고정으로 가져온다)이
    정의하는 용어와, 검사 대상이 되는 네임스페이스.

    네임스페이스는 원문이 정의한 용어에서 파생한다(PROV-O 원문은 rdfs·owl 주석 속성도 선언하므로
    기본 어휘 넷은 뺀다) — 원문을 하나 더 등록하면 그 어휘가 그대로 검사 대상이 된다.
    """
    from rdflib.util import guess_format

    terms: set[URIRef] = set()
    for p in paths:
        g = Graph()
        g.parse(p, format=guess_format(p) or "turtle")
        for t in kb_lib.DEFINING_TYPES:
            terms |= {s for s in g.subjects(RDF.type, t) if isinstance(s, URIRef)}
    base = {str(RDF), str(RDFS), str(OWL), str(XSD)}
    return terms, {_namespace(t) for t in terms} - base


def check_standard_vocab(graphs: dict[str, Graph], terms: set[URIRef], namespaces: set[str]) -> list[str]:
    """(--standard-vocab) 표준 어휘 네임스페이스의 용어는 등록 원문에 정의돼 있어야 한다.

    check_vocab 은 접두사(WELL_KNOWN_PREFIXES)만 보므로 prov:wasDerivedfrom 같은 오타가 통과한다.
    원문이 있으면 술어뿐 아니라 주어·목적어 자리(타입, subPropertyOf 대상)의 용어까지 실재를 본다.
    """
    errors = []
    for path, g in graphs.items():
        seen: set[URIRef] = set()
        for s, p, o in g:
            for node in (s, p, o):
                if isinstance(node, URIRef) and node not in seen:
                    seen.add(node)
                    if _namespace(node) in namespaces and node not in terms:
                        errors.append(f"[vocab] {path}: 표준 어휘 원문에 정의되지 않은 용어 {node} (--standard-vocab 기준)")
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


def check_dangling(merged: Graph, ontology: Graph | None = None) -> list[str]:
    """저장소 안을 가리키는 링크의 대상이 실재하는가 (참조 무결성, 8.2절).

    인용·복합체 부분·가정·출처처럼 id: 개체를 가리키는 술어의 목적어는 그래프에
    주어로 나타나야 한다. 나타나지 않으면 끊어진 링크이고, 끊어진 링크는 실제
    구조를 오도하므로 없는 것보다 해롭다 (8.6절).

    agt:usesConcept 은 개념 IRI를 바로 가리킨다(dependency-graph-design (f)) — 대상은
    온톨로지가 정의한 agt: 용어여야 한다. 온톨로지를 안 주면 병합 그래프의 주어로 대신한다.
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
    concepts = kb_lib.defined_terms(ontology) if ontology is not None else subjects
    for s, o in merged.subject_objects(kb_lib.AGT.usesConcept):
        if o not in concepts:
            errors.append(f"[dangling] {_chunk_location(merged, s)} 의 agt:usesConcept 대상이 온톨로지에 정의되지 않았다: {o}")
    return errors


def _chunk_location(merged: Graph, chunk: URIRef) -> str:
    return next((str(l) for l in merged.objects(chunk, kb_lib.AGT.assertionLocation)), merged.qname(chunk))


def _agt_qname(merged: Graph, term: URIRef) -> str:
    """병합 그래프에는 접두사가 묶여 있지 않아 qname 이 ns2: 처럼 나온다 — agt: 용어는 그대로 적는다."""
    return f"agt:{str(term)[len(str(AGT)):]}" if str(term).startswith(str(AGT)) else merged.qname(term)


def deprecated_terms(ontology: Graph) -> set[URIRef]:
    """폐기된 용어 — owl:deprecated true 가 기준이고, 라벨의 "(deprecated)"/"(폐기)" 표기도 인정한다."""
    terms = {s for s, v in ontology.subject_objects(OWL.deprecated) if str(v).lower() == "true"}
    for s, lbl in ontology.subject_objects(RDFS.label):
        if "(deprecated)" in str(lbl) or "(폐기)" in str(lbl):
            terms.add(s)
    return {t for t in terms if isinstance(t, URIRef)}


def check_deprecated_concepts(merged: Graph, ontology: Graph) -> list[str]:
    """경고(FAIL 아님): agt:usesConcept 의 대상이 폐기된 용어다 — 용어 일관성 (dependency-graph-design §5).

    폐기는 삭제가 아니므로(p0-deprecate-not-delete) 링크 자체는 유효하다. 본문이 옛 용어를 쓰고
    있다는 신호이며, 재검증 시점에 대체 용어로 고칠 대상이다.
    """
    deprecated = deprecated_terms(ontology)
    return sorted(
        f"[usesConcept-deprecated] {_chunk_location(merged, s)} → {_agt_qname(merged, o)}"
        for s, o in merged.subject_objects(kb_lib.AGT.usesConcept)
        if o in deprecated
    )


def check_writer(merged: Graph) -> list[str]:
    """생성자의 쓰기 권한 (AGENTS 표 · kg/catalog-kg.ttl agt:writes) — write plane 경계를 규약에서 기계 검사로.

    generated.by 가 `<역할>/<모델>` 이면 그 역할이 청크의 plane 을 쓸 수 있어야 한다. 못 쓰는 역할(hci·inspection)이
    만든 청크는 쓰기 권한이 있는 역할의 verified(인수)가 있어야 통과한다. 역할이 아닌 생성자(`claude/…`)는 검사하지 않는다.
    """
    from rdflib import RDF, URIRef
    AGT, ID = kb_lib.AGT, kb_lib.ID
    roles = {str(r).split("/")[-1].replace("role-", ""): r for r in merged.subjects(RDF.type, AGT.Role)}
    errors, unattributed = [], 0
    for chunk, by in merged.subject_objects(AGT.generatedBy):
        producer = str(by).split("/")[0]
        if producer not in roles:
            unattributed += 1
            continue
        plane_cls = next((c for c in merged.objects(chunk, RDF.type) if str(c).endswith("Chunk")), None)
        if plane_cls is None or (roles[producer], AGT.writes, plane_cls) in merged:
            continue
        endorsed = any(str(v).split("/")[0] in roles and (roles[str(v).split("/")[0]], AGT.writes, plane_cls) in merged
                       for v in merged.objects(chunk, AGT.verifiedBy))
        if not endorsed:
            where = next((str(l) for l in merged.objects(chunk, AGT.assertionLocation)), merged.qname(chunk))
            errors.append(f"[writer] {where}: 생성자 {by} 의 역할 {producer} 는 {str(plane_cls).split('/')[-1]} 쓰기 권한이 없다 — "
                          f"담당 역할의 verified(인수) 또는 되돌림 (AGENTS 표 · 11.2절)")
    if unattributed:
        print(f"info [writer] 역할 없는 생성자의 청크 {unattributed}개 — 검사 대상 아님 (2026-09-11 이전 표기)")
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
    ap.add_argument("--standard-vocab", nargs="*", default=[],
                    help="등록 표준 어휘 원문(PROV-O·SKOS 등). 주면 그 네임스페이스의 용어가 원문에 정의돼 있는지까지 본다")
    args = ap.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    try:
        onto_merged, onto_files = kb_lib.load_merged(args.ontology)
        odd_merged, odd_files = kb_lib.load_merged(args.odd)
        data_merged, data_files = kb_lib.load_merged(args.data)
        shapes_merged, shapes_files = kb_lib.load_merged(args.shapes)
        std_terms, std_namespaces = load_standard_vocab(args.standard_vocab)
    except Exception as e:  # 파싱 실패 = syntax 게이트 실패
        print(f"FAIL [syntax] {e}")
        return 1

    errors += check_labels(onto_files)
    errors += check_boundary(onto_files)
    errors += check_vocab({**odd_files, **data_files}, onto_merged)
    if args.standard_vocab:
        errors += check_standard_vocab({**onto_files, **shapes_files, **odd_files, **data_files}, std_terms, std_namespaces)

    merged = onto_merged + odd_merged + data_merged
    if args.odd:
        errors += check_odd_refs(merged, odd_merged)
    if data_files:
        errors += check_dangling(merged, onto_merged if args.ontology else None)
        errors += check_writer(merged)
        if args.ontology:
            warnings += check_deprecated_concepts(merged, onto_merged)
    if args.shapes:
        errors += check_shacl(merged, shapes_merged, args.reason)
    if args.verify_queries:
        errors += check_verify(merged, args.verify_queries)

    for w in warnings:
        print(f"warn {w}")
    if warnings:
        print(f"warn — {len(warnings)}건 (게이트 실패 아님)")

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
