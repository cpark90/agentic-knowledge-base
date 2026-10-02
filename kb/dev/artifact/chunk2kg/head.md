---
id: https://agentic-knowledge-base.dev/id/chunk/8752721c-db99-4c2f-be3b-382f6ec0169f
type: artifact
level: executable
title_ko: 모듈 머리 exit-fail (tools/chunk2kg.py)
title: module head exit-fail in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/ab66f02d-6126-4507-b73a-c29429769f11, https://agentic-knowledge-base.dev/id/chunk/01f6a247-ed75-405f-b286-3d59b8acc9d2, https://agentic-knowledge-base.dev/id/chunk/28655d6b-d000-4f43-8d68-9e0ce042c39c]
part_of: https://agentic-knowledge-base.dev/id/composite/b1903be2-0bdb-4f11-9c2b-cc59cc7e9a24
composite: {id: https://agentic-knowledge-base.dev/id/composite/b1903be2-0bdb-4f11-9c2b-cc59cc7e9a24, title_ko: 모듈 머리 복합체 exit-fail (tools/chunk2kg.py), title: section composite exit-fail in tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/8752721c-db99-4c2f-be3b-382f6ec0169f, https://agentic-knowledge-base.dev/id/chunk/9081dacd-219d-4944-b3c6-d5d9a6955f49, https://agentic-knowledge-base.dev/id/chunk/e1d9652e-f3b3-470b-bf7f-f8fa31f8be68, https://agentic-knowledge-base.dev/id/chunk/abf3ca16-b991-4326-8c10-b4581d03a6d2], part_of: https://agentic-knowledge-base.dev/id/composite/f7d6eec7-bef4-4e94-ac55-36e7dda654ce}
---
**모듈 머리** — `tools/chunk2kg.py` 의 모듈 머리 `exit-fail` 다. 모듈 머리

**정의** — `SpecializationError` · `load_plane_level_state` · `apply_plane_level_state` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
EXIT_FAIL = getattr(kb_lib, "EXIT_FAIL", 1)      # 판정 실패
EXIT_CONFIG = getattr(kb_lib, "EXIT_CONFIG", 2)  # 파일 없음·읽을 수 없는 입력

TAG = "chunk2kg"
EPHEMERAL_PATH = "docs/feedback/"  # 소멸성 채널 — 인용원이 될 수 없다 (agrtls-practices-review P)
SPECIALIZATION_KEY = "specializationOf"  # frontmatter 키 — 분할 조각 → 원 청크 (p10-split-keeps-work-identity)
SPECIALIZATION_GATE = getattr(kb_lib, "SPECIALIZATION_GATE", "specialization")  # 게이트 id — FAIL [specialization] (정의처 kb_lib)
LINK_STATE_CANDIDATE = getattr(kb_lib, "LINK_STATE_CANDIDATE", "candidate")  # 후보 — extract_refs 가 낸다 (정의처 kb_lib)
LINK_STATE_CONFIRMED = getattr(kb_lib, "LINK_STATE_CONFIRMED", "confirmed")  # 확정 — frontmatter 링크 (정의처 kb_lib)
SPACE_GATE = getattr(kb_lib, "SPACE_GATE", "space")  # 게이트 id — FAIL [space] (정의처 kb_lib)
SPACE_TYPE = getattr(kb_lib, "SPACE_TYPE", "agt:Space")    # `-space` 청크의 type — plane 이 아니라 클래스다 (p9-candidate-storage)
SPACE_LEVEL = getattr(kb_lib, "SPACE_LEVEL", "logical")    # 후보·제약·배제 근거가 사는 수준 (6.4절 수준 허용표)



PLANE_CLASS = {
    "requirement": "agt:RequirementChunk",
    "decision": "agt:DecisionChunk",
    "contract": "agt:ContractChunk",
    "schema": "agt:SchemaChunk",
    "artifact": "agt:ArtifactChunk",
    "annotation": "agt:AnnotationChunk",
    "memory": "agt:MemoryChunk",
}
# plane 이름 → agt:...Chunk 클래스의 사상(mapping)이다. defs/kb.bzl 은 Starlark 라 클래스 이름을 모르므로 이 표는
# defs/kb.bzl 에 없고 여기가 정의처다(M1 단일 정의처, 2026-09-26 — 아래 PLANES 파생과 같은 결정). 대신 이 표의 키
# 집합은 defs/kb.bzl 의 PLANES 와 같아야 하므로 apply_plane_level_state 가 로드 시점에 단정한다.

_KB_BZL_LIST = re.compile(r"^\s*(LEVELS|PLANES|STATES)\s*=\s*(\[[^\]]*\])", re.M)  # kb_lib.load_residency 와 같은 수법





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
```
<!-- 인용 끝 -->
