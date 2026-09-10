---
id: https://agentic-knowledge-base.dev/id/chunk/e3ac8b70-f181-47ca-a124-a976ab0c4c9c
type: decision
level: concrete
title_ko: 개발 KB의 완결 조건은 정제 완주와 후방 추적 귀속 100%이고 완료는 V&V 상태를 읽어야 선언된다
title: Completion means 100% descent and ascription, and can only be declared by reading the V&V KB
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9, https://agentic-knowledge-base.dev/id/chunk/71d2b786-e873-4705-b160-a443603ae0d2]
composite: {id: https://agentic-knowledge-base.dev/id/composite/c831629d-706d-4d61-90e5-f4d848758731, title_ko: 개발 KB의 완결과 완료 판정, title: Completion of the development KB}
part_of: https://agentic-knowledge-base.dev/id/composite/c831629d-706d-4d61-90e5-f4d848758731
---
**결론** — 개발 KB의 완결 조건은 하나다: **모든 요구가 executable까지 `refines` 연쇄로 닿고, 모든 산출물이 요구로 거슬러 오른다** (CQ19·CQ20). 전방 추적 커버리지·후방 추적 커버리지이 100%가 아니면 개발 KB는 열려 있다 (노트 7.1절).

요구 하나가 "끝났다"의 정의 (7.9절):
1. `refines` 연쇄가 requirement → decision(abstract·logical·concrete) → artifact로 닿음
2. 계약이 구현보다 먼저 확정됨
3. 결정 복합체에 대안 청크가 있음
4. 모든 청크의 가정이 `stable`
5. V&V KB에 검증 목표·기준·verifier가 있고 `verifies`가 유효 — **개발 KB만으로는 완료를 선언할 수 없다**
