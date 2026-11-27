---
id: https://agentic-knowledge-base.dev/id/chunk/89053ad9-4452-401b-92fe-56e8fb811694
type: decision
level: logical
title_ko: DSL 문법을 지키고 실물과 게이트에 맞추며 기준은 시나리오 밖에 둔다
former_title_ko: ["표본 추출 표기가 표준에 있으므로 케이스 생성이 표준 위에 선다", "표본 추출 표기가 표준에 있으므로 테스트 케이스 생성이 표준 위에 선다"]
title: Keep the DSL grammar, match the artifacts and the gate, and keep criteria outside scenarios
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-11-01T04:38:26+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-11-01T04:38:26+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/7fcedb3d-e6cb-4df2-81fc-0787c3934fea
---
**근거** (노트 부록 E.5, 8.11절, 8.22절, 8.23절) — `keep(범위)`는 논리 시나리오의 표준 표기이므로, 도메인 모델만 프로파일이 정의하면 된다. 기준을 시나리오 파일 밖에 두는 것은 8.11절의 귀결이다. 기준 변경이 테스트 케이스 변경으로 보이면 안 되기 때문이다.

**개정** (Q-0075#Q173-a, 2026-11-01) — 2026-10-31 측정에서 옛 결론과 실물이 다섯 자리에서 달랐다. 옛 결론은 "동형 YAML로 시작하고 OSC 텍스트 변환기를 둔다"였지만, 실물은 산문 md 단위 지식 61개였고 변환기는 0개였다(`grep -rliE 'osc|openscenario' tools`). 옛 결론은 DSL의 `cover()`가 이 저장소의 `cover`와 같은 용법이라 적었다. 그러나 `tools/case_gen.py`의 `cover`는 표본 추출 규칙 목록이고, DSL의 `cover()`는 커버리지 수집점이다. 옛 결론은 "세 수준이 한 파일"이라 적었지만, 실물과 게이트 `rung-before-descent`는 수준별 단위 지식과 `refines` 사슬을 요구한다. 또 `tools/extract.py`는 `.py`·`.rq`·`.bzl`만 읽고, 프로파일에는 actor와 action 클래스가 없다.

다음 프로젝트는 `.osc`를 원본으로 쓰고, 충돌하면 DSL 문법을 지킨다. 그래서 결론을 그 선택과 실물에 맞췄다. 한 파일에 세 수준을 두는 안은 실행기 실측과도 어긋났다. `scenario_execution` 1.8.0에서는 `inherits`가 부모의 `do`를 물려받지 못한다. 그래서 수준 사이의 공유는 `import`로 하고, 정제는 단위 지식의 `refines`로 한다. 실행기 실측의 원문은 지워졌고 요약만 복구되었다. 도구 변경을 뒤로 미룬 것은 유저의 답이다.
