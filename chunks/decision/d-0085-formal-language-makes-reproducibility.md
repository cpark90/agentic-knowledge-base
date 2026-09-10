---
id: https://agentic-knowledge-base.dev/id/chunk-d0085
type: decision
level: concrete
title_ko: 재현성은 인터프리터가 아니라 형식 언어가 만든다
title: Reproducibility comes from a formal language, not an interpreter
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 온톨로지에 대응하는 **형식 언어를 정의하고 그 파일 자체를
산출물로 삼는다.** 온톨로지를 읽어 자유형 문서를 생성하는 방식은 쓰지
않는다.

**근거** (노트 6.6절)
- 온톨로지를 읽고 에이전트가 산출물을 "해석해서" 만드는 방식으로는
  **공백 세션에서 같은 산출물이 나오지 않는다.** 재현성을 인터프리터(모델)의
  일관성에 맡기는 것이기 때문이다. 형식 언어로 쓴 파일은 그 자체가
  산출물이므로 해석 단계가 없고, 따라서 재현성 문제도 없다.
- **형식 언어를 따로 설계하지 않는다.** 온톨로지가 기반이므로 어휘는
  온톨로지에서 오고, 결과적으로 온톨로지 개념을 그대로 키워드로 쓰는
  표기가 된다.
- **형식 언어는 사다리의 abstract 단계를 표현하는 언어다.** functional →
  abstract 전이가 곧 "이 언어로 옮기기"이며, 그 이후 단계는 이 언어 위에
  도메인과 값을 채우는 것이다. abstract가 기계가독의 경계인 것과 같은
  이야기다.
