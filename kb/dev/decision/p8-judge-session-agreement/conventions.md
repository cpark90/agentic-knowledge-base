---
id: https://agentic-knowledge-base.dev/id/chunk/41adc59f-417f-4627-9faa-0ac774ea0046
type: decision
level: concrete
title_ko: 규범 문서 규약 — 판정자는 세션이고 임계는 확신도가 아니라 일치율이며 기계 환원이 먼저다
title: Normative-document conventions — The judge is a session, the threshold is agreement rather than confidence, and mechanical reduction comes first
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-jev-system-one}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/abf9e76a-0b1d-42c4-b70c-f77c7902f8db
---
**규약** — `p8-judge-session-agreement`의 결론을 규범 문서에 싣는 문장이다.

규약: 판정 로그 | 판정 로그는 실행 기록이다 — `kb/vv/run/judge-<시각>.md`에 append-only로 쌓이고 생성자는 `process:judge`다(역할이 아니므로 writer 검사 밖). 판정 표의 열이 곧 필수 필드다: 질문 id·값·확신도·**판정자 식별자**(세션·모델 — 외부 서비스가 아니다, 2026-09-30)·입력 지문(보낸 바이트의 sha256)·시각. 열 `일치`(일치·불일치·해당 없음)는 판정자 둘 이상이 같은 (질문·지문)에 답했을 때만 뜻을 갖는다. 확신도는 **자기 보고**라 개별 답을 보증하지 않고 단독 응답으로는 자동 적용이 없다. 결과 주석의 `본문:`은 판정자가 쓰지 못하므로 `해당 없음`이다. 게이트 `judge-log`(`chunk_lint`) — **로그가 0건이면 검사 대상이 없어 PASS**
규약: 기계 환원 | 요약(`핵심:` 항목의 지지 참조)은 게이트 `summary-support`(`chunk_lint`, 오탐 0/0 실측 — 슬롯 사용 0)로 확정된다. 중복·자리는 `consistency.py` ⑩·⑪이 후보만 내고 확정은 판정자(사람 또는 세션 판정자) 몫이다
