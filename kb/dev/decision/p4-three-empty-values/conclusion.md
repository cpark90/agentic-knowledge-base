---
id: https://agentic-knowledge-base.dev/id/chunk/d93492e4-f343-4736-b4a5-d04f48a3a75f
type: decision
level: concrete
title_ko: 빈 자리는 없음·해당 없음·미확정 셋으로만 적는다
title: An empty place is written only as none, not applicable, or undetermined
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-22T20:20:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/1718358a-d741-45d7-bed6-df7818724e78
composite: {id: https://agentic-knowledge-base.dev/id/composite/1718358a-d741-45d7-bed6-df7818724e78, title_ko: 빈 값의 세 뜻, title: The three meanings of an empty value}
---
**결론** — 값이 없는 자리는 세 값 중 하나로 적는다. 세 값은 서로 다른 사실을 뜻한다.

| 값 | 뜻 | 다음 행동 |
|---|---|---|
| `없음` | 찾아봤고 없다 | 없다 |
| `해당 없음` | 이 항목에는 적용되지 않는다 | 없다 |
| `미확정` | 아직 모른다 | 미결로 집계되고 답이 오면 채운다 |

`N/A`·`TBD`·`미정`과 단독 대시를 쓰지 않는다. 자리를 비워 두지도 않는다. 생성 문서의 `없음` 표기(`p12-generated-document-form`)는 이 셋의 부분집합이고, 정의처는 `tools/kb_lib.py`의 상수 하나다.

`미확정`은 청크의 선택 슬롯이다. 미결을 문서(`docs/open-questions/`)가 아니라 항목 안에 두면 집계가 생성물이 되고, 답이 왔을 때 고칠 자리가 하나다.

검사는 보고로 시작해 게이트가 됐다. `consistency` ⑧이 세 값 밖의 표기를 세고, 수치가 0이 된 2026-09-22에 `chunk_lint`의 게이트 `empty-value`로 올렸다. 대상은 살아 있는 청크이고 `deprecated`는 기록이라 대상이 아니다. 낱말의 산문 용법은 오탐이므로 `docs/waivers.md`에 선언하고 집계에서 뺀다.
