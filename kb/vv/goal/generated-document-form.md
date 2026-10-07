---
id: https://agentic-knowledge-base.dev/id/chunk/37d2df45-7012-498f-9f5f-c3c3ef3e5e51
type: requirement
level: functional
pattern: ubiquitous
title_ko: 생성 문서의 본문 서식은 생성 전에 고정된 규약 하나를 따라야 한다
title: The body form of a generated document must follow one convention fixed before generation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-10-06T11:34:24+09:00}
verified: [{by: vnv/claude-sonnet-5-5, at: 2026-10-06T11:34:24+09:00}]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/9807be26-ff48-4cca-89c1-129f52e69df4]
---
**검증 목표** — 본문 서식이 마크다운 표준 규칙 일곱과 빈 값 한 표기이고 생성 문서가 게이트 `gendoc` 의 입력이라는 결정 둘이 함수 하나로 강제된다는 것이 보여져야 한다. 규약의 단일 정의처는 `tools/kb_lib.py` 이고 생성기와 게이트가 같은 것을 import 한다.

- **이해관계자**: 문서를 읽는 사람과 에이전트 · **관심사**: 한 번 익힌 읽기 방식의 재사용

**무엇을 관측하면 성립하는가**

- 모든 생성 뷰가 제목 계층 한 단계씩(G8)·h1 하나(G9)·표의 헤더와 열 수와 빈 줄(G10)·펜스 언어(G11)·120줄 초과 시 목차(G12)·링크 실재(G13)·빈 값 `없음`(G14)·비율 `n/d = p.p%`(G15)·단정 서술형(G18)을 지킨다.
- 인용 구역(`<!-- 인용 시작 … -->` 부터 `<!-- 인용 끝 -->` 까지) 안에서는 G10·G11·G14·G15·G18 을 판정하지 않고 G8·G9·G12·G13 은 판정한다.
- 빈 셀·대시 셀은 G14, 분모 없는 백분율은 G15 로 거부된다.
- `bazel test //...` 가 뷰를 빌드해 검사하므로 생성 문서는 게이트 밖 산출물이 아니다.

판정의 원본은 `tools/kb_lib.py` 의 `check_gendoc`(G8~G15·G18)과 `BUILD.bazel` 의 `gendoc_test` 다.
