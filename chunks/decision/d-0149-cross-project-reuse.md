---
iri: https://agentic-knowledge-base.dev/id/chunk-d0149
plane: decision
level: concrete
label_ko: 청크는 프로젝트를 넘지 않는다
label_en: Chunks do not cross projects
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 프로젝트를 넘는 것은 **어휘·제약·ODD 골격**이고, **청크는
재사용하지 않는다.**

**근거** (노트 10.7절, 3.7절의 확장)
- **온톨로지** — 공유한다. 프로젝트별 확장 모듈만 추가하고 코어는 수정하지
  않는다.
- **ODD** — 복사 후 축소·확장한다 (3.6절 변경 유형).
- **상승으로 올라간 제약** — 온톨로지 공리가 되었으므로 자동 상속된다.
- **`defect` 어휘** — 공유한다.
- **청크** — 재사용하지 않는다. 청크는 **프로젝트 ODD 안에서만 유효**하며,
  다른 ODD로 옮기면 그 청크가 딛고 선 조건이 사라진다.
- 이것이 상승(6.3절)이 청크에서 멈추지 않고 **온톨로지까지 닿아야 하는
  이유**다 — 어휘와 공리로 올라간 것만 다음 프로젝트에서 쓸 수 있다.
