---
id: https://agentic-knowledge-base.dev/id/chunk/70e1825d-2c0f-4bae-b6b4-778494ff3875
type: agt:Space
level: logical
title_ko: 검증기에서 합격 기준으로 가는 바인딩은 어떤 링크 종류인가
title: Which link kind binds a verifier to its pass criteria
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-11-27T12:51:50+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-11-27T12:51:50+09:00}]
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 검증기(executable)에서 합격 기준(logical)으로 가는 바인딩은 어떤 링크 종류인가. 지금은 `refines`이고 검증기 30개에 60건이 있다. 사람 라벨 표본에서 이 꼴의 링크 두 건(Q-0047의 L05·L15)이 모두 '틀리다'였고, 이유는 "검증기는 기준의 판정 술어가 쓰는 검증 수단이고 기준을 풀어 쓴 하위 내용이 아니다"였다. 유저가 이 자리를 설계 공간으로 세웠다(Q184-b). 요구 `r-024`(기준 없는 verifies는 거부한다)에서 바인딩의 링크 종류를 정하는 결정으로 가는 `refines`가 변수다.

이미 정해진 것 — `agt:refines`(정련한다)의 정의는 "정제 전이의 기록 — 하위 수준 항목이 자기가 내려온 상위 수준 항목을 가리킨다"이다. V&V의 대응을 `refines`로 두는 이유는 결정 `p8-scenario-ladder-rungs`(시나리오 정제 계층의 세 높이에 검증 대응물이 필수다)의 근거에 있다(Q30-b). 개발 KB에서 산출물이 결정을 실현하는 관계는 `satisfies`다. 공간을 여는 것만으로 링크는 바뀌지 않는다(Q184-b).

현재 상태(2026-11-27 측정) — 바인딩을 읽는 자리는 넷이다. 게이트 `rung-before-descent`(`kb_lib.rung_violations`), verify 질의 `verifies-without-criteria`(verifies의 주어가 합격 기준을 `refines`해야 한다), 공동 커버 증거(`kb_lib.case_verifiers`·`co_cover`), 지표의 전방 추적이다. L05·L15의 0은 Q-0047의 풀이 "A는 B를 더 자세히 풀어 쓴 하위 내용이다"와 온톨로지 정의의 차이에서 나왔다(관측 기록 `https://agentic-knowledge-base.dev/id/chunk/bbc63eed-be6f-4316-b0cb-5f1a46dadc5c`).

답이 가르는 것 — 바인딩 60건의 링크 종류, 그것을 읽는 네 자리의 정의, 링크 이름이 사람이 읽는 뜻과 맞는지가 갈린다.

선택지 — A는 `refines`를 유지한다. 바뀌는 것이 없고, '구체화'로 읽는 사람에게 틀려 보이는 이름이 남는다. B는 V&V KB 안에서 `satisfies`를 쓴다. 60건과 네 자리, 링크 검사(`defs/kb.bzl`)가 바뀌고, 개발 KB의 산출물→결정 관계와 같은 종류가 V&V KB에도 생긴다. C는 새 링크 종류(검증 수단)를 둔다. 온톨로지에 속성 하나가 생기고 60건과 네 자리, 링크 검사가 바뀐다. 세 후보의 결정은 아직 없고, 변수까지만 채운 단계다.

닫기 기준 — 고른 종류는 셋을 만족해야 한다. 판정지에 온톨로지 정의를 그대로 실어 사람이 다시 판정했을 때 바인딩이 성립한다. 바뀌는 네 자리와 링크 검사가 `bazel test //...`를 다시 통과한다. 한 단어를 두 개념에 쓰지 않는다(`p0-one-word-one-concept`(같은 한글 단어를 두 개념에 쓰지 않는다)).

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/63f17c2d-3fdf-4fd0-b05a-ca7b6b89ce46
  kind: refines
status: open
```
