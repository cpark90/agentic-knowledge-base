---
id: https://agentic-knowledge-base.dev/id/chunk/2b49d8b2-cfa4-409d-80c2-0fb2b0ae7d9d
type: decision
level: logical
title_ko: 구조 모델 하나면 shape 하나와 질의 하나가 모든 항목에 적용된다
title: One structural model lets a single shape and a single query cover every item
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/b4546452-61a1-4d61-b6c3-8af8a25e0f44
---
**근거** (노트 4.7절, Part IV 도입)

- 구조 모델은 온톨로지 밖의 별도 장치가 아니다. 지식 항목마다 다른 구조를 두면
  저장·질의·검사가 항목 수만큼 늘어나지만, **하나의 구조 모델(청크 +
  `part-of` + 순서)** 로 전부 표현하면 shape 하나, 질의 하나가 모든 항목에
  적용된다.
- 시그니처처럼 대부분 청크 하나로 끝나는 항목도 있다 — **복합체를 강제하는
  것이 아니라 청크가 최소 부품임을 강제**하는 것이다.
- 이 결정이 결정 자체의 저작 형식의 근거다. **결정 = 결론·근거·배제된 대안 세
  청크의 복합체**이므로, 결정 하나는 파일 하나가 아니라 세 청크와 그것을 묶는
  복합체로 저작된다. 4.4절 `DecisionChunk`의 역할 태그(결론/근거/대안) 필수
  제약과 5.4절 논증 구조 검사가 이 형태를 검사한다.
