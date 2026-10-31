---
id: https://agentic-knowledge-base.dev/id/chunk/5e4dc67f-c98d-4615-963d-627b9439a492
type: decision
level: logical
title_ko: 센서는 확정하지 않는다
title: A sensor does not settle
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-10-24T17:17:21+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T17:17:21+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/a6dd335e-3bb8-41b4-9c4c-2745b90b5188
---
**근거** — 에이전트는 신뢰할 수 없는 센서이고, 상태를 바꾸는 판단은 컴파일러와 승인자의 몫이다(2.5절). 언어모델의 출력을 확정 근거로 쓰면 10.8절의 검사 가능성 서열에서 맨 아래가 맨 위를 덮는다. 제안을 증거 기록에 `proposal`로 남기는 이유는 누가 이 후보를 냈는가가 출처로 남아야 8.14절의 제안자 드리프트를 잴 수 있기 때문이다. 선호를 서열에서 파생하는 이유는 사람이 선호를 손으로 적지 않아도 기본값이 검사 가능해야 하기 때문이다(노트 9.11절, 2.5절, 9.9절).

**개정** — 유저는 판정을 셋째 자리로 더하기로 했다(유저 결정 Q-0056 Q118-a, 2026-10-24). 판정자 세션도 언어모델의 확률적 추론인데, 옛 결론은 두 곳만 적어 `p10-candidate-and-confirmed-link`의 판정 행과 어긋났다. 판정 결과는 증거 기록의 한 종류로만 남고 확정 근거가 아니므로, 센서가 확정하지 않는다는 원칙은 그대로 지켜진다. 판정을 서열에서 공동 커버 다음, 임베딩 앞에 두는 것은 orchestrator의 제안이고 유저에게 묻지 않았다. 판정은 독립 세션 둘의 일치와 미끼 검출로 걸러지므로 단일 세션의 읽음이나 임베딩 유사도보다 검사 가능성이 높고, 반면 구조에서 나온 공동 커버보다는 낮다는 것이 그 이유다. 결론의 범위 문장에서 요구 r-030을 가리키던 절은 그 요구가 폐기되어 지웠다(Q-0063#Q156).
