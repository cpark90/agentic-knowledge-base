#!/usr/bin/env python3
"""청크 파일 → head 그래프(-kg) 생성.

한 청크는 한 파일이다. head 메타데이터(타입·plane·level·라벨·상태·출처)는
청크 파일의 frontmatter에 있고, 본문(assertion)은 그 아래 있다 (노트 4.3절).
`-kg`의 head 그래프는 손으로 쓰지 않고 이 도구가 청크 파일들에서 생성한다 —
agt:lineCount 와 agt:assertionLocation 은 파일에서 계산되므로 어긋날 수 없다.

frontmatter 형식 (YAML 부분집합 — key: value, 목록은 [a, b], 인라인 맵은 {k: v}).
OKF v0.2 번들이므로 type·status·generated·verified 는 그 스펙의 필드명을 쓴다:
  iri:          항목 IRI (필수)
  type:         requirement | decision | contract | schema | artifact | annotation | memory (필수, OKF)
  level:        functional | abstract | logical | concrete | executable (필수)
  title_ko:     한글 라벨 (필수) — OKF 확장 키
  title:        영어 라벨 (필수) — OKF title
  status:       draft | stable | suspect | invalidated | deprecated (필수, OKF + 확장 2)
  generated:    {by: <행위자>, at: <ISO 8601>} (필수, OKF)
  verified:     [{by: <행위자>, at: <ISO 8601>}, ...] (선택, OKF) — human: 접두어가 사람 검토
  assumes:      가정 IRI 목록 (선택)
  sources:      OKF v0.2 sources — [{resource: IRI, id?, title?, author?}] (선택). resource → prov:wasDerivedFrom
  refines:      이 항목이 정제하는 상위 항목 IRI 목록 (선택, 수직 링크 9.2절)
  supersedes:   이 항목이 대체하는 항목 IRI 목록 (선택)
  serves·verifies·derivesFrom·satisfies·constrains·allocates·generates: 그 밖의 링크 키(LINK_KEYS) — 대상 IRI 목록 (선택).
                모든 링크 키는 직접 트리플(agt:<key>)과 링크 개체(agt:Link, emit_links) 둘로 나간다. verifies 의 주어는 kb/vv 청크뿐 (defs/kb.bzl)
  restored:     복원 링크의 표시 — 같은 청크의 링크 키(LINK_KEYS) 어딘가에 대상으로 있는 IRI 목록 (선택, p10-restored-link-marking).
                그 (주어, 링크 키, 대상)의 agt:Link 개체에 증거가 두 줄 붙는다 — 확정 기록 constructionRecord(사람이 frontmatter 에 적은
                편집 시점 기록; 9.11절 규칙 "구축(+) 또는 실행(+) 없이 확정 불가"를 verify 질의 confirmed-without-evidence 가 강제한다)와
                후보의 출처 proposal(도구·에이전트가 제안하고 사람이 확정). 구축 링크는 constructionRecord 한 줄뿐이므로 proposal 의 유무가
                복원의 표지다. linkState 는 그대로 confirmed 다 — frontmatter 에 적힌 것은 확정이다. 링크 대상에 없는 IRI 는
                `FAIL [restored] <파일>: 복원 표시 <IRI> 가 링크 대상에 없다` 로 거부. 복원 비율(metrics·audit)은 증거 종류로 센다 (kb_lib.link_origins)
  specializationOf: 분할로 생긴 조각이 원 청크를 가리키는 단일 IRI (선택, p10-split-keeps-work-identity) → prov:specializationOf (PROV-O).
                청크 uuid 는 work-id 다: 분할 시 조각 하나가 원 uuid 를 승계하고 나머지는 새 uuid + 이 키로 잇는다. 자기 자신은 거부.
                대상 실재는 validate dangling, 같은 plane·살아 있음·사슬 비순환은 validate check_specialization(FAIL [specialization])이
                판정한다. 순환은 이 도구도 뿌리를 계산할 수 없으므로 같은 게이트 id 로 거부한다
  링크 IRI:     id/link/<sha256(뿌리(출발)|종류|뿌리(도착))[:12]> — 양 끝은 specializationOf 사슬을 따라 올라간 뿌리 uuid(work-id)다.
                그래서 조각을 가리키는 링크와 원본을 가리키던 링크가 같은 개체가 되어 증거·이력이 이어진다. 뿌리는 묶음 전체를 알아야
                계산되므로 --fragment 는 원 IRI 로 해시하고 --merge(와 단일 실행)가 rebase_links 로 다시 계산해 같은 IRI 의 링크·증거
                블록을 하나로 합친다(양 끝·증거의 합집합). 증거 IRI 는 같은 해시에 접미(-proposal)다
  coUpdatesWith: 같은 내용을 담아 함께 갱신되어야 하는 청크 IRI 목록 (선택, relatedTo 족 — 안전율 중복의 표시)
  part_of:      소속 복합체 IRI (선택) — 복합체는 멤버 중 하나가 composite: 로 선언
  composite:    {id: …, title_ko: …, title: …} (선택) — 복합체 개체 선언
  pattern:      ubiquitous | event-driven | state-driven | unwanted-behaviour | optional | complex (선택, type: requirement 에서만) —
                요구 문장의 EARS 패턴 (Mavin RE'09, 결정 p7-dev-plane-substance) → agt:pattern agt:<camelCase 개체>. 다른 plane 에 있으면 거부
  프로파일 타이핑: 청크마다 plane 클래스 뒤에 개발 프로파일의 실체 클래스를 더 붙인다 (`a agt:RequirementChunk , agt:RequirementStatement`,
                PROFILE_SUBSTANCE). 살아 있는 청크든 폐기된 청크든 같다 — 폐기된 요구 문장도 요구 문장이다
  라벨 언어:    title 에 한글([ㄱ-ㆎ가-힣])이 있거나 title_ko 에 한글이 없으면 거부 — 영문 라벨에 한글을 섞지 않는다(0.6절).
                composite 의 title·title_ko 도 같은 @en/@ko 라벨이므로 같은 규칙으로 거부한다
  인용원:       본문(frontmatter 제외)에 소멸성 채널 경로 `docs/feedback/` 가 있으면 거부 — 규칙·근거는 영속 지식
                (노트·결정)에 둔다 (agrtls-practices-review P). status: deprecated 청크는 제외

출력·종료: 위반은 `FAIL [chunk2kg] <경로>: <메시지>` (병합은 `FAIL [chunk2kg-merge]`, 특수화 사슬은 `FAIL [specialization]`) + EXIT_FAIL,
           읽을 수 없는 입력은 EXIT_CONFIG. 생성기이므로 입력 0건은 빈 그래프(SKIP 아님).
사용: chunk2kg.py --out <생성.ttl> <청크 파일들...>
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

try:  # 종료 코드 규약의 단일 정의처는 kb_lib — 이 도구는 rdflib 없이 돌므로(타깃마다 실행) 없으면 같은 값의 폴백
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    try:
        import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
    except ImportError:
        kb_lib = None
EXIT_FAIL = getattr(kb_lib, "EXIT_FAIL", 1)      # 판정 실패
EXIT_CONFIG = getattr(kb_lib, "EXIT_CONFIG", 2)  # 파일 없음·읽을 수 없는 입력

TAG = "chunk2kg"
EPHEMERAL_PATH = "docs/feedback/"  # 소멸성 채널 — 인용원이 될 수 없다 (agrtls-practices-review P)
SPECIALIZATION_KEY = "specializationOf"  # frontmatter 키 — 분할 조각 → 원 청크 (p10-split-keeps-work-identity)
SPECIALIZATION_GATE = getattr(kb_lib, "SPECIALIZATION_GATE", "specialization")  # 게이트 id — FAIL [specialization] (정의처 kb_lib)
LINK_STATE_CANDIDATE = getattr(kb_lib, "LINK_STATE_CANDIDATE", "candidate")  # 후보 — extract_refs 가 낸다 (정의처 kb_lib)
LINK_STATE_CONFIRMED = getattr(kb_lib, "LINK_STATE_CONFIRMED", "confirmed")  # 확정 — frontmatter 링크 (정의처 kb_lib)


class SpecializationError(ValueError):
    """specializationOf 규칙 위반 — 자기 참조·사슬 순환. 게이트 id 는 SPECIALIZATION_GATE 다."""

PLANE_CLASS = {
    "requirement": "agt:RequirementChunk",
    "decision": "agt:DecisionChunk",
    "contract": "agt:ContractChunk",
    "schema": "agt:SchemaChunk",
    "artifact": "agt:ArtifactChunk",
    "annotation": "agt:AnnotationChunk",
    "memory": "agt:MemoryChunk",
}
# 개발 프로파일 — plane → 실체 클래스 (결정 p7-dev-plane-substance; kb/ontology/profile/development/plane-substance-ontology.ttl).
# 프로파일 바인딩 입력의 첫 형태다: 프로파일이 하나뿐이라 입력 파라미터 없이 고정한다. 프로파일이 둘 이상이 되면 이 표가 입력이 된다.
# 이 도구는 rdflib 없이 타깃마다 돌므로(kb.bzl 의 head 액션) 값 어휘 상수는 PLANE_CLASS 와 함께 여기가 정의처다 (STYLEGUIDE §4).
# plane 클래스를 앞에 둔다 — metrics·workset·community 가 첫 rdf:type 을 plane 으로 읽는다
PROFILE_SUBSTANCE = {
    "requirement": "agt:RequirementStatement",
    "decision": "agt:DesignDecision",
    "contract": "agt:InterfaceSignature",
    "schema": "agt:MessageSchema",
    "artifact": "agt:FunctionArtifact",
    "annotation": "agt:ReviewComment",
    "memory": "agt:SessionObservation",
}
# EARS 패턴 (Mavin RE'09) — 요구 frontmatter `pattern:` 의 값 어휘 → 개체 (ears-pattern-ontology.ttl). type: requirement 에서만 허용
EARS_PATTERNS = {
    "ubiquitous": "agt:ubiquitous",
    "event-driven": "agt:eventDriven",
    "state-driven": "agt:stateDriven",
    "unwanted-behaviour": "agt:unwantedBehaviour",
    "optional": "agt:optional",
    "complex": "agt:complex",
}
# 본문 슬롯 표지 (결정 p4-slot-answers-one-question) — 슬롯은 줄 머리 고정 표지 하나와 그것이 답하는 질문 하나다.
# 질문·순서·필수 여부의 정의처는 shape(kb/ontology/shapes/*-body-shapes.ttl)이고 여기는 표지 낱말의 정의처다 —
# 이 도구는 rdflib 없이 타깃마다 돌아 kb_lib 를 의존할 수 없으므로 값 어휘 상수가 PLANE_CLASS 와 함께 여기 있다 (STYLEGUIDE §4).
# 실물이 있는 일곱 틀의 표지만 둔다. 표지를 늘리면 shape 의 틀도 같은 커밋에서 늘린다
BODY_SLOT_MARKERS = ("요구", "이해관계자", "관심사", "출처",                    # 개발 요구 (kb/dev/requirement)
                     "결론", "근거", "대안",                                   # 결정 세 청크 (kb/dev/decision · chunks/decision)
                     "검증 목표", "무엇을 관측하면 성립하는가",                  # 검증 목표 (kb/vv/goal)
                     "합격 기준", "판정식", "확인 절차", "등급",                 # 합격 기준 (kb/vv/criteria)
                     "케이스", "자극", "기대", "실행 명령", "표본 근거")         # 케이스 (kb/vv/case)
BODY_SLOT_SPAN = re.compile(r"\*\*([^*\n]+?)\*\*")
# 줄 머리 `키워드: 값` 형 슬롯 (제안 4.1절). 지금 실물은 선택 슬롯 `미확정:` 하나다 — 미결을 문서가 아니라 항목 안에
# 두면 집계가 생성물이 된다 (p4-three-empty-values). //kg:open 이 이 표지로 미결을 모은다
BODY_SLOT_KEYWORDS = ("미확정",)
BODY_SLOT_KEYWORD = re.compile(r"^(" + "|".join(BODY_SLOT_KEYWORDS) + r"):\s")
BODY_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")  # 코드 펜스 안은 본문 형식이 아니다 — 예시 안의 표지를 슬롯으로 읽지 않는다
LEVELS = {"functional", "abstract", "logical", "concrete", "executable"}
STATES = {"draft", "stable", "suspect", "invalidated", "deprecated"}
HANGUL = re.compile(r"[ㄱ-ㆎ가-힣]")  # 한글 음절·자모 — 라벨 언어 검사 (0.6절 표기 형식)
REQUIRED = ("id", "type", "level", "title_ko", "title", "status", "generated")

PREAMBLE = """\
# 생성 파일 — 손으로 고치지 않는다. 원본은 각 청크 파일의 frontmatter다.
# 생성: tools/chunk2kg.py (bazel build //kg:chunks_kg)
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
"""


def body_slots(body: list[str]) -> list[str]:
    """본문이 쓴 슬롯 표지 — 등록된 표지(BODY_SLOT_MARKERS) 가운데 굵은 span 으로 나타난 것, 첫 등장 순서.

    표지 안의 한정어는 같은 표지로 본다. "**대안 없음**"·"**자극(분석)**" 이 그 예이고 DECISION_ROLE_MARKER 와 같은
    규칙이다 — 그것은 "대안 없음을 기록하라"는 규칙의 이행이지 표지 누락이 아니다.
    """
    seen: list[str] = []
    fence: str | None = None
    for line in body:
        m = BODY_FENCE.match(line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            continue
        if m:
            fence = m.group(1)
            continue
        kw = BODY_SLOT_KEYWORD.match(line)
        if kw and kw.group(1) not in seen:
            seen.append(kw.group(1))
        for span in BODY_SLOT_SPAN.finditer(line):
            for mark in BODY_SLOT_MARKERS:
                if span.group(1).strip().startswith(mark):
                    if mark not in seen:
                        seen.append(mark)
                    break
    return seen


def parse_chunk(path: str) -> tuple[dict, int]:
    """frontmatter dict와 본문 줄 수를 돌려준다."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: frontmatter가 없다 — 한 청크는 한 파일이고 head는 frontmatter다")
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        raise ValueError(f"{path}: frontmatter가 닫히지 않았다")

    meta: dict = {}
    for i, raw in enumerate(lines[1:end], start=2):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            raise ValueError(f"{path}:{i}: 'key: value' 형식이 아니다: {raw!r}")
        key, _, val = raw.partition(":")
        key, val = key.strip(), val.strip()
        meta[key] = parse_value(val)

    body = lines[end + 1 :]
    while body and not body[-1].strip():
        body.pop()
    while body and not body[0].strip():
        body.pop(0)
    meta["_content_hash"] = hashlib.sha256("\n".join(body).encode("utf-8")).hexdigest()[:12]
    meta["_body_slots"] = body_slots(body)  # 본문이 쓴 슬롯 표지 (결정 p4-slot-answers-one-question)

    for k in REQUIRED:
        if not meta.get(k):
            raise ValueError(f"{path}: frontmatter에 {k} 가 없다")
    if meta["type"] not in PLANE_CLASS:
        raise ValueError(f"{path}: 알 수 없는 type {meta['type']!r} — plane 이름이어야 한다")
    if meta["level"] not in LEVELS:
        raise ValueError(f"{path}: 알 수 없는 level {meta['level']!r}")
    if meta["status"] not in STATES:
        raise ValueError(f"{path}: 알 수 없는 status {meta['status']!r}")
    if "pattern" in meta:  # EARS 패턴 — 요구 문장의 형식이지 다른 plane 의 속성이 아니다 (p7-dev-plane-substance)
        if meta["type"] != "requirement":
            raise ValueError(f"{path}: pattern 은 type: requirement 에서만 쓴다 — 실제 type {meta['type']!r} (EARS 패턴은 요구 문장의 형식이다)")
        if meta["pattern"] not in EARS_PATTERNS:
            raise ValueError(f"{path}: 알 수 없는 pattern {meta['pattern']!r} — {' | '.join(EARS_PATTERNS)} 중 하나다 (EARS, Mavin RE'09)")
    if meta["status"] != "deprecated":
        for i, raw in enumerate(lines[end + 1 :], start=end + 2):
            if EPHEMERAL_PATH in raw:
                raise ValueError(f"{path}:{i}: 소멸성 채널 경로를 인용원으로 쓰지 않는다 — 규칙·근거는 영속 지식(노트·결정)에 둔다 "
                                 f"(agrtls-practices-review P): {raw.strip()[:80]}")
    if HANGUL.search(meta["title"]):
        raise ValueError(f"{path}: title {meta['title']!r} 에 한글이 있다 — 영문 라벨에 한글을 섞지 않는다(0.6절)")
    if not HANGUL.search(meta["title_ko"]):
        raise ValueError(f"{path}: title_ko {meta['title_ko']!r} 에 한글이 없다 — 라벨은 한/영 1:1, 한글 라벨은 한글로 쓴다(0.6절)")
    comp = meta.get("composite")
    if isinstance(comp, dict):  # 구조({id, title_ko, title})는 main 이 검사한다 — 여기서는 청크 라벨과 같은 언어 규칙만
        if comp.get("title") and HANGUL.search(comp["title"]):
            raise ValueError(f"{path}: composite.title {comp['title']!r} 에 한글이 있다 — 복합체 라벨도 한/영 1:1(0.6절)")
        if comp.get("title_ko") and not HANGUL.search(comp["title_ko"]):
            raise ValueError(f"{path}: composite.title_ko {comp['title_ko']!r} 에 한글이 없다 — 복합체 라벨도 한/영 1:1(0.6절)")
    gen = meta["generated"]
    if not isinstance(gen, dict) or not gen.get("by") or not gen.get("at"):
        raise ValueError(f"{path}: generated 는 {{by: …, at: …}} 여야 한다 (OKF 행위자 표기)")
    for v in meta.get("verified", []):
        if not isinstance(v, dict) or not v.get("by") or not v.get("at"):
            raise ValueError(f"{path}: verified 항목은 {{by: …, at: …}} 여야 한다")
    if SPECIALIZATION_KEY in meta:  # 분할 조각 → 원 청크 (단일 IRI). 같은 plane·실재·비순환은 묶음 전체를 아는 곳(validate·merge)이 본다
        spec = meta[SPECIALIZATION_KEY]
        if not isinstance(spec, str) or not spec:
            raise SpecializationError(f"{path}: {SPECIALIZATION_KEY} 는 원 청크 IRI 하나여야 한다 — 실제 {spec!r} (p10-split-keeps-work-identity)")
        if spec == meta["id"]:
            raise SpecializationError(f"{path}: {SPECIALIZATION_KEY} 가 자기 자신 {spec} 이다 — 조각은 다른 청크(원본)를 특수화한다")

    return meta, len(body)


def parse_map(text: str) -> dict:
    """인라인 맵 {k: v, k: v} — 값에 콤마·콜론이 없다는 전제."""
    out = {}
    for part in text.strip().strip("{}").split(","):
        if not part.strip():
            continue
        k, _, v = part.partition(":")
        out[k.strip()] = v.strip().strip("'\"")
    return out


def parse_value(val: str):
    """key: value 의 값 — 인라인 맵, 목록(스칼라 또는 맵), 스칼라."""
    if val.startswith("{") and val.endswith("}"):
        return parse_map(val)
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        if inner.startswith("{"):
            return [parse_map(m) for m in re.findall(r"\{[^{}]*\}", inner)]
        return [v.strip().strip("'\"") for v in inner.split(",") if v.strip()]
    return val.strip("'\"")


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def emit_chunk(path: str, meta: dict, line_count: int) -> str:
    stmts = [
        f"a {PLANE_CLASS[meta['type']]} , {PROFILE_SUBSTANCE[meta['type']]}",
        f'rdfs:label "{esc(meta["title"])}"@en',
        f'rdfs:label "{esc(meta["title_ko"])}"@ko',
        f"agt:hasLevel agt:{meta['level']}",
    ]
    if "pattern" in meta:
        stmts.append(f"agt:pattern {EARS_PATTERNS[meta['pattern']]}")
    stmts += [
        f"agt:lineCount {line_count}",
        *(f'agt:bodySlot "{esc(s)}"' for s in meta.get("_body_slots", [])),  # 본문 형태 — 틀의 필수 슬롯은 *-body-shapes.ttl 이 본다
        f'agt:status "{meta["status"]}"',
        f'agt:contentHash "{meta["_content_hash"]}"',
        f'agt:generatedBy "{esc(meta["generated"]["by"])}"',
        f'prov:generatedAtTime "{meta["generated"]["at"]}"^^xsd:dateTime',
        f'agt:assertionLocation "{esc(path)}"',
    ]
    for a in meta.get("assumes", []):
        stmts.append(f"agt:assumes <{a}>")
    for d in meta.get("sources", []):
        res = d.get("resource") if isinstance(d, dict) else d  # OKF: 객체 목록. 옛 문자열 목록도 읽는다
        if not res:
            raise ValueError(f"{path}: sources 항목에 resource 가 없다 (OKF v0.2 §5.1)")
        stmts.append(f"prov:wasDerivedFrom <{res}>")
    if SPECIALIZATION_KEY in meta:  # 같은 것의 다른 입도 — 출처(wasDerivedFrom)와 다르다 (p10-split-keeps-work-identity)
        stmts.append(f"prov:specializationOf <{meta[SPECIALIZATION_KEY]}>")
    for key in LINK_KEYS:  # 링크는 직접 트리플로도 낸다 — CQ-04·16·17·34 와 verify 질의(verifies-without-criteria)·metrics 가 agt:<key> 술어를 본다. 링크 개체는 emit_links
        for to in meta.get(key, []) or []:
            stmts.append(f"agt:{key} <{to}>")
    for c in meta.get("coUpdatesWith", []):  # 알고 둔 중복 — 안전율 (p4-redundancy-as-safety-margin). 대칭·relatedTo 족
        stmts.append(f"agt:coUpdatesWith <{c}>")
    for v in meta.get("verified", []):
        stmts.append(f'agt:verifiedBy "{esc(v["by"])}"')
        stmts.append(f'agt:verifiedAt "{v["at"]}"^^xsd:dateTime')

    lines = [f"<{meta['id']}>"]
    for i, s in enumerate(stmts):
        sep = " ." if i == len(stmts) - 1 else " ;"
        lines.append(f"    {s}{sep}")
    return "\n".join(lines)


LINK_KEYS = ("refines", "serves", "supersedes", "verifies", "satisfies", "constrains", "derivesFrom", "allocates", "generates")
RESTORED_KEY = "restored"  # 복원 링크의 표시 (p10-restored-link-marking) — 값은 같은 청크의 링크 키 대상 IRI 목록
RESTORED_GATE = getattr(kb_lib, "RESTORED_GATE", "restored")  # 게이트 id — FAIL [restored] (정의처 kb_lib)
ID_BASE = "https://agentic-knowledge-base.dev/id/"
# 증거 종류 — 구축(편집 부산물, 10.3절)은 구축 기록, 복원(restored: 표시 — 도구·에이전트가 제안하고 사람이 확정)은 제안 (evidence-ontology)
EVIDENCE_BUILT = "agt:constructionRecord"
EVIDENCE_RESTORED = "agt:proposal"


def link_targets(meta: dict) -> set:
    """청크가 링크 키(LINK_KEYS)로 가리키는 대상 IRI 전부 — restored: 의 IRI 는 이 안에 있어야 한다."""
    return {to for key in LINK_KEYS for to in (meta.get(key, []) or [])}


def check_restored(path: str, meta: dict) -> list:
    """restored: 검사 → 위반 메시지 목록 (게이트 id `restored`). 값은 IRI 목록이고 각 IRI 는 같은 청크의 링크 대상이어야 한다."""
    if RESTORED_KEY not in meta:
        return []
    value = meta[RESTORED_KEY]
    if not isinstance(value, list) or not all(isinstance(v, str) and v for v in value):
        return [f"{path}: {RESTORED_KEY} 는 링크 대상 IRI 목록 [<IRI>, …] 이어야 한다 — 실제 {value!r}"]
    targets = link_targets(meta)
    return [f"{path}: 복원 표시 {iri} 가 링크 대상에 없다 — {RESTORED_KEY} 의 IRI 는 같은 청크의 링크 키({'·'.join(LINK_KEYS)}) 어딘가의 대상이어야 한다 "
            f"(p10-restored-link-marking)" for iri in value if iri not in targets]


def link_hash(frm: str, kind: str, to: str) -> str:
    """링크 개체 IRI 의 해시 부분 — sha256(출발|종류|도착)[:12]. 호출자가 양 끝에 뿌리 uuid(work_id)를 넣는다. extract_refs 도 같은 함수를 쓴다."""
    return hashlib.sha256(f"{frm}|{kind}|{to}".encode("utf-8")).hexdigest()[:12]


def spec_cycles(spec: dict) -> list:
    """specializationOf 사슬(조각 → 원본)의 순환들 — 순환마다 구성원 튜플 하나(가장 작은 IRI 부터). validate check_specialization 과 같은 판정."""
    cycles, reported = [], set()
    for start in sorted(spec):
        seen, cur = [], start
        while cur in spec and cur not in seen:
            seen.append(cur)
            cur = spec[cur]
        if cur in seen:
            cyc = seen[seen.index(cur):]
            i = cyc.index(min(cyc))
            cyc = tuple(cyc[i:] + cyc[:i])
            if cyc not in reported:
                reported.add(cyc)
                cycles.append(cyc)
    return cycles


def work_id(iri: str, spec: dict) -> str:
    """뿌리 uuid(work-id) — specializationOf 사슬(spec: 조각 → 원본)을 따라 올라간 끝. 사슬이 순환하면 SpecializationError.

    대상이 spec 에 없는 IRI(사슬 밖 또는 dangling)면 거기서 멈춘다 — 실재는 validate dangling 이 본다.
    """
    seen = [iri]
    while iri in spec:
        iri = spec[iri]
        if iri in seen:
            raise SpecializationError(f"{SPECIALIZATION_KEY} 사슬이 순환한다: {' → '.join(seen + [iri])} — 조각은 원본을, 원본은 조각을 가리키지 않는다")
        seen.append(iri)
    return iri


def emit_links(meta: dict) -> list:
    """frontmatter 링크 하나 = agt:Link 개체 하나 + 증거 하나 (9.11절, 10.10절).

    링크는 청크를 저작할 때 편집 연산의 부산물로 생겼으므로(10.3절 구축) 증거 종류는 구축 기록이고,
    참조는 그 청크 자신(생성 기록 generatedBy·generatedAtTime 을 지닌다). restored: 에 적힌 대상의 링크는 복원 링크라 증거가 한 줄 더
    붙는다 — 후보의 출처 proposal(도구·에이전트가 제안하고 사람이 frontmatter 에 적어 확정, p10-restored-link-marking). 확정 기록
    constructionRecord 는 복원 링크에도 남는다: 사람이 frontmatter 에 적은 행위가 편집 시점 기록이고, 9.11절 규칙(구축(+) 또는 실행(+)
    없이 확정 불가)을 verify 질의 confirmed-without-evidence 가 강제하므로 proposal 만으로는 확정이 성립하지 않는다. 상태는 둘 다 확정이다.
    IRI 는 (출발, 종류, 도착)의 해시라 결정적이고, 제안 증거의 IRI 는 같은 해시에 접미 -proposal 이다. 여기서는 원 IRI 로 해시한다 —
    뿌리 uuid(work_id)는 묶음 전체를 알아야 하므로 rebase_links 가 --merge·단일 실행에서 다시 계산한다.
    """
    out = []
    restored = set(meta.get(RESTORED_KEY) or []) if isinstance(meta.get(RESTORED_KEY), list) else set()
    for key in LINK_KEYS:
        for to in meta.get(key, []) or []:
            h = link_hash(meta["id"], key, to)
            link = f"{ID_BASE}link/{h}"
            evidences = [(f"{ID_BASE}evidence/{h}", EVIDENCE_BUILT)]
            if to in restored:
                evidences.append((f"{ID_BASE}evidence/{h}-proposal", EVIDENCE_RESTORED))
            out.append((link, f"<{link}>\n    a agt:Link , agt:ConfirmedLink ;\n    agt:linkFrom <{meta['id']}> ;\n    agt:linkTo <{to}> ;\n"
                              f"    agt:linkKind agt:{key} ;\n    agt:linkState \"{LINK_STATE_CONFIRMED}\" ;\n    agt:hasEvidence " + " , ".join(f"<{e}>" for e, _ in evidences) + " ."))
            for ev, kind in evidences:
                out.append((ev, f"<{ev}>\n    a agt:Evidence ;\n    agt:evidenceKind {kind} ;\n    agt:evidenceRef <{meta['id']}> ;\n    agt:polarity \"+\" ."))
    return out


LINK_PREFIX = f"{ID_BASE}link/"
EVIDENCE_PREFIX = f"{ID_BASE}evidence/"
_SPEC_LINE = re.compile(r"^    prov:specializationOf <([^>]+)>", re.MULTILINE)


def is_link_block(iri: str) -> bool:
    """링크·증거 블록인가 — 청크·복합체와 달리 뿌리 uuid 로 IRI 를 다시 계산하고 같은 IRI 는 합친다."""
    return iri.startswith(LINK_PREFIX) or iri.startswith(EVIDENCE_PREFIX)


def parse_block(block: str) -> tuple:
    """emit_links 가 낸 블록 → (IRI, [(술어, [목적어…])…]). 링크·증거 블록 전용 — 목적어에 ` , ` 나 따옴표 속 콤마가 없다."""
    lines = block.split("\n")
    iri = lines[0].strip().strip("<>")
    stmts = []
    for raw in lines[1:]:
        t = raw.strip()
        if t.endswith(" ;") or t.endswith(" ."):
            t = t[:-2]
        pred, _, objs = t.partition(" ")
        stmts.append((pred, [o.strip() for o in objs.split(" , ") if o.strip()]))
    return iri, stmts


def render_block(iri: str, stmts: list) -> str:
    lines = [f"<{iri}>"]
    for i, (pred, objs) in enumerate(stmts):
        sep = " ." if i == len(stmts) - 1 else " ;"
        lines.append(f"    {pred} {' , '.join(objs)}{sep}")
    return "\n".join(lines)


def rebase_links(blocks: list, spec: dict) -> tuple:
    """(IRI, 블록) 목록의 링크·증거 블록 IRI 를 뿌리 uuid 로 다시 계산하고 같은 IRI 의 블록을 합친다 → (블록 목록, 오류 목록).

    spec 은 조각 → 원본 사상(청크 블록의 prov:specializationOf). 링크 블록의 linkFrom·linkTo 를 work_id 로 올려 link_hash 를 다시
    구하고, 해시가 바뀐 링크의 증거 IRI(같은 해시 + 접미)도 함께 바꾼다. 원본을 가리키던 링크 X→O 와 조각을 가리키는 X→F 는
    같은 IRI 가 되어 한 블록이 된다 — 술어별 목적어의 합집합(linkTo 둘, evidenceRef 둘). 청크·복합체 블록은 그대로 둔다.
    사슬 순환은 오류(게이트 id specialization, 순환마다 한 번)다. 합쳐진 블록의 목적어는 정렬 합집합이라 조각 순서와 무관하게 결정적이다.
    """
    errors = [f"{SPECIALIZATION_KEY} 사슬이 순환한다: {' → '.join(cyc + (cyc[0],))} — 조각은 원본을, 원본은 조각을 가리키지 않는다"
              for cyc in spec_cycles(spec)]  # 순환마다 한 번 — 뿌리를 계산할 수 없으므로 링크 IRI 재계산은 하지 않는다
    if errors:
        return blocks, errors
    roots: dict = {}

    def root(iri: str) -> str:
        if iri not in roots:
            roots[iri] = work_id(iri, spec)
        return roots[iri]

    remap: dict = {}
    links, evidences, rest = [], [], []
    for iri, block in blocks:
        if not is_link_block(iri):
            rest.append((iri, block))
            continue
        (links if iri.startswith(LINK_PREFIX) else evidences).append(parse_block(block))
    for iri, stmts in links:
        d = dict(stmts)
        frm, to, kind = d.get("agt:linkFrom", []), d.get("agt:linkTo", []), d.get("agt:linkKind", [""])[0]
        hashes = {link_hash(root(f.strip("<>")), kind.split(":", 1)[-1], root(t.strip("<>"))) for f in frm for t in to}
        old = iri[len(LINK_PREFIX):]
        if len(hashes) == 1 and (new := hashes.pop()) != old:
            remap[old] = new
    def rebased(iri: str) -> str:  # 링크·증거 IRI 의 해시 12자를 바꾼다 — 접미(-proposal)는 그대로
        for prefix in (LINK_PREFIX, EVIDENCE_PREFIX):
            if iri.startswith(prefix):
                old = iri[len(prefix):len(prefix) + 12]
                return prefix + remap.get(old, old) + iri[len(prefix) + 12:]
        return iri

    merged: dict = {}
    for iri, stmts in links + evidences:
        iri = rebased(iri)
        stmts = [(p, [f"<{rebased(o.strip('<>'))}>" if o.startswith("<") else o for o in objs]) for p, objs in stmts]
        if iri not in merged:
            merged[iri] = [(p, list(objs)) for p, objs in stmts]
            continue
        have = merged[iri]  # 같은 IRI 의 두 번째 블록부터 — 술어별 목적어의 정렬 합집합이라 조각 순서와 무관하게 결정적이다 (단일 실행 = 병합)
        for p, objs in stmts:
            slot = next((h for h in have if h[0] == p), None)
            if slot is None:
                have.append((p, list(objs)))
            else:
                slot[1][:] = sorted(set(slot[1]) | set(objs))
    return rest + [(iri, render_block(iri, stmts)) for iri, stmts in merged.items()], errors


def merge(out: str, fragments: list) -> int:
    """타깃별 head 조각(--fragment 출력)을 하나의 -kg 로 병합한다. IRI 중복 검사는 여기서 한다 (한 청크는 한 파일).

    링크·증거 블록은 중복 검사 대상이 아니다 — 뿌리 uuid 로 IRI 를 다시 계산하면(rebase_links) 원본과 조각을 가리키는 링크가
    같은 IRI 가 되는 것이 설계다. 조각 → 원본 사상은 청크 블록의 prov:specializationOf 에서 읽는다.
    """
    chunks, comps, seen, errors = [], [], {}, []
    spec: dict = {}
    for frag in fragments:
        try:
            text = Path(frag).read_text(encoding="utf-8").strip("\n")
        except OSError as e:
            print(f"FAIL [{TAG}-merge] {frag}: 조각을 읽을 수 없다 — {e}", file=sys.stderr)
            return EXIT_CONFIG
        for block in (b for b in text.split("\n\n") if b.strip()):
            iri = block.split("\n", 1)[0].strip("<>")
            if is_link_block(iri):
                chunks.append((iri, block))
                continue
            if iri in seen:
                errors.append(f"{frag}: IRI {iri} 가 {seen[iri]} 와 중복 — 한 청크는 한 파일이다")
                continue
            seen[iri] = frag
            m = _SPEC_LINE.search(block)
            if m:
                spec[iri] = m.group(1)
            (comps if "\n    a agt:Composite" in block else chunks).append((iri, block))
    if errors:
        for e in errors:
            print(f"FAIL [{TAG}-merge] {e}", file=sys.stderr)
        return EXIT_FAIL
    chunks, spec_errors = rebase_links(chunks, spec)
    if spec_errors:
        for e in spec_errors:
            print(f"FAIL [{SPECIALIZATION_GATE}] {e}", file=sys.stderr)
        return EXIT_FAIL
    blocks = [b for _, b in sorted(chunks)] + [b for _, b in sorted(comps)]
    Path(out).write_text(PREAMBLE + "\n" + "\n\n".join(blocks) + "\n", encoding="utf-8")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--fragment", action="store_true", help="타깃 하나의 조각 — 전문(preamble) 없이 블록만 (kb_chunk·kb_decision 액션)")
    ap.add_argument("--merge", action="store_true", help="조각들을 병합해 -kg 를 만든다 (kb_kg_merge)")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()
    if args.merge:
        return merge(args.out, args.files)

    blocks, seen = [], {}
    composites: dict = {}   # iri -> {labels, members[]}
    part_refs: list = []    # (chunk_iri, composite_iri, path)
    errors = []
    restored_errors = []    # 게이트 id `restored` — FAIL [restored] (복원 표시가 링크 대상에 없다)
    spec_errors = []        # 게이트 id `specialization` — FAIL [specialization] (자기 참조·사슬 순환)
    spec: dict = {}         # 조각 IRI → 원본 IRI — 링크 IRI 의 뿌리 계산 (단일 실행에서는 여기서, --merge 에서는 블록에서 읽는다)
    for path in sorted(args.files):
        try:
            meta, n = parse_chunk(path)
        except OSError as e:
            print(f"FAIL [{TAG}] {path}: 읽을 수 없다 — {e}", file=sys.stderr)
            return EXIT_CONFIG
        except SpecializationError as e:
            spec_errors.append(str(e))
            continue
        except ValueError as e:
            errors.append(str(e))
            continue
        if meta["id"] in seen:
            errors.append(f"{path}: IRI {meta['id']} 가 {seen[meta['id']]} 와 중복 — 한 청크는 한 파일이다")
            continue
        seen[meta["id"]] = path
        restored_errors += check_restored(path, meta)
        if SPECIALIZATION_KEY in meta:
            spec[meta["id"]] = meta[SPECIALIZATION_KEY]
        comp = meta.get("composite")
        if comp:
            if not (isinstance(comp, dict) and comp.get("id") and comp.get("title_ko") and comp.get("title")):
                errors.append(f"{path}: composite 는 {{id, title_ko, title}} 이어야 한다")
            elif comp["id"] in composites:
                errors.append(f"{path}: 복합체 {comp['id']} 가 {composites[comp['id']]['path']} 와 중복 선언됨")
            else:
                composites[comp["id"]] = {"ko": comp["title_ko"], "en": comp["title"], "members": [], "path": path}
        if meta.get("part_of"):
            part_refs.append((meta["id"], meta["part_of"], path))
        blocks.append((meta["id"], emit_chunk(path, meta, n)))
        blocks.extend(emit_links(meta))
    for chunk_iri, comp_iri, path in part_refs:
        if comp_iri not in composites:
            errors.append(f"{path}: part_of 대상 복합체 {comp_iri} 가 이 묶음 안에 선언되지 않았다")
        else:
            composites[comp_iri]["members"].append(chunk_iri)
    comp_blocks = []
    for iri, c in sorted(composites.items()):
        if not c["members"]:
            errors.append(f"{c['path']}: 복합체 {iri} 에 부분이 없다 — 멤버 청크가 part_of 로 가리켜야 한다")
            continue
        parts = " ,\n        ".join(f"<{m}>" for m in sorted(c["members"]))
        comp_blocks.append(
            f"<{iri}>\n    a agt:Composite ;\n"
            f'    rdfs:label "{esc(c["en"])}"@en ;\n'
            f'    rdfs:label "{esc(c["ko"])}"@ko ;\n'
            f"    agt:hasDirectPart {parts} ."
        )

    if not args.fragment:  # 단일 실행은 묶음 전체를 아니 뿌리 uuid 로 링크 IRI 를 계산한다 — --merge 와 같은 결과. 조각은 원 IRI 그대로
        blocks, spec_errors2 = rebase_links(blocks, spec)
        spec_errors += spec_errors2
    if errors or restored_errors or spec_errors:
        for e in errors:
            print(f"FAIL [{TAG}] {e}", file=sys.stderr)
        for e in restored_errors:
            print(f"FAIL [{RESTORED_GATE}] {e}", file=sys.stderr)
        for e in spec_errors:
            print(f"FAIL [{SPECIALIZATION_GATE}] {e}", file=sys.stderr)
        return EXIT_FAIL

    body = "\n\n".join([b for _, b in sorted(blocks)] + comp_blocks)  # 정규 순서: 청크 IRI 순, 그다음 복합체 IRI 순 — union 과 merge 가 바이트 동일
    Path(args.out).write_text((body if args.fragment else PREAMBLE + "\n" + body) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
