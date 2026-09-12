---
id: https://agentic-knowledge-base.dev/id/chunk-d0161
type: decision
level: concrete
title_ko: 서술은 그래프가 못 보여주는 것만 적는다
title: Write only what the graph cannot show
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
generated: {by: claude/fable-5, at: 2026-09-12T00:50:00+09:00}
---
**결론** — 노드의 정의·주석에는 그래프 구조가 이미 말하는 것을 반복하지 않고,
구조가 보여주지 못하는 것만 적는다: **왜 존재하고 언제 이것을 고르는가**,
기각한 대안, 제약(지연·비용·프라이버시), 불변식.

**근거** (harness-functional ONTOLOGYSTYLE §1·§1d)
- 검색으로 노드를 만난 사람과 에이전트의 질문은 "이게 무엇인가"가 아니라
  **"이걸 써야 하나"**다. 선택 근거가 서술에 없으면 그 판단을 위해 다시
  그래프를 헤매야 하고, 결국 못 고르고 새로 만든다(d-0160의 실패 경로).
- 쓰지 않을 것을 명시한다: 라벨 재진술("코딩 하네스는 코딩 하네스다"), 수정
  이력과 리뷰 대화, 주석 처리된 죽은 선언. 발견 시 삭제 대상이다 — 남겨두면
  서술 예산만 먹고 검색 정밀도를 떨어뜨린다. 이력은 버전 관리가 갖는다.
- 서술 텍스트가 검색과 뷰의 실제 재료이므로, 이 내용 규칙이 곧 검색 품질
  규칙이다. 좋은 라벨과 좋은 정의가 주석보다 낫다.

**이 저장소와의 관계** — 세 축이 나뉜다: 개념 정의의 **형식**은 속+종차
(d-0034), 개체 서술의 **내용**은 이 규칙, 서술의 **크기**는 토큰 대역(d-0016).
