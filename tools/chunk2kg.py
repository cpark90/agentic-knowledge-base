#!/usr/bin/env python3
"""청크 파일 → head 그래프(-kg) 생성.

한 청크는 한 파일이다. head 메타데이터(타입·plane·level·라벨·상태·출처)는
청크 파일의 frontmatter에 있고, 본문(assertion)은 그 아래 있다 (노트 4.3절).
`-kg`의 head 그래프는 손으로 쓰지 않고 이 도구가 청크 파일들에서 생성한다 —
agt:tokenCount 와 agt:assertionLocation 은 파일에서 계산되므로 어긋날 수 없다.

frontmatter 형식은 YAML 부분집합이다 — key: value, 목록은 [a, b], 인라인 맵은 {k: v}. 키마다의 설명은
그 키를 판정·방출하는 절의 주석에 있다 — 기본 키는 `청크 파싱` 절, 링크 키는 `링크의 방출과 정체성` 절,
복합체 키는 `복합체의 순서` 절이다 (규약을 강제하는 코드 옆에 둔다).

출력·종료: 위반은 `FAIL [chunk2kg] <경로>: <메시지>` (병합은 `FAIL [chunk2kg-merge]`, 특수화 사슬은 `FAIL [specialization]`) + EXIT_FAIL,
           읽을 수 없는 입력은 EXIT_CONFIG. 생성기이므로 입력 0건은 빈 그래프(SKIP 아님).
사용: chunk2kg.py --out <생성.ttl> --residency defs/kb.bzl [--vocab <어휘 파일>] <청크 파일들...>
      (--merge 는 --residency·--vocab 없이 조각을 잇기만 한다)
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import os
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
EPHEMERAL_PATHS = ("harness/channel/", "harness/user/", "docs/feedback/")  # 소멸성 채널(에이전트 채널·유저 채널·옛 채널) — 인용원이 될 수 없다 (agrtls-practices-review P)
SPECIALIZATION_KEY = "specializationOf"  # frontmatter 키 — 분할 조각 → 원 청크 (p10-split-keeps-work-identity)
SPECIALIZATION_GATE = getattr(kb_lib, "SPECIALIZATION_GATE", "specialization")  # 게이트 id — FAIL [specialization] (정의처 kb_lib)
LINK_STATE_CANDIDATE = getattr(kb_lib, "LINK_STATE_CANDIDATE", "candidate")  # 후보 — extract_refs 가 낸다 (정의처 kb_lib)
LINK_STATE_CONFIRMED = getattr(kb_lib, "LINK_STATE_CONFIRMED", "confirmed")  # 확정 — frontmatter 링크 (정의처 kb_lib)
SPACE_GATE = getattr(kb_lib, "SPACE_GATE", "space")  # 게이트 id — FAIL [space] (정의처 kb_lib)
SPACE_TYPE = getattr(kb_lib, "SPACE_TYPE", "agt:Space")    # `-space` 청크의 type — plane 이 아니라 클래스다 (p9-candidate-storage)
SPACE_LEVEL = getattr(kb_lib, "SPACE_LEVEL", "logical")    # 후보·제약·배제 근거가 사는 수준 (6.4절 수준 허용표)


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
    "norm": "agt:DocumentSectionChunk",  # 규범 문서의 절 — 클래스 지역명이 plane 이름에서 오지 않는 유일한 plane (유저 답 Q21-a)
}
# plane 이름 → agt:...Chunk 클래스의 사상(mapping)이다. defs/kb.bzl 은 Starlark 라 클래스 이름을 모르므로 이 표는
# defs/kb.bzl 에 없고 여기가 정의처다(M1 단일 정의처, 2026-09-26 — 아래 PLANES 파생과 같은 결정). 대신 이 표의 키
# 집합은 defs/kb.bzl 의 PLANES 와 같아야 하므로 apply_plane_level_state 가 로드 시점에 단정한다.

_KB_BZL_LIST = re.compile(r"^\s*(LEVELS|PLANES|STATES)\s*=\s*(\[[^\]]*\])", re.M)  # kb_lib.load_residency 와 같은 수법


def load_plane_level_state(path) -> tuple[list[str], list[str], list[str]]:
    """`defs/kb.bzl` 의 `PLANES`·`LEVELS`·`STATES` 리터럴을 읽어 값 어휘를 선언 순서 그대로 돌려준다.

    수준 허용표(RESIDENCY)와 같은 결정(M1 단일 정의처, 2026-09-26)이다 — Starlark 는 파일을 읽지 못해 분석 시점
    판정(`_check_residency`)에 쓰이는 그 표가 원본이고, 파이썬 쪽은 `ast.literal_eval` 로 리터럴을 읽어 파생한다.
    이 도구는 rdflib 없이 타깃마다 돌아(head 액션, kb.bzl 의 kb_chunk·kb_decision) kb_lib 를 import 할 수 없으므로
    (위 try/except) 표준 라이브러리만으로 그 리터럴을 여기서 읽는다 — 리터럴 읽기 함수의 정의처는 이 도구 하나이고,
    `tools/kb_lib.py` 의 `load_residency` 는 PLANES·LEVELS 를 구할 때 이 함수를 import 해 쓴다(정의처를 하나로 모은
    형태 — `weave`·`extract_refs` 가 이 파일을 srcs 로 끌어 쓰는 것과 같은 방식). 경로가 없거나 못 읽으면
    OSError(운영체제가 낸다), 표를 못 읽으면 ValueError — 둘 다 판정 불가지 통과가 아니라 호출자가 그대로 죽는다.
    호출자는 이 결과를 **자기 상태에 반영해야만** 쓰인다 — 이 함수는 읽기만 하고 아무 전역도 바꾸지 않는다
    (chunk2kg 자신은 apply_plane_level_state 로 반영한다).
    """
    text = Path(path).read_text(encoding="utf-8")
    names = {m.group(1): ast.literal_eval(m.group(2)) for m in _KB_BZL_LIST.finditer(text)}
    missing = [w for w in ("PLANES", "LEVELS", "STATES") if w not in names]
    if missing:
        raise ValueError(f"{path}: {', '.join(missing)} 리스트를 찾을 수 없다")
    return names["PLANES"], names["LEVELS"], names["STATES"]


def apply_plane_level_state(planes: list[str], levels: list[str], states: list[str]) -> None:
    """전역 PLANES·LEVELS·STATES 를 교체하고 PLANE_CLASS 의 키 집합과 즉시 대조한다.

    이 도구가 아는 plane 이름(PLANE_CLASS 의 키)과 defs/kb.bzl 의 PLANES 가 갈리면 이 자리에서 죽는다 — 두 곳이
    말없이 갈라지는 것(anti-drift)이 판정 불가지 통과보다 나쁘다. `load_plane_level_state` 는 값을 읽기만 하므로
    반영은 항상 이 함수를 거친다 — `main()`이 `--residency` 를 받았을 때, 또는 `parse_chunk` 를 직접 부르는 다른
    도구가 자기 진입점에서 부른다(defs/knowledge.bzl 의 매크로·각 도구의 --residency 인자).
    """
    global PLANES, LEVELS, STATES
    assert set(PLANE_CLASS) == set(planes), (
        f"PLANE_CLASS 의 키 {sorted(PLANE_CLASS)} 가 defs/kb.bzl 의 PLANES {sorted(planes)} 와 다르다 — "
        f"두 곳을 같은 집합으로 맞춘다(STYLEGUIDE §7 단일 정의처)"
    )
    PLANES, LEVELS, STATES = planes, levels, states

# PLANES·LEVELS·STATES 는 여기서 기본값을 선언하지 않는다 — 자기 위치 기준 추정(예: __file__)이나 폴백은 두지 않는다
# (오케스트레이터 판정, 2026-09-27): defs/kb.bzl 을 못 찾으면 조용히 도는 것보다 즉시 죽는 것이 낫다. 이 세 이름은
# apply_plane_level_state 가 실제로 불릴 때만 생긴다 — 그전에 parse_chunk 를 부르면 NameError 로 죽는다(같은 원칙).

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
# `norm` 은 실체 클래스가 없다 — plane 클래스 agt:DocumentSectionChunk 하나로 타이핑한다 (유저 답 Q21-a, emit_chunk)
# EARS 패턴 (Mavin RE'09) — 요구 frontmatter `pattern:` 의 값 어휘 → 개체 (ears-pattern-ontology.ttl). type: requirement 에서만 허용
EARS_PATTERNS = {
    "ubiquitous": "agt:ubiquitous",
    "event-driven": "agt:eventDriven",
    "state-driven": "agt:stateDriven",
    "unwanted-behaviour": "agt:unwantedBehaviour",
    "optional": "agt:optional",
    "complex": "agt:complex",
}
# 서비스 층 (결정 p0-service-is-a-three-layer-wiki) — frontmatter `layer:` 의 값 어휘 → 개체 (layer-ontology.ttl).
# **plane과 직교하는 역할 속성이라 plane 제한이 없다** — 어느 plane 의 항목이든 세 층 중 하나의 역할을 갖는다
# (같은 plane 에 분야의 결정과 저작 규칙의 결정이 함께 있다). 명시가 없으면 LAYER_DEFAULT 를 방출한다 —
# 표시 누락이 산발로 세어지지 않아야 하므로 기본값이 그래프에 적힌다. 키의 정의처는 kb_lib 다 (EXPOSES_KEY 와 같은 형태).
LAYERS = {
    "knowledge": "agt:knowledgeLayer",
    "methodology": "agt:methodologyLayer",
    "process": "agt:processLayer",
}
LAYER_DEFAULT = "knowledge"  # 명시 없는 항목의 층 — 항목 대부분이 지식 층이다 (결정 근거)
# 주석의 닫힌 어휘 (결정 p7-commentary-form) — 정의처는 kb_lib 이고 여기는 rdflib 없이 도는 폴백이다 (LINK_STATE_* 와 같은 형태)
COMMENT_LABELS = getattr(kb_lib, "COMMENT_LABELS", ("praise", "nitpick", "suggestion", "issue", "question", "thought", "chore"))
COMMENT_DECORATIONS = getattr(kb_lib, "COMMENT_DECORATIONS", ("blocking", "non-blocking", "if-minor"))
COMMENT_RESOLUTIONS = getattr(kb_lib, "COMMENT_RESOLUTIONS", ("열림", "해소", "기각"))
COMMENT_SLOTS = getattr(kb_lib, "COMMENT_SLOTS", ("대상", "본문", "제안", "해소"))
TARGETS_KEY = "targets"  # 주석 → 대상 (agt:targets). 링크 키가 아니다 — 판단 근거는 emit_chunk 의 주석에 있다
EXPOSES_KEY = getattr(kb_lib, "EXPOSES_KEY", "exposes")            # 위험에서 파생된 항목 → 현상 (agt:exposesFactor). 링크 키가 아니다 (정의처 kb_lib)
EXPOSES_PREDICATE = getattr(kb_lib, "EXPOSES_PREDICATE", "agt:exposesFactor")
USES_KEY = getattr(kb_lib, "USES_KEY", "uses")                     # 정의 → 같은 모듈의 정의 (agt:usesDefinition). 링크 키가 아니다 (정의처 kb_lib)
USES_PREDICATE = getattr(kb_lib, "USES_PREDICATE", "agt:usesDefinition")
LAYER_KEY = getattr(kb_lib, "LAYER_KEY", "layer")                  # 항목 → 서비스 층 (agt:inLayer). 링크 키가 아니다 (정의처 kb_lib)
LAYER_PREDICATE = getattr(kb_lib, "LAYER_PREDICATE", "agt:inLayer")
# 본문 슬롯 표지 (결정 p4-slot-answers-one-question) — 슬롯은 줄 머리 고정 표지 하나와 그것이 답하는 질문 하나다.
# 질문·순서·필수 여부의 정의처는 shape(kb/ontology/shapes/*-body-shapes.ttl)이고 여기는 표지 낱말의 정의처다 —
# 이 도구는 rdflib 없이 타깃마다 돌아 kb_lib 를 의존할 수 없으므로 값 어휘 상수가 PLANE_CLASS 와 함께 여기 있다 (STYLEGUIDE §4).
# 실물이 있는 일곱 틀의 표지만 둔다. 표지를 늘리면 shape 의 틀도 같은 커밋에서 늘린다
BODY_SLOT_MARKERS = ("요구", "이해관계자", "관심사", "출처",                    # 개발 요구 (kb/dev/requirement)
                     "결론", "근거", "대안",                                   # 결정 세 청크 (kb/dev/decision · chunks/decision)
                     "규약",                                                  # 결정의 선택 넷째 청크 conventions.md (p4-convention-slot)
                     "검증 목표", "무엇을 관측하면 성립하는가",                  # 검증 목표 (kb/vv/goal)
                     "합격 기준", "판정식", "확인 절차", "등급",                 # 합격 기준 (kb/vv/criteria)
                     "케이스", "자극", "기대", "실행 명령", "표본 근거",         # 케이스 (kb/vv/case)
                     "요인", "배제 자극")                                       # 시나리오 (kb/vv/scenario) — 자극은 위에 이미 있다
# 시나리오의 세 표지(자극·요인·배제 자극)는 결정의 세 슬롯(결론·근거·대안)에 **사상**된다 (결정 p8-scenario-authoring,
# kb_lib.SCENARIO_ROLE_TO_DECISION_SLOT). 새 틀이 아니라 결정 틀의 표지 낱말이 갈린 것이므로 shape 도
# decision-body-shapes.ttl 의 sh:or 에 대안 셋으로 들어간다. `자극` 은 케이스 틀이 이미 쓰는 표지라 여기 한 번만 적는다.
BODY_SLOT_SPAN = re.compile(r"\*\*([^*\n]+?)\*\*")
# 표지는 **자리**로 판정한다(2026-09-29 실측 — 본문 중간의 강조가 표지로 잘못 잡히는 오탐 4건: d-0134·p8-scenario-authoring·
# p8-simulation-credibility·p8-two-verification-targets). 굵은 span 이 슬롯이려면 그 줄에서 "필드 자리"에 있어야 한다 —
# 자리는 줄 머리(불릿 `- ` 다음)이거나, 같은 줄에서 이미 읽은 필드 뒤의 ` · ` 구분자 다음이다. 표 셀(`| `)·산문 접속사
# 뒤·목록 항목 전체를 감싼 굵기는 자리가 아니다 — `chunk_lint`의 `decision-role`이 이미 같은 판정("본문 첫 산문 줄이
# 굵은 표지로 시작")을 쓰므로 방출도 그것과 같게 맞춘다. 표지 뒤에 오는 한정어(`대안 없음`)는 같은 표지이지만 그
# 한정어가 문장 하나만큼 길면(마침표를 포함하거나 BODY_SLOT_QUALIFIER_MAX 를 넘으면) 한정어가 아니라 표지 낱말로
# 시작하는 별개의 문장이다 — "요인 분류가 환경 배정을 결정한다."가 그 예다.
BODY_SLOT_BULLET = re.compile(r"^\s*-\s+")  # 목록 항목의 머리 — 이 뒤가 첫 필드의 자리다
BODY_SLOT_FIELD_SEP = " · "  # 한 줄에 여러 필드를 담을 때(요구·검증 목표의 이해관계자·관심사)의 구분자
BODY_SLOT_QUALIFIER_MAX = 12  # 표지 뒤 한정어의 최대 길이 — 넘으면 한정어가 아니라 문장이다


# ══ 청크 — 어휘·파싱·방출 ════════════════════
# 청크 파일 하나를 읽어 head 블록 하나를 내기까지의 장이다 — plane·슬롯·복합체·절 키의 어휘, frontmatter 파싱, 트리플 방출.

# ── plane 클래스의 역 사상 ────────────────────
# 클래스 지역명 → plane 이름 — PLANE_CLASS 의 역이다. 그래프에서 plane 을 읽는 도구(metrics·weave·workset·community·
# open_questions·validate)가 `<X>Chunk` 의 접두를 소문자로 바꿔 plane 을 얻던 규칙은 `norm` 에서 깨진다 — 그 plane 의
# 클래스는 `agt:DocumentSectionChunk` 다(p12-norm-documents-from-section-chunks). 역 사상의 정의처를 여기 하나로 둔다.
CLASS_PLANE = {cls.split(":", 1)[1]: plane for plane, cls in PLANE_CLASS.items()}


def plane_of_class(cls) -> str:
    """plane 청크 클래스(IRI·`agt:` 접두 이름·지역명) → plane 이름. plane 청크 클래스가 아니면 빈 문자열이다."""
    name = str(cls).rsplit("/", 1)[-1].rsplit(":", 1)[-1]
    return CLASS_PLANE.get(name, "")


# ── 본문 슬롯 표지의 자리 ────────────────────

def _body_slot_at_field_head(line: str, start: int) -> bool:
    """`start` 위치의 굵은 span 이 그 줄의 "필드 자리"에 있는가 — 줄 머리(불릿 다음) 또는 앞선 필드의
    ` · ` 구분자 다음. 표 셀·산문 접속·목록 항목 전체를 감싼 굵기는 이 자리가 아니다(위 BODY_SLOT_SPAN 주석)."""
    prefix = BODY_SLOT_BULLET.sub("", line[:start], count=1)
    while True:
        idx = prefix.find(BODY_SLOT_FIELD_SEP)
        if idx == -1:
            break
        prefix = prefix[idx + len(BODY_SLOT_FIELD_SEP):]
    return prefix.strip() == ""
# 줄 머리 `키워드: 값` 형 슬롯 (제안 4.1절). 선택 슬롯 `미확정:` 은 미결을 문서가 아니라 항목 안에 두어 집계를 생성물로
# 만든다 (p4-three-empty-values) — //kg:open 이 이 표지로 미결을 모은다. 줄 `규약:` 은 결정의 선택 넷째 청크 `conventions.md`
# 가 규범 문서에 싣는 문장 하나다 (p4-convention-slot, 유저 답 Q13-a·Q22-b) — 그 청크 한정은 convention-slot-shapes 가 본다.
# 같은 청크의 역할 표지 `**규약**` 도 같은 값 "규약" 으로 나간다(BODY_SLOT_MARKERS). 줄 `규약:` 은 목록 항목이 아니라 슬롯이다.
# 나머지 넷은 주석의 슬롯이다 (p7-commentary-form).
# 첫 줄 `<라벨> (<장식>): <요지>` 는 표지가 아니라 형식 검사 대상이라 여기 없다 — comment_form 이 읽는다.
# **표지를 늘리면 shape(kb/ontology/shapes/*-body-shapes.ttl)의 틀도 같은 커밋에서 늘린다** — 표지만 늘리면 방출은
# 바뀌는데 강제하는 곳이 없어 틀이 거짓이 된다
BODY_SLOT_KEYWORDS = ("미확정", "규약", *COMMENT_SLOTS)
BODY_SLOT_KEYWORD = re.compile(r"^(" + "|".join(BODY_SLOT_KEYWORDS) + r"):\s")
BODY_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")  # 코드 펜스 안은 본문 형식이 아니다 — 예시 안의 표지를 슬롯으로 읽지 않는다
# ── 복합체의 순서 (결정 p4-composite-order-is-declared, 유저 승인 2026-09-29 — 예외 없음) ─────────────────
# frontmatter 의 **복합체 키**와 순서의 선언 — 이 절이 판정하는 것이다.
#   part_of:      소속 복합체 IRI (선택) — 복합체는 멤버 중 하나가 composite: 로 선언
#   composite:    {id: …, title_ko: …, title: …, ordered: [<부분 IRI>…], part_of: <상위 복합체 IRI>} (선택) — 복합체 개체 선언.
#                 `part_of` 는 선택 키이며 **선언된 복합체**가 다른 복합체의 직접 부분임을 적는다 (p4-composite-as-part-of —
#                 복합체는 청크 또는 다른 복합체를 부분으로 갖는다). 청크의 최상위 `part_of` 와 자리가 다르다: 앞은 청크의
#                 소속, 뒤는 복합체의 소속이다. 상위 복합체도 같은 실행의 입력 집합 안에서 선언돼야 하고 사슬은 순환하지
#                 않는다. 코드 추출(p7-code-links-on-file-composite)의 파일 → 장·절 → 함수 세 단이 이 키로 선다. `ordered` 는 선택 키이고
#                 순서가 뜻을 갖는 복합체만 적는다 (결정 p4-composite-order-is-declared). 있으면 `agt:Composite , co:List` 로
#                 타이핑하고 부분마다 `co:item [ a co:ListItem ; co:index "<1..n>"^^xsd:positiveInteger ; co:itemContent <부분> ]`
#                 을 그 순서로 낸다. 없으면 `agt:hasDirectPart` 만 낸다(순서 없음) — 순서를 요구하지 않는 것에 순서를 붙이면
#                 거짓 정보다. 목록이 부분 전부를 빠짐없이 한 번씩 담지 않으면 거부한다. **예외는 없다** — 결정 복합체도 선언으로만
#                 순서를 갖고(유저 승인 2026-09-29) 그 선언은 `--ordered` 인자로 들어온다. 이 도구는 역할 이름으로 순서를 추측하지 않는다.
#                 **묶음의 단위는 파일이 아니라 이 실행의 입력 집합**이다 (2026-09-26 반영). part_of 대상은 같은 실행의 파일 어딘가에서
#                 composite: 로 선언돼야 한다. 그 입력 집합을 만드는 것이 defs/kb.bzl 의 kb_decision(결론·근거·대안 셋)과
#                 kb_composite(부분 2~9 가변)이고, 청크 하나만 받는 kb_chunk 로는 복합체가 서지 않는다
#   --ordered:    묶음의 복합체가 선언한 부분의 순서 (인자, 선택) — 생성 BUILD 의 `kb_decision.ordered`·`kb_composite.ordered` 가 넘긴다.
#                 결정 복합체 205개의 선언이 이 자리다 (유저 승인 2026-09-29: 예외 없음, 손으로 frontmatter 를 고치지 않는다).
#                 frontmatter `composite.ordered` 와 함께 있으면 같아야 한다 — BUILD 는 뷰이고 frontmatter 가 원본이다
# 순서는 **선언**이다. 선언이 있을 때만 co:List 와 co:index 를 방출하고, 없으면 hasDirectPart 만 낸다(순서 없음) —
# 순서를 요구하지 않는 것에 순서를 붙이면 거짓 정보다(d-0073). 목록은 부분 전부를 빠짐없이 한 번씩 담아야 하고
# 어긋나면 이 게이트가 거부한다. **도구는 역할 이름·파일 stem 으로 순서를 추측하지 않는다** — 추측 갈래는 유저 판정
# (2026-09-29, 선택지 2)으로 삭제됐다. 결정 복합체 205개도 예외가 아니고 선언을 gen_build 가 생성 BUILD 의 명시 인자
# (`kb_decision.ordered`)로 넣어 `--ordered` 로 이 도구에 들어온다 — 손으로 205개 frontmatter 를 고치는 것이 첨가이기 때문이다.
# 선언의 자리는 둘이고 둘 다 명시다: 저작한 복합체는 frontmatter `composite.ordered`, 생성된 결정 복합체는 `--ordered` 인자다.
# 둘이 함께 있으면 같아야 한다 — 생성 BUILD 는 뷰이고 frontmatter 가 원본이므로 불일치는 드리프트다.
# hasDirectPart 는 순서와 무관하게 IRI 순으로 낸다 — community·weave·audit 이 그 술어를 읽고 순서 트리플은 추가일 뿐이다.
ORDERED_KEY = "ordered"
# 복합체가 다른 복합체의 부분이 되는 자리 (p4-composite-as-part-of "복합체는 청크 또는 다른 복합체를 부분으로 갖는다").
# 청크의 최상위 `part_of` 는 그 청크가 어느 복합체의 부분인가이고, `composite.part_of` 는 **선언된 복합체**가 어느
# 복합체의 부분인가다. 코드의 추출(p7-code-links-on-file-composite)이 이 자리를 처음 쓴다 — 파일 복합체 → 장·절
# 복합체 → 함수 청크의 세 단은 부분 상한 9(4.5절) 안에서 파일 하나를 담는 유일한 형태다.
PART_OF_KEY = "part_of"


def order_errors(where: str, order, source: str) -> list:
    """순서 목록 자체의 형 검사 — 목록인가·빈 문자열이 없는가·중복이 없는가. 부분 집합과의 일치는 묶음 전체를 아는 곳이 본다."""
    if not isinstance(order, list) or not all(isinstance(o, str) and o for o in order):
        return [f"{where}: {source} 는 부분 IRI 목록 [<IRI>, …] 이어야 한다 — 실제 {order!r} (p4-composite-order-is-declared)"]
    dups = sorted({o for o in order if order.count(o) > 1})
    return [f"{where}: {source} 에 같은 부분이 두 번 있다 — 부분마다 색인 하나다: {dups}"] if dups else []
# ── 규범 문서의 절 (결정 p12-norm-documents-from-section-chunks, 유저 답 Q19-b·Q21-a·Q22-b) ─────────────────
# frontmatter 의 **절 키** — `type: norm` 에서만 쓴다. 문서 하나가 `kb/dev/norm/<문서 stem>/` 의 복합체 하나이고 순서는
# 선언 청크(머리 청크)의 `composite.ordered` 다. 머리 청크의 본문은 문서 도입문·범례이고 절 키를 갖지 않는다.
#   heading:   절 제목 (머리 청크 밖에서 필수). 번호를 두지 않는다 — 번호는 생성기(tools/gen_norms.py)가 순서로 붙인다
#   depth:     2 또는 3 (머리 청크 밖에서 필수) — 생성 문서의 `##`·`###`
#   items:     순서 목록 (선택). 항목은 셋 중 하나다 — `slug#k` · `slug#k + slug2`(둘째 결정은 링크만) ·
#              `{규약: slug#k, 하위: [slug#k, …]}`. `slug` 는 결정 디렉토리 이름, `k` 는 그 결정의 `conventions.md` 안
#              `규약:` 줄의 1부터의 순번이다. 결정 복합체로의 `agt:projectsConvention` 이 여기서 나온다
#   numbered:  true | false (선택, 절 청크만, 기본 true) — false 면 생성기가 이 depth 2 절에 번호를 붙이지 않고 번호를 소비하지도
#              않는다(문서 끝의 `셀프체크` 같은 부록 절). depth 3 절에서는 뜻이 없어 거부한다
#   numbering: 첫 depth 2 절의 번호 꼴 (선택, 머리 청크만) — `§0.` · `1.` · `0.` 처럼 접두·첫 수·마침표. 없으면 번호가 없다
#   strength:  required | optional (선택, 머리 청크만, 기본 required) — required 면 이 문서가 싣는 `규약:` 줄은 전부
#              `[지킴]`·`[권장]` 강도를 가져야 한다(생성기가 거부한다). 표 절의 줄은 예외 없이 강도를 갖지 않는다
# 절 청크 하나는 항목 묶음 하나(목록 하나 또는 표 하나)를 갖고 본문은 그 묶음 **앞**의 산문이다. 묶음의 꼴은 다음 키가 정한다.
#   form:        bullets | ordered | table (선택, 절 청크만, 기본 bullets, items 가 있을 때만) — ordered 는 항목마다 `1.` 을 낸다
#   columns:     [열 머리, …] (form: table 일 때만, 그때 필수) — 비지 않은 서로 다른 문자열
#   link_column: 열 머리 (선택, columns 가 있을 때만) — columns 의 마지막 원소여야 한다. 그 열의 칸은 생성기가 항목의
#                `slug#k + slug2` 에서 결정 링크로 낸다. 없으면 생성기가 표 바로 앞에 `원본: …` 한 줄을 낸다
#   continues:   true | false (선택, 절 청크만, 기본 false) — true 면 heading·depth·numbered 가 없는 **이어짐 절 청크**다.
#                본문은 앞 묶음 뒤의 산문이고 자기 묶음을 가질 수 있다. 깊이는 앞 절을 잇고 번호를 소비하지 않는다.
#                문서의 첫 절에는 둘 수 없다(순서를 아는 생성기가 판정한다). 그래프에는 agt:sectionContinues true 로 낸다
# 표 절의 `규약:` 줄은 `a | b | c` 꼴이다(바깥 파이프 없음, 링크 열 제외). 칸 수·강도는 생성기가 판정한다.
# 줄의 실재·고아·이중 소비는 문서 전체와 결정 전체를 아는 생성기가 판정한다 — 이 도구는 형식만 본다.
NORM_TYPE = "norm"
NORM_HEADING_KEY, NORM_DEPTH_KEY, NORM_ITEMS_KEY = "heading", "depth", "items"
NORM_NUMBERING_KEY, NORM_STRENGTH_KEY, NORM_NUMBERED_KEY = "numbering", "strength", "numbered"
NORM_FORM_KEY, NORM_COLUMNS_KEY, NORM_LINK_COLUMN_KEY, NORM_CONTINUES_KEY = "form", "columns", "link_column", "continues"
NORM_SECTION_KEYS = (NORM_HEADING_KEY, NORM_DEPTH_KEY, NORM_ITEMS_KEY, NORM_NUMBERED_KEY,  # 절 청크의 키 — 머리 청크는 갖지 않는다
                     NORM_FORM_KEY, NORM_COLUMNS_KEY, NORM_LINK_COLUMN_KEY, NORM_CONTINUES_KEY)
NORM_HEAD_KEYS = (NORM_NUMBERING_KEY, NORM_STRENGTH_KEY)                  # 머리 청크(복합체 선언)만의 키
NORM_DEPTHS = ("2", "3")
NORM_STRENGTHS = ("required", "optional")
NORM_NUMBERED_VALUES = ("true", "false")  # frontmatter 값은 문자열로 읽힌다(parse_value) — 기본 true
NORM_FORMS = ("bullets", "ordered", "table")  # 항목 묶음의 꼴 — 기본 bullets
NORM_FORM_DEFAULT, NORM_FORM_TABLE = "bullets", "table"
NORM_CONTINUES_VALUES = ("true", "false")  # 기본 false
NORM_ITEM_MAIN, NORM_ITEM_SUB = "규약", "하위"  # 하위 항목을 가진 항목의 맵 키
NORM_REF = re.compile(r"^([a-z0-9][a-z0-9-]*)#([1-9][0-9]*)$")  # `slug#k`
NORM_SLUG = re.compile(r"^[a-z0-9][a-z0-9-]*$")
NORM_NUMBERING = re.compile(r"^(\D*?)([0-9]+)\.$")  # 접두(§ 등) + 첫 번호 + 마침표
NORM_HEADING_NUMBERED = re.compile(r"^(§|[0-9]+\.)")  # 손 번호 — 번호는 생성기가 붙인다
# 결정 복합체 → 절 청크의 규약 줄 투영 술어 (norm-section-ontology.ttl). 대상 IRI 는 `--convention-target slug=IRI` 로 받는다
PROJECTS_CONVENTION_PREDICATE = "agt:projectsConvention"


def parse_norm_ref(where: str, text) -> tuple[tuple[str, int], list[str]]:
    """항목 문자열 `slug#k` 또는 `slug#k + slug2 + …` → ((slug, k), [링크만 하는 결정 slug…]). 형식 밖이면 ValueError."""
    if not isinstance(text, str):
        raise ValueError(f"{where}: items 의 항목 {text!r} 는 `slug#k` 꼴의 문자열이어야 한다 (p12-norm-documents-from-section-chunks)")
    head, *extras = [t.strip() for t in text.split("+")]
    m = NORM_REF.match(head)
    if not m:
        raise ValueError(f"{where}: items 의 항목 {text!r} 가 `slug#k` 로 시작하지 않는다 — slug 는 결정 디렉토리 이름, "
                         f"k 는 그 결정의 conventions.md 안 `규약:` 줄의 1부터의 순번이다 (p4-convention-slot)")
    bad = [e for e in extras if not NORM_SLUG.match(e)]
    if bad:
        raise ValueError(f"{where}: items 의 항목 {text!r} 의 `+` 뒤 {bad!r} 는 결정 slug 하나여야 한다 — 둘째 결정은 링크만이다")
    return (m.group(1), int(m.group(2))), extras


def parse_norm_items(where: str, items) -> list[dict]:
    """절 청크의 `items` → [{ref: (slug, k), links: [slug…], sub: [{ref, links}…]}]. 형식 밖이면 ValueError.

    판정의 단일 정의처다 — chunk2kg 의 방출(agt:projectsConvention)과 생성기(tools/gen_norms.py)가 같은 함수를 쓴다.
    """
    if not isinstance(items, list):
        raise ValueError(f"{where}: {NORM_ITEMS_KEY} 는 순서 목록 [..] 이어야 한다 — 실제 {items!r}")
    out = []
    for it in items:
        if isinstance(it, dict):
            if set(it) != {NORM_ITEM_MAIN, NORM_ITEM_SUB}:
                raise ValueError(f"{where}: 하위를 가진 항목은 {{{NORM_ITEM_MAIN}: slug#k, {NORM_ITEM_SUB}: [slug#k, …]}} 이다 — "
                                 f"실제 키 {sorted(it)}")
            ref, links = parse_norm_ref(where, it[NORM_ITEM_MAIN])
            subs = it[NORM_ITEM_SUB]
            if not isinstance(subs, list) or not subs:
                raise ValueError(f"{where}: {NORM_ITEM_SUB} 는 비지 않은 목록 [slug#k, …] 이다 — 실제 {subs!r}")
            out.append({"ref": ref, "links": links,
                        "sub": [dict(zip(("ref", "links"), parse_norm_ref(where, x))) for x in subs]})
        else:
            ref, links = parse_norm_ref(where, it)
            out.append({"ref": ref, "links": links, "sub": []})
    return out


def norm_item_slugs(parsed: list[dict], links: bool = True) -> list[str]:
    """항목이 가리키는 결정 slug — 정렬, 중복 없음. `links` 가 거짓이면 줄을 싣는 결정만이다(링크만 하는 `+ slug2` 를 뺀다).

    줄을 싣는 결정이 agt:projectsConvention 의 대상이다 — 링크만 하는 결정은 그 절에 문장을 싣지 않는다.
    """
    out = set()
    for it in parsed:
        for x in [it] + it["sub"]:
            out.add(x["ref"][0])
            if links:
                out.update(x["links"])
    return sorted(out)


def check_norm_keys(path: str, meta: dict) -> None:
    """절 키의 형식 — plane 제한과 값의 꼴. 머리 청크·절 청크의 구분(선언 여부)은 묶음 전체를 아는 main 이 본다."""
    keys = [k for k in NORM_SECTION_KEYS + NORM_HEAD_KEYS if k in meta]
    if meta["type"] != NORM_TYPE:
        if keys:
            raise ValueError(f"{path}: {', '.join(keys)} 는 type: {NORM_TYPE} 에서만 쓴다 — 실제 type {meta['type']!r} "
                             f"(절 키, p12-norm-documents-from-section-chunks)")
        return
    if NORM_HEADING_KEY in meta:
        h = meta[NORM_HEADING_KEY]
        if not isinstance(h, str) or not h.strip():
            raise ValueError(f"{path}: {NORM_HEADING_KEY} 는 비지 않은 절 제목 문자열이다")
        if NORM_HEADING_NUMBERED.match(h.strip()):
            raise ValueError(f"{path}: {NORM_HEADING_KEY} {h!r} 에 번호가 있다 — 절 번호는 생성기가 순서로 붙이고 소스에 두지 않는다")
    if NORM_DEPTH_KEY in meta and meta[NORM_DEPTH_KEY] not in NORM_DEPTHS:
        raise ValueError(f"{path}: {NORM_DEPTH_KEY} 는 {' 또는 '.join(NORM_DEPTHS)} 이다 — 실제 {meta[NORM_DEPTH_KEY]!r}")
    if NORM_NUMBERED_KEY in meta:
        if meta[NORM_NUMBERED_KEY] not in NORM_NUMBERED_VALUES:
            raise ValueError(f"{path}: {NORM_NUMBERED_KEY} 는 {' | '.join(NORM_NUMBERED_VALUES)} 중 하나다(기본 true) — "
                             f"실제 {meta[NORM_NUMBERED_KEY]!r}")
        if meta.get(NORM_DEPTH_KEY) != "2":
            raise ValueError(f"{path}: {NORM_NUMBERED_KEY} 는 depth 2 절에서만 쓴다 — 번호는 depth 2 절에만 붙는다 "
                             f"(실제 depth {meta.get(NORM_DEPTH_KEY)!r})")
    if NORM_ITEMS_KEY in meta:
        meta["_norm_items"] = parse_norm_items(path, meta[NORM_ITEMS_KEY])
    check_norm_bundle_form(path, meta)
    if NORM_NUMBERING_KEY in meta and not NORM_NUMBERING.match(str(meta[NORM_NUMBERING_KEY])):
        raise ValueError(f"{path}: {NORM_NUMBERING_KEY} 는 첫 절 번호의 꼴(`§0.` · `1.` · `0.`)이다 — 실제 {meta[NORM_NUMBERING_KEY]!r}")
    if NORM_STRENGTH_KEY in meta and meta[NORM_STRENGTH_KEY] not in NORM_STRENGTHS:
        raise ValueError(f"{path}: {NORM_STRENGTH_KEY} 는 {' | '.join(NORM_STRENGTHS)} 중 하나다 — 실제 {meta[NORM_STRENGTH_KEY]!r}")


def check_norm_bundle_form(path: str, meta: dict) -> None:
    """묶음의 꼴(form·columns·link_column)과 이어짐(continues)의 형식 — 한 청크 안에서 판정되는 것만 본다.

    칸 수·표 줄의 강도·첫 절의 이어짐은 결정의 줄과 문서의 순서를 아는 생성기(tools/gen_norms.py)가 판정한다.
    """
    if NORM_CONTINUES_KEY in meta:
        if meta[NORM_CONTINUES_KEY] not in NORM_CONTINUES_VALUES:
            raise ValueError(f"{path}: {NORM_CONTINUES_KEY} 는 {' | '.join(NORM_CONTINUES_VALUES)} 중 하나다(기본 false) — "
                             f"실제 {meta[NORM_CONTINUES_KEY]!r}")
        if meta[NORM_CONTINUES_KEY] == "true":
            have = [k for k in (NORM_HEADING_KEY, NORM_DEPTH_KEY, NORM_NUMBERED_KEY) if k in meta]
            if have:
                raise ValueError(f"{path}: 이어짐 절 청크({NORM_CONTINUES_KEY}: true)는 {', '.join(have)} 를 갖지 않는다 — "
                                 f"제목이 없고 깊이는 앞 절을 잇는다")
    form = meta.get(NORM_FORM_KEY, NORM_FORM_DEFAULT)
    if form not in NORM_FORMS:
        raise ValueError(f"{path}: {NORM_FORM_KEY} 는 {' | '.join(NORM_FORMS)} 중 하나다(기본 {NORM_FORM_DEFAULT}) — 실제 {form!r}")
    if NORM_FORM_KEY in meta and NORM_ITEMS_KEY not in meta:
        raise ValueError(f"{path}: {NORM_FORM_KEY} 는 {NORM_ITEMS_KEY} 가 있는 절에서만 쓴다 — 꼴은 항목 묶음의 꼴이다")
    cols = meta.get(NORM_COLUMNS_KEY)
    if form != NORM_FORM_TABLE:
        bad = [k for k in (NORM_COLUMNS_KEY, NORM_LINK_COLUMN_KEY) if k in meta]
        if bad:
            raise ValueError(f"{path}: {', '.join(bad)} 는 {NORM_FORM_KEY}: {NORM_FORM_TABLE} 에서만 쓴다 — 실제 {NORM_FORM_KEY} {form!r}")
        return
    if not isinstance(cols, list) or not cols or not all(isinstance(c, str) and c.strip() for c in cols) \
            or len(set(cols)) != len(cols) or any("|" in c for c in cols):
        raise ValueError(f"{path}: {NORM_FORM_KEY}: {NORM_FORM_TABLE} 는 {NORM_COLUMNS_KEY}: [열 머리, …] 를 갖는다 — 비지 않고 서로 "
                         f"다르며 `|` 가 없는 문자열의 목록이다. 실제 {cols!r}")
    if NORM_LINK_COLUMN_KEY in meta:
        if meta[NORM_LINK_COLUMN_KEY] != cols[-1]:
            raise ValueError(f"{path}: {NORM_LINK_COLUMN_KEY} {meta[NORM_LINK_COLUMN_KEY]!r} 는 {NORM_COLUMNS_KEY} 의 마지막 원소 "
                             f"{cols[-1]!r} 여야 한다 — 링크 열은 표의 끝 열이다")
        if len(cols) < 2:
            raise ValueError(f"{path}: {NORM_LINK_COLUMN_KEY} 를 둔 표는 링크 열 밖의 열을 하나 이상 갖는다 — 실제 {cols!r}")
    for it in meta.get("_norm_items") or []:
        if it["sub"]:
            raise ValueError(f"{path}: 표 절({NORM_FORM_KEY}: {NORM_FORM_TABLE})의 항목은 하위를 갖지 않는다 — 행 하나가 줄 하나다")


def norm_bundle_errors(declarer: dict, members: list[tuple[dict, str]]) -> list[str]:
    """한 문서(복합체)의 절 청크 구분 — 머리 청크(선언)는 절 키가 없고 그 밖의 부분은 heading·depth 를 갖는다.

    `declarer` 는 선언 청크의 메타(경로는 `_path`), `members` 는 (메타, 경로) 목록이다. 머리 청크만의 키(numbering·strength)가
    절 청크에 있어도 거부한다 — 문서 하나에 값 하나다. 묶음 복합체(문서 복합체 아래의 중첩)는 머리 청크가 없다 — `declarer` 가
    None 이면 부분 전부(선언한 첫 절 청크 포함)를 절 청크로 본다.
    """
    errors = []
    dpath = (declarer or {}).get("_path", "")
    for k in NORM_SECTION_KEYS if declarer is not None else ():
        if k in declarer:
            errors.append(f"{dpath}: 머리 청크(composite: 선언)는 {k} 를 갖지 않는다 — 본문이 문서 도입문·범례이고 절은 다른 청크다 "
                          f"(p12-norm-documents-from-section-chunks)")
    for meta, path in members:
        if meta is declarer or meta.get("type") != NORM_TYPE:
            continue
        if meta.get(NORM_CONTINUES_KEY) == "true":  # 이어짐 절 청크 — 제목·깊이가 없다(check_norm_bundle_form)
            continue
        for k in (NORM_HEADING_KEY, NORM_DEPTH_KEY):
            if k not in meta:
                errors.append(f"{path}: 절 청크에 {k} 가 없다 — 머리 청크 밖의 절 청크는 heading·depth 를 갖는다"
                              f"(이어짐 절 청크 {NORM_CONTINUES_KEY}: true 만 예외다)")
        for k in NORM_HEAD_KEYS:
            if k in meta:
                errors.append(f"{path}: {k} 는 머리 청크(composite: 선언)만의 키다 — 문서 하나에 값 하나다")
    return errors


# LEVELS·STATES(값 어휘)는 위에서 defs/kb.bzl 에서 파생된다(load_plane_level_state) — 여기서 다시 선언하지 않는다.
HANGUL = re.compile(r"[ㄱ-ㆎ가-힣]")  # 한글 음절·자모 — 라벨 언어 검사 (0.6절 표기 형식)
REQUIRED = ("id", "type", "level", "title_ko", "title", "status", "generated")

PREAMBLE = """\
# 생성 파일 — 손으로 고치지 않는다. 원본은 각 청크 파일의 frontmatter다.
# 생성: tools/chunk2kg.py (bazel build //kg:chunks_kg)
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
@prefix co: <http://purl.org/co/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
"""


# ── 본문 슬롯과 주석 형식 ────────────────────

def body_slots(body: list[str]) -> list[str]:
    """본문이 쓴 슬롯 표지 — 등록된 표지(BODY_SLOT_MARKERS) 가운데 굵은 span 으로 나타난 것, 첫 등장 순서.

    표지는 **자리**로 판정한다(2026-09-29, BODY_SLOT_SPAN 주석) — 굵은 span 이 그 줄의 필드 자리
    (`_body_slot_at_field_head`: 줄 머리·불릿 다음·앞선 필드의 ` · ` 다음)에 있어야 슬롯이다. 문장 중간·표
    셀·목록 항목 전체를 감싼 굵기는 강조이지 표지가 아니다.

    표지 안의 한정어는 같은 표지로 본다. "**대안 없음**"·"**자극(분석)**" 이 그 예이고 DECISION_ROLE_MARKER 와 같은
    규칙이다 — 그것은 "대안 없음을 기록하라"는 규칙의 이행이지 표지 누락이 아니다. 한정어는 짧아야 한다
    (BODY_SLOT_QUALIFIER_MAX, 마침표 없음) — 길거나 마침표가 있으면 한정어가 아니라 표지 낱말로 시작하는
    별개의 문장이다("요인 분류가 환경 배정을 결정한다."가 그 예 — 표지가 아니다).
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
            cand = span.group(1).strip()
            for mark in BODY_SLOT_MARKERS:
                if not cand.startswith(mark):
                    continue
                if not _body_slot_at_field_head(line, span.start()):
                    break
                qualifier = cand[len(mark):]
                if len(qualifier) > BODY_SLOT_QUALIFIER_MAX or "." in qualifier:
                    break
                if mark not in seen:
                    seen.append(mark)
                break
    return seen


def _alt(words) -> str:
    """정규식 대안 — 긴 낱말을 앞에 둔다 (`non-blocking` 이 `blocking` 에 가려지지 않게)."""
    return "|".join(re.escape(w) for w in sorted(words, key=len, reverse=True))


COMMENT_HEAD = re.compile(r"^(" + _alt(COMMENT_LABELS) + r")\s*\((" + _alt(COMMENT_DECORATIONS) + r")\)\s*:\s*(\S.*)$")
COMMENT_RESOLUTION = re.compile(r"^(" + _alt(COMMENT_RESOLUTIONS) + r")(?=$|[\s—.,])")  # 해소 슬롯의 첫 낱말 — 뒤는 한 줄 이유다
COMMENT_SLOT_HEAD = re.compile(r"^(" + _alt(COMMENT_SLOTS) + r")\s*:\s*(.*)$")
COMMENT_IRI = re.compile(r"https?://\S+?(?=[\s,)\]`]|$)")
COMMENT_CODE_SPAN = re.compile(r"`[^`]*`")
COMMENT_SENTENCE_END = re.compile(r"[.!?](?=\s|$)")  # 문장 끝 — 코드 스팬·IRI 를 지운 뒤 센다 (`4.1절` 의 마침표는 세지 않는다)


def count_sentences(text: str) -> int:
    """문장 수 — 코드 스팬과 IRI 를 지운 뒤 공백·줄끝 앞의 종결 부호를 센다. 주석 본문의 상한(4)을 재는 자다."""
    return len(COMMENT_SENTENCE_END.findall(COMMENT_IRI.sub(" ", COMMENT_CODE_SPAN.sub(" ", text))))


def comment_form(body: list[str]) -> dict:
    """주석 본문 → {label, decoration, gist, resolution, sentences, targets} (찾은 것만) — 결정 p7-commentary-form.

    첫 산문 줄이 `<라벨> (<장식>): <요지>` 이고 이어서 줄 머리 슬롯이 온다. 없는 것은 넣지 않는다 — 방출이 비면
    shape(review-comment-body-shapes.ttl)의 sh:minCount 가 무엇이 빠졌는지 말한다. 여기서 형식을 두 번 판정하지 않는다.
    """
    form: dict = {}
    slots: dict[str, list[str]] = {}
    cur = None
    for line in body:
        s = line.strip()
        if not s:
            continue
        if not form and (m := COMMENT_HEAD.match(s)):
            form.update(label=m.group(1), decoration=m.group(2), gist=m.group(3))
            continue
        if m := COMMENT_SLOT_HEAD.match(s):
            cur = m.group(1)
            slots.setdefault(cur, []).append(m.group(2))
            continue
        if cur:
            slots[cur].append(s)
    if "본문" in slots:
        form["sentences"] = count_sentences(" ".join(slots["본문"]))
    if "대상" in slots:
        form["targets"] = COMMENT_IRI.findall(" ".join(slots["대상"]))
    if "해소" in slots and (m := COMMENT_RESOLUTION.match(" ".join(slots["해소"]).strip())):
        form["resolution"] = m.group(1)
    return form


# ── 본문과 토큰 계수기 — 크기의 단위는 토큰이다 (결정 p1-chunk-unit-is-tokens) ────────────────────
# 본문을 떼는 규칙과 계수기가 이 모듈에 사는 까닭은 **head 액션**이다 — 청크 타깃마다 한 번 돌고 rdflib 를
# 싣지 않는다(`py_binary //tools:chunk2kg` 의 deps 가 비어 있다). `kb_lib` 에 두면 액션마다 rdflib 적재를
# 문다. `kb_lib` 는 이 이름들을 다시 내보내고 호출자는 `kb_lib.body_text`·`kb_lib.token_count` 를 쓴다.
# 크기의 단위가 줄에서 토큰으로 바뀌면 계수기가 빌드 입력이 된다. 재현의 조건은 둘이다 — 어휘 파일이
# 같은 바이트로 읽히고, 그것을 읽는 패키지의 버전이 같아야 한다. 어휘는 `MODULE.bazel` 의
# `http_file(@tiktoken_o200k_base//file)` 이 sha256 으로 고정하고 패키지는 `tools/requirements_lock.txt`
# 가 고정한다. 그 짝이 ODD 조건 `id:cond-tokenizer-lock` 이고 판정은 파일 해시 대조다.
# 어휘를 `o200k_base` 로 고른 근거는 이 저장소 청크 100개의 실측이다 — 문자/토큰 2.30 으로 `cl100k_base`
# 1.78 · `p50k_base` 0.97 · XLM-R SentencePiece 2.14 를 앞선다. 한글 산문의 토큰 수가 가장 적은 어휘가
# 같은 예산에 가장 많은 지식을 담는다.
# 아래 sha256 은 `MODULE.bazel` 의 http_file 과 같은 값이다. 사본이 둘이므로 동일성은 사람이 아니라
# ODD `CHECKS.tokenizer_lock` 의 명령이 보고, `load_tokenizer` 는 읽은 파일을 이 값으로 대조해 거부한다.
TOKENIZER_NAME = "o200k_base"                 # tiktoken 등록 어휘의 이름 — 패턴도 이 이름의 것을 쓴다
TOKENIZER_PACKAGE = "tiktoken"                # 계수기 패키지 (lock 의 직접 의존)
TOKENIZER_PACKAGE_VERSION = "0.12.0"
TOKENIZER_VOCAB_REPO = "tiktoken_o200k_base"  # MODULE.bazel 의 http_file 이름 (apparent 이름)
# runfiles 디렉토리의 이름은 **canonical 저장소 이름**이다 — `use_repo_rule` 로 만든 저장소는 bzlmod 에서
# `+<규칙 이름>+<저장소 이름>` 이 되고 실측 디렉토리가 `+http_file+tiktoken_o200k_base` 다. apparent 이름만
# 찾으면 인자 없이 부른 runfiles 탐색이 전부 빗나간다 (이 저장소 실측 2026-10-01 — vv_run 이 KB_TOKENIZER_VOCAB
# 를 못 채워 케이스 token-budget·chunk-42-lines 가 자극에 닿기 전에 죽었다). 둘 다 본다.
TOKENIZER_VOCAB_REPO_CANONICAL = f"+http_file+{TOKENIZER_VOCAB_REPO}"
TOKENIZER_VOCAB_FILE = "o200k_base.tiktoken"  # http_file 의 downloaded_file_path
TOKENIZER_VOCAB_SHA256 = "446a9538cb6c348e3516120d7c08b09f57c36495e2acfffe59a5bf8b0cfb1a2d"
TOKENIZER_VOCAB_ENV = "KB_TOKENIZER_VOCAB"    # 어휘 파일 경로의 환경 변수 — bazel 밖 실행의 자리
# o200k_base 의 사전 분할 패턴 — tiktoken 의 등록부(`tiktoken_ext.openai_public`)에서 읽는다. 여기 복제하면
# 정의처가 둘이 되고 패키지 갱신에서 갈린다 (STYLEGUIDE §7 단일 정의처).


def tokenizer_vocab_path(explicit: str | os.PathLike | None = None) -> Path:
    """고정된 어휘 파일의 경로. 명시 경로 → 환경 변수 → runfiles 순으로 찾고 없으면 `FileNotFoundError` 다.

    **명시가 우선이다** — 타깃이 `--vocab=$(rootpath @tiktoken_o200k_base//file)` 로 주는 경로가 그 자리다.
    runfiles 자리는 `bazel run` 의 것이다 — `http_file` 의 산출물은 외부 저장소에 살아
    `<runfiles>/{repo}/file/{name}` 이고, cwd 가 `_main` 인 부트스트랩에서는 `../{repo}/file/{name}` 이다.
    `{repo}` 는 canonical 이름(`+http_file+…`)과 apparent 이름 둘을 다 본다 — bzlmod 의 실측 디렉토리는
    앞의 것이고 뒤의 것만 보면 인자 없이 부른 경로가 전부 빗나간다.
    """
    if explicit:
        p = Path(explicit)
        if not p.is_file():
            raise FileNotFoundError(f"어휘 파일 {p} 가 없다")
        return p
    env = os.environ.get(TOKENIZER_VOCAB_ENV)
    if env:
        return tokenizer_vocab_path(env)
    rels = [f"{repo}/file/{TOKENIZER_VOCAB_FILE}"
            for repo in (TOKENIZER_VOCAB_REPO_CANONICAL, TOKENIZER_VOCAB_REPO)]
    runfiles = os.environ.get("RUNFILES_DIR", "")
    bases = ([Path(runfiles)] if runfiles else []) + [Path(".."), Path("external")]
    for base in bases:
        for rel in rels:
            if (base / rel).is_file():
                return base / rel
    raise FileNotFoundError(
        f"어휘 파일 {TOKENIZER_VOCAB_FILE} 을 찾지 못했다 — `bazel run //tools:tokens` 로 돌리거나 "
        f"{TOKENIZER_VOCAB_ENV} 에 경로를 준다 (고정처는 MODULE.bazel 의 http_file {TOKENIZER_VOCAB_REPO}, "
        f"runfiles 의 이름은 {TOKENIZER_VOCAB_REPO_CANONICAL} 다)")


def tokenizer_vocab_fingerprint(path: str | os.PathLike) -> str:
    """어휘 파일의 sha256 — ODD 조건 `id:cond-tokenizer-lock` 의 판정 값이다."""
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_tokenizer(vocab: str | os.PathLike | None = None):
    """고정된 어휘로 `tiktoken.Encoding` 을 만든다. 해시가 다르면 `ValueError` 로 거부한다.

    네트워크를 쓰지 않는다 — `tiktoken` 의 내려받기 경로(`load_tiktoken_bpe`)를 거치지 않고 고정된 파일을
    직접 해독한다. 파일 형식은 줄마다 `<base64 토큰> <순위>` 다. 특수 토큰은 두지 않는다 — 청크 본문에
    `<|endoftext|>` 같은 문자열이 있어도 보통 텍스트로 센다.
    `import tiktoken` 은 함수 안에 둔다. `kb_lib` 를 import 하는 도구 대부분은 계수기를 의존하지 않고
    그 BUILD 타깃에 패키지가 없다 (`chunk2kg` · `doccheck` 가 그렇다).
    """
    import base64

    import tiktoken
    from tiktoken_ext import openai_public

    path = tokenizer_vocab_path(vocab)
    got = tokenizer_vocab_fingerprint(path)
    if got != TOKENIZER_VOCAB_SHA256:
        raise ValueError(
            f"어휘 파일 {Path(path).as_posix()} 의 sha256 {got} 가 고정값 {TOKENIZER_VOCAB_SHA256} 과 다르다 — "
            f"계수기가 재현되지 않는다 (ODD id:cond-tokenizer-lock 이탈)")
    ranks = {}
    for line in Path(path).read_bytes().splitlines():
        if not line:
            continue
        token, rank = line.split()
        ranks[base64.b64decode(token)] = int(rank)
    pat = getattr(openai_public, TOKENIZER_NAME)()["pat_str"]
    return tiktoken.Encoding(name=TOKENIZER_NAME, pat_str=pat, mergeable_ranks=ranks, special_tokens={})


def body_text(path: str | os.PathLike, text: str) -> str:
    """청크 본문만 — frontmatter 와 앞뒤 빈 줄을 뗀 나머지다. 토큰은 이 문자열에서 센다.

    본문을 떼는 **단일 판정처**다 (결정 p1-chunk-unit-is-tokens 의 게이트 교체, 2026-10-01). 게이트
    (`chunk_lint`)·방출(`parse_chunk`)·실측(`tokens`)이 모두 이 문자열을 보므로 세 자리의 크기 판정이 갈리지 않는다.
    """
    lines = text.splitlines()
    if Path(path).suffix == ".ttl":
        return "\n".join(l for l in lines
                         if l.strip() and not l.lstrip().startswith(("#", "@prefix", "@base")))
    if lines and lines[0].strip() == "---":
        try:
            lines = lines[lines[1:].index("---") + 2:]
        except ValueError:
            pass
    while lines and not lines[-1].strip():
        lines.pop()
    while lines and not lines[0].strip():
        lines.pop(0)
    return "\n".join(lines)


def token_count(text: str, enc=None) -> int:
    """본문 하나의 토큰 수. `enc` 를 주지 않으면 어휘를 새로 적재한다 — 여러 파일은 적재를 한 번만 한다."""
    return len((enc or load_tokenizer()).encode(text))


# ── 청크 파싱 ────────────────────
# frontmatter 의 키 — 이 절의 `parse_chunk` 가 판정하는 것 (OKF v0.2 번들: type·status·generated·verified 는
# 그 스펙의 필드명이다). 링크 키는 `링크의 방출과 정체성` 절, 복합체 키는 `복합체의 순서` 절이 적는다.
# 형식은 YAML 부분집합이다 — key: value, 목록은 [a, b], 인라인 맵은 {k: v}.
#   iri:          항목 IRI (필수)
#   type:         requirement | decision | contract | schema | artifact | annotation | memory (필수, OKF).
#                 예외 하나가 `agt:Space` 다 — plane 이름이 아니라 온톨로지 클래스 이름이고, 그 청크는 설계 공간(`-space`)이라
#                 본문의 후보·제약까지 읽어야 그래프가 된다. 여기서는 frontmatter 만 판정하고(level 은 logical 고정) 방출은
#                 tools/space2kg.py 가 한다 — 이 도구에 넘기면 `FAIL [space]` 다 (결정 p9-candidate-storage)
#   level:        functional | abstract | logical | concrete | executable (필수)
#   title_ko:     한글 라벨 (필수) — OKF 확장 키
#   title:        영어 라벨 (필수) — OKF title
#   status:       draft | stable | suspect | invalidated | deprecated (필수, OKF + 확장 2)
#   generated:    {by: <행위자>, at: <ISO 8601>} (필수, OKF)
#   verified:     [{by: <행위자>, at: <ISO 8601>}, ...] (선택, OKF) — human: 접두어가 사람 검토
#   assumes:      가정 IRI 목록 (선택)
#   sources:      OKF v0.2 sources — [{resource: IRI, id?, title?, author?}] (선택). resource → prov:wasDerivedFrom
#   uses:         이 정의가 이름으로 쓰는 **같은 모듈의 최상위 정의** 청크 IRI 목록 (선택, type: artifact 에서만 —
#                 agt:usesDefinition 의 정의역이 agt:ArtifactChunk 다). agt:usesDefinition 으로 나간다. 링크 키가 아니다 —
#                 Bazel deps 도 링크 개체도 되지 않는다(링크는 파일 복합체의 것이다, p7-code-links-on-file-composite).
#                 값의 원본은 손이 아니라 tools/extract.py 이고 대상 실재는 validate check_dangling 이 본다
#   layer:        knowledge | methodology | process (선택, plane 제한 없음) — 이 항목이 서비스의 어느 층에서 역할을
#                 갖는가 (결정 p0-service-is-a-three-layer-wiki) → agt:inLayer agt:<값>Layer. **명시가 없으면
#                 knowledge 를 방출한다** — 표시 누락을 산발로 세지 않으려고 기본값을 그래프에 적는다. 층은 plane 과
#                 직교하는 역할 속성이고 값의 닫힌 집합은 shape layer-shapes.ttl 이 판정한다. 코드 청크는 등록부가 process 를 준다
#   exposes:      이 항목이 노출하려는 결함 요인(현상) 개체의 agt: IRI 목록 (선택, 위험 분석 G5 — 노트 8.21절).
#                 agt:exposesFactor 로 나간다. 링크 키가 아니다 — 대상이 청크가 아니라 온톨로지 개체이므로 링크 개체의
#                 치역 밖이고 Bazel deps 도 되지 않는다. 대상의 종류는 shape exposes-factor-shapes.ttl 이 판정한다
#   pattern:      ubiquitous | event-driven | state-driven | unwanted-behaviour | optional | complex (선택, type: requirement 에서만) —
#                 요구 문장의 EARS 패턴 (Mavin RE'09, 결정 p7-dev-plane-substance) → agt:pattern agt:<camelCase 개체>. 다른 plane 에 있으면 거부
#   targets:      주석이 관찰하는 대상 IRI 목록 (선택, type: annotation 에서만) → agt:targets 직접 트리플.
#                 **링크 키가 아니다** — 링크 개체(agt:Link)도 Bazel deps(gen_build.LINKS)도 만들지 않는다. 주석이 대상의 deps 가
#                 되면 주석 하나가 대상의 재빌드를 유발해 리뷰가 빌드 그래프를 오염시킨다. 주석은 대상을 관찰하지 구성하지 않는다
#   주석의 본문:   type: annotation 의 본문은 주석이다 (p7-commentary-form). 첫 줄 `<라벨> (<장식>): <요지>` 와 줄 머리 슬롯 넷
#                 (`대상:`·`본문:`·`제안:`·`해소:`)에서 agt:commentLabel·agt:commentDecoration·agt:resolutionState·
#                 agt:commentSentenceCount 를 낸다. 닫힌 어휘와 문장 상한의 판정은 shape(review-comment-body-shapes.ttl)이고
#                 여기서 거부하는 것은 `대상:` 과 frontmatter `targets` 의 불일치 하나뿐이다
#   프로파일 타이핑: 청크마다 plane 클래스 뒤에 개발 프로파일의 실체 클래스를 더 붙인다 (`a agt:RequirementChunk , agt:RequirementStatement`,
#                 PROFILE_SUBSTANCE). 살아 있는 청크든 폐기된 청크든 같다 — 폐기된 요구 문장도 요구 문장이다
#   라벨 언어:    title 에 한글([ㄱ-ㆎ가-힣])이 있거나 title_ko 에 한글이 없으면 거부 — 영문 라벨에 한글을 섞지 않는다(0.6절).
#                 composite 의 title·title_ko 도 같은 @en/@ko 라벨이므로 같은 규칙으로 거부한다
#   인용원:       본문(frontmatter 제외, **코드 펜스 밖**)에 소멸성 채널 경로(`harness/channel/` · `harness/user/` · 옛 `docs/feedback/`)가
#                 있으면 거부 — 근거는 질문 번호(`Q12-a`)로 적는다. 규칙·근거는 영속 지식
#                 (노트·결정)에 둔다 (agrtls-practices-review P). status: deprecated 청크는 제외

def parse_chunk(path: str) -> tuple[dict, str]:
    """frontmatter dict와 **본문 문자열**을 돌려준다 — 크기는 호출자가 센다 (단위는 토큰이다).

    본문을 떼는 규칙은 `body_text` 하나다. 둘째 값이 수가 아니라 문자열인 까닭은 계수기를 부르는 비용을
    호출자가 고르게 하는 것이다 — frontmatter 만 읽는 도구(`gen_build`·`labels`·`weave`)는 어휘를 적재하지 않는다.
    """
    text = Path(path).read_text(encoding="utf-8")
    lines = text.splitlines()
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

    body = body_text(path, text).splitlines()  # 본문의 단일 판정처 — 게이트·방출·실측이 같은 문자열을 본다
    meta["_content_hash"] = hashlib.sha256("\n".join(body).encode("utf-8")).hexdigest()[:12]
    meta["_body_slots"] = body_slots(body)  # 본문이 쓴 슬롯 표지 (결정 p4-slot-answers-one-question)

    for k in REQUIRED:
        if not meta.get(k):
            raise ValueError(f"{path}: frontmatter에 {k} 가 없다")
    if meta["type"] == SPACE_TYPE:  # 설계 공간 — plane 이 아니라 클래스다. 본문(후보·제약)은 space2kg 가 읽는다 (p9-candidate-storage)
        if meta["level"] != SPACE_LEVEL:
            raise ValueError(f"{path}: `-space` 청크의 level 은 {SPACE_LEVEL} 이다 — 후보·제약·배제 근거가 사는 수준이다 "
                             f"(p9-candidate-storage). 실제 {meta['level']!r}")
    elif meta["type"] not in PLANE_CLASS:
        raise ValueError(f"{path}: 알 수 없는 type {meta['type']!r} — plane 이름이거나 `{SPACE_TYPE}` 여야 한다")
    if meta["level"] not in LEVELS:
        raise ValueError(f"{path}: 알 수 없는 level {meta['level']!r}")
    if meta["status"] not in STATES:
        raise ValueError(f"{path}: 알 수 없는 status {meta['status']!r}")
    if "pattern" in meta:  # EARS 패턴 — 요구 문장의 형식이지 다른 plane 의 속성이 아니다 (p7-dev-plane-substance)
        if meta["type"] != "requirement":
            raise ValueError(f"{path}: pattern 은 type: requirement 에서만 쓴다 — 실제 type {meta['type']!r} (EARS 패턴은 요구 문장의 형식이다)")
        if meta["pattern"] not in EARS_PATTERNS:
            raise ValueError(f"{path}: 알 수 없는 pattern {meta['pattern']!r} — {' | '.join(EARS_PATTERNS)} 중 하나다 (EARS, Mavin RE'09)")
    if LAYER_KEY in meta:  # 서비스 층 — plane 과 직교하므로 plane 제한이 없고 값 어휘만 닫힌다 (p0-service-is-a-three-layer-wiki)
        if meta[LAYER_KEY] not in LAYERS:
            raise ValueError(f"{path}: 알 수 없는 {LAYER_KEY} {meta[LAYER_KEY]!r} — {' | '.join(LAYERS)} 중 하나다 "
                             f"(서비스의 세 층. 명시가 없으면 {LAYER_DEFAULT} 다)")
    declared = meta.get(TARGETS_KEY) or []
    if declared and meta["type"] != "annotation":  # agt:targets 의 정의역은 agt:AnnotationChunk 다 — 주석만 대상을 가리킨다
        raise ValueError(f"{path}: {TARGETS_KEY} 는 type: annotation 에서만 쓴다 — 실제 type {meta['type']!r} "
                         f"(agt:targets 의 정의역은 agt:AnnotationChunk 다)")
    if (meta.get(USES_KEY) or []) and meta["type"] != "artifact":  # agt:usesDefinition 의 정의역은 agt:ArtifactChunk 다
        raise ValueError(f"{path}: {USES_KEY} 는 type: artifact 에서만 쓴다 — 실제 type {meta['type']!r} "
                         f"(agt:usesDefinition 의 정의역·치역은 agt:ArtifactChunk 이고 값의 원본은 추출기다)")
    if meta["type"] != SPACE_TYPE:  # 절 키 — 형식과 plane 제한 (p12-norm-documents-from-section-chunks)
        check_norm_keys(path, meta)
    if meta["type"] == "annotation":  # 주석 — 첫 줄과 슬롯을 읽는다 (p7-commentary-form). 형식 판정은 shape 가 한다
        meta["_comment"] = comment_form(body)
        in_body = meta["_comment"].get("targets")
        if in_body is not None and sorted(in_body) != sorted(declared):
            raise ValueError(f"{path}: 주석의 `대상:` 과 frontmatter {TARGETS_KEY} 가 다르다 — 본문 {sorted(in_body)} · "
                             f"frontmatter {sorted(declared)} (p7-commentary-form: 대상은 둘이 일치해야 한다)")
    if meta["status"] != "deprecated":
        fence = None  # 코드 펜스 안은 인용 구역이다 — 생성기는 원문을 고쳐 쓰지 않으므로(p7-code-extraction-direction)
        for i, raw in enumerate(lines[end + 1 :], start=end + 2):  # 인용원 규칙은 **저작된 본문**의 규칙이다
            m = BODY_FENCE.match(raw)
            if fence:
                if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                    fence = None
                continue
            if m:
                fence = m.group(1)
                continue
            if any(e in raw for e in EPHEMERAL_PATHS):
                raise ValueError(f"{path}:{i}: 소멸성 채널 경로를 인용원으로 쓰지 않는다 — 규칙·근거는 영속 지식(노트·결정)에 두고 질문 번호(Q12-a)로 가리킨다 "
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
        if ORDERED_KEY in comp:  # 순서의 선언 — 부분 집합과의 일치는 묶음 전체를 아는 main 이 본다 (p4-composite-order-is-declared)
            for e in order_errors(path, comp[ORDERED_KEY], f"composite.{ORDERED_KEY}"):
                raise ValueError(e)
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

    return meta, "\n".join(body)


def split_outside_brackets(text: str) -> list:
    """콤마로 나누되 `[...]` 안의 콤마는 세지 않는다 — 인라인 맵의 목록 값(`composite: {…, ordered: [a, b]}`)."""
    parts, depth, cur = [], 0, []
    for ch in text:
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
        if ch == "," and depth <= 0:
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    parts.append("".join(cur))
    return parts


def parse_map(text: str) -> dict:
    """인라인 맵 {k: v, k: v} — 값에 콜론이 없다는 전제. 값이 `[...]` 면 목록으로 읽는다(`ordered`)."""
    out = {}
    for part in split_outside_brackets(text.strip().strip("{}")):
        if not part.strip():
            continue
        k, _, v = part.partition(":")
        v = v.strip()
        out[k.strip()] = parse_value(v) if v.startswith("[") else v.strip("'\"")
    return out


def split_top_level(text: str) -> list:
    """콤마로 나누되 `[...]`·`{...}` 안의 콤마는 세지 않는다 — 목록의 원소가 맵이거나 맵이 목록 값을 가질 때(절 키 `items`)."""
    parts, depth, cur = [], 0, []
    for ch in text:
        if ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        if ch == "," and depth <= 0:
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    parts.append("".join(cur))
    return parts


def parse_value(val: str):
    """key: value 의 값 — 인라인 맵, 목록(스칼라·맵·둘의 섞임), 스칼라.

    목록의 원소는 `{` 로 시작하면 맵, 아니면 스칼라다. 스칼라만의 목록과 맵만의 목록은 옛 판독과 같은 값을 낸다 —
    섞인 목록은 절 키 `items`(`[a#1, {규약: b#2, 하위: [c#1]}]`)가 처음 쓴다.
    """
    if val.startswith("{") and val.endswith("}"):
        return parse_map(val)
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        out = []
        for v in split_top_level(inner):
            v = v.strip()
            if not v:
                continue
            out.append(parse_map(v) if v.startswith("{") and v.endswith("}") else v.strip("'\""))
        return out
    return val.strip("'\"")


# ── head 트리플의 방출 ────────────────────

def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def emit_chunk(path: str, meta: dict, tokens: int, conventions: dict | None = None) -> str:
    """청크 하나의 head 블록. `conventions` 는 결정 slug → 결정 복합체 IRI — 절 청크의 `items` 를 agt:projectsConvention 으로 낸다.

    사상에 없는 slug 는 호출자(main)가 먼저 거부한다 — 여기 오면 전부 풀린다.
    """
    substance = PROFILE_SUBSTANCE.get(meta["type"])  # norm 은 실체 클래스가 없다 — plane 클래스 하나로 타이핑한다
    stmts = [
        f"a {PLANE_CLASS[meta['type']]}" + (f" , {substance}" if substance else ""),
        f'rdfs:label "{esc(meta["title"])}"@en',
        f'rdfs:label "{esc(meta["title_ko"])}"@ko',
        f"agt:hasLevel agt:{meta['level']}",
        # 서비스 층 — plane·level 과 나란한 직교 축이다. **명시가 없어도 기본값을 방출한다**: 표시 누락을 산발로
        # 세지 않으려면 지식 층 배정이 그래프에 있어야 하고, 그래야 층별 집계(CQ-38)의 분모가 항목 전수가 된다
        # (p0-service-is-a-three-layer-wiki). 값의 닫힌 집합은 shape layer-shapes.ttl 이 판정한다
        f"{LAYER_PREDICATE} {LAYERS[meta.get(LAYER_KEY, LAYER_DEFAULT)]}",
    ]
    if "pattern" in meta:
        stmts.append(f"agt:pattern {EARS_PATTERNS[meta['pattern']]}")
    if NORM_HEADING_KEY in meta:  # 절 제목·깊이 — 절 청크의 shape(norm-section-shapes.ttl)가 짝과 값을 본다
        stmts.append(f'agt:sectionHeading "{esc(meta[NORM_HEADING_KEY])}"')
    if NORM_DEPTH_KEY in meta:
        stmts.append(f"agt:sectionDepth {int(meta[NORM_DEPTH_KEY])}")
    if meta.get(NORM_CONTINUES_KEY) == "true":  # 이어짐 절 청크 — 제목·깊이 없이 규약 줄을 싣는 자리를 shape 가 머리 청크와 가른다
        stmts.append("agt:sectionContinues true")
    for slug in norm_item_slugs(meta.get("_norm_items") or [], links=False):  # 절이 싣는 줄의 결정
        stmts.append(f"{PROJECTS_CONVENTION_PREDICATE} <{(conventions or {})[slug]}>")
    stmts += [
        f"agt:tokenCount {tokens}",  # 본문의 크기 — 단위는 토큰이고 계수기는 o200k_base 다 (p1-chunk-unit-is-tokens)
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
    # 주석 → 대상 (agt:targets). **링크 키가 아니다**: 주석이 대상의 deps 가 되면 리뷰가 빌드 그래프를 오염시켜 주석 하나가
    # 대상의 재빌드를 유발한다. 주석은 대상을 관찰하지 대상을 구성하지 않으므로 agt:cites 처럼 그래프에만 트리플로 남는다 —
    # LINK_KEYS(링크 개체)에도 gen_build.LINKS(Bazel deps)에도 넣지 않는다. 대상 실재는 validate check_dangling 이 본다
    for t in meta.get(TARGETS_KEY, []) or []:
        stmts.append(f"agt:targets <{t}>")
    # 위험에서 파생된 항목 → 그것이 노출하려는 결함 요인 (agt:exposesFactor, 위험 분석 G5). 대상은 청크가 아니라 온톨로지 개체이므로
    # LINK_KEYS 도 gen_build.LINKS 도 아니다 — 링크 개체의 치역 밖이고 deps 가 되면 T-Box 가 청크의 빌드 입력이 된다.
    # 대상이 agt:DefectFactor 하위 개체인지는 shape 가 본다 (exposes-factor-shapes.ttl)
    for f in meta.get(EXPOSES_KEY, []) or []:
        stmts.append(f"{EXPOSES_PREDICATE} <{f}>")
    # 정의 → 같은 모듈의 정의 (agt:usesDefinition, references 족의 잎). 추출기가 AST 에서 낸 값이고 손으로 쓰지 않는다.
    # LINK_KEYS 도 gen_build.LINKS 도 아니다 — 링크는 파일 복합체의 것이고(p7-code-links-on-file-composite) 함수 churn 이
    # 빌드 그래프를 움직이면 안 된다. 대상 실재는 validate check_dangling 이 본다
    for u in meta.get(USES_KEY, []) or []:
        stmts.append(f"{USES_PREDICATE} <{u}>")
    c = meta.get("_comment") or {}  # 주석의 본문 파생 사실 (p7-commentary-form) — 닫힌 어휘와 상한은 shape 가 판정한다
    for key, pred in (("label", "agt:commentLabel"), ("decoration", "agt:commentDecoration"), ("resolution", "agt:resolutionState")):
        if key in c:
            stmts.append(f'{pred} "{esc(c[key])}"')
    if "sentences" in c:
        stmts.append(f"agt:commentSentenceCount {c['sentences']}")
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


LINK_KEYS = ("refines", "serves", "supersedes", "verifies", "satisfies", "constrains", "derivesFrom", "allocates", "generates",
             "overlapsWith")  # overlapsWith 는 relatedTo 족의 약한 잎 — 링크 키라 링크 개체·복원 표시를 받는다 (overlap-ontology)
RESTORED_KEY = "restored"  # 복원 링크의 표시 (p10-restored-link-marking) — 값은 같은 청크의 링크 키 대상 IRI 목록
RESTORED_GATE = getattr(kb_lib, "RESTORED_GATE", "restored")  # 게이트 id — FAIL [restored] (정의처 kb_lib)
ID_BASE = "https://agentic-knowledge-base.dev/id/"
# 증거 종류 — 구축(편집 부산물, 10.3절)은 구축 기록, 복원(restored: 표시 — 도구·에이전트가 제안하고 사람이 확정)은 제안 (evidence-ontology)
EVIDENCE_BUILT = "agt:constructionRecord"
EVIDENCE_RESTORED = "agt:proposal"


# ══ 링크 — 방출·정체성·재기저 ════════════════════
# 링크를 트리플로 내고, 분할 조각의 링크를 뿌리 uuid 로 되돌린다. 두 절이 한 장인 까닭은 링크의 정체성
# 규칙(`link_hash`·`work_id`)이 재기저의 입력이기 때문이다 — 파일 복합체의 직접 부분 상한 9(4.5절)에
# 맞추려고 자른 묶음이 아니다 (p7-code-links-on-file-composite).

# ── 링크의 방출과 정체성 ────────────────────
# frontmatter 의 **링크 키**와 링크 IRI 의 규칙 — 이 절이 방출하는 것이다.
#   refines:      이 항목이 정제하는 상위 항목 IRI 목록 (선택, 수직 링크 9.2절)
#   supersedes:   이 항목이 대체하는 항목 IRI 목록 (선택)
#   serves·verifies·derivesFrom·satisfies·constrains·allocates·generates·overlapsWith: 그 밖의 링크 키(LINK_KEYS) — 대상 IRI 목록 (선택).
#                 모든 링크 키는 직접 트리플(agt:<key>)과 링크 개체(agt:Link, emit_links) 둘로 나간다. verifies 의 주어는 kb/vv 청크뿐 (defs/kb.bzl).
#                 overlapsWith 는 relatedTo 족의 약한 잎이다 — 추적 매트릭스에 칸이 없어 어느 잎도 이름을 주지 못하는 관계의 자리이고,
#                 Bazel deps 가 되지 않는다(gen_build.LINKS 밖) 대신 링크 개체와 복원 표시를 받는다 (overlap-ontology)
#   restored:     복원 링크의 표시 — 같은 청크의 링크 키(LINK_KEYS) 어딘가에 대상으로 있는 IRI 목록 (선택, p10-restored-link-marking).
#                 그 (주어, 링크 키, 대상)의 agt:Link 개체에 증거가 두 줄 붙는다 — 확정 기록 constructionRecord(사람이 frontmatter 에 적은
#                 편집 시점 기록; 9.11절 규칙 "구축(+) 또는 실행(+) 없이 확정 불가"를 verify 질의 confirmed-without-evidence 가 강제한다)와
#                 후보의 출처 proposal(도구·에이전트가 제안하고 사람이 확정). 구축 링크는 constructionRecord 한 줄뿐이므로 proposal 의 유무가
#                 복원의 표지다. linkState 는 그대로 confirmed 다 — frontmatter 에 적힌 것은 확정이다. 링크 대상에 없는 IRI 는
#                 `FAIL [restored] <파일>: 복원 표시 <IRI> 가 링크 대상에 없다` 로 거부. 복원 비율(metrics·audit)은 증거 종류로 센다 (kb_lib.link_origins)
#   specializationOf: 분할로 생긴 조각이 원 청크를 가리키는 단일 IRI (선택, p10-split-keeps-work-identity) → prov:specializationOf (PROV-O).
#                 청크 uuid 는 work-id 다: 분할 시 조각 하나가 원 uuid 를 승계하고 나머지는 새 uuid + 이 키로 잇는다. 자기 자신은 거부.
#                 대상 실재는 validate dangling, 같은 plane·살아 있음·사슬 비순환은 validate check_specialization(FAIL [specialization])이
#                 판정한다. 순환은 이 도구도 뿌리를 계산할 수 없으므로 같은 게이트 id 로 거부한다
#   링크 IRI:     id/link/<sha256(뿌리(출발)|종류|뿌리(도착))[:12]> — 양 끝은 specializationOf 사슬을 따라 올라간 뿌리 uuid(work-id)다.
#                 그래서 조각을 가리키는 링크와 원본을 가리키던 링크가 같은 개체가 되어 증거·이력이 이어진다. 뿌리는 묶음 전체를 알아야
#                 계산되므로 --fragment 는 원 IRI 로 해시하고 --merge(와 단일 실행)가 rebase_links 로 다시 계산해 같은 IRI 의 링크·증거
#                 블록을 하나로 합친다(양 끝·증거의 합집합). 증거 IRI 는 같은 해시에 접미(-proposal)다
#   coUpdatesWith: 같은 내용을 담아 함께 갱신되어야 하는 청크 IRI 목록 (선택, relatedTo 족 — 안전율 중복의 표시)

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


# ── 링크 블록의 재기저 ────────────────────

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


# ── 병합과 실행 ────────────────────

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
            print(f"FAIL [chunk2kg-merge] {frag}: 조각을 읽을 수 없다 — {e}", file=sys.stderr)
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
            print(f"FAIL [chunk2kg-merge] {e}", file=sys.stderr)
        return EXIT_FAIL
    chunks, spec_errors = rebase_links(chunks, spec)
    if spec_errors:
        for e in spec_errors:
            print(f"FAIL [{SPECIALIZATION_GATE}] {e}", file=sys.stderr)
        return EXIT_FAIL
    blocks = [b for _, b in sorted(chunks)] + [b for _, b in sorted(comps)]
    Path(out).write_text(PREAMBLE + "\n" + "\n\n".join(blocks) + "\n", encoding="utf-8")
    return 0


def attach_parts(composites: dict, part_refs: list) -> list:
    """청크의 `part_of` 와 선언된 복합체의 `composite.part_of` 를 복합체의 members 에 붙인다 — 위반 메시지 목록을 돌려준다.

    대상이 이 묶음(실행의 입력 집합) 안에 선언되지 않았거나 자기 자신이거나 사슬이 순환하면 위반이다 (4.5절 비순환,
    p4-composite-as-part-of).
    """
    errors = []
    for chunk_iri, comp_iri, path in part_refs:
        if comp_iri not in composites:
            errors.append(f"{path}: part_of 대상 복합체 {comp_iri} 가 이 묶음 안에 선언되지 않았다 — 묶음은 이 실행의 입력 집합이고 "
                          f"액션 하나가 부분 청크 전부와 선언 청크를 함께 받아야 한다 (defs/kb.bzl 의 kb_composite·kb_decision)")
        else:
            composites[comp_iri]["members"].append((chunk_iri, path))
    for comp_iri, c in sorted(composites.items()):  # 복합체가 복합체의 부분이 되는 자리 (p4-composite-as-part-of)
        parent = c.get("parent")
        if not parent:
            continue
        if parent not in composites:
            errors.append(f"{c['path']}: composite.{PART_OF_KEY} 대상 복합체 {parent} 가 이 묶음 안에 선언되지 않았다 — 중첩 복합체는 "
                          f"한 액션이 뿌리부터 잎까지 함께 받아야 한다 (defs/kb.bzl 의 kb_composite)")
        elif parent == comp_iri:
            errors.append(f"{c['path']}: composite.{PART_OF_KEY} 가 자기 자신 {parent} 이다 — 부분-전체는 비순환이다 (4.5절)")
        else:
            composites[parent]["members"].append((comp_iri, c["path"]))
    for comp_iri in sorted(composites):  # 사슬 순환 — 반대칭 공리의 생성 시점 대응 (4.5절 비순환)
        seen_chain, cur = {comp_iri}, composites[comp_iri].get("parent")
        while cur in composites:
            if cur in seen_chain:
                errors.append(f"{composites[comp_iri]['path']}: composite.{PART_OF_KEY} 사슬이 순환한다 — {comp_iri} 에서 시작해 {cur} 로 돌아온다 (4.5절 비순환)")
                break
            seen_chain.add(cur)
            cur = composites[cur].get("parent")
    return errors


def parse_convention_targets(where: str, pairs: list, errors: list) -> dict:
    """`--convention-target slug=IRI` 들 → {slug: IRI}. 꼴 밖의 인자는 `errors` 에 더한다 (p12-norm-documents-from-section-chunks)."""
    out = {}
    for pair in pairs:
        slug, sep, iri = pair.partition("=")
        if not sep or not NORM_SLUG.match(slug) or not iri:
            errors.append(f"{where}: --convention-target {pair!r} 는 `slug=IRI` 꼴이다")
        else:
            out[slug] = iri
    return out


def emit_parsed(parsed: list, conventions: dict, enc, errors: list) -> list:
    """읽은 청크 (경로, 메타, 본문) → head 블록. 절 청크가 줄을 싣는 결정의 IRI 를 모르면 방출하지 않고 `errors` 에 더한다."""
    blocks = []
    for path, meta, body in parsed:
        missing = [sl for sl in norm_item_slugs(meta.get("_norm_items") or [], links=False) if sl not in conventions]
        if missing:
            errors.append(f"{path}: items 가 가리키는 결정 {missing} 의 복합체 IRI 를 모른다 — 생성 BUILD 의 kb_composite.conventions "
                          f"(--convention-target slug=IRI)가 넘기지 않았다. 결정 디렉토리 이름을 확인하고 tools/gen_build.py 를 다시 돌린다")
            continue
        blocks.append((meta["id"], emit_chunk(path, meta, token_count(body, enc), conventions)))
        blocks.extend(emit_links(meta))
    return blocks


def norm_composite_errors(composites: dict, parsed: list) -> list:
    """규범 문서의 복합체마다 머리 청크(선언)와 절 청크의 구분 — norm_bundle_errors 를 묶음에 돌린다.

    문서 복합체(뿌리)의 선언 청크는 머리 청크다. 묶음 복합체(`composite.part_of` 가 문서 복합체 또는 다른 묶음)는 직접 부분
    9 이하(4.5절)를 지키려고 절을 나눈 것이고 제목을 내지 않으므로, 그 선언 청크는 묶음의 첫 절 청크이며 절 키를 갖는다.
    """
    by_iri = {meta["id"]: meta for _, meta, _ in parsed}
    errors = []
    for _iri, c in sorted(composites.items()):
        decl = next((m for _, m, _ in parsed if m.get("_path") == c["path"]), None)
        if decl is not None and decl.get("type") == NORM_TYPE:
            members = [(by_iri[m], p) for m, p in c["members"] if m in by_iri]
            errors += norm_bundle_errors(None if c.get("parent") else decl, members)
    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--fragment", action="store_true", help="타깃 하나의 조각 — 전문(preamble) 없이 블록만 (kb_chunk·kb_decision 액션)")
    ap.add_argument("--merge", action="store_true", help="조각들을 병합해 -kg 를 만든다 (kb_kg_merge)")
    ap.add_argument("--ordered", action="append", default=[], metavar="IRI",
                    help="이 묶음의 복합체가 선언한 부분의 순서 — 부분마다 한 번, 선언 순서대로 반복해 준다(`--ordered A --ordered B`). "
                         "목록형(nargs)이 아닌 이유는 청크 파일이 위치 인자라 목록이 그것을 삼키기 때문이다. 생성 BUILD 의 명시 "
                         "인자(kb_decision·kb_composite 의 ordered)가 넘긴다. 복합체 하나를 선언하는 실행에만 준다. "
                         "frontmatter composite.ordered 와 함께 있으면 같아야 한다")
    ap.add_argument("--convention-target", action="append", default=[], metavar="SLUG=IRI",
                    help="결정 디렉토리 이름 → 결정 복합체 IRI — 절 청크(type: norm)의 items 가 가리키는 결정마다 한 번. "
                         "생성 BUILD 의 kb_composite.conventions 가 넘긴다(gen_build 가 결정 디렉토리에서 푼다). 입력에 결정의 "
                         "결론 청크가 있으면 그 디렉토리 이름도 스스로 푼다 (p12-norm-documents-from-section-chunks)")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — --merge 가 아니면 필수다"
                                                      "(kb_chunk·kb_decision 의 head 액션이 --residency defs/kb.bzl 로 넘긴다)")
    ap.add_argument("--vocab", default="", help="토큰 계수기의 어휘 파일 — 없으면 runfiles 의 고정 파일을 쓴다. "
                                                "agt:tokenCount 가 이 어휘로 센 수다 (p1-chunk-unit-is-tokens)")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()
    if args.merge:  # 병합은 이미 방출된 조각을 잇기만 한다 — parse_chunk 를 부르지 않으므로 값 어휘가 필요 없다
        return merge(args.out, args.files)
    if not args.residency:
        print(f"FAIL [{TAG}] --residency 가 없다 — defs/kb.bzl 이 이 액션의 입력이 아니다. 매크로·BUILD 에 //defs:kb.bzl 를 더한다",
              file=sys.stderr)
        return EXIT_CONFIG
    try:
        apply_plane_level_state(*load_plane_level_state(args.residency))
    except (OSError, ValueError) as e:
        print(f"FAIL [{TAG}] {args.residency}: 읽을 수 없다 — {e}", file=sys.stderr)
        return EXIT_CONFIG
    try:  # 어휘는 한 번만 적재한다 — 액션 하나가 청크 여럿을 받는다 (복합체·결정)
        enc = load_tokenizer(args.vocab or None)
    except FileNotFoundError as e:
        print(f"FAIL [{TAG}] 어휘 파일 — {e}", file=sys.stderr)
        return EXIT_CONFIG
    except ValueError as e:  # 해시가 고정값과 다르다 — 계수기가 재현되지 않는다
        print(f"FAIL [{TAG}] {e}", file=sys.stderr)
        return EXIT_FAIL

    blocks, seen = [], {}
    composites: dict = {}   # iri -> {labels, members[]}
    part_refs: list = []    # (chunk_iri, composite_iri, path)
    errors = []
    space_errors = []       # 게이트 id `space` — FAIL [space] (설계 공간 청크가 head 생성기로 왔다)
    restored_errors = []    # 게이트 id `restored` — FAIL [restored] (복원 표시가 링크 대상에 없다)
    spec_errors = []        # 게이트 id `specialization` — FAIL [specialization] (자기 참조·사슬 순환)
    spec: dict = {}         # 조각 IRI → 원본 IRI — 링크 IRI 의 뿌리 계산 (단일 실행에서는 여기서, --merge 에서는 블록에서 읽는다)
    conventions = parse_convention_targets(args.out, args.convention_target, errors)  # 결정 slug → 결정 복합체 IRI
    parsed: list = []       # (경로, 메타, 본문) — 절 청크의 결정 slug 를 풀려면 입력 전부를 먼저 읽어야 한다
    for path in sorted(args.files):
        try:
            meta, body = parse_chunk(path)
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
        if meta["type"] == SPACE_TYPE:  # 후보는 head 로 올라가지 않는다 — 그래야 deps 가 되지 않는다 (p9-candidate-storage)
            space_errors.append(f"{path}: 설계 공간 청크(type: {SPACE_TYPE})는 head 그래프로 올리지 않는다 — 후보 링크는 확정 링크와 자리가 "
                                f"다르고 결코 deps 가 되지 않는다. tools/space2kg.py 로 올린다 (//space:design_space, p9-candidate-storage)")
            continue
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
                composites[comp["id"]] = {"ko": comp["title_ko"], "en": comp["title"], "members": [], "path": path,
                                          "order": comp.get(ORDERED_KEY),  # 선언된 순서 — 없으면 None
                                          "parent": comp.get(PART_OF_KEY)}  # 상위 복합체 — 없으면 None (뿌리)
        if meta.get("part_of"):
            part_refs.append((meta["id"], meta["part_of"], path))
        if meta["type"] == "decision" and Path(path).name == "conclusion.md" and isinstance(comp, dict) and comp.get("id"):
            conventions.setdefault(Path(path).parent.name, comp["id"])  # 입력 안의 결정 — 디렉토리 이름이 slug 다
        meta["_path"] = path
        parsed.append((path, meta, body))
    blocks += emit_parsed(parsed, conventions, enc, errors)  # 방출은 slug 사상이 다 모인 뒤다
    errors += attach_parts(composites, part_refs)  # 청크·복합체 부분을 복합체에 붙이고 사슬을 본다
    if args.ordered:  # 생성 BUILD 의 명시 인자 — 중첩 묶음에서는 부분 집합이 같은 복합체 하나를 고른다
        errors += order_errors(args.out, args.ordered, "--ordered")
        target = [c for c in composites.values() if c["order"] is not None and c["order"] == args.ordered]
        if not target:
            target = [c for c in composites.values() if c["order"] is None and sorted(m for m, _ in c["members"]) == sorted(args.ordered)]
        if len(target) != 1:
            errors.append(f"{args.out}: --ordered 가 가리키는 복합체를 하나로 고를 수 없다 — 선언된 복합체 {len(composites)}개 가운데 "
                          f"frontmatter composite.{ORDERED_KEY} 또는 부분 집합이 인자와 같은 것이 {len(target)}개다 "
                          f"(defs/kb.bzl 의 kb_decision·kb_composite 가 묶음마다 뿌리 복합체의 순서를 한 번 넘긴다)")
        else:
            target[0]["order"] = args.ordered
    errors += norm_composite_errors(composites, parsed)  # 규범 문서 — 머리 청크와 절 청크의 구분
    comp_blocks = []
    for iri, c in sorted(composites.items()):
        if not c["members"]:
            errors.append(f"{c['path']}: 복합체 {iri} 에 부분이 없다 — 멤버 청크가 part_of 로 가리켜야 한다")
            continue
        part_iris = sorted(m for m, _ in c["members"])
        order = c["order"]
        if order is not None and sorted(order) != part_iris:
            errors.append(f"{c['path']}: composite.{ORDERED_KEY} 가 부분 집합과 다르다 — 선언 {sorted(order)} · 부분 {part_iris}. "
                          f"순서 목록은 부분 전부를 빠짐없이 한 번씩 담는다 (p4-composite-order-is-declared)")
            continue
        parts = " ,\n        ".join(f"<{m}>" for m in part_iris)
        block = (f"<{iri}>\n    a agt:Composite{' , co:List' if order else ''} ;\n"
                 f'    rdfs:label "{esc(c["en"])}"@en ;\n'
                 f'    rdfs:label "{esc(c["ko"])}"@ko ;\n'
                 f"    agt:hasDirectPart {parts}")
        if order:  # co:List — 색인은 1 부터의 양의 정수다 (Collections Ontology: co:item / co:ListItem / co:index / co:itemContent)
            items = " ,\n        ".join(f'[ a co:ListItem ; co:index "{n}"^^xsd:positiveInteger ; co:itemContent <{m}> ]'
                                       for n, m in enumerate(order, start=1))
            block += f" ;\n    co:item {items}"
        comp_blocks.append(block + " .")

    if not args.fragment:  # 단일 실행은 묶음 전체를 아니 뿌리 uuid 로 링크 IRI 를 계산한다 — --merge 와 같은 결과. 조각은 원 IRI 그대로
        blocks, spec_errors2 = rebase_links(blocks, spec)
        spec_errors += spec_errors2
    if errors or restored_errors or spec_errors or space_errors:
        for e in errors:
            print(f"FAIL [{TAG}] {e}", file=sys.stderr)
        for e in space_errors:
            print(f"FAIL [{SPACE_GATE}] {e}", file=sys.stderr)
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
