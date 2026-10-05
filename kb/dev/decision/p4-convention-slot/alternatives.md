---
id: https://agentic-knowledge-base.dev/id/chunk/bc50f097-e033-4308-90da-2a3281678cc2
type: decision
level: logical
title_ko: 결론 개정·문서의 손 문장·결론 슬롯·넘는 결정만 전용 청크 안은 기각된다
title: Revising conclusions, hand-written document sentences, a conclusion slot, and a dedicated chunk only for overflowing decisions are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T01:11:35+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/6a38d7ed-105a-44bd-9c25-400871e5e5dc
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 결론을 개정해 세부를 결론에 넣는다 | stable 결정의 개정 승인이 31건 필요하다. 결론이 핵심과 세부를 함께 지면 라벨이 본문을 대표하기 어려워진다. 유저가 Q13에서 고르지 않았다 |
| 세부는 규범 문서의 손 문장으로 허용한다 | 31 자리의 세부가 원본 결정 없이 남아 문서가 결정의 투영이 되지 못한다. 유저가 Q13에서 고르지 않았다 |
| 결론 청크 본문의 선택 슬롯 `규약:`(Q13 원안, 이 결정의 앞선 판) | 줄이 결론의 토큰 상한을 나눠 쓴다. `p12-generated-document-form` 같은 stable 결정은 넘칠 가능성이 높고, 그때 상한 완화나 stable 분할이 필요하다. 유저가 Q22에서 (b)를 골랐다 |
| 상한을 넘는 결정만 `규약:`을 전용 청크로 뗀다(Q22-a) | 자리가 결정마다 둘 중 하나가 되어 생성기·검사가 두 경로를 갖는다. 단순·확고 기준(Q19-b)에 어긋난다. 유저가 Q22에서 고르지 않았다 |

`규약:` 슬롯의 토큰을 상한에서 빼는 안(Q22-c)과 넘는 결정을 분할하는 안(Q22-d)도 기각한다. 앞의 것은 검사 완화이고 뒤의 것은 stable 결정마다 개정 승인을 요구한다.
