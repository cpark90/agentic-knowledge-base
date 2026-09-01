---
iri: https://agentic-knowledge-base.dev/id/chunk-d0075
plane: decision
level: concrete
label_ko: 뷰는 저장하지 않고 질의로 조립한다
label_en: Views are assembled by query, never stored
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 이 체계의 모든 투영은 **그래프 질의의 결과**이며 저장하지
않는다. 문학적 프로그래밍의 두 연산(tangle, weave)도 별도 도구가 아니라
질의다.

**근거** (노트 4.6절)
- **저장된 뷰는 원본과 어긋나는 순간부터 거짓이 된다.** 질의로 조립하면
  어긋날 여지 자체가 없다.
- 네 가지 투영이 같은 방식으로 나온다: **tangle**은 구성체의
  `agt:ArtifactChunk` 부분을 `co:index` 순으로 뽑아 본문을 이어 붙여 코드
  파일을, **weave**는 산출물 청크와 그것을 `targets`하는 논평 청크를 함께
  뽑아 문서를, **라벨 목록**은 스코프 안 청크의 `rdfs:label`만, **situation**은
  스코프의 plane 클래스와 ODD 조건으로 거른 청크를 낸다.
- **논평과 산출물의 분리(5.1절 요구)가 여기서 구현된다.** 두 plane의 청크는
  다른 클래스의 개체로 애초에 따로 존재하고, 산출물 파일과 설명 문서는 각각
  다른 질의의 결과다. 분리를 위한 도구가 필요한 것이 아니라, 분리된 상태를
  기본으로 두고 합치는 질의만 두면 된다.
