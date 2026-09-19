---
id: https://agentic-knowledge-base.dev/id/chunk/7e9efd2b-38fd-41d4-8e6a-a98dfc7f24bb
type: requirement
level: functional
pattern: ubiquitous
title_ko: 모든 항목은 가정을 명시하고 ODD 밖 조건을 참조하는 가정은 거부되어야 한다
title: Every item must declare its assumptions and an assumption referring outside the ODD must be rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T15:40:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/e5c0cbc6-cabf-4594-8733-fa2e045f1249]
---
**검증 목표** — 경계 셋(ODD·스코프·가정) 중 가정이 ODD 속성 위의 명제이고 ODD에 없는 속성을 참조하는 가정은 존재할 수 없다는 결정이 게이트로 강제된다는 것이 보여져야 한다. 살아 있는 청크는 전부 `assumes`를 갖는다.

- **이해관계자**: 프로젝트 · 감사 역할 · **관심사**: 경계와 갱신

**무엇을 관측하면 성립하는가**

- `agt:assumes`의 대상이 그래프에 주어로 없으면 `FAIL [dangling]`으로 거부된다.
- 가정의 `agt:refersTo` 대상이 ODD 그래프에 없으면 `FAIL [odd-ref]`로 거부된다.
- ODD의 모든 조건에 판정 방법과 등급이 있어 가정의 판정이 질의 하나로 환원된다. `//kb/odd:gate_test`가 PASS다.
- CQ-09(전제를 적지 않은 항목)의 행 수가 0이다.

판정의 원본은 `tools/validate.py`의 `check_dangling`·`check_odd_refs`와 `tools/cq-queries`의 CQ-09다.
