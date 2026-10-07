---
id: https://agentic-knowledge-base.dev/id/chunk/b091c80d-3ecf-48a1-841e-f99432200f21
type: norm
level: logical
title_ko: docs/rules.md 절 파일 형식의 이어짐 — 세 빈 값·슬롯 표지와 게이트 id의 단일 정의처
title: docs/rules.md file-format section continued — three empty values, slot markers and the single definition of gate ids
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T11:26:44+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/a57b18df-3b8b-4579-a0f8-db4655159538
continues: true
---
**본문의 빈 자리는 세 값으로만 적는다**(유저 승인 2026-09-22 — [`p4-three-empty-values`](../../decision/p4-three-empty-values/conclusion.md)).
`없음`은 찾아봤고 없다, `해당 없음`은 적용되지 않는다, `미확정`은 아직 모른다는 뜻이고 셋만 행동이 갈린다.
`N/A`·`TBD`·`미정`·단독 대시를 쓰지 않는다. 아직 모르는 것은 선택 슬롯 `미확정:`에 적고, 미결 집계는
문서가 아니라 그 슬롯에서 생성된다. 슬롯에는 그 슬롯의 질문에 답하는 문장만 쓴다
([`p4-slot-answers-one-question`](../../decision/p4-slot-answers-one-question/conclusion.md)) — 다른 슬롯의 답·메타
문장·채움은 첨가다. 순서 목록의 모든 항목은 `1.`로 적고 항목 9개·중첩 2단계·항목당 2줄을 넘지 않는다.
검사는 `consistency` ⑧·⑨ 보고에서 시작해 수치가 0이 된 뒤 `chunk_lint`로 올린다. 슬롯 표지는 **자리**로 판정한다 —
그 줄의 필드 머리(줄 시작·`- ` 다음·` · ` 다음)에 있는 굵은 span만 슬롯이고 표 셀·문장 중간의 굵은 span은 강조다; 한정어는
12자 이하·마침표 없음일 때만 같은 표지다(2026-09-29 — 시나리오 표지를 더하자 옛 청크 32파일 60건의 강조가 슬롯으로
방출됐고 이 규칙으로 0이 됐다). 표지 낱말의 접두 겹침은 `kb_lib.validate_body_slot_markers`가 로드 시점에 거부한다.

**게이트 id의 단일 정의처는 `defs/kb.bzl`의 `GATES`**(id → 실행 계층·판정 도구·한글 라벨·설명 한 줄)**와 `TOOL_TAGS`**(게이트가 아닌 입력
문제·보고 태그)**다**(2026-10-02 — 통일 기획 2단계의 첫 조각; 그 전에는 같은 목록이 넷으로 갈려 있었다). `kb_lib`이 리터럴 읽기로
`*_GATE`·`*_TAG`를 파생하므로 상수를 손으로 두지 않는다. 게이트는 프로세스 층의 **항목**이고 개체는 `//kg:gates_kg`의
`id:gate-<id>`(`agt:Gate`, `agt:gateTier`, `agt:enforcedBy` → 판정 도구의 파일 복합체)다 — `kg/`에 손으로 쓰지 않는다. 갈림은
게이트 `gate-registry`(코드의 태그 ⊆ 등록부 · 손 상수 없음 · 폴백 값 일치 · 등록 id가 코드에 닿음)가 거부한다.
