---
id: https://agentic-knowledge-base.dev/id/chunk/bb6e6a51-c243-4437-a3a7-d458dc547112
type: decision
level: logical
title_ko: 게이트 안의 판정자·붙이지 않기·판정자가 본문을 쓰는 안은 기각된다
title: A judge inside the gates, no binding at all, and a judge that writes the body are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-jev-system-one}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-29T01:20:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/0524cc2d-1d9f-4d40-8a7a-502e6af0e4c5
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 판정자를 게이트 안에 넣는다 | 외부 서비스가 `bazel test`의 입력이 되어 밀폐성이 깨진다. 같은 리비전이 네트워크 상태에 따라 다른 판정을 낸다 |
| 붙이지 않고 에이전트 세션이 판정한다 | 확신도가 자기 보고라 캘리브레이션을 잴 수 없다. 2026-09-11 실험이 "판정 불가"로 끝난 것이 그 실측이다 |
| 판정자가 주석 `본문:`을 쓴다 | 모델이 텍스트를 만들지 못한다는 명시된 한계와 어긋난다. 근거 문장이 없는 슬롯이 남는다 |
| 전체 20건으로 임계를 켠다 | 구간당 표본이 7건 안팎이라 임계별 정확도가 재지지 않는다. 임계의 뜻(①)이 서지 않은 채 자동 적용이 열린다 |

옛 결정의 대안 넷(자유 서술 리뷰·단일 임계·즉시 게이트 차단·계산을 판정자에게)은 그대로 기각된 채 남는다.
