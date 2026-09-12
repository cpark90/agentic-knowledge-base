---
id: https://agentic-knowledge-base.dev/id/chunk/626aabcf-e088-4776-89d8-262d7a866db8
type: decision
level: logical
title_ko: plane이 늘면 shape과 판정 도구가 함께 늘므로 하위 클래스가 기본이다
title: Each new plane multiplies shapes and tools, so subclassing is the default
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/ab95f777-16da-41c6-8b1d-5f51f1484840
---
**근거** (노트 5.5절)

- plane이 하나 늘면 컨텍스트 분리 단위, plane별 shape(4.4절), 판정 도구(5.4절),
  읽기 응답 형식(5.3절)이 함께 는다. 판정 방식이 같은 것을 새 plane으로 두면
  **같은 도구가 두 곳에 걸린다.** 그래서 하위 클래스가 기본이고 plane 추가가
  예외다.
- 승격의 실제 사례가 `requirement`다 — 이해관계자 합의는 형식 검사·실행·사회적
  해소 어디와도 다르므로 기준을 충족했다(5.1절).
- 기준이 판정 방식 하나이므로 후보 심사가 판단이 아니라 대조가 된다.
