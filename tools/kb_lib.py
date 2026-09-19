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
PROV = Namespace("http://www.w3.org/ns/prov#")  # 출처·귀속·특수화는 PROV-O 만 쓴다 (STYLEGUIDE §5)

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

# 개체 IRI 접두사 (docs/rules.md §개체 IRI 접두사) — 카탈로그 정합성 검사(validate `catalog`)가 역할 ↔ 스코프 대응을
# id:role-<slug> ↔ id:scope-<slug> 로 푼다. 카탈로그에 역할→스코프 술어는 없고 슬러그가 대응의 원본이다 (STYLEGUIDE §5)
ROLE_ID_PREFIX = "role-"
SCOPE_ID_PREFIX = "scope-"
# ODD 동적 요소 — 역할별 agt:maxConcurrent 합의 상한 (AGENTS.md 역할 절, kb/odd/project-odd.yml concurrent_agents)
CONCURRENT_AGENTS_CONDITION = ID["cond-concurrent-agents"]
CATALOG_GATE = "catalog"  # 게이트 id — FAIL [catalog]
WRITER_GATE = "writer"    # 게이트 id — FAIL [writer]
# 두 KB 의 경로 접두 (pe-storage-layout) — 역할의 agt:writesIn 값이자 청크 assertionLocation 의 KB 판정 기준 (p8-vv-roles, 2026-09-19).
# gen_build 는 rdflib 없이 돌므로 같은 접두를 자체 상수(VV_ROOT)로 갖는다 — chunk2kg 의 PLANE 상수와 같은 사유
KB_DEV = "kb/dev"
KB_VV = "kb/vv"
KB_ROOTS = (KB_DEV, KB_VV)


def kb_of(location: str) -> str:
    """청크 위치(assertionLocation)가 속한 KB — kb/vv/ 아래면 V&V KB, 그 밖(kb/dev·chunks/…)은 개발 KB."""
    return KB_VV if location.startswith(KB_VV + "/") else KB_DEV

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


# ── OpenODD 식의 상한 — odd2kg 가 agt:conditionValue 에 "<INCLUDE_…> <종류>: <식>" 으로 적는다 (tools/odd2kg.py NUM·RANGE) ──
# Range `[a .. b] unit` 의 b, UpperBound `<= n unit` 의 n, `< n unit` 은 n 미만이라 정수면 n-1. LowerBound·Equal(범주)·unknown 은 상한이 없다
_ODD_RANGE = re.compile(r"\[\s*(-?\d+(?:\.\d+)?)\s*\.\.\s*(-?\d+(?:\.\d+)?)\s*\]")
_ODD_UPPER = re.compile(r"(?<![\w<>=])(<=?)\s*(-?\d+(?:\.\d+)?)")


def odd_upper_bound(value: str) -> int | None:
    """agt:conditionValue 문자열의 정수 상한. 식이 상한을 갖지 않거나 정수가 아니면 None — 호출자가 EXIT_CONFIG 로 다룬다."""
    m = _ODD_RANGE.search(value)
    if m:
        hi = m.group(2)
    else:
        m = _ODD_UPPER.search(value)
        if not m:
            return None
        hi = m.group(2)
    if not re.fullmatch(r"-?\d+", hi):
        return None
    n = int(hi)
    return n - 1 if (not _ODD_RANGE.search(value) and m.group(1) == "<") else n


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


# ── 결정의 역할 표지 (STYLEGUIDE §4, 게이트 id `decision-role` — chunk_lint) ────────────────────────────────
# type: decision 인 .md 의 본문 첫 산문 줄은 굵은 역할 표지로 시작한다. 세 파일 결정은 파일 stem 이 표지를 정하고, 단일 파일 옛 결정
# (chunks/decision/d-*.md)은 결론 표지만 요구한다. 표지 안의 한정어("**대안 없음**"·"**대안 — 미확정**"·"**대안(미해결)**")는 같은 역할
# 표지로 본다 — 첫 실행(2026-09-13) 결론 187/187·근거 187/187 은 맨 표지, 대안 21/187 이 한정어 형태였고 그것은 "대안 없음"을 기록하라는
# 규칙(노트 7.4절)의 이행이지 표지 누락이 아니다 (p6-mass-fail-suspects-the-rule). 굵은 span 이 역할 낱말로 시작하지 않으면 위반이다
DECISION_ROLE_GATE = "decision-role"
DECISION_ROLE_MARKERS = {"conclusion": "결론", "rationale": "근거", "alternatives": "대안"}
DECISION_SINGLE_FILE_MARKER = "결론"
DECISION_ROLE_MARKER = re.compile(r"^\s*\*\*(" + "|".join(sorted(set(DECISION_ROLE_MARKERS.values()))) + r")[^*\n]*\*\*")


# ── 산문 문체 (STYLEGUIDE §0 "산문은 단정 서술형", 유저 결정 2026-09-13) ──────────────────────────
# 판정 가능한 것만 게이트 `prose`(chunk_lint·doccheck)다 — 경어·비격식 종결과 산문의 감탄. 판단이 필요한 것(추측·구어)은
# consistency ⑦ 보고다 (p6-mass-fail-suspects-the-rule: 오탐 0 이 게이트의 조건). 코드·따옴표·주석 안은 산문이 아니므로
# prose_segments 가 먼저 뺀다. 표 셀과 불릿은 산문이다 — 경어체는 어디서든 금지다.
PROSE_GATE = "prose"  # 게이트 id — waivers.md 가 이 이름으로 면제를 선언한다 (축 파일)
# 문장 끝의 경어·비격식 종결 — 뒤에 . ! ? ) " 공백 또는 줄끝. 합쇼체 "…ㅂ니다/습니다"(합니다·됩니다·입니다·있습니다)는
# 받침 ㅂ 음절 + "니다" 로 잡는다 — "습" 도 받침 ㅂ 이다. 그냥 "니다" 로 넓히면 평서형 "아니다"(받침 없음)가 오탐이다 (첫 실행 70건 전부)
_HANGUL_B_FINAL = "".join(chr(0xAC00 + i) for i in range(11172) if i % 28 == 17)  # 종성 ㅂ 인 음절 399자
PROSE_FORBIDDEN_ENDINGS = re.compile(r"(?:[" + _HANGUL_B_FINAL + r"]니다|십시오|세요|해요|예요|이에요|죠|네요|군요|어요|아요)(?=[.!?)\"\s]|$)")
# 산문의 느낌표 — `!=`(부등)·`![`(이미지)는 제외. 코드·따옴표·`<!--` 는 prose_segments 가 이미 뺐다
PROSE_EXCLAMATION = re.compile(r"!(?![=\[])")
# 보고용 — 추측 표현과 구어 후보. `되게`·`진짜`는 정상 용법("…되게 한다", "진짜 결함")이 많아 넣지 않는다
PROSE_HEDGES = re.compile(r"것 같|듯하|듯싶|아닐까|않을까|수도 있|아마도|아마 ")
PROSE_COLLOQUIAL = re.compile(r"근데|그냥|좀|엄청|뭔가|약간")
# 문장 끝의 대리(consistency ⑦ 대시 밀도의 분모) — 둘 중 하나: 마침표 뒤에 공백·줄끝·`|`·`)`·닫는 따옴표(굵게 `**` 는 사이에
# 와도 된다; "4.13절" 처럼 숫자·글자가 이어지면 마침표가 아니다), 또는 마침표 없는 종결 "다" 뒤에 `|`(표 셀)·`)`·닫는 따옴표·줄끝.
# 실측(2026-09-13, 살아 있는 청크 621): "다." 만 세면 209건 > 1.0, 종결 "다" 기반으로 넓혀도 130건 — 명사형 종결("기각."·
# "…시점.")과 "…다 (10.3절)." 의 인용 괄호를 놓쳐 대안 양식("**대안** — X 안. 기각 — Y다 (절).")이 전부 걸렸다(대리의
# 결함, p6-mass-fail-suspects-the-rule). 마침표 종결을 세면 28건이고 대안 양식은 빠진다
PROSE_SENTENCE_END = re.compile(r"(?:다(?=\**\s*(?:[|)\"”」'’]|$))|\.(?=\**(?:[|)\"”」'’\s]|$)))")
# 라벨 대시 — 줄·불릿·번호·표 셀 첫머리에서 종결(`다`·`.`) 없는 짧은 라벨(≤40자; 코드 스팬이 지워져 비어 있어도 된다) 바로
# 뒤의 첫 " — " ("**결론** — …", "- **케이스 저장소** — …", "| 결정 | `d-…` — 결론…", "- 답하는 질문 — …"). 절을 이어 붙인
# 대시가 아니라 구조적 구분자라 대시 밀도의 분자에서 뺀다 — 라벨 대시를 세면 표·불릿 중심 청크가 상위를 차지했다(28건 중 상위
# 전부). 절 끝 "…한다 — " 는 `다` 로 끝나므로 라벨이 아니다
PROSE_LABEL_DASH = re.compile(r"(?:^|\|)[ \t]*(?:[-*+][ \t]+|\d+[.)][ \t]+)?(?:[^—|.\n]{0,40}?[^다\s—|.\n])?[ \t]*—[ \t]")

_MD_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
_MD_CODE_SPAN = re.compile(r"(`+)(.+?)\1")
# 따옴표 안 — 같은 줄에서 짝이 맞는 것만 뺀다. 홑따옴표는 영문 소유격·축약(it's)을 피하려고 앞뒤가 영숫자가 아닌 것만 짝으로 본다
_MD_QUOTED = re.compile(r"\"[^\"]*\"|“[^”]*”|「[^」]*」|(?<![A-Za-z0-9])'[^']*'(?![A-Za-z0-9])|(?<![A-Za-z0-9])‘[^’]*’(?![A-Za-z0-9])")


def prose_segments(text: str) -> list[tuple[int, str]]:
    """(줄 번호, 산문 조각) — frontmatter·코드 펜스·코드 스팬·HTML 주석·따옴표 안을 뺀 나머지.

    표 셀·불릿·제목은 산문으로 남긴다. 뺀 자리는 공백 하나로 메워 앞뒤 낱말이 붙지 않게 한다. 빈 조각은 내지 않는다.
    """
    lines = text.splitlines()
    start = 0
    if lines and lines[0].strip() == "---":
        try:
            start = lines[1:].index("---") + 2
        except ValueError:
            start = 0
    out: list[tuple[int, str]] = []
    fence: str | None = None
    in_comment = False
    for i, line in enumerate(lines[start:], start=start + 1):
        if in_comment:
            if "-->" not in line:
                continue
            in_comment = False
            line = line.split("-->", 1)[1]
        m = _MD_FENCE.match(line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            continue
        if m:
            fence = m.group(1)
            continue
        while "<!--" in line:
            head, _, tail = line.partition("<!--")
            if "-->" in tail:
                line = head + " " + tail.split("-->", 1)[1]
            else:
                in_comment = True
                line = head
        line = _MD_CODE_SPAN.sub(" ", line)
        line = _MD_QUOTED.sub(" ", line)
        if line.strip():
            out.append((i, line))
    return out


def _around(seg: str, start: int, end: int, width: int = 24) -> str:
    return seg[max(0, start - width):end + width].strip()


def check_prose(path: str | Path, text: str, waivers: list[dict] | None = None):
    """산문 문체 검사 → (errors, hedges, colloquial). 각 원소는 (줄 번호, 내용).

    errors 는 게이트(경어·비격식 종결, 산문의 느낌표) — waivers.md 에 게이트 id `prose`(축 파일)로 면제된 파일이면 비운다.
    hedges(추측 표현)·colloquial(구어 후보)은 보고용이고 면제와 무관하다 — 판정은 사람 몫이다.
    """
    errors: list[tuple[int, str]] = []
    hedges: list[tuple[int, str]] = []
    colloquial: list[tuple[int, str]] = []
    for ln, seg in prose_segments(text):
        for m in PROSE_FORBIDDEN_ENDINGS.finditer(seg):
            errors.append((ln, f'경어·비격식 종결 "…{m.group(0)}" — 평서형 "…다"로 쓴다 (STYLEGUIDE §0): {_around(seg, m.start(), m.end())}'))
        for m in PROSE_EXCLAMATION.finditer(seg):
            errors.append((ln, f"산문의 느낌표 — 감탄을 쓰지 않는다 (STYLEGUIDE §0): {_around(seg, m.start(), m.end())}"))
        for m in PROSE_HEDGES.finditer(seg):
            hedges.append((ln, m.group(0).strip()))
        for m in PROSE_COLLOQUIAL.finditer(seg):
            colloquial.append((ln, m.group(0)))
    if errors and waivers and waived(waivers, PROSE_GATE, str(path), "파일"):
        errors = []
    return errors, hedges, colloquial


# ── 그래프 union 과 라벨 인터페이스 (query · cq 뷰) ────────────────────────────────────────────────
# 활용 도구가 읽는 그래프 — metrics 와 같은 입력(head·참조·시드·카탈로그·복합체·ODD)에 온톨로지 모듈을 더한 union.
# 경로는 워크스페이스 상대이고 `bazel run` 의 runfiles 에는 data 로 같은 경로에 놓인다. 온톨로지는 모듈 디렉토리 재귀 glob.
UNION_GRAPH_PATHS = ("kg/chunks-kg.ttl", "kg/references-kg.ttl", "kg/base-kg.ttl", "kg/catalog-kg.ttl", "kg/composite-kg.ttl",
                     "kb/odd/project-odd.ttl")
UNION_GRAPH_GLOBS = ("kb/ontology/**/*-ontology.ttl",)
# IRI 축약 — 표 출력용. rdflib 의 qname 은 로컬부에 `/` 가 있는 청크 IRI(id:chunk/<uuid>)를 만들지 못한다
COMPACT_PREFIXES = ((str(AGT), "agt:"), (str(ID), "id:"), ("http://www.w3.org/ns/prov#", "prov:"),
                    (str(RDFS), "rdfs:"), (str(OWL), "owl:"), (str(RDF), "rdf:"),
                    ("http://www.w3.org/2004/02/skos/core#", "skos:"), ("http://www.w3.org/2001/XMLSchema#", "xsd:"))


def resolve_path(path: str, root: Path) -> Path | None:
    """워크스페이스 상대 경로를 runfiles(현재 디렉토리) → bazel-bin → 소스 순으로 찾는다. 없으면 None (호출자가 EXIT_CONFIG)."""
    for cand in (Path(path), root / "bazel-bin" / path, root / path):
        if cand.is_file():
            return cand
    return None


def resolve_glob(pattern: str, root: Path) -> list[Path]:
    """재귀 glob 을 같은 순서로 찾는다 — 첫 번째로 파일이 나오는 뿌리의 결과만.

    bazel-bin 아래의 `*.runfiles/` 사본은 뺀다 — 테스트마다 같은 원본이 복제돼 한 파일이 여러 번 적재되고, 빈 노드(owl:Restriction)를
    가진 파일은 적재마다 다른 노드가 되어 질의 행이 중복된다 (CQ-36 첫 실행 2026-09-18: 7행이 13행으로). IRI 트리플만 있는 파일은
    중복 적재가 결과를 바꾸지 않아 드러나지 않았다.
    """
    import glob as _glob
    for base in (Path("."), root / "bazel-bin", root):
        found = sorted(Path(p) for p in _glob.glob(str(base / pattern), recursive=True)
                       if not any(part.endswith(".runfiles") for part in Path(p).parts))
        if found:
            return found
    return []


def load_union(ttls: list[str], root: Path) -> Graph:
    """TTL 들을 하나의 Graph 로 (query.py·metrics.py 와 같은 방식). 빈 목록이면 UNION_GRAPH_PATHS + 온톨로지 glob.

    없는 파일은 ValueError — 호출자가 EXIT_CONFIG 로 다룬다. .ttl 이 아닌 입력(청크 .md 등)은 건너뛴다.
    """
    files: list[Path] = []
    if ttls:
        for t in ttls:
            f = resolve_path(t, root)
            if f is None:
                raise ValueError(f"{t}: 그래프 파일이 없다 — bazel build //kg:chunks_kg //kg:references_kg //kb/odd:odd")
            files.append(f)
    else:
        for p in UNION_GRAPH_PATHS:
            f = resolve_path(p, root)
            if f is None:
                raise ValueError(f"{p}: 그래프 파일이 없다 — bazel build //kg:chunks_kg //kg:references_kg //kb/odd:odd")
            files.append(f)
        for pat in UNION_GRAPH_GLOBS:
            found = resolve_glob(pat, root)
            if not found:
                raise ValueError(f"{pat}: 온톨로지 모듈이 없다")
            files += found
    g = Graph()
    for f in files:
        if f.suffix == ".ttl":
            g.parse(str(f), format="turtle")
    return g


def compact_iri(iri: str) -> str:
    for ns, prefix in COMPACT_PREFIXES:
        if iri.startswith(ns):
            return prefix + iri[len(ns):]
    return iri


def chunk_body(text: str) -> str:
    """청크 파일의 본문 — frontmatter 를 뺀 나머지, 앞뒤 빈 줄 제거. frontmatter 가 없으면 전문이 본문이다."""
    lines = text.splitlines()
    start = 0
    if lines and lines[0].strip() == "---":
        try:
            start = lines[1:].index("---") + 2
        except ValueError:
            start = 0
    return "\n".join(lines[start:]).strip("\n")


# ── 문서 뷰 (weave — p12-documents-are-generated: 문서는 저장하지 않고 생성하며 생성 시각과 질의를 적는다) ─────────────────
WEAVE_KINDS = ("adr", "requirements", "changelog", "audit")
WEAVE_GATE = "weave"  # 입력 문제의 태그 — CONFIG [weave]
DECISION_PART_FILES = {"conclusion": "conclusion.md", "rationale": "rationale.md", "alternatives": "alternatives.md"}  # 결정 복합체의 세 부분 (STYLEGUIDE §4)


# ── 실행 기록과 관측 (r-026 append-only · p0-run-as-observation · p8-vv-plane-instances memory = 실행 기록) ──────────────
# 관측은 도구가 쓴다 — 생성자는 역할이 아닌 `process:<도구>` 라 writer 검사 밖이다 (validate check_writer). 카탈로그의 executor
# 하위 역할을 도구가 맡는 첫 형태다. V&V 실행 기록은 V&V KB 의 memory plane 디렉토리(kb/vv/run — gen_build VV_PKGS), 가정 판정
# 관측은 개발 KB 의 memory 디렉토리(kb/dev/memory — assume_check)에 놓인다. weave audit 이 두 곳의 최신 관측을 그대로 요약한다
VV_RUN_DIR = KB_VV + "/run"
DEV_MEMORY_DIR = KB_DEV + "/memory"
RUN_GENERATOR = "process:vv_run"                # V&V 실행 기록의 generated.by (tools/vv_run.py --record)
ASSUME_CHECK_GENERATOR = "process:assume_check"  # 가정 판정 관측의 generated.by (tools/assume_check.py GENERATOR · metrics · weave audit 의 정의처)
RUN_CASE_TABLE_HEADER = "| 케이스 | 실행 명령 | 결과 | 소요 |"  # 실행 기록 본문의 케이스 표 — audit 이 이 헤더로 표를 찾는다
ASSUME_CHECK_TABLE_HEADER = "| 가정 | 판정 유형 | 등급 | 상태 | 직접 영향 | suspect 후보(전이) |"  # 가정 판정 관측의 가정 표 (assume_check.observation)
RUN_VERDICTS = ("pass", "fail", "skip")          # 케이스 판정 — SKIP 은 PASS 가 아니다 (docs/tools.md 실패 종류 3)


# ── 추적 매트릭스 (TIM — plane×plane 의 허용 칸; 노트 14.1 정정본 3단계 "매트릭스", metrics 3단계 대리 · weave audit 이 같은 정의) ──
# (링크 종류, 출발 plane, 도착 plane). 앞 8칸은 개발 KB 안의 정제·대체·만족 링크, 뒤 7칸은 V&V 사슬(p8-scenario-ladder-rungs ·
# p8-pass-criteria): 목표 derivesFrom 요구 · 기준 refines 목표 · 케이스 refines 기준 · 검증기 refines 케이스, 같은 높이의 verifies —
# logical 기준 → 결정, concrete 케이스 → 결정, executable 검증기 → 산출물
TIM_CELLS = (("refines", "decision", "requirement"), ("serves", "decision", "requirement"), ("supersedes", "decision", "decision"),
             ("satisfies", "contract", "decision"), ("derivesFrom", "schema", "decision"), ("constrains", "schema", "contract"),
             ("satisfies", "artifact", "decision"), ("verifies", "requirement", "requirement"),
             ("derivesFrom", "requirement", "requirement"), ("refines", "contract", "requirement"), ("refines", "schema", "contract"),
             ("refines", "artifact", "schema"), ("verifies", "contract", "decision"), ("verifies", "schema", "decision"),
             ("verifies", "artifact", "artifact"))
# 링크의 구축·복원 구분 (유저 결정 2026-09-12 (b), p10-restored-link-marking) — 기준은 술어가 아니라 **증거 종류**다.
# 구축 = 증거가 구축 기록(constructionRecord)뿐인 확정 agt:Link. 본문 식별자 추출(extract_refs)은 직접 트리플(LINK_EXTRACTED)과
# 후보 링크 개체(agt:CandidateLink — cites 만, 증거는 구축 기록)로 나가며 구축·복원 어느 쪽에도 세지 않고 후보로 따로 센다.
# 복원 = 구축 기록이 아닌 증거(proposal — 후보의 출처)를 하나라도 가진 확정 agt:Link. frontmatter `restored:` 표시의 링크에 chunk2kg 가
# 확정 기록(constructionRecord — 사람이 frontmatter 에 적은 편집 시점 기록)과 proposal 을 함께 낸다: 9.11절 규칙 "구축(+) 또는
# 실행(+) 없이 확정 불가"를 verify 질의 confirmed-without-evidence 가 강제하므로 proposal 만으로는 확정 링크가 성립하지 않는다.
# `link` 후보 파이프라인(tools/link.py, //kg:link_candidates)이 후보를 내고 사람이 restored: 로 확정한다
LINK_EXTRACTED = (AGT.cites, AGT.usesConcept)
CONSTRUCTION_EVIDENCE = AGT.constructionRecord
LINK_GATE = "link"          # 후보 생성기 뷰의 태그 — CONFIG [link] (입력 문제만, 판정 실패는 없다)
RESTORED_GATE = "restored"  # 게이트 id — FAIL [restored]: restored: 의 IRI 가 같은 청크의 링크 키 대상에 없다 (chunk2kg)
# 링크 상태 (link-state-ontology agt:linkState) — 후보·확정의 값. 본문 추출 참조(extract_refs 의 agt:cites)는 후보 링크 개체
# (agt:CandidateLink, "candidate")로 나가고 frontmatter 링크는 확정(agt:ConfirmedLink, "confirmed")이다 (p10-extracted-references-are-
# candidates, 유저 승인 2026-09-19). 상태는 증거 종류가 아니라 "누가 링크 키에 적었는가"로 갈린다 — 둘 다 증거는 구축 기록이다.
# chunk2kg·extract_refs 는 rdflib 없이 돌므로 같은 문자열을 getattr 폴백으로 갖는다
LINK_STATE_CANDIDATE = "candidate"
LINK_STATE_CONFIRMED = "confirmed"
# 청크 uuid 는 work-id 다 (p10-split-keeps-work-identity, 유저 승인 2026-09-19). 분할 조각은 frontmatter `specializationOf: <원 IRI>`
# 로 원본을 가리키고 chunk2kg 가 prov:specializationOf 를 방출한다. 링크 IRI 는 양 끝의 뿌리 uuid(사슬을 따라 올라간 work-id)로
# 계산한다. 대상은 살아 있는 같은 plane 의 청크여야 하고 사슬은 순환하지 않는다 — validate check_specialization 이 FAIL [specialization],
# 대상 부재는 check_dangling 이 FAIL [dangling] 으로 거부한다. 순환은 chunk2kg 도 (뿌리를 계산할 수 없으므로) 같은 게이트 id 로 거부한다
SPECIALIZATION_GATE = "specialization"


def link_origins(g: Graph) -> dict:
    """링크 개체(agt:Link)의 후보·구축·복원 구분 — metrics 3단계 대리와 weave audit 링크 근거 절이 이 하나의 정의를 쓴다.

    후보 링크 = linkState 가 candidate 인 agt:Link (본문 추출 참조 — extract_refs). 종류별 수를 candidate_kinds 로 낸다.
    확정 링크(나머지) 중 복원 링크 = 구축 기록이 아닌 증거 종류를 하나라도 가진 것 (restored: 표시 → proposal 이 확정 기록과 함께 붙는다),
    구축 링크 = 그 밖(구축 기록 증거뿐 또는 증거 없음). 복원 비율 = 복원 / (확정 구축 + 복원), 분모 0 이면 None —
    후보는 분모에 들어가지 않는다 (p10-extracted-references-are-candidates). extracted 는 본문 식별자 추출의 직접 트리플 수(참고).
    반환 키: links · confirmed · candidates · candidate_kinds{축약 술어: 수} · built · restored · restored_links · no_evidence ·
             extracted{축약 술어: 수} · ratio
    """
    links = sorted(g.subjects(RDF.type, AGT.Link), key=str)
    candidates = [l for l in links if any(str(s) == LINK_STATE_CANDIDATE for s in g.objects(l, AGT.linkState))]
    confirmed = [l for l in links if l not in set(candidates)]
    restored, no_ev = [], 0
    for link in confirmed:
        kinds = [k for e in g.objects(link, AGT.hasEvidence) for k in g.objects(e, AGT.evidenceKind)]
        if not kinds:
            no_ev += 1
        elif any(k != CONSTRUCTION_EVIDENCE for k in kinds):
            restored.append(link)
    candidate_kinds: dict = {}
    for l in candidates:
        k = compact_iri(str(next(g.objects(l, AGT.linkKind), "")))
        candidate_kinds[k] = candidate_kinds.get(k, 0) + 1
    extracted = {compact_iri(str(p)): sum(1 for _ in g.subject_objects(p)) for p in LINK_EXTRACTED}
    built = len(confirmed) - len(restored)
    total = built + len(restored)
    return {"links": len(links), "confirmed": len(confirmed), "candidates": len(candidates), "candidate_kinds": candidate_kinds,
            "built": built, "restored": len(restored), "restored_links": restored, "no_evidence": no_ev,
            "extracted": extracted, "ratio": (len(restored) / total) if total else None}


def chunk_planes(g: Graph) -> dict:
    """청크 → plane 이름 — rdf:type 중 `…Chunk` 로 끝나는 첫 클래스 (metrics·weave 가 같은 규칙으로 plane 을 읽는다)."""
    out = {}
    for c in g.subjects(AGT.lineCount, None):
        for t in g.objects(c, RDF.type):
            name = str(t).split("/")[-1]
            if name.endswith("Chunk"):
                out[c] = name[: -len("Chunk")].lower()
                break
    return out


def link_cells(g: Graph) -> set:
    """링크 개체(agt:Link)가 채운 (종류, 출발 plane, 도착 plane) 칸의 집합.

    복합체 IRI 는 plane 이 없으므로 복합체의 부분(agt:hasDirectPart) 하나의 plane 으로 보정한다 — 결정 복합체의 부분은 전부 decision 이다.
    """
    plane = chunk_planes(g)
    part_of_comp = {}
    for comp, part in g.subject_objects(AGT.hasDirectPart):
        part_of_comp.setdefault(comp, part)

    def plane_of(node):
        return plane.get(node) or plane.get(part_of_comp.get(node))

    cells = set()
    for link in g.subjects(RDF.type, AGT.Link):
        f, t = next(g.objects(link, AGT.linkFrom), None), next(g.objects(link, AGT.linkTo), None)
        kind = str(next(g.objects(link, AGT.linkKind), "")).split("/")[-1]
        pf, pt = plane_of(f), plane_of(t)
        if kind and pf and pt:
            cells.add((kind, pf, pt))
    return cells


# ── 생성 skill (gen_skills — agrtls K "skill 은 손으로 쓰지 않고 지식·절차에서 생성한다", 로드맵 6단계) ──────────────────
# 어떤 도구를 skill 로 내는가와 그 절차의 원본 절은 이 표가 단일 정의처다. 본문(무엇·언제·사용법)은 도구 모듈의 docstring 이
# 원본이고, 생성기(tools/gen_skills.py)가 둘을 합쳐 .claude/skills/<도구-kebab>/SKILL.md 를 트리에 쓴다. 생성물은 BUILD 와
# 같은 이유로 커밋 대상이며(도구 없이도 skill 이 읽혀야 한다) //:skills_drift_test 가 재생성과 비교한다.
#   tool      tools/<tool>.py 이며 tools/BUILD.bazel 에 같은 이름의 py_binary 가 있어야 한다
#   section   원본 절 — docs/ 아래 문서 `<파일>#<GitHub 앵커>`. 생성기가 앵커 실재를 검사한다
#   when      언제 쓰는가 한 문장(단정 서술형) — skill frontmatter 의 description
#   commands  대표 명령 1~3
SKILLS_DIR = ".claude/skills"
SKILLS_DRIFT_GATE = "skills-drift"  # 게이트 id — FAIL [skills-drift]
GEN_SKILLS_GATE = "gen-skills"      # 생성 시점 거부 — FAIL [gen-skills]
SKILLS = (
    {"tool": "workset", "section": "method.md#8-조회",
     "when": "dispatch 전에 역할·수준 창·앵커로 거른 작업 집합(라벨 목록과 이웃 본문)을 컨텍스트 예산 안에서 뽑을 때 쓴다.",
     "commands": ["bazel build //kg:workset --//kb:role=developer --//kb:anchor='<라벨|IRI>' --//kb:levels=concrete",
                  "cat bazel-bin/kg/workset-developer.md"]},
    {"tool": "query", "section": "method.md#8-조회",
     "when": "역량 질문(CQ)의 답을 그래프에서 라벨 목록으로 얻거나 한 항목이 무엇을 가리키는지 SPARQL 로 확인할 때 쓴다.",
     "commands": ["bazel run //tools:query", "bazel run //tools:query -- CQ-07 --labels",
                  "bazel run //tools:query -- CQ-19 --labels --bind '?x=<IRI|id:슬러그|라벨>'"]},
    {"tool": "impact", "section": "method.md#12-영향-분석",
     "when": "청크·결정을 고치기 전에 영향 항목 수·plane 분포·suspect 가 될 링크 수·승인이 필요한 결정 수를 계산할 때 쓴다.",
     "commands": ["bazel run //tools:impact -- //kb/dev/requirement:<타깃>", "bazel run //tools:impact -- //kb/dev/decision:<결정> --universe //kb/..."]},
    {"tool": "assume_check", "section": "method.md#7-갱신",
     "when": "가정을 ODD 조건으로 판정해 깨진 가정의 직접 영향 집합과 suspect 후보를 내거나 --break 로 인위 파괴 실험을 할 때 쓴다.",
     "commands": ["bazel run //tools:assume_check", "bazel run //tools:assume_check -- --break cond-build-system",
                  "bazel run //tools:assume_check -- --record && python3 tools/gen_build.py --root ."]},
    {"tool": "revalidate", "section": "method.md#7-갱신",
     "when": "청크 본문을 고친 뒤 base 리비전 대비 재판정 대상(링크 상대·복합체 형제·하류 의존자)을 표로 낼 때 쓴다.",
     "commands": ["bazel run //tools:revalidate -- --base HEAD", "bazel run //tools:revalidate -- --base <rev> --out /tmp/revalidate.md"]},
    {"tool": "odd_check", "section": "method.md#2-odd-작성",
     "when": "세션 시작이나 환경 변경 뒤에 실제 조건이 ODD 안인지 CHECKS 명령으로 판정해 이탈을 보고할 때 쓴다.",
     "commands": ["bazel run //tools:odd_check", "bazel run //tools:odd_check -- --out /tmp/odd-check.md"]},
    {"tool": "endorse", "section": "method.md#13-저작-흐름과-완료",
     "when": "쓰기 권한 역할이 검토를 마친 청크에 verified 를 붙여 writer 검사를 해소할 때 쓴다.",
     "commands": ["bazel run //tools:endorse -- --by orchestrator/<모델> --at <ISO 8601> <청크 파일…>"]},
    {"tool": "term_propose", "section": "method.md#10-일반화",
     "when": "관측에서 뽑은 개념 후보를 검사를 거쳐 온톨로지 승인 큐(kb/ontology/proposals/)에 제안할 때 쓴다.",
     "commands": ["bazel run //tools:term_propose -- --id <slug> --kind class --parent agt:<상위> --label-ko '<한글>' --label-en '<english>' --definition '<속+종차>' --cq CQ-NN"]},
    {"tool": "consistency", "section": "method.md#9-뷰",
     "when": "커밋 전에 중복·라벨 형식·용어 옛 표기·단정성(추측·구어·대시 밀도) 후보를 보고로 확인할 때 쓴다.",
     "commands": ["bazel build //kb:consistency && cat bazel-bin/kb/consistency.md"]},
    {"tool": "metrics", "section": "method.md#완료-판정",
     "when": "고아율·CQ19·CQ20 커버리지·도입 단계 통과 조건 같은 수치를 문서에 적지 않고 생성물에서 인용할 때 쓴다.",
     "commands": ["bazel build //kg:metrics && cat bazel-bin/kg/metrics.md"]},
    {"tool": "gen_build", "section": "method.md#6-연결",
     "when": "청크를 추가·삭제하거나 frontmatter 링크(refines·serves·supersedes·verifies)를 고친 뒤 BUILD 를 재생성하고 드리프트를 검사할 때 쓴다.",
     "commands": ["python3 tools/gen_build.py --root .", "python3 tools/gen_build.py --check --root .", "bazel test //:build_drift_test"]},
    {"tool": "link", "section": "method.md#6-연결",
     "when": "frontmatter 링크가 없는 청크 쌍의 복원 후보를 체계 안 증거(본문 인용·테스트 공동 커버·개념 공유)로 뽑아 사람이 restored 표시로 확정할 때 쓴다.",
     "commands": ["bazel build //kg:link_candidates && cat bazel-bin/kg/link-candidates.md",
                  "python3 tools/gen_build.py --root . && bazel test //...   # 앵커 청크에 링크 키와 restored: 를 적은 뒤"]},
    {"tool": "vv_run", "section": "method.md#11-검증--vv-층으로",
     "when": "V&V 케이스의 양성 명령을 실행해 케이스별 pass·fail·skip 을 판정하고 실행 기록(kb/vv/run/, append-only)을 남길 때 쓴다.",
     "commands": ["bazel run //tools:vv_run -- --record", "bazel run //tools:vv_run -- --case <슬러그>",
                  "python3 tools/gen_build.py --root . && bazel test //..."]},
    {"tool": "weave", "section": "method.md#9-뷰",
     "when": "결정 기록·요구 색인·변경 이력·감사 보고서를 저장하지 않고 그래프와 관측에서 생성해 인용할 때 쓴다.",
     "commands": ["bazel build //kg:audit && cat bazel-bin/kg/audit.md", "bazel build //kb/dev:adr //kb/dev:requirements //kb/dev:changelog"]},
    {"tool": "doccheck", "section": "tools.md#게이트-총람--이-문서가-원본이다",
     "when": "문서를 고친 뒤 죽은 링크·앵커·백틱 경로·산문 문체를 게이트와 같은 방식으로 검사할 때 쓴다.",
     "commands": ["bazel run //tools:doccheck -- *.md docs/*.md docs/open-questions/*.md --target-only docs/agent-knowledge-system-notes.md",
                  "bazel test //:doccheck_test"]},
)


def label_of(g: Graph, node, lang: str = "ko") -> str:
    """개체의 rdfs:label — 요청 언어 → 다른 언어 → 축약 IRI 순. 라벨이 인터페이스다 (p4-label-is-the-interface)."""
    labels = list(g.objects(node, RDFS.label))
    for lab in labels:
        if getattr(lab, "language", None) == lang:
            return str(lab)
    return str(labels[0]) if labels else compact_iri(str(node))
