---
id: https://agentic-knowledge-base.dev/id/chunk/8aa5baf8-3c38-4f46-b7bc-00a2f292a980
type: annotation
level: concrete
title_ko: 현상에서 피해로 가는 인과 24쌍 중 둘이 한 문장의 경로를 갖지 못한다
title: Two of the 24 phenomenon-to-impact pairs have no one-sentence path
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/688dd654-9493-4ff5-a3bc-1fe4906776ce]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T02:40:00+09:00}
---
issue (non-blocking): 질문지의 현상에서 피해로 가는 24쌍 가운데 둘이 한 문장의 경로를 갖지 못하고 둘이 빠져 있다.

대상: https://agentic-knowledge-base.dev/id/chunk/688dd654-9493-4ff5-a3bc-1fe4906776ce

본문: 쌍마다 이 현상이 이 피해에 이르는 경로를 한 문장으로 적어 본 결과 22쌍이 서고 둘이 서지 않는다. 서지 않는 둘은 `agt:linkToDeprecatedTarget`(P13)에서 `agt:assumptionSoundnessImpact`(H4)로 가는 쌍과 `agt:documentLag`(P18)에서 `agt:traceabilityImpact`(H3)로 가는 쌍이며, 앞은 폐기가 시간축이고 가정 건전성은 조건 평가라 경로가 끊기고 뒤는 문서가 그래프 밖이라 표가 낡아도 링크는 끊기지 않는다. 빠진 둘은 `agt:orphanKnowledge`(P2)와 `agt:stepRepetition`(P3)에서 `agt:knowledgeLossImpact`(H1 하위)로 가는 쌍이고 둘 다 있는 것을 못 찾아 다시 만든다는 경로가 한 문장으로 선다. P3은 이름이 단계 반복인데 관측 수단이 근사 중복이라 재는 것과 이름이 갈리는 대리 불일치도 함께 남는다.

제안: `defect-rules`의 `agt:hasImpact` 첫 형태에서 서지 않는 둘을 넣지 않고 빠진 둘을 넣는다. P3의 관측 수단은 근사 중복을 재는 것임을 정의문에 적는다.

해소: 열림 — 트리플을 옮기는 것이 developer의 몫이고 그 반영 뒤에 이 주석을 해소한다.
