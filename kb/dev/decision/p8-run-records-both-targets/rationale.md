---
id: https://agentic-knowledge-base.dev/id/chunk/b536dca6-6753-4ec2-867b-cbace3ccd949
type: decision
level: logical
title_ko: 대체 결정은 실행 기록 문장을 기각하지 않고 옮기지 않았다
title: The superseding decision did not reject the run-record sentence; it did not carry it over
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T17:45:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/e182245c-43fd-46de-819d-cb809a20aa8e
---
**근거** (노트 8.8절 `[확정]`, 8.25절) — 이 문장은 `p8-two-verification-targets`의 근거 청크에 있었다. 그 결정을 대체한 `p8-agent-verification-target`은 "검증 대상 둘이라는 구분은 그대로 남는다"고 적고, 없어지는 것을 도착점의 종류가 둘이라는 부분으로 한정한다. 실행 기록과 요인 분류의 문장은 그 대체의 근거·대안 어디에서도 기각되지 않았다. 옮겨지지 않았을 뿐이다.

- 요인과 대상의 대응은 `p8-agent-vv`의 표와 일치한다 — 제품 V&V의 결함은 실행 요인 위주, 에이전트 V&V의 결함은 인지 요인 위주다.
- 실행 기록은 concrete 전용 append-only 관측이다(`p0-run-as-observation`). 관측 시점에는 결함의 귀속이 정해지지 않으므로 귀속은 사후의 판정이다.

미확정: 상호작용 요인의 귀속은 노트 8.8절이 적지 않았다.
