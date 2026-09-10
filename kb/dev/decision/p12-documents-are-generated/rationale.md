---
id: https://agentic-knowledge-base.dev/id/chunk/d18aa19c-6d09-4609-a39b-15fdbd15b2ab
type: decision
level: logical
title_ko: 저장된 문서는 두 번째 진실 공급원이 되고 사본은 출처를 잃는다
title: A stored document becomes a second source of truth, and a copy loses its provenance
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/66832e72-2baf-420e-876f-05120bb3184d
---
**근거** (노트 12.10절)

- 문서를 저장하면 청크와 문서 사이에 **두 번째 진실 공급원**이 생기고, 그
  차이가 조용히 벌어진다. 링크 붕괴와 같은 문제인데 문서에는 재판정 장치가
  없다.
- 생성 시각과 질의를 적는 이유 — **저장된 사본이 원본으로 오인되는 것을
  막는다.** 사본을 손에 든 사람도 언제 무엇으로 만든 것인지 되짚을 수 있어야
  한다.
- ADR이 `decision` 구성체 하나(결론·근거·대안)와 그대로 대응한다. 결정을 세
  청크로 나눈 구성이 문서 생성에서 값을 갚는다.
