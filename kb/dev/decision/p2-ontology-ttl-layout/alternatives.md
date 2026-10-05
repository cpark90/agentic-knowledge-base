---
id: https://agentic-knowledge-base.dev/id/chunk/88900112-99fd-4524-9bf4-aa7321ef5222
type: decision
level: logical
title_ko: 비교한 대안은 없고 정규 직렬화는 주석을 지워 손 저작 꼴이 되지 못한다
title: No alternative was compared, and the canonical serialization erases comments so it cannot serve as the hand-authored form
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/aa03212b-6699-4c65-bbc8-0f9836401c6d
---
**대안 없음** — 2026-09-01 규약 제정 때 다른 꼴을 비교한 기록이 없다.

같은 저장소의 정규 직렬화(`tools/canonicalize.py`)는 손 저작 꼴의 대안이 되지 못한다. 그 정규형은 술어를 `rdf:type` 다음 이름순으로 정렬하고, `--write`로 다시 쓰면 주석이 사라진다(도구 docstring). 배너 주석이 지워지고 술어 순서가 이 결정의 순서와 달라진다.
