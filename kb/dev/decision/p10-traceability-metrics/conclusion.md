---
id: https://agentic-knowledge-base.dev/id/chunk/b1335ecb-5ef9-45bf-a8aa-db8f44e86b5f
type: decision
level: concrete
title_ko: 추적성 지표 다섯과 그 경고 신호
title: Five traceability metrics and what they warn about
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0112]
part_of: https://agentic-knowledge-base.dev/id/composite/759aa68a-d77b-425c-b819-42ead2a9b0e9
composite: {id: https://agentic-knowledge-base.dev/id/composite/759aa68a-d77b-425c-b819-42ead2a9b0e9, title_ko: 추적성 지표 다섯과 그 경고 신호, title: Five traceability metrics and what they warn about}
---
**결론** — 추적성은 다섯 지표로 관측하고, 각 지표에는 무엇을 경고하는지가 함께 정의된다.

| 지표 | 계산 | 경고 |
|---|---|---|
| 링크 밀도 | 링크 수 / 청크 수 | 급락 시 구축 누락 |
| `suspect` 비율 | suspect / 전체 | 상승 시 재판정 지연 |
| 평균 재판정 지연 | suspect 진입 → 해소 시간 | 재판정 경계 조정 |
| 복원 비율 | 복원 링크 / 전체 | 상승 시 구축이 안 되고 있음 |
| 확정 정밀도 | 확정 후 `invalid`가 된 비율 | 판정 근거 재검토 |
