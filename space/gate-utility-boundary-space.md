---
id: https://agentic-knowledge-base.dev/id/chunk/aaf35b2b-c3c5-42c4-bed4-44e34f97d6df
type: agt:Space
level: logical
title_ko: 판정과 활용의 경계를 도구에 긋는가
title: Whether the boundary between judging and using is drawn at the tool
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-09T18:04:39+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 게이트냐 활용이냐가 도구의 속성이 아니라 호출(`GATES` 등록)의 속성이다. `GATES`의 tool 값에 `case_gen`·`workset`·`vv_run`·`gen_norms`·`gen_skills`·`extract`·`stamp`가 들어 있다. 게이트 `rung-before-descent`와 지표가 같은 판정 함수를 쓴다(Q51-a 설계). `harness/scripts_test.py`는 동작 게이트이지만 `GATES` id가 없다. 구조 검수(2026-10-06)가 이 자리를 경계가 모호한 자리로 지적했고 유저가 설계 공간으로 세웠다(Q75-a). 요구 `r-016`(편집은 게이트가 판정한다)에서 판정과 활용의 경계를 정하는 결정으로 가는 `refines`가 변수다.

이미 정해진 것 — 게이트 id 등록부는 `defs/kb.bzl`의 `GATES` 리터럴이다(`p6-gate-tool-code-structure`). 게이트를 어느 기계가 판정하는가는 실행 계층 다섯이다(`p6-gate-catalogue`). 같은 함수를 게이트와 지표가 함께 쓰는 것은 Q51-a의 설계다. 어느 지표가 게이트인가는 공간 `https://agentic-knowledge-base.dev/id/chunk/6c26f560-f346-44d7-9a8f-32ade0458dfa`가 따로 묻는다.

현재 상태(2026-10-09 실측) — `GATES`(`GATES_TAIL` 포함)의 게이트 id는 57개이고 tool 값은 23종이다(리터럴의 `"tool"` 값을 센다). `tools/*.py` 42개 중 41개가 `kb_lib`를 참조한다(`grep -L kb_lib tools/*.py`가 `handoff.py` 하나를 낸다). 지표 `metrics.py:379`가 `kb_lib.vv_counterparts`를 부르고 게이트의 `kb_lib.rung_violations`도 그 함수를 부른다. `harness/BUILD.bazel`의 `scripts_test`는 `bazel test` 대상이고 `GATES`에 그 id가 없다.

답이 가르는 것 — 새 도구나 함수가 판정 쪽인지 활용 쪽인지를 즉시 판단할 수 있는지가 갈린다.

선택지 — A는 게이트 여부를 호출의 `GATES` 등록이 정하는 현행 유지안이다(`p6-gate-or-utility-by-registration`). B는 판정 도구와 활용 도구를 도구 단위로 가르는 안이다(`p6-gate-or-utility-by-tool`). 구조 검수는 이 자리에 선택지를 들지 않았다. 그래서 현행 유지와 질문이 가르는 반대쪽 둘만 세운다. 두 후보 모두 열려 있다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/6a916cc7-e02e-4289-9986-59d4fcd12479
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/9ea3361d-f211-4dbb-993a-33159134b210
    state: open
```
