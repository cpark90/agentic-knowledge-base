---
iri: https://agentic-knowledge-base.dev/id/chunk-d0109
plane: decision
level: concrete
label_ko: 기본 시각화는 추적 매트릭스 — 빈 칸이 곧 누락
label_en: Traceability matrix as default visualization; empty cells are gaps
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 기본 시각화는 **추적 매트릭스**다. plane × plane 격자의 각
셀에 링크 수와 상태(`valid` / `suspect`)를 표시한다. 그래프 시각화는
국소 탐색용이다. **TIM이 허용하는데 셀이 0인 칸을 우선 검토한다.**

**근거** (노트 8.7·8.12절)
- 매트릭스가 기본인 이유는 **빈 칸이 곧 누락**이기 때문이다. 그래프는
  없는 것을 보여 주지 못한다.
- 커버리지 질의(8.7절 고아 탐지)가 매트릭스의 빈 칸으로 한눈에 드러난다.

```
              design   interface   protocol   source   scenario
design           3/1        —          —         —         —   ← supersedes
interface       12/0        —         4/1        —         —   ← satisfies, constrains
protocol         5/0        —          —         —         —   ← derives-from
source          18/2        —          —         —         —   ← satisfies
scenario         9/0       6/0         —         —         —   ← verifies
annotation      (targets: 임의 → 별도 집계)

빈 칸 중 TIM이 허용하는 것:  source→interface (satisfies) : 0  ← 누락 의심
```
