---
id: https://agentic-knowledge-base.dev/id/chunk-d0001
type: decision
level: concrete
title_ko: Bazel 하네스 채택
title: Adopt Bazel harness
status: stable
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain]
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T17:34:48+09:00}
---
**결론** — 지식 베이스의 하네스를 Bazel(bzlmod) 위에 세운다.

**근거**
- 검사 게이트(6.7절)를 테스트 타깃으로 두면 `bazel test //...` 한 번이
  게이트 전체 실행이 되고, 입력 해시 기반 캐시가 "바뀐 지식만 재검사"를
  공짜로 준다 — 8.6절 재판정 경계의 기계적 근사.
- 지식 산출물(온톨로지·ODD·kg·청크)이 데이터 타깃이 되므로 산출물 간
  의존이 BUILD 그래프에 명시된다 — 링크 구축(Part VIII) 전 단계의 골격.
- hermetic 파이썬 툴체인 + 해시 고정 lock으로 판정 도구 자체가 재현 가능
  하다 — 10.1절 재현성 요구를 도구 층에서 충족.

**대안**
- Makefile(참조 저장소 방식): 단순하나 캐시·의존 그래프가 없어 전수
  재검사가 기본이 된다. 기각.
- 스크립트 직접 실행: 게이트 우회가 쉬워 6.7절의 강제력이 사라진다. 기각.
