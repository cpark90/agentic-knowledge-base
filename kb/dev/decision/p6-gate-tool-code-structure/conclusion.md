---
id: https://agentic-knowledge-base.dev/id/chunk/9571ac2c-659c-43b8-a82e-08f1e41f5f09
type: decision
level: concrete
title_ko: 게이트 도구는 규약 상수를 단일 정의처에서 읽고 검사를 독립 함수로 둔다
title: Gate tools read convention constants from a single definition site and keep each check an independent function
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a, https://agentic-knowledge-base.dev/id/chunk/90fc2df7-0a74-43fe-9c8f-546c7afdf1d3]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:14:21+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/d36b748b-cc0d-46c5-9df7-7d05708e3cd1
composite: {id: https://agentic-knowledge-base.dev/id/composite/d36b748b-cc0d-46c5-9df7-7d05708e3cd1, title_ko: 게이트 도구의 코드 구조, title: Gate tool code structure}
---
**결론** — 게이트 도구(`tools/*.py`)의 코드 구조 규약은 둘이다(2026-09-01 저장소 구축 때의 손 문서 `STYLEGUIDE.md` §7, 커밋 `4414911`).

1. **[지킴]** 규약 상수의 단일 정의처는 `tools/kb_lib.py`다. 다른 파일에 복제하지 않는다. 대상은 접미사·네임스페이스·종료 코드·빈 값 표기·생성 문서 규약의 상수 같은 값이다.
1. **[권장]** 새 검사는 독립 함수 `check_*() -> list[str]`로 추가하고 `main`에서 합류한다. 검사 사이에 결합을 만들지 않는다.

단일 정의처는 값이 한 자리에 적힌다는 뜻이다. 그 자리가 `kb_lib` 밖인 경우가 둘이다.

| 값 | 적힌 자리 | `kb_lib`의 몫 |
|---|---|---|
| 게이트 id 등록부 `GATES`(2026-10-02) · 수준 허용표 `RESIDENCY` · 방출 경계 `EXTRACTED_SOURCES` · 치역 경계 `USES_TARGETS` | `defs/kb.bzl`의 리터럴 | 리터럴을 읽어 파생한다. `load_gates`가 적재 시점에 `<이름>_GATE` 상수를 만든다 |
| 본문 떼기·토큰 계수기·`PLANES`·`LEVELS`·`STATES` 리터럴 읽기 | `tools/chunk2kg.py` | 이름을 다시 내보낸다 |

손으로 둔 `*_GATE` 상수는 없다. 게이트 `gate-registry`(`validate`)가 코드의 게이트 태그 집합과 `GATES`의 일치를 판정하고, `defs/kb.bzl`의 `check_gates`가 리터럴의 자기 정합성을 로드 시점에 판정한다.
