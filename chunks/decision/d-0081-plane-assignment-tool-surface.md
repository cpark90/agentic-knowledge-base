---
iri: https://agentic-knowledge-base.dev/id/chunk-d0081
plane: decision
level: concrete
label_ko: plane 배정은 툴 표면을 바꿔야 효과가 난다
label_en: Plane assignment must change the tool surface
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 에이전트는 자신의 read scope와 write scope에 해당하는 plane만
배정받는다. 그리고 **툴 표면이 배정에 따라 실제로 달라져야 한다** — 배정된
plane 밖은 읽기 툴이 반환하지 않는다.

**근거** (노트 5.3절)
- **저장소만 나누고 읽기 툴이 전체를 반환하면 컨텍스트 분리는 달성되지
  않는다.** plane 분리의 목적은 종류가 다른 지식을 한 컨텍스트에 섞지 않는
  것인데, 툴이 전부 반환하면 분리는 이름뿐이고 컨텍스트는 그대로 부푼다.
- 배정이 read와 write로 나뉘는 것도 요점이다. 어떤 plane은 읽되 쓰지 못하게
  해야 단방향 영향 규칙(5.2절)이 실제로 지켜진다.

**대안 (미확정)** — plane 수의 상한이 노트에 미해결로 남아 있다. 현재 6개.
