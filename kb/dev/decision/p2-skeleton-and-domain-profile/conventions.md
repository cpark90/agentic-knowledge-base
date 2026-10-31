---
id: https://agentic-knowledge-base.dev/id/chunk/a5ce0b9e-236b-4b2d-81a9-f0c6226686bb
type: decision
level: concrete
title_ko: 규범 문서 규약 — 프로파일은 코어를 확장만 하는 온톨로지 모듈이다
title: Normative-document conventions — A profile is an ontology module that only extends the skeleton
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:58:36+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/f28573cc-2a81-4db9-9497-160a41fdd56d
---
**규약** — `p2-skeleton-and-domain-profile`의 결론을 규범 문서에 싣는 문장이다.

규약: 1 | **프로파일 구축** | `profile/<분야>` 모듈이다. 각 지식 종류의 실체와 판정 도구, 조건 어휘, 결함 유형을 담는다 | 어휘가 없으면 ODD의 조건을 개념에 대응시킬 수 없다(`p3-odd-first-project-start` 2단계) | [§1](#1-프로파일-구축)
규약: **확장점을 코어에서 열거한다.** 확장점은 지식 종류 일곱의 실체와 판정 도구, 정제 수준별 assertion 형식, 조건 셋째 분류 단계, 결함 하위 유형, 상한 오버라이드, 앵커 해석기다(`p2-skeleton-and-domain-profile` 표). 이 열거가 곧 완료 판정의 분모다.
규약: **모듈 `kb/ontology/profile/<domain>/`에 적는다.** 파일 하나가 확장점 하나이며, 확장점은 실체 하위 클래스, 판정 도구 개체와 그 바인딩, 패턴 어휘다. 모듈은 `project-ontology.ttl`의 `owl:imports`에 넣고 `gen_build`로 모듈 목록을 재생성한다.
규약: **완료를 판정한다.** 완료 조건은 게이트 통과(boundary·shape)와 새 역량 질문의 답 행 1개 이상, 코어 수정 0이다. 채우지 않은 확장점은 아래 표에 "미채움"으로 남긴다.
