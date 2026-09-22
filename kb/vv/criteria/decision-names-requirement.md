---
id: https://agentic-knowledge-base.dev/id/chunk/e1cc9b56-b318-4f5a-8c98-4af5e9a655e7
type: contract
level: logical
title_ko: 살아 있는 결정 전부가 refines·serves 연쇄로 요구에 닿고 후방 추적 귀속의 잔여에 결정이 없어야 한다
title: Every live decision reaches a requirement through the refines and serves chain, and the backward-trace residue contains no decision
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:35:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/9252388a-5087-4055-9897-47c39ea77588]
---
**합격 기준** — 기준 종류는 **불변식**이다. `∀ d ∈ decision ∧ status(d) ≠ deprecated: reaches_req(d)` 이고 `reaches_req` 는 `refines ∪ serves` 의 상향 폐포에 같은 복합체의 형제를 더한 것이다(`tools/metrics.py` 의 `reaches_req`, 케이스 `backward-trace-to-requirement` 와 같은 정의). deprecated 결정은 이력이라 대상이 아니다. `serves(d) ⊆ requirement` 는 분석 시점 규칙이다.

**판정식**

- 양성(구조): `bazel test //defs/tests:plane_direction_test` 가 PASS 다. 결정이 하위 plane 을 `refines` 하는 고정물이 `plane 단방향 위반` 으로 실패할 때만 PASS 다.
- 양성(귀속): `bazel build //kg:metrics` 의 `후방 추적 귀속 (CQ20)` 절 `요구로 거슬러 오르는 비요구 청크: n/d = p.p%` 에서 잔여 `d − n` 을 이루는 청크에 `decision` plane 이 없다. 잔여의 정체는 그래프에서 `status ≠ deprecated ∧ ¬reaches_req` 로 센다.
- 양성(질의): `bazel build //kg:cq` 의 CQ-13 절이 결정 × functional 조상 행을 낸다. CQ-13 은 조상을 내되 상태를 거르지 않고 여집합을 내지 않으므로 잔여 판정의 원본은 `metrics` 다.
- 음성: `serves` 대상이 요구가 아닌 청크는 `serves 의 대상은 requirement 뿐이다 (6.8절)` 로 로드가 실패한다. 서술 표본이다. 고정물은 없다.

**등급** — B 다. 귀속 수치는 뷰가 내지만 잔여의 plane 대조는 사람이 한다. vv_run 은 종료 코드만 본다.

판정의 원본은 `tools/metrics.py`(`live`·`reaches_req`)와 `defs/kb.bzl` 의 `_check_links` 다. Bazel 의존 그래프 질의(`rdeps`)는 frontmatter 의 `status` 를 모르므로 deprecated 결정을 거르지 못해 쓰지 않는다. 잔여 중 살아 있는 결정만 없는 여집합 질의는 `tools/cq-queries/` 에 없다.
