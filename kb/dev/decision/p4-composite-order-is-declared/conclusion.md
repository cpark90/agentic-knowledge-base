---
id: https://agentic-knowledge-base.dev/id/chunk/28655d6b-d000-4f43-8d68-9e0ce042c39c
type: decision
level: concrete
title_ko: 복합체의 순서는 선언 청크의 목록이 원본이고 선언된 것만 co:List로 방출한다
title: A composite's order is declared in the declaring chunk, and only declared order is emitted as co:List
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-30T09:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5-1, at: 2026-09-30T09:05:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/c15bc5d0-4f85-4d7b-bdd2-85cca14af3ba
composite: {id: https://agentic-knowledge-base.dev/id/composite/c15bc5d0-4f85-4d7b-bdd2-85cca14af3ba, title_ko: 복합체 순서의 선언, title: Declaring a composite's order}
---
**결론** — 복합체의 순서는 **선언**이다. 예외는 없다. 선언 청크의 `composite:`에 선택 키 `ordered: [<부분 IRI>…]`가 있을 때만 생성기가 `co:List`와 `co:index`를 방출하고, 없으면 `hasDirectPart`만 낸다(순서 없음). 도구는 역할 이름으로 순서를 추측하지 않는다. 목록은 부분 전부를 빠짐없이 한 번씩 담아야 하며 어긋나면 게이트 `chunk2kg`가 거부한다.

| 복합체 | 순서의 원본 | 방출 |
|---|---|---|
| `kb_decision`(결론·근거·대안) | 역할 순서를 **생성기가 `ordered` 인자로 선언**한다 — 예외가 아니다(유저 답 2026-09-29) | 선언된 순서로 `co:List` |
| `kb_composite`에 `ordered` 있음 | 선언 목록 | 그 순서로 `co:List` |
| `kb_composite`에 `ordered` 없음 | 없음 | `hasDirectPart`만 |

순서는 청크의 본문이 아니라 frontmatter의 메타데이터다 — `ordered`를 더하거나 고쳐도 `generated.at`·`verified`를 건드리지 않는다(`p10-restored-link-marking`과 같은 취급).

순서의 정합성(색인 1..n 연속·중복 없음·부분 집합과 일치)은 shape가 판정한다. 파일명 정렬이나 IRI 정렬은 순서가 아니다 — 그것은 생성기의 결정적 출력 순서일 뿐이며 뜻을 갖지 않는다.
