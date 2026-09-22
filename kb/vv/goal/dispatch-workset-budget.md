---
id: https://agentic-knowledge-base.dev/id/chunk/7a0e2c24-70d8-4d00-ae0f-d083b8ec87a8
type: requirement
level: functional
pattern: event-driven
title_ko: dispatch 에 전달되는 작업 집합은 역할 스코프와 수준 창과 앵커로 걸러져 예산 안이어야 한다
title: The workset handed to a dispatch must be filtered by role scope, level window and anchor and fit within the budget
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:30:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af]
---
**검증 목표** — 작업 집합이 스코프 × 수준 창 × 앵커 이웃으로 거른 청크 집합이고 앵커가 양을 거른다는 결정이 뷰 하나로 성립한다는 것이 보여져야 한다. 뷰의 선택자는 빌드 설정이고 BUILD 를 고치지 않는다.

- **이해관계자**: 에이전트 · **관심사**: 좁은 관측

**무엇을 관측하면 성립하는가**

- `bazel build //kg:workset --//kb:role=<역할> --//kb:anchor=<라벨>` 이 카탈로그 역할의 읽기·쓰기 plane 과 수준 창으로 살아 있는 청크를 거르고 앵커의 1홉 이웃 본문만 펼친다.
- 머리의 `예산 판정` 줄이 `합계 N줄 / 예산 200줄 → 예산 안` 이다.
- 스코프 밖 plane 의 청크는 라벨 목록에도 없다. 라벨 목록은 `scope: <역할>   conditions: …   window: …` 줄로 시작한다.
- `metrics` 가 역할·앵커별 예산 준수율을 낸다(`2단계 대리` 절).

판정의 원본은 `tools/workset.py`, `defs/kb.bzl` 의 `kb_workset_view`, `kg/catalog-kg.ttl` 의 `agt:reads`·`agt:writes` 다.
