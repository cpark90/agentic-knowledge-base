---
id: https://agentic-knowledge-base.dev/id/chunk/20969ebb-5e05-4d3f-aa10-5f97219f896f
type: decision
level: logical
title_ko: 도입 2단계 조건이 앵커별이므로 검사 범위를 앵커가 있는 뷰로 맞춘다
title: The stage-two condition is per anchor, so the check covers only anchored views
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T14:33:11+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/e341786c-ca43-4e4f-bea4-83b4719901ae
---
**근거** — 요구 `context-budget`은 작업 집합이 예산 안에 든다고 정하는데 2026-09-22까지 그것을 강제하는 것이 없었다. 그날의 실측에서 `tools/workset.py`는 예산을 넘어도 종료 코드 0을 내고 머리에 "예산 초과" 한 줄만 적었다. 앵커 없는 기본 뷰는 684줄로 예산 200줄을 넘었고, 앵커를 준 뷰는 예산 안이었다.

- **조건의 문언과 검사 범위가 일치한다.** 도입 2단계 구체화 조건은 "역할·작업(앵커)별 작업 집합 ≤ 예산"이다(`p14-stage-pass-conditions`, `p0-workset-anchor-neighbourhood`). 앵커가 있을 때만 판정하면 이 조건이 `bazel test` 안으로 들어온다.
- **기본 빌드가 깨지지 않는다.** `p0-workset-anchor-neighbourhood`는 앵커 없는 요청에 접힌 라벨 목록만 준다고 정한다. 그 뷰는 양을 거르지 않으므로 예산 판정의 대상이 아니다.
- **비용이 가장 작다.** `tools/workset.py`의 한 갈래와 `docs/tools.md` 총람 한 행이다.

유저가 2026-09-22에 선택지 1을 골랐고 orchestrator 권장안과 같다. 구현은 2026-09-29에 들어왔다. 예산의 단위는 2026-10-01 유저 답으로 줄에서 토큰으로 바뀌었고(`p1-chunk-unit-is-tokens`) 판정의 형태는 그대로다.
