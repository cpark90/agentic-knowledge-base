---
id: https://agentic-knowledge-base.dev/id/chunk/307c5bf0-9888-4c3f-a0af-3ea265d47699
type: decision
level: concrete
title_ko: 규범 문서 규약 — 게이트 도구는 규약 상수를 단일 정의처에서 읽고 검사를 독립 함수로 둔다
title: Normative-document conventions — Gate tools read convention constants from a single definition site and keep each check an independent function
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:14:21+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/d36b748b-cc0d-46c5-9df7-7d05708e3cd1
---
**규약** — `p6-gate-tool-code-structure`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 규약 상수의 단일 정의처는 `tools/kb_lib.py`다. 다른 파일에 복제하지 않는다. 값이 `kb_lib` 밖에 적히는 자리는 둘이다. 분석 시점에 쓰이는 표(`GATES`·`RESIDENCY`·`EXTRACTED_SOURCES`·`USES_TARGETS`)는 `defs/kb.bzl`의 리터럴이고 `kb_lib`이 읽어 파생한다. 본문 떼기·토큰 계수기·`PLANES`·`LEVELS`·`STATES` 리터럴 읽기는 `tools/chunk2kg.py`에 있고 `kb_lib`이 이름을 다시 내보낸다.
규약: [권장] 새 검사는 독립 함수 `check_*() -> list[str]`로 추가하고 `main`에서 합류한다.
