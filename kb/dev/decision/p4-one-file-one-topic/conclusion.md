---
id: https://agentic-knowledge-base.dev/id/chunk/b220928d-884a-474d-a52c-d90e8a878970
type: decision
level: concrete
title_ko: 한 청크는 한 파일이고 한 주제이며 본문을 고치면 라벨이 그 주제를 대표하는지 재검토한다
title: A chunk is one file on one topic, and editing its body calls for re-checking that the label still represents it
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08, https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:12:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/f56035ce-db13-4b21-a3a2-5f5a173f7e03
composite: {id: https://agentic-knowledge-base.dev/id/composite/f56035ce-db13-4b21-a3a2-5f5a173f7e03, title_ko: 청크 단위 — 한 파일 한 주제, title: Chunk unit — one file, one topic}
---
**결론** — 한 청크는 한 파일이고 한 파일은 한 주제다. 지식·온톨로지·shape 전부가 대상이다. 함수 청크도 추출된 파일 하나다(`p7-code-extraction-direction`).

- 라벨 하나로 요약되지 않으면 두 주제다. 그때는 분할한다. 분할의 형식은 `p4-chunk-split-and-merge`를 따른다.
- 본문을 고치면 라벨이 여전히 본문을 대표하는지 재검토한다.

한 파일은 구조가 강제한다. `chunk2kg`는 파일마다 청크 하나의 head를 생성하고 `agt:tokenCount`·`agt:assertionLocation`을 파일에서 계산한다. 한 주제는 리뷰 규범이다(`agt:Chunk` 정의문). 라벨의 대표성은 본문을 고칠 때의 재검토로 지킨다.
