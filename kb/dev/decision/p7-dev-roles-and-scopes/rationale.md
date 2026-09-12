---
id: https://agentic-knowledge-base.dev/id/chunk/eccd625d-df17-4583-bc3d-9de1867544e9
type: decision
level: logical
title_ko: 설계·구현·판정의 분리를 쓰기 권한으로 구조화한다
title: Design, implementation and judgement are separated by write permission
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/92f76b7c-3bd8-4e3c-a014-61c6aec60af4
---
**근거** (노트 7.7절, 11.2절, 8.5절) — 설계/구현/운영이 같은 write 스코프를 갖지 않는다(11.2절)는 원칙을 개발 KB의 plane에 적용한 것이다. V&V가 개발 KB에 `annotation`만 쓰는 것은 8.5절 독립성(V&V → 개발 방향 링크만)의 읽기·쓰기 면이다. developer의 읽기가 `decision` concrete로 제한되는 것은 후보가 여럿인 상태를 developer에게서 지우기 위함이며, 컨텍스트 예산(1.4절)에도 직접 기여한다.
