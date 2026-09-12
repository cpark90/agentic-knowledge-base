---
id: https://agentic-knowledge-base.dev/id/chunk/96966fae-587c-426f-9da7-5233844aa016
type: decision
level: concrete
title_ko: 합격 기준은 검증기와 별도 청크로 존재하고 링크 속성으로 바인딩된다
title: Pass criteria are chunks apart from the verifier, bound as link attributes
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-12T11:50:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/63f17c2d-3fdf-4fd0-b05a-ca7b6b89ce46]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0136]
part_of: https://agentic-knowledge-base.dev/id/composite/14433614-5dd7-4df3-b32c-2422a25daef3
composite: {id: https://agentic-knowledge-base.dev/id/composite/14433614-5dd7-4df3-b32c-2422a25daef3, title_ko: 합격 기준, title: Pass criteria}
---
**결론** — 합격 기준은 **V&V KB의 `contract` plane, logical 수준**에서 판정식으로 태어난다 (7.2절). 개발 KB의 abstract → logical 게이트가 이 기준의 존재를 요구한다 (7.3절). **기준은 검증기와 별도 청크로 존재하고 `verifies` 링크의 속성으로 바인딩된다.** 기준 유형은 일곱이다.

- **명세 대조** — 출력이 `contract`·`schema` 청크와 일치 (응답 스키마 정합)
- **불변식** — 실행 전후로 유지되는 조건 (총량 보존, 참조 무결성)
- **임계** — 측정값이 범위 안 (응답 시간 < 200ms)
- **시간 제약** — 선행·배타·시한 (0.5절 시간 제약 어휘)
- **가정 유지** — 실행 중 `agt:Assumption`이 깨지지 않음 (ODD 이탈 0회)
- **산출물 품질**(에이전트) — 산출 청크가 shape 통과, `refines` 연쇄 완결 (고아율 0)
- **인지**(에이전트) — 작업 집합 대비 누락률 (11.3절)

**기준 없는 `verifies` 링크는 검사 게이트가 거부한다.** 판정식 없는 기준은 logical이 아니라 abstract다.
