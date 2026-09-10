---
id: https://agentic-knowledge-base.dev/id/chunk/4a44f2a8-99c8-47d5-9ff8-e396a8d87e43
type: decision
level: logical
title_ko: 저장된 뷰는 어긋나는 순간 거짓이고 분리된 것을 합치는 것이 질의다
title: A stored view is false the moment it diverges; queries join what is stored apart
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/5d561aaa-6fc8-4102-91b9-96db89f984e8
---
**근거** (노트 4.6절)

- **저장된 뷰는 원본과 어긋나는 순간부터 거짓이 된다.** 이 체계의 모든 뷰는
  질의 결과이므로 어긋날 자리가 없다.
- **주석과 산출물의 분리**(5.1절 요구)가 여기서 구현된다. 두 plane의 청크는
  다른 클래스의 개체로 따로 존재하고, 산출물 파일과 설명 문서는 각각 다른
  질의의 결과다. 개발 프로파일에서는 코드 파일과 문서다. **분리를 위한 도구가
  아니라 분리된 상태에서 합치는 질의가 있을 뿐이다.**
- 읽기 응답(5.3절)과 작업 집합(0.5절)도 같은 장치의 다른 질의다 — 에이전트가
  보는 것과 빌드가 내는 것이 하나의 메커니즘에서 나온다.
