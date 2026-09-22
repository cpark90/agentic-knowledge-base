"""공용 그래프 적재·어휘 헬퍼.

접미사 규약(노트 0.2절)과 네임스페이스(0.3절, 0.7절)의 단일 정의처.
"""

from __future__ import annotations

import hashlib
import os
import re
import unicodedata
from datetime import datetime, timezone
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


# ── 논평의 형식 (STYLEGUIDE §4 annotation, 결정 p7-commentary-form — 게이트 id `blocking-comment`: chunk_lint) ────────────
# annotation 청크는 논평이다. 첫 줄이 `<라벨> (<장식>): <요지>` 이고 이어서 줄 머리 슬롯 넷(대상·본문·제안·해소)이 온다.
# 라벨 일곱과 장식 셋의 표기 원천은 Conventional Comments 이고 해소 셋은 결정이 정했다 — 셋 다 닫힌 어휘다.
# **게이트 효과는 하나뿐이다.** `issue (blocking)` 이면서 `해소: 열림` 인 논평이 있으면 게이트가 막는다. 그 밖의 조합은
# 기록이고 막지 않는다. 형식(첫 줄 꼴·닫힌 어휘·본문 문장 상한)은 shape(review-comment-body-shapes.ttl)가 보고,
# 이 한 조건만 chunk_lint 가 본다 — 판정 도구는 해소 상태의 존재만 보고 이유의 내용을 보지 않는다 (p5-verification-tools-per-plane).
# 값 어휘의 정의처는 여기다. chunk2kg 는 rdflib 없이 타깃마다 돌므로 같은 문자열을 getattr 폴백으로 갖는다 (LINK_STATE_* 와 같은 형태)
BLOCKING_COMMENT_GATE = "blocking-comment"  # 게이트 id — FAIL [blocking-comment]. docs/waivers.md 가 이 이름으로 면제를 선언한다 (축 파일)
COMMENT_LABELS = ("praise", "nitpick", "suggestion", "issue", "question", "thought", "chore")
COMMENT_DECORATIONS = ("blocking", "non-blocking", "if-minor")
COMMENT_RESOLUTIONS = ("열림", "해소", "기각")
COMMENT_SLOTS = ("대상", "본문", "제안", "해소")  # 줄 머리 `키워드: 값` 슬롯 — chunk2kg.BODY_SLOT_KEYWORDS 가 표지로 읽는다
COMMENT_OPEN = COMMENT_RESOLUTIONS[0]            # 아직 해소되지 않은 상태
COMMENT_BLOCKING = (COMMENT_LABELS[3], COMMENT_DECORATIONS[0])  # 막는 (라벨, 장식) 쌍 — issue (blocking)
COMMENT_MAX_SENTENCES = 4                        # 본문 슬롯의 문장 상한 — shape 의 sh:maxInclusive 와 같은 값


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


# ── 빈 값·첨가·목록 (명세 문서 작성 규격 4.1·4.3·9.4, 유저 승인 2026-09-22 — 결정 p4-three-empty-values) ─────
# 세 빈 값은 서로 다른 사실이다. 하나로 합치면 검토하고 비운 자리·해당하지 않는 자리·답을 기다리는 자리가 같은 모양이
# 되어 감사가 셋을 가르지 못한다. 생성 문서 규약의 NONE_MARK 는 이 셋의 첫 값이고 정의처는 여기 하나다 (STYLEGUIDE §7).
EMPTY_REVIEWED = "없음"            # 찾아봤고 없다 — 다음 행동이 없다
EMPTY_NOT_APPLICABLE = "해당 없음"  # 이 항목에는 적용되지 않는다 — 다음 행동이 없다
EMPTY_UNDECIDED = "미확정"          # 아직 모른다 — 미결로 집계되고 답이 오면 채운다
EMPTY_VALUE = (EMPTY_REVIEWED, EMPTY_NOT_APPLICABLE, EMPTY_UNDECIDED)
# 세 값 밖의 빈 값 표기 — 보고용이다. `미정의`(undefined)는 빈 값이 아니라 낱말이라 뺀다. 따옴표·코드 스팬 안은
# prose_segments 가 이미 뺐으므로 규칙 자신을 인용한 문장(결정 p4-three-empty-values)은 잡히지 않는다
EMPTY_VALUE_REJECTED = re.compile(r"(?<![A-Za-z])[Nn]/[Aa](?![A-Za-z])|(?<![A-Za-z])TBD(?![A-Za-z])|미정(?!의)")
EMPTY_DASH_CELL = re.compile(r"[-–—]")  # 단독 대시로 비운 표 셀 — 헤더·구분 행 뒤의 셀에만 적용한다 (G14 와 같은 규칙)
# 메타 문장 — 슬롯의 질문에 답하지 않고 문서의 구조를 안내하는 문장. 좁게 시작한다: 오탐이 하나 나오면 보고 전체가
# 무시되기 때문이다 (p6-mass-fail-suspects-the-rule). "요약하면"·"참고로" 같은 접속 부사는 정상 용법과 가르기
# 어려워 넣지 않는다. 여기 있는 넷은 뒤따르는 내용을 예고할 뿐 자기 자신이 주장이 아니다
PROSE_META = re.compile(r"다음과 같다|(?:이|아래) (?:절|장|문서|청크|표)에서는|아래에서 (?:설명한다|다룬다|기술한다)|(?:앞서|앞에서) (?:말했|언급했|설명했)")
# 채움 문구 — 빈 값을 피하려고 슬롯을 때우는 문장. 세 빈 값과 다르다: `없음` 은 규칙이 요구하는 값이고 채움은 값이
# 아닌 문장이다. 실측 위반 0 이므로 제안 9.4절의 예시 형태를 그대로 옮긴다
PROSE_FILLER = re.compile(r"특이사항(?:은)? 없|일반적[인이] (?:방식|방법)을? (?:따른다|쓴다)|추후 (?:결정한다|정한다|보완한다|채운다)")
# 목록 규칙 (4.3절) — 상한 셋과 항목 정규식. 순서 목록의 번호는 모든 항목이 `1.` 이고 번호는 렌더러가 매긴다
LIST_MAX_ITEMS = 9
LIST_MAX_DEPTH = 2
# 항목 길이는 소스 줄이 아니라 글자로 잰다 — 이 저장소는 산문을 110~120자에서 손으로 접어 소스 줄과 렌더 줄이 다르다.
# 240 = 120자 × 2줄 (STYLEGUIDE §0, 결정 p4-slot-answers-one-question; 유저 승인 2026-09-22)
LIST_MAX_ITEM_CHARS = 240
MD_LIST_ITEM = re.compile(r"^(\s*)(?:[-*+]|(\d+)[.)])(?:\s+|$)")
# 게이트 id — 보고(consistency ⑧·⑨)와 게이트(chunk_lint)가 같은 이름을 쓴다. docs/waivers.md 가 이 이름으로 면제를 선언하고
# (축 `파일`), 면제된 항목은 집계에서 빼되 목록에는 남긴다. 축을 셋으로 가르는 까닭은 규약의 원본이 둘이기 때문이다 —
# 메타 문장·채움은 p4-slot-answers-one-question, 빈 값 표기는 p4-three-empty-values, 목록 규칙은 두 결정의 4.3절이다
ADDITION_GATE = "addition"        # ⑧ 메타 문장·채움 문구 — FAIL [addition]
EMPTY_VALUE_GATE = "empty-value"  # ⑧ 세 빈 값 밖의 표기 — FAIL [empty-value]
LIST_RULES_GATE = "list-rules"    # ⑨ 목록 규칙 — FAIL [list-rules]
# 살아 있는 청크의 status. 보고와 게이트의 대상 집합이 같아야 수치가 갈리지 않는다 — invalidated·deprecated 는
# 고칠 대상이 아니라 기록이므로 둘 다 제외한다 (나머지 둘은 chunk2kg.STATES)
LIVE_STATES = ("draft", "stable", "suspect")


def check_addition(text: str) -> tuple[list, list, list]:
    """첨가 → (메타 문장, 채움 문구, 빈 값 이상 표기). 각 원소는 (줄 번호, 표현, 인용).

    보고용이다 — 판정은 사람 몫이고 게이트가 아니다. 산문 판정은 prose_segments 안에서만 한다(코드·따옴표는
    산문이 아니다). 표의 단독 대시 셀은 산문 조각에 남지 않으므로 표 블록을 따로 훑는다.
    """
    meta: list[tuple[int, str, str]] = []
    filler: list[tuple[int, str, str]] = []
    empty: list[tuple[int, str, str]] = []
    for ln, seg in prose_segments(text):
        for rx, out in ((PROSE_META, meta), (PROSE_FILLER, filler), (EMPTY_VALUE_REJECTED, empty)):
            for m in rx.finditer(seg):
                out.append((ln, m.group(0).strip(), _around(seg, m.start(), m.end())))
    for block in _gendoc_tables(list(md_lines(text.split("\n")))):
        for ln, line in block[2:]:  # 헤더·구분 행 뒤의 값 행만 본다 — `|---|` 는 구분 행이다
            if any(EMPTY_DASH_CELL.fullmatch(c) for c in _gendoc_cells(line)):
                empty.append((ln, "단독 대시 셀", line.strip()))
    return meta, filler, empty


def check_lists(text: str) -> list[tuple[int, str]]:
    """목록 규칙(4.3절) 위반 → (줄 번호, 근거). 보고용이다.

    보는 것은 손 번호(`2.` 이상)·항목 수·중첩 깊이·항목 길이·빈 항목이다. 같은 문법 형은 기계 판정이 되지 않아
    넣지 않는다. 길이는 **글자**로 잰다 — 항목에 이어지는 들여쓴 연속 줄을 합치고 연속 공백을 하나로 줄인 뒤
    센다. 소스 줄을 세면 손 줄바꿈(110~120자)이 그대로 위반이 되어 규칙이 저작 결함을 가리키지 못한다.
    """
    out: list[tuple[int, str]] = []
    stack: list[list] = []   # 열려 있는 목록 — [들여쓰기, 깊이, 항목 수, 첫 줄]
    item: list | None = None  # 열려 있는 항목 — [첫 줄, 내용 들여쓰기, 글자 조각들]

    def close_item():
        nonlocal item
        if item:
            n = len(" ".join(" ".join(item[2]).split()))
            if n > LIST_MAX_ITEM_CHARS:
                out.append((item[0], f"목록 항목이 {n}자다 — 항목당 {LIST_MAX_ITEM_CHARS}자 이하로 쓰고 넘으면 별도 블록으로 나눈다"))
        item = None

    def close_lists(indent: int):
        while stack and stack[-1][0] > indent:
            _, _, count, first = stack.pop()
            if count > LIST_MAX_ITEMS:
                out.append((first, f"목록 항목이 {count}개다 — {LIST_MAX_ITEMS}개 이하로 쓰고 넘으면 블록을 나눈다"))

    for ln, line in md_lines(text.split("\n")):
        m = MD_LIST_ITEM.match(line)
        if m:
            close_item()
            indent = len(m.group(1))
            close_lists(indent)
            if not stack or stack[-1][0] < indent:
                stack.append([indent, len(stack) + 1, 0, ln])
            stack[-1][2] += 1
            if stack[-1][1] > LIST_MAX_DEPTH:
                out.append((ln, f"목록 중첩이 {stack[-1][1]}단계다 — {LIST_MAX_DEPTH}단계 이하로 쓰고 넘으면 블록을 나눈다"))
            if m.group(2) and m.group(2) != "1":
                out.append((ln, f"손 번호 `{m.group(2)}.` — 순서 목록의 항목은 모두 `1.` 로 쓰고 번호는 렌더러가 매긴다"))
            if not line[m.end():].strip():
                out.append((ln, f"빈 목록 항목 — 항목이 없으면 목록을 두지 않고 `{EMPTY_REVIEWED}` 으로 적는다"))
            item = [ln, m.end(), [line[m.end():]]]
        elif not line.strip():
            close_item()
        elif item is not None and len(line) - len(line.lstrip()) >= item[1]:
            item[2].append(line.strip())
        else:
            close_item()
            close_lists(-1)
    close_item()
    close_lists(-1)
    return sorted(out)


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

# ── 설계 공간 (`-space`) — 열린 설계 변수와 그 후보 (결정 p9-candidate-storage · p9-design-space-file) ───────────
# 후보 링크는 확정 링크와 다른 자리에 산다: 확정은 청크 head(frontmatter 링크 키 → Bazel deps), 후보는 `-space` 청크다.
# **후보는 결코 deps 가 되지 않는다** — `-space` 는 kb_chunk 타깃이 아니라 A-Box 그래프(`*-space.ttl`)로만 올라가고
# 그 그래프는 //kg:gate_test 의 --data 다. type 은 plane 이름이 아니라 온톨로지 클래스 `agt:Space` 이고 level 은 logical 이다.
# 후보의 표면 상태 어휘 셋은 링크 상태(agt:linkState)의 기존 값으로 내린다 — 새 상태 어휘를 만들지 않는다 (STYLEGUIDE §0 재사용):
#   open → candidate(agt:CandidateLink) · eliminated → invalid · confirmed → confirmed(agt:ConfirmedLink)
# 배제 근거는 증거 기록의 (−) 한 줄이다 (agt:Evidence · agt:polarity "-") — 근거 없는 배제 금지가 r-011 의 요지다.
SPACE_GATE = "space"        # 게이트 id — FAIL [space] (space2kg 의 생성 시점 거부와 validate check_space 가 같이 쓴다)
SPACE_TYPE = "agt:Space"    # `-space` 청크의 frontmatter type
SPACE_LEVEL = "logical"     # `-space` 청크의 level — 후보·제약·배제 근거가 사는 수준 (6.4절 수준 허용표)
SPACE_STATUS = ("open", "resolved")                            # agt:spaceStatus 의 값 어휘
SPACE_STATES = ("open", "eliminated", "confirmed")             # 후보의 표면 상태 어휘 (본문 `state:`)
LINK_STATE_INVALID = "invalid"                                 # 배제된 후보의 링크 상태 (link-state-ontology)
# 표면 상태 → (rdf:type 목록, agt:linkState). CandidateLink·ConfirmedLink 는 linkState 의 클래스 표현이므로
# 짝이 어긋나면 verify 질의 link-state-class-mismatch 가 잡는다 — 배제는 클래스 없이 상태만 invalid 다
SPACE_STATE_LINK = {
    "open": ("agt:Link , agt:CandidateLink", LINK_STATE_CANDIDATE),
    "eliminated": ("agt:Link", LINK_STATE_INVALID),
    "confirmed": ("agt:Link , agt:ConfirmedLink", LINK_STATE_CONFIRMED),
}
# 확정 근거가 될 수 있는 증거 종류 (9.11절 "구축(+) 또는 실행(+) 없이 확정 불가") — verify 질의 confirmed-without-evidence 와 같은 집합
SPACE_CONFIRMING_EVIDENCE = ("constructionRecord", "runResult")


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
     "when": "커밋 전에 중복·라벨 형식·용어 옛 표기·단정성(추측·구어·대시 밀도)·첨가(메타 문장·채움·빈 값 이상 표기)·목록 규칙 후보를 보고로 확인할 때 쓴다.",
     "commands": ["bazel build //kb:consistency && cat bazel-bin/kb/consistency.md"]},
    {"tool": "open_questions", "section": "method.md#9-뷰",
     "when": "무엇이 아직 미결인지 — 청크의 선택 슬롯 `미확정:` 에 든 질문과 그것을 안은 청크를 문서에 적지 않고 집계에서 인용할 때 쓴다.",
     "commands": ["bazel build //kg:open && cat bazel-bin/kg/open.md"]},
    {"tool": "choices", "section": "method.md#5-후보-관리",
     "when": "무엇을 아직 고르지 않았는가 — 열린 설계 변수와 그 후보를 체크박스(`[ ]` 열림 · `[-]` 배제 + 근거 · `[x]` 확정)로 확인할 때 쓴다.",
     "commands": ["bazel build //space:choices && cat bazel-bin/space/choices.md"]},
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
    {"tool": "gendoc", "section": "tools.md#게이트-총람--이-문서가-원본이다",
     "when": "생성기를 고친 뒤 생성 문서의 머리 블록·표·목차·링크·비율 표기가 규약 G1~G18 안인지 게이트와 같은 방식으로 검사할 때 쓴다.",
     "commands": ["bazel test //:gendoc_test",
                  "bazel run //tools:gendoc -- bazel-bin/kg/metrics.md bazel-bin/kb/dev/index.md"]},
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


# ── 마크다운 구조 헬퍼 — 펜스·제목 앵커·링크 (doccheck 과 생성 문서 게이트의 공용) ────────────────
# 앵커 규칙은 GitHub 과 같다. doccheck·weave·gen_skills·gendoc 이 모두 여기를 쓴다 (STYLEGUIDE §7).
MD_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
MD_HEADING = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.*?)(?:[ \t]+#+)?[ \t]*$")
MD_CODE_SPAN = re.compile(r"(`+)(.+?)\1")
MD_LINK_TEXT = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
MD_HTML_TAG = re.compile(r"<[^>]+>")
MD_SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*:")


def frontmatter_end(lines: list[str]) -> int:
    """YAML frontmatter 뒤 첫 줄의 0-기준 색인. frontmatter 가 없으면 0 이다."""
    if lines and lines[0].strip() == "---":
        try:
            return lines[1:].index("---") + 2
        except ValueError:
            return 0
    return 0


def md_lines(lines: list[str]):
    """(줄 번호, 줄) — 코드 펜스·frontmatter·HTML 주석 안은 산문이 아니므로 건너뛴다."""
    fence: str | None = None
    in_comment = False
    start = frontmatter_end(lines)
    for i, line in enumerate(lines[start:], start=start + 1):
        if in_comment:
            if "-->" in line:
                in_comment = False
                line = line.split("-->", 1)[1]
            else:
                continue
        m = MD_FENCE.match(line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            continue
        if m:
            fence = m.group(1)
            continue
        if "<!--" in line:
            head, _, tail = line.partition("<!--")
            if "-->" in tail:
                line = head + tail.split("-->", 1)[1]
            else:
                in_comment = True
                line = head
        yield i, line


def slug(text: str) -> str:
    """GitHub 제목 앵커 규칙 — 소문자, 공백→'-', 문자·숫자·결합 부호·'-'·'_' 외 제거."""
    text = MD_LINK_TEXT.sub(r"\1", text)
    text = MD_HTML_TAG.sub("", text)
    out = []
    for c in text.lower():
        if c == " ":
            out.append("-")
        elif c in "-_" or c.isalnum() or unicodedata.category(c).startswith("M"):
            out.append(c)
    return "".join(out)


def heading_anchors(headings: list[str]) -> list[str]:
    """제목들의 GitHub 앵커 — 문서 순서로 같은 slug 는 -1, -2 … 로 구분한다."""
    seen: dict[str, int] = {}
    out = []
    for h in headings:
        s = slug(h)
        n = seen.get(s, 0)
        seen[s] = n + 1
        out.append(s if n == 0 else f"{s}-{n}")
    return out


def md_anchors(lines: list[str]) -> set[str]:
    """파일의 제목 앵커 집합."""
    return set(heading_anchors([m.group(2).strip() for _, line in md_lines(lines) if (m := MD_HEADING.match(line))]))


def find_links(line: str):
    """줄 안의 인라인 링크 목적지 — `](` 뒤에서 괄호 짝을 맞춰 읽는다. 제목("…")은 뗀다."""
    i = 0
    while True:
        j = line.find("](", i)
        if j < 0:
            return
        depth, k = 1, j + 2
        while k < len(line) and depth:
            depth += {"(": 1, ")": -1}.get(line[k], 0)
            k += 1
        if depth:
            return
        dest = line[j + 2:k - 1].strip()
        i = k
        if dest.startswith("<") and ">" in dest:
            dest = dest[1:dest.index(">")]
        else:
            dest = dest.split()[0] if dest.split() else ""
        yield dest


# ── 생성 문서 규약 G1~G18 — 에이전트가 만드는 마크다운의 형태 (유저 지시 2026-09-21) ─────────────
# 출력 형태를 생성 전에 고정하고, 파싱·형식 복구를 없애며, 확신 상태(입력 지문·생성 시각·질의)를 값으로 남긴다.
# 여기가 규약의 단일 정의처다 — 상수·머리 블록 방출·검사가 한 곳에 있고 생성기와 게이트가 같은 것을 import 한다 (STYLEGUIDE §7).
GENDOC_GATE = "gendoc"                    # 게이트 id — FAIL [gendoc]
GENDOC_VERSION = "gendoc/1"               # OKF 행위자 표기의 버전 (docs/rules.md 생성자 표기). 도구별이 아니라 규약 하나의 버전이다
GENDOC_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"  # G3 — ISO 8601 UTC 초 해상도. 오프셋 표기(+00:00)·분 해상도를 쓰지 않는다
GENDOC_TIME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
NONE_MARK = EMPTY_REVIEWED                # G14 — 생성 문서의 빈 값 표기. 빈 셀·em dash·"N/A" 를 쓰지 않는다. 정의처는 EMPTY_VALUE 셋의 첫 값 하나다
RATIO_DIGITS = 1                          # G15 — 백분율 소수 자릿수
VALUE_DIGITS = 3                          # G15 — 백분율이 아닌 수치(모듈러리티 Q·Jaccard·링크 밀도·소요 초)의 자릿수
GENDOC_TOC_MIN = 120                      # G12 — 본문이 이 줄 수를 넘으면 목차 절을 둔다 (ISO/IEC/IEEE 26514:2022 9.10.5)
GENDOC_TOC_HEADING = "목차"
GENDOC_INPUT_INLINE_MAX = 6               # G4 — 입력 목록을 머리 블록에 그대로 쓰는 상한. 넘으면 입력 파일 절로 접는다
GENDOC_INPUTS_HEADING = "입력 파일"
GENDOC_HEAD_KEYS = ("생성기", "생성 시각", "입력", "질의", "재현")  # 순서 고정 (G2~G6). 그 뒤가 성격 경고 한 줄 (G7)
GENDOC_H1_SUFFIX = "(생성 파일)"
GENDOC_VIEW_MARK = "이 파일은 뷰다."              # G7 — Bazel 뷰
GENDOC_TREE_MARK = "생성 파일 — 손으로 고치지 않는다."  # G7 — 생성 트리 파일 (SKILL·BUILD)
GENDOC_DETERMINISTIC_NOTE = "생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다"
# 인용 구역 — 생성물이 청크 본문을 그대로 옮긴 자리. 원본 청크가 자기 게이트(chunk_lint prose·42줄)를 이미 통과했고
# 생성기는 원문을 고쳐 쓰지 않으므로(G17), 서식 규칙 G10·G11·G14·G15·G18 은 이 구역을 판정하지 않는다.
# 문서 전체에 걸리는 구조 규칙 G8·G9·G12·G13 은 구역 안에도 그대로 적용한다 — 인용이 문서를 깨뜨리면 안 된다.
GENDOC_QUOTE_OPEN = "<!-- 인용 시작: 청크에서 그대로 옮긴 값 — 원본이 자기 게이트를 통과했다 -->"
GENDOC_QUOTE_CLOSE = "<!-- 인용 끝 -->"
GENDOC_QUOTE_LINE = "<!-- 인용 -->"  # 한 줄짜리 인용 — 라벨처럼 그래프에서 그대로 가져온 값을 담은 줄의 끝에 붙인다
GENDOC_QUOTE_EXEMPT = ("G10", "G11", "G14", "G15", "G18")
_GENDOC_BAZEL_OUT = re.compile(r"^(?:\.\./)*(?:bazel-out/[^/]+/(?:bin|genfiles)/|external/)")
_GENDOC_PCT = re.compile(r"(?<![\d/.])(\d+(?:\.\d+)?)%")
_GENDOC_PCT_OK = re.compile(r"\d+/\d+ = \*{0,2}$")
_GENDOC_EMPTY_CELL = re.compile(r"^(?:|-|—|–|N/A|n/a|없음\s*\(\s*\))$")


def now_utc() -> str:
    """G3 의 생성 시각 — ISO 8601 UTC 초 해상도."""
    return datetime.now(timezone.utc).strftime(GENDOC_TIME_FORMAT)


def pct(n: int, d: int) -> str:
    """G15 — 비율은 `n/d = p.p%` 꼴이다. 분모 없는 백분율을 쓰지 않는다. 0 분모는 없음이다 (G14)."""
    return f"{n}/{d} = {100 * n / d:.{RATIO_DIGITS}f}%" if d else NONE_MARK


def num(x: float) -> str:
    """G15 — 백분율이 아닌 수치의 자릿수. 모듈러리티 Q·Jaccard·링크 밀도·소요 초가 같은 자릿수를 쓴다."""
    return f"{x:.{VALUE_DIGITS}f}"


def gendoc_input_name(path: str) -> str:
    """입력 파일의 표기 — 샌드박스의 bazel-out·external 접두를 떼어 워크스페이스 상대 경로로 보인다."""
    return _GENDOC_BAZEL_OUT.sub("", str(path).replace(os.sep, "/"))


def input_fingerprint(paths) -> str:
    """G4 의 입력 지문 — 정렬된 경로 순으로 내용을 이어 SHA-256, 앞 12자. 리비전보다 정확하고 샌드박스에서도 얻는다."""
    h = hashlib.sha256()
    for p in sorted(paths, key=gendoc_input_name):
        try:
            h.update(Path(p).read_bytes())
        except OSError:
            h.update(b"\0missing\0")
    return "sha256:" + h.hexdigest()[:12]


def gendoc_quote(body: str) -> list[str]:
    """청크 본문을 그대로 옮긴 구역 — 서식 규칙의 판정 밖임을 표시한다 (원문을 고쳐 쓰지 않는다)."""
    return [GENDOC_QUOTE_OPEN, "", body, "", GENDOC_QUOTE_CLOSE, ""]


def gendoc_quoted_lines(lines: list[str]) -> set[int]:
    """인용 구역에 속하는 1-기준 줄 번호."""
    out: set[int] = set()
    inside = False
    for i, line in enumerate(lines, start=1):
        s = line.strip()
        if s == GENDOC_QUOTE_OPEN:
            inside = True
        if inside or s.endswith(GENDOC_QUOTE_LINE):
            out.add(i)
        if s == GENDOC_QUOTE_CLOSE:
            inside = False
    return out


def gendoc_view_notice(source: str) -> str:
    """G7 — Bazel 뷰의 성격 경고. source 는 고칠 원본(청크·frontmatter·그래프)이다."""
    return f"{GENDOC_VIEW_MARK} 저장하지 않고 인용한다. 고칠 것은 {source}이다 (`p12-documents-are-generated`)"


def gendoc_tree_notice(source: str, target: str) -> str:
    """G7 — 생성 트리 파일(SKILL·BUILD)의 성격 경고. target 은 드리프트를 잡는 검사 타깃이다."""
    return f"{GENDOC_TREE_MARK} 원본은 {source}이다. 검사: `{target}`. {GENDOC_DETERMINISTIC_NOTE}"


def gendoc_header(name: str, purpose: str, tool: str, query: str, reproduce: str, inputs, scale: str,
                  notice: str, input_kind: str = "입력 파일", stamped: bool = True, extra=(), input_note: str = "") -> list[str]:
    """G1~G7 의 머리 블록 — 모든 생성 마크다운의 첫 블록이고 순서가 고정이다.

    Args:
      name: 문서 이름 (h1 의 앞부분, 보통 생성물 파일의 stem).
      purpose: 한 줄 목적.
      tool: 생성기 경로 (`tools/<도구>.py`).
      query: 무엇을 물어 만들었는가 (G5).
      reproduce: 자기 자신을 다시 만드는 명령 (G6). 백틱은 이 함수가 붙인다.
      inputs: 입력 파일 경로들. 목록과 지문이 여기서 나온다 (G4).
      scale: 규모 수치 (트리플 수 등).
      notice: 성격 경고 한 줄 (G7) — gendoc_view_notice · gendoc_tree_notice.
      input_kind: 입력 목록의 종류 이름 ("그래프 파일" 등).
      stamped: False 면 생성 시각과 지문을 넣지 않는다 — 재생성 바이트 비교가 건전성 장치인 생성 트리 파일이 그렇다.
      extra: 머리 블록 뒤에 붙일 추가 불릿들.
      input_note: 입력이 파일이 아닐 때(질의 결과·호스트 상태) 그 자리를 대신하는 한 줄. 주면 목록과 지문을 내지 않는다.

    Returns:
      머리 블록의 줄 목록. 마지막은 빈 줄이다.
    """
    files = [gendoc_input_name(p) for p in inputs]
    listed = " · ".join(f"`{f}`" for f in sorted(files))
    scale_part = f" · {scale}" if scale else ""
    if input_note:
        body = f"{input_note}{scale_part}"
    elif not files:
        body = f"{input_kind} {NONE_MARK}{scale_part}"
    elif len(files) <= GENDOC_INPUT_INLINE_MAX:
        fp = f" · 지문 `{input_fingerprint(inputs)}`" if stamped else ""
        body = f"{input_kind} {len(files)}개: {listed}{fp}{scale_part}"
    else:
        fp = f" · 지문 `{input_fingerprint(inputs)}`" if stamped else ""
        body = (f"{input_kind} {len(files)}개{fp}{scale_part} · 전체 목록은 "
                f"[{GENDOC_INPUTS_HEADING}](#{slug(GENDOC_INPUTS_HEADING)})")
    out = [f"# {name} — {purpose} {GENDOC_H1_SUFFIX}", "",
           f"- 생성기: `{tool}` · {GENDOC_VERSION}"]
    if stamped:
        out.append(f"- 생성 시각: {now_utc()}")
    out += [f"- 입력: {body}",
            f"- 질의: {query}",
            f"- 재현: `{reproduce}`",
            f"- {notice}"]
    return out + list(extra) + [""]


def gendoc_inputs_section(inputs, input_kind: str = "입력 파일") -> list[str]:
    """G4 — 머리 블록에 접은 입력 목록의 전체. 입력이 GENDOC_INPUT_INLINE_MAX 를 넘으면 문서 어딘가에 이 절이 있어야 한다.

    파일 하나하나를 전부 적되 디렉토리로 묶는다 — 목록이 본문을 덮지 않으면서 어느 파일이 들어갔는지 판별된다.
    """
    files = sorted({gendoc_input_name(p) for p in inputs})
    groups: dict[str, list[str]] = {}
    for f in files:
        d, _, base = f.rpartition("/")
        groups.setdefault(d + "/" if d else "./", []).append(base)
    out = [f"## {GENDOC_INPUTS_HEADING}", "",
           f"{input_kind} {len(files)}개다. 지문은 이 목록의 파일 내용을 경로 순으로 이어 낸 SHA-256 의 앞 12자다. "
           "디렉토리로 묶었고 빠진 파일은 없다.", ""]
    body = [f"- `{d}` — " + " · ".join(f"`{b}`" for b in sorted(bs)) for d, bs in sorted(groups.items())]
    return out + (body or [f"- {NONE_MARK}"]) + [""]


def _gendoc_headings(lines: list[str]) -> list[tuple[int, str]]:
    """펜스 밖 제목들의 (수준, 텍스트) — 문서 순서."""
    return [(len(m.group(1)), m.group(2).strip()) for _, line in md_lines(lines) if (m := MD_HEADING.match(line))]


def gendoc_assemble(head: list[str], body: list[str], inputs, input_kind: str = "입력 파일",
                    toc_note: str = "", toc_levels=(2,)) -> str:
    """머리 블록 + (G12 가 요구하면) 목차 + 본문 + (G4 가 요구하면) 입력 파일 절 → 문서 전체.

    목차 앵커는 문서 전체의 제목으로 계산한다 — 같은 slug 의 -1, -2 구분이 실제 문서와 같아야 링크가 산다.
    본문이 이미 목차 절을 가지면 덧붙이지 않는다.
    """
    n_files = len({gendoc_input_name(p) for p in inputs})
    tail = gendoc_inputs_section(inputs, input_kind) if n_files > GENDOC_INPUT_INLINE_MAX else []
    rest = list(body) + tail
    have_toc = any(t == GENDOC_TOC_HEADING for _, t in _gendoc_headings(rest))
    if len(head) + len(rest) <= GENDOC_TOC_MIN or have_toc:
        return "\n".join(head + rest) + "\n"
    hs = [(2, GENDOC_TOC_HEADING)] + _gendoc_headings(rest)
    anchors = heading_anchors([t for _, t in hs])
    toc = [f"## {GENDOC_TOC_HEADING}", ""] + ([toc_note, ""] if toc_note else [])
    toc += [f"- [{t}](#{a})" for (lvl, t), a in list(zip(hs, anchors))[1:] if lvl in toc_levels]
    return "\n".join(head + toc + [""] + rest) + "\n"


def gendoc_toc(headings: list[str], note: str = "") -> list[str]:
    """G12 — 목차 절. 앵커는 slug 로 만든다. headings 는 문서에 나오는 순서의 제목 텍스트다."""
    anchors = heading_anchors(headings)
    out = [f"## {GENDOC_TOC_HEADING}", ""] + ([note, ""] if note else [])
    return out + [f"- [{h}](#{a})" for h, a in zip(headings, anchors)] + [""]


def _gendoc_tables(rows: list[tuple[int, str]]) -> list[list[tuple[int, str]]]:
    """연속한 표 줄들의 묶음 — (줄 번호, 줄). 펜스 밖의 '|' 로 시작하는 줄이 표다."""
    blocks: list[list[tuple[int, str]]] = []
    cur: list[tuple[int, str]] = []
    prev = None
    for ln, line in rows:
        if line.lstrip().startswith("|"):
            if cur and prev is not None and ln != prev + 1:
                blocks.append(cur)
                cur = []
            cur.append((ln, line))
        elif cur:
            blocks.append(cur)
            cur = []
        prev = ln
    if cur:
        blocks.append(cur)
    return blocks


def _gendoc_cells(line: str) -> list[str]:
    s = line.strip()
    return [c.strip() for c in s.strip("|").split("|")]


def check_gendoc(path, text: str, exists=None) -> list[tuple[int, str]]:
    """생성 마크다운 규약 G1~G15·G18 중 기계 판정이 되는 것 → (줄 번호, 근거).

    check_prose 와 같은 모양으로 낸다 — 게이트가 `FAIL [gendoc] <파일>:<줄>: <근거>` 로 찍는다.
    exists 는 `경로 → bool` 로 링크 대상의 실재를 판정한다 (G13). 없으면 문서 안 앵커만 본다.
    """
    errors: list[tuple[int, str]] = []
    lines = text.split("\n")
    start = frontmatter_end(lines)
    while start < len(lines) and not lines[start].strip():  # frontmatter 뒤의 빈 줄은 본문 앞이다
        start += 1
    body = lines[start:]
    while body and not body[-1].strip():
        body.pop()
    rows = list(md_lines(lines))
    quoted = gendoc_quoted_lines(lines)

    # G1 · G2~G7 — 머리 블록. h1 한 줄이 첫 줄이고 순서가 고정이다
    first = start + 1
    if not body or not re.fullmatch(r"# \S.*" + re.escape(GENDOC_H1_SUFFIX), body[0]):
        errors.append((first, f"G1 첫 줄이 `# <이름> — <목적> {GENDOC_H1_SUFFIX}` 가 아니다 — kb_lib.gendoc_header 로 낸다"))
    else:
        if len(body) < 2 or body[1].strip():
            errors.append((first + 1, "G1 h1 다음 줄은 빈 줄이다 — kb_lib.gendoc_header 로 낸다"))
        head = []
        for i, line in enumerate(body[2:], start=2):
            if not line.startswith("- "):
                break
            head.append((first + i, line))
        keys = [k for k in GENDOC_HEAD_KEYS]
        got = [(ln, line[2:].split(":", 1)[0]) for ln, line in head]
        want = [k for k in keys if k != "생성 시각" or any(g == "생성 시각" for _, g in got)]
        for i, k in enumerate(want):
            if i >= len(got) or got[i][1] != k:
                errors.append((head[i][0] if i < len(head) else first + 2,
                               f"G2~G6 머리 블록 {i + 1}번째 항목은 `- {k}:` 다 — 순서는 {' · '.join(want)} 이고 그 뒤가 성격 경고 한 줄이다"))
                break
        else:
            v = {k: head[i][1][2:].split(": ", 1)[-1] for i, k in enumerate(want)}
            if GENDOC_VERSION.split("/")[0] + "/" not in v["생성기"]:
                errors.append((head[0][0], f"G2 생성기 줄에 규약 버전 표기 `{GENDOC_VERSION}` 가 없다 — kb_lib.GENDOC_VERSION 이 단일 정의처다"))
            if "생성 시각" in v and not GENDOC_TIME_RE.fullmatch(v["생성 시각"].strip()):
                errors.append((head[want.index("생성 시각")][0],
                               f"G3 생성 시각이 `{GENDOC_TIME_FORMAT}` 가 아니다 (실제 {v['생성 시각'].strip()!r}) — kb_lib.now_utc 를 쓴다"))
            i_in = head[want.index("입력")][0]
            if "생성 시각" in v and "지문 `sha256:" not in v["입력"]:
                errors.append((i_in, "G4 입력 줄에 지문(`sha256:<앞 12자>`)이 없다 — kb_lib.input_fingerprint 를 쓴다"))
            if "개:" not in v["입력"] and f"#{slug(GENDOC_INPUTS_HEADING)}" not in v["입력"] and NONE_MARK not in v["입력"]:
                errors.append((i_in, f"G4 입력 줄에 파일 목록이 없다 — 개수만 적지 않는다. 많으면 `{GENDOC_INPUTS_HEADING}` 절로 접는다"))
            if f"#{slug(GENDOC_INPUTS_HEADING)}" in v["입력"] and not any(
                    (m := MD_HEADING.match(line)) and m.group(2).strip() == GENDOC_INPUTS_HEADING for _, line in rows):
                errors.append((i_in, f"G4 입력 줄이 `{GENDOC_INPUTS_HEADING}` 절을 가리키는데 그 절이 없다 — kb_lib.gendoc_inputs_section 을 붙인다"))
            if "`" not in v["재현"]:
                errors.append((head[want.index("재현")][0], "G6 재현 줄의 명령은 백틱 안에 적는다 — 자기 자신을 다시 만드는 명령이다"))
            notice = head[len(want)][1] if len(head) > len(want) else ""
            if GENDOC_VIEW_MARK not in notice and GENDOC_TREE_MARK not in notice:
                errors.append((head[len(want) - 1][0] + 1,
                               "G7 머리 블록 끝에 성격 경고 한 줄이 없다 — kb_lib.gendoc_view_notice · gendoc_tree_notice"))

    # G8 · G9 — 제목 계층은 한 단계씩, h1 은 문서당 하나 (MD001 · MD025 · MD041)
    prev_level = 0
    for ln, line in rows:
        m = MD_HEADING.match(line)
        if not m:
            continue
        level = len(m.group(1))
        if level == 1 and prev_level:
            errors.append((ln, f"G9 문서당 h1 은 하나다 (MD025) — `{m.group(2).strip()[:40]}`"))
        elif prev_level and level > prev_level + 1:
            errors.append((ln, f"G8 제목 계층은 한 단계씩 내려간다 (MD001) — h{prev_level} 다음에 h{level} 이 왔다"))
        prev_level = level

    # G10 — 표는 헤더 행을 갖고 열 수가 같고 앞뒤에 빈 줄이 있다 (MD055 · MD056 · MD058)
    by_ln = dict(rows)
    for block in _gendoc_tables(rows):
        ln0, first_line = block[0]
        if ln0 in quoted:
            continue
        if len(block) < 2 or not re.fullmatch(r"\|[\s:|-]+\|", block[1][1].strip()):
            errors.append((ln0, "G10 표에 헤더 행과 구분 행(`|---|`)이 없다 (MD055)"))
            continue
        width = len(_gendoc_cells(first_line))
        for ln, line in block[1:]:
            if len(_gendoc_cells(line)) != width:
                errors.append((ln, f"G10 표의 열 수가 헤더와 다르다 (MD056) — 헤더 {width}, 이 행 {len(_gendoc_cells(line))}"))
        before, after = by_ln.get(ln0 - 1), by_ln.get(block[-1][0] + 1)
        if before is not None and before.strip():
            errors.append((ln0, "G10 표 앞에 빈 줄이 있어야 한다 (MD058)"))
        if after is not None and after.strip():
            errors.append((block[-1][0] + 1, "G10 표 뒤에 빈 줄이 있어야 한다 (MD058)"))
        # G14 — 빈 셀은 없음으로 적는다
        for ln, line in block[2:]:
            for c in _gendoc_cells(line):
                if _GENDOC_EMPTY_CELL.fullmatch(c):
                    errors.append((ln, f"G14 빈 표 셀 — 비우거나 대시를 쓰지 않고 `{NONE_MARK}` 으로 적는다 (Microsoft Writing Style Guide, Tables)"))
                    break

    # G11 — 펜스 코드 블록에 언어를 명시한다 (MD040)
    fence = None
    for i, line in enumerate(lines[start:], start=start + 1):
        m = MD_FENCE.match(line)
        if not m:
            continue
        if fence:
            if m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            continue
        fence = m.group(1)
        if i not in quoted and not line.strip()[len(m.group(1)):].strip():
            errors.append((i, "G11 펜스 코드 블록에 언어를 명시한다 (MD040) — 예 ```text"))

    # G12 — 긴 문서는 목차 절을 둔다
    headings = [(ln, MD_HEADING.match(line).group(2).strip()) for ln, line in rows if MD_HEADING.match(line)]
    if len(body) > GENDOC_TOC_MIN and not any(h == GENDOC_TOC_HEADING for _, h in headings):
        errors.append((first, f"G12 본문 {len(body)}줄이 {GENDOC_TOC_MIN}줄을 넘는데 `{GENDOC_TOC_HEADING}` 절이 없다 "
                              "(ISO/IEC/IEEE 26514:2022 9.10.5) — kb_lib.gendoc_toc 를 쓴다"))

    # G13 — 링크의 경로와 앵커가 생성물이 놓이는 위치 기준으로 실재한다
    anchors = {a for _, h in headings for a in [slug(h)]} | md_anchors(lines)
    doc_dir = os.path.dirname(str(path))
    for ln, line in rows:
        for dest in find_links(MD_CODE_SPAN.sub(" ", line)):
            if not dest or MD_SCHEME.match(dest):
                continue
            target, _, frag = dest.partition("#")
            if not target:
                if frag and frag not in anchors:
                    errors.append((ln, f"G13 없는 앵커 ({dest}) — 이 문서의 제목 slug 에 #{frag} 가 없다"))
                continue
            if exists is None:
                continue
            rel = os.path.normpath(target[1:] if target.startswith("/") else os.path.join(doc_dir, target))
            if not exists(rel):
                errors.append((ln, f"G13 깨진 링크 ({dest}) — {rel} 가 없다. 생성물은 전 패키지를 한 파일로 합치므로 "
                                   "파일명 상대 링크가 성립하지 않는다. 문서 안 앵커나 저장소 루트 기준 경로(`/`로 시작)로 적는다"))

    # G15 — 비율은 n/d = p.p%. 분모 없는 백분율을 쓰지 않는다. 목표 표기(G16)는 값이 아니라 기준이므로 뺀다
    heading_lines = {ln for ln, line in rows if MD_HEADING.match(line)}
    for ln, seg in prose_segments(text):
        if ln in quoted or ln in heading_lines:  # 제목은 이름이지 측정이 아니다
            continue
        seg = MD_LINK_TEXT.sub(" ", seg)  # 링크 텍스트도 이름이다 — 목차의 라벨이 백분율을 담을 수 있다
        for m in _GENDOC_PCT.finditer(seg):
            before = seg[:m.start()]
            if "목표" in before[-24:]:
                continue
            if not _GENDOC_PCT_OK.search(before):
                errors.append((ln, f"G15 분모 없는 백분율 `{m.group(0)}` — `n/d = p.p%` 꼴로 적는다 (kb_lib.pct)"))
            elif "." not in m.group(1) or len(m.group(1).split(".")[1]) != RATIO_DIGITS:
                errors.append((ln, f"G15 백분율의 소수 자릿수는 {RATIO_DIGITS} 이다 — `{m.group(0)}` (kb_lib.pct)"))

    # G18 — 산문은 단정 서술형이다 (STYLEGUIDE §0). 인용해 옮긴 청크 본문은 원본이 같은 게이트를 이미 통과했다
    errors += [(ln, why) for ln, why in check_prose(path, text)[0] if ln not in quoted]
    return sorted(errors)
