---
id: https://agentic-knowledge-base.dev/id/chunk-d0129
type: decision
level: concrete
title_ko: 입력 간 의존 순서
title: Dependency order among inputs
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 입력끼리 순서가 있다. 앞의 것이 바뀌면 뒤의 것이 재검토된다.
세 사슬로 정리한다.

**근거** (노트 9.7절)

```
상위 온톨로지 선택 → (온톨로지) → ODD → 에이전트 카탈로그 → 스코프
                                  ↘ 태그 어휘
언어 정책 → 표기 형식 (독립)
실행 모드 → 메모리 승격 규칙 → 재판정 경계
```

- **상위 온톨로지 선택이 사실상 불가역인 이유가 이 그림에 있다** — 사슬의
  맨 앞이므로 바뀌면 그 뒤 전부가 재정렬 대상이다.
- 스코프는 사슬의 끝이다. ODD와 카탈로그 둘 다에서 파생되므로(9.2절)
  어느 쪽이 바뀌어도 재파생된다.
- 언어 정책 사슬은 다른 둘과 만나지 않는다 — 표기 형식만 바꾼다.
- 이 순서가 입력 변경의 파급 계산 순서이자 최초 인스턴스화의 진행 순서다.
