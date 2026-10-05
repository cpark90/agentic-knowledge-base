---
id: https://agentic-knowledge-base.dev/id/chunk/71434736-edb4-4a64-8fe1-b17df12acae7
type: decision
level: logical
title_ko: 스코프 없는 역할은 무엇의 부분집합인지 말할 수 없고 2026-09-13에 이 규약이 게이트가 됐다
title: A role without a scope cannot say what it is a subset of, and the convention became a gate on 2026-09-13
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T18:33:13+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/ec6c636d-2b87-4b60-b355-4ff49437f478
---
**근거** — 초판(2026-09-01)의 문구가 이유를 적는다. 스코프는 ODD 조건의 부분집합에 plane 권한을 더한 것이다(노트 0.4절, `p11-agent-catalog-derives-scope`). 스코프 없는 역할은 무엇의 부분집합인지 말할 수 없다. 노트 0.4절의 관계는 `agt:Harness --grants--> agt:Scope`와 `agt:Scope --subsetOf--> agt:ODD`다. 역할이 ODD에 닿는 길은 스코프 하나다. 산문은 `agt:grants`를 하네스가 스코프를 담아 에이전트에게 주어지게 하는 관계로 읽고 술어 이름은 그대로 둔다(유저 답 Q17-b·Q18-a(2026-10-03)).

2026-09-13에 규약이던 것을 게이트로 올렸다(`validate.check_catalog` docstring). 첫 실행은 역할 4 · 스코프 4 · FAIL 0이었다. 대응을 슬러그로 푸는 까닭은 카탈로그에 역할→스코프 술어가 없기 때문이다(`kb_lib`의 `ROLE_ID_PREFIX` 주석).

미확정: 역할→스코프 술어를 두지 않고 슬러그 대응을 고른 이유는 기록에서 확인하지 못했다.
