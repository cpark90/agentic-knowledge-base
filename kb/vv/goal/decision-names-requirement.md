---
id: https://agentic-knowledge-base.dev/id/chunk/9252388a-5087-4055-9897-47c39ea77588
type: requirement
level: functional
pattern: event-driven
title_ko: 결정은 refines·serves 로 어느 요구의 어느 관심사에 기여하는지 명시해야 한다
title: A decision must state through refines or serves which requirement and which concern it serves
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:30:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/57a2dca5-8628-4255-a964-9928d2fd14a4]
---
**검증 목표** — 결정의 `refines` 도착점이 요구여야 한다는 결정이 링크 규칙과 그래프 귀속 계산으로 강제되고, 명시하지 않은 살아 있는 결정이 잔여로 드러난다는 것이 보여져야 한다. 요구는 본문에 `**관심사**` 를 적으므로 요구를 가리키는 것이 곧 관심사를 가리키는 것이다.

- **이해관계자**: 프로젝트 · **관심사**: 정제 완주

**무엇을 관측하면 성립하는가**

- `serves` 의 대상이 요구가 아니면 분석 시점에 실패한다(`defs/kb.bzl` 의 `serves 의 대상은 requirement 뿐이다`).
- 살아 있는 결정마다 `refines`·`serves` 연쇄가 요구에 닿는다. `metrics` 의 후방 추적 귀속 잔여에 결정이 없다. deprecated 결정은 이력이라 대상이 아니다.
- CQ-13 이 결정마다 functional 조상(요구)을 낸다.
- 모든 요구 청크의 본문에 `**이해관계자**`·`**관심사**` 줄이 있다.

판정의 원본은 `defs/kb.bzl` 의 `_check_links`, `tools/metrics.py` 의 `reaches_req`, `tools/cq-queries/CQ-13.rq` 다.
