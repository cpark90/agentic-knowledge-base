"""공용 그래프 적재·어휘 헬퍼.

접미사 규약(노트 0.2절)과 네임스페이스(0.3절, 0.7절)의 단일 정의처.
"""

from __future__ import annotations

import re
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef

# 이 체계 고유 어휘 (노트 0.3절, 0.7절)
AGT = Namespace("https://agentic-knowledge-base.dev/agt/")
ID = Namespace("https://agentic-knowledge-base.dev/id/")

# 외부 표준 어휘 — 정의를 변경하지 않고 그대로 쓴다 (0.3절)
WELL_KNOWN_PREFIXES = (
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#",   # rdf
    "http://www.w3.org/2000/01/rdf-schema#",          # rdfs
    "http://www.w3.org/2002/07/owl#",                 # owl
    "http://www.w3.org/2001/XMLSchema#",              # xsd
    "http://www.w3.org/2004/02/skos/core#",           # skos
    "http://www.w3.org/ns/shacl#",                    # sh
    "http://www.w3.org/ns/prov#",                     # prov
    "http://purl.org/dc/terms/",                      # dcterms
    "http://purl.org/co/",                            # co (Collections Ontology)
    "http://purl.obolibrary.org/obo/",                # bfo / iao / ro
)

# 산출물 접미사 (0.2절 + SHACL shape 파일용 -shapes 확장)
ALLOWED_TTL_SUFFIXES = (
    "-ontology",
    "-rules",
    "-shapes",
    "-space",
    "-kg",
    "-odd",
)

# 온톨로지 모듈이 "정의"로 간주되는 타입 (2.3절 경계 규칙, 2.5절 정의 완전성)
DEFINING_TYPES = (
    OWL.Class,
    OWL.ObjectProperty,
    OWL.DatatypeProperty,
    OWL.AnnotationProperty,
    OWL.NamedIndividual,
    RDFS.Class,
    RDF.Property,
)


def load_graph(path: str | Path) -> Graph:
    """TTL 파일 하나를 파싱한다. 파싱 실패는 그 자체가 게이트 실패다."""
    g = Graph()
    g.parse(str(path), format="turtle")
    return g


def load_merged(paths: list[str]) -> tuple[Graph, dict[str, Graph]]:
    """파일별 그래프와 병합 그래프를 함께 돌려준다.

    모듈 경계 검사(2.3절)는 파일별 그래프가, SHACL·추론은 병합 그래프가 필요하다.
    """
    per_file: dict[str, Graph] = {}
    merged = Graph()
    for p in paths:
        g = load_graph(p)
        per_file[p] = g
        merged += g
    return merged, per_file


def defined_terms(g: Graph):
    """그래프가 정의하는 agt: 용어(클래스·속성·개체)의 집합."""
    terms = set()
    for t in DEFINING_TYPES:
        for s in g.subjects(RDF.type, t):
            if isinstance(s, URIRef) and str(s).startswith(str(AGT)):
                terms.add(s)
    return terms


def is_well_known(iri: str) -> bool:
    return any(iri.startswith(p) for p in WELL_KNOWN_PREFIXES)


# ── 종료 코드 — 실패 종류를 구분한다 (agrtls-practices-review-2026-09-12 A) ──────────────────
# 판정 실패 / 설정·입력 문제 / 미실행을 하나의 1 로 뭉개지 않는다. **SKIP 은 PASS 가 아니다** —
# 입력이 0건이라 검사가 돌지 않은 것은 통과가 아니라 미실행이다. 모든 게이트·뷰 도구가 같은 상수를 쓴다.
EXIT_OK = 0
EXIT_FAIL = 1      # 판정 실패 — 산출물을 고친다
EXIT_CONFIG = 2    # 설정·입력 문제 — 파일 없음·인자 오류·파싱 불가. 배선을 고친다
EXIT_SKIP = 3      # 검사가 실행되지 않음 — 입력 0건 등. 통과로 세지 않는다


# ── 면제 선언 (docs/waivers.md, agrtls-practices-review-2026-09-12 C) ──────────────────────
# "오탐은 침묵이 아니라 선언으로": 코드 속 면제 대신 표 하나. 도구는 면제 대상을 집계에서 빼되 목록에 남긴다.
WAIVER_COLUMNS = ("게이트 id", "대상", "축", "사유", "판정자", "날짜")
WAIVER_AXES = ("파일", "stem", "상태")


def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def load_waivers(path: str | Path) -> list[dict]:
    """docs/waivers.md 의 표를 읽는다 → [{gate, targets, axis, reason, judge, date, line}].

    헤더가 WAIVER_COLUMNS 와 다르거나 축이 WAIVER_AXES 밖이면 ValueError, 파일이 없으면 FileNotFoundError —
    둘 다 설정 문제(EXIT_CONFIG)이지 판정 실패가 아니다. `대상` 은 ` · ` 로 구분된 여러 값.
    """
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"{path}: waiver 표가 없다")
    header_seen, out = False, []
    for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.lstrip().startswith("|"):
            continue
        cells = _cells(line)
        if not header_seen:
            if tuple(cells) != WAIVER_COLUMNS:
                raise ValueError(f"{path}:{n}: waiver 표의 열은 | {' | '.join(WAIVER_COLUMNS)} | 여야 한다 — 실제 {cells}")
            header_seen = True
            continue
        if all(re.fullmatch(r":?-+:?", c) for c in cells) or tuple(cells) == WAIVER_COLUMNS:
            continue
        if len(cells) != len(WAIVER_COLUMNS):
            raise ValueError(f"{path}:{n}: 열이 {len(cells)}개다 (필요 {len(WAIVER_COLUMNS)})")
        gate, targets, axis, reason, judge, date = (c.strip("`") for c in cells)
        if axis not in WAIVER_AXES:
            raise ValueError(f"{path}:{n}: 축 {axis!r} 는 {'|'.join(WAIVER_AXES)} 중 하나여야 한다")
        out.append({"gate": gate, "axis": axis, "reason": reason, "judge": judge, "date": date, "line": n,
                    "targets": [t.strip().strip("`") for t in re.split(r"\s*·\s*", targets) if t.strip()]})
    if not header_seen:
        raise ValueError(f"{path}: waiver 표가 없다")
    return out


def _target_matches(declared: str, target: str, axis: str) -> bool:
    if axis == "파일":
        t = Path(target).as_posix()
        return t == declared or t.endswith("/" + declared)  # 루트 상대 경로 또는 그 접미(절대 경로로 불렸을 때)
    return declared == target


def waived(waivers: list[dict], gate_id: str, target: str, axis: str) -> bool:
    """게이트 `gate_id` 에서 `target` 이 `axis` 축으로 면제 선언됐는가."""
    return any(w["gate"] == gate_id and w["axis"] == axis and any(_target_matches(d, target, axis) for d in w["targets"])
               for w in waivers)
