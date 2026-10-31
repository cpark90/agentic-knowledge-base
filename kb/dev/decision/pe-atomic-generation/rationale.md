---
id: https://agentic-knowledge-base.dev/id/chunk/8a24627c-2be8-4eb4-98ed-8989fad9d199
type: decision
level: concrete
title_ko: 쓴 뒤에만 판정되는 게이트가 있어 바로 쓰면 반쪽 산출물이 두 번째 진실 공급원이 된다
title: Some gates judge only after writing, so writing in place leaves a partial output that becomes a second source of truth
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0179-atomic-generation.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:59:44+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:59:44+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/99254d62-ee67-4d34-aa30-a42211166fd5
---
**근거** — 출처는 harness-concrete `docs/odr-bind-lock.md`의 "Atomic emit" 절이다.

- 일부 게이트는 파일을 쓴 뒤에만 판정할 수 있으며, 복사한 내용의 해시값 대조가 그렇다. 그래서 목적지에 바로 쓰면 그 실패가 **반쪽 산출물**을 남긴다.
- 반쪽 산출물은 조용한 두 번째 진실 공급원이다. 정상 결과처럼 보이지만 어느 게이트도 통과하지 않았고, 다음 사람이 그것을 원본으로 읽는다. 문서를 저장하지 않고 생성한다는 규칙(`p12-documents-are-generated`)은 생성이 실패하면 이전 상태가 유지된다는 조건이 성립해야 안전하다.
- 임시 위치는 목적지와 같은 저장 계층에 두어야 교체가 실제로 원자적이다. 목적지가 이미 있으면 옛 것을 옆으로 옮긴 뒤 새 것을 놓고, 교체 자체가 실패하면 되돌린다.
- 임시 경로가 산출물 내용에 새어서는 안 된다. 새면 임시 위치를 쓴다는 사실만으로 실행마다 산출이 달라져 바이트 동일성(`pe-lock-snapshot-reproducibility`)이 깨진다.
