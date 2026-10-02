---
id: https://agentic-knowledge-base.dev/id/chunk/91d72e63-e72e-4803-aaf3-281a81994a31
type: requirement
level: functional
pattern: unwanted-behaviour
title_ko: 같은 이름의 지표가 로딩 옵션에 따라 다른 값을 내면 그 차가 드러나야 한다
title: When a same-named metric yields different values under different loading options, the gap must surface
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
exposes: [https://agentic-knowledge-base.dev/agt/metricVariesByLoadingOption]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T06:20:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/2b1e5103-9b9d-43da-9231-6b4027bc370e]
---
**검증 목표** — 같은 리비전의 같은 그래프를 재는 지표가 도구의 로딩 설정에 따라 다른 값을 낼 때 그 차가 값과 함께 드러난다는 것이 보여져야 한다. 이 목표가 다루는 위험은 현상 `agt:metricVariesByLoadingOption`(P21)이다.

- **이해관계자**: 감사 · 검증자 · **관심사**: 지표의 재현성

**무엇을 관측하면 성립하는가**

- 같은 이름의 수치를 내는 도구가 둘 이상일 때 그 값이 같다. 다르면 각 도구가 무엇을 더 읽거나 덜 읽는지가 수로 적힌다.
- 도구가 읽는 그래프 union의 트리플 수가 생성 문서의 머리에 적히고, 도구 사이의 차가 어느 파일에서 오는지 대조된다.
- 실측 2026-09-29에 `//kg:metrics`는 트리플 28749, `//kg:link_candidates`는 28678, `//kg:audit`는 30293이다. 세 값이 갈리는 동안 세 머리 어디에도 그 차가 수로 적혀 있지 않다.
- 이 목표의 표본 근거는 참조 저장소 `../harness-functional`의 실측 실패 R5다. 감사 수치가 추론 켜짐 205와 꺼짐 173으로 갈렸고 필터를 잘못 쓰면 구체 타입이 증발했다.
- 기존 검증 목표 35건은 게이트·음성 시험을 사슬로 묶은 것이고 이 목표는 위험 분석 G1의 현상에서 나왔다. 파생의 표지는 본문의 현상 IRI 인용이다.
