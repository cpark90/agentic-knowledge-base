---
id: https://agentic-knowledge-base.dev/id/chunk/6c26f560-f346-44d7-9a8f-32ade0458dfa
type: agt:Space
level: logical
title_ko: 어느 지표를 쓰고 어느 것이 게이트인가
title: Which metrics to use and which are gates
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T00:17:40+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 체계가 잘 돌아가는지를 무엇으로 재는가. 후보 12개가 열거되어 있으나 초기 집합이며 확정 목록이 아니다. 어느 것을 쓰고, 어느 것이 임계 위반이 곧 실패인 게이트이며 어느 것이 추세만 보는 관측인가가 변수다. 요구 `r-009`(모든 산출물은 요구로 거슬러 오른다)에서 이 배정 규칙으로 가는 `refines`가 열려 있다.

이미 정해진 것 — 후보 12개는 인지능력(입력 정보 누락률)·추적 커버리지·가정 건전성(`p12-evaluation-metrics`), 라벨 대표성·고아율·크기 분포·`draft` 체류 시간(`p4-chunk-quality-metrics`), 링크 밀도·`suspect` 비율·평균 재판정 지연·복원 비율·확정 정밀도(`p10-traceability-metrics`)다. 지표 각각이 메커니즘 하나에 대응하므로 어느 지표가 나빠졌는지가 곧 어느 메커니즘을 손볼지를 가리킨다. 도입 단계의 통과 조건은 의미 보존·구체화·유기적 연결 세 축이고 양 지표는 대리, 실험이 최종 판정이다(`p14-stage-pass-conditions`). 문서는 수치를 적지 않고 생성물을 인용한다. 손으로 센 수치가 낡는 사고가 2026-09-11 이전에 있었다.

현재 상태(2026-10-05 실측) — 자동 측정은 `metrics` 생성물이 한다. 고아율 0/2,251, 크기 분포(상한 9/10 초과 0.5%), 링크 밀도 2.566/청크, 전방 추적 71/78, 후방 추적 1,988/2,119, 복원 비율 78/1,015 = 7.7%, `suspect` 포화율 0/1,015, 가정 판정식 등급(A·B 5/5)을 낸다. `draft` 체류 시간·평균 재판정 지연·확정 정밀도·입력 정보 누락률은 내지 않는다. 라벨 대표성은 이 도구 밖의 실험이다. `metrics`는 그래프 파싱 실패에만 실패하므로 12개 중 어느 것도 `bazel test`의 게이트가 아니다.

답이 가르는 것 — `metrics` 도구가 무엇을 계산하고 그중 무엇이 `bazel test`를 실패시키는지가 갈린다. 게이트로 만들면 지표가 규칙이 되고, 관측으로 두면 추세만 본다.

선택지 — A는 단계 연동이다(`p12-metrics-gate-at-stage-completion`). 12개 전부를 관측으로 재되 게이트 임계는 methodology 각 단계의 완료 판정에만 둔다. `p14-stage-pass-conditions`가 단계별 통과 조건을 세 축의 대리 지표로 정했으나 그 결론은 `r-009`를 정제하지 않고 지표의 게이트·관측 배정을 정하지 않아 새 후보로 둔다. B는 전부 관측하고 게이트는 고아율만 두는 안이다(`p12-metrics-gate-orphan-only`). 최소 개입이다. C는 라벨 대표성을 핵심으로 두는 안이다(`p12-metrics-label-representativeness-core`). 유일하게 지식의 질을 재는 지표이고 에이전트 실험 비용이 크다. `p14-stage-pass-conditions`가 라벨 대표성 실험을 의미 보존 축의 최종 판정으로 두었으나 핵심 지표로 정하지는 않았다. 세 후보 모두 열려 있다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/f6162b3d-76c2-401f-a460-840e78c7d0c5
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/750f0856-c900-45dd-b4d1-fc754f64c27e
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/4d45c88c-e814-4dad-8b6f-8dd7b173b2a2
    state: open
```
