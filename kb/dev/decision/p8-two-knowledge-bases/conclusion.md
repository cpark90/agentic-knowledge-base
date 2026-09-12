---
id: https://agentic-knowledge-base.dev/id/chunk/af618b63-841a-4c19-a935-62ec246c2218
type: decision
level: concrete
title_ko: 지식 베이스는 개발 KB와 V&V KB 둘이다
title: There are two knowledge bases - development and V&V
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/42fde00d-395f-4193-9eef-5c86f0d4abc7, https://agentic-knowledge-base.dev/id/chunk/71d2b786-e873-4705-b160-a443603ae0d2]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0130]
part_of: https://agentic-knowledge-base.dev/id/composite/ff2266a5-716f-41ad-a738-292aca41f27b
composite: {id: https://agentic-knowledge-base.dev/id/composite/ff2266a5-716f-41ad-a738-292aca41f27b, title_ko: 두 지식 베이스, title: The two knowledge bases}
---
**결론** — 지식 베이스는 둘이다. **개발 KB**는 요구에서 실산출물을 생산하기 위한 지식이고, **V&V KB**는 요구와 산출물의 전 과정에 연동되어 **시나리오 기반 확인**를 수행하는 지식이다. 둘은 같은 코어(청크·plane·level·링크)과 같은 기반(온톨로지·ODD)을 쓰되 **저장·스코프·편집 주체가 분리된다.**

- 답하는 질문 — 무엇을 만들 것인가·왜 그렇게 / 만든 것이 요구를 충족하는가·요구가 맞는가
- 계층의 출발과 도착 — 요구 → 구현 산출물 / **검증 목표**(요구에서 파생) → 검증기 + 실행 기록
- 핵심 개체 — 결정·계약·스키마·산출물 / **시나리오**·합격 기준·케이스·검증기·관측·결함
- 편집 주체 — 설계·개발 역할 / V&V·감사 역할 (**개발 역할은 읽기만**)
- 링크 방향 — 자기 안에서 `refines`·`satisfies` / **V&V → 개발** 방향으로만 `verifies`·`derives-from`
