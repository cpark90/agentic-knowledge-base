---
id: https://agentic-knowledge-base.dev/id/chunk-d0080
type: decision
level: concrete
title_ko: 청크 품질 지표 넷
title: Four chunk-level quality metrics
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 평가(10.3절)에 청크 수준 지표 넷을 더한다. shape이 통과했다고
청크가 잘 나뉜 것은 아니므로, shape이 잡지 못하는 것을 지표로 관측한다.

| 지표 | 계산 | 무엇을 잡는가 |
|---|---|---|
| 라벨 대표성 | 라벨만 보고 본문을 예측한 정확도 (에이전트 실험) | 라벨링 원칙 준수 |
| 고아율 | 어떤 구성체의 부분도 아니고 링크도 없는 청크 비율 | 참조 원칙 위반 |
| 크기 분포 | 줄 수 히스토그램 | 억지 분할 |
| `draft` 체류 시간 | 생성 → `valid` 소요 | 게이트 병목 |

**근거** (노트 4.13절)
- **라벨 대표성은 shape으로 검사할 수 없다** (4.4절 "접근 가능한 상세").
  기계가 판정하지 못하므로 지표로 관측하는 것 외에 방법이 없다.
- **고아율은 안티-고아 축의 계측기다.** 구성체에도 링크에도 걸리지 않은
  청크는 만들어졌을 뿐 쓰이지 않는 지식이다.
- **크기 분포가 42줄 근처에 몰리면 억지 분할을 의심한다.** 상한에 맞춰
  자르는 것은 분할 신호(4.10절)를 따른 분할이 아니다.
- `draft` 체류 시간이 길면 게이트가 아니라 게이트 운용에 문제가 있다.
