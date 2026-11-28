---
id: https://agentic-knowledge-base.dev/id/chunk/e79c780e-4a2d-4bb4-b36b-65fe33b906f2
type: decision
level: logical
title_ko: 링크의 높이를 churn 위로 올려야 리팩터링이 재검증을 부르지 않는다
former_title_ko: ["링크의 높이를 churn 위로 올려야 리팩터링이 재판정을 부르지 않는다"]
title: Links must sit above the churn so that refactoring does not trigger re-judgement
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-11-28T16:57:43+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b9ff4ae2-fb83-447d-9aae-73d5264cfae3
---
**근거** — 재검증은 링크 양 끝의 해시 변경에서 온다(`revalidate`). 함수마다 링크가 붙으면 함수 하나를 고칠 때마다 그 링크가 재검증 후보가 되고, 함수 수십 개를 옮기는 리팩터링은 수십 건의 후보를 낸다. 링크를 파일 항목에 두면 함수를 고쳐도 링크의 끝이 움직이지 않는다.

생성물에는 손으로 쓸 자리가 없다는 사실도 같은 답을 가리킨다. 추출기가 다시 만드는 항목에 적은 링크는 지워진다. 사람이 쓰는 지식은 생성되지 않는 자리 — 등록부·선언 파일 — 에 있어야 하고 그 자리는 파일 단위다.

함수와 절을 부분으로도 두지 않는 까닭은 링크가 파일에만 있다는 이 결론 자체에 있다. 부분은 링크를 갖지 못하므로 그래프에서 어느 결정에도 닿지 않고, 원문은 소스에 그대로 있다. 그래서 부분을 생성해 유지하는 비용, 곧 추출기의 부분 수 검사와 절 주석 요구, 부분 링크 게이트는 얻는 것이 없다. 유저가 이를 받아들였다(Q191-a).
