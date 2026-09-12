---
id: https://agentic-knowledge-base.dev/id/chunk/c87af959-a788-459b-8c49-b43202d41686
type: decision
level: concrete
title_ko: 입력 사이에는 순서가 있고 앞이 바뀌면 뒤가 재검토된다
title: Inputs are ordered; a change upstream forces review downstream
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0129]
refines: [https://agentic-knowledge-base.dev/id/chunk/d48f87c5-7224-4e99-b3e1-efa4f8f114ef]
part_of: https://agentic-knowledge-base.dev/id/composite/1b1b47e5-a634-4953-bfd9-7b77bf651857
composite: {id: https://agentic-knowledge-base.dev/id/composite/1b1b47e5-a634-4953-bfd9-7b77bf651857, title_ko: 입력 간 의존 순서, title: Dependency order among inputs}
---
**결론** — 입력끼리 순서가 있다. 앞의 것이 바뀌면 뒤가 재검토된다. 세 사슬로
정리한다.

```
상위 온톨로지 선택 → (온톨로지) → ODD → 에이전트 카탈로그 → 스코프
                                  ↘ 태그 어휘
언어 정책 → 표기 형식 (독립)
실행 모드 → 메모리 승격 규칙 → 재검증 시점
```
