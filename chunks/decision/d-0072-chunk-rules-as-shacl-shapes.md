---
iri: https://agentic-knowledge-base.dev/id/chunk-d0072
plane: decision
level: concrete
label_ko: 청크의 규칙은 SHACL shape으로 쓴다
label_en: Chunk rules are written as SHACL shapes
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 구조적 글쓰기의 원칙을 산문 지침이 아니라 **SHACL shape**으로
쓴다. 원칙이 검사 가능한 제약이 되고, 검사 게이트(6.7절)가 이 shape으로
청크를 검사한다.

**근거** (노트 4.4절) — 원칙별 대응이 일대일로 떨어진다.

| 원칙 | shape |
|---|---|
| 청킹 (작은 단위) | `agt:lineCount` ≤ 42 |
| 관련성 (한 주제) | plane 클래스 정확히 1, `agt:hasLevel` 정확히 1 |
| 라벨링 (이름 필수) | `rdfs:label` 최소 2 — 한/영 각 1 |
| 일관성 (어휘 통일) | assertion 그래프의 모든 술어가 온톨로지에 존재 |

- **"접근 가능한 상세"만 shape으로 쓸 수 없다.** 라벨이 본문을 대표하는지는
  기계가 판정하지 못하므로, 읽기 응답이 라벨을 쓰는 운용으로 강제한다.
- 산문 지침은 지켜졌는지 알 수 없지만 shape은 통과/불통과가 나온다 —
  원칙을 게이트로 옮기는 것이 이 결정의 요점이다.

**plane별 shape은 `agt:ChunkShape`를 상속하고 제약을 더한다.**
`agt:ArtifactChunk`는 심볼 ID 필수, `agt:DecisionChunk`는 결론·근거·대안
중 하나의 역할 태그 필수.
