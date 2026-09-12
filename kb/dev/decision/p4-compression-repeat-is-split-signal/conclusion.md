---
id: https://agentic-knowledge-base.dev/id/chunk/251bd731-fb8d-44aa-990c-d6281fb4a8d4
type: decision
level: concrete
title_ko: 상한에 걸려 압축으로 버틴 횟수는 분할 신호이며 1회 유예·2회 경고·3회부터 부채다
title: The number of times a chunk survived the cap by compression is a split signal: once tolerated, twice warned, three times a debt
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-agrtls-practices-review}]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-12T16:30:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08]
part_of: https://agentic-knowledge-base.dev/id/composite/ff721aef-2663-430e-a491-4e0cc61f73b2
composite: {id: https://agentic-knowledge-base.dev/id/composite/ff721aef-2663-430e-a491-4e0cc61f73b2, title_ko: 상한 압축 반복과 분할 신호, title: Repeated compression at the cap as a split signal}
---
**결론** — 42줄 상한(4.4절)에 걸린 청크가 **압축으로 버틴 횟수**를 분할 신호에 더한다(노트 4.10절 표에 추가).
1회는 유예, 2회는 경고, 3회부터는 부채 — 다음 개정 전에 분할한다. 계수는 git 이력에서 같은 청크의 본문 줄 수가
42 근처에서 오르내린 횟수로 잰다(뷰, 저장하지 않는다).

분할의 형식은 4.10절 그대로다 — 새 IRI를 만들고 옛 IRI를 `prov:wasDerivedFrom`으로 잇고, 옛 청크에는 나뉜 곳을
가리키는 포인터 한 줄을 남긴다. 라벨은 각 조각이 자기 본문을 대표하도록 다시 쓴다.

| 횟수 | 처리 |
|---|---|
| 1 | 유예 — 압축이 서술을 덜어내지 않았는지 리뷰에서 본다 |
| 2 | 경고 — 분할 후보로 `consistency` 보고에 올린다 |
| 3+ | 부채 — 다음 개정 전 분할. 개정이 먼저 오면 게이트가 아니라 리뷰가 막는다 |
