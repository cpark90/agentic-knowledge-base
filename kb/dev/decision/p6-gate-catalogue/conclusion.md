---
id: https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5
type: decision
level: concrete
title_ko: 게이트는 다섯 실행 계층에 배치되며 실패는 draft에 머물러 전파되지 않는다
title: Gates sit on five execution layers; a failure stays in draft and does not propagate
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-12T17:10:00+09:00}
verified: [{by: orchestrator/claude-fable-5-1, at: 2026-09-12T17:10:00+09:00}, {by: process:label-judge-20260912, at: 2026-09-12T17:40:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
composite: {id: https://agentic-knowledge-base.dev/id/composite/33c8a1a1-fc90-4ce7-83a9-20c607a7c163, title_ko: 게이트 총람, title: The gate catalogue}
part_of: https://agentic-knowledge-base.dev/id/composite/33c8a1a1-fc90-4ce7-83a9-20c607a7c163
---
**결론** — 이 문서에 흩어진 게이트를 한 표로 모은다. "실행 계층"은 어느 기계가 판정하는가다 — **shape**(SHACL, 청크 단위, 즉시) / **verify**(SPARQL, 그래프 단위, 재검증 시점) / **analysis**(Bazel 분석 시점, 빌드 실패) / **test**(실행, `bazel test`) / **human**(승인) (노트 6.7절).

shape — 청크 형식(4.4) · 수준 허용표(6.4) · 범위·제약(6.8, +test) · 표본 근거(6.8, 8.23) · 기준 바인딩(8.11) · 대안 기록(7.4)
verify — 통제 어휘(0.0) · 출처(4.3) · ODD 참조(3.3) · ODD 경계(9.10) · 기여(6.8) · 검증 대응물(8.3) · 할당 근거(9.10) · 계약 선행(7.5) · 독립성(8.5)
analysis — 복합체(4.5) · TIM(10.1) / test — 판정 도구(5.4) / human — 승인: `requirement`·`decision`의 `stable` 전이, 온톨로지 확장, 학습 판정자 결과

**shape와 analysis는 편집 즉시, verify와 test는 재검증 시점에서, human은 큐로.** 게이트에 걸린 청크는 `draft`에 머문다. `draft`는 링크의 끝이 될 수 없으므로(4.11절) 실패는 하류로 전파되지 않고 그 자리에서 멈춘다. 이 저장소의 실측(2026-09-10): 기계화 — 청크 형식·통제 어휘·ODD 참조·출처·기준 바인딩·대안 기록·증거 기록 규칙; 미구현 — 수준 허용표 일부·복합체·TIM·ODD 경계·기여·검증 대응물·할당 근거·계약 선행·독립성.

게이트 id(도구의 `FAIL [<id>]` 태그, `tools.md` 총람 `id` 열과 같다 — 2026-09-12): 청크 형식 `chunk`·`chunk2kg` · 수준 허용표·복합체·신뢰 등급 `shacl` · 통제 어휘 `vocab` · 출처·할당 근거·기준 바인딩 `verify` · TIM `tim` · ODD 참조 `odd-ref` · 대안 기록 `gen-build` · 독립성 `visibility` · 승인 `writer` · 참조 무결성 `dangling`·`extract-refs`. 실패 종류는 종료 코드로 가른다 — 판정 실패 1 · 설정·입력 2 · 미실행 3.
