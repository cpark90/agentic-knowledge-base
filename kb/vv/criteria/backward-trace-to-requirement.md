---
id: https://agentic-knowledge-base.dev/id/chunk/1b595055-a384-4309-8946-800c67dd91d6
type: contract
level: logical
title_ko: 후방 추적 커버리지는 metrics 뷰가 refines·serves 연쇄로 세고 CQ-13 이 항목별 functional 조상을 낸다
title: Backward trace coverage is counted by the metrics view over refines and serves chains, and CQ-13 lists each item's functional ancestors
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:35:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/d51e72cb-5403-44ca-b01d-7512b04adcb7]
---
**합격 기준** — 기준 종류는 **명세 대조**다. `coverage = |{c ∈ live ∖ req | reaches_req(c)}| / |live ∖ req|` 이고 `reaches_req` 는 `refines ∪ serves` 의 상향 폐포에 같은 복합체의 형제를 더한 것이다(`tools/metrics.py` 의 `reaches_req`).

**판정식**

- 양성(수치): `bazel build //kg:metrics` 가 성공하고 `bazel-bin/kg/metrics.md` 에 `요구로 거슬러 오르는 비요구 청크: **n/d = p.p%** (후방 추적 커버리지, 목표 100.0%)` 줄이 있다. `n/d` 는 `kb_lib.pct` 꼴이다.
- 양성(질의): `bazel build //kg:cq` 의 CQ-13 절이 행 수와 `ancestorLevel = 기능 수준` 열을 낸다.
- 음성: 요구에 닿지 않는 청크는 분자에서 빠져 `d - n > 0` 으로 드러난다. 2026-09-21 실측 `670/673` 의 잔여 3(memory 관측)이 그 표본이다.

**등급** — A 다. 판정은 생성 뷰 둘이고 사람 판단이 없다. 수치의 목표 도달 여부는 판정이 아니라 관측이다.

판정의 원본은 `tools/metrics.py`(CQ20 절)와 `tools/cq-queries/CQ-13.rq` 다. 전방 추적(요구 → executable)은 CQ19 이고 이 기준 밖이다.
