---
id: https://agentic-knowledge-base.dev/id/chunk/3a2355b4-bcf0-5b08-b129-ae149404c3b4
type: decision
level: logical
title_ko: 논리 시나리오 요인 — 앵커를 준 vnv 작업 집합 뷰의 예산 판정이 노출하는 현상
title: Logical scenario factors — the phenomena exposed by the budget verdict of the anchored vnv workset view
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T22:46:33+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/753f40c0-a1f4-5fcc-a1ae-e7b5961e4e18
---
**요인** — 노출하려는 현상은 `agt:worksetBudgetOverrun` 하나다. 작업 집합이 컨텍스트 예산을 넘는 것이 이 시나리오의 결함 형태다. 표본 근거는 요인 주입 하나다. 변수 `budget`에 keep 밖 값 `10`을 주입해 케이스 하나를 낸다. 예산 10은 이 앵커의 라벨 목록 길이보다 작아 몸통을 펼치기 전에 초과가 확정된다. 몸통 패킹의 근사 검사는 편입 항목마다 최대 한 단위만 초과시키므로 근접한 예산으로는 초과가 결정적이지 않다. vnv는 읽기 plane이 셋뿐이라 스코프 거름이 가장 눈에 띄는 역할이다. 기여하는 검증 목표는 `kb/vv/goal/dispatch-workset-budget.md`(`https://agentic-knowledge-base.dev/id/chunk/7a0e2c24-70d8-4d00-ae0f-d083b8ec87a8`)다.
