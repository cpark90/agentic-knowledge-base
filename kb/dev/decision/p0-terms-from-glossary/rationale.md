---
id: https://agentic-knowledge-base.dev/id/chunk/9ec9c2b1-b204-491d-a7a8-4acb94e3a014
type: decision
level: logical
title_ko: 지어낸 용어는 모델의 사전 지식으로 해석되지 않고 청크는 종류가 아니라 모든 지식이 따르는 구조 규칙이다
title: Invented terms escape the model's prior knowledge, and a chunk is not a kind but the structural discipline all knowledge follows
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-07T03:03:35+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-07T03:03:36+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/cd23fc9b-1ca6-41e7-b749-5dcb0991796b
---
**근거** — 노트 0.0절이 표준어 원칙의 이유를 적는다. 지어낸 용어는 모델이 사전 지식으로 해석할 수 없어 매번 정의를 컨텍스트에 실어야 하고, 그것이 컨텍스트 예산을 잠식한다. 일반 원칙은 `p0-no-invented-terms`가 정했다. 이 결정은 산문 용어의 원본을 용어집 하나로 정한다.

2026-09-10 유저 결정은 저장소의 모든 문서와 에이전트의 용어를 표준 용어로 정규화하라는 것이었다. 정규화 표가 그대로 적용되어 `docs/glossary.md`가 되었다. 용어집의 행은 표준 용어·영문·옛 표기·출처·tier이고, 출처 열이 ISO/IEC/IEEE 24765·29148 같은 표준을 가리킨다.

옛 표기 검사가 tier로 나뉘는 까닭도 용어집에 있다. tier 1은 기계 치환, tier 2는 유저 결정, tier 3은 문맥 공존이라 바꾸지 않는다. 그래서 `consistency` ⑥은 tier 1만 위반으로 센다.

고유 용어는 2026-09-02~04 유저 결정 원장의 7항에서 왔다. 그 항은 청크를 포맷이 아니라 구조 규칙으로 정하고 온톨로지에도 적용했으며, 지식의 종류를 고유 용어로 부르게 했다. 노트 v3 재도출의 설계 검토는 이 규칙을 변하지 않은 것으로 확인했다.
