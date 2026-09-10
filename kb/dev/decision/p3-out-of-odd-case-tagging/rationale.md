---
id: https://agentic-knowledge-base.dev/id/chunk/62757841-88ad-4f01-9bdf-0e1a2c4ac9b7
type: decision
level: logical
title_ko: 버리는 것과 섞는 것 둘 다 손해다
title: Both discarding and mixing lose information
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/334ec611-70bf-40cd-85df-7ed0431ac556
---
**근거** (노트 3.3절) — ODD 밖 케이스를 버리면 이탈 반복의 증거가 사라져 3.6절 ODD 확장 판단의 근거가 없어진다. 그렇다고 안 케이스와 섞으면 커버리지 분모가 흐려져 "설계 범위를 얼마나 덮었는가"라는 질문이 답을 잃는다.

태그로 분리하면 둘 다 피한다 — 보관은 하되 집계에서 빠진다. 태그는 질의로 걸러지므로 별도 저장소가 필요 없다.
