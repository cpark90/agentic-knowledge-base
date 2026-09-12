---
id: https://agentic-knowledge-base.dev/id/chunk/3895f5a0-161c-4e22-82a8-f810684bf94c
type: decision
level: logical
title_ko: 전파 알고리즘의 자체 구현
title: Implementing propagation ourselves
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/560ccdfa-94a3-4a43-bc41-3697c44b69cc
---
**대안** `[안]` — 후보 링크의 도메인 축소는 **호 일관성(arc consistency)** 검사이고, 새 제약 도입 시 영향받는 변수만 다시 검사하는 증분 방식이 이미 성숙해 있다. **자체 구현하지 않고 기성 알고리즘을 쓴다** — 아직 미확정 제안이며, 채택 시에도 이 결정의 실행 시점 규칙은 그대로 적용된다.
