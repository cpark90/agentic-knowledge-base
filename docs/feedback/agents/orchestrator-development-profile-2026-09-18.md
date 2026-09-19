---
from: orchestrator
kind: notice
status: open
targets: [kb/ontology/profile/development/, kb/ontology/shapes/profile-development-shapes.ttl, kb/dev/decision/pe-anchor-is-bazel-label/conclusion.md, kb/dev/requirement/, docs/method.md, tools/chunk2kg.py]
---

# 첫 분야 프로파일 `development`와 구축 절차 — 기록 (2026-09-18)

유저 "계속해서 진행해줘"에 따라 로드맵 다음 산출 5를 수행했다. 프로파일의 내용은 결정(`p2-skeleton-and-domain-profile`·
`p7-dev-plane-substance`)이 이미 정했으므로 유저 판단 없이 진행했다.

- **모듈** `kb/ontology/profile/development/`(developer): 실체 하위 클래스 7(`RequirementStatement`…`SessionObservation`), 판정 도구 6 개체와
  `judgedBy` 바인딩(값 제약 `owl:hasValue` — punning은 rdfs 추론과 ChunkShape가 충돌해 8건 FAIL이라 이 형태), EARS 패턴 6 개체와
  `pattern` 속성, shape 1 파일. 게이트가 코어 재정의를 거부함을 음성 시험으로 확인.
- **바인딩**: `chunk2kg`가 plane을 실체 클래스로 타이핑하고 요구의 `pattern`을 방출한다. 요구 33건에 EARS 패턴을 채웠다(orchestrator —
  ubiquitous 16·event-driven 12·unwanted-behaviour 3·state-driven 1·complex 1). 사상표 `PROFILE_SUBSTANCE`는 head 액션이 rdflib 없이 돌아
  `kb_lib`이 아니라 `chunk2kg.py`에 있다 — 단일 정의처 규칙의 예외이며 docstring에 사유를 적었다.
- **결정 신설** `pe-anchor-is-bazel-label`(앵커 해석기 = Bazel 라벨, refines deterministic-notation).
- **절차** `method.md` §1을 실제 작업에서 뽑아 적었다 — 확장점 열거 → 결정에서 읽기 → 모듈 → 바인딩 → 역량 질문 → 완료 판정, 확장점 표.
- **역량 질문** CQ-33~36 등재(CQ-36: 각 plane의 청크는 무엇이고 무엇이 판정하는가 — 7행).
- 부수 정정: `CQ-05` 질의에 plane 보호 한 줄(실체 타이핑 뒤 231건 오탐), `kb_lib.resolve_glob`가 runfiles 사본을 제외, `roadmap.md`의 절 중복(09-13
  편집 사고) 제거.
- 남긴 것: 조건 셋째 수준(ODD 재배선 필요), 결함 하위 유형(코어 `defect` 모듈, V&V 7단계), `metrics`·`workset`·`community`가 첫 `rdf:type`을 plane으로
  읽는 취약점(지금은 정확 — 후속).

## hci에 전달
- 원장에 "첫 프로파일 development·구축 절차(2026-09-18)" 한 줄. 재판정 대상 없음(라벨 불변; 요구의 `pattern`은 frontmatter).

## 답
(hci가 채움)
