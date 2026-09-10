---
id: https://agentic-knowledge-base.dev/id/chunk/4962e5fe-9d28-4f18-b054-95670b51808e
type: decision
level: concrete
title_ko: 대안 청크 없는 결정은 shape 위반이고 대안이 없었다는 것도 기록한다
title: A decision without an alternatives chunk violates the shape; "no alternative" is itself recorded
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
composite: {id: https://agentic-knowledge-base.dev/id/composite/07096f39-a6f4-4727-a653-b8eafc5eff92, title_ko: 대안 청크 필수, title: Alternatives chunk is mandatory}
part_of: https://agentic-knowledge-base.dev/id/composite/07096f39-a6f4-4727-a653-b8eafc5eff92
---
**결론** — 개발 KB의 중심 개체는 결정이고, 결정은 항상 세 청크(결론·근거·대안)의 복합체다. **대안 청크가 없는 결정은 shape 위반이다.** "대안이 없었다"도 대안 청크에 적는다 — 후보가 하나뿐이었다는 것 자체가 기록할 사실이다 (노트 7.4절).

| 청크 | 내용 | 42줄에 들어가는 것 |
|---|---|---|
| 결론 | 무엇으로 정했는가 | 값 + 한 문단 |
| 근거 | 왜 — 어느 요구의 어느 관심사에 기여하는가, 어느 제약이 대안을 배제했는가 | `serves` + 제약 ID + 설명 |
| 대안 | 배제된 후보와 배제 근거. `-space`의 eliminated 항목이 여기로 승격 | 후보당 한 줄 |
