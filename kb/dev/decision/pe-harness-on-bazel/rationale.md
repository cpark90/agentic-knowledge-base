---
id: https://agentic-knowledge-base.dev/id/chunk/26ca7798-4339-4995-83cb-2ec6a1e28aad
type: decision
level: concrete
title_ko: Bazel은 게이트 실행과 증분 재검사와 산출물 의존과 도구 재현성을 함께 준다
title: Bazel gives gate execution, incremental re-checking, artifact dependencies and reproducible tools together
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0001-bazel-harness.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T03:59:32+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/da7b19bc-5643-490f-9a51-3c45c7d06273
---
**근거** — 근거는 셋이다.

- 검사 게이트(노트 6.7절)를 테스트 타깃으로 두면 `bazel test //...` 한 번이 게이트 전체의 실행이 된다. 입력 해시에 기반한 캐시가 바뀐 지식만 다시 검사하게 해 주므로, 8.6절 재검증 시점을 기계적으로 근사한다.
- 온톨로지와 ODD, 지식그래프, 단위 지식 같은 지식 산출물이 데이터 타깃이 되므로 산출물 사이의 의존이 BUILD 그래프에 드러난다. 그래서 이 의존이 링크 구축(Part VIII) 이전 단계의 토대가 된다.
- 밀폐(hermetic) 파이썬 툴체인과 해시를 고정한 lock 덕분에 판정 도구 자체가 재현 가능하다. 따라서 10.1절의 재현성 요구를 도구 층에서 충족한다.
