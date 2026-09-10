---
id: https://agentic-knowledge-base.dev/id/chunk/f12c958e-2314-43b9-8f6c-77dc38f87a6b
type: decision
level: concrete
title_ko: 검증은 산출물을 묻고 평가는 요구 자체를 묻는다
title: Verification asks about the artifact, validation about the requirement
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901, https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193]
part_of: https://agentic-knowledge-base.dev/id/composite/f78cc6f9-4200-405e-8a12-7c8eb43f9c24
composite: {id: https://agentic-knowledge-base.dev/id/composite/f78cc6f9-4200-405e-8a12-7c8eb43f9c24, title_ko: 검증과 평가, title: Verification and validation}
---
**결론** — V&V는 둘이다. 질문이 다르고 증거가 다르다.

- **검증(verification)** — 산출물이 요구를 충족하는가. 증거는 verifier 실행 결과(기준 대비 통과/실패). 환경 사다리 1~5단계. 결함은 산출물·결정 수정으로 간다. 시나리오 출처는 `origin:designed`(요구에서 파생)
- **평가(validation)** — **요구 자체가 맞는가.** 증거는 실환경 관측·유저 피드백·ODD 이탈 빈도·사후분석. 환경 사다리 5~6단계. 결함은 **요구·ODD 수정**(상승)으로 간다. 시나리오 출처는 `origin:observed`(관측에서 일반화)

**평가의 결과가 개발 KB의 `requirement` plane으로 돌아가는 것이 요구가 바뀌는 유일한 정규 경로다.**

에이전트 검증(7.8절)은 평가의 특수 형태다 — 만드는 주체가 맞게 만들고 있는가를 묻고, 자극은 작업 집합이며 기준은 산출물 품질과 인지 누락률이다.
