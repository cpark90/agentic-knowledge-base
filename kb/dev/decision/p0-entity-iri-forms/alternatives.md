---
id: https://agentic-knowledge-base.dev/id/chunk/1770d81b-9871-4625-9080-7fa466def3b6
type: decision
level: logical
title_ko: 청크의 슬러그 IRI 유지와 모든 개체의 uuid화는 기각된다
title: Keeping slug IRIs for chunks and giving every entity a uuid are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:14:21+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/c9bb4d82-ac37-467d-8661-6982d1684108
---
**대안** — 둘을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 청크에 `chunk-<slug>`를 유지한다(v1 꼴) | IRI에 의미를 넣으면 이름 변경 시 IRI가 깨진다(노트 0.7절). 2026-09-10 재도출이 uuid로 바꿨다 |
| 손 개체에도 uuid를 준다 | 게이트 `catalog`의 역할 ↔ 스코프 대응과 게이트 태그 ↔ 개체 대응이 슬러그에 기댄다. 바꾸면 대응을 잇는 술어나 표가 새로 필요하다 |

v1 잔류 IRI를 uuid로 다시 쓰는 안은 검토 기록이 없다. 결론 표의 v1 잔류 행("새로 만들지 않는다", `supersedes` 대상으로만 남는다)이 그 자리의 현재 진술이다.
