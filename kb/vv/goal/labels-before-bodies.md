---
id: https://agentic-knowledge-base.dev/id/chunk/d84aae5a-3190-44d7-9b27-02013b6b70b1
type: requirement
level: functional
pattern: event-driven
title_ko: 판단에 필요한 지식은 라벨 목록으로 먼저 보이고 본문은 요청된 것만 펼쳐져야 한다
title: Knowledge needed for a judgement must be shown first as a label list and bodies must be expanded only on request
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-10-04T22:47:55+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8]
---
**검증 목표** — 라벨이 청크의 인터페이스이고 에이전트가 라벨 목록을 먼저 받는다는 결정이 두 생성 뷰의 형태로 강제된다는 것이 보여져야 한다. 라벨 목록 뷰(`index`)는 본문을 담지 않고, 작업 집합 뷰(`workset`)는 앵커가 없으면 라벨만 낸다.

- **이해관계자**: 에이전트 · **관심사**: 좁은 관측

**무엇을 관측하면 성립하는가**

- `bazel build //kb/dev:index` 의 생성물이 청크마다 라벨·plane/level·상태·줄 수·복합체 여부만 적고 본문 줄을 싣지 않는다.
- `bazel build //kg:workset` 을 앵커 없이 돌리면 머리에 `펼침 0개` 와 본문을 펼치지 않는다는 문장이 있다.
- 앵커를 주면 1홉 이웃의 본문만 펼치고 나머지는 라벨로 남는다(케이스 `dispatch-workset-budget-factor-1`).
- 두 뷰 모두 `gendoc` 게이트의 입력이라 형태가 생성 전에 고정된다.

판정의 원본은 `tools/labels.py`, `tools/workset.py`, `BUILD.bazel` 의 `gendoc_test` 다.
