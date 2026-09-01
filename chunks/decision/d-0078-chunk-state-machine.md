---
iri: https://agentic-knowledge-base.dev/id/chunk-d0078
plane: decision
level: concrete
label_ko: 청크의 다섯 상태와 전이
label_en: Five chunk states and their transitions
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 청크도 가정·링크와 **같은 상태 기계**를 갖는다.

| 상태 | 의미 | 전이 |
|---|---|---|
| `draft` | shape 미통과 또는 라벨 미확정 | → `valid` (게이트 통과) |
| `valid` | shape 통과, 가정 전부 참 | → `suspect` |
| `suspect` | 재검토 필요 | → `valid` 또는 `invalidated` |
| `invalidated` | 가정 거짓 | → `valid`(수정) 또는 `deprecated` |
| `deprecated` | 폐기. 참조는 남되 신규 참조 금지 | 종료 |

**근거** (노트 4.11절)
- `valid` → `suspect`의 트리거는 둘이다: **가정 변경**과 **참조 청크 변경**.
  둘 다 청크 밖에서 오는 사건이므로 청크 스스로 상태를 지킬 수 없다 —
  상태를 명시적으로 들고 있어야 하는 이유다.
- `deprecated`가 삭제와 구분되는 이유는 기존 참조를 깨뜨리지 않기 위해서다.
  신규 참조만 막는다.

**`draft` 청크는 링크의 끝이 될 수 없다.** 확정되지 않은 것에 의존하는
링크는 만들 수 없다 — 만들면 그 링크가 언제 참이 되는지 아무도 모른다.
