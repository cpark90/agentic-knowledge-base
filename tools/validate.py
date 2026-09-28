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
  dangling    저장소 안을 가리키는 링크의 대상이 실재한다. 주석의 대상(agt:targets)도 본다 — 링크 개체가
              아니라 직접 트리플뿐이므로 여기가 유일한 실재 검사다. agt:usesConcept 의 대상은
              온톨로지가 정의한 용어여야 한다 (dependency-graph-design §5 참조 무결성).
              prov:specializationOf(분할 조각 → 원본)의 대상도 포함한다
  space       설계 공간(agt:Space)의 규율 (p9-candidate-storage, 요구 r-011): 변수의 출발 항목과 후보의 대상이
              실재하고 · 후보의 출발점·링크 타입이 그 공간의 변수와 같고 · spaceStatus resolved 면 확정 후보가
              정확히 하나이며 · 배제된 후보에 (−) 증거, 확정된 후보에 구축·실행 (+) 증거가 있다
  specialization  prov:specializationOf 의 대상은 살아 있는(deprecated 아닌) 같은 plane 의 청크이고 사슬은 순환하지
              않는다 (p10-split-keeps-work-identity — 청크 uuid 는 work-id, 링크 IRI 는 뿌리 uuid 로 계산)
  catalog     (--data 에 agt:Harness 가 있을 때) 카탈로그 정합성 (AGENTS.md 역할 절 · STYLEGUIDE §5 · 9.2·9.6절):
              하네스가 hasRole 하는 역할마다 대응 스코프(id:role-<x> ↔ id:scope-<x>)가 있고 하네스가 grants 한다 ·
              역할마다 read plane ≥ 1 · write plane 은 역할 사이에 겹치지 않는다 · maxConcurrent 합 ≤ ODD 동적 요소
              id:cond-concurrent-agents 의 상한(--odd 의 agt:conditionValue). 상한을 못 뽑으면 EXIT_CONFIG ·
              스코프는 ODD 의 부분집합이다 — agt:subsetOf 대상이 ODD 그래프의 agt:ODD 이고 include/exclude 조건이
              그 ODD 의 agt:hasCondition 에 등록돼 있다 (0.4절, 2026-09-26 metrics 지표에서 게이트로 승격)
  element-drop 소스 요소의 전수와 방출 전수의 차가 공집합이다 (현상 P19 의 관측 수단, 8.21절 G1). 둘을 본다 —
              (a) --chunk-files 를 주면 청크 frontmatter 의 최상위 키 집합에서 chunk2kg 가 소비하는 키 집합
              (REQUIRED ∪ LINK_KEYS ∪ kb_lib.CHUNK_OPTIONAL_KEYS)을 뺀 차. 모르는 키는 조용히 버려지는 요소다.
              (b) 프로파일이 선언한 plane 실체 클래스 집합과 chunk2kg.PROFILE_SUBSTANCE 치역의 대칭차. 어휘에만
              있으면 데이터가 그 클래스를 못 받고, 생성기에만 있으면 정의 없는 클래스가 그래프에 나타난다
  residency   (--shapes --residency defs/kb.bzl) 수준 허용표가 한 곳에만 적혀 있다 — shape `residency-shapes.ttl` 의
              plane × level 구간이 `defs/kb.bzl` 의 `RESIDENCY` 와 같다. 원본은 Starlark 리터럴이다(분석 시점
              판정이 파일을 읽지 못하므로). 갈리면 shape 를 맞춘다 (M1 단일 정의처, 2026-09-26)
  shacl       (--shapes) OWL-RL 추론 후 pySHACL 적합성 (--reason 시 추론 적용)

경고(비영 종료 아님, `warn [검사명]` 접두사)
  usesConcept-deprecated  agt:usesConcept 의 대상이 폐기된 용어(owl:deprecated true 또는
              라벨의 "(deprecated)"/"(폐기)")다 — 용어 일관성 (dependency-graph-design §5)

출력·종료 (agrtls-practices-review A): 위반은 `FAIL [<검사명>] <경로>: <메시지>` 한 줄씩 + EXIT_FAIL.
  파싱되지 않는 입력(syntax)·파일 없음은 게이트가 판정을 내릴 수 없는 상태이므로 EXIT_CONFIG,
  그래프 파일 0건은 EXIT_SKIP — SKIP 은 PASS 가 아니다. bazel test 가 곧 게이트다.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from rdflib import OWL, RDF, RDFS, XSD, Graph, URIRef
from rdflib.namespace import SKOS

try:
    from tools import chunk2kg  # 소비되는 frontmatter 키·plane 실체 사상의 정의처 (element-drop)
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path에 있다
except ImportError:
    import chunk2kg
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준

AGT = kb_lib.AGT
_FM_KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):")  # frontmatter 의 최상위 키 (element-drop)
EXIT_FAIL = getattr(kb_lib, "EXIT_FAIL", 1)      # 판정 실패 (단일 정의처 kb_lib — 없으면 같은 값)
EXIT_CONFIG = getattr(kb_lib, "EXIT_CONFIG", 2)  # 파일 없음·파싱 불가 입력
EXIT_SKIP = getattr(kb_lib, "EXIT_SKIP", 3)      # 검사 대상 0건


class SyntaxFailure(Exception):
    """파일 하나가 파싱되지 않는다 — 어느 파일인지를 메시지에 지닌다."""


class ConfigFailure(Exception):
    """게이트가 판정을 내릴 수 없는 설정·입력 상태(EXIT_CONFIG) — 메시지가 `FAIL [<검사명>] …` 한 줄이다."""


def load_files(paths: list[str]) -> tuple[Graph, dict[str, Graph]]:
    """파일별 그래프와 병합 그래프 — 파싱 실패는 파일을 지목하는 SyntaxFailure 로."""
    merged, per_file = Graph(), {}
    for p in paths:
        try:
            g = kb_lib.load_graph(p)
        except Exception as e:  # rdflib 파서·OSError 모두 — 판정 불가 입력
            raise SyntaxFailure(f"{p}: 파싱 실패 — {e}") from e
        per_file[p] = g
        merged += g
    return merged, per_file


def _where(files: dict[str, Graph], node) -> str:
    """노드를 주어로 가진 파일 — FAIL 메시지의 <경로> 자리. 어느 파일에도 없으면 IRI 그대로."""
    for path, g in files.items():
        if (node, None, None) in g:
            return path
    return str(node)


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
                    f"[boundary] {path}: {g.qname(term)} 가 {owner[term]} 에서 이미 정의됨 — 한 용어는 한 모듈 파일에서만 정의된다 (2.3절)"
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


def check_odd_refs(merged: Graph, odd: Graph, files: dict[str, Graph]) -> list[str]:
    errors = []
    odd_subjects = {s for s in odd.subjects() if isinstance(s, URIRef)}
    for s, o in merged.subject_objects(AGT.refersTo):
        if o not in odd_subjects:
            errors.append(
                f"[odd-ref] {_where(files, s)}: {merged.qname(s)} 가 ODD에 없는 속성을 참조: {o} (0.4절 — ODD를 먼저 확장하라)"
            )
    return errors


def check_dangling(merged: Graph, ontology: Graph | None, files: dict[str, Graph]) -> list[str]:
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
        kb_lib.AGT.verifies,     # V&V → 개발 (7.5절)
        kb_lib.AGT.derivesFrom,  # 검증 목표 → 요구 (8.3절 functional 높이)
        kb_lib.AGT.overlapsWith,  # relatedTo 족의 약한 잎 (overlap-ontology) — 링크 키이므로 대상 실재를 여기서 본다
        kb_lib.AGT.targets,      # 주석 → 대상 (p7-commentary-form) — 링크 개체가 아니라 직접 트리플뿐이라 여기가 유일한 실재 검사다
        kb_lib.PROV.specializationOf,  # 분할 조각 → 원본 (p10-split-keeps-work-identity) — 없는 원본을 특수화할 수 없다
    )
    subjects = set(merged.subjects())
    errors = []
    for pred in checked:
        for s, o in merged.subject_objects(pred):
            if isinstance(o, URIRef) and str(o).startswith(str(kb_lib.ID)) and o not in subjects:
                errors.append(f"[dangling] {_where(files, s)}: {merged.qname(s)} 의 {merged.qname(pred)} 대상이 없다: {o} (참조 무결성 8.2절)")
    concepts = kb_lib.defined_terms(ontology) if ontology is not None else subjects
    for s, o in merged.subject_objects(kb_lib.AGT.usesConcept):
        if o not in concepts:
            errors.append(f"[dangling] {_chunk_location(merged, s)} 의 agt:usesConcept 대상이 온톨로지에 정의되지 않았다: {o}")
    return errors


def _frontmatter_keys(path: str) -> set[str]:
    """청크 파일의 최상위 frontmatter 키 — 중첩 키(`composite.ordered` 등)는 그 부모가 대표한다."""
    text = Path(path).read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return set()
    return {m.group(1) for m in (_FM_KEY.match(l) for l in text.split("---\n", 2)[1].splitlines()) if m}


def check_element_drop(ontology: Graph | None, chunk_files: list[str]) -> list[str]:
    """소스 요소의 전수와 방출 전수의 차 (게이트 id `element-drop`, 현상 P19 의 관측 수단).

    참조 저장소 R3 이 남긴 형태 — 반영이 알려진 요소 집합에서 조립되므로 어휘가 없는 소스 요소는 슬롯을 얻지
    못해 조용히 빠진다. 그것을 잡으려면 소스를 전수로 세고 방출과 대조하는 수밖에 없다. 차가 나오면 대응은
    요소를 버리는 것이 아니라 어휘를 넓히는 것이다 (가정 id:asm-missing-vocabulary-is-signal).
    """
    errors = []
    consumed = set(chunk2kg.REQUIRED) | set(chunk2kg.LINK_KEYS) | set(kb_lib.CHUNK_OPTIONAL_KEYS)
    for path in sorted(chunk_files):
        for key in sorted(_frontmatter_keys(path) - consumed):
            errors.append(f"[{kb_lib.ELEMENT_DROP_GATE}] {path}: frontmatter 키 {key!r} 를 chunk2kg 가 소비하지 않는다 — "
                          f"방출되지 않는 키는 조용히 버려지는 소스 요소다. 키를 쓰려면 chunk2kg 가 읽고 "
                          f"kb_lib.CHUNK_OPTIONAL_KEYS 에 등재해야 한다 (8.21절 G1 현상 P19)")
    if ontology is None:
        return errors
    plane_classes = {URIRef(str(AGT) + q.split(":", 1)[1]) for q in chunk2kg.PLANE_CLASS.values()}
    declared = {s for s, o in ontology.subject_objects(RDFS.subClassOf) if o in plane_classes}
    emitted = {URIRef(str(AGT) + q.split(":", 1)[1]) for q in chunk2kg.PROFILE_SUBSTANCE.values()}
    for term in sorted(declared - emitted, key=str):
        errors.append(f"[{kb_lib.ELEMENT_DROP_GATE}] {_where({}, term)}: 실체 클래스 {ontology.qname(term)} 가 어휘에만 있다 — "
                      f"chunk2kg.PROFILE_SUBSTANCE 가 어느 plane 도 이 클래스로 타이핑하지 않아 데이터가 닿지 않는다 (CQ-28 고립 개념)")
    for term in sorted(emitted - declared, key=str):
        errors.append(f"[{kb_lib.ELEMENT_DROP_GATE}] chunk2kg.PROFILE_SUBSTANCE: 실체 클래스 {term} 가 생성기에만 있다 — "
                      f"프로파일이 plane 청크 클래스의 하위로 선언하지 않았다. 정의 없는 클래스는 어휘 밖이다 (2.3절 경계 규칙)")
    return errors


def check_space(merged: Graph, files: dict[str, Graph]) -> list[str]:
    """설계 공간(agt:Space)의 규율 (결정 p9-candidate-storage, 요구 r-011-no-groundless-assignment, 게이트 id `space`).

    후보는 확정 링크와 다른 자리에 살고 결코 deps 가 되지 않으므로, Bazel 이 로드 시점에 잡아 주는 것(끝점의 실재·방향)을
    여기서 그래프로 대신 판정한다. 검사는 다섯이다.
      (a) 변수의 출발 항목(agt:variableFrom)과 각 후보의 도착점(agt:linkTo)이 실재한다 — 끊긴 후보는 실제 선택지를 오도한다.
      (b) 후보의 출발점·링크 타입이 그 공간의 변수와 같다 — 다른 변수의 후보가 섞이면 "무엇이 열려 있는가"의 답이 틀린다.
      (c) agt:spaceStatus 가 resolved 면 확정 후보가 정확히 하나다 — 둘이면 할당이 아니고 0 이면 해소가 아니다.
      (d) 배제된 후보(linkState invalid)에 (−) 증거가 있다 — 근거 없는 배제 금지가 r-011 의 요지다.
      (e) 확정 후보(linkState confirmed)에 구축(+) 또는 실행(+) 증거가 있다 — 근거 없는 할당 금지 (9.11절).
    """
    AGT_ = kb_lib.AGT
    gate = kb_lib.SPACE_GATE
    subjects = set(merged.subjects())
    errors = []
    for space in sorted(merged.subjects(RDF.type, AGT_.Space), key=str):
        where = _chunk_location(merged, space)
        froms = list(merged.objects(space, AGT_.variableFrom))
        kinds = list(merged.objects(space, AGT_.variableKind))
        for o in froms:  # (a) 출발 항목의 실재 — 수는 shape(agt:SpaceShape)가 본다
            if isinstance(o, URIRef) and str(o).startswith(str(kb_lib.ID)) and o not in subjects:
                errors.append(f"[{gate}] {where}: 변수의 출발 항목이 없다: {_qname(merged, o)} — 없는 항목에 변수를 걸 수 없다 (참조 무결성 8.2절)")
        confirmed = 0
        for link in sorted(merged.objects(space, AGT_.hasCandidate), key=str):
            to = next(merged.objects(link, AGT_.linkTo), None)
            state = str(next(merged.objects(link, AGT_.linkState), ""))
            label = _qname(merged, to) if to is not None else kb_lib.NONE_MARK
            if isinstance(to, URIRef) and str(to).startswith(str(kb_lib.ID)) and to not in subjects:  # (a)
                errors.append(f"[{gate}] {where}: 후보의 대상이 없다: {label} — 없는 항목은 후보가 될 수 없다 (참조 무결성 8.2절)")
            for o in merged.objects(link, AGT_.linkFrom):  # (b)
                if froms and o not in froms:
                    errors.append(f"[{gate}] {where}: 후보 {label} 의 출발점 {_qname(merged, o)} 이 변수의 출발 항목 "
                                  f"{_qname(merged, froms[0])} 과 다르다 — 한 공간은 변수 하나다 (p9-candidate-storage)")
            for o in merged.objects(link, AGT_.linkKind):  # (b)
                if kinds and o not in kinds:
                    errors.append(f"[{gate}] {where}: 후보 {label} 의 링크 타입 {_agt_qname(merged, o)} 이 변수의 타입 "
                                  f"{_agt_qname(merged, kinds[0])} 과 다르다 — 타입이 다르면 다른 변수다 (p9-uncertainty-as-link-uncertainty)")
            polarities = {str(pol) for e in merged.objects(link, AGT_.hasEvidence) for pol in merged.objects(e, AGT_.polarity)}
            if state == kb_lib.LINK_STATE_INVALID and "-" not in polarities:  # (d)
                errors.append(f"[{gate}] {where}: 배제된 후보 {label} 에 배제 근거가 없다 — 후보를 지우려면 (−) 증거 한 줄이 있어야 한다 "
                              f"(`eliminated_by`, 요구 r-011-no-groundless-assignment)")
            if state == kb_lib.LINK_STATE_CONFIRMED:  # (e)
                confirmed += 1
                kinds_ok = {str(k).split("/")[-1] for e in merged.objects(link, AGT_.hasEvidence)
                            for k in merged.objects(e, AGT_.evidenceKind)}
                if not kinds_ok & set(kb_lib.SPACE_CONFIRMING_EVIDENCE):
                    errors.append(f"[{gate}] {where}: 확정된 후보 {label} 에 지지 증거가 없다 — 구축 기록 또는 실행 결과"
                                  f"({' | '.join(kb_lib.SPACE_CONFIRMING_EVIDENCE)}) 없이 확정할 수 없다 "
                                  f"(9.11절, 요구 r-011-no-groundless-assignment)")
        status = str(next(merged.objects(space, AGT_.spaceStatus), ""))
        if status == "resolved" and confirmed != 1:  # (c)
            errors.append(f"[{gate}] {where}: agt:spaceStatus 가 resolved 인데 확정 후보가 {confirmed}개다 — 정확히 하나여야 한다 "
                          f"(둘이면 할당이 아니고 0 이면 해소가 아니다, p9-candidate-storage)")
    return errors


def check_specialization(merged: Graph, files: dict[str, Graph]) -> list[str]:
    """prov:specializationOf 규율 (p10-split-keeps-work-identity, 게이트 id `specialization`).

    분할 조각은 원 청크를 특수화한다 — 같은 것의 다른 입도다. 그래서 대상은 (a) 같은 plane 의 청크이고 (b) 살아 있어야 하며
    (deprecated 원본의 조각은 원본을 승계했어야 한다), (c) 사슬은 순환하지 않는다 (뿌리 uuid 를 계산할 수 없다). 대상 부재는
    check_dangling 이 본다. 순환은 성분마다 한 번 보고한다.
    """
    gate = kb_lib.SPECIALIZATION_GATE
    plane = kb_lib.chunk_planes(merged)
    errors = []
    spec: dict = {}
    for s, o in sorted(merged.subject_objects(kb_lib.PROV.specializationOf), key=lambda so: (str(so[0]), str(so[1]))):
        where = _chunk_location(merged, s)
        if not isinstance(o, URIRef) or o not in plane:
            continue  # 청크가 아닌 대상은 dangling 이 보고한다
        spec[s] = o
        if s == o:
            errors.append(f"[{gate}] {where}: prov:specializationOf 가 자기 자신이다 — 조각은 원본을 특수화한다")
            continue
        if plane.get(s) != plane[o]:
            errors.append(f"[{gate}] {where}: prov:specializationOf 대상 {_qname(merged, o)} 의 plane 이 다르다 ({plane.get(s)} ≠ {plane[o]}) — "
                          f"분할 조각은 같은 plane 의 원본을 특수화한다 (p10-split-keeps-work-identity)")
        if str(next(merged.objects(o, kb_lib.AGT.status), "")) == "deprecated":
            errors.append(f"[{gate}] {where}: prov:specializationOf 대상 {_qname(merged, o)} 이 deprecated 다 — 원본은 살아 있는 청크여야 한다 "
                          f"(폐기된 원본의 조각은 uuid 를 승계했어야 한다)")
    reported: set = set()
    for start in sorted(spec, key=str):
        seen, cur = [], start
        while cur in spec and cur not in seen:
            seen.append(cur)
            cur = spec[cur]
        if cur in seen:  # 순환 — cur 부터 되돌아온다
            cycle = tuple(seen[seen.index(cur):])
            key = min(map(str, cycle))
            if key not in reported:
                reported.add(key)
                errors.append(f"[{gate}] {_chunk_location(merged, cycle[0])}: prov:specializationOf 사슬이 순환한다: "
                              + " → ".join(_qname(merged, c) for c in cycle + (cycle[0],)) + " — 뿌리 uuid 를 계산할 수 없다")
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


def _qname(merged: Graph, term) -> str:
    """agt:·id: 용어는 접두사로 적는다 — 병합 그래프의 qname 은 ns2: 처럼 나온다."""
    for prefix, ns in (("agt", AGT), ("id", kb_lib.ID)):
        if str(term).startswith(str(ns)):
            return f"{prefix}:{str(term)[len(str(ns)):]}"
    return merged.qname(term) if isinstance(term, URIRef) else str(term)


def check_catalog(merged: Graph, odd: Graph | None, files: dict[str, Graph]) -> list[str]:
    """카탈로그 정합성 (AGENTS.md 역할 절 · STYLEGUIDE §5 · 노트 9.2·9.6절) — 규약이던 것을 게이트로 (2026-09-13).

    데이터 그래프에 agt:Harness 가 없으면 대상이 아니다. 하네스마다:
      (a) hasRole 하는 역할마다 대응 스코프가 실재하고 하네스가 grants 한다. 대응은 슬러그다 — id:role-<x> ↔ id:scope-<x>
          (kb_lib.ROLE_ID_PREFIX·SCOPE_ID_PREFIX, rules §개체 IRI 접두사). 카탈로그에 역할→스코프 술어는 없다.
      (b) 역할마다 agt:reads 가 하나 이상이다 — 읽지 못하는 역할은 작업 집합을 받을 수 없다.
      (c) agt:writes 의 plane 은 같은 KB(agt:writesIn — 없으면 kb/dev) 안에서 역할 사이에 겹치지 않는다 — 설계·구현·운영 분리 (9.2절).
          V&V KB 는 코어의 두 번째 인스턴스라 plane 이름이 같으므로(p8-vv-plane-instances) 겹침은 KB 별로 본다 (2026-09-19). writesIn 값은 kb_lib.KB_ROOTS 안이어야 한다.
      (d) agt:maxConcurrent 합 ≤ ODD 동적 요소 id:cond-concurrent-agents 의 상한. 상한은 --odd 그래프의 agt:conditionValue 에서
          kb_lib.odd_upper_bound 로 뽑는다. ODD 가 없거나 조건·상한을 못 뽑으면 ConfigFailure(EXIT_CONFIG) — 판정 불가지 통과가 아니다.
    첫 실행(2026-09-13): 역할 4 · 스코프 4 · write plane 겹침 0 · 합 4 ≤ 5, FAIL 0.
    """
    AGT_, ID = kb_lib.AGT, kb_lib.ID
    gate = kb_lib.CATALOG_GATE
    harnesses = sorted(s for s in merged.subjects(RDF.type, AGT_.Harness) if isinstance(s, URIRef))
    if not harnesses:
        return []
    errors: list[str] = []
    for h in harnesses:
        where = _where(files, h)
        roles = sorted(r for r in merged.objects(h, AGT_.hasRole) if isinstance(r, URIRef))
        grants = set(merged.objects(h, AGT_.grants))
        writers: dict[tuple[str, URIRef], list[URIRef]] = {}  # (KB, plane) → 역할들
        total = 0
        for r in roles:
            rq = _qname(merged, r)
            local = str(r)[len(str(ID)):] if str(r).startswith(str(ID)) else ""
            if not local.startswith(kb_lib.ROLE_ID_PREFIX):
                errors.append(f"[{gate}] {where}: 역할 {rq} 의 IRI 가 id:{kb_lib.ROLE_ID_PREFIX}<slug> 가 아니다 — 대응 스코프를 찾을 수 없다 (rules §개체 IRI 접두사)")
            else:
                scope = ID[kb_lib.SCOPE_ID_PREFIX + local[len(kb_lib.ROLE_ID_PREFIX):]]
                if (scope, RDF.type, AGT_.Scope) not in merged:
                    errors.append(f"[{gate}] {where}: 역할 {rq} 에 대응 스코프 {_qname(merged, scope)} 가 없다 — 역할마다 스코프를 선언한다 (STYLEGUIDE §5 카탈로그 완전성)")
                elif scope not in grants:
                    errors.append(f"[{gate}] {where}: 하네스 {_qname(merged, h)} 가 역할 {rq} 의 스코프 {_qname(merged, scope)} 를 agt:grants 하지 않는다 (STYLEGUIDE §5)")
            if not any(True for _ in merged.objects(r, AGT_.reads)):
                errors.append(f"[{gate}] {where}: 역할 {rq} 의 read plane 이 0 이다 — agt:reads 를 하나 이상 선언한다 (AGENTS 표 read 열)")
            kbs = _writes_in(merged, r)
            for kb in sorted(kbs - set(kb_lib.KB_ROOTS)):
                errors.append(f"[{gate}] {where}: 역할 {rq} 의 agt:writesIn {kb!r} 가 KB 경로 접두({' · '.join(kb_lib.KB_ROOTS)})가 아니다 (pe-storage-layout)")
            for plane in merged.objects(r, AGT_.writes):
                for kb in kbs:
                    writers.setdefault((kb, plane), []).append(r)
            counts = list(merged.objects(r, AGT_.maxConcurrent))
            if not counts:
                errors.append(f"[{gate}] {where}: 역할 {rq} 에 agt:maxConcurrent 가 없다 — 합을 판정할 수 없다 (9.6절)")
                continue
            try:
                total += int(counts[0])
            except (TypeError, ValueError):
                errors.append(f"[{gate}] {where}: 역할 {rq} 의 agt:maxConcurrent {counts[0]!r} 이 정수가 아니다")
        for (kb, plane), rs in sorted(writers.items(), key=lambda kv: (kv[0][0], str(kv[0][1]))):
            if len(rs) > 1:
                names = ", ".join(_qname(merged, r) for r in sorted(rs))
                errors.append(f"[{gate}] {where}: KB {kb} 의 write plane {_qname(merged, plane)} 을 역할 {names} 이 공유한다 — 설계·구현·운영은 같은 KB 안에서 같은 write plane 을 쓰지 않는다 (AGENTS 역할 절, 9.2절; agt:writesIn)")
        cond = kb_lib.CONCURRENT_AGENTS_CONDITION
        if odd is None:
            raise ConfigFailure(f"[{gate}] {where}: maxConcurrent 합의 상한은 ODD 조건 {_qname(merged, cond)} 인데 --odd 그래프가 없다")
        values = list(odd.objects(cond, AGT_.conditionValue))
        if not values:
            raise ConfigFailure(f"[{gate}] {where}: ODD 에 {_qname(merged, cond)} 의 agt:conditionValue 가 없다 — ODD 를 먼저 확장한다 (0.4절)")
        bound = kb_lib.odd_upper_bound(str(values[0]))
        if bound is None:
            raise ConfigFailure(f"[{gate}] {where}: {_qname(merged, cond)} 의 값 {str(values[0])!r} 에서 정수 상한을 뽑을 수 없다 — Range [a .. b] 또는 UpperBound 식이어야 한다")
        if total > bound:
            errors.append(f"[{gate}] {where}: 역할별 agt:maxConcurrent 합 {total} > ODD 동적 요소 {_qname(merged, cond)} 의 상한 {bound} — 역할을 줄이거나 ODD 한도를 먼저 검토한다 (AGENTS 역할 절, 9.6절)")
    errors += _check_scope_subset(merged, odd, files)
    return errors


def _check_scope_subset(merged: Graph, odd: Graph | None, files: dict[str, Graph]) -> list[str]:
    """(e) 스코프는 ODD 의 부분집합이다 (0.4절, scope-ontology agt:subsetOf·agt:includesCondition 의 정의문).

    "ODD에 없는 속성을 참조하는 스코프는 존재할 수 없다" 와 "하네스가 부여하는 스코프는 ODD 의 부분집합이다" 의 실행
    자리다. 지금까지는 `tools/metrics.py` 의 `scope_bad` 지표가 세기만 했다 (2026-09-26 게이트로 승격).
    스코프마다: agt:subsetOf 가 하나 이상이고 그 대상이 ODD 그래프의 agt:ODD 이며 · include/exclude 조건이 그 ODD 에
    agt:hasCondition 으로 등록돼 있다. 첫 실행(2026-09-26, 스코프 4 · 조건 참조 14): FAIL 0.
    """
    AGT_, gate = kb_lib.AGT, kb_lib.CATALOG_GATE
    if odd is None:
        return []
    errors: list[str] = []
    for scope in sorted(s for s in merged.subjects(RDF.type, AGT_.Scope) if isinstance(s, URIRef)):
        where, sq = _where(files, scope), _qname(merged, scope)
        odds = [o for o in merged.objects(scope, AGT_.subsetOf) if isinstance(o, URIRef)]
        if not odds:
            errors.append(f"[{gate}] {where}: 스코프 {sq} 에 agt:subsetOf 가 없다 — 어느 ODD 의 부분집합인지 밝힌다 (0.4절)")
        registered: set[URIRef] = set()
        for o in odds:
            if (o, RDF.type, AGT_.ODD) not in odd:
                errors.append(f"[{gate}] {where}: 스코프 {sq} 의 agt:subsetOf 대상 {_qname(merged, o)} 가 ODD 그래프에 agt:ODD 로 없다 — ODD 를 먼저 확장한다 (0.4절)")
            registered |= {c for c in odd.objects(o, AGT_.hasCondition) if isinstance(c, URIRef)}
        for pred in (AGT_.includesCondition, AGT_.excludesCondition):
            for c in sorted(x for x in merged.objects(scope, pred) if isinstance(x, URIRef)):
                if c not in registered:
                    errors.append(f"[{gate}] {where}: 스코프 {sq} 의 {_qname(merged, pred)} 대상 {_qname(merged, c)} 가 그 ODD 의 agt:hasCondition 목록에 없다 — ODD 밖 조건을 참조하는 스코프는 존재할 수 없다 (0.4절)")
    return errors


def _writes_in(merged: Graph, role: URIRef) -> set[str]:
    """역할이 쓰는 KB 들 — agt:writesIn 값. 없으면 개발 KB(kb_lib.KB_DEV) 하나다 (role-ontology agt:writesIn 정의)."""
    return {str(v) for v in merged.objects(role, kb_lib.AGT.writesIn)} or {kb_lib.KB_DEV}


def check_writer(merged: Graph) -> list[str]:
    """생성자의 쓰기 권한 (AGENTS 표 · kg/catalog-kg.ttl agt:writesIn·agt:writes) — write plane 경계를 규약에서 기계 검사로.

    generated.by 가 `<역할>/<모델>` 이면 그 역할이 청크의 KB 와 plane 을 쓸 수 있어야 한다. KB 는 청크의 assertionLocation 으로
    가른다(kb_lib.kb_of — kb/vv/ 아래면 V&V KB, 아니면 개발 KB) 그리고 역할의 KB 는 agt:writesIn(없으면 kb/dev)이다 (p8-vv-roles,
    2026-09-19). 못 쓰는 역할(hci)이 만든 청크는 같은 KB·plane 의 쓰기 권한이 있는 역할의 verified(인수)가 있어야 통과한다.
    역할이 아닌 생성자(`claude/…`·`process:…`)는 검사하지 않는다.
    """
    AGT = kb_lib.AGT
    gate = kb_lib.WRITER_GATE
    roles = {str(r).split("/")[-1].replace(kb_lib.ROLE_ID_PREFIX, ""): r for r in merged.subjects(RDF.type, AGT.Role)}

    def can_write(role: URIRef, kb: str, plane_cls: URIRef) -> bool:
        return kb in _writes_in(merged, role) and (role, AGT.writes, plane_cls) in merged

    errors, unattributed = [], 0
    for chunk, by in merged.subject_objects(AGT.generatedBy):
        producer = str(by).split("/")[0]
        if producer not in roles:
            unattributed += 1
            continue
        plane_cls = next((c for c in merged.objects(chunk, RDF.type) if str(c).endswith("Chunk")), None)
        if plane_cls is None:
            continue
        where = _chunk_location(merged, chunk)
        kb = kb_lib.kb_of(where)
        if can_write(roles[producer], kb, plane_cls):
            continue
        endorsed = any(str(v).split("/")[0] in roles and can_write(roles[str(v).split("/")[0]], kb, plane_cls)
                       for v in merged.objects(chunk, AGT.verifiedBy))
        if not endorsed:
            errors.append(f"[{gate}] {where}: 생성자 {by} 의 역할 {producer} 는 KB {kb} 의 {str(plane_cls).split('/')[-1]} 쓰기 권한이 없다 "
                          f"(agt:writesIn · agt:writes) — 담당 역할의 verified(인수) 또는 되돌림 (AGENTS 표 · 11.2절)")
    if unattributed:
        print(f"info [{gate}] 역할 없는 생성자의 청크 {unattributed}개 — 검사 대상 아님 (2026-09-11 이전 표기 · process:)")
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
            errors.append(f"[verify] {rq.as_posix()}: 질의 자체가 실패 — {e}")
            continue
        for row in rows[:20]:
            vals = " ".join(str(v) for v in row)
            errors.append(f"[verify] {rq.as_posix()}: {vals}  ({title})")
        if len(rows) > 20:
            errors.append(f"[verify] {rq.as_posix()}: … 외 {len(rows)-20}건")
    return errors


def check_residency(shapes: Graph, bzl_path: str, shape_paths: list[str]) -> list[str]:
    """수준 허용표의 단일 정의처 — shape 가 `defs/kb.bzl` 의 `RESIDENCY` 와 같은 표인가 (M1 단일 정의처, 2026-09-26).

    같은 규칙을 두 곳에 적는 것을 막는다. 원본은 Starlark 쪽 리터럴이다 — Starlark 는 파일을 읽지 못하므로
    분석 시점 판정이 쓰는 표가 원본이어야 하고, shape 는 그것의 RDF 표현이다. plane 은 shape 의
    `sh:targetClass` 지역명 `<X>Chunk` 에서 읽는다(metrics 와 같은 규칙). 표에서 모든 수준을 허용하는 plane
    (annotation)은 구간 제약이 없어야 한다 — 주석은 대상에서 수준을 물려받고 그 판정은 verify 질의가 한다.
    첫 실행(2026-09-26, plane 7 · 구간 제약 6): FAIL 0.
    """
    from rdflib.collection import Collection
    from rdflib.namespace import SH

    gate = kb_lib.RESIDENCY_GATE
    where = ", ".join(shape_paths) or bzl_path
    try:
        _planes, levels, table = kb_lib.load_residency(bzl_path)
    except (OSError, ValueError) as e:
        raise ConfigFailure(f"[{gate}] {bzl_path}: 수준 허용표를 읽을 수 없다 — {e}") from e
    declared = {p: set(v) for p, v in table.items() if set(v) != set(levels)}
    found: dict[str, set[str]] = {}
    for shape, cls in shapes.subject_objects(SH.targetClass):
        plane = str(cls).split("/")[-1]
        if not plane.endswith("Chunk"):
            continue
        plane = plane[: -len("Chunk")].lower()
        for prop in shapes.objects(shape, SH.property):
            if (prop, SH.path, kb_lib.AGT.hasLevel) not in shapes:
                continue
            for lst in shapes.objects(prop, SH["in"]):
                found.setdefault(plane, set()).update(str(v).split("/")[-1] for v in Collection(shapes, lst))
    errors = []
    for plane in sorted(set(declared) | set(found)):
        want, have = declared.get(plane), found.get(plane)
        if want is None:
            errors.append(f"[{gate}] {where}: shape 가 plane {plane} 의 수준 구간을 {sorted(have)} 로 제한하는데 {bzl_path} 의 RESIDENCY 에는 그 제한이 없다 — 표의 원본은 {bzl_path} 다")
        elif have is None:
            errors.append(f"[{gate}] {where}: {bzl_path} 의 RESIDENCY 는 plane {plane} 을 {sorted(want)} 로 제한하는데 shape 에 대응 구간이 없다 — `agt:{plane.capitalize()}Chunk` 의 `agt:hasLevel` 에 `sh:in` 을 단다")
        elif want != have:
            errors.append(f"[{gate}] {where}: plane {plane} 의 수준 구간이 갈린다 — {bzl_path} 는 {sorted(want)}, shape 는 {sorted(have)} 다. 원본은 {bzl_path} 이므로 shape 를 맞춘다")
    return errors


def check_shacl(merged: Graph, shapes: Graph, reason: bool, shape_paths: list[str]) -> list[str]:
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
    return [] if conforms else [f"[shacl] {', '.join(shape_paths)}: shape 부적합 — sh:message 가 수정 방향이다\n{text}"]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ontology", nargs="*", default=[], help="T-Box 모듈 파일들 (*-ontology, *-rules)")
    ap.add_argument("--shapes", nargs="*", default=[], help="SHACL shape 파일들 (*-shapes)")
    ap.add_argument("--odd", nargs="*", default=[], help="ODD 파일들 (*-odd)")
    ap.add_argument("--data", nargs="*", default=[], help="A-Box 파일들 (*-kg, *-space)")
    ap.add_argument("--reason", action="store_true", help="SHACL 전에 OWL-RL 추론 적용")
    ap.add_argument("--residency", default="", help="수준 허용표의 원본 defs/kb.bzl — 주면 shape 가 그 표와 같은지 본다")
    ap.add_argument("--verify-queries", default="", help="안티패턴 SPARQL 디렉토리 (2.5절 verify 계층)")
    ap.add_argument("--chunk-files", nargs="*", default=[],
                    help="청크 파일들(*.md) — 주면 element-drop 의 frontmatter 키 전수 대조가 켜진다")
    ap.add_argument("--standard-vocab", nargs="*", default=[],
                    help="등록 표준 어휘 원문(PROV-O·SKOS 등). 주면 그 네임스페이스의 용어가 원문에 정의돼 있는지까지 본다")
    args = ap.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    n_files = len(args.ontology) + len(args.odd) + len(args.data) + len(args.shapes)
    if n_files == 0:
        print("SKIP [validate] 검사 대상 0건 — 그래프 파일이 없다 (PASS 가 아니다)")
        return EXIT_SKIP
    try:
        onto_merged, onto_files = load_files(args.ontology)
        odd_merged, odd_files = load_files(args.odd)
        data_merged, data_files = load_files(args.data)
        shapes_merged, shapes_files = load_files(args.shapes)
        std_terms, std_namespaces = load_standard_vocab(args.standard_vocab)
    except SyntaxFailure as e:  # 파싱되지 않는 입력 — 게이트가 판정을 내릴 수 없다
        print(f"FAIL [syntax] {e}")
        return EXIT_CONFIG
    except Exception as e:  # 표준 어휘 원문 등 부속 입력의 실패
        print(f"FAIL [syntax] {', '.join(args.standard_vocab) or '?'}: 파싱 실패 — {e}")
        return EXIT_CONFIG

    errors += check_labels(onto_files)
    errors += check_boundary(onto_files)
    errors += check_vocab({**odd_files, **data_files}, onto_merged)
    if args.standard_vocab:
        errors += check_standard_vocab({**onto_files, **shapes_files, **odd_files, **data_files}, std_terms, std_namespaces)

    merged = onto_merged + odd_merged + data_merged
    located = {**odd_files, **data_files}  # 개체 → 파일: FAIL 메시지의 <경로> 자리
    if args.odd:
        errors += check_odd_refs(merged, odd_merged, located)
    if data_files:
        errors += check_dangling(merged, onto_merged if args.ontology else None, located)
        errors += check_space(merged, located)
        errors += check_specialization(merged, located)
        errors += check_writer(merged)
        try:
            errors += check_catalog(merged, odd_merged if args.odd else None, located)
        except ConfigFailure as e:  # 상한을 판정할 수 없다 — 배선·ODD 문제
            print(f"FAIL {e}")
            return EXIT_CONFIG
        if args.ontology:
            warnings += check_deprecated_concepts(merged, onto_merged)
    if args.shapes:
        if args.residency:
            try:
                errors += check_residency(shapes_merged, args.residency, args.shapes)
            except ConfigFailure as e:  # 표를 읽을 수 없다 — 배선 문제
                print(f"FAIL {e}")
                return EXIT_CONFIG
        errors += check_shacl(merged, shapes_merged, args.reason, args.shapes)
    errors += check_element_drop(onto_merged if args.ontology else None, args.chunk_files)
    if args.verify_queries:
        errors += check_verify(merged, args.verify_queries)

    for w in warnings:
        print(f"warn {w}")
    if warnings:
        print(f"warn — {len(warnings)}건 (게이트 실패 아님)")

    if errors:
        for e in errors:
            print(f"FAIL {e}")
        print(f"\nFAIL [validate] — {len(errors)}건")
        return EXIT_FAIL

    print(f"PASS [validate] — 파일 {n_files}개, 트리플 {len(merged)}개")
    return 0


if __name__ == "__main__":
    sys.exit(main())
