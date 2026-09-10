---
id: https://agentic-knowledge-base.dev/id/chunk-d0086
type: decision
level: concrete
title_ko: 검사 게이트는 A-Box를 SHACL로 검사한다
title: The inspection gate checks the A-Box with SHACL
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 에이전트가 A-Box와 설계 공간을 채우게 하려면 기계적 검사가
필수다. **SHACL 제약**으로 카디널리티, 타입 일관성, 필수 필드를 검사하는
게이트를 둔다.

**근거** (노트 6.7절)
- 에이전트의 무효 출력은 세 유형이다: **중간 산출물 반환**(작업이 끝나지
  않은 것을 결과로 냄), **형식 오류**, **형식 이탈**(구조화 대신 자유형
  텍스트). 셋 다 산문 지침으로는 막히지 않고 구조 검사로만 걸린다.
- **온톨로지 위생 검사와 이 게이트는 대상이 다르다.** 위생은 T-Box(어휘가
  건강한가), 게이트는 A-Box(개체가 어휘에 맞는가). 둘을 하나로 합치면
  어휘 문제와 개체 문제가 구분되지 않는다.

**모델 의존성** — 구조화 출력 강제를 위한 별도 전략이 모델마다 필요하다.
**모델을 교체할 때는 통과율을 먼저 측정한다** — 통과율은 게이트의 성질이
아니라 모델과 게이트의 조합의 성질이다.
