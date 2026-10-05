---
id: https://agentic-knowledge-base.dev/id/chunk/81faf402-ee5c-49db-86f9-3d8d71022c2e
type: decision
level: logical
title_ko: 규범 문서를 결정의 투영으로 만들려면 세부 문장의 원본도 결정 안에 있어야 하고 별도 청크는 결론과 토큰 상한을 건드리지 않는다
title: Projecting the normative documents from decisions needs the detailed sentences to live in the decisions too, and a separate chunk leaves the conclusion and the token cap untouched
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:12:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/6a38d7ed-105a-44bd-9c25-400871e5e5dc
---
**근거** — 규범 문서는 방법론 층의 투영이고 원본은 청크다(`p0-service-is-a-three-layer-wiki`). 투영이 성립하려면 문서의 문장마다 원본이 결정 안에 있어야 한다.

- orchestrator 실측(2026-10-03)에서 `STYLEGUIDE.md`의 규약 자리 89 가운데 31은 결정이 핵심만 진술하고 세부 서식·경로 이름이 문서에만 있다. 그 세부는 원본 결정이 없다.
- 같은 실측에서 `STYLEGUIDE.md`의 항목 89는 결정 56을 인용하고, `p12-generated-document-form` 하나가 항목 10을 낸다. 문서 골격이 가리키는 단위는 결정이 아니라 `규약:` 줄 하나다. 그래서 줄에 순번 참조를 준다.
- 결론 슬롯 안(Q13 원안)에서는 `p12-generated-document-form`(stable)에 10줄을 더하면 1,092 토큰을 넘을 가능성이 높았다. `p11-harness-two-channels`도 같았다. 별도 청크는 결론의 토큰을 쓰지 않는다.
- 유저가 Q22에서 (b)를 골랐다. 질문지 Q22의 hci 권장 줄 문언이 "결정마다 자리가 하나라 단순·확고 기준에 가장 가깝다"이다. 기준은 Q19-b의 답(구조의 단순·확고)이다. 넘는 결정만 떼면 자리가 결정마다 둘 중 하나가 된다.
- 유저가 Q13에서 고른 선택지의 문언이 "결론을 고치지 않으므로 stable 개정 승인이 필요 없다"이다. 넷째 청크는 결론 파일을 바꾸지 않으므로 그 성질이 더 확고하다.
- 줄 머리 `규약:`은 `chunk2kg`가 이미 표지로 읽는다(`BODY_SLOT_KEYWORDS`). 같은 판독 경로를 쓰면 투영기가 줄을 집계·인용한다.
- 강도 표시를 줄 머리에 두는 까닭은 강도가 문장의 성질이기 때문이다. 문서는 그 표시를 지킴·권장 구분으로 싣는다.

이 결정의 앞선 판의 미확정(몇 줄을 두는가, 어디에 싣는가)은 닫혔다. 줄 수는 토큰 상한만 정하고, 싣는 자리는 절 청크의 `items`가 정한다(`p12-norm-documents-from-section-chunks`).
