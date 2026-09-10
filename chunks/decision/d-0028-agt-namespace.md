---
id: https://agentic-knowledge-base.dev/id/chunk-d0028
type: decision
level: concrete
title_ko: agt 접두어와 외부 어휘 불변 원칙
title: The agt prefix and unchanged external vocabularies
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 이 체계 고유의 개념은 `agt:` 접두어를 쓴다. **외부 어휘는 그
접두어를 유지하고 정의를 변경하지 않는다.**

| 접두어 | 어휘 | 용도 |
|---|---|---|
| `bfo:`, `iao:` | 상위 온톨로지, 정보 인공물 | 최상위 분류, `part-of` |
| `prov:` | W3C PROV-O | 출처·귀속·버전 |
| `co:` | Collections Ontology | 순서 있는 부분 |
| `sh:` | W3C SHACL | 제약 |
| `skos:` | W3C SKOS | 라벨·동의어 |
| `ro:` | Relations Ontology | 표준 관계 |

**근거** (노트 0.3절)
- 접두어가 이름에 붙어 있으면 그 개념이 어느 어휘에서 왔는지가 드러나,
  낯선 이름을 아는 이름으로 오인하는 학습자료 종속(1.2절)이 차단된다.
  1.5절의 편향 완화 표에서 이 접두어가 학습자료 종속의 대응 장치다.
- 외부 어휘의 정의를 이 체계에 맞춰 바꾸면, 같은 IRI를 읽는 외부 도구와
  추론기가 다른 뜻으로 동작한다. 가져오되 고치지 않는다.
- 고유 개념에만 `agt:`가 붙으므로, 접두어 없는 이름이 나오면 그것이 아직
  어휘에 등록되지 않은 용어라는 것이 즉시 드러난다.
