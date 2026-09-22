---
id: https://agentic-knowledge-base.dev/id/chunk/d51e72cb-5403-44ca-b01d-7512b04adcb7
type: requirement
level: functional
pattern: ubiquitous
title_ko: 모든 산출물은 refines 연쇄로 요구까지 거슬러 오르고 오르지 못하는 것은 세어져야 한다
title: Every artifact must trace back to a requirement through the refines chain and the untraced ones must be counted
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:30:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
---
**검증 목표** — 후방 추적 커버리지가 요구 귀속의 지표라는 결정이 그래프에서 생성되는 수치 하나로 성립한다는 것이 보여져야 한다. 분자는 `refines`·`serves` 연쇄(복합체 형제 포함)로 요구에 닿는 비요구 청크, 분모는 살아 있는 비요구 청크 전부다.

- **이해관계자**: 프로젝트 · **관심사**: 정제 완주

**무엇을 관측하면 성립하는가**

- `bazel build //kg:metrics` 의 `정제 완주 (CQ19) · 후방 추적 귀속 (CQ20)` 절에 `요구로 거슬러 오르는 비요구 청크: n/d = p.p%` 가 있고 `(목표 100.0%)` 가 붙어 있다.
- CQ-13(`이 항목은 어느 상위에서 내려왔는가`)이 항목 × functional 조상 행을 내고, 한 항목을 `--bind` 하면 그 항목의 조상 목록이 나온다.
- 귀속되지 않는 산출물의 수가 `d - n` 으로 문서에서 읽힌다. 문서에 손으로 적은 수치는 없다.

판정의 원본은 `tools/metrics.py` 의 CQ20 절과 `tools/cq-queries/CQ-13.rq` 다.
