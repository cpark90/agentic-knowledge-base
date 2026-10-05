---
id: https://agentic-knowledge-base.dev/id/chunk/8c29d8f6-2473-485e-b540-faf657784ca8
type: decision
level: concrete
title_ko: 규범 문서 규약 — 빈 자리는 없음·해당 없음·미확정 셋으로만 적는다
title: Normative-document conventions — An empty place is written only as none, not applicable, or undetermined
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:12:48+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/1718358a-d741-45d7-bed6-df7818724e78
---
**규약** — `p4-three-empty-values`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] **빈 자리는 세 값으로만 적는다**(유저 승인 2026-09-22). `없음`은 찾아봤고 없다, `해당 없음`은 적용되지 않는다, `미확정`은 아직 모른다는 뜻이다. `N/A`·`TBD`·`미정`·단독 대시를 쓰지 않고 자리를 비워 두지도 않는다. 정의처는 `tools/kb_lib.py`의 상수 하나다.
규약: [지킴] 아직 모르는 것은 본문의 선택 슬롯 **`미확정:`**에 적는다. 미결은 문서가 아니라 항목 안에 있고 집계는 생성물이다. 답이 오면 고칠 자리가 하나다.
규약: [지킴] 세 값 밖의 빈 값 표기는 `chunk_lint`의 게이트 `empty-value`가 거부한다(2026-09-22 승격). 대상은 살아 있는 청크다.
