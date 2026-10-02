---
id: https://agentic-knowledge-base.dev/id/chunk/ed84261a-c592-4e50-85bf-80613f78957e
type: decision
level: logical
title_ko: 양방향 편집은 드리프트이고 잦은 변경에는 코드 편집을 그대로 두는 쪽이 강인하다
title: Bidirectional editing is drift, and under frequent change the robust choice leaves code editing untouched
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-30T14:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/cfdffdf2-c863-4f22-bdfc-2d58e26550be
---
**근거** — 문학적 프로그래밍의 역사적 실패는 tangle된 파일을 직접 고치면 원본에 반영되지 않는다는 데 있다. 양방향 편집을 허용하면 잦은 변경이 곧 드리프트다. 방향은 하나여야 하고 드리프트 게이트가 그것을 강제해야 한다 — 이 저장소가 BUILD·SKILL.md에 이미 쓰는 형식이다.

유저의 조건은 "최적화 전까지 변경이 무척 잦다"이다. tangle이면 코드 편집이 청크 파일 편집이 되어 에디터·타입 체커의 경험이 나빠지고, 추출이면 코드 편집이 그대로다. 그래서 추출이다. 생성물이므로 함수를 고치면 청크가 다시 생성될 뿐이며, 손으로 쓰는 지식(링크·가정)은 움직이지 않는 자리에 둔다.

도장을 테스트 통과로 두는 까닭은 "검증 뒤 내용을 고치면 거부한다"가 코드에 매번 걸리기 때문이다. 판정 주체가 사람에서 검증기로 바뀔 뿐 게이트가 약해지지 않는다 — 코드의 판정 도구는 처음부터 타입 체커·테스트였다(`p7-dev-plane-substance`).

표본을 먼저 재는 까닭은 실패의 범위다. 34 파일을 한 번에 올려 churn이 감당되지 않으면 되돌릴 것이 수백 청크이고, 한 파일이면 한 파일이다.
