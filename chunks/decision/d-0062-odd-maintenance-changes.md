---
id: https://agentic-knowledge-base.dev/id/chunk-d0062
type: decision
level: concrete
title_ko: ODD 변경은 확장·축소·정밀화 셋이고 온톨로지가 선행한다
title: ODD changes are expand, narrow, refine - and the ontology comes first
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — ODD는 버전 관리되는 살아 있는 문서다. 변경은 확장·축소·정밀화
셋이며, **확장은 온톨로지 어휘 안에서만** 가능하다. 순서는 언제나
온톨로지 → ODD → 파생물이다.

**근거** (노트 3.6절)
- **확장**(속성이나 값 범위 추가)은 이탈 반복(3.5절)·상승(6.3절)·유저
  요구에서 오며, 새 속성에 대한 시나리오 도메인 확장을 부른다.
  **축소**(명시 제외 추가 또는 범위 축소)는 축소된 범위에 의존하던 항목을
  무효화한다. **정밀화**(판정 방법 개선)는 `unverified`를 줄이고 대조
  정확도를 높이며 파급이 없다.
- ODD에 새 속성을 쓰려면 그 속성이 온톨로지 `related/condition`에 먼저
  있어야 한다. 없으면 온톨로지 확장(2.3절)이 선행한다.
- ODD 변경은 8.6절 전파의 트리거다. 변경된 속성을 참조하는 스코프·가정·
  시나리오 전부가 재검토 목록에 오른다.

**권한** — 편집은 설계 에이전트에게만, 승인은 유저에게. T-Box 편집과 같은
통제 수준이다(2.4절). ODD가 잘못되면 그 위의 모든 것이 잘못되기 때문이다.
