---
id: https://agentic-knowledge-base.dev/id/chunk/ad41a67a-a629-4c89-aa7c-c5fe933376c3
type: decision
level: concrete
title_ko: 규범 문서 규약 — 가정에는 판정 유형과 판정 식을 함께 적는다
title: Normative-document conventions — Every assumption records its verification kind and expression
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/674dc862-8a79-40df-a50e-9643d9caca63
---
**규약** — `p6-assumption-verification-methods`의 결론을 규범 문서에 싣는 문장이다.

규약: **가정을 판정한다.** 판정 유형과 판정 식이 가정과 함께 저장되어 있어야 한다 (d-0087). 판정 유형은 그래프 질의, 파일 검사, 실행 검사, 외부 조회, 사람 확인이다. 첫 형태는 `bazel run //tools:assume_check`다 — 판정식은 가정이 참조하는 ODD 조건 판정의 연언이고, `--break`가 인위 파괴 실험, `--record`가 관측 청크(memory plane) 기록이다 (2026-09-14).
