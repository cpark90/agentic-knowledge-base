---
id: https://agentic-knowledge-base.dev/id/chunk/d4513996-395c-4dde-9233-0418c59be775
type: decision
level: logical
title_ko: 줄은 계수기에 따라 토큰이 1.7배 갈리므로 단위는 토큰이고 숫자는 도출에서 나온다
title: A line is 1.7× ambiguous in tokens across counters, so the unit is tokens and the number follows from the derivation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-10-01T20:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/128d439b-0863-41e3-8eb3-7c090e7f1742
---
**근거** — 줄은 컨텍스트의 단위가 아니다. 에이전트의 창은 토큰으로 세어지고 한 줄의 토큰은 내용에 따라 갈린다 — 저작 산문은 줄당 27, 코드는 14다. 같은 42줄이 산문에서는 1,138토큰, 코드에서는 600토큰이다. 단위를 줄로 두면 plane마다 상한의 뜻이 달라지고 그것이 `artifact`에 200줄을 따로 두게 한 원인이었다.

숫자는 실측에서 나온다. hci의 근사(한글 3자/토큰)는 예산을 3,200토큰으로 봤고 실측은 5,418이다 — 1.7배. 근사로 정했다면 42×15 = 630을 골라 저작 산문 111개를 쪼갰을 것이고 그 분할은 도출이 아니라 추정의 산물이었다. 고정된 계수기 하나가 있어야 숫자가 재현된다 — 유저가 토크나이저 고정을 조건으로 단 까닭이다.

예산 ÷ 5를 근거로 두는 까닭은 42줄의 근거가 그것이었기 때문이다. 단위를 바꾸면서 도출을 바꾸면 숫자 둘이 바뀌어 어느 것이 단위의 효과인지 알 수 없다. 도출을 고정하고 단위만 바꾸면 1,092가 나오고, 지금 청크 대부분(저작 산문 99.7%)이 그 안에 있다 — 42줄 규칙이 실제로 담던 양이 그만큼이었다는 뜻이다.

`artifact`·`memory`를 따로 두는 까닭은 인용이기 때문이다. 코드와 실행 기록은 저작이 아니라 원문 인용이라 조망 단위가 아니고, 그 상한은 "한 창을 넘지 않는다"다. 옛 200줄을 코드의 줄당 토큰으로 환산한 2,856이 그 값이다.
