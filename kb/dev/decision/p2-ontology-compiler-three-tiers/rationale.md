---
id: https://agentic-knowledge-base.dev/id/chunk/2ef92011-1d5a-4f71-931f-fa142c25c823
type: decision
level: logical
title_ko: 게이트를 질의로 쓰면 규칙이 데이터가 되고, 직렬화가 흔들리면 무효화 판정이 오염된다
title: Gates as queries; unstable serialization poisons invalidation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-11-27T09:33:25+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-06T11:26:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-11-27T09:33:25+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/33d988f2-27b2-44d7-98f2-110215bfe237
---
**근거** (노트 2.5절) — 게이트를 코드로 구현하면 규칙마다 구현체가 생기고 규칙 목록이 어디에도 없다. SPARQL 질의로 쓰면 규칙 자체가 데이터가 되어 세어지고, 검토되고, 어느 결정에서 왔는지 링크된다. 2.12절 메모리 시스템 사례에서 "accepted인데 rationale이 없는 결정"을 질의로 잡은 것이 같은 방식의 실증이다.

세 단계는 잡는 것이 다르다 — 스타일은 사람이 읽을 수 없는 것을, 안티패턴은 이 체계가 금지한 것을, 추론기는 논리적으로 불가능한 것을 잡는다. 어느 하나로 나머지를 대신할 수 없다.

직렬화 순서가 불안정하면 git diff가 의미 없는 변경으로 가득 차고, 6.5절 무효화 판정의 입력(무엇이 실제로 변했는가)이 오염된다.

OBO Foundry에서 가져오는 것은 세 단계의 구조이고 ROBOT이라는 도구가 아니다(Q175-a). ROBOT의 `report`와 `verify`가 하는 판정은 `validate.py`의 검사와 `chunk_lint`, SPARQL verify 질의가 Python과 Bazel 게이트 안에서 한다. ROBOT을 쓰면 Java 런타임이 빌드 의존이 되고, 같은 규칙의 구현이 둘로 갈린다.
