---
id: https://agentic-knowledge-base.dev/id/chunk/d5257525-c3ef-4680-a611-ed964eff79c0
type: requirement
level: functional
pattern: unwanted-behaviour
title_ko: 문서의 표가 생성물의 수치와 어긋나면 그 어긋남이 드러나야 한다
title: When a document table disagrees with the generated numbers, the disagreement must surface
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
exposes: [https://agentic-knowledge-base.dev/agt/documentLag, https://agentic-knowledge-base.dev/agt/metricVariesByLoadingOption]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T02:20:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
---
**검증 목표** — 그래프는 맞고 문서의 표가 낡은 상태가 검사로 드러난다는 것이 보여져야 한다. 이 목표가 다루는 위험은 현상 `agt:documentLag`(P18)이고, 같은 수치가 도구마다 갈리는 형태는 `agt:metricVariesByLoadingOption`(P21)이다.

- **이해관계자**: 검증자 · **관심사**: 문서와 그래프의 일치

**무엇을 관측하면 성립하는가**

- 문서가 적은 수치가 생성물의 같은 수치와 다르면 검사가 그 줄을 인용하며 실패한다.
- 문서는 결정을 복사하지 않고 IRI로 인용한다는 규칙이 수치에도 적용되어, 수치를 적은 자리마다 생성 명령이 함께 적혀 있다.
- 같은 이름의 수치를 내는 도구가 둘 이상이면 각 도구가 무엇을 분모로 세는지 문서가 구분한다.
- 이 목표는 기존 검증 목표 35건과 달리 위험 분석 G1의 현상에서 파생됐다. `doccheck`는 링크·앵커·문체를 보고 표 안의 수치는 보지 않으므로 이 목표의 자리가 기존 검사 밖이다.

미확정: 문서의 수치와 생성물의 수치를 대조하는 관측 수단이 없다 — 대조의 단위가 표 셀인지 줄인지 정해지지 않았다.
