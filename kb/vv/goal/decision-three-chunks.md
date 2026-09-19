---
id: https://agentic-knowledge-base.dev/id/chunk/863a8842-3d1c-4406-99a9-f8d3d755e17a
type: requirement
level: functional
pattern: ubiquitous
title_ko: 대안 없는 결정은 타깃이 될 수 없어야 한다
title: A decision without an alternatives chunk must not become a target
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:40:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
---
**검증 목표** — 결정이 결론·근거·대안 세 청크의 복합체이고 대안 없는 결정이 위반이라는 결정이 로드·분석·검사 세 시점에서 강제된다는 것이 보여져야 한다. 대안이 없었다는 사실도 대안 청크에 적어야 한다.

- **이해관계자**: 개발 역할 · 감사 역할 · **관심사**: 근거 없는 할당이 불가능한 것

**무엇을 관측하면 성립하는가**

- `kb/dev/decision/<슬러그>/`에 `alternatives.md`가 없으면 BUILD 생성기가 실패하고 타깃이 만들어지지 않는다.
- `kb_decision` 규칙의 `alternatives` 속성은 필수이고 비우면 로드 시점에 실패한다.
- 세 부분의 수준이 `decision`의 허용 구간 밖이면 분석 시점에 실패한다.
- `alternatives.md`의 첫 산문 줄이 `**대안**` 표지로 시작하지 않으면 청크 검사가 거부한다.
- 커밋된 결정 전부가 세 청크를 갖고 `bazel test //...`가 PASS다.
