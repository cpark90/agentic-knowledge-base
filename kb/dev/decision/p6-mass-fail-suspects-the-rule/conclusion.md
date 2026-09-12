---
id: https://agentic-knowledge-base.dev/id/chunk/b06008c3-7279-4e44-b4ae-cf48dd7fc3d4
type: decision
level: concrete
title_ko: 대량 FAIL은 산출물보다 규칙을 먼저 의심하는 신호이고 배선 안 된 검사는 정상으로 선언한다
title: A mass FAIL is a signal to suspect the rule before the artefacts, and unwired checks are declared as the known baseline
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-agrtls-practices-review}]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-12T16:30:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
part_of: https://agentic-knowledge-base.dev/id/composite/b0647639-f82c-4e20-a9ce-73b4e7fdb748
composite: {id: https://agentic-knowledge-base.dev/id/composite/b0647639-f82c-4e20-a9ce-73b4e7fdb748, title_ko: 게이트 추가 절차와 대량 FAIL의 판정, title: Gate addition procedure and the mass-FAIL ruling}
---
**결론** — 게이트를 추가하는 절차는 다섯 단계이고, 첫 실행에서 **대량 FAIL**이 나오면 산출물을 고치기 전에
규칙 자체를 의심한다. 판정(규칙 유지·범위 축소·기각)은 총람 행에 기록한다.

| 단계 | 내용 |
|---|---|
| 1 이름 | 게이트 id(kebab, 도구의 `FAIL [<id>]` 태그와 같음) |
| 2 총람 | `tools.md` 총람에 행 — 무엇을 거부·계층·id·해소 절차(누가·어디서) |
| 3 도구 | 실패 종류를 구분해 종료: 판정 실패 1 · 설정·입력 문제 2 · 미실행 3(SKIP은 PASS가 아니다) |
| 4 첫 실행 | 실태를 그대로 기록 — 몇 건이 왜 걸리는가 |
| 5 판정 | 대량 FAIL이면 규칙의 범위·정의를 먼저 검토(예: 결론 라벨 형식 197 → 결론만 25). 면제는 `waivers.md`에 선언 |

**게이트와 보고를 가른다** — 기계적으로 참·거짓이 갈리고 재현되며 오탐이 없는 검사만 게이트(test 타깃), 사람 판정이
필요한 것은 보고(뷰). **비-초록 기준선은 선언한다** — 아직 배선되지 않았거나 알려진 경고는 "정상"으로 총람에 적어
다음 세션이 고치러 오지 않게 한다 (노트 6.7절).
