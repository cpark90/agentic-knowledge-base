---
id: https://agentic-knowledge-base.dev/id/chunk/e79c780e-4a2d-4bb4-b36b-65fe33b906f2
type: decision
level: logical
title_ko: 링크의 높이를 churn 위로 올려야 리팩터링이 재판정을 부르지 않는다
title: Links must sit above the churn so that refactoring does not trigger re-judgement
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-30T14:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/b9ff4ae2-fb83-447d-9aae-73d5264cfae3
---
**근거** — 재판정은 링크 양 끝의 해시 변경에서 온다(`revalidate`). 함수 청크마다 링크가 붙으면 함수 하나를 고칠 때마다 그 링크가 재판정 후보가 되고, 함수 수십 개를 옮기는 리팩터링은 수십 건의 후보를 낸다. 링크를 파일 복합체에 두면 함수의 해시 변경이 링크의 끝을 건드리지 않는다 — 복합체의 정체성(IRI)은 부분이 바뀌어도 같다.

생성물에는 손으로 쓸 자리가 없다는 사실도 같은 답을 가리킨다. 함수 청크는 추출기가 다시 만들므로 거기 적은 링크는 지워진다. 사람이 쓰는 지식은 생성되지 않는 자리 — 등록부·선언 파일 — 에 있어야 하고 그 자리는 파일 단위다.

절 복합체를 두는 까닭은 7±2다. 파일 하나가 함수 68개를 직접 부분으로 가지면 복합체 규칙(≤ 9)을 어기고 읽히지도 않는다. 소스의 절 주석은 저작자가 이미 뜻을 둔 묶음이므로 그것을 쓰고, 없으면 만들게 한다 — 그것이 코드 쪽의 유일한 저작 요구다.
