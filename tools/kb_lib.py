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

# 개체 IRI 접두사 (docs/rules.md §개체 IRI 접두사) — 카탈로그 정합성 검사(validate `catalog`)가 역할 ↔ 스코프 대응을
# id:role-<slug> ↔ id:scope-<slug> 로 푼다. 카탈로그에 역할→스코프 술어는 없고 슬러그가 대응의 원본이다 (STYLEGUIDE §5)
ROLE_ID_PREFIX = "role-"
SCOPE_ID_PREFIX = "scope-"
# ODD 동적 요소 — 역할별 agt:maxConcurrent 합의 상한 (AGENTS.md 역할 절, kb/odd/project-odd.yml concurrent_agents)
CONCURRENT_AGENTS_CONDITION = ID["cond-concurrent-agents"]
CATALOG_GATE = "catalog"  # 게이트 id — FAIL [catalog]

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
