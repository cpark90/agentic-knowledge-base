---
id: https://agentic-knowledge-base.dev/id/chunk/42605476-22c6-483d-9dc9-c386ac797f3e
type: decision
level: concrete
title_ko: 청크 품질은 라벨 대표성·고아율·크기 분포·draft 체류 시간 넷으로 잰다
title: Chunk quality is measured by label representativeness, orphan rate, size distribution and draft dwell time
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-12T00:50:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8, https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0080]
part_of: https://agentic-knowledge-base.dev/id/composite/997c76c5-45f5-496d-84cc-49c5e0907761
composite: {id: https://agentic-knowledge-base.dev/id/composite/997c76c5-45f5-496d-84cc-49c5e0907761, title_ko: 청크 품질 지표, title: Chunk quality metrics}
---
**결론** — 11.3절 평가에 청크 수준 지표 넷을 더한다.

| 지표 | 계산 | 의미 |
|---|---|---|
| **라벨 대표성** | 라벨만 보고 본문을 예측한 정확도 (에이전트 실험) | 라벨링 원칙 준수 |
| **고아율** | 어떤 복합체의 부분도 아니고 링크도 없는 청크 비율 | 4.5절 참조 원칙 위반 |
| **크기 분포** | 줄 수 히스토그램 | 42줄 근처에 몰리면 억지 분할 의심 |
| **`draft` 체류 시간** | 생성 → `stable` 소요 | 게이트 병목 |
