---
id: https://agentic-knowledge-base.dev/id/chunk/3d45e545-3e32-424e-8f36-0b6c9eda7354
type: norm
level: logical
title_ko: docs/method.md 절 검증의 이어짐 — 세션 판정자와 일치율
title: docs/method.md verification section continued — the session judge and the agreement rate
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/ec6a4bb0-67a3-435c-bdab-850ae50240c4
continues: true
---
판정자는 게이트 밖 도구이고 **세션 판정자**, 곧 외부 서비스가 아니라 새 세션을 여는 에이전트다(유저 답 2026-09-30, 결정
[`p8-judge-session-agreement`](../../decision/p8-judge-session-agreement/conclusion.md)). `bazel run //tools:judge -- --question <질문 id>
--responses <json> [--responses <json> …] [--decoys <json>] <청크 파일…>`은 프로파일에 등록된 판정 질문을 단위 지식에 물어 값과
확신도를 받는다. 응답은 세션 판정자가 낸 `{judge, responses: [{question, fingerprint, value, confidence}]}`를 `--responses`로
입력하고, 이 도구는 판정 로그와 결과 주석을 남긴다. 판정 로그는 `memory` 지식 종류로 `kb/vv/run/judge-<시각>.md`에
추가 전용(append-only)으로 쌓이고, 결과 주석은 `kb/vv/verdict/`에 놓인다. 게이트는 판정을 부르지 않고, 로그의 형식과 필수
필드, `일치` 열만 본다. 필수 필드는 질문 id, 값, 확신도, **판정자 식별자**, 입력 해시값, 시각이고, `일치` 열의 값은 일치,
불일치, 해당 없음이다. 질문의 형은 noul, choice, score 셋이고 선택 집합은 255 이하다.

**확신도는 자기 보고이므로 단독 응답은 자동 적용되지 않는다.** 대신 `--responses`를 둘 이상 주면 도구가 같은 질문과 입력
해시값에 대한 값의 일치 여부를 계산해 로그에 낸다. 임계는 확신도 구간이 아니라 **일치율**이고, 일치율은 판정자 둘의 일치와
`label_sample.py --decoys`의 미끼 검출로 잰다. 자동 적용은 정확도와 판별력을 잰 뒤에만 열므로, 지금은 전부 사람 확인 큐다.

판정이 필요한 질문 여섯 가운데 요약과 채움, 중복, 자리의 넷은 기계로 환원되었다. `핵심:` 항목의 지지 참조인 요약과 채움은
게이트 `summary-support`, `addition`, `empty-value`가 맡고, 중복과 자리는 `consistency.py`의 ⑩과 ⑪이 후보까지 낸다. 남는 둘인
근거와 라벨 대표성만 세션 판정자가 맡는다. 세션 판정자를 여는 쪽은 실험자(vnv)이고, 그래서 열쇠 `key.json`을 쥔 쪽이
판정자와 분리된다.
