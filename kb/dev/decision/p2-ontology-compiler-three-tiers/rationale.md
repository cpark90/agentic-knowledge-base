---
id: https://agentic-knowledge-base.dev/id/chunk/2ef92011-1d5a-4f71-931f-fa142c25c823
type: decision
level: logical
title_ko: 게이트를 질의로 쓰면 규칙이 데이터가 되고, 직렬화가 흔들리면 무효화 판정이 오염된다
title: Gates as queries; unstable serialization poisons invalidation
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/33d988f2-27b2-44d7-98f2-110215bfe237
---
**근거** (노트 2.5절) — 게이트를 코드로 구현하면 규칙마다 구현체가 생기고 규칙 목록이 어디에도 없다. SPARQL 질의로 쓰면 규칙 자체가 데이터가 되어 세어지고, 검토되고, 어느 결정에서 왔는지 링크된다. 2.12절 메모리 시스템 사례에서 "accepted인데 rationale이 없는 결정"을 질의로 잡은 것이 같은 방식의 실증이다.

세 계층은 잡는 것이 다르다 — 스타일은 사람이 읽을 수 없는 것을, 안티패턴은 이 체계가 금지한 것을, 추론기는 논리적으로 불가능한 것을 잡는다. 어느 하나로 나머지를 대신할 수 없다.

직렬화 순서가 불안정하면 git diff가 의미 없는 변경으로 가득 차고, 6.5절 무효화 판정의 입력(무엇이 실제로 변했는가)이 오염된다.
