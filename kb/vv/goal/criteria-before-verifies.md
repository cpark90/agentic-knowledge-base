---
id: https://agentic-knowledge-base.dev/id/chunk/73d83879-75e4-43f9-a07a-4335711e2ac1
type: requirement
level: functional
pattern: ubiquitous
title_ko: 합격 기준 없는 verifies 링크는 거부되어야 한다
title: A verifies link without pass criteria must be rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-10-06T11:23:25+09:00}
verified: [{by: vnv/claude-sonnet-5-5, at: 2026-10-06T11:23:25+09:00}]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/63f17c2d-3fdf-4fd0-b05a-ca7b6b89ce46]
---
**검증 목표** — 합격 기준이 검증기와 별도 청크로 존재하고 `verifies` 링크에 바인딩된다는 결정이 verify 실행 계층의 게이트로 강제된다는 것이 보여져야 한다. 기준 없는 `verifies`는 저장소에 들어올 수 없다.

- **이해관계자**: 검증 역할 · 감사 역할 · **관심사**: 판정의 형식화

**무엇을 관측하면 성립하는가**

- `verifies`의 주어가 `agt:ContractChunk`를 `refines` 하지 않으면 verify 질의 `verifies-without-criteria`가 행을 내고 `//kg:gate_test`가 `FAIL [verify]`로 거부한다.
- 커밋된 `verifies` 링크 전부의 주어가 합격 기준을 `refines` 하고 `//kg:gate_test`가 PASS다.
- 감사 보고서의 "기준 없는 `verifies`" 수가 0이고 그 정의가 verify 질의와 같다.

판정의 원본은 `tools/verify-queries/verifies-without-criteria.rq`이고 실행은 `tools/validate.py`의 `check_verify`다.
