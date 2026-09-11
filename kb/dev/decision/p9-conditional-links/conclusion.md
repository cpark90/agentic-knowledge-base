---
id: https://agentic-knowledge-base.dev/id/chunk/2921c7a6-95a6-49b2-83d1-4b90bfd44c1a
type: decision
level: concrete
title_ko: 모든 링크는 when 술어를 가질 수 있고 상태는 조건의 평가 결과이며 assumes와 스코프 conditional은 그 특수형이다
title: Any link may carry a when predicate; state is its evaluation; assumes and scope conditionals are special cases
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/e0d0bf5c-8c1c-4638-9f64-89f94185d366, https://agentic-knowledge-base.dev/id/chunk/e5c0cbc6-cabf-4594-8733-fa2e045f1249, https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c]
composite: {id: https://agentic-knowledge-base.dev/id/composite/0b7abe3a-c03e-434f-b53b-b9d9d936a388, title_ko: 조건부 링크, title: Conditional links}
part_of: https://agentic-knowledge-base.dev/id/composite/0b7abe3a-c03e-434f-b53b-b9d9d936a388
---
**결론** — 후보 링크의 가능성은 두 축으로 구조화된다. **조건**(어떤 상태에서 가능한가)과 **증거**(무엇이 지지하고 반박하는가). 둘 다 수치가 아니다 (노트 9.11절).

모든 링크는 `when` 술어(CEL, ODD 속성·가정 위)를 가질 수 있다. 참이면 가능, 거짓이면 불가능, 판정 불가면 `unverified`. 링크의 상태가 저장된 값이 아니라 **조건의 평가 결과**가 된다 — 후보: 참 open / 거짓 eliminated(`eliminated_by: when`) / 판정 불가 open+unverified; 확정: 참 유효 / 거짓 **suspect** / 판정 불가 suspect.

이것이 6.5절 `assumes`의 일반형이다 — `assumes`는 "가정이 참일 때만 유효"라는 `when`, 3.4절 스코프 conditional은 "결정이 concrete일 때만 쓰기 허용"이라는 `when`. 셋이 한 메커니즘이고 무효화 전파(6.10절)는 `when`이 거짓이 된 링크를 따라가는 것이다. 조건이 ODD 밖 속성을 참조하면 게이트가 거부한다 (3.3절). 이 저장소: 어휘 `agt:when`은 지금, CEL 평가는 도입 5단계 (유저 결정 Q8·Q9).
