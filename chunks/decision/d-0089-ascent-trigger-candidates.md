---
id: https://agentic-knowledge-base.dev/id/chunk-d0089
type: decision
level: concrete
title_ko: 상승 트리거 후보 넷 — 초기에는 유저 지정만 쓴다
title: Four ascent trigger candidates - start with user tagging only
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 상승(6.3절)을 무엇이 촉발하는가에 대한 후보 넷을 둔다. 셋은
반복 횟수 임계값이 필요하고, 하나는 즉시 쓸 수 있다.

| 트리거 | 조건 | 산출 |
|---|---|---|
| 반복 | 같은 결함 요인이 N회 이상 관측 | 요인 청크 → `defect` 어휘 후보 |
| 무효화 빈도 | 같은 가정이 M회 이상 깨짐 | 가정 → ODD 속성 후보 |
| 배제 반복 | 같은 후보가 같은 제약으로 K회 이상 기각 | 제약 → 온톨로지 공리 후보 |
| 유저 지정 | 유저가 관측 청크에 "일반화" 태그 | 즉시 후보 |

**근거** (노트 6.11절)
- 상승이 가치 있는 것은 어휘가 자라기 때문이지만, 아무 관측이나 올리면
  어휘가 오염된다. **반복이 일반화의 신호**라는 것이 세 자동 트리거의 공통
  전제다.
- 무효화 이력이 상승의 입력이라는 6.5절 결정이 두 번째 트리거로 구체화된다.
- **실행 기록이 쌓이기 전에는 유저 지정만 쓴다.** 임계값 트리거는 관측
  모수가 있어야 의미가 있다.

**대안 (미확정)** — 노트가 이 절을 `[안]`으로 둔다. N·M·K의 초기값이
정해지지 않았다.
