---
iri: https://agentic-knowledge-base.dev/id/chunk-d0004
plane: decision
level: concrete
label_ko: plane 간 단방향 영향 규칙
label_en: One-way influence rule between planes
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 상위 plane만 하위 plane에 영향을 줄 수 있다. 순서 기준은
**변화 속도**다 (느린 것이 상위).

```
decision → contract/schema → artifact → annotation → memory
```

**근거** (노트 5.2절) — 빠르게 변하는 지식이 느리게 변하는 지식을 뒤흔들면
갱신 파급이 통제되지 않는다. 무효화(6.5절)도 이 순서를 따라서만 전파되므로
무효 범위 계산이 유계가 된다.

**대안** — annotation을 artifact보다 상위에 두는 안이 미해결로 남아 있다
(노트 5.2절 `[?]`). 논평이 산출물 수정을 유발하는 방향을 중시하면 순서가
바뀐다. 현재는 변화 속도 기준을 유지한다.
