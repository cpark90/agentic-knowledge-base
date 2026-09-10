---
id: https://agentic-knowledge-base.dev/id/chunk/8535b744-654f-448a-8268-d4ef94b61f4c
type: decision
level: logical
title_ko: 검사할 수 없는 원칙과 규칙의 부작용은 지표로만 드러난다
title: Uncheckable principles and rule side effects surface only as metrics
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/997c76c5-45f5-496d-84cc-49c5e0907761
---
**근거** (노트 4.13절)

- 네 지표는 각각 shape이 잡지 못하는 것을 관측한다. **라벨 대표성**은 4.4절이
  "검사 불가"로 남긴 유일한 원칙이라 실험으로만 측정된다.
- **고아율**은 구성에도 링크에도 걸리지 않은 청크를 드러낸다 — 그런 청크는
  어떤 질의로도 조립되지 않으므로 있으나 마나다 (4.5절 참조 원칙).
- **크기 분포**와 **`draft` 체류 시간**은 규칙이 실제로 어떻게 작동하는지를
  드러낸다. 42줄 근처에 몰리면 상한을 맞추려는 억지 분할이고, 체류 시간이 길면
  게이트(6.7절)가 병목이다.
