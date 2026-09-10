---
id: https://agentic-knowledge-base.dev/id/chunk/4eef1ba8-9095-4b69-aa55-69ca65ff7a35
type: decision
level: concrete
title_ko: 청크는 온톨로지 클래스이자 42줄 최소 단위다
title: The chunk is an ontology class and the 42-line minimum unit
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08, https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7, https://agentic-knowledge-base.dev/id/chunk/45f9ad28-7bf6-4267-87f0-271ca83fae5a]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0002]
part_of: https://agentic-knowledge-base.dev/id/composite/dd76498b-2cca-4b79-a1fe-ce5a4d33c0ca
composite: {id: https://agentic-knowledge-base.dev/id/composite/dd76498b-2cca-4b79-a1fe-ce5a4d33c0ca, title_ko: 청크 — 온톨로지 클래스로서, title: Chunk as an ontology class}
---
**결론** — `agt:Chunk`는 온톨로지 `entity/` 모듈의 **최상위 클래스**이며, 상위
온톨로지의 정보 내용 개체 아래에 둔다.

```
iao:InformationContentEntity
  └── agt:KnowledgeItem
        ├── agt:Chunk       ← 본문을 가진 최소 단위
        └── agt:Composite   ← 본문 없이 부분만 가짐. Chunk와 disjoint
```

**모든 지식은 청크를 가장 작은 부품으로 한다.** 청크는 하나의 plane, 하나의
level에 속하고, 한 주제만 다루며, **본문이 42줄을 넘지 않는** 자립적 지식
단위다. 42줄을 넘는 것은 청크가 아니라 복합체이며 분할 대상이다.
