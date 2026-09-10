---
id: https://agentic-knowledge-base.dev/id/chunk/ceee3bb0-7ada-4f07-ad8a-4261358a5099
type: decision
level: concrete
title_ko: 기본 시각화는 추적 매트릭스다
title: The traceability matrix is the default visualization
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0109]
part_of: https://agentic-knowledge-base.dev/id/composite/2e051e5d-6083-4a41-91e0-ade82422c705
composite: {id: https://agentic-knowledge-base.dev/id/composite/2e051e5d-6083-4a41-91e0-ade82422c705, title_ko: 기본 시각화는 추적 매트릭스다, title: The traceability matrix is the default visualization}
---
**결론** — 기본 시각화는 **추적 매트릭스**다. plane × plane 격자에 링크 수와 상태(`valid`/`suspect`)를 표시한다. 그래프 시각화는 국소 탐색용이다.

```
plane × plane
              requirement  decision  contract  schema  artifact
decision          14/0       3/1        —        —        —
contract           —        12/0        —       4/1       —
schema             —         5/0        —        —        —
artifact           —        18/2       9/0       —        —

빈 칸 중 TIM이 허용하는 것: artifact→contract (satisfies) : 0  ← 누락 의심

level × level  (refines만)
              functional  abstract  logical  concrete
abstract          14/0       —         —        —
logical            —       11/1        —        —
concrete           —         —        9/0       —
executable         —         —         —       9/0     ← 하강 완주 9/14
```

**plane × plane은 "TIM이 허용하는데 0"인 칸을 우선 검토한다. level × level 매트릭스는 하강 완주를 보여준다** — 한 칸씩 내려가며 수가 줄어드는 지점이 사슬이 끊긴 곳이다.
