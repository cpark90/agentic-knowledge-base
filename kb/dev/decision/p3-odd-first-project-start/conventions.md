---
id: https://agentic-knowledge-base.dev/id/chunk/5934a9c4-3590-4cf8-8aec-1964e0c921b4
type: decision
level: concrete
title_ko: 규범 문서 규약 — 새 프로젝트는 ODD 작성으로 시작하고 5단계를 거친다
title: Normative-document conventions — A project starts by writing its ODD, in five steps
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/dc652ea1-791f-4fc8-bdb6-8862023ca380
---
**규약** — `p3-odd-first-project-start`의 결론을 규범 문서에 싣는 문장이다.

규약: 2 | **ODD 작성** | 조건 3분류·판정 방법·등급, 명시 제외 | ODD가 비면 스코프가 잘리지 않고 가정이 참조할 속성이 없다 — **체계 전체가 정지한다** (d-0063) | [§2](#2-odd-작성)
규약: ODD 작성 | 조건마다 객관적 판정 방법과 등급 A~C · 5단계 절차의 마지막(실제 조건 대조)에서 이탈 0 (d-0063)
규약: 프로젝트가 의존하는 조건을 **정적 요소 / 환경 조건 / 동적 요소** 3갈래로 열거한다.
규약: 현재 **실제 조건이 ODD 안에 있는지 대조**한다. 명령은 `bazel run //tools:odd_check`다 (`CHECKS.cmd`, 3.5절). 첫 모니터링에서 이탈이 나오면 틀린 쪽은 현실이 아니라 ODD다.
