---
id: https://agentic-knowledge-base.dev/id/chunk/b36581f8-2688-46dc-9b44-3e1019a37d66
type: decision
level: concrete
title_ko: 가정이 깨지면 의존 항목이 자동으로 무효화된다
title: Breaking an assumption invalidates every dependent item automatically
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/e5c0cbc6-cabf-4594-8733-fa2e045f1249, https://agentic-knowledge-base.dev/id/chunk/e0d0bf5c-8c1c-4638-9f64-89f94185d366]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0007]
part_of: https://agentic-knowledge-base.dev/id/composite/db06ba12-f04a-45c7-b5e3-d26d97dc7e51
composite: {id: https://agentic-knowledge-base.dev/id/composite/db06ba12-f04a-45c7-b5e3-d26d97dc7e51, title_ko: 가정과 무효화, title: Assumptions and invalidation}
---
**결론** — 각 지식 항목은 **참이라고 전제한 조건들 위에 서 있다.** 그 조건이 `agt:Assumption`이며 온톨로지 개념에 대한 명제로 표현된다. 조건은 0.4절의 세 갈래(정적 요소·환경 조건·동적 요소)로 분류되고 **각 조건은 객관적 판정 방법을 동반한다.** 가정은 **청크 단위**로 붙는다 (4.4절).

**가정이 깨지면 그 가정에 의존하는 모든 항목이 자동으로 무효화 표시된다.** 전수조사가 필요 없다 — 어떤 가정이 깨졌는지만 판정하면 무효 범위가 계산된다. 청크의 상태는 셋이다.

- `valid` — 모든 가정이 참. 그대로 사용
- `invalidated` — 가정 하나 이상이 거짓. 재검토 대상이며 읽을 때 경고
- `unverified` — 판정 불가. 검사 대상

무효화는 5.2절 단방향 규칙을 따라 전파되며 **삭제가 아니다.**
