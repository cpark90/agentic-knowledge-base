---
id: https://agentic-knowledge-base.dev/id/chunk/3cbdac9a-dbb5-4378-bb0f-89231dd05cd4
type: decision
level: concrete
title_ko: 작업 집합의 예산 초과는 앵커가 있을 때만 빌드를 실패시킨다
title: Exceeding the workset budget fails the build only when an anchor is given
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/45f9ad28-7bf6-4267-87f0-271ca83fae5a]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T14:33:11+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/e341786c-ca43-4e4f-bea4-83b4719901ae
composite: {id: https://agentic-knowledge-base.dev/id/composite/e341786c-ca43-4e4f-bea4-83b4719901ae, title_ko: 작업 집합 예산의 강제, title: Enforcing the workset budget}
---
**결론** — 작업 집합 뷰의 예산 판정은 **앵커가 주어졌을 때만** 게이트다(유저 답 2026-09-22, 선택지 1).

- 앵커가 있으면 뷰 문서 전체(라벨 목록과 펼친 본문)를 예산과 비교한다. 넘으면 `FAIL [workset-budget]`을 내고 종료 코드 1로 빌드를 실패시킨다.
- 앵커가 없으면 예산 판정을 하지 않는다. 뷰의 머리에 판정 한 줄만 적고 종료 코드는 0이다. 앵커 없는 뷰는 스코프 전체의 라벨 목록이라 구조적으로 예산을 넘는다.
- 기본 설정의 `//kg:workset` 빌드는 앵커가 비어 있으므로 깨지지 않는다. 판정은 `bazel build //kg:workset --//kb:anchor=<IRI|라벨 부분>`이 종료 코드로 한다.
- 예산의 값은 이 결정이 정하지 않는다. 값은 `p1-chunk-unit-is-tokens`가 정하고 단일 정의처는 `kb_lib.CONTEXT_TOKEN_BUDGET`이다.

구현은 `tools/workset.py`이고 게이트 id는 `workset-budget`이다(`docs/tools.md` 총람).
