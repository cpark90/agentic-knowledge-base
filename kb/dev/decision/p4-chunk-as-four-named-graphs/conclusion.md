---
id: https://agentic-knowledge-base.dev/id/chunk/ab66f02d-6126-4507-b73a-c29429769f11
type: decision
level: concrete
title_ko: 청크는 네 개의 이름 붙은 그래프다
title: A chunk is four named graphs
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/3b134d68-35ab-47bc-86cc-94f3eb12be93, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0011]
part_of: https://agentic-knowledge-base.dev/id/composite/428f00f0-6790-41c0-83a8-bf8a564e848e
composite: {id: https://agentic-knowledge-base.dev/id/composite/428f00f0-6790-41c0-83a8-bf8a564e848e, title_ko: 청크의 구조 — 이름 붙은 그래프, title: Chunk structure as named graphs}
---
**결론** — 청크 하나는 **네 개의 이름 붙은 그래프(named graph)** 다.

| 그래프 | 담는 것 | 어휘 |
|---|---|---|
| **head** | 타입·plane·level·라벨. 나머지 셋을 연결 | `agt:` |
| **assertion** | 본문. **42줄 제한은 여기만** | plane별 (4.12절) |
| **provenance** | 이 본문이 무엇에서 왔는가 | PROV-O |
| **pubinfo** | 누가 언제 만들었는가, 버전 | PROV-O |

- **출처와 메타데이터는 W3C PROV-O로 쓴다.**
- **본문의 내용 해시를 청크 IRI 버전에 넣는다.**
- **가정과 링크는 이 네 그래프 안에 없다.** 링크 모델(9.5절)이 청크 IRI를
  가리킬 뿐이다.
