---
id: https://agentic-knowledge-base.dev/id/chunk/1c529a5e-a476-47d1-8551-78d829948e2e
type: annotation
level: executable
title_ko: 추적 매트릭스의 빈 칸 constrains schema→contract 는 개발 KB 에 schema·contract 청크가 없어 이 저장소에서 해당 없음이다
title: The empty TIM cell constrains schema to contract does not apply in this repository because the development KB holds no schema or contract chunks
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/1a5c517a-088b-47c7-b29a-b4a044c84946]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T13:21:50+09:00}
---
thought (non-blocking): 빈 칸 `constrains`:schema→contract 는 누락이 아니라 이 저장소의 개발 KB 가 그 칸의 양 끝을 갖지 않아 생기는 해당 없음이다

대상: https://agentic-knowledge-base.dev/id/chunk/1a5c517a-088b-47c7-b29a-b4a044c84946

본문: `p10-link-types` 는 `constrains` 를 개발 KB 안의 수평 링크(메시지 정의 → 인터페이스 시그니처, `p7-dev-plane-substance`)로 둔다. 2026-10-04 실측에서 `schema` 청크 38 은 전부 `kb/vv/case/` 이고 `contract` 청크 41 은 전부 `kb/vv/criteria/` 라 개발 KB 의 두 plane 은 0 이며 `constrains:` 키를 쓴 청크도 0 이다. V&V 의 케이스 → 기준은 `refines`:schema→contract 칸이 이미 채우므로 `constrains` 로 다시 잇는 것은 같은 쌍의 중복이다. 이 칸은 개발 산출물이 메시지·시그니처를 청크로 두는 프로젝트에서만 찰 수 있다.

제안: 해당 없음을 표시할 어휘가 온톨로지에 없어 이 주석으로만 남긴다. 감사 보고서의 빈 칸 수에서 이 칸을 빼려면 TIM 표가 칸의 적용 조건(양 끝 plane 의 개발 KB 거주 수)을 함께 가져야 하고 그 결정은 orchestrator 몫이다.

해소: 열림 — 판정은 해당 없음이고 표의 적용 조건이 정해지면 닫힌다.
