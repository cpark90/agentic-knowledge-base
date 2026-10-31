---
id: https://agentic-knowledge-base.dev/id/chunk/41adc59f-417f-4627-9faa-0ac774ea0046
type: decision
level: concrete
title_ko: 규범 문서 규약 — 판정자는 세션이고 임계는 확신도가 아니라 일치율이며 기계 환원이 먼저다
title: Normative-document conventions — The judge is a session, the threshold is agreement rather than confidence, and mechanical reduction comes first
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-jev-system-one}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T01:35:45+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/abf9e76a-0b1d-42c4-b70c-f77c7902f8db
---
**규약** — `p8-judge-session-agreement`의 결론을 규범 문서에 싣는 문장이다.

규약: 판정 로그 | 판정 로그는 실행 기록이어서 `kb/vv/run/judge-<시각>.md`에 append-only로 쌓이고, 생성자는 `process:judge`이며 역할이 아니므로 writer 검사 밖이다. 판정 표의 열이 곧 필수 필드로, 질문 id와 값, 확신도, **판정자 식별자**, 입력 해시값, 시각이다. 판정자 식별자는 외부 서비스가 아니라 세션·모델이다(2026-09-30). 입력 해시값은 보낸 바이트의 sha256이다. 열 `일치`의 값은 일치, 불일치, 해당 없음이고, 이 열은 판정자 둘 이상이 같은 질문과 해시값의 쌍에 답했을 때만 뜻을 갖는다. 확신도는 **자기 보고**라 개별 답을 보증하지 않으므로 단독 응답으로는 자동 적용이 없다. 결과 주석의 `본문:`은 판정자가 쓰지 못하므로 `해당 없음`이다. 게이트는 `chunk_lint`의 `judge-log`이고, **로그가 0건이면 검사 대상이 없어 PASS다**
규약: 기계 환원 | `핵심:` 항목의 지지 참조인 요약은 `chunk_lint`의 게이트 `summary-support`로 확정되며, 이 게이트의 측정 오탐은 0/0이고 슬롯 사용은 0이다. 중복과 자리는 `consistency.py` ⑩·⑪이 후보만 내고, 확정은 판정자, 곧 사람 또는 세션 판정자가 한다
규약: 쌍 판정 | 링크 후보의 판정은 쌍 모드(`judge --pairs`)다. 행은 쌍 하나이고 `대상` 열은 `<앵커 IRI> ↔ <대상 IRI> · <링크 종류>`다. 질문은 링크 종류가 겹침이면 `overlapsHolds`, 그 밖이면 `proposedLinkHolds`이고 둘 다 예/아니오형이다. 결과 주석은 쌍마다 하나로, 판정자 둘의 값과 확신도, 일치를 함께 담고 `targets:`에 두 IRI를 적는다. 미끼는 판정 로그와 증거에 넣지 않고 검출률만 로그에 남긴다. 쌍의 입력 해시값은 두 파일 바이트를 이은 것의 sha256이고, 지금 두 파일과 다르면 낡은 판정이라 증거를 내지 않으므로 그 쌍은 다시 판정한다. 판정 증거는 반박만 있어도 후보를 무효로 만들지 않고, 이미 확정된 쌍에는 붙지 않는다. 판정자 하나만 답한 쌍은 판정 없음으로 센다(Q-0061#Q145)
